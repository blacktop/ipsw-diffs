## MusicLibrary

> `/System/Library/PrivateFrameworks/MusicLibrary.framework/MusicLibrary`

```diff

-4024.210.2.0.0
-  __TEXT.__text: 0x27a18c
+4024.300.14.0.0
+  __TEXT.__text: 0x27aefc
   __TEXT.__auth_stubs: 0x1fa0
-  __TEXT.__objc_methlist: 0xd814
+  __TEXT.__objc_methlist: 0xd81c
   __TEXT.__const: 0x26080
-  __TEXT.__gcc_except_tab: 0x137e4
-  __TEXT.__cstring: 0x661a7
-  __TEXT.__oslogstring: 0x19fc4
+  __TEXT.__gcc_except_tab: 0x13898
+  __TEXT.__cstring: 0x66727
+  __TEXT.__oslogstring: 0x1a168
   __TEXT.__ustring: 0x210
   __TEXT.__dlopen_cstrs: 0x193
-  __TEXT.__unwind_info: 0x7160
+  __TEXT.__unwind_info: 0x7188
   __TEXT.__eh_frame: 0x1ca0
   __TEXT.__objc_classname: 0x1919
   __TEXT.__objc_methname: 0x1df24
   __TEXT.__objc_methtype: 0x5276
   __TEXT.__objc_stubs: 0x14740
   __DATA_CONST.__got: 0xb18
-  __DATA_CONST.__const: 0x9038
+  __DATA_CONST.__const: 0x90d0
   __DATA_CONST.__objc_classlist: 0x6e0
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0xa8

   __DATA_CONST.__objc_selrefs: 0x6a18
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x510
-  __DATA_CONST.__objc_arraydata: 0x1070
+  __DATA_CONST.__objc_arraydata: 0x1098
   __AUTH_CONST.__auth_got: 0xfe8
   __AUTH_CONST.__auth_ptr: 0x18
   __AUTH_CONST.__const: 0x12560
-  __AUTH_CONST.__cfstring: 0x24b60
+  __AUTH_CONST.__cfstring: 0x24d80
   __AUTH_CONST.__objc_const: 0x15830
-  __AUTH_CONST.__objc_arrayobj: 0x2058
-  __AUTH_CONST.__objc_intobj: 0x1b48
+  __AUTH_CONST.__objc_arrayobj: 0x20b8
+  __AUTH_CONST.__objc_intobj: 0x1b60
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0xe6c
   __DATA.__data: 0x1960
-  __DATA.__bss: 0xb00
+  __DATA.__bss: 0xb20
   __DATA.__common: 0xa58
   __DATA_DIRTY.__objc_data: 0x4470
   __DATA_DIRTY.__data: 0x198
-  __DATA_DIRTY.__bss: 0x11e8
+  __DATA_DIRTY.__bss: 0x11d8
   __DATA_DIRTY.__common: 0x38
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 8068
-  Symbols:   9789
-  CStrings:  12367
+  Functions: 8075
+  Symbols:   9800
+  CStrings:  12389
 
Symbols:
+ _ML3AlbumPropertyStoreCanonicalID
+ _ML3ArtistPropertyStoreCanonicalID
+ _ML3TrackPropertyStoreTVSeasonCanonicalItemId
+ _ML3TrackPropertyStoreTVShowCanonicalItemId
CStrings:
+ "ALTER TABLE album_artist ADD COLUMN name_order INTEGER NOT NULL DEFAULT 0"
+ "ALTER TABLE item_store ADD COLUMN tv_season_canonical_id TEXT NOT NULL DEFAULT ''"
+ "ALTER TABLE item_store ADD COLUMN tv_show_canonical_id TEXT NOT NULL DEFAULT ''"
+ "CREATE INDEX IF NOT EXISTS AlbumArtistNameOrder ON album_artist (name_order ASC)"
+ "CacheManagement_Oversize"
+ "Clearing match properties for trackPIDS=%!{(MISSING)public}@"
+ "Failed to clear match source properties for track_pid=%!l(MISSING)ld, error=%!{(MISSING)public}@"
+ "Found %!l(MISSING)u albums to purge %!{(MISSING)public}@"
+ "LEFT OUTER JOIN item_store AS artist_item_store ON (item_artist.representative_item_pid == artist_item_store.ROWID)"
+ "PRAGMA user_version = 2220000;"
+ "PRAGMA user_version = 2220010;"
+ "PRAGMA user_version = 2220020;"
+ "Purged %!l(MISSING)ld bytes of media data for urgency %!d(MISSING) (%!l(MISSING)ld bytes requested)"
+ "Purged %!l(MISSING)lu bytes of streaming assets from tracks %!{(MISSING)public}@"
+ "Purged %!l(MISSING)u tracks from album %!{(MISSING)public}@ (%!{(MISSING)public}@ bytes): %!{(MISSING)public}@"
+ "Purging media data of at least %!l(MISSING)li bytes for urgency %!d(MISSING). includeAutoFilledTracks=%!{(MISSING)BOOL}u, optimizedStorageEnabled=%!{(MISSING)BOOL}u, minStorageAmount=%!l(MISSING)lu"
+ "SELECT item_pid FROM item_store WHERE (store_saga_id = 0 AND cloud_universal_library_id != '')"
+ "UPDATE album_artist SET grouping_key = iPhoneGroupingKey(album_artist), sort_order = IFNULL((SELECT name_order FROM sort_map WHERE name = IFNULL(album_artist.sort_album_artist, ML3SortString(album_artist.album_artist))), 0), sort_order_section = IFNULL((SELECT name_section FROM sort_map WHERE name = IFNULL(album_artist.sort_album_artist, ML3SortString(album_artist.album_artist))), 0), name_order = IFNULL((SELECT name_order FROM sort_map WHERE name = IFNULL(album_artist.album_artist, '')), 0)"
+ "UPDATE album_artist SET name_order = (SELECT IFNULL(name_order, 0) FROM sort_map WHERE sort_map.name=album_artist.album_artist) WHERE album_artist.representative_item_pid != 0"
+ "UPDATE item_extra SET integrity = (SELECT ML3TrackIntegrityCompute(item.item_pid, item.media_type, item_extra.location, item_extra.file_size) FROM item JOIN item_extra AS item_extra2 USING (item_pid) WHERE item_extra.item_pid = item.item_pid) WHERE item_pid IN (SELECT item_pid FROM item WHERE base_location_id != 0)"
+ "UPDATE item_store SET match_redownload_params=?, needs_reporting=?, playback_endpoint_type=?, cloud_playback_endpoint_type=?, cloud_in_my_library=?, cloud_album_id=?, cloud_universal_library_id=? WHERE item_pid=?"
+ "album_item_store.tv_season_canonical_id"
+ "artist_item_store.tv_show_canonical_id"
+ "failed to prepare collections"
+ "item_store.tv_season_canonical_id"
+ "item_store.tv_show_canonical_id"
+ "one OR more collections are not set correctly for track: artist=%!{(MISSING)BOOL}u, albumArtist=%!{(MISSING)BOOL}u, composer=%!{(MISSING)BOOL}u, genre=%!{(MISSING)BOOL}u, album=%!{(MISSING)BOOL}u"
+ "tv_season_canonical_id"
+ "tv_show_canonical_id"
- "Purged %!l(MISSING)ld bytes of media data"
- "Purged streaming assets %!{(MISSING)public}@"
- "Purging album %!{(MISSING)public}@ (%!{(MISSING)public}@ bytes): %!{(MISSING)public}@"
- "Purging media data of at least %!l(MISSING)li bytes for urgency %!d(MISSING). includeAutoFilledTracks=%!d(MISSING)"
- "Successfully purged redownloadable assets for album %!{(MISSING)public}@"
- "UPDATE album_artist SET grouping_key = iPhoneGroupingKey(album_artist), sort_order = IFNULL((SELECT name_order FROM sort_map WHERE name = IFNULL(album_artist.sort_album_artist, ML3SortString(album_artist.album_artist))), 0), sort_order_section = IFNULL((SELECT name_section FROM sort_map WHERE name = IFNULL(album_artist.sort_album_artist, ML3SortString(album_artist.album_artist))), 0)"
- "UPDATE item_extra SET integrity = (SELECT ML3TrackIntegrityCompute(item.item_pid, item.media_type, item_extra.location, item_extra.file_size) FROM item JOIN item_extra AS item_extra2 USING (item_pid) WHERE item_extra.item_pid = item.item_pid)"

```
