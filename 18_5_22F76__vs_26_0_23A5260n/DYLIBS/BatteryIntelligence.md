## BatteryIntelligence

> `/System/Library/PrivateFrameworks/BatteryIntelligence.framework/BatteryIntelligence`

```diff

-97.120.2.0.0
-  __TEXT.__text: 0x518
-  __TEXT.__auth_stubs: 0x130
-  __TEXT.__objc_methlist: 0x140
-  __TEXT.__const: 0x50
-  __TEXT.__cstring: 0x116
-  __TEXT.__oslogstring: 0x1d
-  __TEXT.__unwind_info: 0x90
-  __TEXT.__objc_classname: 0x52
-  __TEXT.__objc_methname: 0x221
-  __TEXT.__objc_methtype: 0x97
-  __TEXT.__objc_stubs: 0x120
-  __DATA_CONST.__got: 0x20
-  __DATA_CONST.__const: 0x28
-  __DATA_CONST.__objc_classlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x10
+155.0.0.502.2
+  __TEXT.__text: 0x4e00
+  __TEXT.__auth_stubs: 0x440
+  __TEXT.__objc_methlist: 0x7c4
+  __TEXT.__const: 0xa0
+  __TEXT.__cstring: 0x5fa
+  __TEXT.__oslogstring: 0x3ed
+  __TEXT.__gcc_except_tab: 0x264
+  __TEXT.__unwind_info: 0x248
+  __TEXT.__objc_classname: 0x1ba
+  __TEXT.__objc_methname: 0x10e2
+  __TEXT.__objc_methtype: 0x36e
+  __TEXT.__objc_stubs: 0xd80
+  __DATA_CONST.__got: 0xd8
+  __DATA_CONST.__const: 0x1c0
+  __DATA_CONST.__objc_classlist: 0x58
+  __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb8
-  __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0xa0
-  __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__cfstring: 0xa0
-  __AUTH_CONST.__objc_const: 0x2a8
-  __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x14
-  __DATA.__data: 0xc0
-  __DATA.__bss: 0x20
+  __DATA_CONST.__objc_selrefs: 0x510
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_superrefs: 0x48
+  __DATA_CONST.__objc_arraydata: 0x10
+  __AUTH_CONST.__auth_got: 0x230
+  __AUTH_CONST.__const: 0xc0
+  __AUTH_CONST.__cfstring: 0x400
+  __AUTH_CONST.__objc_const: 0x1308
+  __AUTH_CONST.__objc_intobj: 0x30
+  __AUTH_CONST.__objc_arrayobj: 0x30
+  __AUTH.__objc_data: 0x1e0
+  __DATA.__objc_ivar: 0x78
+  __DATA.__data: 0x240
+  __DATA.__bss: 0x30
+  __DATA_DIRTY.__objc_data: 0x190
+  __DATA_DIRTY.__bss: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CoreML.framework/CoreML
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3D5D1FCE-FA2E-348E-8370-73F19A0A292E
-  Functions: 25
-  Symbols:   129
-  CStrings:  68
+  UUID: DEC22E48-BA90-342F-BA08-1F39F729747D
+  Functions: 178
+  Symbols:   782
+  CStrings:  391
 
Symbols:
+ +[BIBatteryAnalysisContainer supportsSecureCoding]
+ +[BIBatteryAnalysisOutput supportsSecureCoding]
+ +[BIBatteryAnalysisSharedResources areTargetsValid:]
+ +[BIBatteryAnalysisSharedResources getLocalizedStringForKey:]
+ +[BIBatteryAnalysisSharedResources isTargetValid:]
+ +[BIBatteryAnalysisSharedResources sharedTargetDetails]
+ +[BIBatteryAnalysisSharedResources sharedTargetDetails].cold.1
+ +[battery_analysis_tt80_model URLOfModelInThisBundle]
+ +[battery_analysis_tt80_model URLOfModelInThisBundle].cold.1
+ +[battery_analysis_tt80_model loadContentsOfURL:configuration:completionHandler:]
+ +[battery_analysis_tt80_model loadWithConfiguration:completionHandler:]
+ -[BIBatteryAnalysisClient .cxx_destruct]
+ -[BIBatteryAnalysisClient connection]
+ -[BIBatteryAnalysisClient dealloc]
+ -[BIBatteryAnalysisClient delegate]
+ -[BIBatteryAnalysisClient estimateForTarget:withError:]
+ -[BIBatteryAnalysisClient estimateForTarget:withError:].cold.1
+ -[BIBatteryAnalysisClient estimateForTarget:withError:].cold.2
+ -[BIBatteryAnalysisClient estimateFromCache:withError:]
+ -[BIBatteryAnalysisClient estimateFromCache:withError:].cold.1
+ -[BIBatteryAnalysisClient formattedEstimateForOutput:withTarget:]
+ -[BIBatteryAnalysisClient initWithTargets:]
+ -[BIBatteryAnalysisClient initWithTargets:].cold.1
+ -[BIBatteryAnalysisClient initWithTargets:].cold.2
+ -[BIBatteryAnalysisClient initWithTargets:].cold.3
+ -[BIBatteryAnalysisClient logger]
+ -[BIBatteryAnalysisClient notificationTokens]
+ -[BIBatteryAnalysisClient queue]
+ -[BIBatteryAnalysisClient registerForUpdatesToTarget:]
+ -[BIBatteryAnalysisClient registerForUpdatesToTarget:].cold.1
+ -[BIBatteryAnalysisClient setConnection:]
+ -[BIBatteryAnalysisClient setDelegate:]
+ -[BIBatteryAnalysisClient setLogger:]
+ -[BIBatteryAnalysisClient setNotificationTokens:]
+ -[BIBatteryAnalysisClient setQueue:]
+ -[BIBatteryAnalysisClient setTargetOutputs:]
+ -[BIBatteryAnalysisClient setTargets:]
+ -[BIBatteryAnalysisClient targetOutputs]
+ -[BIBatteryAnalysisClient targets]
+ -[BIBatteryAnalysisClient updateEstimateForTarget:]
+ -[BIBatteryAnalysisContainer .cxx_destruct]
+ -[BIBatteryAnalysisContainer description]
+ -[BIBatteryAnalysisContainer encodeWithCoder:]
+ -[BIBatteryAnalysisContainer error]
+ -[BIBatteryAnalysisContainer estimateObj]
+ -[BIBatteryAnalysisContainer initWithCoder:]
+ -[BIBatteryAnalysisContainer lastUpdatedMonotonicTime]
+ -[BIBatteryAnalysisContainer setError:]
+ -[BIBatteryAnalysisContainer setEstimateObj:]
+ -[BIBatteryAnalysisContainer setLastUpdatedMonotonicTime:]
+ -[BIBatteryAnalysisManagerClient .cxx_destruct]
+ -[BIBatteryAnalysisManagerClient adHocRunWithError:]
+ -[BIBatteryAnalysisManagerClient connection]
+ -[BIBatteryAnalysisManagerClient dealloc]
+ -[BIBatteryAnalysisManagerClient init]
+ -[BIBatteryAnalysisManagerClient init].cold.1
+ -[BIBatteryAnalysisManagerClient init].cold.2
+ -[BIBatteryAnalysisManagerClient logger]
+ -[BIBatteryAnalysisManagerClient setConnection:]
+ -[BIBatteryAnalysisManagerClient setLogger:]
+ -[BIBatteryAnalysisManagerClient updateTarget:withEstimate:withError:]
+ -[BIBatteryAnalysisOutput .cxx_destruct]
+ -[BIBatteryAnalysisOutput additionalInformation]
+ -[BIBatteryAnalysisOutput confidenceScore]
+ -[BIBatteryAnalysisOutput description]
+ -[BIBatteryAnalysisOutput encodeWithCoder:]
+ -[BIBatteryAnalysisOutput endSOC]
+ -[BIBatteryAnalysisOutput estimate]
+ -[BIBatteryAnalysisOutput formattedEstimate]
+ -[BIBatteryAnalysisOutput initWithCoder:]
+ -[BIBatteryAnalysisOutput isEstimateOverridden]
+ -[BIBatteryAnalysisOutput isFirstEstimate]
+ -[BIBatteryAnalysisOutput setAdditionalInformation:]
+ -[BIBatteryAnalysisOutput setConfidenceScore:]
+ -[BIBatteryAnalysisOutput setEndSOC:]
+ -[BIBatteryAnalysisOutput setEstimate:]
+ -[BIBatteryAnalysisOutput setFormattedEstimate:]
+ -[BIBatteryAnalysisOutput setIsEstimateOverridden:]
+ -[BIBatteryAnalysisOutput setIsFirstEstimate:]
+ -[BIBatteryAnalysisOutput setSocAtEstimateTime:]
+ -[BIBatteryAnalysisOutput socAtEstimateTime]
+ -[BIBatteryAnalysisTargetDetails .cxx_destruct]
+ -[BIBatteryAnalysisTargetDetails friendlyName]
+ -[BIBatteryAnalysisTargetDetails notificationName]
+ -[BIBatteryAnalysisTargetDetails setFriendlyName:]
+ -[BIBatteryAnalysisTargetDetails setNotificationName:]
+ -[battery_analysis_tt80_model .cxx_destruct]
+ -[battery_analysis_tt80_model initWithConfiguration:error:]
+ -[battery_analysis_tt80_model initWithContentsOfURL:configuration:error:]
+ -[battery_analysis_tt80_model initWithContentsOfURL:error:]
+ -[battery_analysis_tt80_model initWithMLModel:]
+ -[battery_analysis_tt80_model init]
+ -[battery_analysis_tt80_model model]
+ -[battery_analysis_tt80_model predictionFromFeatures:completionHandler:]
+ -[battery_analysis_tt80_model predictionFromFeatures:error:]
+ -[battery_analysis_tt80_model predictionFromFeatures:options:completionHandler:]
+ -[battery_analysis_tt80_model predictionFromFeatures:options:error:]
+ -[battery_analysis_tt80_model predictionFromInput_1:error:]
+ -[battery_analysis_tt80_model predictionsFromInputs:options:error:]
+ -[battery_analysis_tt80_modelInput .cxx_destruct]
+ -[battery_analysis_tt80_modelInput featureNames]
+ -[battery_analysis_tt80_modelInput featureValueForName:]
+ -[battery_analysis_tt80_modelInput initWithInput_1:]
+ -[battery_analysis_tt80_modelInput input_1]
+ -[battery_analysis_tt80_modelInput setInput_1:]
+ -[battery_analysis_tt80_modelOutput .cxx_destruct]
+ -[battery_analysis_tt80_modelOutput featureNames]
+ -[battery_analysis_tt80_modelOutput featureValueForName:]
+ -[battery_analysis_tt80_modelOutput initWithTt80_prediction:]
+ -[battery_analysis_tt80_modelOutput setTt80_prediction:]
+ -[battery_analysis_tt80_modelOutput tt80_prediction]
+ GCC_except_table0
+ GCC_except_table13
+ GCC_except_table21
+ GCC_except_table24
+ GCC_except_table29
+ GCC_except_table31
+ GCC_except_table4
+ GCC_except_table9
+ _BIBatteryAnalysisErrorDomain
+ _IOPSGetPercentRemaining
+ _NSStringFromSelector
+ _OBJC_CLASS_$_BIBatteryAnalysisClient
+ _OBJC_CLASS_$_BIBatteryAnalysisContainer
+ _OBJC_CLASS_$_BIBatteryAnalysisManagerClient
+ _OBJC_CLASS_$_BIBatteryAnalysisOutput
+ _OBJC_CLASS_$_BIBatteryAnalysisSharedResources
+ _OBJC_CLASS_$_BIBatteryAnalysisTargetDetails
+ _OBJC_CLASS_$_MLArrayBatchProvider
+ _OBJC_CLASS_$_MLFeatureValue
+ _OBJC_CLASS_$_MLModel
+ _OBJC_CLASS_$_MLPredictionOptions
+ _OBJC_CLASS_$_NSBundle
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OBJC_CLASS_$_NSDateComponentsFormatter
+ _OBJC_CLASS_$_NSDictionary
+ _OBJC_CLASS_$_NSError
+ _OBJC_CLASS_$_NSMutableArray
+ _OBJC_CLASS_$_NSMutableDictionary
+ _OBJC_CLASS_$_NSMutableSet
+ _OBJC_CLASS_$_NSNumber
+ _OBJC_CLASS_$_NSNumberFormatter
+ _OBJC_CLASS_$_NSSet
+ _OBJC_CLASS_$_NSURL
+ _OBJC_CLASS_$_NSXPCConnection
+ _OBJC_CLASS_$_NSXPCInterface
+ _OBJC_CLASS_$_battery_analysis_tt80_model
+ _OBJC_CLASS_$_battery_analysis_tt80_modelInput
+ _OBJC_CLASS_$_battery_analysis_tt80_modelOutput
+ _OBJC_IVAR_$_BIBatteryAnalysisClient._connection
+ _OBJC_IVAR_$_BIBatteryAnalysisClient._delegate
+ _OBJC_IVAR_$_BIBatteryAnalysisClient._logger
+ _OBJC_IVAR_$_BIBatteryAnalysisClient._notificationTokens
+ _OBJC_IVAR_$_BIBatteryAnalysisClient._queue
+ _OBJC_IVAR_$_BIBatteryAnalysisClient._targetOutputs
+ _OBJC_IVAR_$_BIBatteryAnalysisClient._targets
+ _OBJC_IVAR_$_BIBatteryAnalysisContainer._error
+ _OBJC_IVAR_$_BIBatteryAnalysisContainer._estimateObj
+ _OBJC_IVAR_$_BIBatteryAnalysisContainer._lastUpdatedMonotonicTime
+ _OBJC_IVAR_$_BIBatteryAnalysisManagerClient._connection
+ _OBJC_IVAR_$_BIBatteryAnalysisManagerClient._logger
+ _OBJC_IVAR_$_BIBatteryAnalysisOutput._additionalInformation
+ _OBJC_IVAR_$_BIBatteryAnalysisOutput._confidenceScore
+ _OBJC_IVAR_$_BIBatteryAnalysisOutput._endSOC
+ _OBJC_IVAR_$_BIBatteryAnalysisOutput._estimate
+ _OBJC_IVAR_$_BIBatteryAnalysisOutput._formattedEstimate
+ _OBJC_IVAR_$_BIBatteryAnalysisOutput._isEstimateOverridden
+ _OBJC_IVAR_$_BIBatteryAnalysisOutput._isFirstEstimate
+ _OBJC_IVAR_$_BIBatteryAnalysisOutput._socAtEstimateTime
+ _OBJC_IVAR_$_BIBatteryAnalysisTargetDetails._friendlyName
+ _OBJC_IVAR_$_BIBatteryAnalysisTargetDetails._notificationName
+ _OBJC_IVAR_$_battery_analysis_tt80_model._model
+ _OBJC_IVAR_$_battery_analysis_tt80_modelInput._input_1
+ _OBJC_IVAR_$_battery_analysis_tt80_modelOutput._tt80_prediction
+ _OBJC_METACLASS_$_BIBatteryAnalysisClient
+ _OBJC_METACLASS_$_BIBatteryAnalysisContainer
+ _OBJC_METACLASS_$_BIBatteryAnalysisManagerClient
+ _OBJC_METACLASS_$_BIBatteryAnalysisOutput
+ _OBJC_METACLASS_$_BIBatteryAnalysisSharedResources
+ _OBJC_METACLASS_$_BIBatteryAnalysisTargetDetails
+ _OBJC_METACLASS_$_battery_analysis_tt80_model
+ _OBJC_METACLASS_$_battery_analysis_tt80_modelInput
+ _OBJC_METACLASS_$_battery_analysis_tt80_modelOutput
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ __Block_object_dispose
+ __NSConcreteStackBlock
+ __OBJC_$_CLASS_METHODS_BIBatteryAnalysisContainer
+ __OBJC_$_CLASS_METHODS_BIBatteryAnalysisOutput
+ __OBJC_$_CLASS_METHODS_BIBatteryAnalysisSharedResources
+ __OBJC_$_CLASS_METHODS_battery_analysis_tt80_model
+ __OBJC_$_CLASS_PROP_LIST_BIBatteryAnalysisContainer
+ __OBJC_$_CLASS_PROP_LIST_BIBatteryAnalysisOutput
+ __OBJC_$_INSTANCE_METHODS_BIBatteryAnalysisClient
+ __OBJC_$_INSTANCE_METHODS_BIBatteryAnalysisContainer
+ __OBJC_$_INSTANCE_METHODS_BIBatteryAnalysisManagerClient
+ __OBJC_$_INSTANCE_METHODS_BIBatteryAnalysisOutput
+ __OBJC_$_INSTANCE_METHODS_BIBatteryAnalysisTargetDetails
+ __OBJC_$_INSTANCE_METHODS_battery_analysis_tt80_model
+ __OBJC_$_INSTANCE_METHODS_battery_analysis_tt80_modelInput
+ __OBJC_$_INSTANCE_METHODS_battery_analysis_tt80_modelOutput
+ __OBJC_$_INSTANCE_VARIABLES_BIBatteryAnalysisClient
+ __OBJC_$_INSTANCE_VARIABLES_BIBatteryAnalysisContainer
+ __OBJC_$_INSTANCE_VARIABLES_BIBatteryAnalysisManagerClient
+ __OBJC_$_INSTANCE_VARIABLES_BIBatteryAnalysisOutput
+ __OBJC_$_INSTANCE_VARIABLES_BIBatteryAnalysisTargetDetails
+ __OBJC_$_INSTANCE_VARIABLES_battery_analysis_tt80_model
+ __OBJC_$_INSTANCE_VARIABLES_battery_analysis_tt80_modelInput
+ __OBJC_$_INSTANCE_VARIABLES_battery_analysis_tt80_modelOutput
+ __OBJC_$_PROP_LIST_BIBatteryAnalysisClient
+ __OBJC_$_PROP_LIST_BIBatteryAnalysisContainer
+ __OBJC_$_PROP_LIST_BIBatteryAnalysisManagerClient
+ __OBJC_$_PROP_LIST_BIBatteryAnalysisOutput
+ __OBJC_$_PROP_LIST_BIBatteryAnalysisTargetDetails
+ __OBJC_$_PROP_LIST_MLFeatureProvider
+ __OBJC_$_PROP_LIST_NSObject
+ __OBJC_$_PROP_LIST_battery_analysis_tt80_model
+ __OBJC_$_PROP_LIST_battery_analysis_tt80_modelInput
+ __OBJC_$_PROP_LIST_battery_analysis_tt80_modelOutput
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BIBatteryAnalysisManagerProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BIBatteryAnalysisProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MLFeatureProvider
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BIBatteryAnalysisManagerProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BIBatteryAnalysisProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MLFeatureProvider
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject
+ __OBJC_$_PROTOCOL_REFS_BIBatteryAnalysisManagerProtocol
+ __OBJC_$_PROTOCOL_REFS_BIBatteryAnalysisProtocol
+ __OBJC_CLASS_PROTOCOLS_$_BIBatteryAnalysisContainer
+ __OBJC_CLASS_PROTOCOLS_$_BIBatteryAnalysisOutput
+ __OBJC_CLASS_PROTOCOLS_$_battery_analysis_tt80_modelInput
+ __OBJC_CLASS_PROTOCOLS_$_battery_analysis_tt80_modelOutput
+ __OBJC_CLASS_RO_$_BIBatteryAnalysisClient
+ __OBJC_CLASS_RO_$_BIBatteryAnalysisContainer
+ __OBJC_CLASS_RO_$_BIBatteryAnalysisManagerClient
+ __OBJC_CLASS_RO_$_BIBatteryAnalysisOutput
+ __OBJC_CLASS_RO_$_BIBatteryAnalysisSharedResources
+ __OBJC_CLASS_RO_$_BIBatteryAnalysisTargetDetails
+ __OBJC_CLASS_RO_$_battery_analysis_tt80_model
+ __OBJC_CLASS_RO_$_battery_analysis_tt80_modelInput
+ __OBJC_CLASS_RO_$_battery_analysis_tt80_modelOutput
+ __OBJC_LABEL_PROTOCOL_$_BIBatteryAnalysisManagerProtocol
+ __OBJC_LABEL_PROTOCOL_$_BIBatteryAnalysisProtocol
+ __OBJC_LABEL_PROTOCOL_$_MLFeatureProvider
+ __OBJC_LABEL_PROTOCOL_$_NSObject
+ __OBJC_METACLASS_RO_$_BIBatteryAnalysisClient
+ __OBJC_METACLASS_RO_$_BIBatteryAnalysisContainer
+ __OBJC_METACLASS_RO_$_BIBatteryAnalysisManagerClient
+ __OBJC_METACLASS_RO_$_BIBatteryAnalysisOutput
+ __OBJC_METACLASS_RO_$_BIBatteryAnalysisSharedResources
+ __OBJC_METACLASS_RO_$_BIBatteryAnalysisTargetDetails
+ __OBJC_METACLASS_RO_$_battery_analysis_tt80_model
+ __OBJC_METACLASS_RO_$_battery_analysis_tt80_modelInput
+ __OBJC_METACLASS_RO_$_battery_analysis_tt80_modelOutput
+ __OBJC_PROTOCOL_$_BIBatteryAnalysisManagerProtocol
+ __OBJC_PROTOCOL_$_BIBatteryAnalysisProtocol
+ __OBJC_PROTOCOL_$_MLFeatureProvider
+ __OBJC_PROTOCOL_$_NSObject
+ __OBJC_PROTOCOL_REFERENCE_$_BIBatteryAnalysisManagerProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_BIBatteryAnalysisProtocol
+ __Unwind_Resume
+ ___38-[BIBatteryAnalysisManagerClient init]_block_invoke
+ ___38-[BIBatteryAnalysisManagerClient init]_block_invoke.169
+ ___38-[BIBatteryAnalysisManagerClient init]_block_invoke.169.cold.1
+ ___38-[BIBatteryAnalysisManagerClient init]_block_invoke.cold.1
+ ___43-[BIBatteryAnalysisClient initWithTargets:]_block_invoke
+ ___43-[BIBatteryAnalysisClient initWithTargets:]_block_invoke.84
+ ___43-[BIBatteryAnalysisClient initWithTargets:]_block_invoke.84.cold.1
+ ___43-[BIBatteryAnalysisClient initWithTargets:]_block_invoke.86
+ ___43-[BIBatteryAnalysisClient initWithTargets:]_block_invoke.cold.1
+ ___51-[BIBatteryAnalysisClient updateEstimateForTarget:]_block_invoke
+ ___51-[BIBatteryAnalysisClient updateEstimateForTarget:]_block_invoke.89
+ ___51-[BIBatteryAnalysisClient updateEstimateForTarget:]_block_invoke.89.cold.1
+ ___51-[BIBatteryAnalysisClient updateEstimateForTarget:]_block_invoke.cold.1
+ ___52-[BIBatteryAnalysisManagerClient adHocRunWithError:]_block_invoke
+ ___52-[BIBatteryAnalysisManagerClient adHocRunWithError:]_block_invoke.173
+ ___52-[BIBatteryAnalysisManagerClient adHocRunWithError:]_block_invoke.173.cold.1
+ ___52-[BIBatteryAnalysisManagerClient adHocRunWithError:]_block_invoke.cold.1
+ ___54-[BIBatteryAnalysisClient registerForUpdatesToTarget:]_block_invoke
+ ___55+[BIBatteryAnalysisSharedResources sharedTargetDetails]_block_invoke
+ ___55-[BIBatteryAnalysisClient estimateForTarget:withError:]_block_invoke
+ ___70-[BIBatteryAnalysisManagerClient updateTarget:withEstimate:withError:]_block_invoke
+ ___70-[BIBatteryAnalysisManagerClient updateTarget:withEstimate:withError:]_block_invoke.171
+ ___70-[BIBatteryAnalysisManagerClient updateTarget:withEstimate:withError:]_block_invoke.171.cold.1
+ ___70-[BIBatteryAnalysisManagerClient updateTarget:withEstimate:withError:]_block_invoke.cold.1
+ ___72-[battery_analysis_tt80_model predictionFromFeatures:completionHandler:]_block_invoke
+ ___80-[battery_analysis_tt80_model predictionFromFeatures:options:completionHandler:]_block_invoke
+ ___81+[battery_analysis_tt80_model loadContentsOfURL:configuration:completionHandler:]_block_invoke
+ ___Block_byref_object_copy_
+ ___Block_byref_object_dispose_
+ ___abbreviatedHourNSTimeIntervalFormatter_block_invoke
+ ___abbreviatedNSTimeIntervalFormatter_block_invoke
+ ___block_descriptor_40_e8_32bs_e29_v24?0"MLModel"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32bs_e41_v24?0"<MLFeatureProvider>"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32w_e5_v8?0lw32l8
+ ___block_descriptor_48_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_48_e8_32s_e17_v16?0"NSError"8ls32l8
+ ___block_descriptor_56_e8_32s40r_e17_v16?0"NSError"8ls32l8r40l8
+ ___block_descriptor_56_e8_32s40r_e45_v24?0"BIBatteryAnalysisOutput"8"NSError"16ls32l8r40l8
+ ___block_descriptor_56_e8_32s40w_e8_v12?0i8lw40l8s32l8
+ ___block_descriptor_64_e8_32s40r48r_e20_v20?0B8"NSError"12lr40l8s32l8r48l8
+ ___block_descriptor_72_e8_32s40r48r56w_e5_v8?0lw56l8r40l8r48l8s32l8
+ ___block_literal_global.3
+ ___block_literal_global.5
+ ___objc_personality_v0
+ ___percentFormatter_block_invoke
+ __os_log_default
+ __os_log_error_impl
+ __os_log_impl
+ _abbreviatedHourNSTimeIntervalFormatter
+ _abbreviatedHourNSTimeIntervalFormatter.cold.1
+ _abbreviatedHourNSTimeIntervalFormatter.formatter
+ _abbreviatedHourNSTimeIntervalFormatter.onceToken
+ _abbreviatedNSTimeIntervalFormatter
+ _abbreviatedNSTimeIntervalFormatter.cold.1
+ _abbreviatedNSTimeIntervalFormatter.formatter
+ _abbreviatedNSTimeIntervalFormatter.onceToken
+ _clock_gettime_nsec_np
+ _dispatch_async
+ _dispatch_block_cancel
+ _dispatch_block_create
+ _dispatch_queue_attr_make_with_autorelease_frequency
+ _dispatch_queue_create
+ _dispatch_semaphore_create
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
+ _dispatch_time
+ _formatNSNumberAsPercentage
+ _getBatteryUISOC
+ _getMonotonicTimeInNanoSeconds
+ _notify_cancel
+ _notify_register_dispatch
+ _objc_alloc
+ _objc_autorelease
+ _objc_claimAutoreleasedReturnValue
+ _objc_copyWeak
+ _objc_destroyWeak
+ _objc_enumerationMutation
+ _objc_initWeak
+ _objc_loadWeakRetained
+ _objc_msgSend$URLOfModelInThisBundle
+ _objc_msgSend$UTF8String
+ _objc_msgSend$activate
+ _objc_msgSend$addObject:
+ _objc_msgSend$additionalInformation
+ _objc_msgSend$allKeys
+ _objc_msgSend$allowedUnits
+ _objc_msgSend$areTargetsValid:
+ _objc_msgSend$arrayWithCapacity:
+ _objc_msgSend$bundleForClass:
+ _objc_msgSend$confidenceScore
+ _objc_msgSend$containsObject:
+ _objc_msgSend$count
+ _objc_msgSend$countByEnumeratingWithState:objects:count:
+ _objc_msgSend$decodeBoolForKey:
+ _objc_msgSend$decodeObjectForKey:
+ _objc_msgSend$decodeObjectOfClass:forKey:
+ _objc_msgSend$delegate
+ _objc_msgSend$dictionaryWithObjects:forKeys:count:
+ _objc_msgSend$didUpdateEstimateFor:newEstimate:error:
+ _objc_msgSend$doubleValue
+ _objc_msgSend$encodeBool:forKey:
+ _objc_msgSend$encodeObject:forKey:
+ _objc_msgSend$endSOC
+ _objc_msgSend$error
+ _objc_msgSend$errorWithDomain:code:userInfo:
+ _objc_msgSend$estimate
+ _objc_msgSend$estimateForTarget:withHandler:
+ _objc_msgSend$estimateFromCache:withError:
+ _objc_msgSend$estimateObj
+ _objc_msgSend$featureValueForName:
+ _objc_msgSend$featureValueWithMultiArray:
+ _objc_msgSend$featuresAtIndex:
+ _objc_msgSend$fileURLWithPath:
+ _objc_msgSend$formattedEstimateForOutput:withTarget:
+ _objc_msgSend$getLocalizedStringForKey:
+ _objc_msgSend$initWithContentsOfURL:configuration:error:
+ _objc_msgSend$initWithContentsOfURL:error:
+ _objc_msgSend$initWithFeatureProviderArray:
+ _objc_msgSend$initWithInput_1:
+ _objc_msgSend$initWithMLModel:
+ _objc_msgSend$initWithMachServiceName:options:
+ _objc_msgSend$initWithTt80_prediction:
+ _objc_msgSend$input_1
+ _objc_msgSend$integerValue
+ _objc_msgSend$interfaceWithProtocol:
+ _objc_msgSend$invalidate
+ _objc_msgSend$isEqualToString:
+ _objc_msgSend$isEstimateOverridden
+ _objc_msgSend$isFirstEstimate
+ _objc_msgSend$isTargetValid:
+ _objc_msgSend$lastUpdatedMonotonicTime
+ _objc_msgSend$loadContentsOfURL:configuration:completionHandler:
+ _objc_msgSend$localizedStringForKey:value:table:
+ _objc_msgSend$localizedStringWithFormat:
+ _objc_msgSend$logger
+ _objc_msgSend$model
+ _objc_msgSend$modelWithContentsOfURL:configuration:error:
+ _objc_msgSend$modelWithContentsOfURL:error:
+ _objc_msgSend$multiArrayValue
+ _objc_msgSend$notificationName
+ _objc_msgSend$numberWithDouble:
+ _objc_msgSend$numberWithInt:
+ _objc_msgSend$numberWithInteger:
+ _objc_msgSend$objectForKey:
+ _objc_msgSend$pathForResource:ofType:
+ _objc_msgSend$predictionFromFeatures:completionHandler:
+ _objc_msgSend$predictionFromFeatures:error:
+ _objc_msgSend$predictionFromFeatures:options:completionHandler:
+ _objc_msgSend$predictionFromFeatures:options:error:
+ _objc_msgSend$predictionsFromBatch:options:error:
+ _objc_msgSend$registerForUpdatesToTarget:
+ _objc_msgSend$runAndReply:
+ _objc_msgSend$set
+ _objc_msgSend$setAllowedUnits:
+ _objc_msgSend$setError:
+ _objc_msgSend$setEstimateObj:
+ _objc_msgSend$setFormattedEstimate:
+ _objc_msgSend$setFriendlyName:
+ _objc_msgSend$setInterruptionHandler:
+ _objc_msgSend$setInvalidationHandler:
+ _objc_msgSend$setIsEstimateOverridden:
+ _objc_msgSend$setIsFirstEstimate:
+ _objc_msgSend$setLastUpdatedMonotonicTime:
+ _objc_msgSend$setNotificationName:
+ _objc_msgSend$setNumberStyle:
+ _objc_msgSend$setObject:forKey:
+ _objc_msgSend$setRemoteObjectInterface:
+ _objc_msgSend$setSocAtEstimateTime:
+ _objc_msgSend$setUnitsStyle:
+ _objc_msgSend$setWithArray:
+ _objc_msgSend$sharedTargetDetails
+ _objc_msgSend$stringFromNumber:
+ _objc_msgSend$stringFromTimeInterval:
+ _objc_msgSend$synchronousRemoteObjectProxyWithErrorHandler:
+ _objc_msgSend$tt80_prediction
+ _objc_msgSend$unsignedIntValue
+ _objc_msgSend$updateEstimateForTarget:
+ _objc_msgSend$updateTarget:withEstimate:andReply:
+ _objc_opt_class
+ _objc_opt_new
+ _objc_opt_respondsToSelector
+ _objc_release_x21
+ _objc_release_x22
+ _objc_release_x23
+ _objc_release_x24
+ _objc_release_x25
+ _objc_release_x26
+ _objc_release_x27
+ _objc_release_x28
+ _objc_release_x9
+ _objc_retain
+ _objc_retainAutorelease
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x21
+ _objc_retain_x22
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x8
+ _objc_storeWeak
+ _os_transaction_create
+ _percentFormatter
+ _percentFormatter.cold.1
+ _percentFormatter.formatter
+ _percentFormatter.onceToken
+ _sharedTargetDetails.onceToken
+ _sharedTargetDetails.targetDetails
CStrings:
+ ""
+ "#16@0:8"
+ "<BIBatteryAnalysisContainer: estimate: %@, lastUpdatedMonotonicTime: %ld, Error: %@>"
+ "<BatteryAnalysisOutput: estimate: %.02f, socAtEstimateTime: %ld, endSOC: %ld, confidenceScore: %.02f, additionalInformation: %ld, formattedEstimate: %@, isFirstEstimate: %@, isEstimateOverridden: %@>"
+ "@\"<BIBatteryAnalysisDelegate>\""
+ "@\"BIBatteryAnalysisOutput\""
+ "@\"MLFeatureValue\"24@0:8@\"NSString\"16"
+ "@\"MLModel\""
+ "@\"MLMultiArray\""
+ "@\"NSError\""
+ "@\"NSMutableDictionary\""
+ "@\"NSMutableSet\""
+ "@\"NSObject<OS_dispatch_queue>\""
+ "@\"NSSet\""
+ "@\"NSSet\"16@0:8"
+ "@\"NSString\""
+ "@\"NSString\"16@0:8"
+ "@\"NSXPCConnection\""
+ "@24@0:8:16"
+ "@32@0:8:16@24"
+ "@32@0:8@16^@24"
+ "@32@0:8@16q24"
+ "@32@0:8q16^@24"
+ "@40@0:8:16@24@32"
+ "@40@0:8@16@24^@32"
+ "B"
+ "B24@0:8#16"
+ "B24@0:8:16"
+ "B24@0:8@\"Protocol\"16"
+ "B24@0:8@16"
+ "B24@0:8^@16"
+ "B24@0:8q16"
+ "B40@0:8q16d24^@32"
+ "BIBatteryAnalysis-Localizable"
+ "BIBatteryAnalysisClient"
+ "BIBatteryAnalysisClient init"
+ "BIBatteryAnalysisContainer"
+ "BIBatteryAnalysisManagerClient"
+ "BIBatteryAnalysisManagerClient init"
+ "BIBatteryAnalysisManagerProtocol"
+ "BIBatteryAnalysisOutput"
+ "BIBatteryAnalysisProtocol"
+ "BIBatteryAnalysisSharedResources"
+ "BIBatteryAnalysisTargetDetails"
+ "CHARGE_TIME"
+ "CHARGE_TIME_GREATER_THAN_THRESHOLD"
+ "Client output:%@"
+ "Connection to service interrupted."
+ "Connection to service invalidated."
+ "Could not load battery_analysis_tt80_model.mlmodelc in the bundle resource"
+ "Error cancelling notification token: %u, result: %d."
+ "Error executing %@: %@"
+ "Established connection to batteryintelligenced."
+ "Estimate updated for %@ target with client output: %@"
+ "Failed to connect to batteryintelligenced."
+ "Failed to initialize BIBatteryAnalysisClient."
+ "Failed to initialize BIBatteryAnalysisManagerClient."
+ "Failed to register to get notification for %@ target with status 0x%x"
+ "Invalid target: %@, Valid targets are: %@"
+ "Invalid targets are being used for registration: %@. Valid targets are: %@"
+ "MLFeatureProvider"
+ "NO"
+ "NSObject"
+ "Notification received %@"
+ "Passing the updated estimate to the delegate UpdateEstimateFor method for target %@"
+ "Q16@0:8"
+ "SLOW_CHARGER"
+ "Server error %@"
+ "Successfully cancelled notification token: %u."
+ "T#,R"
+ "T@\"<BIBatteryAnalysisDelegate>\",W,N,V_delegate"
+ "T@\"BIBatteryAnalysisOutput\",&,N,V_estimateObj"
+ "T@\"MLModel\",R,N,V_model"
+ "T@\"MLMultiArray\",&,N,V_input_1"
+ "T@\"MLMultiArray\",&,N,V_tt80_prediction"
+ "T@\"NSError\",&,N,V_error"
+ "T@\"NSMutableDictionary\",&,N,V_targetOutputs"
+ "T@\"NSMutableSet\",&,N,V_notificationTokens"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue"
+ "T@\"NSSet\",&,N,V_targets"
+ "T@\"NSSet\",R,N"
+ "T@\"NSString\",&,N,V_formattedEstimate"
+ "T@\"NSString\",&,N,V_friendlyName"
+ "T@\"NSString\",&,N,V_notificationName"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",R,C"
+ "T@\"NSXPCConnection\",&,N,V_connection"
+ "TB,N,V_isEstimateOverridden"
+ "TB,N,V_isFirstEstimate"
+ "TQ,R"
+ "TT80"
+ "TTL"
+ "Tq,N,V_lastUpdatedMonotonicTime"
+ "Tq,N,V_socAtEstimateTime"
+ "URLOfModelInThisBundle"
+ "UTF8String"
+ "Vv16@0:8"
+ "Wait time exceeded for target %@"
+ "YES"
+ "^{_NSZone=}16@0:8"
+ "_connection"
+ "_delegate"
+ "_error"
+ "_estimateObj"
+ "_formattedEstimate"
+ "_friendlyName"
+ "_input_1"
+ "_isEstimateOverridden"
+ "_isFirstEstimate"
+ "_lastUpdatedMonotonicTime"
+ "_model"
+ "_notificationName"
+ "_notificationTokens"
+ "_queue"
+ "_socAtEstimateTime"
+ "_targetOutputs"
+ "_targets"
+ "_tt80_prediction"
+ "a"
+ "activate"
+ "adHocRunWithError:"
+ "addObject:"
+ "allKeys"
+ "allowedUnits"
+ "areTargetsValid:"
+ "arrayWithCapacity:"
+ "autorelease"
+ "battery_analysis_tt80_model"
+ "battery_analysis_tt80_modelInput"
+ "battery_analysis_tt80_modelOutput"
+ "bundleForClass:"
+ "class"
+ "com.apple.BatteryIntelligence.BatteryAnalysis"
+ "com.apple.batteryintelligence.batteryanalysisclient"
+ "com.apple.batteryintelligenced.battery-analysis-client-estimate-for-target"
+ "com.apple.batteryintelligenced.battery-analysis-client-estimate-update"
+ "com.apple.batteryintelligenced.batteryanalysis"
+ "com.apple.batteryintelligenced.batteryanalysismanager"
+ "com.apple.batteryintelligenced.batteryanalysistt80updated"
+ "com.apple.batteryintelligenced.batteryanalysisttlupdated"
+ "conformsToProtocol:"
+ "connection"
+ "containsObject:"
+ "count"
+ "countByEnumeratingWithState:objects:count:"
+ "dealloc"
+ "debugDescription"
+ "decodeBoolForKey:"
+ "decodeObjectForKey:"
+ "decodeObjectOfClass:forKey:"
+ "delegate"
+ "dictionaryWithObjects:forKeys:count:"
+ "didUpdateEstimateFor:newEstimate:error:"
+ "doubleValue"
+ "encodeBool:forKey:"
+ "encodeObject:forKey:"
+ "error"
+ "errorWithDomain:code:userInfo:"
+ "estimateForTarget:withError:"
+ "estimateForTarget:withHandler:"
+ "estimateFromCache:withError:"
+ "estimateObj"
+ "featureNames"
+ "featureValueForName:"
+ "featureValueWithMultiArray:"
+ "featuresAtIndex:"
+ "fileURLWithPath:"
+ "formattedEstimate"
+ "formattedEstimateForOutput:withTarget:"
+ "friendlyName"
+ "getLocalizedStringForKey:"
+ "hash"
+ "initWithConfiguration:error:"
+ "initWithContentsOfURL:configuration:error:"
+ "initWithContentsOfURL:error:"
+ "initWithFeatureProviderArray:"
+ "initWithInput_1:"
+ "initWithMLModel:"
+ "initWithMachServiceName:options:"
+ "initWithTargets:"
+ "initWithTt80_prediction:"
+ "input_1"
+ "integerValue"
+ "interfaceWithProtocol:"
+ "invalidate"
+ "isEqual:"
+ "isEqualToString:"
+ "isEstimateOverridden"
+ "isFirstEstimate"
+ "isKindOfClass:"
+ "isMemberOfClass:"
+ "isProxy"
+ "isTargetValid:"
+ "lastUpdatedMonotonicTime"
+ "loadContentsOfURL:configuration:completionHandler:"
+ "loadWithConfiguration:completionHandler:"
+ "localizedStringForKey:value:table:"
+ "localizedStringWithFormat:"
+ "mlmodelc"
+ "model"
+ "modelWithContentsOfURL:configuration:error:"
+ "modelWithContentsOfURL:error:"
+ "multiArrayValue"
+ "notificationName"
+ "notificationTokens"
+ "numberWithDouble:"
+ "numberWithInt:"
+ "numberWithInteger:"
+ "objectForKey:"
+ "pathForResource:ofType:"
+ "performSelector:"
+ "performSelector:withObject:"
+ "performSelector:withObject:withObject:"
+ "predictionFromFeatures:completionHandler:"
+ "predictionFromFeatures:error:"
+ "predictionFromFeatures:options:completionHandler:"
+ "predictionFromFeatures:options:error:"
+ "predictionFromInput_1:error:"
+ "predictionsFromBatch:options:error:"
+ "predictionsFromInputs:options:error:"
+ "queue"
+ "registerForUpdatesToTarget:"
+ "release"
+ "respondsToSelector:"
+ "retain"
+ "retainCount"
+ "runAndReply:"
+ "self"
+ "set"
+ "setAllowedUnits:"
+ "setConnection:"
+ "setDelegate:"
+ "setError:"
+ "setEstimateObj:"
+ "setFormattedEstimate:"
+ "setFriendlyName:"
+ "setInput_1:"
+ "setInterruptionHandler:"
+ "setInvalidationHandler:"
+ "setIsEstimateOverridden:"
+ "setIsFirstEstimate:"
+ "setLastUpdatedMonotonicTime:"
+ "setNotificationName:"
+ "setNotificationTokens:"
+ "setNumberStyle:"
+ "setObject:forKey:"
+ "setQueue:"
+ "setRemoteObjectInterface:"
+ "setSocAtEstimateTime:"
+ "setTargetOutputs:"
+ "setTargets:"
+ "setTt80_prediction:"
+ "setUnitsStyle:"
+ "setWithArray:"
+ "sharedTargetDetails"
+ "socAtEstimateTime"
+ "stringFromNumber:"
+ "stringFromTimeInterval:"
+ "superclass"
+ "synchronousRemoteObjectProxyWithErrorHandler:"
+ "target %@ was not registered at init"
+ "targetOutputs"
+ "targets"
+ "tt80_prediction"
+ "unsignedIntValue"
+ "updateEstimateForTarget:"
+ "updateTarget:withEstimate:andReply:"
+ "updateTarget:withEstimate:withError:"
+ "v12@?0i8"
+ "v16@?0@\"NSError\"8"
+ "v20@0:8B16"
+ "v20@?0B8@\"NSError\"12"
+ "v24@0:8@?16"
+ "v24@0:8@?<v@?B@\"NSError\">16"
+ "v24@?0@\"<MLFeatureProvider>\"8@\"NSError\"16"
+ "v24@?0@\"BIBatteryAnalysisOutput\"8@\"NSError\"16"
+ "v24@?0@\"MLModel\"8@\"NSError\"16"
+ "v32@0:8@16@?24"
+ "v32@0:8q16@?24"
+ "v32@0:8q16@?<v@?@\"BIBatteryAnalysisOutput\"@\"NSError\">24"
+ "v40@0:8@16@24@?32"
+ "v40@0:8q16d24@?32"
+ "v40@0:8q16d24@?<v@?B@\"NSError\">32"
+ "zone"

```
