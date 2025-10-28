## FrontBoardServices

> `/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`

```diff

 1000.1.4.0.0
-  __TEXT.__text: 0xa2a00
-  __TEXT.__auth_stubs: 0x10f0
+  __TEXT.__text: 0xa368c
+  __TEXT.__auth_stubs: 0x1110
   __TEXT.__delay_helper: 0xc8
-  __TEXT.__objc_methlist: 0x84e0
+  __TEXT.__objc_methlist: 0x8600
   __TEXT.__const: 0x270
-  __TEXT.__cstring: 0xc874
+  __TEXT.__cstring: 0xcbe9
   __TEXT.__oslogstring: 0x3d7d
   __TEXT.__gcc_except_tab: 0x2410
-  __TEXT.__unwind_info: 0x2c98
-  __TEXT.__objc_classname: 0x1424
-  __TEXT.__objc_methname: 0x10236
+  __TEXT.__unwind_info: 0x2cd0
+  __TEXT.__objc_classname: 0x145f
+  __TEXT.__objc_methname: 0x105a2
   __TEXT.__objc_methtype: 0x35a6
-  __TEXT.__objc_stubs: 0xaee0
-  __DATA_CONST.__got: 0x718
+  __TEXT.__objc_stubs: 0xb220
+  __DATA_CONST.__got: 0x720
   __DATA_CONST.__const: 0x2fc8
-  __DATA_CONST.__objc_classlist: 0x490
+  __DATA_CONST.__objc_classlist: 0x4a0
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x220
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3cd0
+  __DATA_CONST.__objc_selrefs: 0x3dd8
   __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__objc_superrefs: 0x318
   __DATA_CONST.__objc_arraydata: 0x8
-  __AUTH_CONST.__auth_got: 0x888
-  __AUTH_CONST.__const: 0x820
-  __AUTH_CONST.__cfstring: 0xa160
-  __AUTH_CONST.__objc_const: 0xffc8
+  __AUTH_CONST.__auth_got: 0x898
+  __AUTH_CONST.__const: 0x860
+  __AUTH_CONST.__cfstring: 0xa3c0
+  __AUTH_CONST.__objc_const: 0x10328
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__objc_intobj: 0x48
+  __AUTH_CONST.__objc_intobj: 0x90
   __AUTH.__objc_data: 0xdc0
   __DATA.__objc_ivar: 0xa60
   __DATA.__data: 0x19b4
   __DATA.__bss: 0x398
-  __DATA_DIRTY.__objc_data: 0x1fe0
-  __DATA_DIRTY.__bss: 0x1c8
+  __DATA_DIRTY.__objc_data: 0x2080
+  __DATA_DIRTY.__bss: 0x1f8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2AFB7210-FE9C-3029-AB50-F996524E8C73
-  Functions: 4274
-  Symbols:   13588
-  CStrings:  6839
+  UUID: 97BBB5BC-AF24-3231-BF5E-3E28DB22D4A6
+  Functions: 4301
+  Symbols:   13693
+  CStrings:  6934
 
Symbols:
+ +[FBSDeviceEmulationConfiguration _forceIsD22ChecksToPass]
+ +[FBSDeviceEmulationConfiguration _isEmulatedDeviceViaDefaults]
+ +[FBSDeviceEmulationConfiguration _isEmulatedDeviceViaGestalt]
+ +[FBSDeviceEmulationConfiguration _isEmulatedDeviceViaGestalt].cold.1
+ +[FBSDeviceEmulationConfiguration _sharedDefaults]
+ +[FBSDeviceEmulationConfiguration _sharedDefaults].cold.1
+ +[FBSDeviceEmulationConfiguration customScaleFactorX]
+ +[FBSDeviceEmulationConfiguration customScaleFactorY]
+ +[FBSDeviceEmulationConfiguration customTranslationOffsetX]
+ +[FBSDeviceEmulationConfiguration customTranslationOffsetY]
+ +[FBSDeviceEmulationConfiguration deviceEmulationVersion]
+ +[FBSDeviceEmulationConfiguration emulatedArtworkSubtype]
+ +[FBSDeviceEmulationConfiguration emulatedDeviceBezelImageName]
+ +[FBSDeviceEmulationConfiguration emulatedDeviceBounds]
+ +[FBSDeviceEmulationConfiguration emulatedDeviceClass]
+ +[FBSDeviceEmulationConfiguration emulatedDeviceImageContainingBundle]
+ +[FBSDeviceEmulationConfiguration emulatedDeviceMaskImageName]
+ +[FBSDeviceEmulationConfiguration emulatedDisplayCornerRadius]
+ +[FBSDeviceEmulationConfiguration emulatedHomeButtonType]
+ +[FBSDeviceEmulationConfiguration hasEmulatedDeviceBounds]
+ +[FBSDeviceEmulationConfiguration isEmulatedDevice]
+ +[FBSDeviceEmulationConfiguration rootLayerBackgroundColorString]
+ +[FBSDeviceEmulationConfiguration scalingStyle]
+ -[FBSDeviceEmulationDefaults _bindAndRegisterDefaults]
+ _MGGetBoolAnswer
+ _OBJC_CLASS_$_BSAbstractDefaultDomain
+ _OBJC_CLASS_$_FBSDeviceEmulationConfiguration
+ _OBJC_CLASS_$_FBSDeviceEmulationDefaults
+ _OBJC_METACLASS_$_BSAbstractDefaultDomain
+ _OBJC_METACLASS_$_FBSDeviceEmulationConfiguration
+ _OBJC_METACLASS_$_FBSDeviceEmulationDefaults
+ __OBJC_$_CLASS_METHODS_FBSDeviceEmulationConfiguration
+ __OBJC_$_CLASS_PROP_LIST_FBSDeviceEmulationConfiguration
+ __OBJC_$_INSTANCE_METHODS_FBSDeviceEmulationDefaults
+ __OBJC_$_PROP_LIST_FBSDeviceEmulationDefaults
+ __OBJC_CLASS_RO_$_FBSDeviceEmulationConfiguration
+ __OBJC_CLASS_RO_$_FBSDeviceEmulationDefaults
+ __OBJC_METACLASS_RO_$_FBSDeviceEmulationConfiguration
+ __OBJC_METACLASS_RO_$_FBSDeviceEmulationDefaults
+ ___50+[FBSDeviceEmulationConfiguration _sharedDefaults]_block_invoke
+ ___62+[FBSDeviceEmulationConfiguration _isEmulatedDeviceViaGestalt]_block_invoke
+ ___63+[FBSDeviceEmulationConfiguration _isEmulatedDeviceViaDefaults]_block_invoke
+ ___block_literal_global.3
+ ___kCFBooleanFalse
+ __isEmulatedDeviceViaDefaults.isEmulatedViaDefaults
+ __isEmulatedDeviceViaDefaults.onceToken
+ __isEmulatedDeviceViaGestalt.onceToken
+ __isEmulatedDeviceViaGestalt.sIsEmulatedDevice
+ __sharedDefaults.onceToken
+ __sharedDefaults.sEmulationDefaults
+ _objc_msgSend$_bindProperty:withDefaultKey:toDefaultValue:options:
+ _objc_msgSend$_initWithDomain:
+ _objc_msgSend$_isEmulatedDeviceViaDefaults
+ _objc_msgSend$_isEmulatedDeviceViaGestalt
+ _objc_msgSend$_sharedDefaults
+ _objc_msgSend$bezelImageName
+ _objc_msgSend$bundleProxyForIdentifier:
+ _objc_msgSend$bundleWithURL:
+ _objc_msgSend$customScaleFactorX
+ _objc_msgSend$customScaleFactorY
+ _objc_msgSend$customTranslationOffsetX
+ _objc_msgSend$customTranslationOffsetY
+ _objc_msgSend$emulatedArtworkSubtype
+ _objc_msgSend$emulatedDeviceBounds
+ _objc_msgSend$emulatedDeviceClass
+ _objc_msgSend$emulatedDisplayCornerRadius
+ _objc_msgSend$emulatedDisplayHeight
+ _objc_msgSend$emulatedDisplayWidth
+ _objc_msgSend$emulatedHomeButtonType
+ _objc_msgSend$enableEmulation
+ _objc_msgSend$forceIsD22ChecksToPass
+ _objc_msgSend$imageContainingBundleIdentifier
+ _objc_msgSend$isEmulatedDevice
+ _objc_msgSend$maskImageName
+ _objc_msgSend$rootLayerBackgroundColorString
+ _objc_msgSend$scalingStyle
+ _os_variant_has_internal_diagnostics
CStrings:
+ "FBSBezelImageName"
+ "FBSCustomXScaleFactor"
+ "FBSCustomXTranslationOffset"
+ "FBSCustomYScaleFactor"
+ "FBSCustomYTranslationOffset"
+ "FBSDeviceEmulationBackgroundColorString"
+ "FBSDeviceEmulationConfiguration"
+ "FBSDeviceEmulationDefaults"
+ "FBSDeviceEmulationScalingStyle"
+ "FBSEmulatedArtworkSubtype"
+ "FBSEmulatedDeviceClass"
+ "FBSEmulatedDisplayCornerRadius"
+ "FBSEmulatedDisplayHeight"
+ "FBSEmulatedDisplayWidth"
+ "FBSEmulatedHomeButtonType"
+ "FBSEnableDeviceEmulation"
+ "FBSForceIsD22ChecksToPass"
+ "FBSImageContainingBundleIdentifier"
+ "FBSMaskImageName"
+ "T@\"NSBundle\",R,N"
+ "TB,R,N,G_forceIsD22ChecksToPass"
+ "TB,R,N,GisEmulatedDevice"
+ "Ti,D,N"
+ "_bindAndRegisterDefaults"
+ "_bindProperty:withDefaultKey:toDefaultValue:options:"
+ "_forceIsD22ChecksToPass"
+ "_initWithDomain:"
+ "_isEmulatedDeviceViaDefaults"
+ "_isEmulatedDeviceViaGestalt"
+ "_sharedDefaults"
+ "bezelImageName"
+ "bundleProxyForIdentifier:"
+ "bundleWithURL:"
+ "com.apple.frontboardservices.device_emulation"
+ "customScaleFactorX"
+ "customScaleFactorY"
+ "customTranslationOffsetX"
+ "customTranslationOffsetY"
+ "deviceEmulationVersion"
+ "emulatedArtworkSubtype"
+ "emulatedDevice"
+ "emulatedDeviceBezelImageName"
+ "emulatedDeviceBounds"
+ "emulatedDeviceClass"
+ "emulatedDeviceImageContainingBundle"
+ "emulatedDeviceMaskImageName"
+ "emulatedDisplayCornerRadius"
+ "emulatedDisplayHeight"
+ "emulatedDisplayWidth"
+ "emulatedHomeButtonType"
+ "enableEmulation"
+ "forceIsD22ChecksToPass"
+ "hasEmulatedDeviceBounds"
+ "imageContainingBundleIdentifier"
+ "isEmulatedDevice"
+ "maskImageName"
+ "rootLayerBackgroundColorString"
+ "scalingStyle"
+ "z5G/N9jcMdgPm8UegLwbKg"

```
