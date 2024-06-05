import { Module } from "@nestjs/common";
import { PortfolioModuleBase } from "./base/portfolio.module.base";
import { PortfolioService } from "./portfolio.service";
import { PortfolioController } from "./portfolio.controller";
import { PortfolioResolver } from "./portfolio.resolver";

@Module({
  imports: [PortfolioModuleBase],
  controllers: [PortfolioController],
  providers: [PortfolioService, PortfolioResolver],
  exports: [PortfolioService],
})
export class PortfolioModule {}
