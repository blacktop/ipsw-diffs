## SpotlightServices

> `/System/Library/PrivateFrameworks/SpotlightServices.framework/SpotlightServices`

```diff

-2459.105.0.0.0
-  __TEXT.__text: 0x15b480
-  __TEXT.__objc_methlist: 0xe628
-  __TEXT.__const: 0x2df8
-  __TEXT.__cstring: 0x3a8ba
-  __TEXT.__gcc_except_tab: 0x5068
-  __TEXT.__oslogstring: 0xba3b
+2465.1.2.0.0
+  __TEXT.__text: 0x15c150
+  __TEXT.__objc_methlist: 0xe648
+  __TEXT.__const: 0x2e38
+  __TEXT.__cstring: 0x3a99a
+  __TEXT.__gcc_except_tab: 0x5058
+  __TEXT.__oslogstring: 0xbc0b
   __TEXT.__ustring: 0x892
   __TEXT.__dlopen_cstrs: 0x12f
   __TEXT.__swift5_typeref: 0x1e8

   __TEXT.__swift5_proto: 0xc
   __TEXT.__swift5_types: 0x18
   __TEXT.__swift5_capture: 0xa4
-  __TEXT.__unwind_info: 0x4020
+  __TEXT.__unwind_info: 0x4068
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x100d8
+  __DATA_CONST.__const: 0x10108
   __DATA_CONST.__objc_classlist: 0x5d0
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8da0
+  __DATA_CONST.__objc_selrefs: 0x8dd0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x428
   __DATA_CONST.__objc_arraydata: 0x4778
-  __DATA_CONST.__got: 0x1c30
-  __AUTH_CONST.__const: 0x2b20
-  __AUTH_CONST.__cfstring: 0x36c00
-  __AUTH_CONST.__objc_const: 0x181c0
+  __DATA_CONST.__got: 0x1c40
+  __AUTH_CONST.__const: 0x2b80
+  __AUTH_CONST.__cfstring: 0x36c60
+  __AUTH_CONST.__objc_const: 0x181f0
   __AUTH_CONST.__objc_intobj: 0x4788
   __AUTH_CONST.__objc_arrayobj: 0xc90
   __AUTH_CONST.__objc_doubleobj: 0x310
   __AUTH_CONST.__objc_dictobj: 0x258
   __AUTH_CONST.__objc_floatobj: 0x20
-  __AUTH_CONST.__auth_got: 0xf40
+  __AUTH_CONST.__auth_got: 0xf80
   __AUTH.__objc_data: 0x16e8
   __AUTH.__data: 0xc8
-  __DATA.__objc_ivar: 0x15b4
+  __DATA.__objc_ivar: 0x15b8
   __DATA.__data: 0xe88
   __DATA.__common: 0x28
   __DATA_DIRTY.__objc_data: 0x2580

   - /System/Library/PrivateFrameworks/AeroML.framework/AeroML
   - /System/Library/PrivateFrameworks/AggregateDictionary.framework/AggregateDictionary
   - /System/Library/PrivateFrameworks/AppPredictionClient.framework/AppPredictionClient
+  - /System/Library/PrivateFrameworks/AppProtection.framework/AppProtection
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams

   - /System/Library/PrivateFrameworks/SpotlightLinguistics.framework/SpotlightLinguistics
   - /System/Library/PrivateFrameworks/SpotlightResources.framework/SpotlightResources
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
+  - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities
   - /System/Library/PrivateFrameworks/ToolKit.framework/ToolKit
   - /System/Library/PrivateFrameworks/VoiceShortcutClient.framework/VoiceShortcutClient

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 6435
-  Symbols:   14844
-  CStrings:  7929
+  Functions: 6458
+  Symbols:   14887
+  CStrings:  7943
 
Symbols:
+ -[PRSRankingItem hasCorrespondingBookmark]
+ -[PRSRankingItem setHasCorrespondingBookmark:]
+ -[SPSearchQueryContext contactEntity]
+ GCC_except_table58
+ GCC_except_table61
+ GCC_except_table91
+ _OBJC_CLASS_$_APApplication
+ _OBJC_IVAR_$_PRSRankingItem._hasCorrespondingBookmark
+ _SSAppExclusionsEnabled
+ _SSAppExclusionsEnabled.sEnabled
+ _SSAppExclusionsEnabled.sOnce
+ _SSCampoEnabled.cachedResult
+ _SSCampoEnabled.deadline
+ _SSCopyTCCDisabledBundlesForSiriAccess
+ _SSCopyTCCDisabledBundlesForSiriAccess.tccOnce
+ _SSHomeBundleIdentifier
+ _SSHomeItemBelowRetrievalThresholds
+ _SSInvalidateAppExclusionsDisabledIDsCache
+ _SSRefreshTCCDisabledBundlesCache
+ _SSSantizedBundleIDList
+ _SSSectionIsHome
+ _SSSubscribeTCCEventsForSiriAccess
+ _SSUnsubscribeTCCEventsForSiriAccess
+ _TCCAccessCopyBundleIdentifiersDisabledForService
+ __SSApply11_2Migration.onceToken
+ __SSApply11_2Migration.sResult
+ ___SSAppExclusionsEnabled_block_invoke
+ ___SSCopyTCCDisabledBundlesForSiriAccess_block_invoke
+ ___SSSubscribeTCCEventsForSiriAccess_block_invoke
+ ____SSApply11_2Migration_block_invoke
+ ___block_descriptor_40_e8_32bs_e50_v24?0Q8"NSObject<OS_tcc_authorization_record>"16ls32l8
+ _homeExtractEmbeddingSqDistances
+ _homeSqDistanceForSlot
+ _kTCCServiceSiriAccess
+ _mach_continuous_time
+ _mach_timebase_info
+ _objc_msgSend$displayNameIncludingCountry:
+ _objc_msgSend$hiddenApplications
+ _objc_msgSend$lockedApplications
+ _sDisabledIDsCache
+ _sDisabledIDsCacheLock
+ _sDisabledIDsCacheValid
+ _tccCacheLock
+ _tccCachedBundles
+ _tcc_events_filter_create_with_criteria
+ _tcc_events_subscribe
+ _tcc_events_unsubscribe
+ _xpc_bool_create
+ _xpc_dictionary_create
- GCC_except_table50
- GCC_except_table57
- GCC_except_table90
- _SPCopyPrefsDisabledApps.onceToken
- ___SPCopyPrefsDisabledApps_block_invoke
- _homeCosineForSlot
CStrings:
+ "AppExclusions"
+ "DisabledBundlesFromSiriTCC"
+ "Failed to create TCC events filter; disabled bundle cache will not auto-refresh"
+ "Failed to get TCC service name; disabled bundle cache will not auto-refresh"
+ "IntelligenceFlow"
+ "TCCAccessCopyBundleIdentifiersDisabledForService returned NULL; preserving existing cache"
+ "TCCAccessCopyBundleIdentifiersDisabledForService returned invalid type; preserving existing cache"
+ "[HomeDebug] [SqDistance] rejecting slot %lu: sqDist=%f out of valid [0,4] range (or NaN)"
+ "[HomeWeakRetrieval]"
+ "com.apple.spotlight.clear.pasteboard.history"
+ "com.apple.spotlight.tcc.siri-access"
+ "siri-access TCC event fired"
+ "siri-access TCC subscription armed"
+ "spotlight: TCC siri-access disabled bundles refreshed: %{private}@"
+ "v24@?0Q8@\"NSObject<OS_tcc_authorization_record>\"16"
- "[HomeDebug] [Consine] rejecting slot %lu: sqDist=%f out of valid [0,4] range (or NaN)"
```
