## MusicLibrary

> `/System/Library/PrivateFrameworks/MusicLibrary.framework/MusicLibrary`

```diff

-4024.100.105.0.0
-  __TEXT.__text: 0x27bd98
+4024.200.3.0.0
+  __TEXT.__text: 0x279950
   __TEXT.__auth_stubs: 0x1fa0
-  __TEXT.__objc_methlist: 0xd7d4
-  __TEXT.__const: 0x26460
-  __TEXT.__gcc_except_tab: 0x137c4
-  __TEXT.__cstring: 0x660c6
-  __TEXT.__oslogstring: 0x19e31
+  __TEXT.__objc_methlist: 0xd814
+  __TEXT.__const: 0x26080
+  __TEXT.__gcc_except_tab: 0x137cc
+  __TEXT.__cstring: 0x6612c
+  __TEXT.__oslogstring: 0x19dde
   __TEXT.__ustring: 0x210
   __TEXT.__dlopen_cstrs: 0x193
-  __TEXT.__unwind_info: 0x7130
-  __TEXT.__eh_frame: 0x1e48
+  __TEXT.__unwind_info: 0x7150
+  __TEXT.__eh_frame: 0x1ca0
   __TEXT.__objc_classname: 0x1919
-  __TEXT.__objc_methname: 0x1dd7f
-  __TEXT.__objc_methtype: 0x5227
-  __TEXT.__objc_stubs: 0x14720
-  __DATA_CONST.__got: 0xb20
-  __DATA_CONST.__const: 0x9010
+  __TEXT.__objc_methname: 0x1df24
+  __TEXT.__objc_methtype: 0x5276
+  __TEXT.__objc_stubs: 0x14760
+  __DATA_CONST.__got: 0xb18
+  __DATA_CONST.__const: 0x9038
   __DATA_CONST.__objc_classlist: 0x6e0
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x69f0
+  __DATA_CONST.__objc_selrefs: 0x6a18
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x510
-  __DATA_CONST.__objc_arraydata: 0x1078
+  __DATA_CONST.__objc_arraydata: 0x1070
   __AUTH_CONST.__auth_got: 0xfe8
   __AUTH_CONST.__auth_ptr: 0x18
-  __AUTH_CONST.__const: 0x12a88
+  __AUTH_CONST.__const: 0x12560
   __AUTH_CONST.__cfstring: 0x24aa0
   __AUTH_CONST.__objc_const: 0x15830
-  __AUTH_CONST.__objc_arrayobj: 0x2070
+  __AUTH_CONST.__objc_arrayobj: 0x2058
   __AUTH_CONST.__objc_intobj: 0x1b48
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x1ef0
-  __AUTH.__data: 0x110
+  __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0xe6c
-  __DATA.__data: 0x18e0
-  __DATA.__bss: 0xaa0
-  __DATA.__common: 0xa60
-  __DATA_DIRTY.__objc_data: 0x25d0
-  __DATA_DIRTY.__data: 0x88
-  __DATA_DIRTY.__bss: 0x11f8
+  __DATA.__data: 0x1960
+  __DATA.__bss: 0xaf0
+  __DATA.__common: 0xa58
+  __DATA_DIRTY.__objc_data: 0x4470
+  __DATA_DIRTY.__data: 0x198
+  __DATA_DIRTY.__bss: 0x11e8
   __DATA_DIRTY.__common: 0x38
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 8012
-  Symbols:   9779
-  CStrings:  12350
+  Functions: 8064
+  Symbols:   9785
+  CStrings:  12357
 
CStrings:
+ "B48@0:8@16i24B28r^q32Q40"
+ "B52@0:8i16@20@28B36@40B48"
+ "B56@0:8@16i24B28r^q32Q40@48"
+ "SELECT 1 FROM container WHERE store_cloud_id != 0 AND cloud_is_subscribed AND liked_state != 2 LIMIT 1"
+ "SELECT 1 FROM item JOIN item_store USING (item_pid) JOIN item_stats USING (item_pid) WHERE item.in_my_library AND item_store.cloud_status = 8 AND item_stats.liked_state != 2 LIMIT 1"
+ "[ML3MusicLibrary+RemoveSourceOrTracks] ML3MusicLibrary+RemoveSourceOrTracks removing source %!d(MISSING) from %!l(MISSING)u tracks, canonocalizeCollections=%!{(MISSING)BOOL}u"
+ "_insertArtworkRowWithArtworkToken passed empty path for artwork with token %!{(MISSING)public}@"
+ "_removeSource:fromPersistentIDS:forImportOperation:canonocalizeCollections:usingConnection:postNotifications:"
+ "deleteFromLibrary:deletionType:canonicalizeCollections:persistentIDs:count:"
+ "deleteFromLibrary:deletionType:canonicalizeCollections:persistentIDs:count:usingConnection:"
+ "msv_errorByRemovingUnsafeUserInfo"
+ "removeSource:fromPersistentIDS:forImportOperation:canonocalizeCollections:usingConnection:postNotifications:"
- "%!{(MISSING)public}@ checking in connection=%!p(MISSING), closeConnectionWhenCheckingIn=%!{(MISSING)BOOL}u, wrapper=%!{(MISSING)public}@"
- "SELECT 1 FROM container WHERE store_cloud_id != 0 AND cloud_is_subscribed LIMIT 1"
- "SELECT 1 FROM item JOIN item_store USING (item_pid) WHERE in_my_library AND cloud_status = ? LIMIT 1"
- "[ML3MusicLibrary+RemoveSourceOrTracks] ML3MusicLibrary+RemoveSourceOrTracks removing source %!d(MISSING) from %!l(MISSING)u tracks"
- "[ML3RemoveCloudSourcesOperation] Remove cloud sources maintenance task operation finished in %!f(MISSING) seconds"

```
