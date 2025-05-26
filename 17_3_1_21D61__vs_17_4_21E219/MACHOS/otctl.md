## otctl

> `/usr/sbin/otctl`

```diff

-61040.82.1.0.0
-  __TEXT.__text: 0xffd0
-  __TEXT.__auth_stubs: 0x550
-  __TEXT.__objc_stubs: 0x1e80
-  __TEXT.__objc_methlist: 0xa58
-  __TEXT.__const: 0x58
-  __TEXT.__gcc_except_tab: 0x588
-  __TEXT.__objc_methname: 0x2f89
-  __TEXT.__cstring: 0x2b2f
+61123.100.169.0.0
+  __TEXT.__text: 0x12080
+  __TEXT.__auth_stubs: 0x560
+  __TEXT.__objc_stubs: 0x2020
+  __TEXT.__objc_methlist: 0xac8
+  __TEXT.__const: 0x60
+  __TEXT.__gcc_except_tab: 0x5b8
+  __TEXT.__objc_methname: 0x30eb
+  __TEXT.__cstring: 0x2d20
   __TEXT.__objc_classname: 0xb5
-  __TEXT.__objc_methtype: 0x3dd
+  __TEXT.__objc_methtype: 0x3f2
   __TEXT.__oslogstring: 0xa5
-  __TEXT.__unwind_info: 0x3fc
-  __DATA_CONST.__auth_got: 0x2b8
-  __DATA_CONST.__got: 0x88
+  __TEXT.__unwind_info: 0x424
+  __DATA_CONST.__auth_got: 0x2c0
+  __DATA_CONST.__got: 0x90
+  __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x3c0
-  __DATA_CONST.__cfstring: 0xe20
+  __DATA_CONST.__cfstring: 0xf00
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0xd38
-  __DATA.__objc_selrefs: 0xbb8
-  __DATA.__objc_classrefs: 0xf0
-  __DATA.__objc_superrefs: 0x28
-  __DATA.__objc_ivar: 0xa4
+  __DATA_CONST.__objc_classrefs: 0x100
+  __DATA_CONST.__objc_superrefs: 0x28
+  __DATA_CONST.__objc_arraydata: 0x10
+  __DATA_CONST.__objc_dictobj: 0x28
+  __DATA.__objc_const: 0xda8
+  __DATA.__objc_selrefs: 0xc28
+  __DATA.__objc_ivar: 0xac
   __DATA.__objc_data: 0x190
-  __DATA.__data: 0x2020
-  __DATA.__bss: 0x180
+  __DATA.__data: 0x128
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security

   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 267
-  Symbols:   141
-  CStrings:  961
+  Functions: 277
+  Symbols:   147
+  CStrings:  1000
 
Symbols:
+ _OBJC_CLASS_$_NSConstantDictionary
+ _OBJC_CLASS_$_NSISO8601DateFormatter
+ _OBJC_CLASS_$_NSSet
+ ___chkstk_darwin
+ ___kCFBooleanTrue
+ _memset
CStrings:
+ "    Encryption public key: %s\n"
+ "    Signing public key: %s\n"
+ "!#\x12\x12"
+ "<HealthCheckResult: postRepairCFU: %@, postEscrowCFU: %@, resetOctagon: %@, leaveTrust: %@, reroll: %@, moveRequest? %@, totalEscrowRecords: %llu, collectableEscrowRecords: %llu, collectedEscrowRecords: %llu, escrowRecordGarbageCollectionEnabled: %@, totalTlkShares: %llu, collectableTlkShares: %llu, collectedTlkShares: %llu, tlkShareGarbageCollectionEnabled: %@, totalPeers: %llu, trustedPeers: %llu, superfluousPeers: %llu, peersCleanedup: %llu, superfluousPeersCleanupEnabled: %@>"
+ "@136@0:8B16B20B24B28B32@36Q44Q52Q60B68Q72Q80Q88B96Q100Q108Q116Q124B132"
+ "Error rerolling: %s\n"
+ "Fetching status had no error and gave no result!\n"
+ "Join with a recovery key"
+ "No result returned and no data"
+ "Recovery Key:"
+ "Reroll PeerID"
+ "Reroll successful."
+ "T@\"NSString\",&,N,V_oldPeerID"
+ "TB,V_reroll"
+ "_oldPeerID"
+ "_reroll"
+ "annotateStatus:"
+ "bytes"
+ "containsObject:"
+ "dictionaryWithDictionary:"
+ "distrusted_by_self"
+ "fetchAllBottles:control:overrideEscrowCache:"
+ "fetchAllEscrowRecords:json:overrideEscrowCache:"
+ "fetchAllViableBottles:source:reply:"
+ "fetchEscrowRecords:json:overrideEscrowCache:"
+ "hasOldPeerID"
+ "i32@0:8@16B24B28"
+ "initWithArray:"
+ "initWithData:"
+ "initWithPostRepairCFU:postEscrowCFU:resetOctagon:leaveTrust:reroll:moveRequest:totalEscrowRecords:collectableEscrowRecords:collectedEscrowRecords:escrowRecordGarbageCollectionEnabled:totalTlkShares:collectableTlkShares:collectedTlkShares:tlkShareGarbageCollectionEnabled:totalPeers:trustedPeers:superfluousPeers:peersCleanedup:superfluousPeersCleanupEnabled:"
+ "join-with-recovery-key"
+ "joinWithRecoveryKeyWithArguments:recoveryKey:"
+ "joining with recovery key failed: %s\n"
+ "oldPeerID"
+ "recovery key"
+ "recoveryKey"
+ "recovery_encryption_public_key"
+ "recovery_signing_public_key"
+ "reroll"
+ "reroll:reply:"
+ "rerollWithArguments:json:"
+ "setEscrowFetchSource:"
+ "setOldPeerID:"
+ "setReroll:"
+ "stringFromDate:"
+ "successfully joined using recovery key %s, in octagon\n"
+ "trusted_by_self"
- "!\"\x12\x12"
- "<HealthCheckResult: postRepairCFU: %@, postEscrowCFU: %@, resetOctagon: %@, leaveTrust: %@, moveRequest? %@, totalEscrowRecords: %llu, collectableEscrowRecords: %llu, collectedEscrowRecords: %llu, escrowRecordGarbageCollectionEnabled: %@, totalTlkShares: %llu, collectableTlkShares: %llu, collectedTlkShares: %llu, tlkShareGarbageCollectionEnabled: %@, totalPeers: %llu, trustedPeers: %llu, superfluousPeers: %llu, peersCleanedup: %llu, superfluousPeersCleanupEnabled: %@>"
- "@132@0:8B16B20B24B28@32Q40Q48Q56B64Q68Q76Q84B92Q96Q104Q112Q120B128"
- "deliverAKDeviceListDelta:reply:"
- "fetchAllBottles:control:"
- "fetchAllEscrowRecords:json:"
- "fetchAllViableBottles:reply:"
- "fetchEscrowRecords:json:"
- "initWithPostRepairCFU:postEscrowCFU:resetOctagon:leaveTrust:moveRequest:totalEscrowRecords:collectableEscrowRecords:collectedEscrowRecords:escrowRecordGarbageCollectionEnabled:totalTlkShares:collectableTlkShares:collectedTlkShares:tlkShareGarbageCollectionEnabled:totalPeers:trustedPeers:superfluousPeers:peersCleanedup:superfluousPeersCleanupEnabled:"
- "setOverrideEscrowCache:"

```
