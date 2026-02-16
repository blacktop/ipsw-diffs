## CarPlayUIServices

> `/System/Library/PrivateFrameworks/CarPlayUIServices.framework/CarPlayUIServices`

```diff

-526.35.1.0.0
-  __TEXT.__text: 0x1c2f4
-  __TEXT.__auth_stubs: 0x500
-  __TEXT.__objc_methlist: 0x2e5c
-  __TEXT.__const: 0x1f0
-  __TEXT.__oslogstring: 0xda5
-  __TEXT.__cstring: 0x1363
-  __TEXT.__gcc_except_tab: 0x420
-  __TEXT.__unwind_info: 0x998
-  __TEXT.__objc_classname: 0xf18
-  __TEXT.__objc_methname: 0x5e0d
-  __TEXT.__objc_methtype: 0x1474
-  __TEXT.__objc_stubs: 0x4060
-  __DATA_CONST.__got: 0x3f8
-  __DATA_CONST.__const: 0x8f0
-  __DATA_CONST.__objc_classlist: 0x280
+555.9.0.0.0
+  __TEXT.__text: 0x2a478
+  __TEXT.__auth_stubs: 0xb60
+  __TEXT.__objc_methlist: 0x30dc
+  __TEXT.__const: 0x5b4
+  __TEXT.__oslogstring: 0x1274
+  __TEXT.__cstring: 0x16c2
+  __TEXT.__gcc_except_tab: 0x5d4
+  __TEXT.__swift5_typeref: 0x1da
+  __TEXT.__swift5_fieldmd: 0x12c
+  __TEXT.__constg_swiftt: 0x15c
+  __TEXT.__swift5_reflstr: 0x159
+  __TEXT.__swift5_builtin: 0x28
+  __TEXT.__swift5_capture: 0x44
+  __TEXT.__swift5_protos: 0x4
+  __TEXT.__swift5_types: 0x18
+  __TEXT.__swift5_assocty: 0x30
+  __TEXT.__swift5_proto: 0x30
+  __TEXT.__unwind_info: 0xe00
+  __TEXT.__eh_frame: 0x40
+  __TEXT.__objc_classname: 0x10b1
+  __TEXT.__objc_methname: 0x644c
+  __TEXT.__objc_methtype: 0x16a5
+  __TEXT.__objc_stubs: 0x46e0
+  __DATA_CONST.__got: 0x510
+  __DATA_CONST.__const: 0xab0
+  __DATA_CONST.__objc_classlist: 0x2c0
   __DATA_CONST.__objc_catlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x158
+  __DATA_CONST.__objc_protolist: 0x168
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1618
-  __DATA_CONST.__objc_protorefs: 0x90
+  __DATA_CONST.__objc_selrefs: 0x17c0
+  __DATA_CONST.__objc_protorefs: 0x98
   __DATA_CONST.__objc_superrefs: 0x180
   __DATA_CONST.__objc_arraydata: 0x40
-  __AUTH_CONST.__auth_got: 0x290
-  __AUTH_CONST.__const: 0x4e0
-  __AUTH_CONST.__cfstring: 0x11c0
-  __AUTH_CONST.__objc_const: 0xefc0
+  __AUTH_CONST.__auth_got: 0x5c0
+  __AUTH_CONST.__const: 0xbc8
+  __AUTH_CONST.__cfstring: 0x1280
+  __AUTH_CONST.__objc_const: 0xf6f8
   __AUTH_CONST.__objc_doubleobj: 0x80
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0x1900
-  __DATA.__objc_ivar: 0x328
-  __DATA.__data: 0x1030
-  __DATA.__bss: 0xc0
+  __AUTH.__objc_data: 0x1c70
+  __AUTH.__data: 0xe8
+  __DATA.__objc_ivar: 0x32c
+  __DATA.__data: 0x11e0
+  __DATA.__bss: 0x728
+  __DATA.__common: 0xf8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
+  - /System/Library/Frameworks/DeveloperToolsSupport.framework/DeveloperToolsSupport
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
+  - /System/Library/PrivateFrameworks/BoardServices.framework/BoardServices
   - /System/Library/PrivateFrameworks/CarKit.framework/CarKit
   - /System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 55BB98DB-BE6D-30A2-B88D-996483BA2E82
-  Functions: 950
-  Symbols:   4131
-  CStrings:  1718
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  - /usr/lib/swift/libswiftsimd.dylib
+  UUID: 56537145-7D2B-3847-A071-7A7754A0C670
+  Functions: 1245
+  Symbols:   4533
+  CStrings:  1863
 
Symbols:
+ -[CRSUIClimateDockSceneClientSettings isOverlayHidden]
+ -[CRSUIClimateDockSceneClientSettings mutableCopyWithZone:]
+ -[CRSUIClimateDockSceneClientSettings presentedPopoverFrames]
+ -[CRSUIClimateDockSceneClientSettings stepperInsets]
+ -[CRSUIClimateDockSceneSettings hasPhysicalControlBars]
+ -[CRSUIClimateDockSceneSettings mutableCopyWithZone:]
+ -[CRSUIClimateDockSceneSettings persistentElements]
+ -[CRSUIClimateDockSceneSettings primaryDockFrame]
+ -[CRSUIClimateDockSceneSettings secondaryDockFrame]
+ -[CRSUIClimateDockSceneSpecification clientSettingsClass]
+ -[CRSUIClimateDockSceneSpecification settingsClass]
+ -[CRSUIClimateQuickControlsSceneClientSettings mutableCopyWithZone:]
+ -[CRSUIClimateQuickControlsSceneSettings mutableCopyWithZone:]
+ -[CRSUIClimateQuickControlsSceneSpecification clientSettingsClass]
+ -[CRSUIClimateQuickControlsSceneSpecification settingsClass]
+ -[CRSUIClusterThemeManager _getActiveDriveMode:]
+ -[CRSUIClusterThemeManager _getLinked:]
+ -[CRSUIClusterThemeManager _hasDriveModeConfigurationOverride:]
+ -[CRSUIClusterThemeManager _resetCurrentDriveModeThemeOverride:]
+ -[CRSUIClusterThemeManager _setLinked:completionHandler:]
+ -[CRSUIClusterThemeManager activeDriveMode]
+ -[CRSUIClusterThemeManager getActiveDriveMode:]
+ -[CRSUIClusterThemeManager getLinked:]
+ -[CRSUIClusterThemeManager hasDriveModeConfigurationOverride:]
+ -[CRSUIClusterThemeManager resetCurrentDriveModeThemeOverride:]
+ -[CRSUIClusterThemeManager setActiveDriveMode:]
+ -[CRSUIClusterThemeManager setLinked:completionHandler:]
+ -[CRSUIClusterThemeService getActiveDriveMode:]
+ -[CRSUIClusterThemeService getActiveDriveMode:].cold.1
+ -[CRSUIClusterThemeService getDriveModeThemeLinked:]
+ -[CRSUIClusterThemeService getDriveModeThemeLinked:].cold.1
+ -[CRSUIClusterThemeService hasDriveModeConfigurationOverride:]
+ -[CRSUIClusterThemeService hasDriveModeConfigurationOverride:].cold.1
+ -[CRSUIClusterThemeService resetCurrentDriveModeThemeOverride:]
+ -[CRSUIClusterThemeService resetCurrentDriveModeThemeOverride:].cold.1
+ -[CRSUIClusterThemeService setActiveDriveMode:]
+ -[CRSUIClusterThemeService setDriveModeThemeLinked:reply:]
+ -[CRSUIClusterThemeService setDriveModeThemeLinked:reply:].cold.1
+ -[CRSUIMutableClimateDockSceneClientSettings copyWithZone:]
+ -[CRSUIMutableClimateDockSceneClientSettings isOverlayHidden]
+ -[CRSUIMutableClimateDockSceneClientSettings presentedPopoverFrames]
+ -[CRSUIMutableClimateDockSceneClientSettings setIsOverlayHidden:]
+ -[CRSUIMutableClimateDockSceneClientSettings setPresentedPopoverFrames:]
+ -[CRSUIMutableClimateDockSceneClientSettings setStepperInsets:]
+ -[CRSUIMutableClimateDockSceneClientSettings stepperInsets]
+ -[CRSUIMutableClimateDockSceneSettings copyWithZone:]
+ -[CRSUIMutableClimateDockSceneSettings hasPhysicalControlBars]
+ -[CRSUIMutableClimateDockSceneSettings persistentElements]
+ -[CRSUIMutableClimateDockSceneSettings primaryDockFrame]
+ -[CRSUIMutableClimateDockSceneSettings secondaryDockFrame]
+ -[CRSUIMutableClimateDockSceneSettings setHasPhysicalControlBars:]
+ -[CRSUIMutableClimateDockSceneSettings setPersistentElements:]
+ -[CRSUIMutableClimateDockSceneSettings setPrimaryDockFrame:]
+ -[CRSUIMutableClimateDockSceneSettings setSecondaryDockFrame:]
+ -[CRSUIMutableClimateQuickControlsSceneClientSettings copyWithZone:]
+ -[CRSUIMutableClimateQuickControlsSceneSettings copyWithZone:]
+ GCC_except_table13
+ GCC_except_table19
+ GCC_except_table40
+ _CGAffineTransformMakeScale
+ _CGSizeApplyAffineTransform
+ _OBJC_CLASS_$_CAAnimation
+ _OBJC_CLASS_$_CALayer
+ _OBJC_CLASS_$_CAScrollLayer
+ _OBJC_CLASS_$_CAShapeLayer
+ _OBJC_CLASS_$_CATextLayer
+ _OBJC_CLASS_$_CATiledLayer
+ _OBJC_CLASS_$_CATransaction
+ _OBJC_CLASS_$_CRSUIClimateDockSceneClientSettings
+ _OBJC_CLASS_$_CRSUIClimateDockSceneSettings
+ _OBJC_CLASS_$_CRSUIClimateDockSceneSpecification
+ _OBJC_CLASS_$_CRSUIClimateQuickControlsSceneClientSettings
+ _OBJC_CLASS_$_CRSUIClimateQuickControlsSceneSettings
+ _OBJC_CLASS_$_CRSUIClimateQuickControlsSceneSpecification
+ _OBJC_CLASS_$_CRSUIMutableClimateDockSceneClientSettings
+ _OBJC_CLASS_$_CRSUIMutableClimateDockSceneSettings
+ _OBJC_CLASS_$_CRSUIMutableClimateQuickControlsSceneClientSettings
+ _OBJC_CLASS_$_CRSUIMutableClimateQuickControlsSceneSettings
+ _OBJC_CLASS_$_NSKeyedUnarchiver
+ _OBJC_CLASS_$_NSTimer
+ _OBJC_CLASS_$_OS_os_log
+ _OBJC_CLASS_$__TtC17CarPlayUIServices15CRSUIMicaPlayer
+ _OBJC_CLASS_$__TtC17CarPlayUIServices19CRSUIMicaPlayerView
+ _OBJC_CLASS_$__TtCs12_SwiftObject
+ _OBJC_IVAR_$_CRSUIClusterThemeManager._activeDriveMode
+ _OBJC_IVAR_$_CRSUIMutableClimateDockSceneSettings._secondaryDockFrame
+ _OBJC_METACLASS_$_CRSUIClimateDockSceneClientSettings
+ _OBJC_METACLASS_$_CRSUIClimateDockSceneSettings
+ _OBJC_METACLASS_$_CRSUIClimateDockSceneSpecification
+ _OBJC_METACLASS_$_CRSUIClimateQuickControlsSceneClientSettings
+ _OBJC_METACLASS_$_CRSUIClimateQuickControlsSceneSettings
+ _OBJC_METACLASS_$_CRSUIClimateQuickControlsSceneSpecification
+ _OBJC_METACLASS_$_CRSUIMutableClimateDockSceneClientSettings
+ _OBJC_METACLASS_$_CRSUIMutableClimateDockSceneSettings
+ _OBJC_METACLASS_$_CRSUIMutableClimateQuickControlsSceneClientSettings
+ _OBJC_METACLASS_$_CRSUIMutableClimateQuickControlsSceneSettings
+ _OBJC_METACLASS_$__TtC17CarPlayUIServices15CRSUIMicaPlayer
+ _OBJC_METACLASS_$__TtC17CarPlayUIServices19CRSUIMicaPlayerView
+ _OBJC_METACLASS_$__TtCs12_SwiftObject
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ __Block_copy
+ __Block_release
+ __DATA__TtC17CarPlayUIServices15CRSUIMicaPlayer
+ __DATA__TtC17CarPlayUIServices19CRSUIMicaPlayerView
+ __DATA__TtC17CarPlayUIServicesP33_72AD03403294BC2F2FEA2FE615B9425019ResourceBundleClass
+ __INSTANCE_METHODS__TtC17CarPlayUIServices15CRSUIMicaPlayer
+ __INSTANCE_METHODS__TtC17CarPlayUIServices19CRSUIMicaPlayerView
+ __IVARS__TtC17CarPlayUIServices15CRSUIMicaPlayer
+ __IVARS__TtC17CarPlayUIServices19CRSUIMicaPlayerView
+ __METACLASS_DATA__TtC17CarPlayUIServices15CRSUIMicaPlayer
+ __METACLASS_DATA__TtC17CarPlayUIServices19CRSUIMicaPlayerView
+ __METACLASS_DATA__TtC17CarPlayUIServicesP33_72AD03403294BC2F2FEA2FE615B9425019ResourceBundleClass
+ __OBJC_$_INSTANCE_METHODS_CRSUIClimateDockSceneClientSettings
+ __OBJC_$_INSTANCE_METHODS_CRSUIClimateDockSceneSettings
+ __OBJC_$_INSTANCE_METHODS_CRSUIClimateDockSceneSpecification
+ __OBJC_$_INSTANCE_METHODS_CRSUIClimateQuickControlsSceneClientSettings
+ __OBJC_$_INSTANCE_METHODS_CRSUIClimateQuickControlsSceneSettings
+ __OBJC_$_INSTANCE_METHODS_CRSUIClimateQuickControlsSceneSpecification
+ __OBJC_$_INSTANCE_METHODS_CRSUIMutableClimateDockSceneClientSettings
+ __OBJC_$_INSTANCE_METHODS_CRSUIMutableClimateDockSceneSettings
+ __OBJC_$_INSTANCE_METHODS_CRSUIMutableClimateQuickControlsSceneClientSettings
+ __OBJC_$_INSTANCE_METHODS_CRSUIMutableClimateQuickControlsSceneSettings
+ __OBJC_$_INSTANCE_VARIABLES_CRSUIMutableClimateDockSceneSettings
+ __OBJC_$_PROP_LIST_CRSUIClimateDockSceneClientSettings
+ __OBJC_$_PROP_LIST_CRSUIClimateDockSceneSettings
+ __OBJC_$_PROP_LIST_CRSUIMutableClimateDockSceneClientSettings
+ __OBJC_$_PROP_LIST_CRSUIMutableClimateDockSceneSettings
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CRSUIClusterThemeObserving
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying
+ __OBJC_CLASS_RO_$_CRSUIClimateDockSceneClientSettings
+ __OBJC_CLASS_RO_$_CRSUIClimateDockSceneSettings
+ __OBJC_CLASS_RO_$_CRSUIClimateDockSceneSpecification
+ __OBJC_CLASS_RO_$_CRSUIClimateQuickControlsSceneClientSettings
+ __OBJC_CLASS_RO_$_CRSUIClimateQuickControlsSceneSettings
+ __OBJC_CLASS_RO_$_CRSUIClimateQuickControlsSceneSpecification
+ __OBJC_CLASS_RO_$_CRSUIMutableClimateDockSceneClientSettings
+ __OBJC_CLASS_RO_$_CRSUIMutableClimateDockSceneSettings
+ __OBJC_CLASS_RO_$_CRSUIMutableClimateQuickControlsSceneClientSettings
+ __OBJC_CLASS_RO_$_CRSUIMutableClimateQuickControlsSceneSettings
+ __OBJC_LABEL_PROTOCOL_$_NSCopying
+ __OBJC_METACLASS_RO_$_CRSUIClimateDockSceneClientSettings
+ __OBJC_METACLASS_RO_$_CRSUIClimateDockSceneSettings
+ __OBJC_METACLASS_RO_$_CRSUIClimateDockSceneSpecification
+ __OBJC_METACLASS_RO_$_CRSUIClimateQuickControlsSceneClientSettings
+ __OBJC_METACLASS_RO_$_CRSUIClimateQuickControlsSceneSettings
+ __OBJC_METACLASS_RO_$_CRSUIClimateQuickControlsSceneSpecification
+ __OBJC_METACLASS_RO_$_CRSUIMutableClimateDockSceneClientSettings
+ __OBJC_METACLASS_RO_$_CRSUIMutableClimateDockSceneSettings
+ __OBJC_METACLASS_RO_$_CRSUIMutableClimateQuickControlsSceneClientSettings
+ __OBJC_METACLASS_RO_$_CRSUIMutableClimateQuickControlsSceneSettings
+ __OBJC_PROTOCOL_$_NSCopying
+ __PROTOCOLS__TtC17CarPlayUIServices15CRSUIMicaPlayer
+ __PROTOCOLS__TtC17CarPlayUIServices15CRSUIMicaPlayer.3
+ ___38-[CRSUIClusterThemeManager getLinked:]_block_invoke
+ ___39-[CRSUIClusterThemeManager _getLinked:]_block_invoke
+ ___47-[CRSUIClusterThemeManager getActiveDriveMode:]_block_invoke
+ ___47-[CRSUIClusterThemeManager setActiveDriveMode:]_block_invoke
+ ___47-[CRSUIClusterThemeService getActiveDriveMode:]_block_invoke
+ ___47-[CRSUIClusterThemeService setActiveDriveMode:]_block_invoke
+ ___52-[CRSUIClusterThemeService getDriveModeThemeLinked:]_block_invoke
+ ___53-[CRSUIClusterThemeManager _setThemeData:completion:]_block_invoke.55
+ ___56-[CRSUIClusterThemeManager setLinked:completionHandler:]_block_invoke
+ ___58-[CRSUIClusterThemeService setDriveModeThemeLinked:reply:]_block_invoke
+ ___62-[CRSUIClusterThemeManager hasDriveModeConfigurationOverride:]_block_invoke
+ ___62-[CRSUIClusterThemeManager hasDriveModeConfigurationOverride:]_block_invoke_2
+ ___62-[CRSUIClusterThemeService hasDriveModeConfigurationOverride:]_block_invoke
+ ___63-[CRSUIClusterThemeManager resetCurrentDriveModeThemeOverride:]_block_invoke
+ ___63-[CRSUIClusterThemeService resetCurrentDriveModeThemeOverride:]_block_invoke
+ ___70-[CRSUIClusterThemeService listener:didReceiveConnection:withContext:]_block_invoke.94
+ ___79-[CRSUIClusterThemeManager _getURLForAssetWithIdentifier:displayID:completion:]_block_invoke.57
+ ___block_descriptor_40_e8_32bs_e30_v24?0"NSNumber"8"NSError"16ls32l8
+ ___block_descriptor_48_e8_32s40r_e42_v24?0"<CRSUIClusterThemeObserving>"8^B16lr40l8s32l8
+ ___block_descriptor_49_e8_32s40r_e42_v24?0"<CRSUIClusterThemeObserving>"8^B16lr40l8s32l8
+ ___block_descriptor_56_e8_32s40r48r_e42_v24?0"<CRSUIClusterThemeObserving>"8^B16lr40l8s32l8r48l8
+ ___block_descriptor_56_e8_32s40r48r_e42_v24?0"<CRSUIClusterThemeObserving>"8^B16ls32l8r40l8r48l8
+ ___block_literal_global.65
+ ___block_literal_global.67
+ ___chkstk_darwin
+ ___swift_allocate_value_buffer
+ ___swift_destroy_boxed_opaque_existential_0
+ ___swift_instantiateConcreteTypeFromMangledNameAbstractV2
+ ___swift_instantiateConcreteTypeFromMangledNameV2
+ ___swift_memcpy16_8
+ ___swift_noop_void_return
+ ___swift_project_boxed_opaque_existential_0
+ ___swift_project_value_buffer
+ ___swift_reflection_version
+ __swiftEmptyArrayStorage
+ __swiftEmptyDictionarySingleton
+ __swiftImmortalRefCount
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_CarPlayUIServices
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftCoreImage_$_CarPlayUIServices
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftDispatch_$_CarPlayUIServices
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation_$_CarPlayUIServices
+ __swift_FORCE_LOAD_$_swiftMetal
+ __swift_FORCE_LOAD_$_swiftMetal_$_CarPlayUIServices
+ __swift_FORCE_LOAD_$_swiftOSLog
+ __swift_FORCE_LOAD_$_swiftOSLog_$_CarPlayUIServices
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_CarPlayUIServices
+ __swift_FORCE_LOAD_$_swiftQuartzCore
+ __swift_FORCE_LOAD_$_swiftQuartzCore_$_CarPlayUIServices
+ __swift_FORCE_LOAD_$_swiftUIKit
+ __swift_FORCE_LOAD_$_swiftUIKit_$_CarPlayUIServices
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers_$_CarPlayUIServices
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftXPC_$_CarPlayUIServices
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_Builtin_float_$_CarPlayUIServices
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftos_$_CarPlayUIServices
+ __swift_FORCE_LOAD_$_swiftsimd
+ __swift_FORCE_LOAD_$_swiftsimd_$_CarPlayUIServices
+ __swift_stdlib_malloc_size
+ __swift_stdlib_reportUnimplementedInitializer
+ _associated conformance So22CALayerContentsGravityaSHSCSQ
+ _associated conformance So22CALayerContentsGravityas20_SwiftNewtypeWrapperSCSY
+ _associated conformance So22CALayerContentsGravityas20_SwiftNewtypeWrapperSCs35_HasCustomAnyHashableRepresentation
+ _block_copy_helper
+ _block_descriptor
+ _block_destroy_helper
+ _bzero
+ _free
+ _kCAGravityBottom
+ _kCAGravityBottomLeft
+ _kCAGravityBottomRight
+ _kCAGravityCenter
+ _kCAGravityLeft
+ _kCAGravityResize
+ _kCAGravityResizeAspect
+ _kCAGravityResizeAspectFill
+ _kCAGravityRight
+ _kCAGravityTop
+ _kCAGravityTopLeft
+ _kCAGravityTopRight
+ _malloc_size
+ _memcpy
+ _memmove
+ _objc_allocWithZone
+ _objc_msgSend$_getActiveDriveMode:
+ _objc_msgSend$_getLinked:
+ _objc_msgSend$_hasDriveModeConfigurationOverride:
+ _objc_msgSend$_resetCurrentDriveModeThemeOverride:
+ _objc_msgSend$_setLinked:completionHandler:
+ _objc_msgSend$addAnimation:forKey:
+ _objc_msgSend$animationForKey:
+ _objc_msgSend$animationKeys
+ _objc_msgSend$begin
+ _objc_msgSend$bundleForClass:
+ _objc_msgSend$clusterThemeManager:didUpdateDriveMode:
+ _objc_msgSend$clusterThemeService:didSetDriveModeThemeLinked:
+ _objc_msgSend$clusterThemeService:getActiveDriveModeWithError:
+ _objc_msgSend$clusterThemeService:getDriveModeThemeLinkedWithError:
+ _objc_msgSend$clusterThemeService:hasDriveModeConfigurationOverrideWithError:
+ _objc_msgSend$clusterThemeServiceDidClearCurrentDriveModeThemeConfiguration:
+ _objc_msgSend$clusterThemeServiceGetDisplayIdentifier:
+ _objc_msgSend$commit
+ _objc_msgSend$getActiveDriveMode:
+ _objc_msgSend$getDriveModeThemeLinked:
+ _objc_msgSend$hasDriveModeConfigurationOverride:
+ _objc_msgSend$init
+ _objc_msgSend$initWithCoder:
+ _objc_msgSend$initWithDynamicProvider:
+ _objc_msgSend$initWithFrame:
+ _objc_msgSend$insertSublayer:atIndex:
+ _objc_msgSend$isRemovedOnCompletion
+ _objc_msgSend$mainBundle
+ _objc_msgSend$mask
+ _objc_msgSend$name
+ _objc_msgSend$needsDisplay
+ _objc_msgSend$needsLayout
+ _objc_msgSend$numberWithBool:
+ _objc_msgSend$removeFromSuperlayer
+ _objc_msgSend$resetCurrentDriveModeThemeOverride:
+ _objc_msgSend$resolvedColorWithTraitCollection:
+ _objc_msgSend$scheduledTimerWithTimeInterval:repeats:block:
+ _objc_msgSend$setActiveDriveMode:
+ _objc_msgSend$setContentsMultiplyColor:
+ _objc_msgSend$setDisableActions:
+ _objc_msgSend$setDriveModeThemeLinked:reply:
+ _objc_msgSend$setFillColor:
+ _objc_msgSend$setFrame:
+ _objc_msgSend$setMask:
+ _objc_msgSend$setNeedsDisplay
+ _objc_msgSend$setNeedsLayout
+ _objc_msgSend$setRepeatCount:
+ _objc_msgSend$setStrokeColor:
+ _objc_msgSend$shouldArchiveValueForKey:
+ _objc_msgSend$sublayers
+ _objc_msgSend$superlayer
+ _objc_msgSend$unregisterObserver:
+ _objc_msgSend$valueForKey:
+ _objc_retain_x9
+ _swift_allocObject
+ _swift_arrayDestroy
+ _swift_beginAccess
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRelease_n
+ _swift_bridgeObjectRetain
+ _swift_bridgeObjectRetain_n
+ _swift_coroFrameAlloc
+ _swift_deallocClassInstance
+ _swift_deallocObject
+ _swift_deletedMethodError
+ _swift_dynamicCast
+ _swift_dynamicCastObjCClass
+ _swift_dynamicCastUnknownClass
+ _swift_endAccess
+ _swift_errorRelease
+ _swift_errorRetain
+ _swift_getErrorValue
+ _swift_getForeignTypeMetadata
+ _swift_getObjCClassFromMetadata
+ _swift_getObjCClassFromObject
+ _swift_getObjCClassMetadata
+ _swift_getObjectType
+ _swift_getTypeByMangledNameInContext2
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _swift_getWitnessTable
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_lookUpClassMethod
+ _swift_once
+ _swift_release
+ _swift_retain
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_unknownObjectRelease
+ _swift_unknownObjectRetain
+ _swift_unknownObjectWeakAssign
+ _swift_unknownObjectWeakDestroy
+ _swift_unknownObjectWeakInit
+ _swift_unknownObjectWeakLoadStrong
+ _symbolic $s17CarPlayUIServices23CRSUIMicaPlayerDelegateP
+ _symbolic $sSY
+ _symbolic $ss21_ObjectiveCBridgeableP
+ _symbolic SDySSypG
+ _symbolic SS
+ _symbolic SS_ypt
+ _symbolic SaySo7CALayerCG
+ _symbolic Sb
+ _symbolic Sd
+ _symbolic Sf
+ _symbolic So6UIViewC
+ _symbolic So7CALayerC
+ _symbolic So7NSTimerCSg
+ _symbolic So8NSObjectC
+ _symbolic So8NSStringC
+ _symbolic _____ 12CoreGraphics7CGFloatV
+ _symbolic _____ 17CarPlayUIServices15CRSUIMicaPlayerC
+ _symbolic _____ 17CarPlayUIServices19CRSUIMicaPlayerViewC
+ _symbolic _____ 17CarPlayUIServices19ResourceBundleClass33_72AD03403294BC2F2FEA2FE615B94250LLC
+ _symbolic _____ So22CALayerContentsGravitya
+ _symbolic _____ So6CGSizeV
+ _symbolic _____SgXw 17CarPlayUIServices15CRSUIMicaPlayerC
+ _symbolic _____So17UITraitCollectionCIeggg_ 17CarPlayUIServices15CRSUIMicaPlayerC
+ _symbolic _____So17UITraitCollectionCytIegnnr_ 17CarPlayUIServices15CRSUIMicaPlayerC
+ _symbolic _____XDXMT 17CarPlayUIServices19CRSUIMicaPlayerViewC
+ _symbolic ______pSgXw 17CarPlayUIServices23CRSUIMicaPlayerDelegateP
+ _symbolic _____ySSG s11_SetStorageC
+ _symbolic _____ySSypG s18_DictionaryStorageC
+ _symbolic _____y_____G s23_ContiguousArrayStorageC s5UInt8V
+ _symbolic _____y______pXpG s23_ContiguousArrayStorageC 5UIKit17UITraitDefinitionP
+ _symbolic _____yyXlXpG s23_ContiguousArrayStorageC
+ _symbolic x
+ _symbolic y______So17UITraitCollectionCtcSg 17CarPlayUIServices15CRSUIMicaPlayerC
+ _symbolic ypSg
+ _type_layout_string So22CALayerContentsGravitya
+ _type_layout_string So6CGSizeV
- -[CRSUIClimateOverlaySceneClientSettings isOverlayHidden]
- -[CRSUIClimateOverlaySceneClientSettings mutableCopyWithZone:]
- -[CRSUIClimateOverlaySceneClientSettings presentedPopoverFrames]
- -[CRSUIClimateOverlaySceneClientSettings stepperInsets]
- -[CRSUIClimateOverlaySceneSettings hasPhysicalControlBars]
- -[CRSUIClimateOverlaySceneSettings mutableCopyWithZone:]
- -[CRSUIClimateOverlaySceneSettings persistentElements]
- -[CRSUIClimateOverlaySceneSettings primaryDockFrame]
- -[CRSUIClimateOverlaySceneSettings secondaryDockFrame]
- -[CRSUIClimateOverlaySceneSpecification clientSettingsClass]
- -[CRSUIClimateOverlaySceneSpecification settingsClass]
- -[CRSUIMutableClimateOverlaySceneClientSettings copyWithZone:]
- -[CRSUIMutableClimateOverlaySceneClientSettings isOverlayHidden]
- -[CRSUIMutableClimateOverlaySceneClientSettings presentedPopoverFrames]
- -[CRSUIMutableClimateOverlaySceneClientSettings setIsOverlayHidden:]
- -[CRSUIMutableClimateOverlaySceneClientSettings setPresentedPopoverFrames:]
- -[CRSUIMutableClimateOverlaySceneClientSettings setStepperInsets:]
- -[CRSUIMutableClimateOverlaySceneClientSettings stepperInsets]
- -[CRSUIMutableClimateOverlaySceneSettings copyWithZone:]
- -[CRSUIMutableClimateOverlaySceneSettings hasPhysicalControlBars]
- -[CRSUIMutableClimateOverlaySceneSettings persistentElements]
- -[CRSUIMutableClimateOverlaySceneSettings primaryDockFrame]
- -[CRSUIMutableClimateOverlaySceneSettings secondaryDockFrame]
- -[CRSUIMutableClimateOverlaySceneSettings setHasPhysicalControlBars:]
- -[CRSUIMutableClimateOverlaySceneSettings setPersistentElements:]
- -[CRSUIMutableClimateOverlaySceneSettings setPrimaryDockFrame:]
- -[CRSUIMutableClimateOverlaySceneSettings setSecondaryDockFrame:]
- GCC_except_table14
- _OBJC_CLASS_$_CRSUIClimateOverlaySceneClientSettings
- _OBJC_CLASS_$_CRSUIClimateOverlaySceneSettings
- _OBJC_CLASS_$_CRSUIClimateOverlaySceneSpecification
- _OBJC_CLASS_$_CRSUIMutableClimateOverlaySceneClientSettings
- _OBJC_CLASS_$_CRSUIMutableClimateOverlaySceneSettings
- _OBJC_IVAR_$_CRSUIMutableClimateOverlaySceneSettings._secondaryDockFrame
- _OBJC_METACLASS_$_CRSUIClimateOverlaySceneClientSettings
- _OBJC_METACLASS_$_CRSUIClimateOverlaySceneSettings
- _OBJC_METACLASS_$_CRSUIClimateOverlaySceneSpecification
- _OBJC_METACLASS_$_CRSUIMutableClimateOverlaySceneClientSettings
- _OBJC_METACLASS_$_CRSUIMutableClimateOverlaySceneSettings
- __OBJC_$_INSTANCE_METHODS_CRSUIClimateOverlaySceneClientSettings
- __OBJC_$_INSTANCE_METHODS_CRSUIClimateOverlaySceneSettings
- __OBJC_$_INSTANCE_METHODS_CRSUIClimateOverlaySceneSpecification
- __OBJC_$_INSTANCE_METHODS_CRSUIMutableClimateOverlaySceneClientSettings
- __OBJC_$_INSTANCE_METHODS_CRSUIMutableClimateOverlaySceneSettings
- __OBJC_$_INSTANCE_VARIABLES_CRSUIMutableClimateOverlaySceneSettings
- __OBJC_$_PROP_LIST_CRSUIClimateOverlaySceneClientSettings
- __OBJC_$_PROP_LIST_CRSUIClimateOverlaySceneSettings
- __OBJC_$_PROP_LIST_CRSUIMutableClimateOverlaySceneClientSettings
- __OBJC_$_PROP_LIST_CRSUIMutableClimateOverlaySceneSettings
- __OBJC_CLASS_RO_$_CRSUIClimateOverlaySceneClientSettings
- __OBJC_CLASS_RO_$_CRSUIClimateOverlaySceneSettings
- __OBJC_CLASS_RO_$_CRSUIClimateOverlaySceneSpecification
- __OBJC_CLASS_RO_$_CRSUIMutableClimateOverlaySceneClientSettings
- __OBJC_CLASS_RO_$_CRSUIMutableClimateOverlaySceneSettings
- __OBJC_METACLASS_RO_$_CRSUIClimateOverlaySceneClientSettings
- __OBJC_METACLASS_RO_$_CRSUIClimateOverlaySceneSettings
- __OBJC_METACLASS_RO_$_CRSUIClimateOverlaySceneSpecification
- __OBJC_METACLASS_RO_$_CRSUIMutableClimateOverlaySceneClientSettings
- __OBJC_METACLASS_RO_$_CRSUIMutableClimateOverlaySceneSettings
- ___53-[CRSUIClusterThemeManager _setThemeData:completion:]_block_invoke.44
- ___70-[CRSUIClusterThemeService listener:didReceiveConnection:withContext:]_block_invoke.79
- ___79-[CRSUIClusterThemeManager _getURLForAssetWithIdentifier:displayID:completion:]_block_invoke.46
- ___block_literal_global.53
- ___block_literal_global.55
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$addObserver:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x3
- _objc_retain_x4
CStrings:
+ "@\"NSError\"24@0:8@\"CRSUIClusterThemeService\"16"
+ "@\"NSError\"28@0:8@\"CRSUIClusterThemeService\"16B24"
+ "@\"NSString\"24@0:8@\"CRSUIClusterThemeService\"16"
+ "@\"NSString\"32@0:8@\"CRSUIClusterThemeService\"16^@24"
+ "@24@0:8^v16"
+ "@28@0:8@16B24"
+ "@32@0:8@16^@24"
+ "Active drive mode: %@"
+ "B32@0:8@\"CRSUIClusterThemeService\"16^@24"
+ "B32@0:8@16^@24"
+ "CRSUIClimateDockSceneClientSettings"
+ "CRSUIClimateDockSceneSettings"
+ "CRSUIClimateDockSceneSpecification"
+ "CRSUIClimateQuickControlsSceneClientSettings"
+ "CRSUIClimateQuickControlsSceneSettings"
+ "CRSUIClimateQuickControlsSceneSpecification"
+ "CRSUIMutableClimateDockSceneClientSettings"
+ "CRSUIMutableClimateDockSceneSettings"
+ "CRSUIMutableClimateQuickControlsSceneClientSettings"
+ "CRSUIMutableClimateQuickControlsSceneSettings"
+ "CarPlayUIServices.CRSUIMicaPlayer"
+ "CarPlayUIServices.CRSUIMicaPlayerView"
+ "CarPlayUIServices/CRSUIMicaPlayerView.swift"
+ "Cluster_Display"
+ "Connection not available"
+ "Current drive mode theme configuration state: %@"
+ "Drive mode theme linked state: %@"
+ "Error clearing current drive mode theme configuration: %@"
+ "Error getting active drive mode: %@"
+ "Error getting current drive mode theme configuration state: %@"
+ "Error getting drive mode theme linked state: %@"
+ "Error setting drive mode theme linked: %@"
+ "Fatal error"
+ "NO"
+ "NSCopying"
+ "Normal"
+ "Received request for active drive mode (connection: %@)"
+ "Received request for current drive mode theme configuration state (connection: %@)"
+ "Received request for drive mode theme linked state (connection: %@)"
+ "Received request to clear current drive mode theme configuration (connection: %@)"
+ "Received request to set drive mode theme linked (connection: %@): %@"
+ "Successfully cleared current drive mode theme configuration"
+ "Successfully set drive mode theme linked to: %@"
+ "T@\"NSString\",&,N,V_activeDriveMode"
+ "Unable to decode Mica file: %{public}s"
+ "Unable to find Mica document: %{public}s with extension .caar"
+ "Unable to load Mica document with path: %{public}s"
+ "Unable to open Mica file: %{public}s: %{public}s"
+ "Unknown gravity: %s"
+ "Unsupported file extension '%{public}s' for path: %{public}s. Supported extension: .caar"
+ "Vv24@0:8@?<v@?@\"NSError\">16"
+ "Vv24@0:8@?<v@?@\"NSNumber\"@\"NSError\">16"
+ "Vv24@0:8@?<v@?@\"NSString\"@\"NSError\">16"
+ "Vv32@0:8@\"NSNumber\"16@?<v@?@\"NSError\">24"
+ "YES"
+ "_TtC17CarPlayUIServices15CRSUIMicaPlayer"
+ "_TtC17CarPlayUIServices19CRSUIMicaPlayerView"
+ "_TtC17CarPlayUIServicesP33_72AD03403294BC2F2FEA2FE615B9425019ResourceBundleClass"
+ "_activeDriveMode"
+ "_getActiveDriveMode:"
+ "_getLinked:"
+ "_hasDriveModeConfigurationOverride:"
+ "_preferredPlaybackSpeed"
+ "_resetCurrentDriveModeThemeOverride:"
+ "_setLinked:completionHandler:"
+ "activeDriveMode"
+ "addAnimation:forKey:"
+ "animationForKey:"
+ "animationKeys"
+ "backgroundFilters"
+ "begin"
+ "bundleForClass:"
+ "clusterThemeManager:didUpdateDriveMode:"
+ "clusterThemeService:didSetDriveModeThemeLinked:"
+ "clusterThemeService:getActiveDriveModeWithError:"
+ "clusterThemeService:getDriveModeThemeLinkedWithError:"
+ "clusterThemeService:hasDriveModeConfigurationOverrideWithError:"
+ "clusterThemeServiceDidClearCurrentDriveModeThemeConfiguration:"
+ "clusterThemeServiceGetDisplayIdentifier:"
+ "colorCustomization"
+ "commit"
+ "compositingFilter"
+ "contentGravity"
+ "edgeAntialiasingMask"
+ "getActiveDriveMode:"
+ "getDriveModeThemeLinked:"
+ "getLinked:"
+ "hasDriveModeConfigurationOverride:"
+ "init()"
+ "init(coder:) has not been implemented. Use init(micaPlayer:frame:) instead."
+ "init(frame:)"
+ "initWithDynamicProvider:"
+ "insertSublayer:atIndex:"
+ "isNotifyingDelegate"
+ "isRemovedOnCompletion"
+ "levelsOfDetailBias"
+ "loopDuringPlayback"
+ "magnificationFilter"
+ "mainBundle"
+ "manager driveMode=%@"
+ "mask"
+ "micaPlayer"
+ "minificationFilter"
+ "minificationFilterBias"
+ "name"
+ "needsDisplay"
+ "needsDisplayOnBoundsChange"
+ "needsLayout"
+ "numberWithBool:"
+ "packageSize"
+ "path"
+ "playTimer"
+ "publishedObjects"
+ "rasterizationScale"
+ "removeFromSuperlayer"
+ "resetCurrentDriveModeThemeOverride:"
+ "resolvedColorWithTraitCollection:"
+ "retinaScale"
+ "scheduledTimerWithTimeInterval:repeats:block:"
+ "service driveMode=%@"
+ "setActiveDriveMode:"
+ "setContentsMultiplyColor:"
+ "setDisableActions:"
+ "setDriveModeThemeLinked:reply:"
+ "setFillColor:"
+ "setFrame:"
+ "setLinked:completionHandler:"
+ "setMask:"
+ "setNeedsDisplay"
+ "setNeedsLayout"
+ "setRepeatCount:"
+ "setStrokeColor:"
+ "shadowPathIsBounds"
+ "shouldArchiveValueForKey:"
+ "sublayerTransform"
+ "sublayers"
+ "superlayer"
+ "unregisterObserver:"
+ "v16@?0@\"NSTimer\"8"
+ "v24@?0@\"NSNumber\"8@\"NSError\"16"
+ "v28@0:8B16@?20"
+ "valueForKey:"
- "7"
- "CRSUIClimateOverlaySceneClientSettings"
- "CRSUIClimateOverlaySceneSettings"
- "CRSUIClimateOverlaySceneSpecification"
- "CRSUIMutableClimateOverlaySceneClientSettings"
- "CRSUIMutableClimateOverlaySceneSettings"

```
