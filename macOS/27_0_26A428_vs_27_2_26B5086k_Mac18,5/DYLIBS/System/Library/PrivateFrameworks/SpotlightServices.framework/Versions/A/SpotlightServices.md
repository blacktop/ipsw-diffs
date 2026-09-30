## SpotlightServices

> `/System/Library/PrivateFrameworks/SpotlightServices.framework/Versions/A/SpotlightServices`

```diff

-2459.405.0.0.0
-  __TEXT.__text: 0x17f368
+2465.1.2.0.0
+  __TEXT.__text: 0x180528
   __TEXT.__delay_helper: 0xdc
-  __TEXT.__objc_methlist: 0xfc08
-  __TEXT.__const: 0x2f14
-  __TEXT.__cstring: 0x3c315
-  __TEXT.__oslogstring: 0xb39b
-  __TEXT.__gcc_except_tab: 0x5254
+  __TEXT.__objc_methlist: 0xfc70
+  __TEXT.__const: 0x2f44
+  __TEXT.__cstring: 0x3c415
+  __TEXT.__oslogstring: 0xb57b
+  __TEXT.__gcc_except_tab: 0x52ac
   __TEXT.__ustring: 0x892
   __TEXT.__dlopen_cstrs: 0x12f
   __TEXT.__swift5_typeref: 0x276

   __TEXT.__swift5_types: 0x20
   __TEXT.__swift5_capture: 0xa4
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__unwind_info: 0x4220
+  __TEXT.__unwind_info: 0x4260
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xeaa8
+  __DATA_CONST.__const: 0xeab0
   __DATA_CONST.__objc_classlist: 0x600
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9ba8
+  __DATA_CONST.__objc_selrefs: 0x9bf8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x440
   __DATA_CONST.__objc_arraydata: 0x44e0
-  __DATA_CONST.__got: 0x1cc8
-  __AUTH_CONST.__const: 0x4808
-  __AUTH_CONST.__cfstring: 0x38860
-  __AUTH_CONST.__objc_const: 0x1a4e0
+  __DATA_CONST.__got: 0x1cd0
+  __AUTH_CONST.__const: 0x4878
+  __AUTH_CONST.__cfstring: 0x38900
+  __AUTH_CONST.__objc_const: 0x1a5a0
   __AUTH_CONST.__objc_intobj: 0x48f0
   __AUTH_CONST.__objc_arrayobj: 0xbb8
   __AUTH_CONST.__objc_doubleobj: 0x430
   __AUTH_CONST.__objc_dictobj: 0x280
   __AUTH_CONST.__objc_floatobj: 0x20
-  __AUTH_CONST.__auth_got: 0xe50
+  __AUTH_CONST.__auth_got: 0xe90
   __AUTH.__objc_data: 0x14b8
   __AUTH.__data: 0x138
-  __DATA.__objc_ivar: 0x182c
+  __DATA.__objc_ivar: 0x183c
   __DATA.__data: 0xf48
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x2940

   - /System/Library/PrivateFrameworks/SpotlightIndex.framework/Versions/A/SpotlightIndex
   - /System/Library/PrivateFrameworks/SpotlightLinguistics.framework/Versions/A/SpotlightLinguistics
   - /System/Library/PrivateFrameworks/SpotlightResources.framework/Versions/A/SpotlightResources
+  - /System/Library/PrivateFrameworks/TCC.framework/Versions/A/TCC
   - /System/Library/PrivateFrameworks/TelephonyUtilities.framework/Versions/A/TelephonyUtilities
   - /System/Library/PrivateFrameworks/ToolKit.framework/Versions/A/ToolKit
   - /System/Library/PrivateFrameworks/VoiceShortcutClient.framework/Versions/A/VoiceShortcutClient

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 6975
-  Symbols:   16061
-  CStrings:  8132
+  Functions: 7004
+  Symbols:   16118
+  CStrings:  8148
 
Symbols:
+ -[PRSRankingItem hasCorrespondingBookmark]
+ -[PRSRankingItem setHasCorrespondingBookmark:]
+ -[SPSearchQueryContext contactEntity]
+ -[SSMixedRankingConfig pinOverrideMrScoreThreshold]
+ -[SSMixedRankingConfig setPinOverrideMrScoreThreshold:]
+ -[SSMixedRankingScore policyApplied]
+ -[SSMixedRankingScore prePolicyScore]
+ -[SSMixedRankingScore setPolicyApplied:]
+ -[SSMixedRankingScore setPrePolicyScore:]
+ GCC_except_table52
+ GCC_except_table59
+ GCC_except_table63
+ GCC_except_table68
+ GCC_except_table98
+ OBJC_IVAR_$_PRSRankingItem._hasCorrespondingBookmark
+ OBJC_IVAR_$_SSMixedRankingConfig._pinOverrideMrScoreThreshold
+ OBJC_IVAR_$_SSMixedRankingScore._policyApplied
+ OBJC_IVAR_$_SSMixedRankingScore._prePolicyScore
+ SSAppExclusionsEnabled
+ SSAppExclusionsEnabled.sEnabled
+ SSAppExclusionsEnabled.sOnce
+ SSCampoEnabled.cachedResult
+ SSCampoEnabled.deadline
+ SSCopyTCCDisabledBundlesForSiriAccess
+ SSCopyTCCDisabledBundlesForSiriAccess.tccOnce
+ SSRefreshTCCDisabledBundlesCache
+ SSSubscribeTCCEventsForSiriAccess
+ _SSAppExclusionsEnabled
+ _SSCopyTCCDisabledBundlesForSiriAccess
+ _SSHomeBundleIdentifier
+ _SSHomeItemBelowRetrievalThresholds
+ _SSRefreshTCCDisabledBundlesCache
+ _SSSantizedBundleIDList
+ _SSSectionIsHome
+ _SSSubscribeTCCEventsForSiriAccess
+ _SSUnsubscribeTCCEventsForSiriAccess
+ _TCCAccessCopyBundleIdentifiersDisabledForService
+ ___SSAppExclusionsEnabled_block_invoke
+ ___SSCopyTCCDisabledBundlesForSiriAccess_block_invoke
+ ___SSSubscribeTCCEventsForSiriAccess_block_invoke
+ ___block_descriptor_40_e8_32bs_e50_v24?0Q8"NSObject<OS_tcc_authorization_record>"16l
+ _homeExtractEmbeddingSqDistances
+ _homeSqDistanceForSlot
+ _kTCCServiceSiriAccess
+ _mach_continuous_time
+ _mach_timebase_info
+ _objc_msgSend$bestTokenMatchRatio
+ _objc_msgSend$displayNameIncludingCountry:
+ _objc_msgSend$hasCorrespondingBookmark
+ _objc_msgSend$policyApplied
+ _objc_msgSend$prePolicyScore
+ _objc_msgSend$runningBundleIdsForProcessIds
+ _objc_msgSend$setRunningBundleIdsForProcessIds:
+ _tccCacheLock
+ _tccCachedBundles
+ _tcc_events_filter_create_with_criteria
+ _tcc_events_subscribe
+ _tcc_events_unsubscribe
+ _xpc_bool_create
+ _xpc_dictionary_create
+ homeSqDistanceForSlot
- GCC_except_table48
- GCC_except_table55
- _homeCosineForSlot
- homeCosineForSlot
CStrings:
+ ", policy: %@, prePolicyMrScore: %.04f"
+ "AppExclusions"
+ "Failed to create TCC events filter; disabled bundle cache will not auto-refresh"
+ "Failed to get TCC service name; disabled bundle cache will not auto-refresh"
+ "IntelligenceFlow"
+ "TCCAccessCopyBundleIdentifiersDisabledForService returned NULL; preserving existing cache"
+ "TCCAccessCopyBundleIdentifiersDisabledForService returned invalid type; preserving existing cache"
+ "[HomeDebug] [SqDistance] rejecting slot %lu: sqDist=%f out of valid [0,4] range (or NaN)"
+ "[HomeWeakRetrieval]"
+ "[PA]"
+ "com.apple.spotlight.clear.pasteboard.history"
+ "com.apple.spotlight.tcc.siri-access"
+ "mrScore: %.04f, %@, freshnessDate: %@%@"
+ "pinOverrideMrScoreThreshold"
+ "siri-access TCC event fired"
+ "siri-access TCC subscription armed"
+ "spotlight: TCC siri-access disabled bundles refreshed: %{private}@"
+ "v24@?0Q8@\"NSObject<OS_tcc_authorization_record>\"16"
- "[HomeDebug] [Consine] rejecting slot %lu: sqDist=%f out of valid [0,4] range (or NaN)"
- "mrScore: %.04f, %@, freshnessDate: %@"
```
