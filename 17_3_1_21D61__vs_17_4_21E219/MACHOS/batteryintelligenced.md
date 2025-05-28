## batteryintelligenced

> `/usr/libexec/batteryintelligenced`

```diff

-31.60.2.0.0
-  __TEXT.__text: 0xf8bc
-  __TEXT.__auth_stubs: 0x540
-  __TEXT.__objc_stubs: 0x18e0
-  __TEXT.__objc_methlist: 0x1264
-  __TEXT.__objc_methname: 0x1c4c
-  __TEXT.__oslogstring: 0x11bf
-  __TEXT.__cstring: 0x879
-  __TEXT.__objc_classname: 0x138
-  __TEXT.__objc_methtype: 0x3d7
+31.100.4.0.0
+  __TEXT.__text: 0x135d8
+  __TEXT.__auth_stubs: 0x5c0
+  __TEXT.__objc_stubs: 0x1ae0
+  __TEXT.__objc_methlist: 0x16bc
+  __TEXT.__cstring: 0x9fd
+  __TEXT.__objc_classname: 0x1b5
+  __TEXT.__objc_methname: 0x1f9b
+  __TEXT.__objc_methtype: 0x4ca
+  __TEXT.__oslogstring: 0x127f
   __TEXT.__const: 0x58
-  __TEXT.__gcc_except_tab: 0xd0
-  __TEXT.__unwind_info: 0x2b4
-  __DATA_CONST.__auth_got: 0x2b0
+  __TEXT.__gcc_except_tab: 0xf8
+  __TEXT.__unwind_info: 0x378
+  __DATA_CONST.__auth_got: 0x2f0
   __DATA_CONST.__got: 0x80
-  __DATA_CONST.__const: 0x418
-  __DATA_CONST.__cfstring: 0xea0
-  __DATA_CONST.__objc_classlist: 0x78
-  __DATA_CONST.__objc_protolist: 0x8
+  __DATA_CONST.__const: 0x4e8
+  __DATA_CONST.__cfstring: 0xfc0
+  __DATA_CONST.__objc_classlist: 0xa0
+  __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_arraydata: 0x590
-  __DATA_CONST.__objc_arrayobj: 0x168
-  __DATA_CONST.__objc_intobj: 0x1c8
-  __DATA_CONST.__objc_doubleobj: 0x30
-  __DATA.__objc_const: 0x2900
-  __DATA.__objc_selrefs: 0x838
-  __DATA.__objc_classrefs: 0x150
-  __DATA.__objc_superrefs: 0x78
-  __DATA.__objc_ivar: 0x2a8
-  __DATA.__objc_data: 0x4b0
-  __DATA.__data: 0x60
-  __DATA.__bss: 0x68
+  __DATA_CONST.__objc_classrefs: 0x180
+  __DATA_CONST.__objc_superrefs: 0x90
+  __DATA_CONST.__objc_intobj: 0x2a0
+  __DATA_CONST.__objc_arraydata: 0x5e8
+  __DATA_CONST.__objc_arrayobj: 0x1b0
+  __DATA_CONST.__objc_doubleobj: 0x90
+  __DATA.__objc_const: 0x4238
+  __DATA.__objc_selrefs: 0x8c8
+  __DATA.__objc_ivar: 0x308
+  __DATA.__objc_data: 0x640
+  __DATA.__data: 0x120
+  __DATA.__bss: 0xc8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreML.framework/CoreML
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 531
-  Symbols:   141
-  CStrings:  740
+  Functions: 667
+  Symbols:   150
+  CStrings:  838
 
Symbols:
+ _IOPSGetPercentRemaining
+ _IOPSGetYearAndWeekOfManufactureFromBatterySerial
+ _OBJC_CLASS_$_MLMultiArray
+ _dispatch_after
+ _dispatch_async
+ _dispatch_time
+ _notify_cancel
+ _notify_get_state
+ _notify_is_valid_token
+ _notify_register_check
+ _notify_register_dispatch
- _objc_retainAutorelease
- _objc_retain_x26
CStrings:
+ "\x02"
+ "\x04"
+ "\x11\x13"
+ "#16@0:8"
+ "(subsystem == 'BatteryDataCollection' AND category == 'BDC_SBC' AND IsCharging==True)"
+ "@\"NSString\"16@0:8"
+ "@24@0:8:16"
+ "@32@0:8:16@24"
+ "@40@0:8:16@24@32"
+ "@40@0:8@16@24q32"
+ "Aborting inference: %u %u %u"
+ "B24@0:8#16"
+ "B24@0:8:16"
+ "B24@0:8@\"Protocol\"16"
+ "B24@0:8@16"
+ "BIDeltaPredictorCommon"
+ "BIMetricRecorder"
+ "BINccpDeltaPredictor"
+ "BIPredictorProtocol"
+ "BIQmaxpDeltaPredictor"
+ "BIWraDeltaPredictor"
+ "Connected state %u unchanged"
+ "Connected state changed to %u"
+ "DUMMY"
+ "Error %d registering for %s notification"
+ "Failed at reading metadata for %@"
+ "Failed at reading predicted feature name for %@"
+ "Failed to create Global FeatureGen"
+ "Fetched yww from IOKit: %@"
+ "Identity"
+ "Invalid registration token for kIOPSNotifyTimeRemaining"
+ "IsCharging"
+ "LastConnectedState"
+ "Most-recent one: %@"
+ "NSObject"
+ "Nil enumerator for BDC_SBC"
+ "Not enough history to make prediction; only received %d rows"
+ "Predicting TT80 using model %@"
+ "Problems creating TT80Model"
+ "Q16@0:8"
+ "Received %@ rows"
+ "T#,R"
+ "T@\"NSObject<OS_os_log>\",&,N,V_logger"
+ "T@\"NSString\",&,N,V_name"
+ "T@\"NSString\",&,N,V_predictedFeatureName"
+ "T@\"NSString\",&,N,V_version"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",R,C"
+ "T@\"NSString\",R,N"
+ "TB,N,V_logToCoreAnalytics"
+ "TB,N,V_logToPPS"
+ "TQ,R"
+ "TT80 prediction: %@"
+ "TimeTo80Estimator"
+ "TimeTo80Model"
+ "Tq,N,V_outputFeatureType"
+ "Unable to create TT80Model"
+ "Unable to get year and week from IOPSGetYearAndWeekOfManufactureFromBatterySerial"
+ "Voltage"
+ "Vv16@0:8"
+ "^{_NSZone=}16@0:8"
+ "_copyFeaturesWithParams:modelName:error:"
+ "_logToCoreAnalytics"
+ "_logToPPS"
+ "autorelease"
+ "bimodeldeltapredictorcommon"
+ "class"
+ "com.apple.batteryintelligence.collectionqueue"
+ "com.apple.system.powersources.source"
+ "com.apple.system.powersources.timeremaining"
+ "conformsToProtocol:"
+ "debugDescription"
+ "description"
+ "distantPast"
+ "getPayloadForCoreAnalyticsWithParams:"
+ "getPayloadForPPSWithParams:andFeatureValue:"
+ "hash"
+ "initWithMetrics:predicate:timeFilter:limitCount:offsetCount:readDirection:"
+ "initWithName:"
+ "initWithShape:dataType:error:"
+ "isKindOfClass:"
+ "isMemberOfClass:"
+ "isProxy"
+ "logToCoreAnalytics"
+ "logToPPS"
+ "logger"
+ "metricValueForKey:"
+ "metricrecorder"
+ "minTimeSteps"
+ "nccpdeltapredictor"
+ "numberWithInteger:"
+ "numberWithUnsignedChar:"
+ "numberWithUnsignedInteger:"
+ "outputFeatureType"
+ "performSelector:"
+ "performSelector:withObject:"
+ "performSelector:withObject:withObject:"
+ "predict:"
+ "predictAndRecordWithParams:"
+ "q16@0:8"
+ "qmaxpdeltapredictor"
+ "release"
+ "respondsToSelector:"
+ "retain"
+ "retainCount"
+ "runInferenceForModel:withParams:outputFeatureType:"
+ "sbc_in"
+ "self"
+ "sendToCoreAnalytics:forEvent:"
+ "sendToPPS:forIdentifier:"
+ "setLogToCoreAnalytics:"
+ "setLogToPPS:"
+ "setLogger:"
+ "setName:"
+ "setObject:forKey:"
+ "setOutputFeatureType:"
+ "setPredictedFeatureName:"
+ "setVersion:"
+ "sharedInstance"
+ "sharedPredictor"
+ "superclass"
+ "tt80_lstm"
+ "tt80estimator"
+ "tt80listener"
+ "v12@?0i8"
+ "v20@0:8B16"
+ "v24@0:8@\"NSDictionary\"16"
+ "v24@0:8q16"
+ "v32@0:8@16@24"
+ "wradeltapredictor"
+ "zone"
- "\x01\x14"
- "\x03"
- "%@ model added"
- "BIModelContainer"
- "BIModelContainerManager"
- "Design capacity is 0. Unable to calculate NCCP."
- "Design capacity is 0. Unable to calculate QmaxP."
- "Failed to allocate container for model %@"
- "Failed to create _globalFeatureGen"
- "Failed to create _modelDictionary"
- "Failed to create logger"
- "Populating payload for CA. Model name = %@, currentVal = %f, pastBaselineVal = %f, predictedDelta = %@, predictedVal = %f"
- "Running with override params %@"
- "T@\"NSString\",R,N,V_name"
- "T@\"NSString\",R,N,V_predictedFeatureName"
- "Unknown model name %@"
- "Unsupported model name %@."
- "_copyFeaturesWithParams:error:"
- "_globalFeatureGen"
- "_modelDictionary"
- "bimodelcontainer_%@"
- "bimodelcontainermanager"
- "containsObject:"
- "copySupportedModels"
- "getModelByName:"
- "getPayloadForCoreAnalytics:withParams:"
- "getPayloadForPPS:withParams:andFeatureValue:"
- "initWithModelName:featureGenerator:"
- "runDeltaModelsWithParams:"
- "runInferenceWithParams:"
- "sendToCoreAnalytics:"
- "sendToPPS:"
- "sharedModelContainerManager"

```
