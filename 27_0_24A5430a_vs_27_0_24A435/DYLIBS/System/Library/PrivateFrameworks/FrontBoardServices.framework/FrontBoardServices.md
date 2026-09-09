## FrontBoardServices

> `/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`

```diff

 1153.0.1.0.0
-  __TEXT.__text: 0x98a4c
+  __TEXT.__text: 0x996d8
   __TEXT.__lazy_helpers: 0x54
-  __TEXT.__objc_methlist: 0x8688
+  __TEXT.__objc_methlist: 0x87a8
   __TEXT.__const: 0x270
-  __TEXT.__cstring: 0xc0b0
+  __TEXT.__cstring: 0xc425
   __TEXT.__oslogstring: 0x3b78
   __TEXT.__gcc_except_tab: 0x1e30
-  __TEXT.__unwind_info: 0x2ad8
+  __TEXT.__unwind_info: 0x2b18
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x3128
-  __DATA_CONST.__objc_classlist: 0x490
+  __DATA_CONST.__objc_classlist: 0x4a0
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x228
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3d68
+  __DATA_CONST.__objc_selrefs: 0x3e70
   __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__objc_superrefs: 0x328
   __DATA_CONST.__objc_arraydata: 0x8
-  __DATA_CONST.__got: 0x738
-  __AUTH_CONST.__const: 0x840
-  __AUTH_CONST.__cfstring: 0xa2e0
-  __AUTH_CONST.__objc_const: 0x100f8
+  __DATA_CONST.__got: 0x740
+  __AUTH_CONST.__const: 0x880
+  __AUTH_CONST.__cfstring: 0xa540
+  __AUTH_CONST.__objc_const: 0x10458
   __AUTH_CONST.__lazy_load_got: 0x8
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__objc_intobj: 0x48
-  __AUTH_CONST.__auth_got: 0x878
+  __AUTH_CONST.__objc_intobj: 0x90
+  __AUTH_CONST.__auth_got: 0x888
   __AUTH.__objc_data: 0xdc0
   __DATA.__objc_ivar: 0xa58
   __DATA.__data: 0x1a14
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
-  Functions: 4380
-  Symbols:   7902
-  CStrings:  1938
+  Functions: 4407
+  Symbols:   7976
+  CStrings:  1974
 
Symbols:
+ +[FBSDeviceEmulationConfiguration _forceIsD22ChecksToPass]
+ +[FBSDeviceEmulationConfiguration _isEmulatedDeviceViaDefaults]
+ +[FBSDeviceEmulationConfiguration _isEmulatedDeviceViaGestalt]
+ +[FBSDeviceEmulationConfiguration _sharedDefaults]
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
+ "bezelImageName"
+ "com.apple.frontboardservices.device_emulation"
+ "customScaleFactorX"
+ "customScaleFactorY"
+ "customTranslationOffsetX"
+ "customTranslationOffsetY"
+ "emulatedArtworkSubtype"
+ "emulatedDeviceClass"
+ "emulatedDisplayCornerRadius"
+ "emulatedDisplayHeight"
+ "emulatedDisplayWidth"
+ "emulatedHomeButtonType"
+ "enableEmulation"
+ "forceIsD22ChecksToPass"
+ "imageContainingBundleIdentifier"
+ "maskImageName"
+ "rootLayerBackgroundColorString"
+ "scalingStyle"
+ "z5G/N9jcMdgPm8UegLwbKg"
```
