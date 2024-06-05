import * as graphql from "@nestjs/graphql";
import { ArtworkResolverBase } from "./base/artwork.resolver.base";
import { Artwork } from "./base/Artwork";
import { ArtworkService } from "./artwork.service";

@graphql.Resolver(() => Artwork)
export class ArtworkResolver extends ArtworkResolverBase {
  constructor(protected readonly service: ArtworkService) {
    super(service);
  }
}
