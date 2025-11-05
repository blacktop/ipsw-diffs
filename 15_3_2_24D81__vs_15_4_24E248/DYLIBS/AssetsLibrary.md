## AssetsLibrary

> `/System/iOSSupport/System/Library/Frameworks/AssetsLibrary.framework/Versions/A/AssetsLibrary`

```diff

-741.0.130.0.0
-  __TEXT.__text: 0x9e60
-  __TEXT.__auth_stubs: 0x4f0
-  __TEXT.__objc_methlist: 0x994
+751.0.104.0.0
+  __TEXT.__text: 0x9e44
+  __TEXT.__auth_stubs: 0x510
+  __TEXT.__objc_methlist: 0xae4
+  __TEXT.__dlopen_cstrs: 0x43
   __TEXT.__const: 0x58
   __TEXT.__gcc_except_tab: 0x4cc
   __TEXT.__cstring: 0x850
   __TEXT.__oslogstring: 0xab
-  __TEXT.__dlopen_cstrs: 0x43
-  __TEXT.__unwind_info: 0x580
+  __TEXT.__unwind_info: 0x578
   __TEXT.__objc_classname: 0x119
   __TEXT.__objc_methname: 0x2358
   __TEXT.__objc_methtype: 0x440

   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9c0
+  __DATA_CONST.__objc_selrefs: 0xa60
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x48
-  __AUTH_CONST.__auth_got: 0x288
+  __AUTH_CONST.__auth_got: 0x298
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x6a0
-  __AUTH_CONST.__objc_const: 0x10d8
+  __AUTH_CONST.__objc_const: 0xe78
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x320
   __DATA.__objc_ivar: 0x80

   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 958A44CA-DE78-3603-BD2E-18868725903F
-  Functions: 296
-  Symbols:   947
+  UUID: 37F95E4F-992F-3B79-B956-020808267E6B
+  Functions: 295
+  Symbols:   949
   CStrings:  597
 
Symbols:
+ _objc_release_x2
+ _objc_release_x3
Functions:
~ ___42-[ALAsset setVideoAtPath:completionBlock:]_block_invoke : 584 -> 588
~ ___49-[ALAsset setImageData:metadata:completionBlock:]_block_invoke : 584 -> 588
~ ___28-[ALAsset valueForProperty:]_block_invoke : 864 -> 852
~ -[ALAssetsGroup addAsset:] : 332 -> 324
~ ___26-[ALAssetsGroup addAsset:]_block_invoke : 284 -> 288
~ ___28-[ALAssetsGroup posterImage]_block_invoke : 104 -> 108
- sub_2633095d8
~ ___72-[ALAssetsLibrary addAssetsGroupAlbumWithName:resultBlock:failureBlock:]_block_invoke_2 : 260 -> 264
~ ___72-[ALAssetsLibrary addAssetsGroupAlbumWithName:resultBlock:failureBlock:]_block_invoke_4 : 208 -> 212
~ ___56-[ALAssetsLibrary assetForURL:resultBlock:failureBlock:]_block_invoke_2 : 368 -> 372
~ ___90-[ALAssetsLibrary _writeVideoAtPathToSavedPhotosAlbum:internalProperties:completionBlock:]_block_invoke_2 : 364 -> 368
~ ___68-[ALAssetsLibrary enumerateGroupsWithTypes:usingBlock:failureBlock:]_block_invoke_9 : 424 -> 432
~ +[ALAssetsLibrary _linkedBefore7] : 68 -> 72
~ ___53-[ALAssetRepresentationPrivate _performBlockAndWait:]_block_invoke_2 : 212 -> 208
~ ___39-[ALAssetPrivate _performBlockAndWait:]_block_invoke_2 : 136 -> 132
~ ___45-[ALAssetsGroupPrivate _performBlockAndWait:]_block_invoke_2 : 328 -> 324
~ -[ALAssetsGroupPrivate setAssetsFilter:] : 92 -> 84

```
