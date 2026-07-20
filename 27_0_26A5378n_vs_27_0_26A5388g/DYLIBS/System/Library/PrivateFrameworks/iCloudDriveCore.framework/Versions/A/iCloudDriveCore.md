## iCloudDriveCore

> `/System/Library/PrivateFrameworks/iCloudDriveCore.framework/Versions/A/iCloudDriveCore`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__data`
- `__DATA.__data`

```diff

-5140.0.0.0.2
-  __TEXT.__text: 0x342acc
-  __TEXT.__objc_methlist: 0x1c000
+5168.0.5.0.2
+  __TEXT.__text: 0x343180
+  __TEXT.__objc_methlist: 0x1c010
   __TEXT.__const: 0x4f8
-  __TEXT.__cstring: 0x82d8d
-  __TEXT.__oslogstring: 0x3ead2
-  __TEXT.__gcc_except_tab: 0x17b20
+  __TEXT.__cstring: 0x82cea
+  __TEXT.__oslogstring: 0x3ebca
+  __TEXT.__gcc_except_tab: 0x17b54
   __TEXT.__ustring: 0x36
-  __TEXT.__unwind_info: 0xa468
+  __TEXT.__unwind_info: 0xa480
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_superrefs: 0x958
   __DATA_CONST.__objc_arraydata: 0xfd8
   __DATA_CONST.__got: 0x1808
-  __AUTH_CONST.__const: 0xbc38
+  __AUTH_CONST.__const: 0xbc18
   __AUTH_CONST.__cfstring: 0x23b40
-  __AUTH_CONST.__objc_const: 0x41948
+  __AUTH_CONST.__objc_const: 0x41978
   __AUTH_CONST.__objc_intobj: 0xc48
   __AUTH_CONST.__objc_arrayobj: 0x348
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_doubleobj: 0x50
   __AUTH_CONST.__auth_got: 0xd10
-  __AUTH.__objc_data: 0x27d8
+  __AUTH.__objc_data: 0x25f8
   __AUTH.__data: 0x38
-  __DATA.__objc_ivar: 0x2050
+  __DATA.__objc_ivar: 0x2054
   __DATA.__data: 0x28e8
   __DATA.__bss: 0x248
-  __DATA_DIRTY.__objc_data: 0x43a8
+  __DATA_DIRTY.__objc_data: 0x4588
   __DATA_DIRTY.__data: 0xc8
   __DATA_DIRTY.__bss: 0x430
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts

   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 14507
-  Symbols:   25378
-  CStrings:  12256
+  Functions: 14509
+  Symbols:   25379
+  CStrings:  12258
 
