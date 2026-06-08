## powerexperienced

> `/usr/libexec/powerexperienced`

```diff

-136.100.13.0.0
-  __TEXT.__text: 0x1af70
-  __TEXT.__auth_stubs: 0x680
-  __TEXT.__objc_stubs: 0x35c0
-  __TEXT.__objc_methlist: 0x212c
+165.0.0.502.1
+  __TEXT.__text: 0x1a604
+  __TEXT.__auth_stubs: 0x6d0
+  __TEXT.__objc_stubs: 0x3820
+  __TEXT.__objc_methlist: 0x2334
   __TEXT.__const: 0x138
-  __TEXT.__cstring: 0x121d
-  __TEXT.__objc_methname: 0x3da1
-  __TEXT.__oslogstring: 0x2d42
-  __TEXT.__objc_classname: 0x3f0
-  __TEXT.__objc_methtype: 0x819
+  __TEXT.__cstring: 0x12ab
+  __TEXT.__objc_methname: 0x4060
+  __TEXT.__oslogstring: 0x2f7e
+  __TEXT.__objc_classname: 0x400
+  __TEXT.__objc_methtype: 0x840
   __TEXT.__gcc_except_tab: 0x48
   __TEXT.__dlopen_cstrs: 0x8d
-  __TEXT.__unwind_info: 0x788
-  __DATA_CONST.__auth_got: 0x350
-  __DATA_CONST.__got: 0x178
-  __DATA_CONST.__const: 0x870
-  __DATA_CONST.__cfstring: 0x1300
-  __DATA_CONST.__objc_classlist: 0xd0
+  __TEXT.__unwind_info: 0x710
+  __DATA_CONST.__const: 0x8d0
+  __DATA_CONST.__cfstring: 0x12e0
+  __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x48
-  __DATA_CONST.__objc_superrefs: 0xc0
+  __DATA_CONST.__objc_superrefs: 0xd0
   __DATA_CONST.__objc_intobj: 0xf0
-  __DATA.__objc_const: 0x5360
-  __DATA.__objc_selrefs: 0x1068
-  __DATA.__objc_ivar: 0x238
-  __DATA.__objc_data: 0x820
+  __DATA_CONST.__auth_got: 0x378
+  __DATA_CONST.__got: 0x178
+  __DATA.__objc_const: 0x5680
+  __DATA.__objc_selrefs: 0x1108
+  __DATA.__objc_ivar: 0x260
+  __DATA.__objc_data: 0x8c0
   __DATA.__data: 0x600
-  __DATA.__bss: 0x230
+  __DATA.__bss: 0x258
   __DATA.__common: 0x80
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMotion.framework/CoreMotion

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 51EB0653-9CD9-314F-B950-57E8D2DC670B
-  Functions: 785
-  Symbols:   164
-  CStrings:  1533
+  UUID: 65753D96-5AF7-3591-98BC-D1E7C72B49AB
+  Functions: 829
+  Symbols:   169
+  CStrings:  1573
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x3
+ _objc_retain_x8
+ _objc_retain_x9
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "3!R"
+ "@\"CLPCPolicyInterfaceHelper\""
+ "AssistantMode changing from %@ to %@ (siriRemoteSession=%d, siriLocalSession=%d, assistantUI=%d, siriAudio=%d)"
+ "AssistantModeController"
+ "AssistantUI"
+ "C16@0:8"
+ "Captured battery level at plug-in: %d%%"
+ "DisplaySecondary"
+ "Error setting clpc trial value %@"
+ "Failed to update CLPC with Assistant Mode state %@. Error: %@"
+ "Failed to update CLPC with LPM state %@. Error: %@"
+ "Failed to write SDTP key. Error 0x%x"
+ "Ignoring invalid thermal state from defaults: %lu"
+ "Restoring thermal state from defaults: %@"
+ "Saved thermal state to defaults: %@"
+ "SiriLocalSession"
+ "SiriRemoteSession"
+ "T@\"CLPCPolicyInterfaceHelper\",&,V_clpcHelper"
+ "T@\"NSNumber\",&,V_lastForwardedLPMState"
+ "TB,V_assistantModeActive"
+ "TC,V_currentThermalState"
+ "Thermal state changing from %@ to %@ (angle %.1f)"
+ "ThermalExperienceController"
+ "ThermalExperienceController not supported on this platform"
+ "ThermalExperienceState"
+ "ThermalState"
+ "Trial:No trial value for CLPC tuning option. Resetting to default"
+ "Updated CLPC with Assistant Mode state %@"
+ "Updated CLPC with LPM state %@"
+ "Updating CLTM with thermal state %@"
+ "_assistantModeActive"
+ "_clpcHelper"
+ "_currentThermalState"
+ "_lastForwardedLPMState"
+ "assistantModeActive"
+ "assistantmodecontroller"
+ "clpcHelper"
+ "currentThermalState"
+ "evaluateAssistantMode"
+ "evaluateControllers"
+ "evaluatePowerMode: %@: %d display %d , carPlay %d, pluggedIn %d, dataMigrationInProgress %d, batterylevel %@, batteryLevelAtPlugIn %d, lowPowerMode %d, predictedShortCharge %d, predictedLongCharge %d"
+ "evaluatePowerMode: %@: %d display %d, carPlaySession %d, nFCSession %d, audioSession %d, sleepInProgress %d, wakeInProgress %d, onenessSession %d, siriAudio %d, siriRemoteSession %d, siriLocalSession %d, assistantUI %d, fitnessIntelligence %d, dataMigrationInProgress %d, usbDeviceMode %d, pluggedIn %d (allowOnCharger: %d)"
+ "evaluatePowerMode: lowPowerModeActive %d batteryLevelAtPlugIn %d"
+ "evaluateThermalState"
+ "floatValue"
+ "forwardLPMStateToCLPC"
+ "inUse displayOn %d, carPlaySession %d, cameraActive %d, hotspotActive %d, audioSession %d, phoneCall %d, onenessActive %d, siriAudio %d, siriRemoteSession %d, siriLocalSession %d, assistantUI %d"
+ "kAngleContext"
+ "kBatteryLevelAtPlugInContext"
+ "lastForwardedLPMState"
+ "numberWithUnsignedChar:"
+ "setAssistantMode:"
+ "setAssistantMode:options:error:"
+ "setAssistantModeActive:"
+ "setClpcHelper:"
+ "setCurrentThermalState:"
+ "setLastForwardedLPMState:"
+ "setLowPowerMode:"
+ "setLowPowerMode:options:error:"
+ "shouldEngageForCriticalBattery:predictor:"
+ "shouldEngageForLowPowerMode:predictor:"
+ "shouldEngageForPredictedShortSession:predictor:"
+ "thermalexperiencecontroller"
+ "updateCLTMThermalState:"
+ "v20@0:8C16"
- "3!Q"
- "CLPC_LPMOption"
- "HardwarePlatform"
- "Trial: Device/Platform not expected for LPM Trial."
- "Trial: Setting TrialID: %lld with CLPC"
- "Trial: Setting TrialID: %lld with CLPCInternal"
- "Trial:CLPC LPMOption %lld adjusted to %lld"
- "Trial:CLPC LPMOption factor %lld"
- "Trial:CLPC_TuningOption and CLPC_LPMOption are both zero. Resetting to default"
- "Trial:CLPC_TuningOption and CLPC_LPMOption both have non-zero values. Resetting to default"
- "Trial:Error setting clpc trial value %@"
- "adjustLPMOption:"
- "evaluatePowerController"
- "evaluatePowerMode: %@: %d display %d unlocked %d, carPlay %d, pluggedIn %d, dataMigrationInProgress %d, batterylevel %@"
- "evaluatePowerMode: %@: %d display %d, carPlaySession %d, nFCSession %d, audioSession %d, sleepInProgress %d, wakeInProgress %d, onenessSession %d, siriAudio %d, fitnessIntelligence %d, dataMigrationInProgress %d, pluggedIn %d (allowOnCharger: %d)"
- "evaluatePowerMode: isUnlocked %d"
- "inUse displayOn %d, carPlaySession %d, cameraActive %d, hotspotActive %d, audioSession %d, phoneCall %d, onenessActive %d, siriAudio %d"
- "kHardwarePlatformContext"
- "q24@0:8q16"
- "t8101"
- "t8110"
- "t8120"
- "t8130"
- "t8140"
- "t8150"

```
