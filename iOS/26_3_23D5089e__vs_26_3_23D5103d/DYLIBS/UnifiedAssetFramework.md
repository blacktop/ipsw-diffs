## UnifiedAssetFramework

> `/System/Library/PrivateFrameworks/UnifiedAssetFramework.framework/UnifiedAssetFramework`

```diff

-3515.4.2.0.0
-  __TEXT.__text: 0x7be30
+3515.6.1.0.0
+  __TEXT.__text: 0x7be38
   __TEXT.__auth_stubs: 0x1160
-  __TEXT.__objc_methlist: 0x3748
+  __TEXT.__objc_methlist: 0x3768
   __TEXT.__const: 0x1c0
   __TEXT.__dlopen_cstrs: 0x296
-  __TEXT.__cstring: 0xb791
+  __TEXT.__cstring: 0xb766
   __TEXT.__constg_swiftt: 0x48
   __TEXT.__swift5_typeref: 0x67
   __TEXT.__swift5_reflstr: 0x9
   __TEXT.__swift5_fieldmd: 0x1c
-  __TEXT.__oslogstring: 0xeb1d
+  __TEXT.__oslogstring: 0xeb4c
   __TEXT.__swift5_types: 0x4
   __TEXT.__gcc_except_tab: 0x15d0
-  __TEXT.__unwind_info: 0x13e0
+  __TEXT.__unwind_info: 0x13e8
   __TEXT.__objc_classname: 0x483
-  __TEXT.__objc_methname: 0xa297
-  __TEXT.__objc_methtype: 0x10dd
-  __TEXT.__objc_stubs: 0x8380
+  __TEXT.__objc_methname: 0xa30e
+  __TEXT.__objc_methtype: 0x10eb
+  __TEXT.__objc_stubs: 0x83e0
   __DATA_CONST.__got: 0x578
-  __DATA_CONST.__const: 0x1eb8
+  __DATA_CONST.__const: 0x1ec0
   __DATA_CONST.__objc_classlist: 0x1a0
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2748
+  __DATA_CONST.__objc_selrefs: 0x2760
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xe8
-  __DATA_CONST.__objc_arraydata: 0xd8
+  __DATA_CONST.__objc_arraydata: 0x130
   __AUTH_CONST.__auth_got: 0x8c0
   __AUTH_CONST.__const: 0x668
-  __AUTH_CONST.__cfstring: 0x4be0
-  __AUTH_CONST.__objc_const: 0x4540
-  __AUTH_CONST.__objc_intobj: 0x138
-  __AUTH_CONST.__objc_arrayobj: 0x78
+  __AUTH_CONST.__cfstring: 0x4c00
+  __AUTH_CONST.__objc_const: 0x4558
+  __AUTH_CONST.__objc_intobj: 0x240
+  __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH.__objc_data: 0x3e0
   __AUTH.__data: 0xc8

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 6F0CFC02-345A-32E7-8F19-A10AEFE3D45C
-  Functions: 1552
-  Symbols:   5674
-  CStrings:  4604
+  UUID: 6F8DB8B3-9468-32BA-B324-EFF536610AF9
+  Functions: 1553
+  Symbols:   5681
+  CStrings:  4613
 
Symbols:
+ +[UAFAssetSetStatus coalesceDownloadStatus:withDownloadStatus:]
+ +[UAFAssetSetStatus precedenceOfStatus:]
+ GCC_except_table92
+ __OBJC_$_CLASS_METHODS_UAFAssetSetStatus
+ __OBJC_$_CLASS_PROP_LIST_UAFAssetSetStatus
+ _objc_msgSend$coalesceDownloadStatus:withDownloadStatus:
+ _objc_msgSend$indexOfObject:
+ _objc_msgSend$precedenceOfStatus:
- GCC_except_table78
- GCC_except_table93
- ___86+[UAFAutoAssetManager stageAssetsWithNewSubscriptions:oldSubscriptions:autoAssetSets:]_block_invoke
CStrings:
+ "%s Failed to get precedence of status: %@ (%@)"
+ "+[UAFAssetSetStatus precedenceOfStatus:]"
+ "Q32@0:8Q16Q24"
+ "T@\"NSArray\",R,N"
+ "coalesceDownloadStatus:withDownloadStatus:"
+ "device locked"
+ "downloadStatusPrecedence"
+ "indexOfObject:"
+ "precedenceOfStatus:"
+ "undefined status"
- "+[UAFAutoAssetManager stageAssetsWithNewSubscriptions:oldSubscriptions:autoAssetSets:]_block_invoke"
- "unknown status"

```
