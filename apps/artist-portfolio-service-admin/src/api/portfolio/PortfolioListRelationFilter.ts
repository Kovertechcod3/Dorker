import { PortfolioWhereInput } from "./PortfolioWhereInput";

export type PortfolioListRelationFilter = {
  every?: PortfolioWhereInput;
  some?: PortfolioWhereInput;
  none?: PortfolioWhereInput;
};
