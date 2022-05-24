# -*- coding: utf-8 -*-
"""
Created on Tue May 24 07:54:55 2022

@author: mueyyed garzuddin
"""
import numpy as np
import math, matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

first_values = np.array([[0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0], [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1]])

def plott(values):
    
    A = values
    
    figure = plt.figure()
    ax = figure.add_subplot(111, projection='3d')
    ax.scatter3D(A[:, 0], A[:, 1], A[:, 2])

    vertices = [[A[0],A[1],A[2],A[3]], [A[4],A[5],A[6],A[7]], [A[0],A[1],A[5],A[4]], [A[2],A[3],A[7],A[6]], [A[1],A[2],A[6],A[5]],[A[4],A[7],A[3],A[0]]]


    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.add_collection3d(Poly3DCollection(vertices,facecolors='blue', linewidths=2, edgecolors='r', alpha=.50))


    plt.show()
    
    
    
    
def translation(values):
    count = int(values.size/3)
    result = np.zeros((count,3))
    x_val = float( input("X icin oteleme deger: "))
    y_val = float( input("Y icin oteleme deger : "))
    z_val = float( input("Z icin oteleme deger: "))

    for i in range (count):
        result[i][0] = values[i][0] + x_val
        result[i][1] = values[i][1] + y_val
        result[i][2] = values[i][2] + z_val
    return result




def rotation(values):
    count = int(values.size/3)
    result = np.zeros((count,3))
    u = float(input("dondurme deger girin : "))
    which_axis = str(input("Hangi axis ? sadece  x,y,z harfe girilebilir : "))
    if which_axis.lower() == "x":
        for i in range(count):
            result[i][0] = values[i][0]
            result[i][1] = (values[i][1]*math.cos(u)) - (values[i][2]*math.sin(u))
            result[i][2] = (values[i][1]*math.sin(u)) + (values[i][2]*math.cos(u))
        return result

    elif which_axis.lower() == "y":
        for i in range(count):
            result[i][0] = (values[i][2]*math.sin(u)) + (values[i][0]*math.cos(u))
            result[i][1] = values[i][1]
            result[i][2] = (values[i][2]*math.cos(u)) - (values[i][0]*math.sin(u))
        return result

    elif which_axis.lower() == "z":
        for i in range(count):
            result[i][0] = (values[i][0]*math.cos(u)) - (values[i][1]*math.sin(u))
            result[i][1] = (values[i][0]*math.sin(u)) + (values[i][1]*math.cos(u))
            result[i][2] = values[i][2]
        return result

    else:
        print("yalnis axis girdiniz !")

    return values
    

def scaling(values):
    count = int(values.size/3)
    result = np.zeros((count,3))
    x_val = float( input("  x-axis icin olcekleme degeri : "))
    y_val = float( input("y-axis icin olcekleme degeri   : "))
    z_val = float( input("z-axis icin olcekleme degeri   : "))

    for i in range (count):
        result[i][0] = values[i][0] * x_val
        result[i][1] = values[i][1] * y_val
        result[i][2] = values[i][2] * z_val
    return result
    
    
if __name__ == "__main__":
    command_list = []
    
    selection = 1

    while selection == 1:
        print("*********************************************************")
        print("[0]    exit icin basin")
        print("[1]    Ana sekil goruntulemek icin basin ")
        print("[2]    bazi donusumler uygulayabilmek icin basin")
        print("*********************************************************")
        selection = int( input("Selection : "))
        if selection == 1:
            plott(first_values)
        elif selection == 0:
            print("program bitiriyor...")
            exit()

    
    if selection == 2:
        while 1:
            print("*********************************************************")
            print("dikkatine ------------------------->ayni anda birkac donusumlar uygulanabilir ")
            print("[0]  bitirmek icin basin .") 
            print("[1]  otelemek icin basin.")
            print("[2]  dondurmek icin basin .")
            print("[3]  olceklendirmek icn basin .")
            print("[4]  donusumler uygulayabilmek icin basin ")
            print("*********************************************************")
            if len(command_list):
                print("eger sadece bir daha donusum uygulamak istiyorsan 4 basin ")
            selection = int( input("Selection : "))
            if selection == 0:
                print("program bitiriyor...")
                exit()
            elif selection == 4:
                break
            elif (0 < selection < 4) == 0:
                print("yalnis giris ! program bitiriyor...")
                exit()
            command_list.append(selection)
        
        temp_values = first_values
        for i in command_list:
            if i == 1:
                temp_values = translation(temp_values)
            elif i == 2:
                temp_values = rotation(temp_values)
            elif i == 3:
                temp_values = scaling(temp_values)

        plott(temp_values)

