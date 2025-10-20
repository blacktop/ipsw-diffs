## MediaControls

> `/System/Library/PrivateFrameworks/MediaControls.framework/MediaControls`

```diff

-4025.210.17.2.0
-  __TEXT.__text: 0x1e388c
-  __TEXT.__auth_stubs: 0x3910
-  __TEXT.__objc_methlist: 0x152bc
+4025.210.2.0.0
+  __TEXT.__text: 0x1e5f38
+  __TEXT.__auth_stubs: 0x38e0
+  __TEXT.__objc_methlist: 0x152d4
   __TEXT.__cstring: 0x973d
   __TEXT.__ustring: 0x22
-  __TEXT.__const: 0x9424
+  __TEXT.__const: 0x9d14
   __TEXT.__gcc_except_tab: 0x1844
   __TEXT.__oslogstring: 0x7c39
   __TEXT.__dlopen_cstrs: 0x64
-  __TEXT.__constg_swiftt: 0x68b0
-  __TEXT.__swift5_typeref: 0x2c80
+  __TEXT.__constg_swiftt: 0x6888
+  __TEXT.__swift5_typeref: 0x2c58
   __TEXT.__swift5_reflstr: 0x3c93
-  __TEXT.__swift5_fieldmd: 0x4004
+  __TEXT.__swift5_fieldmd: 0x3ff8
   __TEXT.__swift5_types: 0x4c4
-  __TEXT.__swift5_capture: 0xf40
+  __TEXT.__swift5_capture: 0xf54
   __TEXT.__swift5_protos: 0xa4
   __TEXT.__swift5_proto: 0x500
   __TEXT.__swift5_builtin: 0x2a8

   __TEXT.__swift_as_entry: 0x2c
   __TEXT.__swift_as_ret: 0x28
   __TEXT.__swift5_assocty: 0x2e8
-  __TEXT.__unwind_info: 0x7ab8
+  __TEXT.__unwind_info: 0x7ab0
   __TEXT.__eh_frame: 0x1468
   __TEXT.__objc_classname: 0x267f
-  __TEXT.__objc_methname: 0x3022f
+  __TEXT.__objc_methname: 0x30254
   __TEXT.__objc_methtype: 0x7ef3
-  __TEXT.__objc_stubs: 0x1bc20
+  __TEXT.__objc_stubs: 0x1bc40
   __DATA_CONST.__got: 0x16d0
   __DATA_CONST.__const: 0x2f48
   __DATA_CONST.__objc_classlist: 0x948
   __DATA_CONST.__objc_catlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x450
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa2c8
+  __DATA_CONST.__objc_selrefs: 0xa2d0
   __DATA_CONST.__objc_protorefs: 0xa8
   __DATA_CONST.__objc_superrefs: 0x5f0
   __DATA_CONST.__objc_arraydata: 0x1b8
-  __AUTH_CONST.__auth_got: 0x1c98
-  __AUTH_CONST.__const: 0x8df0
+  __AUTH_CONST.__auth_got: 0x1c80
+  __AUTH_CONST.__const: 0x8e18
   __AUTH_CONST.__cfstring: 0x4fe0
-  __AUTH_CONST.__objc_const: 0x41ab0
+  __AUTH_CONST.__objc_const: 0x41a90
   __AUTH_CONST.__objc_intobj: 0x2b8
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_doubleobj: 0xf0

   __AUTH.__objc_data: 0x60e0
   __AUTH.__data: 0xaf8
   __DATA.__objc_ivar: 0x1870
-  __DATA.__data: 0x3c58
+  __DATA.__data: 0x41b0
   __DATA.__bss: 0x71e0
   __DATA.__common: 0x4c0
   __DATA_DIRTY.__objc_data: 0x41f8
-  __DATA_DIRTY.__data: 0x2f18
+  __DATA_DIRTY.__data: 0x2968
   __DATA_DIRTY.__bss: 0x21c8
   __DATA_DIRTY.__common: 0x9b8
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: A2643FBB-9876-35E5-85EF-8E8BAF532496
-  Functions: 13110
-  Symbols:   24903
-  CStrings:  11308
+  UUID: 1865E909-22D0-3202-8900-652831E828A0
+  Functions: 13114
+  Symbols:   24910
+  CStrings:  11307
 
Symbols:
+ +[MRUVisualStylingProvider stylingProviderForLockScreenPlatters]
+ __OBJC_$_CLASS_METHODS_MRUVisualStylingProvider
+ ___swift_instantiateConcreteTypeFromMangledNameAbstractV2
+ ___swift_instantiateConcreteTypeFromMangledNameV2
+ _objc_msgSend$stylingProviderForLockScreenPlatters
+ _symbolic _____ 12MediaControl12ArtworkTokenC
+ _symbolic ______pSg s5ErrorP
- ___swift_instantiateConcreteTypeFromMangledName
- ___swift_instantiateConcreteTypeFromMangledNameAbstract
- _symbolic SDySS_____G 12MediaControl13ArtworkLoaderC
- _symbolic _____SgXw 13MediaControls25SessionArtworksDataSourceC
- _symbolic _____SgXwz_Xx 13MediaControls25SessionArtworksDataSourceC
- _symbolic _____ySS_____G s18_DictionaryStorageC 12MediaControl13ArtworkLoaderC
CStrings:
+ "[%s] didLoadImage(%s) for %s - no presentation matches token, skipping."
+ "[%s] didLoadImage(%s) for %s - will update images for matching presentations."
+ "[%s] loadImage for %s"
+ "[%s] loadImage for %s - already loading image for %s, skipping."
+ "[%s] loadImage for %s - failed with error: %@"
+ "[%s] loadImage for %s - loadingTokens: %s"
+ "[%s] loadImage for %s - will load image for %s"
+ "[%s] setupResetTaskIfNeeded for %s - reset task timed out, clearing existing image"
+ "stylingProviderForLockScreenPlatters"
- "[%s] didLoadImage(%s) for %s"
- "[%s] didLoadImage(%s), presentation: %s - token is nil, updating image to nil."
- "[%s] loadImage for %s - already loading image for token, skipping."
- "[%s] loadImage for %s - loader would not load a new image, skipping."
- "[%s] loadImage for %s - loading: %s"
- "[%s] loadImage for %s - will load a new image."
- "[%s] loadImage for %s, token:%s"
- "[%s] resetTask(%s) timed out, clearing existing image"
- "[%s] setUpLoader for %s"

```
