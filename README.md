# Prion - gacetilla de prensa

## Generar el PDF

Instalá las dependencias y ejecutá desde la raíz del proyecto:

```powershell
pip install -r requirements.txt
python gacetilla.py
```

También se puede ejecutar como módulo:

```powershell
python -m prion_gacetilla
```

Los originales de las imágenes deben estar en `src/images/`. El PDF se genera
en la raíz del proyecto y las versiones JPG optimizadas junto a sus originales.
Las tapas originales de `Time of Plagues`, `Impressions`, `Uncertain Process`
y `Aberrant Calamity` se optimizan como JPG y se distribuyen a la derecha de
la biografía en cuatro espacios iguales que ocupan toda el área imprimible
de la página, manteniendo la proporción de cada imagen. La tapa de
`Aberrant Calamity` es `aberrant calamity cover.jpg`; `aberrant_calamity.webp`
se reserva para el fondo del documento y se optimiza como
`aberrant_calamity_optimized.jpg`.

## Organización

- `prion_gacetilla/config.py`: rutas y enlaces oficiales.
- `prion_gacetilla/assets.py`: preparación y optimización de imágenes.
- `prion_gacetilla/styles.py`: fuentes, colores y estilos del PDF.
- `prion_gacetilla/page_layout.py`: fondo y pie de página.
- `prion_gacetilla/utils.py`: componentes reutilizables, como QR y tablas.
- `prion_gacetilla/sections/`: portada, actualidad, biografía y prensa.
- `prion_gacetilla/generator.py`: ensamblado de secciones y creación del PDF.
- `gacetilla.py`: punto de entrada compatible.
