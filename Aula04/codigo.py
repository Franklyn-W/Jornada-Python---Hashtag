""" 
    Botao de iniciar o chat
    pop-up para entrar no chat
    Quando entrar no chat:
        notificar a entrada ao demais
        O campo e o botao de enviar mensagens
    A cada mensagem enviada:
        Nome: Texto da mensagem
"""



import flet as ft

def main(pagina):
    titulo = ft.Text("Zapilson")
    
    chat = ft.Column()
    
    nome_usuario = ft.TextField(label="Escreva seu nome")
    
    def enviar_mensagem_tunel(mensagem):
        tipo = mensagem["tipo"]
        
        if tipo == "mensagem":
            usuario_mensagem = mensagem["usuario"]
            texto_mensagem = mensagem["texto"]
            
            chat.controls.append(ft.Text(f"{usuario_mensagem}: {texto_mensagem}")) # Copiar mensagem digitada para o campo de chat
        else:
            usuario_mensagem = mensagem["usuario"]
            chat.controls.append(ft.Text(
                f"{usuario_mensagem} entrou no chat",
                size = 12, 
                italic = True,
                color = ft.colors.GREEN_ACCENT
                ))
        pagina.update()
    
    pagina.pubsub.subscribe(enviar_mensagem_tunel)
    
    def enviar_mensagem(evento):
        pagina.pubsub.send_all({
            "texto" : campo_mensagem.value,
            "usuario" : nome_usuario.value,
            "tipo" : "mensagem"
            })
        campo_mensagem.value = "" # Limpar o campo de mensagem digitada
        pagina.update()
    
    campo_mensagem = ft.TextField(label="Digite uma mensagem", on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    
    def entrar_popup(evento):
        pagina.pubsub.send_all({"usuario" : nome_usuario.value, "tipo" : "entrada"})
        popup.open = False # Fechar o popup
        pagina.remove(botao_iniciar) # Remover o botao de entrar
        pagina.remove(titulo) # Remover nome do aplicativo
        pagina.add(chat) # Inserir campo com mensagens
        pagina.add(ft.Row(
            [campo_mensagem, botao_enviar]
            )) # Adicionando campo de mensagem e botao na mesma linha
        pagina.update() # Atualizar pagina com as alterações
    
    popup = ft.AlertDialog(
        open = False, 
        modal = True, 
        title = ft.Text("Bem vindo ao Zapilson"),
        content = nome_usuario,
        actions = [ft.ElevatedButton("Entrar", on_click=entrar_popup)],
        )
    
    def entrar_chat(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()
    
    botao_iniciar = ft.ElevatedButton(
        "Iniciar chat",
        on_click = entrar_chat
        )
    
    
    pagina.add(titulo)
    pagina.add(botao_iniciar)

porta_acesso = 65535 # Definir a porta de acesso
ft.app(target=main, view= ft.WEB_BROWSER, port= porta_acesso)  # type: ignore