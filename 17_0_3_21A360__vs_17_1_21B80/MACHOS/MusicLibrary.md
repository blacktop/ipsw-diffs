## MusicLibrary

> `/System/Library/SyncBundles/MusicLibrary.syncBundle/MusicLibrary`

```diff

-4023.110.4.0.0
-  __TEXT.__text: 0x6146c
+4023.210.4.0.0
+  __TEXT.__text: 0x61e90
   __TEXT.__auth_stubs: 0x850
-  __TEXT.__objc_stubs: 0x49e0
+  __TEXT.__objc_stubs: 0x4a00
   __TEXT.__objc_methlist: 0xacc
   __TEXT.__const: 0xde88
-  __TEXT.__gcc_except_tab: 0xa38
-  __TEXT.__objc_methname: 0x5b6e
+  __TEXT.__gcc_except_tab: 0xa64
+  __TEXT.__objc_methname: 0x5bbe
   __TEXT.__objc_classname: 0x224
-  __TEXT.__objc_methtype: 0xbd2
-  __TEXT.__cstring: 0x1ea5
-  __TEXT.__oslogstring: 0x421a
+  __TEXT.__objc_methtype: 0xbd5
+  __TEXT.__cstring: 0x207c
+  __TEXT.__oslogstring: 0x4291
   __TEXT.__dlopen_cstrs: 0x108
-  __TEXT.__unwind_info: 0x79c
+  __TEXT.__unwind_info: 0x7ac
   __TEXT.__eh_frame: 0x50
   __DATA_CONST.__auth_got: 0x438
   __DATA_CONST.__got: 0x360
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x63f0
-  __DATA_CONST.__cfstring: 0x1760
+  __DATA_CONST.__const: 0x6418
+  __DATA_CONST.__cfstring: 0x17c0
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_catlist: 0x0
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_intobj: 0x318
-  __DATA_CONST.__objc_arraydata: 0x1c0
-  __DATA_CONST.__objc_arrayobj: 0x240
+  __DATA_CONST.__objc_intobj: 0x360
+  __DATA_CONST.__objc_arraydata: 0x200
+  __DATA_CONST.__objc_arrayobj: 0x288
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA.__objc_const: 0x2038
-  __DATA.__objc_selrefs: 0x1568
+  __DATA.__objc_selrefs: 0x1570
   __DATA.__objc_protorefs: 0x10
   __DATA.__objc_classrefs: 0x2b0
   __DATA.__objc_superrefs: 0x28

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 542
+  Functions: 547
   Symbols:   350
-  CStrings:  1522
+  CStrings:  1526
 
CStrings:
+ "B40@0:8q16@24B32B36"
+ "MLSagaClientFeaturesVersion"
+ "SELECT item.keep_local_status_reason, album_pid FROM item JOIN album USING (album_pid) WHERE (item.keep_local_status = ? OR item.keep_local_status = ?) AND album.keep_local > ?"
+ "SELECT item.keep_local_status_reason, container_pid FROM item JOIN container_item USING (item_pid) JOIN container USING (container_pid) WHERE (item.keep_local_status = ? OR item.keep_local_status = ?) AND container.keep_local > ?"
+ "Updating containers' keep local status reason based on tracks' keep local status reason"
+ "_shouldSyncPlaylistWithPersistentId:forSupportedMediaTypes:includeNonLibraryContent:pairedDeviceCanProcessStandaloneCollections:"
+ "not syncing playlist pid=%lld. hidden=%d, isGenius=%d, isIgnorableITunesPlaylist=%d, distinguishedKind=%d, mediaType=%lx, isSubscribedCloudPlaylist=%d, pairedDeviceCanProcessStandaloneCollections=%{BOOL}u, syncFSP=%{BOOL}u"
+ "sagaClientFeaturesVersion"
+ "setSagaClientFeaturesVersion:"
+ "setting saga on disk revision=%llu, sagaClientFeaturesVersion=%{public}@"
+ "v32@?0@\"NSNumber\"8@\"NSNumber\"16^B24"
- "B36@0:8q16@24B32"
- "[delete album] pid=%lld"
- "_shouldSyncPlaylistWithPersistentId:forSupportedMediaTypes:includeNonLibraryContent:"
- "exportAlbumDeleted:"
- "failed to export delete for album %lld. err=%{public}@"
- "not syncing playlist pid=%lld. hidden=%d, isGenius=%d, isIgnorableITunesPlaylist=%d, distinguishedKind=%d, mediaType=%lx, isSubscribedCloudPlaylist=%d"
- "setting saga on disk revision=%llu"

```
