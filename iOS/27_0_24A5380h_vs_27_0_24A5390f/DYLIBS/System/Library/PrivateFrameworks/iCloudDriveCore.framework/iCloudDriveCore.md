## iCloudDriveCore

> `/System/Library/PrivateFrameworks/iCloudDriveCore.framework/iCloudDriveCore`

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
- `__DATA_DIRTY.__data`

```diff

-5140.0.0.0.2
-  __TEXT.__text: 0x306a2c
-  __TEXT.__objc_methlist: 0x1be28
+5168.0.5.0.2
+  __TEXT.__text: 0x3070a8
+  __TEXT.__objc_methlist: 0x1be40
   __TEXT.__const: 0x4f0
-  __TEXT.__cstring: 0x825b9
-  __TEXT.__oslogstring: 0x3db8d
-  __TEXT.__gcc_except_tab: 0x17698
+  __TEXT.__cstring: 0x82516
+  __TEXT.__oslogstring: 0x3dc85
+  __TEXT.__gcc_except_tab: 0x176c8
   __TEXT.__ustring: 0x36
-  __TEXT.__unwind_info: 0xa3f0
+  __TEXT.__unwind_info: 0xa400
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_superrefs: 0x960
   __DATA_CONST.__objc_arraydata: 0xeb8
   __DATA_CONST.__got: 0x17a8
-  __AUTH_CONST.__const: 0x2cc8
+  __AUTH_CONST.__const: 0x2ca8
   __AUTH_CONST.__cfstring: 0x23520
-  __AUTH_CONST.__objc_const: 0x419f0
+  __AUTH_CONST.__objc_const: 0x41a20
   __AUTH_CONST.__objc_intobj: 0xc30
   __AUTH_CONST.__objc_arrayobj: 0x2b8
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_doubleobj: 0x50
   __AUTH_CONST.__auth_got: 0xd98
-  __AUTH.__objc_data: 0x2738
+  __AUTH.__objc_data: 0x2558
   __AUTH.__data: 0x18
-  __DATA.__objc_ivar: 0x2028
+  __DATA.__objc_ivar: 0x202c
   __DATA.__data: 0x29f0
   __DATA.__bss: 0x200
-  __DATA_DIRTY.__objc_data: 0x43a8
+  __DATA_DIRTY.__objc_data: 0x4588
   __DATA_DIRTY.__data: 0xd0
   __DATA_DIRTY.__bss: 0x428
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 14204
-  Symbols:   24521
-  CStrings:  12123
+  Functions: 14206
+  Symbols:   24524
+  CStrings:  12125
 
Symbols:
+ +[AppTelemetryTimeSeriesEvent(BRCAdditions) newIPCMethodAccessEventForMethod:bundleID:isSandboxed:]
+ -[BRCAccountSession(IPCTelemetry) postIPCMethodTelemetry:bundleID:isSandboxed:]
+ -[BRCQueryItemInfo isInDataScope]
+ -[BRCXPCRegularIPCsClient(FPFSAdditions) _resolveSyncUpZoneName:zoneOwner:itemIDString:forLocalItem:]
+ GCC_except_table104
+ GCC_except_table106
+ GCC_except_table113
+ GCC_except_table120
+ GCC_except_table133
+ GCC_except_table166
+ GCC_except_table176
+ GCC_except_table179
+ GCC_except_table183
+ GCC_except_table187
+ GCC_except_table189
+ GCC_except_table193
+ GCC_except_table199
+ GCC_except_table205
+ GCC_except_table212
+ GCC_except_table239
+ GCC_except_table264
+ GCC_except_table279
+ GCC_except_table294
+ GCC_except_table311
+ GCC_except_table345
+ GCC_except_table353
+ GCC_except_table79
+ _OBJC_IVAR_$_BRCQueryItemInfo._isInDataScope
+ ___block_descriptor_80_e8_32s40s48s56s64r72r_e5_B8?0ls32l8s40l8s48l8r64l8r72l8s56l8
+ _objc_msgSend$_resolveSyncUpZoneName:zoneOwner:itemIDString:forLocalItem:
+ _objc_msgSend$newIPCMethodAccessEventForMethod:bundleID:isSandboxed:
+ _objc_msgSend$postIPCMethodTelemetry:bundleID:isSandboxed:
- +[AppTelemetryTimeSeriesEvent(BRCAdditions) newMissingShareAliasEventWithZoneMangledID:enhancedDrivePrivacyEnabled:itemIDString:]
- -[BRCAccountSession _submitReimportDomainFailedTelemetryEventIfNeeded]
- GCC_except_table114
- GCC_except_table132
- GCC_except_table139
- GCC_except_table141
- GCC_except_table145
- GCC_except_table152
- GCC_except_table165
- GCC_except_table168
- GCC_except_table171
- GCC_except_table175
- GCC_except_table190
- GCC_except_table195
- GCC_except_table204
- GCC_except_table214
- GCC_except_table248
- GCC_except_table260
- GCC_except_table261
- GCC_except_table281
- GCC_except_table300
- GCC_except_table333
- GCC_except_table337
- ___70-[BRCAccountSession _submitReimportDomainFailedTelemetryEventIfNeeded]_block_invoke
- ___block_descriptor_64_e8_32s40s48s56s_e5_B8?0ls32l8s40l8s48l8s56l8
- _objc_msgSend$_submitReimportDomainFailedTelemetryEventIfNeeded
- _objc_msgSend$br_reimportDomainErrorInfoPath
- _objc_msgSend$newReimportDomainFailureEventWithError:description:
- _objc_msgSend$secondsToWaitBeforeSendingReimportDomainFailureTTR
CStrings:
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
- "Reimport domain on startup failed"
- "Reimport domain on startup failed, need to verify that things got recovered correctly"
- "[CRIT] UNREACHABLE: That's weird but Documents is still on disk.%@"
- "[DEBUG] Checking if there is a need to submit reimport failed telemetry%@"
- "it reset the database"
```
