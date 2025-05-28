## AXAssetLoader

> `/System/Library/PrivateFrameworks/AXAssetLoader.framework/AXAssetLoader`

```diff

-3093.2.4.4.11
+3093.23.0.0.0
   __TEXT.__text: 0x1292c
   __TEXT.__auth_stubs: 0x590
   __TEXT.__objc_methlist: 0x1020

   __TEXT.__dlopen_cstrs: 0x23a
   __TEXT.__unwind_info: 0x66c
   __TEXT.__objc_classname: 0x2d5
-  __TEXT.__objc_methname: 0x2fde
+  __TEXT.__objc_methname: 0x2ff0
   __TEXT.__objc_methtype: 0x5b5
   __TEXT.__objc_stubs: 0x2500
   __DATA_CONST.__got: 0x40

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x1510
   __DATA_CONST.__objc_selrefs: 0xb68
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0x100
+  __DATA_CONST.__objc_superrefs: 0x68
   __AUTH_CONST.__cfstring: 0xe00
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_const: 0x0
+  __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__auth_got: 0x2d8
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x100
-  __DATA.__objc_superrefs: 0x68
   __DATA.__objc_ivar: 0xd4
   __DATA.__data: 0x240
   __DATA.__bss: 0x8
-  __DATA_DIRTY.__const: 0x200
+  __DATA_DIRTY.__const: 0x1a0
   __DATA_DIRTY.__objc_const: 0x900
   __DATA_DIRTY.__objc_data: 0x6e0
   __DATA_DIRTY.__bss: 0xc0

   - /usr/lib/libobjc.A.dylib
   Functions: 505
   Symbols:   1796
-  CStrings:  819
+  CStrings:  820
 
Symbols:
+ ___122-[AXAssetController refreshAssetsByForceUpdatingCatalog:updatingCatalogIfNeeded:catalogRefreshOverrideTimeout:completion:]_block_invoke.250
+ ___53-[AXAssetController _queue_refreshAssets:completion:]_block_invoke.282
+ ___53-[AXAssetController _queue_refreshAssets:completion:]_block_invoke.283
+ ___66-[AXAssetController _updateCatalogWithOverrideTimeout:completion:]_block_invoke.288
+ ___66-[AXAssetController _updateCatalogWithOverrideTimeout:completion:]_block_invoke.292
+ ___69-[AXAssetController _replaceCachedAssetsWithAssets:error:completion:]_block_invoke.273
+ ___70-[AXAssetController downloadAssets:successStartBlock:completionBlock:]_block_invoke.267
+ ___block_literal_global.270
+ ___block_literal_global.285
- ___122-[AXAssetController refreshAssetsByForceUpdatingCatalog:updatingCatalogIfNeeded:catalogRefreshOverrideTimeout:completion:]_block_invoke.226
- ___53-[AXAssetController _queue_refreshAssets:completion:]_block_invoke.258
- ___53-[AXAssetController _queue_refreshAssets:completion:]_block_invoke.259
- ___66-[AXAssetController _updateCatalogWithOverrideTimeout:completion:]_block_invoke.264
- ___66-[AXAssetController _updateCatalogWithOverrideTimeout:completion:]_block_invoke.268
- ___69-[AXAssetController _replaceCachedAssetsWithAssets:error:completion:]_block_invoke.249
- ___70-[AXAssetController downloadAssets:successStartBlock:completionBlock:]_block_invoke.243
- ___block_literal_global.246
- ___block_literal_global.261
CStrings:
+ "T@\"NSString\",?,R,C"

```
