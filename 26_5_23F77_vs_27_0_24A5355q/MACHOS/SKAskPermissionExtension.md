## SKAskPermissionExtension

> `/System/Library/Frameworks/StoreKit.framework/PlugIns/SKAskPermissionExtension.appex/SKAskPermissionExtension`

```diff

-815.5.6.0.0
-  __TEXT.__text: 0x3754
-  __TEXT.__auth_stubs: 0x290
-  __TEXT.__objc_stubs: 0x780
-  __TEXT.__objc_methlist: 0x9fc
-  __TEXT.__objc_classname: 0x2ae
-  __TEXT.__objc_methname: 0x1924
-  __TEXT.__objc_methtype: 0xda9
-  __TEXT.__cstring: 0xb78
-  __TEXT.__gcc_except_tab: 0x34c
-  __TEXT.__const: 0x1a
-  __TEXT.__oslogstring: 0x23d
-  __TEXT.__unwind_info: 0x230
-  __DATA_CONST.__auth_got: 0x158
-  __DATA_CONST.__got: 0xa0
-  __DATA_CONST.__const: 0x4e0
-  __DATA_CONST.__cfstring: 0x19a0
+816.0.30.2.1
+  __TEXT.__text: 0x2450
+  __TEXT.__auth_stubs: 0x230
+  __TEXT.__objc_stubs: 0x5c0
+  __TEXT.__objc_methlist: 0x894
+  __TEXT.__objc_classname: 0x293
+  __TEXT.__objc_methname: 0x13dc
+  __TEXT.__objc_methtype: 0xa54
+  __TEXT.__cstring: 0xb50
+  __TEXT.__gcc_except_tab: 0x1ac
+  __TEXT.__const: 0x12
+  __TEXT.__oslogstring: 0x14a
+  __TEXT.__unwind_info: 0x198
+  __DATA_CONST.__const: 0x480
+  __DATA_CONST.__cfstring: 0x1a00
   __DATA_CONST.__objc_classlist: 0x20
-  __DATA_CONST.__objc_protolist: 0xe8
+  __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x38
+  __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA.__objc_const: 0xf68
-  __DATA.__objc_selrefs: 0x638
-  __DATA.__objc_ivar: 0x20
+  __DATA_CONST.__auth_got: 0x128
+  __DATA_CONST.__got: 0x88
+  __DATA.__objc_const: 0xd68
+  __DATA.__objc_selrefs: 0x538
+  __DATA.__objc_ivar: 0x10
   __DATA.__objc_data: 0x140
-  __DATA.__data: 0xea8
+  __DATA.__data: 0xe48
   __DATA.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  UUID: 41ECC3BD-60C5-30D1-B8D1-A2B56E0A8B62
-  Functions: 83
-  Symbols:   84
-  CStrings:  763
+  UUID: BE3EE6FC-BFDD-3330-A6A3-AC59AF661B97
+  Functions: 59
+  Symbols:   75
+  CStrings:  709
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x8
- _OBJC_CLASS_$_NSBundle
- _OBJC_CLASS_$_NSMutableArray
- __dispatch_main_q
- __os_feature_enabled_impl
- _notify_cancel
- _notify_is_valid_token
- _notify_register_dispatch
- _objc_release_x23
- _objc_retain
- _objc_retainAutorelease
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x21
- _objc_retain_x26
CStrings:
+ "PartnerReferralService"
+ "cachePartnerReferral:reply:"
+ "currentPartnerReferralsWithReply:"
+ "phase"
+ "presentManageSubscriptionsSheetWithRequest:reply:"
+ "presentOfferCodeRedemptionSheetWithRequest:reply:"
+ "presentTransactionRefundRequestSheetWithRequest:reply:"
+ "purchaseResult"
+ "refreshUnifiedAppReceipt:reply:"
+ "storeKitAPI"
+ "v32@0:8@\"NSData\"16@?<v@?@\"NSString\"@\"NSError\">24"
- "%{public}@ Not registering for unfinished transaction notifications because no bundle ID was available"
- "%{public}@: Error getting unfinished transactions: %{public}@"
- "%{public}@: Error in remote proxy getting unfinished transactions: %{public}@"
- "LegacyProductService"
- "SKStatusReceiverProtocol"
- "StoreKit"
- "UTF8String"
- "UseTransactionCacheManager"
- "_cancelNotifyTokenIfValid:"
- "_handleUnfinishedTransactionsNotification"
- "_receivedPurchaseIntentsToken"
- "_subscriptionStatusListeners"
- "_transactionListeners"
- "_unfinishedTransactionsNotificationName"
- "_unfinishedTransactionsToken"
- "appTransactionForClient:ignoreCache:reply:"
- "array"
- "bundleIdentifier"
- "checkServerQueueForClientIfNecessary:forceCheck:reply:"
- "checkServerQueueForQueue:withClient:"
- "dealloc"
- "enumerateCurrentReceiptsForClient:productID:withReceiver:skipTransactionSync:reply:"
- "enumerateReceiptsForClient:productID:withReceiver:skipTransactionSync:reply:"
- "enumerateSubscriptionStatusesForClient:withReceiver:skipStatusSync:reply:"
- "enumerateUnfinishedTransactionsForClient:withReceiver:skipTransactionSync:reply:"
- "finishPaymentWithIdentifier:reply:"
- "hasTransactionListener"
- "i"
- "invalidateTransactionsAndStatusCacheWithReply:"
- "legacyAuthenticateAndSyncTransactionsAndStatusWithReply:"
- "length"
- "mainBundle"
- "manageSubscriptionsEngagementRequestWithRequest:reply:"
- "objectForKeyedSubscript:"
- "presentCodeRedemptionSheetWithSceneID:reply:"
- "presentManageSubscriptionsWithRequest:reply:"
- "presentRefundRequestSheetForTransactionID:sceneID:reply:"
- "receivedStatuses:"
- "registerSubscriptionStatusListener:"
- "registerTransactionListener:"
- "removedTransactions:"
- "renewReceiptWithOptions:client:replyBlock:"
- "restoreCompletedTransactionsForUsername:client:reply:"
- "statusForClient:subscriptionGroupID:skipStatusSync:reply:"
- "statusForClient:transactionID:skipStatusSync:reply:"
- "transactionForID:client:skipTransactionSync:reply:"
- "unregisterSubscriptionStatusListener:"
- "unregisterTransactionListener:"
- "updateTransactions:forClient:"
- "updatedTransactions:"
- "v12@?0i8"
- "v20@0:8i16"
- "v24@?0@\"NSArray\"8@\"NSError\"16"
- "v32@0:8@\"ManageSubscriptionsRequest\"16@?<v@?@\"NSData\"@\"NSError\">24"
- "v32@0:8@\"ManageSubscriptionsRequest\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSArray\"16@\"NSDictionary\"24"
- "v32@0:8@\"NSString\"16@\"NSDictionary\"24"
- "v36@0:8@\"NSDictionary\"16B24@?<v@?@\"NSArray\"@\"NSError\">28"
- "v36@0:8@\"NSDictionary\"16B24@?<v@?@\"NSString\"@\"NSError\">28"
- "v36@0:8@16B24@?28"
- "v40@0:8@\"NSDictionary\"16@\"NSDictionary\"24@?<v@?B@\"NSError\">32"
- "v40@0:8@\"NSString\"16@\"NSDictionary\"24@?<v@?@\"NSArray\"@\"NSError\">32"
- "v44@0:8@\"NSDictionary\"16@\"<SKStatusReceiverProtocol>\"24B32@?<v@?@\"NSError\">36"
- "v44@0:8@\"NSDictionary\"16@\"<SKTransactionReceiverProtocol>\"24B32@?<v@?@\"NSError\">36"
- "v44@0:8@\"NSDictionary\"16@\"NSString\"24B32@?<v@?@\"NSDictionary\"@\"NSError\">36"
- "v44@0:8@\"NSString\"16@\"NSDictionary\"24B32@?<v@?@\"NSString\"@\"NSError\">36"
- "v52@0:8@\"NSDictionary\"16@\"NSString\"24@\"<SKTransactionReceiverProtocol>\"32B40@?<v@?@\"NSError\">44"
- "v52@0:8@16@24@32B40@?44"

```
