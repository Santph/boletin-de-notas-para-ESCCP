from tkinter import *

materias = ["matematica", "lengua", "historia", "geografia", "ciencias naturales", "informatica", "educacion fisica", "accion solidaria", "plastica", "musica", "taller de aprendisaje", "ingles"]
instancias = ["P.E. y concepto(1er cuatrimestre)", "prueba integradora(1er cuatrimestre)", "P.E. y concepto(2do cuatrimestre)", "prueba integradora(2do cuatrimestre)", "noviembre", "diciembre", "febrero", "marzo"]

def periodico(num_periodico):
    que_debolver = ""
    num_list =  list()
    num_str = str(num_periodico) 
    len_num = len(str(num_periodico))
    if(len_num > 8):
        for i in num_str:
            num_list.append(i)

        while(len(num_list) > 7):
            num_list.pop(-1)

        for i in range(0, len(num_list)):
            que_debolver = que_debolver + str(num_list[i])
            if(i == len(num_list) - 1):
                que_debolver = que_debolver + "*"
    else:
        que_debolver = str(num_periodico)

    return que_debolver




def promediar_cuatrimestre(cuatrimestre = int):
    returned = 0.0
    if(cuatrimestre == 1):
        try:
            returned = int(mate1.cget("text")) + int(mate2.cget("text")) + int(leng1.cget("text")) + int(leng2.cget("text")) + int(histo1.cget("text")) + int(histo2.cget("text")) + int(geo1.cget("text")) + int(geo2.cget("text")) + int(natu1.cget("text")) + int(natu2.cget("text")) + int(info1.cget("text")) + int(info2.cget("text")) + int(efisica1.cget("text")) + int(efisica2.cget("text")) + int(asoli1.cget("text")) + int(asoli2.cget("text")) + int(plas1.cget("text")) + int(plas2.cget("text")) + int(musi1.cget("text")) + int(musi2.cget("text")) + int(tdapren1.cget("text")) + int(tdapren2.cget("text")) + int(ing1.cget("text")) + int(ing2.cget("text"))
        except:
            returned = None
    else:
        try:
            returned = int(mate3.cget("text")) + int(mate4.cget("text")) + int(leng3.cget("text")) + int(leng4.cget("text")) + int(histo3.cget("text")) + int(histo4.cget("text")) + int(geo3.cget("text")) + int(geo4.cget("text")) + int(natu3.cget("text")) + int(natu4.cget("text")) + int(info3.cget("text")) + int(info4.cget("text")) + int(efisica3.cget("text")) + int(efisica4.cget("text")) + int(asoli3.cget("text")) + int(asoli4.cget("text")) + int(plas3.cget("text")) + int(plas4.cget("text")) + int(musi3.cget("text")) + int(musi4.cget("text")) + int(tdapren3.cget("text")) + int(tdapren4.cget("text")) + int(ing3.cget("text")) + int(ing4.cget("text"))
        except:
            returned = None

    try:
        return returned / 24
    except:
        return returned

def on_closing():
    #guardar los datos
    datos_guardados = list()
    datos_guardados = datos_a_guardar()

    guardar_datos(datos_guardados, "celdas.txt")
    #destuir la raiz
    root.destroy()

def datos_a_guardar():

    returned = list()
    for i in range(0, 144):
        returned.append("")

    returned[0] = mate1.cget('text')
    returned[1] = mate2.cget("text")
    returned[2] = mate3.cget("text")
    returned[3] = mate4.cget("text")
    returned[4] = mate5.cget("text")
    returned[5] = mate6.cget("text")
    returned[6] = mate7.cget("text")
    returned[7] = mate8.cget("text")
    returned[8] = mate9.cget("text")
    returned[9] = mate10.cget("text")
    returned[10] = mate11.cget("text")
    returned[11] = mate12.cget("text")
    
    returned[12] = leng1.cget("text")
    returned[13] = leng2.cget("text")
    returned[14] = leng3.cget("text")
    returned[15] = leng4.cget("text")
    returned[16] = leng5.cget("text")
    returned[17] = leng6.cget("text")
    returned[18] = leng7.cget("text")
    returned[19] = leng8.cget("text")
    returned[20] = leng9.cget("text")
    returned[21] = leng10.cget("text")
    returned[22] = leng11.cget("text")
    returned[23] = leng12.cget("text")
    
    returned[24] = histo1.cget("text")
    returned[25] = histo2.cget("text")
    returned[26] = histo3.cget("text")
    returned[27] = histo4.cget("text")
    returned[28] = histo5.cget("text")
    returned[29] = histo6.cget("text")
    returned[30] = histo7.cget("text")
    returned[31] = histo8.cget("text")
    returned[32] = histo9.cget("text")
    returned[33] = histo10.cget("text")
    returned[34] = histo11.cget("text")
    returned[35] = histo12.cget("text")

    returned[36] = geo1.cget("text")
    returned[37] = geo2.cget("text")
    returned[38] = geo3.cget("text")
    returned[39] = geo4.cget("text")
    returned[40] = geo5.cget("text")
    returned[41] = geo6.cget("text")
    returned[42] = geo7.cget("text")
    returned[43] = geo8.cget("text")
    returned[44] = geo9.cget("text")
    returned[45] = geo10.cget("text")
    returned[46] = geo11.cget("text")
    returned[47] = geo12.cget("text")

    returned[48] = natu1.cget("text")
    returned[49] = natu2.cget("text")
    returned[50] = natu3.cget("text")
    returned[51] = natu4.cget("text")
    returned[52] = natu5.cget("text")
    returned[53] = natu6.cget("text")
    returned[54] = natu7.cget("text")
    returned[55] = natu8.cget("text")
    returned[56] = natu9.cget("text")
    returned[57] = natu10.cget("text")
    returned[58] = natu11.cget("text")
    returned[59] = natu12.cget("text")

    returned[60] = info1.cget("text")
    returned[61] = info2.cget("text")
    returned[62] = info3.cget("text")
    returned[63] = info4.cget("text")
    returned[64] = info5.cget("text")
    returned[65] = info6.cget("text")
    returned[66] = info7.cget("text")
    returned[67] = info8.cget("text")
    returned[68] = info9.cget("text")
    returned[69] = info10.cget("text")
    returned[70] = info11.cget("text")
    returned[71] = info12.cget("text")

    returned[72] = efisica1.cget("text")
    returned[73] = efisica2.cget("text")
    returned[74] = efisica3.cget("text")
    returned[75] = efisica4.cget("text")
    returned[76] = efisica5.cget("text")
    returned[77] = efisica6.cget("text")
    returned[78] = efisica7.cget("text")
    returned[79] = efisica8.cget("text")
    returned[80] = efisica9.cget("text")
    returned[81] = efisica10.cget("text")
    returned[82] = efisica11.cget("text")
    returned[83] = efisica12.cget("text")

    returned[84] = asoli1.cget("text")
    returned[85] = asoli2.cget("text")
    returned[86] = asoli3.cget("text")
    returned[87] = asoli4.cget("text")
    returned[88] = asoli5.cget("text")
    returned[89] = asoli6.cget("text")
    returned[90] = asoli7.cget("text")
    returned[91] = asoli8.cget("text")
    returned[92] = asoli9.cget("text")
    returned[93] = asoli10.cget("text")
    returned[94] = asoli11.cget("text")
    returned[95] = asoli12.cget("text")

    returned[96] = plas1.cget("text")
    returned[97] = plas2.cget("text")
    returned[98] = plas3.cget("text")
    returned[99] = plas4.cget("text")
    returned[100] = plas5.cget("text")
    returned[101] = plas6.cget("text")
    returned[102] = plas7.cget("text")
    returned[103] = plas8.cget("text")
    returned[104] = plas9.cget("text")
    returned[105] = plas10.cget("text")
    returned[106] = plas11.cget("text")
    returned[107] = plas12.cget("text")

    returned[108] = musi1.cget("text")
    returned[109] = musi2.cget("text")
    returned[110] = musi3.cget("text")
    returned[111] = musi4.cget("text")
    returned[112] = musi5.cget("text")
    returned[113] = musi6.cget("text")
    returned[114] = musi7.cget("text")
    returned[115] = musi8.cget("text")
    returned[116] = musi9.cget("text")
    returned[117] = musi10.cget("text")
    returned[118] = musi11.cget("text")
    returned[119] = musi12.cget("text")
    
    returned[120] = tdapren1.cget("text")
    returned[121] = tdapren2.cget("text")
    returned[122] = tdapren3.cget("text")
    returned[123] = tdapren4.cget("text")
    returned[124] = tdapren5.cget("text")
    returned[125] = tdapren6.cget("text")
    returned[126] = tdapren7.cget("text")
    returned[127] = tdapren8.cget("text")
    returned[128] = tdapren9.cget("text")
    returned[129] = tdapren10.cget("text")
    returned[130] = tdapren11.cget("text")
    returned[131] = tdapren12.cget("text")

    returned[132] = ing1.cget("text")
    returned[133] = ing2.cget("text")
    returned[134] = ing3.cget("text")
    returned[135] = ing4.cget("text")
    returned[136] = ing5.cget("text")
    returned[137] = ing6.cget("text")
    returned[138] = ing7.cget("text")
    returned[139] = ing8.cget("text")
    returned[140] = ing9.cget("text")
    returned[141] = ing10.cget("text")
    returned[142] = ing11.cget("text")
    returned[143] = ing12.cget("text")

    return returned

    

