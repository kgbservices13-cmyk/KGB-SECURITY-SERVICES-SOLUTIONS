# KGB Security Services & Solutions

Landing page institucional de KGB Security Services & Solutions, construida con Astro y
preparada para despliegue estático.

## Requisitos

- **Node.js 22.12.0 o superior** (Astro 7 lo exige). La versión está fijada en
  `.node-version` y `.nvmrc`.
- npm 10 o superior (incluido con Node).

Verifica tu entorno:

```bash
node -v
npm -v
```

Si `node` no se reconoce, instala Node 22 LTS desde https://nodejs.org y **cierra y
vuelve a abrir la terminal** antes de continuar.

## Desarrollo local

```bash
npm install
npm run dev
```

El sitio queda disponible en `http://localhost:4321`.

## Producción

```bash
npm install
npm run build
```

El resultado se genera en `dist/`.

## Despliegue en Cloudflare Pages (recomendado)

Cloudflare construye el sitio en la nube, así que no necesitas Node instalado en tu
equipo para publicar.

1. En el panel de Cloudflare: **Workers & Pages → Create → Pages → Connect to Git**.
2. Selecciona el repositorio `KGB-SECURITY-SERVICES-SOLUTIONS`.
3. Configura la compilación:

   | Opción                     | Valor           |
   | :------------------------- | :-------------- |
   | Framework preset           | `Astro`         |
   | Build command              | `npm run build` |
   | Build output directory     | `dist`          |
   | Root directory             | `/`             |

4. En **Environment variables** añade `NODE_VERSION` = `22.12.0` (o deja que Cloudflare
   lea `.node-version`, ya incluido en el repo).
5. Guarda y despliega. Cada `git push` a `main` publica automáticamente.

### Despliegue manual con Wrangler (opcional)

Solo si prefieres publicar desde tu equipo. Requiere Node 22 instalado:

```bash
npm install
npm run build
npx wrangler pages deploy dist --project-name=kgb-security
```

> Si Wrangler falla con `Falló la ejecución de la compilación personalizada
> 'npm run build'`, casi siempre es porque Node no está instalado o es una versión
> anterior a 22.12. Ejecuta `node -v` para confirmarlo y reinstala Node 22 LTS.
