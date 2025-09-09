## PBBridgeSupport

> `/System/Library/PrivateFrameworks/PBBridgeSupport.framework/PBBridgeSupport`

```diff

-1303.0.0.0.0
-  __TEXT.__text: 0x42fb8
-  __TEXT.__auth_stubs: 0xbb0
+1303.1.0.0.0
+  __TEXT.__text: 0x430a4
+  __TEXT.__auth_stubs: 0xbd0
   __TEXT.__objc_methlist: 0x5124
-  __TEXT.__cstring: 0x5df5
-  __TEXT.__const: 0x920
+  __TEXT.__cstring: 0x5e02
+  __TEXT.__const: 0x9c0
   __TEXT.__oslogstring: 0x275d
   __TEXT.__gcc_except_tab: 0x200
   __TEXT.__dlopen_cstrs: 0x17c
   __TEXT.__ustring: 0xe
   __TEXT.__unwind_info: 0xf98
   __TEXT.__objc_classname: 0xb03
-  __TEXT.__objc_methname: 0x9261
+  __TEXT.__objc_methname: 0x926f
   __TEXT.__objc_methtype: 0x16c4
   __TEXT.__objc_stubs: 0x5620
   __DATA_CONST.__got: 0x5e8
-  __DATA_CONST.__const: 0x13e8
+  __DATA_CONST.__const: 0x1408
   __DATA_CONST.__objc_classlist: 0x290
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x40

   __DATA_CONST.__objc_selrefs: 0x2528
   __DATA_CONST.__objc_superrefs: 0x248
   __DATA_CONST.__objc_arraydata: 0x48
-  __AUTH_CONST.__auth_got: 0x5e8
+  __AUTH_CONST.__auth_got: 0x5f8
   __AUTH_CONST.__const: 0x3c0
-  __AUTH_CONST.__cfstring: 0x5800
+  __AUTH_CONST.__cfstring: 0x5840
   __AUTH_CONST.__objc_const: 0x7178
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x48

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C23F5A29-CE04-3439-AB58-6114DF491AF1
+  UUID: ABAC565F-6E0B-3FFD-8D4F-5B260333C295
   Functions: 1838
-  Symbols:   5792
-  CStrings:  3719
+  Symbols:   5794
+  CStrings:  3723
 
Symbols:
+ -[PBBridgeAssetsManager _startAssetDownload:downloadGroup:]
+ ___59-[PBBridgeAssetsManager _startAssetDownload:downloadGroup:]_block_invoke
+ ___59-[PBBridgeAssetsManager _startAssetDownload:downloadGroup:]_block_invoke.310
+ ___block_literal_global.252
+ _dispatch_group_enter
+ _dispatch_group_leave
+ _objc_msgSend$_startAssetDownload:downloadGroup:
- -[PBBridgeAssetsManager _startAssetDownload:]
- ___45-[PBBridgeAssetsManager _startAssetDownload:]_block_invoke
- ___45-[PBBridgeAssetsManager _startAssetDownload:]_block_invoke.310
- ___block_literal_global.249
- _objc_msgSend$_startAssetDownload:
Functions:
~ -[PBBridgeWatchAttributeController init] : 1336 -> 1376
~ -[PBBridgeWatchAttributeController setDevice:] : 972 -> 996
~ -[PBBridgeWatchAttributeController fallbackMaterialForSize:] : 36 -> 44
~ +[PBBridgeWatchAttributeController sizeFromDevice:] : 532 -> 552
~ +[PBBridgeWatchAttributeController sizeFromPdrDevice:] : 456 -> 476
~ -[PBBridgeAssetsManager beginPullingAssetsForDeviceMaterial:size:completion:] : 292 -> 304
~ -[PBBridgeAssetsManager _beginAssetDownloads:] : 512 -> 532
~ ___46-[PBBridgeAssetsManager _beginAssetDownloads:]_block_invoke : 368 -> 372
~ -[PBBridgeAssetsManager _startAssetDownload:] -> -[PBBridgeAssetsManager _startAssetDownload:downloadGroup:] : 380 -> 376
~ ___45-[PBBridgeAssetsManager _startAssetDownload:]_block_invoke -> ___59-[PBBridgeAssetsManager _startAssetDownload:downloadGroup:]_block_invoke : 324 -> 336
~ ___45-[PBBridgeAssetsManager _startAssetDownload:]_block_invoke.310 -> ___59-[PBBridgeAssetsManager _startAssetDownload:downloadGroup:]_block_invoke.310 : 12 -> 64
~ -[PBBridgeProgressView _size] : 256 -> 284
CStrings:
+ "-M28"
+ "Alum-41"
+ "_startAssetDownload:downloadGroup:"
- "_startAssetDownload:"

```