def guardar_datos(datos = list(), direccion_archivo = str):
    datos_str = list()
    for i in range(0, len(datos)):
        datos_str.append(str(datos[i]))

    archivo = open(direccion_archivo, "w")

    for i in range(0, len(datos_str)):
        archivo.write(str(datos_str[i] + ","))


    archivo.close()

def recuperar_datos(direccion_archivo = str):
    

    try:
        archivo = open(direccion_archivo, "r")
    except:
        guardar_datos([], "celdas.txt")
        archivo = open(direccion_archivo, "r")
        

    datos = archivo.read()
        
    datos_list = list()
    appendable = ""

    for char in datos:
        if(char == ","):
            datos_list.append(appendable)
            appendable = ""
        else:
            appendable = appendable + char


    return datos_list



def redondeo_especial(nums_a_redondear = list()):
    nums_a_redondear_integer = list()
    for i in range(0, len(nums_a_redondear)):
        try:
            nums_a_redondear_integer.append(int(nums_a_redondear[i]))
        except:
            return ""
    num2 = 0
    for i in range(0, len(nums_a_redondear_integer)):
        num2 = num2 + int(nums_a_redondear_integer[i])
    num2 = num2 / len(nums_a_redondear_integer)
    deci = num2 % 1
    if(deci > 0.49 and num2 > 4):
        num2 = num2 - deci + 1
        
    else:
        num2 = num2 - deci
    return int(num2)


#on enter/on leave mate
def on_enter_mate(event):
    mate1.config(bg="yellow")
    mate2.config(bg="yellow")
    mate3.config(bg="yellow")
    mate4.config(bg="yellow")
    mate5.config(bg="yellow")
    mate6.config(bg="yellow")
    mate7.config(bg="yellow")
    mate8.config(bg="yellow")
    mate9.config(bg="yellow")
    mate10.config(bg="yellow")
    mate11.config(bg="yellow")
    mate12.config(bg="yellow")
    valor2.set(materias[0])

def on_leave_mate(event):
    mate1.config(bg=original_bg)
    mate2.config(bg=original_bg)
    mate3.config(bg=original_bg)
    mate4.config(bg=original_bg)
    mate5.config(bg=original_bg)
    mate6.config(bg=original_bg)
    mate7.config(bg=original_bg)
    mate8.config(bg=original_bg)
    mate9.config(bg=original_bg)
    mate10.config(bg=original_bg)
    mate11.config(bg=original_bg)
    mate12.config(bg=original_bg)

#on enter/on leave lengua
def on_enter_leng(event):
    leng1.config(bg="yellow")
    leng2.config(bg="yellow")
    leng3.config(bg="yellow")
    leng4.config(bg="yellow")
    leng5.config(bg="yellow")
    leng6.config(bg="yellow")
    leng7.config(bg="yellow")
    leng8.config(bg="yellow")
    leng9.config(bg="yellow")
    leng10.config(bg="yellow")
    leng11.config(bg="yellow")
    leng12.config(bg="yellow")
    valor2.set(materias[1])

def on_leave_leng(event):
    leng1.config(bg=original_bg)
    leng2.config(bg=original_bg)
    leng3.config(bg=original_bg)
    leng4.config(bg=original_bg)
    leng5.config(bg=original_bg)
    leng6.config(bg=original_bg)
    leng7.config(bg=original_bg)
    leng8.config(bg=original_bg)
    leng9.config(bg=original_bg)
    leng10.config(bg=original_bg)
    leng11.config(bg=original_bg)
    leng12.config(bg=original_bg)

#on enter/on leave historia
def on_enter_histo(event):
    histo1.config(bg="yellow")
    histo2.config(bg="yellow")
    histo3.config(bg="yellow")
    histo4.config(bg="yellow")
    histo5.config(bg="yellow")
    histo6.config(bg="yellow")
    histo7.config(bg="yellow")
    histo8.config(bg="yellow")
    histo9.config(bg="yellow")
    histo10.config(bg="yellow")
    histo11.config(bg="yellow")
    histo12.config(bg="yellow")
    valor2.set(materias[2])

def on_leave_histo(event):
    histo1.config(bg=original_bg)
    histo2.config(bg=original_bg)
    histo3.config(bg=original_bg)
    histo4.config(bg=original_bg)
    histo5.config(bg=original_bg)
    histo6.config(bg=original_bg)
    histo7.config(bg=original_bg)
    histo8.config(bg=original_bg)
    histo9.config(bg=original_bg)
    histo10.config(bg=original_bg)
    histo11.config(bg=original_bg)
    histo12.config(bg=original_bg)

#on enter/on leave geografia
def on_enter_geo(event):
    geo1.config(bg="yellow")
    geo2.config(bg="yellow")
    geo3.config(bg="yellow")
    geo4.config(bg="yellow")
    geo5.config(bg="yellow")
    geo6.config(bg="yellow")
    geo7.config(bg="yellow")
    geo8.config(bg="yellow")
    geo9.config(bg="yellow")
    geo10.config(bg="yellow")
    geo11.config(bg="yellow")
    geo12.config(bg="yellow")
    valor2.set(materias[3])

def on_leave_geo(event):
    geo1.config(bg=original_bg)
    geo2.config(bg=original_bg)
    geo3.config(bg=original_bg)
    geo4.config(bg=original_bg)
    geo5.config(bg=original_bg)
    geo6.config(bg=original_bg)
    geo7.config(bg=original_bg)
    geo8.config(bg=original_bg)
    geo9.config(bg=original_bg)
    geo10.config(bg=original_bg)
    geo11.config(bg=original_bg)
    geo12.config(bg=original_bg)

#on enter/on leave naturales
def on_enter_natu(event):
    natu1.config(bg="yellow")
    natu2.config(bg="yellow")
    natu3.config(bg="yellow")
    natu4.config(bg="yellow")
    natu5.config(bg="yellow")
    natu6.config(bg="yellow")
    natu7.config(bg="yellow")
    natu8.config(bg="yellow")
    natu9.config(bg="yellow")
    natu10.config(bg="yellow")
    natu11.config(bg="yellow")
    natu12.config(bg="yellow")
    valor2.set(materias[4])

def on_leave_natu(event):
    natu1.config(bg=original_bg)
    natu2.config(bg=original_bg)
    natu3.config(bg=original_bg)
    natu4.config(bg=original_bg)
    natu5.config(bg=original_bg)
    natu6.config(bg=original_bg)
    natu7.config(bg=original_bg)
    natu8.config(bg=original_bg)
    natu9.config(bg=original_bg)
    natu10.config(bg=original_bg)
    natu11.config(bg=original_bg)
    natu12.config(bg=original_bg)

