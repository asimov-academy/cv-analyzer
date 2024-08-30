import uuid
from models.job import Job
from database import AnalyzeDatabase

database = AnalyzeDatabase()

name = 'Vaga de Gestor Comercial de B2B'

activities = '''
Gerenciar o time Comercial
Desenhar estratégias de B2B para escalar o faturamento
Definir e acompanhar metas do B2B com o time
Acompanhar e ajudar o time a executar as estratégias definidas
Reportar resultados e projeções dos seus KPIs
'''

prequisites = '''
Experiência comprovada como Gestor de Vendas, Líder Comercial, Diretor Comercial ou afins
Experiência comprovada em Vendas B2B (business to business)
Experiência em empresas de Infoprodutos
Proatividade e curiosidade, buscando constantemente aprender e melhorar as habilidades.
Foco em bater as metas estabelecidas para o time de Vendas
Disponibilidade para trabalho em período integral (full time)
'''

differentials = '''
Conhecimento da metodologia VTSD (Leandro Ladeira)
Conhecimento avançado de Funis de Venda, com uma abordagem estratégica e eficaz na aquisição e retenção de clientes
Interesse por Programação e Tecnologia (fique tranquilo, NÃO é necessário saber programar)
Experiência como Gestor Comercial no nicho de Tecnologia em geral, Programação ou Data Science, proporcionando uma compreensão mais profunda do nosso público-alvo
'''

job = Job(
    id=str(uuid.uuid4()),
    name=name,
    main_activities=activities,
    prerequisites=prequisites,
    differentials=differentials,
)

database.jobs.insert(job.model_dump())