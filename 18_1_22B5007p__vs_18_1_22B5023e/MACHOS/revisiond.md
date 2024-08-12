## revisiond

> `/System/Library/PrivateFrameworks/GenerationalStorage.framework/revisiond`

```diff

-380.0.0.0.1
-  __TEXT.__text: 0x2a314
-  __TEXT.__auth_stubs: 0xf20
+382.0.0.0.0
+  __TEXT.__text: 0x2a3f0
+  __TEXT.__auth_stubs: 0xf30
   __TEXT.__objc_stubs: 0x3380
   __TEXT.__objc_methlist: 0x100c
   __TEXT.__const: 0x258
   __TEXT.__gcc_except_tab: 0x5c0
   __TEXT.__cstring: 0x50bb
   __TEXT.__objc_methname: 0x39c7
-  __TEXT.__oslogstring: 0x291d
+  __TEXT.__oslogstring: 0x294d
   __TEXT.__objc_classname: 0x1a7
   __TEXT.__objc_methtype: 0x12da
   __TEXT.__unwind_info: 0x8d0
-  __DATA_CONST.__auth_got: 0x7a0
+  __DATA_CONST.__auth_got: 0x7a8
   __DATA_CONST.__got: 0x278
   __DATA_CONST.__const: 0x1020
   __DATA_CONST.__cfstring: 0x2620

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/MobileCoreServices.framework/MobileCoreServices
+  - /System/Library/PrivateFrameworks/APFS.framework/APFS
   - /System/Library/PrivateFrameworks/CacheDelete.framework/CacheDelete
   - /System/Library/PrivateFrameworks/ChunkingLibrary.framework/ChunkingLibrary
   - /System/Library/PrivateFrameworks/GenerationalStorage.framework/GenerationalStorage

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 840
-  Symbols:   336
-  CStrings:  1559
+  Functions: 841
+  Symbols:   337
+  CStrings:  1560
 
Symbols:
+ _APFSVolumeRole
CStrings:
+ "15:29:17"
+ "Aug  2 2024"
+ "[ERROR] Disabling storage on system volume 0x%!x(MISSING)"
- "12:03:50"
- "Jul 10 2024"

```