#on enter/on leave informatica
def on_enter_info(event):
    info1.config(bg="yellow")
    info2.config(bg="yellow")
    info3.config(bg="yellow")
    info4.config(bg="yellow")
    info5.config(bg="yellow")
    info6.config(bg="yellow")
    info7.config(bg="yellow")
    info8.config(bg="yellow")
    info9.config(bg="yellow")
    info10.config(bg="yellow")
    info11.config(bg="yellow")
    info12.config(bg="yellow")
    valor2.set(materias[5])

def on_leave_info(event):
    info1.config(bg=original_bg)
    info2.config(bg=original_bg)
    info3.config(bg=original_bg)
    info4.config(bg=original_bg)
    info5.config(bg=original_bg)
    info6.config(bg=original_bg)
    info7.config(bg=original_bg)
    info8.config(bg=original_bg)
    info9.config(bg=original_bg)
    info10.config(bg=original_bg)
    info11.config(bg=original_bg)
    info12.config(bg=original_bg)

#on enter/on leave E.fisica
def on_enter_efisica(event):
    efisica1.config(bg="yellow")
    efisica2.config(bg="yellow")
    efisica3.config(bg="yellow")
    efisica4.config(bg="yellow")
    efisica5.config(bg="yellow")
    efisica6.config(bg="yellow")
    efisica7.config(bg="yellow")
    efisica8.config(bg="yellow")
    efisica9.config(bg="yellow")
    efisica10.config(bg="yellow")
    efisica11.config(bg="yellow")
    efisica12.config(bg="yellow")
    valor2.set(materias[6])

def on_leave_efisica(event):
    efisica1.config(bg=original_bg)
    efisica2.config(bg=original_bg)
    efisica3.config(bg=original_bg)
    efisica4.config(bg=original_bg)
    efisica5.config(bg=original_bg)
    efisica6.config(bg=original_bg)
    efisica7.config(bg=original_bg)
    efisica8.config(bg=original_bg)
    efisica9.config(bg=original_bg)
    efisica10.config(bg=original_bg)
    efisica11.config(bg=original_bg)
    efisica12.config(bg=original_bg)

#on enter/on leave A.solidaria
def on_enter_asoli(event):
    asoli1.config(bg="yellow")
    asoli2.config(bg="yellow")
    asoli3.config(bg="yellow")
    asoli4.config(bg="yellow")
    asoli5.config(bg="yellow")
    asoli6.config(bg="yellow")
    asoli7.config(bg="yellow")
    asoli8.config(bg="yellow")
    asoli9.config(bg="yellow")
    asoli10.config(bg="yellow")
    asoli11.config(bg="yellow")
    asoli12.config(bg="yellow")
    valor2.set(materias[7])

def on_leave_asoli(event):
    asoli1.config(bg=original_bg)
    asoli2.config(bg=original_bg)
    asoli3.config(bg=original_bg)
    asoli4.config(bg=original_bg)
    asoli5.config(bg=original_bg)
    asoli6.config(bg=original_bg)
    asoli7.config(bg=original_bg)
    asoli8.config(bg=original_bg)
    asoli9.config(bg=original_bg)
    asoli10.config(bg=original_bg)
    asoli11.config(bg=original_bg)
    asoli12.config(bg=original_bg)

#on enter/on leave plastica
def on_enter_plas(event):
    plas1.config(bg="yellow")
    plas2.config(bg="yellow")
    plas3.config(bg="yellow")
    plas4.config(bg="yellow")
    plas5.config(bg="yellow")
    plas6.config(bg="yellow")
    plas7.config(bg="yellow")
    plas8.config(bg="yellow")
    plas9.config(bg="yellow")
    plas10.config(bg="yellow")
    plas11.config(bg="yellow")
    valor2.set(materias[8])

def on_leave_plas(event):
    plas1.config(bg=original_bg)
    plas2.config(bg=original_bg)
    plas3.config(bg=original_bg)
    plas4.config(bg=original_bg)
    plas5.config(bg=original_bg)
    plas6.config(bg=original_bg)
    plas7.config(bg=original_bg)
    plas8.config(bg=original_bg)
    plas9.config(bg=original_bg)
    plas10.config(bg=original_bg)
    plas11.config(bg=original_bg)
    plas12.config(bg=original_bg)

#on enter/on leave musica
def on_enter_musi(event):
    musi1.config(bg="yellow")
    musi2.config(bg="yellow")
    musi3.config(bg="yellow")
    musi4.config(bg="yellow")
    musi5.config(bg="yellow")
    musi6.config(bg="yellow")
    musi7.config(bg="yellow")
    musi8.config(bg="yellow")
    musi9.config(bg="yellow")
    musi10.config(bg="yellow")
    musi11.config(bg="yellow")
    musi12.config(bg="yellow")
    valor2.set(materias[9])

def on_leave_musi(event):
    musi1.config(bg=original_bg)
    musi2.config(bg=original_bg)
    musi3.config(bg=original_bg)
    musi4.config(bg=original_bg)
    musi5.config(bg=original_bg)
    musi6.config(bg=original_bg)
    musi7.config(bg=original_bg)
    musi8.config(bg=original_bg)
    musi9.config(bg=original_bg)
    musi10.config(bg=original_bg)
    musi11.config(bg=original_bg)
    musi12.config(bg=original_bg)

#on enter/on leave T. de aprendisaje
def on_enter_tdaprend(event):
    tdapren1.config(bg="yellow")
    tdapren2.config(bg="yellow")
    tdapren3.config(bg="yellow")
    tdapren4.config(bg="yellow")
    tdapren5.config(bg="yellow")
    tdapren6.config(bg="yellow")
    tdapren7.config(bg="yellow")
    tdapren8.config(bg="yellow")
    tdapren9.config(bg="yellow")
    tdapren10.config(bg="yellow")
    tdapren11.config(bg="yellow")
    tdapren12.config(bg="yellow")
    valor2.set(materias[10])

def on_leave_tdaprend(event):
    tdapren1.config(bg=original_bg)
    tdapren2.config(bg=original_bg)
    tdapren3.config(bg=original_bg)
    tdapren4.config(bg=original_bg)
    tdapren5.config(bg=original_bg)
    tdapren6.config(bg=original_bg)
    tdapren7.config(bg=original_bg)
    tdapren8.config(bg=original_bg)
    tdapren9.config(bg=original_bg)
    tdapren10.config(bg=original_bg)
    tdapren11.config(bg=original_bg)
    tdapren12.config(bg=original_bg)

def on_enter_ing(event):
    ing1.config(bg="yellow")
    ing2.config(bg="yellow")
    ing3.config(bg="yellow")
    ing4.config(bg="yellow")
    ing5.config(bg="yellow")
    ing6.config(bg="yellow")
    ing7.config(bg="yellow")
    ing8.config(bg="yellow")
    ing9.config(bg="yellow")
    ing10.config(bg="yellow")
    ing11.config(bg="yellow")
    ing12.config(bg="yellow")
    valor2.set(materias[11])

def on_leave_ing(event):
    ing1.config(bg=original_bg)
    ing2.config(bg=original_bg)
    ing3.config(bg=original_bg)
    ing4.config(bg=original_bg)
    ing5.config(bg=original_bg)
    ing6.config(bg=original_bg)
    ing7.config(bg=original_bg)
    ing8.config(bg=original_bg)
    ing9.config(bg=original_bg)
    ing10.config(bg=original_bg)
    ing11.config(bg=original_bg)
    ing12.config(bg=original_bg)





