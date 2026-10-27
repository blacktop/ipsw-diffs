## CoreSpotlight

> `/System/Library/Frameworks/CoreSpotlight.framework/Versions/A/CoreSpotlight`

```diff

-2459.405.0.0.0
-  __TEXT.__text: 0x19c670
-  __TEXT.__objc_methlist: 0x146f8
+2465.1.9.0.0
+  __TEXT.__text: 0x1a0878
+  __TEXT.__objc_methlist: 0x14ac0
   __TEXT.__const: 0xf60
-  __TEXT.__cstring: 0x2c481
-  __TEXT.__oslogstring: 0xbce7
-  __TEXT.__gcc_except_tab: 0x988c
+  __TEXT.__cstring: 0x2c6f8
+  __TEXT.__oslogstring: 0xc115
+  __TEXT.__gcc_except_tab: 0x9af8
   __TEXT.__ustring: 0x218e
-  __TEXT.__dlopen_cstrs: 0x49a
+  __TEXT.__dlopen_cstrs: 0x438
   __TEXT.__constg_swiftt: 0x1bc
   __TEXT.__swift5_typeref: 0x2ba
   __TEXT.__swift5_reflstr: 0x8e

   __TEXT.__swift_as_cont: 0xc
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x6150
+  __TEXT.__unwind_info: 0x6270
   __TEXT.__eh_frame: 0x1e8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3f28
-  __DATA_CONST.__objc_classlist: 0xab0
+  __DATA_CONST.__const: 0x3f30
+  __DATA_CONST.__objc_classlist: 0xad8
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa5d8
+  __DATA_CONST.__objc_selrefs: 0xa740
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x728
+  __DATA_CONST.__objc_superrefs: 0x750
   __DATA_CONST.__objc_arraydata: 0x11108
-  __DATA_CONST.__got: 0xeb8
-  __AUTH_CONST.__const: 0x54b0
-  __AUTH_CONST.__cfstring: 0x2de00
-  __AUTH_CONST.__objc_const: 0x1ff20
+  __DATA_CONST.__got: 0xee0
+  __AUTH_CONST.__const: 0x5610
+  __AUTH_CONST.__cfstring: 0x2e0e0
+  __AUTH_CONST.__objc_const: 0x208e0
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x3a98
   __AUTH_CONST.__objc_dictobj: 0xaf78
   __AUTH_CONST.__objc_intobj: 0xe58
   __AUTH_CONST.__objc_doubleobj: 0x180
   __AUTH_CONST.__objc_floatobj: 0x20
-  __AUTH_CONST.__auth_got: 0x1320
+  __AUTH_CONST.__auth_got: 0x1330
   __AUTH_CONST.__auth_ptr: 0x0
-  __AUTH.__objc_data: 0x5b90
+  __AUTH.__objc_data: 0x5848
   __AUTH.__data: 0x3a0
-  __AUTH.__thread_vars: 0x48
-  __AUTH.__thread_bss: 0x18
-  __DATA.__objc_ivar: 0x145c
-  __DATA.__data: 0x1c40
-  __DATA.__bss: 0x19a0
-  __DATA_DIRTY.__objc_data: 0xf50
+  __AUTH.__thread_vars: 0x60
+  __AUTH.__thread_bss: 0x28
+  __DATA.__objc_ivar: 0x14d4
+  __DATA.__data: 0x1c48
+  __DATA.__bss: 0x19c0
+  __DATA_DIRTY.__objc_data: 0x1428
   __DATA_DIRTY.__data: 0x20
   __DATA_DIRTY.__bss: 0xa7f0
   __DATA_DIRTY.__common: 0x18

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 9103
-  Symbols:   18171
-  CStrings:  8083
+  Functions: 9204
+  Symbols:   18385
+  CStrings:  8122
 
Symbols:
+ +[CSBundleFilterAttributeBackfillGroup supportsSecureCoding]
+ +[CSBundleFilterAttributeBackfillResult supportsSecureCoding]
+ +[CSBundleFilterEvaluationReply supportsSecureCoding]
+ +[CSBundleFilterEvaluationRequest supportsSecureCoding]
+ +[CSBundleFilterFileProviderContainerGroup supportsSecureCoding]
+ +[CSSearchConnection _test_connection]
+ +[CSSearchConnection _test_setGameModeSuspended:]
+ +[_CSSearchPipelineExecutor executeNextStage:index:stageResults:stageMap:attributeTranslator:customStageHandler:promptedStageHandler:searchableIndex:boundVariables:extractValueConfigs:completion:]
+ +[_CSSearchPipelineExecutor executePipeline:configuration:typedCompletion:]
+ +[_CSSearchPipelineExecutor executePipeline:customStageHandler:promptedStageHandler:searchableIndex:completion:]
+ +[_CSSearchPipelineExecutor executeStage:stageResults:stageMap:attributeTranslator:customStageHandler:promptedStageHandler:searchableIndex:boundVariables:completion:]
+ +[_CSSearchPipelineExecutor executeStagesInOrder:pipeline:customStageHandler:promptedStageHandler:searchableIndex:completion:]
+ -[CSBundleFilterAttributeBackfillGroup .cxx_destruct]
+ -[CSBundleFilterAttributeBackfillGroup attributeName]
+ -[CSBundleFilterAttributeBackfillGroup bundleID]
+ -[CSBundleFilterAttributeBackfillGroup encodeWithCoder:]
+ -[CSBundleFilterAttributeBackfillGroup identifiers]
+ -[CSBundleFilterAttributeBackfillGroup initWithBundleID:attributeName:protectionClass:identifiers:]
+ -[CSBundleFilterAttributeBackfillGroup initWithCoder:]
+ -[CSBundleFilterAttributeBackfillGroup protectionClass]
+ -[CSBundleFilterAttributeBackfillResult .cxx_destruct]
+ -[CSBundleFilterAttributeBackfillResult bundleID]
+ -[CSBundleFilterAttributeBackfillResult confirmedAbsentIdentifiers]
+ -[CSBundleFilterAttributeBackfillResult encodeWithCoder:]
+ -[CSBundleFilterAttributeBackfillResult initWithBundleID:resolvedValues:confirmedAbsentIdentifiers:]
+ -[CSBundleFilterAttributeBackfillResult initWithCoder:]
+ -[CSBundleFilterAttributeBackfillResult resolvedValues]
+ -[CSBundleFilterEvaluationReply .cxx_destruct]
+ -[CSBundleFilterEvaluationReply attributeBackfillResults]
+ -[CSBundleFilterEvaluationReply encodeWithCoder:]
+ -[CSBundleFilterEvaluationReply excludedAppBundleIdentifiers]
+ -[CSBundleFilterEvaluationReply fileProviderMatchedIdentifiers]
+ -[CSBundleFilterEvaluationReply fileProviderUnresolvedIdentifiers]
+ -[CSBundleFilterEvaluationReply hiddenAppBundleIdentifiers]
+ -[CSBundleFilterEvaluationReply initWithCoder:]
+ -[CSBundleFilterEvaluationReply initWithFileProviderMatchedIdentifiers:fileProviderUnresolvedIdentifiers:lockedAppBundleIdentifiers:hiddenAppBundleIdentifiers:mdmRestrictedBundleIdentifiers:excludedAppBundleIdentifiers:attributeBackfillResults:]
+ -[CSBundleFilterEvaluationReply lockedAppBundleIdentifiers]
+ -[CSBundleFilterEvaluationReply mdmRestrictedBundleIdentifiers]
+ -[CSBundleFilterEvaluationRequest .cxx_destruct]
+ -[CSBundleFilterEvaluationRequest attributeBackfillGroups]
+ -[CSBundleFilterEvaluationRequest encodeWithCoder:]
+ -[CSBundleFilterEvaluationRequest fileProviderContainerGroups]
+ -[CSBundleFilterEvaluationRequest fileProviderExcludedBundleIDs]
+ -[CSBundleFilterEvaluationRequest initWithCoder:]
+ -[CSBundleFilterEvaluationRequest initWithFileProviderContainerGroups:fileProviderExcludedBundleIDs:needsAppProtectionBundleIDs:needsMDMRestrictedBundleIDs:needsExcludedAppBundleIDs:attributeBackfillGroups:]
+ -[CSBundleFilterEvaluationRequest needsAppProtectionBundleIDs]
+ -[CSBundleFilterEvaluationRequest needsExcludedAppBundleIDs]
+ -[CSBundleFilterEvaluationRequest needsMDMRestrictedBundleIDs]
+ -[CSBundleFilterFileProviderContainerGroup .cxx_destruct]
+ -[CSBundleFilterFileProviderContainerGroup bundleID]
+ -[CSBundleFilterFileProviderContainerGroup encodeWithCoder:]
+ -[CSBundleFilterFileProviderContainerGroup identifiers]
+ -[CSBundleFilterFileProviderContainerGroup initWithBundleID:identifiers:knownOIDPaths:]
+ -[CSBundleFilterFileProviderContainerGroup initWithCoder:]
+ -[CSBundleFilterFileProviderContainerGroup knownOIDPaths]
+ -[CSCoder abandonBuildPastStackReserve]
+ -[CSCoder abandoned]
+ -[CSSearchConnection _test_issueAndCancelDummyQueryWithID:]
+ -[CSSearchQuery didResolveFriendlyAttributeNames:resolvedFetchAttributes:]
+ -[CSSearchQueryContext allDisabledBundlesSet]
+ -[CSSearchQueryContext federationDisabledBundles]
+ -[CSSearchQueryContext predicateFrameworkGenerated]
+ -[CSSearchQueryContext predicateSearchToolGenerated]
+ -[CSSearchQueryContext setFederationDisabledBundles:]
+ -[CSSearchQueryContext setPredicateFrameworkGenerated:]
+ -[CSSearchQueryContext setPredicateSearchToolGenerated:]
+ -[CSSearchableIndex _evaluateFilters:completionHandler:]
+ -[CSSearchableItem filteringResult]
+ -[CSSearchableItem setFilteringResult:]
+ -[_CSHydrationStage applyDelegateReplacementForIdentifier:atIndex:handledSnapshot:into:]
+ -[_CSHydrationStage collectDelegateItems:requested:into:]
+ -[_CSHydrationStage dispatchDelegateHydration:index:identifiersByBundle:group:collectInto:]
+ -[_CSHydrationStage dispatchDelegateHydrationForBundleIdentifiers:delegate:index:variant:group:collectInto:]
+ -[_CSHydrationStage hydrateItemViaDataProvider:bundleID:contentTypes:timeout:index:completion:]
+ -[_CSHydrationStage hydrateItemWithIdentifier:bundleID:path:contentTypes:timeout:maxFileSize:allowFileSystem:index:completion:]
+ -[_CSHydrationStage remainingIdentifiers:notHandledIn:]
+ -[_CSHydrationStage runIndexHydrationForInput:identifiersByBundle:handledSnapshot:index:context:hydrationAttributes:contentTypes:timeout:maxFileSize:allowFileSystem:completion:]
+ -[_CSSearchPipelineExecutionContext searchableIndex]
+ -[_CSSearchPipelineExecutionContext setSearchableIndex:]
+ GCC_except_table100
+ GCC_except_table104
+ GCC_except_table107
+ GCC_except_table1083
+ GCC_except_table112
+ GCC_except_table113
+ GCC_except_table117
+ GCC_except_table132
+ GCC_except_table133
+ GCC_except_table139
+ GCC_except_table140
+ GCC_except_table145
+ GCC_except_table148
+ GCC_except_table152
+ GCC_except_table155
+ GCC_except_table156
+ GCC_except_table163
+ GCC_except_table1661
+ GCC_except_table1669
+ GCC_except_table167
+ GCC_except_table176
+ GCC_except_table177
+ GCC_except_table181
+ GCC_except_table185
+ GCC_except_table188
+ GCC_except_table189
+ GCC_except_table194
+ GCC_except_table214
+ GCC_except_table217
+ GCC_except_table221
+ GCC_except_table222
+ GCC_except_table226
+ GCC_except_table227
+ GCC_except_table231
+ GCC_except_table236
+ GCC_except_table239
+ GCC_except_table247
+ GCC_except_table252
+ GCC_except_table255
+ GCC_except_table260
+ GCC_except_table262
+ GCC_except_table266
+ GCC_except_table267
+ GCC_except_table270
+ GCC_except_table275
+ GCC_except_table278
+ GCC_except_table288
+ GCC_except_table29
+ GCC_except_table301
+ GCC_except_table306
+ GCC_except_table309
+ GCC_except_table310
+ GCC_except_table311
+ GCC_except_table314
+ GCC_except_table319
+ GCC_except_table324
+ GCC_except_table330
+ GCC_except_table334
+ GCC_except_table337
+ GCC_except_table338
+ GCC_except_table342
+ GCC_except_table344
+ GCC_except_table346
+ GCC_except_table348
+ GCC_except_table366
+ GCC_except_table367
+ GCC_except_table370
+ GCC_except_table371
+ GCC_except_table374
+ GCC_except_table375
+ GCC_except_table378
+ GCC_except_table379
+ GCC_except_table380
+ GCC_except_table381
+ GCC_except_table382
+ GCC_except_table383
+ GCC_except_table39
+ GCC_except_table395
+ GCC_except_table407
+ GCC_except_table408
+ GCC_except_table412
+ GCC_except_table416
+ GCC_except_table421
+ GCC_except_table423
+ GCC_except_table429
+ GCC_except_table442
+ GCC_except_table443
+ GCC_except_table446
+ GCC_except_table452
+ GCC_except_table462
+ GCC_except_table472
+ GCC_except_table477
+ GCC_except_table482
+ GCC_except_table56
+ GCC_except_table568
+ GCC_except_table569
+ GCC_except_table570
+ GCC_except_table571
+ GCC_except_table579
+ GCC_except_table621
+ GCC_except_table675
+ GCC_except_table68
+ GCC_except_table80
+ GCC_except_table93
+ GCC_except_table96
+ OBJC_IVAR_$_CSBundleFilterAttributeBackfillGroup._attributeName
+ OBJC_IVAR_$_CSBundleFilterAttributeBackfillGroup._bundleID
+ OBJC_IVAR_$_CSBundleFilterAttributeBackfillGroup._identifiers
+ OBJC_IVAR_$_CSBundleFilterAttributeBackfillGroup._protectionClass
+ OBJC_IVAR_$_CSBundleFilterAttributeBackfillResult._bundleID
+ OBJC_IVAR_$_CSBundleFilterAttributeBackfillResult._confirmedAbsentIdentifiers
+ OBJC_IVAR_$_CSBundleFilterAttributeBackfillResult._resolvedValues
+ OBJC_IVAR_$_CSBundleFilterEvaluationReply._attributeBackfillResults
+ OBJC_IVAR_$_CSBundleFilterEvaluationReply._excludedAppBundleIdentifiers
+ OBJC_IVAR_$_CSBundleFilterEvaluationReply._fileProviderMatchedIdentifiers
+ OBJC_IVAR_$_CSBundleFilterEvaluationReply._fileProviderUnresolvedIdentifiers
+ OBJC_IVAR_$_CSBundleFilterEvaluationReply._hiddenAppBundleIdentifiers
+ OBJC_IVAR_$_CSBundleFilterEvaluationReply._lockedAppBundleIdentifiers
+ OBJC_IVAR_$_CSBundleFilterEvaluationReply._mdmRestrictedBundleIdentifiers
+ OBJC_IVAR_$_CSBundleFilterEvaluationRequest._attributeBackfillGroups
+ OBJC_IVAR_$_CSBundleFilterEvaluationRequest._fileProviderContainerGroups
+ OBJC_IVAR_$_CSBundleFilterEvaluationRequest._fileProviderExcludedBundleIDs
+ OBJC_IVAR_$_CSBundleFilterEvaluationRequest._needsAppProtectionBundleIDs
+ OBJC_IVAR_$_CSBundleFilterEvaluationRequest._needsExcludedAppBundleIDs
+ OBJC_IVAR_$_CSBundleFilterEvaluationRequest._needsMDMRestrictedBundleIDs
+ OBJC_IVAR_$_CSBundleFilterFileProviderContainerGroup._bundleID
+ OBJC_IVAR_$_CSBundleFilterFileProviderContainerGroup._identifiers
+ OBJC_IVAR_$_CSBundleFilterFileProviderContainerGroup._knownOIDPaths
+ OBJC_IVAR_$_CSCoder._abandoned
+ OBJC_IVAR_$_CSFileProviderDomainMonitor._savedRemovedCount
+ OBJC_IVAR_$_CSSearchQueryContext._allDisabledBundlesSet
+ OBJC_IVAR_$_CSSearchQueryContext._federationDisabledBundles
+ OBJC_IVAR_$_CSSearchableItem._filePathLock
+ OBJC_IVAR_$_CSSearchableItem._filteringResult
+ OBJC_IVAR_$__CSSearchPipelineExecutionContext._searchableIndex
+ _CSShouldTraceMessagesDonation
+ _NSURLFileSizeKey
+ _OBJC_CLASS_$_CSBundleFilterAttributeBackfillGroup
+ _OBJC_CLASS_$_CSBundleFilterAttributeBackfillResult
+ _OBJC_CLASS_$_CSBundleFilterEvaluationReply
+ _OBJC_CLASS_$_CSBundleFilterEvaluationRequest
+ _OBJC_CLASS_$_CSBundleFilterFileProviderContainerGroup
+ _OBJC_METACLASS_$_CSBundleFilterAttributeBackfillGroup
+ _OBJC_METACLASS_$_CSBundleFilterAttributeBackfillResult
+ _OBJC_METACLASS_$_CSBundleFilterEvaluationReply
+ _OBJC_METACLASS_$_CSBundleFilterEvaluationRequest
+ _OBJC_METACLASS_$_CSBundleFilterFileProviderContainerGroup
+ _PRBuildQueryTree
+ __108-[_CSHydrationStage dispatchDelegateHydrationForBundleIdentifiers:delegate:index:variant:group:collectInto:]_block_invoke
+ __177-[_CSHydrationStage runIndexHydrationForInput:identifiersByBundle:handledSnapshot:index:context:hydrationAttributes:contentTypes:timeout:maxFileSize:allowFileSystem:completion:]_block_invoke
+ __177-[_CSHydrationStage runIndexHydrationForInput:identifiersByBundle:handledSnapshot:index:context:hydrationAttributes:contentTypes:timeout:maxFileSize:allowFileSystem:completion:]_block_invoke_2
+ __196+[_CSSearchPipelineExecutor executeNextStage:index:stageResults:stageMap:attributeTranslator:customStageHandler:promptedStageHandler:searchableIndex:boundVariables:extractValueConfigs:completion:]_block_invoke
+ __56-[CSSearchableIndex _evaluateFilters:completionHandler:]_block_invoke
+ __74-[CSSearchQuery didResolveFriendlyAttributeNames:resolvedFetchAttributes:]_block_invoke
+ __MDPlistContainerAbandonBuild
+ __MDPlistContainerAddNullValue
+ __MDPlistContainerAllocFailure
+ __OBJC_$_CLASS_METHODS_CSBundleFilterAttributeBackfillGroup
+ __OBJC_$_CLASS_METHODS_CSBundleFilterAttributeBackfillResult
+ __OBJC_$_CLASS_METHODS_CSBundleFilterEvaluationReply
+ __OBJC_$_CLASS_METHODS_CSBundleFilterEvaluationRequest
+ __OBJC_$_CLASS_METHODS_CSBundleFilterFileProviderContainerGroup
+ __OBJC_$_CLASS_PROP_LIST_CSBundleFilterAttributeBackfillGroup
+ __OBJC_$_CLASS_PROP_LIST_CSBundleFilterAttributeBackfillResult
+ __OBJC_$_CLASS_PROP_LIST_CSBundleFilterEvaluationReply
+ __OBJC_$_CLASS_PROP_LIST_CSBundleFilterEvaluationRequest
+ __OBJC_$_CLASS_PROP_LIST_CSBundleFilterFileProviderContainerGroup
+ __OBJC_$_INSTANCE_METHODS_CSBundleFilterAttributeBackfillGroup
+ __OBJC_$_INSTANCE_METHODS_CSBundleFilterAttributeBackfillResult
+ __OBJC_$_INSTANCE_METHODS_CSBundleFilterEvaluationReply
+ __OBJC_$_INSTANCE_METHODS_CSBundleFilterEvaluationRequest
+ __OBJC_$_INSTANCE_METHODS_CSBundleFilterFileProviderContainerGroup
+ __OBJC_$_INSTANCE_VARIABLES_CSBundleFilterAttributeBackfillGroup
+ __OBJC_$_INSTANCE_VARIABLES_CSBundleFilterAttributeBackfillResult
+ __OBJC_$_INSTANCE_VARIABLES_CSBundleFilterEvaluationReply
+ __OBJC_$_INSTANCE_VARIABLES_CSBundleFilterEvaluationRequest
+ __OBJC_$_INSTANCE_VARIABLES_CSBundleFilterFileProviderContainerGroup
+ __OBJC_$_PROP_LIST_CSBundleFilterAttributeBackfillGroup
+ __OBJC_$_PROP_LIST_CSBundleFilterAttributeBackfillResult
+ __OBJC_$_PROP_LIST_CSBundleFilterEvaluationReply
+ __OBJC_$_PROP_LIST_CSBundleFilterEvaluationRequest
+ __OBJC_$_PROP_LIST_CSBundleFilterFileProviderContainerGroup
+ __OBJC_CLASS_PROTOCOLS_$_CSBundleFilterAttributeBackfillGroup
+ __OBJC_CLASS_PROTOCOLS_$_CSBundleFilterAttributeBackfillResult
+ __OBJC_CLASS_PROTOCOLS_$_CSBundleFilterEvaluationReply
+ __OBJC_CLASS_PROTOCOLS_$_CSBundleFilterEvaluationRequest
+ __OBJC_CLASS_PROTOCOLS_$_CSBundleFilterFileProviderContainerGroup
+ __OBJC_CLASS_RO_$_CSBundleFilterAttributeBackfillGroup
+ __OBJC_CLASS_RO_$_CSBundleFilterAttributeBackfillResult
+ __OBJC_CLASS_RO_$_CSBundleFilterEvaluationReply
+ __OBJC_CLASS_RO_$_CSBundleFilterEvaluationRequest
+ __OBJC_CLASS_RO_$_CSBundleFilterFileProviderContainerGroup
+ __OBJC_METACLASS_RO_$_CSBundleFilterAttributeBackfillGroup
+ __OBJC_METACLASS_RO_$_CSBundleFilterAttributeBackfillResult
+ __OBJC_METACLASS_RO_$_CSBundleFilterEvaluationReply
+ __OBJC_METACLASS_RO_$_CSBundleFilterEvaluationRequest
+ __OBJC_METACLASS_RO_$_CSBundleFilterFileProviderContainerGroup
+ ___108-[_CSHydrationStage dispatchDelegateHydrationForBundleIdentifiers:delegate:index:variant:group:collectInto:]_block_invoke
+ ___112+[_CSSearchPipelineExecutor executePipeline:customStageHandler:promptedStageHandler:searchableIndex:completion:]_block_invoke
+ ___127-[_CSHydrationStage hydrateItemWithIdentifier:bundleID:path:contentTypes:timeout:maxFileSize:allowFileSystem:index:completion:]_block_invoke
+ ___177-[_CSHydrationStage runIndexHydrationForInput:identifiersByBundle:handledSnapshot:index:context:hydrationAttributes:contentTypes:timeout:maxFileSize:allowFileSystem:completion:]_block_invoke
+ ___177-[_CSHydrationStage runIndexHydrationForInput:identifiersByBundle:handledSnapshot:index:context:hydrationAttributes:contentTypes:timeout:maxFileSize:allowFileSystem:completion:]_block_invoke_2
+ ___196+[_CSSearchPipelineExecutor executeNextStage:index:stageResults:stageMap:attributeTranslator:customStageHandler:promptedStageHandler:searchableIndex:boundVariables:extractValueConfigs:completion:]_block_invoke
+ ___49+[CSSearchConnection _test_setGameModeSuspended:]_block_invoke
+ ___49+[CSSearchConnection _test_setGameModeSuspended:]_block_invoke_2
+ ___56-[CSSearchableIndex _evaluateFilters:completionHandler:]_block_invoke
+ ___56-[CSSearchableIndex _evaluateFilters:completionHandler:]_block_invoke_2
+ ___56-[CSSearchableIndex _evaluateFilters:completionHandler:]_block_invoke_3
+ ___74-[CSSearchQuery didResolveFriendlyAttributeNames:resolvedFetchAttributes:]_block_invoke
+ ___75+[_CSSearchPipelineExecutor executePipeline:configuration:typedCompletion:]_block_invoke
+ ___75+[_CSSearchPipelineExecutor executePipeline:configuration:typedCompletion:]_block_invoke_2
+ ___block_descriptor_113_ea8_32s40s48s56s64s72s80s88bs_e5_v8?0l
+ ___block_descriptor_137_ea8_32s40s48s56s64s72s80s88s96s104s112bs_e5_v8?0l
+ ___block_descriptor_144_e8_32s40s48s56s64s72s80s88s96s104s112bs120bs_e20_v24?08"NSError"16l
+ ___block_descriptor_222_e8_32s40s48s56s64s72s80s88s96s104s112s120s128s136s144s152s160w_e5_v8?0l
+ ___block_descriptor_33_e5_v8?0l
+ ___block_descriptor_40_e8_32s_e41_B24?0"CSTopHitResult"8"NSDictionary"16l
+ ___block_descriptor_48_ea8_32s40r_e5_B8?0l
+ ___block_descriptor_52_e8_32s40bs_e17_v16?0"NSError"8l
+ ___block_descriptor_56_e8_32s40s_e19_v32?0{?=*Q{?=IC}}8l
+ ___block_descriptor_56_e8_32s40s_e26_v48?0r*8Q16{?=*Q{?=IC}}24l
+ ___block_descriptor_72_ea8_32s40s48s56s64bs_e17_v16?0"NSArray"8l
+ ___copy_helper_block_e8_32s40s48s56s64s72s80s88s96s104s112b120b
+ ___copy_helper_block_e8_32s40s48s56s64s72s80s88s96s104s112s120s128s136s144s152s160w
+ ___copy_helper_block_ea8_32s40r
+ ___copy_helper_block_ea8_32s40s48s56s64b
+ ___copy_helper_block_ea8_32s40s48s56s64s72s80s88b
+ ___copy_helper_block_ea8_32s40s48s56s64s72s80s88s96s104s112b
+ ___decodeObject_block_invoke
+ ___decodeObject_block_invoke_2
+ ___destroy_helper_block_e8_32s40s48s56s64s72s80s88s96s104s112s120s128s136s144s152s160w
+ ___destroy_helper_block_ea8_32s40r
+ ___destroy_helper_block_ea8_32s40s48s56s64s
+ ___destroy_helper_block_ea8_32s40s48s56s64s72s80s88s
+ ___destroy_helper_block_ea8_32s40s48s56s64s72s80s88s96s104s112s
+ ___dropHomeWeakRetrievalItems_block_invoke
+ ___getSSHomeItemBelowRetrievalThresholdsSymbolLoc_block_invoke
+ ___logForCSLogCategoryDonationTracing_block_invoke
+ __decodeObject_block_invoke
+ __dropHomeWeakRetrievalItems_block_invoke
+ _coderStackFloor
+ _decodeObject
+ _logForCSLogCategoryDonationTracing
+ _objc_msgSend$abandonBuildPastStackReserve
+ _objc_msgSend$abandoned
+ _objc_msgSend$applyDelegateReplacementForIdentifier:atIndex:handledSnapshot:into:
+ _objc_msgSend$attributeBackfillGroups
+ _objc_msgSend$cancelQuery:
+ _objc_msgSend$collectDelegateItems:requested:into:
+ _objc_msgSend$decodeArrayOfObjectsOfClass:forKey:
+ _objc_msgSend$decodeDictionaryWithKeysOfClass:objectsOfClass:forKey:
+ _objc_msgSend$didResolveFriendlyAttributeNames:resolvedFetchAttributes:
+ _objc_msgSend$dispatchDelegateHydration:index:identifiersByBundle:group:collectInto:
+ _objc_msgSend$dispatchDelegateHydrationForBundleIdentifiers:delegate:index:variant:group:collectInto:
+ _objc_msgSend$executeNextStage:index:stageResults:stageMap:attributeTranslator:customStageHandler:promptedStageHandler:searchableIndex:boundVariables:extractValueConfigs:completion:
+ _objc_msgSend$executePipeline:configuration:typedCompletion:
+ _objc_msgSend$executePipeline:customStageHandler:promptedStageHandler:searchableIndex:completion:
+ _objc_msgSend$executeStage:stageResults:stageMap:attributeTranslator:customStageHandler:promptedStageHandler:searchableIndex:boundVariables:completion:
+ _objc_msgSend$executeStagesInOrder:pipeline:customStageHandler:promptedStageHandler:searchableIndex:completion:
+ _objc_msgSend$federationDisabledBundles
+ _objc_msgSend$fileProviderContainerGroups
+ _objc_msgSend$filterUsingPredicate:
+ _objc_msgSend$hydrateItemViaDataProvider:bundleID:contentTypes:timeout:index:completion:
+ _objc_msgSend$hydrateItemWithIdentifier:bundleID:path:contentTypes:timeout:maxFileSize:allowFileSystem:index:completion:
+ _objc_msgSend$initWithFileProviderMatchedIdentifiers:fileProviderUnresolvedIdentifiers:lockedAppBundleIdentifiers:hiddenAppBundleIdentifiers:mdmRestrictedBundleIdentifiers:excludedAppBundleIdentifiers:attributeBackfillResults:
+ _objc_msgSend$needsAppProtectionBundleIDs
+ _objc_msgSend$needsExcludedAppBundleIDs
+ _objc_msgSend$needsMDMRestrictedBundleIDs
+ _objc_msgSend$remainingIdentifiers:notHandledIn:
+ _objc_msgSend$removeItemAtURL:error:
+ _objc_msgSend$runIndexHydrationForInput:identifiersByBundle:handledSnapshot:index:context:hydrationAttributes:contentTypes:timeout:maxFileSize:allowFileSystem:completion:
+ _objc_msgSend$searchableItemsForIdentifiers:protectionClass:searchableItemsHandler:
+ _objc_msgSend$searchableItemsForIdentifiers:searchableItemsHandler:
+ _objc_msgSend$setFederationDisabledBundles:
+ _objc_msgSend$setPredicateFrameworkGenerated:
+ _objc_msgSend$setPredicateSearchToolGenerated:
+ _pthread_get_stackaddr_np
+ _pthread_get_stacksize_np
+ _pthread_self
+ _quotedValue
+ _representativeUTIForSelector
+ _sDonationXPCTraceID
+ decodeObject
+ encodeStackFloor.memo
+ encodeStackFloor.memo$tlv$init
+ getSSHomeItemBelowRetrievalThresholdsSymbolLoc.ptr
+ logForCSLogCategoryDonationTracing
+ logForCSLogCategoryDonationTracing.onceToken
+ logForCSLogCategoryDonationTracing.sDonationTracingLog
+ reportDecodeStackHeadroomExhausted.rejectionCount
+ reportEncodeStackHeadroomExhausted.rejectionCount
- +[_CSSearchPipelineExecutor executeNextStage:index:stageResults:stageMap:attributeTranslator:customStageHandler:promptedStageHandler:boundVariables:extractValueConfigs:completion:]
- +[_CSSearchPipelineExecutor executeStage:stageResults:stageMap:attributeTranslator:customStageHandler:promptedStageHandler:boundVariables:completion:]
- +[_CSSearchPipelineExecutor executeStagesInOrder:pipeline:customStageHandler:promptedStageHandler:completion:]
- -[CSSearchQuery didResolveFriendlyAttributeNames:fromFetchAttributes:]
- -[CSSearchableItemAttributeSet(CSPrivateAttributes) _standardizeProcessorAttributesForBundle:protectionClass:isUpdate:]
- -[_CSHydrationStage hydrateItemViaDataProvider:bundleID:contentTypes:timeout:completion:]
- -[_CSHydrationStage hydrateItemWithIdentifier:bundleID:path:contentTypes:timeout:maxFileSize:allowFileSystem:completion:]
- GCC_except_table102
- GCC_except_table105
- GCC_except_table1084
- GCC_except_table115
- GCC_except_table116
- GCC_except_table124
- GCC_except_table127
- GCC_except_table135
- GCC_except_table143
- GCC_except_table147
- GCC_except_table150
- GCC_except_table153
- GCC_except_table161
- GCC_except_table165
- GCC_except_table1666
- GCC_except_table1674
- GCC_except_table169
- GCC_except_table179
- GCC_except_table183
- GCC_except_table186
- GCC_except_table187
- GCC_except_table192
- GCC_except_table197
- GCC_except_table198
- GCC_except_table205
- GCC_except_table213
- GCC_except_table223
- GCC_except_table224
- GCC_except_table225
- GCC_except_table228
- GCC_except_table229
- GCC_except_table232
- GCC_except_table233
- GCC_except_table237
- GCC_except_table238
- GCC_except_table241
- GCC_except_table242
- GCC_except_table245
- GCC_except_table249
- GCC_except_table250
- GCC_except_table257
- GCC_except_table264
- GCC_except_table269
- GCC_except_table271
- GCC_except_table273
- GCC_except_table280
- GCC_except_table282
- GCC_except_table284
- GCC_except_table285
- GCC_except_table287
- GCC_except_table289
- GCC_except_table293
- GCC_except_table294
- GCC_except_table299
- GCC_except_table305
- GCC_except_table307
- GCC_except_table31
- GCC_except_table312
- GCC_except_table321
- GCC_except_table326
- GCC_except_table331
- GCC_except_table340
- GCC_except_table351
- GCC_except_table352
- GCC_except_table353
- GCC_except_table354
- GCC_except_table355
- GCC_except_table358
- GCC_except_table361
- GCC_except_table363
- GCC_except_table364
- GCC_except_table376
- GCC_except_table377
- GCC_except_table388
- GCC_except_table401
- GCC_except_table402
- GCC_except_table405
- GCC_except_table410
- GCC_except_table415
- GCC_except_table417
- GCC_except_table435
- GCC_except_table436
- GCC_except_table439
- GCC_except_table445
- GCC_except_table449
- GCC_except_table455
- GCC_except_table465
- GCC_except_table475
- GCC_except_table52
- GCC_except_table53
- GCC_except_table561
- GCC_except_table562
- GCC_except_table563
- GCC_except_table564
- GCC_except_table572
- GCC_except_table609
- GCC_except_table663
- GCC_except_table69
- GCC_except_table746
- GCC_except_table82
- GCC_except_table97
- GCC_except_table98
- SpotlightKnowledgeLibraryCore.frameworkLibrary
- _PRBuildDefaultQueryTree
- _PRBuildHomeQueryTree
- _PRBuildMailQueryTree
- _PRBuildMessagesQueryTree
- _PRBuildPhotosQueryTree
- __180+[_CSSearchPipelineExecutor executeNextStage:index:stageResults:stageMap:attributeTranslator:customStageHandler:promptedStageHandler:boundVariables:extractValueConfigs:completion:]_block_invoke
- __51-[_CSHydrationStage executeWithContext:completion:]_block_invoke
- __51-[_CSHydrationStage executeWithContext:completion:]_block_invoke_2
- __70-[CSSearchQuery didResolveFriendlyAttributeNames:fromFetchAttributes:]_block_invoke
- ___121-[_CSHydrationStage hydrateItemWithIdentifier:bundleID:path:contentTypes:timeout:maxFileSize:allowFileSystem:completion:]_block_invoke
- ___180+[_CSSearchPipelineExecutor executeNextStage:index:stageResults:stageMap:attributeTranslator:customStageHandler:promptedStageHandler:boundVariables:extractValueConfigs:completion:]_block_invoke
- ___213-[CSSearchableIndex indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:updatingDonationProgress:protectionClass:forBundleID:options:reason:completionHandler:]_block_invoke_2
- ___51-[_CSHydrationStage executeWithContext:completion:]_block_invoke_2
- ___61+[_CSSearchPipelineExecutor executePipeline:typedCompletion:]_block_invoke
- ___61+[_CSSearchPipelineExecutor executePipeline:typedCompletion:]_block_invoke_2
- ___70-[CSSearchQuery didResolveFriendlyAttributeNames:fromFetchAttributes:]_block_invoke
- ___96+[_CSSearchPipelineExecutor executePipeline:customStageHandler:promptedStageHandler:completion:]_block_invoke
- ___CSDecodeObject_block_invoke
- ___SpotlightKnowledgeLibraryCore_block_invoke
- ____CSDecodeObject_block_invoke
- ____CSDecodeObject_block_invoke_2
- ___block_descriptor_136_e8_32s40s48s56s64s72s80s88s96s104bs112bs_e20_v24?08"NSError"16l
- ___block_descriptor_209_e8_32s40s48s56s64s72s80s88s96s104s112s120s128s136s144s152w_e5_v8?0l
- ___block_descriptor_48_e8_32s40s_e19_v32?0{?=*Q{?=IC}}8l
- ___block_descriptor_97_ea8_32s40s48s56s64s72bs_e5_v8?0l
- ___copy_helper_block_e8_32s40s48s56s64s72s80s88s96s104b112b
- ___copy_helper_block_e8_32s40s48s56s64s72s80s88s96s104s112s120s128s136s144s152w
- ___copy_helper_block_ea8_32s40s48s56s64s72b
- ___destroy_helper_block_e8_32s40s48s56s64s72s80s88s96s104s112s
- ___destroy_helper_block_e8_32s40s48s56s64s72s80s88s96s104s112s120s128s136s144s152w
- ___destroy_helper_block_ea8_32s40s48s56s64s72s
- ___getSKGAttributeProcessorClass_block_invoke
- __getSKGAttributeProcessorClass_block_invoke
- _audit_stringSpotlightKnowledge
- _objc_msgSend$_standardizeProcessorAttributesForBundle:protectionClass:isUpdate:
- _objc_msgSend$didResolveFriendlyAttributeNames:fromFetchAttributes:
- _objc_msgSend$executeNextStage:index:stageResults:stageMap:attributeTranslator:customStageHandler:promptedStageHandler:boundVariables:extractValueConfigs:completion:
- _objc_msgSend$executePipeline:customStageHandler:promptedStageHandler:completion:
- _objc_msgSend$executePipeline:typedCompletion:
- _objc_msgSend$executeStage:stageResults:stageMap:attributeTranslator:customStageHandler:promptedStageHandler:boundVariables:completion:
- _objc_msgSend$executeStagesInOrder:pipeline:customStageHandler:promptedStageHandler:completion:
- _objc_msgSend$hydrateItemViaDataProvider:bundleID:contentTypes:timeout:completion:
- _objc_msgSend$hydrateItemWithIdentifier:bundleID:path:contentTypes:timeout:maxFileSize:allowFileSystem:completion:
- _objc_msgSend$processorAttributesForRecord:bundleID:protectionClass:isUpdate:
- _objc_msgSend$sharedProcessor
- getSKGAttributeProcessorClass.softClass
CStrings:
+ "%@ != %@"
+ "%@ = %@"
+ "(%@) refusing donation of %ld items/%ld deletes: encoding was abandoned, so the payload would be silently incomplete"
+ "?P"
+ "At the %lu removed FP domain ceiling; not tracking further removals"
+ "B24@?0@\"CSTopHitResult\"8@\"NSDictionary\"16"
+ "B8@?0"
+ "Discarding saved FP domain list: %llu bytes exceeds the %llu byte budget"
+ "Donation completion block firing, requestID=%u error=%@"
+ "Donation enqueued on CSSearchableIndexRequest, requestID=%u itemCount=%lu"
+ "Donation item manifest, requestID=%u itemIDs=%@"
+ "Donation sending XPC message, requestID=%u donationXPCTraceID=%llu"
+ "DonationTracing"
+ "MessageIndexing"
+ "NoteIndexing"
+ "SSHomeItemBelowRetrievalThresholds"
+ "Saved FP domain list holds %lu entries; tracking the first %lu and ignoring the rest"
+ "[qid=%ld][CSTopHitRanking] bundle=%@ dropped %lu of %lu results below Home retrieval thresholds"
+ "abandoned encoding an excessively nested object (occurrence #%llu): less than %zu bytes of stack headroom remain"
+ "attribute set encoding was abandoned; archiving an empty container so the peer's -initWithCoder: fails rather than decoding an empty attribute set"
+ "attributeBackfillGroups"
+ "attributeBackfillResults"
+ "com.apple.iwork.pages.pages"
+ "com.apple.spotlight.CSSearchConnectionConcurrencyTests.nonexistent"
+ "confirmedAbsentIdentifiers"
+ "donation-xpc-trace-id"
+ "evaluate-filters"
+ "evaluate-filters-data"
+ "evaluate-filters-data-size"
+ "evaluate_filters"
+ "excludedAppBundleIdentifiers"
+ "fdb"
+ "federationDisabledBundles"
+ "fileProviderContainerGroups"
+ "fileProviderExcludedBundleIDs"
+ "fileProviderMatchedIdentifiers"
+ "fileProviderUnresolvedIdentifiers"
+ "hiddenAppBundleIdentifiers"
+ "kMDItemContentTypeTree = %@"
+ "knownOIDPaths"
+ "lockedAppBundleIdentifiers"
+ "mdmRestrictedBundleIdentifiers"
+ "needsAppProtectionBundleIDs"
+ "needsExcludedAppBundleIDs"
+ "needsMDMRestrictedBundleIDs"
+ "org.openxmlformats.wordprocessingml.document"
+ "rejecting excessively nested encoded object (occurrence #%llu): less than %zu bytes of stack headroom remain"
+ "resolvedValues"
- "%@ != \"%@\""
- "%@ = \"%@\""
- "/System/Library/PrivateFrameworks/SpotlightKnowledge.framework/Contents/MacOS/SpotlightKnowledge"
- "SKGAttributeProcessor"
- "SpotlightKnowledge"
- "SpotlightKnowledgePipelineRefactorStandalone"
- "com.apple.pages"
- "com.microsoft.word.docx"
- "softlink:r:path:/System/Library/PrivateFrameworks/SpotlightKnowledge.framework/SpotlightKnowledge"
```
