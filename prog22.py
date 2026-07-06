codigo=input("digete o codigo")
match dia:
    case "200"
        print:("sucesso! tudo certo com a sua requisição.")
    case "400"
        print("erro do clinte: requisição malformada.")
    case "401" | "403"
        print("erro de permissão:você não tem acesso a esta página.")
    case "404"
        print("erro pagina não encontrada")
    case "500|503"
        print ("erro no servidor. nosso sistema esta invalido no momento")
    case _:
        print ("codigo de erro não reconhecido")
        
