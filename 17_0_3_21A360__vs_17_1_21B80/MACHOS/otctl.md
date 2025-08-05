## otctl

> `/usr/sbin/otctl`

```diff

-61040.2.2.0.0
-  __TEXT.__text: 0xea04
+61040.42.1.0.0
+  __TEXT.__text: 0xf810
   __TEXT.__auth_stubs: 0x550
-  __TEXT.__objc_stubs: 0x1b00
-  __TEXT.__objc_methlist: 0x7ec
+  __TEXT.__objc_stubs: 0x1e00
+  __TEXT.__objc_methlist: 0xa08
   __TEXT.__const: 0x58
   __TEXT.__gcc_except_tab: 0x574
-  __TEXT.__objc_methname: 0x25d9
-  __TEXT.__cstring: 0x26ed
-  __TEXT.__objc_classname: 0x76
-  __TEXT.__objc_methtype: 0x34a
+  __TEXT.__objc_methname: 0x2e47
+  __TEXT.__cstring: 0x2a62
+  __TEXT.__objc_classname: 0xb4
+  __TEXT.__objc_methtype: 0x3c2
   __TEXT.__oslogstring: 0xa5
-  __TEXT.__unwind_info: 0x3d4
+  __TEXT.__unwind_info: 0x3e4
   __DATA_CONST.__auth_got: 0x2b8
   __DATA_CONST.__got: 0x80
-  __DATA_CONST.__const: 0x380
-  __DATA_CONST.__cfstring: 0xae0
-  __DATA_CONST.__objc_classlist: 0x20
+  __DATA_CONST.__const: 0x3a8
+  __DATA_CONST.__cfstring: 0xd80
+  __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x8
+  __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x828
-  __DATA.__objc_selrefs: 0x9f0
-  __DATA.__objc_classrefs: 0xe8
-  __DATA.__objc_superrefs: 0x20
-  __DATA.__objc_ivar: 0x58
-  __DATA.__objc_data: 0x140
-  __DATA.__data: 0x1ef8
+  __DATA.__objc_const: 0xcf8
+  __DATA.__objc_selrefs: 0xb68
+  __DATA.__objc_classrefs: 0xf0
+  __DATA.__objc_superrefs: 0x28
+  __DATA.__objc_ivar: 0xa0
+  __DATA.__objc_data: 0x190
+  __DATA.__data: 0x1fb8
   __DATA.__bss: 0x17c
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6376DE96-F886-3DB1-8712-F316F7B096FA
-  Functions: 216
-  Symbols:   139
-  CStrings:  914
+  UUID: 13FC8975-2FD1-3B12-AE2C-7075AAEFAF52
+  Functions: 259
+  Symbols:   140
+  CStrings:  1048
 
Symbols:
+ _OBJC_CLASS_$_OTEscrowMoveRequestContext
CStrings:
+ "\x11"
+ "<HealthCheckResult: postRepairCFU: %@, postEscrowCFU: %@, resetOctagon: %@, leaveTrust: %@, moveRequest? %@, totalEscrowRecords: %llu, collectableEscrowRecords: %llu, collectedEscrowRecords: %llu, escrowRecordGarbageCollectionEnabled: %@, totalTlkShares: %llu, collectableTlkShares: %llu, collectedTlkShares: %llu, tlkShareGarbageCollectionEnabled: %@, totalPeers: %llu, trustedPeers: %llu, superfluousPeers: %llu, peersCleanedup: %llu, superfluousPeersCleanupEnabled: %@>"
+ "@\"OTEscrowMoveRequestContext\""
+ "@132@0:8B16B20B24B28@32Q40Q48Q56B64Q68Q76Q84B92Q96Q104Q112Q120B128"
+ "@24@0:8@\"NSCoder\"16"
+ "NSCoding"
+ "NSSecureCoding"
+ "T@\"OTEscrowMoveRequestContext\",&,V_moveRequest"
+ "TB,R"
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
+ "_collectableEscrowRecords"
+ "_collectableTlkShares"
+ "_collectedEscrowRecords"
+ "_collectedTlkShares"
+ "_escrowRecordGarbageCollectionEnabled"
+ "_leaveTrust"
+ "_moveRequest"
+ "_peersCleanedup"
+ "_postEscrowCFU"
+ "_postRepairCFU"
+ "_resetOctagon"
+ "_superfluousPeers"
+ "_superfluousPeersCleanupEnabled"
+ "_tlkShareGarbageCollectionEnabled"
+ "_totalEscrowRecords"
+ "_totalPeers"
+ "_totalTlkShares"
+ "_trustedPeers"
+ "areRecoveryKeysDistrusted:reply:"
+ "collectableEscrowRecords"
+ "collectableTlkShares"
+ "collectedEscrowRecords"
+ "collectedTlkShares"
+ "decodeBoolForKey:"
+ "decodeInt64ForKey:"
+ "decodeObjectOfClass:forKey:"
+ "encodeBool:forKey:"
+ "encodeInt64:forKey:"
+ "encodeObject:forKey:"
+ "encodeWithCoder:"
+ "escrowRecordGarbageCollectionEnabled"
+ "false"
+ "healthCheck:skipRateLimitingCheck:repair:json:"
+ "initWithCoder:"
+ "initWithPostRepairCFU:postEscrowCFU:resetOctagon:leaveTrust:moveRequest:totalEscrowRecords:collectableEscrowRecords:collectedEscrowRecords:escrowRecordGarbageCollectionEnabled:totalTlkShares:collectableTlkShares:collectedTlkShares:tlkShareGarbageCollectionEnabled:totalPeers:trustedPeers:superfluousPeers:peersCleanedup:superfluousPeersCleanupEnabled:"
+ "leaveTrust"
+ "moveRequest"
+ "peersCleanedup"
+ "postEscrowCFU"
+ "postRepairCFU"
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
+ "supportsSecureCoding"
+ "tlkShareGarbageCollectionEnabled"
+ "totalEscrowRecords"
+ "totalPeers"
+ "totalTlkShares"
+ "true"
+ "trustedPeers"
+ "v24@0:8@\"NSCoder\"16"
+ "v24@?0@\"TrustedPeersHelperHealthCheckResult\"8@\"NSError\"16"
- "healthCheck:skipRateLimitingCheck:repair:"
- "i32@0:8@16B24B28"

```
