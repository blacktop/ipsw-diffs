## SpaceAttribution

> `/System/Library/PrivateFrameworks/SpaceAttribution.framework/SpaceAttribution`

```diff

-175.2.1.0.0
-  __TEXT.__text: 0xd02c
-  __TEXT.__auth_stubs: 0x540
-  __TEXT.__objc_methlist: 0xc08
+180.42.1.0.0
+  __TEXT.__text: 0xd234
+  __TEXT.__auth_stubs: 0x550
+  __TEXT.__objc_methlist: 0xc38
   __TEXT.__const: 0x80
-  __TEXT.__cstring: 0xc0a
-  __TEXT.__oslogstring: 0xb6c
-  __TEXT.__gcc_except_tab: 0x580
-  __TEXT.__unwind_info: 0x46c
+  __TEXT.__cstring: 0xc2c
+  __TEXT.__oslogstring: 0xc0c
+  __TEXT.__gcc_except_tab: 0x4e0
+  __TEXT.__unwind_info: 0x440
   __TEXT.__objc_classname: 0x13a
-  __TEXT.__objc_methname: 0x1eb1
-  __TEXT.__objc_methtype: 0x68e
-  __TEXT.__objc_stubs: 0x1560
+  __TEXT.__objc_methname: 0x1f8b
+  __TEXT.__objc_methtype: 0x6a7
+  __TEXT.__objc_stubs: 0x1600
   __DATA_CONST.__got: 0x58
   __DATA_CONST.__const: 0x3d8
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1160
-  __DATA_CONST.__objc_selrefs: 0x8a8
+  __DATA_CONST.__objc_const: 0x1190
+  __DATA_CONST.__objc_selrefs: 0x8e8
   __DATA_CONST.__objc_arraydata: 0x100
-  __AUTH_CONST.__cfstring: 0xd80
+  __AUTH_CONST.__cfstring: 0xe00
   __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_const: 0x7e0
   __AUTH_CONST.__objc_arrayobj: 0x60
-  __AUTH_CONST.__auth_got: 0x2b0
+  __AUTH_CONST.__auth_got: 0x2b8
   __AUTH.__objc_data: 0x4b0
   __DATA.__objc_protorefs: 0x10
   __DATA.__objc_classrefs: 0xd8
   __DATA.__objc_superrefs: 0x58
-  __DATA.__objc_ivar: 0xc8
+  __DATA.__objc_ivar: 0xcc
   __DATA.__data: 0x180
   __DATA.__bss: 0x30
   __DATA_DIRTY.__objc_data: 0xf0

   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
+  - /System/Library/PrivateFrameworks/DiskImages2.framework/DiskImages2
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AEA2AEF3-F333-3EFA-BC0F-96A965FDC5E9
-  Functions: 401
-  Symbols:   1381
-  CStrings:  797
+  UUID: EFC5CA46-F035-3340-9E1A-783BE7B7645C
+  Functions: 410
+  Symbols:   1400
+  CStrings:  820
 
Symbols:
+ +[SASupport getPathOfNodeID:FSid:]
+ +[SASupport getPathOfNodeID:FSid:].cold.1
+ -[SAAppSizerResults clonesInfo]
+ -[SAAppSizerResults initDiskUsedAndCapacity].cold.4
+ -[SAAppSizerResults initDiskUsedAndCapacity].cold.5
+ -[SAAppSizerResults setClonesInfo:]
+ -[SAAppSizerResults zeroSizeAppsFiltering]
+ GCC_except_table61
+ GCC_except_table62
+ _OBJC_CLASS_$_DIIOMedia
+ _OBJC_IVAR_$_SAAppSizerResults._clonesInfo
+ ___42-[SAAppSizerResults zeroSizeAppsFiltering]_block_invoke
+ ___42-[SAAppSizerResults zeroSizeAppsFiltering]_block_invoke.cold.1
+ ___57-[SAAppSizerResults postProcessFilteringWithAppPathList:]_block_invoke.309
+ ___62-[SAPathManager unregisterURLs:forBundleID:completionHandler:]_block_invoke.141
+ ___62-[SAPathManager unregisterURLs:forBundleID:completionHandler:]_block_invoke.141.cold.1
+ ___62-[SAPathManager unregisterURLs:forBundleID:completionHandler:]_block_invoke.cold.1
+ ___block_descriptor_40_e8_32s_e33_v32?0"NSSet"8"SAAppSize"16^B24ls32l8
+ _fsgetpath
+ _objc_msgSend$clonesInfo
+ _objc_msgSend$copyPropertyWithClass:key:
+ _objc_msgSend$initWithDevName:error:
+ _objc_msgSend$stringWithUTF8String:
+ _objc_msgSend$unsignedLongLongValue
- GCC_except_table27
- GCC_except_table30
- GCC_except_table31
- GCC_except_table33
- GCC_except_table64
- GCC_except_table67
- _OBJC_CLASS_$_NSLock
- ___57-[SAAppSizerResults postProcessFilteringWithAppPathList:]_block_invoke.306
- ___61-[SAPathManager registerPaths:forBundleID:completionHandler:]_block_invoke_5
- ___62-[SAPathManager unregisterURLs:forBundleID:completionHandler:]_block_invoke.142
- ___62-[SAPathManager unregisterURLs:forBundleID:completionHandler:]_block_invoke.142.cold.1
- ___62-[SAPathManager unregisterURLs:forBundleID:completionHandler:]_block_invoke_2
- ___62-[SAPathManager unregisterURLs:forBundleID:completionHandler:]_block_invoke_2.cold.1
- ___block_descriptor_64_e8_32bs40r48r56r_e17_v16?0"NSError"8lr40l8r48l8s32l8r56l8
CStrings:
+ "\x01G"
+ "%s:%s: Failed to find disk0 in the registry: %@"
+ "%s:%s: Failed to find size of disk0"
+ "%s:%s: spaceAvail %llu (capacity:%llu)"
+ "@32@0:8Q16^{fsid=[2i]}24"
+ "Bundle set %@ totalSize is 0"
+ "Clones Data"
+ "Size"
+ "T@\"NSMutableDictionary\",&,V_clonesInfo"
+ "_clonesInfo"
+ "clonesInfo"
+ "copyPropertyWithClass:key:"
+ "disk0"
+ "fsgetpath returned errno %d for nodeID %llu"
+ "getPathOfNodeID:FSid:"
+ "initWithDevName:error:"
+ "setClonesInfo:"
+ "stringWithUTF8String:"
+ "unsignedLongLongValue"
+ "zeroSizeAppsFiltering"
- "\x01F"
- "%s:%s:spaceAvail:%llu:capacity:%llu"

```
