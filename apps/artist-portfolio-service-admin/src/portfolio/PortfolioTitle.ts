import { Portfolio as TPortfolio } from "../api/portfolio/Portfolio";

export const PORTFOLIO_TITLE_FIELD = "id";

export const PortfolioTitle = (record: TPortfolio): string => {
  return record.id?.toString() || String(record.id);
};
