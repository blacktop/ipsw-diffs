## CallHistory

> `/System/Library/PrivateFrameworks/CallHistory.framework/CallHistory`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__eh_frame`
- `__TEXT.__objc_classname`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-  __TEXT.__text: 0x1c2568
+  __TEXT.__text: 0x1c2dd0
   __TEXT.__auth_stubs: 0x2560
-  __TEXT.__objc_methlist: 0x3a8c
-  __TEXT.__const: 0x1e618
-  __TEXT.__cstring: 0x4194
-  __TEXT.__oslogstring: 0x5f49
-  __TEXT.__gcc_except_tab: 0x854
+  __TEXT.__objc_methlist: 0x3acc
+  __TEXT.__const: 0x1e628
+  __TEXT.__cstring: 0x41c4
+  __TEXT.__oslogstring: 0x6159
+  __TEXT.__gcc_except_tab: 0x884
   __TEXT.__dlopen_cstrs: 0x147
   __TEXT.__swift5_typeref: 0x52c1
   __TEXT.__swift5_reflstr: 0x6fb0

   __TEXT.__swift_as_ret: 0xd4
   __TEXT.__swift5_capture: 0x3c8
   __TEXT.__swift5_mpenum: 0x14
-  __TEXT.__unwind_info: 0x6730
+  __TEXT.__unwind_info: 0x6738
   __TEXT.__eh_frame: 0x7b78
   __TEXT.__objc_classname: 0x19ef
-  __TEXT.__objc_methname: 0xa271
-  __TEXT.__objc_methtype: 0x12ef
-  __TEXT.__objc_stubs: 0x7c00
-  __DATA_CONST.__got: 0x9f8
-  __DATA_CONST.__const: 0x1540
+  __TEXT.__objc_methname: 0xa42a
+  __TEXT.__objc_methtype: 0x1349
+  __TEXT.__objc_stubs: 0x7ca0
+  __DATA_CONST.__got: 0xa00
+  __DATA_CONST.__const: 0x1560
   __DATA_CONST.__objc_classlist: 0x468
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2558
+  __DATA_CONST.__objc_selrefs: 0x2590
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x140
   __AUTH_CONST.__auth_got: 0x12c0
   __AUTH_CONST.__const: 0x4f78
-  __AUTH_CONST.__cfstring: 0x37e0
-  __AUTH_CONST.__objc_const: 0x14e98
+  __AUTH_CONST.__cfstring: 0x3800
+  __AUTH_CONST.__objc_const: 0x14ec8
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH.__objc_data: 0x1c50
   __AUTH.__data: 0x14d48
-  __DATA.__objc_ivar: 0x2c4
+  __DATA.__objc_ivar: 0x2c8
   __DATA.__data: 0x4480
   __DATA.__bss: 0x1a730
   __DATA.__common: 0xc0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 12397
-  Symbols:   5898
-  CStrings:  2988
+  Functions: 12410
+  Symbols:   5911
+  CStrings:  3011
 
Symbols:
+ +[CHPersistentStoreDescription persistentStoreDescriptionWithURL:processHandle:error:]
+ +[DBManager persistentStoreOptionsWithURL:isEncrypted:error:]
+ -[CallDBManagerClient _createDatabaseIsPermanent:afterSyncHelperDidSucceed:]
+ -[CallDBManagerClient _createDatabaseIsPermanent:atLocation:shouldRetry:shouldSetChangeReason:]
+ -[CallDBManagerClient _didValidateDatabaseIsPermanent:atLocation:]
+ -[CallDBManagerClient helperConnectionFactory]
+ -[CallDBManagerClient initWithProcessHandle:metaInfoProvider:databaseLocationProvider:helperConnectionFactory:]
+ -[CallDBManagerClient setHelperConnectionFactory:]
+ GCC_except_table12
+ GCC_except_table23
+ _OBJC_CLASS_$_NSError
+ _OBJC_IVAR_$_CallDBManagerClient._helperConnectionFactory
+ ___111-[CallDBManagerClient initWithProcessHandle:metaInfoProvider:databaseLocationProvider:helperConnectionFactory:]_block_invoke
+ ___111-[CallDBManagerClient initWithProcessHandle:metaInfoProvider:databaseLocationProvider:helperConnectionFactory:]_block_invoke_2
+ ___block_descriptor_32_e22_"NSXPCConnection"8?0l
+ _objc_msgSend$_createDatabaseIsPermanent:afterSyncHelperDidSucceed:
+ _objc_msgSend$_createDatabaseIsPermanent:atLocation:shouldRetry:shouldSetChangeReason:
+ _objc_msgSend$_didValidateDatabaseIsPermanent:atLocation:
+ _objc_msgSend$errorWithDomain:code:userInfo:
+ _objc_msgSend$helperConnectionFactory
+ _objc_msgSend$initWithProcessHandle:metaInfoProvider:databaseLocationProvider:helperConnectionFactory:
+ _objc_msgSend$persistentStoreDescriptionWithURL:processHandle:error:
+ _objc_msgSend$persistentStoreOptionsWithURL:isEncrypted:error:
- +[CHPersistentStoreDescription persistentStoreDescriptionWithURL:]
- +[DBManager persistentStoreOptionsWithURL:isEncrypted:]
- -[CallDBManagerClient _createDatabaseIsPermanent:]
- GCC_except_table19
- _OUTLINED_FUNCTION_9
- ___45-[CallDBManagerClient initWithProcessHandle:]_block_invoke
- ___87-[CallDBManagerClient initWithProcessHandle:metaInfoProvider:databaseLocationProvider:]_block_invoke
- _objc_msgSend$_createDatabaseIsPermanent:
- _objc_msgSend$persistentStoreDescriptionWithURL:
- _objc_msgSend$persistentStoreOptionsWithURL:isEncrypted:
CStrings:
+ "106.700.62"
+ "106.700.62~19"
+ "@\"NSXPCConnection\"8@?0"
+ "@36@0:8@16B24^@28"
+ "@48@0:8@16@?24@32@?40"
+ "Call History access requires data store access entitlement %@ or %@. This will be a hard error in the future."
+ "Call History access requires data vault entitlement %@"
+ "Client is missing the %@ and %@ entitlements (in future, one of these will be required)"
+ "Data store (permanent:%{public}i) metadata valid but database validation failed with code %{public}@"
+ "Database (permanent:%{public}i) file doesn't exist"
+ "Database (permanent:%{public}i) validation failed"
+ "Failed to get persistent store options for destination data store, with error %{public}@"
+ "Failed to get persistent store options for source data store: %{public}@, with error %{public}@"
+ "Failed to get persistent store options to add data store, with error %{public}@"
+ "Poking sync helper for data store (permanent:%{public}i)"
+ "T@\"NSXPCConnection\",&,N,V_helperConnection"
+ "T@,&,N,V_syncHelperReadyNotificationRef"
+ "T@?,C,N,V_helperConnectionFactory"
+ "TQ,N,V_interruptionRetryCount"
+ "Will not poke sync helper for data store (permanent:%{public}i); client lacks sufficient access"
+ "_createDatabaseIsPermanent:afterSyncHelperDidSucceed:"
+ "_createDatabaseIsPermanent:atLocation:shouldRetry:shouldSetChangeReason:"
+ "_didValidateDatabaseIsPermanent:atLocation:"
+ "_helperConnectionFactory"
+ "com.apple.private.CallHistory"
+ "createDatabase client (permanent:%{public}i) (syncHelperDidSucceed:%{public}i)"
+ "errorWithDomain:code:userInfo:"
+ "helperConnectionFactory"
+ "initWithProcessHandle:metaInfoProvider:databaseLocationProvider:helperConnectionFactory:"
+ "persistentStoreDescriptionWithURL:processHandle:error:"
+ "persistentStoreOptionsWithURL:isEncrypted:error:"
+ "setHelperConnectionFactory:"
+ "v24@0:8B16B20"
+ "v28@0:8B16@20"
+ "v44@0:8B16@20^B28^B36"
- "106.700.42"
- "106.700.42~46"
- "Call History access requires boolean entitlement %@ or %@. This will be a hard error in the future."
- "Database (permanent:%{public}i) file doesn't exist; poking sync helper. Error code: %{public}@"
- "Database (permanent:%{public}i) metadata valid but data store check failed with code: %{public}@; poking sync helper"
- "Database (permanent:%{public}i) validation failed, poking sync helper"
- "T@\"NSXPCConnection\",&,V_helperConnection"
- "T@,&,V_syncHelperReadyNotificationRef"
- "TQ,V_interruptionRetryCount"
- "_createDatabaseIsPermanent:"
- "createDatabase client (permanent:%{public}i)"
- "persistentStoreOptionsWithURL:isEncrypted:"
```
