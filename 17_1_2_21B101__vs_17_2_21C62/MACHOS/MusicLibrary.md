## MusicLibrary

> `/System/Library/SyncBundles/MusicLibrary.syncBundle/MusicLibrary`

```diff

-4023.210.4.0.0
-  __TEXT.__text: 0x61e90
-  __TEXT.__auth_stubs: 0x850
-  __TEXT.__objc_stubs: 0x4a00
+4023.310.4.0.0
+  __TEXT.__text: 0x62628
+  __TEXT.__auth_stubs: 0x860
+  __TEXT.__objc_stubs: 0x4a80
   __TEXT.__objc_methlist: 0xacc
   __TEXT.__const: 0xde88
-  __TEXT.__gcc_except_tab: 0xa64
-  __TEXT.__objc_methname: 0x5bbe
+  __TEXT.__gcc_except_tab: 0xb08
+  __TEXT.__objc_methname: 0x5c70
   __TEXT.__objc_classname: 0x224
   __TEXT.__objc_methtype: 0xbd5
-  __TEXT.__cstring: 0x207c
-  __TEXT.__oslogstring: 0x4291
+  __TEXT.__cstring: 0x2267
+  __TEXT.__oslogstring: 0x4340
   __TEXT.__dlopen_cstrs: 0x108
-  __TEXT.__unwind_info: 0x7ac
+  __TEXT.__unwind_info: 0x7b8
   __TEXT.__eh_frame: 0x50
-  __DATA_CONST.__auth_got: 0x438
-  __DATA_CONST.__got: 0x360
+  __DATA_CONST.__auth_got: 0x440
+  __DATA_CONST.__got: 0x368
   __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__const: 0x6418
-  __DATA_CONST.__cfstring: 0x17c0
+  __DATA_CONST.__cfstring: 0x1820
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_catlist: 0x0
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_intobj: 0x360
-  __DATA_CONST.__objc_arraydata: 0x200
-  __DATA_CONST.__objc_arrayobj: 0x288
+  __DATA_CONST.__objc_intobj: 0x390
+  __DATA_CONST.__objc_arraydata: 0x230
+  __DATA_CONST.__objc_arrayobj: 0x2b8
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA.__objc_const: 0x2038
-  __DATA.__objc_selrefs: 0x1570
+  __DATA.__objc_selrefs: 0x1590
   __DATA.__objc_protorefs: 0x10
   __DATA.__objc_classrefs: 0x2b0
   __DATA.__objc_superrefs: 0x28

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: A3E53F11-1289-3B12-99EF-8218EA1A4141
-  Functions: 547
-  Symbols:   350
-  CStrings:  1716
+  UUID: C29AE2EE-B249-3E92-A5E2-6CAFA204FA65
+  Functions: 551
+  Symbols:   352
+  CStrings:  1728
 
Symbols:
+ _ML3TrackPropertyIsPlayable
+ __ATLogCategoryAssetUtils_Oversize
CStrings:
+ "Cleared keep local status reason for album pids=%{public}@"
+ "Cleared keep local status reason for container pids=%{public}@"
+ "MLSyncParamMLSagaClientAddToLibraryWhenFavoriting"
+ "SELECT item.keep_local_status_reason, album_pid FROM item JOIN album USING (album_pid) WHERE (item.keep_local_status = ? AND album.keep_local > ? AND album.keep_local_status_reason != ?)"
+ "SELECT item.keep_local_status_reason, container.container_pid FROM item JOIN container_item USING (item_pid) JOIN container USING (container_pid) WHERE (item.keep_local_status = ? AND container.keep_local > ? AND container.keep_local_status_reason != ?)"
+ "clearSagaClientFeaturesVersion"
+ "clearSagaCloudFavoriteSongAddToLibraryBehavior"
+ "keepLocalCancelledOrDisabledAndIsDownloadingOrPausedPredicate"
+ "sagaCloudFavoriteSongAddToLibraryBehavior"
+ "setSagaCloudFavoriteSongAddToLibraryBehavior:"
+ "updating cloud account id from paired device: %lld --> %lld, addEntityToLibraryWhenFavoritingBehavior=%{public}@"
- "keepLocalCancelledAndIsDownloadingOrPausedPredicate"
- "updating cloud account id from paired device: %lld --> %lld"

```
