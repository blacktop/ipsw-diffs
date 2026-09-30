## FinHealthInsights

> `/System/Library/PrivateFrameworks/FinHealthInsights.framework/FinHealthInsights`

```diff

-1.7.4.1.0
-  __TEXT.__text: 0xb178
-  __TEXT.__auth_stubs: 0x4e0
-  __TEXT.__objc_methlist: 0x994
-  __TEXT.__const: 0x98
-  __TEXT.__gcc_except_tab: 0x40c
-  __TEXT.__cstring: 0x1535
-  __TEXT.__oslogstring: 0x1de
-  __TEXT.__unwind_info: 0x238
-  __TEXT.__objc_classname: 0x14e
-  __TEXT.__objc_methname: 0x2321
-  __TEXT.__objc_methtype: 0x905
-  __TEXT.__objc_stubs: 0x17e0
-  __DATA_CONST.__got: 0x218
-  __DATA_CONST.__const: 0x3e8
-  __DATA_CONST.__objc_classlist: 0x48
-  __DATA_CONST.__objc_protolist: 0x38
+1.8.1.44.0
+  __TEXT.__text: 0x1f698
+  __TEXT.__auth_stubs: 0xbe0
+  __TEXT.__objc_methlist: 0x664
+  __TEXT.__const: 0x17b2
+  __TEXT.__gcc_except_tab: 0x244
+  __TEXT.__cstring: 0x871
+  __TEXT.__oslogstring: 0x736
+  __TEXT.__swift5_typeref: 0x4a6
+  __TEXT.__swift5_reflstr: 0x3b5
+  __TEXT.__swift5_assocty: 0xc0
+  __TEXT.__constg_swiftt: 0x3c8
+  __TEXT.__swift5_fieldmd: 0x5a8
+  __TEXT.__swift5_proto: 0x170
+  __TEXT.__swift5_types: 0x5c
+  __TEXT.__unwind_info: 0x7c8
+  __TEXT.__eh_frame: 0x738
+  __TEXT.__objc_classname: 0xd6
+  __TEXT.__objc_methname: 0x137a
+  __TEXT.__objc_methtype: 0x26d
+  __TEXT.__objc_stubs: 0xee0
+  __DATA_CONST.__got: 0x258
+  __DATA_CONST.__const: 0x368
+  __DATA_CONST.__objc_classlist: 0x40
+  __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8a8
-  __DATA_CONST.__objc_superrefs: 0x48
-  __DATA_CONST.__objc_arraydata: 0xc8
-  __AUTH_CONST.__auth_got: 0x280
-  __AUTH_CONST.__const: 0x120
-  __AUTH_CONST.__cfstring: 0x1340
-  __AUTH_CONST.__objc_const: 0x1250
-  __AUTH_CONST.__objc_arrayobj: 0x60
-  __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_ivar: 0x80
-  __DATA.__data: 0x2b0
-  __DATA.__bss: 0x28
+  __DATA_CONST.__objc_selrefs: 0x538
+  __DATA_CONST.__objc_superrefs: 0x38
+  __DATA_CONST.__objc_arraydata: 0x38
+  __AUTH_CONST.__auth_got: 0x600
+  __AUTH_CONST.__const: 0xe18
+  __AUTH_CONST.__cfstring: 0x720
+  __AUTH_CONST.__objc_const: 0xba8
+  __AUTH_CONST.__objc_arrayobj: 0x18
+  __AUTH.__objc_data: 0x140
+  __AUTH.__data: 0xd0
+  __DATA.__objc_ivar: 0x58
+  __DATA.__data: 0x4c0
+  __DATA.__bss: 0x3058
+  __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0xf0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/FinHealthCore.framework/FinHealthCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7BC6AF89-F846-3C5E-AAA0-EFE118753F1E
-  Functions: 172
-  Symbols:   897
-  CStrings:  768
+  - /usr/lib/swift/libswiftAVFoundation.dylib
+  - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
+  - /usr/lib/swift/libswiftCoreLocation.dylib
+  - /usr/lib/swift/libswiftCoreMIDI.dylib
+  - /usr/lib/swift/libswiftCoreMedia.dylib
+  - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftIntents.dylib
+  - /usr/lib/swift/libswiftMLCompute.dylib
+  - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  - /usr/lib/swift/libswiftsimd.dylib
+  UUID: 7D488532-A422-36A1-882D-90D16A92F1CA
+  Functions: 774
+  Symbols:   873
+  CStrings:  436
 
Symbols:
+ -[FHInsightsFetcher retrieveSpendInsightsWithStartDate:endDate:insightTypeItems:trendWindow:sourceId:accountType:]
+ -[FHInsightsFetcher totalSpendAmountBetweenDates:endDate:sourceId:accountType:]
+ GCC_except_table5
+ _FHDatabaseQueryJoinTypeInner
+ _OBJC_CLASS_$_FHDatabaseJoinClauseFromBuilder
+ _OBJC_CLASS_$__TtCs12_SwiftObject
+ _OBJC_METACLASS_$__TtCs12_SwiftObject
+ __DATA__TtC17FinHealthInsights12OrderMatcher
+ __METACLASS_DATA__TtC17FinHealthInsights12OrderMatcher
+ ___61-[FHInsightsSpendingTrends _computeCategoryAndMerchantTrends]_block_invoke.122
+ ___61-[FHInsightsSpendingTrends _computeCategoryAndMerchantTrends]_block_invoke.130
+ ___79-[FHInsightsFetcher totalSpendAmountBetweenDates:endDate:sourceId:accountType:]_block_invoke
+ ___79-[FHInsightsFetcher totalSpendAmountBetweenDates:endDate:sourceId:accountType:]_block_invoke_2
+ ___84-[FHInsightsSpendingTrends initWithWeeklyThreshold:monthlyThreshold:merchantCounts:]_block_invoke
+ ___88-[FHInsightsFetcher retrieveInsightsWithStartDate:endDate:insightTypeItems:trendWindow:]_block_invoke.119
+ ___block_descriptor_32_e37_v16?0"FHDatabaseJoinClauseBuilder"8l
+ ___block_descriptor_64_e8_32s40s48s_e33_v16?0"FHDatabaseClauseBuilder"8ls32l8s40l8s48l8
+ ___block_literal_global.109
+ ___block_literal_global.135
+ ___block_literal_global.182
+ ___chkstk_darwin
+ ___swift_destroy_boxed_opaque_existential_0Tm
+ ___swift_destroy_boxed_opaque_existential_1
+ ___swift_instantiateConcreteTypeFromMangledName
+ ___swift_instantiateConcreteTypeFromMangledNameAbstract
+ ___swift_memcpy112_8
+ ___swift_memcpy144_8
+ ___swift_memcpy1_1
+ ___swift_memcpy24_8
+ ___swift_memcpy32_8
+ ___swift_memcpy37_8
+ ___swift_memcpy65_8
+ ___swift_noop_void_return
+ ___swift_project_boxed_opaque_existential_1
+ ___swift_reflection_version
+ __swiftEmptyArrayStorage
+ __swiftEmptyDictionarySingleton
+ __swiftEmptySetSingleton
+ __swiftImmortalRefCount
+ __swift_FORCE_LOAD_$_swiftAVFoundation
+ __swift_FORCE_LOAD_$_swiftAVFoundation_$_FinHealthInsights
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftAccelerate_$_FinHealthInsights
+ __swift_FORCE_LOAD_$_swiftCompression
+ __swift_FORCE_LOAD_$_swiftCompression_$_FinHealthInsights
+ __swift_FORCE_LOAD_$_swiftCoreAudio
+ __swift_FORCE_LOAD_$_swiftCoreAudio_$_FinHealthInsights
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_FinHealthInsights
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftCoreImage_$_FinHealthInsights
+ __swift_FORCE_LOAD_$_swiftCoreLocation
+ __swift_FORCE_LOAD_$_swiftCoreLocation_$_FinHealthInsights
+ __swift_FORCE_LOAD_$_swiftCoreMIDI
+ __swift_FORCE_LOAD_$_swiftCoreMIDI_$_FinHealthInsights
+ __swift_FORCE_LOAD_$_swiftCoreMedia
+ __swift_FORCE_LOAD_$_swiftCoreMedia_$_FinHealthInsights
+ __swift_FORCE_LOAD_$_swiftDarwin
+ __swift_FORCE_LOAD_$_swiftDarwin_$_FinHealthInsights
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftDispatch_$_FinHealthInsights
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation_$_FinHealthInsights
+ __swift_FORCE_LOAD_$_swiftIntents
+ __swift_FORCE_LOAD_$_swiftIntents_$_FinHealthInsights
+ __swift_FORCE_LOAD_$_swiftMLCompute
+ __swift_FORCE_LOAD_$_swiftMLCompute_$_FinHealthInsights
+ __swift_FORCE_LOAD_$_swiftMetal
+ __swift_FORCE_LOAD_$_swiftMetal_$_FinHealthInsights
+ __swift_FORCE_LOAD_$_swiftOSLog
+ __swift_FORCE_LOAD_$_swiftOSLog_$_FinHealthInsights
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_FinHealthInsights
+ __swift_FORCE_LOAD_$_swiftQuartzCore
+ __swift_FORCE_LOAD_$_swiftQuartzCore_$_FinHealthInsights
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers_$_FinHealthInsights
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftXPC_$_FinHealthInsights
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_Builtin_float_$_FinHealthInsights
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_FinHealthInsights
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_FinHealthInsights
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_FinHealthInsights
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftos_$_FinHealthInsights
+ __swift_FORCE_LOAD_$_swiftsimd
+ __swift_FORCE_LOAD_$_swiftsimd_$_FinHealthInsights
+ __swift_stdlib_malloc_size
+ __swift_stdlib_strtod_clocale
+ _associated conformance 17FinHealthInsights11SourceTypesVSHAASQ
+ _associated conformance 17FinHealthInsights11SourceTypesVs10SetAlgebraAASQ
+ _associated conformance 17FinHealthInsights11SourceTypesVs10SetAlgebraAAs25ExpressibleByArrayLiteral
+ _associated conformance 17FinHealthInsights11SourceTypesVs9OptionSetAASY
+ _associated conformance 17FinHealthInsights11SourceTypesVs9OptionSetAAs0G7Algebra
+ _associated conformance 17FinHealthInsights11SourceValueV10CodingKeys33_AD7E66248EE952FEA068A8CB5406DA91LLOyx_GSHAASQ
+ _associated conformance 17FinHealthInsights11SourceValueV10CodingKeys33_AD7E66248EE952FEA068A8CB5406DA91LLOyx_Gs0F3KeyAAs23CustomStringConvertible
+ _associated conformance 17FinHealthInsights11SourceValueV10CodingKeys33_AD7E66248EE952FEA068A8CB5406DA91LLOyx_Gs0F3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 17FinHealthInsights11SourceValueVyxGSHAASQ
+ _associated conformance 17FinHealthInsights11TransactionV10CodingKeys33_AD7E66248EE952FEA068A8CB5406DA91LLOSHAASQ
+ _associated conformance 17FinHealthInsights11TransactionV10CodingKeys33_AD7E66248EE952FEA068A8CB5406DA91LLOs0E3KeyAAs23CustomStringConvertible
+ _associated conformance 17FinHealthInsights11TransactionV10CodingKeys33_AD7E66248EE952FEA068A8CB5406DA91LLOs0E3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 17FinHealthInsights11TransactionVSHAASQ
+ _associated conformance 17FinHealthInsights12OrderMatcherC27SimilarityScoreDimensionKeyOSHAASQ
+ _associated conformance 17FinHealthInsights12OrderMatcherC27SimilarityScoreDimensionKeyOs12CaseIterableAA8AllCasessAFP_Sl
+ _associated conformance 17FinHealthInsights14CurrencyAmountV10CodingKeys33_AD7E66248EE952FEA068A8CB5406DA91LLOSHAASQ
+ _associated conformance 17FinHealthInsights14CurrencyAmountV10CodingKeys33_AD7E66248EE952FEA068A8CB5406DA91LLOs0F3KeyAAs23CustomStringConvertible
+ _associated conformance 17FinHealthInsights14CurrencyAmountV10CodingKeys33_AD7E66248EE952FEA068A8CB5406DA91LLOs0F3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 17FinHealthInsights14CurrencyAmountVSHAASQ
+ _associated conformance 17FinHealthInsights16OrderMatchReasonV10CodingKeys33_13DA7845D051EC7050019FDC064B25ADLLOSHAASQ
+ _associated conformance 17FinHealthInsights16OrderMatchReasonV10CodingKeys33_13DA7845D051EC7050019FDC064B25ADLLOs0G3KeyAAs23CustomStringConvertible
+ _associated conformance 17FinHealthInsights16OrderMatchReasonV10CodingKeys33_13DA7845D051EC7050019FDC064B25ADLLOs0G3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 17FinHealthInsights19ShippingFulfillmentV10CodingKeys33_AD7E66248EE952FEA068A8CB5406DA91LLOSHAASQ
+ _associated conformance 17FinHealthInsights19ShippingFulfillmentV10CodingKeys33_AD7E66248EE952FEA068A8CB5406DA91LLOs0F3KeyAAs23CustomStringConvertible
+ _associated conformance 17FinHealthInsights19ShippingFulfillmentV10CodingKeys33_AD7E66248EE952FEA068A8CB5406DA91LLOs0F3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 17FinHealthInsights19ShippingFulfillmentVSHAASQ
+ _associated conformance 17FinHealthInsights20OrderMatchReasonTypeOSHAASQ
+ _associated conformance 17FinHealthInsights5EmailV0D4TypeOSHAASQ
+ _associated conformance 17FinHealthInsights5EmailV10CodingKeys33_AD7E66248EE952FEA068A8CB5406DA91LLOSHAASQ
+ _associated conformance 17FinHealthInsights5EmailV10CodingKeys33_AD7E66248EE952FEA068A8CB5406DA91LLOs0E3KeyAAs23CustomStringConvertible
+ _associated conformance 17FinHealthInsights5EmailV10CodingKeys33_AD7E66248EE952FEA068A8CB5406DA91LLOs0E3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 17FinHealthInsights5OrderV10CodingKeys33_AD7E66248EE952FEA068A8CB5406DA91LLOSHAASQ
+ _associated conformance 17FinHealthInsights5OrderV10CodingKeys33_AD7E66248EE952FEA068A8CB5406DA91LLOs0E3KeyAAs23CustomStringConvertible
+ _associated conformance 17FinHealthInsights5OrderV10CodingKeys33_AD7E66248EE952FEA068A8CB5406DA91LLOs0E3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 17FinHealthInsights8MerchantV10CodingKeys33_AD7E66248EE952FEA068A8CB5406DA91LLOSHAASQ
+ _associated conformance 17FinHealthInsights8MerchantV10CodingKeys33_AD7E66248EE952FEA068A8CB5406DA91LLOs0E3KeyAAs23CustomStringConvertible
+ _associated conformance 17FinHealthInsights8MerchantV10CodingKeys33_AD7E66248EE952FEA068A8CB5406DA91LLOs0E3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 17FinHealthInsights8MerchantVSHAASQ
+ _bzero
+ _get_enum_tag_for_layout_string 17FinHealthInsights14CurrencyAmountVSg
+ _get_enum_tag_for_layout_string 17FinHealthInsights16OrderMatchReasonVSg
+ _get_witness_table SyRzlSSSyHPyHC.30
+ _malloc_size
+ _memcpy
+ _memmove
+ _objc_allocWithZone
+ _objc_msgSend$addKeyPairsWithJoinType:leftEntity:rightEntity:joinKey:
+ _objc_msgSend$initWithEntity:joinClause:
+ _objc_msgSend$totalSpendAmountBetweenDates:endDate:sourceId:accountType:
+ _objc_opt_self
+ _objc_retainAutoreleasedReturnValue
+ _swift_allocObject
+ _swift_arrayDestroy
+ _swift_arrayInitWithCopy
+ _swift_arrayInitWithTakeBackToFront
+ _swift_arrayInitWithTakeFrontToBack
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRetain
+ _swift_bridgeObjectRetain_n
+ _swift_checkMetadataState
+ _swift_cvw_allocateGenericValueMetadataWithLayoutString
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_deallocClassInstance
+ _swift_errorRelease
+ _swift_getAtKeyPath
+ _swift_getGenericMetadata
+ _swift_getKeyPath
+ _swift_getObjectType
+ _swift_getTypeByMangledNameInContext2
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _swift_getWitnessTable
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_lookUpClassMethod
+ _swift_once
+ _swift_release
+ _swift_retain
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_stdlib_isStackAllocationSafe
+ _swift_unknownObjectRetain
+ _swift_willThrow
+ _symbolic $sSY
+ _symbolic $ss10SetAlgebraP
+ _symbolic $ss12CaseIterableP
+ _symbolic $ss25ExpressibleByArrayLiteralP
+ _symbolic $ss9OptionSetP
+ _symbolic SDySSShy_____y_____GGG 17FinHealthInsights11SourceValueV AA19ShippingFulfillmentV
+ _symbolic SS
+ _symbolic SSSg
+ _symbolic SaySSG
+ _symbolic Say_____G 17FinHealthInsights12OrderMatcherC27SimilarityScoreDimensionKeyO
+ _symbolic Say_____G 17FinHealthInsights5EmailV
+ _symbolic Sb
+ _symbolic SdSg
+ _symbolic SfSg
+ _symbolic Shy_____ySSGG 17FinHealthInsights11SourceValueV
+ _symbolic Shy_____y_____GG 17FinHealthInsights11SourceValueV AA11TransactionV
+ _symbolic Shy_____y_____GG 17FinHealthInsights11SourceValueV AA14CurrencyAmountV
+ _symbolic Shy_____y_____GG 17FinHealthInsights11SourceValueV AA19ShippingFulfillmentV
+ _symbolic Shy_____y_____GG 17FinHealthInsights11SourceValueV AA8MerchantV
+ _symbolic Si
+ _symbolic _____ 17FinHealthInsights11SourceTypesV
+ _symbolic _____ 17FinHealthInsights11SourceValueV
+ _symbolic _____ 17FinHealthInsights11SourceValueV10CodingKeys33_AD7E66248EE952FEA068A8CB5406DA91LLO
+ _symbolic _____ 17FinHealthInsights11TransactionV
+ _symbolic _____ 17FinHealthInsights11TransactionV10CodingKeys33_AD7E66248EE952FEA068A8CB5406DA91LLO
+ _symbolic _____ 17FinHealthInsights12OrderMatcherC
+ _symbolic _____ 17FinHealthInsights12OrderMatcherC27SimilarityScoreDimensionKeyO
+ _symbolic _____ 17FinHealthInsights14CurrencyAmountV
+ _symbolic _____ 17FinHealthInsights14CurrencyAmountV10CodingKeys33_AD7E66248EE952FEA068A8CB5406DA91LLO
+ _symbolic _____ 17FinHealthInsights15MerchantMatcherV
+ _symbolic _____ 17FinHealthInsights16OrderMatchReasonV
+ _symbolic _____ 17FinHealthInsights16OrderMatchReasonV10CodingKeys33_13DA7845D051EC7050019FDC064B25ADLLO
+ _symbolic _____ 17FinHealthInsights18OrderMatchDecisionV
+ _symbolic _____ 17FinHealthInsights19ShippingFulfillmentV
+ _symbolic _____ 17FinHealthInsights19ShippingFulfillmentV10CodingKeys33_AD7E66248EE952FEA068A8CB5406DA91LLO
+ _symbolic _____ 17FinHealthInsights20OrderMatchReasonTypeO
+ _symbolic _____ 17FinHealthInsights5EmailV
+ _symbolic _____ 17FinHealthInsights5EmailV0D4TypeO
+ _symbolic _____ 17FinHealthInsights5EmailV10CodingKeys33_AD7E66248EE952FEA068A8CB5406DA91LLO
+ _symbolic _____ 17FinHealthInsights5OrderV
+ _symbolic _____ 17FinHealthInsights5OrderV10CodingKeys33_AD7E66248EE952FEA068A8CB5406DA91LLO
+ _symbolic _____ 17FinHealthInsights8MerchantV
+ _symbolic _____ 17FinHealthInsights8MerchantV10CodingKeys33_AD7E66248EE952FEA068A8CB5406DA91LLO
+ _symbolic _____ s5UInt8V
+ _symbolic _____Sg 10Foundation4DateV
+ _symbolic _____Sg 17FinHealthInsights14CurrencyAmountV
+ _symbolic _____Sg 17FinHealthInsights16OrderMatchReasonV
+ _symbolic ______AAt 10Foundation4DateV
+ _symbolic ______AAtSg 10Foundation4DateV
+ _symbolic _____ySJG s11_SetStorageC
+ _symbolic _____ySSG 17FinHealthInsights11SourceValueV
+ _symbolic _____ySSG s11_SetStorageC
+ _symbolic _____ySSG s23_ContiguousArrayStorageC
+ _symbolic _____ySSShy_____y_____GGG s18_DictionaryStorageC 17FinHealthInsights11SourceValueV AC19ShippingFulfillmentV
+ _symbolic _____ySdG s23_ContiguousArrayStorageC
+ _symbolic _____ySsG s23_ContiguousArrayStorageC
+ _symbolic _____y_____G 17FinHealthInsights11SourceValueV AA11TransactionV
+ _symbolic _____y_____G 17FinHealthInsights11SourceValueV AA14CurrencyAmountV
+ _symbolic _____y_____G 17FinHealthInsights11SourceValueV AA19ShippingFulfillmentV
+ _symbolic _____y_____G 17FinHealthInsights11SourceValueV AA8MerchantV
+ _symbolic _____y_____G s11_SetStorageC 10Foundation4DateV
+ _symbolic _____y_____G s11_SetStorageC 17FinHealthInsights14CurrencyAmountV
+ _symbolic _____y_____G s22KeyedDecodingContainerV 17FinHealthInsights11TransactionV10CodingKeys33_AD7E66248EE952FEA068A8CB5406DA91LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 17FinHealthInsights14CurrencyAmountV10CodingKeys33_AD7E66248EE952FEA068A8CB5406DA91LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 17FinHealthInsights16OrderMatchReasonV10CodingKeys33_13DA7845D051EC7050019FDC064B25ADLLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 17FinHealthInsights19ShippingFulfillmentV10CodingKeys33_AD7E66248EE952FEA068A8CB5406DA91LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 17FinHealthInsights5EmailV10CodingKeys33_AD7E66248EE952FEA068A8CB5406DA91LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 17FinHealthInsights5OrderV10CodingKeys33_AD7E66248EE952FEA068A8CB5406DA91LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 17FinHealthInsights8MerchantV10CodingKeys33_AD7E66248EE952FEA068A8CB5406DA91LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 17FinHealthInsights11TransactionV10CodingKeys33_AD7E66248EE952FEA068A8CB5406DA91LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 17FinHealthInsights14CurrencyAmountV10CodingKeys33_AD7E66248EE952FEA068A8CB5406DA91LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 17FinHealthInsights16OrderMatchReasonV10CodingKeys33_13DA7845D051EC7050019FDC064B25ADLLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 17FinHealthInsights19ShippingFulfillmentV10CodingKeys33_AD7E66248EE952FEA068A8CB5406DA91LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 17FinHealthInsights5EmailV10CodingKeys33_AD7E66248EE952FEA068A8CB5406DA91LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 17FinHealthInsights5OrderV10CodingKeys33_AD7E66248EE952FEA068A8CB5406DA91LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 17FinHealthInsights8MerchantV10CodingKeys33_AD7E66248EE952FEA068A8CB5406DA91LLO
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 10Foundation4DateV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 17FinHealthInsights14CurrencyAmountV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC s5UInt8V
+ _symbolic _____y_____SfSgG s18_DictionaryStorageC 17FinHealthInsights12OrderMatcherC27SimilarityScoreDimensionKeyO
+ _symbolic x
+ _type_layout_string 17FinHealthInsights11SourceTypesV
+ _type_layout_string 17FinHealthInsights11TransactionV
+ _type_layout_string 17FinHealthInsights16OrderMatchReasonV
+ _type_layout_string 17FinHealthInsights18OrderMatchDecisionV
+ _type_layout_string 17FinHealthInsights5EmailV
+ _type_layout_string 17FinHealthInsights5OrderV
+ _type_layout_string 17FinHealthInsights8MerchantV
- -[FHInferenceController .cxx_destruct]
- -[FHInferenceController _formattedAppleCashTransactionsWithStartDate:endDate:]
- -[FHInferenceController _getAccountsByAccountType:]
- -[FHInferenceController _monthlyHighlightsWithModelId:]
- -[FHInferenceController _monthlyStatementsWithAccountType:sourceIdentifier:]
- -[FHInferenceController _streamBankConnectTransactionsWithSingleQuery:modelId:temperature:delegate:]
- -[FHInferenceController _streamCardTransactionsWithSingleQuery:modelId:temperature:delegate:]
- -[FHInferenceController _streamCashTransactionsWithSingleQuery:modelId:temperature:delegate:error:]
- -[FHInferenceController _summarizationAndStreamWithSingleQuery:modelId:temperature:delegate:]
- -[FHInferenceController _yearlyHighlights]
- -[FHInferenceController acDawTicket]
- -[FHInferenceController accountEntities]
- -[FHInferenceController dateFormatter]
- -[FHInferenceController initWithACDawTicket:]
- -[FHInferenceController monthOnlyDateFormatter]
- -[FHInferenceController numberFormatter]
- -[FHInferenceController queryWithAlternatingRoles:modelId:temperature:completion:]
- -[FHInferenceController selectFieldsForTransactionsAndFeatures]
- -[FHInferenceController setAcDawTicket:]
- -[FHInferenceController setAccountEntities:]
- -[FHInferenceController setDateFormatter:]
- -[FHInferenceController setMonthOnlyDateFormatter:]
- -[FHInferenceController setNumberFormatter:]
- -[FHInferenceController setSelectFieldsForTransactionsAndFeatures:]
- -[FHInferenceController setTransactionAndFeauturesEntities:]
- -[FHInferenceController setTransactionsEntities:]
- -[FHInferenceController streamingBillPaymentInferenceSuggestionWithQuery:accountSummary:modelId:temperature:delegate:]
- -[FHInferenceController streamingHighlightsInferenceResponseWithFollowupQuery:previousResponse:modelId:temperature:delegate:]
- -[FHInferenceController streamingInsightsInferenceResponseWithQuery:modelId:temperature:delegate:error:]
- -[FHInferenceController streamingMerchantProductsAndServicesWithModelId:temperature:delegate:]
- -[FHInferenceController streamingQueryWithAlternatingRoles:modelId:temperature:delegate:]
- -[FHInferenceController transactionAndFeauturesEntities]
- -[FHInferenceController transactionsEntities]
- -[FHInferenceFMAPIClient .cxx_destruct]
- -[FHInferenceFMAPIClient URLSession:dataTask:didReceiveData:]
- -[FHInferenceFMAPIClient URLSession:dataTask:didReceiveResponse:completionHandler:]
- -[FHInferenceFMAPIClient URLSession:didBecomeInvalidWithError:]
- -[FHInferenceFMAPIClient URLSession:task:didCompleteWithError:]
- -[FHInferenceFMAPIClient acDawTicket]
- -[FHInferenceFMAPIClient delegate]
- -[FHInferenceFMAPIClient initWithDelegate:acDawTicket:]
- -[FHInferenceFMAPIClient sendPromptWithAlternatingRoles:modelId:temperature:]
- -[FHInferenceFMAPIClient setAcDawTicket:]
- -[FHInferenceFMAPIClient setDelegate:]
- -[FHInsightsFetcher retrieveSpendInsightsWithStartDate:endDate:insightTypeItems:trendWindow:]
- -[FHInsightsFetcher totalSpendAmountBetweenDates:endDate:]
- GCC_except_table10
- GCC_except_table17
- GCC_except_table2
- GCC_except_table23
- GCC_except_table26
- GCC_except_table4
- _FHAccountInformationTableName
- _FHErrorDomain
- _FHLanguagChatModelURLEndpoint
- _FHLanguageChatModelStreamURLEndpoint
- _FHLanguageModelName1
- _FHLanguageModelName2
- _FHLanguageModelName3
- _FHStartOfYear
- _OBJC_CLASS_$_FHAccount
- _OBJC_CLASS_$_FHInferenceController
- _OBJC_CLASS_$_FHInferenceFMAPIClient
- _OBJC_CLASS_$_NSCalendar
- _OBJC_CLASS_$_NSCharacterSet
- _OBJC_CLASS_$_NSDictionary
- _OBJC_CLASS_$_NSError
- _OBJC_CLASS_$_NSJSONSerialization
- _OBJC_CLASS_$_NSMutableSet
- _OBJC_CLASS_$_NSMutableURLRequest
- _OBJC_CLASS_$_NSNumberFormatter
- _OBJC_CLASS_$_NSOperationQueue
- _OBJC_CLASS_$_NSSet
- _OBJC_CLASS_$_NSTimeZone
- _OBJC_CLASS_$_NSURL
- _OBJC_CLASS_$_NSURLSession
- _OBJC_CLASS_$_NSURLSessionConfiguration
- _OBJC_IVAR_$_FHInferenceController._acDawTicket
- _OBJC_IVAR_$_FHInferenceController._accountEntities
- _OBJC_IVAR_$_FHInferenceController._dateFormatter
- _OBJC_IVAR_$_FHInferenceController._monthOnlyDateFormatter
- _OBJC_IVAR_$_FHInferenceController._numberFormatter
- _OBJC_IVAR_$_FHInferenceController._selectFieldsForTransactionsAndFeatures
- _OBJC_IVAR_$_FHInferenceController._transactionAndFeauturesEntities
- _OBJC_IVAR_$_FHInferenceController._transactionsEntities
- _OBJC_IVAR_$_FHInferenceFMAPIClient._acDawTicket
- _OBJC_IVAR_$_FHInferenceFMAPIClient._delegate
- _OBJC_METACLASS_$_FHInferenceController
- _OBJC_METACLASS_$_FHInferenceFMAPIClient
- __OBJC_$_INSTANCE_METHODS_FHInferenceController
- __OBJC_$_INSTANCE_METHODS_FHInferenceFMAPIClient
- __OBJC_$_INSTANCE_VARIABLES_FHInferenceController
- __OBJC_$_INSTANCE_VARIABLES_FHInferenceFMAPIClient
- __OBJC_$_PROP_LIST_FHInferenceController
- __OBJC_$_PROP_LIST_FHInferenceFMAPIClient
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSURLSessionDataDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSURLSessionDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSURLSessionTaskDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSURLSessionDataDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSURLSessionDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSURLSessionTaskDelegate
- __OBJC_$_PROTOCOL_REFS_NSURLSessionDataDelegate
- __OBJC_$_PROTOCOL_REFS_NSURLSessionDelegate
- __OBJC_$_PROTOCOL_REFS_NSURLSessionTaskDelegate
- __OBJC_CLASS_PROTOCOLS_$_FHInferenceFMAPIClient
- __OBJC_CLASS_RO_$_FHInferenceController
- __OBJC_CLASS_RO_$_FHInferenceFMAPIClient
- __OBJC_LABEL_PROTOCOL_$_NSURLSessionDataDelegate
- __OBJC_LABEL_PROTOCOL_$_NSURLSessionDelegate
- __OBJC_LABEL_PROTOCOL_$_NSURLSessionTaskDelegate
- __OBJC_METACLASS_RO_$_FHInferenceController
- __OBJC_METACLASS_RO_$_FHInferenceFMAPIClient
- __OBJC_PROTOCOL_$_NSURLSessionDataDelegate
- __OBJC_PROTOCOL_$_NSURLSessionDelegate
- __OBJC_PROTOCOL_$_NSURLSessionTaskDelegate
- ___100-[FHInferenceController _streamBankConnectTransactionsWithSingleQuery:modelId:temperature:delegate:]_block_invoke
- ___100-[FHInferenceController _streamBankConnectTransactionsWithSingleQuery:modelId:temperature:delegate:]_block_invoke_2
- ___104-[FHInferenceController streamingInsightsInferenceResponseWithQuery:modelId:temperature:delegate:error:]_block_invoke
- ___104-[FHInferenceController streamingInsightsInferenceResponseWithQuery:modelId:temperature:delegate:error:]_block_invoke.173
- ___51-[FHInferenceController _getAccountsByAccountType:]_block_invoke
- ___58-[FHInsightsFetcher totalSpendAmountBetweenDates:endDate:]_block_invoke
- ___58-[FHInsightsFetcher totalSpendAmountBetweenDates:endDate:]_block_invoke_2
- ___61-[FHInsightsSpendingTrends _computeCategoryAndMerchantTrends]_block_invoke.112
- ___61-[FHInsightsSpendingTrends _computeCategoryAndMerchantTrends]_block_invoke.120
- ___76-[FHInferenceController _monthlyStatementsWithAccountType:sourceIdentifier:]_block_invoke
- ___76-[FHInferenceController _monthlyStatementsWithAccountType:sourceIdentifier:]_block_invoke_2
- ___78-[FHInferenceController _formattedAppleCashTransactionsWithStartDate:endDate:]_block_invoke
- ___78-[FHInferenceController _formattedAppleCashTransactionsWithStartDate:endDate:]_block_invoke_2
- ___78-[FHInferenceController _formattedAppleCashTransactionsWithStartDate:endDate:]_block_invoke_3
- ___82-[FHInferenceController queryWithAlternatingRoles:modelId:temperature:completion:]_block_invoke
- ___88-[FHInsightsFetcher retrieveInsightsWithStartDate:endDate:insightTypeItems:trendWindow:]_block_invoke.110
- ___93-[FHInferenceController _streamCardTransactionsWithSingleQuery:modelId:temperature:delegate:]_block_invoke
- ___93-[FHInferenceController _streamCardTransactionsWithSingleQuery:modelId:temperature:delegate:]_block_invoke_2
- ___93-[FHInferenceController _summarizationAndStreamWithSingleQuery:modelId:temperature:delegate:]_block_invoke
- ___93-[FHInferenceController _summarizationAndStreamWithSingleQuery:modelId:temperature:delegate:]_block_invoke.312
- ___93-[FHInferenceController _summarizationAndStreamWithSingleQuery:modelId:temperature:delegate:]_block_invoke_2
- ___94-[FHInferenceController streamingMerchantProductsAndServicesWithModelId:temperature:delegate:]_block_invoke
- ___block_descriptor_40_e8_32s_e29_q24?0"NSArray"8"NSArray"16ls32l8
- ___block_descriptor_48_e8_32bs40r_e46_v32?0"NSData"8"NSURLResponse"16"NSError"24lr40l8s32l8
- ___block_descriptor_48_e8_32s40r_e18_v16?0"NSString"8lr40l8s32l8
- ___block_descriptor_48_e8_32s_e32_v28?0"NSArray"8"NSArray"16B24ls32l8
- ___block_descriptor_48_e8_32s_e33_v16?0"FHDatabaseClauseBuilder"8ls32l8
- ___block_descriptor_56_e8_32s40s48w_e32_v28?0"NSArray"8"NSArray"16B24lw48l8s32l8s40l8
- ___block_descriptor_76_e8_32s40s48s56r_e5_v8?0lr56l8s32l8s40l8s48l8
- ___block_descriptor_88_e8_32s40s48s56r64r_e5_v8?0ls32l8s40l8r56l8r64l8s48l8
- ___block_descriptor_88_e8_32s40s48s56s64s72r80r_e18_v16?0"NSString"8ls32l8s40l8s48l8s56l8r72l8r80l8s64l8
- ___block_literal_global.125
- ___block_literal_global.172
- ___block_literal_global.267
- ___block_literal_global.301
- ___block_literal_global.405
- ___block_literal_global.426
- ___kCFBooleanFalse
- __dispatch_main_q
- _dispatch_group_create
- _dispatch_group_enter
- _dispatch_group_leave
- _dispatch_group_notify
- _objc_autorelease
- _objc_msgSend$JSONObjectWithData:options:error:
- _objc_msgSend$URLWithString:
- _objc_msgSend$_formattedAppleCashTransactionsWithStartDate:endDate:
- _objc_msgSend$_getAccountsByAccountType:
- _objc_msgSend$_monthlyHighlightsWithModelId:
- _objc_msgSend$_monthlyStatementsWithAccountType:sourceIdentifier:
- _objc_msgSend$_streamBankConnectTransactionsWithSingleQuery:modelId:temperature:delegate:
- _objc_msgSend$_streamCardTransactionsWithSingleQuery:modelId:temperature:delegate:
- _objc_msgSend$_streamCashTransactionsWithSingleQuery:modelId:temperature:delegate:error:
- _objc_msgSend$accountID
- _objc_msgSend$accountType
- _objc_msgSend$allObjects
- _objc_msgSend$arrayWithObjects:count:
- _objc_msgSend$components:fromDate:
- _objc_msgSend$componentsJoinedByString:
- _objc_msgSend$componentsSeparatedByCharactersInSet:
- _objc_msgSend$containsString:
- _objc_msgSend$currentCalendar
- _objc_msgSend$dataTaskWithRequest:
- _objc_msgSend$dataTaskWithRequest:completionHandler:
- _objc_msgSend$dataUsingEncoding:
- _objc_msgSend$dataWithJSONObject:options:error:
- _objc_msgSend$dateFromComponents:
- _objc_msgSend$dateFromString:
- _objc_msgSend$day
- _objc_msgSend$defaultSessionConfiguration
- _objc_msgSend$description
- _objc_msgSend$dictionaryWithObjects:forKeys:count:
- _objc_msgSend$errorWithDomain:code:userInfo:
- _objc_msgSend$inferenceDidBegin
- _objc_msgSend$inferenceDidCompleteWithError:
- _objc_msgSend$inferenceDidFailWithError:
- _objc_msgSend$inferenceDidUpdateTextContent:
- _objc_msgSend$initWithData:encoding:
- _objc_msgSend$initWithDelegate:acDawTicket:
- _objc_msgSend$initWithJoinKey:entities:
- _objc_msgSend$initWithLeftJoinKey:entities:
- _objc_msgSend$initWithString:
- _objc_msgSend$institutionName
- _objc_msgSend$intAtIndex:
- _objc_msgSend$invalidateAndCancel
- _objc_msgSend$length
- _objc_msgSend$localizedDescription
- _objc_msgSend$lowercaseString
- _objc_msgSend$mainQueue
- _objc_msgSend$newlineCharacterSet
- _objc_msgSend$numberWithFloat:
- _objc_msgSend$queryWithAlternatingRoles:modelId:temperature:completion:
- _objc_msgSend$resume
- _objc_msgSend$retrieveSpendInsightsWithStartDate:endDate:insightTypeItems:trendWindow:
- _objc_msgSend$safelyAddObjectToArrayCollection:forKey:
- _objc_msgSend$sendPromptWithAlternatingRoles:modelId:temperature:
- _objc_msgSend$sessionWithConfiguration:
- _objc_msgSend$sessionWithConfiguration:delegate:delegateQueue:
- _objc_msgSend$setAccountDescription:
- _objc_msgSend$setAccountID:
- _objc_msgSend$setAccountType:
- _objc_msgSend$setDateFormat:
- _objc_msgSend$setDay:
- _objc_msgSend$setHTTPBody:
- _objc_msgSend$setHTTPMethod:
- _objc_msgSend$setInstitutionName:
- _objc_msgSend$setPositiveFormat:
- _objc_msgSend$setTimeZone:
- _objc_msgSend$setURL:
- _objc_msgSend$setValue:forHTTPHeaderField:
- _objc_msgSend$setWithArray:
- _objc_msgSend$statusCode
- _objc_msgSend$streamingQueryWithAlternatingRoles:modelId:temperature:delegate:
- _objc_msgSend$stringByReplacingOccurrencesOfString:withString:
- _objc_msgSend$stringFromDate:
- _objc_msgSend$timeZoneForSecondsFromGMT:
- _objc_msgSend$totalSpendAmountBetweenDates:endDate:
- _objc_msgSend$unsignedIntegerValue
- _objc_msgSend$valueForKey:
- _objc_opt_respondsToSelector
- _objc_retain
- _objc_retain_x3
- _objc_retain_x5
- _objc_storeWeak
CStrings:
+ "%s \t score: %f weight: %f"
+ "=== OrderMatcher full match END : FAIL ==="
+ "=== OrderMatcher full match END : PASS ==="
+ "=== OrderMatcher full match START ==="
+ "@64@0:8@16@24@32q40@48q56"
+ "Order 1:%s, Order 2: %s"
+ "\\.(com|net|org)$"
+ "_TtC17FinHealthInsights12OrderMatcher"
+ "addKeyPairsWithJoinType:leftEntity:rightEntity:joinKey:"
+ "amount"
+ "basic match failed: order1(orderNumber:%s, trackingNumber:%s, senderDomain:%s) order2(orderNumber:%s, trackingNumber:%s, senderDomain:%s)"
+ "basic match passed: order1(orderNumber:%s, senderDomain:%s) order2(orderNumbers:%s, senderDomain:%s)"
+ "basic match passed: order1.trackingNumbers:%s order2.trackingNumbers:%s"
+ "dateTime"
+ "defaultShippingFulfillments"
+ "fromEmailAddress"
+ "full match amounts: order1:%s order2:%s"
+ "full match closest date pair: date1:%s date2:%s"
+ "full match converted dateTime: order1:%s order2:%s"
+ "full match dateTime: order1(orderDates:%s dateSent:%s transactionDate:%s) order2(orderDates:%s dateSent:%s transactionDate:%s)"
+ "full match exits because fails to meet security constraints. order number and merchant match: %s tracking number match: %s order number match with length and time difference constraint: %s"
+ "full match exits early because amounts don't match"
+ "full match exits early because merchant names don't match"
+ "full match exits early because of timeDifference=%f date1=%s date2=%s"
+ "full match exits early because orderNumbers don't match"
+ "full match last4digits: order1:%s order2:%s"
+ "full match merchants: order1(merchants:%s transactionDescription:%s) order2(merchants:%s transactionDescription:%s)"
+ "full match orderNumber : order1:%s order2:%s"
+ "heuristics_match"
+ "initWithEntity:joinClause:"
+ "lastFourDigits"
+ "merchantDisplayName"
+ "orderCancellation"
+ "orderConfirmation"
+ "orderTypeIdentifier"
+ "order_number_and_domains_match"
+ "order_number_mismatch"
+ "retrieveSpendInsightsWithStartDate:endDate:insightTypeItems:trendWindow:sourceId:accountType:"
+ "security_constraints_not_pass"
+ "shippingFulfillments"
+ "shippingUpdateFromCarrier"
+ "shippingUpdateFromMerchant"
+ "skip full match because of orderNumber mismatch"
+ "totalCurrencyAmounts"
+ "totalScore: %f intercept: %f threshold:%f"
+ "totalSpendAmountBetweenDates:endDate:sourceId:accountType:"
+ "tracking_numbers_match"
+ "transactionDescription"
+ "v16@?0@\"FHDatabaseJoinClauseBuilder\"8"
+ "yyyy-MM-dd'T'HH:mm:ss.SSSZ"
- ""
- "\n"
- "\n\n######## %@###########\n\n: %@\\n\\n\\n"
- " "
- "  - If the question cannot be assigned to either card or cash category, then the category is Unknown"
- "  - If the question contains AppleCard reference, general spending habits, purchases, spending or general finances or about products/restaurants/services/merchants, then the category is AppleCard"
- "  - If the question is about Debit card, the category is BankConnect"
- "  - If the question is about Discover card, the category is BankConnect"
- "  - If the question is about cash or money sent, received or requested, the category is AppleCash"
- "$"
- "%.2f"
- "%@"
- "%@\n\n\nAppleCard account: <%@>"
- "%@ - %@,%@ - %@,%@,%@,%@\n"
- "%@,%@%@,%@,%@"
- "%@,%@,%@,%@"
- "%@,%@,%@,%@,%@"
- "%@;%@"
- "- %@"
- "- Analyze the query delimited by ```."
- "- Analyze the statement."
- "- Analyze the transactions"
- "- Analyze the transactions."
- "- Answer the following question asked by the user: \"%@\""
- "- Answer the following question asked by the user: \"%@\"."
- "- Answer the question: \"%@\"."
- "- Do not add comments, and only allow bulleted list formatting"
- "- Exclude harmful products or services such as alcohol, tobacco and firearms."
- "- Extract the intent of the question, and assign a category. The intent rules are as follows:"
- "- Find at least 3 products sold or services offered."
- "- Limit your answer to %lu words."
- "- Make sure response is limited to one sentence."
- "- Minimize mathematical operations such as sums or totals, and inform the user that the model has limited support for mathematical operations since it's still in the beta phase."
- "- The output must be human readable and must follow the format: ||merchant name:product1;score1|product2;score2||\n###. Therefore your response must not contain any kind of code in any programming language."
- "- The score range is [0.0 - 0.99999]."
- "0.##"
- "@\"<FHInferenceControllerDelegate>\""
- "@\"NSArray\""
- "@\"NSDateFormatter\""
- "@\"NSNumberFormatter\""
- "@24@0:8Q16"
- "@24@0:8q16"
- "@32@0:8@16@24"
- "@32@0:8q16@24"
- "Accept"
- "AppleCard"
- "AppleCash"
- "BankConnect"
- "Combine the statments for the period %@ - %@ delimited by ``` into one response and include some details."
- "Content-Type"
- "Cookie"
- "Do not add comments."
- "Do not display irrelevant responses or responses that have no significant results."
- "Ensure the user knows that the dates covered are between %@ and %@ due to the current model limitations."
- "FHInferenceController"
- "FHInferenceFMAPIClient"
- "Failed with code: %lu, errorContent: %@, error: %@"
- "Find the top %lu interesting insights from my AppleCard monthly highlights report regardless of date, and make sure the response is less than %lu words. The monthly highlights report is delimited by ```.\nmonthly highlights report:\n\n\n```%@```"
- "If some responses are similar or look like duplicated, combine them into one."
- "If the results span more than one month, display the results in chronological order."
- "JSONObjectWithData:options:error:"
- "MM/dd/yyyy"
- "MMMM yyyy"
- "Make sure the answer is 1 paragraph without formatting, unless the user asks for formatting."
- "NOT (SELF CONTAINS[cd] %@)"
- "NSURLSessionDataDelegate"
- "NSURLSessionDelegate"
- "NSURLSessionTaskDelegate"
- "POST"
- "ROLE_ASSISTANT"
- "ROLE_USER"
- "T@\"<FHInferenceControllerDelegate>\",W,N,V_delegate"
- "T@\"FHDatabaseEntity\",&,N,V_accountEntities"
- "T@\"FHDatabaseEntity\",&,N,V_transactionAndFeauturesEntities"
- "T@\"FHDatabaseEntity\",&,N,V_transactionsEntities"
- "T@\"NSArray\",&,N,V_selectFieldsForTransactionsAndFeatures"
- "T@\"NSDateFormatter\",C,N,V_dateFormatter"
- "T@\"NSDateFormatter\",C,N,V_monthOnlyDateFormatter"
- "T@\"NSNumberFormatter\",&,N,V_numberFormatter"
- "T@\"NSString\",&,N,V_acDawTicket"
- "The AppleCard transactions between %@ and %@ are delimited by ```."
- "Transaction entry : %@"
- "Transactions for \"%@\" between  %@ and %@ : \n ```\n%@\n```\n\n"
- "URLSession:dataTask:didBecomeDownloadTask:"
- "URLSession:dataTask:didBecomeStreamTask:"
- "URLSession:dataTask:didReceiveData:"
- "URLSession:dataTask:didReceiveResponse:completionHandler:"
- "URLSession:dataTask:willCacheResponse:completionHandler:"
- "URLSession:didBecomeInvalidWithError:"
- "URLSession:didCreateTask:"
- "URLSession:didReceiveChallenge:completionHandler:"
- "URLSession:task:didCompleteWithError:"
- "URLSession:task:didFinishCollectingMetrics:"
- "URLSession:task:didReceiveChallenge:completionHandler:"
- "URLSession:task:didReceiveInformationalResponse:"
- "URLSession:task:didSendBodyData:totalBytesSent:totalBytesExpectedToSend:"
- "URLSession:task:needNewBodyStream:"
- "URLSession:task:needNewBodyStreamFromOffset:completionHandler:"
- "URLSession:task:willBeginDelayedRequest:completionHandler:"
- "URLSession:task:willPerformHTTPRedirection:newRequest:completionHandler:"
- "URLSession:taskIsWaitingForConnectivity:"
- "URLSessionDidFinishEventsForBackgroundURLSession:"
- "URLWithString:"
- "You are given an AppleCash statement delimited by ```. Your task is the following:"
- "You are given the names of merchants where a user made some transactions. The merchants are delimited by ```."
- "You are provided with a list of user bank statements separated by ```."
- "Your task is the following:"
- "\\"
- "\\n"
- "_acDawTicket"
- "_accountEntities"
- "_dateFormatter"
- "_delegate"
- "_formattedAppleCashTransactionsWithStartDate:endDate:"
- "_getAccountsByAccountType:"
- "_monthOnlyDateFormatter"
- "_monthlyHighlightsWithModelId:"
- "_monthlyStatementsWithAccountType:sourceIdentifier:"
- "_numberFormatter"
- "_selectFieldsForTransactionsAndFeatures"
- "_streamBankConnectTransactionsWithSingleQuery:modelId:temperature:delegate:"
- "_streamCardTransactionsWithSingleQuery:modelId:temperature:delegate:"
- "_streamCashTransactionsWithSingleQuery:modelId:temperature:delegate:error:"
- "_summarizationAndStreamWithSingleQuery:modelId:temperature:delegate:"
- "_transactionsEntities"
- "_yearlyHighlights"
- "```"
- "acDawTicket"
- "acack=%@"
- "accountEntities"
- "accountID"
- "accountType"
- "allObjects"
- "application/json"
- "arrayWithObjects:count:"
- "components:fromDate:"
- "componentsJoinedByString:"
- "componentsSeparatedByCharactersInSet:"
- "containsString:"
- "content"
- "current period,previous period,amount spent,delta,merchant category\n"
- "currentCalendar"
- "dataTaskWithRequest:"
- "dataTaskWithRequest:completionHandler:"
- "dataUsingEncoding:"
- "dataWithJSONObject:options:error:"
- "date(mm/dd/yyyy),amount,sent/received/requested,phone number\n"
- "dateFormatter"
- "dateFromComponents:"
- "day"
- "defaultSessionConfiguration"
- "delegate"
- "delta"
- "dictionaryWithObjects:forKeys:count:"
- "enable_logging"
- "errorWithDomain:code:userInfo:"
- "fh_account_information.account_description"
- "fh_account_information.account_type"
- "fh_account_information.institution_name"
- "fh_account_information.source_identifier"
- "highlightsContent: %@"
- "inferenceDidBegin"
- "inferenceDidCompleteWithError:"
- "inferenceDidFailWithError:"
- "inferenceDidUpdateTextContent:"
- "initWithACDawTicket:"
- "initWithData:encoding:"
- "initWithDelegate:acDawTicket:"
- "initWithJoinKey:entities:"
- "initWithLeftJoinKey:entities:"
- "initWithString:"
- "institutionName"
- "intAtIndex:"
- "invalidateAndCancel"
- "length"
- "localizedDescription"
- "lowercaseString"
- "mainQueue"
- "merchant name,amount,transaction date,merchant category"
- "merchants:\n```\n%@\n```"
- "messages"
- "model"
- "modelId: %lu, temperature: %f"
- "monthOnlyDateFormatter"
- "monthlyHighlight: %@"
- "n/a"
- "newlineCharacterSet"
- "numberFormatter"
- "numberWithFloat:"
- "options"
- "q24@?0@\"NSArray\"8@\"NSArray\"16"
- "query:```%@```"
- "queryWithAlternatingRoles:modelId:temperature:completion:"
- "received"
- "requested"
- "response: %@"
- "result"
- "resume"
- "retrieveSpendInsightsWithStartDate:endDate:insightTypeItems:trendWindow:"
- "role"
- "safelyAddObjectToArrayCollection:forKey:"
- "selectFieldsForTransactionsAndFeatures"
- "sendPromptWithAlternatingRoles:modelId:temperature:"
- "sent"
- "sessionWithConfiguration:"
- "sessionWithConfiguration:delegate:delegateQueue:"
- "setAcDawTicket:"
- "setAccountDescription:"
- "setAccountEntities:"
- "setAccountID:"
- "setAccountType:"
- "setDateFormatter:"
- "setDay:"
- "setDelegate:"
- "setHTTPBody:"
- "setHTTPMethod:"
- "setInstitutionName:"
- "setMonthOnlyDateFormatter:"
- "setNumberFormatter:"
- "setPositiveFormat:"
- "setSelectFieldsForTransactionsAndFeatures:"
- "setTimeZone:"
- "setTransactionsEntities:"
- "setURL:"
- "setValue:forHTTPHeaderField:"
- "setWithArray:"
- "statement:```%@```"
- "statements: ```%@```"
- "statusCode"
- "streamingBillPaymentInferenceSuggestionWithQuery:accountSummary:modelId:temperature:delegate:"
- "streamingHighlightsInferenceResponseWithFollowupQuery:previousResponse:modelId:temperature:delegate:"
- "streamingInsightsInferenceResponseWithQuery:modelId:temperature:delegate:error:"
- "streamingMerchantProductsAndServicesWithModelId:temperature:delegate:"
- "streamingQueryWithAlternatingRoles:modelId:temperature:delegate:"
- "stringByReplacingOccurrencesOfString:withString:"
- "stringFromDate:"
- "temperature"
- "timeZoneForSecondsFromGMT:"
- "totalSpendAmountBetweenDates:endDate:"
- "transactions.m_name"
- "transactions.peer_pay_counterpart"
- "transactions.peer_pay_is_recurring"
- "transactions.peer_pay_type"
- "transactions.t_description"
- "transactions: ```"
- "transactionsEntities"
- "unsignedIntegerValue"
- "userMessage: %@, response: %@"
- "userMessageContents: %@"
- "v16@?0@\"NSString\"8"
- "v24@0:8@\"NSURLSession\"16"
- "v32@0:8@\"NSURLSession\"16@\"NSError\"24"
- "v32@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24"
- "v32@0:8@16@24"
- "v32@?0@\"NSData\"8@\"NSURLResponse\"16@\"NSError\"24"
- "v36@0:8@16q24f32"
- "v36@0:8q16f24@28"
- "v40@0:8@\"NSURLSession\"16@\"NSURLAuthenticationChallenge\"24@?<v@?q@\"NSURLCredential\">32"
- "v40@0:8@\"NSURLSession\"16@\"NSURLSessionDataTask\"24@\"NSData\"32"
- "v40@0:8@\"NSURLSession\"16@\"NSURLSessionDataTask\"24@\"NSURLSessionDownloadTask\"32"
- "v40@0:8@\"NSURLSession\"16@\"NSURLSessionDataTask\"24@\"NSURLSessionStreamTask\"32"
- "v40@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSError\"32"
- "v40@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSHTTPURLResponse\"32"
- "v40@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSURLSessionTaskMetrics\"32"
- "v40@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@?<v@?@\"NSInputStream\">32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24@?32"
- "v44@0:8@16q24f32@36"
- "v44@0:8@16q24f32@?36"
- "v48@0:8@\"NSURLSession\"16@\"NSURLSessionDataTask\"24@\"NSCachedURLResponse\"32@?<v@?@\"NSCachedURLResponse\">40"
- "v48@0:8@\"NSURLSession\"16@\"NSURLSessionDataTask\"24@\"NSURLResponse\"32@?<v@?q>40"
- "v48@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSURLAuthenticationChallenge\"32@?<v@?q@\"NSURLCredential\">40"
- "v48@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSURLRequest\"32@?<v@?q@\"NSURLRequest\">40"
- "v48@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24q32@?<v@?@\"NSInputStream\">40"
- "v48@0:8@16@24@32@?40"
- "v48@0:8@16@24q32@?40"
- "v48@0:8@16Q24d32@40"
- "v52@0:8@16@24q32f40@44"
- "v52@0:8@16q24f32@36^@44"
- "v56@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSHTTPURLResponse\"32@\"NSURLRequest\"40@?<v@?@\"NSURLRequest\">48"
- "v56@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24q32q40q48"
- "v56@0:8@16@24@32@40@?48"
- "v56@0:8@16@24q32q40q48"
- "valueForKey:"
- "yearlyHighlight: %@"

```
