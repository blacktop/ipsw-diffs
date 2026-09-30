## MusicLibrary

> `/System/Library/SyncBundles/MusicLibrary.syncBundle/MusicLibrary`

```diff

-4025.200.17.0.0
-  __TEXT.__text: 0x710dc
+4025.300.10.0.0
+  __TEXT.__text: 0x7113c
   __TEXT.__auth_stubs: 0x870
   __TEXT.__objc_stubs: 0x4c60
   __TEXT.__objc_methlist: 0x119c

   __TEXT.__objc_methname: 0x5e79
   __TEXT.__objc_classname: 0x224
   __TEXT.__objc_methtype: 0xbec
-  __TEXT.__cstring: 0x2633
+  __TEXT.__cstring: 0x2634
   __TEXT.__oslogstring: 0x46bd
   __TEXT.__unwind_info: 0x810
   __TEXT.__eh_frame: 0x48
   __DATA_CONST.__auth_got: 0x448
-  __DATA_CONST.__got: 0x608
+  __DATA_CONST.__got: 0x610
   __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__const: 0x68c8
   __DATA_CONST.__cfstring: 0x19a0

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x28
-  __DATA_CONST.__objc_intobj: 0x360
+  __DATA_CONST.__objc_intobj: 0x378
   __DATA_CONST.__objc_arraydata: 0x248
   __DATA_CONST.__objc_arrayobj: 0x2e8
   __DATA_CONST.__objc_doubleobj: 0x10

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: E661A6CF-9AE3-3C4F-90BD-9ACE81A45A07
+  UUID: C0B34FA1-7C9D-3D9E-96D3-4A67B831A5C7
   Functions: 587
-  Symbols:   356
+  Symbols:   357
   CStrings:  1772
 
Symbols:
+ _ML3TrackPropertyAlbumPersistentID
Functions:
~ sub_4e320 : 1332 -> 1452
~ sub_54e0c -> sub_54e84 : 3992 -> 3968
CStrings:
+ "SELECT artwork_token.artwork_token, sync_id, item_pid, media_type, title FROM item JOIN item_store USING (item_pid) JOIN item_extra USING (item_pid) JOIN artwork_token ON album_pid = entity_pid AND entity_type = ? LEFT OUTER JOIN artwork ON artwork_token.artwork_token = artwork.artwork_token WHERE item_store.sync_id != 0 AND artwork_token.artwork_source_type = ? AND artwork.artwork_token IS NULL GROUP BY artwork_token.artwork_token"
- "SELECT artwork_token.artwork_token, sync_id, item_pid, media_type, title FROM item JOIN item_store USING (item_pid) JOIN item_extra USING (item_pid) JOIN artwork_token ON item_pid = entity_pid AND entity_type = ? LEFT OUTER JOIN artwork ON artwork_token.artwork_token = artwork.artwork_token WHERE item_store.sync_id != 0 AND artwork_token.artwork_source_type = ? AND artwork.artwork_token IS NULL GROUP BY artwork_token.artwork_token"

```
