## powerexperienced

> `/usr/libexec/powerexperienced`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`

```diff

-182.60.2.0.0
-  __TEXT.__text: 0x1b994
-  __TEXT.__auth_stubs: 0x6c0
-  __TEXT.__objc_stubs: 0x3c40
-  __TEXT.__objc_methlist: 0x25cc
-  __TEXT.__const: 0x150
-  __TEXT.__cstring: 0x13d1
-  __TEXT.__objc_methname: 0x444c
-  __TEXT.__oslogstring: 0x33a9
-  __TEXT.__objc_classname: 0x442
-  __TEXT.__objc_methtype: 0x8d3
-  __TEXT.__gcc_except_tab: 0x4c
-  __TEXT.__unwind_info: 0x9f0
-  __DATA_CONST.__const: 0x900
-  __DATA_CONST.__cfstring: 0x14e0
+182.60.3.0.0
+  __TEXT.__text: 0x1d138
+  __TEXT.__auth_stubs: 0x720
+  __TEXT.__objc_stubs: 0x4020
+  __TEXT.__objc_methlist: 0x2744
+  __TEXT.__const: 0x158
+  __TEXT.__cstring: 0x1507
+  __TEXT.__objc_methname: 0x48ad
+  __TEXT.__oslogstring: 0x37a4
+  __TEXT.__objc_classname: 0x45e
+  __TEXT.__objc_methtype: 0x954
+  __TEXT.__gcc_except_tab: 0x74
+  __TEXT.__dlopen_cstrs: 0xb0
+  __TEXT.__unwind_info: 0xa60
+  __DATA_CONST.__const: 0x9b0
+  __DATA_CONST.__cfstring: 0x15c0
   __DATA_CONST.__objc_classlist: 0xf0
-  __DATA_CONST.__objc_protolist: 0x88
+  __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0xe0
   __DATA_CONST.__objc_intobj: 0x108
   __DATA_CONST.__objc_floatobj: 0x10
-  __DATA_CONST.__auth_got: 0x370
+  __DATA_CONST.__auth_got: 0x3a0
   __DATA_CONST.__got: 0x1a0
-  __DATA.__objc_const: 0x5a10
-  __DATA.__objc_selrefs: 0x1240
-  __DATA.__objc_ivar: 0x28c
+  __DATA.__objc_const: 0x5c18
+  __DATA.__objc_selrefs: 0x1348
+  __DATA.__objc_ivar: 0x2b4
   __DATA.__objc_data: 0x960
-  __DATA.__data: 0x660
+  __DATA.__data: 0x6c0
   __DATA.__common: 0x80
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMotion.framework/CoreMotion

   - /System/Library/PrivateFrameworks/PerformanceControlKit.framework/PerformanceControlKit
   - /System/Library/PrivateFrameworks/PowerExperience.framework/PowerExperience
   - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
+  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/Trial.framework/Trial
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 882
-  Symbols:   171
-  CStrings:  1491
+  Functions: 925
+  Symbols:   177
+  CStrings:  1586
 
