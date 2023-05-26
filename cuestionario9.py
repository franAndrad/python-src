# cp, cl, ct, mc = 0, 0, 0, 0
# texto = input('Ingrese el texto (termine con un punto): ')
# for car in texto:
#     cl += 1
#     if car == ' ' or car == '.':
#         if cl > 1:
#             cp += 1

#         if cp == 1:
#             mc = cl
#         elif cl < mc:
#             mc = cl

#         cl = 0

# print('Longitud de la palabra más corta:', mc)

# cp, cl, ct, mc = 0, 0, 0, 0
# texto = input('Ingrese el texto (termine con un punto): ')
# for car in texto:
#     cl += 1
#     if car == ' ' or car == '.':
#         if cl > 1:
#             cp += 1

#         if cp == 1:
#             mc = cl - 1
#         elif cl < mc:
#             mc = cl - 1

#         cl = 0

# print('Longitud de la palabra más corta:', mc)

cp, cl, ct, mc = 0, 0, 0, 0
texto = input('Ingrese el texto (termine con un punto): ')
for car in texto:
    cl += 1
    if car == ' ' or car == '.':
        if cl > 1:
            cp += 1

        if cp == 1:
            mc = cl - 1
        elif cl < mc:
            mc = cl - 1

print('Longitud de la palabra más corta:', mc)
