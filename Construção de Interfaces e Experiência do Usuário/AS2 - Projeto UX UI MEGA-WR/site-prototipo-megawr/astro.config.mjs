// @ts-check
import { defineConfig } from 'astro/config';

// Dominio definitivo da MEGA-WR. Alimenta as URLs absolutas (canonical, og:image)
// e a geracao do sitemap. Enquanto o dominio nao propagar, o site segue
// respondendo na URL provisoria de teste com noindex (flag INDEXAR_SITE em src/config.ts).
export const SITE_URL = 'https://megawr.com.br';

// https://astro.build/config
export default defineConfig({
  site: SITE_URL,
  integrations: [],
});
