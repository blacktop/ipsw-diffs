## securityd

> `/usr/libexec/securityd`

```diff

-61040.2.2.0.0
-  __TEXT.__text: 0x221338
+61040.42.1.0.0
+  __TEXT.__text: 0x223d28
   __TEXT.__auth_stubs: 0x38b0
-  __TEXT.__objc_stubs: 0x1a3a0
-  __TEXT.__objc_methlist: 0x12774
+  __TEXT.__objc_stubs: 0x1a580
+  __TEXT.__objc_methlist: 0x1295c
   __TEXT.__const: 0x62d
-  __TEXT.__cstring: 0x1e905
-  __TEXT.__oslogstring: 0x27c56
-  __TEXT.__gcc_except_tab: 0x69ec
-  __TEXT.__objc_classname: 0x2225
-  __TEXT.__objc_methname: 0x2887f
-  __TEXT.__objc_methtype: 0x918b
+  __TEXT.__cstring: 0x1edd7
+  __TEXT.__oslogstring: 0x27fef
+  __TEXT.__gcc_except_tab: 0x6a5c
+  __TEXT.__objc_classname: 0x224a
+  __TEXT.__objc_methname: 0x29031
+  __TEXT.__objc_methtype: 0x9268
   __TEXT.__dlopen_cstrs: 0x114
   __TEXT.__ustring: 0x28
-  __TEXT.__unwind_info: 0x61b4
+  __TEXT.__unwind_info: 0x623c
   __DATA_CONST.__auth_got: 0x1c68
   __DATA_CONST.__got: 0x8f0
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0x13338
-  __DATA_CONST.__cfstring: 0x19d60
-  __DATA_CONST.__objc_classlist: 0x878
+  __DATA_CONST.__const: 0x13380
+  __DATA_CONST.__cfstring: 0x1a120
+  __DATA_CONST.__objc_classlist: 0x880
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0x208
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x470
   __DATA_CONST.__objc_arrayobj: 0x3f0
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA.__objc_const: 0x22ed0
-  __DATA.__objc_selrefs: 0x8680
+  __DATA.__objc_const: 0x232f0
+  __DATA.__objc_selrefs: 0x8780
   __DATA.__objc_protorefs: 0x60
-  __DATA.__objc_classrefs: 0xcd8
-  __DATA.__objc_superrefs: 0x7d8
-  __DATA.__objc_ivar: 0x1808
-  __DATA.__objc_data: 0x54b0
-  __DATA.__data: 0x1fe0
+  __DATA.__objc_classrefs: 0xce8
+  __DATA.__objc_superrefs: 0x7e0
+  __DATA.__objc_ivar: 0x184c
+  __DATA.__objc_data: 0x5500
+  __DATA.__data: 0x1fe8
   __DATA.__thread_vars: 0xc0
   __DATA.__thread_bss: 0x1a
   __DATA.__bss: 0x9f8

   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: E64C58EE-B0CA-3F92-9728-B2CC0C9FD99B
-  Functions: 9044
-  Symbols:   1365
-  CStrings:  18204
+  UUID: 64686ED0-09C5-328E-881F-D5DCAEDFC4B3
+  Functions: 9090
+  Symbols:   1366
+  CStrings:  18351
 
Symbols:
+ _OBJC_CLASS_$_OTEscrowMoveRequestContext
CStrings:
+ "\x03\x12\x11\x11\x1f\x0f\t"
+ "-[CuttlefishXPCWrapper octagonContainsDistrustedRecoveryKeysWithSpecificUser:reply:]_block_invoke"
+ "114829039"
+ "<HealthCheckResult: postRepairCFU: %@, postEscrowCFU: %@, resetOctagon: %@, leaveTrust: %@, moveRequest? %@, totalEscrowRecords: %llu, collectableEscrowRecords: %llu, collectedEscrowRecords: %llu, escrowRecordGarbageCollectionEnabled: %@, totalTlkShares: %llu, collectableTlkShares: %llu, collectedTlkShares: %llu, tlkShareGarbageCollectionEnabled: %@, totalPeers: %llu, trustedPeers: %llu, superfluousPeers: %llu, peersCleanedup: %llu, superfluousPeersCleanupEnabled: %@>"
+ "@\"TrustedPeersHelperHealthCheckResult\""
+ "@132@0:8B16B20B24B28@32Q40Q48Q56B64Q68Q76Q84B92Q96Q104Q112Q120B128"
+ "@60@0:8@16@24@32@40B48B52B56"
+ "Cannot change SharingGroup using this API"
+ "Cannot delete shared item for unentitled client"
+ "Cannot send invitation for group, share didn't groupify"
+ "Cannot update shared item for unentitled client"
+ "Custodian key removal"
+ "Did not obtain group object for now-deleted group %@, can't cancel pending invitations"
+ "Failed to decline unusable invitation for groupID %{public}@: %{public}@"
+ "Failed to save recordID=%@ because we missed a deletion, will treat it as deletion now"
+ "Inheritance key removal"
+ "Please TTR unless you were just removing a legacy contact"
+ "Please TTR unless you were just removing a recovery contact"
+ "Preparing to delete inet rowid=%lli because of an incoming item deletion"
+ "Preparing to delete inet rowid=%lli because we deleted its ggrp"
+ "Preparing to delete keys rowid=%lli because of an incoming item deletion"
+ "Preparing to delete keys rowid=%lli because we deleted its ggrp"
+ "Rejecting a areRecoveryKeysDistrusted RPC for arguments (%@): %@"
+ "Returning from cuttlefish trust check call: postRepairCFU(%d), postEscrowCFU(%d), resetOctagon(%d), leaveTrust(%d), moveRequest(%d), results=%@"
+ "SOSAccountWriteEmptyCircleToKVS failed to create circle key: %@"
+ "SOSCCPushResetCircle_Server: error writing reset circle to kvs: %@"
+ "Sync error translation: seems we were offline for zoneID=%{public}@, returning translated error"
+ "Sync error translation: zoneID=%{public}@ did not error, returning nil"
+ "T@\"NSString\",&,N,V_circleName"
+ "T@\"SOSAccount\",&,N,V_account"
+ "T@\"TrustedPeersHelperHealthCheckResult\",&,V_results"
+ "TB,R,V_repair"
+ "TB,R,V_reportRateLimitingError"
+ "TB,R,V_skipRateLimitingCheck"
+ "TB,V_escrowRecordGarbageCollectionEnabled"
+ "TB,V_superfluousPeersCleanupEnabled"
+ "TB,V_tlkShareGarbageCollectionEnabled"
+ "TQ,V_collectableEscrowRecords"
+ "TQ,V_collectableTlkShares"
+ "TQ,V_collectedEscrowRecords"
+ "TQ,V_collectedTlkShares"
+ "TQ,V_peersCleanedup"
+ "TQ,V_superfluousPeers"
+ "TQ,V_totalEscrowRecords"
+ "TQ,V_totalPeers"
+ "TQ,V_totalTlkShares"
+ "TQ,V_trustedPeers"
+ "TTROnCRKRemoval"
+ "T^{__CFDictionary=},N,V_pending_changes"
+ "T^{__OpaqueSOSEngine=},N,V_engine"
+ "The Internet connection appears to be offline."
+ "TrustedPeersHelperHealthCheckResult"
+ "Zone ID \"%@\" did not contain KCSharingGroupID"
+ "^{__OpaqueSOSEngine=}"
+ "^{__OpaqueSOSEngine=}16@0:8"
+ "_circleName"
+ "_collectableEscrowRecords"
+ "_collectableTlkShares"
+ "_collectedEscrowRecords"
+ "_collectedTlkShares"
+ "_escrowRecordGarbageCollectionEnabled"
+ "_healthCheckResults"
+ "_peersCleanedup"
+ "_pending_changes"
+ "_reportRateLimitingError"
+ "_results"
+ "_superfluousPeers"
+ "_superfluousPeersCleanupEnabled"
+ "_tlkShareGarbageCollectionEnabled"
+ "_totalEscrowRecords"
+ "_totalPeers"
+ "_totalTlkShares"
+ "_trustedPeers"
+ "areRecoveryKeysDistrusted:"
+ "areRecoveryKeysDistrusted:reply:"
+ "bad response from AuthKit"
+ "collectableEscrowRecords"
+ "collectableTlkShares"
+ "collectedEscrowRecords"
+ "collectedTlkShares"
+ "cuttlefish came back with these suggestions: %@"
+ "escrowRecordGarbageCollectionEnabled"
+ "false"
+ "handleRepairSuggestions:"
+ "initWithDependencies:intendedState:errorState:deviceInfo:skipRateLimitedCheck:reportRateLimitingError:repair:"
+ "initWithPostRepairCFU:postEscrowCFU:resetOctagon:leaveTrust:moveRequest:totalEscrowRecords:collectableEscrowRecords:collectedEscrowRecords:escrowRecordGarbageCollectionEnabled:totalTlkShares:collectableTlkShares:collectedTlkShares:tlkShareGarbageCollectionEnabled:totalPeers:trustedPeers:superfluousPeers:peersCleanedup:superfluousPeersCleanupEnabled:"
+ "item's accessGroup '%@' not in %@"
+ "octagonContainsDistrustedRecoveryKeysWithSpecificUser:reply:"
+ "peersCleanedup"
+ "reportRateLimitingError"
+ "results"
+ "results=%@"
+ "setCollectableEscrowRecords:"
+ "setCollectableTlkShares:"
+ "setCollectedEscrowRecords:"
+ "setCollectedTlkShares:"
+ "setEscrowRecordGarbageCollectionEnabled:"
+ "setPeersCleanedup:"
+ "setResults:"
+ "setSuperfluousPeers:"
+ "setSuperfluousPeersCleanupEnabled:"
+ "setTlkShareGarbageCollectionEnabled:"
+ "setTotalEscrowRecords:"
+ "setTotalPeers:"
+ "setTotalTlkShares:"
+ "setTrustedPeers:"
+ "superfluousPeers"
+ "superfluousPeersCleanupEnabled"
+ "tlkShareGarbageCollectionEnabled"
+ "totalEscrowRecords"
+ "totalPeers"
+ "totalTlkShares"
+ "translateSyncErrorForGroupRequest:zoneID:"
+ "true"
+ "trustedPeers"
+ "unused"
+ "v24@0:8^{__OpaqueSOSEngine=}16"
+ "v24@?0@\"TrustedPeersHelperHealthCheckResult\"8@\"NSError\"16"
+ "v40@0:8@\"OTControlArguments\"16B24B28@?<v@?@\"TrustedPeersHelperHealthCheckResult\"@\"NSError\">32"
+ "v48@0:8@\"TPSpecificUser\"16B24B28@\"NSArray\"32@?<v@?@\"TrustedPeersHelperHealthCheckResult\"@\"NSError\">40"
- "\x03\x12\x11\x1f\x0f\t"
- "Failed to decline unusable invitation for groupID %{public}@"
- "Returning from cuttlefish trust check call: postRepairCFU(%d), postEscrowCFU(%d), resetOctagon(%d), leaveTrust(%d), moveRequest(%d)"
- "T@\"NSString\",&,VcircleName"
- "TB,V_repair"
- "TB,V_skipRateLimitingCheck"
- "T^v,Vengine"
- "T^{__CFDictionary=},Vpending_changes"
- "Zone ID did not contain KCSharingGroupID"
- "^v"
- "cuttlefish came back with these suggestions: post repair? %d, post escrow? %d, reset octagon? %d, leave trust? %d, move record? %d"
- "handleRepairSuggestions:postEscrowCFU:resetOctagon:leaveTrust:moveRequest:"
- "initWithDependencies:intendedState:errorState:deviceInfo:skipRateLimitedCheck:repair:"
- "items accessGroup '%@' not in %@"
- "setRepair:"
- "setSkipRateLimitingCheck:"
- "v24@0:8^v16"
- "v40@0:8@\"OTControlArguments\"16B24B28@?<v@?@\"NSError\">32"
- "v40@0:8B16B20B24B28@32"
- "v40@?0B8B12B16B20@\"OTEscrowMoveRequestContext\"24@\"NSError\"32"
- "v48@0:8@\"TPSpecificUser\"16B24B28@\"NSArray\"32@?<v@?BBBB@\"OTEscrowMoveRequestContext\"@\"NSError\">40"

```
