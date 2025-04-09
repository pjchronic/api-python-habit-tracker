

def create_user(data):
    if not data.get('name') or not data.get('email'):
        raise Exception('Nome ou Email não consta')
    else:
        return {"message": "Usuário criado com sucesso"}