def button_function():

    nota = obtener_nota.get()
    instancia = valor1.get()
    materia = valor2.get()
    
    if(materia == materias[0]):
        if(instancia == instancias[0]):
            mate1.config(text=nota)
        elif(instancia == instancias[1]):
            mate2.config(text=nota)
        elif(instancia == instancias[2]):
            mate3.config(text=nota)
        elif(instancia == instancias[3]):
            mate4.config(text=nota)
        elif(instancia == instancias[4]):
            mate5.config(text=nota)
        elif(instancia == instancias[5]):
            mate6.config(text=nota)
        elif(instancia == instancias[6]):
            mate7.config(text=nota)
        elif(instancia == instancias[7]):
            mate8.config(text=nota)
        elif(instancia == instancias[8]):
            mate9.config(text=nota)
        elif(instancia == instancias[9]):
            mate10.config(text=nota)
        elif(instancia == instancias[10]):
            mate11.config(text=nota)
        elif(instancia == instancias[11]):
            mate12.config(text=nota)
    
    if(materia == materias[1]):
        if(instancia == instancias[0]):
            leng1.config(text=nota)
        elif(instancia == instancias[1]):
            leng2.config(text=nota)
        elif(instancia == instancias[2]):
            leng3.config(text=nota)
        elif(instancia == instancias[3]):
            leng4.config(text=nota)
        elif(instancia == instancias[4]):
            leng5.config(text=nota)
        elif(instancia == instancias[5]):
            leng6.config(text=nota)
        elif(instancia == instancias[6]):
            leng7.config(text=nota)
        elif(instancia == instancias[7]):
            leng8.config(text=nota)
        elif(instancia == instancias[8]):
            leng9.config(text=nota)
        elif(instancia == instancias[9]):
            leng10.config(text=nota)
        elif(instancia == instancias[10]):
            leng11.config(text=nota)
        elif(instancia == instancias[11]):
            leng12.config(text=nota)

    if(materia == materias[2]):
        if(instancia == instancias[0]):
            histo1.config(text=nota)
        elif(instancia == instancias[1]):
            histo2.config(text=nota)
        elif(instancia == instancias[2]):
            histo3.config(text=nota)
        elif(instancia == instancias[3]):
            histo4.config(text=nota)
        elif(instancia == instancias[4]):
            histo5.config(text=nota)
        elif(instancia == instancias[5]):
            histo6.config(text=nota)
        elif(instancia == instancias[6]):
            histo7.config(text=nota)
        elif(instancia == instancias[7]):
            histo8.config(text=nota)
        elif(instancia == instancias[8]):
            histo9.config(text=nota)
        elif(instancia == instancias[9]):
            histo10.config(text=nota)
        elif(instancia == instancias[10]):
            histo11.config(text=nota)
        elif(instancia == instancias[11]):
            histo12.config(text=nota)

    if(materia == materias[3]):
        if(instancia == instancias[0]):
            geo1.config(text=nota)
        elif(instancia == instancias[1]):
            geo2.config(text=nota)
        elif(instancia == instancias[2]):
            geo3.config(text=nota)
        elif(instancia == instancias[3]):
            geo4.config(text=nota)
        elif(instancia == instancias[4]):
            geo5.config(text=nota)
        elif(instancia == instancias[5]):
            geo6.config(text=nota)
        elif(instancia == instancias[6]):
            geo7.config(text=nota)
        elif(instancia == instancias[7]):
            geo8.config(text=nota)
        elif(instancia == instancias[8]):
            geo9.config(text=nota)
        elif(instancia == instancias[9]):
            geo10.config(text=nota)
        elif(instancia == instancias[10]):
            geo11.config(text=nota)
        elif(instancia == instancias[11]):
            geo12.config(text=nota)

    if(materia == materias[4]):
        if(instancia == instancias[0]):
            natu1.config(text=nota)
        elif(instancia == instancias[1]):
            natu2.config(text=nota)
        elif(instancia == instancias[2]):
            natu3.config(text=nota)
        elif(instancia == instancias[3]):
            natu4.config(text=nota)
        elif(instancia == instancias[4]):
            natu5.config(text=nota)
        elif(instancia == instancias[5]):
            natu6.config(text=nota)
        elif(instancia == instancias[6]):
            natu7.config(text=nota)
        elif(instancia == instancias[7]):
            natu8.config(text=nota)
        elif(instancia == instancias[8]):
            natu9.config(text=nota)
        elif(instancia == instancias[9]):
            natu10.config(text=nota)
        elif(instancia == instancias[10]):
            natu11.config(text=nota)
        elif(instancia == instancias[11]):
            natu12.config(text=nota)
    
    if(materia == materias[5]):
        if(instancia == instancias[0]):
            info1.config(text=nota)
        elif(instancia == instancias[1]):
            info2.config(text=nota)
        elif(instancia == instancias[2]):
            info3.config(text=nota)
        elif(instancia == instancias[3]):
            info4.config(text=nota)
        elif(instancia == instancias[4]):
            info5.config(text=nota)
        elif(instancia == instancias[5]):
            info6.config(text=nota)
        elif(instancia == instancias[6]):
            info7.config(text=nota)
        elif(instancia == instancias[7]):
            info8.config(text=nota)
        elif(instancia == instancias[8]):
            info9.config(text=nota)
        elif(instancia == instancias[9]):
            info10.config(text=nota)
        elif(instancia == instancias[10]):
            info11.config(text=nota)
        elif(instancia == instancias[11]):
            info12.config(text=nota)

    if(materia == materias[6]):
        if(instancia == instancias[0]):
            efisica1.config(text=nota)
        elif(instancia == instancias[1]):
            efisica2.config(text=nota)
        elif(instancia == instancias[2]):
            efisica3.config(text=nota)
        elif(instancia == instancias[3]):
            efisica4.config(text=nota)
        elif(instancia == instancias[4]):
            efisica5.config(text=nota)
        elif(instancia == instancias[5]):
            efisica6.config(text=nota)
        elif(instancia == instancias[6]):
            efisica7.config(text=nota)
        elif(instancia == instancias[7]):
            efisica8.config(text=nota)
        elif(instancia == instancias[8]):
            efisica9.config(text=nota)
        elif(instancia == instancias[9]):
            efisica10.config(text=nota)
        elif(instancia == instancias[10]):
            efisica11.config(text=nota)
        elif(instancia == instancias[11]):
            efisica12.config(text=nota)

    if(materia == materias[7]):
        if(instancia == instancias[0]):
            asoli1.config(text=nota)
        elif(instancia == instancias[1]):
            asoli2.config(text=nota)
        elif(instancia == instancias[2]):
            asoli3.config(text=nota)
        elif(instancia == instancias[3]):
            asoli4.config(text=nota)
        elif(instancia == instancias[4]):
            asoli5.config(text=nota)
        elif(instancia == instancias[5]):
            asoli6.config(text=nota)
        elif(instancia == instancias[6]):
            asoli7.config(text=nota)
        elif(instancia == instancias[7]):
            asoli8.config(text=nota)
        elif(instancia == instancias[8]):
            asoli9.config(text=nota)
        elif(instancia == instancias[9]):
            asoli10.config(text=nota)
        elif(instancia == instancias[10]):
            asoli11.config(text=nota)
        elif(instancia == instancias[11]):
            asoli12.config(text=nota)

    if(materia == materias[8]):
        if(instancia == instancias[0]):
            plas1.config(text=nota)
        elif(instancia == instancias[1]):
            plas2.config(text=nota)
        elif(instancia == instancias[2]):
            plas3.config(text=nota)
        elif(instancia == instancias[3]):
            plas4.config(text=nota)
        elif(instancia == instancias[4]):
            plas5.config(text=nota)
        elif(instancia == instancias[5]):
            plas6.config(text=nota)
        elif(instancia == instancias[6]):
            plas7.config(text=nota)
        elif(instancia == instancias[7]):
            plas8.config(text=nota)
        elif(instancia == instancias[8]):
            plas9.config(text=nota)
        elif(instancia == instancias[9]):
            plas10.config(text=nota)
        elif(instancia == instancias[10]):
            plas11.config(text=nota)
        elif(instancia == instancias[11]):
            plas12.config(text=nota)

    if(materia == materias[9]):
        if(instancia == instancias[0]):
            musi1.config(text=nota)
        elif(instancia == instancias[1]):
            musi2.config(text=nota)
        elif(instancia == instancias[2]):
            musi3.config(text=nota)
        elif(instancia == instancias[3]):
            musi4.config(text=nota)
        elif(instancia == instancias[4]):
            musi5.config(text=nota)
        elif(instancia == instancias[5]):
            musi6.config(text=nota)
        elif(instancia == instancias[6]):
            musi7.config(text=nota)
        elif(instancia == instancias[7]):
            musi8.config(text=nota)
        elif(instancia == instancias[8]):
            musi9.config(text=nota)
        elif(instancia == instancias[9]):
            musi10.config(text=nota)
        elif(instancia == instancias[10]):
            musi11.config(text=nota)
        elif(instancia == instancias[11]):
            musi12.config(text=nota)

    if(materia == materias[10]):
        if(instancia == instancias[0]):
            tdapren1.config(text=nota)
        elif(instancia == instancias[1]):
            tdapren2.config(text=nota)
        elif(instancia == instancias[2]):
            tdapren3.config(text=nota)
        elif(instancia == instancias[3]):
            tdapren4.config(text=nota)
        elif(instancia == instancias[4]):
            tdapren5.config(text=nota)
        elif(instancia == instancias[5]):
            tdapren6.config(text=nota)
        elif(instancia == instancias[6]):
            tdapren7.config(text=nota)
        elif(instancia == instancias[7]):
            tdapren8.config(text=nota)
        elif(instancia == instancias[8]):
            tdapren9.config(text=nota)
        elif(instancia == instancias[9]):
            tdapren10.config(text=nota)
        elif(instancia == instancias[10]):
            tdapren11.config(text=nota)
        elif(instancia == instancias[11]):
            tdapren12.config(text=nota)

    if(materia == materias[11]):
        if(instancia == instancias[0]):
            ing1.config(text=nota)
        elif(instancia == instancias[1]):
            ing2.config(text=nota)
        elif(instancia == instancias[2]):
            ing3.config(text=nota)
        elif(instancia == instancias[3]):
            ing4.config(text=nota)
        elif(instancia == instancias[4]):
            ing5.config(text=nota)
        elif(instancia == instancias[5]):
            ing6.config(text=nota)
        elif(instancia == instancias[6]):
            ing7.config(text=nota)
        elif(instancia == instancias[7]):
            ing8.config(text=nota)
        elif(instancia == instancias[8]):
            ing9.config(text=nota)
        elif(instancia == instancias[9]):
            ing10.config(text=nota)
        elif(instancia == instancias[10]):
            ing11.config(text=nota)
        elif(instancia == instancias[11]):
            ing12.config(text=nota)

    promedio_cuatrimestre_1.config(text="promedio del segundo cuatrimestre: " + str(promediar_cuatrimestre(1)))
    promedio_cuatrimestre_2.config(text="promedio del segundo cuatrimestre: " + str(promediar_cuatrimestre(2)))

