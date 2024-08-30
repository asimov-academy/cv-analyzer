import uuid
from helper import get_pdf_paths, read_uploaded_file, extract_data_analysis
from database import AnalyzeDatabase
from ai import GroqClient
from models.resum import Resum
from models.file import File

# Inicializar a conexão com o banco de dados de análise
database = AnalyzeDatabase()

# Obter a vaga de emprego a partir do banco de dados
# Buscar pela vaga de 'Gestor Comercial de B2B'
job = database.get_job_by_name('Vaga de Gestor Comercial de B2B')

# Inicializar o cliente de IA para processar os currículos
ai = GroqClient()

# Obter os caminhos dos arquivos PDF contendo os currículos
# Esta função retorna uma lista de caminhos de arquivos dentro da pasta 'curriculos'
cv_paths = get_pdf_paths('curriculos')

# Iterar sobre cada caminho de arquivo de currículo na lista
for path in cv_paths:
    # Ler o conteúdo do arquivo PDF de currículo
    content = read_uploaded_file(path)
    
    # Usar o modelo de IA para resumir o conteúdo do currículo
    resum = ai.resume_cv(content)
    print(resum)  # Exibir o resumo gerado para o usuário
    
    # Gerar uma opinião sobre o currículo com base na vaga de emprego
    opnion = ai.generate_opnion(content, job)
    print(opnion)  # Exibir a opinião gerada para o usuário
    
    # Calcular uma pontuação para o currículo com base no resumo e nos requisitos da vaga
    score = ai.generate_score(resum, job)
    print(score)  # Exibir a pontuação gerada para o usuário
    
    # Criar uma instância do schema Resum para armazenar os dados do resumo
    resum_schema = Resum(
        id=str(uuid.uuid4()),  # Gerar um UUID único para o ID do resumo
        job_id=job.get('id'),  # Associar o ID da vaga ao resumo
        content=resum,  # Armazenar o conteúdo do resumo
        file=str(path),  # Armazenar o caminho do arquivo de currículo
        opnion=opnion  # Armazenar a opinião gerada
    )
    
    # Criar uma instância do schema File para armazenar os dados do arquivo
    file = File(
        file_id=str(uuid.uuid4()),  # Gerar um UUID único para o ID do arquivo
        job_id=job.get('id')  # Associar o ID da vaga ao arquivo
    )
    
    # Extrair a análise dos dados utilizando o resumo e informações adicionais
    analysis = extract_data_analysis(resum, resum_schema.job_id, resum_schema.id, score)
    
    # Inserir os dados gerados no banco de dados
    # Inserir o resumo no banco de dados
    database.resums.insert(resum_schema.model_dump())
    # Inserir a análise no banco de dados
    database.analysis.insert(analysis.model_dump())
    # Inserir os dados do arquivo no banco de dados
    database.files.insert(file.model_dump())
