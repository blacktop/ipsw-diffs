## CoreSpotlight

> `/System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight`

```diff

-2465.1.3.0.0
-  __TEXT.__text: 0x176310
-  __TEXT.__objc_methlist: 0x14440
+2465.1.7.0.0
+  __TEXT.__text: 0x1792f4
+  __TEXT.__objc_methlist: 0x147d8
   __TEXT.__const: 0xf08
-  __TEXT.__gcc_except_tab: 0x94fc
-  __TEXT.__cstring: 0x2bc60
-  __TEXT.__oslogstring: 0xbd15
+  __TEXT.__cstring: 0x2bedd
+  __TEXT.__gcc_except_tab: 0x9718
+  __TEXT.__oslogstring: 0xbf0c
   __TEXT.__ustring: 0x218e
   __TEXT.__dlopen_cstrs: 0x4c4
   __TEXT.__constg_swiftt: 0x1bc

   __TEXT.__swift_as_cont: 0xc
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x7150
+  __TEXT.__unwind_info: 0x7290
   __TEXT.__eh_frame: 0x210
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x65e0
-  __DATA_CONST.__objc_classlist: 0xa90
+  __DATA_CONST.__const: 0x6718
+  __DATA_CONST.__objc_classlist: 0xab8
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa4d8
+  __DATA_CONST.__objc_selrefs: 0xa618
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x720
+  __DATA_CONST.__objc_superrefs: 0x748
   __DATA_CONST.__objc_arraydata: 0x11290
-  __DATA_CONST.__got: 0xe50
-  __AUTH_CONST.__const: 0x2410
-  __AUTH_CONST.__cfstring: 0x2de80
-  __AUTH_CONST.__objc_const: 0x1f820
+  __DATA_CONST.__got: 0xe70
+  __AUTH_CONST.__const: 0x2430
+  __AUTH_CONST.__cfstring: 0x2e140
+  __AUTH_CONST.__objc_const: 0x20100
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x3ae0
   __AUTH_CONST.__objc_dictobj: 0xaf78
   __AUTH_CONST.__objc_intobj: 0xe58
   __AUTH_CONST.__objc_doubleobj: 0x180
   __AUTH_CONST.__objc_floatobj: 0x20
-  __AUTH_CONST.__auth_got: 0x1130
-  __AUTH.__objc_data: 0x5618
+  __AUTH_CONST.__auth_got: 0x1160
+  __AUTH.__objc_data: 0x57a8
   __AUTH.__data: 0x3a0
-  __AUTH.__thread_vars: 0x48
-  __AUTH.__thread_bss: 0x18
-  __DATA.__objc_ivar: 0x1400
+  __AUTH.__thread_vars: 0x60
+  __AUTH.__thread_bss: 0x28
+  __DATA.__objc_ivar: 0x1468
   __DATA.__data: 0x1c60
   __DATA_DIRTY.__objc_data: 0x1388
   __DATA_DIRTY.__data: 0x20

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 8869
-  Symbols:   14514
-  CStrings:  8077
+  Functions: 8955
+  Symbols:   14690
+  CStrings:  8104
 
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
+ -[CSFileProviderContainerCache containerOIDsForOwnerBundleIDs:]
+ -[CSSearchConnection _test_issueAndCancelDummyQueryWithID:]
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
+ GCC_except_table101
+ GCC_except_table108
+ GCC_except_table129
+ GCC_except_table136
+ GCC_except_table141
+ GCC_except_table148
+ GCC_except_table151
+ GCC_except_table152
+ GCC_except_table159
+ GCC_except_table180
+ GCC_except_table198
+ GCC_except_table203
+ GCC_except_table206
+ GCC_except_table207
+ GCC_except_table214
+ GCC_except_table233
+ GCC_except_table234
+ GCC_except_table238
+ GCC_except_table241
+ GCC_except_table242
+ GCC_except_table254
+ GCC_except_table257
+ GCC_except_table262
+ GCC_except_table277
+ GCC_except_table289
+ GCC_except_table29
+ GCC_except_table303
+ GCC_except_table304
+ GCC_except_table308
+ GCC_except_table312
+ GCC_except_table318
+ GCC_except_table320
+ GCC_except_table321
+ GCC_except_table322
+ GCC_except_table337
+ GCC_except_table340
+ GCC_except_table341
+ GCC_except_table345
+ GCC_except_table346
+ GCC_except_table347
+ GCC_except_table349
+ GCC_except_table354
+ GCC_except_table355
+ GCC_except_table362
+ GCC_except_table363
+ GCC_except_table371
+ GCC_except_table373
+ GCC_except_table529
+ GCC_except_table576
+ GCC_except_table65
+ GCC_except_table72
+ GCC_except_table93
+ _OBJC_CLASS_$_CSBundleFilterAttributeBackfillGroup
+ _OBJC_CLASS_$_CSBundleFilterAttributeBackfillResult
+ _OBJC_CLASS_$_CSBundleFilterEvaluationReply
+ _OBJC_CLASS_$_CSBundleFilterEvaluationRequest
+ _OBJC_CLASS_$_CSBundleFilterFileProviderContainerGroup
+ _OBJC_IVAR_$_CSBundleFilterAttributeBackfillGroup._attributeName
+ _OBJC_IVAR_$_CSBundleFilterAttributeBackfillGroup._bundleID
+ _OBJC_IVAR_$_CSBundleFilterAttributeBackfillGroup._identifiers
+ _OBJC_IVAR_$_CSBundleFilterAttributeBackfillGroup._protectionClass
+ _OBJC_IVAR_$_CSBundleFilterAttributeBackfillResult._bundleID
+ _OBJC_IVAR_$_CSBundleFilterAttributeBackfillResult._confirmedAbsentIdentifiers
+ _OBJC_IVAR_$_CSBundleFilterAttributeBackfillResult._resolvedValues
+ _OBJC_IVAR_$_CSBundleFilterEvaluationReply._attributeBackfillResults
+ _OBJC_IVAR_$_CSBundleFilterEvaluationReply._excludedAppBundleIdentifiers
+ _OBJC_IVAR_$_CSBundleFilterEvaluationReply._fileProviderMatchedIdentifiers
+ _OBJC_IVAR_$_CSBundleFilterEvaluationReply._fileProviderUnresolvedIdentifiers
+ _OBJC_IVAR_$_CSBundleFilterEvaluationReply._hiddenAppBundleIdentifiers
+ _OBJC_IVAR_$_CSBundleFilterEvaluationReply._lockedAppBundleIdentifiers
+ _OBJC_IVAR_$_CSBundleFilterEvaluationReply._mdmRestrictedBundleIdentifiers
+ _OBJC_IVAR_$_CSBundleFilterEvaluationRequest._attributeBackfillGroups
+ _OBJC_IVAR_$_CSBundleFilterEvaluationRequest._fileProviderContainerGroups
+ _OBJC_IVAR_$_CSBundleFilterEvaluationRequest._fileProviderExcludedBundleIDs
+ _OBJC_IVAR_$_CSBundleFilterEvaluationRequest._needsAppProtectionBundleIDs
+ _OBJC_IVAR_$_CSBundleFilterEvaluationRequest._needsExcludedAppBundleIDs
+ _OBJC_IVAR_$_CSBundleFilterEvaluationRequest._needsMDMRestrictedBundleIDs
+ _OBJC_IVAR_$_CSBundleFilterFileProviderContainerGroup._bundleID
+ _OBJC_IVAR_$_CSBundleFilterFileProviderContainerGroup._identifiers
+ _OBJC_IVAR_$_CSBundleFilterFileProviderContainerGroup._knownOIDPaths
+ _OBJC_IVAR_$_CSCoder._abandoned
+ _OBJC_IVAR_$_CSSearchableItem._filteringResult
+ _OBJC_IVAR_$__CSSearchPipelineExecutionContext._searchableIndex
+ _OBJC_METACLASS_$_CSBundleFilterAttributeBackfillGroup
+ _OBJC_METACLASS_$_CSBundleFilterAttributeBackfillResult
+ _OBJC_METACLASS_$_CSBundleFilterEvaluationReply
+ _OBJC_METACLASS_$_CSBundleFilterEvaluationRequest
+ _OBJC_METACLASS_$_CSBundleFilterFileProviderContainerGroup
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
+ ___108-[_CSHydrationStage dispatchDelegateHydrationForBundleIdentifiers:delegate:index:variant:group:collectInto:]_block_invoke_2
+ ___112+[_CSSearchPipelineExecutor executePipeline:customStageHandler:promptedStageHandler:searchableIndex:completion:]_block_invoke
+ ___127-[_CSHydrationStage hydrateItemWithIdentifier:bundleID:path:contentTypes:timeout:maxFileSize:allowFileSystem:index:completion:]_block_invoke
+ ___177-[_CSHydrationStage runIndexHydrationForInput:identifiersByBundle:handledSnapshot:index:context:hydrationAttributes:contentTypes:timeout:maxFileSize:allowFileSystem:completion:]_block_invoke
+ ___177-[_CSHydrationStage runIndexHydrationForInput:identifiersByBundle:handledSnapshot:index:context:hydrationAttributes:contentTypes:timeout:maxFileSize:allowFileSystem:completion:]_block_invoke_2
+ ___177-[_CSHydrationStage runIndexHydrationForInput:identifiersByBundle:handledSnapshot:index:context:hydrationAttributes:contentTypes:timeout:maxFileSize:allowFileSystem:completion:]_block_invoke_3
+ ___177-[_CSHydrationStage runIndexHydrationForInput:identifiersByBundle:handledSnapshot:index:context:hydrationAttributes:contentTypes:timeout:maxFileSize:allowFileSystem:completion:]_block_invoke_4
+ ___177-[_CSHydrationStage runIndexHydrationForInput:identifiersByBundle:handledSnapshot:index:context:hydrationAttributes:contentTypes:timeout:maxFileSize:allowFileSystem:completion:]_block_invoke_5
+ ___196+[_CSSearchPipelineExecutor executeNextStage:index:stageResults:stageMap:attributeTranslator:customStageHandler:promptedStageHandler:searchableIndex:boundVariables:extractValueConfigs:completion:]_block_invoke
+ ___49+[CSSearchConnection _test_setGameModeSuspended:]_block_invoke
+ ___49+[CSSearchConnection _test_setGameModeSuspended:]_block_invoke_2
+ ___56-[CSSearchableIndex _evaluateFilters:completionHandler:]_block_invoke
+ ___56-[CSSearchableIndex _evaluateFilters:completionHandler:]_block_invoke_2
+ ___56-[CSSearchableIndex _evaluateFilters:completionHandler:]_block_invoke_3
+ ___56-[CSSearchableIndex _evaluateFilters:completionHandler:]_block_invoke_4
+ ___63-[CSFileProviderContainerCache containerOIDsForOwnerBundleIDs:]_block_invoke
+ ___63-[CSFileProviderContainerCache containerOIDsForOwnerBundleIDs:]_block_invoke_2
+ ___75+[_CSSearchPipelineExecutor executePipeline:configuration:typedCompletion:]_block_invoke
+ ___75+[_CSSearchPipelineExecutor executePipeline:configuration:typedCompletion:]_block_invoke_2
+ ___block_descriptor_113_ea8_32s40s48s56s64s72s80s88bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
+ ___block_descriptor_137_ea8_32s40s48s56s64s72s80s88s96s104s112bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8s112l8
+ ___block_descriptor_144_e8_32s40s48s56s64s72s80s88s96s104s112bs120bs_e20_v24?08"NSError"16ls32l8s112l8s40l8s48l8s56l8s64l8s72l8s80l8s120l8s88l8s96l8s104l8
+ ___block_descriptor_145_e8_32s40s48s56s64s72s80s88s96s104s112s120bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s120l8s72l8s80l8s88l8s96l8s104l8s112l8
+ ___block_descriptor_33_e5_v8?0l
+ ___block_descriptor_48_e8_32s40s_e35_v32?0"NSString"8"NSNumber"16^B24ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e46_v32?0"NSString"8"NSMutableDictionary"16^B24ls32l8s40l8
+ ___block_descriptor_48_ea8_32s40r_e5_B8?0ls32l8r40l8
+ ___block_descriptor_56_e8_32s40s48w_e5_v8?0lw48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40s_e19_v32?0{?=*Q{?=IC}}8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s_e26_v48?0r*8Q16{?=*Q{?=IC}}24ls32l8s40l8
+ ___block_descriptor_72_ea8_32s40s48s56s64bs_e17_v16?0"NSArray"8ls64l8s32l8s40l8s48l8s56l8
+ ___decodeObject_block_invoke
+ ___decodeObject_block_invoke_2
+ ___decodeObject_block_invoke_3
+ ___decodeObject_block_invoke_4
+ _coderStackFloor
+ _decodeObject
+ _encodeStackFloor.memo
+ _encodeStackFloor.memo$tlv$init
+ _pthread_get_stackaddr_np
+ _pthread_get_stacksize_np
+ _pthread_self
+ _quotedValue
+ _reportDecodeStackHeadroomExhausted.rejectionCount
+ _reportEncodeStackHeadroomExhausted.rejectionCount
+ _representativeUTIForSelector
- +[_CSSearchPipelineExecutor executeNextStage:index:stageResults:stageMap:attributeTranslator:customStageHandler:promptedStageHandler:boundVariables:extractValueConfigs:completion:]
- +[_CSSearchPipelineExecutor executeStage:stageResults:stageMap:attributeTranslator:customStageHandler:promptedStageHandler:boundVariables:completion:]
- +[_CSSearchPipelineExecutor executeStagesInOrder:pipeline:customStageHandler:promptedStageHandler:completion:]
- -[_CSHydrationStage hydrateItemViaDataProvider:bundleID:contentTypes:timeout:completion:]
- -[_CSHydrationStage hydrateItemWithIdentifier:bundleID:path:contentTypes:timeout:maxFileSize:allowFileSystem:completion:]
- GCC_except_table102
- GCC_except_table103
- GCC_except_table120
- GCC_except_table133
- GCC_except_table146
- GCC_except_table150
- GCC_except_table157
- GCC_except_table162
- GCC_except_table178
- GCC_except_table179
- GCC_except_table189
- GCC_except_table192
- GCC_except_table197
- GCC_except_table205
- GCC_except_table212
- GCC_except_table216
- GCC_except_table220
- GCC_except_table235
- GCC_except_table253
- GCC_except_table255
- GCC_except_table256
- GCC_except_table265
- GCC_except_table271
- GCC_except_table275
- GCC_except_table281
- GCC_except_table285
- GCC_except_table298
- GCC_except_table300
- GCC_except_table301
- GCC_except_table302
- GCC_except_table31
- GCC_except_table316
- GCC_except_table319
- GCC_except_table323
- GCC_except_table325
- GCC_except_table328
- GCC_except_table331
- GCC_except_table332
- GCC_except_table335
- GCC_except_table336
- GCC_except_table357
- GCC_except_table358
- GCC_except_table361
- GCC_except_table368
- GCC_except_table52
- GCC_except_table524
- GCC_except_table53
- GCC_except_table571
- GCC_except_table63
- GCC_except_table87
- GCC_except_table92
- GCC_except_table97
- ___121-[_CSHydrationStage hydrateItemWithIdentifier:bundleID:path:contentTypes:timeout:maxFileSize:allowFileSystem:completion:]_block_invoke
- ___180+[_CSSearchPipelineExecutor executeNextStage:index:stageResults:stageMap:attributeTranslator:customStageHandler:promptedStageHandler:boundVariables:extractValueConfigs:completion:]_block_invoke
- ___51-[_CSHydrationStage executeWithContext:completion:]_block_invoke_2
- ___51-[_CSHydrationStage executeWithContext:completion:]_block_invoke_3
- ___51-[_CSHydrationStage executeWithContext:completion:]_block_invoke_4
- ___51-[_CSHydrationStage executeWithContext:completion:]_block_invoke_5
- ___61+[_CSSearchPipelineExecutor executePipeline:typedCompletion:]_block_invoke
- ___61+[_CSSearchPipelineExecutor executePipeline:typedCompletion:]_block_invoke_2
- ___96+[_CSSearchPipelineExecutor executePipeline:customStageHandler:promptedStageHandler:completion:]_block_invoke
- ____CSDecodeObject_block_invoke
- ____CSDecodeObject_block_invoke_2
- ____CSDecodeObject_block_invoke_3
- ____CSDecodeObject_block_invoke_4
- ___block_descriptor_136_e8_32s40s48s56s64s72s80s88s96s104bs112bs_e20_v24?08"NSError"16ls32l8s104l8s40l8s48l8s56l8s64l8s72l8s80l8s112l8s88l8s96l8
- ___block_descriptor_145_e8_32s40s48s56s64s72s80s88s96s104s112s120bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8s112l8s120l8
- ___block_descriptor_48_e8_32s40s_e19_v32?0{?=*Q{?=IC}}8ls32l8s40l8
- ___block_descriptor_97_ea8_32s40s48s56s64s72bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8
CStrings:
+ "%@ != %@"
+ "%@ = %@"
+ "(%@) refusing donation of %ld items/%ld deletes: encoding was abandoned, so the payload would be silently incomplete"
+ "B8@?0"
+ "abandoned encoding an excessively nested object (occurrence #%llu): less than %zu bytes of stack headroom remain"
+ "attribute set encoding was abandoned; archiving an empty container so the peer's -initWithCoder: fails rather than decoding an empty attribute set"
+ "attributeBackfillGroups"
+ "attributeBackfillResults"
+ "com.apple.iwork.pages.pages"
+ "com.apple.spotlight.CSSearchConnectionConcurrencyTests.nonexistent"
+ "confirmedAbsentIdentifiers"
+ "evaluate-filters"
+ "evaluate-filters-data"
+ "evaluate-filters-data-size"
+ "evaluate_filters"
+ "excludedAppBundleIdentifiers"
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
- "com.apple.pages"
- "com.microsoft.word.docx"
```
