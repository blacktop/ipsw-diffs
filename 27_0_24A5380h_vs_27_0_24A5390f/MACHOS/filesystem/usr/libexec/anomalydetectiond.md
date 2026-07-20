## anomalydetectiond

> `/usr/libexec/anomalydetectiond`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-166.0.0.0.0
-  __TEXT.__text: 0x36d0e4
+170.0.0.0.0
+  __TEXT.__text: 0x36fcdc
   __TEXT.__auth_stubs: 0x1840
   __TEXT.__objc_stubs: 0x9480
   __TEXT.__objc_methlist: 0x8d98
-  __TEXT.__gcc_except_tab: 0x10470
-  __TEXT.__const: 0xfaee
-  __TEXT.__cstring: 0x1c8dd
-  __TEXT.__oslogstring: 0x118e6
+  __TEXT.__gcc_except_tab: 0x10560
+  __TEXT.__const: 0xfcbe
+  __TEXT.__cstring: 0x1c922
+  __TEXT.__oslogstring: 0x11b5f
   __TEXT.__objc_classname: 0x1070
-  __TEXT.__objc_methtype: 0x5f66
-  __TEXT.__objc_methname: 0xc218
+  __TEXT.__objc_methtype: 0x5f74
+  __TEXT.__objc_methname: 0xc220
   __TEXT.__ustring: 0x10ae
-  __TEXT.__unwind_info: 0xc7a8
+  __TEXT.__unwind_info: 0xc840
   __TEXT.__eh_frame: 0x670
-  __DATA_CONST.__const: 0x27530
-  __DATA_CONST.__cfstring: 0x6a40
+  __DATA_CONST.__const: 0x28848
+  __DATA_CONST.__cfstring: 0x6a60
   __DATA_CONST.__objc_classlist: 0x4c8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x128

   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__auth_got: 0xc38
   __DATA_CONST.__got: 0x678
-  __DATA_CONST.__auth_ptr: 0x48
+  __DATA_CONST.__auth_ptr: 0x50
   __DATA.__objc_const: 0x10660
   __DATA.__objc_selrefs: 0x3050
   __DATA.__objc_ivar: 0x94c
   __DATA.__objc_data: 0x2fd0
   __DATA.__data: 0x2020
-  __DATA.__bss: 0x230
+  __DATA.__bss: 0x228
   __DATA.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 17147
+  Functions: 17220
   Symbols:   608
-  CStrings:  9341
+  CStrings:  9354
 
