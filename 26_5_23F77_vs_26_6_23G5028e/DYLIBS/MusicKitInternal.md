## MusicKitInternal

> `/System/Library/PrivateFrameworks/MusicKitInternal.framework/MusicKitInternal`

```diff

-4025.610.1.0.0
-  __TEXT.__text: 0x88fa14
+4025.700.2.0.0
+  __TEXT.__text: 0x88faf8
   __TEXT.__auth_stubs: 0xc630
   __TEXT.__objc_methlist: 0x26cc
-  __TEXT.__const: 0x6bcd4
+  __TEXT.__const: 0x6bce4
   __TEXT.__gcc_except_tab: 0xbc4
-  __TEXT.__cstring: 0x16e25
+  __TEXT.__cstring: 0x16e75
   __TEXT.__dlopen_cstrs: 0x10f7
   __TEXT.__swift5_typeref: 0x184af
   __TEXT.__oslogstring: 0xaf17
-  __TEXT.__swift5_reflstr: 0x10d1b
+  __TEXT.__swift5_reflstr: 0x10d3b
   __TEXT.__swift5_assocty: 0x3be0
   __TEXT.__constg_swiftt: 0x10210
-  __TEXT.__swift5_fieldmd: 0x14d34
+  __TEXT.__swift5_fieldmd: 0x14d40
   __TEXT.__swift5_builtin: 0x514
   __TEXT.__swift5_proto: 0x5d24
   __TEXT.__swift5_types: 0x1544

   __TEXT.__swift5_capture: 0x3bc0
   __TEXT.__swift5_mpenum: 0x150
   __TEXT.__lldbsummaries: 0x67
-  __TEXT.__unwind_info: 0x202d0
+  __TEXT.__unwind_info: 0x202b8
   __TEXT.__eh_frame: 0x3cda8
   __TEXT.__objc_classname: 0x1d75
-  __TEXT.__objc_methname: 0xaed5
+  __TEXT.__objc_methname: 0xaef5
   __TEXT.__objc_methtype: 0x1f15
-  __TEXT.__objc_stubs: 0x7720
+  __TEXT.__objc_stubs: 0x7740
   __DATA_CONST.__got: 0x3848
   __DATA_CONST.__const: 0x2120
   __DATA_CONST.__objc_classlist: 0x310
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x1b8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2140
+  __DATA_CONST.__objc_selrefs: 0x2148
   __DATA_CONST.__objc_protorefs: 0xc8
   __DATA_CONST.__objc_superrefs: 0x148
   __AUTH_CONST.__auth_got: 0x6328

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 5BC7074B-C9F2-3000-BEAB-0661DBC0D373
-  Functions: 54604
-  Symbols:   62421
-  CStrings:  4354
+  UUID: 89EF90D2-DC21-3787-B28E-511E78AAD908
+  Functions: 54609
+  Symbols:   62428
+  CStrings:  4356
 
Symbols:
+ ___swift_memcpy313_8
+ _objc_msgSend$setModificationDateTime:
- ___swift_memcpy304_8
CStrings:
+ ",\n  modificationDateMilliseconds: "
+ "SELECT item_pid, title, total_time_ms, content_rating, disc_number, track_number, copyright, date_released, bit_rate, composer.composer, genre.genre, item_extra.date_modified, item.album_pid, album.album, disc_count, track_count, item.album_artist_pid, album_artist.album_artist FROM item JOIN item_extra USING (item_pid) JOIN item_store USING (item_pid) JOIN item_playback USING (item_pid) JOIN album USING (album_pid) LEFT OUTER JOIN album_artist USING (album_artist_pid) LEFT OUTER JOIN composer USING (composer_pid) LEFT OUTER JOIN genre USING (genre_id) WHERE item.media_type & 8 AND base_location_id > 200 AND is_protected = 0"
+ "setModificationDateTime:"
- "SELECT item_pid, title, total_time_ms, content_rating, disc_number, track_number, copyright, date_released, bit_rate, composer.composer, genre.genre, item.album_pid, album.album, disc_count, track_count, item.album_artist_pid, album_artist.album_artist FROM item JOIN item_extra USING (item_pid) JOIN item_store USING (item_pid) JOIN item_playback USING (item_pid) JOIN album USING (album_pid) LEFT OUTER JOIN album_artist USING (album_artist_pid) LEFT OUTER JOIN composer USING (composer_pid) LEFT OUTER JOIN genre USING (genre_id) WHERE item.media_type & 8 AND base_location_id > 200 AND is_protected = 0"

```
