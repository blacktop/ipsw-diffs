## Pegasus

> `/System/Library/PrivateFrameworks/Pegasus.framework/Pegasus`

```diff

-293.2.1.0.0
-  __TEXT.__text: 0x4147c
-  __TEXT.__auth_stubs: 0x8d0
-  __TEXT.__objc_methlist: 0x4394
-  __TEXT.__const: 0x1d0
-  __TEXT.__cstring: 0x4660
+297.0.0.0.0
+  __TEXT.__text: 0x42b04
+  __TEXT.__auth_stubs: 0xa90
+  __TEXT.__objc_methlist: 0x43dc
+  __TEXT.__const: 0x1ea
+  __TEXT.__cstring: 0x468e
   __TEXT.__oslogstring: 0x1acc
   __TEXT.__gcc_except_tab: 0x5e4
   __TEXT.__dlopen_cstrs: 0x52
-  __TEXT.__unwind_info: 0x13f8
-  __TEXT.__objc_classname: 0x8b8
-  __TEXT.__objc_methname: 0xd8f8
-  __TEXT.__objc_methtype: 0x2764
-  __TEXT.__objc_stubs: 0x8f40
-  __DATA_CONST.__got: 0x430
-  __DATA_CONST.__const: 0x1b58
+  __TEXT.__swift5_typeref: 0x1c
+  __TEXT.__swift5_capture: 0x24
+  __TEXT.__unwind_info: 0x1440
+  __TEXT.__objc_classname: 0x8b4
+  __TEXT.__objc_methname: 0xda63
+  __TEXT.__objc_methtype: 0x276b
+  __TEXT.__objc_stubs: 0x9060
+  __DATA_CONST.__got: 0x440
+  __DATA_CONST.__const: 0x1bf0
   __DATA_CONST.__objc_classlist: 0x1a8
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0xc8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2b38
+  __DATA_CONST.__objc_selrefs: 0x2b90
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x190
+  __DATA_CONST.__objc_superrefs: 0x198
   __DATA_CONST.__objc_arraydata: 0x70
-  __AUTH_CONST.__auth_got: 0x478
-  __AUTH_CONST.__const: 0x3c0
+  __AUTH_CONST.__auth_got: 0x558
+  __AUTH_CONST.__const: 0x438
   __AUTH_CONST.__cfstring: 0x2e20
-  __AUTH_CONST.__objc_const: 0xa848
+  __AUTH_CONST.__objc_const: 0xa988
   __AUTH_CONST.__objc_intobj: 0x318
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0xbe0
-  __DATA.__objc_ivar: 0x584
-  __DATA.__data: 0x968
+  __AUTH.__objc_data: 0xb90
+  __DATA.__objc_ivar: 0x5a4
+  __DATA.__data: 0x970
   __DATA.__bss: 0xa8
-  __DATA_DIRTY.__objc_data: 0x4b0
+  __DATA_DIRTY.__objc_data: 0x500
   __DATA_DIRTY.__bss: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/PrivateFrameworks/AssertionServices.framework/AssertionServices
   - /System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
+  - /System/Library/PrivateFrameworks/BoardServices.framework/BoardServices
   - /System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/PrototypeTools.framework/PrototypeTools
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
+  - /System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation
   - /System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 83A71F93-8A83-3B63-8534-C8DB976CF849
-  Functions: 1688
-  Symbols:   6435
-  CStrings:  3288
+  - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
+  - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  - /usr/lib/swift/libswiftsimd.dylib
+  UUID: D15C6ABE-5409-3709-92D5-F43E395679F5
+  Functions: 1706
+  Symbols:   6508
+  CStrings:  3307
 
Symbols:
+ +[PGButtonView buttonWithDelegate:wantsGlassBackground:]
+ +[_PGButton buttonWithType:wantsGlassBackground:]
+ -[PGControlsContainerView _setupSubviews]
+ -[PGControlsViewModelValues contentType]
+ -[PGControlsViewModelValues controlsViewWantsGlassBackground]
+ -[PGFillView .cxx_destruct]
+ -[PGFillView fillColor]
+ -[PGFillView hitTest:withEvent:]
+ -[PGFillView initWithFrame:wantsGlassBackground:]
+ -[PGFillView setFillColor:]
+ -[PGFillView(PGVibrancyEffects) PG_updateVibrancyEffectForTintColor]
+ -[PGLayoutContainerView initWithFrame:wantsGlassBackground:]
+ -[PGMaterialView initWithFrame:wantsGlassBackground:]
+ -[PGProgressIndicator customElapsedTrackFillColor]
+ -[PGProgressIndicator initWithFrame:wantsGlassBackground:]
+ -[PGProgressIndicator setCustomElapsedTrackFillColor:]
+ GCC_except_table10
+ GCC_except_table28
+ GCC_except_table34
+ GCC_except_table46
+ _OBJC_CLASS_$_PGFillView
+ _OBJC_IVAR_$_PGButtonView._wantsGlassBackground
+ _OBJC_IVAR_$_PGControlsView._wantsGlassBackground
+ _OBJC_IVAR_$_PGFillView._fillColor
+ _OBJC_IVAR_$_PGFillView._wantsGlassBackground
+ _OBJC_IVAR_$_PGMaterialView._backgroundMaterialView
+ _OBJC_IVAR_$_PGMaterialView._wantsGlassBackground
+ _OBJC_IVAR_$_PGPrerollIndicatorView._wantsGlassBackground
+ _OBJC_IVAR_$_PGProgressIndicator._customElapsedTrackFillColor
+ _OBJC_IVAR_$_PGProgressIndicator._wantsGlassBackground
+ _OBJC_IVAR_$__PGButton._wantsGlassBackground
+ _OBJC_METACLASS_$_PGFillView
+ __Block_copy
+ __Block_release
+ __OBJC_$_CLASS_METHODS_UIView(PGVibrancyEffects|PGCABackdropLayerViewSupport|PGAdditions|Pegasus)
+ __OBJC_$_CLASS_METHODS__PGButton
+ __OBJC_$_INSTANCE_METHODS_PGFillView(PGVibrancyEffects)
+ __OBJC_$_INSTANCE_METHODS_UIView(PGVibrancyEffects|PGCABackdropLayerViewSupport|PGAdditions|Pegasus)
+ __OBJC_$_INSTANCE_VARIABLES_PGFillView
+ __OBJC_$_PROP_LIST_PGFillView
+ __OBJC_CLASS_RO_$_PGFillView
+ __OBJC_METACLASS_RO_$_PGFillView
+ __UISolariumEnabled
+ ___chkstk_darwin
+ ___swift_allocate_boxed_opaque_existential_1
+ ___swift_instantiateConcreteTypeFromMangledName
+ ___swift_reflection_version
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftAccelerate_$_Pegasus
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_Pegasus
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftCoreImage_$_Pegasus
+ __swift_FORCE_LOAD_$_swiftDarwin
+ __swift_FORCE_LOAD_$_swiftDarwin_$_Pegasus
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftDispatch_$_Pegasus
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation_$_Pegasus
+ __swift_FORCE_LOAD_$_swiftMetal
+ __swift_FORCE_LOAD_$_swiftMetal_$_Pegasus
+ __swift_FORCE_LOAD_$_swiftOSLog
+ __swift_FORCE_LOAD_$_swiftOSLog_$_Pegasus
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_Pegasus
+ __swift_FORCE_LOAD_$_swiftQuartzCore
+ __swift_FORCE_LOAD_$_swiftQuartzCore_$_Pegasus
+ __swift_FORCE_LOAD_$_swiftUIKit
+ __swift_FORCE_LOAD_$_swiftUIKit_$_Pegasus
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers_$_Pegasus
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftXPC_$_Pegasus
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_Builtin_float_$_Pegasus
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_Pegasus
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_Pegasus
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_Pegasus
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftos_$_Pegasus
+ __swift_FORCE_LOAD_$_swiftsimd
+ __swift_FORCE_LOAD_$_swiftsimd_$_Pegasus
+ _block_copy_helper
+ _block_descriptor
+ _block_destroy_helper
+ _objc_msgSend$PG_setGlassBackgroundEnabled:
+ _objc_msgSend$PG_setGlassGroupEnabled:
+ _objc_msgSend$_setupSubviews
+ _objc_msgSend$buttonWithDelegate:wantsGlassBackground:
+ _objc_msgSend$buttonWithType:wantsGlassBackground:
+ _objc_msgSend$colorWithAlphaComponent:
+ _objc_msgSend$controlsViewWantsGlassBackground
+ _objc_msgSend$customElapsedTrackFillColor
+ _objc_msgSend$initWithFrame:wantsGlassBackground:
+ _objc_msgSend$lightGrayColor
+ _objc_msgSend$setCustomElapsedTrackFillColor:
+ _objc_msgSend$setFillColor:
+ _objc_msgSend$setTitleColor:forState:
+ _objc_msgSend$systemBlackColor
+ _objc_opt_self
+ _swift_allocBox
+ _swift_allocObject
+ _swift_deallocObject
+ _swift_getTypeByMangledNameInContext2
+ _swift_isEscapingClosureAtFileLocation
+ _swift_release
+ _swift_retain
+ _swift_task_isCurrentExecutor
+ _swift_task_reportUnexpectedExecutor
+ _symbolic Ig_
+ _symbolic Sb
+ _symbolic So6UIViewC
+ _symbolic _____Sg 5UIKit29_UICornerMaskingConfigurationV
- +[PGButtonView buttonWithDelegate:]
- -[PGControlsView initWithCoder:]
- -[PGLayoutContainerView initWithFrame:]
- -[PGMaterialView initWithFrame:]
- -[PGProgressIndicator _setCornerRadius:]
- -[PGProgressIndicator customElapsedTrackTintColor]
- -[PGProgressIndicator initWithFrame:]
- -[PGProgressIndicator setCustomElapsedTrackTintColor:]
- -[PGVibrantFillView hitTest:withEvent:]
- -[PGVibrantFillView initWithFrame:]
- -[PGVibrantFillView tintColorDidChange]
- -[PGVibrantFillView(PGVibrancyEffects) PG_updateVibrancyEffectForTintColor]
- GCC_except_table11
- GCC_except_table33
- GCC_except_table45
- _OBJC_CLASS_$_NSNull
- _OBJC_CLASS_$_PGVibrantFillView
- _OBJC_IVAR_$_PGMaterialView._backdropLayerView
- _OBJC_IVAR_$_PGProgressIndicator._customElapsedTrackTintColor
- _OBJC_METACLASS_$_PGVibrantFillView
- __OBJC_$_CLASS_METHODS_UIView(PGVibrancyEffects|PGCABackdropLayerViewSupport|PGAdditions)
- __OBJC_$_INSTANCE_METHODS_PGVibrantFillView(PGVibrancyEffects)
- __OBJC_$_INSTANCE_METHODS_UIView(PGVibrancyEffects|PGCABackdropLayerViewSupport|PGAdditions)
- __OBJC_CLASS_RO_$_PGVibrantFillView
- __OBJC_METACLASS_RO_$_PGVibrantFillView
- _objc_msgSend$buttonWithDelegate:
- _objc_msgSend$buttonWithType:
- _objc_msgSend$customElapsedTrackTintColor
- _objc_msgSend$null
- _objc_msgSend$setCustomElapsedTrackTintColor:
CStrings:
+ "1"
+ "@\"PGFillView\""
+ "@28@0:8@16B24"
+ "PGFillView"
+ "PG_setGlassBackgroundEnabled:"
+ "PG_setGlassGroupEnabled:"
+ "Pegasus"
+ "Pegasus/UIView+Solarium.swift"
+ "T@\"UIColor\",&,N,V_customElapsedTrackFillColor"
+ "T@\"UIColor\",C,N,V_fillColor"
+ "_backgroundMaterialView"
+ "_customElapsedTrackFillColor"
+ "_fillColor"
+ "_setupSubviews"
+ "_wantsGlassBackground"
+ "aB"
+ "buttonWithDelegate:wantsGlassBackground:"
+ "buttonWithType:wantsGlassBackground:"
+ "colorWithAlphaComponent:"
+ "controlsViewWantsGlassBackground"
+ "customElapsedTrackFillColor"
+ "fillColor"
+ "initWithFrame:wantsGlassBackground:"
+ "lightGrayColor"
+ "setCustomElapsedTrackFillColor:"
+ "setFillColor:"
+ "setTitleColor:forState:"
+ "systemBlackColor"
+ "view == _contentView || view == _backgroundMaterialView"
- "@\"PGVibrantFillView\""
- "PGControlsView.m"
- "PGVibrantFillView"
- "QB"
- "T@\"UIColor\",&,N,V_customElapsedTrackTintColor"
- "You cannot do this, but Xcode thinks you can."
- "_backdropLayerView"
- "_customElapsedTrackTintColor"
- "buttonWithDelegate:"
- "customElapsedTrackTintColor"
- "null"
- "setCustomElapsedTrackTintColor:"
- "view == _contentView || view == _backdropLayerView"

```
