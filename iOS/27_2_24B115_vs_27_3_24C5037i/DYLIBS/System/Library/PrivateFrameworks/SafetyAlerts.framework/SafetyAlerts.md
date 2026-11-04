## SafetyAlerts

> `/System/Library/PrivateFrameworks/SafetyAlerts.framework/SafetyAlerts`

```diff

-70.0.21.0.0
-  __TEXT.__text: 0xbddc
-  __TEXT.__objc_methlist: 0x704
+70.0.27.0.0
+  __TEXT.__text: 0xc18c
+  __TEXT.__objc_methlist: 0x724
   __TEXT.__const: 0xa8
-  __TEXT.__gcc_except_tab: 0x12b4
-  __TEXT.__cstring: 0xfd5
-  __TEXT.__oslogstring: 0x326f
+  __TEXT.__gcc_except_tab: 0x132c
+  __TEXT.__cstring: 0x10b6
+  __TEXT.__oslogstring: 0x32cd
   __TEXT.__unwind_info: 0x568
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5d8
+  __DATA_CONST.__objc_selrefs: 0x5f0
   __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__got: 0xf8
   __AUTH_CONST.__const: 0xa0
-  __AUTH_CONST.__cfstring: 0xec0
-  __AUTH_CONST.__objc_const: 0xb68
+  __AUTH_CONST.__cfstring: 0xf60
+  __AUTH_CONST.__objc_const: 0xbf8
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x140
-  __DATA.__objc_ivar: 0x8c
-  __DATA.__data: 0x1a8
+  __DATA.__objc_ivar: 0x98
+  __DATA.__data: 0x1c0
   __DATA_DIRTY.__objc_data: 0xa0
   __DATA_DIRTY.__common: 0x20
   __DATA_DIRTY.__bss: 0x60

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 168
-  Symbols:   493
-  CStrings:  299
+  Functions: 171
+  Symbols:   503
+  CStrings:  307
 
Symbols:
+ -[SAGeoAlertData initWithAlertHash:title:message:instructionMessage:language:translationLanguage:translatedMessageText:translatedInstructionsText:safetyCategory:safetyEvent:safetyCategoryEnums:safetyEventEnums:deliveryTime:displayTime:displayed:polygonalGeofences:circularGeofences:epicenterCoordinate:alertType:]
+ -[SAGeoAlertData translatedInstructionsText]
+ -[SAGeoAlertData translatedMessageText]
+ -[SAGeoAlertData translationLanguage]
+ GCC_except_table49
+ GCC_except_table50
+ GCC_except_table51
+ _OBJC_IVAR_$_SAGeoAlertData._translatedInstructionsText
+ _OBJC_IVAR_$_SAGeoAlertData._translatedMessageText
+ _OBJC_IVAR_$_SAGeoAlertData._translationLanguage
+ _kSAOtherAlertsDescriptionNoRelay
+ _kSATMachineTranslation
+ _kSATMachineTranslationDescription
- -[SAGeoAlertData initWithAlertHash:title:message:instructionMessage:language:safetyCategory:safetyEvent:safetyCategoryEnums:safetyEventEnums:deliveryTime:displayTime:displayed:polygonalGeofences:circularGeofences:epicenterCoordinate:alertType:]
- GCC_except_table46
- GCC_except_table48
CStrings:
+ "DeviceSupportsGenerativeModelSystems"
+ "MACHINE_TRANSLATION"
+ "MACHINE_TRANSLATION_DESCRIPTION"
+ "MachineTranslation"
+ "SAFETY_ALERTS_OTHER_ALERTS_DESCRIPTION_NO_RELAY"
+ "translatedInstructionsText"
+ "translatedMessageText"
+ "translationLanguage"
+ "{\"msg%{public}.0s\":\"#platformInfo\", \"deviceClass\":%{private, location:escape_only}s, \"iPhone\":%{private}hhd, \"iPod\":%{private}hhd, \"iPad\":%{private}hhd, \"watch\":%{private}hhd, \"appleTV\":%{private}hhd, \"homePod\":%{private}hhd, \"mac\":%{private}hhd, \"cellular\":%{private}hhd, \"dualSim\":%{private}hhd, \"cellularWatch\":%{private}hhd, \"wifiOnlyWatch\":%{private}hhd, \"internal\":%{private}hhd, \"supportedDevice\":%{private}hhd, \"supportedOSType\":%{private}hhd, \"supportedPlatform\":%{private}hhd, \"aop\":%{private}hhd, \"generativeModels\":%{private}hhd, \"tinkerWatch\":%{private}hhd}"
+ "{\"msg%{public}.0s\":\"daemonInterfaceProd,settingsData\", \"eqState\":%{public, location:escape_only}@, \"alwaysPlaySoundState\":%{public, location:escape_only}@, \"otherAlertsState\":%{public, location:escape_only}@, \"improvedAlertDeliveryState\":%{public, location:escape_only}@, \"machineTranslationState\":%{public, location:escape_only}@, \"mainSafetyAlerts\":%{public, location:escape_only}@}"
- "{\"msg%{public}.0s\":\"#platformInfo\", \"deviceClass\":%{private, location:escape_only}s, \"iPhone\":%{private}hhd, \"iPod\":%{private}hhd, \"iPad\":%{private}hhd, \"watch\":%{private}hhd, \"appleTV\":%{private}hhd, \"homePod\":%{private}hhd, \"mac\":%{private}hhd, \"cellular\":%{private}hhd, \"dualSim\":%{private}hhd, \"cellularWatch\":%{private}hhd, \"wifiOnlyWatch\":%{private}hhd, \"internal\":%{private}hhd, \"supportedDevice\":%{private}hhd, \"supportedOSType\":%{private}hhd, \"supportedPlatform\":%{private}hhd, \"aop\":%{private}hhd, \"tinkerWatch\":%{private}hhd}"
- "{\"msg%{public}.0s\":\"daemonInterfaceProd,settingsData\", \"eqState\":%{public, location:escape_only}@, \"alwaysPlaySoundState\":%{public, location:escape_only}@, \"otherAlertsState\":%{public, location:escape_only}@, \"improvedAlertDeliveryState\":%{public, location:escape_only}@, \"mainSafetyAlerts\":%{public, location:escape_only}@}"
```
