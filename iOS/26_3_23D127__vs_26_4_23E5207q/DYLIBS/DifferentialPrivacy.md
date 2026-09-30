## DifferentialPrivacy

> `/System/Library/PrivateFrameworks/DifferentialPrivacy.framework/DifferentialPrivacy`

```diff

-684.80.8.0.0
-  __TEXT.__text: 0x60264
-  __TEXT.__auth_stubs: 0x1180
-  __TEXT.__objc_methlist: 0x5924
+684.100.52.0.1
+  __TEXT.__text: 0x62838
+  __TEXT.__auth_stubs: 0x1120
+  __TEXT.__objc_methlist: 0x591c
   __TEXT.__const: 0x9e8
-  __TEXT.__cstring: 0x4b7c
-  __TEXT.__oslogstring: 0x4350
-  __TEXT.__gcc_except_tab: 0xcfc
+  __TEXT.__cstring: 0x482c
+  __TEXT.__oslogstring: 0x4237
+  __TEXT.__gcc_except_tab: 0xd0c
   __TEXT.__ustring: 0x4
   __TEXT.__dlopen_cstrs: 0x74
   __TEXT.__constg_swiftt: 0x300

   __TEXT.__swift5_proto: 0x40
   __TEXT.__swift5_mpenum: 0x10
   __TEXT.__swift5_capture: 0x28
-  __TEXT.__unwind_info: 0x1898
-  __TEXT.__eh_frame: 0x858
-  __TEXT.__objc_classname: 0xdbf
-  __TEXT.__objc_methname: 0x9de3
-  __TEXT.__objc_methtype: 0x12de
-  __TEXT.__objc_stubs: 0x7f00
-  __DATA_CONST.__got: 0x818
+  __TEXT.__unwind_info: 0x1990
+  __TEXT.__eh_frame: 0x798
+  __TEXT.__objc_classname: 0xed3
+  __TEXT.__objc_methname: 0xa1ad
+  __TEXT.__objc_methtype: 0x1407
+  __TEXT.__objc_stubs: 0x7f60
+  __DATA_CONST.__got: 0x800
   __DATA_CONST.__const: 0x1238
   __DATA_CONST.__objc_classlist: 0x4b8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2530
+  __DATA_CONST.__objc_selrefs: 0x2540
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x2e8
   __DATA_CONST.__objc_arraydata: 0x108
-  __AUTH_CONST.__auth_got: 0x8d8
+  __AUTH_CONST.__auth_got: 0x8a8
   __AUTH_CONST.__const: 0x7a0
-  __AUTH_CONST.__cfstring: 0x4200
+  __AUTH_CONST.__cfstring: 0x4340
   __AUTH_CONST.__objc_const: 0xafd8
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_intobj: 0x378
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0xf60
+  __AUTH.__objc_data: 0xe70
   __AUTH.__data: 0x168
   __DATA.__objc_ivar: 0x534
   __DATA.__data: 0x9d0
-  __DATA.__bss: 0x940
+  __DATA.__bss: 0x950
   __DATA.__common: 0x18
-  __DATA_DIRTY.__objc_data: 0x24e8
+  __DATA_DIRTY.__objc_data: 0x25d8
   __DATA_DIRTY.__data: 0xc0
   __DATA_DIRTY.__bss: 0x188
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: C96C10E5-D509-3170-9CF4-8542F3572082
-  Functions: 2447
-  Symbols:   7761
-  CStrings:  3591
+  UUID: DFB6BC42-85C1-3F78-9B18-5E75DDF9469A
+  Functions: 2460
+  Symbols:   7918
+  CStrings:  3574
 
Symbols:
+ +[_DPCoreAnalyticsCollector reportCoreAnalyticsExecutionStageForKey:executionStage:error:count:]
+ +[_DPCoreAnalyticsCollector setTestCollector:]
+ -[_DPBitValueRandomizer randomizeBitValues:forKey:error:]
+ -[_DPBitValueRandomizer randomizeStrings:forKey:error:]
+ -[_DPNumberRandomizer randomizeBitValues:forKey:error:]
+ -[_DPNumberRandomizer randomizeNumbers:forKey:error:]
+ -[_DPNumberRandomizer randomizeStrings:forKey:error:]
+ -[_DPOBHRandomizer randomizeBitValues:forKey:error:]
+ -[_DPOBHRandomizer randomizeStrings:forKey:error:]
+ -[_DPOHEBitValueRandomizer randomizeBitValues:forKey:error:]
+ -[_DPOHEBitValueRandomizer randomizeStrings:forKey:error:]
+ -[_DPPINERandomizer addNoiseToData:metadata:error:]
+ -[_DPPINERandomizer addNoiseToData:metadata:error:].cold.1
+ -[_DPPINERandomizer addNoiseToData:metadata:error:].cold.2
+ -[_DPPINERandomizer addNoiseToData:metadata:error:].cold.3
+ -[_DPPINERandomizer addNoiseToData:metadata:error:].cold.4
+ -[_DPPINERandomizer pineParameterWithMetadata:error:]
+ -[_DPPINERandomizer pineParameterWithMetadata:error:].cold.1
+ -[_DPPINERandomizer pineParameterWithMetadata:error:].cold.2
+ -[_DPPINERandomizer pineParameterWithMetadata:error:].cold.3
+ -[_DPPINERandomizer randomizeFloatVector:metadata:error:]
+ -[_DPPINERandomizer randomizeFloatVector:metadata:error:].cold.1
+ -[_DPPINERandomizer randomizeFloatVector:metadata:error:].cold.2
+ -[_DPPINERandomizer randomizeFloatVector:metadata:error:].cold.3
+ -[_DPPINERandomizer randomizeFloatVectors:metadata:forKey:error:]
+ -[_DPPINERandomizer randomizeFloatVectors:metadata:forKey:error:].cold.1
+ -[_DPPreambleRandomizer randomizeBitValues:metadata:forKey:error:]
+ -[_DPPreambleRandomizer randomizeBitVectors:metadata:forKey:error:]
+ -[_DPPrio3SumVectorRandomizer randomizeBitValues:metadata:forKey:error:]
+ -[_DPPrio3SumVectorRandomizer randomizeBitValues:metadata:forKey:error:].cold.1
+ -[_DPPrio3SumVectorRandomizer randomizeBitValues:metadata:forKey:error:].cold.2
+ -[_DPPrio3SumVectorRandomizer randomizeBitVectors:metadata:forKey:error:]
+ -[_DPPrio3SumVectorRandomizer randomizeBitVectors:metadata:forKey:error:].cold.1
+ -[_DPPrio3SumVectorRandomizer randomizeBitVectors:metadata:forKey:error:].cold.2
+ -[_DPPrioPiRapporValueRandomizer randomizeBitValues:forKey:error:]
+ -[_DPPrioPiRapporValueRandomizer randomizeBitValues:metadata:forKey:error:]
+ -[_DPPrioPiRapporValueRandomizer randomizeBitVectors:metadata:forKey:error:]
+ -[_DPPrioPiRapporValueRandomizer randomizeStrings:forKey:error:]
+ -[_DPPrioPlusPlusMetadataValueRandomizer randomizeBitValues:forKey:error:]
+ -[_DPPrioPlusPlusMetadataValueRandomizer randomizeBitVectors:forKey:error:]
+ -[_DPPrioPlusPlusMetadataValueRandomizer randomizeBitVectors:metadata:forKey:error:]
+ -[_DPPrioPlusPlusMetadataValueRandomizer randomizeStrings:forKey:error:]
+ -[_DPPrioPlusPlusMetricsValueRandomizer randomizeBitValues:forKey:error:]
+ -[_DPPrioPlusPlusMetricsValueRandomizer randomizeFloatVectors:forKey:error:]
+ -[_DPPrioPlusPlusMetricsValueRandomizer randomizeFloatVectors:metadata:forKey:error:]
+ -[_DPPrioPlusPlusMetricsValueRandomizer randomizeStrings:forKey:error:]
+ -[_DPPrioPlusPlusValueRandomizer randomizeBitValues:forKey:error:]
+ -[_DPPrioPlusPlusValueRandomizer randomizeFloatVectors:forKey:error:]
+ -[_DPPrioPlusPlusValueRandomizer randomizeFloatVectors:metadata:forKey:error:]
+ -[_DPPrioPlusPlusValueRandomizer randomizeStrings:forKey:error:]
+ -[_DPPrioValueRandomizer randomizeBitValues:forKey:error:]
+ -[_DPPrioValueRandomizer randomizeBitValues:metadata:forKey:error:]
+ -[_DPPrioValueRandomizer randomizeBitValues:metadata:forKey:error:].cold.1
+ -[_DPPrioValueRandomizer randomizeBitValues:metadata:forKey:error:].cold.2
+ -[_DPPrioValueRandomizer randomizeBitValues:metadata:forKey:error:].cold.3
+ -[_DPPrioValueRandomizer randomizeBitVectors:metadata:forKey:error:]
+ -[_DPPrioValueRandomizer randomizeBitVectors:metadata:forKey:error:].cold.1
+ -[_DPPrioValueRandomizer randomizeBitVectors:metadata:forKey:error:].cold.2
+ -[_DPPrioValueRandomizer randomizeBitVectors:metadata:forKey:error:].cold.3
+ -[_DPPrioValueRandomizer randomizeStrings:forKey:error:]
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_9
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ __ZSt28__throw_bad_array_new_lengthB9foe210106v
+ ___46-[_DPDatabaseRecorder recordStrings:metadata:]_block_invoke.57
+ ___46-[_DPDatabaseRecorder recordStrings:metadata:]_block_invoke.57.cold.1
+ ___67-[_DPPreambleRandomizer randomizeBitVectors:metadata:forKey:error:]_block_invoke
+ ___67-[_DPPreambleRandomizer randomizeBitVectors:metadata:forKey:error:]_block_invoke.cold.1
+ ___67-[_DPPreambleRandomizer randomizeBitVectors:metadata:forKey:error:]_block_invoke.cold.2
+ ___67-[_DPPreambleRandomizer randomizeBitVectors:metadata:forKey:error:]_block_invoke.cold.3
+ ___67-[_DPPreambleRandomizer randomizeBitVectors:metadata:forKey:error:]_block_invoke.cold.4
+ ___74-[_DPDediscoReporter reportToDediscoRecords:forKey:keyProperties:storage:]_block_invoke.35
+ ___74-[_DPDediscoReporter reportToDediscoRecords:forKey:keyProperties:storage:]_block_invoke.35.cold.1
+ ___74-[_DPDediscoReporter reportToDediscoRecords:forKey:keyProperties:storage:]_block_invoke.35.cold.2
+ ___block_descriptor_48_e8_32s40s_e17_v16?0"NSError"8ls32l8s40l8
+ ___block_descriptor_72_e8_32s40s48s56s64r_e23_v32?0"NSData"8Q16^B24lr64l8s32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s_e20_v20?0B8"NSError"12ls32l8s40l8s48l8
+ __testCollector
+ _objc_msgSend$UUIDString
+ _objc_msgSend$addNoiseToData:metadata:error:
+ _objc_msgSend$init
+ _objc_msgSend$pineParameterWithMetadata:error:
+ _objc_msgSend$randomZeroMeanFloatVectorWithLength:stddev:
+ _objc_msgSend$randomizeBitValues:forKey:error:
+ _objc_msgSend$randomizeBitValues:metadata:forKey:error:
+ _objc_msgSend$randomizeBitVectors:forKey:error:
+ _objc_msgSend$randomizeBitVectors:metadata:forKey:error:
+ _objc_msgSend$randomizeFloatVector:metadata:error:
+ _objc_msgSend$randomizeFloatVectors:forKey:error:
+ _objc_msgSend$randomizeFloatVectors:metadata:forKey:error:
+ _objc_msgSend$randomizeNumbers:forKey:error:
+ _objc_msgSend$randomizeNumbers:metadata:forKey:error:
+ _objc_msgSend$randomizeNumbersVectors:forKey:error:
+ _objc_msgSend$randomizeNumbersVectors:metadata:forKey:error:
+ _objc_msgSend$randomizeStrings:forKey:error:
+ _objc_msgSend$randomizeStrings:metadata:forKey:error:
+ _objc_msgSend$reportCoreAnalyticsExecutionStageForKey:executionStage:error:count:
- -[_DPBitValueRandomizer randomizeBitValues:forKey:]
- -[_DPBitValueRandomizer randomizeStrings:forKey:]
- -[_DPDatabaseRecorder reportCoreAnalyticsExecutionStage:key:error:count:]
- -[_DPDediscoReporter reportCoreAnalyticsExecutionStage:error:key:count:]
- -[_DPNumberRandomizer randomizeBitValues:forKey:]
- -[_DPNumberRandomizer randomizeNumbers:forKey:]
- -[_DPNumberRandomizer randomizeStrings:forKey:]
- -[_DPOBHRandomizer randomizeBitValues:forKey:]
- -[_DPOBHRandomizer randomizeStrings:forKey:]
- -[_DPOHEBitValueRandomizer randomizeBitValues:forKey:]
- -[_DPOHEBitValueRandomizer randomizeStrings:forKey:]
- -[_DPPINERandomizer addNoiseToData:metadata:]
- -[_DPPINERandomizer addNoiseToData:metadata:].cold.1
- -[_DPPINERandomizer addNoiseToData:metadata:].cold.2
- -[_DPPINERandomizer addNoiseToData:metadata:].cold.3
- -[_DPPINERandomizer pineParameterWithMetadata:]
- -[_DPPINERandomizer pineParameterWithMetadata:].cold.1
- -[_DPPINERandomizer pineParameterWithMetadata:].cold.2
- -[_DPPINERandomizer randomizeFloatVector:metadata:]
- -[_DPPINERandomizer randomizeFloatVector:metadata:].cold.1
- -[_DPPINERandomizer randomizeFloatVector:metadata:].cold.2
- -[_DPPINERandomizer randomizeFloatVector:metadata:].cold.3
- -[_DPPINERandomizer randomizeFloatVectors:metadata:forKey:]
- -[_DPPINERandomizer randomizeFloatVectors:metadata:forKey:].cold.1
- -[_DPPINERandomizer randomizeFloatVectors:metadata:forKey:].cold.2
- -[_DPPreambleRandomizer randomizeBitValues:metadata:forKey:]
- -[_DPPreambleRandomizer randomizeBitVectors:metadata:forKey:]
- -[_DPPrio3SumVectorRandomizer randomizeBitValues:metadata:forKey:]
- -[_DPPrio3SumVectorRandomizer randomizeBitValues:metadata:forKey:].cold.1
- -[_DPPrio3SumVectorRandomizer randomizeBitValues:metadata:forKey:].cold.2
- -[_DPPrio3SumVectorRandomizer randomizeBitVectors:metadata:forKey:]
- -[_DPPrio3SumVectorRandomizer randomizeBitVectors:metadata:forKey:].cold.1
- -[_DPPrio3SumVectorRandomizer randomizeBitVectors:metadata:forKey:].cold.2
- -[_DPPrioPiRapporValueRandomizer randomizeBitValues:forKey:]
- -[_DPPrioPiRapporValueRandomizer randomizeBitValues:metadata:forKey:]
- -[_DPPrioPiRapporValueRandomizer randomizeBitVectors:metadata:forKey:]
- -[_DPPrioPiRapporValueRandomizer randomizeStrings:forKey:]
- -[_DPPrioPlusPlusMetadataValueRandomizer randomizeBitValues:forKey:]
- -[_DPPrioPlusPlusMetadataValueRandomizer randomizeBitVectors:forKey:]
- -[_DPPrioPlusPlusMetadataValueRandomizer randomizeBitVectors:metadata:forKey:]
- -[_DPPrioPlusPlusMetadataValueRandomizer randomizeStrings:forKey:]
- -[_DPPrioPlusPlusMetricsValueRandomizer randomizeBitValues:forKey:]
- -[_DPPrioPlusPlusMetricsValueRandomizer randomizeFloatVectors:forKey:]
- -[_DPPrioPlusPlusMetricsValueRandomizer randomizeFloatVectors:metadata:forKey:]
- -[_DPPrioPlusPlusMetricsValueRandomizer randomizeStrings:forKey:]
- -[_DPPrioPlusPlusValueRandomizer randomizeBitValues:forKey:]
- -[_DPPrioPlusPlusValueRandomizer randomizeFloatVectors:forKey:]
- -[_DPPrioPlusPlusValueRandomizer randomizeFloatVectors:metadata:forKey:]
- -[_DPPrioPlusPlusValueRandomizer randomizeStrings:forKey:]
- -[_DPPrioValueRandomizer randomizeBitValues:forKey:]
- -[_DPPrioValueRandomizer randomizeBitValues:metadata:forKey:]
- -[_DPPrioValueRandomizer randomizeBitValues:metadata:forKey:].cold.1
- -[_DPPrioValueRandomizer randomizeBitValues:metadata:forKey:].cold.2
- -[_DPPrioValueRandomizer randomizeBitValues:metadata:forKey:].cold.3
- -[_DPPrioValueRandomizer randomizeBitVectors:metadata:forKey:]
- -[_DPPrioValueRandomizer randomizeBitVectors:metadata:forKey:].cold.1
- -[_DPPrioValueRandomizer randomizeBitVectors:metadata:forKey:].cold.2
- -[_DPPrioValueRandomizer randomizeBitVectors:metadata:forKey:].cold.3
- -[_DPPrioValueRandomizer randomizeStrings:forKey:]
- -[_DPServer reportCoreAnalyticsExecutionStage:error:key:count:]
- __ZSt28__throw_bad_array_new_lengthB8ne200100v
- ___46-[_DPDatabaseRecorder recordStrings:metadata:]_block_invoke.56
- ___46-[_DPDatabaseRecorder recordStrings:metadata:]_block_invoke.56.cold.1
- ___61-[_DPPreambleRandomizer randomizeBitVectors:metadata:forKey:]_block_invoke
- ___61-[_DPPreambleRandomizer randomizeBitVectors:metadata:forKey:]_block_invoke.cold.1
- ___61-[_DPPreambleRandomizer randomizeBitVectors:metadata:forKey:]_block_invoke.cold.2
- ___61-[_DPPreambleRandomizer randomizeBitVectors:metadata:forKey:]_block_invoke.cold.3
- ___61-[_DPPreambleRandomizer randomizeBitVectors:metadata:forKey:]_block_invoke.cold.4
- ___74-[_DPDediscoReporter reportToDediscoRecords:forKey:keyProperties:storage:]_block_invoke.52
- ___74-[_DPDediscoReporter reportToDediscoRecords:forKey:keyProperties:storage:]_block_invoke.52.cold.1
- ___74-[_DPDediscoReporter reportToDediscoRecords:forKey:keyProperties:storage:]_block_invoke.52.cold.2
- ___block_descriptor_56_e8_32s40s48s_e17_v16?0"NSError"8ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48s56s_e23_v32?0"NSData"8Q16^B24ls32l8s40l8s48l8s56l8
- ___block_descriptor_80_e8_32s40s48s56s_e20_v20?0B8"NSError"12ls32l8s40l8s48l8s56l8
- _memset
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$addNoiseToData:metadata:
- _objc_msgSend$pineParameterWithMetadata:
- _objc_msgSend$randomizeBitValues:forKey:
- _objc_msgSend$randomizeBitValues:metadata:forKey:
- _objc_msgSend$randomizeBitVectors:forKey:
- _objc_msgSend$randomizeBitVectors:metadata:forKey:
- _objc_msgSend$randomizeFloatVectors:forKey:
- _objc_msgSend$randomizeFloatVectors:metadata:forKey:
- _objc_msgSend$randomizeNumbers:forKey:
- _objc_msgSend$randomizeNumbers:metadata:forKey:
- _objc_msgSend$randomizeNumbersVectors:forKey:
- _objc_msgSend$randomizeNumbersVectors:metadata:forKey:
- _objc_msgSend$randomizeStrings:forKey:
- _objc_msgSend$randomizeStrings:metadata:forKey:
- _objc_msgSend$reportCoreAnalyticsExecutionStage:error:key:count:
- _objc_msgSend$reportCoreAnalyticsExecutionStage:key:error:count:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x3
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x7
- _objc_retain_x9
CStrings:
+ "%@/%@_%@_%@.%@"
+ "/AppleInternal/Library/BuildRoots/4~CH9OugCbzjzGWiYQltZlb6O4i_KGXChAfcmtpYM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__hash_table:1892: libc++ Hardening assertion __p != end() failed: unordered container::erase(iterator) called with a non-dereferenceable iterator\n"
+ "@\"NSArray\"40@0:8@\"NSArray\"16@\"NSString\"24^@32"
+ "@\"NSArray\"48@0:8@\"NSArray\"16@\"NSDictionary\"24@\"NSString\"32^@40"
+ "Bit vector dimension=%lu exceeds limit=%lu"
+ "Fail to add noise to vector with key=%@, error=%@"
+ "Fail to privatize vector with key=%@, error=%@"
+ "Noise generation failed for dimension=%lu, sigma=%f"
+ "UUIDString"
+ "_DPDediscoPrioPiRapporShare"
+ "addNoiseToData:metadata:error:"
+ "pineParameterWithMetadata:error:"
+ "randomizeBitValues:forKey:error:"
+ "randomizeBitValues:metadata:forKey:error:"
+ "randomizeBitVectors:forKey:error:"
+ "randomizeBitVectors:metadata:forKey:error:"
+ "randomizeFloatVector:metadata:error:"
+ "randomizeFloatVectors:forKey:error:"
+ "randomizeFloatVectors:metadata:forKey:error:"
+ "randomizeNumbers:forKey:error:"
+ "randomizeNumbers:metadata:forKey:error:"
+ "randomizeNumbersVectors:forKey:error:"
+ "randomizeNumbersVectors:metadata:forKey:error:"
+ "randomizeStrings:forKey:error:"
+ "randomizeStrings:metadata:forKey:error:"
+ "reportCoreAnalyticsExecutionStageForKey:executionStage:error:count:"
+ "setTestCollector:"
+ "v48@0:8@16Q24@32Q40"
- "%@/%@_%@.%@"
- "@\"NSArray\"32@0:8@\"NSArray\"16@\"NSString\"24"
- "@\"NSArray\"40@0:8@\"NSArray\"16@\"NSDictionary\"24@\"NSString\"32"
- "Fail to add noise to vector with key=%@, continuing..."
- "Fail to privatize vector with key=%@, continuing..."
- "addNoiseToData:metadata:"
- "pineParameterWithMetadata:"
- "randomizeBitValues:forKey:"
- "randomizeBitValues:metadata:forKey:"
- "randomizeBitVectors:forKey:"
- "randomizeBitVectors:metadata:forKey:"
- "randomizeFloatVectors:forKey:"
- "randomizeFloatVectors:metadata:forKey:"
- "randomizeNumbers:forKey:"
- "randomizeNumbers:metadata:forKey:"
- "randomizeNumbersVectors:forKey:"
- "randomizeNumbersVectors:metadata:forKey:"
- "randomizeStrings:forKey:"
- "randomizeStrings:metadata:forKey:"
- "reportCoreAnalyticsExecutionStage:error:key:count:"
- "reportCoreAnalyticsExecutionStage:key:error:count:"
- "v48@0:8Q16@24@32Q40"

```
