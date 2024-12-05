import { Injectable } from "@nestjs/common";
import { PrismaService } from "../prisma/prisma.service";
import { PortfolioServiceBase } from "./base/portfolio.service.base";

@Injectable()
export class PortfolioService extends PortfolioServiceBase {
  constructor(protected readonly prisma: PrismaService) {
    super(prisma);
  }
}
