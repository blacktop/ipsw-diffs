## BackupAgent2

> `/usr/libexec/BackupAgent2`

```diff

-2891.0.0.0.0
-  __TEXT.__text: 0x9ed90
-  __TEXT.__auth_stubs: 0x1a20
+2899.0.2.0.0
+  __TEXT.__text: 0x9edd4
+  __TEXT.__auth_stubs: 0x1a30
   __TEXT.__objc_stubs: 0xd8e0
   __TEXT.__objc_methlist: 0x6b98
-  __TEXT.__const: 0x4c0
+  __TEXT.__const: 0x4d0
   __TEXT.__cstring: 0x1ba82
   __TEXT.__oslogstring: 0xe708
-  __TEXT.__objc_methname: 0xfc53
+  __TEXT.__objc_methname: 0xfc6c
   __TEXT.__objc_classname: 0xaeb
-  __TEXT.__objc_methtype: 0x2162
+  __TEXT.__objc_methtype: 0x2176
   __TEXT.__gcc_except_tab: 0x2740
   __TEXT.__unwind_info: 0x1bb8
-  __DATA_CONST.__auth_got: 0xd20
+  __DATA_CONST.__auth_got: 0xd28
   __DATA_CONST.__got: 0x538
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x1600

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 09A6C47E-5EF2-316D-A9EA-2D76E46558E6
+  UUID: C5858809-F377-33B9-92B2-B975622F84D1
   Functions: 2705
-  Symbols:   600
-  CStrings:  8923
+  Symbols:   601
+  CStrings:  8924
 
Symbols:
+ _MBSnapshotFormatContainsManifests
Functions:
~ sub_10005871c : 896 -> 932
~ sub_100059974 -> sub_100059998 : 1752 -> 1780
~ sub_100092a3c -> sub_100092a7c : 2272 -> 2276
CStrings:
+ "addDomainsToBackUpToiCloudWithAppManager:manager:format:account:"
+ "isLegacyPerAppPlaceholderDomain"
+ "isLegacyPerAppPlaceholderName:"
+ "size:%lld (%@)/%lld/%lld, files:%llu, dirs:%llu, clones:%llu/%llu, hardlinks:%llu, symlinks:%llu"
+ "v48@0:8@16@24q32@40"
- "addDomainsToBackUpToiCloudWithAppManager:manager:account:"
- "isAppPlaceholderName:"
- "isPlaceholderAppDomain"
- "size:%lld (%@)/%lld/%lld, files:%llu, dirs:%llu, clones:%llu/%llu, hardLinks:%llu, symLinks:%llu"

```
