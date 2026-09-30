## FrontBoardServices

> `/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`

```diff

-1000.3.4.0.0
-  __TEXT.__text: 0xa2a00
-  __TEXT.__auth_stubs: 0x10f0
+1000.3.4.100.0
+  __TEXT.__text: 0xa3878
+  __TEXT.__auth_stubs: 0x1110
   __TEXT.__delay_helper: 0xdc
-  __TEXT.__objc_methlist: 0x84f0
+  __TEXT.__objc_methlist: 0x8618
   __TEXT.__const: 0x270
-  __TEXT.__cstring: 0xc874
+  __TEXT.__cstring: 0xcbf4
   __TEXT.__oslogstring: 0x3d7d
   __TEXT.__gcc_except_tab: 0x2410
-  __TEXT.__unwind_info: 0x2ca0
-  __TEXT.__objc_classname: 0x1424
-  __TEXT.__objc_methname: 0x10255
+  __TEXT.__unwind_info: 0x2cd8
+  __TEXT.__objc_classname: 0x145f
+  __TEXT.__objc_methname: 0x105ee
   __TEXT.__objc_methtype: 0x35a6
-  __TEXT.__objc_stubs: 0xaee0
-  __DATA_CONST.__got: 0x718
-  __DATA_CONST.__const: 0x2fc8
-  __DATA_CONST.__objc_classlist: 0x490
+  __TEXT.__objc_stubs: 0xb240
+  __DATA_CONST.__got: 0x720
+  __DATA_CONST.__const: 0x2fa0
+  __DATA_CONST.__objc_classlist: 0x4a0
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x220
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3cd8
+  __DATA_CONST.__objc_selrefs: 0x3df0
   __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__objc_superrefs: 0x318
   __DATA_CONST.__objc_arraydata: 0x8
-  __AUTH_CONST.__auth_got: 0x888
-  __AUTH_CONST.__const: 0x820
-  __AUTH_CONST.__cfstring: 0xa160
-  __AUTH_CONST.__objc_const: 0xffd0
+  __AUTH_CONST.__auth_got: 0x898
+  __AUTH_CONST.__const: 0x860
+  __AUTH_CONST.__cfstring: 0xa3e0
+  __AUTH_CONST.__objc_const: 0x10330
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
-  UUID: 06560AEC-3C00-320A-A1D4-939A526DC793
-  Functions: 4275
-  Symbols:   13590
-  CStrings:  6840
+  UUID: A22C8550-B61B-345D-8096-A663707AAC84
+  Functions: 4305
+  Symbols:   13701
+  CStrings:  6940
 
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
+ -[_FBSScenesClientHostEvent _addCompletions:]
+ -[_FBSScenesClientHostEvent addCompletion:]
+ -[_FBSScenesClientHostEvent addCompletion:].cold.1
+ -[_FBSScenesClientHostEvent addCompletion:].cold.2
+ GCC_except_table176
+ GCC_except_table182
+ _MGGetBoolAnswer
+ _OBJC_CLASS_$_BSAbstractDefaultDomain
+ _OBJC_CLASS_$_FBSDeviceEmulationConfiguration
+ _OBJC_CLASS_$_FBSDeviceEmulationDefaults
+ _OBJC_IVAR_$__FBSScenesClientHostEvent._completions
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
+ ___60-[FBSWorkspaceScenesClient createSceneFutureWithDefinition:]_block_invoke.225
+ ___62+[FBSDeviceEmulationConfiguration _isEmulatedDeviceViaGestalt]_block_invoke
+ ___63+[FBSDeviceEmulationConfiguration _isEmulatedDeviceViaDefaults]_block_invoke
+ ___63-[FBSWorkspaceScenesClient requestSceneWithOptions:completion:]_block_invoke.248
+ ___63-[FBSWorkspaceScenesClient requestSceneWithOptions:completion:]_block_invoke_2.250
+ ___63-[FBSWorkspaceScenesClient requestSceneWithOptions:completion:]_block_invoke_2.250.cold.1
+ ___63-[FBSWorkspaceScenesClient requestSceneWithOptions:completion:]_block_invoke_2.250.cold.2
+ ___63-[FBSWorkspaceScenesClient requestSceneWithOptions:completion:]_block_invoke_2.250.cold.3
+ ___88-[FBSWorkspaceScenesClient _initWithIdentifier:connection:queue:calloutQueue:workspace:]_block_invoke.184
+ ___88-[FBSWorkspaceScenesClient _initWithIdentifier:connection:queue:calloutQueue:workspace:]_block_invoke.198
+ ___88-[FBSWorkspaceScenesClient _initWithIdentifier:connection:queue:calloutQueue:workspace:]_block_invoke.202
+ ___88-[FBSWorkspaceScenesClient _initWithIdentifier:connection:queue:calloutQueue:workspace:]_block_invoke_2.189
+ ___93-[FBSWorkspaceScenesClient _callOutQueue_sendDidCreateForScene:transitionContext:completion:]_block_invoke.345
+ ___93-[FBSWorkspaceScenesClient _callOutQueue_sendDidCreateForScene:transitionContext:completion:]_block_invoke.345.cold.1
+ ___93-[FBSWorkspaceScenesClient _callOutQueue_sendDidCreateForScene:transitionContext:completion:]_block_invoke.349
+ ___95-[FBSWorkspaceScenesClient reconnectSceneWithIdentity:parameters:transitionContext:completion:]_block_invoke.303
+ ___block_literal_global.3
+ ___kCFBooleanFalse
+ __isEmulatedDeviceViaDefaults.isEmulatedViaDefaults
+ __isEmulatedDeviceViaDefaults.onceToken
+ __isEmulatedDeviceViaGestalt.onceToken
+ __isEmulatedDeviceViaGestalt.sIsEmulatedDevice
+ __sharedDefaults.onceToken
+ __sharedDefaults.sEmulationDefaults
+ _objc_msgSend$_addCompletions:
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
- GCC_except_table181
- GCC_except_table64
- _OBJC_IVAR_$__FBSScenesClientHostEvent._completion
- ___51-[_FBSScenesClientHostEvent coalesceEvent:skipped:]_block_invoke
- ___60-[FBSWorkspaceScenesClient createSceneFutureWithDefinition:]_block_invoke.217
- ___63-[FBSWorkspaceScenesClient requestSceneWithOptions:completion:]_block_invoke.232
- ___63-[FBSWorkspaceScenesClient requestSceneWithOptions:completion:]_block_invoke_2.242
- ___63-[FBSWorkspaceScenesClient requestSceneWithOptions:completion:]_block_invoke_2.242.cold.1
- ___63-[FBSWorkspaceScenesClient requestSceneWithOptions:completion:]_block_invoke_2.242.cold.2
- ___63-[FBSWorkspaceScenesClient requestSceneWithOptions:completion:]_block_invoke_2.242.cold.3
- ___88-[FBSWorkspaceScenesClient _initWithIdentifier:connection:queue:calloutQueue:workspace:]_block_invoke.177
- ___88-[FBSWorkspaceScenesClient _initWithIdentifier:connection:queue:calloutQueue:workspace:]_block_invoke.190
- ___88-[FBSWorkspaceScenesClient _initWithIdentifier:connection:queue:calloutQueue:workspace:]_block_invoke.194
- ___88-[FBSWorkspaceScenesClient _initWithIdentifier:connection:queue:calloutQueue:workspace:]_block_invoke_2.182
- ___93-[FBSWorkspaceScenesClient _callOutQueue_sendDidCreateForScene:transitionContext:completion:]_block_invoke.337
- ___93-[FBSWorkspaceScenesClient _callOutQueue_sendDidCreateForScene:transitionContext:completion:]_block_invoke.337.cold.1
- ___93-[FBSWorkspaceScenesClient _callOutQueue_sendDidCreateForScene:transitionContext:completion:]_block_invoke.341
- ___95-[FBSWorkspaceScenesClient reconnectSceneWithIdentity:parameters:transitionContext:completion:]_block_invoke.295
- ___block_descriptor_48_e8_32bs40bs_e5_v8?0ls32l8s40l8
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
+ "_addCompletions:"
+ "_bindAndRegisterDefaults"
+ "_bindProperty:withDefaultKey:toDefaultValue:options:"
+ "_completions"
+ "_forceIsD22ChecksToPass"
+ "_initWithDomain:"
+ "_isEmulatedDeviceViaDefaults"
+ "_isEmulatedDeviceViaGestalt"
+ "_sharedDefaults"
+ "addCompletion:"
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
