
# Conversão de Shapefile para Parquet

Este projeto demonstra como converter um arquivo **Shapefile** para o formato **Parquet**, utilizando a biblioteca `GeoPandas` em Python. O processo inclui a leitura do shapefile, a conversão de dados geoespaciais e a gravação do arquivo Parquet comprimido.

## Pré-requisitos

Para rodar este script, você precisará ter as seguintes bibliotecas Python instaladas:

- `geopandas` – Para trabalhar com dados geoespaciais.
- `pyarrow` – Para manipulação de arquivos Parquet.
- `gzip` – Para compressão do arquivo Parquet (opcional, mas recomendado para redução de tamanho).

Você pode instalar essas bibliotecas utilizando `pip`:

```bash
pip install geopandas pyarrow
```

## Estrutura do Projeto

```
/CarConversion
  ├── README.md           # Este arquivo
  ├── convert_shapefile.py # Script Python para conversão
  ├── geo_pol_car.shp     # Arquivo shapefile de entrada
  └── car.parquet         # Arquivo Parquet gerado (exemplo de saída)
```

## Como Utilizar

1. **Coloque seu shapefile no diretório correto**:  
   Certifique-se de que o arquivo shapefile (com extensão `.shp`) está presente no caminho especificado no script Python. O script é configurado para ler o arquivo `geo_pol_car.shp` a partir do caminho `C:/Temp/car/geo_pol_car.shp`.

2. **Executando o Script**:  
   Execute o script Python para converter o arquivo shapefile em um arquivo Parquet comprimido.

   ```bash
   python convert_shapefile.py
   ```

   O script fará o seguinte:
   - Lerá o arquivo shapefile.
   - Converterá os dados para um **GeoDataFrame**.
   - Grava o arquivo de saída no formato **Parquet** usando a compressão Gzip.

3. **Resultado da Conversão**:  
   O arquivo Parquet comprimido será gerado no local especificado. O tamanho do arquivo resultante será significativamente menor devido à compressão, facilitando o armazenamento e o desempenho em processos de leitura subsequentes.

   **Exemplo de saída**:  
   O script irá imprimir a seguinte mensagem após a execução bem-sucedida:

   ```
   Arquivo Parquet comprimido gerado em: C:/Temp/car/car.parquet
   ```

4. **Exemplo de redução de tamanho**:  
   O processo de conversão para Parquet, além de compactar os dados, oferece uma melhoria considerável na eficiência de armazenamento. Por exemplo, a conversão de um shapefile de 3,24 MB resultou em um arquivo Parquet comprimido de 2,30 MB.

## Como Funciona o Script

O script Python (`convert_shapefile.py`) segue os seguintes passos:

```python
import geopandas as gpd

shapefile_path = "C:/Temp/car/geo_pol_car.shp"
parquet_path = "C:/Temp/car/car.parquet"

# Leitura do shapefile com GeoPandas
gdf = gpd.read_file(shapefile_path)

# Gravação do arquivo Parquet com compressão Gzip
gdf.to_parquet(parquet_path, engine='pyarrow', compression='gzip', compression_level=9, index=False)

# Mensagem de sucesso
print(f"Arquivo Parquet comprimido gerado em: {parquet_path}")
```

- O script utiliza `geopandas` para ler o shapefile e convertê-lo em um `GeoDataFrame`.
- O arquivo é então convertido para o formato Parquet utilizando o `pyarrow`, com compressão Gzip para redução de tamanho. O parâmetro `compression_level=9` garante uma compressão máxima.

## Benefícios do Formato Parquet

- **Compactação**: O Parquet utiliza técnicas eficientes de compressão, o que reduz significativamente o tamanho do arquivo.
- **Leitura mais rápida**: O Parquet é otimizado para leitura rápida, o que é especialmente útil para grandes volumes de dados.
- **Suporte a dados estruturados**: O formato Parquet é adequado para armazenar dados tabulares e estruturados, o que o torna uma excelente opção para dados geoespaciais armazenados em tabelas.

## Conclusão

Este processo oferece uma maneira simples e eficiente de converter dados geoespaciais de um formato Shapefile para Parquet, com benefícios claros em termos de compactação e desempenho na leitura.

---

Esse README fornece um guia claro de como configurar e executar o processo de conversão, além de explicar os benefícios e a funcionalidade do script.
