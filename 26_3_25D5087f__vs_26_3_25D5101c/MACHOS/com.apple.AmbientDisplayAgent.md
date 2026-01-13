## com.apple.AmbientDisplayAgent

> `/System/Library/PrivateFrameworks/AmbientDisplay.framework/Versions/A/XPCServices/com.apple.AmbientDisplayAgent.xpc/Contents/MacOS/com.apple.AmbientDisplayAgent`

```diff

-149.0.0.0.0
-  __TEXT.__text: 0x43a4
-  __TEXT.__auth_stubs: 0xaa0
-  __TEXT.__objc_stubs: 0x1c0
-  __TEXT.__objc_methlist: 0x8c
-  __TEXT.__cstring: 0x3301
-  __TEXT.__objc_methname: 0x203
-  __TEXT.__objc_classname: 0xf
-  __TEXT.__objc_methtype: 0x97
-  __TEXT.__const: 0x1e0
+150.0.0.0.0
+  __TEXT.__text: 0x5164
+  __TEXT.__auth_stubs: 0xb80
+  __TEXT.__objc_stubs: 0x3c0
+  __TEXT.__objc_methlist: 0x1ac
+  __TEXT.__cstring: 0x3f43
+  __TEXT.__objc_methname: 0x6d5
+  __TEXT.__objc_classname: 0x22
+  __TEXT.__objc_methtype: 0xec
+  __TEXT.__const: 0x1e8
   __TEXT.__oslogstring: 0x14
-  __TEXT.__unwind_info: 0x148
-  __DATA_CONST.__auth_got: 0x558
-  __DATA_CONST.__got: 0x88
-  __DATA_CONST.__const: 0x3c0
-  __DATA_CONST.__cfstring: 0x180
-  __DATA_CONST.__objc_classlist: 0x8
+  __TEXT.__unwind_info: 0x180
+  __DATA_CONST.__auth_got: 0x5c8
+  __DATA_CONST.__got: 0x98
+  __DATA_CONST.__const: 0x3f8
+  __DATA_CONST.__cfstring: 0x280
+  __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x8
-  __DATA.__objc_const: 0x198
-  __DATA.__objc_selrefs: 0x80
-  __DATA.__objc_ivar: 0x20
-  __DATA.__objc_data: 0x50
+  __DATA_CONST.__objc_superrefs: 0x10
+  __DATA_CONST.__objc_arraydata: 0x48
+  __DATA_CONST.__objc_arrayobj: 0x30
+  __DATA.__objc_const: 0x448
+  __DATA.__objc_selrefs: 0x180
+  __DATA.__objc_ivar: 0x54
+  __DATA.__objc_data: 0xa0
   __DATA.__data: 0xc8
   __DATA.__bss: 0x131
   __DATA.__common: 0x10

   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/AmbientDisplay.framework/Versions/A/AmbientDisplay
+  - /System/Library/PrivateFrameworks/CoreBrightness.framework/Versions/A/CoreBrightness
   - /System/Library/PrivateFrameworks/DisplayServices.framework/Versions/A/DisplayServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E1B28F6E-A65A-349F-8011-9F2EDF5B219E
-  Functions: 67
-  Symbols:   221
-  CStrings:  366
+  UUID: B55F179A-CFA0-3E0E-BD85-6CAF016ABE32
+  Functions: 96
+  Symbols:   248
+  CStrings:  494
 
Symbols:
+ OBJC_IVAR_$_BrightnessModule._displayID
+ OBJC_IVAR_$_BrightnessModule._dsClient
+ OBJC_IVAR_$_BrightnessModule._hasALSCompensation
+ OBJC_IVAR_$_BrightnessModule._hasALSReset
+ OBJC_IVAR_$_BrightnessModule._observer
+ _AMBDsetCompensationStateAsync
+ _DisplayServicesCanResetAmbientLight
+ _DisplayServicesGetBrightness
+ _DisplayServicesGetBrightnessIncrement
+ _DisplayServicesHasAmbientLightCompensation
+ _DisplayServicesIsBuiltInDisplay
+ _DisplayServicesRegisterForNotification
+ _DisplayServicesSetBrightnessWithType
+ _DisplayServicesUnregisterForNotification
+ _OBJC_CLASS_$_BrightnessModule
+ _OBJC_CLASS_$_DisplayServicesClient
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_NSNumber
+ _OBJC_METACLASS_$_BrightnessModule
+ _ambientBrightnessChangedCallBack
+ _ambientResetChangedCallBack
+ _compensationEnableable
+ _displayUSBHotplugCallBack
+ _objc_alloc_init
+ _objc_opt_class
+ _objc_opt_isKindOfClass
+ _objc_retainAutorelease
+ _objc_storeStrong
+ _setCompensationStateAndRelatedWork
- _canEnableCompensation
- _setCompensationState
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
+ "/AppleInternal/Library/BuildRoots/4~CE8VugD7bXxtRzRh3JFuh7K1XpHdwZQM3JrOz7Q/Library/Caches/com.apple.xbs/Sources/AmbientDisplay/Sources/AmbientDisplayAgent.c"
+ "@\"DeviceGammaContext\""
+ "@\"DisplayServicesClient\""
+ "@20@0:8I16"
+ "AMBD %s: first time (calling setupDynamicCompensationNotifications)"
+ "AMBD Agent %s: registered displayID 0x%0x for Brightness Change Notifications"
+ "AMBD Agent: Waking"
+ "AMBD: %s DisplayServicesGetBrightness failed (error = %d)"
+ "AMBD: %s DisplayServicesGetBrightnessIncrement failed (error = %d)"
+ "AMBD: %s NULL observer passed in"
+ "AMBD: %s failed to register for Ambient Light Brightness Notifications"
+ "AMBD: %s failed to register for Ambient Reset Change Notifications"
+ "AMBD: %s failed to register for Display USB Hot Plug Notifications"
+ "AMBD: %s failed to unregister for Ambient Light Brightness Notifications"
+ "AMBD: %s failed to unregister for Ambient Reset Change Notifications"
+ "AMBD: %s failed to unregister for Display USB Hot Plug Notifications"
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
+ "AMBD: %s: handleBacklightChangeNotification() doing nothing on displayID 0x%0x (AMBD compensation %f, DSOOTF %f"
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
+ "I"
+ "TB,R,V_autoBrightnessIsAvailable"
+ "TB,R,V_autoBrightnessIsForcedDisabled"
+ "TB,R,V_brightnessIsLocked"
+ "TB,R,V_builtIn"
+ "TB,V_autoBrightnessEnabledState"
+ "Tf"
+ "Tf,R,V_brightnessIncrement"
+ "UTF8String"
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
+ "brightnessModuleRegisterForNotifications:"
+ "brightnessModuleUnregisterForNotifications:"
+ "brightnessSetting"
+ "copyPropertyForKey:andDisplay:"
+ "deactivate"
+ "description"
+ "disabled"
+ "displayIsBuiltIn"
+ "displayUSBHotplugCallBack"
+ "enabled"
+ "f"
+ "floatValue"
+ "initBrightnessModuleWithDisplayID:"
+ "isEqualToString:"
+ "kWake"
+ "locked"
+ "not locked"
+ "registerDisplayNotificationCallbackBlock:"
+ "registerNotificationForKeys:andDisplay:"
+ "setAutoBrightnessEnabledState:"
+ "setBrightnessSetting:"
+ "setCompensationStateAndRelatedWork"
+ "setUpBacklightNotifications"
+ "unregisterDisplayNotificationBlock"
+ "unregisterNotificationForKeys:andDisplay:"
+ "v20@0:8f16"
+ "v24@0:8^v16"
+ "v32@?0@\"NSString\"8Q16@24"
- "/AppleInternal/Library/BuildRoots/4~CDyzugC2qJRdaLbaZtkb8Rg55DrcCOtIESitl0w/Library/Caches/com.apple.xbs/Sources/AmbientDisplay/Sources/AmbientDisplayAgent.c"
- "AMBD Agent: registered 0x%0x for Brightness Change Notifications"
- "AMBD: %s: handleBacklightChangeNotification() on displayID 0x%0x with compensationState disabled; doing nothing"
- "setCompensationState"

```
