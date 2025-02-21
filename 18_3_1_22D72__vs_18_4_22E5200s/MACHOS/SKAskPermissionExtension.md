## SKAskPermissionExtension

> `/System/Library/Frameworks/StoreKit.framework/PlugIns/SKAskPermissionExtension.appex/SKAskPermissionExtension`

```diff

-814.2.21.0.0
-  __TEXT.__text: 0x3a34
+814.4.17.0.0
+  __TEXT.__text: 0x3bc4
   __TEXT.__auth_stubs: 0x290
-  __TEXT.__objc_stubs: 0x760
-  __TEXT.__objc_methlist: 0x2a4
-  __TEXT.__cstring: 0xaf8
+  __TEXT.__objc_stubs: 0x780
+  __TEXT.__objc_methlist: 0x964
+  __TEXT.__objc_classname: 0x28a
+  __TEXT.__objc_methname: 0x17ec
+  __TEXT.__objc_methtype: 0xe2f
+  __TEXT.__cstring: 0xb36
   __TEXT.__gcc_except_tab: 0x348
-  __TEXT.__const: 0x18
-  __TEXT.__objc_methname: 0x160e
+  __TEXT.__const: 0x1a
   __TEXT.__oslogstring: 0x23d
-  __TEXT.__objc_classname: 0x1e5
-  __TEXT.__objc_methtype: 0xcad
-  __TEXT.__unwind_info: 0x248
+  __TEXT.__unwind_info: 0x258
   __DATA_CONST.__auth_got: 0x158
   __DATA_CONST.__got: 0xa0
-  __DATA_CONST.__const: 0x4c8
-  __DATA_CONST.__cfstring: 0x1960
-  __DATA_CONST.__objc_classlist: 0x18
-  __DATA_CONST.__objc_protolist: 0xa8
+  __DATA_CONST.__const: 0x538
+  __DATA_CONST.__cfstring: 0x19c0
+  __DATA_CONST.__objc_classlist: 0x20
+  __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x30
+  __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA.__objc_const: 0x1870
-  __DATA.__objc_selrefs: 0x2d8
+  __DATA.__objc_const: 0xed8
+  __DATA.__objc_selrefs: 0x5d8
   __DATA.__objc_ivar: 0x20
-  __DATA.__objc_data: 0xf0
-  __DATA.__data: 0xb78
+  __DATA.__objc_data: 0x140
+  __DATA.__data: 0xdd0
   __DATA.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/AskPermission.framework/AskPermission
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 85
-  Symbols:   76
-  CStrings:  523
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 90
+  Symbols:   92
+  CStrings:  549
 
Symbols:
+ _OBJC_CLASS_$_XPCInterface
+ _OBJC_METACLASS_$_XPCInterface
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftDarwin
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
CStrings:
+ "AccountService"
+ "AppTransactionCacheService"
+ "AppTransactionReceiverProtocol"
+ "OfferEligibilityService"
+ "SubscriptionStatusCacheService"
+ "T@\"NSString\",R,N"
+ "T@\"NSXPCInterface\",R,N"
+ "TransactionCacheService"
+ "XPCInterface"
+ "account:reply:"
+ "advancedCommerceData"
+ "appTransactionCacheServiceWithErrorHandler:"
+ "authenticate:reply:"
+ "clearCacheWithReply:"
+ "client"
+ "developerErrorCode"
+ "developerErrorMessage"
+ "enumerateCurrentReceiptsForClient:productID:withReceiver:skipTransactionSync:reply:"
+ "enumerateReceiptsForClient:productID:withReceiver:skipTransactionSync:reply:"
+ "enumerateSubscriptionStatusesForClient:withReceiver:skipStatusSync:reply:"
+ "enumerateUnfinishedTransactionsForClient:withReceiver:skipTransactionSync:reply:"
+ "executeAppTransactionQuery:withReceiver:ignoreCache:reply:"
+ "executeSubscriptionStatusQuery:withReceiver:skipStatusSync:reply:"
+ "executeTransactionQuery:withReceiver:skipTransactionSync:reply:"
+ "offerEligibilityServiceWithErrorHandler:"
+ "receivedAppTransaction:"
+ "service"
+ "serviceName"
+ "statusForClient:subscriptionGroupID:skipStatusSync:reply:"
+ "subscriptionStatusCacheServiceWithErrorHandler:"
+ "transactionCacheServiceWithErrorHandler:"
+ "v44@0:8@\"NSData\"16@\"<AppTransactionReceiverProtocol>\"24B32@?<v@?@\"NSError\">36"
+ "v44@0:8@\"NSData\"16@\"<SKStatusReceiverProtocol>\"24B32@?<v@?@\"NSError\">36"
+ "v44@0:8@\"NSData\"16@\"<SKTransactionReceiverProtocol>\"24B32@?<v@?@\"NSError\">36"
+ "v44@0:8@\"NSDictionary\"16@\"<SKStatusReceiverProtocol>\"24B32@?<v@?@\"NSError\">36"
+ "v44@0:8@\"NSDictionary\"16@\"<SKTransactionReceiverProtocol>\"24B32@?<v@?@\"NSError\">36"
+ "v44@0:8@\"NSDictionary\"16@\"NSString\"24B32@?<v@?@\"NSDictionary\"@\"NSError\">36"
+ "v52@0:8@\"NSDictionary\"16@\"NSString\"24@\"<SKTransactionReceiverProtocol>\"32B40@?<v@?@\"NSError\">44"
+ "v52@0:8@16@24@32B40@?44"
- "_storeKitClientInterface"
- "_storeKitServiceInterface"
- "enumerateCurrentReceiptsForProductID:withReceiver:reply:"
- "enumerateReceiptsForProductID:withReceiver:reply:"
- "enumerateSubscriptionStatusesWithReceiver:reply:"
- "enumerateUnfinishedTransactionsWithReceiver:reply:"
- "overrideServiceWithErrorHandler:"
- "overrideSynchronousServiceWithErrorHandler:"
- "statusForSubscriptionGroupID:reply:"
- "storefrontServiceWithErrorHandler:"
- "v32@0:8@\"<SKStatusReceiverProtocol>\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"<SKTransactionReceiverProtocol>\"16@?<v@?@\"NSError\">24"
- "v40@0:8@\"NSString\"16@\"<SKTransactionReceiverProtocol>\"24@?<v@?@\"NSError\">32"

```
