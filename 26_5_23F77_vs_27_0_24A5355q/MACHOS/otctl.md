## otctl

> `/usr/sbin/otctl`

```diff

-61901.120.67.0.0
-  __TEXT.__text: 0x15a34
-  __TEXT.__auth_stubs: 0x590
-  __TEXT.__objc_stubs: 0x2400
-  __TEXT.__objc_methlist: 0xcd4
-  __TEXT.__const: 0x78
-  __TEXT.__gcc_except_tab: 0x74c
-  __TEXT.__objc_methname: 0x3adb
-  __TEXT.__cstring: 0x3336
-  __TEXT.__objc_classname: 0xb8
-  __TEXT.__objc_methtype: 0x4f4
-  __TEXT.__oslogstring: 0xa5
-  __TEXT.__unwind_info: 0x538
-  __DATA_CONST.__auth_got: 0x2d8
-  __DATA_CONST.__got: 0x180
-  __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x460
-  __DATA_CONST.__cfstring: 0xf20
+62426.0.0.0.4
+  __TEXT.__text: 0x18be4
+  __TEXT.__auth_stubs: 0x5d0
+  __TEXT.__objc_stubs: 0x2660
+  __TEXT.__objc_methlist: 0xd74
+  __TEXT.__const: 0xa8
+  __TEXT.__gcc_except_tab: 0x798
+  __TEXT.__objc_methname: 0x3de6
+  __TEXT.__cstring: 0x3a9e
+  __TEXT.__objc_classname: 0xad
+  __TEXT.__objc_methtype: 0x4fa
+  __TEXT.__oslogstring: 0xa42
+  __TEXT.__unwind_info: 0x518
+  __DATA_CONST.__const: 0x4b8
+  __DATA_CONST.__cfstring: 0x11c0
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18

   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__objc_dictobj: 0x78
-  __DATA.__objc_const: 0xf00
-  __DATA.__objc_selrefs: 0xde0
-  __DATA.__objc_ivar: 0xc8
+  __DATA_CONST.__auth_got: 0x2f8
+  __DATA_CONST.__got: 0x190
+  __DATA_CONST.__auth_ptr: 0x8
+  __DATA.__objc_const: 0xff0
+  __DATA.__objc_selrefs: 0xe98
+  __DATA.__objc_ivar: 0xd8
   __DATA.__objc_data: 0x190
   __DATA.__data: 0x128
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4CBB22B8-3B3B-322A-AC68-0584A1D1B562
-  Functions: 326
-  Symbols:   150
-  CStrings:  1252
+  UUID: FA6B4706-E660-3B82-A59F-A404753D606D
+  Functions: 343
+  Symbols:   156
+  CStrings:  1425
 
Symbols:
+ _OBJC_CLASS_$_NSNull
+ __os_log_default
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x3
+ _objc_retain_x5
+ _objc_retain_x6
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "    - %s\n"
+ "    - {\"machineID\": \"%s\", \"sdid\": \"%s\", \"lduid\": \"%s\", \"trustTimestamp\": \"%s\"}\n"
+ "  (null)"
+ "  Deleted Device Hash:              %s\n"
+ "  Evicted Removals:                 %lu devices\n"
+ "  IDMS Devices Version:             %s\n"
+ "  Machine IDs:                      %lu devices\n"
+ "  Stable Trusted Device IDs:        %lu pairs\n"
+ "  Trusted Device Hash:              %s\n"
+ "  Unknown Reason Removals:          %lu devices\n"
+ "  Update Timestamp:                 %s\n"
+ "  User-Initiated Removals:          %lu devices\n"
+ "  Version:                          %s\n"
+ "  idMS_trust_timestamp: %s\n"
+ "  lduid:                %s\n"
+ "  sdid:                 %s\n"
+ "(null)"
+ "<HealthCheckResult: postRepairCFU: %@, postEscrowCFU: %@, resetOctagon: %@, leaveTrust: %@, reroll: %@, stableTrustedDeviceIDReroll: %@, totalEscrowRecords: %llu, collectableEscrowRecords: %llu, collectedEscrowRecords: %llu, escrowRecordGarbageCollectionEnabled: %@, totalTlkShares: %llu, collectableTlkShares: %llu, collectedTlkShares: %llu, tlkShareGarbageCollectionEnabled: %@, totalPeers: %llu, trustedPeers: %llu, superfluousPeers: %llu, peersCleanedup: %llu, superfluousPeersCleanupEnabled: %@>"
+ "@132@0:8B16B20B24B28B32B36Q40Q48Q56B64Q68Q76Q84B92Q96Q104Q112Q120B128"
+ "Account Metadata:"
+ "AuthKit:"
+ "Error fetching trusted device list: %s\n"
+ "Error rerolling for stable trusted device ID: %s\n"
+ "Error:            %s\n"
+ "Fetch stable trusted device ID from both AuthKit and cached metadata"
+ "Fetch trusted device list from AuthKit"
+ "Force stable trusted device ID reroll as part of health check"
+ "Matching:         %s\n"
+ "Reroll PeerID for stable trusted device ID"
+ "Reroll for stable trusted device ID successful."
+ "T@\"NSString\",&,N,V_idMSTrustTimestamp"
+ "T@\"NSString\",&,N,V_lduid"
+ "T@\"NSString\",&,N,V_sdid"
+ "TB,V_stableTrustedDeviceIDReroll"
+ "Trusted Device List:"
+ "_idMSTrustTimestamp"
+ "_lduid"
+ "_sdid"
+ "_stableTrustedDeviceIDReroll"
+ "account_metadata_stable_trusted_device_id"
+ "allObjects"
+ "authkit_stable_trusted_device_id"
+ "compare:"
+ "deleted_device_hash"
+ "evicted_removals"
+ "fetch-stable-trusted-device-id"
+ "fetch-tdl"
+ "fetchStableTrustedDeviceID:reply:"
+ "fetchStableTrustedDeviceIDWithArguments:json:"
+ "fetchTrustedDeviceList:reply:"
+ "fetchTrustedDeviceListWithArguments:json:"
+ "forceStableTrustedDeviceIDReroll"
+ "hasIdMSTrustTimestamp"
+ "hasLduid"
+ "hasSdid"
+ "healthCheck:skipRateLimitingCheck:repair:danglingPeerCleanup:caesarPeerCleanup:updateIdMS:forceStableTrustedDeviceIDReroll:json:"
+ "healthCheck:skipRateLimitingCheck:repair:danglingPeerCleanup:caesarPeerCleanup:updateIdMS:forceStableTrustedDeviceIDReroll:reply:"
+ "honor_idms_list_changes"
+ "i52@0:8@16B24B28B32B36B40B44B48"
+ "idMSTrustTimestamp"
+ "idMS_trust_timestamp"
+ "idms_trust_timestamp"
+ "idms_trusted_devices_version"
+ "initWithPostRepairCFU:postEscrowCFU:resetOctagon:leaveTrust:reroll:stableTrustedDeviceIDReroll:totalEscrowRecords:collectableEscrowRecords:collectedEscrowRecords:escrowRecordGarbageCollectionEnabled:totalTlkShares:collectableTlkShares:collectedTlkShares:tlkShareGarbageCollectionEnabled:totalPeers:trustedPeers:superfluousPeers:peersCleanedup:superfluousPeersCleanupEnabled:"
+ "lduid"
+ "machine_id"
+ "machine_ids"
+ "matching"
+ "mid_stable_trusted_device_ids"
+ "nil"
+ "null"
+ "operation: allBottles"
+ "operation: check-custodian-recovery-key, uuid: %@"
+ "operation: check-inheritance-key, uuid: %@"
+ "operation: check-recovery-key"
+ "operation: ckks-policy"
+ "operation: create-custodian-recovery-key, uuid: %@"
+ "operation: create-inheritance-key, uuid: %@"
+ "operation: create-inheritance-key-with-claim-wrapping, uuid: %@"
+ "operation: depart"
+ "operation: disable-walrus"
+ "operation: disable-webaccess"
+ "operation: enable-walrus"
+ "operation: enable-webaccess"
+ "operation: er-reset"
+ "operation: er-status"
+ "operation: er-store"
+ "operation: er-trigger"
+ "operation: escrowCheck"
+ "operation: fetch-account-state"
+ "operation: fetch-account-wide-state, forceFetch: %d"
+ "operation: fetch-account-wide-state-default, forceFetch: %d"
+ "operation: fetch-stable-trusted-device-id"
+ "operation: fetch-tdl"
+ "operation: fetchAllEscrowRecords"
+ "operation: fetchEscrowRecords"
+ "operation: generate-inheritance-key"
+ "operation: health, skipRateLimiting: %d, repair: %d, danglingPeerCleanup: %d, caesarPeerCleanup: %d, updateIdMS: %d, forceStableTrustedDeviceIDReroll: %d"
+ "operation: icsc-repair-reset"
+ "operation: join-with-custodian-recovery-key, uuid: %@"
+ "operation: join-with-inheritance-key, uuid: %@"
+ "operation: join-with-recovery-key"
+ "operation: performCKServerUnreadableDataRemoval, appleID: %@, dsid: %@"
+ "operation: preflight-join-with-custodian-recovery-key, uuid: %@"
+ "operation: preflight-join-with-inheritance-key, uuid: %@"
+ "operation: preflight-join-with-recovery-key"
+ "operation: print-account-metadata"
+ "operation: recover, bottleID: %@"
+ "operation: recover-record, recordID: %s, appleID: %@"
+ "operation: recover-record-silent, appleID: %@"
+ "operation: recreate-inheritance-key, uuid: %@"
+ "operation: remove-custodian-recovery-key, uuid: %@"
+ "operation: remove-inheritance-key, uuid: %@"
+ "operation: remove-recovery-key"
+ "operation: reroll"
+ "operation: reroll-stable-device-id"
+ "operation: reset, appleID: %@, dsid: %@"
+ "operation: reset-account-cdp-contents, notifyIdMS: %d"
+ "operation: resetProtectedData, appleID: %@, dsid: %@, notifyIdMS: %d"
+ "operation: resetoctagon, notifyIdMS: %d, timeout: %f"
+ "operation: set-machine-id-override, machineID: %s"
+ "operation: set-recovery-key"
+ "operation: sign-in"
+ "operation: sign-out"
+ "operation: simulate-receive-push"
+ "operation: simulate-receive-tdl-push"
+ "operation: start"
+ "operation: status"
+ "operation: store-inheritance-key, uuid: %@"
+ "operation: taptoradar"
+ "operation: tlk-recoverability"
+ "operation: total-trusted-peers"
+ "operation: trusted-full-peers"
+ "operation: user-controllable-views, enable: %d, pause: %d"
+ "reroll-stable-device-id"
+ "rerollForStableTrustedDeviceID:reply:"
+ "rerollForStableTrustedDeviceIDWithArguments:json:"
+ "sdid"
+ "setIdMSTrustTimestamp:"
+ "setLduid:"
+ "setSdid:"
+ "setStableTrustedDeviceIDReroll:"
+ "setStableTrustedDeviceIDStatus:"
+ "sortedArrayUsingSelector:"
+ "stableID"
+ "stableTrustedDeviceIDReroll"
+ "trust_timestamp"
+ "trusted_device_hash"
+ "trusted_devices_update_timestamp"
+ "unknown_reason_removals"
+ "user_initiated_removals"
+ "v112@?0@\"NSSet\"8@\"NSSet\"16@\"NSSet\"24@\"NSSet\"32@\"NSString\"40@\"NSString\"48@\"NSString\"56@\"NSNumber\"64@\"NSString\"72@\"OTMetricsSessionData\"80@\"NSSet\"88q96@\"NSError\"104"
+ "v32@?0@\"TPStableTrustedDeviceID\"8@\"TPStableTrustedDeviceID\"16@\"NSError\"24"
+ "version"
- "<HealthCheckResult: postRepairCFU: %@, postEscrowCFU: %@, resetOctagon: %@, leaveTrust: %@, reroll: %@, totalEscrowRecords: %llu, collectableEscrowRecords: %llu, collectedEscrowRecords: %llu, escrowRecordGarbageCollectionEnabled: %@, totalTlkShares: %llu, collectableTlkShares: %llu, collectedTlkShares: %llu, tlkShareGarbageCollectionEnabled: %@, totalPeers: %llu, trustedPeers: %llu, superfluousPeers: %llu, peersCleanedup: %llu, superfluousPeersCleanupEnabled: %@>"
- "@128@0:8B16B20B24B28B32Q36Q44Q52B60Q64Q72Q80B88Q92Q100Q108Q116B124"
- "healthCheck:skipRateLimitingCheck:repair:danglingPeerCleanup:caesarPeerCleanup:updateIdMS:json:"
- "healthCheck:skipRateLimitingCheck:repair:danglingPeerCleanup:caesarPeerCleanup:updateIdMS:reply:"
- "i48@0:8@16B24B28B32B36B40B44"
- "initWithPostRepairCFU:postEscrowCFU:resetOctagon:leaveTrust:reroll:totalEscrowRecords:collectableEscrowRecords:collectedEscrowRecords:escrowRecordGarbageCollectionEnabled:totalTlkShares:collectableTlkShares:collectedTlkShares:tlkShareGarbageCollectionEnabled:totalPeers:trustedPeers:superfluousPeers:peersCleanedup:superfluousPeersCleanupEnabled:"

```
