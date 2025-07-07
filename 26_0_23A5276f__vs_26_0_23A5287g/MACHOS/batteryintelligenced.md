## batteryintelligenced

> `/usr/libexec/batteryintelligenced`

```diff

-160.0.0.0.0
-  __TEXT.__text: 0x2ccc8
+167.0.0.0.1
+  __TEXT.__text: 0x30424
   __TEXT.__auth_stubs: 0x8b0
-  __TEXT.__objc_stubs: 0x3520
-  __TEXT.__objc_methlist: 0x1ad4
-  __TEXT.__cstring: 0x27e3
-  __TEXT.__objc_classname: 0x419
-  __TEXT.__objc_methtype: 0x755
+  __TEXT.__objc_stubs: 0x3640
+  __TEXT.__objc_methlist: 0x1f94
+  __TEXT.__cstring: 0x2999
+  __TEXT.__objc_classname: 0x5d9
+  __TEXT.__objc_methtype: 0x766
   __TEXT.__const: 0x1f8
-  __TEXT.__oslogstring: 0x503f
-  __TEXT.__objc_methname: 0x4111
-  __TEXT.__gcc_except_tab: 0x260
-  __TEXT.__unwind_info: 0x778
+  __TEXT.__oslogstring: 0x52ae
+  __TEXT.__objc_methname: 0x4295
+  __TEXT.__gcc_except_tab: 0x278
+  __TEXT.__unwind_info: 0x888
   __DATA_CONST.__auth_got: 0x468
   __DATA_CONST.__got: 0x230
-  __DATA_CONST.__const: 0x960
-  __DATA_CONST.__cfstring: 0x2ca0
-  __DATA_CONST.__objc_classlist: 0x128
+  __DATA_CONST.__const: 0x988
+  __DATA_CONST.__cfstring: 0x2ec0
+  __DATA_CONST.__objc_classlist: 0x170
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x108
-  __DATA_CONST.__objc_arraydata: 0x568
-  __DATA_CONST.__objc_arrayobj: 0x3c0
-  __DATA_CONST.__objc_intobj: 0x798
+  __DATA_CONST.__objc_superrefs: 0x150
+  __DATA_CONST.__objc_arraydata: 0x6a0
+  __DATA_CONST.__objc_arrayobj: 0x480
+  __DATA_CONST.__objc_intobj: 0x810
   __DATA_CONST.__objc_doubleobj: 0x40
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x4678
-  __DATA.__objc_selrefs: 0x1038
-  __DATA.__objc_ivar: 0x210
-  __DATA.__objc_data: 0xb90
+  __DATA.__objc_const: 0x5038
+  __DATA.__objc_selrefs: 0x1088
+  __DATA.__objc_ivar: 0x23c
+  __DATA.__objc_data: 0xe60
   __DATA.__data: 0x2e0
-  __DATA.__bss: 0x1b8
+  __DATA.__bss: 0x1c8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreML.framework/CoreML
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BB5A3B5B-20B8-3285-9F0F-7CF47DCAD1CD
-  Functions: 875
+  UUID: 9A71C492-34D0-3054-9503-8E8120BCA81F
+  Functions: 985
   Symbols:   226
-  CStrings:  2096
+  CStrings:  2163
 
CStrings:
+ "%K >= %ld AND %K <= %ld"
+ "6t6qz674si"
+ "@40@0:8q16@24@32"
+ "@48@0:8@16@24@32Q40"
+ "CA metrics already computed for the endSOC: %u"
+ "CA metrics is already computed for the endSOC: %u"
+ "Cannot compute core analytics metrics for invalid end SOC: %@"
+ "Completed computing core analytics metrics for endSOC: %@"
+ "Corrected model path is: %@."
+ "Could not load battery_analysis_tt80_model_6t6qz674si.mlmodelc in the bundle resource"
+ "Could not load battery_analysis_tt80_model_bkwqiw7f79.mlmodelc in the bundle resource"
+ "Could not load battery_analysis_tt80_model_ypt4vmy8c3.mlmodelc in the bundle resource"
+ "Could not load battery_analysis_ttl_model_7ssi6t5tb5.mlmodelc in the bundle resource"
+ "Could not load battery_analysis_ttl_model_k5wmzvi5mm.mlmodelc in the bundle resource"
+ "Could not send data to core analytics for event: %@"
+ "Device reached %@ endSOC within %0.02f seconds"
+ "Device reached %d in %@, First estimate at plugin was %@."
+ "Getting data from PPS for the following inputs:\ndateFrom - %@, dateTill - %@, interval - %@, predicate - %@"
+ "Invalid date range: dateFrom is %.6f seconds after dateTill. From: %@, Till: %@"
+ "Invalid endSOC"
+ "Invalid uiSOC %u within context store information."
+ "Key %@ does not exist in inputDict. Unable to obtain value. Returning"
+ "Loading compiled trial model stored locally from default assets. Original (requested) path: %@"
+ "Prediction date (%@) is outside valid range [%@ to %@]"
+ "Received unexpected value for kIOPMPSAdapterDetailsIsWirelessKey key within adapter details."
+ "Resetting timeSincePlugin and socAtPlugin as currentMonotonicTimeInSeconds < pluginMonotonicTimeInSeconds."
+ "SELF.%@.value.externalConnected = %@ AND SELF.%@.value IN %@"
+ "System/Library/PrivateFrameworks/BatteryIntelligence.framework/assets_BATTERYINTELLIGENCE_BATTERY_ANALYSIS/"
+ "T@\"NSMutableDictionary\",&,N,V_predictedFeatureNames"
+ "T@\"NSNumber\",&,N,V_isAdapterWireless"
+ "Tq,N,V_caMetricsComputedBitMask"
+ "Tq,N,V_socAtPlugin"
+ "Unable to obtain model ID from trial. Defaulting to model version %@ at %@."
+ "Using adjusted endSOC: %@ (+%ld)"
+ "Using adjusted endSOC: %@ (-%ld)"
+ "_caMetricsComputedBitMask"
+ "_isAdapterWireless"
+ "_socAtPlugin"
+ "battAmperage"
+ "battVoltage"
+ "batteryAnalysisModelID"
+ "batteryAnalysisTTLModelID"
+ "battery_analysis_tt80_model_"
+ "battery_analysis_tt80_model_6t6qz674si"
+ "battery_analysis_tt80_model_6t6qz674siInput"
+ "battery_analysis_tt80_model_6t6qz674siOutput"
+ "battery_analysis_tt80_model_bkwqiw7f79"
+ "battery_analysis_tt80_model_bkwqiw7f79Input"
+ "battery_analysis_tt80_model_bkwqiw7f79Output"
+ "battery_analysis_tt80_model_ypt4vmy8c3"
+ "battery_analysis_tt80_model_ypt4vmy8c3Input"
+ "battery_analysis_tt80_model_ypt4vmy8c3Output"
+ "battery_analysis_ttl_model_"
+ "battery_analysis_ttl_model_7ssi6t5tb5"
+ "battery_analysis_ttl_model_7ssi6t5tb5Input"
+ "battery_analysis_ttl_model_7ssi6t5tb5Output"
+ "battery_analysis_ttl_model_k5wmzvi5mm"
+ "battery_analysis_ttl_model_k5wmzvi5mmInput"
+ "battery_analysis_ttl_model_k5wmzvi5mmOutput"
+ "caMetricsComputedBitMask"
+ "com.apple.bi.battery_analysis"
+ "computeAndSendCoreAnalyticsMetricsForEndSOC:"
+ "curr_batt_voltage"
+ "endSOCEnumMapping"
+ "end_soc_enum"
+ "enumForEndSOC:"
+ "estimateForTarget:withFeatures:andModelDict:"
+ "getBatteryAnalysisEstimatesFromDate:toDate:predicate:limit:"
+ "iOS version is not supported to fetch PPS data."
+ "isAdapterWireless"
+ "isUnsupportedModelVersion:"
+ "isWirelessAdapter"
+ "k5wmzvi5mm"
+ "modelDict is empty"
+ "modelVersionForTarget:fromTrial:"
+ "original_session_start_soc"
+ "q24@0:8@16"
+ "setCaMetricsComputedBitMask:"
+ "setIsAdapterWireless:"
+ "setSocAtPlugin:"
+ "socAtPlugin"
+ "socAtPlugin was not provided."
+ "stringByAppendingPathComponent:"
+ "stringByAppendingPathExtension:"
+ "stringByAppendingString:"
+ "stringByDeletingLastPathComponent"
+ "stringByDeletingPathExtension"
+ "uiSOC at disconnect: %u"
- " com.apple.bi.battery_analysis"
- "(subsystem == %@ AND category == %@)"
- "@32@0:8q16@24"
- "@40@0:8@16@24Q32"
- "Can compute core analytics metrics."
- "Can not compute core analytics metrics."
- "Cannot compute core analytics metrics as we do not know plugin time: pluginMonotonicTimeInSeconds - %llu"
- "Completed computing core analytics metrics."
- "Core analytics metrics have been computed once for the current charging session.\n"
- "Could not load battery_analysis_tt80_model.mlmodelc in the bundle resource"
- "Could not load battery_analysis_ttl_model.mlmodelc in the bundle resource"
- "Device reached %d in %@, TT80 estimate at plugin was %@."
- "Device reached to 80 SOC within %f seconds"
- "Event epoch timestamp(%@) is prior to recorded plugin timestamp(%@) within the listener. Not computing metrics for event #%@: %@"
- "ExperimentIdentifiers: %@"
- "Failed to load ML model for target: %@."
- "Failed to load experiment identifiers. Returning nil."
- "Getting data from PPS for the following inputs:\ndateFrom - %@, dateTill - %@, interval - %@"
- "Loading default model for %@."
- "Resetting timeSincePlugin as currentMonotonicTimeInSeconds < pluginMonotonicTimeInSeconds."
- "SELF.%@.value.externalConnected = %@ AND SELF.%@.value = %@"
- "T@\"NSDictionary\",&,N,V_predictedFeatureNames"
- "TB,N,V_caMetricsComputed"
- "Trial Client %@"
- "Unable to compute the core analytics metrics as SMC data is not available."
- "Unable to load ML model from trial"
- "_caMetricsComputed"
- "batteryAnalysisModel"
- "battery_analysis_tt80_model"
- "battery_analysis_tt80_modelInput"
- "battery_analysis_tt80_modelOutput"
- "battery_analysis_ttl_model"
- "battery_analysis_ttl_modelInput"
- "battery_analysis_ttl_modelOutput"
- "caMetricsComputed"
- "canComputeCoreAnalyticsMetrics"
- "com.apple.batteryintelligence.trialmanager.loadmodel"
- "computeAndSendCoreAnalyticsMetrics"
- "estimateForTarget:withFeatures:"
- "experimentIdentifiersWithNamespaceName:"
- "getBatteryAnalysisEstimatesFromDate:toDate:limit:"
- "setCaMetricsComputed:"
- "trackingId"

```
