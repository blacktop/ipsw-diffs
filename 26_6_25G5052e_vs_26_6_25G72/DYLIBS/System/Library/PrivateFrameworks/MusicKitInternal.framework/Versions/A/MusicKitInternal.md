## MusicKitInternal

> `/System/Library/PrivateFrameworks/MusicKitInternal.framework/Versions/A/MusicKitInternal`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__got`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-4025.700.2.0.0
+4025.700.3.0.0
   __TEXT.__text: 0x83e7a4
   __TEXT.__auth_stubs: 0xc2e0
   __TEXT.__objc_methlist: 0x24d4
   __TEXT.__const: 0x6b3cc
   __TEXT.__gcc_except_tab: 0x9d8
-  __TEXT.__cstring: 0x16565
+  __TEXT.__cstring: 0x165e5
   __TEXT.__dlopen_cstrs: 0xc8c
   __TEXT.__swift5_typeref: 0x17fff
   __TEXT.__oslogstring: 0x9c67
CStrings:
+ "SELECT container_pid, item_pid FROM container_item JOIN item USING (item_pid) JOIN item_extra USING (item_pid) JOIN item_store USING (item_pid) JOIN container USING (container_pid) WHERE item.media_type & 8 AND item.base_location_id > 200 AND item_store.is_protected = 0 AND location NOT LIKE '%.movpkg' AND container.is_hidden = 0 ORDER BY container_pid, position ASC"
+ "SELECT item_pid, title, total_time_ms, content_rating, disc_number, track_number, copyright, item_store.date_released, bit_rate, composer.composer, genre.genre, item_extra.date_modified, item.album_pid, album.album, disc_count, track_count, item.album_artist_pid, album_artist.album_artist FROM item JOIN item_extra USING (item_pid) JOIN item_store USING (item_pid) JOIN item_playback USING (item_pid) JOIN album USING (album_pid) LEFT OUTER JOIN album_artist USING (album_artist_pid) LEFT OUTER JOIN composer USING (composer_pid) LEFT OUTER JOIN genre USING (genre_id) WHERE item.media_type & 8 AND base_location_id > 200 AND is_protected = 0 AND location NOT LIKE '%.movpkg'"
- "SELECT container_pid, item_pid FROM container_item JOIN item USING (item_pid) JOIN item_store USING (item_pid) JOIN container USING (container_pid) WHERE item.media_type & 8 AND item.base_location_id > 200 AND item_store.is_protected = 0 AND container.is_hidden = 0 ORDER BY container_pid, position ASC"
- "SELECT item_pid, title, total_time_ms, content_rating, disc_number, track_number, copyright, date_released, bit_rate, composer.composer, genre.genre, item_extra.date_modified, item.album_pid, album.album, disc_count, track_count, item.album_artist_pid, album_artist.album_artist FROM item JOIN item_extra USING (item_pid) JOIN item_store USING (item_pid) JOIN item_playback USING (item_pid) JOIN album USING (album_pid) LEFT OUTER JOIN album_artist USING (album_artist_pid) LEFT OUTER JOIN composer USING (composer_pid) LEFT OUTER JOIN genre USING (genre_id) WHERE item.media_type & 8 AND base_location_id > 200 AND is_protected = 0"
```