#ejecutar redondeos
    mate9.config(text=redondeo_especial([mate1.cget("text"), mate2.cget("text")]))
    mate10.config(text=redondeo_especial([mate3.cget("text"), mate4.cget("text")]))
    mate11.config(text=redondeo_especial([mate1.cget("text"), mate2.cget("text"), mate3.cget("text"), mate4.cget("text")]))
    mate12.config(text=redondeo_especial([mate11.cget("text"), leng11.cget("text"), histo11.cget("text"), geo11.cget("text"), natu11.cget("text"), info11.cget("text"), efisica11.cget("text"), asoli11.cget("text"), plas11.cget("text"), musi11.cget("text"), tdapren11.cget("text")]))

    leng9.config(text=redondeo_especial([leng1.cget("text"), leng2.cget("text")]))
    leng10.config(text=redondeo_especial([leng3.cget("text"), leng4.cget("text")]))
    leng11.config(text=redondeo_especial([leng1.cget("text"), leng2.cget("text"), leng3.cget("text"), leng4.cget("text")]))

    histo9.config(text=redondeo_especial([histo1.cget("text"), histo2.cget("text")]))
    histo10.config(text=redondeo_especial([histo3.cget("text"), histo4.cget("text")]))
    histo11.config(text=redondeo_especial([histo1.cget("text"), histo2.cget("text"), histo3.cget("text"), histo4.cget("text")]))

    geo9.config(text=redondeo_especial([geo1.cget("text"), geo2.cget("text")]))
    geo10.config(text=redondeo_especial([geo3.cget("text"), geo4.cget("text")]))
    geo11.config(text=redondeo_especial([geo1.cget("text"), geo2.cget("text"), geo3.cget("text"), geo4.cget("text")]))

    natu9.config(text=redondeo_especial([natu1.cget("text"), natu2.cget("text")]))
    natu10.config(text=redondeo_especial([natu3.cget("text"), natu4.cget("text")]))
    natu11.config(text=redondeo_especial([natu1.cget("text"), natu2.cget("text"), mate3.cget("text"), mate4.cget("text")]))

    info9.config(text=redondeo_especial([info1.cget("text"), info2.cget("text")]))
    info10.config(text=redondeo_especial([info3.cget("text"), info4.cget("text")]))
    info11.config(text=redondeo_especial([info1.cget("text"), info2.cget("text"), mate3.cget("text"), mate4.cget("text")]))

    efisica9.config(text=redondeo_especial([efisica1.cget("text"), efisica2.cget("text")]))
    efisica10.config(text=redondeo_especial([efisica3.cget("text"), efisica4.cget("text")]))
    efisica11.config(text=redondeo_especial([efisica1.cget("text"), efisica2.cget("text"), mate3.cget("text"), mate4.cget("text")]))

    asoli9.config(text=redondeo_especial([asoli1.cget("text"), asoli2.cget("text")]))
    asoli10.config(text=redondeo_especial([asoli3.cget("text"), asoli4.cget("text")]))
    asoli11.config(text=redondeo_especial([asoli1.cget("text"), asoli2.cget("text"), mate3.cget("text"), mate4.cget("text")]))

    plas9.config(text=redondeo_especial([plas1.cget("text"), plas2.cget("text")]))
    plas10.config(text=redondeo_especial([plas3.cget("text"), plas4.cget("text")]))
    plas11.config(text=redondeo_especial([plas1.cget("text"), plas2.cget("text"), mate3.cget("text"), mate4.cget("text")]))

    musi9.config(text=redondeo_especial([musi1.cget("text"), musi2.cget("text")]))
    musi10.config(text=redondeo_especial([musi3.cget("text"), musi4.cget("text")]))
    musi11.config(text=redondeo_especial([musi1.cget("text"), musi2.cget("text"), mate3.cget("text"), mate4.cget("text")]))

    tdapren9.config(text=redondeo_especial([tdapren1.cget("text"), tdapren2.cget("text")]))
    tdapren10.config(text=redondeo_especial([tdapren3.cget("text"), tdapren4.cget("text")]))
    tdapren11.config(text=redondeo_especial([tdapren1.cget("text"), tdapren2.cget("text"), mate3.cget("text"), mate4.cget("text")]))

    ing9.config(text=redondeo_especial([ing1.cget("text"), ing2.cget("text")]))
    ing10.config(text=redondeo_especial([ing3.cget("text"), ing4.cget("text")]))
    ing11.config(text=redondeo_especial([ing1.cget("text"), ing2.cget("text"), mate3.cget("text"), mate4.cget("text")]))





root=Tk()
root.title("boletin")
root.resizable(False, False)

frame = Frame()
frame.pack()
frame.config(width="900", height="900")

original_bg = root.cget("bg")

Label(frame, text="boletin: ").grid(row=0, column=0, pady=15)
#materias
Label(frame, text="materias", bg="orange").grid(row=2, column=0, padx=10)

matematica = Label(frame, text=materias[0], bg="orange")
matematica.grid(row=3, column=0)
matematica.bind("<Enter>", on_enter_mate)
matematica.bind("<Leave>", on_leave_mate)

lengua = Label(frame, text=materias[1], bg="orange")
lengua.grid(row=4, column=0)
lengua.bind("<Enter>", on_enter_leng)
lengua.bind("<Leave>", on_leave_leng)

