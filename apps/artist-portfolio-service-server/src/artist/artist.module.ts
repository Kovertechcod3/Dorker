import { Module } from "@nestjs/common";
import { ArtistModuleBase } from "./base/artist.module.base";
import { ArtistService } from "./artist.service";
import { ArtistController } from "./artist.controller";
import { ArtistResolver } from "./artist.resolver";

@Module({
  imports: [ArtistModuleBase],
  controllers: [ArtistController],
  providers: [ArtistService, ArtistResolver],
  exports: [ArtistService],
})
export class ArtistModule {}
