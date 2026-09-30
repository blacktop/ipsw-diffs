## CallHistory

> `/System/Library/PrivateFrameworks/CallHistory.framework/Versions/A/CallHistory`

```diff

-55.400.141.0.0
-  __TEXT.__text: 0x3cdf0
+55.500.181.1.1
+  __TEXT.__text: 0x3d330
   __TEXT.__auth_stubs: 0x5f0
-  __TEXT.__objc_methlist: 0x2cd8
-  __TEXT.__const: 0x338
-  __TEXT.__cstring: 0x2242
-  __TEXT.__oslogstring: 0x4b20
-  __TEXT.__gcc_except_tab: 0x6c4
+  __TEXT.__objc_methlist: 0x338c
+  __TEXT.__const: 0x358
+  __TEXT.__cstring: 0x226b
+  __TEXT.__oslogstring: 0x4bd4
+  __TEXT.__gcc_except_tab: 0x6e8
   __TEXT.__dlopen_cstrs: 0x95
-  __TEXT.__unwind_info: 0xe80
+  __TEXT.__unwind_info: 0xed8
   __TEXT.__eh_frame: 0x50
   __TEXT.__objc_classname: 0x5e7
-  __TEXT.__objc_methname: 0x8822
-  __TEXT.__objc_methtype: 0x1052
-  __TEXT.__objc_stubs: 0x6aa0
+  __TEXT.__objc_methname: 0x88ea
+  __TEXT.__objc_methtype: 0x1065
+  __TEXT.__objc_stubs: 0x6ac0
   __DATA_CONST.__got: 0x380
-  __DATA_CONST.__const: 0x680
+  __DATA_CONST.__const: 0x688
   __DATA_CONST.__objc_classlist: 0x1a8
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2040
+  __DATA_CONST.__objc_selrefs: 0x20f8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x128
   __AUTH_CONST.__auth_got: 0x308
   __AUTH_CONST.__const: 0xe80
-  __AUTH_CONST.__cfstring: 0x2800
-  __AUTH_CONST.__objc_const: 0x8ea8
+  __AUTH_CONST.__cfstring: 0x2820
+  __AUTH_CONST.__objc_const: 0x8320
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH.__objc_data: 0x5f0
-  __DATA.__objc_ivar: 0x288
+  __DATA.__objc_ivar: 0x28c
   __DATA.__data: 0x8a8
   __DATA.__bss: 0x118
   __DATA.__common: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E9D17382-A2BB-31FA-A156-7CAA34285D5F
-  Functions: 1309
-  Symbols:   3540
-  CStrings:  2732
+  UUID: E4E2CA80-CC18-3003-97C1-F4EABAFF0FE0
+  Functions: 1327
+  Symbols:   3560
+  CStrings:  2743
 
Symbols:
+ +[CHDatabaseClientHandleManager sharedInstance].cold.1
+ +[CHHandle normalizedHandleWithType:value:isoCountryCode:]
+ +[CHLogServer sharedInstance].cold.1
+ +[CHSharedAddressBook get].cold.1
+ +[CHUserConfiguration registeredDefaults].cold.1
+ +[CallHistoryDBHandle objectId].cold.1
+ +[DBManager getManagedObjectModelFromDB:orModelURL:orMetadata:]
+ -[CHProcessHandle hasCloudSyncEntitlement]
+ -[CallDBManagerClient createPermanent].cold.2
+ -[CallDBManagerClient createPermanent].cold.3
+ -[CallDBManagerClient createTemporary].cold.2
+ -[CallDBManagerClient currentProcessHandle]
+ -[CallDBManagerClient initWithProcessHandle:]
+ -[CallDBManagerClient setCurrentProcessHandle:]
+ CHGetRootVersionString.cold.1
+ CHGetUserCallHistoryDataStoreClassCFileURL.cold.1
+ CHGetUserCallHistoryDataStoreClassDFileURL.cold.1
+ CHGetUserCallHistoryDataStoreDirectoryURL.cold.1
+ OBJC_IVAR_$_CallDBManagerClient._currentProcessHandle
+ _CHCloudSyncEntitlement
+ __45-[CallDBManagerClient createHelperConnection]_block_invoke.64
+ __45-[CallDBManagerClient createHelperConnection]_block_invoke.64.cold.1
+ __45-[CallDBManagerClient createHelperConnection]_block_invoke.cold.2
+ _objc_msgSend$currentProcessHandle
+ _objc_msgSend$getManagedObjectModelFromDB:orModelURL:orMetadata:
+ _objc_msgSend$hasCloudSyncEntitlement
+ ch_framework_log.cold.1
+ ch_security_log.cold.1
+ getSharedGEOPhoneNumberResolver.cold.1
+ isInternalBuild.cold.1
+ maybeLogVersionInfo.cold.1
+ userDataEncryptionKey.cold.1
- +[DBManager getManagedObjectModelFromDB:orModelURL:]
- +[DBManager modelForDBMetadata:]
- +[DBManager modelForDBMetadata:].cold.1
- GCC_except_table12
- GCC_except_table6
- _OUTLINED_FUNCTION_5
- __45-[CallDBManagerClient createHelperConnection]_block_invoke.61
- __45-[CallDBManagerClient createHelperConnection]_block_invoke.61.cold.1
- _objc_msgSend$getManagedObjectModelFromDB:orModelURL:
- _objc_msgSend$modelForDBMetadata:
CStrings:
+ "55.500.181.1.1"
+ "55.500.181.1.1~5"
+ "@\"CHProcessHandle\""
+ "Attempting to reconnect to the SyncHelper"
+ "Couldn't get managedObjectModel from db at %{public}@, model at %{public}@, or metadata %{public}@: %{public}@"
+ "Not attempting to reconnect to the SyncHelper because we're missing the %@ entitlement"
+ "Permanent database file doesn't exist; poking sync helper. Error code: %{public}@"
+ "T@\"CHProcessHandle\",&,N,V_currentProcessHandle"
+ "_currentProcessHandle"
+ "com.apple.CallHistory.sync.allow"
+ "currentProcessHandle"
+ "getManagedObjectModelFromDB:orModelURL:orMetadata:"
+ "hasCloudSyncEntitlement"
+ "initWithProcessHandle:"
+ "normalizedHandleWithType:value:isoCountryCode:"
+ "setCurrentProcessHandle:"
- "55.400.141"
- "55.400.141~3"
- "Couldn't get managedObjectModel from db at %{public}@ or model at %{public}@: %{public}@"
- "Failed to get model because no metadata was provided"
- "getManagedObjectModelFromDB:orModelURL:"
- "modelForDBMetadata:"

```
