## AppStoreEvalLighthousePlugin

> `/System/Library/PrivateFrameworks/AppleMediaDiscovery.framework/PlugIns/AppStoreEvalLighthousePlugin.appex/AppStoreEvalLighthousePlugin`

```diff

-1.2.17.0.0
-  __TEXT.__text: 0x27080
-  __TEXT.__auth_stubs: 0x330
-  __TEXT.__objc_stubs: 0x2100
-  __TEXT.__objc_methlist: 0x8d8
-  __TEXT.__const: 0x5f8
-  __TEXT.__cstring: 0xfa2
-  __TEXT.__objc_classname: 0x169
-  __TEXT.__objc_methname: 0x2731
-  __TEXT.__objc_methtype: 0x526
+1.2.29.0.0
+  __TEXT.__text: 0x22db8
+  __TEXT.__auth_stubs: 0x310
+  __TEXT.__objc_stubs: 0x1fc0
+  __TEXT.__objc_methlist: 0x880
+  __TEXT.__const: 0x5a0
+  __TEXT.__cstring: 0xd42
+  __TEXT.__objc_classname: 0x13a
+  __TEXT.__objc_methname: 0x264c
+  __TEXT.__objc_methtype: 0x511
   __TEXT.__gcc_except_tab: 0x1e8
-  __TEXT.__oslogstring: 0xf1
-  __TEXT.__unwind_info: 0x228
-  __DATA_CONST.__auth_got: 0x1a8
+  __TEXT.__oslogstring: 0xfe
+  __TEXT.__unwind_info: 0x220
+  __DATA_CONST.__auth_got: 0x198
   __DATA_CONST.__got: 0x40
-  __DATA_CONST.__const: 0xd0
-  __DATA_CONST.__cfstring: 0x1da0
-  __DATA_CONST.__objc_classlist: 0x68
+  __DATA_CONST.__const: 0xa8
+  __DATA_CONST.__cfstring: 0x1aa0
+  __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_classrefs: 0x150
+  __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_intobj: 0x48
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x1720
-  __DATA.__objc_selrefs: 0x8e0
-  __DATA.__objc_classrefs: 0x168
-  __DATA.__objc_superrefs: 0x30
-  __DATA.__objc_ivar: 0x11c
-  __DATA.__objc_data: 0x410
-  __DATA.__data: 0x7a0
+  __DATA.__objc_const: 0x1630
+  __DATA.__objc_selrefs: 0x8a0
+  __DATA.__objc_ivar: 0x120
+  __DATA.__objc_data: 0x370
+  __DATA.__data: 0x6f8
   __DATA.__bss: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreML.framework/CoreML
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/AppStoreEvalLighthouseUtils.framework/AppStoreEvalLighthouseUtils
   - /System/Library/PrivateFrameworks/AppleMediaDiscovery.framework/AppleMediaDiscovery
-  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/Espresso.framework/Espresso
   - /System/Library/PrivateFrameworks/MLRuntime.framework/MLRuntime
   - /System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PrivateFederatedLearning
   - /System/Library/PrivateFrameworks/Trial.framework/Trial
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 185
-  Symbols:   2462
-  CStrings:  724
+  Functions: 178
+  Symbols:   2328
+  CStrings:  689
 
Symbols:
+ -[AMDLighthouseODMLPlugin init]
+ -[AMDLighthouseODMLPlugin setUpForGenericTaskWithClient:outError:]
+ -[AMDLighthouseODMLPlugin setWorker:]
+ -[AMDLighthouseODMLPlugin worker]
+ OBJC_IVAR_$_AMDLighthouseODMLPlugin._worker
+ _OBJC_CLASS_$_AMDLighthouseODMLWorker
+ _objc_msgSend$setModelsURL:
+ _objc_msgSend$setTriExperimentIdentifiers:
+ _objc_msgSend$setUpForGenericTaskWithClient:outError:
+ _objc_msgSend$setWorker:
+ _objc_msgSend$stop
+ _objc_msgSend$worker
+ _unnamed_array_storage.99
- -[AMDHeuristicModelEvaluator computeAndGetMetrics:model:error:errorDomain:dataProvider:metricNames:]
- -[AMDHeuristicModelEvaluator runTask:error:errorDomain:dataProvider:]
- -[AMDHeuristicModelEvaluator taskResultFromDict:]
- -[AMDLighthouseODMLPlugin checkIfModelShouldBeDownloaded:outError:]
- -[AMDLighthouseODMLPlugin gatherMetricsToReturn:withRecipe:withAttachments:outError:]
- -[AMDLighthouseODMLPlugin logAllResultsToCoreAnalyticsOrDeDisco:withLoggingStrategies:outError:]
- -[AMDLighthouseODMLPlugin logDeDiscoResults:outError:]
- -[AMDLighthouseODMLPlugin logMultipleDeDiscoResults:outError:]
- -[AMDLighthouseODMLPlugin logResultToCoreAnalytics:withMetric:withValue:]
- -[AMDLighthouseODMLPlugin performGenericTask:outError:]
- /Library/Caches/com.apple.xbs/Binaries/AppleMediaDiscoveryFramework/install/TempContent/Objects/AppleMediaDiscoveryFramework.build/AppStoreEvalLighthousePlugin.build/Objects-normal/arm64e/AMDHeuristicModelEvaluator.o
- AMDHeuristicModelEvaluator.m
- _AnalyticsSendEventLazy
- _CoreAnalytics
- _CoreAnalyticsEventName
- _CoreMLTrainerShouldNotUseHeuristicModelError
- _DataContentTypes
- _DataPostProcessing
- _DataProcessingAndModelTraining
- _DataProcessingToCheckIfDownloadModel
- _DataToUpload
- _DeDisco
- _DeDiscoEncodingHasMetricNotAvailableInMetricsError
- _DeDiscoEncodingReadError
- _DeDiscoEncodingToJSONParseError
- _DeploymentIdKey
- _EncodingPath
- _ExpectedMetricNotOfSizeOne
- _ExperimentIdKey
- _FailedToSubmitToDeDiscoError
- _FailureKey
- _FinalMetricsToCollect
- _IsHeuristicModel
- _LoggingStrategyNotRecognizedError
- _MetricNameKeyForLogging
- _MetricValKeyForLogging
- _MissingDataProcessingAndModelTrainingSectionError
- _MissingExpectedMetricError
- _MissingModelNameKeyError
- _ModelNameKeyForLogging
- _MultipleDeDisco
- _OBJC_CLASS_$_AMDDODMLConstants
- _OBJC_CLASS_$_AMDHeuristicModelEvaluator
- _OBJC_CLASS_$_FedStatsDataEncoder
- _OBJC_CLASS_$_MLRTask
- _OBJC_CLASS_$_MLRTaskParameters
- _OBJC_METACLASS_$_AMDDODMLConstants
- _OBJC_METACLASS_$_AMDHeuristicModelEvaluator
- _PopulationSection
- _TRIExperimentIdentifiersNullError
- _TaskParameters
- _TreatmentIdKey
- __OBJC_$_INSTANCE_METHODS_AMDHeuristicModelEvaluator
- __OBJC_CLASS_RO_$_AMDDODMLConstants
- __OBJC_CLASS_RO_$_AMDHeuristicModelEvaluator
- __OBJC_METACLASS_RO_$_AMDDODMLConstants
- __OBJC_METACLASS_RO_$_AMDHeuristicModelEvaluator
- ___73-[AMDLighthouseODMLPlugin logResultToCoreAnalytics:withMetric:withValue:]_block_invoke
- ___block_descriptor_64_e8_32s40s48s56s_e19_"NSDictionary"8?0ls32l8s40l8s48l8s56l8
- __os_log_debug_impl
- _objc_msgSend$allKeys
- _objc_msgSend$computeAndGetMetrics:model:error:errorDomain:dataProvider:metricNames:
- _objc_msgSend$deploymentId
- _objc_msgSend$encodeDataAndRecord:dataTypeContent:baseKey:errorOut:
- _objc_msgSend$experimentId
- _objc_msgSend$getElementInCoreDictionary:
- _objc_msgSend$initWithParameters:attachments:
- _objc_msgSend$initWithParametersDict:
- _objc_msgSend$logDeDiscoResults:outError:
- _objc_msgSend$logMultipleDeDiscoResults:outError:
- _objc_msgSend$logResultToCoreAnalytics:withMetric:withValue:
- _objc_msgSend$performGenericTask:outError:
- _objc_msgSend$predictionsFromBatch:error:
- _objc_msgSend$resetDataProcessorWithRecipe:
- _objc_msgSend$setElementsInCoreDictionary:
- _objc_msgSend$treatmentId
- _unnamed_array_storage.118
CStrings:
+ "@\"AMDLighthouseODMLWorker\""
+ "Encountered error when setting up for generic task: %@"
+ "T@\"AMDLighthouseODMLWorker\",&,N,V_worker"
+ "T@\"NSString\",?,R,C"
+ "_worker"
+ "setModelsURL:"
+ "setTriExperimentIdentifiers:"
+ "setUpForGenericTaskWithClient:outError:"
+ "setWorker:"
+ "worker"
- "\x06"
- "@\"NSDictionary\"8@?0"
- "@48@0:8@16@24@32^@40"
- "@64@0:8q16@24^@32@40@48@56"
- "AMDDODMLConstants"
- "AMDHeuristicModelEvaluator"
- "CoreAnalytics"
- "DataPostProcessing"
- "DataProcessingAndModelTraining"
- "DataProcessingToCheckIfDownloadModel"
- "DataToUpload"
- "DeDisco"
- "Failed to submit to dedisco. Error is %@"
- "FinalMetricsToCollect"
- "IsHeuristicModel"
- "MultipleDeDisco"
- "PopulationSection"
- "TaskParameters"
- "allKeys"
- "baseKeyWithTrialInfo: %@"
- "com.apple.ampaiml.AppleMediaDiscoveryFrameworkLighthousePlugin:%@:%@:%@"
- "com.apple.ampaiml.AppleMediaDiscoveryFrameworkLighthousePlugin:%@:%@:%@:%@"
- "com.apple.ampaiml.AppleMediaDiscoveryLighthousePlugin.ModelEvaluationResult"
- "computeAndGetMetrics:model:error:errorDomain:dataProvider:metricNames:"
- "dataContentTypes"
- "dataToUpload: %@"
- "deploymentId"
- "encodeDataAndRecord:dataTypeContent:baseKey:errorOut:"
- "experimentId"
- "fail"
- "initWithParameters:attachments:"
- "initWithParametersDict:"
- "logDeDiscoResults:outError:"
- "logMultipleDeDiscoResults:outError:"
- "logResultToCoreAnalytics:withMetric:withValue:"
- "metricName"
- "metricValue"
- "modelName"
- "models/encoding.json"
- "performGenericTask:outError:"
- "predictionsFromBatch:error:"
- "treatmentId"

```
