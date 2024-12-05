import * as graphql from "@nestjs/graphql";
import { PortfolioResolverBase } from "./base/portfolio.resolver.base";
import { Portfolio } from "./base/Portfolio";
import { PortfolioService } from "./portfolio.service";

@graphql.Resolver(() => Portfolio)
export class PortfolioResolver extends PortfolioResolverBase {
  constructor(protected readonly service: PortfolioService) {
    super(service);
  }
}
