import type { APIRoute } from 'astro';

// Copia de teste do site (projeto academico): bloqueia o rastreamento por completo.
export const GET: APIRoute = () =>
  new Response('User-agent: *\nDisallow: /\n', {
    headers: { 'Content-Type': 'text/plain; charset=utf-8' },
  });
