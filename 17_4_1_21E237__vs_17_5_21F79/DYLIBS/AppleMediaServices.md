## AppleMediaServices

> `/System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices`

```diff

-7.4.38.2.4
-  __TEXT.__text: 0x6289e4
-  __TEXT.__auth_stubs: 0x3d60
-  __TEXT.__objc_methlist: 0x1c174
+7.4.46.0.0
+  __TEXT.__text: 0x62ae90
+  __TEXT.__auth_stubs: 0x3df0
+  __TEXT.__objc_methlist: 0x1c22c
   __TEXT.__const: 0x55844
-  __TEXT.__cstring: 0x22754
-  __TEXT.__swift5_typeref: 0x2b35
-  __TEXT.__swift5_reflstr: 0x1874
+  __TEXT.__cstring: 0x22878
+  __TEXT.__swift5_typeref: 0x2b67
+  __TEXT.__swift5_reflstr: 0x1894
   __TEXT.__swift5_assocty: 0x630
-  __TEXT.__swift5_fieldmd: 0x1d0c
+  __TEXT.__swift5_fieldmd: 0x1d18
   __TEXT.__constg_swiftt: 0x21b4
   __TEXT.__swift5_builtin: 0x190
   __TEXT.__swift5_mpenum: 0x50
-  __TEXT.__swift5_capture: 0x12d0
+  __TEXT.__swift5_capture: 0x1314
   __TEXT.__swift5_protos: 0x64
   __TEXT.__swift5_proto: 0x500
   __TEXT.__swift5_types: 0x24c
-  __TEXT.__gcc_except_tab: 0x16308
-  __TEXT.__oslogstring: 0x29deb
+  __TEXT.__gcc_except_tab: 0x162a8
+  __TEXT.__oslogstring: 0x29fed
   __TEXT.__dlopen_cstrs: 0xa35
   __TEXT.__ustring: 0x1b2
-  __TEXT.__unwind_info: 0x1196c
-  __TEXT.__eh_frame: 0x84b0
-  __TEXT.__objc_classname: 0x37b4
-  __TEXT.__objc_methname: 0x3adf8
-  __TEXT.__objc_methtype: 0x660e
-  __TEXT.__objc_stubs: 0x29940
-  __DATA_CONST.__got: 0xa58
-  __DATA_CONST.__const: 0xa328
+  __TEXT.__unwind_info: 0x11ab8
+  __TEXT.__eh_frame: 0x8528
+  __TEXT.__objc_classname: 0x37b7
+  __TEXT.__objc_methname: 0x3b174
+  __TEXT.__objc_methtype: 0x664e
+  __TEXT.__objc_stubs: 0x29ae0
+  __DATA_CONST.__got: 0xa68
+  __DATA_CONST.__const: 0xa3a0
   __DATA_CONST.__objc_classlist: 0x10b8
   __DATA_CONST.__objc_catlist: 0xe8
   __DATA_CONST.__objc_protolist: 0x300
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x28de8
-  __DATA_CONST.__objc_selrefs: 0xd1d0
+  __DATA_CONST.__objc_const: 0x28e58
+  __DATA_CONST.__objc_selrefs: 0xd260
   __DATA_CONST.__objc_protorefs: 0x138
   __DATA_CONST.__objc_classrefs: 0x11c0
-  __DATA_CONST.__objc_superrefs: 0xb38
+  __DATA_CONST.__objc_superrefs: 0xb40
   __DATA_CONST.__objc_arraydata: 0x508
-  __AUTH_CONST.__const: 0x242a8
+  __AUTH_CONST.__const: 0x24418
   __AUTH_CONST.__objc_const: 0xd2e0
-  __AUTH_CONST.__cfstring: 0x1da20
-  __AUTH_CONST.__objc_intobj: 0xcd8
+  __AUTH_CONST.__cfstring: 0x1db00
+  __AUTH_CONST.__objc_intobj: 0xcf0
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_dictobj: 0x118
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0x1ec8
-  __AUTH.__objc_data: 0x6b30
-  __AUTH.__data: 0xae8
-  __DATA.__objc_ivar: 0x15d4
+  __AUTH_CONST.__auth_got: 0x1f10
+  __AUTH.__objc_data: 0x6ae0
+  __AUTH.__data: 0xaf0
+  __DATA.__objc_ivar: 0x15dc
   __DATA.__objc_data: 0x20
-  __DATA.__data: 0x5978
+  __DATA.__data: 0x5858
   __DATA.__thread_vars: 0x30
   __DATA.__thread_bss: 0x5
-  __DATA.__bss: 0x7ae0
-  __DATA.__common: 0xac0
+  __DATA.__bss: 0x7608
+  __DATA.__common: 0xaac
   __DATA_DIRTY.__objc_const: 0x48
   __DATA_DIRTY.__objc_ivar: 0x62c
-  __DATA_DIRTY.__objc_data: 0x4c38
-  __DATA_DIRTY.__data: 0x1750
-  __DATA_DIRTY.__bss: 0x2268
-  __DATA_DIRTY.__common: 0x78
+  __DATA_DIRTY.__objc_data: 0x4c88
+  __DATA_DIRTY.__data: 0x1d48
+  __DATA_DIRTY.__bss: 0x2328
+  __DATA_DIRTY.__common: 0x80
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 3CB24D26-30AE-3E37-8489-2CB17B4DE1A2
-  Functions: 21069
-  Symbols:   50132
-  CStrings:  22238
+  UUID: 7CF6FCD4-148C-3672-AA6C-A4167BD2BF0D
+  Functions: 21107
+  Symbols:   50207
+  CStrings:  22288
 
Symbols:
+ +[AMSBagNetworkTask _bagDataByApplyingOverridesToBagData:overrides:ignoredKeys:inserts:]
+ +[AMSDefaults bagOverrideInserts]
+ +[AMSDefaults setBagOverrideInserts:]
+ +[AMSDevice _deviceIsBundleWithMobileActivationFlag:storage:canHonorLasset:defaultsFlag:]
+ +[AMSDevice deviceIsChinaSKU]
+ +[AMSKeepAlive rbs_keepAliveWithName:style:qosOverrideIfRBManaged:relativePriority:block:]
+ +[AMSKeychain _primaryConstraintsForOpticID]
+ +[AMSLogConfig sharedRegulatoryEligibilityConfig]
+ -[ACAccount(AppleMediaServices) ams_isSubjectToPerDeviceBundleHolderAcknowledgement]
+ -[AMSLRUCache performExclusively:]
+ -[AMSMetricsIdentifierStore init]
+ -[AMSRatingsStorefrontTask _queryItems]
+ -[AMSRatingsStorefrontTask _urlBagKeyForMediaType:]
+ -[AMSSQLiteConnectionOptions isCheckpointingOnCloseDisabled]
+ -[AMSSQLiteConnectionOptions setCheckpointingOnCloseDisabled:]
+ -[NSMutableDictionary(AppleMediaServices) ams_deleteValueForKeyPath:]
+ -[NSMutableDictionary(AppleMediaServices) ams_flatInsertValue:forKeyPath:]
+ -[NSMutableDictionary(AppleMediaServices) ams_insertValue:forKeyPath:]
+ -[NSMutableDictionary(AppleMediaServices) ams_setValue:forKeyPath:shouldAppendToContainers:shouldFlatten:]
+ -[NSMutableDictionary(AppleMediaServices) ams_setValue:forKeyPathComponents:shouldAppendToContainers:shouldFlatten:]
+ _AMSBagKeyExpressCheckoutPaymentChoicesUsePost
+ _AMSMetricsDatabaseBlockWithKeepAlive
+ _OBJC_IVAR_$_AMSLRUCache._lock
+ _OBJC_IVAR_$_AMSMetricsIdentifierStore._database
+ _OBJC_IVAR_$_AMSSQLiteConnectionOptions._checkpointingOnCloseDisabled
+ __OBJC_$_CATEGORY_NSHTTPCookie_$_AppleMediaServices
+ __OBJC_$_CLASS_METHODS_NSHTTPCookie(AppleMediaServices|AMSCookieProperties|NSSecureCoding_Temporary)
+ __OBJC_$_INSTANCE_METHODS_NSHTTPCookie(AppleMediaServices|AMSCookieProperties|NSSecureCoding_Temporary)
+ __OBJC_CLASS_PROTOCOLS_$_NSHTTPCookie(AppleMediaServices|NSSecureCoding_Temporary)
+ ___107-[AMSPurchaseProtocolHandler _determineUpdatedBuyParamsFromResponse:urlAction:selectedAction:purchaseInfo:]_block_invoke
+ ___116-[NSMutableDictionary(AppleMediaServices) ams_setValue:forKeyPathComponents:shouldAppendToContainers:shouldFlatten:]_block_invoke
+ ___27-[AMSMetricsDatabase close]_block_invoke
+ ___29+[AMSDevice deviceIsChinaSKU]_block_invoke
+ ___33-[AMSEngagement syncWithRequest:]_block_invoke.103
+ ___40-[AMSEngagement _handleServiceResponse:]_block_invoke.133
+ ___40-[AMSEngagement _handleServiceResponse:]_block_invoke.146
+ ___40-[AMSEngagement _handleServiceResponse:]_block_invoke.147
+ ___41-[AMSMetricsDatabase insertEvents:error:]_block_invoke.86
+ ___42-[AMSMetricsDatabase initWithContainerId:]_block_invoke.9
+ ___44-[AMSAuthenticateTask performAuthentication]_block_invoke.44
+ ___46-[AMSAuthenticateTask _runCreateAccountDialog]_block_invoke.101
+ ___49+[AMSLogConfig sharedRegulatoryEligibilityConfig]_block_invoke
+ ___50-[AMSEngagement _failAllRunningPromisesWithError:]_block_invoke.127
+ ___52+[AMSMetricsDatabase sharedDatabaseWithContainerId:]_block_invoke_5
+ ___52+[AMSMetricsLoggingEvent shouldSampleErrorsWithBag:]_block_invoke.317
+ ___56-[AMSMetricsDatabase connectionNeedsResetForCorruption:]_block_invoke
+ ___56-[AMSMetricsDatabase removeIdentifiersForAccount:error:]_block_invoke.110
+ ___56-[AMSMetricsDatabase removeIdentifiersForAccount:error:]_block_invoke.114
+ ___57-[AMSMetricsDatabase cleanupInvalidIdentifiersWithError:]_block_invoke.103
+ ___57-[AMSMetricsDatabase identifierForKey:updateMaybe:error:]_block_invoke.130
+ ___57-[AMSMetricsDatabase identifierForKey:updateMaybe:error:]_block_invoke.138
+ ___58-[AMSAuthenticateTaskCoordinator _removeFromPromiseStore:]_block_invoke
+ ___62-[AMSMetricsDatabase identifierStoreForKey:updateMaybe:error:]_block_invoke.118
+ ___62-[AMSMetricsDatabase identifierStoreForKey:updateMaybe:error:]_block_invoke.126
+ ___62-[AMSMetricsDatabase permanentlyRemoveIdentifierForKey:error:]_block_invoke.159
+ ___67-[AMSMetricsDatabase enumerateEventsWithTopic:lockKey:objectBlock:]_block_invoke.74
+ ___67-[AMSMetricsDatabase enumerateEventsWithTopic:lockKey:objectBlock:]_block_invoke.80
+ ___67-[AMSMetricsDatabase enumerateUnsyncedIdentifiersUsingBlock:error:]_block_invoke.152
+ ___71-[AMSFinanceExpressCheckoutResponse _paymentChoicesRequestForCardData:]_block_invoke
+ ___72-[AMSMetricsDatabase enumerateUnsyncedIdentifierStoresUsingBlock:error:]_block_invoke.148
+ ___73-[AMSAuthenticateTask _finishWithVerifiedAccount:andAuthKitUpdateResult:]_block_invoke.79
+ ___74-[AMSFinanceExpressCheckoutResponse _recordUserChoiceForEngagementResult:]_block_invoke.64
+ ___76-[AMSAuthenticateTask _performAuthenticationAndGeneratePasswordWithAccount:]_block_invoke.91
+ ___76-[AMSAuthenticateTask _performAuthenticationAndGeneratePasswordWithAccount:]_block_invoke.92
+ ___76-[AMSAuthenticateTask _performAuthenticationAndGeneratePasswordWithAccount:]_block_invoke.93
+ ___76-[AMSAuthenticateTask _performAuthenticationAndGeneratePasswordWithAccount:]_block_invoke.95
+ ___76-[AMSAuthenticateTask _performAuthenticationAndGeneratePasswordWithAccount:]_block_invoke.97
+ ___77-[AMSAuthenticateTaskCoordinator _enqueueItem:handleAuthenticationWithBlock:]_block_invoke.54
+ ___77-[AMSAuthenticateTaskCoordinator _enqueueItem:handleAuthenticationWithBlock:]_block_invoke.55
+ ___77-[AMSAuthenticateTaskCoordinator _enqueueItem:handleAuthenticationWithBlock:]_block_invoke.56
+ ___77-[AMSAuthenticateTaskCoordinator _enqueueItem:handleAuthenticationWithBlock:]_block_invoke.57
+ ___77-[AMSAuthenticateTaskCoordinator _enqueueItem:handleAuthenticationWithBlock:]_block_invoke.58
+ ___77-[AMSAuthenticateTaskCoordinator _enqueueItem:handleAuthenticationWithBlock:]_block_invoke_2.59
+ ___88+[AMSBagNetworkTask _bagDataByApplyingOverridesToBagData:overrides:ignoredKeys:inserts:]_block_invoke
+ ___88+[AMSBagNetworkTask _bagDataByApplyingOverridesToBagData:overrides:ignoredKeys:inserts:]_block_invoke.108
+ ___90+[AMSDefaults shouldSampleWithPercentageValue:sessionDurationValue:identifier:completion:]_block_invoke.318
+ ___94+[AMSEngagement _recordLoggingEventWithBag:enqueueData:eventType:userInfo:destinations:error:]_block_invoke_4
+ ___94+[AMSEngagement _recordLoggingEventWithBag:enqueueData:eventType:userInfo:destinations:error:]_block_invoke_5
+ ___AMSMetricsDatabaseBlockWithKeepAlive_block_invoke
+ ___block_descriptor_32_e31_B24?0"NSString"8"NSString"16l
+ ___block_descriptor_32_e34_16?0"AMSEngagementDestination"8l
+ ___block_descriptor_40_e8_32s_e17_B16?0"AMSPair"8ls32l8
+ ___block_descriptor_40_e8_32s_e34_v32?0"NSString"8"NSArray"16^B24ls32l8
+ ___block_descriptor_48_e8_32s40w_e43_v24?0"AMSAuthenticateResult"8"NSError"16lw40l8s32l8
+ ___block_descriptor_56_e8_32s40s48w_e43_v24?0"AMSAuthenticateResult"8"NSError"16lw48l8s32l8s40l8
+ ___block_descriptor_72_e8_32s40s48s56s64r_e5_v8?0ls32l8s40l8r64l8s48l8s56l8
+ ___block_literal_global.136
+ ___block_literal_global.144
+ ___block_literal_global.152
+ ___block_literal_global.160
+ ___block_literal_global.163
+ ___block_literal_global.166
+ ___block_literal_global.171
+ ___block_literal_global.298
+ ___block_literal_global.307
+ ___block_literal_global.309
+ ___block_literal_global.311
+ ___block_literal_global.321
+ ___block_literal_global.397
+ ___block_literal_global.74
+ __unnamed_array_storage.72
+ _block_copy_helper.42
+ _block_destroy_helper.43
+ _objc_msgSend$_bagDataByApplyingOverridesToBagData:overrides:ignoredKeys:inserts:
+ _objc_msgSend$_deviceIsBundleWithMobileActivationFlag:storage:canHonorLasset:defaultsFlag:
+ _objc_msgSend$_primaryConstraintsForOpticID
+ _objc_msgSend$_queryItems
+ _objc_msgSend$_urlBagKeyForMediaType:
+ _objc_msgSend$ak_redactedCopy
+ _objc_msgSend$ams_deleteValueForKeyPath:
+ _objc_msgSend$ams_flatInsertValue:forKeyPath:
+ _objc_msgSend$ams_isSubjectToPerDeviceBundleHolderAcknowledgement
+ _objc_msgSend$ams_setValue:forKeyPath:shouldAppendToContainers:shouldFlatten:
+ _objc_msgSend$ams_setValue:forKeyPathComponents:shouldAppendToContainers:shouldFlatten:
+ _objc_msgSend$bagOverrideInserts
+ _objc_msgSend$deviceIsChinaSKU
+ _objc_msgSend$keepAliveWithName:style:qosOverrideIfRBManaged:relativePriority:block:
+ _objc_msgSend$rbs_keepAliveWithName:style:qosOverrideIfRBManaged:relativePriority:block:
+ _objc_msgSend$setCheckpointingOnCloseDisabled:
+ _objc_msgSend$sharedRegulatoryEligibilityConfig
+ _os_eligibility_get_domain_answer
+ _sqlite3_db_config
+ _symbolic _____Sg 8Dispatch0A3QoSV0B6SClassO
+ _symbolic ______pIegzo_ s5ErrorP
+ _symbolic ______pIgzo_ s5ErrorP
+ _symbolic ______pSgz_Xx s5ErrorP
- +[AMSKeychain _primaryConstraintsForReality]
- -[AMSLRUCache accessQueue]
- -[AMSLRUCache setAccessQueue:]
- -[AMSLRUCache setBackingDictionary:]
- -[AMSLRUCache setBackingList:]
- -[AMSLRUCacheItem setKey:]
- _AMSLogableAuthenticationResults
- _OBJC_IVAR_$_AMSLRUCache._accessQueue
- __OBJC_$_CATEGORY_NSHTTPCookie_$_NSSecureCoding_Temporary
- __OBJC_$_CLASS_METHODS_NSHTTPCookie(NSSecureCoding_Temporary|AppleMediaServices|AMSCookieProperties)
- __OBJC_$_INSTANCE_METHODS_NSHTTPCookie(NSSecureCoding_Temporary|AppleMediaServices|AMSCookieProperties)
- __OBJC_CLASS_PROTOCOLS_$_NSHTTPCookie(NSSecureCoding_Temporary|AppleMediaServices)
- ___20-[AMSLRUCache count]_block_invoke
- ___26-[AMSLRUCache description]_block_invoke
- ___31-[AMSLRUCache removeAllObjects]_block_invoke
- ___32-[AMSLRUCache allObjectsAndKeys]_block_invoke_2
- ___32-[AMSLRUCache setObject:forKey:]_block_invoke
- ___33-[AMSEngagement syncWithRequest:]_block_invoke.98
- ___40-[AMSEngagement _handleServiceResponse:]_block_invoke.129
- ___40-[AMSEngagement _handleServiceResponse:]_block_invoke.135
- ___40-[AMSEngagement _handleServiceResponse:]_block_invoke.142
- ___41-[AMSMetricsDatabase insertEvents:error:]_block_invoke.79
- ___44-[AMSAuthenticateTask performAuthentication]_block_invoke.26
- ___46-[AMSAuthenticateTask _runCreateAccountDialog]_block_invoke.83
- ___46-[AMSLRUCache objectForKey:canLogCacheMisses:]_block_invoke
- ___46-[AMSLRUCache objectForKey:withCreationBlock:]_block_invoke
- ___50-[AMSEngagement _failAllRunningPromisesWithError:]_block_invoke.123
- ___52+[AMSMetricsLoggingEvent shouldSampleErrorsWithBag:]_block_invoke.314
- ___56-[AMSMetricsDatabase removeIdentifiersForAccount:error:]_block_invoke.103
- ___56-[AMSMetricsDatabase removeIdentifiersForAccount:error:]_block_invoke.107
- ___57-[AMSMetricsDatabase cleanupInvalidIdentifiersWithError:]_block_invoke.96
- ___57-[AMSMetricsDatabase identifierForKey:updateMaybe:error:]_block_invoke.123
- ___57-[AMSMetricsDatabase identifierForKey:updateMaybe:error:]_block_invoke.131
- ___62-[AMSMetricsDatabase identifierStoreForKey:updateMaybe:error:]_block_invoke.111
- ___62-[AMSMetricsDatabase identifierStoreForKey:updateMaybe:error:]_block_invoke.119
- ___62-[AMSMetricsDatabase permanentlyRemoveIdentifierForKey:error:]_block_invoke.152
- ___67-[AMSMetricsDatabase enumerateEventsWithTopic:lockKey:objectBlock:]_block_invoke.67
- ___67-[AMSMetricsDatabase enumerateEventsWithTopic:lockKey:objectBlock:]_block_invoke.73
- ___67-[AMSMetricsDatabase enumerateUnsyncedIdentifiersUsingBlock:error:]_block_invoke.145
- ___72-[AMSMetricsDatabase enumerateUnsyncedIdentifierStoresUsingBlock:error:]_block_invoke.141
- ___73-[AMSAuthenticateTask _finishWithVerifiedAccount:andAuthKitUpdateResult:]_block_invoke.61
- ___74-[AMSFinanceExpressCheckoutResponse _recordUserChoiceForEngagementResult:]_block_invoke.63
- ___76-[AMSAuthenticateTask _performAuthenticationAndGeneratePasswordWithAccount:]_block_invoke.73
- ___76-[AMSAuthenticateTask _performAuthenticationAndGeneratePasswordWithAccount:]_block_invoke.74
- ___76-[AMSAuthenticateTask _performAuthenticationAndGeneratePasswordWithAccount:]_block_invoke.75
- ___76-[AMSAuthenticateTask _performAuthenticationAndGeneratePasswordWithAccount:]_block_invoke.77
- ___76-[AMSAuthenticateTask _performAuthenticationAndGeneratePasswordWithAccount:]_block_invoke.79
- ___77-[AMSAuthenticateTaskCoordinator _enqueueItem:handleAuthenticationWithBlock:]_block_invoke.36
- ___77-[AMSAuthenticateTaskCoordinator _enqueueItem:handleAuthenticationWithBlock:]_block_invoke.37
- ___77-[AMSAuthenticateTaskCoordinator _enqueueItem:handleAuthenticationWithBlock:]_block_invoke.38
- ___77-[AMSAuthenticateTaskCoordinator _enqueueItem:handleAuthenticationWithBlock:]_block_invoke.39
- ___77-[AMSAuthenticateTaskCoordinator _enqueueItem:handleAuthenticationWithBlock:]_block_invoke.40
- ___77-[AMSAuthenticateTaskCoordinator _enqueueItem:handleAuthenticationWithBlock:]_block_invoke_2.41
- ___90+[AMSDefaults shouldSampleWithPercentageValue:sessionDurationValue:identifier:completion:]_block_invoke.315
- ___block_descriptor_32_e17_B16?0"AMSPair"8l
- ___block_descriptor_48_e8_32s40s_e43_v24?0"AMSAuthenticateResult"8"NSError"16ls32l8s40l8
- ___block_descriptor_56_e8_32s40s48s_e43_v24?0"AMSAuthenticateResult"8"NSError"16ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48bs56r_e5_v8?0lr56l8s32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48s56r_e5_v8?0ls32l8s40l8r56l8s48l8
- ___block_literal_global.114
- ___block_literal_global.123
- ___block_literal_global.132
- ___block_literal_global.141
- ___block_literal_global.148
- ___block_literal_global.156
- ___block_literal_global.162
- ___block_literal_global.295
- ___block_literal_global.301
- ___block_literal_global.306
- ___block_literal_global.308
- ___block_literal_global.318
- ___block_literal_global.394
- __unnamed_array_storage.71
- _objc_msgSend$_primaryConstraintsForReality
- _objc_msgSend$rbs_invalidate
- _objc_msgSend$rbs_keepAliveWithName:
- _objc_msgSend$setValue:forKeyPath:
CStrings:
+ "\x01\x13"
+ "%{public}@ Removing request from store. pair = %{public}@"
+ "%{public}@ There are no matching authentication requests calling authHandler immediately for request = %{public}@"
+ "%{public}@ Updating account bundle holder record.@"
+ "%{public}@: [%{public}@] Error getting URL from the bag for the key: %@."
+ "%{public}@: [%{public}@] Failed to get `AMSBagKeyExpressCheckoutPaymentChoicesUsePost` bag key. %{public}@"
+ "%{public}@: [%{public}@] Inserting to the following keys: %{public}@"
+ "%{public}@: [%{public}@] Will attempt to set new per device holder record. Setting  to %d"
+ "%{public}@Recording metrics for a successful biometric authorization that is neither Signature- nor PET-based"
+ "1.7"
+ "@16@?0@\"AMSEngagementDestination\"8"
+ "AMSMetricsDatabase-init-createDirectory"
+ "AMSMetricsDatabase-init-updateSchema"
+ "AMSMetricsDatabase: Database operation took %f seconds"
+ "AMSPurchaseProtocolHandler: [%{public}@] Updating buy params from any action the current URLAction is %{public}@ selected action is %{public}@"
+ "AMSRatingsStorefrontAppsURL"
+ "AMSRatingsStorefrontBooksURL"
+ "AMSRatingsStorefrontMediaURL"
+ "AMSRatingsStorefrontPodcastsURL"
+ "B24@?0@\"NSString\"8@\"NSString\"16"
+ "B36@0:8B16@20B28B32"
+ "BagOverrideInserts"
+ "Exited early because of null account"
+ "Failed to disable checkpointing on close: %{public}d"
+ "Storefronts URL string malformed"
+ "T@\"<NSCopying>\",R,N,V_key"
+ "T@\"AMSDoubleLinkedList\",R,N,V_backingList"
+ "T@\"NSMutableDictionary\",R,N,V_backingDictionary"
+ "TB,N,GisCheckpointingOnCloseDisabled,V_checkpointingOnCloseDisabled"
+ "_bagDataByApplyingOverridesToBagData:overrides:ignoredKeys:inserts:"
+ "_checkpointingOnCloseDisabled"
+ "_deviceIsBundleWithMobileActivationFlag:storage:canHonorLasset:defaultsFlag:"
+ "_primaryConstraintsForOpticID"
+ "_queryItems"
+ "_urlBagKeyForMediaType:"
+ "ak_redactedCopy"
+ "ams_deleteValueForKeyPath:"
+ "ams_flatInsertValue:forKeyPath:"
+ "ams_insertValue:forKeyPath:"
+ "ams_isSubjectToPerDeviceBundleHolderAcknowledgement"
+ "ams_setValue:forKeyPath:shouldAppendToContainers:shouldFlatten:"
+ "ams_setValue:forKeyPathComponents:shouldAppendToContainers:shouldFlatten:"
+ "applePayExpressCheckoutPaymentChoicesUsePost"
+ "bagOverrideInserts"
+ "checkpointingOnCloseDisabled"
+ "cnformat"
+ "deviceIsChinaSKU"
+ "isCheckpointingOnCloseDisabled"
+ "js_version"
+ "keepAliveWithName:style:qosOverrideIfRBManaged:relativePriority:block:"
+ "performExclusively:"
+ "rbsAssertionAcquired"
+ "rbs_keepAliveWithName:style:qosOverrideIfRBManaged:relativePriority:block:"
+ "regulatoryeligibility"
+ "setBagOverrideInserts:"
+ "setCheckpointingOnCloseDisabled:"
+ "sharedRegulatoryEligibilityConfig"
+ "v40@0:8@16@24B32B36"
+ "v52@0:8@16q24I32q36@?44"
- "%{public}@ Removing request from store"
- "%{public}@ There are no matching authentication requests for request = %{publid}@"
- "%{public}@: [%{public}@] Recording metrics for a successful biometric authorization that is neither Signature- nor PET-based"
- "AMSMetricsDatabase-init"
- "AMSMetricsDatabase-vacuum"
- "AMSMetricsDatabaseSchema-migration-from-%ld"
- "AMSPurchaseProtocolHandler: [%{public}@] Updating buy params from any action"
- "Exited early because of null acount"
- "Successfully checkpoint-truncated WAL: walLogFrames = %d, walFramesCheckpointed = %d."
- "T@\"<NSCopying>\",W,N,V_key"
- "T@\"AMSDoubleLinkedList\",&,N,V_backingList"
- "T@\"NSMutableDictionary\",&,N,V_backingDictionary"
- "_primaryConstraintsForReality"
- "com.apple.AppleMediaServices.AMSLRUCache.accessQueue.%p"
- "com.apple.AppleMediaServicesUIDynamic"
- "setBackingList:"
- "setValue:forKeyPath:"

```
