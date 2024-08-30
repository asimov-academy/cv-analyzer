from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google.oauth2.credentials import Credentials

# Escopo de acesso
SCOPES = ["https://www.googleapis.com/auth/drive.readonly"]

# Carregar credenciais do arquivo token.json
creds = Credentials.from_authorized_user_file('token.json', SCOPES)

# Construa o serviço da API Google Drive
service = build('drive', 'v3', credentials=creds)

# ID da pasta que você deseja listar os arquivos
folder_id = '1flYfkoDOelDkKuRYrOOtJUTq0hAKsyo1'

# Listar arquivos na pasta especificada pelo folder_id
results = service.files().list(
    q=f"'{folder_id}' in parents", fields="files(id, name)"
).execute()

# Obter a lista de arquivos
files = results.get('files', [])

if not files:
    raise FileNotFoundError('No files found.')
else:
    print('Files:')
    for file in files:
        print(f"{file['name']} ({file['id']})")

        # Download de cada arquivo no drive
        request = service.files().get_media(fileId=file['id'])
        file_path = f"./curriculos/{file['name']}"  # Define o caminho de onde salvar o arquivo
        with open(file_path, 'wb') as f:
            downloader = MediaIoBaseDownload(f, request)
            done = False
            while not done:
                status, done = downloader.next_chunk()
                print(f"Download {int(status.progress() * 100)}%.")
