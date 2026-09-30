## SpotlightKnowledgeDaemon

> `/System/Library/PrivateFrameworks/SpotlightKnowledgeDaemon.framework/SpotlightKnowledgeDaemon`

```diff

-2465.1.2.0.0
-  __TEXT.__text: 0x48df90
-  __TEXT.__objc_methlist: 0x9600
-  __TEXT.__const: 0x178f8
-  __TEXT.__oslogstring: 0x1296e
-  __TEXT.__cstring: 0x1622e
-  __TEXT.__gcc_except_tab: 0x5a58
+2465.1.3.0.0
+  __TEXT.__text: 0x492098
+  __TEXT.__objc_methlist: 0x9618
+  __TEXT.__const: 0x17a68
+  __TEXT.__oslogstring: 0x12ace
+  __TEXT.__cstring: 0x162f3
+  __TEXT.__gcc_except_tab: 0x5c6c
   __TEXT.__dlopen_cstrs: 0x5e
-  __TEXT.__swift5_typeref: 0xedea
-  __TEXT.__constg_swiftt: 0x90b8
+  __TEXT.__swift5_typeref: 0xee46
+  __TEXT.__constg_swiftt: 0x9188
+  __TEXT.__swift5_reflstr: 0x8d7d
+  __TEXT.__swift5_fieldmd: 0x9194
   __TEXT.__swift5_builtin: 0x244
-  __TEXT.__swift5_reflstr: 0x8d1a
-  __TEXT.__swift5_fieldmd: 0x9130
-  __TEXT.__swift5_assocty: 0x13b0
-  __TEXT.__swift5_capture: 0x38c4
-  __TEXT.__swift5_proto: 0x10ac
-  __TEXT.__swift5_types: 0x8e8
-  __TEXT.__swift_as_entry: 0x488
-  __TEXT.__swift_as_ret: 0x4d8
-  __TEXT.__swift_as_cont: 0x578
-  __TEXT.__swift5_protos: 0x280
+  __TEXT.__swift5_assocty: 0x13e0
+  __TEXT.__swift5_proto: 0x10c4
+  __TEXT.__swift5_types: 0x8f4
+  __TEXT.__swift5_capture: 0x3900
+  __TEXT.__swift_as_entry: 0x498
+  __TEXT.__swift_as_ret: 0x4e0
+  __TEXT.__swift_as_cont: 0x57c
+  __TEXT.__swift5_protos: 0x284
   __TEXT.__swift5_mpenum: 0x94
   __TEXT.__swift5_types2: 0x4
-  __TEXT.__unwind_info: 0xfa38
-  __TEXT.__eh_frame: 0x152d0
+  __TEXT.__unwind_info: 0xf770
+  __TEXT.__eh_frame: 0x158c0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3570
+  __DATA_CONST.__const: 0x35f8
   __DATA_CONST.__objc_classlist: 0x968
   __DATA_CONST.__objc_catlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x1f8
+  __DATA_CONST.__objc_protolist: 0x1f0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5e60
+  __DATA_CONST.__objc_selrefs: 0x5e80
   __DATA_CONST.__objc_protorefs: 0xc0
-  __DATA_CONST.__objc_superrefs: 0x4d8
-  __DATA_CONST.__objc_arraydata: 0x890
-  __DATA_CONST.__got: 0x2338
-  __AUTH_CONST.__const: 0x19588
-  __AUTH_CONST.__cfstring: 0x9260
-  __AUTH_CONST.__objc_const: 0x183c0
+  __DATA_CONST.__objc_superrefs: 0x4d0
+  __DATA_CONST.__objc_arraydata: 0xa30
+  __DATA_CONST.__got: 0x2350
+  __AUTH_CONST.__const: 0x19778
+  __AUTH_CONST.__cfstring: 0x9400
+  __AUTH_CONST.__objc_const: 0x18508
   __AUTH_CONST.__weak_auth_got: 0x18
-  __AUTH_CONST.__objc_intobj: 0x9a8
-  __AUTH_CONST.__objc_arrayobj: 0x588
-  __AUTH_CONST.__objc_dictobj: 0x280
+  __AUTH_CONST.__objc_intobj: 0xb40
+  __AUTH_CONST.__objc_arrayobj: 0x630
+  __AUTH_CONST.__objc_dictobj: 0x2d0
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH_CONST.__auth_got: 0x37e8
-  __AUTH.__objc_data: 0x16e8
-  __AUTH.__data: 0x2bb8
-  __DATA.__objc_ivar: 0xb6c
-  __DATA.__data: 0x3ed0
-  __DATA.__common: 0xe0
-  __DATA_DIRTY.__objc_data: 0x3f00
-  __DATA_DIRTY.__data: 0xc2f8
-  __DATA_DIRTY.__bss: 0x88f0
-  __DATA_DIRTY.__common: 0x380
+  __AUTH_CONST.__auth_got: 0x37f0
+  __AUTH.__objc_data: 0x1648
+  __AUTH.__data: 0x2478
+  __DATA.__objc_ivar: 0xb90
+  __DATA.__data: 0x3560
+  __DATA.__common: 0x58
+  __DATA_DIRTY.__objc_data: 0x3f50
+  __DATA_DIRTY.__data: 0xd608
+  __DATA_DIRTY.__bss: 0x99f0
+  __DATA_DIRTY.__common: 0x408
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreML.framework/CoreML

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 16737
-  Symbols:   14226
-  CStrings:  3753
+  Functions: 16839
+  Symbols:   14269
+  CStrings:  3765
 
Symbols:
+ -[SKDAnalyticsLogger accumulateError:processor:cellKey:status:]
+ -[SKDAnalyticsLogger accumulateModelCounts:context:language:bucket:]
+ -[SKDAnalyticsLogger sendEvents:]
+ -[SKDAnalyticsLogger slotForCellKey:]
+ -[SKDAnalyticsLogger slotForModelCellKey:]
+ -[SKDAnalyticsLogger takeSnapshot:batchCells:replacementCells:]
+ -[SKDLocationResolution _logPIROutcomeWithLocations:error:]
+ -[SKDPipelineFeedback addAddressesCount:]
+ -[SKDPipelineFeedback addBreadcrumbsCount:]
+ -[SKDPipelineFeedback addLocationsCount:]
+ -[SKDPipelineFeedback addPIRCount:]
+ -[SKDPipelineFeedback addressesCount]
+ -[SKDPipelineFeedback setAddressesCount:]
+ -[SKDPipelineFeedback setPIRCount:]
+ -[SKDRecordProcessor(Internal) logBatchFailureForUpdates:info:]
+ -[SKGDataDetector _callPIRWithQuery:errorBlock:useCase:]
+ -[SKGDataDetector _retrieveLocationFromPIR:locale:errorBlock:]
+ -[SKGDataDetector enumerateDetectedDataInString:locale:referenceDate:referenceTimezone:entityBlock:rangeBlock:errorBlock:]
+ -[SKGDataDetector enumerateDetectedDataInString:locale:referenceDate:referenceTimezone:entityCategories:entityBlock:rangeBlock:errorBlock:]
+ -[SKGDataDetector enumerateDetectedLocationsInString:locale:entityBlock:rangeBlock:errorBlock:]
+ -[SKGDataDetector locationFromAddress:locale:errorBlock:]
+ GCC_except_table48
+ _OBJC_IVAR_$_SKDAnalyticsLogger._cellCount
+ _OBJC_IVAR_$_SKDAnalyticsLogger._cellKeys
+ _OBJC_IVAR_$_SKDAnalyticsLogger._cellOverflow
+ _OBJC_IVAR_$_SKDAnalyticsLogger._completedItemCount
+ _OBJC_IVAR_$_SKDAnalyticsLogger._errorKeyCount
+ _OBJC_IVAR_$_SKDAnalyticsLogger._erroredItemCount
+ _OBJC_IVAR_$_SKDAnalyticsLogger._modelCellCount
+ _OBJC_IVAR_$_SKDAnalyticsLogger._modelCellCounts
+ _OBJC_IVAR_$_SKDAnalyticsLogger._modelCellKeys
+ _OBJC_IVAR_$_SKDAnalyticsLogger._modelCellOverflow
+ _OBJC_IVAR_$_SKDAnalyticsLogger._resultCount
+ _OBJC_IVAR_$_SKDPipelineFeedback._addressesCount
+ __DATA__TtC24SpotlightKnowledgeDaemon29GLPInsightsEmbeddingProcessor
+ __IVARS__TtC24SpotlightKnowledgeDaemon29GLPInsightsEmbeddingProcessor
+ __METACLASS_DATA__TtC24SpotlightKnowledgeDaemon29GLPInsightsEmbeddingProcessor
+ __MergedGlobals
+ ___40-[SKDAnalyticsLogSender sendLog:domain:]_block_invoke_2
+ ___56-[SKGDataDetector _callPIRWithQuery:errorBlock:useCase:]_block_invoke
+ ___62-[SKGDataDetector _retrieveLocationFromPIR:locale:errorBlock:]_block_invoke
+ ___62-[SKGDataDetector _retrieveLocationFromPIR:locale:errorBlock:]_block_invoke_2
+ ___62-[SKGDataDetector _retrieveLocationFromPIR:locale:errorBlock:]_block_invoke_3
+ ___76-[SKGDataDetector enumerateAirportCodesInStringUsingGeoScanner:entityBlock:]_block_invoke
+ ___78-[SKDLocationResolution _collectPIRResults:forQuery:locale:completionHandler:]_block_invoke_2
+ ___83-[SKDDataDetector enumerateResultsWithInputs:options:usingBlock:completionHandler:]_block_invoke_4
+ ___89-[SKDLocationResolution enumerateResultsWithInputs:options:usingBlock:completionHandler:]_block_invoke_4
+ ___block_descriptor_112_e8_32s40bs48r56r64r72r80r88r96r_e17_v16?0"NSError"8lr48l8s32l8r56l8s40l8r64l8r72l8r80l8r88l8r96l8
+ ___block_descriptor_48_e8_32bs40r_e17_v16?0"NSError"8lr40l8s32l8
+ ___block_descriptor_64_e8_32s40bs48r56r_e17_v16?0"NSError"8ls32l8r48l8s40l8r56l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e39_v24?0"SKDEntityLocation"8"NSError"16ls32l8s40l8s56l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s56l8s48l8
+ ___block_descriptor_72_e8_32s40bs48r56r64r_e17_v16?0"NSError"8ls32l8r48l8s40l8r56l8r64l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_80_e8_32s40bs48r56r64r_e17_v16?0"NSError"8ls32l8r48l8s40l8r56l8r64l8
+ ___block_descriptor_80_e8_32s40s48bs56r64r72r_e17_v16?0"NSError"8ls32l8r56l8s48l8r64l8s40l8r72l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72bs_e5_v8?0ls32l8s40l8s48l8s56l8s72l8s64l8
+ ___block_descriptor_96_e8_32s40s48bs56r64r72r80r_e17_v16?0"NSError"8ls32l8r56l8s48l8r64l8s40l8r72l8r80l8
+ ___block_descriptor_96_e8_32s40s48s56s64s72bs80r88r_e17_v16?0"NSError"8lr80l8s32l8s40l8s72l8s48l8r88l8s56l8s64l8
+ ___contextIndexFromFeedback_block_invoke
+ ___errorCodeTable_block_invoke
+ ___errorDomainTable_block_invoke
+ ___processorIndexFromIdentifier_block_invoke
+ ___reportPIRError_block_invoke
+ ___swift_exist.box.addr_destructor.789Tm
+ _associated conformance 24SpotlightKnowledgeDaemon39GLPInsightsEmbeddingProcessorDescriptorVAA07CascadefG8ProtocolAA0F0AA0fgI0P_AA0hfI0
+ _associated conformance 24SpotlightKnowledgeDaemon39GLPInsightsEmbeddingProcessorDescriptorVAA0fG8ProtocolAA0F0AaDP_AA0fH0
+ _contextIndexFromFeedback
+ _contextIndexFromFeedback.map
+ _contextIndexFromFeedback.onceToken
+ _errorDomainTable
+ _errorDomainTable.domains
+ _errorDomainTable.onceToken
+ _objc_msgSend$_callPIRWithQuery:errorBlock:useCase:
+ _objc_msgSend$_retrieveLocationFromPIR:locale:errorBlock:
+ _objc_msgSend$addAddressesCount:
+ _objc_msgSend$addBreadcrumbsCount:
+ _objc_msgSend$addLocationsCount:
+ _objc_msgSend$addPIRCount:
+ _objc_msgSend$addressesCount
+ _objc_msgSend$enumerateDetectedDataInString:locale:referenceDate:referenceTimezone:entityBlock:rangeBlock:errorBlock:
+ _objc_msgSend$enumerateDetectedDataInString:locale:referenceDate:referenceTimezone:entityCategories:entityBlock:rangeBlock:errorBlock:
+ _objc_msgSend$enumerateDetectedLocationsInString:locale:entityBlock:rangeBlock:errorBlock:
+ _objc_msgSend$locationFromAddress:locale:errorBlock:
+ _objc_msgSend$logBatchFailureForUpdates:info:
+ _objc_msgSend$setPIRCount:
+ _processorIndexFromIdentifier
+ _processorIndexFromIdentifier.map
+ _processorIndexFromIdentifier.onceToken
+ _reportPIRError
+ _reportPIRError.onceToken
+ _sPIRNoLocationFoundError
+ _sPIRServerErrorNoUnderlying
+ _symbolic $s24SpotlightKnowledgeDaemon22GLPInsightsInterfacingP
+ _symbolic _____ 24SpotlightKnowledgeDaemon20GLPInsightsInterfaceV
+ _symbolic _____ 24SpotlightKnowledgeDaemon29GLPInsightsEmbeddingProcessorC
+ _symbolic _____ 24SpotlightKnowledgeDaemon39GLPInsightsEmbeddingProcessorDescriptorV
+ _symbolic ______p 24SpotlightKnowledgeDaemon22GLPInsightsInterfacingP
- -[SKDAnalyticsErrorKey .cxx_destruct]
- -[SKDAnalyticsErrorKey code]
- -[SKDAnalyticsErrorKey copyWithZone:]
- -[SKDAnalyticsErrorKey domain]
- -[SKDAnalyticsErrorKey hash]
- -[SKDAnalyticsErrorKey initWithDomain:code:]
- -[SKDAnalyticsErrorKey isEqual:]
- -[SKDAnalyticsLogger accumulateError:]
- -[SKDBaseItem initWithIdentifier:status:info:]
- -[SKDPipelineFeedback setPirCount:]
- -[SKDRecordUpdate initWithIdentifier:status:info:]
- -[SKGDataDetector _callPIRWithQuery:hitError:useCase:]
- -[SKGDataDetector _retrieveLocationFromPIR:locale:]
- -[SKGDataDetector enumerateDetectedDataInString:locale:referenceDate:referenceTimezone:entityBlock:rangeBlock:]
- -[SKGDataDetector enumerateDetectedDataInString:locale:referenceDate:referenceTimezone:entityCategories:entityBlock:rangeBlock:]
- -[SKGDataDetector enumerateDetectedLocationsInString:locale:entityBlock:rangeBlock:]
- -[SKGDataDetector locationFromAddress:locale:]
- _OBJC_CLASS_$_SKDAnalyticsErrorKey
- _OBJC_IVAR_$_SKDAnalyticsErrorKey._code
- _OBJC_IVAR_$_SKDAnalyticsErrorKey._domain
- _OBJC_IVAR_$_SKDAnalyticsLogger._processTable
- _OBJC_METACLASS_$_SKDAnalyticsErrorKey
- __OBJC_$_INSTANCE_METHODS_SKDAnalyticsErrorKey
- __OBJC_$_INSTANCE_VARIABLES_SKDAnalyticsErrorKey
- __OBJC_$_PROP_LIST_SKDAnalyticsErrorKey
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying
- __OBJC_CLASS_PROTOCOLS_$_SKDAnalyticsErrorKey
- __OBJC_CLASS_RO_$_SKDAnalyticsErrorKey
- __OBJC_LABEL_PROTOCOL_$_NSCopying
- __OBJC_METACLASS_RO_$_SKDAnalyticsErrorKey
- __OBJC_PROTOCOL_$_NSCopying
- ___51-[SKGDataDetector _retrieveLocationFromPIR:locale:]_block_invoke
- ___51-[SKGDataDetector _retrieveLocationFromPIR:locale:]_block_invoke_2
- ___54-[SKGDataDetector _callPIRWithQuery:hitError:useCase:]_block_invoke
- ___block_descriptor_112_e8_32s40bs48r56r64r72r80r88r96r_e17_v16?0"NSError"8lr48l8s40l8r56l8r64l8s32l8r72l8r80l8r88l8r96l8
- ___block_descriptor_56_e8_32s40s48bs_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s48bs_e39_v24?0"SKDEntityLocation"8"NSError"16ls32l8s48l8s40l8
- ___block_descriptor_64_e8_32s40bs48r56r_e17_v16?0"NSError"8ls40l8r48l8r56l8s32l8
- ___block_descriptor_72_e8_32s40bs48r56r64r_e17_v16?0"NSError"8ls40l8r48l8r56l8s32l8r64l8
- ___block_descriptor_80_e8_32s40bs48r56r64r_e17_v16?0"NSError"8ls40l8r48l8r56l8s32l8r64l8
- ___block_descriptor_80_e8_32s40s48bs56r64r72r_e17_v16?0"NSError"8ls48l8s32l8r56l8s40l8r64l8r72l8
- ___block_descriptor_96_e8_32s40s48bs56r64r72r80r_e17_v16?0"NSError"8ls48l8r56l8s32l8r64l8s40l8r72l8r80l8
- ___block_descriptor_96_e8_32s40s48s56s64s72bs80r88r_e17_v16?0"NSError"8lr80l8s72l8s32l8s40l8s48l8r88l8s56l8s64l8
- ___swift_exist.box.addr_destructor.786Tm
- _objc_msgSend$_callPIRWithQuery:hitError:useCase:
- _objc_msgSend$_retrieveLocationFromPIR:locale:
- _objc_msgSend$enumerateDetectedDataInString:locale:referenceDate:referenceTimezone:entityBlock:rangeBlock:
- _objc_msgSend$enumerateDetectedDataInString:locale:referenceDate:referenceTimezone:entityCategories:entityBlock:rangeBlock:
- _objc_msgSend$enumerateDetectedLocationsInString:locale:entityBlock:rangeBlock:
- _objc_msgSend$initWithDomain:code:
- _objc_msgSend$locationFromAddress:locale:
- _objc_msgSend$setBreadcrumbsCount:
- _objc_msgSend$setPirCount:
- _pipelineIndexFromName.map
- _pipelineIndexFromName.onceToken
CStrings:
+ "SKDAnalyticsLogger: merged cell table saturated at %{public}lu cells; some (processor, context, language, textSize) cells were not reported"
+ "SKDAnalyticsLogger: model cell table saturated at %{public}lu cells; some (model, context, language, textSize) cells were not reported"
+ "SKDDataDetectorsProcessor"
+ "SKDKeyphrasesProcessor"
+ "SKDLocationResolutionProcessor"
+ "SKDTextEmbeddingProcessor"
+ "[GLPInsightsEmbeddingProcessor] Passing through item in set %hu"
+ "[ModelCatalog] AEM version modified, %s to %ld. Requesting MD%ld. Posting notification"
+ "contextName"
+ "glpInsightsEmbedding"
+ "itemCount"
+ "languageType"
+ "modelCount"
+ "modelName"
+ "resultCount"
+ "textContentSize"
- "[ModelCatalog] AEM version modified, %ld to %ld. Posting notification"
- "skd_batch_summary"
- "skd_error_summary"
- "skd_process_summary"
```
