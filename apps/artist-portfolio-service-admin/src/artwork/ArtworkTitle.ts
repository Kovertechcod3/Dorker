import { Artwork as TArtwork } from "../api/artwork/Artwork";

export const ARTWORK_TITLE_FIELD = "id";

export const ArtworkTitle = (record: TArtwork): string => {
  return record.id?.toString() || String(record.id);
};
