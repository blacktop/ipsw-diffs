## CoreSpotlight

> `/System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight`

```diff

-2465.2.7.101.0
-  __TEXT.__text: 0x17aee4
-  __TEXT.__objc_methlist: 0x148d8
-  __TEXT.__const: 0xf38
-  __TEXT.__cstring: 0x2bf4b
-  __TEXT.__gcc_except_tab: 0x9758
-  __TEXT.__oslogstring: 0xc1b5
-  __TEXT.__ustring: 0x218e
+2465.2.13.0.0
+  __TEXT.__text: 0x184b3c
+  __TEXT.__objc_methlist: 0x14db0
+  __TEXT.__const: 0xfa8
+  __TEXT.__cstring: 0x2c155
+  __TEXT.__gcc_except_tab: 0xa664
+  __TEXT.__oslogstring: 0xc332
+  __TEXT.__ustring: 0x2192
   __TEXT.__dlopen_cstrs: 0x4c4
   __TEXT.__constg_swiftt: 0x1bc
   __TEXT.__swift5_typeref: 0x2ba

   __TEXT.__swift_as_cont: 0xc
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x7310
+  __TEXT.__unwind_info: 0x7820
   __TEXT.__eh_frame: 0x210
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x67b8
-  __DATA_CONST.__objc_classlist: 0xac0
+  __DATA_CONST.__const: 0x68d0
+  __DATA_CONST.__objc_classlist: 0xad8
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa6c8
+  __DATA_CONST.__objc_selrefs: 0xa928
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x750
-  __DATA_CONST.__objc_arraydata: 0x11290
-  __DATA_CONST.__got: 0xe88
-  __AUTH_CONST.__const: 0x2450
-  __AUTH_CONST.__cfstring: 0x2e160
-  __AUTH_CONST.__objc_const: 0x20370
-  __AUTH_CONST.__weak_auth_got: 0x10
-  __AUTH_CONST.__objc_arrayobj: 0x3ae0
+  __DATA_CONST.__objc_superrefs: 0x768
+  __DATA_CONST.__objc_arraydata: 0x112f0
+  __DATA_CONST.__got: 0xeb0
+  __AUTH_CONST.__const: 0x2598
+  __AUTH_CONST.__cfstring: 0x2e460
+  __AUTH_CONST.__objc_const: 0x20910
+  __AUTH_CONST.__weak_auth_got: 0x20
+  __AUTH_CONST.__objc_arrayobj: 0x3b10
   __AUTH_CONST.__objc_dictobj: 0xaf78
   __AUTH_CONST.__objc_intobj: 0xe58
   __AUTH_CONST.__objc_doubleobj: 0x180
   __AUTH_CONST.__objc_floatobj: 0x20
-  __AUTH_CONST.__auth_got: 0x1190
-  __AUTH.__objc_data: 0x57f8
+  __AUTH_CONST.__auth_got: 0x11d0
+  __AUTH.__objc_data: 0x58e8
   __AUTH.__data: 0x3a0
   __AUTH.__thread_vars: 0x60
   __AUTH.__thread_bss: 0x28
-  __DATA.__objc_ivar: 0x1498
+  __DATA.__objc_ivar: 0x14f8
   __DATA.__data: 0x1c60
   __DATA_DIRTY.__objc_data: 0x1388
   __DATA_DIRTY.__data: 0x20

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 8993
-  Symbols:   14753
-  CStrings:  8117
+  Functions: 9215
+  Symbols:   15103
+  CStrings:  8143
 
Symbols:
+ +[_CSAgenticQuery _searchableItemsFromRows:]
+ +[_CSHydrationReadRoot rootWithScope:]
+ +[_CSSearchPipelineExecutor applyAttributeLifting:]
+ +[_CSSearchPipelineExecutor applyAttributeLiftingReturningVisitCount:]
+ +[_CSSearchPipelineExecutor contextForStage:stageResults:stageMap:attributeTranslator:customStageHandler:promptedStageHandler:searchableIndex:boundVariables:]
+ +[_CSSearchPipelineExecutor executeNextStage:index:stageResults:stageMap:attributeTranslator:customStageHandler:promptedStageHandler:searchableIndex:boundVariables:rowKinds:extractValueConfigs:completion:]
+ +[_CSSearchPipelineExecutor resolveRunTypesForStage:rowKinds:runInput:runOutput:]
+ +[_CSSearchPipelineExecutor rowErrorForStage:runOutput:result:kind:]
+ +[_CSSearchPipelineExecutor storeResult:forStageId:stageResults:boundVariables:extractValueConfigs:]
+ +[_CSSearchPipelineStage queryStageWithId:queryString:queryOperation:fetchedAttributes:rankingConfiguration:limit:inputStageId:extractValue:preservesLimit:]
+ +[_CSStringPredicate slowScanningSuffixPredicateWithAttribute:operator:stringValue:caseSensitive:diacriticsSensitive:wordBased:tokenize:]
+ -[_CSAgenticQuery _applyResumeCursorForQuery:error:]
+ -[_CSAgenticQuery _claimStart]
+ -[_CSAgenticQuery _deliverCompletion:]
+ -[_CSAgenticQuery _deliverFoundItems:]
+ -[_CSAgenticQuery _finishWithoutQueries]
+ -[_CSAgenticQuery _isCancelled]
+ -[_CSAgenticQuery _registerActiveQueries:]
+ -[_CSAgenticQueryConfiguration customStageHandler]
+ -[_CSAgenticQueryConfiguration fileScopes]
+ -[_CSAgenticQueryConfiguration promptedStageHandler]
+ -[_CSAgenticQueryConfiguration setCustomStageHandler:]
+ -[_CSAgenticQueryConfiguration setFileScopes:]
+ -[_CSAgenticQueryConfiguration setPromptedStageHandler:]
+ -[_CSAttributeLiftingGraph .cxx_destruct]
+ -[_CSAttributeLiftingGraph addNames:toQueryStage:]
+ -[_CSAttributeLiftingGraph admitFreeFormName:toSet:freeForm:stage:]
+ -[_CSAttributeLiftingGraph contained:]
+ -[_CSAttributeLiftingGraph dependencyIdsOfStage:]
+ -[_CSAttributeLiftingGraph expand:names:frontier:]
+ -[_CSAttributeLiftingGraph indexStageIds]
+ -[_CSAttributeLiftingGraph initWithStages:]
+ -[_CSAttributeLiftingGraph liftExtractionConfigs:]
+ -[_CSAttributeLiftingGraph liftMap:]
+ -[_CSAttributeLiftingGraph liftNames:fromSource:]
+ -[_CSAttributeLiftingGraph liftRequirementsOfStage:]
+ -[_CSAttributeLiftingGraph liftableNames:]
+ -[_CSAttributeLiftingGraph lifted]
+ -[_CSAttributeLiftingGraph pop:]
+ -[_CSAttributeLiftingGraph push:crossed:onto:]
+ -[_CSAttributeLiftingGraph readEdges]
+ -[_CSAttributeLiftingGraph visit:names:visited:frontier:]
+ -[_CSAttributeLiftingGraph visitCount]
+ -[_CSAttributeLiftingGraph warnings]
+ -[_CSComputeStage attributeLiftingBehavior]
+ -[_CSComputeStage implicitReferencedFieldsByStage]
+ -[_CSComputeStage reservedOutputFieldName]
+ -[_CSCountStage attributeLiftingBehavior]
+ -[_CSCustomStage resolvedOutputTypeForInputType:error:]
+ -[_CSExtractGroupItemsStage attributeLiftingBehavior]
+ -[_CSExtractGroupItemsStage dataFlowDependencies]
+ -[_CSExtractGroupItemsStage explicitRequiredAttributesBySourceStage]
+ -[_CSExtractGroupItemsStage valueReadDependencies]
+ -[_CSFilterStage dataFlowDependencies]
+ -[_CSFilterStage explicitRequiredAttributesBySourceStage]
+ -[_CSFilterStage extractSourceAttributeNames]
+ -[_CSFilterStage filterBlockForInputType:]
+ -[_CSFilterStage predicateAttributeNames]
+ -[_CSFilterStage valueReadDependencies]
+ -[_CSForEachStage executionBlockForInputType:]
+ -[_CSGroupByStage attributeLiftingBehavior]
+ -[_CSGroupByStage reservedOutputFieldName]
+ -[_CSHydrationFileReads .cxx_destruct]
+ -[_CSHydrationFileReads initWithRoots:byteBudget:]
+ -[_CSHydrationFileReads reserveBytes:]
+ -[_CSHydrationFileReads returnBytes:]
+ -[_CSHydrationFileReads roots]
+ -[_CSHydrationReadRoot .cxx_destruct]
+ -[_CSHydrationReadRoot dealloc]
+ -[_CSHydrationReadRoot fd]
+ -[_CSHydrationReadRoot givenPath]
+ -[_CSHydrationReadRoot initWithDescriptor:givenPath:kernelPath:]
+ -[_CSHydrationReadRoot kernelPath]
+ -[_CSHydrationStage fileSystemReadRoots]
+ -[_CSHydrationStage hydrateItemFromFileSystem:fileReads:maxFileSize:contentTypes:completion:]
+ -[_CSHydrationStage hydrateItemWithIdentifier:bundleID:path:contentTypes:timeout:maxFileSize:allowFileSystem:fileReads:index:completion:]
+ -[_CSHydrationStage reportNotHydratedCount:context:]
+ -[_CSHydrationStage row:mergingDelegateItem:]
+ -[_CSHydrationStage runIndexHydrationForInput:identifiersByBundle:handledSnapshot:index:context:hydrationAttributes:contentTypes:timeout:maxFileSize:allowFileSystem:fileReads:completion:]
+ -[_CSLimitStage executionBlockForInputType:]
+ -[_CSLimitStage firstRowOf:withDescriptors:]
+ -[_CSLimitStage sortRows:withDescriptors:]
+ -[_CSPredicateNode(VariableResolution) collectReferencedAttributeNames:]
+ -[_CSPromptedStage attributeLiftingBehavior]
+ -[_CSPromptedStage resolvedOutputTypeForInputType:error:]
+ -[_CSQueryNode collectReferencedAttributeNames:]
+ -[_CSQueryOperation collectReferencedAttributeNames:]
+ -[_CSQueryStage dataFlowDependencies]
+ -[_CSQueryStage explicitRequiredAttributesBySourceStage]
+ -[_CSQueryStage preservesLimit]
+ -[_CSQueryStage selectResultTyped:selector:context:error:]
+ -[_CSQueryStage setPreservesLimit:]
+ -[_CSQueryStage valueReadDependencies]
+ -[_CSSamplingStage executionBlockForInputType:]
+ -[_CSSearchPipelineExecutionContext effectiveInputType]
+ -[_CSSearchPipelineExecutionContext setEffectiveInputType:]
+ -[_CSSearchPipelineStage attributeLiftingBehavior]
+ -[_CSSearchPipelineStage dataFlowDependencies]
+ -[_CSSearchPipelineStage explicitRequiredAttributesBySourceStage]
+ -[_CSSearchPipelineStage fileScopes]
+ -[_CSSearchPipelineStage implicitReferencedFieldsByStage]
+ -[_CSSearchPipelineStage requiredInputAttributes]
+ -[_CSSearchPipelineStage reservedOutputFieldName]
+ -[_CSSearchPipelineStage runInputTypeInContext:]
+ -[_CSSearchPipelineStage setFileScopes:]
+ -[_CSSearchPipelineStage valueReadDependencies]
+ -[_CSStageGroup dataFlowDependencies]
+ -[_CSStageGroup valueReadDependencies]
+ -[_CSStringPredicate predicateWithStringValue:]
+ -[_CSStringPredicate string:containsWithOptions:]
+ GCC_except_table111
+ GCC_except_table113
+ GCC_except_table114
+ GCC_except_table116
+ GCC_except_table120
+ GCC_except_table130
+ GCC_except_table133
+ GCC_except_table147
+ GCC_except_table153
+ GCC_except_table154
+ GCC_except_table155
+ GCC_except_table156
+ GCC_except_table157
+ GCC_except_table163
+ GCC_except_table183
+ GCC_except_table184
+ GCC_except_table192
+ GCC_except_table205
+ GCC_except_table208
+ GCC_except_table211
+ GCC_except_table213
+ GCC_except_table215
+ GCC_except_table216
+ GCC_except_table235
+ GCC_except_table252
+ GCC_except_table260
+ GCC_except_table265
+ GCC_except_table270
+ GCC_except_table272
+ GCC_except_table275
+ GCC_except_table281
+ GCC_except_table285
+ GCC_except_table290
+ GCC_except_table305
+ GCC_except_table31
+ GCC_except_table310
+ GCC_except_table314
+ GCC_except_table315
+ GCC_except_table326
+ GCC_except_table339
+ GCC_except_table348
+ GCC_except_table350
+ GCC_except_table352
+ GCC_except_table353
+ GCC_except_table357
+ GCC_except_table358
+ GCC_except_table359
+ GCC_except_table360
+ GCC_except_table370
+ GCC_except_table374
+ GCC_except_table375
+ GCC_except_table376
+ GCC_except_table380
+ GCC_except_table384
+ GCC_except_table388
+ GCC_except_table390
+ GCC_except_table398
+ GCC_except_table402
+ GCC_except_table408
+ GCC_except_table409
+ GCC_except_table413
+ GCC_except_table417
+ GCC_except_table42
+ GCC_except_table421
+ GCC_except_table425
+ GCC_except_table427
+ GCC_except_table428
+ GCC_except_table435
+ GCC_except_table44
+ GCC_except_table441
+ GCC_except_table442
+ GCC_except_table443
+ GCC_except_table445
+ GCC_except_table446
+ GCC_except_table447
+ GCC_except_table448
+ GCC_except_table45
+ GCC_except_table455
+ GCC_except_table456
+ GCC_except_table457
+ GCC_except_table458
+ GCC_except_table459
+ GCC_except_table46
+ GCC_except_table461
+ GCC_except_table462
+ GCC_except_table463
+ GCC_except_table464
+ GCC_except_table465
+ GCC_except_table466
+ GCC_except_table467
+ GCC_except_table468
+ GCC_except_table469
+ GCC_except_table470
+ GCC_except_table471
+ GCC_except_table473
+ GCC_except_table474
+ GCC_except_table48
+ GCC_except_table484
+ GCC_except_table490
+ GCC_except_table491
+ GCC_except_table494
+ GCC_except_table496
+ GCC_except_table50
+ GCC_except_table63
+ GCC_except_table74
+ GCC_except_table80
+ _CFNumberIsFloatType
+ _CSExtractionConfigRequirements
+ _CSExtractionConfigValueReadStages
+ _CSVariableReferenceRegex
+ _OBJC_CLASS_$_NSFileHandle
+ _OBJC_CLASS_$__CSAttributeLiftingGraph
+ _OBJC_CLASS_$__CSHydrationFileReads
+ _OBJC_CLASS_$__CSHydrationReadRoot
+ _OBJC_IVAR_$__CSAgenticQuery._cancelled
+ _OBJC_IVAR_$__CSAgenticQuery._completionDelivered
+ _OBJC_IVAR_$__CSAgenticQuery._started
+ _OBJC_IVAR_$__CSAgenticQueryConfiguration._customStageHandler
+ _OBJC_IVAR_$__CSAgenticQueryConfiguration._fileScopes
+ _OBJC_IVAR_$__CSAgenticQueryConfiguration._promptedStageHandler
+ _OBJC_IVAR_$__CSAttributeLiftingGraph._droppedByStage
+ _OBJC_IVAR_$__CSAttributeLiftingGraph._droppedOverLong
+ _OBJC_IVAR_$__CSAttributeLiftingGraph._edges
+ _OBJC_IVAR_$__CSAttributeLiftingGraph._freeForm
+ _OBJC_IVAR_$__CSAttributeLiftingGraph._indexById
+ _OBJC_IVAR_$__CSAttributeLiftingGraph._lifted
+ _OBJC_IVAR_$__CSAttributeLiftingGraph._stages
+ _OBJC_IVAR_$__CSAttributeLiftingGraph._structuralPass
+ _OBJC_IVAR_$__CSAttributeLiftingGraph._visitCount
+ _OBJC_IVAR_$__CSHydrationFileReads._byteBudget
+ _OBJC_IVAR_$__CSHydrationFileReads._roots
+ _OBJC_IVAR_$__CSHydrationFileReads._usedBytes
+ _OBJC_IVAR_$__CSHydrationReadRoot._fd
+ _OBJC_IVAR_$__CSHydrationReadRoot._givenPath
+ _OBJC_IVAR_$__CSHydrationReadRoot._kernelPath
+ _OBJC_IVAR_$__CSQueryStage._preservesLimit
+ _OBJC_IVAR_$__CSSearchPipelineExecutionContext._effectiveInputType
+ _OBJC_IVAR_$__CSSearchPipelineStage._fileScopes
+ _OBJC_METACLASS_$__CSAttributeLiftingGraph
+ _OBJC_METACLASS_$__CSHydrationFileReads
+ _OBJC_METACLASS_$__CSHydrationReadRoot
+ _SSSemanticSearchMD10Enabled.ffStatus
+ _SSSemanticSearchMD10Enabled.onceToken
+ __CSPipelineIsGroupRow
+ __OBJC_$_CLASS_METHODS__CSHydrationReadRoot
+ __OBJC_$_INSTANCE_METHODS__CSAttributeLiftingGraph
+ __OBJC_$_INSTANCE_METHODS__CSHydrationFileReads
+ __OBJC_$_INSTANCE_METHODS__CSHydrationReadRoot
+ __OBJC_$_INSTANCE_VARIABLES__CSAttributeLiftingGraph
+ __OBJC_$_INSTANCE_VARIABLES__CSHydrationFileReads
+ __OBJC_$_INSTANCE_VARIABLES__CSHydrationReadRoot
+ __OBJC_$_PROP_LIST__CSAttributeLiftingGraph
+ __OBJC_$_PROP_LIST__CSHydrationFileReads
+ __OBJC_$_PROP_LIST__CSHydrationReadRoot
+ __OBJC_CLASS_RO_$__CSAttributeLiftingGraph
+ __OBJC_CLASS_RO_$__CSHydrationFileReads
+ __OBJC_CLASS_RO_$__CSHydrationReadRoot
+ __OBJC_METACLASS_RO_$__CSAttributeLiftingGraph
+ __OBJC_METACLASS_RO_$__CSHydrationFileReads
+ __OBJC_METACLASS_RO_$__CSHydrationReadRoot
+ __ZL11cs_rowValueP11objc_objectRK11CSNameForms
+ __ZL12cs_sortCellsRKNSt3__16vectorIP11objc_objectNS_9allocatorIS3_EEEERKNS0_I9CSSortKeyNS4_IS9_EEEE
+ __ZL13cs_scrubArrayP7NSArrayP12NSDictionaryIP8NSStringP5NSSetEm
+ __ZL13cs_sortFamilyP11objc_object
+ __ZL14cs_rowPrecedesPK10CSSortCellS1_RKNSt3__16vectorI9CSSortKeyNS2_9allocatorIS4_EEEE
+ __ZL15cs_identityPairP11objc_objectS0_
+ __ZL16addRequiredNamesP19NSMutableDictionaryIP8NSStringP12NSMutableSetIS1_EES1_P5NSSetIS1_E
+ __ZL17cs_fileSystemPathP11objc_objectPc
+ __ZL17cs_makeRowMatcherP12_CSQueryNodeP33_CSSearchPipelineExecutionContext
+ __ZL17cs_remainderBelowPKcmP6NSData
+ __ZL18cs_resolveSortKeysP7NSArrayIP16NSSortDescriptorEU13block_pointerFP8NSStringS5_ES7_
+ __ZL18cs_scrubProvenanceP11objc_objectP12NSDictionaryIP8NSStringP5NSSetEm
+ __ZL19cs_resolveNameFormsP8NSStringU13block_pointerFS0_S0_ES2_
+ __ZL19isMaxCallExpressionP8NSString
+ __ZL20cs_collectProvenanceP11objc_objectP19NSMutableDictionaryIP8NSStringP12NSMutableSetEm
+ __ZL20cs_rowProvenanceKeysv
+ __ZL21collectVariableFieldsP11objc_objectP19NSMutableDictionaryIP8NSStringP12NSMutableSetIS3_EElPl
+ __ZL22cs_identityPairAllowedP12NSDictionaryIP8NSStringP5NSSetEP11objc_objectS7_
+ __ZL22cs_isAllowedProvenanceP12NSDictionaryIP8NSStringP5NSSetES1_P11objc_object
+ __ZL23cs_allowProvenanceValueP19NSMutableDictionaryIP8NSStringP12NSMutableSetES1_P11objc_object
+ __ZL23cs_withExtractionSourceP5NSSetIP8NSStringEP18_CSValueExtractionS1_
+ __ZL24cs_extractionSourceNamesP18_CSValueExtraction
+ __ZL24executeSelectAggregationP14_CSSelectIndexP8NSStringP7NSArraybS2_P33_CSSearchPipelineExecutionContext
+ __ZL25cs_collectChildProvenancePU28objcproto17NSFastEnumeration11objc_objectP19NSMutableDictionaryIP8NSStringP12NSMutableSetEm
+ __ZL25cs_extractionRequirementsP18_CSValueExtractionP8NSString
+ __ZL25cs_kernelPathOfDescriptori
+ __ZL26cs_extractionSourceStageIdP18_CSValueExtraction
+ __ZL27substituteVariablesInStringP8NSStringP33_CSSearchPipelineExecutionContextPU15__autoreleasingP7NSError
+ __ZL28cs_isReservedOutputFieldNameP8NSString
+ __ZL30cs_rowsWithInputProvenanceOnlyP7NSArrayS0_P5NSSetIP8NSStringE
+ __ZN11CSNameFormsD1Ev
+ __ZN20CSAttributeNameCache8formsForEP8NSString
+ __ZN20CSAttributeNameCacheC2EU13block_pointerFP8NSStringS1_ES3_
+ __ZN9CSSortKeyD1Ev
+ __ZNKSt3__119__shared_weak_count13__get_deleterERKSt9type_info
+ __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorI11CSNameFormsEEPS2_EclB9fqe220106Ev
+ __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorI9CSSortKeyEEPS2_EclB9fqe220106Ev
+ __ZNSt3__113__stable_sortINS_17_ClassicAlgPolicyERZL14cs_sortedOrderRKNS_6vectorI10CSSortCellNS_9allocatorIS3_EEEERKNS2_I9CSSortKeyNS4_IS9_EEEEmE3$_0NS_11__wrap_iterIPmEEEEvT1_SJ_T0_NS_15iterator_traitsISJ_E15difference_typeEPNSM_10value_typeEl
+ __ZNSt3__114__split_bufferI10CSSortCellRNS_9allocatorIS1_EEED2Ev
+ __ZNSt3__114__split_bufferI11CSNameFormsRNS_9allocatorIS1_EEE17__destruct_at_endB9fqe220106EPS1_
+ __ZNSt3__114__split_bufferI11CSNameFormsRNS_9allocatorIS1_EEED2Ev
+ __ZNSt3__114__split_bufferI9CSSortKeyRNS_9allocatorIS1_EEE17__destruct_at_endB9fqe220106EPS1_
+ __ZNSt3__114__split_bufferI9CSSortKeyRNS_9allocatorIS1_EEED2Ev
+ __ZNSt3__115__inplace_mergeINS_17_ClassicAlgPolicyERZL14cs_sortedOrderRKNS_6vectorI10CSSortCellNS_9allocatorIS3_EEEERKNS2_I9CSSortKeyNS4_IS9_EEEEmE3$_0NS_11__wrap_iterIPmEEEEvT1_SJ_SJ_OT0_NS_15iterator_traitsISJ_E15difference_typeESO_PNSN_10value_typeEl
+ __ZNSt3__116__if_likely_elseB9fqe220106IZNS_6vectorI10CSSortCellNS_9allocatorIS2_EEE12emplace_backIJS2_EEEvDpOT_EUlvE_ZNS6_IJS2_EEEvS9_EUlvE0_EEvbT_T0_
+ __ZNSt3__116allocator_traitsINS_9allocatorI11CSNameFormsEEE7destroyB9fqe220106IS2_Li0EEEvRS3_PT_
+ __ZNSt3__116allocator_traitsINS_9allocatorI9CSSortKeyEEE7destroyB9fqe220106IS2_Li0EEEvRS3_PT_
+ __ZNSt3__118__stable_sort_moveINS_17_ClassicAlgPolicyERZL14cs_sortedOrderRKNS_6vectorI10CSSortCellNS_9allocatorIS3_EEEERKNS2_I9CSSortKeyNS4_IS9_EEEEmE3$_0NS_11__wrap_iterIPmEEEEvT1_SJ_T0_NS_15iterator_traitsISJ_E15difference_typeEPNSM_10value_typeE
+ __ZNSt3__119__allocate_at_leastB9fqe220106INS_9allocatorI10CSSortCellEENS_16allocator_traitsIS3_EEEENS_19__allocation_resultINT0_7pointerENS7_9size_typeEEERT_m
+ __ZNSt3__119__allocate_at_leastB9fqe220106INS_9allocatorI11CSNameFormsEENS_16allocator_traitsIS3_EEEENS_19__allocation_resultINT0_7pointerENS7_9size_typeEEERT_m
+ __ZNSt3__119__allocate_at_leastB9fqe220106INS_9allocatorI9CSSortKeyEENS_16allocator_traitsIS3_EEEENS_19__allocation_resultINT0_7pointerENS7_9size_typeEEERT_m
+ __ZNSt3__119__allocate_at_leastB9fqe220106INS_9allocatorIP11objc_objectEENS_16allocator_traitsIS5_EEEENS_19__allocation_resultINT0_7pointerENS9_9size_typeEEERT_m
+ __ZNSt3__119__allocate_at_leastB9fqe220106INS_9allocatorImEENS_16allocator_traitsIS2_EEEENS_19__allocation_resultINT0_7pointerENS6_9size_typeEEERT_m
+ __ZNSt3__119__shared_weak_count14__release_weakEv
+ __ZNSt3__119__shared_weak_count16__release_sharedB9fqe220106Ev
+ __ZNSt3__119__shared_weak_countD2Ev
+ __ZNSt3__120__shared_ptr_emplaceI20CSAttributeNameCacheNS_9allocatorIS1_EEE16__on_zero_sharedEv
+ __ZNSt3__120__shared_ptr_emplaceI20CSAttributeNameCacheNS_9allocatorIS1_EEE21__on_zero_shared_weakEv
+ __ZNSt3__120__shared_ptr_emplaceI20CSAttributeNameCacheNS_9allocatorIS1_EEED0Ev
+ __ZNSt3__120__shared_ptr_emplaceI20CSAttributeNameCacheNS_9allocatorIS1_EEED1Ev
+ __ZNSt3__122__rotate_random_accessB9fqe220106INS_17_ClassicAlgPolicyENS_11__wrap_iterIPmEES4_EET0_S5_S5_T1_
+ __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorI11CSNameFormsEEPS3_EEED2B9fqe220106Ev
+ __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorI9CSSortKeyEEPS3_EEED2B9fqe220106Ev
+ __ZNSt3__134__uninitialized_allocator_relocateB9fqe220106INS_9allocatorI11CSNameFormsEEPS2_EEvRT_T0_S7_S7_
+ __ZNSt3__134__uninitialized_allocator_relocateB9fqe220106INS_9allocatorI9CSSortKeyEEPS2_EEvRT_T0_S7_S7_
+ __ZNSt3__135__uninitialized_allocator_copy_implB9fqe220106INS_9allocatorI9CSSortKeyEEPKS2_S5_PS2_EET2_RT_T0_T1_S7_
+ __ZNSt3__16vectorI10CSSortCellNS_9allocatorIS1_EEE16__destroy_vectorclB9fqe220106Ev
+ __ZNSt3__16vectorI10CSSortCellNS_9allocatorIS1_EEE20__throw_length_errorB9fqe220106Ev
+ __ZNSt3__16vectorI10CSSortCellNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJS1_EEEPS1_DpOT_
+ __ZNSt3__16vectorI10CSSortCellNS_9allocatorIS1_EEE26__swap_out_circular_bufferERNS_14__split_bufferIS1_RS3_EE
+ __ZNSt3__16vectorI10CSSortCellNS_9allocatorIS1_EEE7reserveEm
+ __ZNSt3__16vectorI10CSSortCellNS_9allocatorIS1_EEE9push_backB9fqe220106EOS1_
+ __ZNSt3__16vectorI11CSNameFormsNS_9allocatorIS1_EEE16__destroy_vectorclB9fqe220106Ev
+ __ZNSt3__16vectorI11CSNameFormsNS_9allocatorIS1_EEE20__throw_length_errorB9fqe220106Ev
+ __ZNSt3__16vectorI11CSNameFormsNS_9allocatorIS1_EEE22__base_destruct_at_endB9fqe220106EPS1_
+ __ZNSt3__16vectorI11CSNameFormsNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJS1_EEEPS1_DpOT_
+ __ZNSt3__16vectorI11CSNameFormsNS_9allocatorIS1_EEE9push_backB9fqe220106EOS1_
+ __ZNSt3__16vectorI9CSSortKeyNS_9allocatorIS1_EEE11__vallocateB9fqe220106Em
+ __ZNSt3__16vectorI9CSSortKeyNS_9allocatorIS1_EEE16__destroy_vectorclB9fqe220106Ev
+ __ZNSt3__16vectorI9CSSortKeyNS_9allocatorIS1_EEE16__init_with_sizeB9fqe220106IPKS1_S7_EEvT_T0_m
+ __ZNSt3__16vectorI9CSSortKeyNS_9allocatorIS1_EEE20__throw_length_errorB9fqe220106Ev
+ __ZNSt3__16vectorI9CSSortKeyNS_9allocatorIS1_EEE22__base_destruct_at_endB9fqe220106EPS1_
+ __ZNSt3__16vectorI9CSSortKeyNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJS1_EEEPS1_DpOT_
+ __ZNSt3__16vectorI9CSSortKeyNS_9allocatorIS1_EEE7reserveEm
+ __ZNSt3__16vectorIP11objc_objectNS_9allocatorIS3_EEE11__vallocateB9fqe220106Em
+ __ZNSt3__16vectorIP11objc_objectNS_9allocatorIS3_EEE20__throw_length_errorB9fqe220106Ev
+ __ZNSt3__16vectorIP11objc_objectNS_9allocatorIS3_EEEC2B9fqe220106Em
+ __ZNSt3__16vectorImNS_9allocatorImEEE11__vallocateB9fqe220106Em
+ __ZNSt3__16vectorImNS_9allocatorImEEE20__throw_length_errorB9fqe220106Ev
+ __ZNSt3__16vectorImNS_9allocatorImEEE24__emplace_back_slow_pathIJRKmEEEPmDpOT_
+ __ZNSt3__16vectorImNS_9allocatorImEEE7reserveEm
+ __ZNSt3__16vectorImNS_9allocatorImEEEC2B9fqe220106Em
+ __ZNSt3__17__sort3B9fqe220106INS_17_ClassicAlgPolicyERZL23cs_nthByKeyThenPositionRNS_6vectorImNS_9allocatorImEEEEmRKNS2_I10CSSortCellNS3_IS7_EEEERKNS2_I9CSSortKeyNS3_ISC_EEEEEUlmmE_NS_11__wrap_iterIPmEELi0EEEbT1_SM_SM_T0_
+ __ZNSt3__18__rotateB9fqe220106INS_17_ClassicAlgPolicyENS_11__wrap_iterIPmEES4_EENS_4pairIT0_S6_EES6_S6_T1_
+ __ZSt7nothrow
+ __ZSt9terminatev
+ __ZTINSt3__119__shared_weak_countE
+ __ZTINSt3__120__shared_ptr_emplaceI20CSAttributeNameCacheNS_9allocatorIS1_EEEE
+ __ZTSNSt3__120__shared_ptr_emplaceI20CSAttributeNameCacheNS_9allocatorIS1_EEEE
+ __ZTVN10__cxxabiv120__si_class_type_infoE
+ __ZTVNSt3__120__shared_ptr_emplaceI20CSAttributeNameCacheNS_9allocatorIS1_EEEE
+ __ZZ24CSVariableReferenceRegexE5regex
+ __ZZ24CSVariableReferenceRegexE9onceToken
+ __ZZL18cs_rowIdentityKeysvE4keys
+ __ZZL18cs_rowIdentityKeysvE4once
+ __ZZL20cs_hydrationDenylistvE4once
+ __ZZL20cs_hydrationDenylistvE6denied
+ __ZZL20cs_rowProvenanceKeysvE4keys
+ __ZZL20cs_rowProvenanceKeysvE4once
+ __ZZL26cs_customStageMintableKeysvE4keys
+ __ZZL26cs_customStageMintableKeysvE4once
+ __ZdlPvSt19__type_descriptor_t
+ __ZnwmRKSt9nothrow_t
+ ___137-[_CSHydrationStage hydrateItemWithIdentifier:bundleID:path:contentTypes:timeout:maxFileSize:allowFileSystem:fileReads:index:completion:]_block_invoke
+ ___187-[_CSHydrationStage runIndexHydrationForInput:identifiersByBundle:handledSnapshot:index:context:hydrationAttributes:contentTypes:timeout:maxFileSize:allowFileSystem:fileReads:completion:]_block_invoke
+ ___187-[_CSHydrationStage runIndexHydrationForInput:identifiersByBundle:handledSnapshot:index:context:hydrationAttributes:contentTypes:timeout:maxFileSize:allowFileSystem:fileReads:completion:]_block_invoke_2
+ ___187-[_CSHydrationStage runIndexHydrationForInput:identifiersByBundle:handledSnapshot:index:context:hydrationAttributes:contentTypes:timeout:maxFileSize:allowFileSystem:fileReads:completion:]_block_invoke_3
+ ___187-[_CSHydrationStage runIndexHydrationForInput:identifiersByBundle:handledSnapshot:index:context:hydrationAttributes:contentTypes:timeout:maxFileSize:allowFileSystem:fileReads:completion:]_block_invoke_4
+ ___187-[_CSHydrationStage runIndexHydrationForInput:identifiersByBundle:handledSnapshot:index:context:hydrationAttributes:contentTypes:timeout:maxFileSize:allowFileSystem:fileReads:completion:]_block_invoke_5
+ ___205+[_CSSearchPipelineExecutor executeNextStage:index:stageResults:stageMap:attributeTranslator:customStageHandler:promptedStageHandler:searchableIndex:boundVariables:rowKinds:extractValueConfigs:completion:]_block_invoke
+ ___36-[_CSAttributeLiftingGraph liftMap:]_block_invoke
+ ___48-[_CSCustomStage executeWithContext:completion:]_block_invoke
+ ___50-[_CSAttributeLiftingGraph liftExtractionConfigs:]_block_invoke
+ ___50-[_CSAttributeLiftingGraph liftExtractionConfigs:]_block_invoke_2
+ ___50-[_CSPromptedStage executeWithContext:completion:]_block_invoke
+ ___52-[_CSAttributeLiftingGraph liftRequirementsOfStage:]_block_invoke
+ ___52-[_CSAttributeLiftingGraph liftRequirementsOfStage:]_block_invoke_2
+ ___CSVariableReferenceRegex_block_invoke
+ ___SSSemanticSearchMD10Enabled_block_invoke
+ ____ZL17cs_makeRowMatcherP12_CSQueryNodeP33_CSSearchPipelineExecutionContext_block_invoke
+ ____ZL18cs_rowIdentityKeysv_block_invoke
+ ____ZL18cs_scrubDictionaryP12NSDictionaryPS_IP8NSStringP5NSSetEm_block_invoke
+ ____ZL20cs_hydrationDenylistv_block_invoke
+ ____ZL20cs_rowProvenanceKeysv_block_invoke
+ ____ZL26cs_customStageMintableKeysv_block_invoke
+ ____ZL26cs_mergeDelegateAttributesP19NSMutableDictionaryP12NSDictionary_block_invoke
+ ____ZL29collectVariableFieldsInStringP8NSStringP19NSMutableDictionaryIS0_P12NSMutableSetIS0_EEPl_block_invoke
+ ___block_descriptor_121_ea8_32s40s48s56s64s72s80s88s96bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8
+ ___block_descriptor_145_ea8_32s40s48s56s64s72s80s88s96s104s112s120bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8s112l8s120l8
+ ___block_descriptor_176_e8_32s40s48s56s64s72s80s88s96s104s112s120s128bs136bs144bs_e20_v24?08"NSError"16ls128l8s32l8s40l8s136l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s144l8s104l8s112l8s120l8
+ ___block_descriptor_40_e8_32s_e45_v32?0"NSString"8"_CSValueExtraction"16^B24ls32l8
+ ___block_descriptor_48_e8_32s40r_e5_B8?0ls32l8r40l8
+ ___block_descriptor_48_e8_32s40s_e19_"NSDictionary"8?0ls32l8s40l8
+ ___block_descriptor_48_ea8_32s40bs_e20_v24?08"NSError"16ls32l8s40l8
+ ___block_descriptor_48_ea8_32s40s_e15_v32?0816^B24ls32l8s40l8
+ ___block_descriptor_56_ea8_32r40c48_ZTSNSt3__110shared_ptrI20CSAttributeNameCacheEE_e21_24?08"NSString"16l
+ ___block_descriptor_56_ea8_32s40bs48r_e8_B16?08lr48l8s32l8s40l8
+ ___block_descriptor_56_ea8_32s40s48bs_e20_v24?08"NSError"16ls48l8s32l8s40l8
+ ___block_descriptor_56_ea8_32s40s_e37_v32?0"NSTextCheckingResult"8Q16^B24ls32l8s40l8
+ ___block_descriptor_72_ea8_32s40s48s56r_e15_v32?0816^B24ls32l8s40l8r56l8s48l8
+ ___block_descriptor_80_ea8_32s40s48s56s64s72bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_81_ea8_32s40s48s56s64bs_e29_v24?0"NSData"8"NSString"16ls64l8s32l8s40l8s48l8s56l8
+ ___clang_call_terminate
+ ___copy_helper_block_ea8_40c48_ZTSNSt3__110shared_ptrI20CSAttributeNameCacheEE
+ ___cs_makeSingleClaim_block_invoke
+ ___cs_reservedOutputNames_block_invoke
+ ___cxa_begin_catch
+ ___destroy_helper_block_ea8_40c48_ZTSNSt3__110shared_ptrI20CSAttributeNameCacheEE
+ ___valueReadStageIds_block_invoke
+ _appendLiftingWarnings
+ _appendUnseenItems
+ _checkNoReservedOutputFields
+ _cs_errorForStageException
+ _cs_reservedOutputNames.names
+ _cs_reservedOutputNames.onceToken
+ _cs_rowKindError
+ _cs_warningSafeStageId
+ _detachUnstartedQueries
+ _fcntl
+ _kRowIdentityKeys
+ _memmove
+ _objc_exception_rethrow
+ _parametersWithoutReservedKeys
+ _strnlen
- +[_CSSearchPipelineExecutor executeNextStage:index:stageResults:stageMap:attributeTranslator:customStageHandler:promptedStageHandler:searchableIndex:boundVariables:extractValueConfigs:completion:]
- -[_CSFilterStage evaluatePredicate:againstDictionary:]
- -[_CSFilterStage evaluatePredicate:againstItem:context:]
- -[_CSHydrationStage hydrateItemFromFileSystem:maxFileSize:contentTypes:completion:]
- -[_CSHydrationStage hydrateItemWithIdentifier:bundleID:path:contentTypes:timeout:maxFileSize:allowFileSystem:index:completion:]
- -[_CSHydrationStage isPathSafeToRead:]
- -[_CSHydrationStage runIndexHydrationForInput:identifiersByBundle:handledSnapshot:index:context:hydrationAttributes:contentTypes:timeout:maxFileSize:allowFileSystem:completion:]
- -[_CSLimitStage sortItemArray:withDescriptors:]
- -[_CSLimitStage sortRecordArray:withDescriptors:]
- -[_CSQueryStage selectResultTyped:selector:error:]
- GCC_except_table101
- GCC_except_table104
- GCC_except_table105
- GCC_except_table108
- GCC_except_table122
- GCC_except_table127
- GCC_except_table134
- GCC_except_table136
- GCC_except_table141
- GCC_except_table148
- GCC_except_table159
- GCC_except_table166
- GCC_except_table167
- GCC_except_table171
- GCC_except_table175
- GCC_except_table180
- GCC_except_table191
- GCC_except_table194
- GCC_except_table199
- GCC_except_table204
- GCC_except_table214
- GCC_except_table219
- GCC_except_table223
- GCC_except_table224
- GCC_except_table225
- GCC_except_table232
- GCC_except_table233
- GCC_except_table241
- GCC_except_table257
- GCC_except_table262
- GCC_except_table266
- GCC_except_table267
- GCC_except_table289
- GCC_except_table303
- GCC_except_table307
- GCC_except_table308
- GCC_except_table309
- GCC_except_table311
- GCC_except_table312
- GCC_except_table313
- GCC_except_table318
- GCC_except_table320
- GCC_except_table340
- GCC_except_table345
- GCC_except_table349
- GCC_except_table354
- GCC_except_table93
- GCC_except_table94
- _SSSemanticSearchMD8Enabled.ffStatus
- _SSSemanticSearchMD8Enabled.onceToken
- __ZL24executeSelectAggregationP14_CSSelectIndexP8NSStringP7NSArraybS2_
- __ZL27substituteVariablesInStringP8NSStringP12NSDictionaryIS0_P11objc_objectEPU15__autoreleasingP7NSError
- __ZNSt3__111nth_elementB9fqe220106INS_11__wrap_iterIPP12NSDictionaryEEZL24executeSelectAggregationP14_CSSelectIndexP8NSStringP7NSArraybSA_E3$_0EEvT_SE_SE_T0_
- __ZNSt3__111nth_elementB9fqe220106INS_11__wrap_iterIPP12NSDictionaryEEZL24executeSelectAggregationP14_CSSelectIndexP8NSStringP7NSArraybSA_E3$_1EEvT_SE_SE_T0_
- __ZNSt3__119__allocate_at_leastB9fqe220106INS_9allocatorIP12NSDictionaryEENS_16allocator_traitsIS5_EEEENS_19__allocation_resultINT0_7pointerENS9_9size_typeEEERT_m
- __ZNSt3__16vectorIP12NSDictionaryNS_9allocatorIS3_EEE20__throw_length_errorB9fqe220106Ev
- __ZNSt3__16vectorIP12NSDictionaryNS_9allocatorIS3_EEE24__emplace_back_slow_pathIJRKS2_EEEPS3_DpOT_
- __ZNSt3__16vectorIP12NSDictionaryNS_9allocatorIS3_EEE7reserveEm
- __ZZL24executeSelectAggregationP14_CSSelectIndexP8NSStringP7NSArraybS2_ENK3$_0clEP12NSDictionaryS7_
- __ZZL24executeSelectAggregationP14_CSSelectIndexP8NSStringP7NSArraybS2_ENK3$_1clEP12NSDictionaryS7_
- __ZZZ35-[_CSLimitStage makeLegacyStrategy]EUb0_ENK3$_1clEP12NSDictionaryS1_
- __ZZZ40-[_CSLimitStage makeRecordArrayStrategy]EUb_ENK3$_0clEP12NSDictionaryS1_
- ___127-[_CSHydrationStage hydrateItemWithIdentifier:bundleID:path:contentTypes:timeout:maxFileSize:allowFileSystem:index:completion:]_block_invoke
- ___177-[_CSHydrationStage runIndexHydrationForInput:identifiersByBundle:handledSnapshot:index:context:hydrationAttributes:contentTypes:timeout:maxFileSize:allowFileSystem:completion:]_block_invoke
- ___177-[_CSHydrationStage runIndexHydrationForInput:identifiersByBundle:handledSnapshot:index:context:hydrationAttributes:contentTypes:timeout:maxFileSize:allowFileSystem:completion:]_block_invoke_2
- ___177-[_CSHydrationStage runIndexHydrationForInput:identifiersByBundle:handledSnapshot:index:context:hydrationAttributes:contentTypes:timeout:maxFileSize:allowFileSystem:completion:]_block_invoke_3
- ___177-[_CSHydrationStage runIndexHydrationForInput:identifiersByBundle:handledSnapshot:index:context:hydrationAttributes:contentTypes:timeout:maxFileSize:allowFileSystem:completion:]_block_invoke_4
- ___177-[_CSHydrationStage runIndexHydrationForInput:identifiersByBundle:handledSnapshot:index:context:hydrationAttributes:contentTypes:timeout:maxFileSize:allowFileSystem:completion:]_block_invoke_5
- ___196+[_CSSearchPipelineExecutor executeNextStage:index:stageResults:stageMap:attributeTranslator:customStageHandler:promptedStageHandler:searchableIndex:boundVariables:extractValueConfigs:completion:]_block_invoke
- ___47-[_CSLimitStage sortItemArray:withDescriptors:]_block_invoke
- ___49-[_CSLimitStage sortRecordArray:withDescriptors:]_block_invoke
- ___54-[_CSFilterStage evaluatePredicate:againstDictionary:]_block_invoke
- ___56-[_CSFilterStage evaluatePredicate:againstItem:context:]_block_invoke
- ___SSSemanticSearchMD8Enabled_block_invoke
- ___block_descriptor_113_ea8_32s40s48s56s64s72s80s88bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
- ___block_descriptor_137_ea8_32s40s48s56s64s72s80s88s96s104s112bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8s112l8
- ___block_descriptor_144_e8_32s40s48s56s64s72s80s88s96s104s112bs120bs_e20_v24?08"NSError"16ls32l8s112l8s40l8s48l8s56l8s64l8s72l8s80l8s120l8s88l8s96l8s104l8
- ___block_descriptor_40_ea8_32s_e21_24?08"NSString"16ls32l8
- ___block_descriptor_48_ea8_32s40s_e21_24?08"NSString"16ls32l8s40l8
- ___block_descriptor_48_ea8_32s40s_e47_q24?0"CSSearchableItem"8"CSSearchableItem"16ls32l8s40l8
- ___block_descriptor_56_ea8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_73_ea8_32s40s48s56bs_e29_v24?0"NSData"8"NSString"16ls56l8s32l8s40l8s48l8
- ___stderrp
- _fprintf
CStrings:
+ "\x1fidentityPair"
+ "  %lu. %{private}@ [%{public}@, strategy=%{public}@]"
+ "\"*%@\""
+ "%{private}@"
+ "Auto-generated stage ID: %{private}s"
+ "B16@?0@8"
+ "CountStage[%{private}@] ENTER: input='%{private}@' input_count=%lu"
+ "CountStage[%{private}@] EXIT: input='%{private}@' count=%lu"
+ "Custom stage '%@' did not return a list of rows."
+ "Defaulted input to previous stage: %{private}s"
+ "Executing stage '%{private}@' (supports parallel: %{public}@)"
+ "Executing stage '%{private}@' in parallel across %lu partitions"
+ "Failed to determine execution order: %{private}@"
+ "FilterStage[%{private}@] ENTER (itemArray): input='%{private}@' input_count=%lu"
+ "FilterStage[%{private}@] ENTER (legacy): input='%{private}@' input_count=%lu"
+ "FilterStage[%{private}@] ENTER (recordArray): input='%{private}@' input_count=%lu"
+ "FilterStage[%{private}@] EXIT (itemArray): passed=%lu failed=%lu"
+ "FilterStage[%{private}@] EXIT (legacy): passed=%lu failed=%lu"
+ "FilterStage[%{private}@] EXIT (recordArray): passed=%lu failed=%lu"
+ "GroupByStage[%{private}@] ENTER: input='%{private}@' groupBy='%{private}@' input_count=%lu"
+ "GroupByStage[%{private}@] EXIT: groups=%lu filtered=%lu top5=[%{private}@]"
+ "GroupByStage[%{private}@] filtered %lu items with nil '%{private}@' attribute (input had %lu items)"
+ "HydrationStage requires ItemArray or RecordArray input"
+ "Index position is relative to the sorted array! Items with no usable sort value are skipped: index and percentiles address only the rest."
+ "LimitStage[%{private}@] ENTER (itemArray): input='%{private}@' input_count=%lu limit=%lu"
+ "LimitStage[%{private}@] ENTER (legacy): input='%{private}@' input_count=%lu limit=%lu sort_key='%{private}@' sort_asc=%d"
+ "LimitStage[%{private}@] ENTER (recordArray): input='%{private}@' input_count=%lu limit=%lu sort_key='%{private}@'"
+ "LimitStage[%{private}@] EXIT (itemArray): output_count=%lu"
+ "LimitStage[%{private}@] EXIT (legacy first-row scan): output_count=%lu"
+ "LimitStage[%{private}@] EXIT (legacy): output_count=%lu"
+ "LimitStage[%{private}@] EXIT (recordArray first-row scan): output_count=%lu"
+ "LimitStage[%{private}@] EXIT (recordArray): output_count=%lu"
+ "Merge stage '%{private}@': input stage '%{private}@' not found, skipping"
+ "Merging %lu partition results for stage '%{private}@'"
+ "NOTE: %lu attribute names longer than %d characters were ignored."
+ "NOTE: Attribute lifting could not be applied to every stage; some referenced attributes may be missing from results."
+ "NOTE: Query stage '%@' fetches at most %d attributes named only by {{stage.field}} references; %@ more were dropped."
+ "Output field '%@' of stage '%@' is reserved for item identity; choose another name."
+ "Parallel stage '%{private}@' failed: %{private}@"
+ "Partitioning data using strategy '%{public}@' with key '%{private}@'"
+ "Pipeline validation failed: %{private}@"
+ "QueryStage[%{private}@] ENTER: input='%{private}@' query='%{private}@'"
+ "QueryStage[%{private}@] EXIT: output_items=%lu"
+ "Resolved numeric variable '%{private}@' to value: %{private}@"
+ "Resolved variable '%{private}@' to value: %{private}@"
+ "SearchUnifiedEmbeddingMD10"
+ "Selected result is not a record or an item"
+ "Serial stage '%{private}@' failed: %{private}@"
+ "Stage '%@' %@"
+ "Stage '%@' failed: %@"
+ "Stage '%@' returned rows that do not match its output type"
+ "Stage group %{private}@: all %lu sub-pipelines failed"
+ "Stage group %{private}@: executing %lu sub-pipelines in parallel"
+ "Stage group %{private}@: merge failed - %{private}@"
+ "Stage group %{private}@: merged %lu sub-results into %lu items"
+ "Stage group %{private}@: partial failure - %lu/%lu sub-pipelines succeeded"
+ "Stage group %{private}@: sub-pipeline %lu completed successfully"
+ "Stage group %{private}@: sub-pipeline %lu failed - %{private}@"
+ "Stage group %{private}@: validation failed - no sub-pipelines"
+ "TYPE_INFERENCE: stage='%{private}@' class='%{public}@' inputType=%ld outputType=%ld"
+ "TYPE_INFERENCE_FAILED: %{private}@"
+ "[ExtractGroupItems] Resolved $%{private}@ from boundVariables → '%{private}@'"
+ "[ExtractGroupItems] Variable $%{private}@ not found in boundVariables"
+ "_CSPredicateNode: range value could not be parsed as date expression (attribute=%{private}@, values=[%{private}@, %{private}@])"
+ "__cs"
+ "__csByteBudget"
+ "_avg"
+ "_max"
+ "_median"
+ "_min"
+ "_select"
+ "_stddev"
+ "_sum"
+ "attribute lifting: apply raised %{public}@"
+ "attribute lifting: dataFlowDependencies raised %{public}@"
+ "attribute lifting: dropped over-long name (%lu chars)"
+ "attribute lifting: name cap reached for a query stage, dropped a referenced name"
+ "attribute lifting: stage classification raised %{public}@"
+ "attribute lifting: stage requirements raised %{public}@"
+ "ends_with"
+ "endswith"
+ "extractValue for stage '%{private}@': field '%{private}@' not found or null in selected result"
+ "extractValue for stage '%{private}@': index %ld out of bounds [0, %lu)"
+ "extractValue for stage '%{private}@': maxBy/minBy selector missing field"
+ "extractValue for stage '%{private}@': no items with numeric field '%{private}@'"
+ "extractValue for stage '%{private}@': source '%{private}@' is empty, skipping"
+ "extractValue for stage '%{private}@': source '%{private}@' is not an array (%{public}@)"
+ "extractValue for stage '%{private}@': source stage '%{private}@' not found in results"
+ "extractValue for stage '%{private}@': unknown selector type %ld"
+ "extractValue: bound '%{private}@' = '%{private}@' (from stage '%{private}@' field '%{private}@')"
+ "limit strip: a stage raised %{public}@; remaining limits kept"
+ "page_"
+ "returned items and records together."
+ "returned rows that are neither items nor records."
+ "slow_suffix"
+ "source-code"
+ "suffix"
+ "v32@?0@\"NSString\"8@\"_CSValueExtraction\"16^B24"
+ "…"
+ "⚠️ Type-inference for '$%{private}@' found %lu candidates — ambiguous, skipping"
+ "❌ PIPELINE_STAGE_ERROR: stage=%{private}@ error=%{private}@"
+ "❌ PIPELINE_STAGE_EXCEPTION: stage=%{private}@ name=%{public}@"
+ "❌ PROMPTED_STAGE_LIMIT: stage=%{private}@ count=%{public}lu limit=%{public}ld"
+ "🔗 Type-inferred variable '$%{private}@' = %{private}@ (from stage '%{private}@' groupBy '%{private}@')"
- "  %lu. %{public}@ [%{public}@, strategy=%{public}@]"
- " typed=%@ attr=%@ count=%lu"
- "%{public}@"
- "<no compile>"
- "Auto-generated stage ID: %{public}s"
- "CountStage[%{public}@] ENTER: input='%{public}@' input_count=%lu"
- "CountStage[%{public}@] EXIT: input='%{public}@' count=%lu"
- "Defaulted input to previous stage: %{public}s"
- "ERROR: Sort descriptor missing required 'field' key: %s\n"
- "Executing stage '%{public}@' (supports parallel: %{public}@)"
- "Executing stage '%{public}@' in parallel across %lu partitions"
- "Failed to determine execution order: %{public}@"
- "FilterStage[%{public}@] ENTER (itemArray): input='%{public}@' input_count=%lu"
- "FilterStage[%{public}@] ENTER (legacy): input='%{public}@' input_count=%lu"
- "FilterStage[%{public}@] ENTER (recordArray): input='%{public}@' input_count=%lu"
- "FilterStage[%{public}@] EXIT (itemArray): passed=%lu failed=%lu"
- "FilterStage[%{public}@] EXIT (legacy): passed=%lu failed=%lu"
- "FilterStage[%{public}@] EXIT (recordArray): passed=%lu failed=%lu"
- "GroupByStage[%{public}@] ENTER: input='%{public}@' groupBy='%{public}@' input_count=%lu"
- "GroupByStage[%{public}@] EXIT: groups=%lu filtered=%lu top5=[%{public}@]"
- "GroupByStage[%{public}@] filtered %lu items with nil '%{public}@' attribute (input had %lu items)"
- "HydrationStage requires ItemArray input"
- "Index position is relative to the sorted array!"
- "LimitStage[%{public}@] ENTER (itemArray): input='%{public}@' input_count=%lu limit=%lu"
- "LimitStage[%{public}@] ENTER (legacy): input='%{public}@' input_count=%lu limit=%lu sort_key='%{public}@' sort_asc=%d"
- "LimitStage[%{public}@] ENTER (recordArray): input='%{public}@' input_count=%lu limit=%lu sort_key='%{public}@'"
- "LimitStage[%{public}@] EXIT (itemArray): output_count=%lu"
- "LimitStage[%{public}@] EXIT (legacy fast-path O(n)): output_count=1"
- "LimitStage[%{public}@] EXIT (legacy): output_count=%lu"
- "LimitStage[%{public}@] EXIT (recordArray fast-path O(n)): output_count=1"
- "LimitStage[%{public}@] EXIT (recordArray): output_count=%lu"
- "Merge stage '%{public}@': input stage '%{public}@' not found, skipping"
- "Merging %lu partition results for stage '%{public}@'"
- "Parallel stage '%{public}@' failed: %{public}@"
- "Partitioning data using strategy '%{public}@' with key '%{public}@'"
- "QueryStage[%{public}@] ENTER: input='%{public}@' query='%{public}@'"
- "QueryStage[%{public}@] EXIT: output_items=%lu"
- "Resolved numeric variable '%{public}@' to value: %{public}@"
- "Resolved variable '%{public}@' to value: %{public}@"
- "Selected result is not a dictionary"
- "Serial stage '%{public}@' failed: %{public}@"
- "Stage group %{public}@: all %lu sub-pipelines failed"
- "Stage group %{public}@: executing %lu sub-pipelines in parallel"
- "Stage group %{public}@: merge failed - %{public}@"
- "Stage group %{public}@: merged %lu sub-results into %lu items"
- "Stage group %{public}@: partial failure - %lu/%lu sub-pipelines succeeded"
- "Stage group %{public}@: sub-pipeline %lu completed successfully"
- "Stage group %{public}@: sub-pipeline %lu failed - %{public}@"
- "Stage group %{public}@: validation failed - no sub-pipelines"
- "TYPE_INFERENCE: stage='%{public}@' class='%{public}@' inputType=%ld outputType=%ld"
- "TYPE_INFERENCE_FAILED: %{public}@"
- "[ExtractGroupItems] Resolved $%{public}@ from boundVariables → '%{public}@'"
- "[ExtractGroupItems] Variable $%{public}@ not found in boundVariables"
- "\\{\\{([a-zA-Z0-9_]+)\\.[a-zA-Z0-9_]+\\}\\}"
- "_CSPredicateNode: range value could not be parsed as date expression (attribute=%{public}@, values=[%{public}@, %{public}@])"
- "extractValue for stage '%{public}@': field '%{public}@' not found or null in selected result"
- "extractValue for stage '%{public}@': index %ld out of bounds [0, %lu)"
- "extractValue for stage '%{public}@': maxBy/minBy selector missing field"
- "extractValue for stage '%{public}@': no items with numeric field '%{public}@'"
- "extractValue for stage '%{public}@': source '%{public}@' is empty, skipping"
- "extractValue for stage '%{public}@': source '%{public}@' is not an array (%{public}@)"
- "extractValue for stage '%{public}@': source stage '%{public}@' not found in results"
- "extractValue for stage '%{public}@': unknown selector type %ld"
- "extractValue: bound '%{public}@' = '%{public}@' (from stage '%{public}@' field '%{public}@')"
- "prompted:"
- "⚠️ Type-inference for '$%{public}@' found %lu candidates — ambiguous, skipping"
- "⚠️ [CSAgenticQuery] Cursor page_size mismatch: %u vs %lu"
- "❌ PIPELINE_STAGE_ERROR: stage=%{public}@ error=%{public}@"
- "❌ PROMPTED_STAGE_LIMIT: stage=%{public}@ count=%{public}lu limit=%{public}ld"
- "🔍🔍🔍 [CSAgenticQuery] Already started - returning early"
- "🔍🔍🔍 [CSAgenticQuery] Next page cursor: %@"
- "🔍🔍🔍 [CSAgenticQuery] Resuming from cursor offset: %u"
- "🔗 Type-inferred variable '$%{public}@' = %{public}@ (from stage '%{public}@' groupBy '%{public}@')"
- "🔧 [QueryStage]       inner-pred[%lu.%lu.%lu] class=%s compiled=%s\n"
- "🔧 [QueryStage]     grandchild[%lu.%lu] class=%s compiled=%s%s\n"
- "🔧 [QueryStage]   child[%lu] class=%s desc=%s compiled=%s\n"
- "🔧 [QueryStage] Compiled query string: %s\n"
- "🔧 [QueryStage] resolved QueryNode: %s\n"
```
