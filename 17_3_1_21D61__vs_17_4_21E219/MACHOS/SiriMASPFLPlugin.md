## SiriMASPFLPlugin

> `/System/Library/ExtensionKit/Extensions/SiriMASPFLPlugin.appex/SiriMASPFLPlugin`

```diff

-4.0.0.0.0
-  __TEXT.__text: 0x13d20
-  __TEXT.__auth_stubs: 0xc60
-  __TEXT.__cstring: 0xb9d
-  __TEXT.__const: 0xe7c
-  __TEXT.__constg_swiftt: 0x44c
-  __TEXT.__swift5_typeref: 0x3d0
-  __TEXT.__swift5_reflstr: 0x5a5
-  __TEXT.__swift5_fieldmd: 0x4c8
-  __TEXT.__objc_methname: 0x2fa
-  __TEXT.__swift5_types: 0x48
-  __TEXT.__objc_classname: 0x12
-  __TEXT.__objc_methtype: 0x47
-  __TEXT.__swift5_proto: 0xd0
-  __TEXT.__swift5_assocty: 0xf0
+6.0.0.0.0
+  __TEXT.__text: 0x2ce0
+  __TEXT.__auth_stubs: 0x4f0
+  __TEXT.__const: 0x13a
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__swift5_capture: 0x30
-  __TEXT.__unwind_info: 0x524
-  __TEXT.__eh_frame: 0x988
-  __DATA_CONST.__auth_got: 0x630
-  __DATA_CONST.__got: 0x148
-  __DATA_CONST.__auth_ptr: 0x28
-  __DATA_CONST.__const: 0xd18
-  __DATA_CONST.__objc_classlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x10
+  __TEXT.__constg_swiftt: 0x28
+  __TEXT.__swift5_typeref: 0xda
+  __TEXT.__swift5_fieldmd: 0x10
+  __TEXT.__swift5_reflstr: 0xe
+  __TEXT.__swift5_assocty: 0x18
+  __TEXT.__cstring: 0x208
+  __TEXT.__objc_methname: 0x12
+  __TEXT.__swift5_proto: 0x8
+  __TEXT.__swift5_types: 0x4
+  __TEXT.__unwind_info: 0x10c
+  __TEXT.__eh_frame: 0x1f0
+  __DATA_CONST.__auth_got: 0x278
+  __DATA_CONST.__got: 0x90
+  __DATA_CONST.__auth_ptr: 0x8
+  __DATA_CONST.__const: 0x198
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x510
-  __DATA.__objc_selrefs: 0x120
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x60
-  __DATA.__data: 0xa30
-  __DATA.__bss: 0x1a10
-  __DATA.__common: 0x18
-  - /System/Library/Frameworks/CoreML.framework/CoreML
+  __DATA.__objc_selrefs: 0x10
+  __DATA.__data: 0x78
+  __DATA.__bss: 0x108
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
-  - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/BiomePubSub.framework/BiomePubSub
-  - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
-  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/LighthouseBackground.framework/LighthouseBackground
   - /System/Library/PrivateFrameworks/MLRuntime.framework/MLRuntime
   - /System/Library/PrivateFrameworks/NightingaleTraining.framework/NightingaleTraining
+  - /System/Library/PrivateFrameworks/SiriMASPFLTraining.framework/SiriMASPFLTraining
   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftSceneKit.dylib
+  - /usr/lib/swift/libswiftShazamKit.dylib
   - /usr/lib/swift/libswiftSpriteKit.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftVision.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 456
-  Symbols:   132
-  CStrings:  131
+  Functions: 45
+  Symbols:   66
+  CStrings:  13
 
Symbols:
+ _SiriMASPFLPluginVersionNumber
+ _SiriMASPFLPluginVersionString
+ __swift_FORCE_LOAD_$_swiftShazamKit
- _AnalyticsSendEventLazy
- _BiomeLibrary
- _OBJC_CLASS_$_BMPublisherOptions
- _OBJC_CLASS_$_BMSQLDatabase
- _OBJC_CLASS_$_MLArrayBatchProvider
- _OBJC_CLASS_$_MLDictionaryFeatureProvider
- _OBJC_CLASS_$_MLModel
- _OBJC_CLASS_$_MLModelConfiguration
- _OBJC_CLASS_$_MLMultiArray
- _OBJC_CLASS_$_MLProgramTrainer
- _OBJC_CLASS_$_MLRTaskResult
- _OBJC_CLASS_$_NSJSONSerialization
- _OBJC_CLASS_$_NSNumber
- _OBJC_CLASS_$_NSObject
- _OBJC_CLASS_$__TtCs12_SwiftObject
- _OBJC_METACLASS_$__TtCs12_SwiftObject
- __Block_copy
- __Block_release
- __NSConcreteStackBlock
- ___stack_chk_fail
- ___stack_chk_guard
- __objc_empty_cache
- __os_log_impl
- __swift_stdlib_bridgeErrorToNSError
- _malloc_size
- _memcpy
- _objc_autoreleaseReturnValue
- _objc_opt_self
- _objc_release
- _objc_release_x19
- _objc_release_x20
- _objc_release_x21
- _objc_release_x22
- _objc_release_x23
- _objc_release_x24
- _objc_release_x25
- _objc_release_x26
- _objc_retain_x19
- _objc_retain_x20
- _objc_retain_x24
- _objc_retain_x8
- _os_log_type_enabled
- _swift_allocError
- _swift_allocateGenericClassMetadata
- _swift_arrayDestroy
- _swift_arrayInitWithCopy
- _swift_beginAccess
- _swift_bridgeObjectRelease_n
- _swift_bridgeObjectRetain_n
- _swift_deallocClassInstance
- _swift_deallocObject
- _swift_deallocPartialClassInstance
- _swift_deletedMethodError
- _swift_endAccess
- _swift_getGenericMetadata
- _swift_getObjCClassFromMetadata
- _swift_getObjCClassMetadata
- _swift_getObjectType
- _swift_getTypeByMangledNameInContextInMetadataState2
- _swift_initClassMetadata2
- _swift_initStaticObject
- _swift_isUniquelyReferenced_nonNull_bridgeObject
- _swift_once
- _swift_retain_n
- _swift_slowAlloc
- _swift_slowDealloc
- _swift_unknownObjectRelease
- _swift_unknownObjectRetain
- _swift_willThrow
CStrings:
- "@\"MLFeatureValue\"24@0:8@\"NSString\"16"
- "@\"NSDictionary\"8@?0"
- "@\"NSSet\"16@0:8"
- "@16@0:8"
- "@24@0:8@16"
- "Aggregating SQL rows."
- "AppSelection"
- "Baseline"
- "Baseline/Trained metric value not found for %s"
- "BatchGroupingFeature"
- "Couldn't find %s value in %s"
- "Couldn't find feature value for %s"
- "Couldn't form SiriMASPFLPluginArgs: %@"
- "Error executing %s in Biome: %@"
- "Error forming MLBatchProvider: %@"
- "Error in fetching row: %@"
- "Evaluation metrics are nil."
- "Executing SQL query."
- "Feature value not scalar: %@"
- "FeatureBiomeSqlQuery"
- "FeatureCount"
- "FeatureNames"
- "Finished initialising SiriMASPFLPluginRunner."
- "Finishing plugin by returning %ld metrics and weight delta."
- "Initialising SiriMASPFLPluginRunner for recipe %s."
- "Initializing training data for aggregating value %ld"
- "Invalid feature value %@"
- "LearningRate"
- "ML program trainer init failed for %s: %@"
- "MLFeatureProvider"
- "MaximumNumEvents"
- "MetadataMetricName"
- "MetricEncoding"
- "MetricEvaluationType"
- "MinimumNumEvents"
- "Mismatch in number of columns in trainingData %ld and number of features in arg %ld"
- "Model attachment not found"
- "Model init failed for %s with error: %@"
- "ModelEvaluationMetricSpecs"
- "ModelInputName"
- "ModelLabelName"
- "ModelMetricName"
- "ModelName"
- "Music"
- "No Biome datapoints found, returning empty MLRTaskResult"
- "No ML program found for %s"
- "NumLocalIterations"
- "Producing MLBatchProvider for training."
- "Row cannot be converted into SiriPrivateLearningPFLBiomeSQLRow"
- "Scalar"
- "Siri"
- "SiriMASPFLPlugin"
- "Size of featureNames (%ld is not equal to featureCount (%u"
- "T@\"NSSet\",R,N"
- "TargetFeature"
- "Trained"
- "Training %ld for %u epochs."
- "Training model %s with %ld datapoints for %u epochs."
- "Unable to convert value for %s to float"
- "_TtC16SiriMASPFLPlugin12ModelTrainer"
- "_TtC16SiriMASPFLPlugin14BiomeSQLClient"
- "_TtC16SiriMASPFLPlugin21BiomeSQLRowAggregator"
- "_TtC16SiriMASPFLPlugin22SiriMASPFLPluginRunner"
- "aggregatingColumnName"
- "aggregatingValue not found."
- "args"
- "biomeSQLClient"
- "biomeSQLRowAggregator"
- "com.apple.priml.PFLMLHostPlugins"
- "com.apple.priml.PFLPluginReach"
- "copyCurrentTrainingDelta"
- "count"
- "dataWithJSONObject:options:error:"
- "doubleValue"
- "error"
- "evaluateUsingTestData:evaluationMetricNames:error:"
- "evaluationMetrics"
- "featureNames"
- "featureValueForName:"
- "featuresAtIndex:"
- "flattenedModelUpdate"
- "floatValue"
- "init"
- "initWithDataPointer:shape:dataType:strides:deallocator:error:"
- "initWithDictionary:error:"
- "initWithFeatureProviderArray:"
- "initWithJSONResult:unprivatizedVector:"
- "initWithProgram:learningRate:error:"
- "initWithStartDate:endDate:maxEvents:lastN:reversed:"
- "inputMLArrayKey"
- "inputMatrix"
- "int64Value"
- "labelFeatureName"
- "m"
- "modelTrainer"
- "modelWithContentsOfURL:configuration:error:"
- "multiArrayValue"
- "n"
- "next"
- "objectAtIndexedSubscript:"
- "outputMLArrayKey"
- "outputVector"
- "program"
- "programTrainer"
- "publisherWithOptions:"
- "queryResultSet"
- "row"
- "rowMajor"
- "setComputeUnits:"
- "sinkWithCompletion:receiveInput:"
- "sqlDb"
- "trainUsingTrainingData:error:"
- "trainingDataForAggregatingValue"
- "type"
- "v16@?0@\"BPSCompletion\"8"
- "v16@?0@8"
- "v16@?0^v8"

```
