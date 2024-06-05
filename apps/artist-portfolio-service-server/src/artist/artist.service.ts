import { Injectable } from "@nestjs/common";
import { PrismaService } from "../prisma/prisma.service";
import { ArtistServiceBase } from "./base/artist.service.base";

@Injectable()
export class ArtistService extends ArtistServiceBase {
  constructor(protected readonly prisma: PrismaService) {
    super(prisma);
  }
}
