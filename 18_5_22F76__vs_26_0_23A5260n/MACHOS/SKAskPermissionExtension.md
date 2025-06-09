## SKAskPermissionExtension

> `/System/Library/Frameworks/StoreKit.framework/PlugIns/SKAskPermissionExtension.appex/SKAskPermissionExtension`

```diff

-814.5.3.0.0
-  __TEXT.__text: 0x3bc4
-  __TEXT.__auth_stubs: 0x290
+815.0.28.0.0
+  __TEXT.__text: 0x3928
+  __TEXT.__auth_stubs: 0x2a0
   __TEXT.__objc_stubs: 0x780
-  __TEXT.__objc_methlist: 0x964
-  __TEXT.__objc_classname: 0x28c
-  __TEXT.__objc_methname: 0x17ec
-  __TEXT.__objc_methtype: 0xe2f
+  __TEXT.__objc_methlist: 0x9d4
+  __TEXT.__objc_classname: 0x2a9
+  __TEXT.__objc_methname: 0x18d7
+  __TEXT.__objc_methtype: 0xf33
   __TEXT.__cstring: 0xb36
   __TEXT.__gcc_except_tab: 0x348
   __TEXT.__const: 0x1a
   __TEXT.__oslogstring: 0x23d
-  __TEXT.__unwind_info: 0x258
-  __DATA_CONST.__auth_got: 0x158
+  __TEXT.__unwind_info: 0x240
+  __DATA_CONST.__auth_got: 0x160
   __DATA_CONST.__got: 0xa0
-  __DATA_CONST.__const: 0x538
+  __DATA_CONST.__const: 0x518
   __DATA_CONST.__cfstring: 0x19c0
   __DATA_CONST.__objc_classlist: 0x20
-  __DATA_CONST.__objc_protolist: 0xd8
+  __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x38
+  __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA.__objc_const: 0xed8
-  __DATA.__objc_selrefs: 0x5d8
+  __DATA.__objc_const: 0xf48
+  __DATA.__objc_selrefs: 0x618
   __DATA.__objc_ivar: 0x20
   __DATA.__objc_data: 0x140
-  __DATA.__data: 0xdd0
+  __DATA.__data: 0xe30
   __DATA.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: A6687B6F-2F00-3969-83A2-4DB4C9BFC855
-  Functions: 90
-  Symbols:   92
-  CStrings:  753
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
+  UUID: A48B5CFE-84E9-307D-930A-0559EB645574
+  Functions: 84
+  Symbols:   89
+  CStrings:  765
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ _objc_release_x24
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd
CStrings:
+ "OfferDisplayEngagementService"
+ "PaymentService"
+ "SKSubscriptionGroupStatusReceiverProtocol"
+ "accountType:reply:"
+ "clientTypeRequest:reply:"
+ "executeSubscriptionStatusQuery:withReceiver:reply:"
+ "executeTransactionQuery:withReceiver:reply:"
+ "finishTransaction:reply:"
+ "legacyRestoreCompletedTransactions:reply:"
+ "legacyUnfinishedTransactions:reply:"
+ "performPurchase:authDelegate:reply:"
+ "processPrivatePaymentWithPaymentDict:client:dialogDelegate:reply:"
+ "processPurchaseResult:reply:"
+ "receivedStatusGroups:"
+ "statusForClient:transactionID:skipStatusSync:reply:"
+ "transactionForID:client:skipTransactionSync:reply:"
+ "v40@0:8@\"NSData\"16@\"<SKDialogProtocol>\"24@?<v@?@\"NSData\"@\"NSError\">32"
+ "v40@0:8@\"NSData\"16@\"<SKSubscriptionGroupStatusReceiverProtocol>\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"NSData\"16@\"<SKTransactionReceiverProtocol>\"24@?<v@?@\"NSError\">32"
+ "v44@0:8@\"NSString\"16@\"NSDictionary\"24B32@?<v@?@\"NSString\"@\"NSError\">36"
+ "v48@0:8@\"NSDictionary\"16@\"Client\"24@\"<SKDialogProtocol>\"32@?<v@?@\"NSDictionary\"@\"NSDictionary\"@\"NSError\">40"
- "AppTransactionCacheService"
- "SubscriptionStatusCacheService"
- "appTransactionCacheServiceWithErrorHandler:"
- "executeSubscriptionStatusQuery:withReceiver:skipStatusSync:reply:"
- "executeTransactionQuery:withReceiver:skipTransactionSync:reply:"
- "subscriptionStatusCacheServiceWithErrorHandler:"
- "transactionCacheServiceWithErrorHandler:"
- "v44@0:8@\"NSData\"16@\"<SKStatusReceiverProtocol>\"24B32@?<v@?@\"NSError\">36"
- "v44@0:8@\"NSData\"16@\"<SKTransactionReceiverProtocol>\"24B32@?<v@?@\"NSError\">36"

```