Symbols:
+ __Block_object_dispose
+ __sl_dlopen
+ _abort_report_np
+ _free
+ _objc_getClass
+ _objc_retainAutorelease
CStrings:
+ "%s"
+ "@\"BIThermalPredictionClient\""
+ "@\"PowerUISmartChargeClient\""
+ "BIThermalPredictionClient"
+ "BIThermalPredictionDelegate"
+ "Battery %d reached charge limit %d, TLC mitigation is ignored"
+ "BatteryIntelligence unavailable; TLC predicted package power limits are off"
+ "Charging, not in use and TLC engaged"
+ "Charging, not in use and TLC predicted"
+ "Listening for TLC predictions"
+ "MCL limit changed to %d"
+ "PowerUISmartChargeClient"
+ "Q20@0:8i16"
+ "Q24@0:8Q16"
+ "Resetting TLC Mitigation Background and Utility Power Budgets"
+ "Seeding TLC prediction"
+ "Setting TLC Mitigation Background and Utility Power Budgets %.2f and %.2f"
+ "T@\"BIThermalPredictionClient\",&,N,V_predictionClient"
+ "T@\"PowerUISmartChargeClient\",&,N,V_smartChargeClient"
+ "TB,V_tlcEnabled"
+ "TB,V_tlcPredicted"
+ "TLC prediction changed to %d"
+ "TLC prediction error %@"
+ "TLC prediction update willHitTLC=%d"
+ "TLC seed prediction failed: %@"
+ "TLC seed prediction willHitTLC=%d"
+ "TLCMitigationHighSOC"
+ "TLCMitigationHighSOCPackagePowerTarget"
+ "TLCMitigationLowSOC"
+ "TLCMitigationLowSOCPackagePowerTarget"
+ "TLCMitigationSOCThreshold"
+ "TLCMitigationsEnabled"
+ "TQ,V_tlcHighSOCPowerOption"
+ "TQ,V_tlcLowSOCPowerOption"
+ "Tf,V_tlcBgPowerTarget"
+ "Tf,V_tlcUtilityPowerTarget"
+ "Ti,V_mclLimit"
+ "Ti,V_tlcSOCThreshold"
+ "Trial: TLC Mitigation High SOC Package Power Target = %lld"
+ "Trial: TLC Mitigation Low SOC Package Power Target = %lld"
+ "Trial: TLC Mitigation SOC Threshold = %lld"
+ "Trial: TLC Mitigations Enabled = %d"
+ "Trial:No trial value for TLC Mitigation High SOC Package Power Target"
+ "Trial:No trial value for TLC Mitigation Low SOC Package Power Target"
+ "Trial:No trial value for TLC Mitigation SOC Threshold"
+ "Trial:No trial value for TLC Mitigations Enabled"
+ "Unable to find class %s"
+ "_mclLimit"
+ "_predictionClient"
+ "_smartChargeClient"
+ "_tlcBgPowerTarget"
+ "_tlcEnabled"
+ "_tlcHighSOCPowerOption"
+ "_tlcLowSOCPowerOption"
+ "_tlcPredicted"
+ "_tlcSOCThreshold"
+ "_tlcUtilityPowerTarget"
+ "c\"s"
+ "chargeLimit"
+ "com.apple.powerexperienced.tlcPredictionSeed"
+ "didUpdateTLCPrediction:error:"
+ "getMCLLimitWithHandler:"
+ "initWithClientName:"
+ "isTLCEngaged"
+ "isTLCPredictedOrTLCEngaged"
+ "mclLimit"
+ "predictTLCWithError:"
+ "predictionClient"
+ "setMclLimit:"
+ "setPredictionClient:"
+ "setSmartChargeClient:"
+ "setTlcBgPowerTarget:"
+ "setTlcEnabled:"
+ "setTlcHighSOCPowerOption:"
+ "setTlcLowSOCPowerOption:"
+ "setTlcPredicted:"
+ "setTlcSOCThreshold:"
+ "setTlcUtilityPowerTarget:"
+ "setUpTLCPrediction"
+ "smartChargeClient"
+ "softlink:r:path:/System/Library/PrivateFrameworks/BatteryIntelligence.framework/BatteryIntelligence"
+ "softlink:r:path:/System/Library/PrivateFrameworks/PowerUI.framework/PowerUI"
+ "tlcBgPowerTarget"
+ "tlcEnabled"
+ "tlcHighSOCPowerOption"
+ "tlcLowSOCPowerOption"
+ "tlcMitigationForBatteryLevel:"
+ "tlcPackagePowerOptionForMitigation:"
+ "tlcPredicted"
+ "tlcSOCThreshold"
+ "tlcUtilityPowerTarget"
+ "updateTLCBGUtilityPowerTargets:"
+ "updateTLCPrediction:"
+ "v20@?0C8@\"NSError\"12"
+ "v32@0:8@\"BIThermalPredictionOutput\"16@\"NSError\"24"
+ "willHitTLC"
- "C!R"
```
