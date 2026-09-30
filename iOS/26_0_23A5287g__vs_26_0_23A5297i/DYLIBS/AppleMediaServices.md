## AppleMediaServices

> `/System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices`

```diff

-9.0.67.0.0
-  __TEXT.__text: 0x76dd58
-  __TEXT.__auth_stubs: 0x48f0
-  __TEXT.__objc_methlist: 0x21b04
-  __TEXT.__const: 0x5c578
-  __TEXT.__dlopen_cstrs: 0x937
-  __TEXT.__cstring: 0x2a4ee
+9.0.72.0.0
+  __TEXT.__text: 0x778980
+  __TEXT.__auth_stubs: 0x48b0
+  __TEXT.__objc_methlist: 0x21b0c
+  __TEXT.__const: 0x5c698
+  __TEXT.__dlopen_cstrs: 0x98b
+  __TEXT.__cstring: 0x2a764
   __TEXT.__swift5_typeref: 0x5a6b
-  __TEXT.__swift5_reflstr: 0x3104
+  __TEXT.__swift5_reflstr: 0x30e4
   __TEXT.__swift5_assocty: 0xe88
   __TEXT.__constg_swiftt: 0x4714
   __TEXT.__swift5_builtin: 0x2bc
-  __TEXT.__swift5_fieldmd: 0x3f48
+  __TEXT.__swift5_fieldmd: 0x3f3c
   __TEXT.__swift5_proto: 0xe60
   __TEXT.__swift5_types: 0x524
   __TEXT.__swift_as_entry: 0x628

   __TEXT.__swift5_capture: 0x2c50
   __TEXT.__swift5_mpenum: 0x58
   __TEXT.__swift5_protos: 0xb8
-  __TEXT.__oslogstring: 0x2eb6a
-  __TEXT.__gcc_except_tab: 0x5bc8
+  __TEXT.__oslogstring: 0x2ec9c
+  __TEXT.__gcc_except_tab: 0x5c54
   __TEXT.__ustring: 0x1b2
-  __TEXT.__unwind_info: 0x101a8
-  __TEXT.__eh_frame: 0x12454
-  __TEXT.__objc_classname: 0x3ee0
-  __TEXT.__objc_methname: 0x4321a
-  __TEXT.__objc_methtype: 0x77fe
-  __TEXT.__objc_stubs: 0x2db80
+  __TEXT.__unwind_info: 0xfd58
+  __TEXT.__eh_frame: 0x12518
+  __TEXT.__objc_classname: 0x3ede
+  __TEXT.__objc_methname: 0x4330c
+  __TEXT.__objc_methtype: 0x77c8
+  __TEXT.__objc_stubs: 0x2dcc0
   __DATA_CONST.__got: 0x19a0
-  __DATA_CONST.__const: 0xbf40
+  __DATA_CONST.__const: 0xbfd8
   __DATA_CONST.__objc_classlist: 0x13e0
   __DATA_CONST.__objc_catlist: 0xf0
   __DATA_CONST.__objc_protolist: 0x420
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xec40
+  __DATA_CONST.__objc_selrefs: 0xec78
   __DATA_CONST.__objc_protorefs: 0x200
   __DATA_CONST.__objc_superrefs: 0xc90
-  __DATA_CONST.__objc_arraydata: 0x508
-  __AUTH_CONST.__auth_got: 0x2490
-  __AUTH_CONST.__const: 0x2ba28
-  __AUTH_CONST.__cfstring: 0x21740
-  __AUTH_CONST.__objc_const: 0x3aca0
+  __DATA_CONST.__objc_arraydata: 0x578
+  __AUTH_CONST.__auth_got: 0x2470
+  __AUTH_CONST.__const: 0x2cb58
+  __AUTH_CONST.__cfstring: 0x21980
+  __AUTH_CONST.__objc_const: 0x3abd0
   __AUTH_CONST.__objc_intobj: 0xc48
-  __AUTH_CONST.__objc_arrayobj: 0x108
+  __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_dictobj: 0x118
   __AUTH.__objc_data: 0x8ce0
-  __AUTH.__data: 0x1de0
-  __DATA.__objc_ivar: 0x1860
-  __DATA.__data: 0x69f0
+  __AUTH.__data: 0x1dd0
+  __DATA.__objc_ivar: 0x1864
+  __DATA.__data: 0x69b0
   __DATA.__bss: 0x17e79
-  __DATA.__common: 0xb18
-  __DATA_DIRTY.__objc_ivar: 0x6b4
+  __DATA.__common: 0xb68
+  __DATA_DIRTY.__objc_ivar: 0x69c
   __DATA_DIRTY.__objc_data: 0x5968
   __DATA_DIRTY.__data: 0x1f58
-  __DATA_DIRTY.__bss: 0x3840
+  __DATA_DIRTY.__bss: 0x3860
   __DATA_DIRTY.__common: 0x78
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 5A96913B-A12B-3FE0-A0B6-899C728176B1
-  Functions: 24221
-  Symbols:   49975
-  CStrings:  24867
+  UUID: 0C95B0D3-69F1-32A5-AC8D-EE7ABA7D79CA
+  Functions: 24228
+  Symbols:   50010
+  CStrings:  24910
 
Symbols:
+ +[AMSMappedBundleInfo bundleIdentifierIsGames:]
+ +[AMSMetrics _defaultAccountClearingTopics]
+ -[AMSBagFrozenDataSource dictionary]
+ -[AMSChannelLinkTask _processSubscriptionStatusForResult:]
+ -[AMSMetrics _cachedAccountClearingTopicsFromBag]
+ -[AMSMetrics _clearAccountForEventIfNeeded:]
+ -[AMSMetrics _configureAccountIdentifierForEvent:]
+ -[AMSMetrics _topicsRequiringAccountClearing]
+ -[AMSMetrics enqueueEventWithoutAccountClearing:]
+ -[AMSMetrics enqueueEventsWithoutAccountClearing:]
+ -[AMSMetrics promiseForEnqueueingEvents:skipAccountClearing:]
+ -[AMSPaymentSheetPerformanceMetrics pageEndTime]
+ -[AMSPaymentSheetPerformanceMetrics setPageEndTime:]
+ -[AMSSnapshotBag dictionary]
+ -[AMSSystemEngagementTask resultPromise]
+ -[AMSSystemEngagementTask setResultPromise:]
+ GCC_except_table80
+ _OBJC_IVAR_$_AMSPaymentSheetPerformanceMetrics._pageEndTime
+ ___34-[AMSSystemEngagementTask present]_block_invoke.10
+ ___36-[AMSMetrics _processOperationQueue]_block_invoke.139
+ ___36-[AMSMetrics _processOperationQueue]_block_invoke.144
+ ___36-[AMSMetrics _processOperationQueue]_block_invoke_2.140
+ ___43+[AMSMetrics _defaultAccountClearingTopics]_block_invoke
+ ___44-[AMSMetrics _handleFlushIntervalWithStyle:]_block_invoke.151
+ ___49-[AMSMetrics _cachedAccountClearingTopicsFromBag]_block_invoke
+ ___50-[AMSMetrics _beginFlushIntervalWithStyle:events:]_block_invoke.147
+ ___50-[AMSMetrics _beginFlushIntervalWithStyle:events:]_block_invoke.149
+ ___52-[AMSChannelLinkTask _recordEngagementMetricsEvent:]_block_invoke.179
+ ___58-[AMSChannelLinkTask _processSubscriptionStatusForResult:]_block_invoke
+ ___74-[AMSSystemEngagementTask _listenForAppForegroundWithHandle:monitorInApp:]_block_invoke.105
+ ___74-[AMSSystemEngagementTask _listenForAppForegroundWithHandle:monitorInApp:]_block_invoke.110
+ ___74-[AMSSystemEngagementTask _listenForAppForegroundWithHandle:monitorInApp:]_block_invoke.112
+ ___82-[AMSPaymentSheetTask paymentAuthorizationController:didAuthorizePayment:handler:]_block_invoke.309
+ ___block_descriptor_32_e22_v16?0"NSDictionary"8l
+ ___block_descriptor_40_e8_32s_e47_v24?0"ICMusicSubscriptionStatus"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32w_e53_"AMSPromise"24?0"AMSEngagementResult"8"NSError"16lw32l8
+ ___block_literal_global.132
+ ___block_literal_global.167
+ ___block_literal_global.194
+ _objc_msgSend$_cachedAccountClearingTopicsFromBag
+ _objc_msgSend$_clearAccountForEventIfNeeded:
+ _objc_msgSend$_configureAccountIdentifierForEvent:
+ _objc_msgSend$_defaultAccountClearingTopics
+ _objc_msgSend$_processSubscriptionStatusForResult:
+ _objc_msgSend$_topicsRequiringAccountClearing
+ _objc_msgSend$cachedValuesForKeys:observationToken:updateHandler:
+ _objc_msgSend$enqueueEventsWithoutAccountClearing:
+ _objc_msgSend$pageEndTime
+ _objc_msgSend$promiseForEnqueueingEvents:skipAccountClearing:
+ _objc_msgSend$removeObserverWithToken:
+ _objc_msgSend$setResultPromise:
+ _objc_msgSend$setSubscriptionStatusFromResponsePayload:withCompletionHandler:
- -[AMSDeveloperSilentAuthTokenConsentTask appId]
- -[AMSDeveloperSilentAuthTokenConsentTask initWithAppId:account:bag:]
- -[AMSDeveloperSilentAuthTokenFetchTask appId]
- -[AMSDeveloperSilentAuthTokenFetchTask initWithAppId:account:bag:]
- -[AMSDeveloperSilentAuthTokenUpdateConsentTask appId]
- -[AMSDeveloperSilentAuthTokenUpdateConsentTask initWithAppId:account:bag:]
- -[AMSDeveloperSilentAuthTokenUpdateTask appId]
- -[AMSDeveloperSilentAuthTokenUpdateTask initWithAppId:account:bag:]
- -[AMSSystemEngagementTask dispatchGroup]
- -[AMSSystemEngagementTask error]
- -[AMSSystemEngagementTask result]
- -[AMSSystemEngagementTask setDispatchGroup:]
- -[AMSSystemEngagementTask setError:]
- -[AMSSystemEngagementTask setResult:]
- GCC_except_table51
- GCC_except_table70
- ___36-[AMSMetrics _processOperationQueue]_block_invoke.87
- ___36-[AMSMetrics _processOperationQueue]_block_invoke.92
- ___36-[AMSMetrics _processOperationQueue]_block_invoke_2.88
- ___44-[AMSMetrics _handleFlushIntervalWithStyle:]_block_invoke.99
- ___50-[AMSMetrics _beginFlushIntervalWithStyle:events:]_block_invoke.95
- ___50-[AMSMetrics _beginFlushIntervalWithStyle:events:]_block_invoke.97
- ___52-[AMSChannelLinkTask _recordEngagementMetricsEvent:]_block_invoke.175
- ___74-[AMSSystemEngagementTask _listenForAppForegroundWithHandle:monitorInApp:]_block_invoke.101
- ___74-[AMSSystemEngagementTask _listenForAppForegroundWithHandle:monitorInApp:]_block_invoke.106
- ___74-[AMSSystemEngagementTask _listenForAppForegroundWithHandle:monitorInApp:]_block_invoke.108
- ___82-[AMSPaymentSheetTask paymentAuthorizationController:didAuthorizePayment:handler:]_block_invoke.308
- ___block_literal_global.115
- ___block_literal_global.190
- ___block_literal_global.77
- _dispatch_group_create
- _dispatch_group_enter
- _dispatch_group_leave
- _dispatch_group_wait
- _objc_msgSend$dispatchGroup
- _objc_msgSend$initWithBundleId:account:bag:
- _objc_msgSend$setDispatchGroup:
CStrings:
+ "%{public}@: [%{public}@] Clearing account for event with topic: %{public}@"
+ "%{public}@: [%{public}@] Processed subscription status successfully: %{public}@"
+ "%{public}@: [%{public}@] Processing subscription status failed. Error: %{public}@."
+ "%{public}@: [%{public}@] Processing subscription status: %{public}@"
+ "@\"AMSPromise\"24@?0@\"AMSEngagementResult\"8@\"NSError\"16"
+ "Td,N,V_pageEndTime"
+ "_cachedAccountClearingTopicsFromBag"
+ "_clearAccountForEventIfNeeded:"
+ "_configureAccountIdentifierForEvent:"
+ "_defaultAccountClearingTopics"
+ "_pageEndTime"
+ "_processSubscriptionStatusForResult:"
+ "_topicsRequiringAccountClearing"
+ "accountClearingTopics"
+ "bundleIdentifierIsGames:"
+ "com.apple.GameOverlayUI"
+ "com.apple.games"
+ "enqueueEventWithoutAccountClearing:"
+ "enqueueEventsWithoutAccountClearing:"
+ "omitAppBadge"
+ "promiseForEnqueueingEvents:skipAccountClearing:"
+ "setSubscriptionStatusFromResponsePayload:withCompletionHandler:"
+ "v24@?0@\"ICMusicSubscriptionStatus\"8@\"NSError\"16"
+ "xp_ase_appstore/arcade_substate"
+ "xp_ase_appstore/billing_refunds"
+ "xp_ase_appstore/preorders"
+ "xp_ase_appstore/subscription_movement"
+ "xp_ase_messaging/appstore_experimentation"
+ "xp_ase_messaging/appstore_notifications"
+ "xp_ase_payments/appstore_payments_ue"
+ "xp_ase_payments/appstore_redeem_ue"
+ "xp_ase_payments/transient"
+ "xp_ase_personalization/appstore"
+ "xp_ase_subscriptions/commerce"
+ "xp_ase_subscriptions/movement"
+ "xp_ase_subscriptions/ue"
+ "xp_ase_transient/appstore_ue"
- "@\"AMSEngagementResult\""
- "@\"NSObject<OS_dispatch_group>\""
- "T@\"AMSEngagementResult\",&,N,V_result"
- "T@\"NSObject<OS_dispatch_group>\",&,N,V_dispatchGroup"
- "T@\"NSString\",R,C,N,V_appId"
- "_appId"
- "_dispatchGroup"
- "appId"
- "dispatchGroup"
- "initWithAppId:account:bag:"
- "setDispatchGroup:"

```
