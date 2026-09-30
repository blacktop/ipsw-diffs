## amsaccountsd

> `/System/Library/PrivateFrameworks/AppleMediaServices.framework/amsaccountsd`

```diff

-9.1.10.0.0
-  __TEXT.__text: 0x20ebf8
+9.1.17.0.0
+  __TEXT.__text: 0x210cb0
   __TEXT.__auth_stubs: 0x3cd0
-  __TEXT.__objc_stubs: 0x97e0
-  __TEXT.__objc_methlist: 0x53fc
-  __TEXT.__const: 0x1b944
-  __TEXT.__objc_classname: 0xe6d
-  __TEXT.__objc_methname: 0xe8a8
-  __TEXT.__oslogstring: 0xd521
-  __TEXT.__objc_methtype: 0x4211
-  __TEXT.__cstring: 0xb0b7
+  __TEXT.__objc_stubs: 0x9a80
+  __TEXT.__objc_methlist: 0x55bc
+  __TEXT.__const: 0x1b964
+  __TEXT.__objc_classname: 0xed7
+  __TEXT.__objc_methname: 0xec21
+  __TEXT.__oslogstring: 0xd9a1
+  __TEXT.__objc_methtype: 0x42c6
+  __TEXT.__cstring: 0xaff7
   __TEXT.__gcc_except_tab: 0xe30
   __TEXT.__dlopen_cstrs: 0x34d
   __TEXT.__swift5_typeref: 0x6cc8
   __TEXT.__swift5_fieldmd: 0x63e4
   __TEXT.__constg_swiftt: 0x52cc
   __TEXT.__swift5_builtin: 0x118
-  __TEXT.__swift5_reflstr: 0x466c
+  __TEXT.__swift5_reflstr: 0x465c
   __TEXT.__swift5_assocty: 0x8f8
   __TEXT.__swift5_protos: 0xa8
   __TEXT.__swift5_proto: 0x16d8
   __TEXT.__swift5_types: 0x67c
-  __TEXT.__swift_as_entry: 0x200
-  __TEXT.__swift5_mpenum: 0x78
   __TEXT.__swift5_capture: 0xa28
+  __TEXT.__swift_as_entry: 0x200
   __TEXT.__swift_as_ret: 0x2a8
+  __TEXT.__swift5_mpenum: 0x78
   __TEXT.__swift5_types2: 0x8
-  __TEXT.__unwind_info: 0x85c0
-  __TEXT.__eh_frame: 0xf6f4
+  __TEXT.__unwind_info: 0x82e0
+  __TEXT.__eh_frame: 0xf6e4
   __DATA_CONST.__auth_got: 0x1e78
-  __DATA_CONST.__got: 0x1218
-  __DATA_CONST.__auth_ptr: 0xc98
-  __DATA_CONST.__const: 0x121b8
-  __DATA_CONST.__cfstring: 0x3fc0
-  __DATA_CONST.__objc_classlist: 0x340
+  __DATA_CONST.__got: 0x1220
+  __DATA_CONST.__auth_ptr: 0xcb8
+  __DATA_CONST.__const: 0x12178
+  __DATA_CONST.__cfstring: 0x3fa0
+  __DATA_CONST.__objc_classlist: 0x350
   __DATA_CONST.__objc_catlist: 0x90
-  __DATA_CONST.__objc_protolist: 0x268
+  __DATA_CONST.__objc_protolist: 0x270
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x68
-  __DATA_CONST.__objc_superrefs: 0x190
-  __DATA_CONST.__objc_intobj: 0x90
+  __DATA_CONST.__objc_superrefs: 0x198
+  __DATA_CONST.__objc_intobj: 0xa8
   __DATA_CONST.__linkguard: 0x2c
-  __DATA.__objc_const: 0xadb8
-  __DATA.__objc_selrefs: 0x37a8
-  __DATA.__objc_ivar: 0x33c
-  __DATA.__objc_data: 0x2330
-  __DATA.__data: 0xa160
+  __DATA.__objc_const: 0xb018
+  __DATA.__objc_selrefs: 0x3870
+  __DATA.__objc_ivar: 0x350
+  __DATA.__objc_data: 0x23d0
+  __DATA.__data: 0xa1c0
   __DATA.__bss: 0x2d410
   __DATA.__common: 0x190
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 864EDC0A-1A38-3219-87BD-A75A25231B4B
-  Functions: 13172
-  Symbols:   1866
-  CStrings:  5376
+  UUID: AEF89EC9-A3E8-3F4E-A530-8B0EB95A97F1
+  Functions: 13203
+  Symbols:   1867
+  CStrings:  5433
 
Symbols:
+ _OBJC_CLASS_$_NSUserDefaults
CStrings:
+ "#"
+ "%{public}@Attempted to setup the database subscription too many times. Refusing to try again."
+ "%{public}@Creating database subscription: %{public}@"
+ "%{public}@Daemon startup completed Multi-User Databse Notification Subscriptin check. success = %{public}@ | error = %{public}@"
+ "%{public}@Failed to setup the database subscription. error = %{public}@"
+ "%{public}@Found subscription date for identifier %{public}@: %{public}@"
+ "%{public}@No previous subscription date found for %{public}@. Should renew."
+ "%{public}@No subscription date found for identifier: %{public}@"
+ "%{public}@Resetting all Subscription Dates."
+ "%{public}@Scheduling another attempt to setup the database subscription. timeInterval = %f"
+ "%{public}@Setting up a database subscription. database = %{public}@"
+ "%{public}@Subscription for %{public}@ is still valid. Skipping renewal."
+ "%{public}@Subscription modification completed. saved = %{public}@ | error = %{public}@"
+ "%{public}@Successfully setup the database subscription."
+ "%{public}@Time since last subscription for %{public}@: %.2f seconds. Max age: %.2f seconds. Should renew: %{public}@"
+ "%{public}@Wrote subscription date for identifier: %{public}@"
+ "@\"<AMSDCloudDataSubscriptionStorageProtocol>\""
+ "@\"CKDatabase\""
+ "@\"NSDate\"24@0:8@\"NSString\"16"
+ "AMSCloudDataDatabaseSubscriptionDate"
+ "AMSDCloudDataSubscriptionStorage"
+ "AMSDCloudDataSubscriptionStorageProtocol"
+ "AMSDCloudDataSubscriptionTask"
+ "B32@0:8@\"NSDate\"16@\"NSString\"24"
+ "B32@0:8@16d24"
+ "NO"
+ "T@\"<AMSDCloudDataSubscriptionStorageProtocol>\",&,N,V_storage"
+ "T@\"CKDatabase\",&,N,V_database"
+ "T@\"NSString\",&,N,V_identifier"
+ "TQ,N,V_maxRetries"
+ "Td,N,V_maxAge"
+ "YES"
+ "_maxAge"
+ "_maxRetries"
+ "_performSubscriptionModification:"
+ "_readSubscriptionDateForIdentifier:"
+ "_shouldRenewSubscriptionForIdentifier:"
+ "_shouldRenewSubscriptionForIdentifier:maxAge:"
+ "_storage"
+ "_subscriptionForIdentifier:"
+ "_writeSubscriptionDateForIdentifier:"
+ "initWithDatabase:identifier:"
+ "initWithDatabase:identifier:storage:"
+ "maxAge"
+ "maxRetries"
+ "performRefreshMultiUserDatabaseNotificationSubscriptionsForceRefresh:"
+ "refreshMultiUserDatabaseNotificationSubscriptionsForced:completion:"
+ "resetLastAttemptDate"
+ "resetMultiUserDatabaseNotificationSubscriptionsCompletion:"
+ "resetStorage"
+ "setDatabase:"
+ "setIdentifier:"
+ "setMaxAge:"
+ "setMaxRetries:"
+ "setStorage:"
+ "standardUserDefaults"
+ "storage"
+ "subscriptionDateForIdentifier:"
+ "synchronize"
+ "v28@0:8B16@?20"
+ "v28@0:8B16@?<v@?B@\"NSError\">20"
+ "writeSubscriptionDate:identifier:"
- "Subscribing to private database changes initially failed."
- "Subscribing to shared database changes initially failed."
- "com.apple.amsaccountsd.multiuser.privateDatabaseSubscription"
- "com.apple.amsaccountsd.multiuser.sharedDatabaseSubscription"

```
