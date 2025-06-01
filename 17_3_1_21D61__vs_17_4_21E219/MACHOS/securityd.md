## securityd

> `/usr/libexec/securityd`

```diff

-61040.82.1.0.0
-  __TEXT.__text: 0x22c1b0
-  __TEXT.__auth_stubs: 0x38c0
-  __TEXT.__objc_stubs: 0x1aaa0
-  __TEXT.__objc_methlist: 0x12cfc
-  __TEXT.__const: 0x62d
-  __TEXT.__cstring: 0x1faec
-  __TEXT.__oslogstring: 0x28432
-  __TEXT.__gcc_except_tab: 0x6c9c
-  __TEXT.__objc_classname: 0x2282
-  __TEXT.__objc_methname: 0x29c62
-  __TEXT.__objc_methtype: 0x95d6
+61123.100.169.0.0
+  __TEXT.__text: 0x2313ec
+  __TEXT.__auth_stubs: 0x38e0
+  __TEXT.__objc_stubs: 0x1ade0
+  __TEXT.__objc_methlist: 0x12efc
+  __TEXT.__const: 0x70d
+  __TEXT.__cstring: 0x1ff51
+  __TEXT.__oslogstring: 0x28adc
+  __TEXT.__gcc_except_tab: 0x6d60
+  __TEXT.__objc_classname: 0x22b5
+  __TEXT.__objc_methname: 0x2a158
+  __TEXT.__objc_methtype: 0x963b
   __TEXT.__dlopen_cstrs: 0x26a
   __TEXT.__ustring: 0x28
-  __TEXT.__unwind_info: 0x6318
-  __DATA_CONST.__auth_got: 0x1c70
+  __TEXT.__unwind_info: 0x63b8
+  __DATA_CONST.__auth_got: 0x1c80
   __DATA_CONST.__got: 0x8f8
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0x135e0
-  __DATA_CONST.__cfstring: 0x1acc0
-  __DATA_CONST.__objc_classlist: 0x890
+  __DATA_CONST.__const: 0x136f0
+  __DATA_CONST.__cfstring: 0x1b080
+  __DATA_CONST.__objc_classlist: 0x8a0
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0x208
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_intobj: 0x13e0
+  __DATA_CONST.__objc_protorefs: 0x60
+  __DATA_CONST.__objc_classrefs: 0xd08
+  __DATA_CONST.__objc_superrefs: 0x7f0
+  __DATA_CONST.__objc_intobj: 0x1428
   __DATA_CONST.__objc_arraydata: 0x468
   __DATA_CONST.__objc_arrayobj: 0x3d8
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA.__objc_const: 0x238e0
-  __DATA.__objc_selrefs: 0x8948
-  __DATA.__objc_protorefs: 0x60
-  __DATA.__objc_classrefs: 0xcf8
-  __DATA.__objc_superrefs: 0x7e8
-  __DATA.__objc_ivar: 0x18a8
-  __DATA.__objc_data: 0x55a0
-  __DATA.__data: 0x1fe8
+  __DATA.__objc_const: 0x23c48
+  __DATA.__objc_selrefs: 0x8a28
+  __DATA.__objc_ivar: 0x18e0
+  __DATA.__objc_data: 0x5640
+  __DATA.__data: 0x2038
   __DATA.__thread_vars: 0xc0
   __DATA.__thread_bss: 0x1a
-  __DATA.__bss: 0xa60
+  __DATA.__bss: 0xaa0
   __DATA.__common: 0x10
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 45E28C5C-96AA-346A-B3AF-47F4F86F55BD
-  Functions: 9182
-  Symbols:   1368
-  CStrings:  18677
+  UUID: 3A88B79D-B2E9-3877-B18C-7160F8126E7E
+  Functions: 9245
+  Symbols:   1370
+  CStrings:  18825
 
Symbols:
+ _CKUnderlyingErrorDomain
+ _arc4random_uniform
+ _calloc
- _CKInternalErrorDomain
CStrings:
+ "\x125\x13"
+ "\x13\x14"
+ "\x19"
+ "!#\x12\x12"
+ "(%@ is NULL OR (%@ IS NOT NULL AND %@%@(?)))"
+ "-[CuttlefishXPCWrapper handleEvictedMachineIDsWithSpecificUser:machineIDs:reply:]_block_invoke"
+ "-[CuttlefishXPCWrapper handleRemovedMachineIDsDueToUnknownReasonsWithSpecificUser:machineIDs:reply:]_block_invoke"
+ "-[CuttlefishXPCWrapper setAllowedMachineIDsWithSpecificUser:allowedMachineIDs:userInitiatedRemovals:evictedRemovals:unknownReasonRemovals:honorIDMSListChanges:version:reply:]_block_invoke"
+ "-[CuttlefishXPCWrapper vouchWithRerollWithSpecificUser:oldPeerID:tlkShares:reply:]_block_invoke"
+ "3Q"
+ "<HealthCheckResult: postRepairCFU: %@, postEscrowCFU: %@, resetOctagon: %@, leaveTrust: %@, reroll: %@, moveRequest? %@, totalEscrowRecords: %llu, collectableEscrowRecords: %llu, collectedEscrowRecords: %llu, escrowRecordGarbageCollectionEnabled: %@, totalTlkShares: %llu, collectableTlkShares: %llu, collectedTlkShares: %llu, tlkShareGarbageCollectionEnabled: %@, totalPeers: %llu, trustedPeers: %llu, superfluousPeers: %llu, peersCleanedup: %llu, superfluousPeersCleanupEnabled: %@>"
+ "@136@0:8B16B20B24B28B32@36Q44Q52Q60B68Q72Q80Q88B96Q100Q108Q116Q124B132"
+ "@76@0:8@16@24@32@40@48@56@64B72"
+ "AAFAnalyticsEvent"
+ "AAFAnalyticsEvent+Security.m"
+ "AKAccountManager"
+ "An operation of this type is already enqueued"
+ "B24@0:8^{rusage_info_v6=[16C]QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ[12Q]}16"
+ "CKKSSQLWhereNullOrValue"
+ "Cannot find an account matching primary persona/altDSID, allowing default context return: %@ %@"
+ "Cannot resync due to failure to fetch all CK groups: %@"
+ "Class getAAFAnalyticsEventClass(void)_block_invoke"
+ "Class getAKAccountManagerClass(void)_block_invoke"
+ "CloudKit is presumably down; scheduling upload after %d seconds"
+ "CloudKit reports no private and no shared groups, returning early from resync"
+ "Couldn't fetch OQE %@: %@"
+ "Couldn't save OQE %@ as %@: %@"
+ "Current state: '%@'"
+ "CurrentUserMetadata for key %@ already at new value (or removed)"
+ "Device evicted due to limit for (%@) version %@: %@"
+ "Device evicted for unknown reason for (%@) version %@: %@"
+ "Error while serializing identifiers: %@"
+ "Failed resync during merge: %@"
+ "Failed to complete CloudKit group fetch before deadline"
+ "Failed to fetch all known CloudKit groups: %@"
+ "Failed to set feature usage to %lu: %@"
+ "Fetched all known CloudKit groups"
+ "HomePod unexpectedly lost CDP trust (please do not file this radar if you performed Reset Protected Data on another device, or otherwise intended to cause CDP trust loss on this HomePod). To disable this prompt for testing, turn off the Security/TTRTrustLossOnHomePod feature flag on the HomePod.\n\n%@"
+ "Ignoring Private DB CKRecordZone with non-group zoneID: %{public}@"
+ "Ignoring Shared DB CKRecordZone with non-group zoneID: %{public}@"
+ "Ignoring reroll signal"
+ "KCSharing appears not to be in use, foregoing resync"
+ "KCSharing appears not to be in use, resyncing anyway because RPC"
+ "KCSharing feature usage: %lu, proceeding with resync"
+ "KCSharingPerformResync"
+ "KCSharingSyncController.m"
+ "Must provide all arguments to this function"
+ "Must supply arguments to this function"
+ "NSString *getkAAFDeviceSessionId(void)"
+ "NSString *getkAAFFlowId(void)"
+ "Not passing a completion handler here is a bug"
+ "Not setting up maintenance: have extant operation"
+ "Not setting up resync: have extant operation"
+ "OTVouchWithRerollOperation"
+ "Object Size (%lu bytes) too large: %@ %{private}@"
+ "Object size too large"
+ "OctagonActivityReroll"
+ "OctagonAllStates"
+ "OctagonEventReroll"
+ "OctagonEventVoucherWithReroll"
+ "OctagonReadyStates"
+ "OctagonStateCreateIdentityForReroll"
+ "OctagonStateStashAccountSettingsForReroll"
+ "OctagonStateVouchWithReroll"
+ "PushResetCircle"
+ "Rejecting a reroll RPC for arguments (%@): %@"
+ "Requesting maintenance"
+ "Requesting resync"
+ "Resync complete"
+ "Resync failed: %@"
+ "Resync: kicking off full CK fetch"
+ "Resync: obtaining list of groups from CloudKit"
+ "Resync: setting change tokens to nil"
+ "Returning from cuttlefish trust check call: postRepairCFU(%d), postEscrowCFU(%d), resetOctagon(%d), leaveTrust(%d), reroll(%d), moveRequest(%d), results=%@"
+ "SELECT %1$@, o.rowid, o.data           FROM sharingIncomingQueue i           JOIN sharingOutgoingQueue o ON (o.agrp, o.ownr, o.zone, o.uuid) = (i.agrp, i.ownr, i.zone, i.uuid)           WHERE i.agrp = ?1 AND                 o.deln AND                 NOT i.deln AND                 NOT EXISTS (                     SELECT 1 FROM sharingIncomingQueue ish                     WHERE (ish.agrp, ish.ownr, ish.zone, ish.uuid) = (i.agrp, i.ownr, i.zone, ?2) AND                           ish.deln                 ) AND                 NOT EXISTS (                     SELECT 1 FROM sharingOutgoingQueue osh                     WHERE (osh.agrp, osh.ownr, osh.zone, osh.uuid) = (i.agrp, i.ownr, i.zone, ?2) AND                           osh.deln                 )"
+ "Saving OQE %@ scheduled for retry at: %@"
+ "Scheduled resync complete 🎉"
+ "Setting private DB change token to nil for zoneID %@"
+ "Setting private credential purge time to %lld minutes"
+ "Setting shared DB change token to nil for zoneID %@"
+ "Starting resync operation with merge"
+ "Successfully vouched with a reroll: %@, %@"
+ "T@\"NSError\",&,V_descriptionUnderlyingError"
+ "T@\"NSString\",&,N,V_oldPeerID"
+ "T@\"NSString\",&,V_oldPeerID"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",R,N,V_recordChangeTag"
+ "TB,V_reroll"
+ "Unable to complete scheduled resync: %@"
+ "Unable to find Apple account matching primary persona (nil)"
+ "Unmirrored %@ CloudKit zones: %{public}@"
+ "User initiated removed machine ID for (%@) version %@: %@"
+ "Verification complete, groups %@ in sync"
+ "_descriptionUnderlyingError"
+ "_maintenanceOperation"
+ "_oldPeerID"
+ "_onQueueFetchRemoteChangesForZoneIDs:completion:"
+ "_onqueueRegisterMultiStateArrivalWatcher:startTimeout:"
+ "_onqueueSaveRecordsWithDelay:viewState:"
+ "_recordChangeTag"
+ "_reroll"
+ "_resyncOperation"
+ "accountAccessTelemetryOptInForAccount:"
+ "afterAuthKitFetch:userInitiatedRemovals:evictedRemovals:unknownReasonRemovals:accountIsDemo:version:"
+ "archivedDataWithRootObject:"
+ "are"
+ "aren't"
+ "authkit: super shrug here. Device is in the deletedDeviceList but has an undefined removal reason (%ld) for (%@) version %@: %@"
+ "authoritativeGroupFetch"
+ "changeTag"
+ "checkIfPasscodeIsSetForDevice is %{BOOL}d"
+ "com.apple.ckks.state"
+ "com.apple.security.aafanalyticsevent.queue"
+ "com.apple.security.octagon.client"
+ "com.apple.securityd.kcsharing.resync"
+ "createSuccessfulFetchDependency"
+ "creating aps rate limiter with min initial delay of %llu"
+ "creating voucher for reroll"
+ "currentUserMetadataFeatureUsage"
+ "deletedDeviceList"
+ "descriptionUnderlyingError"
+ "fetchAllViableBottles:source:reply:"
+ "handleEvictedMachineIDsWithSpecificUser:machineIDs:reply:"
+ "handleExternalClientStateMachineRequest:client:timeout:"
+ "handleExternalRequest:startTimeout:"
+ "handleRemovedMachineIDsDueToUnknownReasonsWithSpecificUser:machineIDs:reply:"
+ "hasOldPeerID"
+ "haveUnmirroredGroups:forDatabase:"
+ "init:sourceStates:serialQueue:transitionOp:"
+ "initWithDeletedRecord:"
+ "initWithDependencies:intendedState:errorState:saveVoucher:"
+ "initWithEventName:eventCategory:initData:"
+ "initWithPlaceholderOutgoingDatabaseItem:error:"
+ "initWithPostRepairCFU:postEscrowCFU:resetOctagon:leaveTrust:reroll:moveRequest:totalEscrowRecords:collectableEscrowRecords:collectedEscrowRecords:escrowRecordGarbageCollectionEnabled:totalTlkShares:collectableTlkShares:collectedTlkShares:tlkShareGarbageCollectionEnabled:totalPeers:trustedPeers:superfluousPeers:peersCleanedup:superfluousPeersCleanupEnabled:"
+ "initWithStore:queue:container:privateSyncEngine:sharedSyncEngine:messagingdConnection:lockStateTracker:forTesting:"
+ "isCKInternalServerHTTPError"
+ "isFullPeer:"
+ "isInUse"
+ "kAAFDeviceSessionId"
+ "kAAFFlowId"
+ "machine ID list notification -- refreshing device list"
+ "max splay window seconds for limiter %d"
+ "model_id"
+ "notificationOfMachineIDListChange"
+ "obtainAuthoritativeGroupsForPrivate:shared:error:"
+ "octagon-count-trusted-peers"
+ "octagon-health: aks_get_device_state failed with: %d"
+ "octagon: Error loading account metadata: %@"
+ "octagon: Error preparing voucher using reroll: %@"
+ "oldPeerID"
+ "onqueueHandleStartTimeout:"
+ "os_version"
+ "peer_id"
+ "postHomePodLostTrustTTR:"
+ "primaryAuthKitAccount"
+ "privateDB"
+ "received notifyAKDeviceListDeltaMessagePayload"
+ "registerMultiStateArrivalWatcher:startTimeout:"
+ "registerStateTransitionWatcher:startTimeout:"
+ "removalReason"
+ "reroll"
+ "reroll invoked for arguments (%@)"
+ "reroll:reply:"
+ "rerollWithReply:"
+ "resyncFromRPC:completion:"
+ "resyncWithCompletion:"
+ "serial"
+ "serializeRecordIDAndChangeTag"
+ "setAllowedMachineIDsWithSpecificUser:allowedMachineIDs:userInitiatedRemovals:evictedRemovals:unknownReasonRemovals:honorIDMSListChanges:version:reply:"
+ "setCurrentUserMetadataFeatureUsage:"
+ "setDescriptionUnderlyingError:"
+ "setFeatureInUse"
+ "setOldPeerID:"
+ "setRecordIDAndChangeTagFromData:error:"
+ "setReroll:"
+ "setServerChangeToken:forZoneID:"
+ "setServerChangeTokenForDatabase:"
+ "sharedDB"
+ "stageOutgoingShares:deletionsForShares:error:"
+ "telemetryDeviceSessionIDForAccount:"
+ "timeoutErrorForState:"
+ "totalTrustedPeers errored: %@"
+ "totalTrustedPeers succeeded, total count: %@"
+ "unarchivedDictionaryWithKeysOfClass:objectsOfClass:fromData:error:"
+ "unmirroredZonesForPrivate:shared:error:"
+ "v24@0:8@\"NSError\"16"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSSet\"@\"NSSet\"@\"NSSet\"@\"NSSet\"@\"NSString\"@\"NSError\">24"
+ "v40@0:8@\"OTControlArguments\"16q24@?<v@?@\"NSArray\"@\"NSArray\"@\"NSError\">32"
+ "v48@0:8@\"TPSpecificUser\"16@\"NSString\"24@\"NSArray\"32@?<v@?@\"NSData\"@\"NSData\"@\"NSArray\"@\"TrustedPeersHelperTLKRecoveryResult\"@\"NSError\">40"
+ "v56@?0@\"NSSet\"8@\"NSSet\"16@\"NSSet\"24@\"NSSet\"32@\"NSString\"40@\"NSError\"48"
+ "v60@0:8@16@24@32@40B48@52"
+ "v76@0:8@\"TPSpecificUser\"16@\"NSSet\"24@\"NSSet\"32@\"NSSet\"40@\"NSSet\"48B56@\"NSString\"60@?<v@?B@\"NSError\">68"
+ "v76@0:8@16@24@32@40@48B56@60@?68"
+ "void *AuthKitLibrary(void)"
+ "vouchWithRerollWithSpecificUser:oldPeerID:tlkShares:reply:"
- "\x12\x16\x12"
- "\x13\x13"
- "\x17"
- "!\"\x12\x12"
- "-[CuttlefishXPCWrapper addAllowedMachineIDsWithSpecificUser:machineIDs:reply:]_block_invoke"
- "-[CuttlefishXPCWrapper pushHealthInquiryWithSpecificUser:reply:]_block_invoke"
- "-[CuttlefishXPCWrapper removeAllowedMachineIDsWithSpecificUser:machineIDs:reply:]_block_invoke"
- "-[CuttlefishXPCWrapper reportHealthWithSpecificUser:stateMachineState:trustState:reply:]_block_invoke"
- "-[CuttlefishXPCWrapper setAllowedMachineIDsWithSpecificUser:allowedMachineIDs:honorIDMSListChanges:version:reply:]_block_invoke"
- "1a"
- "<HealthCheckResult: postRepairCFU: %@, postEscrowCFU: %@, resetOctagon: %@, leaveTrust: %@, moveRequest? %@, totalEscrowRecords: %llu, collectableEscrowRecords: %llu, collectedEscrowRecords: %llu, escrowRecordGarbageCollectionEnabled: %@, totalTlkShares: %llu, collectableTlkShares: %llu, collectedTlkShares: %llu, tlkShareGarbageCollectionEnabled: %@, totalPeers: %llu, trustedPeers: %llu, superfluousPeers: %llu, peersCleanedup: %llu, superfluousPeersCleanupEnabled: %@>"
- "@132@0:8B16B20B24B28@32Q40Q48Q56B64Q68Q76Q84B92Q96Q104Q112Q120B128"
- "@56@0:8@16@24@32Q40@48"
- "B24@0:8^{rusage_info_v6=[16C]QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ[14Q]}16"
- "Cannot find an account matching persona/altDSID, allowing default context return: %@ %@"
- "HomePod unexpectedly lost CDP trust (please do not file this radar if you performed Reset Protected Data on another device, or otherwise intended to cause CDP trust loss on this HomePod). To disable this prompt for testing, turn off the Security/TTRTrustLossOnHomePod feature flag on the HomePod."
- "Machines-added push is for wrong altDSID (%@); current altDSID (%@)"
- "Machines-removed push is for wrong altDSID (%@); current altDSID (%@)"
- "Remote CloudKit zone %{public}@ not found in local mirror!"
- "Remote CloudKit zones: %{public}@"
- "Returning from cuttlefish trust check call: postRepairCFU(%d), postEscrowCFU(%d), resetOctagon(%d), leaveTrust(%d), moveRequest(%d), results=%@"
- "SELECT %1$@, o.rowid           FROM sharingIncomingQueue i           JOIN sharingOutgoingQueue o ON (o.agrp, o.ownr, o.zone, o.uuid) = (i.agrp, i.ownr, i.zone, i.uuid)           WHERE i.agrp = ?1 AND                 o.deln AND                 NOT i.deln AND                 NOT EXISTS (                     SELECT 1 FROM sharingIncomingQueue ish                     WHERE (ish.agrp, ish.ownr, ish.zone, ish.uuid) = (i.agrp, i.ownr, i.zone, ?2) AND                           ish.deln                 ) AND                 NOT EXISTS (                     SELECT 1 FROM sharingOutgoingQueue osh                     WHERE (osh.agrp, osh.ownr, osh.zone, osh.uuid) = (i.agrp, i.ownr, i.zone, ?2) AND                           osh.deln                 )"
- "Setting private credential purge time to %llu minutes"
- "Starting maintenance"
- "T@\"CKKSResultOperation\",&,V_initialTimeoutListenerOp"
- "Verified local and remote groups are in sync"
- "_initialTimeoutListenerOp"
- "_onqueuePerformTimeoutWithUnderlyingError"
- "_onqueuePerformTimeoutWithUnderlyingError:"
- "_onqueueRegisterMultiStateArrivalWatcher:"
- "addAllow succeeded"
- "addAllowedMachineIDsWithSpecificUser:machineIDs:reply:"
- "adding machines for altDSID(%@): %@"
- "afterAuthKitFetch:accountIsDemo:version:"
- "com.appple.ckks.state"
- "createSuccesfulFetchDependency"
- "creating aps rate limiter"
- "deliverAKDeviceListDelta:reply:"
- "fetchAllViableBottles:reply:"
- "handleExternalClientStateMachineRequest:client:"
- "handleExternalRequest:"
- "handleHealthRequest"
- "incomplete machine ID list notification -- refreshing device list"
- "incompleteNotificationOfMachineIDListChange"
- "init:sourceStates:serialQueue:timeout:transitionOp:"
- "initWithDeletedRecordID:"
- "initWithPostRepairCFU:postEscrowCFU:resetOctagon:leaveTrust:moveRequest:totalEscrowRecords:collectableEscrowRecords:collectedEscrowRecords:escrowRecordGarbageCollectionEnabled:totalTlkShares:collectableTlkShares:collectedTlkShares:tlkShareGarbageCollectionEnabled:totalPeers:trustedPeers:superfluousPeers:peersCleanedup:superfluousPeersCleanupEnabled:"
- "initWithResponseBody:"
- "initialTimeoutListenerOp"
- "kvsSendAccountChangedWithDSID:err:"
- "machinesAdded:altDSID:"
- "machinesRemoved:altDSID:"
- "octagon-authkit: Unable to load account metadata: %@"
- "octagon-authkit: addAllow errored: %@"
- "octagon-authkit: removeAllow errored: %@"
- "octagon: health report is lost: %@"
- "partial push or no machine IDs in list; treating as incomplete"
- "postHomePodLostTrustTTR"
- "pushHealthInquiryWithSpecificUser:reply:"
- "received notifyAKDeviceListDeltaMessagePayload: %@, parsed payload: %{BOOL}d"
- "registerMultiStateArrivalWatcher:"
- "registerStateTransitionWatcher:"
- "removeAllow succeeded"
- "removeAllowedMachineIDsWithSpecificUser:machineIDs:reply:"
- "removing machines for altDSID(%@): %@"
- "reportHealthWithSpecificUser:stateMachineState:trustState:reply:"
- "setAllowedMachineIDsWithSpecificUser:allowedMachineIDs:honorIDMSListChanges:version:reply:"
- "setInitialTimeoutListenerOp:"
- "stageOutgoingShares:deletionsForShareIDs:error:"
- "v32@0:8@\"NSArray\"16@\"NSString\"24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSSet\"@\"NSString\"@\"NSError\">24"
- "v32@0:8@\"OTControlArguments\"16@?<v@?@\"NSArray\"@\"NSArray\"@\"NSError\">24"
- "v32@?0@\"NSSet\"8@\"NSString\"16@\"NSError\"24"
- "v40@0:8@\"TPSpecificUser\"16@\"NSArray\"24@?<v@?@\"NSError\">32"
- "v48@0:8@\"TPSpecificUser\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSError\">40"
- "v52@0:8@\"TPSpecificUser\"16@\"NSSet\"24B32@\"NSString\"36@?<v@?B@\"NSError\">44"
- "v52@0:8@16@24B32@36@?44"
- "verifyGroupsInSync"
- "watcher-timeout-%@"

```
