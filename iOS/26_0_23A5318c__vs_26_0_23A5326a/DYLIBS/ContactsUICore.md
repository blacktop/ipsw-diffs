## ContactsUICore

> `/System/Library/PrivateFrameworks/ContactsUICore.framework/ContactsUICore`

```diff

-3683.100.1.2.4
-  __TEXT.__text: 0x2cbaf4
-  __TEXT.__auth_stubs: 0x6f50
-  __TEXT.__objc_methlist: 0x967c
-  __TEXT.__const: 0x21c84
-  __TEXT.__oslogstring: 0x6c52
-  __TEXT.__cstring: 0xd3a6
+3683.100.1.2.6
+  __TEXT.__text: 0x2cce00
+  __TEXT.__auth_stubs: 0x6f90
+  __TEXT.__objc_methlist: 0x9694
+  __TEXT.__const: 0x21cb4
+  __TEXT.__oslogstring: 0x6cb2
+  __TEXT.__cstring: 0xd476
   __TEXT.__gcc_except_tab: 0xd58
   __TEXT.__dlopen_cstrs: 0xb73
-  __TEXT.__constg_swiftt: 0x9ac4
-  __TEXT.__swift5_typeref: 0x2432c
+  __TEXT.__constg_swiftt: 0x9b1c
+  __TEXT.__swift5_typeref: 0x2439a
   __TEXT.__swift5_builtin: 0x258
-  __TEXT.__swift5_reflstr: 0x5b3a
-  __TEXT.__swift5_fieldmd: 0x6d98
+  __TEXT.__swift5_reflstr: 0x5b9a
+  __TEXT.__swift5_fieldmd: 0x6dc8
   __TEXT.__swift5_assocty: 0x1fc8
   __TEXT.__swift5_proto: 0x11c4
   __TEXT.__swift5_types: 0x91c
   __TEXT.__swift5_protos: 0xb0
   __TEXT.__swift_as_entry: 0x370
   __TEXT.__swift_as_ret: 0x320
-  __TEXT.__swift5_capture: 0x1f9c
+  __TEXT.__swift5_capture: 0x1fac
   __TEXT.__swift5_mpenum: 0x128
-  __TEXT.__unwind_info: 0xb078
+  __TEXT.__unwind_info: 0xb0c0
   __TEXT.__eh_frame: 0xa09c
   __TEXT.__objc_classname: 0x2410
-  __TEXT.__objc_methname: 0x19b44
+  __TEXT.__objc_methname: 0x19c2a
   __TEXT.__objc_methtype: 0x45fe
-  __TEXT.__objc_stubs: 0x10120
-  __DATA_CONST.__got: 0x2658
+  __TEXT.__objc_stubs: 0x10140
+  __DATA_CONST.__got: 0x2670
   __DATA_CONST.__const: 0x3760
   __DATA_CONST.__objc_classlist: 0x9d0
   __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0x3b0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5aa8
+  __DATA_CONST.__objc_selrefs: 0x5ad0
   __DATA_CONST.__objc_protorefs: 0x118
   __DATA_CONST.__objc_superrefs: 0x490
   __DATA_CONST.__objc_arraydata: 0xc0
-  __AUTH_CONST.__auth_got: 0x37b8
-  __AUTH_CONST.__const: 0x12fe0
+  __AUTH_CONST.__auth_got: 0x37d8
+  __AUTH_CONST.__const: 0x13030
   __AUTH_CONST.__cfstring: 0x29c0
-  __AUTH_CONST.__objc_const: 0x16ec8
+  __AUTH_CONST.__objc_const: 0x16f78
   __AUTH_CONST.__objc_intobj: 0x330
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_doubleobj: 0x50
   __AUTH.__objc_data: 0x52d0
-  __AUTH.__data: 0x6c98
-  __DATA.__objc_ivar: 0x6ec
-  __DATA.__data: 0xcb30
+  __AUTH.__data: 0x6d08
+  __DATA.__objc_ivar: 0x6f0
+  __DATA.__data: 0xcb40
   __DATA.__objc_stublist: 0x18
   __DATA.__bss: 0x200c8
   __DATA.__common: 0x1330

   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreImage.framework/CoreImage
+  - /System/Library/Frameworks/CoreML.framework/CoreML
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight
   - /System/Library/Frameworks/CoreText.framework/CoreText

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 4CA605FF-2302-3C22-821E-7964DAB37CB2
-  Functions: 16330
-  Symbols:   19500
-  CStrings:  7055
+  UUID: 276D8739-1EEB-33B4-B7A9-96FB73ADC1A9
+  Functions: 16349
+  Symbols:   19518
+  CStrings:  7070
 
Symbols:
+ -[CNUIPhotosPosterConfigurationReader setVisiblePreviewImageFaceRect:]
+ -[CNUIPhotosPosterConfigurationReader visiblePreviewImageFaceRect]
+ _CARenderRelease
+ _OBJC_CLASS_$_VNSession
+ _OBJC_IVAR_$_CNUIPhotosPosterConfigurationReader._visiblePreviewImageFaceRect
+ _VNComputeStageMain
+ _objc_msgSend$fullExtentPreviewImageFaceRect
+ _symbolic So29VNDetectFaceRectanglesRequestCSg
+ _symbolic So44VNGenerateAttentionBasedSaliencyImageRequestCSg
+ _symbolic _____Sg 6CoreML15MLComputeDeviceO
+ _symbolic _____SgXw 14ContactsUICore22PosterSaliencyAnalyzerC
- GCC_except_table22
CStrings:
+ "$__lazy_storage_$_faceRequest"
+ "$__lazy_storage_$_saliencyRequest"
+ "Can't use real time GPU processing"
+ "Failed to prewarm PosterSaliencyAnalyzer: %@"
+ "Prewarm PosterSaliencyAnalyzer"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_visiblePreviewImageFaceRect"
+ "_visiblePreviewImageFaceRect"
+ "com.apple.ContactsUICore.PosterSaliencyAnalyzer.prewarm"
+ "globalSession"
+ "isPrewarmed"
+ "prepareForPerformingRequests:error:"
+ "prewarmQueue"
+ "setMetalContextPriority:"
+ "setVisiblePreviewImageFaceRect:"
+ "visiblePreviewImageFaceRect"

```
