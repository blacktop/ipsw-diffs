## SmartStackUIServices

> `/System/Library/PrivateFrameworks/SmartStackUIServices.framework/SmartStackUIServices`

```diff

 337.0.0.0.0
-  __TEXT.__text: 0x2bf8
-  __TEXT.__const: 0x3f0
-  __TEXT.__constg_swiftt: 0xe8
-  __TEXT.__swift5_typeref: 0xbf
+  __TEXT.__text: 0x16ab4
+  __TEXT.__objc_methlist: 0x8c0
+  __TEXT.__const: 0x132a
+  __TEXT.__cstring: 0x5f8
+  __TEXT.__constg_swiftt: 0x768
+  __TEXT.__swift5_typeref: 0xa34
   __TEXT.__swift5_builtin: 0x3c
-  __TEXT.__swift5_reflstr: 0x313
-  __TEXT.__swift5_fieldmd: 0x18c
-  __TEXT.__swift5_assocty: 0x18
-  __TEXT.__swift5_proto: 0x1c
-  __TEXT.__swift5_types: 0x1c
-  __TEXT.__cstring: 0x99
-  __TEXT.__oslogstring: 0x52
-  __TEXT.__unwind_info: 0x138
-  __TEXT.__eh_frame: 0x48
+  __TEXT.__swift5_reflstr: 0x8d5
+  __TEXT.__swift5_fieldmd: 0x5d4
+  __TEXT.__swift5_assocty: 0xb0
+  __TEXT.__swift5_proto: 0x4c
+  __TEXT.__swift5_types: 0x5c
+  __TEXT.__swift5_capture: 0x194
+  __TEXT.__oslogstring: 0x725
+  __TEXT.__swift5_protos: 0x18
+  __TEXT.__swift_as_entry: 0x8
+  __TEXT.__swift_as_ret: 0x4
+  __TEXT.__swift_as_cont: 0x4
+  __TEXT.__unwind_info: 0x7b0
+  __TEXT.__eh_frame: 0x368
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
-  __DATA_CONST.__const: 0x98
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x1e0
+  __DATA_CONST.__objc_classlist: 0x78
+  __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x80
-  __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x948
-  __AUTH_CONST.__auth_got: 0x240
-  __DATA.__data: 0x98
+  __DATA_CONST.__objc_selrefs: 0x5d8
+  __DATA_CONST.__objc_protorefs: 0x50
+  __DATA_CONST.__objc_superrefs: 0x20
+  __DATA_CONST.__got: 0x278
+  __AUTH_CONST.__const: 0x1078
+  __AUTH_CONST.__cfstring: 0x20
+  __AUTH_CONST.__objc_const: 0x1398
+  __AUTH_CONST.__auth_got: 0x878
+  __AUTH.__objc_data: 0x800
+  __AUTH.__data: 0x578
+  __DATA.__objc_ivar: 0x10
+  __DATA.__data: 0x890
+  __DATA.__common: 0x10
   - /System/Library/Frameworks/ClockKit.framework/ClockKit
+  - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/RelevanceKit.framework/RelevanceKit

   - /System/Library/Frameworks/WidgetKit.framework/WidgetKit
   - /System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices
   - /System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost
+  - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/ChronoServices.framework/ChronoServices
   - /System/Library/PrivateFrameworks/ClockKitUI.framework/ClockKitUI
   - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags

   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
+  - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftObservation.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 129
-  Symbols:   147
-  CStrings:  7
+  Functions: 722
+  Symbols:   649
+  CStrings:  70
 
Symbols:
+ -[SSUICardClientSceneSettingsDiffContext .cxx_destruct]
+ -[SSUICardClientSceneSettingsDiffContext currentSettings]
+ -[SSUICardClientSceneSettingsDiffContext initWithPreviousSettings:currentSettings:]
+ -[SSUICardClientSceneSettingsDiffContext previousSettings]
+ -[SSUICardClientSceneSettingsDiffInspector _observeProperty:observer:]
+ -[SSUICardClientSceneSettingsDiffInspector inspectDiff:withContext:]
+ -[SSUICardClientSceneSettingsDiffInspector observeContentReadyForDisplayWithBlock:]
+ -[SSUICardSceneSettingsDiffContext .cxx_destruct]
+ -[SSUICardSceneSettingsDiffContext currentSettings]
+ -[SSUICardSceneSettingsDiffContext initWithPreviousSettings:currentSettings:]
+ -[SSUICardSceneSettingsDiffContext previousSettings]
+ -[SSUICardSceneSettingsDiffInspector _observeProperty:observer:]
+ -[SSUICardSceneSettingsDiffInspector inspectDiff:withContext:]
+ -[SSUICardSceneSettingsDiffInspector observeAllowBacklightActiveCardUpdatesWithBlock:]
+ -[SSUICardSceneSettingsDiffInspector observeCardGlassStyleFractionWithBlock:]
+ -[SSUICardSceneSettingsDiffInspector observeCardTintColorWithBlock:]
+ _BKSTouchDeliveryPolicyServerGetProxyWithErrorHandler
+ _OBJC_CLASS_$_BKSTouchDeliveryPolicy
+ _OBJC_CLASS_$_BKSTouchDeliveryPolicyAssertion
+ _OBJC_CLASS_$_BLSHBacklightFBSceneEnvironmentActionHandler
+ _OBJC_CLASS_$_BSAction
+ _OBJC_CLASS_$_BSContinuousMachTimer
+ _OBJC_CLASS_$_CLKDevice
+ _OBJC_CLASS_$_FBSSceneClientSettings
+ _OBJC_CLASS_$_FBSSceneClientSettingsDiff
+ _OBJC_CLASS_$_FBSSceneClientSettingsDiffInspector
+ _OBJC_CLASS_$_FBSSceneComponent
+ _OBJC_CLASS_$_FBSSceneExtension
+ _OBJC_CLASS_$_FBSSceneSettings
+ _OBJC_CLASS_$_FBSSceneSettingsDiff
+ _OBJC_CLASS_$_FBSSceneSettingsDiffInspector
+ _OBJC_CLASS_$_FBSSettingsExtension
+ _OBJC_CLASS_$_FBScene
+ _OBJC_CLASS_$_FBSceneLayer
+ _OBJC_CLASS_$_NSObject
+ _OBJC_CLASS_$_OS_dispatch_queue
+ _OBJC_CLASS_$_RBSProcessIdentity
+ _OBJC_CLASS_$_SSUICardClientSceneSettingsDiffContext
+ _OBJC_CLASS_$_SSUICardClientSceneSettingsDiffInspector
+ _OBJC_CLASS_$_SSUICardSceneSettingsDiffContext
+ _OBJC_CLASS_$_SSUICardSceneSettingsDiffInspector
+ _OBJC_CLASS_$_UIColor
+ _OBJC_CLASS_$_UIViewController
+ _OBJC_CLASS_$__TtC20SmartStackUIServices18CardSceneExtension
+ _OBJC_CLASS_$__TtC20SmartStackUIServices22CardHostViewController
+ _OBJC_CLASS_$__TtC20SmartStackUIServices22CardSceneHostComponent
+ _OBJC_CLASS_$__TtC20SmartStackUIServices22CardSceneSpecification
+ _OBJC_CLASS_$__TtC20SmartStackUIServices24CardSceneClientComponent
+ _OBJC_CLASS_$__TtC20SmartStackUIServices27CardHostSceneViewController
+ _OBJC_CLASS_$__TtCs12_SwiftObject
+ _OBJC_CLASS_$__UISceneHostingController
+ _OBJC_CLASS_$__UISceneHostingSceneSpecification
+ _OBJC_IVAR_$_SSUICardClientSceneSettingsDiffContext._currentSettings
+ _OBJC_IVAR_$_SSUICardClientSceneSettingsDiffContext._previousSettings
+ _OBJC_IVAR_$_SSUICardSceneSettingsDiffContext._currentSettings
+ _OBJC_IVAR_$_SSUICardSceneSettingsDiffContext._previousSettings
+ _OBJC_METACLASS_$_FBSSceneClientSettingsDiffInspector
+ _OBJC_METACLASS_$_FBSSceneComponent
+ _OBJC_METACLASS_$_FBSSceneExtension
+ _OBJC_METACLASS_$_FBSSceneSettingsDiffInspector
+ _OBJC_METACLASS_$_NSObject
+ _OBJC_METACLASS_$_SSUICardClientSceneSettingsDiffContext
+ _OBJC_METACLASS_$_SSUICardClientSceneSettingsDiffInspector
+ _OBJC_METACLASS_$_SSUICardSceneSettingsDiffContext
+ _OBJC_METACLASS_$_SSUICardSceneSettingsDiffInspector
+ _OBJC_METACLASS_$_UIViewController
+ _OBJC_METACLASS_$__TtC20SmartStackUIServices18CardSceneExtension
+ _OBJC_METACLASS_$__TtC20SmartStackUIServices22CardHostViewController
+ _OBJC_METACLASS_$__TtC20SmartStackUIServices22CardSceneHostComponent
+ _OBJC_METACLASS_$__TtC20SmartStackUIServices22CardSceneSpecification
+ _OBJC_METACLASS_$__TtC20SmartStackUIServices24CardSceneClientComponent
+ _OBJC_METACLASS_$__TtC20SmartStackUIServices27CardHostSceneViewController
+ _OBJC_METACLASS_$__TtCC20SmartStackUIServices30ViewHitTestingAssertionManagerP33_E670015C4E4E217135EC2432F63A3AF29Assertion
+ _OBJC_METACLASS_$__TtCs12_SwiftObject
+ _OBJC_METACLASS_$__UISceneHostingSceneSpecification
+ _SSFIsInternalBuild
+ _SSUISSceneSessionRoleCard
+ __Block_copy
+ __Block_release
+ __CLASS_METHODS__TtC20SmartStackUIServices18CardSceneExtension
+ __DATA__TtC20SmartStackUIServices17CardHostViewModel
+ __DATA__TtC20SmartStackUIServices18CardSceneExtension
+ __DATA__TtC20SmartStackUIServices22CardHostSceneViewModel
+ __DATA__TtC20SmartStackUIServices22CardHostViewController
+ __DATA__TtC20SmartStackUIServices22CardSceneHostComponent
+ __DATA__TtC20SmartStackUIServices22CardSceneSpecification
+ __DATA__TtC20SmartStackUIServices24CardSceneClientComponent
+ __DATA__TtC20SmartStackUIServices27CardHostSceneViewController
+ __DATA__TtC20SmartStackUIServices29BSContinuousMachTimerProvider
+ __DATA__TtC20SmartStackUIServices30ViewHitTestingAssertionManager
+ __DATA__TtCC20SmartStackUIServices30ViewHitTestingAssertionManagerP33_E670015C4E4E217135EC2432F63A3AF29Assertion
+ __INSTANCE_METHODS__TtC20SmartStackUIServices18CardSceneExtension
+ __INSTANCE_METHODS__TtC20SmartStackUIServices22CardHostViewController
+ __INSTANCE_METHODS__TtC20SmartStackUIServices22CardSceneSpecification
+ __INSTANCE_METHODS__TtC20SmartStackUIServices24CardSceneClientComponent
+ __INSTANCE_METHODS__TtC20SmartStackUIServices27CardHostSceneViewController
+ __INSTANCE_METHODS__TtCC20SmartStackUIServices30ViewHitTestingAssertionManagerP33_E670015C4E4E217135EC2432F63A3AF29Assertion
+ __IVARS__TtC20SmartStackUIServices17CardHostViewModel
+ __IVARS__TtC20SmartStackUIServices22CardHostSceneViewModel
+ __IVARS__TtC20SmartStackUIServices22CardHostViewController
+ __IVARS__TtC20SmartStackUIServices22CardSceneHostComponent
+ __IVARS__TtC20SmartStackUIServices24CardSceneClientComponent
+ __IVARS__TtC20SmartStackUIServices27CardHostSceneViewController
+ __IVARS__TtC20SmartStackUIServices30ViewHitTestingAssertionManager
+ __IVARS__TtCC20SmartStackUIServices30ViewHitTestingAssertionManagerP33_E670015C4E4E217135EC2432F63A3AF29Assertion
+ __METACLASS_DATA__TtC20SmartStackUIServices17CardHostViewModel
+ __METACLASS_DATA__TtC20SmartStackUIServices18CardSceneExtension
+ __METACLASS_DATA__TtC20SmartStackUIServices22CardHostSceneViewModel
+ __METACLASS_DATA__TtC20SmartStackUIServices22CardHostViewController
+ __METACLASS_DATA__TtC20SmartStackUIServices22CardSceneHostComponent
+ __METACLASS_DATA__TtC20SmartStackUIServices22CardSceneSpecification
+ __METACLASS_DATA__TtC20SmartStackUIServices24CardSceneClientComponent
+ __METACLASS_DATA__TtC20SmartStackUIServices27CardHostSceneViewController
+ __METACLASS_DATA__TtC20SmartStackUIServices29BSContinuousMachTimerProvider
+ __METACLASS_DATA__TtC20SmartStackUIServices30ViewHitTestingAssertionManager
+ __METACLASS_DATA__TtCC20SmartStackUIServices30ViewHitTestingAssertionManagerP33_E670015C4E4E217135EC2432F63A3AF29Assertion
+ __NSConcreteStackBlock
+ __OBJC_$_INSTANCE_METHODS_SSUICardClientSceneSettingsDiffContext
+ __OBJC_$_INSTANCE_METHODS_SSUICardClientSceneSettingsDiffInspector
+ __OBJC_$_INSTANCE_METHODS_SSUICardSceneSettingsDiffContext
+ __OBJC_$_INSTANCE_METHODS_SSUICardSceneSettingsDiffInspector
+ __OBJC_$_INSTANCE_METHODS__TtC20SmartStackUIServices22CardSceneHostComponent(SmartStackUIServices)
+ __OBJC_$_INSTANCE_VARIABLES_SSUICardClientSceneSettingsDiffContext
+ __OBJC_$_INSTANCE_VARIABLES_SSUICardSceneSettingsDiffContext
+ __OBJC_$_PROP_LIST_BLSHBacklightSceneHostEnvironment
+ __OBJC_$_PROP_LIST_NSObject
+ __OBJC_$_PROP_LIST_SSUICardClientSceneSettings
+ __OBJC_$_PROP_LIST_SSUICardClientSceneSettingsDiffContext
+ __OBJC_$_PROP_LIST_SSUICardSceneSettings
+ __OBJC_$_PROP_LIST_SSUICardSceneSettingsDiffContext
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BLSHBacklightSceneHostEnvironment
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BSInvalidatable
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_BLSHBacklightSceneHostEnvironment
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_FBSSceneComponent
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_FBSSceneObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_FBSceneComponent
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_FBSceneLayerManagerObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_FBSceneObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SSUICardClientSceneSettings
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SSUICardSceneSettings
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BLSHBacklightSceneHostEnvironment
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BSInvalidatable
+ __OBJC_$_PROTOCOL_METHOD_TYPES_FBSSceneComponent
+ __OBJC_$_PROTOCOL_METHOD_TYPES_FBSSceneObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_FBSceneComponent
+ __OBJC_$_PROTOCOL_METHOD_TYPES_FBSceneLayerManagerObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_FBSceneObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SSUICardClientSceneSettings
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SSUICardSceneSettings
+ __OBJC_$_PROTOCOL_REFS_BLSHBacklightSceneHostEnvironment
+ __OBJC_$_PROTOCOL_REFS_BSInvalidatable
+ __OBJC_$_PROTOCOL_REFS_FBSSceneComponent
+ __OBJC_$_PROTOCOL_REFS_FBSSceneObserver
+ __OBJC_$_PROTOCOL_REFS_FBSceneComponent
+ __OBJC_$_PROTOCOL_REFS_FBSceneLayerManagerObserver
+ __OBJC_$_PROTOCOL_REFS_FBSceneObserver
+ __OBJC_CLASS_PROTOCOLS_$__TtC20SmartStackUIServices22CardSceneHostComponent(SmartStackUIServices)
+ __OBJC_CLASS_RO_$_SSUICardClientSceneSettingsDiffContext
+ __OBJC_CLASS_RO_$_SSUICardClientSceneSettingsDiffInspector
+ __OBJC_CLASS_RO_$_SSUICardSceneSettingsDiffContext
+ __OBJC_CLASS_RO_$_SSUICardSceneSettingsDiffInspector
+ __OBJC_LABEL_PROTOCOL_$_BLSHBacklightSceneHostEnvironment
+ __OBJC_LABEL_PROTOCOL_$_BSInvalidatable
+ __OBJC_LABEL_PROTOCOL_$_FBSSceneComponent
+ __OBJC_LABEL_PROTOCOL_$_FBSSceneObserver
+ __OBJC_LABEL_PROTOCOL_$_FBSceneComponent
+ __OBJC_LABEL_PROTOCOL_$_FBSceneLayerManagerObserver
+ __OBJC_LABEL_PROTOCOL_$_FBSceneObserver
+ __OBJC_LABEL_PROTOCOL_$_NSObject
+ __OBJC_LABEL_PROTOCOL_$_SSUICardClientSceneSettings
+ __OBJC_LABEL_PROTOCOL_$_SSUICardSceneSettings
+ __OBJC_METACLASS_RO_$_SSUICardClientSceneSettingsDiffContext
+ __OBJC_METACLASS_RO_$_SSUICardClientSceneSettingsDiffInspector
+ __OBJC_METACLASS_RO_$_SSUICardSceneSettingsDiffContext
+ __OBJC_METACLASS_RO_$_SSUICardSceneSettingsDiffInspector
+ __OBJC_PROTOCOL_$_BLSHBacklightSceneHostEnvironment
+ __OBJC_PROTOCOL_$_BSInvalidatable
+ __OBJC_PROTOCOL_$_FBSSceneComponent
+ __OBJC_PROTOCOL_$_FBSSceneObserver
+ __OBJC_PROTOCOL_$_FBSceneComponent
+ __OBJC_PROTOCOL_$_FBSceneLayerManagerObserver
+ __OBJC_PROTOCOL_$_FBSceneObserver
+ __OBJC_PROTOCOL_$_NSObject
+ __OBJC_PROTOCOL_$_SSUICardClientSceneSettings
+ __OBJC_PROTOCOL_$_SSUICardSceneSettings
+ __PROPERTIES__TtC20SmartStackUIServices22CardSceneSpecification
+ __PROTOCOLS__TtC20SmartStackUIServices24CardSceneClientComponent
+ __PROTOCOLS__TtCC20SmartStackUIServices30ViewHitTestingAssertionManagerP33_E670015C4E4E217135EC2432F63A3AF29Assertion
+ ___64-[SSUICardSceneSettingsDiffInspector _observeProperty:observer:]_block_invoke
+ ___70-[SSUICardClientSceneSettingsDiffInspector _observeProperty:observer:]_block_invoke
+ ___CFConstantStringClassReference
+ ___block_descriptor_40_e8_32bs_e9_v16?0^v8ls32l8
+ ___swift__destructor
+ ___swift_assignWithCopy_strong
+ ___swift_assignWithTake_strong
+ ___swift_async_cont_functlets
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ ___swift_closure_destructor
+ ___swift_destroy_boxed_opaque_existential_0Tm
+ ___swift_destroy_boxed_opaque_existential_1Tm
+ ___swift_destroy_strong
+ ___swift_initWithCopy_strong
+ ___swift_instantiateConcreteTypeFromMangledNameAbstractV2
+ ___swift_instantiateGenericMetadata
+ ___swift_memcpy24_8
+ ___swift_memcpy40_8
+ ___swift_memcpy48_8
+ ___swift_memcpy8_8
+ ___swift_mutable_project_boxed_opaque_existential_1
+ ___unnamed_1
+ __objc_empty_cache
+ __swift_FORCE_LOAD_$_swiftCoreMIDI
+ __swift_FORCE_LOAD_$_swiftCoreMIDI_$_SmartStackUIServices
+ __swift_stdlib_reportUnimplementedInitializer
+ _associated conformance 20SmartStackUIServices12CardHostViewV011PlaceholderF0V7SwiftUI0F0AA4BodyAfGP_AfG
+ _associated conformance 20SmartStackUIServices12CardHostViewV05ErrorF0V7SwiftUI0F0AA4BodyAfGP_AfG
+ _associated conformance 20SmartStackUIServices12CardHostViewV0D9ContainerVy_xG7SwiftUI0F0AA4BodyAgHP_AgH
+ _associated conformance 20SmartStackUIServices12CardHostViewV7SwiftUI0F0AA4BodyAdEP_AdE
+ _associated conformance 20SmartStackUIServices17CardHostSceneViewV7SwiftUI0G0AA4BodyAdEP_AdE
+ _associated conformance 20SmartStackUIServices17CardHostSceneViewV7SwiftUI29UIViewControllerRepresentableAaD0G0
+ _block_copy_helper
+ _block_descriptor
+ _block_destroy_helper
+ _flat unique So33BLSHBacklightSceneHostEnvironment_p
+ _free
+ _get_witness_table 20SmartStackUIServices12CardHostViewV0D9ContainerVy_7SwiftUI15ModifiedContentVyAHyAF6VStackVyAF05TupleK0VyAF0F0PAFE8redacted6reasonQrAF16RedactionReasonsV_tFQOyAF4TextV_Qo__A2UQPGGAF16_FlexFrameLayoutVGAF30_EnvironmentKeyWritingModifierVyAF13AnyShapeStyleVSgGGGAfMHPyHC
+ _get_witness_table 7SwiftUI15ModifiedContentVyAA4ViewP9WidgetKitE24defineFontsForSmartStackQryFQOyAA012_ConditionalD0VyAIyAIyAIy0kL10UIServices08CardHostE0V05ErrorE0VANGACyACyAJ0op5SceneE0VAA14_OpacityEffectVGAA16_OverlayModifierVyAL011PlaceholderE0VSgGGGANGAXG_Qo_AA022_EnvironmentKeyWritingV0VyAA19WatchDisplayVariantOGGAaDHPqd__AaDHD2_A3_HO_A8_AA0eV0HPyHCHC
+ _get_witness_table 7SwiftUI19_ConditionalContentVy20SmartStackUIServices12CardHostViewV0H9ContainerVy_AA6VStackVyAA05TupleD0VyAA4TextV_ANQPGGGAA05EmptyJ0VGAA0J0HPAqaUHPyHC_AsaUHPyHCHC
+ _get_witness_table 7SwiftUI4ViewRzlAA15ModifiedContentVyAaBPAAE12_glassEffect_2inQrAA6_GlassV_qd__tAA5ShapeRd__lFQOyADyADyADyAE9WidgetKitE24defineFontsForSmartStackQryFQOyx_Qo_AA30_EnvironmentKeyWritingModifierVyAA19WatchDisplayVariantOGGAA14_PaddingLayoutVGAA06_FrameZ0VG_AA16RoundedRectangleVQo_AA028_ContainerRoundedRectangularjU0VyA_GGAaBHPqd0__AaBHD3_A0_HO_A3_AA0cU0HPyHCHC
+ _keypath_get.12Tm
+ _keypath_set.13Tm
+ _objc_autoreleaseReturnValue
+ _objc_msgSend$_FBSScene
+ _objc_msgSend$_contextId
+ _objc_msgSend$_observeProperty:observer:
+ _objc_msgSend$addChildViewController:
+ _objc_msgSend$addObserver:
+ _objc_msgSend$addSubview:
+ _objc_msgSend$allowBacklightActiveCardUpdates
+ _objc_msgSend$allowsHitTesting
+ _objc_msgSend$backlightSceneHostEnvironment
+ _objc_msgSend$bounds
+ _objc_msgSend$cardGlassStyleFraction
+ _objc_msgSend$cardIndex
+ _objc_msgSend$cardTintColor
+ _objc_msgSend$clearColor
+ _objc_msgSend$clientScene
+ _objc_msgSend$componentForExtension:ofClass:
+ _objc_msgSend$contentReadyForDisplay
+ _objc_msgSend$contextID
+ _objc_msgSend$currentDevice
+ _objc_msgSend$currentSettings
+ _objc_msgSend$endpoint
+ _objc_msgSend$extensionForProtocol:
+ _objc_msgSend$hostScene
+ _objc_msgSend$identityForEmbeddedApplicationIdentifier:
+ _objc_msgSend$init
+ _objc_msgSend$initWithCoder:
+ _objc_msgSend$initWithIdentifier:
+ _objc_msgSend$initWithNibName:bundle:
+ _objc_msgSend$initWithPreviousSettings:currentSettings:
+ _objc_msgSend$initWithProcessIdentity:sceneSpecification:
+ _objc_msgSend$inspectDiff:withContext:
+ _objc_msgSend$invalidate
+ _objc_msgSend$ipc_addPolicy:
+ _objc_msgSend$layer
+ _objc_msgSend$layerManager
+ _objc_msgSend$layers
+ _objc_msgSend$observeAllowBacklightActiveCardUpdatesWithBlock:
+ _objc_msgSend$observeCardGlassStyleFractionWithBlock:
+ _objc_msgSend$observeCardTintColorWithBlock:
+ _objc_msgSend$observeContentReadyForDisplayWithBlock:
+ _objc_msgSend$observeProperty:withBlock:
+ _objc_msgSend$policyRequiringSharingOfTouchesDeliveredToChildContextId:withHostContextId:
+ _objc_msgSend$previousSettings
+ _objc_msgSend$respondToActions:forFBScene:
+ _objc_msgSend$sceneView
+ _objc_msgSend$sceneViewController
+ _objc_msgSend$scheduleWithFireInterval:leewayInterval:queue:handler:
+ _objc_msgSend$setAllowBacklightActiveCardUpdates:
+ _objc_msgSend$setAllowsHitTesting:
+ _objc_msgSend$setAlwaysOnEnabledForEnvironment:
+ _objc_msgSend$setAssertionEndpoint:
+ _objc_msgSend$setBackgroundColor:
+ _objc_msgSend$setBounds:
+ _objc_msgSend$setCardGlassStyleFraction:
+ _objc_msgSend$setCardIndex:
+ _objc_msgSend$setCardTintColor:
+ _objc_msgSend$setContentReadyForDisplay:
+ _objc_msgSend$setFrame:
+ _objc_msgSend$setOpaque:
+ _objc_msgSend$settings
+ _objc_msgSend$settingsDiff
+ _objc_msgSend$updateClientSettings:
+ _objc_msgSend$updateSettingsWithBlock:
+ _objc_msgSend$view
+ _objc_msgSend$window
+ _objc_msgSendSuper2
+ _objc_release
+ _objc_release_x1
+ _objc_release_x25
+ _objc_release_x26
+ _objc_release_x28
+ _objc_release_x8
+ _objc_release_x9
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x10
+ _objc_retain_x19
+ _objc_retain_x2
+ _objc_retain_x21
+ _objc_retain_x22
+ _objc_retain_x23
+ _objc_retain_x25
+ _objc_retain_x26
+ _objc_retain_x27
+ _objc_retain_x28
+ _objc_retain_x3
+ _objc_retain_x8
+ _objc_storeStrong
+ _swift_arrayDestroy
+ _swift_arrayInitWithCopy
+ _swift_beginAccess
+ _swift_coroFrameAlloc
+ _swift_cvw_allocateGenericValueMetadataWithLayoutString
+ _swift_cvw_instantiateLayoutString
+ _swift_deallocClassInstance
+ _swift_deallocObject
+ _swift_deletedMethodError
+ _swift_dynamicCast
+ _swift_dynamicCastClass
+ _swift_dynamicCastObjCClass
+ _swift_endAccess
+ _swift_errorRelease
+ _swift_errorRetain
+ _swift_getErrorValue
+ _swift_getGenericMetadata
+ _swift_getKeyPath
+ _swift_getOpaqueTypeConformance2
+ _swift_getOpaqueTypeMetadata2
+ _swift_getSingletonMetadata
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _swift_initStackObject
+ _swift_isEscapingClosureAtFileLocation
+ _swift_lookUpClassMethod
+ _swift_makeBoxUnique
+ _swift_release_n
+ _swift_release_x1
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x23
+ _swift_release_x24
+ _swift_release_x25
+ _swift_release_x26
+ _swift_release_x27
+ _swift_release_x8
+ _swift_release_x9
+ _swift_retain
+ _swift_retain_n
+ _swift_retain_x1
+ _swift_retain_x19
+ _swift_retain_x2
+ _swift_retain_x20
+ _swift_retain_x21
+ _swift_retain_x22
+ _swift_retain_x23
+ _swift_retain_x25
+ _swift_retain_x26
+ _swift_retain_x27
+ _swift_retain_x8
+ _swift_retain_x9
+ _swift_task_alloc
+ _swift_task_create
+ _swift_task_dealloc
+ _swift_task_deinitOnExecutor
+ _swift_task_getMainExecutor
+ _swift_task_isCurrentExecutor
+ _swift_task_reportUnexpectedExecutor
+ _swift_task_switch
+ _swift_unknownObjectRelease
+ _swift_unknownObjectWeakAssign
+ _swift_unknownObjectWeakDestroy
+ _swift_unknownObjectWeakInit
+ _swift_unknownObjectWeakLoadStrong
+ _swift_updateClassMetadata2
+ _swift_weakDestroy
+ _swift_weakInit
+ _swift_weakLoadStrong
+ _symbolic $s20SmartStackUIServices18DetachedSceneTimerP
+ _symbolic $s20SmartStackUIServices27DetachedSceneTimerProvidingP
+ _symbolic $s20SmartStackUIServices30CardHostViewControllerDelegateP
+ _symbolic $s20SmartStackUIServices30CardSceneHostComponentDelegateP
+ _symbolic $s20SmartStackUIServices32CardSceneClientComponentDelegateP
+ _symbolic $s20SmartStackUIServices32CardSceneClientComponentProtocolP
+ _symbolic $s7SwiftUI29UIViewControllerRepresentableP
+ _symbolic $s7SwiftUI4ViewP
+ _symbolic Iegh_
+ _symbolic SDy_____So31BKSTouchDeliveryPolicyAssertionCG s6UInt32V
+ _symbolic SS
+ _symbolic SSSg
+ _symbolic SaySSG
+ _symbolic Say_____G 8Dispatch0A13WorkItemFlagsV
+ _symbolic ScA_pSg
+ _symbolic ScPSg
+ _symbolic Sd
+ _symbolic So16UIViewControllerC
+ _symbolic So17FBSSceneComponentC
+ _symbolic So17FBSSceneExtensionC
+ _symbolic So23FBSMutableSceneSettingsCIgg_
+ _symbolic So25_UISceneHostingControllerC
+ _symbolic So33_UISceneHostingSceneSpecificationC
+ _symbolic So34SSUICardSceneSettingsDiffInspectorCSg
+ _symbolic So40SSUICardClientSceneSettingsDiffInspectorCSg
+ _symbolic So44BLSHBacklightFBSceneEnvironmentActionHandlerC
+ _symbolic So6UIViewCSgXw
+ _symbolic So7UIColorCSg
+ _symbolic So8NSObjectC
+ _symbolic So8NSObjectCSg
+ _symbolic So8UIWindowCSgXw
+ _symbolic _____ 11Observation0A9RegistrarV
+ _symbolic _____ 20SmartStackUIServices12CardHostViewV
+ _symbolic _____ 20SmartStackUIServices12CardHostViewV011PlaceholderF0V
+ _symbolic _____ 20SmartStackUIServices12CardHostViewV05ErrorF0V
+ _symbolic _____ 20SmartStackUIServices12CardHostViewV0D9ContainerV
+ _symbolic _____ 20SmartStackUIServices17CardHostSceneViewV
+ _symbolic _____ 20SmartStackUIServices17CardHostViewModelC
+ _symbolic _____ 20SmartStackUIServices18CardSceneExtensionC
+ _symbolic _____ 20SmartStackUIServices22CardHostSceneViewModelC
+ _symbolic _____ 20SmartStackUIServices22CardHostViewControllerC
+ _symbolic _____ 20SmartStackUIServices22CardSceneHostComponentC
+ _symbolic _____ 20SmartStackUIServices22CardSceneSpecificationC
+ _symbolic _____ 20SmartStackUIServices24CardSceneClientComponentC
+ _symbolic _____ 20SmartStackUIServices27CardHostSceneViewControllerC
+ _symbolic _____ 20SmartStackUIServices29BSContinuousMachTimerProviderC
+ _symbolic _____ 20SmartStackUIServices30ViewHitTestingAssertionManagerC
+ _symbolic _____ 20SmartStackUIServices30ViewHitTestingAssertionManagerC0G033_E670015C4E4E217135EC2432F63A3AF2LLC
+ _symbolic _____ 2os6LoggerV
+ _symbolic _____ 7SwiftUI17EnvironmentValuesV
+ _symbolic _____ 7SwiftUI19WatchDisplayVariantO
+ _symbolic _____ s5NeverO
+ _symbolic _____Sg 20SmartStackFoundation30CancellableObservationTrackingC
+ _symbolic _____Sg 20SmartStackUIServices22CardHostSceneViewModelC
+ _symbolic _____Sg 7SwiftUI13AnyShapeStyleV
+ _symbolic _____SgXw 20SmartStackUIServices22CardHostSceneViewModelC
+ _symbolic _____SgXw 20SmartStackUIServices22CardHostViewControllerC
+ _symbolic _____SgXw 20SmartStackUIServices22CardSceneHostComponentC
+ _symbolic _____SgXw 20SmartStackUIServices24CardSceneClientComponentC
+ _symbolic _____SgXw 20SmartStackUIServices30ViewHitTestingAssertionManagerC
+ _symbolic _____SgXwz_Xx 20SmartStackUIServices22CardHostViewControllerC
+ _symbolic ______p 20SmartStackUIServices27DetachedSceneTimerProvidingP
+ _symbolic ______pSg 20SmartStackUIServices18DetachedSceneTimerP
+ _symbolic ______pSg So33BLSHBacklightSceneHostEnvironmentP
+ _symbolic ______pSgXw 20SmartStackUIServices30CardHostViewControllerDelegateP
+ _symbolic ______pSgXw 20SmartStackUIServices30CardSceneHostComponentDelegateP
+ _symbolic ______pSgXw 20SmartStackUIServices32CardSceneClientComponentDelegateP
+ _symbolic _____yAAyAAyAAy_____ABG_____yADy__________G_____y_____SgGGGABGAIG 7SwiftUI19_ConditionalContentV 20SmartStackUIServices12CardHostViewV05ErrorJ0V AA08ModifiedD0V AD0hi5SceneJ0V AA14_OpacityEffectV AA16_OverlayModifierV AF011PlaceholderJ0V
+ _symbolic _____yAAyAAy_____ABG_____yADy__________G_____y_____SgGGGABG 7SwiftUI19_ConditionalContentV 20SmartStackUIServices12CardHostViewV05ErrorJ0V AA08ModifiedD0V AD0hi5SceneJ0V AA14_OpacityEffectV AA16_OverlayModifierV AF011PlaceholderJ0V
+ _symbolic _____yAAy_____ABG_____yADy__________G_____y_____SgGGG 7SwiftUI19_ConditionalContentV 20SmartStackUIServices12CardHostViewV05ErrorJ0V AA08ModifiedD0V AD0hi5SceneJ0V AA14_OpacityEffectV AA16_OverlayModifierV AF011PlaceholderJ0V
+ _symbolic _____yAAy__________G_____y_____SgGG 7SwiftUI15ModifiedContentV 20SmartStackUIServices17CardHostSceneViewV AA14_OpacityEffectV AA16_OverlayModifierV AD0hiK0V011PlaceholderK0V
+ _symbolic _____yAAy_____y_____y_____y______Qo__A2EQPGG_____G_____y_____SgGG 7SwiftUI15ModifiedContentV AA6VStackV AA05TupleD0V AA4ViewPAAE8redacted6reasonQrAA16RedactionReasonsV_tFQO AA4TextV AA16_FlexFrameLayoutV AA30_EnvironmentKeyWritingModifierV AA13AnyShapeStyleV
+ _symbolic _____ySSG s23_ContiguousArrayStorageC
+ _symbolic _____y_____ABG 7SwiftUI19_ConditionalContentV 20SmartStackUIServices12CardHostViewV05ErrorJ0V
+ _symbolic _____y_____G 7SwiftUI19UIHostingControllerC 20SmartStackUIServices12CardHostViewV
+ _symbolic _____y_____G 7SwiftUI30HierarchicalShapeStyleModifierV AA04TintdE0V
+ _symbolic _____y_____G 7SwiftUI30_EnvironmentKeyWritingModifierV AA19WatchDisplayVariantO
+ _symbolic _____y_____G 7SwiftUI41_ContainerRoundedRectangularShapeModifierV AA0D9RectangleV
+ _symbolic _____y_____G s11_SetStorageC s6UInt32V
+ _symbolic _____y_____GSg 7SwiftUI19UIHostingControllerC 20SmartStackUIServices12CardHostViewV
+ _symbolic _____y_____SgG 7SwiftUI16_OverlayModifierV 20SmartStackUIServices12CardHostViewV011PlaceholderJ0V
+ _symbolic _____y_____So31BKSTouchDeliveryPolicyAssertionCG s18_DictionaryStorageC s6UInt32V
+ _symbolic _____y______Qo_ 7SwiftUI4ViewPAAE8redacted6reasonQrAA16RedactionReasonsV_tFQO AA4TextV
+ _symbolic _____y______Qo__A2Bt 7SwiftUI4ViewPAAE8redacted6reasonQrAA16RedactionReasonsV_tFQO AA4TextV
+ _symbolic _____y__________G 7SwiftUI15ModifiedContentV 20SmartStackUIServices17CardHostSceneViewV AA14_OpacityEffectV
+ _symbolic _____y___________y_____y______Qo__A2EQPGG 7SwiftUI13_VariadicViewO4TreeV AA13_VStackLayoutV AA12TupleContentV AA0D0PAAE8redacted6reasonQrAA16RedactionReasonsV_tFQO AA4TextV
+ _symbolic _____y__________y_____GG 7SwiftUI15ModifiedContentV AA5ImageV AA24_ForegroundStyleModifierV AA5ColorV
+ _symbolic _____y______pG s23_ContiguousArrayStorageC s7CVarArgP
+ _symbolic _____y______yABy_____y_____y_____y______Qo__A2FQPGG_____G_____y_____SgGGG 20SmartStackUIServices12CardHostViewV0D9ContainerV 7SwiftUI15ModifiedContentV AF6VStackV AF05TupleK0V AF0F0PAFE8redacted6reasonQrAF16RedactionReasonsV_tFQO AF4TextV AF16_FlexFrameLayoutV AF30_EnvironmentKeyWritingModifierV AF13AnyShapeStyleV
+ _symbolic _____y______y_____y______ADQPGGG 20SmartStackUIServices12CardHostViewV0D9ContainerV 7SwiftUI6VStackV AF12TupleContentV AF4TextV
+ _symbolic _____y_____yAAyAAyAAy_____ABG_____yADy__________G_____y_____SgGGGABGAIG_Qo_ 7SwiftUI4ViewP9WidgetKitE24defineFontsForSmartStackQryFQO AA19_ConditionalContentV 0iJ10UIServices08CardHostC0V05ErrorC0V AA08ModifiedL0V AH0no5SceneC0V AA14_OpacityEffectV AA16_OverlayModifierV AJ011PlaceholderC0V
+ _symbolic _____y_____yAAyAAyAAy_____yx_Qo______y_____GG_____G_____G______Qo______yAKGG 7SwiftUI15ModifiedContentV AA4ViewPAAE12_glassEffect_2inQrAA6_GlassV_qd__tAA5ShapeRd__lFQO AE9WidgetKitE24defineFontsForSmartStackQryFQO AA30_EnvironmentKeyWritingModifierV AA19WatchDisplayVariantO AA14_PaddingLayoutV AA06_FrameZ0V AA16RoundedRectangleV AA028_ContainerRoundedRectangularjU0V
+ _symbolic _____y_____y______y_____y______AEQPGGG_____G 7SwiftUI19_ConditionalContentV 20SmartStackUIServices12CardHostViewV0H9ContainerV AA6VStackV AA05TupleD0V AA4TextV AA05EmptyJ0V
+ _symbolic _____y_____y_____yAByAByABy_____ACGAAyAAy__________G_____y_____SgGGGACGAIG_Qo______y_____GG 7SwiftUI15ModifiedContentV AA4ViewP9WidgetKitE24defineFontsForSmartStackQryFQO AA012_ConditionalD0V 0kL10UIServices08CardHostE0V05ErrorE0V AJ0op5SceneE0V AA14_OpacityEffectV AA16_OverlayModifierV AL011PlaceholderE0V AA022_EnvironmentKeyWritingV0V AA19WatchDisplayVariantO
+ _symbolic _____y_____y_____y_____y______Qo__A2EQPGG_____G 7SwiftUI15ModifiedContentV AA6VStackV AA05TupleD0V AA4ViewPAAE8redacted6reasonQrAA16RedactionReasonsV_tFQO AA4TextV AA16_FlexFrameLayoutV
+ _symbolic _____yyXlXpG s23_ContiguousArrayStorageC
+ _symbolic qd__
+ _symbolic x
+ _symbolic xyc
+ _symbolic yXlXp
+ _symbolic ypSg
+ _symbolic yt
+ _symbolic ytIeAgHr_
+ _symbolic yt______pIgrzo_ s5ErrorP
+ _symbolic yyYbScMYccSg
+ _type_layout_string 20SmartStackUIServices12CardHostViewV
+ _type_layout_string 20SmartStackUIServices12CardHostViewV011PlaceholderF0V
+ _type_layout_string 20SmartStackUIServices12CardHostViewV05ErrorF0V
+ _type_layout_string 20SmartStackUIServices17CardHostSceneViewV
+ _type_layout_string 7SwiftUI4ViewRzl20SmartStackUIServices08CardHostC0V0G9ContainerVy_xG
- ___swift_memcpy17_8
CStrings:
+ " active but missing scene"
+ " scene deactivated"
+ " scene invalidated"
+ "%s Backstop timer fired but VC is back in hierarchy or already inactive. No-op."
+ "%s Backstop timer fired — deactivating detached scene to prevent resource leak."
+ "%s Detached scene detected (%s). Starting %fs backstop timer."
+ "%s Re-attached to hierarchy (%s). Cancelling backstop timer."
+ "%s allowBacklightActiveCardUpdates=(%{bool}d)"
+ "%s backlightSceneEnvironment changed: %s"
+ "%s deinit"
+ "%s isActive=(%{bool}d) tintColor=%s"
+ "%s set glassStyleFraction=%f (isActive=%{bool}d)"
+ "%s set tintColor=%s (isActive=%{bool}d)"
+ "%s takeTouchCancellationAssertion: %s"
+ "%s: could not acquire assertion — sceneHostViewModel is unavailable (isActive=%{bool}d)"
+ "-DetachedSceneTimer"
+ "CardHostSceneViewModel-ReadyBackstop-"
+ "Clearing any touch delivery policies"
+ "Fatal error"
+ "Glass subvariant base '%{public}s' mix=%f (suppressForeground=%{bool}d, layerId=%ld)"
+ "Incorrect actor executor assumption; Expected same executor as "
+ "Invalidating assertion for context id %u"
+ "Saving touch policy assertion for context id %u"
+ "Sending touch delivery policy failed with error: %s"
+ "SmartStackUIServices.Assertion"
+ "SmartStackUIServices.CardHostSceneViewController"
+ "SmartStackUIServices.CardHostViewController"
+ "SmartStackUIServices/CardHostSceneView.swift"
+ "SmartStackUIServices/CardHostSceneViewModel.swift"
+ "SmartStackUIServices/CardHostView+CardContainer.swift"
+ "SmartStackUIServices/CardHostView+ErrorView.swift"
+ "SmartStackUIServices/CardHostView+PlaceholderView.swift"
+ "SmartStackUIServices/CardHostView.swift"
+ "SmartStackUIServices/CardHostViewController.swift"
+ "SmartStackUIServices/CardSceneHostComponent.swift"
+ "SmartStackUIServices/DetachedSceneTimer.swift"
+ "SmartStackUIServices/ViewHitTestingAssertionManager.swift"
+ "Updating touch delivery policies for layers: %@"
+ "ViewHitTestingAssertion"
+ "allowBacklightActiveCardUpdates changed: %{bool}d"
+ "cardGlassStyleFraction changed: %f"
+ "cardTintColor changed to %s but delegate is nil — update dropped (initial-tint sync should cover connect)"
+ "cardTintColor changed: %s"
+ "com.apple.NanoSmartStack"
+ "com.apple.clockface"
+ "hero27"
+ "init()"
+ "init(coder:) has not been implemented"
+ "init(nibName:bundle:)"
+ "questionmark.circle"
+ "received contentReadyForDisplay"
+ "removeAssertion: removed assertion on view layer (assertions=%ld)"
+ "removeAssertion: restored hit testing on view layer (last assertion)"
+ "sceneDidInvalidate"
+ "sceneWillDeactivate"
+ "signaling contentReadyForDisplay"
+ "smart-stack-card"
+ "takeAssertion: added assertion on view layer (assertions=%ld)"
+ "takeAssertion: disabled hit testing on view layer (assertions=1)"
+ "takeAssertion: view deallocated, cannot take assertion"
+ "takeTouchCancellationAssertion()"
+ "v16@?0^v8"
+ "viewDidDisappear"
+ "watchSmartStackFace"
- "Selected glass subvariant '%{public}s' (suppressForeground=%{bool}d, layerId=%ld)"
```
