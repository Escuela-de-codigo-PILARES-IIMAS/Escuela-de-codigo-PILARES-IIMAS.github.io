#!/bash/bin

pdftk  \
    'Portada e indice.pdf' \
    'Escuela de Código para PILARES Descripción del plan de estudios.pdf' \
    'Escuela de Código para PILARES Descripción de talleres.pdf' \
    'Escuela de Código para PILARES Definición de materiales.pdf' \
    'Escuela de Código para PILARES Descripción de actividades - Parte 1_ Conociendo el ambiente de computación (M0) .pdf' \
    'Escuela de Código para PILARES Descripción de actividades - Parte 2_ Módulo Elaboración de sistemas web (MW) .pdf' \
    'Escuela de Código para PILARES Descripción de actividades - Parte 3_ Programación (MP) .pdf' \
    'Escuela de Código para PILARES Descripción de actividades - Parte 4_ Desarrollo de aplicaciones móviles (MM).pdf' \
    'Escuela de Código para PILARES Descripción de actividades - Parte 5_ Administración sistemas Linux (ML).pdf' \
    'Escuela de Código para PILARES Descripción de actividades - Parte 6_ Base de datos (MBD).pdf' \
    'Escuela de Código para PILARES Guía de la Perspectiva de Género en el programa de estudios.pdf' \
    'Escuela de Código para PILARES Perfil de la tallerista.pdf' \
    'Escuela de Código para PILARES Tabla de especificaciones e Instrumentos de evaluación - M0 .pdf' \
    'Escuela de Código para PILARES Tabla de especificaciones e Instrumentos de evaluación - MBD.pdf' \
    'Escuela de Código para PILARES Tabla de especificaciones e Instrumentos de evaluación - ML.pdf' \
    'Escuela de Código para PILARES Tabla de especificaciones e Instrumentos de evaluación - MM.pdf' \
    'Escuela de Código para PILARES Tabla de especificaciones e Instrumentos de evaluación - MP.pdf' \
    'Escuela de Código para PILARES Tabla de especificaciones e Instrumentos de evaluación - MW.pdf' \
    anexos/*.pdf \
    cat output ec.pdf

gs  -q -dNOPAUSE -dBATCH -dSAFER \
    -sDEVICE=pdfwrite \
    -dCompatibilityLevel=1.4 \
    -dPDFSETTINGS=/screen \
    -dEmbedAllFonts=true \
    -dSubsetFonts=true \
    -dDownsampleColorImages=true \
    -dDownsampleGrayImages=true \
    -dDownsampleMonoImages=true \
    -dColorImageDownsampleType=/Bicubic \
    -dColorImageResolution=64 \
    -dGrayImageDownsampleType=/Bicubic \
    -dGrayImageResolution=64 \
    -dMonoImageDownsampleType=/Bicubic \
    -dMonoImageResolution=64 \
    -sOutputFile="Escuela de Código para PILARES.pdf" \
    ec.pdf

rm ec.pdf

