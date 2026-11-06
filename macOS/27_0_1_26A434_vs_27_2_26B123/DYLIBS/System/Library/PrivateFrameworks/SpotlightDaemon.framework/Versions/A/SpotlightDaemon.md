## SpotlightDaemon

> `/System/Library/PrivateFrameworks/SpotlightDaemon.framework/Versions/A/SpotlightDaemon`

```diff

-2459.405.0.0.0
-  __TEXT.__text: 0xc7888
-  __TEXT.__objc_methlist: 0x4b4c
-  __TEXT.__const: 0x3e8
-  __TEXT.__cstring: 0x981e
-  __TEXT.__gcc_except_tab: 0x46f8
-  __TEXT.__oslogstring: 0xc063
-  __TEXT.__unwind_info: 0x2750
+2465.1.9.0.0
+  __TEXT.__text: 0xcd298
+  __TEXT.__objc_methlist: 0x4d54
+  __TEXT.__const: 0x410
+  __TEXT.__cstring: 0x9d6f
+  __TEXT.__gcc_except_tab: 0x46a8
+  __TEXT.__oslogstring: 0xc426
+  __TEXT.__unwind_info: 0x2890
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x618
-  __DATA_CONST.__objc_classlist: 0x1b8
+  __DATA_CONST.__const: 0x650
+  __DATA_CONST.__objc_classlist: 0x1d8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3be8
+  __DATA_CONST.__objc_selrefs: 0x3dc0
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x138
+  __DATA_CONST.__objc_superrefs: 0x150
   __DATA_CONST.__objc_arraydata: 0x2f0
-  __DATA_CONST.__got: 0xba8
-  __AUTH_CONST.__const: 0x57b8
-  __AUTH_CONST.__cfstring: 0x7d60
-  __AUTH_CONST.__objc_const: 0x60d8
+  __DATA_CONST.__got: 0xbf0
+  __AUTH_CONST.__const: 0x5988
+  __AUTH_CONST.__cfstring: 0x80a0
+  __AUTH_CONST.__objc_const: 0x64e8
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x360
   __AUTH_CONST.__objc_intobj: 0x210
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x1050
+  __AUTH_CONST.__auth_got: 0x1068
   __AUTH_CONST.__auth_ptr: 0x0
-  __AUTH.__objc_data: 0x190
-  __DATA.__objc_ivar: 0x520
-  __DATA.__data: 0x3f8
-  __DATA.__bss: 0x1c0
+  __AUTH.__objc_data: 0x2d0
+  __DATA.__objc_ivar: 0x54c
+  __DATA.__data: 0x3f0
+  __DATA.__bss: 0x1f0
   __DATA.__common: 0x4
   __DATA_DIRTY.__objc_data: 0xfa0
-  __DATA_DIRTY.__data: 0x158
-  __DATA_DIRTY.__bss: 0x5b8
+  __DATA_DIRTY.__data: 0x160
+  __DATA_DIRTY.__bss: 0x600
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/Contacts.framework/Versions/A/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  Functions: 3390
-  Symbols:   6868
-  CStrings:  2572
+  Functions: 3476
+  Symbols:   7072
+  CStrings:  2640
 
Symbols:
+ +[CSAccessMetricsRegistry sharedRegistry]
+ +[CSAccessMetricsReporter reportAccessForClient:target:kind:]
+ -[CSAccessMetricsRegistry .cxx_destruct]
+ -[CSAccessMetricsRegistry claimFirstSightOfClient:target:kind:]
+ -[CSAccessMetricsRegistry init]
+ -[CSAccessTuple .cxx_destruct]
+ -[CSAccessTuple hash]
+ -[CSAccessTuple initWithClient:target:kind:]
+ -[CSAccessTuple isEqual:]
+ -[CSBundleFilterEscalatedIdentifiers .cxx_destruct]
+ -[CSBundleFilterEscalatedIdentifiers excludedAppBundleIdentifiers]
+ -[CSBundleFilterEscalatedIdentifiers fileProviderExcludedBundleIDs]
+ -[CSBundleFilterEscalatedIdentifiers hiddenAppBundleIdentifiers]
+ -[CSBundleFilterEscalatedIdentifiers initWithLockedAppBundleIdentifiers:hiddenAppBundleIdentifiers:mdmRestrictedBundleIdentifiers:excludedAppBundleIdentifiers:fileProviderExcludedBundleIDs:]
+ -[CSBundleFilterEscalatedIdentifiers lockedAppBundleIdentifiers]
+ -[CSBundleFilterEscalatedIdentifiers mdmRestrictedBundleIdentifiers]
+ -[MDSearchableIndexService _decodeAttributeBackfillResultForGroup:plistBytes:]
+ -[MDSearchableIndexService _decodeBundleFilterEvaluationRequest:error:]
+ -[MDSearchableIndexService _evaluateFileProviderContainerGroups:excludedBundleIDs:completionHandler:]
+ -[MDSearchableIndexService _mergeFileProviderExcludedBundleIDsForRequest:lockedAppBundleIdentifiers:hiddenAppBundleIdentifiers:excludedAppBundleIdentifiers:]
+ -[MDSearchableIndexService _processIndexDataForBundle:protectionClass:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:donationTimestamp:donationXPCTraceID:deletes:completionHandler:]
+ -[MDSearchableIndexService _rejectIfDisallowedBundleID:]
+ -[MDSearchableIndexService _rejectIfNotInternal:reason:]
+ -[MDSearchableIndexService _resolveAttributeBackfillResultsForGroups:completionHandler:]
+ -[MDSearchableIndexService _resolveEscalatedIdentifiersForRequest:]
+ -[MDSearchableIndexService _resolveExcludedAppBundleIdentifiers]
+ -[MDSearchableIndexService _resolveFileProviderAndAttributeBackfillForRequest:escalated:completionHandler:]
+ -[MDSearchableIndexService _resolveHiddenAppBundleIdentifiers]
+ -[MDSearchableIndexService _resolveLockedAppBundleIdentifiers]
+ -[MDSearchableIndexService _resolveMDMRestrictedBundleIdentifiers]
+ -[MDSearchableIndexService _sendBundleFilterEvaluationReply:overConnection:indexID:evaluationReply:attributeBackfillResults:evaluationError:escalated:]
+ -[MDSearchableIndexService _validateAttributeBackfillGroup:]
+ -[MDSearchableIndexService _validateAttributeBackfillGroupsInRequest:]
+ -[MDSearchableIndexService _validateBundleFilterEvaluationRequest:]
+ -[MDSearchableIndexService _validateFileProviderContainerGroup:]
+ -[MDSearchableIndexService _validateFileProviderContainerGroupsInRequest:]
+ -[MDSearchableIndexService evaluateFilters:]
+ -[SPConcreteCoreSpotlightIndexer deferFixupWhileSuspended:]
+ -[SPConcreteCoreSpotlightIndexer indexFromBundle:fromClient:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:donationTimestamp:donationXPCTraceID:deletes:canCreateNewIndex:completionHandler:]
+ -[SPCoreSpotlightIndexer indexFromBundle:fromClient:protectionClass:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:donationTimestamp:donationXPCTraceID:deletes:canCreateNewIndex:completionHandler:]
+ -[SPCoreSpotlightTask _knownDisabledBundleIDsFromBundleIDs:excludingFPBundleIDs:]
+ -[SPCoreSpotlightTask _makeNotificationSourcesQueryStringWithBundleIDs:]
+ -[SPCoreSpotlightTask _makePrefsQueryStringWithPrefsDisabledBundles:]
+ CSAccessMetricsSendQueue.onceToken
+ CSAccessMetricsSendQueue.queue
+ GCC_except_table1001
+ GCC_except_table102
+ GCC_except_table1024
+ GCC_except_table105
+ GCC_except_table1053
+ GCC_except_table1054
+ GCC_except_table106
+ GCC_except_table1079
+ GCC_except_table1124
+ GCC_except_table1129
+ GCC_except_table119
+ GCC_except_table1193
+ GCC_except_table122
+ GCC_except_table1240
+ GCC_except_table1241
+ GCC_except_table1247
+ GCC_except_table1249
+ GCC_except_table1259
+ GCC_except_table1261
+ GCC_except_table1279
+ GCC_except_table1285
+ GCC_except_table1289
+ GCC_except_table1304
+ GCC_except_table1320
+ GCC_except_table1327
+ GCC_except_table1334
+ GCC_except_table1341
+ GCC_except_table1348
+ GCC_except_table1366
+ GCC_except_table144
+ GCC_except_table1441
+ GCC_except_table1442
+ GCC_except_table1444
+ GCC_except_table145
+ GCC_except_table1451
+ GCC_except_table146
+ GCC_except_table148
+ GCC_except_table1511
+ GCC_except_table1518
+ GCC_except_table167
+ GCC_except_table168
+ GCC_except_table190
+ GCC_except_table202
+ GCC_except_table203
+ GCC_except_table204
+ GCC_except_table205
+ GCC_except_table206
+ GCC_except_table207
+ GCC_except_table208
+ GCC_except_table21
+ GCC_except_table212
+ GCC_except_table213
+ GCC_except_table214
+ GCC_except_table215
+ GCC_except_table216
+ GCC_except_table217
+ GCC_except_table218
+ GCC_except_table219
+ GCC_except_table220
+ GCC_except_table221
+ GCC_except_table222
+ GCC_except_table223
+ GCC_except_table224
+ GCC_except_table225
+ GCC_except_table226
+ GCC_except_table227
+ GCC_except_table228
+ GCC_except_table229
+ GCC_except_table230
+ GCC_except_table235
+ GCC_except_table249
+ GCC_except_table256
+ GCC_except_table259
+ GCC_except_table267
+ GCC_except_table269
+ GCC_except_table281
+ GCC_except_table285
+ GCC_except_table289
+ GCC_except_table292
+ GCC_except_table298
+ GCC_except_table308
+ GCC_except_table311
+ GCC_except_table337
+ GCC_except_table340
+ GCC_except_table342
+ GCC_except_table344
+ GCC_except_table368
+ GCC_except_table376
+ GCC_except_table382
+ GCC_except_table388
+ GCC_except_table416
+ GCC_except_table426
+ GCC_except_table441
+ GCC_except_table476
+ GCC_except_table477
+ GCC_except_table481
+ GCC_except_table49
+ GCC_except_table507
+ GCC_except_table53
+ GCC_except_table536
+ GCC_except_table55
+ GCC_except_table557
+ GCC_except_table558
+ GCC_except_table586
+ GCC_except_table613
+ GCC_except_table626
+ GCC_except_table629
+ GCC_except_table65
+ GCC_except_table66
+ GCC_except_table682
+ GCC_except_table708
+ GCC_except_table73
+ GCC_except_table738
+ GCC_except_table759
+ GCC_except_table760
+ GCC_except_table77
+ GCC_except_table772
+ GCC_except_table801
+ GCC_except_table82
+ GCC_except_table827
+ GCC_except_table828
+ GCC_except_table829
+ GCC_except_table83
+ GCC_except_table855
+ GCC_except_table87
+ GCC_except_table921
+ GCC_except_table942
+ GCC_except_table964
+ GCC_except_table968
+ GCC_except_table972
+ GCC_except_table98
+ OBJC_IVAR_$_CSAccessMetricsRegistry._lock
+ OBJC_IVAR_$_CSAccessMetricsRegistry._seen
+ OBJC_IVAR_$_CSAccessTuple._client
+ OBJC_IVAR_$_CSAccessTuple._hash
+ OBJC_IVAR_$_CSAccessTuple._kind
+ OBJC_IVAR_$_CSAccessTuple._target
+ OBJC_IVAR_$_CSBundleFilterEscalatedIdentifiers._excludedAppBundleIdentifiers
+ OBJC_IVAR_$_CSBundleFilterEscalatedIdentifiers._fileProviderExcludedBundleIDs
+ OBJC_IVAR_$_CSBundleFilterEscalatedIdentifiers._hiddenAppBundleIdentifiers
+ OBJC_IVAR_$_CSBundleFilterEscalatedIdentifiers._lockedAppBundleIdentifiers
+ OBJC_IVAR_$_CSBundleFilterEscalatedIdentifiers._mdmRestrictedBundleIdentifiers
+ SPBundleFilterAllowedAttributeBackfillAttributeNames.onceToken
+ SPBundleFilterAllowedAttributeBackfillAttributeNames.sAllowed
+ _CSAccessMetricsReportQuery
+ _CSShouldTraceMessagesDonation
+ _MDItemEventSourceBundleIdentifier
+ _MDItemRelatedAppBundleIdentifier
+ _OBJC_CLASS_$_CSAccessMetricsRegistry
+ _OBJC_CLASS_$_CSAccessMetricsReporter
+ _OBJC_CLASS_$_CSAccessTuple
+ _OBJC_CLASS_$_CSBundleFilterAttributeBackfillResult
+ _OBJC_CLASS_$_CSBundleFilterEscalatedIdentifiers
+ _OBJC_CLASS_$_CSBundleFilterEvaluationReply
+ _OBJC_CLASS_$_CSBundleFilterEvaluationRequest
+ _OBJC_METACLASS_$_CSAccessMetricsRegistry
+ _OBJC_METACLASS_$_CSAccessMetricsReporter
+ _OBJC_METACLASS_$_CSAccessTuple
+ _OBJC_METACLASS_$_CSBundleFilterEscalatedIdentifiers
+ __107-[MDSearchableIndexService _resolveFileProviderAndAttributeBackfillForRequest:escalated:completionHandler:]_block_invoke
+ __234-[SPConcreteCoreSpotlightIndexer indexFromBundle:fromClient:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:donationTimestamp:donationXPCTraceID:deletes:canCreateNewIndex:completionHandler:]_block_invoke
+ __234-[SPConcreteCoreSpotlightIndexer indexFromBundle:fromClient:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:donationTimestamp:donationXPCTraceID:deletes:canCreateNewIndex:completionHandler:]_block_invoke_2
+ __242-[SPCoreSpotlightIndexer indexFromBundle:fromClient:protectionClass:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:donationTimestamp:donationXPCTraceID:deletes:canCreateNewIndex:completionHandler:]_block_invoke
+ __242-[SPCoreSpotlightIndexer indexFromBundle:fromClient:protectionClass:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:donationTimestamp:donationXPCTraceID:deletes:canCreateNewIndex:completionHandler:]_block_invoke_2
+ __88-[MDSearchableIndexService _resolveAttributeBackfillResultsForGroups:completionHandler:]_block_invoke
+ __OBJC_$_CLASS_METHODS_CSAccessMetricsRegistry
+ __OBJC_$_CLASS_METHODS_CSAccessMetricsReporter
+ __OBJC_$_INSTANCE_METHODS_CSAccessMetricsRegistry
+ __OBJC_$_INSTANCE_METHODS_CSAccessTuple
+ __OBJC_$_INSTANCE_METHODS_CSBundleFilterEscalatedIdentifiers
+ __OBJC_$_INSTANCE_VARIABLES_CSAccessMetricsRegistry
+ __OBJC_$_INSTANCE_VARIABLES_CSAccessTuple
+ __OBJC_$_INSTANCE_VARIABLES_CSBundleFilterEscalatedIdentifiers
+ __OBJC_$_PROP_LIST_CSBundleFilterEscalatedIdentifiers
+ __OBJC_CLASS_RO_$_CSAccessMetricsRegistry
+ __OBJC_CLASS_RO_$_CSAccessMetricsReporter
+ __OBJC_CLASS_RO_$_CSAccessTuple
+ __OBJC_CLASS_RO_$_CSBundleFilterEscalatedIdentifiers
+ __OBJC_METACLASS_RO_$_CSAccessMetricsRegistry
+ __OBJC_METACLASS_RO_$_CSAccessMetricsReporter
+ __OBJC_METACLASS_RO_$_CSAccessTuple
+ __OBJC_METACLASS_RO_$_CSBundleFilterEscalatedIdentifiers
+ __SDEventMonitorSetUserInfoError
+ ___101-[MDSearchableIndexService _evaluateFileProviderContainerGroups:excludedBundleIDs:completionHandler:]_block_invoke
+ ___107-[MDSearchableIndexService _resolveFileProviderAndAttributeBackfillForRequest:escalated:completionHandler:]_block_invoke
+ ___234-[SPConcreteCoreSpotlightIndexer indexFromBundle:fromClient:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:donationTimestamp:donationXPCTraceID:deletes:canCreateNewIndex:completionHandler:]_block_invoke
+ ___234-[SPConcreteCoreSpotlightIndexer indexFromBundle:fromClient:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:donationTimestamp:donationXPCTraceID:deletes:canCreateNewIndex:completionHandler:]_block_invoke_2
+ ___234-[SPConcreteCoreSpotlightIndexer indexFromBundle:fromClient:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:donationTimestamp:donationXPCTraceID:deletes:canCreateNewIndex:completionHandler:]_block_invoke_3
+ ___242-[SPCoreSpotlightIndexer indexFromBundle:fromClient:protectionClass:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:donationTimestamp:donationXPCTraceID:deletes:canCreateNewIndex:completionHandler:]_block_invoke
+ ___242-[SPCoreSpotlightIndexer indexFromBundle:fromClient:protectionClass:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:donationTimestamp:donationXPCTraceID:deletes:canCreateNewIndex:completionHandler:]_block_invoke_2
+ ___41+[CSAccessMetricsRegistry sharedRegistry]_block_invoke
+ ___44-[MDSearchableIndexService evaluateFilters:]_block_invoke
+ ___88-[MDSearchableIndexService _resolveAttributeBackfillResultsForGroups:completionHandler:]_block_invoke
+ ___CSAccessMetricsSendQueue_block_invoke
+ ___CSAccessMetricsSend_block_invoke
+ ___CSAccessMetricsSend_block_invoke_2
+ ___MDQueryCreateStringByAddingBackslashEscapes
+ ___SPBundleFilterAllowedAttributeBackfillAttributeNames_block_invoke
+ ____bgst_queue_block_invoke
+ ___bgst_complete_task_block_invoke
+ ___bgst_expire_task_block_invoke
+ ___bgst_register_task_block_invoke
+ ___block_descriptor_112_e8_32s40s48s56s_e63_v32?0"CSBundleFilterEvaluationReply"8"NSArray"16"NSError"24l
+ ___block_descriptor_160_e8_32s40s48s56s64s72s80r88r96r104r112r120w_e69_v48?0"SPQueryJob"8q16Q24^{__MDStoreOIDArray=}32^{__MDPlistBytes=}40l
+ ___block_descriptor_162_e8_32s40s48s56s64s72s80s88s96s104s112s120bs_e5_v8?0l
+ ___block_descriptor_168_e8_32s40s48s56s64s72s80s88s96s104s112s120r128r136r_e40_v16?0"SPConcreteCoreSpotlightIndexer"8l
+ ___block_descriptor_202_e8_32s40s48s56s64s72s80s88s96s104s112s120s128s136bs144w_e18_v20?0^{__SI=}8C16l
+ ___block_descriptor_48_e8_32s40r_e17_v16?0"NSArray"8l
+ ___block_descriptor_48_e8_32s40s_e25_v16?0"OSLogEventProxy"8l
+ ___block_descriptor_48_e8_32s40s_e37_v24?0Q8"OSLogEventStreamPosition"16l
+ ___block_descriptor_56_e8_32s40r48r_e51_v24?0"CSBundleFilterEvaluationReply"8"NSError"16l
+ ___block_descriptor_64_e8_32s40s48r_e5_v8?0l
+ ___block_descriptor_73_e8_32s40s48s56r64r_e5_v8?0l
+ ___block_descriptor_80_e8_32s40s48s56s64r72r_e20_v24?08"NSError"16l
+ ___copy_helper_block_e8_32s40s48s56s64s72s80r88r96r104r112r120w
+ ___destroy_helper_block_e8_32s40s48s56s64s72s80r88r96r104r112r120w
+ ___isWellFormedBundleID_block_invoke
+ ___logForCSLogCategoryDonationTracing_block_invoke
+ ___syslogCollectSlice_block_invoke
+ ___syslogMakeStream_block_invoke
+ __bgst_expire_task_block_invoke
+ __bgst_queue
+ __bgst_register_task_block_invoke
+ __syslogCollectSlice_block_invoke
+ _bgst_complete_task
+ _bgst_expire_task
+ _bgst_queue
+ _bgst_queue.onceToken
+ _bgst_queue.queue
+ _bgst_register_task
+ _bundleIDsPassingGrammar
+ _isWellFormedBundleID
+ _kSyslogSliceDurations
+ _logForCSLogCategoryDonationTracing
+ _objc_msgSend$_decodeAttributeBackfillResultForGroup:plistBytes:
+ _objc_msgSend$_decodeBundleFilterEvaluationRequest:error:
+ _objc_msgSend$_evaluateFileProviderContainerGroups:excludedBundleIDs:completionHandler:
+ _objc_msgSend$_knownDisabledBundleIDsFromBundleIDs:excludingFPBundleIDs:
+ _objc_msgSend$_makeNotificationSourcesQueryStringWithBundleIDs:
+ _objc_msgSend$_mergeFileProviderExcludedBundleIDsForRequest:lockedAppBundleIdentifiers:hiddenAppBundleIdentifiers:excludedAppBundleIdentifiers:
+ _objc_msgSend$_processIndexDataForBundle:protectionClass:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:donationTimestamp:donationXPCTraceID:deletes:completionHandler:
+ _objc_msgSend$_rejectIfDisallowedBundleID:
+ _objc_msgSend$_rejectIfNotInternal:reason:
+ _objc_msgSend$_resolveAttributeBackfillResultsForGroups:completionHandler:
+ _objc_msgSend$_resolveEscalatedIdentifiersForRequest:
+ _objc_msgSend$_resolveExcludedAppBundleIdentifiers
+ _objc_msgSend$_resolveFileProviderAndAttributeBackfillForRequest:escalated:completionHandler:
+ _objc_msgSend$_resolveHiddenAppBundleIdentifiers
+ _objc_msgSend$_resolveLockedAppBundleIdentifiers
+ _objc_msgSend$_resolveMDMRestrictedBundleIdentifiers
+ _objc_msgSend$_sendBundleFilterEvaluationReply:overConnection:indexID:evaluationReply:attributeBackfillResults:evaluationError:escalated:
+ _objc_msgSend$_validateAttributeBackfillGroup:
+ _objc_msgSend$_validateAttributeBackfillGroupsInRequest:
+ _objc_msgSend$_validateBundleFilterEvaluationRequest:
+ _objc_msgSend$_validateFileProviderContainerGroup:
+ _objc_msgSend$_validateFileProviderContainerGroupsInRequest:
+ _objc_msgSend$abandoned
+ _objc_msgSend$allDisabledBundlesSet
+ _objc_msgSend$attributeBackfillGroups
+ _objc_msgSend$attributeName
+ _objc_msgSend$claimFirstSightOfClient:target:kind:
+ _objc_msgSend$deferFixupWhileSuspended:
+ _objc_msgSend$evaluateFilters:
+ _objc_msgSend$excludedAppBundleIdentifiers
+ _objc_msgSend$federationDisabledBundles
+ _objc_msgSend$fileProviderContainerGroups
+ _objc_msgSend$fileProviderExcludedBundleIDs
+ _objc_msgSend$fileProviderMatchedIdentifiers
+ _objc_msgSend$fileProviderUnresolvedIdentifiers
+ _objc_msgSend$hiddenAppBundleIdentifiers
+ _objc_msgSend$identifiers
+ _objc_msgSend$indexFromBundle:fromClient:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:donationTimestamp:donationXPCTraceID:deletes:canCreateNewIndex:completionHandler:
+ _objc_msgSend$indexFromBundle:fromClient:protectionClass:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:donationTimestamp:donationXPCTraceID:deletes:canCreateNewIndex:completionHandler:
+ _objc_msgSend$initWithBundleID:resolvedValues:confirmedAbsentIdentifiers:
+ _objc_msgSend$initWithClient:target:kind:
+ _objc_msgSend$initWithFileProviderMatchedIdentifiers:fileProviderUnresolvedIdentifiers:lockedAppBundleIdentifiers:hiddenAppBundleIdentifiers:mdmRestrictedBundleIdentifiers:excludedAppBundleIdentifiers:attributeBackfillResults:
+ _objc_msgSend$initWithLockedAppBundleIdentifiers:hiddenAppBundleIdentifiers:mdmRestrictedBundleIdentifiers:excludedAppBundleIdentifiers:fileProviderExcludedBundleIDs:
+ _objc_msgSend$knownOIDPaths
+ _objc_msgSend$lockedAppBundleIdentifiers
+ _objc_msgSend$lossCount
+ _objc_msgSend$lossEndUnixDate
+ _objc_msgSend$lossStartUnixDate
+ _objc_msgSend$mdmRestrictedBundleIdentifiers
+ _objc_msgSend$needsAppProtectionBundleIDs
+ _objc_msgSend$needsExcludedAppBundleIDs
+ _objc_msgSend$needsMDMRestrictedBundleIDs
+ _objc_msgSend$numberWithUnsignedChar:
+ _objc_msgSend$predicateFrameworkGenerated
+ _objc_msgSend$predicateSearchToolGenerated
+ _objc_msgSend$reportAccessForClient:target:kind:
+ _objc_msgSend$setAdditionalBundleIDs:
+ _objc_msgSend$setAdditionalQueries:
+ _objc_msgSend$setInstantAnswersBundleIDs:
+ _objc_msgSend$setInstantAnswersQueries:
+ _objc_msgSend$setPrefsDisabledBundles:
+ _objc_msgSend$setTarget:
+ _objc_msgSend$sharedRegistry
+ _objc_msgSend$unixDate
+ _stringQueryTemplatesOnly
+ _syslogDateString
+ _syslogEventTimestamp
+ _syslogFileGeneration
+ _syslogLocalTimeString
+ _syslogLossMarker
+ _syslogRotateGenerations
+ _syslogSliceStamp
+ _syslogWriteHeader
+ _syslogWriteLine
+ _syslogWriteTrailer
+ _xpc_data_get_bytes_ptr
+ _xpc_data_get_length
+ isWellFormedBundleID
+ isWellFormedBundleID.allowed
+ isWellFormedBundleID.once
+ kSPUserActivityPurgeTargets_block_invoke_9.registered
+ logForCSLogCategoryDonationTracing
+ logForCSLogCategoryDonationTracing.onceToken
+ logForCSLogCategoryDonationTracing.sDonationTracingLog
+ sharedRegistry.onceToken
+ sharedRegistry.sharedInstance
+ syslogWriteLine
- -[MDSearchableIndexService _processIndexDataForBundle:protectionClass:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:donationTimestamp:deletes:completionHandler:]
- -[SPConcreteCoreSpotlightIndexer indexFromBundle:fromClient:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:donationTimestamp:deletes:canCreateNewIndex:completionHandler:]
- -[SPCoreSpotlightIndexer indexFromBundle:fromClient:protectionClass:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:donationTimestamp:deletes:canCreateNewIndex:completionHandler:]
- -[SPCoreSpotlightTask _makePrefsQueryStringWithBundleIDs:prefsDisabledBundles:]
- GCC_except_table1007
- GCC_except_table1036
- GCC_except_table1037
- GCC_except_table104
- GCC_except_table1046
- GCC_except_table1062
- GCC_except_table110
- GCC_except_table1111
- GCC_except_table1116
- GCC_except_table112
- GCC_except_table1180
- GCC_except_table120
- GCC_except_table1221
- GCC_except_table1227
- GCC_except_table1228
- GCC_except_table123
- GCC_except_table1235
- GCC_except_table1236
- GCC_except_table1246
- GCC_except_table1266
- GCC_except_table1272
- GCC_except_table1276
- GCC_except_table129
- GCC_except_table1291
- GCC_except_table1307
- GCC_except_table131
- GCC_except_table1314
- GCC_except_table132
- GCC_except_table1321
- GCC_except_table1328
- GCC_except_table1335
- GCC_except_table1353
- GCC_except_table140
- GCC_except_table141
- GCC_except_table142
- GCC_except_table1428
- GCC_except_table1429
- GCC_except_table1431
- GCC_except_table1438
- GCC_except_table1498
- GCC_except_table1505
- GCC_except_table153
- GCC_except_table155
- GCC_except_table158
- GCC_except_table159
- GCC_except_table169
- GCC_except_table170
- GCC_except_table171
- GCC_except_table172
- GCC_except_table173
- GCC_except_table174
- GCC_except_table175
- GCC_except_table176
- GCC_except_table177
- GCC_except_table178
- GCC_except_table179
- GCC_except_table180
- GCC_except_table181
- GCC_except_table182
- GCC_except_table183
- GCC_except_table184
- GCC_except_table187
- GCC_except_table188
- GCC_except_table189
- GCC_except_table193
- GCC_except_table248
- GCC_except_table255
- GCC_except_table257
- GCC_except_table266
- GCC_except_table268
- GCC_except_table279
- GCC_except_table284
- GCC_except_table287
- GCC_except_table291
- GCC_except_table296
- GCC_except_table307
- GCC_except_table309
- GCC_except_table336
- GCC_except_table339
- GCC_except_table341
- GCC_except_table343
- GCC_except_table357
- GCC_except_table365
- GCC_except_table371
- GCC_except_table377
- GCC_except_table405
- GCC_except_table415
- GCC_except_table430
- GCC_except_table465
- GCC_except_table466
- GCC_except_table47
- GCC_except_table470
- GCC_except_table496
- GCC_except_table50
- GCC_except_table52
- GCC_except_table525
- GCC_except_table546
- GCC_except_table547
- GCC_except_table57
- GCC_except_table575
- GCC_except_table602
- GCC_except_table615
- GCC_except_table618
- GCC_except_table62
- GCC_except_table671
- GCC_except_table685
- GCC_except_table70
- GCC_except_table71
- GCC_except_table722
- GCC_except_table728
- GCC_except_table743
- GCC_except_table75
- GCC_except_table756
- GCC_except_table78
- GCC_except_table785
- GCC_except_table80
- GCC_except_table811
- GCC_except_table812
- GCC_except_table813
- GCC_except_table839
- GCC_except_table85
- GCC_except_table905
- GCC_except_table91
- GCC_except_table926
- GCC_except_table947
- GCC_except_table951
- GCC_except_table955
- GCC_except_table96
- GCC_except_table97
- GCC_except_table984
- _OUTLINED_FUNCTION_45
- __215-[SPConcreteCoreSpotlightIndexer indexFromBundle:fromClient:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:donationTimestamp:deletes:canCreateNewIndex:completionHandler:]_block_invoke
- __215-[SPConcreteCoreSpotlightIndexer indexFromBundle:fromClient:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:donationTimestamp:deletes:canCreateNewIndex:completionHandler:]_block_invoke_2
- __223-[SPCoreSpotlightIndexer indexFromBundle:fromClient:protectionClass:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:donationTimestamp:deletes:canCreateNewIndex:completionHandler:]_block_invoke
- __223-[SPCoreSpotlightIndexer indexFromBundle:fromClient:protectionClass:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:donationTimestamp:deletes:canCreateNewIndex:completionHandler:]_block_invoke_2
- __67-[SPCoreSpotlightIndexer registerPostJournalPlaybackBGSTActivities]_block_invoke_3
- __67-[SPCoreSpotlightIndexer registerPostJournalPlaybackBGSTActivities]_block_invoke_4
- __SDEventMonitorErrorMake
- ___215-[SPConcreteCoreSpotlightIndexer indexFromBundle:fromClient:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:donationTimestamp:deletes:canCreateNewIndex:completionHandler:]_block_invoke
- ___215-[SPConcreteCoreSpotlightIndexer indexFromBundle:fromClient:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:donationTimestamp:deletes:canCreateNewIndex:completionHandler:]_block_invoke_2
- ___215-[SPConcreteCoreSpotlightIndexer indexFromBundle:fromClient:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:donationTimestamp:deletes:canCreateNewIndex:completionHandler:]_block_invoke_3
- ___223-[SPCoreSpotlightIndexer indexFromBundle:fromClient:protectionClass:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:donationTimestamp:deletes:canCreateNewIndex:completionHandler:]_block_invoke
- ___223-[SPCoreSpotlightIndexer indexFromBundle:fromClient:protectionClass:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:donationTimestamp:deletes:canCreateNewIndex:completionHandler:]_block_invoke_2
- ___block_descriptor_152_e8_32s40s48s56s64s72r80r88r96r104r112w_e69_v48?0"SPQueryJob"8q16Q24^{__MDStoreOIDArray=}32^{__MDPlistBytes=}40l
- ___block_descriptor_154_e8_32s40s48s56s64s72s80s88s96s104s112s120bs_e5_v8?0l
- ___block_descriptor_160_e8_32s40s48s56s64s72s80s88s96s104s112s120r128r136r_e40_v16?0"SPConcreteCoreSpotlightIndexer"8l
- ___block_descriptor_194_e8_32s40s48s56s64s72s80s88s96s104s112s120s128s136bs144w_e18_v20?0^{__SI=}8C16l
- ___block_descriptor_40_e8_32s_e25_v16?0"OSLogEventProxy"8l
- ___block_descriptor_40_e8_32s_e37_v24?0Q8"OSLogEventStreamPosition"16l
- ___block_descriptor_72_e8_32s40s48s56r64r_e5_v8?0l
- ___copy_helper_block_e8_32s40s48s56s64s72r80r88r96r104r112w
- ___destroy_helper_block_e8_32s40s48s56s64s72r80r88r96r104r112w
- _objc_msgSend$_makePrefsQueryStringWithBundleIDs:prefsDisabledBundles:
- _objc_msgSend$_processIndexDataForBundle:protectionClass:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:donationTimestamp:deletes:completionHandler:
- _objc_msgSend$dateByAddingTimeInterval:
- _objc_msgSend$indexFromBundle:fromClient:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:donationTimestamp:deletes:canCreateNewIndex:completionHandler:
- _objc_msgSend$indexFromBundle:fromClient:protectionClass:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:donationTimestamp:deletes:canCreateNewIndex:completionHandler:
- _objc_msgSend$truncateAtOffset:error:
CStrings:
+ " && _kMDItemBundleID!=\"com.apple.people.screenTimeRequest\""
+ "### BEGIN slice=[%@, %@]\n"
+ "### END status=%s events=%llu lossEvents=%llu lossMessages=%llu%s writeFailures=%llu\n"
+ "### LOG LOSS: %u%s message(s) dropped between %@ and %@\n"
+ "###collectSpotlightLogs Deadline reached after %zu of %zu slices"
+ "###collectSpotlightLogs Failed to create stream for slice"
+ "###collectSpotlightLogs Getting spotlight oslog past 60 mins in %zu slices, newest first"
+ "###collectSpotlightLogs Timeout draining oslog handlers"
+ "###collectSpotlightLogs Write failed, log will be short: %@"
+ "#apphistory dropping action for %@: attribute set encoding was abandoned"
+ "%@ == \"%@\""
+ "%@.%06d%c%02ld%02ld"
+ "%Y%m%dT%H%M%S%z"
+ "%Y-%m-%d %H:%M:%S"
+ "%Y-%m-%d %H:%M:%S%z"
+ "%ld%@"
+ "%llu"
+ "(!((%@) || (%@) || (%@) || (%@) || ((%@)%@)))"
+ "((%@) && (%@ == \"%@\") && (%@))"
+ "(_kMDItemBundleID = \"com.apple.usernotificationsd\" && %@)"
+ "(all)"
+ "(process contains 'corespotlightd') OR (process contains 'spotlightknowledged') OR sender = 'CoreSpotlight'"
+ "+"
+ "+ (counter saturated)"
+ "-[MDSearchableIndexService evaluateFilters:]"
+ "-[SPConcreteCoreSpotlightIndexer indexFromBundle:fromClient:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:donationTimestamp:donationXPCTraceID:deletes:canCreateNewIndex:completionHandler:]_block_invoke"
+ ".1.%@.log"
+ "3rd party"
+ "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-."
+ "Access"
+ "AppProtection bundle IDs"
+ "Attempt to access Mail by client %@"
+ "BGST activity:%@ already registered, launch handler unchanged"
+ "BGST activity:%@ rejected, never registered in this process"
+ "Client %@ passed a non-string %@ entry; dropping it"
+ "Client %@ passed malformed %@ entry (%@); dropping it"
+ "Client %@ trying to search additional bundle (%@) without having entitlement %@"
+ "Client %@ trying to use instant answers without being an allowed client"
+ "ClientBundleID"
+ "DaemonName"
+ "Deferring %s while the index is suspended. dataclass:%@, suspended:%d, suspending:%d"
+ "Donation dispatched to concrete indexer, donationXPCTraceID=%llu bundleID=%@ dataclass=%@ itemsBytes=%lu deletesBytes=%lu"
+ "DonationTracing"
+ "Excluded Apps bundle IDs"
+ "Failed to deserialize user info property list, class:%@, error:%@"
+ "Failed to expire BGST activity:%@, completing instead, error:%@"
+ "IsCrossBundle"
+ "MDM-restricted bundle IDs"
+ "Non-internal client %@ requested %s"
+ "Received \"%s\" notification with no event name"
+ "Registered BGST activity:%@"
+ "TRUNCATED-deadline"
+ "TRUNCATED-no-stream"
+ "TRUNCATED-undrained"
+ "TargetBundleID"
+ "additionalBundleIDs"
+ "additionalQueries"
+ "attribute backfill"
+ "com.apple.corespotlight.syslog-collect"
+ "com.apple.distnoted.matching.trusted"
+ "com.apple.searchd.bgst"
+ "com.apple.spotlight.CSAccessMetrics.send"
+ "com.apple.spotlight.index.BundleAccess"
+ "complete"
+ "cross-bundle exclusion match"
+ "disableBundles"
+ "donation-xpc-trace-id"
+ "evaluate-filters-data"
+ "evaluate-filters-data-size"
+ "evaluate_filters"
+ "failed to encode bundle filter evaluation reply %@"
+ "fetchAttributes has no index for protectionClass:%@, bundleID:%@"
+ "instantAnswersBundleIDs"
+ "instantAnswersQueries"
+ "invalid"
+ "issueDocIDConsistencyCheck"
+ "kMDItemCreator"
+ "prefsDisabledBundles"
+ "runUserActivityPurgeFixup"
+ "stream-error"
+ "v24@?0@\"CSBundleFilterEvaluationReply\"8@\"NSError\"16"
+ "v32@?0@\"CSBundleFilterEvaluationReply\"8@\"NSArray\"16@\"NSError\"24"
- "###collectSpotlightLogs  Writing to file: %s"
- "###collectSpotlightLogs Failed to truncate file: %s"
- "###collectSpotlightLogs Getting spotlight oslog past 60 mins"
- "###collectSpotlightLogs Timeout on getting oslog stream"
- "(!((%@) || (%@) || (%@) || ((%@) && _kMDItemBundleID!=\"com.apple.people.screenTimeRequest\")))"
- "(%@ == %@)"
- "(process contains 'corespotlightd') OR (process contains 'mds') OR process = 'mdbulkimport' OR process = 'mdworker_shared' OR (process contains 'spotlightknowledged') OR sender = 'CoreSpotlight'"
- "-[SPConcreteCoreSpotlightIndexer indexFromBundle:fromClient:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:donationTimestamp:deletes:canCreateNewIndex:completionHandler:]_block_invoke"
- ".%d.log"
- ".1.log"
- "Failed to expire task %@ with error: %@"
- "Failed to expire task with error"
- "Registering BGST activity:%@"
- "Registering BGST repeating task %@"
```