historia = Label(frame, text=materias[2], bg="orange")
historia.grid(row=5, column=0)
historia.bind("<Enter>", on_enter_histo)
historia.bind("<Leave>", on_leave_histo)

geografia = Label(frame, text=materias[3], bg="orange")
geografia.grid(row=6, column=0)
geografia.bind("<Enter>", on_enter_geo)
geografia.bind("<Leave>", on_leave_geo)

naturales = Label(frame, text=materias[4], bg="orange")
naturales.grid(row=7, column=0)
naturales.bind("<Enter>", on_enter_natu)
naturales.bind("<Leave>", on_leave_natu)

informatica = Label(frame, text=materias[5], bg="orange")
informatica.grid(row=8, column=0)
informatica.bind("<Enter>", on_enter_info)
informatica.bind("<Leave>", on_leave_info)

efisica = Label(frame, text=materias[6], bg="orange")
efisica.grid(row=9, column=0)
efisica.bind("<Enter>", on_enter_efisica)
efisica.bind("<Leave>", on_leave_efisica)

asolidaria = Label(frame, text=materias[7], bg="orange")
asolidaria.grid(row=10, column=0)
asolidaria.bind("<Enter>", on_enter_asoli)
asolidaria.bind("<Leave>", on_leave_asoli)

plastica = Label(frame, text=materias[8], bg="orange")
plastica.grid(row=11, column=0)
plastica.bind("<Enter>", on_enter_plas)
plastica.bind("<Leave>", on_leave_plas)

musica = Label(frame, text=materias[9], bg="orange")
musica.grid(row=12, column=0)
musica.bind("<Enter>", on_enter_musi)
musica.bind("<Leave>", on_leave_musi)

tdaprendisaje = Label(frame, text=materias[10], bg="orange")
tdaprendisaje.grid(row=13, column=0)
tdaprendisaje.bind("<Enter>", on_enter_tdaprend)
tdaprendisaje.bind("<Leave>", on_leave_tdaprend)

ingles = Label(frame, text=materias[11], bg="orange")
ingles.grid(row=14, column=0)
ingles.bind("<Enter>", on_enter_ing)
ingles.bind("<Leave>", on_leave_ing)
#1er on_leave_tdaprend
Label(frame, text="1er cuatrimestre: ", bg="light blue").grid(row=1, column=1)
Label(frame, text="P.E. y concepto", bg="light blue").grid(row=2, column=1, padx=10)
Label(frame, text="prueva integradora", bg="light blue").grid(row=2, column=2)
#2do cuatrimestre
Label(frame, text="2do cuatrimestre: ", bg="pink").grid(row=1, column=3,)
Label(frame, text="P.E. y concepto", bg="pink").grid(row=2, column=3, padx=10)
Label(frame, text="prueva integradora", bg="pink").grid(row=2, column=4)
#promedios
Label(frame, text="promedios: ", bg="light green").grid(row=1, column=9)
Label(frame, text="1er cuatrimestre", bg="light green").grid(row=2, column=9)
Label(frame, text="2do cuatrimestre", bg="light green").grid(row=2, column=10)
Label(frame, text="promedio anual(por materia)", bg="light green").grid(row=2, column=11)
Label(frame, text="promedio anual(todas las materias)", bg="light green").grid(row=2, column=12)
#instancias de recuperacion
Label(frame, text="instancias de: ", bg="purple").grid(row=1, column=5)
Label(frame, text="noviembre", bg="purple").grid(row=2, column=5)
Label(frame, text="diciembre", bg="purple").grid(row=2, column=6)
Label(frame, text="febrero", bg="purple").grid(row=2, column=7)
Label(frame, text="marzo", bg="purple").grid(row=2, column=8)
#celdas configurables
mate1 = Label(frame)
mate1.grid(row=3, column=1)
mate2 = Label(frame)
mate2.grid(row=3, column=2)
mate3 = Label(frame)
mate3.grid(row=3, column=3)
mate4 = Label(frame)
mate4.grid(row=3, column=4)
mate5 = Label(frame)
mate5.grid(row=3, column=5)
mate6 = Label(frame)
mate6.grid(row=3, column=6)
mate7 = Label(frame)
mate7.grid(row=3, column=7)
mate8 = Label(frame)
mate8.grid(row=3, column=8)
mate9 = Label(frame)
mate9.grid(row=3, column=9)
mate10 = Label(frame)
mate10.grid(row=3, column=10)
mate11 = Label(frame)
mate11.grid(row=3, column=11)
mate12 = Label(frame)
mate12.grid(row=3, column=12)


leng1 = Label(frame)
leng1.grid(row=4, column=1)
leng2 = Label(frame)
leng2.grid(row=4, column=2)
leng3 = Label(frame)
leng3.grid(row=4, column=3)
leng4 = Label(frame)
leng4.grid(row=4, column=4)
leng5 = Label(frame)
leng5.grid(row=4, column=5)
leng6 = Label(frame)
leng6.grid(row=4, column=6)
leng7 = Label(frame)
leng7.grid(row=4, column=7)
leng8 = Label(frame)
leng8.grid(row=4, column=8)
leng9 = Label(frame)
leng9.grid(row=4, column=9)
leng10 = Label(frame)
leng10.grid(row=4, column=10)
leng11 = Label(frame)
leng11.grid(row=4, column=11)
leng12 = Label(frame)


histo1 = Label(frame)
histo1.grid(row=5, column=1)
histo2 = Label(frame)
histo2.grid(row=5, column=2)
histo3 = Label(frame)
histo3.grid(row=5, column=3)
histo4 = Label(frame)
histo4.grid(row=5, column=4)
histo5 = Label(frame)
histo5.grid(row=5, column=5)
histo6 = Label(frame)
histo6.grid(row=5, column=6)
histo7 = Label(frame)
histo7.grid(row=5, column=7)
histo8 = Label(frame)
histo8.grid(row=5, column=8)
histo9 = Label(frame)
histo9.grid(row=5, column=9)
histo10 = Label(frame)
histo10.grid(row=5, column=10)
histo11 = Label(frame)
histo11.grid(row=5, column=11)
histo12 = Label(frame)
histo12.grid(row=5, column=12)


geo1 = Label(frame)
geo1.grid(row=6, column=1)
geo2 = Label(frame)
geo2.grid(row=6, column=2)
geo3 = Label(frame)
geo3.grid(row=6, column=3)
geo4 = Label(frame)
geo4.grid(row=6, column=4)
geo5 = Label(frame)
geo5.grid(row=6, column=5)
geo6 = Label(frame)
geo6.grid(row=6, column=6)
geo7 = Label(frame)
geo7.grid(row=6, column=7)
geo8 = Label(frame)
geo8.grid(row=6, column=8)
geo9 = Label(frame)
geo9.grid(row=6, column=9)
geo10 = Label(frame)
geo10.grid(row=6, column=10)
geo11 = Label(frame)
geo11.grid(row=6, column=11)
geo12 = Label(frame)
geo12.grid(row=6, column=12)


natu1 = Label(frame)
natu1.grid(row=7, column=1)
natu2 = Label(frame)
natu2.grid(row=7, column=2)
natu3 = Label(frame)
natu3.grid(row=7, column=3)
natu4 = Label(frame)
natu4.grid(row=7, column=4)
natu5 = Label(frame)
natu5.grid(row=7, column=5)
natu6 = Label(frame)
natu6.grid(row=7, column=6)
natu7 = Label(frame)
natu7.grid(row=7, column=7)
natu8 = Label(frame)
natu8.grid(row=7, column=8)
natu9 = Label(frame)
natu9.grid(row=7, column=9)
natu10 = Label(frame)
natu10.grid(row=7, column=10)
natu11 = Label(frame)
natu11.grid(row=7, column=11)
natu12 = Label(frame)
natu12.grid(row=7, column=12)


