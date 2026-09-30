## AmbientDisplay

> `/System/Library/PrivateFrameworks/AmbientDisplay.framework/Versions/A/AmbientDisplay`

```diff

-149.0.0.0.0
-  __TEXT.__text: 0x1c4f8
-  __TEXT.__auth_stubs: 0xba0
-  __TEXT.__objc_methlist: 0x46c
+150.0.0.0.0
+  __TEXT.__text: 0x1d31c
+  __TEXT.__auth_stubs: 0xc30
+  __TEXT.__objc_methlist: 0x5a4
   __TEXT.__const: 0x908
-  __TEXT.__cstring: 0xcf07
+  __TEXT.__cstring: 0xdbf9
   __TEXT.__gcc_except_tab: 0x18c
   __TEXT.__oslogstring: 0x14
-  __TEXT.__unwind_info: 0x7b8
-  __TEXT.__objc_classname: 0x21
-  __TEXT.__objc_methname: 0xeaf
-  __TEXT.__objc_methtype: 0x29d
-  __TEXT.__objc_stubs: 0xc40
-  __DATA_CONST.__got: 0x168
+  __TEXT.__unwind_info: 0x7e8
+  __TEXT.__objc_classname: 0x34
+  __TEXT.__objc_methname: 0x13b1
+  __TEXT.__objc_methtype: 0x2f7
+  __TEXT.__objc_stubs: 0xec0
+  __DATA_CONST.__got: 0x178
   __DATA_CONST.__const: 0x170
-  __DATA_CONST.__objc_classlist: 0x10
+  __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x370
-  __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__objc_arraydata: 0x50
-  __AUTH_CONST.__auth_got: 0x5e8
-  __AUTH_CONST.__const: 0x2a0
-  __AUTH_CONST.__cfstring: 0x5c0
-  __AUTH_CONST.__objc_const: 0x8b0
+  __DATA_CONST.__objc_selrefs: 0x478
+  __DATA_CONST.__objc_superrefs: 0x10
+  __DATA_CONST.__objc_arraydata: 0x98
+  __AUTH_CONST.__auth_got: 0x630
+  __AUTH_CONST.__const: 0x270
+  __AUTH_CONST.__cfstring: 0x6c0
+  __AUTH_CONST.__objc_const: 0xba0
+  __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0xf0
+  __AUTH.__objc_data: 0xf0
+  __DATA.__objc_ivar: 0x12c
   __DATA.__data: 0x120
   __DATA.__common: 0x10
   __DATA.__bss: 0x171

   - /System/Library/Frameworks/CoreVideo.framework/Versions/A/CoreVideo
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
+  - /System/Library/PrivateFrameworks/CoreBrightness.framework/Versions/A/CoreBrightness
   - /System/Library/PrivateFrameworks/DisplayServices.framework/Versions/A/DisplayServices
   - /System/Library/PrivateFrameworks/IOPresentment.framework/Versions/A/IOPresentment
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6F85FF3C-715F-3010-8174-3020E6EF2F7D
-  Functions: 560
-  Symbols:   1052
-  CStrings:  1278
+  UUID: D50ECE5A-22BC-31C9-AA4A-4C42203A1687
+  Functions: 589
+  Symbols:   1132
+  CStrings:  1407
 
Symbols:
+ -[BrightnessModule .cxx_destruct]
+ -[BrightnessModule _getAutoBrightnessAvailable]
+ -[BrightnessModule _getAutoBrightnessForcedDisabledState]
+ -[BrightnessModule _getBrightnessIncrement]
+ -[BrightnessModule _getBrightnessLockedState]
+ -[BrightnessModule _getBrightnessSetting]
+ -[BrightnessModule _pollToRefreshAutoBrightnessEnabled]
+ -[BrightnessModule activate]
+ -[BrightnessModule autoBrightnessEnabledState]
+ -[BrightnessModule autoBrightnessIsAvailable]
+ -[BrightnessModule autoBrightnessIsForcedDisabled]
+ -[BrightnessModule autoBrightnessState]
+ -[BrightnessModule brightnessIncrement]
+ -[BrightnessModule brightnessIsLocked]
+ -[BrightnessModule brightnessModuleRegisterForNotifications:]
+ -[BrightnessModule brightnessModuleUnregisterForNotifications:]
+ -[BrightnessModule brightnessSetting]
+ -[BrightnessModule deactivate]
+ -[BrightnessModule dealloc]
+ -[BrightnessModule displayIsBuiltIn]
+ -[BrightnessModule initBrightnessModuleWithDisplayID:]
+ -[BrightnessModule setAutoBrightnessEnabledState:]
+ -[BrightnessModule setBrightnessSetting:]
+ -[DeviceGammaContext overridesSearched]
+ -[DeviceGammaContext setCompensationState:]
+ -[DeviceGammaContext setupBrightnessModule]
+ OBJC_IVAR_$_BrightnessModule._autoBrightnessEnabledState
+ OBJC_IVAR_$_BrightnessModule._autoBrightnessIsAvailable
+ OBJC_IVAR_$_BrightnessModule._autoBrightnessIsForcedDisabled
+ OBJC_IVAR_$_BrightnessModule._brightnessIncrement
+ OBJC_IVAR_$_BrightnessModule._brightnessIsLocked
+ OBJC_IVAR_$_BrightnessModule._builtIn
+ OBJC_IVAR_$_BrightnessModule._currentBrightness
+ OBJC_IVAR_$_BrightnessModule._displayID
+ OBJC_IVAR_$_BrightnessModule._dsClient
+ OBJC_IVAR_$_BrightnessModule._hasALSCompensation
+ OBJC_IVAR_$_BrightnessModule._hasALSReset
+ OBJC_IVAR_$_BrightnessModule._observer
+ OBJC_IVAR_$_BrightnessModule._smallestBrightnessIncrement
+ OBJC_IVAR_$_DeviceGammaContext.brightnessModule
+ OBJC_IVAR_$_DeviceGammaContext.overridesSearched
+ _AMBDsetCompensationStateAsync
+ _AMBDwake
+ _DisplayServicesCanResetAmbientLight
+ _DisplayServicesGetBrightness
+ _DisplayServicesGetBrightnessIncrement
+ _DisplayServicesRegisterForNotification
+ _DisplayServicesSetBrightnessWithType
+ _DisplayServicesUnregisterForNotification
+ _OBJC_CLASS_$_BrightnessModule
+ _OBJC_CLASS_$_DisplayServicesClient
+ _OBJC_METACLASS_$_BrightnessModule
+ __OBJC_$_INSTANCE_METHODS_BrightnessModule
+ __OBJC_$_INSTANCE_VARIABLES_BrightnessModule
+ __OBJC_$_PROP_LIST_BrightnessModule
+ __OBJC_CLASS_RO_$_BrightnessModule
+ __OBJC_METACLASS_RO_$_BrightnessModule
+ ___28-[BrightnessModule activate]_block_invoke
+ ___block_descriptor_40_e8_32s_e24_v32?0"NSString"8Q1624l
+ __block_descriptor_tmp.150
+ __block_descriptor_tmp.158
+ _ambientBrightnessChangedCallBack
+ _ambientResetChangedCallBack
+ _compensationEnableable
+ _displayUSBHotplugCallBack
+ _objc_alloc_init
+ _objc_msgSend$_getAutoBrightnessAvailable
+ _objc_msgSend$_getAutoBrightnessForcedDisabledState
+ _objc_msgSend$_getBrightnessIncrement
+ _objc_msgSend$_getBrightnessLockedState
+ _objc_msgSend$_getBrightnessSetting
+ _objc_msgSend$_pollToRefreshAutoBrightnessEnabled
+ _objc_msgSend$activate
+ _objc_msgSend$boolValue
+ _objc_msgSend$brightnessModuleRegisterForNotifications:
+ _objc_msgSend$copyPropertyForKey:andDisplay:
+ _objc_msgSend$description
+ _objc_msgSend$floatValue
+ _objc_msgSend$initBrightnessModuleWithDisplayID:
+ _objc_msgSend$isEqualToString:
+ _objc_msgSend$overridesSearched
+ _objc_msgSend$registerDisplayNotificationCallbackBlock:
+ _objc_msgSend$registerNotificationForKeys:andDisplay:
+ _objc_msgSend$setCompensationState:
+ _objc_msgSend$setupBrightnessModule
+ _objc_msgSend$unregisterDisplayNotificationBlock
+ _objc_msgSend$unregisterNotificationForKeys:andDisplay:
+ _objc_opt_class
+ _objc_opt_isKindOfClass
+ _objc_storeStrong
- -[DeviceGammaContext enableCompensation:]
- _DisplayServicesAmbientLightCompensationEnabled
- __AMBDapplyIntentionFromPreferencesForDisplayID_block_invoke.98
- ___AMBDapplyIntentionFromPreferencesForDisplayID_block_invoke
- __block_descriptor_tmp.101
- __block_descriptor_tmp.121
- __block_descriptor_tmp.162
- __block_descriptor_tmp.170
- _canEnableCompensation
- _objc_msgSend$enableCompensation:
CStrings:
+ "-[BrightnessModule _getAutoBrightnessAvailable]"
+ "-[BrightnessModule _getAutoBrightnessForcedDisabledState]"
+ "-[BrightnessModule _getBrightnessIncrement]"
+ "-[BrightnessModule _getBrightnessLockedState]"
+ "-[BrightnessModule _getBrightnessSetting]"
+ "-[BrightnessModule _pollToRefreshAutoBrightnessEnabled]"
+ "-[BrightnessModule activate]"
+ "-[BrightnessModule activate]_block_invoke"
+ "-[BrightnessModule brightnessModuleRegisterForNotifications:]"
+ "-[BrightnessModule brightnessModuleUnregisterForNotifications:]"
+ "-[BrightnessModule initBrightnessModuleWithDisplayID:]"
+ ".cxx_destruct"
+ "/AppleInternal/Library/BuildRoots/4~CE8VugD7bXxtRzRh3JFuh7K1XpHdwZQM3JrOz7Q/Library/Caches/com.apple.xbs/Sources/AmbientDisplay/Sources/AmbientDisplayServices.c"
+ "/AppleInternal/Library/BuildRoots/4~CE8VugD7bXxtRzRh3JFuh7K1XpHdwZQM3JrOz7Q/Library/Caches/com.apple.xbs/Sources/AmbientDisplay/Sources/DeviceGammaContext.m"
+ "@\"BrightnessModule\""
+ "@\"DeviceGammaContext\""
+ "@\"DisplayServicesClient\""
+ "@20@0:8I16"
+ "AMBD %f: validDeviceContextList() returned 0, skipping this call on displayID 0x%0x"
+ "AMBD %s: ALSlocation builtIn, setting setFrontALservice to alsService 0x%0x, on displayID 0x%0x"
+ "AMBD %s: ALSlocation unknown expected for some devices, setting setFrontALservice to alsService 0x%0x, on displayID 0x%0x"
+ "AMBD %s: displayID 0, using internal displayID 0x%0x instead"
+ "AMBD %s: setFrontALservice to alsService 0x%0x, on displayID 0x%0x"
+ "AMBD %s: setRearALservice to alsService 0x%0x, on displayID 0x%0x"
+ "AMBD %s: unknown ALSlocation %d for ALSservice 0x%0x, on displayID 0x%0x: skipping setting the ALSservice on the device context"
+ "AMBD Agent %s: all the ambient display overrides found, setting hasOverrides TRUE on display 0x%0x\n"
+ "AMBD Services: %s loading intention values %s %f %f %f %f (displayID 0x%0x)"
+ "AMBD Services: sending kWake"
+ "AMBD: %s DisplayServicesGetBrightness failed (error = %d)"
+ "AMBD: %s DisplayServicesGetBrightnessIncrement failed (error = %d)"
+ "AMBD: %s NULL observer passed in"
+ "AMBD: %s failed to register for Ambient Light Brightness Notifications"
+ "AMBD: %s failed to register for Ambient Reset Change Notifications"
+ "AMBD: %s failed to register for Display USB Hot Plug Notifications"
+ "AMBD: %s failed to unregister for Ambient Light Brightness Notifications"
+ "AMBD: %s failed to unregister for Ambient Reset Change Notifications"
+ "AMBD: %s failed to unregister for Display USB Hot Plug Notifications"
+ "AMBD: %s findAndCopyDeviceContextByDeviceID(0x%0x) failed to find the display"
+ "AMBD: %s first-time processing initially polled CoreBrightness values on displayID %p which is AMBD compensation enableable"
+ "AMBD: %s first-time, disabling compensation via AMBDsetCompensationState for displayID %p (enableable, with autobrightness disabled)"
+ "AMBD: %s first-time, disabling compensation via AMBDsetCompensationState for displayID %p (enableable, with autobrightness not available)"
+ "AMBD: %s first-time, disabling compensation via AMBDsetCompensationState for displayID %p (not-enableable)"
+ "AMBD: %s first-time, enabling compensation via AMBDsetCompensationState for displayID %p (enableable, with autobrightness enabled)"
+ "AMBD: %s invalid displayID"
+ "AMBD: %s kCoreBrightnessAutoBrightnessAvailable property is (%@)"
+ "AMBD: %s kCoreBrightnessAutoBrightnessEnabled property is (%@)"
+ "AMBD: %s kCoreBrightnessDisplayPresetDisableAutoBrightness property is (%@)"
+ "AMBD: %s kCoreBrightnessDisplayPresetLockBrightnessUpdates property is (%@)"
+ "AMBD: %s null observer, skipping notification"
+ "AMBD: %s observer: %p, notification"
+ "AMBD: %s received a notification for propertyKey: %s, value: %s"
+ "AMBD: %s received kCoreBrightnessAutoBrightnessAvailable %s"
+ "AMBD: %s received kCoreBrightnessAutoBrightnessEnabled %s"
+ "AMBD: %s received kCoreBrightnessDisplayPresetDisableAutoBrightness (force disabled) %s"
+ "AMBD: %s received kCoreBrightnessDisplayPresetLockBrightnessUpdates %s"
+ "AMBD: %s received kDisplayServicesBrightness: %f"
+ "AMBD: %s received unknown propertyKey: %s"
+ "BrightnessModule"
+ "BrightnessModule callback block"
+ "CBAutoBrightnessAvailable"
+ "CBAutoBrightnessEnabled"
+ "CBDisplayPresetDisableAutoBrightness"
+ "CBDisplayPresetLockBrightnessUpdates"
+ "DisplayServicesAmbientBrightness"
+ "DisplayServicesAmbientReset"
+ "DisplayServicesBrightness"
+ "DisplayServicesUSBHotPlug"
+ "TB,R,V_autoBrightnessIsAvailable"
+ "TB,R,V_autoBrightnessIsForcedDisabled"
+ "TB,R,V_brightnessIsLocked"
+ "TB,R,V_builtIn"
+ "TB,V_autoBrightnessEnabledState"
+ "Tf"
+ "Tf,R,V_brightnessIncrement"
+ "_autoBrightnessEnabledState"
+ "_autoBrightnessIsAvailable"
+ "_autoBrightnessIsForcedDisabled"
+ "_brightnessIncrement"
+ "_brightnessIsLocked"
+ "_builtIn"
+ "_currentBrightness"
+ "_displayID"
+ "_dsClient"
+ "_getAutoBrightnessAvailable"
+ "_getAutoBrightnessForcedDisabledState"
+ "_getBrightnessIncrement"
+ "_getBrightnessLockedState"
+ "_getBrightnessSetting"
+ "_hasALSCompensation"
+ "_hasALSReset"
+ "_observer"
+ "_pollToRefreshAutoBrightnessEnabled"
+ "_smallestBrightnessIncrement"
+ "activate"
+ "ambientBrightnessChangedCallBack"
+ "ambientResetChangedCallBack"
+ "autoBrightnessEnabledState"
+ "autoBrightnessIsAvailable"
+ "autoBrightnessIsForcedDisabled"
+ "autoBrightnessState"
+ "boolValue"
+ "brightnessIncrement"
+ "brightnessIsLocked"
+ "brightnessModule"
+ "brightnessModuleRegisterForNotifications:"
+ "brightnessModuleUnregisterForNotifications:"
+ "brightnessSetting"
+ "compensationEnableable"
+ "copyPropertyForKey:andDisplay:"
+ "deactivate"
+ "description"
+ "disabled"
+ "displayIsBuiltIn"
+ "displayUSBHotplugCallBack"
+ "enabled"
+ "floatValue"
+ "initBrightnessModuleWithDisplayID:"
+ "isEqualToString:"
+ "locked"
+ "not locked"
+ "overridesSearched"
+ "registerDisplayNotificationCallbackBlock:"
+ "registerNotificationForKeys:andDisplay:"
+ "setAutoBrightnessEnabledState:"
+ "setBrightnessSetting:"
+ "setCompensationState:"
+ "setupBrightnessModule"
+ "unregisterDisplayNotificationBlock"
+ "unregisterNotificationForKeys:andDisplay:"
+ "v24@0:8^v16"
+ "v32@?0@\"NSString\"8Q16@24"
- "/AppleInternal/Library/BuildRoots/4~CDyzugC2qJRdaLbaZtkb8Rg55DrcCOtIESitl0w/Library/Caches/com.apple.xbs/Sources/AmbientDisplay/Sources/AmbientDisplayServices.c"
- "/AppleInternal/Library/BuildRoots/4~CDyzugC2qJRdaLbaZtkb8Rg55DrcCOtIESitl0w/Library/Caches/com.apple.xbs/Sources/AmbientDisplay/Sources/DeviceGammaContext.m"
- "AMBD %s: ALCGetDisplayAutoBrightnessEnabled() fails; enabling Ambient Compensation for display: 0x%0x"
- "AMBD %s: DisplayServicesAmbientLightCompensationEnabled() failed with (0x%x), forcing Ambient Compensation ON"
- "AMBD Services: %s Ambient Compensation tied to auto brightness: %s"
- "AMBD Services: %s DisplayServicesHasAmbientLightCompensation() reports no auto brightness for display id (display: 0x%x), forcing Ambient Compensation ON"
- "AMBD Services: %s loading intention values %s %f %f %f %f (displayID 0x%0x) Compensation %s"
- "AMBD: %s findAndCopyDeviceContextByDeviceID(0x%0x) failed\n"
- "canEnableCompensation"
- "enableCompensation:"

```
