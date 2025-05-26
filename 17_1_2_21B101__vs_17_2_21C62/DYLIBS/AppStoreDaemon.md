## AppStoreDaemon

> `/System/Library/PrivateFrameworks/AppStoreDaemon.framework/AppStoreDaemon`

```diff

-10.1.6.0.0
-  __TEXT.__text: 0x74d94
+10.2.8.0.0
+  __TEXT.__text: 0x75ae8
   __TEXT.__auth_stubs: 0xaa0
-  __TEXT.__objc_methlist: 0x8b8c
+  __TEXT.__objc_methlist: 0x8cb4
   __TEXT.__const: 0x90
-  __TEXT.__cstring: 0x4f70
-  __TEXT.__oslogstring: 0x3f6a
+  __TEXT.__cstring: 0x4f94
+  __TEXT.__oslogstring: 0x4056
   __TEXT.__gcc_except_tab: 0x960
   __TEXT.__dlopen_cstrs: 0xb1
-  __TEXT.__unwind_info: 0x22a8
-  __TEXT.__objc_classname: 0x1715
-  __TEXT.__objc_methname: 0x11eeb
-  __TEXT.__objc_methtype: 0x292b
-  __TEXT.__objc_stubs: 0x7de0
+  __TEXT.__unwind_info: 0x22dc
+  __TEXT.__objc_classname: 0x17ea
+  __TEXT.__objc_methname: 0x12954
+  __TEXT.__objc_methtype: 0x2f44
+  __TEXT.__objc_stubs: 0x7fa0
   __DATA_CONST.__got: 0x118
-  __DATA_CONST.__const: 0x2508
-  __DATA_CONST.__objc_classlist: 0x5a8
+  __DATA_CONST.__const: 0x2558
+  __DATA_CONST.__objc_classlist: 0x5b0
   __DATA_CONST.__objc_catlist: 0x48
-  __DATA_CONST.__objc_protolist: 0x1d8
+  __DATA_CONST.__objc_protolist: 0x208
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x106a8
-  __DATA_CONST.__objc_selrefs: 0x3ba0
+  __DATA_CONST.__objc_const: 0x110c8
+  __DATA_CONST.__objc_selrefs: 0x3c60
   __DATA_CONST.__objc_arraydata: 0xc8
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__objc_const: 0x5a38
-  __AUTH_CONST.__cfstring: 0x6280
-  __AUTH_CONST.__const: 0x6e0
+  __AUTH_CONST.__objc_const: 0x5ac8
+  __AUTH_CONST.__cfstring: 0x62e0
+  __AUTH_CONST.__const: 0x740
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x560
-  __AUTH.__objc_data: 0x1860
-  __DATA.__objc_protorefs: 0x130
-  __DATA.__objc_classrefs: 0x580
+  __AUTH.__objc_data: 0x18b0
+  __DATA.__objc_protorefs: 0x140
+  __DATA.__objc_classrefs: 0x590
   __DATA.__objc_superrefs: 0x458
   __DATA.__objc_ivar: 0xc0c
-  __DATA.__data: 0x1638
+  __DATA.__data: 0x1878
   __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_ivar: 0x1ac
   __DATA_DIRTY.__objc_data: 0x2030
   __DATA_DIRTY.__data: 0x50
-  __DATA_DIRTY.__bss: 0x258
+  __DATA_DIRTY.__bss: 0x270
   __DATA_DIRTY.__common: 0x150
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3902
-  Symbols:   12205
-  CStrings:  5071
+  Functions: 3932
+  Symbols:   12327
+  CStrings:  5192
 
Symbols:
+ +[StoreKitService _serviceConnectionInvalidated]
+ +[StoreKitService _serviceConnection]
+ +[StoreKitService _storeKitClientInterface]
+ +[StoreKitService _storeKitServiceInterface]
+ +[StoreKitService processStoreKitPurchase:withResultHandler:]
+ +[StoreKitService shouldProcessStoreKitPurchase:]
+ +[StoreKitService storeKitServiceWithErrorHandler:]
+ -[StoreKitService askToShowMessageWithReplyBlock:]
+ -[StoreKitService downloadAdded:]
+ -[StoreKitService downloadRemoved:]
+ -[StoreKitService downloadStatusChanged:]
+ -[StoreKitService handleAuthenticateRequest:resultHandler:]
+ -[StoreKitService handleDialogRequest:resultHandler:]
+ -[StoreKitService handleEngagementRequest:resultHandler:]
+ -[StoreKitService hasAnyMessageListenersWithReply:]
+ -[StoreKitService pendingMessages:]
+ -[StoreKitService receivedStatuses:]
+ -[StoreKitService receivedTransactions:]
+ -[StoreKitService removedEntitlementsForProductIdentifiers:]
+ -[StoreKitService removedTransactions:]
+ -[StoreKitService shouldContinueTransaction:withNewStorefront:replyBlock:]
+ -[StoreKitService storefrontChanged:]
+ -[StoreKitService updatedTransactions:]
+ _OBJC_CLASS_$_AMSBuyParams
+ _OBJC_CLASS_$_StoreKitService
+ _OBJC_METACLASS_$_StoreKitService
+ __OBJC_$_CLASS_METHODS_StoreKitService
+ __OBJC_$_INSTANCE_METHODS_StoreKitService
+ __OBJC_$_PROP_LIST_StoreKitService
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ASDNotificationCenterDialogObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ASDStoreKitClientProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ASDStoreKitMessageReceiverProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ASDStoreKitServiceProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ASDStoreKitStatusReceiverProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ASDStoreKitTransactionReceiverProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_ASDNotificationCenterDialogObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ASDNotificationCenterDialogObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ASDStoreKitClientProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ASDStoreKitMessageReceiverProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ASDStoreKitServiceProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ASDStoreKitStatusReceiverProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ASDStoreKitTransactionReceiverProtocol
+ __OBJC_$_PROTOCOL_REFS_ASDNotificationCenterDialogObserver
+ __OBJC_$_PROTOCOL_REFS_ASDStoreKitClientProtocol
+ __OBJC_$_PROTOCOL_REFS_ASDStoreKitMessageReceiverProtocol
+ __OBJC_$_PROTOCOL_REFS_ASDStoreKitServiceProtocol
+ __OBJC_$_PROTOCOL_REFS_ASDStoreKitStatusReceiverProtocol
+ __OBJC_$_PROTOCOL_REFS_ASDStoreKitTransactionReceiverProtocol
+ __OBJC_CLASS_PROTOCOLS_$_StoreKitService
+ __OBJC_CLASS_RO_$_StoreKitService
+ __OBJC_LABEL_PROTOCOL_$_ASDNotificationCenterDialogObserver
+ __OBJC_LABEL_PROTOCOL_$_ASDStoreKitClientProtocol
+ __OBJC_LABEL_PROTOCOL_$_ASDStoreKitMessageReceiverProtocol
+ __OBJC_LABEL_PROTOCOL_$_ASDStoreKitServiceProtocol
+ __OBJC_LABEL_PROTOCOL_$_ASDStoreKitStatusReceiverProtocol
+ __OBJC_LABEL_PROTOCOL_$_ASDStoreKitTransactionReceiverProtocol
+ __OBJC_METACLASS_RO_$_StoreKitService
+ __OBJC_PROTOCOL_$_ASDNotificationCenterDialogObserver
+ __OBJC_PROTOCOL_$_ASDStoreKitClientProtocol
+ __OBJC_PROTOCOL_$_ASDStoreKitMessageReceiverProtocol
+ __OBJC_PROTOCOL_$_ASDStoreKitServiceProtocol
+ __OBJC_PROTOCOL_$_ASDStoreKitStatusReceiverProtocol
+ __OBJC_PROTOCOL_$_ASDStoreKitTransactionReceiverProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_ASDStoreKitClientProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_ASDStoreKitServiceProtocol
+ ___37+[StoreKitService _serviceConnection]_block_invoke
+ ___37+[StoreKitService _serviceConnection]_block_invoke_2
+ ___37+[StoreKitService _serviceConnection]_block_invoke_3
+ ___51+[StoreKitService storeKitServiceWithErrorHandler:]_block_invoke
+ ___54-[ASDPurchaseManager startPurchase:withResultHandler:]_block_invoke_4
+ ___61+[StoreKitService processStoreKitPurchase:withResultHandler:]_block_invoke
+ ___61+[StoreKitService processStoreKitPurchase:withResultHandler:]_block_invoke.16
+ ___block_descriptor_48_e8_32bs_e17_v16?0"NSError"8ls32l8
+ ___block_descriptor_48_e8_32bs_e34_v24?0"NSDictionary"8"NSError"16ls32l8
+ ___block_literal_global.23
+ ___block_literal_global.25
+ _objc_msgSend$_serviceConnection
+ _objc_msgSend$_serviceConnectionInvalidated
+ _objc_msgSend$_storeKitClientInterface
+ _objc_msgSend$_storeKitServiceInterface
+ _objc_msgSend$buyParameters
+ _objc_msgSend$buyParamsWithString:
+ _objc_msgSend$initWithSuccess:error:
+ _objc_msgSend$parameterForKey:
+ _objc_msgSend$processPaymentWithBuyParamsString:reply:
+ _objc_msgSend$processStoreKitPurchase:withResultHandler:
+ _objc_msgSend$setParameter:forKey:
+ _objc_msgSend$shouldProcessStoreKitPurchase:
+ _objc_msgSend$storeKitServiceWithErrorHandler:
+ _objc_msgSend$vendorName
CStrings:
+ "ASDNotificationCenterDialogObserver"
+ "ASDStoreKitClientProtocol"
+ "ASDStoreKitMessageReceiverProtocol"
+ "ASDStoreKitServiceProtocol"
+ "ASDStoreKitStatusReceiverProtocol"
+ "ASDStoreKitTransactionReceiverProtocol"
+ "StoreKitService"
+ "[%{public}@] Processing ASDPurchase with StoreKit service"
+ "[%{public}@]: Error in StoreKit service - %@"
+ "[%{public}@]: Error processing ASDPurchase with StoreKit service - %@"
+ "[%{public}@]: StoreKit service finished processing ASDPurchase"
+ "_serviceConnection"
+ "_serviceConnectionInvalidated"
+ "_storeKitClientInterface"
+ "_storeKitServiceInterface"
+ "addDownloadWithID:"
+ "addPurchaseIntent:reply:"
+ "appTransactionForClient:ignoreCache:reply:"
+ "arcadeSubscriptionStatusWithNonce:resultHandler:"
+ "askToShowMessageWithReplyBlock:"
+ "authenticateAndSyncTransactionsAndStatusWithReply:"
+ "bid"
+ "buyParamsWithString:"
+ "canOpenGatewayWithReply:"
+ "cancelDownloadWithID:"
+ "checkForMessages"
+ "checkServerQueueForClientIfNecessary:forceCheck:reply:"
+ "checkServerQueueForQueue:withClient:"
+ "com.apple.storekitd"
+ "deleteContentForProductID:"
+ "displayMessageWithType:"
+ "downloadAdded:"
+ "downloadRemoved:"
+ "downloadStatusChanged:"
+ "engagementRequestForOfferCodeRedemptionSheetWithReply:"
+ "enumerateCurrentReceiptsForProductID:withReceiver:reply:"
+ "enumerateReceiptsForProductID:withReceiver:reply:"
+ "enumerateUnfinishedTransactionsWithReceiver:reply:"
+ "finishPaymentWithIdentifier:"
+ "finishPaymentWithIdentifier:reply:"
+ "forceSandboxForBundleIdentifier:untilDate:"
+ "handleInvalidReceipt:"
+ "handlePurchase:resultHandler:"
+ "hasAnyMessageListenersWithReply:"
+ "insertMessageForBundleID:status:useSandboxAccount:allowDeveloperControl:type:reply:"
+ "invalidateTransactionsAndStatusCacheWithReply:"
+ "lookUpItemIDsForDeletableSystemAppsWithBundleIDs:reply:"
+ "manageSubscriptionsRequestWithReply:"
+ "openAlternativeWithReply:"
+ "openGatewayWithReply:"
+ "parameterForKey:"
+ "pauseDownloadWithID:"
+ "pendingMessages:"
+ "presentCodeRedemptionSheet"
+ "processPayment:forClient:paymentDelegate:reply:"
+ "processPaymentWithBuyParamsString:reply:"
+ "processStoreKitPurchase:withResultHandler:"
+ "productType"
+ "promotionInfoForProductIdentifiers:client:reply:"
+ "purchaseIntentAppInstallSheetOpenForBundleIdentifier:reply:"
+ "purchaseIntentsForClient:clearOnRetrieval:reply:"
+ "receivedStatuses:"
+ "receivedTransactions:"
+ "refundRequestForTransactionId:replyBlock:"
+ "registerArcadeAppWithRandomFromLib:randomFromLibLength:resultHandler:"
+ "registerForInstallAttribution"
+ "removedEntitlementsForProductIdentifiers:"
+ "removedTransactions:"
+ "renewReceiptWithOptions:client:replyBlock:"
+ "repairArcadeApp"
+ "requestProductReview"
+ "requestProductsWithIdentifiers:client:replyBlock:"
+ "restoreCompletedTransactionsForUsername:client:reply:"
+ "restoreCompletedTransactionsToQueue:forUsername:withClient:replyBlock:"
+ "resumeDownloadWithID:"
+ "setClientOverrides:forBundleIdentifier:untilDate:reply:"
+ "setParameter:forKey:"
+ "setPromotionInfo:forClient:reply:"
+ "shouldContinueTransaction:withNewStorefront:replyBlock:"
+ "shouldProcessStoreKitPurchase:"
+ "statusForSubscriptionGroupID:reply:"
+ "storeKitServiceWithErrorHandler:"
+ "storefrontChanged:"
+ "storefrontWithReplyBlock:"
+ "updateConversionValue:"
+ "updateConversionValue:completionHandler:"
+ "updatedTransactions:"
+ "useAppStoreDaemonWithReplyBlock:"
+ "v24@0:8@\"NSNumber\"16"
+ "v24@0:8@\"NSString\"16"
+ "v24@0:8@?<v@?@\"NSError\"@\"NSData\">16"
+ "v24@0:8@?<v@?@\"NSString\"@\"NSString\">16"
+ "v24@0:8@?<v@?BB>16"
+ "v24@0:8@?<v@?q>16"
+ "v32@0:8@\"<ASDStoreKitTransactionReceiverProtocol>\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"AMSPurchaseSIWA\"16@?<v@?@\"AMSPurchaseSIWAResult\"@\"NSError\">24"
+ "v32@0:8@\"NSDictionary\"16@?<v@?>24"
+ "v32@0:8@\"NSNumber\"16@?<v@?@\"NSError\"@\"NSData\">24"
+ "v32@0:8@\"NSString\"16@\"NSDate\"24"
+ "v32@0:8@\"NSString\"16@\"NSDictionary\"24"
+ "v32@0:8@\"NSString\"16@?<v@?>24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSDictionary\"@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSError\">24"
+ "v32@0:8Q16@?<v@?@\"NSData\"I@\"NSData\"I@\"NSError\">24"
+ "v36@0:8@\"NSData\"16I24@?<v@?@\"NSData\"I@\"NSData\"I@\"NSError\">28"
+ "v36@0:8@\"NSDictionary\"16B24@?<v@?@\"NSArray\"@\"NSError\">28"
+ "v36@0:8@\"NSDictionary\"16B24@?<v@?@\"NSString\"@\"NSError\">28"
+ "v36@0:8@16I24@?28"
+ "v40@0:8@\"NSArray\"16@\"NSDictionary\"24@?<v@?@\"NSArray\"@\"NSArray\"@\"NSError\">32"
+ "v40@0:8@\"NSDictionary\"16@\"NSDictionary\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"NSDictionary\"16@\"NSDictionary\"24@?<v@?B@\"NSError\">32"
+ "v40@0:8@\"NSSet\"16@\"NSDictionary\"24@?<v@?@\"NSArray\"@\"NSError\">32"
+ "v40@0:8@\"NSString\"16@\"<ASDStoreKitTransactionReceiverProtocol>\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"NSString\"16@\"NSDictionary\"24@?<v@?@\"NSArray\"@\"NSError\">32"
+ "v48@0:8@\"NSDictionary\"16@\"NSDictionary\"24@\"<ASDStoreKitPaymentProtocol>\"32@?<v@?@\"NSDictionary\"@\"NSError\">40"
+ "v48@0:8@\"NSDictionary\"16@\"NSString\"24@\"NSDate\"32@?<v@?@\"NSError\">40"
+ "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSDictionary\"32@?<v@?B@\"NSError\">40"
+ "v56@0:8@\"NSString\"16q24B32B36q40@?<v@?@\"NSError\">48"
+ "v56@0:8@16q24B32B36q40@?48"
+ "xcodeTestCertificatesWithReply:"
+ "xcodeTestServerPortWithReplyBlock:"

```