info1 = Label(frame)
info1.grid(row=8, column=1)
info2 = Label(frame)
info2.grid(row=8, column=2)
info3 = Label(frame)
info3.grid(row=8, column=3)
info4 = Label(frame)
info4.grid(row=8, column=4)
info5 = Label(frame)
info5.grid(row=8, column=5)
info6 = Label(frame)
info6.grid(row=8, column=6)
info7 = Label(frame)
info7.grid(row=8, column=7)
info8 = Label(frame)
info8.grid(row=8, column=8)
info9 = Label(frame)
info9.grid(row=8, column=9)
info10 = Label(frame)
info10.grid(row=8, column=10)
info11 = Label(frame)
info11.grid(row=8, column=11)
info12 = Label(frame)
info12.grid(row=8, column=12)


efisica1 = Label(frame)
efisica1.grid(row=9, column=1)
efisica2 = Label(frame)
efisica2.grid(row=9, column=2)
efisica3 = Label(frame)
efisica3.grid(row=9, column=3)
efisica4 = Label(frame)
efisica4.grid(row=9, column=4)
efisica5 = Label(frame)
efisica5.grid(row=9, column=5)
efisica6 = Label(frame)
efisica6.grid(row=9, column=6)
efisica7 = Label(frame)
efisica7.grid(row=9, column=7)
efisica8 = Label(frame)
efisica8.grid(row=9, column=8)
efisica9 = Label(frame)
efisica9.grid(row=9, column=9)
efisica10 = Label(frame)
efisica10.grid(row=9, column=10)
efisica11 = Label(frame)
efisica11.grid(row=9, column=11)
efisica12 = Label(frame)
efisica12.grid(row=9, column=12)


asoli1 = Label(frame)
asoli1.grid(row=10, column=1)
asoli2 = Label(frame)
asoli2.grid(row=10, column=2)
asoli3 = Label(frame)
asoli3.grid(row=10, column=3)
asoli4 = Label(frame)
asoli4.grid(row=10, column=4)
asoli5 = Label(frame)
asoli5.grid(row=10, column=5)
asoli6 = Label(frame)
asoli6.grid(row=10, column=6)
asoli7 = Label(frame)
asoli7.grid(row=10, column=7)
asoli8 = Label(frame)
asoli8.grid(row=10, column=8)
asoli9 = Label(frame)
asoli9.grid(row=10, column=9)
asoli10 = Label(frame)
asoli10.grid(row=10, column=10)
asoli11 = Label(frame)
asoli11.grid(row=10, column=11)
asoli12 = Label(frame)
asoli12.grid(row=10, column=12)


plas1 = Label(frame)
plas1.grid(row=11, column=1)
plas2 = Label(frame)
plas2.grid(row=11, column=2)
plas3 = Label(frame)
plas3.grid(row=11, column=3)
plas4 = Label(frame)
plas4.grid(row=11, column=4)
plas5 = Label(frame)
plas5.grid(row=11, column=5)
plas6 = Label(frame)
plas6.grid(row=11, column=6)
plas7 = Label(frame)
plas7.grid(row=11, column=7)
plas8 = Label(frame)
plas8.grid(row=11, column=8)
plas9 = Label(frame)
plas9.grid(row=11, column=9)
plas10 = Label(frame)
plas10.grid(row=11, column=10)
plas11 = Label(frame)
plas11.grid(row=11, column=11)
plas12 = Label(frame)
plas12.grid(row=11, column=12)


musi1 = Label(frame)
musi1.grid(row=12, column=1)
musi2 = Label(frame)
musi2.grid(row=12, column=2)
musi3 = Label(frame)
musi3.grid(row=12, column=3)
musi4 = Label(frame)
musi4.grid(row=12, column=4)
musi5 = Label(frame)
musi5.grid(row=12, column=5)
musi6 = Label(frame)
musi6.grid(row=12, column=6)
musi7 = Label(frame)
musi7.grid(row=12, column=7)
musi8 = Label(frame)
musi8.grid(row=12, column=8)
musi9 = Label(frame)
musi9.grid(row=12, column=9)
musi10 = Label(frame)
musi10.grid(row=12, column=10)
musi11 = Label(frame)
musi11.grid(row=12, column=11)
musi12 = Label(frame)
musi12.grid(row=12, column=12)


tdapren1 = Label(frame)
tdapren1.grid(row=13, column=1)
tdapren2 = Label(frame)
tdapren2.grid(row=13, column=2)
tdapren3 = Label(frame)
tdapren3.grid(row=13, column=3)
tdapren4 = Label(frame)
tdapren4.grid(row=13, column=4)
tdapren5 = Label(frame)
tdapren5.grid(row=13, column=5)
tdapren6 = Label(frame)
tdapren6.grid(row=13, column=6)
tdapren7 = Label(frame)
tdapren7.grid(row=13, column=7)
tdapren8 = Label(frame)
tdapren8.grid(row=13, column=8)
tdapren9 = Label(frame)
tdapren9.grid(row=13, column=9)
tdapren10 = Label(frame)
tdapren10.grid(row=13, column=10)
tdapren11 = Label(frame)
tdapren11.grid(row=13, column=11)
tdapren12 = Label(frame)
tdapren12.grid(row=13, column=12)


ing1 = Label(frame)
ing1.grid(row=14, column=1)
ing2 = Label(frame)
ing2.grid(row=14, column=2)
ing3 = Label(frame)
ing3.grid(row=14, column=3)
ing4 = Label(frame)
ing4.grid(row=14, column=4)
ing5 = Label(frame)
ing5.grid(row=14, column=5)
ing6 = Label(frame)
ing6.grid(row=14, column=6)
ing7 = Label(frame)
ing7.grid(row=14, column=7)
ing8 = Label(frame)
ing8.grid(row=14, column=8)
ing9 = Label(frame)
ing9.grid(row=14, column=9)
ing10 = Label(frame)
ing10.grid(row=14, column=10)
ing11 = Label(frame)
ing11.grid(row=14, column=11)
ing12 = Label(frame)
ing12.grid(row=14, column=12)


#configurar celdas
obtener_nota = Entry()
obtener_nota.place(x=290, y=365)
obtener_nota.config(width=4)

valor1 = StringVar()
valor1.set(instancias[0])
elegir_instancia = OptionMenu(frame, valor1,*instancias)
elegir_instancia.grid(row=16, column=3)

valor2 = StringVar()
valor2.set(materias[0])
elegir_materia = OptionMenu(frame, valor2,*materias)
elegir_materia.grid(row=16, column=4)



poner_nota =  Button(frame, text="poner nota")
poner_nota.grid(row=16, column=5, pady=15)
poner_nota.config(command=lambda: button_function())
#abrir datos
datos = recuperar_datos("celdas.txt")

try:
    mate1.config(text=datos[0])
except:
    pass
try:
    mate2.config(text=datos[1])
except:
    pass
try:
    mate3.config(text=datos[2])
except:
    pass
try:
    mate4.config(text=datos[3])
except:
    pass
try:
    mate5.config(text=datos[4])
except:
    pass
try:
    mate6.config(text=datos[5])
except:
    pass
try:
    mate7.config(text=datos[6])
except:
    pass
try:
    mate8.config(text=datos[7])
except:
    pass
try:
    mate9.config(text=datos[8])
except:
    pass
try:
    mate10.config(text=datos[9])
except:
    pass
try:
    mate11.config(text=datos[10])
except:
    pass
try:
    mate12.config(text=datos[11])
except:
    pass

try:
    leng1.config(text=datos[12])
except:
    pass
try:
    leng2.config(text=datos[13])
except:
    pass
try:
    leng3.config(text=datos[14])
except:
    pass
try:
    leng4.config(text=datos[15])
except:
    pass
try:
    leng5.config(text=datos[16])
except:
    pass
try:
    leng6.config(text=datos[17])
except:
    pass
try:
    leng7.config(text=datos[18])
except:
    pass
try:
    leng8.config(text=datos[19])
except:
    pass
try:
    leng9.config(text=datos[20])
except:
    pass
try:
    leng10.config(text=datos[21])
except:
    pass
try:
    leng11.config(text=datos[22])
except:
    pass
try:
    leng12.config(text=datos[23])
except:
    pass

try:
    histo1.config(text=datos[24])
except:
    pass
