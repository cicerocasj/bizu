dado = "LEITURA DAS BANDAS LANDSAT 5"

l1 = dado[0] # BANDA 1
l3 = dado[2] # BANDA 3
l4 = dado[3] # BANDA 4
l5 = dado[4] # BANDA 5
l6 = dado[5] # BANDA 6

nuvem_b6 = numpy.where((l6 < 18.0), 1, 0)
l1 = l1 * nuvem_b6
l3 = l3 * nuvem_b6
l4 = l4 * nuvem_b6
l5 = l5 * nuvem_b6

print "Calculando não vegetação."
no_veg = numpy.where(((l1 < l3) & (l3 < l4) & (l4 < (l5 * 1.07)) & (l5 < 0.65) | ((l1 * 0.8) < l3) & (
    (l3 < (l4 * 0.8)) < (l4 < l5)) & (l3 < 0.22)), 1, 0)

if numpy.any(no_veg):
    l1 = l1 * numpy.logical_not(no_veg)
    l3 = l3 * numpy.logical_not(no_veg)
    l4 = l4 * numpy.logical_not(no_veg)
    l5 = l5 * numpy.logical_not(no_veg)

print "Calculando áqua."
aqua = numpy.where((((l3 > l4) & (l3 > (l5 * 0.67)) & (l1 < 0.30) & (l3 < 0.20)) | (
    (l3 > (l4 * 0.08)) & (l3 > (l5 * 0.67)) & (l3 < 0.06))), 1, 0)

if numpy.any(aqua):
    l1 = l1 * numpy.logical_not(aqua)
    l3 = l3 * numpy.logical_not(aqua)
    l4 = l4 * numpy.logical_not(aqua)
    l5 = l5 * numpy.logical_not(aqua)

print "Calculando 'talvez nuvem'."
talvez_nuvem = numpy.where((((l1 > 0.15) | (l3 > 0.18)) & (l5 > 0.12) & (numpy.maximum(l1, l3) > (l5 * 0.67))), 1, 0)

if numpy.any(talvez_nuvem):
    l1 = l1 * numpy.logical_not(talvez_nuvem)
    l3 = l3 * numpy.logical_not(talvez_nuvem)
    l4 = l4 * numpy.logical_not(talvez_nuvem)
    l5 = l5 * numpy.logical_not(talvez_nuvem)

print "Calculando vegetação."
veg = numpy.where((l1 + l3 + l4 + l5), 1, 0)

print "Calculando cirrus."
cirrus = numpy.where((veg + aqua), 1, 0)

print "Calculando nuvem."
nuvem = numpy.where((nuvem_b6 - cirrus), 0, 1)
