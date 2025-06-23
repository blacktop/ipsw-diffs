## otctl

> `/usr/sbin/otctl`

```diff

-61901.0.9.0.1
-  __TEXT.__text: 0x147dc
+61901.0.33.0.2
+  __TEXT.__text: 0x1464c
   __TEXT.__auth_stubs: 0x570
-  __TEXT.__objc_stubs: 0x2380
-  __TEXT.__objc_methlist: 0xbec
+  __TEXT.__objc_stubs: 0x2320
+  __TEXT.__objc_methlist: 0xbcc
   __TEXT.__const: 0x70
   __TEXT.__gcc_except_tab: 0x734
-  __TEXT.__objc_methname: 0x3710
-  __TEXT.__cstring: 0x31f0
-  __TEXT.__objc_classname: 0xb5
-  __TEXT.__objc_methtype: 0x497
+  __TEXT.__objc_methname: 0x367b
+  __TEXT.__cstring: 0x31d3
+  __TEXT.__objc_classname: 0xb3
+  __TEXT.__objc_methtype: 0x475
   __TEXT.__oslogstring: 0xa5
-  __TEXT.__unwind_info: 0x4b8
+  __TEXT.__unwind_info: 0x4c0
   __DATA_CONST.__auth_got: 0x2c8
-  __DATA_CONST.__got: 0x188
+  __DATA_CONST.__got: 0x180
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x460
-  __DATA_CONST.__cfstring: 0xe60
+  __DATA_CONST.__cfstring: 0xe40
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18

   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA.__objc_const: 0xdb0
-  __DATA.__objc_selrefs: 0xd30
-  __DATA.__objc_ivar: 0xb4
+  __DATA.__objc_const: 0xd80
+  __DATA.__objc_selrefs: 0xd10
+  __DATA.__objc_ivar: 0xb0
   __DATA.__objc_data: 0x190
   __DATA.__data: 0x128
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8E410748-E4A7-3567-AB0B-4FFB30C77DC3
-  Functions: 305
-  Symbols:   149
-  CStrings:  1203
+  UUID: 6023A834-32E8-3AA3-B0FA-0B9F8378E5A0
+  Functions: 302
+  Symbols:   148
+  CStrings:  1194
 
Symbols:
- _OBJC_CLASS_$_OTEscrowMoveRequestContext
CStrings:
+ "<HealthCheckResult: postRepairCFU: %@, postEscrowCFU: %@, resetOctagon: %@, leaveTrust: %@, reroll: %@, totalEscrowRecords: %llu, collectableEscrowRecords: %llu, collectedEscrowRecords: %llu, escrowRecordGarbageCollectionEnabled: %@, totalTlkShares: %llu, collectableTlkShares: %llu, collectedTlkShares: %llu, tlkShareGarbageCollectionEnabled: %@, totalPeers: %llu, trustedPeers: %llu, superfluousPeers: %llu, peersCleanedup: %llu, superfluousPeersCleanupEnabled: %@>"
+ "@128@0:8B16B20B24B28B32Q36Q44Q52B60Q64Q72Q80B88Q92Q100Q108Q116B124"
+ "initWithPostRepairCFU:postEscrowCFU:resetOctagon:leaveTrust:reroll:totalEscrowRecords:collectableEscrowRecords:collectedEscrowRecords:escrowRecordGarbageCollectionEnabled:totalTlkShares:collectableTlkShares:collectedTlkShares:tlkShareGarbageCollectionEnabled:totalPeers:trustedPeers:superfluousPeers:peersCleanedup:superfluousPeersCleanupEnabled:"
- "<HealthCheckResult: postRepairCFU: %@, postEscrowCFU: %@, resetOctagon: %@, leaveTrust: %@, reroll: %@, moveRequest? %@, totalEscrowRecords: %llu, collectableEscrowRecords: %llu, collectedEscrowRecords: %llu, escrowRecordGarbageCollectionEnabled: %@, totalTlkShares: %llu, collectableTlkShares: %llu, collectedTlkShares: %llu, tlkShareGarbageCollectionEnabled: %@, totalPeers: %llu, trustedPeers: %llu, superfluousPeers: %llu, peersCleanedup: %llu, superfluousPeersCleanupEnabled: %@>"
- "@\"OTEscrowMoveRequestContext\""
- "@136@0:8B16B20B24B28B32@36Q44Q52Q60B68Q72Q80Q88B96Q100Q108Q116Q124B132"
- "T@\"OTEscrowMoveRequestContext\",&,V_moveRequest"
- "_moveRequest"
- "decodeObjectOfClass:forKey:"
- "encodeObject:forKey:"
- "initWithPostRepairCFU:postEscrowCFU:resetOctagon:leaveTrust:reroll:moveRequest:totalEscrowRecords:collectableEscrowRecords:collectedEscrowRecords:escrowRecordGarbageCollectionEnabled:totalTlkShares:collectableTlkShares:collectedTlkShares:tlkShareGarbageCollectionEnabled:totalPeers:trustedPeers:superfluousPeers:peersCleanedup:superfluousPeersCleanupEnabled:"
- "moveRequest"
- "setMoveRequest:"

```
