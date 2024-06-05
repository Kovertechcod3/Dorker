import { Artist as TArtist } from "../api/artist/Artist";

export const ARTIST_TITLE_FIELD = "id";

export const ArtistTitle = (record: TArtist): string => {
  return record.id?.toString() || String(record.id);
};
