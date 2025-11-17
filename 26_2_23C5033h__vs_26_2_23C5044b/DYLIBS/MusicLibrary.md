## MusicLibrary

> `/System/Library/PrivateFrameworks/MusicLibrary.framework/MusicLibrary`

```diff

-4025.300.12.0.0
-  __TEXT.__text: 0x29e870
+4025.310.5.0.0
+  __TEXT.__text: 0x29ea6c
   __TEXT.__auth_stubs: 0x1fa0
   __TEXT.__objc_methlist: 0xe55c
   __TEXT.__const: 0x266e4
   __TEXT.__dlopen_cstrs: 0x277
-  __TEXT.__gcc_except_tab: 0x14660
-  __TEXT.__cstring: 0x6b41c
+  __TEXT.__gcc_except_tab: 0x14674
+  __TEXT.__cstring: 0x6b441
   __TEXT.__oslogstring: 0x1c131
   __TEXT.__ustring: 0x210
   __TEXT.__unwind_info: 0x7188

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 9EE313EF-E967-3C73-8E82-2640606AEE65
+  UUID: 773C659B-093D-3512-98F1-04742DF355FC
   Functions: 8327
   Symbols:   25336
   CStrings:  17798
Functions:
~ -[ML3ProcessDownloadedAssetsOperation _processTrackAsset:forSource:withError:] : 2600 -> 2728
~ __ZN16ML3ImportSession9_addAlbumENSt3__110shared_ptrI13ML3ImportItemEEP26ML3AlbumGroupingIdentifierxS3_ : 15656 -> 16036
CStrings:
+ "INSERT OR REPLACE INTO sort_map (name, sort_key, name_section) VALUES (?, iPhoneSortKey(?), iPhoneSortSection(iPhoneSortKey(?)))"
+ "SELECT album, sort_album, feed_url, rowid, grouping_key, album_artist_pid, season_number, all_compilations, user_rating, liked_state, album_year, (CASE WHEN season_number > 0 THEN season_number ELSE IFNULL(sort_album, album) END), contains_classical_work, user_rating_is_derived, sync_id, classical_experience_available, store_id, liked_state_changed_date, cloud_library_id, editorial_notes FROM album "
+ "SELECT artwork_token.artwork_token, artwork_token.artwork_source_type, (artwork.relative_path != '') AS has_artwork_on_disk FROM artwork_token LEFT OUTER JOIN artwork USING (artwork_token, artwork_variant_type) WHERE artwork_token.entity_pid = ? AND artwork_token.entity_type = ? AND artwork_token.artwork_type = ? AND artwork_token.artwork_variant_type = ? ORDER BY artwork_token.artwork_source_type ASC"
- "INSERT INTO sort_map (name, sort_key, name_section) VALUES (?, iPhoneSortKey(?), iPhoneSortSection(iPhoneSortKey(?)))"
- "SELECT album, sort_album, feed_url, rowid, grouping_key, album_artist_pid, season_number, all_compilations, user_rating, liked_state, album_year, (CASE WHEN season_number > 0 THEN season_number ELSE IFNULL(sort_album, album) END), contains_classical_work, user_rating_is_derived, sync_id, classical_experience_available, store_id, liked_state_changed_date, cloud_library_id, description FROM album "
- "SELECT artwork_token.artwork_token, artwork_token.artwork_source_type, (artwork.relative_path != '') AS has_artwork_on_disk FROM artwork_token LEFT OUTER JOIN artwork USING (artwork_token) WHERE artwork_token.entity_pid = ? AND artwork_token.entity_type = ? AND artwork_token.artwork_type = ? AND artwork_token.artwork_variant_type = ? ORDER BY artwork_token.artwork_source_type ASC"

```
