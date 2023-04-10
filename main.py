import openai
import config
import typer
from rich import print 
from rich.table import Table


def main():
    openai.api_key = config.api_key
    
    #Inicializamos chatGPT
    context= {"role":"system","content": "Hola mundo"}
    messages=[context]

    print("💬 [bold green]ChatGPT API en Python[/bold green]")

    table = Table("Comando", "Descripción")
    table.add_row("exit", "Salir de la aplicación")
    table.add_row("new", "Crear una nueva conversación")

    print(table)

    while True:
        content = __prompt()

        #Se guardan Mensajes usuario
        messages.append({"role": "user", "content": content})



        if content == "new":
            print("🆕 Nueva conversación creada")
            messages = [context]
            content = __prompt()

        response =openai.ChatCompletion.create(model="gpt-3.5-turbo-0301", 
                                    messages=messages)
        #Se guarda Respuestas de ChatGPt
        messages.append({"role": "assistant", "content": response})


        print(response.choices[0].message.content)


def __prompt() -> str:
    prompt = typer.prompt("\n¿Sobre qué quieres hablar? ")

    if prompt == "exit":
        exit = typer.confirm("✋ ¿Estás seguro?")
        if exit:
            print("👋 ¡Hasta luego!")
            raise typer.Abort()

        return __prompt()

    return prompt
if __name__ == "__main__":
    typer.run(main)