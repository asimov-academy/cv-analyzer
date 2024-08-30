from tinydb import TinyDB, Query

class AnalyzeDatabase(TinyDB):
    def __init__(self, file_path='db.json') -> None:
        # Inicializar o banco de dados TinyDB com o arquivo especificado
        # Criar tabelas para armazenar vagas, resumos de currículos, análises e arquivos
        super().__init__(file_path)
        self.jobs = self.table('jobs')
        self.resums = self.table('resums')
        self.analysis = self.table('analysis')
        self.files = self.table('files')

    def get_job_by_name(self, name):
        # Buscar uma vaga pelo nome no banco de dados e retornar o primeiro resultado encontrado
        job = Query()
        result = self.jobs.search(job.name == name)
        return result[0] if result else None
    
    def get_resum_by_id(self, id):
        # Buscar um resumo de currículo específico pelo ID do resumo
        resum = Query()
        result = self.resums.search(resum.id == id)
        return result[0] if result else None

    def get_analysis_by_job_id(self, job_id):
        # Buscar todas as análises associadas a um ID de vaga específico
        analysis = Query()
        result = self.analysis.search(analysis.job_id == job_id)
        return result

    def get_resums_by_job_id(self, job_id):
        # Buscar todos os resumos de currículos associados a um ID de vaga específico
        resum = Query()
        result = self.resums.search(resum.job_id == job_id)
        return result

    def delete_all_resums_by_job_id(self, job_id):
        # Remover todos os resumos de currículos associados a um ID de vaga específico
        resum = Query()
        self.resums.remove(resum.job_id == job_id)

    def delete_all_analysis_by_job_id(self, job_id):
        # Remover todas as análises associadas a um ID de vaga específico
        analysis = Query()
        self.analysis.remove(analysis.job_id == job_id)

    def delete_all_files_by_job_id(self, job_id):
        # Remover todas as análises associadas a um ID de vaga específico
        file = Query()
        self.analysis.remove(file.job_id == job_id)