Symbols:
+ +[AppTelemetryTimeSeriesEvent(BRCAdditions) newIPCMethodAccessEventForMethod:bundleID:isSandboxed:]
+ -[BRCAccountSession(IPCTelemetry) postIPCMethodTelemetry:bundleID:isSandboxed:]
+ -[BRCQueryItemInfo isInDataScope]
+ -[BRCXPCRegularIPCsClient(FPFSAdditions) _resolveSyncUpZoneName:zoneOwner:itemIDString:forLocalItem:]
+ GCC_except_table106
+ GCC_except_table118
+ GCC_except_table160
+ GCC_except_table172
+ GCC_except_table175
+ GCC_except_table181
+ GCC_except_table186
+ GCC_except_table199
+ GCC_except_table201
+ GCC_except_table212
+ GCC_except_table217
+ GCC_except_table222
+ GCC_except_table227
+ GCC_except_table234
+ GCC_except_table237
+ GCC_except_table241
+ GCC_except_table247
+ GCC_except_table249
+ GCC_except_table266
+ GCC_except_table269
+ GCC_except_table274
+ GCC_except_table285
+ GCC_except_table294
+ GCC_except_table309
+ GCC_except_table315
+ GCC_except_table339
+ OBJC_IVAR_$_BRCQueryItemInfo._isInDataScope
+ __99-[BRCAccountSession learnNewItemIdentifier:forItemIdentifier:zoneName:ownerName:completionHandler:]_block_invoke_2
+ ___block_descriptor_80_e8_32s40s48s56s64r72r_e5_B8?0l
+ _objc_msgSend$_resolveSyncUpZoneName:zoneOwner:itemIDString:forLocalItem:
+ _objc_msgSend$newIPCMethodAccessEventForMethod:bundleID:isSandboxed:
+ _objc_msgSend$postIPCMethodTelemetry:bundleID:isSandboxed:
- +[AppTelemetryTimeSeriesEvent(BRCAdditions) newMissingShareAliasEventWithZoneMangledID:enhancedDrivePrivacyEnabled:itemIDString:]
- -[BRCAccountSession _submitReimportDomainFailedTelemetryEventIfNeeded]
- GCC_except_table130
- GCC_except_table146
- GCC_except_table150
- GCC_except_table166
- GCC_except_table171
- GCC_except_table179
- GCC_except_table182
- GCC_except_table188
- GCC_except_table189
- GCC_except_table194
- GCC_except_table196
- GCC_except_table202
- GCC_except_table208
- GCC_except_table210
- GCC_except_table213
- GCC_except_table220
- GCC_except_table225
- GCC_except_table236
- GCC_except_table258
- GCC_except_table260
- GCC_except_table262
- GCC_except_table265
- GCC_except_table302
- GCC_except_table317
- GCC_except_table331
- GCC_except_table345
- __70-[BRCAccountSession _submitReimportDomainFailedTelemetryEventIfNeeded]_block_invoke
- ___70-[BRCAccountSession _submitReimportDomainFailedTelemetryEventIfNeeded]_block_invoke
- ___block_descriptor_64_e8_32s40s48s56s_e5_B8?0l
- _objc_msgSend$_submitReimportDomainFailedTelemetryEventIfNeeded
- _objc_msgSend$br_reimportDomainErrorInfoPath
- _objc_msgSend$newReimportDomainFailureEventWithError:description:
- _objc_msgSend$secondsToWaitBeforeSendingReimportDomainFailureTTR
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.1bXXDK/Sources/CloudDocs_executables/core/shared/account/BRCAccountSession.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.1bXXDK/Sources/CloudDocs_executables/core/shared/account/BRCAccountsManager.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.1bXXDK/Sources/CloudDocs_executables/core/shared/backup/BRCBackupSession.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.1bXXDK/Sources/CloudDocs_executables/core/shared/containers/BRCClientZone.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.1bXXDK/Sources/CloudDocs_executables/core/shared/containers/BRCServerZone.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.1bXXDK/Sources/CloudDocs_executables/core/shared/daemon/BRCDaemon.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.1bXXDK/Sources/CloudDocs_executables/core/shared/database/BRCClientDatabaseFacade.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.1bXXDK/Sources/CloudDocs_executables/core/shared/database/BRCClientState.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.1bXXDK/Sources/CloudDocs_executables/core/shared/database/BRCDatabaseManager.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.1bXXDK/Sources/CloudDocs_executables/core/shared/database/BRCDatabaseSchema.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.1bXXDK/Sources/CloudDocs_executables/core/shared/database/BRCServerPersistedState.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.1bXXDK/Sources/CloudDocs_executables/core/shared/foundation/BRCFairScheduler.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.1bXXDK/Sources/CloudDocs_executables/core/shared/foundation/BRCPQLConnection.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.1bXXDK/Sources/CloudDocs_executables/core/shared/items/BRCItemID.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.1bXXDK/Sources/CloudDocs_executables/core/shared/notifs/BRCAccountHandler.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.1bXXDK/Sources/CloudDocs_executables/core/shared/sync/records/CKRecord+BRCItemAdditions.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.1bXXDK/Sources/CloudDocs_executables/core/shared/sync/transfers/BRCTransferStream.m"
+ "IPC_METHOD_ACCESS"
+ "[CRIT] Assertion failed: (bits & BRCSyncStateNeedsSyncUp) == 0%@"
+ "[CRIT] Assertion failed: (self.syncState & BRCSyncStateNeedsSyncUp) == 0%@"
+ "[CRIT] UNREACHABLE: Dead item already holds learn-target id %@ for %@%@"
+ "[CRIT] UNREACHABLE: Failed to save item during learn for %@%@"
+ "[ERROR] Connection %@ auto rollback handler...%@"
+ "[WARNING] Documents folder is on disk - possibly a delete retry%@"
+ "unreachable: Dead item already holds learn-target id %@ for %@"
+ "unreachable: Failed to save item during learn for %@"
- "-[BRCAccountSession _submitReimportDomainFailedTelemetryEventIfNeeded]"
- "-[BRCAccountSession _submitReimportDomainFailedTelemetryEventIfNeeded]_block_invoke"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7Nh9Xa/Sources/CloudDocs_executables/core/shared/account/BRCAccountSession.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7Nh9Xa/Sources/CloudDocs_executables/core/shared/account/BRCAccountsManager.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7Nh9Xa/Sources/CloudDocs_executables/core/shared/backup/BRCBackupSession.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7Nh9Xa/Sources/CloudDocs_executables/core/shared/containers/BRCClientZone.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7Nh9Xa/Sources/CloudDocs_executables/core/shared/containers/BRCServerZone.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7Nh9Xa/Sources/CloudDocs_executables/core/shared/daemon/BRCDaemon.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7Nh9Xa/Sources/CloudDocs_executables/core/shared/database/BRCClientDatabaseFacade.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7Nh9Xa/Sources/CloudDocs_executables/core/shared/database/BRCClientState.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7Nh9Xa/Sources/CloudDocs_executables/core/shared/database/BRCDatabaseManager.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7Nh9Xa/Sources/CloudDocs_executables/core/shared/database/BRCDatabaseSchema.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7Nh9Xa/Sources/CloudDocs_executables/core/shared/database/BRCServerPersistedState.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7Nh9Xa/Sources/CloudDocs_executables/core/shared/foundation/BRCFairScheduler.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7Nh9Xa/Sources/CloudDocs_executables/core/shared/foundation/BRCPQLConnection.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7Nh9Xa/Sources/CloudDocs_executables/core/shared/items/BRCItemID.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7Nh9Xa/Sources/CloudDocs_executables/core/shared/notifs/BRCAccountHandler.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7Nh9Xa/Sources/CloudDocs_executables/core/shared/sync/records/CKRecord+BRCItemAdditions.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7Nh9Xa/Sources/CloudDocs_executables/core/shared/sync/transfers/BRCTransferStream.m"
- "Reimport domain on startup failed"
- "Reimport domain on startup failed, need to verify that things got recovered correctly"
- "[CRIT] UNREACHABLE: That's weird but Documents is still on disk.%@"
- "[DEBUG] Checking if there is a need to submit reimport failed telemetry%@"
- "it reset the database"
```
