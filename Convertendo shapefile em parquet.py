

# Conversão 1,67 MB

Convertendo shapefile do car

import geopandas as gpd

shapefile_path = "C:/Temp/car/geo_pol_car.shp"
parquet_path = "C:/Temp/car/car.parquet"
gdf = gpd.read_file(shapefile_path)
gdf.to_parquet(parquet_path, engine='pyarrow', compression='gzip', compression_level=9, index=False)
print(f"Arquivo Parquet comprimido gerado em: {parquet_path}")

A conversão foi de 3,24 para 2,30 MB

Escreva um readme




"""
# Conversão 2,02 MB

import geopandas as gpd

shapefile_path = "C:/Temp/quilombolas/geo_pol_com_qlmb.shp"
parquet_path = "C:/Temp/quilombolas/teste.parquet"
gdf = gpd.read_file(shapefile_path)
gdf.to_parquet(parquet_path, engine='pyarrow', compression='Zstd', index=False)
print(f"Arquivo Parquet comprimido gerado em: {parquet_path}")
"""


"""
# Conversão 1,67 MB

import geopandas as gpd

shapefile_path = "C:/Temp/quilombolas/geo_pol_com_qlmb.shp"
parquet_path = "C:/Temp/quilombolas/teste.parquet"
gdf = gpd.read_file(shapefile_path)
gdf.to_parquet(parquet_path, engine='pyarrow', compression='brotli', compression_level=11, index=False)
print(f"Arquivo Parquet comprimido gerado em: {parquet_path}")
"""
