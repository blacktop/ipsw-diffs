## PencilPairingUI

> `/System/Library/PrivateFrameworks/PencilPairingUI.framework/PencilPairingUI`

```diff

-170.204.1.0.0
-  __TEXT.__text: 0x276a4
-  __TEXT.__auth_stubs: 0x800
-  __TEXT.__objc_methlist: 0x3d60
-  __TEXT.__const: 0x330
-  __TEXT.__cstring: 0x1297
-  __TEXT.__oslogstring: 0x6bc
-  __TEXT.__gcc_except_tab: 0x278
+179.0.0.0.0
+  __TEXT.__text: 0x2822c
+  __TEXT.__auth_stubs: 0x940
+  __TEXT.__objc_methlist: 0x3e10
+  __TEXT.__const: 0x366
+  __TEXT.__cstring: 0x135f
+  __TEXT.__oslogstring: 0x73f
+  __TEXT.__gcc_except_tab: 0x28c
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__unwind_info: 0xcd8
-  __TEXT.__objc_classname: 0x9df
-  __TEXT.__objc_methname: 0x9611
-  __TEXT.__objc_methtype: 0x1da3
-  __TEXT.__objc_stubs: 0x7e20
-  __DATA_CONST.__got: 0x5e8
-  __DATA_CONST.__const: 0x840
-  __DATA_CONST.__objc_classlist: 0x1c8
-  __DATA_CONST.__objc_catlist: 0x10
+  __TEXT.__swift5_typeref: 0xe
+  __TEXT.__constg_swiftt: 0x50
+  __TEXT.__swift5_fieldmd: 0x10
+  __TEXT.__swift5_types: 0x4
+  __TEXT.__unwind_info: 0xd08
+  __TEXT.__objc_classname: 0x9e2
+  __TEXT.__objc_methname: 0x9810
+  __TEXT.__objc_methtype: 0x1dc5
+  __TEXT.__objc_stubs: 0x7fc0
+  __DATA_CONST.__got: 0x5f0
+  __DATA_CONST.__const: 0x8d8
+  __DATA_CONST.__objc_classlist: 0x1d0
+  __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2690
+  __DATA_CONST.__objc_selrefs: 0x2708
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x138
   __DATA_CONST.__objc_arraydata: 0x120
-  __AUTH_CONST.__auth_got: 0x410
+  __AUTH_CONST.__auth_got: 0x4b0
   __AUTH_CONST.__const: 0x320
-  __AUTH_CONST.__cfstring: 0x1b80
-  __AUTH_CONST.__objc_const: 0xb6b0
+  __AUTH_CONST.__cfstring: 0x1ba0
+  __AUTH_CONST.__objc_const: 0xb828
   __AUTH_CONST.__objc_intobj: 0x2d0
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH.__objc_data: 0x11d0
-  __DATA.__objc_ivar: 0x49c
-  __DATA.__data: 0xc10
+  __AUTH.__data: 0x98
+  __DATA.__objc_ivar: 0x4ac
+  __DATA.__data: 0xc18
   __DATA.__bss: 0xd8
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F97C31D5-9627-374A-8312-D6BACB99B840
-  Functions: 1266
-  Symbols:   5006
-  CStrings:  2494
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
+  UUID: 67F41BCB-E409-3381-9529-9546F5A4D53F
+  Functions: 1286
+  Symbols:   5110
+  CStrings:  2524
 
Symbols:
+ +[PNPWelcomeController(Factory) controllerWithType:buttonType:deviceType:features:delegate:]
+ -[PNPPlatterContainerView initDimmingView]
+ -[PNPPlatterContainerView initEffectView]
+ -[PNPPlatterContainerView initShadowView]
+ -[PNPSqueezeController _squeezePaletteVisibilityDidChange:]
+ -[PNPWelcomeController features]
+ -[PNPWelcomeController setFeatures:]
+ -[PNPWizardViewController setWatchdogTimer:]
+ -[PNPWizardViewController setupWatchdogTimer]
+ -[PNPWizardViewController syncVisibleTimestamp]
+ -[PNPWizardViewController teardownWatchdogTimer]
+ -[PNPWizardViewController watchdogTimer]
+ -[PencilEducationViewController viewDidLayoutSubviews]
+ GCC_except_table12
+ GCC_except_table17
+ GCC_except_table3
+ _OBJC_CLASS_$__TtCs12_SwiftObject
+ _OBJC_IVAR_$_PNPWelcomeController._features
+ _OBJC_IVAR_$_PNPWizardViewController._watchdogTimer
+ _OBJC_IVAR_$_PencilEducationViewController._containerViewWidthConstraint
+ _OBJC_IVAR_$_PencilEducationViewController._segmentedControlWidthConstraint
+ _OBJC_METACLASS_$__TtCs12_SwiftObject
+ _PKPencilSqueezeInteractionDidChangePaletteViewVisibilityNotification
+ __CATEGORY_INSTANCE_METHODS_UIView_$_PencilPairingUI
+ __CATEGORY_UIView_$_PencilPairingUI
+ __DATA__TtC15PencilPairingUIP33_6925EB4B72432CB9F3036B06086EE36619ResourceBundleClass
+ __METACLASS_DATA__TtC15PencilPairingUIP33_6925EB4B72432CB9F3036B06086EE36619ResourceBundleClass
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_PNPWizardViewDelegate
+ __UISolariumEnabled
+ ___45-[PNPWizardViewController setupWatchdogTimer]_block_invoke
+ ___59-[PNPSqueezeController _squeezePaletteVisibilityDidChange:]_block_invoke
+ ___chkstk_darwin
+ ___swift_allocate_boxed_opaque_existential_1
+ ___swift_instantiateConcreteTypeFromMangledName
+ ___swift_reflection_version
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftAccelerate_$_PencilPairingUI
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_PencilPairingUI
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftCoreImage_$_PencilPairingUI
+ __swift_FORCE_LOAD_$_swiftDarwin
+ __swift_FORCE_LOAD_$_swiftDarwin_$_PencilPairingUI
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftDispatch_$_PencilPairingUI
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation_$_PencilPairingUI
+ __swift_FORCE_LOAD_$_swiftMetal
+ __swift_FORCE_LOAD_$_swiftMetal_$_PencilPairingUI
+ __swift_FORCE_LOAD_$_swiftOSLog
+ __swift_FORCE_LOAD_$_swiftOSLog_$_PencilPairingUI
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_PencilPairingUI
+ __swift_FORCE_LOAD_$_swiftQuartzCore
+ __swift_FORCE_LOAD_$_swiftQuartzCore_$_PencilPairingUI
+ __swift_FORCE_LOAD_$_swiftUIKit
+ __swift_FORCE_LOAD_$_swiftUIKit_$_PencilPairingUI
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers_$_PencilPairingUI
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftXPC_$_PencilPairingUI
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_Builtin_float_$_PencilPairingUI
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_PencilPairingUI
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_PencilPairingUI
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_PencilPairingUI
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftos_$_PencilPairingUI
+ __swift_FORCE_LOAD_$_swiftsimd
+ __swift_FORCE_LOAD_$_swiftsimd_$_PencilPairingUI
+ _objc_msgSend$_disableTapInteractionWhenNotVisible
+ _objc_msgSend$_paletteViewVisible
+ _objc_msgSend$controllerWithType:buttonType:deviceType:features:delegate:
+ _objc_msgSend$didMoveToParentViewController:
+ _objc_msgSend$features
+ _objc_msgSend$featuresForWelcomeControllerType:
+ _objc_msgSend$initDimmingView
+ _objc_msgSend$initEffectView
+ _objc_msgSend$initShadowView
+ _objc_msgSend$now
+ _objc_msgSend$pencilKitResponderState
+ _objc_msgSend$ppuiSetCapsuleCornerMaskingConfiguration
+ _objc_msgSend$ppuiSetGlassBackground
+ _objc_msgSend$setActiveToolPicker:
+ _objc_msgSend$setDouble:forKey:
+ _objc_msgSend$setFeatures:
+ _objc_msgSend$setStateAutosaveName:
+ _objc_msgSend$setToolPickerVisibility:
+ _objc_msgSend$setupWatchdogTimer
+ _objc_msgSend$syncVisibleTimestamp
+ _objc_msgSend$teardownWatchdogTimer
+ _objc_msgSend$timeIntervalSinceReferenceDate
+ _objc_opt_self
+ _objc_retain_x6
+ _swift_allocBox
+ _swift_deallocClassInstance
+ _swift_deletedMethodError
+ _swift_getTypeByMangledNameInContext2
+ _swift_release
+ _swift_task_isCurrentExecutor
+ _swift_task_reportUnexpectedExecutor
+ _symbolic _____ 15PencilPairingUI19ResourceBundleClass33_6925EB4B72432CB9F3036B06086EE366LLC
+ _symbolic _____Sg 5UIKit29_UICornerMaskingConfigurationV
- -[PNPSqueezeController toolPickerSelectedToolDidChange:]
- -[PNPSqueezeController toolPickerVisibilityDidChange:]
- GCC_except_table13
- GCC_except_table4
- GCC_except_table8
- _OBJC_CLASS_$_PKInkingTool
- _PKInkTypePen
- ___54-[PNPSqueezeController toolPickerVisibilityDidChange:]_block_invoke
- _objc_msgSend$_paletteView
- _objc_msgSend$controllerWithType:buttonType:deviceType:delegate:
- _objc_msgSend$initWithInkType:color:
- _objc_msgSend$isVisible
- _objc_msgSend$selectedTool
- _objc_msgSend$setAutoHideEnabled:
- _objc_msgSend$setSelectedTool:
- _objc_msgSend$setTool:
- _objc_msgSend$setVisible:forFirstResponder:
CStrings:
+ "1"
+ "@56@0:8q16q24q32Q40@48"
+ "PNPWizardController setup watchdog timer."
+ "PNPWizardController sync visible timestamp."
+ "PNPWizardController teardown watchdog timer."
+ "PencilPairingUI/UIKit+Solarium.swift"
+ "Q24@0:8q16"
+ "TQ,N,V_features"
+ "_TtC15PencilPairingUIP33_6925EB4B72432CB9F3036B06086EE36619ResourceBundleClass"
+ "_containerViewWidthConstraint"
+ "_disableTapInteractionWhenNotVisible"
+ "_features"
+ "_paletteViewVisible"
+ "_segmentedControlWidthConstraint"
+ "_squeezePaletteVisibilityDidChange:"
+ "controllerWithType:buttonType:deviceType:features:delegate:"
+ "didMoveToParentViewController:"
+ "features"
+ "featuresForWelcomeControllerType:"
+ "initDimmingView"
+ "initEffectView"
+ "initShadowView"
+ "latestTimestampForVisibleEduUI"
+ "now"
+ "pencilKitResponderState"
+ "ppuiSetCapsuleCornerMaskingConfiguration"
+ "ppuiSetGlassBackground"
+ "setActiveToolPicker:"
+ "setDouble:forKey:"
+ "setFeatures:"
+ "setStateAutosaveName:"
+ "setToolPickerVisibility:"
+ "setupWatchdogTimer"
+ "syncVisibleTimestamp"
+ "teardownWatchdogTimer"
+ "timeIntervalSinceReferenceDate"
- "$!"
- "A"
- "_paletteView"
- "initWithInkType:color:"
- "isVisible"
- "selectedTool"
- "setAutoHideEnabled:"
- "setSelectedTool:"
- "setTool:"
- "setVisible:forFirstResponder:"

```
