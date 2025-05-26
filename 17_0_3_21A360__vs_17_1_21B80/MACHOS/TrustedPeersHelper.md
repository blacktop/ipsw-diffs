## TrustedPeersHelper

> `/System/Library/Frameworks/Security.framework/XPCServices/TrustedPeersHelper.xpc/TrustedPeersHelper`

```diff

-61040.2.2.0.0
-  __TEXT.__text: 0x1c4354
-  __TEXT.__auth_stubs: 0x1b10
-  __TEXT.__objc_stubs: 0x24e0
-  __TEXT.__objc_methlist: 0x2584
-  __TEXT.__const: 0x9460
-  __TEXT.__objc_methname: 0x6f76
-  __TEXT.__cstring: 0x1a44f
+61040.42.1.0.0
+  __TEXT.__text: 0x1bed40
+  __TEXT.__auth_stubs: 0x1ae0
+  __TEXT.__objc_stubs: 0x2740
+  __TEXT.__objc_methlist: 0x27ac
+  __TEXT.__const: 0x8f90
+  __TEXT.__objc_methname: 0x777e
+  __TEXT.__cstring: 0x1acea
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x2ef8
-  __TEXT.__swift5_typeref: 0x3216
-  __TEXT.__swift5_fieldmd: 0x21fc
+  __TEXT.__constg_swiftt: 0x2fb0
+  __TEXT.__swift5_typeref: 0x3152
+  __TEXT.__swift5_fieldmd: 0x21c8
   __TEXT.__swift5_builtin: 0x8c
-  __TEXT.__swift5_reflstr: 0x1c0b
+  __TEXT.__swift5_reflstr: 0x1d3b
   __TEXT.__swift5_assocty: 0x288
-  __TEXT.__swift5_proto: 0x864
-  __TEXT.__swift5_types: 0x268
-  __TEXT.__objc_classname: 0x3ec
-  __TEXT.__objc_methtype: 0x1c56
+  __TEXT.__swift5_proto: 0x818
+  __TEXT.__swift5_types: 0x258
+  __TEXT.__objc_classname: 0x412
+  __TEXT.__objc_methtype: 0x1cbc
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__swift5_capture: 0x2fdc
+  __TEXT.__swift5_capture: 0x3050
   __TEXT.__swift5_protos: 0x18
-  __TEXT.__gcc_except_tab: 0xd4
+  __TEXT.__gcc_except_tab: 0xd8
   __TEXT.__oslogstring: 0x258
   __TEXT.__dlopen_cstrs: 0x66
-  __TEXT.__unwind_info: 0x4fac
-  __TEXT.__eh_frame: 0x5460
-  __DATA_CONST.__auth_got: 0xd98
-  __DATA_CONST.__got: 0x3f0
+  __TEXT.__unwind_info: 0x4cf0
+  __TEXT.__eh_frame: 0x52d8
+  __DATA_CONST.__auth_got: 0xd80
+  __DATA_CONST.__got: 0x3e8
   __DATA_CONST.__auth_ptr: 0x78
-  __DATA_CONST.__const: 0x8388
-  __DATA_CONST.__cfstring: 0x1ae0
-  __DATA_CONST.__objc_classlist: 0x218
+  __DATA_CONST.__const: 0x8470
+  __DATA_CONST.__cfstring: 0x1d80
+  __DATA_CONST.__objc_classlist: 0x228
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xc8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x6b60
-  __DATA.__objc_selrefs: 0x1b80
+  __DATA.__objc_const: 0x7198
+  __DATA.__objc_selrefs: 0x1cc0
   __DATA.__objc_protorefs: 0x50
-  __DATA.__objc_classrefs: 0x370
-  __DATA.__objc_superrefs: 0xe0
-  __DATA.__objc_ivar: 0x23c
-  __DATA.__objc_data: 0x2728
-  __DATA.__data: 0xe198
-  __DATA.__objc_stublist: 0xa0
-  __DATA.__common: 0x948
-  __DATA.__bss: 0x108c8
+  __DATA.__objc_classrefs: 0x378
+  __DATA.__objc_superrefs: 0xe8
+  __DATA.__objc_ivar: 0x284
+  __DATA.__objc_data: 0x2788
+  __DATA.__data: 0xe0c8
+  __DATA.__objc_stublist: 0x98
+  __DATA.__common: 0x8f0
+  __DATA.__bss: 0xff48
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 9791
+  Functions: 9657
   Symbols:   447
-  CStrings:  2874
+  CStrings:  3006
 
Symbols:
+ _OBJC_CLASS_$_TrustedPeersHelperHealthCheckResult
- _OBJC_METACLASS_$__TtCO18TrustedPeersHelper13CuttlefishAPI22ValidatePeersOperation
CStrings:
+ "\x11"
+ "<HealthCheckResult: postRepairCFU: %@, postEscrowCFU: %@, resetOctagon: %@, leaveTrust: %@, moveRequest? %@, totalEscrowRecords: %llu, collectableEscrowRecords: %llu, collectedEscrowRecords: %llu, escrowRecordGarbageCollectionEnabled: %@, totalTlkShares: %llu, collectableTlkShares: %llu, collectedTlkShares: %llu, tlkShareGarbageCollectionEnabled: %@, totalPeers: %llu, trustedPeers: %llu, superfluousPeers: %llu, peersCleanedup: %llu, superfluousPeersCleanupEnabled: %@>"
+ "@\"OTEscrowMoveRequestContext\""
+ "@132@0:8B16B20B24B28@32Q40Q48Q56B64Q68Q76Q84B92Q96Q104Q112Q120B128"
+ "CRK UUID %s already exists"
+ "Custodian Recovery Key is not trusted"
+ "Found CRKs that are being distrusted: %s"
+ "Please TTR unless you just removed a recovery or legacy contact"
+ "Recovery Contact or Legacy Contact just removed from another device"
+ "T@\"OTEscrowMoveRequestContext\",&,V_moveRequest"
+ "TB,V_escrowRecordGarbageCollectionEnabled"
+ "TB,V_leaveTrust"
+ "TB,V_postEscrowCFU"
+ "TB,V_postRepairCFU"
+ "TB,V_resetOctagon"
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
+ "TrustedPeersHelperHealthCheckResult"
+ "_TtCV18TrustedPeersHelper23GetRepairActionResponseP33_34B9299B76A248B7A76BCBE38D1FA2CF13_StorageClass"
+ "_collectableEscrowRecords"
+ "_collectableTlkShares"
+ "_collectedEscrowRecords"
+ "_collectedTlkShares"
+ "_escrowRecordGarbageCollectionEnabled"
+ "_escrowRecordMoveRequest"
+ "_leaveTrust"
+ "_moveRequest"
+ "_peersCleanedup"
+ "_postEscrowCFU"
+ "_postRepairCFU"
+ "_repairAction"
+ "_resetOctagon"
+ "_superfluousPeers"
+ "_superfluousPeersCleanupEnabled"
+ "_tlkShareGarbageCollectionEnabled"
+ "_totalEscrowRecords"
+ "_totalPeers"
+ "_totalTlkShares"
+ "_trustedPeers"
+ "beginning a octagonContainsDistrustedRecoveryKeys"
+ "collectableEscrowRecords"
+ "collectableTlkShares"
+ "collectable_escrow_records"
+ "collectable_tlk_shares"
+ "collectedEscrowRecords"
+ "collectedTlkShares"
+ "collected_escrow_records"
+ "collected_tlk_shares"
+ "custodian recovery key UUID already exists"
+ "distrusted recovery keys exist: %{bool}d"
+ "doesOctagonContainsDistrustedRecoveryKeys"
+ "escrowRecordGarbageCollectionEnabled"
+ "escrow_record_garbage_collection_enabled"
+ "false"
+ "initWithPostRepairCFU:postEscrowCFU:resetOctagon:leaveTrust:moveRequest:totalEscrowRecords:collectableEscrowRecords:collectedEscrowRecords:escrowRecordGarbageCollectionEnabled:totalTlkShares:collectableTlkShares:collectedTlkShares:tlkShareGarbageCollectionEnabled:totalPeers:trustedPeers:superfluousPeers:peersCleanedup:superfluousPeersCleanupEnabled:"
+ "leaveTrust"
+ "moveRequest"
+ "numberWithBool:"
+ "octagon contains distrusted recovery keys complete: %{public}s %{public}s"
+ "octagonContainsDistrustedRecoveryKeys failed for %{public}s: %{public}s"
+ "octagonContainsDistrustedRecoveryKeys for %{public}s"
+ "octagonContainsDistrustedRecoveryKeysWithSpecificUser:reply:"
+ "peersCleanedup"
+ "peers_cleanedup"
+ "postEscrowCFU"
+ "postRepairCFU"
+ "preflightCustodianRecoveryKey: custodian recovery key is not trusted"
+ "recovery key is not registered, nothing to remove."
+ "resetOctagon"
+ "setCollectableEscrowRecords:"
+ "setCollectableTlkShares:"
+ "setCollectedEscrowRecords:"
+ "setCollectedTlkShares:"
+ "setEscrowRecordGarbageCollectionEnabled:"
+ "setLeaveTrust:"
+ "setMoveRequest:"
+ "setPeersCleanedup:"
+ "setPostEscrowCFU:"
+ "setPostRepairCFU:"
+ "setResetOctagon:"
+ "setSuperfluousPeers:"
+ "setSuperfluousPeersCleanupEnabled:"
+ "setTlkShareGarbageCollectionEnabled:"
+ "setTotalEscrowRecords:"
+ "setTotalPeers:"
+ "setTotalTlkShares:"
+ "setTrustedPeers:"
+ "superfluousPeers"
+ "superfluousPeersCleanupEnabled"
+ "superfluous_peers"
+ "superfluous_peers_cleanup_enabled"
+ "tlkShareGarbageCollectionEnabled"
+ "tlk_share_garbage_collection_enabled"
+ "totalEscrowRecords"
+ "totalPeers"
+ "totalTlkShares"
+ "total_escrow_records"
+ "total_peers"
+ "total_tlk_shares"
+ "true"
+ "trustedPeers"
+ "v48@0:8@\"TPSpecificUser\"16B24B28@\"NSArray\"32@?<v@?@\"TrustedPeersHelperHealthCheckResult\"@\"NSError\">40"
- "Custodian Recovery Key is not enrolled"
- "TrustedPeersHelper.ValidatePeersOperation"
- "_TtCO18TrustedPeersHelper13CuttlefishAPI22ValidatePeersOperation"
- "account_health"
- "failure_description"
- "preflightCustodianRecoveryKey: custodian recovery Key is not enrolled"
- "results"
- "success"
- "tlk_share"
- "v48@0:8@\"TPSpecificUser\"16B24B28@\"NSArray\"32@?<v@?BBBB@\"OTEscrowMoveRequestContext\"@\"NSError\">40"
- "validators_health"

```
