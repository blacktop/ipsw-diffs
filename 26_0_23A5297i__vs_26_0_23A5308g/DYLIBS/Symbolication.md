## Symbolication

> `/System/Library/PrivateFrameworks/Symbolication.framework/Symbolication`

```diff

-64572.134.1.0.0
-  __TEXT.__text: 0xb0834
+64572.137.1.0.0
+  __TEXT.__text: 0xb089c
   __TEXT.__auth_stubs: 0x2410
-  __TEXT.__objc_methlist: 0x65c0
+  __TEXT.__objc_methlist: 0x65d0
   __TEXT.__const: 0x2b6
   __TEXT.__cstring: 0xff88
   __TEXT.__gcc_except_tab: 0x4ebc

   __TEXT.__swift5_types: 0x14
   __TEXT.__unwind_info: 0x2940
   __TEXT.__objc_classname: 0x83a
-  __TEXT.__objc_methname: 0xf42d
-  __TEXT.__objc_methtype: 0x5e7c
+  __TEXT.__objc_methname: 0xf440
+  __TEXT.__objc_methtype: 0x5e7d
   __TEXT.__objc_stubs: 0x9a00
   __DATA_CONST.__got: 0x458
   __DATA_CONST.__const: 0x35f8

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3560
+  __DATA_CONST.__objc_selrefs: 0x3568
   __DATA_CONST.__objc_superrefs: 0x200
   __DATA_CONST.__objc_arraydata: 0x870
   __AUTH_CONST.__auth_got: 0x1220

   __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH.__objc_data: 0x4a0
+  __AUTH.__objc_data: 0x4f0
   __AUTH.__data: 0x50
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x8

   __DATA.__data: 0xd58
   __DATA.__bss: 0x548
   __DATA.__common: 0xf9
-  __DATA_DIRTY.__objc_data: 0x17c0
+  __DATA_DIRTY.__objc_data: 0x1770
   __DATA_DIRTY.__crash_info: 0x148
   __DATA_DIRTY.__bss: 0xe8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 2F6D5596-0601-3FED-9FB3-80F939E23DD4
-  Functions: 3119
-  Symbols:   10531
-  CStrings:  7742
+  UUID: 04364C94-600F-3AB3-9D2A-A647BFCE329B
+  Functions: 3120
+  Symbols:   10533
+  CStrings:  7743
 
Symbols:
+ -[VMUVMRegion isReadonlyAndClean]
+ ___32-[VMULeakDetector buildLeakTree]_block_invoke.63
+ ___32-[VMULeakDetector buildLeakTree]_block_invoke.68
+ ___32-[VMULeakDetector buildLeakTree]_block_invoke.79
+ ___32-[VMULeakDetector buildLeakTree]_block_invoke.87
+ ___40-[VMULeakDetector detectLeaksWithError:]_block_invoke.157
+ ___block_literal_global.134
- ___32-[VMULeakDetector buildLeakTree]_block_invoke.64
- ___32-[VMULeakDetector buildLeakTree]_block_invoke.70
- ___32-[VMULeakDetector buildLeakTree]_block_invoke.80
- ___32-[VMULeakDetector buildLeakTree]_block_invoke.88
- ___40-[VMULeakDetector detectLeaksWithError:]_block_invoke.158
- ___block_literal_global.135
Functions:
~ -[VMUTaskMemoryScanner mapDyldSharedCacheFromTargetWithRegions:] : 460 -> 500
~ -[VMUTaskMemoryScanner _removeFalsePositiveLeakedVMregionsFromNodes:nodeCount:recorder:] : 1132 -> 1148
~ +[VMULeakDetector referenceDescription:dstDescription:is64bit:] : 532 -> 444
~ -[VMUClassInfo _parseIvarsAndLayouts] : 96 -> 184
+ -[VMUVMRegion isReadonlyAndClean]
CStrings:
+ "%@%@ --> %@"
+ "i48@0:8^Q16^Q24^I32^{vm_region_submap_short_info_64=iiIQIISCCiiISS}40"
+ "isReadonlyAndClean"
- "%@%@%s --> %@"
- "i48@0:8^Q16^Q24^I32^{vm_region_submap_short_info_64=iiIQIISCCiiIS}40"

```
