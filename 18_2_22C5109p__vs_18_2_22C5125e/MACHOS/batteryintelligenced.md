## batteryintelligenced

> `/usr/libexec/batteryintelligenced`

```diff

-97.0.0.0.0
-  __TEXT.__text: 0x1f0b0
-  __TEXT.__auth_stubs: 0x780
-  __TEXT.__objc_stubs: 0x2640
-  __TEXT.__objc_methlist: 0x11b0
-  __TEXT.__cstring: 0x17d6
-  __TEXT.__objc_classname: 0x2d7
-  __TEXT.__objc_methtype: 0x54a
+97.60.7.0.0
+  __TEXT.__text: 0x1ff30
+  __TEXT.__auth_stubs: 0x790
+  __TEXT.__objc_stubs: 0x2880
+  __TEXT.__objc_methlist: 0x1290
+  __TEXT.__cstring: 0x18cb
+  __TEXT.__objc_classname: 0x2e9
+  __TEXT.__objc_methtype: 0x5b2
   __TEXT.__const: 0x1d8
-  __TEXT.__oslogstring: 0x3035
-  __TEXT.__objc_methname: 0x2f49
+  __TEXT.__oslogstring: 0x33b4
+  __TEXT.__objc_methname: 0x32a8
   __TEXT.__gcc_except_tab: 0x184
-  __TEXT.__unwind_info: 0x500
-  __DATA_CONST.__auth_got: 0x3d0
-  __DATA_CONST.__got: 0x1c0
-  __DATA_CONST.__const: 0x708
-  __DATA_CONST.__cfstring: 0x2020
-  __DATA_CONST.__objc_classlist: 0xe8
+  __TEXT.__unwind_info: 0x510
+  __DATA_CONST.__auth_got: 0x3d8
+  __DATA_CONST.__got: 0x1d0
+  __DATA_CONST.__const: 0x768
+  __DATA_CONST.__cfstring: 0x20a0
+  __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0xc8
-  __DATA_CONST.__objc_arraydata: 0x390
-  __DATA_CONST.__objc_arrayobj: 0x2a0
-  __DATA_CONST.__objc_intobj: 0x5a0
+  __DATA_CONST.__objc_superrefs: 0xd0
+  __DATA_CONST.__objc_arraydata: 0x378
+  __DATA_CONST.__objc_arrayobj: 0x288
+  __DATA_CONST.__objc_intobj: 0x570
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA.__objc_const: 0x3b88
-  __DATA.__objc_selrefs: 0xb00
-  __DATA.__objc_ivar: 0x1a8
-  __DATA.__objc_data: 0x910
+  __DATA.__objc_const: 0x3d48
+  __DATA.__objc_selrefs: 0xbd0
+  __DATA.__objc_ivar: 0x1c0
+  __DATA.__objc_data: 0x960
   __DATA.__data: 0x188
-  __DATA.__bss: 0x150
+  __DATA.__bss: 0x160
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreML.framework/CoreML
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/CoreDuetContext.framework/CoreDuetContext
   - /System/Library/PrivateFrameworks/PerfPowerServicesReader.framework/PerfPowerServicesReader
   - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
+  - /System/Library/PrivateFrameworks/Trial.framework/Trial
+  - /System/Library/PrivateFrameworks/TrialProto.framework/TrialProto
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 592
-  Symbols:   190
-  CStrings:  1243
+  Functions: 618
+  Symbols:   193
+  CStrings:  1310
 
Symbols:
+ _OBJC_CLASS_$_TRIClient
+ _OBJC_CLASS_$_TRINamespace
+ _notify_post
+ _objc_setProperty_atomic
- _dispatch_async
CStrings:
+ "\x11\x14"
+ "@\"BITrialManager\""
+ "@\"TRIClient\""
+ "@\"TRIExperimentIdentifiers\""
+ "@\"TRITrackingId\""
+ "@20@0:8I16"
+ "BITrialManager"
+ "Event epoch timestamp(%!@(MISSING)) is prior to recorded plugin timestamp(%!@(MISSING)) within the listener. Not computing metrics for event #%!@(MISSING): %!@(MISSING)"
+ "Failed to load experiment identifiers. Returning nil."
+ "Failed to load model from %!@(MISSING) with error: %!@(MISSING)"
+ "Feature flag disabled: Not posting notification"
+ "Found nil objects/incorrect timestamp within PPS Event. Not computing metrics for event #%!@(MISSING): %!@(MISSING)"
+ "Loading ML model with factor name: %!@(MISSING) from trial."
+ "Loading compiled model from %!@(MISSING)"
+ "Posted notification for estimate changed"
+ "Request to load model from path: %!@(MISSING) "
+ "SOC value of %!z(MISSING)d is < 0"
+ "SOC value of %!z(MISSING)d is > 100"
+ "Successfully loaded compiled model."
+ "T@\"BITrialManager\",&,N,V_trialManager"
+ "T@\"NSString\",&,N,V_trialNamespaceName"
+ "T@\"TRIClient\",&,N,V_trialClient"
+ "T@\"TRIExperimentIdentifiers\",&,V_experimentIdentifiers"
+ "T@\"TRITrackingId\",&,V_trialTrackingID"
+ "Trial Client %!@(MISSING)"
+ "Unable to load ML model from trial. Loading default model for %!@(MISSING)."
+ "Unable to load from null path."
+ "Updating payload for CA with trial parameters."
+ "_experimentIdentifiers"
+ "_trialClient"
+ "_trialManager"
+ "_trialNamespaceName"
+ "_trialTrackingID"
+ "bhfModel"
+ "clientWithIdentifier:"
+ "com.apple.batteryintelligence.ChargeEstimateChanged"
+ "com.apple.batteryintelligence.trialmanager.loadmodel"
+ "com.apple.batteryintelligenced.tt80.connection-update"
+ "com.apple.batteryintelligenced.tt80.model-run"
+ "com.apple.batteryintelligenced.tt80.setup-run"
+ "deploymentId"
+ "directoryValue"
+ "experimentId"
+ "experimentIdentifiers"
+ "experimentIdentifiersWithNamespaceName:"
+ "initWithNamespaceId:"
+ "levelForFactor:withNamespaceName:"
+ "loadCompiledModelFromPath:withConfiguration:"
+ "loadTrialMLModelForModelName:withConfiguration:"
+ "modelID is null. Not computing CA metrics."
+ "namespaceNameFromId:"
+ "path"
+ "postNotificationForChargeTimeEstimateUpdate"
+ "sendToCoreAnalytics:forEvent:withTrialManager:"
+ "setExperimentIdentifiers:"
+ "setTrialClient:"
+ "setTrialManager:"
+ "setTrialNamespaceName:"
+ "setTrialTrackingID:"
+ "startSOCBin is nil. Not computing CA metrics for event #%!@(MISSING): %!@(MISSING)"
+ "stringValue"
+ "timeOfPredictionOffsetBin is nil. Not computing CA metrics for event #%!@(MISSING): %!@(MISSING)"
+ "trackingId"
+ "treatmentId"
+ "trialClient"
+ "trialDeploymentId"
+ "trialExperimentId"
+ "trialFactorLevel:"
+ "trialManager"
+ "trialNamespaceName"
+ "trialTrackingID"
+ "trialTreatmentId"
+ "trialmanager"
+ "v40@0:8@16@24@32"
- "Invalid SOC: %!@(MISSING)"
- "SOC value of %!@(MISSING) is < 0"
- "SOC value of %!@(MISSING) is > 100"
- "com.apple.batteryintelligenced.tt80.checkconnection"
- "getSOCBin"
- "getTimeIntervalBin"
- "sendToCoreAnalytics:forEvent:"

```
