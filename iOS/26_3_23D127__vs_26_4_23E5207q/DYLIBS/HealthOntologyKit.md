## HealthOntologyKit

> `/System/Library/PrivateFrameworks/HealthOntologyKit.framework/HealthOntologyKit`

```diff

-6200.4.9.0.0
-  __TEXT.__text: 0x303a8
-  __TEXT.__auth_stubs: 0xff0
-  __TEXT.__objc_methlist: 0x28c
-  __TEXT.__const: 0x4ca0
-  __TEXT.__cstring: 0x9a1
-  __TEXT.__swift5_typeref: 0xd02
-  __TEXT.__constg_swiftt: 0x11fc
-  __TEXT.__swift5_builtin: 0x8c
-  __TEXT.__swift5_mpenum: 0x28
-  __TEXT.__swift5_reflstr: 0x512
-  __TEXT.__swift5_fieldmd: 0xd3c
-  __TEXT.__swift5_proto: 0x434
-  __TEXT.__swift5_types: 0x138
+6200.5.77.2.6
+  __TEXT.__text: 0x3fae0
+  __TEXT.__auth_stubs: 0x1450
+  __TEXT.__objc_methlist: 0x6ec
+  __TEXT.__const: 0x5b28
+  __TEXT.__gcc_except_tab: 0x4c
+  __TEXT.__cstring: 0x859
+  __TEXT.__oslogstring: 0x618
+  __TEXT.__constg_swiftt: 0x13b4
+  __TEXT.__swift5_typeref: 0xf22
+  __TEXT.__swift5_builtin: 0xb4
+  __TEXT.__swift5_reflstr: 0x69d
+  __TEXT.__swift5_fieldmd: 0xfc4
+  __TEXT.__swift5_assocty: 0x1c8
+  __TEXT.__swift5_proto: 0x520
+  __TEXT.__swift5_types: 0x16c
+  __TEXT.__swift5_capture: 0x200
   __TEXT.__swift5_protos: 0x38
-  __TEXT.__swift5_assocty: 0xf0
-  __TEXT.__oslogstring: 0x1b8
-  __TEXT.__swift5_capture: 0x18c
-  __TEXT.__swift_as_entry: 0x8
-  __TEXT.__swift_as_ret: 0x8
-  __TEXT.__unwind_info: 0x1068
-  __TEXT.__eh_frame: 0x17a8
-  __TEXT.__objc_classname: 0x32
-  __TEXT.__objc_methname: 0x315
-  __TEXT.__objc_methtype: 0x10b
-  __DATA_CONST.__got: 0x2e0
-  __DATA_CONST.__const: 0xd0
-  __DATA_CONST.__objc_classlist: 0x30
-  __DATA_CONST.__objc_protolist: 0x50
+  __TEXT.__swift_as_entry: 0x18
+  __TEXT.__swift_as_ret: 0x10
+  __TEXT.__swift5_mpenum: 0x30
+  __TEXT.__unwind_info: 0x15e8
+  __TEXT.__eh_frame: 0x1d00
+  __TEXT.__objc_classname: 0x391
+  __TEXT.__objc_methname: 0x1067
+  __TEXT.__objc_methtype: 0x64d
+  __TEXT.__objc_stubs: 0x8c0
+  __DATA_CONST.__got: 0x370
+  __DATA_CONST.__const: 0x3c8
+  __DATA_CONST.__objc_classlist: 0x50
+  __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x150
-  __DATA_CONST.__objc_protorefs: 0x30
-  __AUTH_CONST.__auth_got: 0x7f8
-  __AUTH_CONST.__const: 0x2908
-  __AUTH_CONST.__objc_const: 0x748
-  __AUTH.__objc_data: 0x260
-  __AUTH.__data: 0x2d0
-  __DATA.__data: 0x10c0
-  __DATA.__bss: 0x8200
-  __DATA_DIRTY.__data: 0xc0
+  __DATA_CONST.__objc_selrefs: 0x428
+  __DATA_CONST.__objc_protorefs: 0x58
+  __DATA_CONST.__objc_superrefs: 0x20
+  __AUTH_CONST.__auth_got: 0xa38
+  __AUTH_CONST.__const: 0x3170
+  __AUTH_CONST.__cfstring: 0xa0
+  __AUTH_CONST.__objc_const: 0xd38
+  __AUTH.__objc_data: 0x300
+  __AUTH.__data: 0x478
+  __DATA.__objc_ivar: 0x1c
+  __DATA.__data: 0x15a0
+  __DATA.__bss: 0x9e80
+  __DATA.__common: 0x18
+  __DATA_DIRTY.__objc_data: 0xa0
+  __DATA_DIRTY.__data: 0x120
+  __DATA_DIRTY.__bss: 0x80
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/HealthKit.framework/HealthKit

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 1BC30033-33CA-32AD-8D9E-03E95C00A2BF
-  Functions: 1581
-  Symbols:   625
-  CStrings:  150
+  UUID: 29336385-9133-36DF-9D5B-7DAA2D398FFC
+  Functions: 2003
+  Symbols:   1150
+  CStrings:  339
 
Symbols:
+ +[HKConceptQuery clientInterfaceProtocol]
+ +[HKConceptQuery configurationClass]
+ +[HKConceptQuery configureClientInterface:]
+ +[HKConceptQueryConfiguration supportsSecureCoding]
+ +[HKOntologyStore clientInterface]
+ +[HKOntologyStore serverInterface]
+ -[HKConceptQuery .cxx_destruct]
+ -[HKConceptQuery _enumerateConceptsWithHandler:handler:]
+ -[HKConceptQuery client_deliverConcepts:queryUUID:]
+ -[HKConceptQuery initWithConceptSelection:resultsHandler:]
+ -[HKConceptQuery queue_deliverError:]
+ -[HKConceptQuery queue_populateConfiguration:]
+ -[HKConceptQuery queue_queryDidDeactivate:]
+ -[HKConceptQuery queue_validate]
+ -[HKConceptQuery unitTesting_conceptSelection]
+ -[HKConceptQuery unitTesting_handlerWithConcept]
+ -[HKConceptQueryConfiguration .cxx_destruct]
+ -[HKConceptQueryConfiguration copyWithZone:]
+ -[HKConceptQueryConfiguration encodeWithCoder:]
+ -[HKConceptQueryConfiguration initWithCoder:]
+ -[HKConceptQueryConfiguration selection]
+ -[HKConceptQueryConfiguration setSelection:]
+ -[HKOntologyStore .cxx_destruct]
+ -[HKOntologyStore _callUnitTestHookObserving:success:error:]
+ -[HKOntologyStore _handleAutomaticProxyReconnection]
+ -[HKOntologyStore _handleAutomaticProxyReconnection].cold.1
+ -[HKOntologyStore _notifyObserversAboutReconnect]
+ -[HKOntologyStore _observeOntologyStoreChanges:completion:]
+ -[HKOntologyStore _registerFirstObserver]
+ -[HKOntologyStore _synchronouslyRegisterToObserveOntologyStoreChanges:]
+ -[HKOntologyStore _unregisterLastObserver]
+ -[HKOntologyStore client_didImportEntry:]
+ -[HKOntologyStore client_didStageEntry:]
+ -[HKOntologyStore connectionInvalidated]
+ -[HKOntologyStore downloadRequiredShardsWithCompletion:]
+ -[HKOntologyStore exportedInterface]
+ -[HKOntologyStore importRequiredShardsWithCompletion:]
+ -[HKOntologyStore initWithHealthStore:]
+ -[HKOntologyStore init]
+ -[HKOntologyStore insertEntries:completion:]
+ -[HKOntologyStore markShardsWithIdentifiers:options:completion:]
+ -[HKOntologyStore ontologyServerURLWithCompletion:]
+ -[HKOntologyStore ontologyShardRegistryEntriesWithCompletion:]
+ -[HKOntologyStore pruneOntologyWithOptions:completion:]
+ -[HKOntologyStore registerObserver:queue:]
+ -[HKOntologyStore remoteInterface]
+ -[HKOntologyStore requestGatedOntologyUpdateWithCompletion:]
+ -[HKOntologyStore setOntologyServerURL:completion:]
+ -[HKOntologyStore setUnitTesting_didChangeObserverRegistration:]
+ -[HKOntologyStore shardRequirementStatusesWithCompletion:]
+ -[HKOntologyStore unitTest_noOpWithCompletion:]
+ -[HKOntologyStore unitTesting_didChangeObserverRegistration]
+ -[HKOntologyStore unregisterObserver:]
+ -[HKOntologyStore updateOntologyForReason:completion:]
+ -[HKOntologyStore updateOntologyWithAdhocShardImportConfiguration:completion:]
+ -[HKOntologyStore updateOntologyWithEntry:completion:]
+ -[HKOntologyStore updateShardRegistryWithCompletion:]
+ GCC_except_table1
+ GCC_except_table12
+ GCC_except_table68
+ _HKCurrentSchemaVersionForShardIdentifier
+ _HKLogHealthOntology
+ _HKOntologyShardSchemaTypeForShardIdentifier
+ _HKOntologyStoreServerIdentifier
+ _HKStringFromOntologyShardState
+ _NSDebugDescriptionErrorKey
+ _NSInvalidArgumentException
+ _NSLocalizedDescriptionKey
+ _NSStringFromProtocol
+ _NSStringFromSelector
+ _OBJC_CLASS_$_HKConcept
+ _OBJC_CLASS_$_HKConceptQuery
+ _OBJC_CLASS_$_HKConceptQueryConfiguration
+ _OBJC_CLASS_$_HKConceptSelection
+ _OBJC_CLASS_$_HKObserverSet
+ _OBJC_CLASS_$_HKOntologyShardRegistryEntry
+ _OBJC_CLASS_$_HKOntologyStore
+ _OBJC_CLASS_$_HKQuery
+ _OBJC_CLASS_$_HKQueryServerConfiguration
+ _OBJC_CLASS_$_NSError
+ _OBJC_CLASS_$_NSException
+ _OBJC_CLASS_$_NSUUID
+ _OBJC_CLASS_$_OS_dispatch_queue
+ _OBJC_IVAR_$_HKConceptQuery._handler
+ _OBJC_IVAR_$_HKConceptQuery._selection
+ _OBJC_IVAR_$_HKConceptQueryConfiguration._selection
+ _OBJC_IVAR_$_HKOntologyStore._identifier
+ _OBJC_IVAR_$_HKOntologyStore._observers
+ _OBJC_IVAR_$_HKOntologyStore._proxyProvider
+ _OBJC_IVAR_$_HKOntologyStore._unitTesting_didChangeObserverRegistration
+ _OBJC_METACLASS_$_HKConceptQuery
+ _OBJC_METACLASS_$_HKConceptQueryConfiguration
+ _OBJC_METACLASS_$_HKOntologyStore
+ _OBJC_METACLASS_$_HKQuery
+ _OBJC_METACLASS_$_HKQueryServerConfiguration
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _OntologyPluginIdentifier
+ __Block_object_dispose
+ __DATA__TtC17HealthOntologyKit26OntologyShardStateObserver
+ __HKInitializeLogging
+ __HKLogDroppedError
+ __HKQueryValidationFailureException
+ __IVARS__TtC17HealthOntologyKit26OntologyShardStateObserver
+ __METACLASS_DATA__TtC17HealthOntologyKit26OntologyShardStateObserver
+ __OBJC_$_CLASS_METHODS_HKConceptQuery
+ __OBJC_$_CLASS_METHODS_HKConceptQueryConfiguration
+ __OBJC_$_CLASS_METHODS_HKOntologyStore
+ __OBJC_$_INSTANCE_METHODS_HKConceptQuery
+ __OBJC_$_INSTANCE_METHODS_HKConceptQueryConfiguration
+ __OBJC_$_INSTANCE_METHODS_HKOntologyStore
+ __OBJC_$_INSTANCE_METHODS__TtC17HealthOntologyKit26OntologyShardStateObserver(HealthOntologyKit)
+ __OBJC_$_INSTANCE_VARIABLES_HKConceptQuery
+ __OBJC_$_INSTANCE_VARIABLES_HKConceptQueryConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_HKOntologyStore
+ __OBJC_$_PROP_LIST_HKConceptQuery
+ __OBJC_$_PROP_LIST_HKConceptQueryConfiguration
+ __OBJC_$_PROP_LIST_HKOntologyStore
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HKConceptQueryClientInterface
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HKOntologyStoreClientInterface
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HKOntologyStoreObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HKOntologyStoreServerInterface
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HKQueryClientInterface
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HKUnitTestingTaskServerInterface
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HKConceptQueryClientInterface
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HKOntologyStoreClientInterface
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HKOntologyStoreObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HKOntologyStoreServerInterface
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HKQueryClientInterface
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HKUnitTestingTaskServerInterface
+ __OBJC_$_PROTOCOL_REFS_HKConceptQueryClientInterface
+ __OBJC_$_PROTOCOL_REFS_HKOntologyStoreClientInterface
+ __OBJC_$_PROTOCOL_REFS_HKOntologyStoreServerInterface
+ __OBJC_$_PROTOCOL_REFS_HKQueryClientInterface
+ __OBJC_CLASS_PROTOCOLS_$_HKConceptQuery
+ __OBJC_CLASS_PROTOCOLS_$_HKOntologyStore
+ __OBJC_CLASS_PROTOCOLS_$__TtC17HealthOntologyKit26OntologyShardStateObserver(HealthOntologyKit)
+ __OBJC_CLASS_RO_$_HKConceptQuery
+ __OBJC_CLASS_RO_$_HKConceptQueryConfiguration
+ __OBJC_CLASS_RO_$_HKOntologyStore
+ __OBJC_LABEL_PROTOCOL_$_HKConceptQueryClientInterface
+ __OBJC_LABEL_PROTOCOL_$_HKOntologyStoreClientInterface
+ __OBJC_LABEL_PROTOCOL_$_HKOntologyStoreObserver
+ __OBJC_LABEL_PROTOCOL_$_HKOntologyStoreServerInterface
+ __OBJC_LABEL_PROTOCOL_$_HKQueryClientInterface
+ __OBJC_LABEL_PROTOCOL_$_HKUnitTestingTaskServerInterface
+ __OBJC_METACLASS_RO_$_HKConceptQuery
+ __OBJC_METACLASS_RO_$_HKConceptQueryConfiguration
+ __OBJC_METACLASS_RO_$_HKOntologyStore
+ __OBJC_PROTOCOL_$_HKConceptQueryClientInterface
+ __OBJC_PROTOCOL_$_HKOntologyStoreClientInterface
+ __OBJC_PROTOCOL_$_HKOntologyStoreObserver
+ __OBJC_PROTOCOL_$_HKOntologyStoreServerInterface
+ __OBJC_PROTOCOL_$_HKQueryClientInterface
+ __OBJC_PROTOCOL_$_HKUnitTestingTaskServerInterface
+ __OBJC_PROTOCOL_REFERENCE_$_HKConceptQueryClientInterface
+ __OBJC_PROTOCOL_REFERENCE_$_HKOntologyStoreClientInterface
+ __OBJC_PROTOCOL_REFERENCE_$_HKOntologyStoreObserver
+ __OBJC_PROTOCOL_REFERENCE_$_HKOntologyStoreServerInterface
+ __Unwind_Resume
+ ___37-[HKConceptQuery queue_deliverError:]_block_invoke
+ ___38-[HKOntologyStore unregisterObserver:]_block_invoke
+ ___39-[HKOntologyStore initWithHealthStore:]_block_invoke
+ ___40-[HKOntologyStore client_didStageEntry:]_block_invoke
+ ___41-[HKOntologyStore _registerFirstObserver]_block_invoke
+ ___41-[HKOntologyStore _registerFirstObserver]_block_invoke.cold.1
+ ___41-[HKOntologyStore client_didImportEntry:]_block_invoke
+ ___42-[HKOntologyStore _unregisterLastObserver]_block_invoke
+ ___42-[HKOntologyStore registerObserver:queue:]_block_invoke
+ ___44-[HKOntologyStore insertEntries:completion:]_block_invoke
+ ___44-[HKOntologyStore insertEntries:completion:]_block_invoke_2
+ ___47-[HKOntologyStore unitTest_noOpWithCompletion:]_block_invoke
+ ___47-[HKOntologyStore unitTest_noOpWithCompletion:]_block_invoke_2
+ ___49-[HKOntologyStore _notifyObserversAboutReconnect]_block_invoke
+ ___51-[HKConceptQuery client_deliverConcepts:queryUUID:]_block_invoke
+ ___51-[HKConceptQuery client_deliverConcepts:queryUUID:]_block_invoke_2
+ ___51-[HKOntologyStore ontologyServerURLWithCompletion:]_block_invoke
+ ___51-[HKOntologyStore ontologyServerURLWithCompletion:]_block_invoke_2
+ ___51-[HKOntologyStore setOntologyServerURL:completion:]_block_invoke
+ ___51-[HKOntologyStore setOntologyServerURL:completion:]_block_invoke_2
+ ___53-[HKOntologyStore updateShardRegistryWithCompletion:]_block_invoke
+ ___53-[HKOntologyStore updateShardRegistryWithCompletion:]_block_invoke_2
+ ___54-[HKOntologyStore importRequiredShardsWithCompletion:]_block_invoke
+ ___54-[HKOntologyStore importRequiredShardsWithCompletion:]_block_invoke_2
+ ___54-[HKOntologyStore updateOntologyForReason:completion:]_block_invoke
+ ___54-[HKOntologyStore updateOntologyForReason:completion:]_block_invoke_2
+ ___54-[HKOntologyStore updateOntologyWithEntry:completion:]_block_invoke
+ ___54-[HKOntologyStore updateOntologyWithEntry:completion:]_block_invoke_2
+ ___55-[HKOntologyStore pruneOntologyWithOptions:completion:]_block_invoke
+ ___55-[HKOntologyStore pruneOntologyWithOptions:completion:]_block_invoke_2
+ ___56-[HKConceptQuery _enumerateConceptsWithHandler:handler:]_block_invoke
+ ___56-[HKOntologyStore downloadRequiredShardsWithCompletion:]_block_invoke
+ ___56-[HKOntologyStore downloadRequiredShardsWithCompletion:]_block_invoke_2
+ ___58-[HKOntologyStore shardRequirementStatusesWithCompletion:]_block_invoke
+ ___58-[HKOntologyStore shardRequirementStatusesWithCompletion:]_block_invoke_2
+ ___59-[HKOntologyStore _observeOntologyStoreChanges:completion:]_block_invoke
+ ___59-[HKOntologyStore _observeOntologyStoreChanges:completion:]_block_invoke_2
+ ___60-[HKOntologyStore requestGatedOntologyUpdateWithCompletion:]_block_invoke
+ ___60-[HKOntologyStore requestGatedOntologyUpdateWithCompletion:]_block_invoke_2
+ ___62-[HKOntologyStore ontologyShardRegistryEntriesWithCompletion:]_block_invoke
+ ___62-[HKOntologyStore ontologyShardRegistryEntriesWithCompletion:]_block_invoke_2
+ ___64-[HKOntologyStore markShardsWithIdentifiers:options:completion:]_block_invoke
+ ___64-[HKOntologyStore markShardsWithIdentifiers:options:completion:]_block_invoke_2
+ ___71-[HKOntologyStore _synchronouslyRegisterToObserveOntologyStoreChanges:]_block_invoke
+ ___71-[HKOntologyStore _synchronouslyRegisterToObserveOntologyStoreChanges:]_block_invoke_2
+ ___71-[HKOntologyStore _synchronouslyRegisterToObserveOntologyStoreChanges:]_block_invoke_3
+ ___78-[HKOntologyStore updateOntologyWithAdhocShardImportConfiguration:completion:]_block_invoke
+ ___78-[HKOntologyStore updateOntologyWithAdhocShardImportConfiguration:completion:]_block_invoke_2
+ ___Block_byref_object_copy_
+ ___Block_byref_object_dispose_
+ ___CFConstantStringClassReference
+ ___block_descriptor_40_e8_32bs_e17_v16?0"NSError"8ls32l8
+ ___block_descriptor_40_e8_32bs_e42_v16?0"<HKOntologyStoreServerInterface>"8ls32l8
+ ___block_descriptor_40_e8_32r_e17_v16?0"NSError"8lr32l8
+ ___block_descriptor_40_e8_32s_e20_v20?0B8"NSError"12ls32l8
+ ___block_descriptor_40_e8_32s_e35_v16?0"<HKOntologyStoreObserver>"8ls32l8
+ ___block_descriptor_40_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_40_e8_32w_e28_v24?0"HKProxyProvider"816lw32l8
+ ___block_descriptor_41_e8_32bs_e42_v16?0"<HKOntologyStoreServerInterface>"8ls32l8
+ ___block_descriptor_48_e8_32bs_e42_v16?0"<HKOntologyStoreServerInterface>"8ls32l8
+ ___block_descriptor_48_e8_32r40r_e20_v20?0B8"NSError"12lr32l8r40l8
+ ___block_descriptor_48_e8_32r40r_e42_v16?0"<HKOntologyStoreServerInterface>"8lr32l8r40l8
+ ___block_descriptor_48_e8_32s40bs_e42_v16?0"<HKOntologyStoreServerInterface>"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e35_v16?0"<HKOntologyStoreObserver>"8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40bs_e42_v16?0"<HKOntologyStoreServerInterface>"8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48r_e5_v8?0lr48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40bs_e26_v32?0"HKConcept"8Q16^B24ls32l8s40l8
+ ___objc_personality_v0
+ ___stack_chk_fail
+ ___stack_chk_guard
+ ___swift_memcpy72_8
+ ___swift_memcpy88_8
+ __os_log_error_impl
+ _associated conformance 17HealthOntologyKit17HgQLTraversalPathV10CodingKeys33_6E0FFDB0E16AE1AC9B5BC333799C003CLLOSHAASQ
+ _associated conformance 17HealthOntologyKit17HgQLTraversalPathV10CodingKeys33_6E0FFDB0E16AE1AC9B5BC333799C003CLLOs0G3KeyAAs23CustomStringConvertible
+ _associated conformance 17HealthOntologyKit17HgQLTraversalPathV10CodingKeys33_6E0FFDB0E16AE1AC9B5BC333799C003CLLOs0G3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 17HealthOntologyKit17HgQLTraversalPathVSHAASQ
+ _associated conformance 17HealthOntologyKit18ConceptNameRequestV10CodingKeys33_5893165D1B732B459975319B1FF9F1DDLLOSHAASQ
+ _associated conformance 17HealthOntologyKit18ConceptNameRequestV10CodingKeys33_5893165D1B732B459975319B1FF9F1DDLLOs0G3KeyAAs23CustomStringConvertible
+ _associated conformance 17HealthOntologyKit18ConceptNameRequestV10CodingKeys33_5893165D1B732B459975319B1FF9F1DDLLOs0G3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 17HealthOntologyKit18ConceptNameRequestVAA013HgQLDecodableF0AA8ResponseAA0bF0P_AA0ghI0
+ _associated conformance 17HealthOntologyKit18ConceptNameRequestVAA0bF0AA8ResponseAaDP_SE
+ _associated conformance 17HealthOntologyKit18ConceptNameRequestVAA0bF0AA8ResponseAaDP_Se
+ _associated conformance 17HealthOntologyKit18ConceptNameRequestVSHAASQ
+ _associated conformance 17HealthOntologyKit18ConceptNameWrapperV10CodingKeysOSHAASQ
+ _associated conformance 17HealthOntologyKit18ConceptNameWrapperV10CodingKeysOs0G3KeyAAs23CustomStringConvertible
+ _associated conformance 17HealthOntologyKit18ConceptNameWrapperV10CodingKeysOs0G3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 17HealthOntologyKit18ConceptNameWrapperVAA13HgQLDecodableAA0B3RowAaDP_AA0g8QLResultI9Decodable
+ _associated conformance 17HealthOntologyKit18ConceptNameWrapperVSHAASQ
+ _associated conformance 17HealthOntologyKit18ConceptNameWrapperVs12IdentifiableAA2IDsADP_SH
+ _associated conformance 17HealthOntologyKit19ConceptNameResponseV10CodingKeys33_5893165D1B732B459975319B1FF9F1DDLLOSHAASQ
+ _associated conformance 17HealthOntologyKit19ConceptNameResponseV10CodingKeys33_5893165D1B732B459975319B1FF9F1DDLLOs0G3KeyAAs23CustomStringConvertible
+ _associated conformance 17HealthOntologyKit19ConceptNameResponseV10CodingKeys33_5893165D1B732B459975319B1FF9F1DDLLOs0G3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 17HealthOntologyKit19ConceptNameResponseVAA013HgQLDecodableF0AA13DecodableTypeAaDP_AA0gH0
+ _associated conformance 17HealthOntologyKit20ConceptNameResultRowV10CodingKeysOSHAASQ
+ _associated conformance 17HealthOntologyKit20ConceptNameResultRowV10CodingKeysOs0H3KeyAAs23CustomStringConvertible
+ _associated conformance 17HealthOntologyKit20ConceptNameResultRowV10CodingKeysOs0H3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 17HealthOntologyKit20ConceptNameResultRowV10CodingKeysOs12CaseIterableAA8AllCasessAFP_Sl
+ _associated conformance 17HealthOntologyKit20ConceptNameResultRowVSHAASQ
+ _associated conformance So25HKOntologyShardIdentifieraSHSCSQ
+ _associated conformance So25HKOntologyShardIdentifieras20_SwiftNewtypeWrapperSCSY
+ _associated conformance So25HKOntologyShardIdentifieras20_SwiftNewtypeWrapperSCs35_HasCustomAnyHashableRepresentation
+ _dispatch_async
+ _get_witness_table 17HealthOntologyKit15HgQLMatchFilterVAA0D8QLFilterHPyHC.17
+ _get_witness_table 17HealthOntologyKit18HgQLSubgraphFilterVAA0D8QLFilterHPyHC.18
+ _objc_alloc
+ _objc_copyWeak
+ _objc_destroyWeak
+ _objc_initWeak
+ _objc_loadWeakRetained
+ _objc_msgSend$UUID
+ _objc_msgSend$_callUnitTestHookObserving:success:error:
+ _objc_msgSend$_enumerateConceptsWithHandler:handler:
+ _objc_msgSend$_handleAutomaticProxyReconnection
+ _objc_msgSend$_notifyObserversAboutReconnect
+ _objc_msgSend$_observeOntologyStoreChanges:completion:
+ _objc_msgSend$_registerFirstObserver
+ _objc_msgSend$_synchronouslyRegisterToObserveOntologyStoreChanges:
+ _objc_msgSend$_unregisterLastObserver
+ _objc_msgSend$availableState
+ _objc_msgSend$clientInterface
+ _objc_msgSend$clientQueue
+ _objc_msgSend$clientQueueActionHandlerWithCompletion:
+ _objc_msgSend$clientQueueObjectHandlerWithCompletion:
+ _objc_msgSend$copy
+ _objc_msgSend$count
+ _objc_msgSend$currentVersion
+ _objc_msgSend$deactivateCallCount
+ _objc_msgSend$decodeObjectOfClass:forKey:
+ _objc_msgSend$description
+ _objc_msgSend$encodeObject:forKey:
+ _objc_msgSend$enumerateObjectsUsingBlock:
+ _objc_msgSend$fetchProxyWithHandler:errorHandler:
+ _objc_msgSend$getSynchronousProxyWithHandler:errorHandler:
+ _objc_msgSend$hk_setArrayOfClass:forSelector:argumentIndex:ofReply:
+ _objc_msgSend$identifier
+ _objc_msgSend$init
+ _objc_msgSend$initWithDomain:code:userInfo:
+ _objc_msgSend$initWithHealthStore:
+ _objc_msgSend$initWithHealthStore:taskIdentifier:exportedObject:taskUUID:
+ _objc_msgSend$initWithName:loggingCategory:
+ _objc_msgSend$initWithRawIdentifier:
+ _objc_msgSend$interfaceWithProtocol:
+ _objc_msgSend$notifyObservers:
+ _objc_msgSend$ontologyShardRegistryEntriesWithCompletion:
+ _objc_msgSend$ontologyStore:didImportEntry:
+ _objc_msgSend$ontologyStore:didStageEntry:
+ _objc_msgSend$ontologyStoreDidReconnect:
+ _objc_msgSend$preferredName
+ _objc_msgSend$queue
+ _objc_msgSend$queue_dispatchToClientForUUID:shouldDeactivate:block:
+ _objc_msgSend$raise:format:
+ _objc_msgSend$rawIdentifier
+ _objc_msgSend$registerObserver:queue:
+ _objc_msgSend$registerObserver:queue:runIfFirstObserver:
+ _objc_msgSend$remote_downloadRequiredShardsWithCompletion:
+ _objc_msgSend$remote_executeWithRequest:with:
+ _objc_msgSend$remote_importRequiredShardsWithCompletion:
+ _objc_msgSend$remote_insertEntries:completion:
+ _objc_msgSend$remote_markShardsWithIdentifiers:options:completion:
+ _objc_msgSend$remote_observeOntologyStoreChanges:completion:
+ _objc_msgSend$remote_ontologyServerURLWithCompletion:
+ _objc_msgSend$remote_ontologyShardRegistryEntriesWithCompletion:
+ _objc_msgSend$remote_pruneOntologyWithOptions:completion:
+ _objc_msgSend$remote_requestGatedOntologyUpdateWithCompletion:
+ _objc_msgSend$remote_setOntologyServerURL:completion:
+ _objc_msgSend$remote_shardRequirementStatusesWithCompletion:
+ _objc_msgSend$remote_unitTesting_createTaskServerNoOpWithCompletion:
+ _objc_msgSend$remote_updateOntologyForReason:completion:
+ _objc_msgSend$remote_updateOntologyWithConfiguration:completion:
+ _objc_msgSend$remote_updateOntologyWithEntry:completion:
+ _objc_msgSend$remote_updateShardRegistryWithCompletion:
+ _objc_msgSend$schemaType
+ _objc_msgSend$schemaVersion
+ _objc_msgSend$serverInterface
+ _objc_msgSend$setAutomaticProxyReconnectionHandler:
+ _objc_msgSend$setSelection:
+ _objc_msgSend$setShouldRetryOnInterruption:
+ _objc_msgSend$stringValue
+ _objc_msgSend$unregisterObserver:runIfLastObserver:
+ _objc_opt_class
+ _objc_release_x9
+ _objc_retainAutorelease
+ _objc_retainBlock
+ _objc_retain_x1
+ _objc_retain_x21
+ _objc_retain_x23
+ _objc_retain_x24
+ _objc_retain_x4
+ _objc_retain_x8
+ _objc_setProperty_nonatomic_copy
+ _objc_storeStrong
+ _objc_unsafeClaimAutoreleasedReturnValue
+ _objectdestroyTm
+ _swift_arrayInitWithTakeBackToFront
+ _swift_arrayInitWithTakeFrontToBack
+ _swift_bridgeObjectRetain_n
+ _swift_continuation_await
+ _swift_continuation_init
+ _swift_getSingletonMetadata
+ _swift_setDeallocating
+ _swift_task_create
+ _swift_task_isCurrentExecutor
+ _swift_task_reportUnexpectedExecutor
+ _swift_updateClassMetadata2
+ _symbolic $ss12CaseIterableP
+ _symbolic $ss21_ObjectiveCBridgeableP
+ _symbolic SS_Sbt
+ _symbolic Say_____G 17HealthOntologyKit0B17ConceptIdentifierV
+ _symbolic Say_____G 17HealthOntologyKit17HgQLTraversalPathV
+ _symbolic Say_____G 17HealthOntologyKit18ConceptNameWrapperV
+ _symbolic Say_____G 17HealthOntologyKit20ConceptNameResultRowV10CodingKeysO
+ _symbolic Sb
+ _symbolic ScA_pSg
+ _symbolic ScSySbG
+ _symbolic ScSy_____G So20HKOntologyShardStateV
+ _symbolic So15HKOntologyStoreC
+ _symbolic So28HKOntologyShardRegistryEntryC
+ _symbolic So8NSStringC
+ _symbolic _____ 17HealthOntologyKit0B18ShardStateObserverC
+ _symbolic _____ 17HealthOntologyKit17HgQLTraversalPathV
+ _symbolic _____ 17HealthOntologyKit17HgQLTraversalPathV10CodingKeys33_6E0FFDB0E16AE1AC9B5BC333799C003CLLO
+ _symbolic _____ 17HealthOntologyKit18ConceptNameRequestV
+ _symbolic _____ 17HealthOntologyKit18ConceptNameRequestV10CodingKeys33_5893165D1B732B459975319B1FF9F1DDLLO
+ _symbolic _____ 17HealthOntologyKit18ConceptNameWrapperV
+ _symbolic _____ 17HealthOntologyKit18ConceptNameWrapperV10CodingKeysO
+ _symbolic _____ 17HealthOntologyKit19ConceptNameResponseV
+ _symbolic _____ 17HealthOntologyKit19ConceptNameResponseV10CodingKeys33_5893165D1B732B459975319B1FF9F1DDLLO
+ _symbolic _____ 17HealthOntologyKit20ConceptNameResultRowV
+ _symbolic _____ 17HealthOntologyKit20ConceptNameResultRowV10CodingKeysO
+ _symbolic _____ So20HKOntologyShardStateV
+ _symbolic _____ So25HKOntologyShardIdentifiera
+ _symbolic _____Sg 17HealthOntologyKit17HgQLTraversalPathV
+ _symbolic _____XDXMT 17HealthOntologyKit0B18ShardStateObserverC
+ _symbolic _____ySb_G ScS12ContinuationV
+ _symbolic _____y______G ScS12ContinuationV So20HKOntologyShardStateV
+ _symbolic ytIeAgHr_
+ _type_layout_string 17HealthOntologyKit15HgQLMatchFilterV
+ _type_layout_string 17HealthOntologyKit17HgQLTraversalPathV
+ _type_layout_string 17HealthOntologyKit18ConceptNameRequestV
+ _type_layout_string 17HealthOntologyKit18ConceptNameWrapperV
+ _type_layout_string 17HealthOntologyKit19ConceptNameResponseV
+ _type_layout_string 17HealthOntologyKit20ConceptNameResultRowV
+ _type_layout_string So25HKOntologyShardIdentifiera
- ___swift_memcpy48_8
- _get_witness_table 17HealthOntologyKit15HgQLMatchFilterVAA0D8QLFilterHPyHC.11
- _get_witness_table 17HealthOntologyKit18HgQLSubgraphFilterVAA0D8QLFilterHPyHC.12
- _malloc
- _objc_release_x28
- _symbolic SaySay_____GG 17HealthOntologyKit6TripleV
- _symbolic Say_____GSg 17HealthOntologyKit6TripleV
CStrings:
+ "%@ handler must not be nil"
+ "%{public}@: No need to restart observation, because there are no registered observers"
+ "%{public}@: Received notification of successful server reconnection"
+ "%{public}@: Resume observation on server reconnection"
+ "%{public}@: unable to register to observe changes: %{public}@"
+ "%{public}@: unable to unregister observing changes: %{public}@"
+ "@\"HKConceptSelection\""
+ "@\"HKObserverSet<HKOntologyStoreObserver>\""
+ "@\"HKTaskServerProxyProvider\""
+ "@\"NSUUID\""
+ "@24@0:8^{_NSZone=}16"
+ "@32@0:8@16@?24"
+ "@?"
+ "@?16@0:8"
+ "B24@0:8^@16"
+ "ConceptNameOntologyRequest"
+ "Converting DecodingError to XPC-safe NSError: %{public}s"
+ "Failed to decode ontology data"
+ "HKConceptQuery"
+ "HKConceptQueryClientInterface"
+ "HKConceptQueryConfiguration"
+ "HKOntologyStore"
+ "HKOntologyStoreClientInterface"
+ "HKOntologyStoreObserver"
+ "HKOntologyStoreServerIdentifier"
+ "HKOntologyStoreServerInterface"
+ "HKQueryClientInterface"
+ "HKUnitTestingTaskServerInterface"
+ "HealthOntology"
+ "HealthOntologyKit"
+ "HealthOntologyKit/OntologyShardStateObserver.swift"
+ "Selection"
+ "T@\"HKConceptSelection\",C,N,V_selection"
+ "T@\"HKConceptSelection\",R,N"
+ "T@?,C,N,V_unitTesting_didChangeObserverRegistration"
+ "T@?,R,N"
+ "The -%@ method is not available on %@"
+ "Type mismatch for "
+ "UUID"
+ "Unknown decoding error"
+ "Value not found for "
+ "[%{public}@] Failed to resume observation on server reconnection: %{public}@"
+ "[%{public}s] Current %{public}s availability state: %{public}s isImported: %{bool,public}d"
+ "[%{public}s] Did import registry entry: %{sensitive}@"
+ "[%{public}s] Did stage registry entry: %{sensitive}@"
+ "[%{public}s] Failed to find %{public}s shard in registry entries."
+ "[%{public}s] Failed to get ontology shard registry entries, error: %{public}s"
+ "[%{public}s] Querying for ontology shard registry entries."
+ "[%{public}s] Registering for shard updates."
+ "[%{public}s] Shard check override enabled. Skipping registering for shard updates"
+ "[%{public}s] did reconnect to healthd"
+ "_TtC17HealthOntologyKit26OntologyShardStateObserver"
+ "_callUnitTestHookObserving:success:error:"
+ "_createCheckedThrowingContinuation(_:)"
+ "_enumerateConceptsWithHandler:handler:"
+ "_handleAutomaticProxyReconnection"
+ "_handler"
+ "_identifier"
+ "_initWithObjectType:predicate:"
+ "_notifyObserversAboutReconnect"
+ "_observeOntologyStoreChanges:completion:"
+ "_observers"
+ "_proxyProvider"
+ "_registerFirstObserver"
+ "_selection"
+ "_synchronouslyRegisterToObserveOntologyStoreChanges:"
+ "_unitTesting_didChangeObserverRegistration"
+ "_unregisterLastObserver"
+ "availableState"
+ "clientInterface"
+ "clientInterfaceProtocol"
+ "clientQueue"
+ "clientQueueActionHandlerWithCompletion:"
+ "client_deliverConcepts:queryUUID:"
+ "client_deliverError:forQuery:"
+ "client_didImportEntry:"
+ "client_didStageEntry:"
+ "com.apple.health.ontology.decoding"
+ "concept"
+ "configurationClass"
+ "configureClientInterface:"
+ "copy"
+ "copyWithZone:"
+ "count"
+ "currentVersion"
+ "deactivateCallCount"
+ "decodeObjectOfClass:forKey:"
+ "downloadRequiredShardsWithCompletion:"
+ "enumerateObjectsUsingBlock:"
+ "getSynchronousProxyWithHandler:errorHandler:"
+ "grouperPreferredName"
+ "grouperPreferredNameEnUS"
+ "hk_setArrayOfClass:forSelector:argumentIndex:ofReply:"
+ "importRequiredShardsWithCompletion:"
+ "initWithConceptSelection:resultsHandler:"
+ "initWithDomain:code:userInfo:"
+ "initWithHealthStore:"
+ "initWithName:loggingCategory:"
+ "insertEntries:completion:"
+ "isImportedContinuation"
+ "isImportedStream"
+ "markShardsWithIdentifiers:options:completion:"
+ "notifyObservers:"
+ "ontologyServerURLWithCompletion:"
+ "ontologyShardRegistryEntriesWithCompletion:"
+ "ontologyStore:didImportEntry:"
+ "ontologyStore:didStageEntry:"
+ "ontologyStoreDidReconnect:"
+ "preferredNameEnUS"
+ "pruneOntologyWithOptions:completion:"
+ "queue"
+ "queue_deliverError:"
+ "queue_dispatchToClientForUUID:shouldDeactivate:block:"
+ "queue_populateConfiguration:"
+ "queue_queryDidDeactivate:"
+ "queue_validate"
+ "raise:format:"
+ "registerObserver:queue:"
+ "registerObserver:queue:runIfFirstObserver:"
+ "remote_downloadRequiredShardsWithCompletion:"
+ "remote_importRequiredShardsWithCompletion:"
+ "remote_insertEntries:completion:"
+ "remote_markShardsWithIdentifiers:options:completion:"
+ "remote_observeOntologyStoreChanges:completion:"
+ "remote_ontologyServerURLWithCompletion:"
+ "remote_ontologyShardRegistryEntriesWithCompletion:"
+ "remote_pruneOntologyWithOptions:completion:"
+ "remote_requestGatedOntologyUpdateWithCompletion:"
+ "remote_setOntologyServerURL:completion:"
+ "remote_shardRequirementStatusesWithCompletion:"
+ "remote_unitTesting_createTaskServerNoOpWithCompletion:"
+ "remote_updateOntologyForReason:completion:"
+ "remote_updateOntologyWithConfiguration:completion:"
+ "remote_updateOntologyWithEntry:completion:"
+ "remote_updateShardRegistryWithCompletion:"
+ "requestGatedOntologyUpdateWithCompletion:"
+ "schemaType"
+ "schemaVersion"
+ "selection"
+ "serverInterface"
+ "setAutomaticProxyReconnectionHandler:"
+ "setOntologyServerURL:completion:"
+ "setSelection:"
+ "setShouldRetryOnInterruption:"
+ "setUnitTesting_didChangeObserverRegistration:"
+ "shardRequirementStatusesWithCompletion:"
+ "shardStateContinuation"
+ "shardStateStream"
+ "unitTest_noOpWithCompletion:"
+ "unitTesting_conceptSelection"
+ "unitTesting_didChangeObserverRegistration"
+ "unitTesting_handlerWithConcept"
+ "unregisterObserver:"
+ "unregisterObserver:runIfLastObserver:"
+ "updateOntologyForReason:completion:"
+ "updateOntologyWithAdhocShardImportConfiguration:completion:"
+ "updateOntologyWithEntry:completion:"
+ "updateShardRegistryWithCompletion:"
+ "v16@?0@\"<HKOntologyStoreObserver>\"8"
+ "v16@?0@\"<HKOntologyStoreServerInterface>\"8"
+ "v20@?0B8@\"NSError\"12"
+ "v24@0:8@\"HKOntologyShardRegistryEntry\"16"
+ "v24@0:8@\"HKOntologyStore\"16"
+ "v24@0:8@?16"
+ "v24@0:8@?<v@?@\"NSArray\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"NSDictionary\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"NSURL\"@\"NSError\">16"
+ "v24@0:8@?<v@?B@\"NSError\">16"
+ "v24@?0@\"HKProxyProvider\"8@16"
+ "v24@?0@\"NSArray\"8@\"NSError\"16"
+ "v28@0:8B16@?20"
+ "v28@0:8B16@?<v@?B@\"NSError\">20"
+ "v32@0:8@\"HKAdhocShardImportConfiguration\"16@?<v@?B@\"NSError\">24"
+ "v32@0:8@\"HKOntologyShardRegistryEntry\"16@?<v@?B@\"NSError\">24"
+ "v32@0:8@\"HKOntologyStore\"16@\"HKOntologyShardRegistryEntry\"24"
+ "v32@0:8@\"NSArray\"16@\"NSUUID\"24"
+ "v32@0:8@\"NSArray\"16@?<v@?B@\"NSError\">24"
+ "v32@0:8@\"NSError\"16@\"NSUUID\"24"
+ "v32@0:8@\"NSURL\"16@?<v@?B@\"NSError\">24"
+ "v32@0:8@16@24"
+ "v32@0:8B16B20@24"
+ "v32@0:8Q16@?24"
+ "v32@0:8Q16@?<v@?B@\"NSError\">24"
+ "v32@0:8q16@?24"
+ "v32@0:8q16@?<v@?B@\"NSError\">24"
+ "v32@?0@\"HKConcept\"8Q16^B24"
+ "v40@0:8@\"NSArray\"16Q24@?<v@?B@\"NSError\">32"
+ "v40@0:8@16Q24@?32"
+ "v8@?0"

```
