from BACKEND.read_analize_CSV import open_csv
from BACKEND.showInfo import  describe

saved_excercises = open_csv() #Read CSV

describe("En un teatro cada cliente paga $10.000 por entrada y cada función le cuesta al teatro $300.000 por la atención prestada. Por cada cliente que entre el teatro debe pagar un costo de $2.000 por aseo. Desarrollar un programa que reciba el número de clientes de una función y devuelva el valor de las ganancias obtenidas.", saved_excercises)
describe("Un cliente ordena una cierta cantidad de brochas de cerda, rodillos y sellador; las brochas de cerda tienen un 20% de descuento y los rodillos un 15% de descuento. Los datos que se tienen por cada tipo de articulo son: La cantidad pedida y el precio unitario. Además, si se paga de contado todo tiene un descuento del 7%. Elaborar un programa que permita visualizar el precio total de una cierta orden de n cantidad productos, tanto para pago de contado como pago a crédito.", saved_excercises)
describe("A través de una estructura persona, crear un archivo que guarde 5 registros de la estructura persona, una línea por registro. Se deben usar las características mas notables de una persona",saved_excercises)
describe("Hacer un programa el cual al leer un archivo de texto, pueda contar el número de palabras que componen al archivo.", saved_excercises)
# s = "por cada cliente que entre en el
# l = "En un teatro cada cliente paga $10.000 por entrada y cada función le cuesta al teatro $300.000 por la atención prestada. Por cada cliente que entre el teatro debe pagar un costo de $2.000 por aseo. Desarrollar un programa que reciba el número de clientes de una función y devuelva el valor de las ganancias obtenidas."
# print(s in l)