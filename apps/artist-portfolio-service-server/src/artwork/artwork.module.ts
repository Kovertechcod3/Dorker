import { Module } from "@nestjs/common";
import { ArtworkModuleBase } from "./base/artwork.module.base";
import { ArtworkService } from "./artwork.service";
import { ArtworkController } from "./artwork.controller";
import { ArtworkResolver } from "./artwork.resolver";

@Module({
  imports: [ArtworkModuleBase],
  controllers: [ArtworkController],
  providers: [ArtworkService, ArtworkResolver],
  exports: [ArtworkService],
})
export class ArtworkModule {}
