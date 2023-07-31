from gildedrose import Normal, BrieAñejado, ConjuredItem, Sulfuras, BackstagePasses

test_item = Normal(50,30)

test_item.update_quality(10)
if test_item.show_quality() != 40:
    raise ValueError ("El valor del item es incorrecto.")
test_item.reset_quality()

test_item.update_quality(32)
if test_item.show_quality() != 16:
    raise ValueError ("El valor del item es incorrecto.")
test_item.reset_quality()

test_item.update_quality(10000)
if test_item.show_quality() <0:
    raise ValueError ("El valor Quality del item no puede ser menor que cero.")
test_item.reset_quality()

if test_item.show_quality() >50:
    raise ValueError ("El valor Quality del item no puede ser mayor de 50.")
test_item.reset_quality()

test_queso = BrieAñejado(10)
test_queso.update_quality(100)

if test_queso.show_quality() > 50:
    raise ValueError ("El valor Quality del queso no puede ser mayor de 50.")
test_queso.reset_quality()

test_sulfuras = Sulfuras(80)

if test_sulfuras.show_quality() != 80:
    raise ValueError ("El valor Quality de Sulfuras no puede ser diferente de 80.")

test_conjured_item = ConjuredItem(50,10)

test_conjured_item.update_quality(10)
if test_conjured_item.show_quality() != 30:
    raise ValueError ("El valor del item conjurado es incorrecto.")
test_conjured_item.reset_quality()

test_conjured_item.update_quality(14)
if test_conjured_item.show_quality() != 14:
    raise ValueError ("El valor del item conjurado es incorrecto.")
test_conjured_item.reset_quality()

test_conjured_item.update_quality(10000)
if test_conjured_item.show_quality() <0:
    raise ValueError ("El valor Quality del item conjurado no puede ser menor que cero.")
test_conjured_item.reset_quality()

if test_conjured_item.show_quality() >50:
    raise ValueError ("El valor Quality del item conjurado no puede ser mayor de 50.")
test_conjured_item.reset_quality()

test_backstage_passes = BackstagePasses(10,15)

test_backstage_passes.update_quality(4)
if test_backstage_passes.show_quality() != 10:
    raise ValueError("El valor Quality de las entradas no es correcto.")
test_backstage_passes.reset_quality()

test_backstage_passes.update_quality(6)
if test_backstage_passes.show_quality() != 12:
    raise ValueError("El valor Quality de las entradas no es correcto.")
test_backstage_passes.reset_quality()

test_backstage_passes.update_quality(14)
if test_backstage_passes.show_quality() != 15:
    raise ValueError("El valor Quality de las entradas no es correcto.")
test_backstage_passes.reset_quality()

test_backstage_passes.update_quality(16)
if test_backstage_passes.show_quality() != 0:
    raise ValueError("El valor Quality de las entradas no es correcto, debería ser cero.")
test_backstage_passes.reset_quality()