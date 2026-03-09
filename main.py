import streamlit as st
from datetime import datetime
import base64

# Configuro a página
st.set_page_config(
    page_title="Semáforo de Evasão",
    page_icon="📚",
    layout="wide"
)

# Crio uma variável para pegar a data dinamicamente
data_atual = datetime.now().strftime("%d/%m/%Y")

# Crio o estilo do CSS da página
cor_azul = "#0056b3"

st.markdown(f"""
    <style>
   
    [data-testid="stSidebar"] {{ background-color: {cor_azul}; }}
    [data-testid="stSidebar"] * {{ color: white !important; }}
    .main-header {{
        background-color: {cor_azul};
        color: white;
        padding: 2rem;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 2rem;
    }}


    .section-card {{
        background-color: #fcfdfd;
        padding: 20px;
        border-radius: 5px;
        border-left: 5px solid #004d40; 
        box-shadow: 2px 2px 5px rgba(0,0,0,0.05);
        margin-bottom: 20px;
        color: #333 !important; 
    }}
    
    .metric-card {{
        background-color: white;
        border: 1px solid #e6e6e6;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 10px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.03);
    }}
    </style>
    """, unsafe_allow_html=True)

# Crio a Sidebar
with st.sidebar:
    
    url_imagem = "https://cdn-icons-png.flaticon.com/512/3429/3429149.png" 
    
    st.image(url_imagem, width=200)
    

    st.title("Menu de Navegação")
    
    selecao = st.radio("Ir para:", ["Painel Geral", "Semáforo"])
    
    st.divider()
    
    st.markdown(f"""
        <div class="texto-suave">
            <p><b>📅 Atualização:</b> {data_atual}</p>
            <p>O painel apresenta análise dos dados disponibilizados pelo SED, utilizando estatística básica e visualização interativa no Power BI para apoio à tomadas de decisão acadêmicas.</p>
            <p>Os dados foram anonimizados para atender normas da LGPD e não publicar dados sensíveis dos alunos.</p>
            <p>Atividades Extensionistas II - UNINTER</p>
            <p><b>Analista:</b> Letícia Guedes Vieira | <b>RU:</b> 5219222</p>
        </div>
    """, unsafe_allow_html=True)

# Crio a seção de conteúdo da página
if selecao == "Painel Geral":
    st.markdown(f'<div class="main-header"><h1>Semáforo de Evasão: Painel de Monitoramento de Desempenho de Alunos</h1><p>Análise de Dados dos Alunos, com base no SED em Sorocaba/SP</p></div>', unsafe_allow_html=True)
    st.subheader("Informações Gerais para a Análise")

    
    st.markdown("""
        <div class="section-card">
            <b>Frequência:</b> O número de faltas dos alunos dentro do semestre.<br>
            <b>Notas:</b> O desempenho dos alunos nas disciplinas dentro do semestre.<br>
            <b>Anos Anteriores:</b> Foram realizadas análises dos alunos, considerando se houve ou não reprova(s).<br>
            <b>Disciplinas:</b> Foram separadas nas 4 áreas de conhecimento do novo Ensino Médio: Linguagens, Matemática, Ciências Humanas e Ciências da Natureza.<br>
            <b>Graduação:</b> Foram analisados os alunos do Ensino Médio.<br>
            <b>Semafóro:</b> A elaboração do semáforo foi definida seguindo um critério de pontuação, ou seja, de acordo com métricas críticas (como reprova ou alto índice de faltas) o aluno pontua (negativamente) e acende o alerta do semáforo.
        </div>
        """, unsafe_allow_html=True)

    # Crio os cards informativos
    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(f"""
            <div class="metric-card" style="border-left: 5px solid #634198;">
                <p style="color: #666; margin: 0; font-size: 0.9rem;">Total de Alunos</p>
                <h2 style="color: #333; margin: 0;">47</h2>
            </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown(f"""
            <div class="metric-card" style="border-left: 5px solid #333;">
                <p style="color: #666; margin: 0; font-size: 0.9rem;">Turmas Analisadas</p>
                <h2 style="color: #333; margin: 0;">1</h2>
            </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown(f"""
            <div class="metric-card" style="border-left: 5px solid #1c3d5a;">
                <p style="color: #666; margin: 0; font-size: 0.9rem;">Série</p>
                <h2 style="color: #333; margin: 0;">3º Ano</h2>
            </div>
        """, unsafe_allow_html=True)
        

elif selecao == "Semáforo":
    st.markdown(f'<div class="main-header"><h1>Semáforo de Evasão: Painel de Monitoramento de Desempenho de Alunos</h1><p>Análise de Dados dos Alunos, com base no SED em Sorocaba/SP</p></div>', unsafe_allow_html=True)
    st.subheader(f"Visão Consolidada | {data_atual}")
    #st.title("Semáforo de Evasão")
    link_power_bi = "https://app.powerbi.com/view?r=eyJrIjoiOWQxNGU1M2MtZTBjZi00YTkzLTk1YTUtMWE5ZWQ2ZTQ4ZTM3IiwidCI6ImMwMTVkYjY0LWY5ZDctNGYwNi04Njc2LWI2YjcxZDVkMmY4MSJ9"
    st.components.v1.iframe(link_power_bi, height=800)