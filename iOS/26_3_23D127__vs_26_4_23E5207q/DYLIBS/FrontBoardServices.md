## FrontBoardServices

> `/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`

```diff

-1000.3.4.100.0
-  __TEXT.__text: 0xa3878
-  __TEXT.__auth_stubs: 0x1110
+1000.4.9.0.0
+  __TEXT.__text: 0xa1800
+  __TEXT.__auth_stubs: 0x10a0
   __TEXT.__delay_helper: 0xdc
-  __TEXT.__objc_methlist: 0x8618
+  __TEXT.__objc_methlist: 0x84f8
   __TEXT.__const: 0x270
-  __TEXT.__cstring: 0xcbf4
+  __TEXT.__cstring: 0xc888
   __TEXT.__oslogstring: 0x3d7d
-  __TEXT.__gcc_except_tab: 0x2410
-  __TEXT.__unwind_info: 0x2cd8
-  __TEXT.__objc_classname: 0x145f
-  __TEXT.__objc_methname: 0x105ee
+  __TEXT.__gcc_except_tab: 0x22c4
+  __TEXT.__unwind_info: 0x2e78
+  __TEXT.__objc_classname: 0x1424
+  __TEXT.__objc_methname: 0x10278
   __TEXT.__objc_methtype: 0x35a6
-  __TEXT.__objc_stubs: 0xb240
-  __DATA_CONST.__got: 0x720
-  __DATA_CONST.__const: 0x2fa0
-  __DATA_CONST.__objc_classlist: 0x4a0
+  __TEXT.__objc_stubs: 0xaee0
+  __DATA_CONST.__got: 0x718
+  __DATA_CONST.__const: 0x3030
+  __DATA_CONST.__objc_classlist: 0x490
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x220
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3df0
+  __DATA_CONST.__objc_selrefs: 0x3ce0
   __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__objc_superrefs: 0x318
   __DATA_CONST.__objc_arraydata: 0x8
-  __AUTH_CONST.__auth_got: 0x898
-  __AUTH_CONST.__const: 0x860
-  __AUTH_CONST.__cfstring: 0xa3e0
-  __AUTH_CONST.__objc_const: 0x10330
+  __AUTH_CONST.__auth_got: 0x860
+  __AUTH_CONST.__const: 0x840
+  __AUTH_CONST.__cfstring: 0xa180
+  __AUTH_CONST.__objc_const: 0xffd0
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__objc_intobj: 0x90
+  __AUTH_CONST.__objc_intobj: 0x48
   __AUTH.__objc_data: 0xdc0
   __DATA.__objc_ivar: 0xa60
   __DATA.__data: 0x19b4
-  __DATA.__bss: 0x398
-  __DATA_DIRTY.__objc_data: 0x2080
-  __DATA_DIRTY.__bss: 0x1f8
+  __DATA.__bss: 0x3a8
+  __DATA_DIRTY.__objc_data: 0x1fe0
+  __DATA_DIRTY.__bss: 0x1c8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A22C8550-B61B-345D-8096-A663707AAC84
-  Functions: 4305
-  Symbols:   13701
-  CStrings:  6940
+  UUID: F0AD0E5A-E297-3BDE-B302-99727611D347
+  Functions: 4423
+  Symbols:   14042
+  CStrings:  6845
 
Symbols:
+ _FBLogShutdown
+ _FBLogShutdown.__logObj
+ _FBLogShutdown.cold.1
+ _FBLogShutdown.onceToken
+ _OUTLINED_FUNCTION_57
+ _OUTLINED_FUNCTION_58
+ _OUTLINED_FUNCTION_59
+ _OUTLINED_FUNCTION_60
+ _OUTLINED_FUNCTION_61
+ _OUTLINED_FUNCTION_62
+ _OUTLINED_FUNCTION_63
+ _OUTLINED_FUNCTION_64
+ _OUTLINED_FUNCTION_65
+ _OUTLINED_FUNCTION_66
+ _OUTLINED_FUNCTION_67
+ _OUTLINED_FUNCTION_68
+ _OUTLINED_FUNCTION_69
+ _OUTLINED_FUNCTION_70
+ _OUTLINED_FUNCTION_71
+ _OUTLINED_FUNCTION_72
+ _OUTLINED_FUNCTION_73
+ _OUTLINED_FUNCTION_74
+ ___FBLogShutdown_block_invoke
+ ___block_literal_global.25
+ _objc_msgSend$shouldPreventLaunch
+ _objc_release_x2
- +[FBSDeviceEmulationConfiguration _forceIsD22ChecksToPass]
- +[FBSDeviceEmulationConfiguration _isEmulatedDeviceViaDefaults]
- +[FBSDeviceEmulationConfiguration _isEmulatedDeviceViaGestalt]
- +[FBSDeviceEmulationConfiguration _isEmulatedDeviceViaGestalt].cold.1
- +[FBSDeviceEmulationConfiguration _sharedDefaults]
- +[FBSDeviceEmulationConfiguration _sharedDefaults].cold.1
- +[FBSDeviceEmulationConfiguration customScaleFactorX]
- +[FBSDeviceEmulationConfiguration customScaleFactorY]
- +[FBSDeviceEmulationConfiguration customTranslationOffsetX]
- +[FBSDeviceEmulationConfiguration customTranslationOffsetY]
- +[FBSDeviceEmulationConfiguration deviceEmulationVersion]
- +[FBSDeviceEmulationConfiguration emulatedArtworkSubtype]
- +[FBSDeviceEmulationConfiguration emulatedDeviceBezelImageName]
- +[FBSDeviceEmulationConfiguration emulatedDeviceBounds]
- +[FBSDeviceEmulationConfiguration emulatedDeviceClass]
- +[FBSDeviceEmulationConfiguration emulatedDeviceImageContainingBundle]
- +[FBSDeviceEmulationConfiguration emulatedDeviceMaskImageName]
- +[FBSDeviceEmulationConfiguration emulatedDisplayCornerRadius]
- +[FBSDeviceEmulationConfiguration emulatedHomeButtonType]
- +[FBSDeviceEmulationConfiguration hasEmulatedDeviceBounds]
- +[FBSDeviceEmulationConfiguration isEmulatedDevice]
- +[FBSDeviceEmulationConfiguration rootLayerBackgroundColorString]
- +[FBSDeviceEmulationConfiguration scalingStyle]
- -[FBSDeviceEmulationDefaults _bindAndRegisterDefaults]
- -[FBSSettings mutableCopyWithZone:].cold.1
- _MGGetBoolAnswer
- _OBJC_CLASS_$_BSAbstractDefaultDomain
- _OBJC_CLASS_$_FBSDeviceEmulationConfiguration
- _OBJC_CLASS_$_FBSDeviceEmulationDefaults
- _OBJC_METACLASS_$_BSAbstractDefaultDomain
- _OBJC_METACLASS_$_FBSDeviceEmulationConfiguration
- _OBJC_METACLASS_$_FBSDeviceEmulationDefaults
- __OBJC_$_CLASS_METHODS_FBSDeviceEmulationConfiguration
- __OBJC_$_CLASS_PROP_LIST_FBSDeviceEmulationConfiguration
- __OBJC_$_INSTANCE_METHODS_FBSDeviceEmulationDefaults
- __OBJC_$_PROP_LIST_FBSDeviceEmulationDefaults
- __OBJC_CLASS_RO_$_FBSDeviceEmulationConfiguration
- __OBJC_CLASS_RO_$_FBSDeviceEmulationDefaults
- __OBJC_METACLASS_RO_$_FBSDeviceEmulationConfiguration
- __OBJC_METACLASS_RO_$_FBSDeviceEmulationDefaults
- ___50+[FBSDeviceEmulationConfiguration _sharedDefaults]_block_invoke
- ___62+[FBSDeviceEmulationConfiguration _isEmulatedDeviceViaGestalt]_block_invoke
- ___63+[FBSDeviceEmulationConfiguration _isEmulatedDeviceViaDefaults]_block_invoke
- ___block_literal_global.3
- ___kCFBooleanFalse
- __isEmulatedDeviceViaDefaults.isEmulatedViaDefaults
- __isEmulatedDeviceViaDefaults.onceToken
- __isEmulatedDeviceViaGestalt.onceToken
- __isEmulatedDeviceViaGestalt.sIsEmulatedDevice
- __sharedDefaults.onceToken
- __sharedDefaults.sEmulationDefaults
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$_bindProperty:withDefaultKey:toDefaultValue:options:
- _objc_msgSend$_initWithDomain:
- _objc_msgSend$_isEmulatedDeviceViaDefaults
- _objc_msgSend$_isEmulatedDeviceViaGestalt
- _objc_msgSend$_sharedDefaults
- _objc_msgSend$bezelImageName
- _objc_msgSend$bundleProxyForIdentifier:
- _objc_msgSend$bundleWithURL:
- _objc_msgSend$customScaleFactorX
- _objc_msgSend$customScaleFactorY
- _objc_msgSend$customTranslationOffsetX
- _objc_msgSend$customTranslationOffsetY
- _objc_msgSend$emulatedArtworkSubtype
- _objc_msgSend$emulatedDeviceBounds
- _objc_msgSend$emulatedDeviceClass
- _objc_msgSend$emulatedDisplayCornerRadius
- _objc_msgSend$emulatedDisplayHeight
- _objc_msgSend$emulatedDisplayWidth
- _objc_msgSend$emulatedHomeButtonType
- _objc_msgSend$enableEmulation
- _objc_msgSend$forceIsD22ChecksToPass
- _objc_msgSend$imageContainingBundleIdentifier
- _objc_msgSend$isEmulatedDevice
- _objc_msgSend$isUserOverridden
- _objc_msgSend$maskImageName
- _objc_msgSend$rootLayerBackgroundColorString
- _objc_msgSend$scalingStyle
- _objc_msgSend$warningState
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x9
- _os_variant_has_internal_diagnostics
CStrings:
+ "Shutdown"
+ "shouldPreventLaunch"
- "FBSBezelImageName"
- "FBSCustomXScaleFactor"
- "FBSCustomXTranslationOffset"
- "FBSCustomYScaleFactor"
- "FBSCustomYTranslationOffset"
- "FBSDeviceEmulationBackgroundColorString"
- "FBSDeviceEmulationConfiguration"
- "FBSDeviceEmulationDefaults"
- "FBSDeviceEmulationScalingStyle"
- "FBSEmulatedArtworkSubtype"
- "FBSEmulatedDeviceClass"
- "FBSEmulatedDisplayCornerRadius"
- "FBSEmulatedDisplayHeight"
- "FBSEmulatedDisplayWidth"
- "FBSEmulatedHomeButtonType"
- "FBSEnableDeviceEmulation"
- "FBSForceIsD22ChecksToPass"
- "FBSImageContainingBundleIdentifier"
- "FBSMaskImageName"
- "T@\"NSBundle\",R,N"
- "TB,R,N,G_forceIsD22ChecksToPass"
- "TB,R,N,GisEmulatedDevice"
- "Ti,D,N"
- "_bindAndRegisterDefaults"
- "_bindProperty:withDefaultKey:toDefaultValue:options:"
- "_forceIsD22ChecksToPass"
- "_initWithDomain:"
- "_isEmulatedDeviceViaDefaults"
- "_isEmulatedDeviceViaGestalt"
- "_sharedDefaults"
- "bezelImageName"
- "bundleProxyForIdentifier:"
- "bundleWithURL:"
- "com.apple.frontboardservices.device_emulation"
- "customScaleFactorX"
- "customScaleFactorY"
- "customTranslationOffsetX"
- "customTranslationOffsetY"
- "deviceEmulationVersion"
- "emulatedArtworkSubtype"
- "emulatedDevice"
- "emulatedDeviceBezelImageName"
- "emulatedDeviceBounds"
- "emulatedDeviceClass"
- "emulatedDeviceImageContainingBundle"
- "emulatedDeviceMaskImageName"
- "emulatedDisplayCornerRadius"
- "emulatedDisplayHeight"
- "emulatedDisplayWidth"
- "emulatedHomeButtonType"
- "enableEmulation"
- "forceIsD22ChecksToPass"
- "hasEmulatedDeviceBounds"
- "imageContainingBundleIdentifier"
- "isEmulatedDevice"
- "isUserOverridden"
- "maskImageName"
- "rootLayerBackgroundColorString"
- "scalingStyle"
- "warningState"
- "z5G/N9jcMdgPm8UegLwbKg"

```
