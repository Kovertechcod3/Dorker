import * as common from "@nestjs/common";
import * as swagger from "@nestjs/swagger";
import { ArtistService } from "./artist.service";
import { ArtistControllerBase } from "./base/artist.controller.base";

@swagger.ApiTags("artists")
@common.Controller("artists")
export class ArtistController extends ArtistControllerBase {
  constructor(protected readonly service: ArtistService) {
    super(service);
  }
}
