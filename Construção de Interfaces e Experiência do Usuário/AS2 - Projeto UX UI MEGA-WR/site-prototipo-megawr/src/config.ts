// Dados do cliente em um lugar so — mudou aqui, muda no site inteiro.
// Fonte: Clientes/MEGA WR/DOCUMENTO-INSTITUCIONAL.md

// Lancado em megawr.com.br em 12/08/2026 — site liberado para indexacao.
// Voltar para false so se precisar tirar o site da busca temporariamente.
// COPIA DE TESTE (AS2 PUCPR): nunca indexar. O site oficial continua em
// 0-Claude/Clientes/MEGA WR/Site e nao e' afetado por esta pasta.
export const INDEXAR_SITE = false;

// Rota do orcamento guiado proposto no projeto de UX/UI.
export const ORCAMENTO_URL = '/orcamento';

export const empresa = {
  nome: 'MEGA-WR Confecções',
  cnpj: '06.315.623/0001-30',
  endereco: 'Rua Bernardino de Campos, 1055 — Vila Santucci, Leme/SP',
  email: 'wtsuyama@gmail.com',
  horario: 'Segunda a sexta, 9h–18h · Sábado, 9h–12h',
  // WhatsApp oficial da MEGA-WR — mesmo número da fachada e das redes sociais.
  whatsapp: '5519991336523',
  whatsappExibicao: '(19) 9 9133-6523',
};

// Mesmos dados de `empresa`, quebrados em campos separados para o JSON-LD
// que o Google le (ficha de negocio local na busca e no Maps).
export const enderecoEstruturado = {
  rua: 'Rua Bernardino de Campos, 1055',
  bairro: 'Vila Santucci',
  cidade: 'Leme',
  estado: 'SP',
  pais: 'BR',
  cep: '13614-180',
};

// Formato exigido pelo schema.org (OpeningHoursSpecification).
export const horarioEstruturado = [
  { dias: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'], abre: '09:00', fecha: '18:00' },
  { dias: ['Saturday'], abre: '09:00', fecha: '12:00' },
];

// Redes divulgadas no site. Hoje so o Instagram; se outra entrar, adicionar aqui.
export const redes = [
  {
    nome: 'Instagram',
    handle: '@megawr_uniformes',
    url: 'https://www.instagram.com/megawr_uniformes/',
  },
];

export const whatsappLink = (mensagem: string) =>
  `https://wa.me/${empresa.whatsapp}?text=${encodeURIComponent(mensagem)}`;

export const CTA_PADRAO =
  'Olá! Vim pelo site e gostaria de solicitar um orçamento de uniformes.';
