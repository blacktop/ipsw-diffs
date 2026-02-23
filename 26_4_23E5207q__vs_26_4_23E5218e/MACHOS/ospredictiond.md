## ospredictiond

> `/usr/libexec/ospredictiond`

```diff

-234.100.11.0.0
-  __TEXT.__text: 0x6192c
-  __TEXT.__auth_stubs: 0x7d0
-  __TEXT.__objc_stubs: 0x8a80
-  __TEXT.__objc_methlist: 0x89d8
+234.100.14.0.0
+  __TEXT.__text: 0x62f70
+  __TEXT.__auth_stubs: 0x7f0
+  __TEXT.__objc_stubs: 0x8c20
+  __TEXT.__objc_methlist: 0x8a28
   __TEXT.__const: 0x308
-  __TEXT.__cstring: 0x49df
-  __TEXT.__objc_methname: 0x13da5
-  __TEXT.__oslogstring: 0x5754
+  __TEXT.__cstring: 0x4be7
+  __TEXT.__objc_methname: 0x13f70
+  __TEXT.__oslogstring: 0x5a19
   __TEXT.__objc_classname: 0xd53
-  __TEXT.__objc_methtype: 0x2269
-  __TEXT.__gcc_except_tab: 0x9bc
-  __TEXT.__unwind_info: 0x16a8
-  __DATA_CONST.__auth_got: 0x3f8
-  __DATA_CONST.__got: 0x3c0
-  __DATA_CONST.__const: 0xf50
-  __DATA_CONST.__cfstring: 0x56a0
+  __TEXT.__objc_methtype: 0x232b
+  __TEXT.__gcc_except_tab: 0x9a8
+  __TEXT.__unwind_info: 0x16b0
+  __DATA_CONST.__auth_got: 0x408
+  __DATA_CONST.__got: 0x3c8
+  __DATA_CONST.__const: 0xf30
+  __DATA_CONST.__cfstring: 0x59e0
   __DATA_CONST.__objc_classlist: 0x3b0
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x330
-  __DATA_CONST.__objc_intobj: 0x1f8
+  __DATA_CONST.__objc_intobj: 0x210
   __DATA_CONST.__objc_arraydata: 0x13a8
   __DATA_CONST.__objc_dictobj: 0x140
   __DATA_CONST.__objc_arrayobj: 0x438
   __DATA_CONST.__objc_doubleobj: 0x50
-  __DATA.__objc_const: 0xf7b8
-  __DATA.__objc_selrefs: 0x3890
+  __DATA.__objc_const: 0xf7c0
+  __DATA.__objc_selrefs: 0x38f0
   __DATA.__objc_ivar: 0xd18
   __DATA.__objc_data: 0x24e0
   __DATA.__data: 0x720

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FBFF0DF2-7774-3BA7-885E-6F41414EA9D3
-  Functions: 3065
-  Symbols:   252
-  CStrings:  5164
+  UUID: 5EBC1FE2-9D98-3001-B6FF-2FF3D1FBFB4F
+  Functions: 3075
+  Symbols:   255
+  CStrings:  5248
 
Symbols:
+ _NSLocalizedDescriptionKey
+ __os_feature_enabled_impl
+ _dispatch_async
CStrings:
+ "%@-interrupted-%@"
+ "CSPN Session from %@ (predicted until %@), interrupted at %@"
+ "CSPN Session started at %@, interrupted at %@"
+ "CoreSmartPowerNapIPad"
+ "Creating Trial Client for Project %d (fallback/thresholds)"
+ "Creating iPad inactivity predictor"
+ "Entering handle engagement interruption method"
+ "Entering store engagement method"
+ "Extracting thresholds from Trial Namespace %@"
+ "Invalid engagement times: start=%@, end=%@"
+ "Invalid times"
+ "Loading iPad duration model from %{public}@"
+ "Loading iPad engage model from %{public}@"
+ "Reading metadata from loaded models"
+ "Recording engagement from %@ to %@ (interrupted=%d)"
+ "Stored %lu additional parameters from client"
+ "Stored engagement session with %@ model. Total sessions: %lu"
+ "User has enough inactivity history; using two stage ML model for iPhone."
+ "arrayForKey:"
+ "client_%@"
+ "durationModel_iPad.mlmodelc"
+ "durationSeconds"
+ "endTime"
+ "engageModel_iPad.mlmodelc"
+ "engagementSessions"
+ "exclamationmark.circle"
+ "fileExistsAtPath:"
+ "handleEngagementInterruptionFrom:to:withPredictedEnd:"
+ "hasEnoughBatteryDataWithMinimumDays:"
+ "iPad duration model not found at %{public}@, falling back to Trial default"
+ "iPad engage model not found at %{public}@, falling back to Trial default"
+ "iPad using default two stage ML model (feature disabled)."
+ "iPad with CoreSmartPowerNapIPad enabled; using iPad predictor path."
+ "iPadPredictor"
+ "inactivity.iPadPredictor"
+ "initForIPad"
+ "interrupted"
+ "loadiPadModels"
+ "postInterruptionNotificationFrom:to:withPredictedEnd:"
+ "powerd"
+ "predictedDurationSeconds"
+ "recordEngagement"
+ "recordEngagementFrom:to:wasInterrupted:withPredictedMetadata:predictedOutput:withAdditionalParameters:withHandler:"
+ "removeObjectsInRange:"
+ "setDateFormat:"
+ "startTime"
+ "storeEngagementSessionFrom:to:wasInterrupted:withOutput:withMetadata:withAdditionalParameters:"
+ "stringByAppendingPathComponent:"
+ "twoStageXGB_iPad"
+ "v60@0:8@16@24B32@36@44@52"
+ "v68@0:8@\"NSDate\"16@\"NSDate\"24B32@\"_OSInactivityPredictorMetadata\"36@\"_OSInactivityPredictorOutput\"44@\"NSDictionary\"52@?<v@?B@\"NSError\">60"
+ "v68@0:8@16@24B32@36@44@52@?60"
+ "wasInterrupted"
+ "yyyy-MM-dd HH:mm:ss"
- "Error getting battery level biome events in firstBatteryLevelDate %@"
- "Oldest battery event at %@, greater than %lu days"
- "User has enough inactivity history; using two stage ML model."
- "com.apple.powerui.smartcharging.mlmodelpredictor.queryBatteryEvents"
- "hasEnoughBatteryDateWithMinimumDays:"

```
