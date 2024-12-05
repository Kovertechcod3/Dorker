import * as graphql from "@nestjs/graphql";
import { ArtistResolverBase } from "./base/artist.resolver.base";
import { Artist } from "./base/Artist";
import { ArtistService } from "./artist.service";

@graphql.Resolver(() => Artist)
export class ArtistResolver extends ArtistResolverBase {
  constructor(protected readonly service: ArtistService) {
    super(service);
  }
}
