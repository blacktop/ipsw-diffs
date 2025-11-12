## PosterBoard

> `/System/Library/PrivateFrameworks/PosterBoard.framework/PosterBoard`

```diff

-304.2.3.101.0
-  __TEXT.__text: 0x1a1f58
-  __TEXT.__auth_stubs: 0x2a40
-  __TEXT.__objc_methlist: 0xc590
+304.2.5.100.0
+  __TEXT.__text: 0x1a2298
+  __TEXT.__auth_stubs: 0x2a30
+  __TEXT.__objc_methlist: 0xc5e8
   __TEXT.__const: 0x29c4
   __TEXT.__gcc_except_tab: 0x4b08
   __TEXT.__cstring: 0x14e1b

   __TEXT.__swift5_protos: 0x40
   __TEXT.__swift_as_entry: 0x10
   __TEXT.__swift_as_ret: 0x10
-  __TEXT.__unwind_info: 0x4ea8
+  __TEXT.__unwind_info: 0x4eb8
   __TEXT.__eh_frame: 0x960
-  __TEXT.__objc_classname: 0x2132
-  __TEXT.__objc_methname: 0x2a266
+  __TEXT.__objc_classname: 0x2156
+  __TEXT.__objc_methname: 0x2a30e
   __TEXT.__objc_methtype: 0x8ca7
-  __TEXT.__objc_stubs: 0x187c0
-  __DATA_CONST.__got: 0x1538
-  __DATA_CONST.__const: 0x4990
+  __TEXT.__objc_stubs: 0x18820
+  __DATA_CONST.__got: 0x1528
+  __DATA_CONST.__const: 0x49b8
   __DATA_CONST.__objc_classlist: 0x5f0
   __DATA_CONST.__objc_catlist: 0xc8
-  __DATA_CONST.__objc_protolist: 0x5a0
+  __DATA_CONST.__objc_protolist: 0x5a8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8670
+  __DATA_CONST.__objc_selrefs: 0x8690
   __DATA_CONST.__objc_protorefs: 0x218
   __DATA_CONST.__objc_superrefs: 0x338
   __DATA_CONST.__objc_arraydata: 0x1a0
-  __AUTH_CONST.__auth_got: 0x1530
-  __AUTH_CONST.__const: 0x5d00
-  __AUTH_CONST.__cfstring: 0xa460
-  __AUTH_CONST.__objc_const: 0x2da68
+  __AUTH_CONST.__auth_got: 0x1528
+  __AUTH_CONST.__const: 0x5ce0
+  __AUTH_CONST.__cfstring: 0xa440
+  __AUTH_CONST.__objc_const: 0x2daa8
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_dictobj: 0x190
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH.__objc_data: 0x1f60
   __AUTH.__data: 0x490
-  __DATA.__objc_ivar: 0xe28
-  __DATA.__data: 0x3e40
+  __DATA.__objc_ivar: 0xe2c
+  __DATA.__data: 0x3ea0
   __DATA.__bss: 0x830
   __DATA.__common: 0x90
   __DATA_DIRTY.__objc_data: 0x61e8
   __DATA_DIRTY.__data: 0x1008
   __DATA_DIRTY.__crash_info: 0x148
-  __DATA_DIRTY.__bss: 0x10c8
+  __DATA_DIRTY.__bss: 0x10b8
   __DATA_DIRTY.__common: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: A14358A1-5002-31A5-A54D-ABC3EB2AE150
-  Functions: 7398
-  Symbols:   19706
-  CStrings:  11474
+  UUID: CC2C32D7-E33E-3E41-B536-F111E781F167
+  Functions: 7403
+  Symbols:   19720
+  CStrings:  11478
 
Symbols:
+ -[PBFPosterGalleryAssetHelper _enumerateObservers:]
+ -[PBFPosterGalleryAssetHelper _enumerateObserversRespondingToSelector:enumerator:]
+ -[PBFPosterGalleryAssetHelper _notifyObserversDidUpdateAssetsForPosterPreviews:]
+ -[PBFPosterGalleryAssetHelper addObserver:]
+ -[PBFPosterGalleryAssetHelper removeObserver:]
+ -[_PBFGalleryCollectionViewController _buildSnapshotFromDataProvider:]
+ GCC_except_table122
+ GCC_except_table126
+ GCC_except_table138
+ GCC_except_table140
+ GCC_except_table150
+ GCC_except_table151
+ GCC_except_table152
+ GCC_except_table46
+ GCC_except_table85
+ _OBJC_IVAR_$_PBFPosterGalleryAssetHelper._observers
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_PBFPosterGalleryAssetHelperObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PBFPosterGalleryAssetHelperObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PBFPosterGalleryAssetHelperObserver
+ __OBJC_$_PROTOCOL_REFS_PBFPosterGalleryAssetHelperObserver
+ __OBJC_LABEL_PROTOCOL_$_PBFPosterGalleryAssetHelperObserver
+ __OBJC_PROTOCOL_$_PBFPosterGalleryAssetHelperObserver
+ ___110-[PBFPosterGalleryAssetHelper _receiveUpdatedAssetForPosterPreview:snapshotContext:snapshotBundle:fetchError:]_block_invoke
+ ___64-[PBFPosterGalleryAssetHelper _setupLiveDisplayStyleForPreview:]_block_invoke
+ ___block_descriptor_48_e8_32s40s_e47_v16?0"<PBFPosterGalleryAssetHelperObserver>"8ls32l8s40l8
+ ___block_literal_global.280
+ ___block_literal_global.308
+ ___block_literal_global.438
+ _objc_msgSend$_buildSnapshotFromDataProvider:
+ _objc_msgSend$_enumerateObservers:
+ _objc_msgSend$_notifyObserversDidUpdateAssetsForPosterPreviews:
+ _objc_msgSend$pf_unprotectedUserDefaults
- +[NSUserDefaults(PBFUtilities) pbf_unprotectedUserDefaults].cold.1
- -[PBFPosterGalleryDataProvider buildSnapshot]
- GCC_except_table115
- GCC_except_table119
- GCC_except_table120
- GCC_except_table137
- GCC_except_table139
- GCC_except_table143
- GCC_except_table144
- GCC_except_table86
- __CFPreferencesSetFileProtectionClass
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_PBFPosterGalleryAssetHelperDelegate
- ___59+[NSUserDefaults(PBFUtilities) pbf_unprotectedUserDefaults]_block_invoke
- ___block_literal_global.221
- ___block_literal_global.290
- ___block_literal_global.313
- ___block_literal_global.414
- ___block_literal_global.435
- _kCFPreferencesCurrentHost
- _kCFPreferencesCurrentUser
- _objc_msgSend$buildSnapshot
- _pbf_unprotectedUserDefaults.onceToken
- _pbf_unprotectedUserDefaults.unprotectedUserDefaults
CStrings:
+ "(%p) _sizeAssetsForActiveDisplayContext for %{public}@; notify observers of updated assets: %{public}@"
+ "(%p) bail _sizeAssetsForActiveDisplayContext for %{public}@; no updated poster previews to notify observers of"
+ "PBFPosterGalleryAssetHelperObserver"
+ "_buildSnapshotFromDataProvider:"
+ "_enumerateObservers:"
+ "_enumerateObserversRespondingToSelector:enumerator:"
+ "_notifyObserversDidUpdateAssetsForPosterPreviews:"
+ "pf_unprotectedUserDefaults"
+ "v16@?0@\"<PBFPosterGalleryAssetHelperObserver>\"8"
- "(%p) _sizeAssetsForActiveDisplayContext for %{public}@; notify delegate of updated assets: %{public}@"
- "(%p) bail _sizeAssetsForActiveDisplayContext for %{public}@; no updated poster previews to notify delegate of"
- "buildSnapshot"
- "com.apple.PosterBoard.unprotectedUserDefaults"

```
