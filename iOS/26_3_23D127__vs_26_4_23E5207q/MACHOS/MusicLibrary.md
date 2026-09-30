## MusicLibrary

> `/System/Library/SyncBundles/MusicLibrary.syncBundle/MusicLibrary`

```diff

-4025.400.4.0.0
-  __TEXT.__text: 0x7113c
-  __TEXT.__auth_stubs: 0x870
-  __TEXT.__objc_stubs: 0x4c60
-  __TEXT.__objc_methlist: 0x11ac
+4025.500.40.0.0
+  __TEXT.__text: 0x8145c
+  __TEXT.__auth_stubs: 0x850
+  __TEXT.__objc_stubs: 0x4ca0
+  __TEXT.__objc_methlist: 0x11b4
   __TEXT.__dlopen_cstrs: 0x108
-  __TEXT.__const: 0xf6d4
-  __TEXT.__gcc_except_tab: 0xe80
-  __TEXT.__objc_methname: 0x5e98
+  __TEXT.__const: 0xf7a4
+  __TEXT.__gcc_except_tab: 0xe34
+  __TEXT.__objc_methname: 0x5f0b
   __TEXT.__objc_classname: 0x224
   __TEXT.__objc_methtype: 0xbec
-  __TEXT.__cstring: 0x2634
-  __TEXT.__oslogstring: 0x46bd
-  __TEXT.__unwind_info: 0x810
-  __TEXT.__eh_frame: 0x48
-  __DATA_CONST.__auth_got: 0x448
+  __TEXT.__cstring: 0x280b
+  __TEXT.__oslogstring: 0x46f2
+  __TEXT.__unwind_info: 0x870
+  __TEXT.__eh_frame: 0x80
+  __DATA_CONST.__auth_got: 0x438
   __DATA_CONST.__got: 0x610
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x68c8
-  __DATA_CONST.__cfstring: 0x19a0
+  __DATA_CONST.__const: 0x6c38
+  __DATA_CONST.__cfstring: 0x1a00
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x28
-  __DATA_CONST.__objc_intobj: 0x378
-  __DATA_CONST.__objc_arraydata: 0x248
-  __DATA_CONST.__objc_arrayobj: 0x2e8
+  __DATA_CONST.__objc_intobj: 0x360
+  __DATA_CONST.__objc_arraydata: 0x258
+  __DATA_CONST.__objc_arrayobj: 0x300
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA.__objc_const: 0x1388
-  __DATA.__objc_selrefs: 0x1858
+  __DATA.__objc_selrefs: 0x1870
   __DATA.__objc_ivar: 0x100
   __DATA.__objc_data: 0x1e0
-  __DATA.__data: 0x7f0
+  __DATA.__data: 0xa08
   __DATA.__bss: 0x200
   __DATA.__common: 0xa18
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 72235687-9630-3D03-949F-0A2262905EE5
-  Functions: 587
-  Symbols:   357
-  CStrings:  1773
+  UUID: CB921089-2C57-3060-AEAE-8B78DB5FA611
+  Functions: 567
+  Symbols:   355
+  CStrings:  1784
 
Symbols:
+ _ML3MusicLibraryCachingAvailabilityDidChangeNotification
+ _objc_autorelease
+ _objc_release_x2
+ _objc_retainAutoreleasedReturnValue
- _ML3TrackPropertyAlbumPersistentID
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x9
CStrings:
+ "Album"
+ "Caching availability has changed - requesting a sync"
+ "MLSyncPolicyChangedObserverStartSyncSessionSignificantChangesOnlyKey"
+ "SELECT artwork_token.artwork_token, sync_id, album_pid, album FROM album JOIN artwork_token ON album_pid = entity_pid LEFT OUTER JOIN artwork ON artwork_token.artwork_token = artwork.artwork_token WHERE sync_id != 0 AND artwork_token.entity_type = ? AND artwork_token.artwork_source_type = ? AND artwork.artwork_token IS NULL GROUP BY artwork_token.artwork_token"
+ "SELECT artwork_token.artwork_token, sync_id, item_pid, media_type, title FROM item JOIN item_store USING (item_pid) JOIN item_extra USING (item_pid) JOIN artwork_token ON item_pid = entity_pid AND entity_type = ? LEFT OUTER JOIN artwork ON artwork_token.artwork_token = artwork.artwork_token WHERE item_store.sync_id != 0 AND artwork_token.artwork_source_type = ? AND artwork.artwork_token IS NULL GROUP BY artwork_token.artwork_token"
+ "_handleCachingAvailabilityDidChangeNotification:"
+ "allow_explicit_content_in_library"
+ "setIgnoreRestrictionsPredicates:"
+ "setIgnoreSystemFilterPredicates:"
- "SELECT artwork_token.artwork_token, sync_id, item_pid, media_type, title FROM item JOIN item_store USING (item_pid) JOIN item_extra USING (item_pid) JOIN artwork_token ON album_pid = entity_pid AND entity_type = ? LEFT OUTER JOIN artwork ON artwork_token.artwork_token = artwork.artwork_token WHERE item_store.sync_id != 0 AND artwork_token.artwork_source_type = ? AND artwork.artwork_token IS NULL GROUP BY artwork_token.artwork_token"

```