try:
    histo2.config(text=datos[25])
except:
    pass
try:
    histo3.config(text=datos[26])
except:
    pass
try:
    histo4.config(text=datos[27])
except:
    pass
try:
    histo5.config(text=datos[28])
except:
    pass
try:
    histo6.config(text=datos[29])
except:
    pass
try:
    histo7.config(text=datos[30])
except:
    pass
try:
    histo8.config(text=datos[31])
except:
    pass
try:
    histo9.config(text=datos[32])
except:
    pass
try:
    histo10.config(text=datos[33])
except:
    pass
try:
    histo11.config(text=datos[34])
except:
    pass
try:
    histo12.config(text=datos[35])
except:
    pass

try:
    geo1.config(text=datos[36])
except:
    pass
try:
    geo2.config(text=datos[37])
except:
    pass
try:
    geo3.config(text=datos[38])
except:
    pass
try:
    geo4.config(text=datos[39])
except:
    pass
try:
    geo5.config(text=datos[40])
except:
    pass
try:
    geo6.config(text=datos[41])
except:
    pass
try:
    geo7.config(text=datos[42])
except:
    pass
try:
    geo8.config(text=datos[43])
except:
    pass
try:
    geo9.config(text=datos[44])
except:
    pass
try:
    geo10.config(text=datos[45])
except:
    pass
try:
    geo11.config(text=datos[46])
except:
    pass
try:
    geo12.config(text=datos[47])
except:
    pass

try:
    natu1.config(text=datos[48])
except:
    pass
try:
    natu2.config(text=datos[49])
except:
    pass
try:
    natu3.config(text=datos[50])
except:
    pass
try:
    natu4.config(text=datos[51])
except:
    pass
try:
    natu5.config(text=datos[52])
except:
    pass
try:
    natu6.config(text=datos[53])
except:
    pass
try:
    natu7.config(text=datos[54])
except:
    pass
try:
    natu8.config(text=datos[55])
except:
    pass
try:
    natu9.config(text=datos[56])
except:
    pass
try:
    natu10.config(text=datos[57])
except:
    pass
try:
    natu11.config(text=datos[58])
except:
    pass
try:
    natu12.config(text=datos[59])
except:
    pass

try:
    info1.config(text=datos[60])
except:
    pass
try:
    info2.config(text=datos[61])
except:
    pass
try:
    info3.config(text=datos[62])
except:
    pass
try:
    info4.config(text=datos[63])
except:
    pass
try:
    info5.config(text=datos[64])
except:
    pass
try:
    info6.config(text=datos[65])
except:
    pass
try:
    info7.config(text=datos[66])
except:
    pass
try:
    info8.config(text=datos[67])
except:
    pass
try:
    info9.config(text=datos[68])
except:
    pass
try:
    info10.config(text=datos[69])
except:
    pass
try:
    info11.config(text=datos[70])
except:
    pass
try:
    info12.config(text=datos[71])
except:
    pass

try:
    efisica1.config(text=datos[72])
except:
    pass
try:
    efisica2.config(text=datos[73])
except:
    pass
try:
    efisica3.config(text=datos[74])
except:
    pass
try:
    efisica4.config(text=datos[75])
except:
    pass
try:
    efisica5.config(text=datos[76])
except:
    pass
try:
    efisica6.config(text=datos[77])
except:
    pass
try:
    efisica7.config(text=datos[78])
except:
    pass
try:
    efisica8.config(text=datos[79])
except:
    pass
try:
    efisica9.config(text=datos[80])
except:
    pass
try:
    efisica10.config(text=datos[81])
except:
    pass
try:
    efisica11.config(text=datos[82])
except:
    pass
try:
    efisica12.config(text=datos[83])
except:
    pass

try:
    asoli1.config(text=datos[84])
except:
    pass
try:
    asoli2.config(text=datos[85])
except:
    pass
try:
    asoli3.config(text=datos[86])
except:
    pass
try:
    asoli4.config(text=datos[87])
except:
    pass
try:
    asoli5.config(text=datos[88])
except:
    pass
try:
    asoli6.config(text=datos[89])
except:
    pass
try:
    asoli7.config(text=datos[90])
except:
    pass
try:
    asoli8.config(text=datos[91])
except:
    pass
try:
    asoli9.config(text=datos[92])
except:
    pass
try:
    asoli10.config(text=datos[93])
except:
    pass
try:
    asoli11.config(text=datos[94])
except:
    pass
try:
    asoli12.config(text=datos[95])
except:
    pass

try:
    plas1.config(text=datos[96])
except:
    pass
try:
    plas2.config(text=datos[97])
except:
    pass
try:
    plas3.config(text=datos[98])
except:
    pass
try:
    plas4.config(text=datos[99])
except:
    pass
try:
    plas5.config(text=datos[100])
except:
    pass
try:
    plas6.config(text=datos[101])
except:
    pass
try:
    plas7.config(text=datos[102])
except:
    pass
try:
    plas8.config(text=datos[103])
except:
    pass
try:
    plas9.config(text=datos[104])
except:
    pass
try:
    plas10.config(text=datos[105])
except:
    pass
try:
    plas11.config(text=datos[106])
except:
    pass
try:
    plas12.config(text=datos[107])
except:
    pass

try:
    musi1.config(text=datos[108])
except:
    pass
try:
    musi2.config(text=datos[109])
except:
    pass
try:
    musi3.config(text=datos[110])
except:
    pass
try:
    musi4.config(text=datos[111])
except:
    pass
try:
    musi5.config(text=datos[112])
except:
    pass
try:
    musi6.config(text=datos[113])
except:
    pass
try:
    musi7.config(text=datos[114])
except:
    pass
try:
    musi8.config(text=datos[115])
except:
    pass
try:
    musi9.config(text=datos[116])
except:
    pass
try:
    musi10.config(text=datos[117])
except:
    pass
try:
    musi11.config(text=datos[118])
except:
    pass
try:
    musi12.config(text=datos[119])
except:
    pass

try:
    tdapren1.config(text=datos[120])
except:
    pass
try:
    tdapren2.config(text=datos[121])
except:
    pass
try:
    tdapren3.config(text=datos[122])
except:
    pass
try:
    tdapren4.config(text=datos[123])
except:
    pass
try:
    tdapren5.config(text=datos[124])
except:
    pass
try:
    tdapren6.config(text=datos[125])
except:
    pass
try:
    tdapren7.config(text=datos[126])
except:
    pass
try:
    tdapren8.config(text=datos[127])
except:
    pass
try:
    tdapren9.config(text=datos[128])
except:
    pass
try:
    tdapren10.config(text=datos[129])
except:
    pass
try:
    tdapren11.config(text=datos[130])
except:
    pass
try:
    tdapren12.config(text=datos[131])
except:
    pass

try:
    ing1.config(text=datos[132])
except:
    pass
try:
    ing2.config(text=datos[133])
except:
    pass
try:
    ing3.config(text=datos[134])
except:
    pass
try:
    ing4.config(text=datos[135])
except:
    pass
try:
    ing5.config(text=datos[136])
except:
    pass
try:
    ing6.config(text=datos[137])
except:
    pass
try:
    ing7.config(text=datos[138])
except:
    pass
try:
    ing8.config(text=datos[139])
except:
    pass
try:
    ing9.config(text=datos[140])
except:
    pass
try:
    ing10.config(text=datos[141])
except:
    pass
try:
    ing11.config(text=datos[142])
except:
    pass
try:
    ing12.config(text=datos[143])
except:
    pass



#guardar datos
root.protocol("WM_DELETE_WINDOW", on_closing)

#promedio de cuatrimestre
promedio_cuatrimestre_1 = Label(frame, text="promedio del primer cuatrimestre: " + periodico(promediar_cuatrimestre(1)))
promedio_cuatrimestre_1.grid(row=16, column=9)

promedio_cuatrimestre_2 = Label(frame, text="promedio del segundo cuatrimestre: " + periodico(promediar_cuatrimestre(2)))
promedio_cuatrimestre_2.grid(row=17, column=9)

root.mainloop()