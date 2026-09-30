## CoreUI

> `/System/Library/PrivateFrameworks/CoreUI.framework/CoreUI`

```diff

-971.4.0.0.0
-  __TEXT.__text: 0xc9d44
-  __TEXT.__auth_stubs: 0x2be0
+971.6.0.0.0
+  __TEXT.__text: 0xca1d8
+  __TEXT.__auth_stubs: 0x2c10
   __TEXT.__delay_stubs: 0x2c
   __TEXT.__delay_helper: 0xa4
   __TEXT.__objc_methlist: 0xa298
-  __TEXT.__const: 0x4f70
-  __TEXT.__gcc_except_tab: 0x1614
-  __TEXT.__cstring: 0x2539b
+  __TEXT.__const: 0x4fd8
+  __TEXT.__gcc_except_tab: 0x1624
+  __TEXT.__cstring: 0x254cb
   __TEXT.__oslogstring: 0x200
+  __TEXT.__dlopen_cstrs: 0x4f
   __TEXT.__constg_swiftt: 0x33c
   __TEXT.__swift5_typeref: 0x392
   __TEXT.__swift5_reflstr: 0x132

   __TEXT.__swift5_capture: 0x15c
   __TEXT.__swift5_proto: 0x20
   __TEXT.__swift5_assocty: 0x58
-  __TEXT.__unwind_info: 0x3900
+  __TEXT.__unwind_info: 0x3918
   __TEXT.__eh_frame: 0x130
   __TEXT.__objc_classname: 0x10e8
   __TEXT.__objc_methname: 0x16350
   __TEXT.__objc_methtype: 0x5f9b
   __TEXT.__objc_stubs: 0xe820
   __DATA_CONST.__got: 0x9e0
-  __DATA_CONST.__const: 0xe858
+  __DATA_CONST.__const: 0xe8e0
   __DATA_CONST.__objc_classlist: 0x500
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x70

   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x4a8
   __DATA_CONST.__objc_arraydata: 0xbc0
-  __AUTH_CONST.__auth_got: 0x1610
+  __AUTH_CONST.__auth_got: 0x1628
   __AUTH_CONST.__const: 0x3170
-  __AUTH_CONST.__cfstring: 0x11f40
+  __AUTH_CONST.__cfstring: 0x11f60
   __AUTH_CONST.__objc_const: 0xefe8
   __AUTH_CONST.__objc_intobj: 0x2d0
   __AUTH_CONST.__objc_doubleobj: 0x20

   __DATA.__objc_ivar: 0xc04
   __DATA.__data: 0x77c
   __DATA.__common: 0x8
-  __DATA.__bss: 0x7a8
+  __DATA.__bss: 0x7b8
   __DATA_DIRTY.__objc_data: 0xfa0
   __DATA_DIRTY.__crash_info: 0x148
   __DATA_DIRTY.__bss: 0x3b8

   - /System/Library/PrivateFrameworks/CoreSVG.framework/CoreSVG
   - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
   - /System/Library/PrivateFrameworks/InternationalSupport.framework/InternationalSupport
+  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/TextureIO.framework/TextureIO
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: B1091097-46A5-33D4-8C4B-98F811BCEEC6
-  Functions: 5309
-  Symbols:   15850
-  CStrings:  12112
+  UUID: F33CEE3C-2E69-3945-8B59-B8E7AE87FD99
+  Functions: 5313
+  Symbols:   15868
+  CStrings:  12119
 
Symbols:
+ _CGPathCreateWithRect
+ _CoreGraphicsLibraryCore.frameworkLibrary
+ __CUICreateNewContinuousRoundedRect.cold.1
+ ___CoreGraphicsLibraryCore_block_invoke
+ ___block_descriptor_40_e5_v8?0l
+ ___block_descriptor_40_e8_32r_e5_v8?0lr32l8
+ ___block_descriptor_56_e8_32o_e45_"CUIRenditionKey"24?0"CUIRenditionKey"8d16ls32l8
+ ___getCGPathCreateWithContinuousRoundedRectSymbolLoc_block_invoke
+ ___getCGPathCreateWithContinuousRoundedRectSymbolLoc_block_invoke.cold.1
+ ___swift_instantiateConcreteTypeFromMangledNameAbstractV2
+ ___swift_instantiateConcreteTypeFromMangledNameV2
+ __sl_dlopen
+ _audit_stringCoreGraphics
+ _dlerror
+ _dlsym
+ _getCGPathCreateWithContinuousRoundedRectSymbolLoc.ptr
- _CGPathCreateWithContinuousRoundedRect
- ___swift_instantiateConcreteTypeFromMangledName
- ___swift_instantiateConcreteTypeFromMangledNameAbstract
CStrings:
+ "CGPathCreateWithContinuousRoundedRect"
+ "CGPathRef soft_CGPathCreateWithContinuousRoundedRect(CGRect, CGFloat, CGFloat, const CGAffineTransform * _Nullable)"
+ "CUIContinuousCurves.m"
+ "Failed to find CGPathCreateWithContinuousRoundedRect, falling back to a standard rect. LAR=%d"
+ "softlink:r:path:/System/Library/Frameworks/CoreGraphics.framework/CoreGraphics"
+ "void *CoreGraphicsLibrary(void)"

```
