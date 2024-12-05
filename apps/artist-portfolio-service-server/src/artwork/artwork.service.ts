import { Injectable } from "@nestjs/common";
import { PrismaService } from "../prisma/prisma.service";
import { ArtworkServiceBase } from "./base/artwork.service.base";

@Injectable()
export class ArtworkService extends ArtworkServiceBase {
  constructor(protected readonly prisma: PrismaService) {
    super(prisma);
  }
}
