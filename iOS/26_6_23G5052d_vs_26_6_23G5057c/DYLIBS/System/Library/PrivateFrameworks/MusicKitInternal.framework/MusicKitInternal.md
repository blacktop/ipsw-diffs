## MusicKitInternal

> `/System/Library/PrivateFrameworks/MusicKitInternal.framework/MusicKitInternal`

```diff

   __TEXT.__objc_methlist: 0x26cc
   __TEXT.__const: 0x6bce4
   __TEXT.__gcc_except_tab: 0xbc4
-  __TEXT.__cstring: 0x16e75
+  __TEXT.__cstring: 0x16ef5
   __TEXT.__dlopen_cstrs: 0x10f7
   __TEXT.__swift5_typeref: 0x184af
   __TEXT.__oslogstring: 0xaf17
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__const : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__unwind_info : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH.__objc_data : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
~ __DATA_DIRTY.__data : content changed
CStrings:
+ "SELECT container_pid, item_pid FROM container_item JOIN item USING (item_pid) JOIN item_extra USING (item_pid) JOIN item_store USING (item_pid) JOIN container USING (container_pid) WHERE item.media_type & 8 AND item.base_location_id > 200 AND item_store.is_protected = 0 AND location NOT LIKE '%.movpkg' AND container.is_hidden = 0 ORDER BY container_pid, position ASC"
+ "SELECT item_pid, title, total_time_ms, content_rating, disc_number, track_number, copyright, item_store.date_released, bit_rate, composer.composer, genre.genre, item_extra.date_modified, item.album_pid, album.album, disc_count, track_count, item.album_artist_pid, album_artist.album_artist FROM item JOIN item_extra USING (item_pid) JOIN item_store USING (item_pid) JOIN item_playback USING (item_pid) JOIN album USING (album_pid) LEFT OUTER JOIN album_artist USING (album_artist_pid) LEFT OUTER JOIN composer USING (composer_pid) LEFT OUTER JOIN genre USING (genre_id) WHERE item.media_type & 8 AND base_location_id > 200 AND is_protected = 0 AND location NOT LIKE '%.movpkg'"
- "SELECT container_pid, item_pid FROM container_item JOIN item USING (item_pid) JOIN item_store USING (item_pid) JOIN container USING (container_pid) WHERE item.media_type & 8 AND item.base_location_id > 200 AND item_store.is_protected = 0 AND container.is_hidden = 0 ORDER BY container_pid, position ASC"
- "SELECT item_pid, title, total_time_ms, content_rating, disc_number, track_number, copyright, date_released, bit_rate, composer.composer, genre.genre, item_extra.date_modified, item.album_pid, album.album, disc_count, track_count, item.album_artist_pid, album_artist.album_artist FROM item JOIN item_extra USING (item_pid) JOIN item_store USING (item_pid) JOIN item_playback USING (item_pid) JOIN album USING (album_pid) LEFT OUTER JOIN album_artist USING (album_artist_pid) LEFT OUTER JOIN composer USING (composer_pid) LEFT OUTER JOIN genre USING (genre_id) WHERE item.media_type & 8 AND base_location_id > 200 AND is_protected = 0"

```
