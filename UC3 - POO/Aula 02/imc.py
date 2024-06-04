import dearpygui.dearpygui as xd

# ou print(f"{imc * 10000}")

xd.create_context()

def calculo_de_imc():
    altura = xd.get_value("altura")
    peso = xd.get_value("peso")

    try:
        altura = float(altura) 
        peso = float(peso)
        imc = peso / (altura ** 2)
        xd.set_value("resultado", f"O seu IMC é {imc}")

    except ValueError:
        xd.set_value("resultado", "Valor errado, tente de novo!")

xd.create_viewport(title = "Calculadora de IMC", width=600, height=300)

with xd.window(label = "Inserção de dados", width=600, height=300):
    xd.add_input_text(label = "Altura", tag="altura")
    xd.add_input_text(label = "Peso", tag="peso")
    xd.add_button(label ="Calcular IMC", callback = calculo_de_imc)
    xd.add_text("", tag = "resultado")

xd.setup_dearpygui()
xd.show_viewport()
xd.start_dearpygui()
xd.destroy_context()