CStrings:
+ "@154@0:8Q16C24f28f32C36S40c44c48c52c56c60Q64[3 ]72C80C84S88Q92 100 102 104C106C110*114B122C126f130f134C138B142S146C150"
+ "DebugAnomalyFMDeescSkipFailedLowSense"
+ "T^{TriggerSample=CCSIQffcccccQ[3 ]CCSQCBC[16c]ffCCBS   C},R,N"
+ "[%s] DEBUG seam active: skipping failed low-sense epochs during evaluation"
+ "[%s] DEBUG skipping failed low-sense epoch %zu"
+ "[%s] adapter-gate-fail,invalid,invalid=%u"
+ "[%s] all low-sense epochs below threshold, deescalate"
+ "[%s] all low-sense epochs below threshold, deescalate inert"
+ "[%s] epochFinalize: insufficient data (IMU=%u/%d, pressure=%u/%d, dm=%u/%d)"
+ "[%s] gate-fail,model,w=%u,rc=%d"
+ "[%s] model predicted crash on low-sense epoch %zu of %zu"
+ "[%s] no low-sense epoch observed, returning no decision"
+ "[%s] pipeline did not run on low-sense epoch %zu, cannot deescalate"
+ "[%s] summary,A,%{public}llu,B,%{public}u,mode,%{public}u,config-1,%{public}d,debug-1a,%{public}u,debug-1b,%{public}u,debug-1c,%{public}u,debug-1d,%{public}d,debug-1e,%{public}d,debug-2a,%{public}zu,debug-2b,%{public}zu,debug-2c,%{public}zu"
+ "[%s] test-drop,dm,idx=%llu"
+ "[%s] test-drop,fastaccel,idx=%llu"
+ "[%s] test-drop,pressure,idx=%llu"
+ "[%s] unexpected dimensions, model %zu crash %zu rollover %zu"
+ "[AnomalyFM] summary,A,%{public}llu,B,%{public}f,config-1,%{public}d,config-2,%{public}f,config-3,%{public}d,debug-1a,%{public}u,debug-1b,%{public}u,debug-1c,%{public}u,debug-1d,%{public}u,debug-1e,%{public}d,debug-1f,%{public}d,debug-1g,%{public}f,debug-1h,%{public}f,debug-2a,%{public}u,debug-2b,%{public}u,debug-2c,%{public}d,debug-2d,%{public}u,debug-2e,%{public}u,debug-2f,%{public}u"
+ "[Zg] summary,%{public}d,A,%{public}llu,B,%{public}hu,C,%{public}hu,D,%{public}f,E,%{public}f,F,%{public}f,G,%{public}f,H,%{public}f,I,%{public}hd,J,%{public}hu,K,%{public}d,L,%{public}d,M,%{public}d,N,%{public}llu,O,%{public}u,config-1,%{public}f,config-2,%{public}f"
+ "^{TriggerSample=CCSIQffcccccQ[3 ]CCSQCBC[16c]ffCCBS   C}16@0:8"
+ "com.apple.fm.coremotion.anomalyfm"
+ "com.apple.fm.coremotion.anomalyfm.adaptor"
+ "gpsAltitudeUncertainty"
+ "imuIndex"
+ "initWithTimestamp:meta:decel:impact:path:armedSec:motionHint:gpsHint:basebandHint:wifiHint:btHint:lastValidImuTimestamp:vehicleProbabilityLongTermMean:martyPath:enableMode:martyArmedSec:companionAopTs:maxMeanTenMinPreTrigger:lastCompleted15sWindowMean:currentWindowMean:numMaxEnvelopes:igneousPath:igneousGUID:isCharging:sigEnv:martyImpactMagnitude:martyRotationMagnitude:overrideMode:martyIsBicycle:martyArmedSecBicycle:locallyArmed:"
+ "propertyA0"
+ "propertyA1"
+ "{TriggerSample=\"meta\"C\"path\"C\"armedSec\"S\"rmsSN\"I\"timestamp\"Q\"decel\"f\"impact\"f\"motionHint\"c\"gpsHint\"c\"basebandHint\"c\"wifiHint\"c\"btHint\"c\"lastValidImuTimestamp\"Q\"vehicleProbabilityLongTermMean\"[3 ]\"martyPath\"C\"enableMode\"C\"martyArmedSec\"S\"companionAopTs\"Q\"igneousPath\"C\"isCharging\"B\"sigEnv\"C\"igneousGUID\"[16c]\"martyImpactMagnitude\"f\"martyRotationMagnitude\"f\"locallyArmed\"C\"overrideMode\"C\"martyIsBicycle\"B\"martyArmedSecBicycle\"S\"maxMeanTenMinPreTrigger\" \"lastCompleted15sWindowMean\" \"currentWindowMean\" \"numMaxEnvelopes\"C}"
- "@150@0:8Q16C24f28f32C36S40c44c48c52c56c60Q64[3 ]72C80C84S88Q92 100 102 104C106C110*114B122f126f130C134B138S142C146"
- "T^{TriggerSample=CCSIQffcccccQ[3 ]CCSQCB[16c]ffCCBS   C},R,N"
- "[%s] all epochs were below threshold, deescalate inert: %d %d"
- "[%s] all epochs were below threshold, deescalate: %d %d"
- "[%s] deescalator active: %d %d: model found presence of crash"
- "[%s] returning decision nop"
- "[%s] skipping inference until all inputs present"
- "[%s] summary,A,%{public}llu,B,%{public}u,mode,%{public}u,config-1,%{public}d,debug-1a,%{public}u,debug-1b,%{public}u,debug-1c,%{public}u,debug-1d,%{public}d,debug-1e,%{public}d"
- "[AnomalyFM] summary,A,%{public}llu,B,%{public}f,config-1,%{public}d,config-2,%{public}f,config-3,%{public}d,debug-1a,%{public}u,debug-1b,%{public}u,debug-1c,%{public}u,debug-1d,%{public}u,debug-1e,%{public}d,debug-1f,%{public}d,debug-1g,%{public}f,debug-1h,%{public}f"
- "[Zg] epoch %{public}d YES\n"
- "[Zg] summary,%{public}d,A,%{public}llu,B,%{public}hu,C,%{public}hu,D,%{public}f,E,%{public}f,F,%{public}f,G,%{public}f,H,%{public}f,I,%{public}hd,J,%{public}hu,K,%{public}d,L,%{public}d,M,%{public}d,N,%{public}llu,config-1,%{public}f,config-2,%{public}f\n"
- "^{TriggerSample=CCSIQffcccccQ[3 ]CCSQCB[16c]ffCCBS   C}16@0:8"
- "com.apple.fm.coremotion.anomalyfm.sideload.adapter"
- "com.apple.fm.coremotion.anomalyfm.sideload.base"
- "initWithTimestamp:meta:decel:impact:path:armedSec:motionHint:gpsHint:basebandHint:wifiHint:btHint:lastValidImuTimestamp:vehicleProbabilityLongTermMean:martyPath:enableMode:martyArmedSec:companionAopTs:maxMeanTenMinPreTrigger:lastCompleted15sWindowMean:currentWindowMean:numMaxEnvelopes:igneousPath:igneousGUID:isCharging:martyImpactMagnitude:martyRotationMagnitude:overrideMode:martyIsBicycle:martyArmedSecBicycle:locallyArmed:"
- "{TriggerSample=\"meta\"C\"path\"C\"armedSec\"S\"rmsSN\"I\"timestamp\"Q\"decel\"f\"impact\"f\"motionHint\"c\"gpsHint\"c\"basebandHint\"c\"wifiHint\"c\"btHint\"c\"lastValidImuTimestamp\"Q\"vehicleProbabilityLongTermMean\"[3 ]\"martyPath\"C\"enableMode\"C\"martyArmedSec\"S\"companionAopTs\"Q\"igneousPath\"C\"isCharging\"B\"igneousGUID\"[16c]\"martyImpactMagnitude\"f\"martyRotationMagnitude\"f\"locallyArmed\"C\"overrideMode\"C\"martyIsBicycle\"B\"martyArmedSecBicycle\"S\"maxMeanTenMinPreTrigger\" \"lastCompleted15sWindowMean\" \"currentWindowMean\" \"numMaxEnvelopes\"C}"
```
