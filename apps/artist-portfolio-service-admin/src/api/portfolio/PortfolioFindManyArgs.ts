import { PortfolioWhereInput } from "./PortfolioWhereInput";
import { PortfolioOrderByInput } from "./PortfolioOrderByInput";

export type PortfolioFindManyArgs = {
  where?: PortfolioWhereInput;
  orderBy?: Array<PortfolioOrderByInput>;
  skip?: number;
  take?: number;
};
