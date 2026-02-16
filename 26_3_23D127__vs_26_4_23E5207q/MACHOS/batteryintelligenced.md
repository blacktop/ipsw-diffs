## batteryintelligenced

> `/usr/libexec/batteryintelligenced`

```diff

-183.80.2.0.0
-  __TEXT.__text: 0x32780
-  __TEXT.__auth_stubs: 0x8c0
-  __TEXT.__objc_stubs: 0x3700
-  __TEXT.__objc_methlist: 0x214c
-  __TEXT.__cstring: 0x2a7a
-  __TEXT.__objc_classname: 0x659
-  __TEXT.__objc_methtype: 0x795
+195.100.2.0.0
+  __TEXT.__text: 0x3723c
+  __TEXT.__auth_stubs: 0x880
+  __TEXT.__objc_stubs: 0x3880
+  __TEXT.__objc_methlist: 0x259c
+  __TEXT.__cstring: 0x2b8a
+  __TEXT.__objc_classname: 0x775
+  __TEXT.__objc_methtype: 0x80c
   __TEXT.__const: 0x270
-  __TEXT.__objc_methname: 0x4396
-  __TEXT.__oslogstring: 0x586f
-  __TEXT.__gcc_except_tab: 0x280
-  __TEXT.__unwind_info: 0x8f0
-  __DATA_CONST.__auth_got: 0x470
-  __DATA_CONST.__got: 0x230
+  __TEXT.__objc_methname: 0x4622
+  __TEXT.__oslogstring: 0x5b5a
+  __TEXT.__gcc_except_tab: 0x268
+  __TEXT.__unwind_info: 0xc08
+  __DATA_CONST.__auth_got: 0x450
+  __DATA_CONST.__got: 0x240
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x9d0
-  __DATA_CONST.__cfstring: 0x2fc0
-  __DATA_CONST.__objc_classlist: 0x188
-  __DATA_CONST.__objc_protolist: 0x38
+  __DATA_CONST.__const: 0xa90
+  __DATA_CONST.__cfstring: 0x3120
+  __DATA_CONST.__objc_classlist: 0x1c0
+  __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x168
-  __DATA_CONST.__objc_arraydata: 0xc88
-  __DATA_CONST.__objc_arrayobj: 0x510
-  __DATA_CONST.__objc_intobj: 0xcf0
+  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__objc_superrefs: 0x1a0
+  __DATA_CONST.__objc_arraydata: 0xca8
+  __DATA_CONST.__objc_arrayobj: 0x570
+  __DATA_CONST.__objc_intobj: 0xd20
   __DATA_CONST.__objc_doubleobj: 0x40
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x5358
-  __DATA.__objc_selrefs: 0x10b8
-  __DATA.__objc_ivar: 0x248
-  __DATA.__objc_data: 0xf50
-  __DATA.__data: 0x2e8
-  __DATA.__bss: 0x1e8
+  __DATA.__objc_const: 0x5eb8
+  __DATA.__objc_selrefs: 0x1148
+  __DATA.__objc_ivar: 0x270
+  __DATA.__objc_data: 0x1180
+  __DATA.__data: 0x370
+  __DATA.__bss: 0x210
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreML.framework/CoreML
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/CoreDuetContext.framework/CoreDuetContext
   - /System/Library/PrivateFrameworks/PerfPowerServicesReader.framework/PerfPowerServicesReader
   - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
+  - /System/Library/PrivateFrameworks/PowerUI.framework/PowerUI
   - /System/Library/PrivateFrameworks/Trial.framework/Trial
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FB7B5ED6-0E05-3CB5-BA6F-3A1ECA7D56BB
-  Functions: 1033
-  Symbols:   228
-  CStrings:  2209
+  UUID: D27E75A9-EFD0-335D-B5F7-60D1E3D70044
+  Functions: 1159
+  Symbols:   226
+  CStrings:  2282
 
Symbols:
+ ___NSArray0__struct
+ ___NSDictionary0__struct
+ _objc_setProperty_atomic_copy
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x3
- _objc_retain_x4
CStrings:
+ "%@ is not ready yet"
+ "%@ is not ready yet. Attempt to trigger run failed."
+ "%@: accepted new connection from pid %d and service name: %@"
+ "%@: rejected new connection from pid %d. Not entitled"
+ "AverageTemperature"
+ "BatteryAlgorithmsControlProtocol"
+ "BatteryAlgorithmsControlService"
+ "BatteryAnalysisEstimator is not supported on this platform."
+ "CafeLVR"
+ "ChemID"
+ "Could not load battery_analysis_ttl_model_6w2j9kistm.mlmodelc in the bundle resource"
+ "Could not load ocv_drift_model_myxd7pqa68.mlmodelc in the bundle resource"
+ "Current SOC (%@) is >= target endSOC (%@)"
+ "Current SOC (%@) is >= target endSOC (%@). Cannot estimate."
+ "Key passed in = %@ is not allowed"
+ "LowVoltageResidencyCounters"
+ "Registered %@ for batteryalgorithmscontrolservice"
+ "SOCVVoltage"
+ "Started %@ sharedInstance without registering algo"
+ "Started BatteryAlgorithmsControlService."
+ "Starting BatteryAlgorithmsControlService."
+ "T@\"NSDictionary\",&,V_algorithms"
+ "T@?,C,V_batteryAlgorithmsInitAndRunTrigger"
+ "T@?,C,V_batteryAlgorithmsInitTrigger"
+ "T@?,C,V_batteryAlgorithmsRunTrigger"
+ "XPC handler is nil/invalid for getAvailableAlgorithms. Client disconnected or connection invalid. Cannot deliver response."
+ "_algorithms"
+ "_batteryAlgorithmsInitAndRunTrigger"
+ "_batteryAlgorithmsInitTrigger"
+ "_batteryAlgorithmsRunTrigger"
+ "algorithms"
+ "batteryAlgorithmsInitAndRunTrigger"
+ "batteryAlgorithmsInitTrigger"
+ "batteryAlgorithmsRunTrigger"
+ "battery_analysis_ttl_model_6w2j9kistm"
+ "battery_analysis_ttl_model_6w2j9kistmInput"
+ "battery_analysis_ttl_model_6w2j9kistmOutput"
+ "com.apple.batteryintelligenced.batteryalgorithmscontrol"
+ "curr_charge_accum"
+ "curr_wra"
+ "get:specifier:reply:"
+ "getAvailableAlgorithms:"
+ "getWithSpecifier:"
+ "isWatchSeries9OrNewer"
+ "ocv_drift_model_myxd7pqa68"
+ "ocv_drift_model_myxd7pqa68Input"
+ "ocv_drift_model_myxd7pqa68Output"
+ "ready"
+ "service"
+ "setAlgorithms:"
+ "setBatteryAlgorithmsInitAndRunTrigger:"
+ "setBatteryAlgorithmsInitTrigger:"
+ "setBatteryAlgorithmsRunTrigger:"
+ "triggerInit"
+ "triggerInitAndRun"
+ "triggerRunOnly"
+ "update:specifier:"
+ "updateWithSpecifier:"
+ "v24@0:8@?<v@?@\"NSArray\">16"
+ "v32@0:8@\"NSString\"16@\"NSString\"24"
+ "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSDictionary\">32"
- "BatteryAnalysisEstimator is not supported in this platform."

```
