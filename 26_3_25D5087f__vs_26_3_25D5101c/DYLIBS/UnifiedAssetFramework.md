## UnifiedAssetFramework

> `/System/Library/PrivateFrameworks/UnifiedAssetFramework.framework/Versions/A/UnifiedAssetFramework`

```diff

-3515.4.2.0.0
-  __TEXT.__text: 0x87cd4
+3515.6.1.0.0
+  __TEXT.__text: 0x87cec
   __TEXT.__auth_stubs: 0xfb0
-  __TEXT.__objc_methlist: 0x36c8
+  __TEXT.__objc_methlist: 0x36e8
   __TEXT.__const: 0x1c8
   __TEXT.__dlopen_cstrs: 0x296
-  __TEXT.__cstring: 0xb77f
+  __TEXT.__cstring: 0xb754
   __TEXT.__constg_swiftt: 0x48
   __TEXT.__swift5_typeref: 0x67
   __TEXT.__swift5_reflstr: 0x9
   __TEXT.__swift5_fieldmd: 0x1c
-  __TEXT.__oslogstring: 0xedc5
+  __TEXT.__oslogstring: 0xedf4
   __TEXT.__swift5_types: 0x4
   __TEXT.__gcc_except_tab: 0x1634
-  __TEXT.__unwind_info: 0x1480
+  __TEXT.__unwind_info: 0x1488
   __TEXT.__objc_classname: 0x483
-  __TEXT.__objc_methname: 0xa28b
-  __TEXT.__objc_methtype: 0x10b1
-  __TEXT.__objc_stubs: 0x82a0
+  __TEXT.__objc_methname: 0xa302
+  __TEXT.__objc_methtype: 0x10bf
+  __TEXT.__objc_stubs: 0x8300
   __DATA_CONST.__got: 0x5b8
-  __DATA_CONST.__const: 0x9c0
+  __DATA_CONST.__const: 0x9c8
   __DATA_CONST.__objc_classlist: 0x1a0
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2708
+  __DATA_CONST.__objc_selrefs: 0x2720
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xe8
-  __DATA_CONST.__objc_arraydata: 0xd8
+  __DATA_CONST.__objc_arraydata: 0x130
   __AUTH_CONST.__auth_got: 0x7e8
   __AUTH_CONST.__const: 0x1d38
-  __AUTH_CONST.__cfstring: 0x4a40
-  __AUTH_CONST.__objc_const: 0x4540
-  __AUTH_CONST.__objc_intobj: 0x120
-  __AUTH_CONST.__objc_arrayobj: 0x78
+  __AUTH_CONST.__cfstring: 0x4a60
+  __AUTH_CONST.__objc_const: 0x4558
+  __AUTH_CONST.__objc_intobj: 0x228
+  __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH.__objc_data: 0x390
   __AUTH.__data: 0xc8

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: C2B8A242-2A8B-349D-B5CB-A84FB7D57463
-  Functions: 1607
-  Symbols:   4154
-  CStrings:  4581
+  UUID: 350E210E-31A4-36FD-A3CB-F776129AD59C
+  Functions: 1608
+  Symbols:   4160
+  CStrings:  4590
 
Symbols:
+ +[UAFAssetSetStatus coalesceDownloadStatus:withDownloadStatus:]
+ +[UAFAssetSetStatus precedenceOfStatus:]
+ __OBJC_$_CLASS_METHODS_UAFAssetSetStatus
+ __OBJC_$_CLASS_PROP_LIST_UAFAssetSetStatus
+ _objc_msgSend$coalesceDownloadStatus:withDownloadStatus:
+ _objc_msgSend$indexOfObject:
+ _objc_msgSend$precedenceOfStatus:
- GCC_except_table96
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
