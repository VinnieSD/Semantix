import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    st.title("Análise de Leitos de Ocupação de COVID-19")
    uploaded_file = st.file_uploader("Selecione o arquivo CSV", type=["csv"])
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        columns = df.columns.tolist()
        
        st.subheader("Colunas Disponíveis")
        st.write(columns)
        
        coluna_ocupacao = st.selectbox("Selecione a coluna de ocupação", columns)
        
        st.subheader("Dados Gerais")
        st.write(df)
        
        st.subheader("Gráfico de Ocupação")
        chart_type = st.selectbox("Selecione o tipo de gráfico", ["Gráfico de Linhas", "Gráfico de Barras", "Gráfico de Pizza"])
        
        if chart_type == "Gráfico de Linhas":
            st.line_chart(df[coluna_ocupacao])
        elif chart_type == "Gráfico de Barras":
            st.bar_chart(df[coluna_ocupacao])
        elif chart_type == "Gráfico de Pizza":
            st.pie_chart(df[coluna_ocupacao])
        
        st.subheader("Análise Individual de Coluna")
        coluna_selecionada = st.selectbox("Selecione a coluna para análise individual", columns)
        
        st.subheader("Dados da Coluna Selecionada")
        st.write(df[coluna_selecionada])
        
        # Exportar dados filtrados
        export_filename = st.text_input("Nome do arquivo de exportação (sem extensão)")
        export_format = st.selectbox("Formato de exportação", ["CSV", "Excel", "Metadados"])
        
        if st.button("Exportar Dados"):
            filtered_df = df[[coluna_selecionada]]
            
            if export_format == "CSV":
                csv_data = filtered_df.to_csv(index=False)
                st.download_button("Baixar Arquivo CSV", data=csv_data, file_name=f"{export_filename}.csv")
            elif export_format == "Excel":
                excel_data = filtered_df.to_excel(index=False)
                st.download_button("Baixar Arquivo Excel", data=excel_data, file_name=f"{export_filename}.xlsx")
            elif export_format == "Metadados":
                metadata = df.describe().transpose()
                metadata_csv = metadata.to_csv(index=True)
                st.download_button("Baixar Metadados (CSV)", data=metadata_csv, file_name=f"{export_filename}_metadata.csv")
        
        st.subheader("Matriz de Correlação")
        matriz_corr = df.corr()
        sns.heatmap(matriz_corr, annot=True, cmap="coolwarm")
        st.pyplot(plt)
        
if __name__ == "__main__":
    main()


