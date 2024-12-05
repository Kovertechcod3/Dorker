import { ArtworkWhereInput } from "./ArtworkWhereInput";
import { ArtworkOrderByInput } from "./ArtworkOrderByInput";

export type ArtworkFindManyArgs = {
  where?: ArtworkWhereInput;
  orderBy?: Array<ArtworkOrderByInput>;
  skip?: number;
  take?: number;
};
