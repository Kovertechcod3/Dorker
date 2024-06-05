import * as common from "@nestjs/common";
import * as swagger from "@nestjs/swagger";
import { ArtworkService } from "./artwork.service";
import { ArtworkControllerBase } from "./base/artwork.controller.base";

@swagger.ApiTags("artworks")
@common.Controller("artworks")
export class ArtworkController extends ArtworkControllerBase {
  constructor(protected readonly service: ArtworkService) {
    super(service);
  }
}
