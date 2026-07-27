## CallHistory

> `/System/Library/PrivateFrameworks/CallHistory.framework/Versions/A/CallHistory`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__unwind_info`
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

-106.700.42.0.0
-  __TEXT.__text: 0x1c2b7c
+106.700.62.1.1
+  __TEXT.__text: 0x1c31cc
   __TEXT.__auth_stubs: 0x2350
-  __TEXT.__objc_methlist: 0x392c
+  __TEXT.__objc_methlist: 0x396c
   __TEXT.__const: 0x1e4f8
-  __TEXT.__cstring: 0x4186
-  __TEXT.__oslogstring: 0x5fd9
-  __TEXT.__gcc_except_tab: 0x838
+  __TEXT.__cstring: 0x41c6
+  __TEXT.__oslogstring: 0x6159
+  __TEXT.__gcc_except_tab: 0x850
   __TEXT.__dlopen_cstrs: 0xe3
   __TEXT.__swift5_typeref: 0x528d
   __TEXT.__swift5_reflstr: 0x6f80

   __TEXT.__unwind_info: 0x6520
   __TEXT.__eh_frame: 0x7a18
   __TEXT.__objc_classname: 0x196f
-  __TEXT.__objc_methname: 0xa071
-  __TEXT.__objc_methtype: 0x1200
-  __TEXT.__objc_stubs: 0x7b00
-  __DATA_CONST.__got: 0xa00
-  __DATA_CONST.__const: 0x960
+  __TEXT.__objc_methname: 0xa22a
+  __TEXT.__objc_methtype: 0x125a
+  __TEXT.__objc_stubs: 0x7b80
+  __DATA_CONST.__got: 0xa08
+  __DATA_CONST.__const: 0x980
   __DATA_CONST.__objc_classlist: 0x458
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0xc8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2528
+  __DATA_CONST.__objc_selrefs: 0x2560
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x138
   __AUTH_CONST.__auth_got: 0x11b8
   __AUTH_CONST.__const: 0x5a70
-  __AUTH_CONST.__cfstring: 0x36c0
-  __AUTH_CONST.__objc_const: 0x144e8
+  __AUTH_CONST.__cfstring: 0x36e0
+  __AUTH_CONST.__objc_const: 0x14518
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH.__objc_data: 0x1bb0
   __AUTH.__data: 0x14c70
-  __DATA.__objc_ivar: 0x2b0
+  __DATA.__objc_ivar: 0x2b4
   __DATA.__data: 0x4320
   __DATA.__bss: 0x1a680
   __DATA.__common: 0xb0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 12308
-  Symbols:   5869
-  CStrings:  2957
+  Functions: 12317
+  Symbols:   5881
+  CStrings:  2978
 
Symbols:
+ +[CHPersistentStoreDescription persistentStoreDescriptionWithURL:processHandle:error:]
+ +[DBManager persistentStoreOptionsWithURL:isEncrypted:error:]
+ -[CallDBManagerClient _createDatabaseIsPermanent:afterSyncHelperDidSucceed:]
+ -[CallDBManagerClient _createDatabaseIsPermanent:atLocation:shouldRetry:shouldSetChangeReason:]
+ -[CallDBManagerClient _didValidateDatabaseIsPermanent:atLocation:]
+ -[CallDBManagerClient helperConnectionFactory]
+ -[CallDBManagerClient initWithProcessHandle:metaInfoProvider:databaseLocationProvider:helperConnectionFactory:]
+ -[CallDBManagerClient setHelperConnectionFactory:]
+ GCC_except_table11
+ GCC_except_table25
+ OBJC_IVAR_$_CallDBManagerClient._helperConnectionFactory
+ _OBJC_CLASS_$_NSError
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
- GCC_except_table21
- _OUTLINED_FUNCTION_9
- ___45-[CallDBManagerClient initWithProcessHandle:]_block_invoke
- ___87-[CallDBManagerClient initWithProcessHandle:metaInfoProvider:databaseLocationProvider:]_block_invoke
- _objc_msgSend$_createDatabaseIsPermanent:
- _objc_msgSend$hasDataVaultEntitlement
- _objc_msgSend$persistentStoreDescriptionWithURL:
- _objc_msgSend$persistentStoreOptionsWithURL:isEncrypted:
CStrings:
+ "106.700.62.1.1"
+ "106.700.62.1.1~1"
+ "@\"NSXPCConnection\"8@?0"
+ "@36@0:8@16B24^@28"
+ "@48@0:8@16@?24@32@?40"
+ "Call History access requires data store access entitlement %@ or %@. This will be a hard error in the future."
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
- "106.700.42~14"
- "Call History access requires boolean entitlement %@ or %@. This will be a hard error in the future."
- "Database (permanent:%{public}i) file doesn't exist; poking sync helper. Error code: %{public}@"
- "Database (permanent:%{public}i) metadata valid but data store check failed with code: %{public}@; poking sync helper"
- "Database (permanent:%{public}i) validation failed, poking sync helper"
- "Not attempting to create helper connection because we're missing the %@ entitlement"
- "T@\"NSXPCConnection\",&,V_helperConnection"
- "T@,&,V_syncHelperReadyNotificationRef"
- "TQ,V_interruptionRetryCount"
- "_createDatabaseIsPermanent:"
- "createDatabase client (permanent:%{public}i)"
- "persistentStoreOptionsWithURL:isEncrypted:"
```
