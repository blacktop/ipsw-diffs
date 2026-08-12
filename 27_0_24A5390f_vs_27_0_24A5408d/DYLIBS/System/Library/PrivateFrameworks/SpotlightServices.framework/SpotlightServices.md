## SpotlightServices

> `/System/Library/PrivateFrameworks/SpotlightServices.framework/SpotlightServices`

```diff

-2454.100.0.0.0
-  __TEXT.__text: 0x15ff68
-  __TEXT.__objc_methlist: 0xe610
-  __TEXT.__const: 0x2e18
-  __TEXT.__cstring: 0x3aa1a
-  __TEXT.__gcc_except_tab: 0x5050
-  __TEXT.__oslogstring: 0xbc3b
+2459.102.0.0.0
+  __TEXT.__text: 0x15f5e4
+  __TEXT.__objc_methlist: 0xe628
+  __TEXT.__const: 0x2df8
+  __TEXT.__cstring: 0x3a8aa
+  __TEXT.__gcc_except_tab: 0x5068
+  __TEXT.__oslogstring: 0xba3b
   __TEXT.__ustring: 0x892
   __TEXT.__dlopen_cstrs: 0x12f
   __TEXT.__swift5_typeref: 0x1e8

   __TEXT.__swift5_proto: 0xc
   __TEXT.__swift5_types: 0x18
   __TEXT.__swift5_capture: 0xa4
-  __TEXT.__unwind_info: 0x31f8
+  __TEXT.__unwind_info: 0x3438
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x10100
+  __DATA_CONST.__const: 0x100d8
   __DATA_CONST.__objc_classlist: 0x5d0
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8d98
+  __DATA_CONST.__objc_selrefs: 0x8da0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x428
-  __DATA_CONST.__objc_arraydata: 0x4770
-  __DATA_CONST.__got: 0x1c40
-  __AUTH_CONST.__const: 0x2b80
-  __AUTH_CONST.__cfstring: 0x36ca0
+  __DATA_CONST.__objc_arraydata: 0x4778
+  __DATA_CONST.__got: 0x1c30
+  __AUTH_CONST.__const: 0x2b20
+  __AUTH_CONST.__cfstring: 0x36be0
   __AUTH_CONST.__objc_const: 0x181c0
-  __AUTH_CONST.__objc_intobj: 0x47a0
+  __AUTH_CONST.__objc_intobj: 0x4788
   __AUTH_CONST.__objc_arrayobj: 0xc90
   __AUTH_CONST.__objc_doubleobj: 0x310
   __AUTH_CONST.__objc_dictobj: 0x258
   __AUTH_CONST.__objc_floatobj: 0x20
-  __AUTH_CONST.__auth_got: 0xf70
+  __AUTH_CONST.__auth_got: 0xf40
   __AUTH.__objc_data: 0x16e8
   __AUTH.__data: 0xc8
   __DATA.__objc_ivar: 0x15b4
   __DATA.__data: 0xe88
-  __DATA.__bss: 0x618
+  __DATA.__bss: 0x5d8
   __DATA.__common: 0x28
   __DATA_DIRTY.__objc_data: 0x2580
   __DATA_DIRTY.__data: 0x308

   - /System/Library/PrivateFrameworks/AeroML.framework/AeroML
   - /System/Library/PrivateFrameworks/AggregateDictionary.framework/AggregateDictionary
   - /System/Library/PrivateFrameworks/AppPredictionClient.framework/AppPredictionClient
-  - /System/Library/PrivateFrameworks/AppProtection.framework/AppProtection
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams

   - /System/Library/PrivateFrameworks/SpotlightLinguistics.framework/SpotlightLinguistics
   - /System/Library/PrivateFrameworks/SpotlightResources.framework/SpotlightResources
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
-  - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities
   - /System/Library/PrivateFrameworks/ToolKit.framework/ToolKit
   - /System/Library/PrivateFrameworks/VoiceShortcutClient.framework/VoiceShortcutClient

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 6458
-  Symbols:   14880
-  CStrings:  7947
+  Functions: 6435
+  Symbols:   14843
+  CStrings:  7928
 
Symbols:
+ -[PRSRankingItem populateOtherFeatures:withEvaluator:currentTime:quParsedEvaluator:queryID:isSearchToolClient:quParsedArgSearchTermsEvaluator:]
+ -[PRSRankingItem(Scoring) topicalityScoreWithEvaluator:quParsedEvaluator:isSearchToolClient:quParsedArgSearchTermsEvaluator:]
+ -[SFSearchResult_SpotlightExtras initWithSearchResult:]
+ -[SPQUParse presentIntentArgTypes]
+ -[SPSearchQueryContext searchToolPredictedAppBundleIDs]
+ -[SPSearchQueryContext setSearchToolPredictedAppBundleIDs:]
+ _OBJC_IVAR_$_SPSearchQueryContext._searchToolPredictedAppBundleIDs
+ _OUTLINED_FUNCTION_23
+ _SPCopyPrefsDisabledApps.onceToken
+ ___SPCopyPrefsDisabledApps_block_invoke
+ _homeCosineForSlot
+ _objc_msgSend$populateOtherFeatures:withEvaluator:currentTime:quParsedEvaluator:queryID:isSearchToolClient:quParsedArgSearchTermsEvaluator:
+ _objc_msgSend$searchToolPredictedAppBundleIDs
+ _objc_msgSend$setSearchToolPredictedAppBundleIDs:
+ _objc_msgSend$setWithCapacity:
+ _objc_msgSend$topicalityScoreWithEvaluator:quParsedEvaluator:isSearchToolClient:quParsedArgSearchTermsEvaluator:
- -[PRSQueryRankingConfiguration isSiriDeserving]
- -[PRSQueryRankingConfiguration setIsSiriDeserving:]
- -[PRSRankingItem populateOtherFeatures:withEvaluator:currentTime:quParsedEvaluator:queryID:isSearchToolClient:quParsedArgSearchTermsEvaluator:isSiriDeserving:]
- -[PRSRankingItem(Scoring) topicalityScoreWithEvaluator:quParsedEvaluator:isSearchToolClient:quParsedArgSearchTermsEvaluator:isSiriDeserving:]
- GCC_except_table32
- GCC_except_table70
- _OBJC_CLASS_$_APApplication
- _OBJC_IVAR_$_PRSQueryRankingConfiguration._isSiriDeserving
- _OUTLINED_FUNCTION_13
- _SSAppExclusionsEnabled
- _SSAppExclusionsEnabled.sEnabled
- _SSAppExclusionsEnabled.sOnce
- _SSCopyTCCDisabledBundlesForSiriAccess
- _SSCopyTCCDisabledBundlesForSiriAccess.tccOnce
- _SSForcedSpotlightMaxChars
- _SSForcedSpotlightMaxWordCount
- _SSInvalidateAppExclusionsDisabledIDsCache
- _SSNumberOfResultsToConsiderForSiriDeserving
- _SSRefreshTCCDisabledBundlesCache
- _SSSantizedBundleIDList
- _SSSiriDeservingEarlyExitTimeout
- _SSSiriDeservingHeuristicDisabled
- _SSSiriDeservingMinChars
- _SSSiriDeservingMinWordCount
- _SSSiriDeservingRegexDisabled
- _SSSiriDeservingScoreThreshold
- _SSSiriDeservingSimulatedDelay
- _SSSubscribeTCCEventsForSiriAccess
- _SSUnsubscribeTCCEventsForSiriAccess
- _TCCAccessCopyBundleIdentifiersDisabledForService
- __SSApply11_2Migration.onceToken
- __SSApply11_2Migration.sResult
- ___SSAppExclusionsEnabled_block_invoke
- ___SSCopyTCCDisabledBundlesForSiriAccess_block_invoke
- ___SSSubscribeTCCEventsForSiriAccess_block_invoke
- ____SSApply11_2Migration_block_invoke
- ___block_descriptor_40_e8_32bs_e50_v24?0Q8"NSObject<OS_tcc_authorization_record>"16ls32l8
- _kTCCServiceSiriAccess
- _objc_msgSend$floatForKey:
- _objc_msgSend$hiddenApplications
- _objc_msgSend$isSiriDeserving
- _objc_msgSend$populateOtherFeatures:withEvaluator:currentTime:quParsedEvaluator:queryID:isSearchToolClient:quParsedArgSearchTermsEvaluator:isSiriDeserving:
- _objc_msgSend$topicalityScoreWithEvaluator:quParsedEvaluator:isSearchToolClient:quParsedArgSearchTermsEvaluator:isSiriDeserving:
- _sDisabledIDsCache
- _sDisabledIDsCacheLock
- _sDisabledIDsCacheValid
- _tccCacheLock
- _tccCachedBundles
- _tcc_events_filter_create_with_criteria
- _tcc_events_subscribe
- _tcc_events_unsubscribe
- _xpc_bool_create
- _xpc_dictionary_create
CStrings:
+ "[HomeDebug] [Consine] rejecting slot %lu: sqDist=%f out of valid [0,4] range (or NaN)"
+ "[bundle=%@][qid=%lu][query=\"%@\"] Home item %@: L1=%.4f embSim=%.4f normSparse=%.4f normDense=%.4f normText=%.4f normMedia=%.4f base=%.4f cam=%.2f room=%.2f home=%.2f temp=%.2f content=%.2f tmBoost=%.2f sdBoost=%.2f L2=%.4f"
+ "_kMDItemBundleID==com.apple.spotlight"
+ "normMedia"
+ "normText"
+ "sparseDenseBoost"
+ "textMediaBoost"
- "AppExclusions"
- "DisabledBundlesFromSiriTCC"
- "Failed to create TCC events filter; disabled bundle cache will not auto-refresh"
- "Failed to get TCC service name; disabled bundle cache will not auto-refresh"
- "IntelligenceFlow"
- "SSSpotlightSiriDeservingHeuristicDisabled"
- "SSSpotlightSiriDeservingRegexDisabled"
- "TCCAccessCopyBundleIdentifiersDisabledForService returned NULL; preserving existing cache"
- "TCCAccessCopyBundleIdentifiersDisabledForService returned invalid type; preserving existing cache"
- "[bundle=%@][qid=%lu][query=\"%@\"] Home item %@: L1=%.4f embSim=%.4f normSparse=%.4f normDense=%.4f base=%.4f cam=%.2f room=%.2f home=%.2f temp=%.2f content=%.2f L2=%.4f"
- "[siri-deserving-diag][qid=%lu] responseHandler ENTERED for PriorityTimeout (localSelf=%s, cancelled=%s)"
- "[siri-deserving-diag][qid=%lu] responseHandler: delegate=%s, about to call gotResponse"
- "com.apple.spotlight.tcc.siri-access"
- "forcedSpotlightMaxChars"
- "forcedSpotlightMaxWordCount"
- "n/a"
- "numberOfResultsToConsiderForSiriDeserving"
- "siri-access TCC event fired"
- "siri-access TCC subscription armed"
- "siriDeservingEarlyExitTimeout"
- "siriDeservingMinChars"
- "siriDeservingMinWordCount"
- "siriDeservingSimulatedDelay"
- "siriDeservingThreshold"
- "spotlight: TCC siri-access disabled bundles refreshed: %{private}@"
- "v24@?0Q8@\"NSObject<OS_tcc_authorization_record>\"16"
```
