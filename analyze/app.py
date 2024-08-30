import os
import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode
from database import AnalyzeDatabase

# Inicializa a base de dados
database = AnalyzeDatabase()

# Configura a página do Streamlit com layout largo e título "Recrutador"
st.set_page_config(layout="wide", page_title="Recrutador", page_icon=":brain:")

# Cria um menu de seleção para escolher uma vaga disponível na base de dados
option = st.selectbox(
    "Escolha sua vaga:",
    [job.get('name') for job in database.jobs.all()],
    index=None
)

# Inicializa a variável `data`
data = None

# Verifica se uma vaga foi selecionada
if option:
    # Obtém as informações da vaga selecionada pelo nome
    job = database.get_job_by_name(option)
    
    # Obtém as análises relacionadas à vaga selecionada
    data = database.get_analysis_by_job_id(job.get('id'))

    # Cria um DataFrame do Pandas para armazenar os dados das análises
    df = pd.DataFrame(
        data if data else {},
        columns=[
            'name',
            'education',
            'skills',
            'languages',
            'score',
            'resum_id',
            'id'
        ]
    )

    # Renomeia as colunas para melhorar a legibilidade
    df.rename(
        columns={
            'name': 'Nome',
            'education': 'Educação',
            'skills': 'Habilidades',
            'languages': 'Idiomas',
            'score': 'Score',
            'resum_id': 'Resum ID',
            'id': 'ID'
        },
        inplace=True
    )

    # Configura a tabela interativa usando GridOptionsBuilder
    gb = GridOptionsBuilder.from_dataframe(df)
    gb.configure_pagination(paginationAutoPageSize=True)  # Habilita paginação automática

    # Configura a ordenação e seleção, se houver dados
    if data:
        gb.configure_column("Score", header_name="Score", sort="desc")  # Ordena pela coluna 'Score'
        gb.configure_selection(selection_mode="multiple", use_checkbox=True)  # Adiciona seleção com checkboxes

    # Constrói as opções de grid
    grid_options = gb.build()

    # Exibe um gráfico de barras com as pontuações dos candidatos
    st.subheader('Classificação dos Candidatos')
    st.bar_chart(df, x="Nome", y="Score", color="Nome", horizontal=True)

    # Exibe a tabela interativa usando AgGrid
    response = AgGrid(
        df,
        gridOptions=grid_options,
        enable_enterprise_modules=True,
        update_mode=GridUpdateMode.SELECTION_CHANGED,
        theme='streamlit',
    )

    # Obtém os candidatos selecionados na tabela
    selected_candidates = response.get('selected_rows', [])
    candidates_df = pd.DataFrame(selected_candidates)

    # Obtém os currículos relacionados à vaga
    resums = database.get_resums_by_job_id(job.get('id'))

    # Função para deletar os arquivos dos currículos
    def delete_files_resum(resums):
        for resum in resums:
            path = resum.get('file')
            if os.path.isfile(path):
                os.remove(path)

    # Botão para limpar as análises e deletar os currículos
    if st.button('Limpar Análise'):
        database.delete_all_resums_by_job_id(job.get('id'))  # Deleta todos os currículos
        database.delete_all_analysis_by_job_id(job.get('id'))  # Deleta todas as análises
        database.delete_all_files_by_job_id(job.get('id')) # Deleta todos os arquivos
        delete_files_resum(resums)  # Deleta os arquivos dos currículos
        st.rerun()  # Recarrega a página

    # Exibe os currículos dos candidatos selecionados
    if not candidates_df.empty:
        cols = st.columns(len(candidates_df))  # Cria colunas para exibir os currículos
        for idx, row in enumerate(candidates_df.iterrows()):
            with cols[idx]:  # Exibe cada currículo em uma coluna
                with st.container():
                    if resum_data := database.get_resum_by_id(row[1]['Resum ID']):
                        st.markdown(resum_data.get('content')) # Exibe o resumo do currículo
                        st.markdown(resum_data.get('opnion')) # Exibe a opnião da IA sobre o curriculo

                        # Exibe um botão para download do currículo em PDF
                        with open(resum_data.get('file'), "rb") as pdf_file:
                            pdf_data = pdf_file.read()
                            st.download_button(
                                label=f"Download Currículo {row[1]['Nome']}",
                                data=pdf_data,
                                file_name=f"{row[1]['Nome']}.pdf",
                                mime="application/pdf"
                            )
