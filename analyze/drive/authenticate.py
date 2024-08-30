import os.path
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# Defina o escopo de acesso que você precisa
# Estes escopos permitem ler e modificar arquivos no Google Drive
SCOPES = [
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive.readonly",
    "https://www.googleapis.com/auth/drive.metadata.readonly"
]

# Inicialize a variável de credenciais
creds = None

# Verifica se o arquivo token.json existe no diretório atual
# Este arquivo armazena as credenciais de acesso
if os.path.exists('token.json'):
    # Se existir, carrega as credenciais a partir do arquivo token.json
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    print('Credenciais carregadas do arquivo token.json.')

# Verifica se as credenciais não existem ou são inválidas/expiradas
if not creds or not creds.valid:
    # Se as credenciais existirem mas estiverem expiradas e puderem ser renovadas
    if creds and creds.expired and creds.refresh_token:
        # Renova as credenciais usando o refresh token
        creds.refresh(Request())
        print('Credenciais renovadas com sucesso.')
    else:
        # Se não houver credenciais válidas, inicia o fluxo de autorização do OAuth
        print('Iniciando o fluxo de autorização do OAuth...')
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)  # Executa o servidor local para autorização
        print('Autorização concluída.')

    # Salva as credenciais renovadas ou novas no arquivo token.json
    with open('token.json', 'w') as token:
        token.write(creds.to_json())
        print('Credenciais salvas no arquivo token.json.')

