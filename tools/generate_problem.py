#!/usr/bin/env python3
"""Generador reproducible de problemas de práctica de TermoIA-UAMC.

No genera soluciones; produce parámetros distintos a partir de una semilla.
"""
import argparse, random, math


def first_law(rng):
    m = rng.choice([100,150,200,250,300])
    c = 4.184
    dT = rng.choice([8,12,15,20,25])
    return (f"Se calientan {m} g de agua desde una temperatura inicial T hasta T+{dT} °C. "
            f"Usa c={c} J g^-1 K^-1. Delimita el sistema, declara signos y calcula el calor ideal transferido. "
            "Después explica qué parte de la respuesta cambiaría si el recipiente tuviera capacidad calorífica no despreciable.")


def gibbs(rng):
    K = rng.choice([0.1,0.5,2,5,10,50,100])
    Q = rng.choice([0.05,0.2,1,3,20,200])
    T = rng.choice([293.15,298.15,310.15])
    return (f"A T={T:.2f} K una reacción tiene K={K:g} y en el estado actual Q={Q:g}. "
            "Sin usar primero una calculadora, predice la dirección termodinámica. Luego calcula el signo de ΔG y verifica que ambas rutas concuerden.")


def mixing(rng):
    x = rng.choice([0.1,0.2,0.3,0.4,0.5])
    return (f"Una mezcla binaria ideal tiene x1={x:.1f} y x2={1-x:.1f}. "
            "Calcula ΔS_mix por mol total y compara cualitativamente con una mezcla equimolar. Explica el límite x1→0.")


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--seed',type=int,default=4603003)
    ap.add_argument('--type',choices=['first-law','gibbs','mixing','random'],default='random')
    args=ap.parse_args()
    rng=random.Random(args.seed)
    typ=args.type
    if typ=='random': typ=rng.choice(['first-law','gibbs','mixing'])
    print({'first-law':first_law,'gibbs':gibbs,'mixing':mixing}[typ](rng))

if __name__=='__main__': main()
