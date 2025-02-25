<h1 align="center">🕷️ SEO Meta Robots Checker</h1>

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/License-MIT-yellow">
  <img src="https://img.shields.io/badge/Version-1.0.0-success">
</div>

## 📋 Descrição

Ferramenta para verificação em massa da meta tag robots (index/follow) com paralelismo inteligente e geração de relatórios. Ideal para auditorias técnicas de SEO em grande escala.

## 🚀 Funcionalidades Principais

- **Verificação paralela** de URLs usando `ThreadPoolExecutor`
- **Validação rigorosa** de URLs com regex avançado
- Detecção de 5 cenários diferentes:
  - ✅ Configuração correta (`index, follow`)
  - ⚠️ Meta tag ausente
  - ❗ Configuração incomum
  - 🚨 Erros HTTP (4xx/5xx)
  - 🔥 Erros de processamento
- **Geração automática** de relatórios em Excel (.xlsx)
- **Logging detalhado** com métricas de performance

## 🛠️ Tecnologias Utilizadas

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![Requests](https://img.shields.io/badge/Requests-2.28.0-green?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-2.0.0-red?logo=pandas)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4.12.0-lightgrey?logo=beautifulsoup)

## ⚙️ Installation

1. Clone o repositório

```bash
git clone https://github.com/armandomonteir-o/script-metarobots.git
cd script-metarobots
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

## 🎯 Como Usar

1. Prepare seu arquivo CSV de entrada com as URLs (uma por linha)

   - Você pode usar o arquivo de exemplo [`example_urls.csv`](examples/example_urls.csv) como modelo
   - O arquivo deve conter uma coluna chamada "URLS" com as URLs

2. Execute o script principal:

```bash
python main.py input.csv
```

3. O relatório será gerado automaticamente na pasta `results` com o formato:
   - `resultado_AAAAMMDD_HHMMSS.xlsx`

💡 **Dica**: Para testar o script, você pode usar nosso arquivo de exemplo:

```bash
python main.py examples/example_urls.csv
```

3. The report will be automatically generated in the `results` folder

## 📊 Relatório

O relatório gerado em Excel contém as seguintes colunas:

- URL
- HTTP Status

## 🔍 Example Output

```
[https://example.com] -> ✅ Configuração correta: 'index, follow'
[https://invalid.url] -> 🚨 ERRO HTTP: 404
[https://example.org] -> ❗ Meta Tag encontrada, porém configuração incomum: index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1
```

## 🤝 Contributors

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/armandomonteir-o">
        <img src="https://avatars.githubusercontent.com/u/141039211?s=400&u=574881d437dd6350183e057c6da9cffd83ed4069&v=4" width="100px;" alt="Armando Monteiro"/><br>
        <sub>
          <b>Armando Monteiro</b>
        </sub>
      </a>
    </td>
  </tr>
</table>

## 📈 Project Status

![Status](https://img.shields.io/badge/Status-In%20Development-yellow)

## 📝 License

This project is under the MIT license. See the [LICENSE](LICENSE) file for more details.

## 💡 Contribuindo

Contribuições são sempre bem-vindas! Sinta-se à vontade para:

1. Relatar bugs

2. Sugerir novas funcionalidades

3. Enviar pull requests

### Passo a passo para contribuição:

1. Faça um fork do repositório
2. Crie sua branch de funcionalidade (`git checkout -b feature/AmazingFeature`)
3. Registre suas alterações (`git commit -m 'Add some AmazingFeature'`)
4. Envie para o branch remoto (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 🔮 Melhorias Futuras

- [ ] Adicionar suporte para mais meta tags
- [ ] Implementar modelos de relatório personalizados
- [ ] Adicionar opções de integração via API
- [ ] Criar interface web
- [ ] Adicionar suporte para configurações de proxy
