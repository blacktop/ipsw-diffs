## SKAskPermissionExtension

> `/System/Library/Frameworks/StoreKit.framework/Versions/A/PlugIns/SKAskPermissionExtension.appex/Contents/MacOS/SKAskPermissionExtension`

```diff

-814.2.21.0.0
-  __TEXT.__text: 0x3c0c
+814.4.24.1.3
+  __TEXT.__text: 0x3dc4
   __TEXT.__auth_stubs: 0x1e0
-  __TEXT.__objc_stubs: 0x740
-  __TEXT.__objc_methlist: 0x28c
-  __TEXT.__cstring: 0xafc
+  __TEXT.__objc_stubs: 0x760
+  __TEXT.__objc_methlist: 0x984
+  __TEXT.__objc_classname: 0x2a5
+  __TEXT.__objc_methname: 0x1873
+  __TEXT.__objc_methtype: 0xe7b
+  __TEXT.__cstring: 0xb3a
   __TEXT.__gcc_except_tab: 0x2f4
-  __TEXT.__const: 0x18
-  __TEXT.__objc_methname: 0x1699
+  __TEXT.__const: 0x1a
   __TEXT.__oslogstring: 0x23d
-  __TEXT.__objc_classname: 0x1fe
-  __TEXT.__objc_methtype: 0xcf9
-  __TEXT.__unwind_info: 0x240
+  __TEXT.__unwind_info: 0x250
   __DATA_CONST.__auth_got: 0x100
   __DATA_CONST.__got: 0xa0
-  __DATA_CONST.__const: 0x4f0
-  __DATA_CONST.__cfstring: 0x1960
-  __DATA_CONST.__objc_classlist: 0x18
-  __DATA_CONST.__objc_protolist: 0xb0
+  __DATA_CONST.__const: 0x568
+  __DATA_CONST.__cfstring: 0x19c0
+  __DATA_CONST.__objc_classlist: 0x20
+  __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x30
+  __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA.__objc_const: 0x18e8
-  __DATA.__objc_selrefs: 0x2c8
+  __DATA.__objc_const: 0xef8
+  __DATA.__objc_selrefs: 0x5f0
   __DATA.__objc_ivar: 0x20
-  __DATA.__objc_data: 0xf0
-  __DATA.__data: 0xbd8
+  __DATA.__objc_data: 0x140
+  __DATA.__data: 0xe30
   __DATA.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /System/Library/PrivateFrameworks/AskPermission.framework/Versions/A/AskPermission
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D7FFDE3E-EEFF-3DA3-B421-0BF292DE0A2B
-  Functions: 88
-  Symbols:   65
-  CStrings:  729
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftIOKit.dylib
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
+  UUID: 5D48DEC9-86EF-3EDD-9BDC-F58A7E3BF38D
+  Functions: 93
+  Symbols:   82
+  CStrings:  758
 
Symbols:
+ _OBJC_CLASS_$_XPCInterface
+ _OBJC_METACLASS_$_XPCInterface
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftDarwin
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftIOKit
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
+ "AppTransactionCacheService"
+ "AppTransactionReceiverProtocol"
+ "OfferEligibilityService"
+ "SKAccountService"
+ "SubscriptionStatusCacheService"
+ "T@\"NSString\",R"
+ "T@\"NSXPCInterface\",R"
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
