## MusicLibrary

> `/System/Library/PrivateFrameworks/MusicLibrary.framework/MusicLibrary`

```diff

-4024.200.3.0.0
-  __TEXT.__text: 0x279950
+4024.200.4.0.0
+  __TEXT.__text: 0x279878
   __TEXT.__auth_stubs: 0x1fa0
   __TEXT.__objc_methlist: 0xd814
   __TEXT.__const: 0x26080
-  __TEXT.__gcc_except_tab: 0x137cc
-  __TEXT.__cstring: 0x6612c
-  __TEXT.__oslogstring: 0x19dde
+  __TEXT.__gcc_except_tab: 0x137d4
+  __TEXT.__cstring: 0x66150
+  __TEXT.__oslogstring: 0x19ebe
   __TEXT.__ustring: 0x210
   __TEXT.__dlopen_cstrs: 0x193
   __TEXT.__unwind_info: 0x7150

   __TEXT.__objc_classname: 0x1919
   __TEXT.__objc_methname: 0x1df24
   __TEXT.__objc_methtype: 0x5276
-  __TEXT.__objc_stubs: 0x14760
+  __TEXT.__objc_stubs: 0x14740
   __DATA_CONST.__got: 0xb18
   __DATA_CONST.__const: 0x9038
   __DATA_CONST.__objc_classlist: 0x6e0

   __AUTH_CONST.__auth_got: 0xfe8
   __AUTH_CONST.__auth_ptr: 0x18
   __AUTH_CONST.__const: 0x12560
-  __AUTH_CONST.__cfstring: 0x24aa0
+  __AUTH_CONST.__cfstring: 0x24ac0
   __AUTH_CONST.__objc_const: 0x15830
   __AUTH_CONST.__objc_arrayobj: 0x2058
   __AUTH_CONST.__objc_intobj: 0x1b48

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 8064
-  Symbols:   9785
-  CStrings:  12357
+  Functions: 8063
+  Symbols:   9784
+  CStrings:  12360
 
CStrings:
+ "[ML3RemoveCloudSourcesOperation] %!{(MISSING)public}@ - Removing %!l(MISSING)d playlists synced from the cloud"
+ "[ML3RemoveCloudSourcesOperation] %!{(MISSING)public}@ - Removing cloud id properties failed with error=%!{(MISSING)public}@."
+ "[ML3RemoveCloudSourcesOperation] %!{(MISSING)public}@ - Updating is_src_remote failed with error=%!{(MISSING)public}@."
+ "UPDATE container SET is_src_remote=1 WHERE sync_id != 0"
+ "[ML3RemoveCloudSourcesOperation] %!{(MISSING)public}@ - Removing cloud source from albums and artists"
+ "UPDATE container SET store_cloud_id = 0"
+ "[ML3RemoveCloudSourcesOperation] %!{(MISSING)public}@ - Removing cloud source from playlists"
- "[ML3RemoveCloudSourcesOperation] %!{(MISSING)public}@ - Removing %!l(MISSING)d remote playlists."
- "UPDATE container SET store_cloud_id=0 WHERE container_pid=?"
- "[ML3RemoveCloudSourcesOperation] %!{(MISSING)public}@ - Removing %!l(MISSING)d visible playlists."
- "[ML3RemoveCloudSourcesOperation] %!{(MISSING)public}@ - Clearing cloud ID for %!l(MISSING)d visible playlists."

```
