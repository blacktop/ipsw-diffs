## secd

> `/usr/libexec/secd`

### Sections with Same Size but Changed Content

- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__info_plist`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__thread_vars`

```diff

-62460.1.3.0.0
-  __TEXT.__text: 0x283acc
-  __TEXT.__auth_stubs: 0x40d0
-  __TEXT.__objc_stubs: 0x1d880
-  __TEXT.__objc_methlist: 0x15e98
-  __TEXT.__const: 0x920
-  __TEXT.__objc_classname: 0x2506
-  __TEXT.__objc_methname: 0x2e52a
-  __TEXT.__objc_methtype: 0xb011
+62460.40.78.0.0
+  __TEXT.__text: 0x28b5b4
+  __TEXT.__auth_stubs: 0x4150
+  __TEXT.__objc_stubs: 0x1dcc0
+  __TEXT.__objc_methlist: 0x15fe0
+  __TEXT.__const: 0x930
+  __TEXT.__objc_classname: 0x2531
+  __TEXT.__objc_methname: 0x2eb6a
+  __TEXT.__objc_methtype: 0xb17b
   __TEXT.__constg_swiftt: 0x274
   __TEXT.__swift5_typeref: 0x35e
   __TEXT.__swift5_reflstr: 0xc7

   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_proto: 0x24
   __TEXT.__swift5_types: 0x20
-  __TEXT.__cstring: 0x21937
-  __TEXT.__oslogstring: 0x2f9ca
+  __TEXT.__cstring: 0x22258
+  __TEXT.__oslogstring: 0x2fede
   __TEXT.__swift5_capture: 0x1bc
   __TEXT.__swift_as_entry: 0x40
   __TEXT.__swift_as_ret: 0x3c
   __TEXT.__swift_as_cont: 0x48
-  __TEXT.__gcc_except_tab: 0xa0ac
-  __TEXT.__dlopen_cstrs: 0xb4
+  __TEXT.__dlopen_cstrs: 0x5a
+  __TEXT.__gcc_except_tab: 0xa138
   __TEXT.__info_plist: 0x4fc
-  __TEXT.__unwind_info: 0x7dc8
+  __TEXT.__unwind_info: 0x7e58
   __TEXT.__eh_frame: 0xa60
-  __DATA_CONST.__const: 0x15a10
-  __DATA_CONST.__cfstring: 0x1ba60
-  __DATA_CONST.__objc_classlist: 0x910
+  __DATA_CONST.__const: 0x15bd0
+  __DATA_CONST.__cfstring: 0x1c4c0
+  __DATA_CONST.__objc_classlist: 0x918
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0x258
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x68
-  __DATA_CONST.__objc_superrefs: 0x810
-  __DATA_CONST.__objc_intobj: 0x1428
+  __DATA_CONST.__objc_superrefs: 0x818
+  __DATA_CONST.__objc_intobj: 0x1470
   __DATA_CONST.__objc_arraydata: 0x408
   __DATA_CONST.__objc_dictobj: 0x78
   __DATA_CONST.__objc_arrayobj: 0x360
-  __DATA_CONST.__auth_got: 0x2078
-  __DATA_CONST.__got: 0x1468
+  __DATA_CONST.__auth_got: 0x20b8
+  __DATA_CONST.__got: 0x1498
   __DATA_CONST.__auth_ptr: 0x1d8
-  __DATA.__objc_const: 0x23cd0
-  __DATA.__objc_selrefs: 0x9850
-  __DATA.__objc_ivar: 0x1ae8
-  __DATA.__objc_data: 0x5d98
-  __DATA.__data: 0x3098
+  __DATA.__objc_const: 0x23ee8
+  __DATA.__objc_selrefs: 0x9968
+  __DATA.__objc_ivar: 0x1b04
+  __DATA.__objc_data: 0x5de8
+  __DATA.__data: 0x30a0
   __DATA.__thread_vars: 0xc0
   __DATA.__thread_bss: 0x30
-  __DATA.__bss: 0x12a8
+  __DATA.__bss: 0x19a8
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/Versions/A/TapToRadarKit
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/CloudKit.framework/Versions/A/CloudKit

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 10037
-  Symbols:   1843
-  CStrings:  16268
+  Functions: 10078
+  Symbols:   1857
+  CStrings:  16435
 
Symbols:
+ _AKTelemetryFlowID
+ _OBJC_CLASS_$_MetricSessionInfo
+ _OBJC_CLASS_$_NSFileManager
+ _OBJC_CLASS_$_TPMIDStableTrustedDeviceID
+ _dirname_r
+ _kSecItemCountNonSyncableLive
+ _kSecItemCountNonSyncableTombstone
+ _kSecItemCountSyncableLive
+ _kSecItemCountSyncableTombstone
+ _pread
+ _sqlite3_close_v2
+ _statfs
+ _strcmp
+ _strlcpy
+ _strncmp
+ _strstr
- _OBJC_CLASS_$_TPMIDStableTrustedDeviceIDPair
- _kSecurityRTCEventCategoryAccountDataAccessRecovery
CStrings:
+ " AND agrp IN (?"
+ " GROUP BY agrp"
+ " WHERE agrp IN (?"
+ " WHERE musr = ?"
+ "%02x"
+ "%@: (%@, %@, %@, %@, %@)"
+ "%s-wal"
+ "%s.%d.tmp"
+ "(%d) %s"
+ "-[CuttlefishXPCWrapper notifyPeerTrustEstablishedWithSpecificUser:reply:]_block_invoke"
+ "-[CuttlefishXPCWrapper prepareWithSpecificUser:epoch:machineID:bottleSalt:bottleID:modelID:deviceName:serialNumber:osVersion:stableTrustedDeviceID:flowID:deviceSessionID:policyVersion:policySecrets:syncUserControllableViews:secureElementIdentity:setting:signingPrivKeyPersistentRef:encPrivKeyPersistentRef:reply:]_block_invoke"
+ "-[CuttlefishXPCWrapper setAllowedMachineIDsWithSpecificUser:allowed:userInitiatedRemovals:evictedRemovals:unknownReasonRemovals:honorIDMSListChanges:version:flowID:deviceSessionID:canSendMetrics:altDSID:trustedDeviceHash:deletedDeviceHash:trustedDevicesUpdateTimestamp:idmsStableTrustedDevicesVersion:thisDeviceMachineID:reply:]_block_invoke"
+ "-corruption-log.plist"
+ ":memory:"
+ "<CKKSFixup:KeyMaterialAccessibility (%@)>"
+ "@\"CKKSLocalResetOperation\""
+ "@\"OctagonStateTransitionWatcher\""
+ "@196@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120@128@136#144#152@160B168B172B176@180@188"
+ "@64@0:8@16@24@32@40@48@?56"
+ "Attempting to update trusted device list, flowID: %@ (source: %s)"
+ "B16@?0^{__OpaqueSecDbConnection={__CFRuntimeBase=QAQ}^{__OpaqueSecDb}BBQBiB^{__CFError}{?=CCCCBBiiiiiCI[4[160c]][128c][256c][192c]}^{sqlite3}i^{__CFArray}}8"
+ "B32@0:8^@16q24"
+ "B48@0:8@16^{__CFString=}24^{__CFString=}32^@40"
+ "CDP is enabled, Skipping backing up sync items"
+ "CKKSFixupKeyMaterialAccessibilityOperation"
+ "CREATE INDEX IF NOT EXISTS cert_agrp_musr_sync_tomb ON cert(agrp, musr, sync, tomb);"
+ "CREATE INDEX IF NOT EXISTS genp_agrp_musr_sync_tomb ON genp(agrp, musr, sync, tomb);"
+ "CREATE INDEX IF NOT EXISTS inet_agrp_musr_sync_tomb ON inet(agrp, musr, sync, tomb);"
+ "CREATE INDEX IF NOT EXISTS keys_agrp_musr_sync_tomb ON keys(agrp, musr, sync, tomb);"
+ "Fixup %@ is needed, but device is locked; deferring until unlock"
+ "Minimum fixup across all zones is %lu (current is %lu)"
+ "No fixups needed, all zones up to date"
+ "Received a %@ RPC for arguments (%@)"
+ "SELECT agrp,                                  SUM(CASE WHEN sync=0 AND tomb=0 THEN 1 ELSE 0 END) AS nonsync_live,                                  SUM(CASE WHEN sync=0 AND tomb=1 THEN 1 ELSE 0 END) AS nonsync_tomb,                                  SUM(CASE WHEN sync=1 AND tomb=0 THEN 1 ELSE 0 END) AS sync_live,                                  SUM(CASE WHEN sync=1 AND tomb=1 THEN 1 ELSE 0 END) AS sync_tomb                                  FROM %@                                  GROUP BY agrp"
+ "SELECT agrp, SUM(CASE WHEN sync=0 AND tomb=0 THEN 1 ELSE 0 END), SUM(CASE WHEN sync=0 AND tomb=1 THEN 1 ELSE 0 END), SUM(CASE WHEN sync=1 AND tomb=0 THEN 1 ELSE 0 END), SUM(CASE WHEN sync=1 AND tomb=1 THEN 1 ELSE 0 END) FROM %@"
+ "SELECT count(*) FROM cert"
+ "SELECT count(*) FROM genp"
+ "SELECT count(*) FROM inet"
+ "SELECT count(*) FROM keys"
+ "SecDBCheckCorrupted integrity_check returned %{public}s"
+ "SecDbCorruptionLog: close failed (%{darwin.errno}d)"
+ "SecDbCorruptionLog: log at %{public}@ was unusable, starting over"
+ "SecDbCorruptionLog: path too long: %{public}@"
+ "SecDbCorruptionLog: unable (%{darwin.errno}d) to create %s"
+ "SecDbCorruptionLog: unable (%{darwin.errno}d) to rename into place"
+ "SecDbCorruptionLog: unable to serialize log for %{public}@"
+ "SecDbCorruptionLog: write failed (%{darwin.errno}d)"
+ "SecDbHandleCorrupt: Tried to write corruption marker %{public}s but one already exists"
+ "SecDbSecDbProcessCorruptionMarker: found corruption marker %{public}s"
+ "SecServerItemCountAllWithAccessGroups query template: %@"
+ "Successfully performed a KeyMaterialAccessibility fixup"
+ "T@\"CKKSLocalResetOperation\",&,V_lastLocalResetOperation"
+ "T@\"OTMetricsSessionData\",&,V_currentFlowContext"
+ "T@\"OTMetricsSessionData\",R,V_flowContext"
+ "T@\"OTMetricsSessionData\",R,V_sessionMetrics"
+ "T@\"OctagonStateTransitionWatcher\",W,V_currentFlowWatcher"
+ "T@\"OctagonStateTransitionWatcher\",W,V_pathWatcher"
+ "Unable to fetch CDP status: %@"
+ "Unable to fix up AfterFirstUnlock key material because device is locked; will retry after unlock"
+ "Unable to fix up AfterFirstUnlock key material: %@"
+ "Unable to fix up WhenUnlocked key material because device is locked; will retry after unlock"
+ "Unable to fix up WhenUnlocked key material: %@"
+ "Updated zone fixup state to CKKSFixupKeyMaterialAccessibility"
+ "_currentFlowContext"
+ "_currentFlowWatcher"
+ "_flowContext"
+ "_lastLocalResetOperation"
+ "_onqueueForgetFlowContextIfDone"
+ "_pathWatcher"
+ "absoluteString"
+ "accessGroups must be a non-empty CFArray, got %@"
+ "afterAuthKitFetch:userInitiatedRemovals:evictedRemovals:unknownReasonRemovals:trustedDeviceHash:deletedDeviceHash:trustedDevicesUpdateTimestamp:accountIsDemo:version:idmsStableTrustedDevicesVersion:"
+ "applicationID"
+ "bytesRead"
+ "checkEscrowCheck:sessionMetrics:reply:"
+ "checkOctagonHealth:repair:danglingPeerCleanup:caesarPeerCleanup:updateIdMS:forceStableTrustedDeviceIDReroll:sessionMetrics:reply:"
+ "com.apple.private.security.access-group-item-counts"
+ "com.apple.security.egoIdentities"
+ "componentsWithURL:resolvingAgainstBaseURL:"
+ "consumeIdMSTDLNotificationFlowID"
+ "corruptionError"
+ "couldNotRun"
+ "currentFlowContext"
+ "currentFlowWatcher"
+ "dataWithContentsOfFile:options:error:"
+ "dbDeleted"
+ "dbMtime"
+ "dbSize"
+ "dbUnlinkFailed"
+ "defaultManager"
+ "detectedAt"
+ "disableWalrus:isDBRv2:pdpState:sessionMetrics:reply:"
+ "doSimpleStateMachineRPC:op:sourceStates:flowContext:reply:"
+ "doWatchedStateMachineRPC:sourceStates:path:flowContext:reply:"
+ "doWatchedStateMachineRPC:sourceStates:path:transitionOp:flowContext:reply:"
+ "enableWalrus:isDBRv2:pdpState:sessionMetrics:reply:"
+ "entries"
+ "episode"
+ "failingSQL"
+ "fetchStableTrustedDeviceIDWithSessionMetrics:reply:"
+ "fetchTrustedDeviceListWithStableTrustedDeviceIDStatus:sessionMetrics:reply:"
+ "file:"
+ "fileChangeCounter"
+ "fileExistsAtPath:"
+ "fileHeader"
+ "fileSystemRepresentation"
+ "fileURLWithPath:"
+ "filesAtDetection"
+ "fixup_key_material_accessibility"
+ "flow"
+ "flowContext"
+ "getCDPStatusSync:error:"
+ "hadPriorIOFailure"
+ "handlePairingRestart:sessionMetrics:"
+ "headerFirst32Hex"
+ "idMSTDLNotificationFlowID"
+ "idms push"
+ "immutable=1"
+ "init:sourceStates:serialQueue:transitionOp:flowContext:"
+ "initForContainer:contextID:activeAccount:stateHolder:flagHandler:sosAdapter:octagonAdapter:accountsAdapter:authKitAdapter:personaAdapter:deviceInfoAdapter:secureBackupAdapter:laContextAdapter:ckksAccountSync:lockStateTracker:cuttlefishXPCWrapper:escrowRequestClass:notifierClass:sessionMetrics:permittedToSendMetrics:accountIsD:accountIsW:reachabilityTracker:escrowChecker:"
+ "initWithBytes:length:encoding:"
+ "initWithFlowID:deviceSessionID:idMSTDLNotificationFlowID:"
+ "initWithMetrics:session:eventName:"
+ "initWithMetrics:session:eventName:canSendMetrics:"
+ "initWithSession:eventName:"
+ "integrityCheck"
+ "integrityCheckRowsTotal"
+ "integrityCheckStatus"
+ "isHomeAccessory"
+ "item-counts"
+ "joinWithBottle:entropy:bottleSalt:sessionMetrics:reply:"
+ "joinWithCustodianRecoveryKey:sessionMetrics:reply:"
+ "joinWithInheritanceKey:sessionMetrics:reply:"
+ "joinWithRecoveryKey:sessionMetrics:reply:"
+ "lastLocalResetOperation"
+ "lastObject"
+ "lastWriterSqliteVersion"
+ "localResetWithSessionMetrics:reply:"
+ "magicValid"
+ "markerAgeSeconds"
+ "markerOutcome"
+ "migrationFailure"
+ "noSuccessor"
+ "nonsync_live"
+ "nonsync_tomb"
+ "notificationOfMachineIDListChangeWithFlowID:"
+ "notifyPeerTrustEstablishedWithSpecificUser:reply:"
+ "octagon-authkit: unable to fetch this device's machine ID for telemetry: %@"
+ "octagon: failed to notify TPH of trust establishment: %@"
+ "openErrmsg"
+ "openFailed"
+ "openResultCode"
+ "operationDependenciesWithSessionMetrics:"
+ "origin"
+ "pageSize"
+ "pathWatcher"
+ "performCKServerUnreadableDataRemoval:accountIsW:altDSID:sessionMetrics:reply:"
+ "postMortem"
+ "preexisted"
+ "prepareInformationWithSessionMetrics:"
+ "prepareWithSpecificUser:epoch:machineID:bottleSalt:bottleID:modelID:deviceName:serialNumber:osVersion:stableTrustedDeviceID:flowID:deviceSessionID:policyVersion:policySecrets:syncUserControllableViews:secureElementIdentity:setting:signingPrivKeyPersistentRef:encPrivKeyPersistentRef:reply:"
+ "priorLogUnreadable"
+ "q32@0:8@16^@24"
+ "ranAndFailed"
+ "readErrno"
+ "remediation"
+ "removeObjectsInRange:"
+ "reportingFlowID"
+ "requestTrustedDeviceListRefreshWithFlowID:"
+ "rerollWithSessionMetrics:reply:"
+ "resetOnly"
+ "rpcAccountWideSettingsWithForceFetch:sessionMetrics:reply:"
+ "rpcEstablish:sessionMetrics:reply:"
+ "rpcFetchAccountSettingsWithSessionMetrics:reply:"
+ "rpcFetchAllViableBottlesFromSource:sessionMetrics:reply:"
+ "rpcFetchUserControllableViewsSyncingStatusWithSessionMetrics:reply:"
+ "rpcJoin:vouchSig:sessionMetrics:reply:"
+ "rpcPrepareIdentityAsApplicantWithConfiguration:epoch:sessionMetrics:reply:"
+ "rpcRefetchCKKSPolicyWithSessionMetrics:reply:"
+ "rpcReset:isDBRv2:sessionMetrics:reply:"
+ "rpcResetAndEstablish:idmsTargetContext:idmsCuttlefishPassword:notifyIdMS:accountSettings:isDBRv2:accountIsW:sessionMetrics:reply:"
+ "rpcSetAccountSetting:sessionMetrics:reply:"
+ "rpcSetUserControllableViewsSyncingStatus:sessionMetrics:reply:"
+ "rpcVoucherWithConfiguration:permanentInfo:permanentInfoSig:stableInfo:stableInfoSig:sessionMetrics:reply:"
+ "schemaVersionNew"
+ "schemaVersionOld"
+ "sec_count_all_with_access_groups_id"
+ "sessionInfoWithAltDSID:"
+ "sessionInfoWithAltDSID:flowID:deviceSessionID:"
+ "setAllowedMachineIDsWithSpecificUser:allowed:userInitiatedRemovals:evictedRemovals:unknownReasonRemovals:honorIDMSListChanges:version:flowID:deviceSessionID:canSendMetrics:altDSID:trustedDeviceHash:deletedDeviceHash:trustedDevicesUpdateTimestamp:idmsStableTrustedDevicesVersion:thisDeviceMachineID:reply:"
+ "setCurrentFlowContext:"
+ "setCurrentFlowWatcher:"
+ "setLastLocalResetOperation:"
+ "setPathWatcher:"
+ "setQuery:"
+ "setTelemetryFlowID:"
+ "sizeInPages"
+ "sqlite3: (%d) %{public}s"
+ "sqliteCorrupt"
+ "sqliteErrmsg"
+ "sqliteExtendedCode"
+ "sqliteLog"
+ "sqliteNotADb"
+ "sqliteSystemErrno"
+ "staleWalLeftBehind"
+ "stringWithCapacity:"
+ "sync = 0"
+ "sync_live"
+ "sync_tomb"
+ "tableRowCounts"
+ "totalEpisodes"
+ "trusted stable id is missing components for machine %@"
+ "updateKeyMaterialAccessibilityInZone:fromAccessible:toAccessible:error:"
+ "uptimeAtDetection"
+ "v148@0:8@\"TPSpecificUser\"16@\"NSSet\"24@\"NSSet\"32@\"NSSet\"40@\"NSSet\"48q56@\"NSString\"64@\"NSString\"72@\"NSString\"80B88@\"NSString\"92@\"NSString\"100@\"NSString\"108@\"NSNumber\"116@\"NSString\"124@\"NSString\"132@?<v@?B@\"NSError\">140"
+ "v172@0:8@\"TPSpecificUser\"16Q24@\"NSString\"32@\"NSString\"40@\"NSString\"48@\"NSString\"56@\"NSString\"64@\"NSString\"72@\"NSString\"80@\"TPStableTrustedDeviceID\"88@\"NSString\"96@\"NSString\"104@\"TPPolicyVersion\"112@\"NSDictionary\"120i128@\"TPPBSecureElementIdentity\"132@\"OTAccountSettings\"140@\"NSData\"148@\"NSData\"156@?<v@?@\"NSString\"@\"NSData\"@\"NSData\"@\"NSData\"@\"NSData\"@\"TPSyncingPolicy\"@\"NSError\">164"
+ "v172@0:8@16Q24@32@40@48@56@64@72@80@88@96@104@112@120i128@132@140@148@156@?164"
+ "v32@0:8@\"OTControlArguments\"16@?<v@?@\"NSSet\"@\"NSSet\"@\"NSSet\"@\"NSSet\"@\"NSString\"@\"NSString\"@\"NSString\"@\"NSNumber\"@\"NSString\"@\"OTMetricsSessionData\"q@\"NSError\">24"
+ "v36@0:8B16@\"OTMetricsSessionData\"20@?<v@?@\"OTEscrowCheckCallResult\"@\"NSError\">28"
+ "v40@0:8q16@24@?32"
+ "v44@0:8q16B24@28@?36"
+ "v48@0:8@16B24i28@32@?40"
+ "v48@0:8@16Q24@32@?40"
+ "v48@0:8B16B20@24@32@?40"
+ "v52@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32B40@?<v@?@\"NSSet\"@\"NSSet\"@\"NSSet\"@\"NSSet\"@\"NSString\"@\"NSString\"@\"NSString\"@\"NSNumber\"@\"NSString\"@\"OTMetricsSessionData\"@\"NSError\">44"
+ "v56@0:8B16B20B24B28B32B36@40@?48"
+ "v72@0:8@16@24@32@40@48@56@?64"
+ "v76@0:8q16@24@32B40@44B52B56@60@?68"
+ "v92@0:8@16@24@32@40@48@56@64B72@76@84"
+ "v96@?0@\"NSSet\"8@\"NSSet\"16@\"NSSet\"24@\"NSSet\"32@\"NSString\"40@\"NSString\"48@\"NSString\"56@\"NSNumber\"64@\"NSString\"72@\"OTMetricsSessionData\"80@\"NSError\"88"
+ "versionValidFor"
+ "volumeFreeBytes"
+ "volumeReadOnly"
+ "waitForOctagonUpgradeWithSessionMetrics:reply:"
+ "walBytesNotCounted"
+ "walSize"
+ "writeFailed"
+ "written"
+ "zone-deletion"
+ "zone-deletion-operation"
+ "\xb1\x91"
+ "\xf1Q"
- "%@: (%@, %@, %@)"
- "-[CuttlefishXPCWrapper prepareWithSpecificUser:epoch:machineID:bottleSalt:bottleID:modelID:deviceName:serialNumber:osVersion:stableTrustedDeviceID:policyVersion:policySecrets:syncUserControllableViews:secureElementIdentity:setting:signingPrivKeyPersistentRef:encPrivKeyPersistentRef:reply:]_block_invoke"
- "-[CuttlefishXPCWrapper setAllowedMachineIDsWithSpecificUser:allowedMachineIDs:userInitiatedRemovals:evictedRemovals:unknownReasonRemovals:honorIDMSListChanges:version:flowID:deviceSessionID:canSendMetrics:altDSID:trustedDeviceHash:deletedDeviceHash:trustedDevicesUpdateTimestamp:idmsStableTrustedDevicesVersion:midStableTrustedDeviceIDs:reply:]_block_invoke"
- "@204@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120@128@136#144#152@160@168B176B180B184@188@196"
- "Attempting to update trusted device list"
- "B16@?0^{__OpaqueSecDbConnection={__CFRuntimeBase=QAQ}^{__OpaqueSecDb}BBQBiB^{__CFError}^{sqlite3}i^{__CFArray}}8"
- "MetricsOverrideTestsAreEnabled"
- "SELECT agrp,                                  SUM(1 - tomb) AS count_tomb_0,                                  SUM(tomb) AS count_tomb_1                                  FROM %@                                  GROUP BY agrp"
- "SecDBCheckCorrupted integrity_check returned %s"
- "SecDbHandleCorrupt: Tried to write corruption marker %s but one already exists"
- "SecDbSecDbProcessCorruptionMarker: found corruption marker %s"
- "T@\"NSString\",&,V_deviceSessionID"
- "T@\"NSString\",&,V_flowID"
- "_deviceSessionID"
- "_flowID"
- "afterAuthKitFetch:userInitiatedRemovals:evictedRemovals:unknownReasonRemovals:trustedDeviceHash:deletedDeviceHash:trustedDevicesUpdateTimestamp:accountIsDemo:version:idmsStableTrustedDevicesVersion:midStableTrustedDeviceIDs:"
- "bool soft_MetricsOverrideTestsAreEnabled(void)"
- "checkEscrowCheck:reply:"
- "checkOctagonHealth:repair:danglingPeerCleanup:caesarPeerCleanup:updateIdMS:forceStableTrustedDeviceIDReroll:reply:"
- "disableWalrus:isDBRv2:pdpState:reply:"
- "doSimpleStateMachineRPC:op:sourceStates:reply:"
- "doWatchedStateMachineRPC:sourceStates:path:reply:"
- "doWatchedStateMachineRPC:sourceStates:path:transitionOp:reply:"
- "enableWalrus:isDBRv2:pdpState:reply:"
- "fetchStableTrustedDeviceIDWithReply:"
- "fetchTrustedDeviceListWithStableTrustedDeviceIDStatus:reply:"
- "fetched MID/StableID pair is %@"
- "handlePairingRestart:"
- "init:sourceStates:serialQueue:transitionOp:"
- "initForContainer:contextID:activeAccount:stateHolder:flagHandler:sosAdapter:octagonAdapter:accountsAdapter:authKitAdapter:personaAdapter:deviceInfoAdapter:secureBackupAdapter:laContextAdapter:ckksAccountSync:lockStateTracker:cuttlefishXPCWrapper:escrowRequestClass:notifierClass:flowID:deviceSessionID:permittedToSendMetrics:accountIsD:accountIsW:reachabilityTracker:escrowChecker:"
- "initWithCKKSMetrics:altDSID:eventName:testsAreEnabled:category:sendMetric:"
- "initWithFlowID:deviceSessionID:"
- "initWithKeychainCircleMetrics:altDSID:flowID:deviceSessionID:eventName:testsAreEnabled:canSendMetrics:category:"
- "joinWithBottle:entropy:bottleSalt:reply:"
- "joinWithCustodianRecoveryKey:reply:"
- "joinWithInheritanceKey:reply:"
- "joinWithRecoveryKey:reply:"
- "localReset:"
- "notificationOfMachineIDListChange"
- "performCKServerUnreadableDataRemoval:accountIsW:altDSID:reply:"
- "prepareWithSpecificUser:epoch:machineID:bottleSalt:bottleID:modelID:deviceName:serialNumber:osVersion:stableTrustedDeviceID:policyVersion:policySecrets:syncUserControllableViews:secureElementIdentity:setting:signingPrivKeyPersistentRef:encPrivKeyPersistentRef:reply:"
- "requestTrustedDeviceListRefresh"
- "rerollWithReply:"
- "rpcAccountWideSettingsWithForceFetch:reply:"
- "rpcEstablish:reply:"
- "rpcFetchAccountSettings:"
- "rpcFetchAllViableBottlesFromSource:reply:"
- "rpcFetchUserControllableViewsSyncingStatus:"
- "rpcJoin:vouchSig:reply:"
- "rpcPrepareIdentityAsApplicantWithConfiguration:epoch:reply:"
- "rpcRefetchCKKSPolicy:"
- "rpcReset:isDBRv2:reply:"
- "rpcResetAndEstablish:idmsTargetContext:idmsCuttlefishPassword:notifyIdMS:accountSettings:isDBRv2:accountIsW:reply:"
- "rpcSetAccountSetting:reply:"
- "rpcSetUserControllableViewsSyncingStatus:reply:"
- "rpcVoucherWithConfiguration:permanentInfo:permanentInfoSig:stableInfo:stableInfoSig:reply:"
- "setAllowedMachineIDsWithSpecificUser:allowedMachineIDs:userInitiatedRemovals:evictedRemovals:unknownReasonRemovals:honorIDMSListChanges:version:flowID:deviceSessionID:canSendMetrics:altDSID:trustedDeviceHash:deletedDeviceHash:trustedDevicesUpdateTimestamp:idmsStableTrustedDevicesVersion:midStableTrustedDeviceIDs:reply:"
- "tomb_0"
- "tomb_1"
- "trusted stable id in fetch TDL is missing components for machine %@"
- "v100@0:8@16@24@32@40@48@56@64B72@76@84@92"
- "v104@?0@\"NSSet\"8@\"NSSet\"16@\"NSSet\"24@\"NSSet\"32@\"NSString\"40@\"NSString\"48@\"NSString\"56@\"NSNumber\"64@\"NSString\"72@\"OTMetricsSessionData\"80@\"NSSet\"88@\"NSError\"96"
- "v148@0:8@\"TPSpecificUser\"16@\"NSSet\"24@\"NSSet\"32@\"NSSet\"40@\"NSSet\"48q56@\"NSString\"64@\"NSString\"72@\"NSString\"80B88@\"NSString\"92@\"NSString\"100@\"NSString\"108@\"NSNumber\"116@\"NSString\"124@\"NSSet\"132@?<v@?B@\"NSError\">140"
- "v156@0:8@\"TPSpecificUser\"16Q24@\"NSString\"32@\"NSString\"40@\"NSString\"48@\"NSString\"56@\"NSString\"64@\"NSString\"72@\"NSString\"80@\"TPStableTrustedDeviceID\"88@\"TPPolicyVersion\"96@\"NSDictionary\"104i112@\"TPPBSecureElementIdentity\"116@\"OTAccountSettings\"124@\"NSData\"132@\"NSData\"140@?<v@?@\"NSString\"@\"NSData\"@\"NSData\"@\"NSData\"@\"NSData\"@\"TPSyncingPolicy\"@\"NSError\">148"
- "v28@0:8B16@?<v@?@\"OTEscrowCheckCallResult\"@\"NSError\">20"
- "v32@0:8@\"OTControlArguments\"16@?<v@?@\"NSSet\"@\"NSSet\"@\"NSSet\"@\"NSSet\"@\"NSString\"@\"NSString\"@\"NSString\"@\"NSNumber\"@\"NSString\"@\"OTMetricsSessionData\"@\"NSSet\"q@\"NSError\">24"
- "v32@0:8^@16q24"
- "v40@0:8@16B24i28@?32"
- "v40@0:8B16B20@24@?32"
- "v48@0:8B16B20B24B28B32B36@?40"
- "v52@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32B40@?<v@?@\"NSSet\"@\"NSSet\"@\"NSSet\"@\"NSSet\"@\"NSString\"@\"NSString\"@\"NSString\"@\"NSNumber\"@\"NSString\"@\"OTMetricsSessionData\"@\"NSSet\"@\"NSError\">44"
- "v68@0:8q16@24@32B40@44B52B56@?60"
- "waitForOctagonUpgrade:"
- "\xa1"
- "\xf1a"
```
