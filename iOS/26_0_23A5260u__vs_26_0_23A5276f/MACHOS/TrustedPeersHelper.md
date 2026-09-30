## TrustedPeersHelper

> `/System/Library/Frameworks/Security.framework/XPCServices/TrustedPeersHelper.xpc/TrustedPeersHelper`

```diff

-61901.0.9.0.1
-  __TEXT.__text: 0x203274
-  __TEXT.__auth_stubs: 0x1ff0
-  __TEXT.__objc_stubs: 0x2600
-  __TEXT.__objc_methlist: 0x2884
-  __TEXT.__const: 0xa088
+61901.0.33.0.2
+  __TEXT.__text: 0x2052f8
+  __TEXT.__auth_stubs: 0x2000
+  __TEXT.__objc_stubs: 0x2500
+  __TEXT.__objc_methlist: 0x276c
+  __TEXT.__const: 0xa200
   __TEXT.__dlopen_cstrs: 0x228
-  __TEXT.__cstring: 0x17a42
-  __TEXT.__objc_methname: 0x7785
+  __TEXT.__cstring: 0x17b96
+  __TEXT.__objc_methname: 0x7537
   __TEXT.__oslogstring: 0xa72a
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x3720
-  __TEXT.__swift5_typeref: 0x3800
-  __TEXT.__swift5_fieldmd: 0x26d4
-  __TEXT.__swift5_reflstr: 0x21c7
+  __TEXT.__constg_swiftt: 0x3778
+  __TEXT.__swift5_typeref: 0x380e
+  __TEXT.__swift5_fieldmd: 0x2750
+  __TEXT.__swift5_reflstr: 0x22f7
   __TEXT.__swift5_builtin: 0xb4
   __TEXT.__swift5_assocty: 0x3f0
-  __TEXT.__swift5_proto: 0x8bc
-  __TEXT.__swift5_types: 0x28c
-  __TEXT.__objc_classname: 0x42d
-  __TEXT.__objc_methtype: 0x21b8
+  __TEXT.__swift5_proto: 0x8c8
+  __TEXT.__swift5_types: 0x290
+  __TEXT.__objc_classname: 0x42b
+  __TEXT.__objc_methtype: 0x2196
   __TEXT.__swift5_mpenum: 0x18
   __TEXT.__swift5_capture: 0x4438
   __TEXT.__gcc_except_tab: 0x170
   __TEXT.__swift5_protos: 0x18
-  __TEXT.__unwind_info: 0x4a20
-  __TEXT.__eh_frame: 0x7340
-  __DATA_CONST.__auth_got: 0x1008
+  __TEXT.__unwind_info: 0x4b98
+  __TEXT.__eh_frame: 0x77a8
+  __DATA_CONST.__auth_got: 0x1010
   __DATA_CONST.__got: 0x958
-  __DATA_CONST.__auth_ptr: 0x678
-  __DATA_CONST.__const: 0x12890
-  __DATA_CONST.__cfstring: 0x18c0
+  __DATA_CONST.__auth_ptr: 0x690
+  __DATA_CONST.__const: 0x12900
+  __DATA_CONST.__cfstring: 0x17c0
   __DATA_CONST.__objc_classlist: 0x250
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_superrefs: 0xe8
-  __DATA.__objc_const: 0x6a28
-  __DATA.__objc_selrefs: 0x1d68
-  __DATA.__objc_ivar: 0x208
-  __DATA.__objc_data: 0x2a50
-  __DATA.__data: 0x7ae0
+  __DATA.__objc_const: 0x68e0
+  __DATA.__objc_selrefs: 0x1cc0
+  __DATA.__objc_ivar: 0x1e8
+  __DATA.__objc_data: 0x2a00
+  __DATA.__data: 0x7a80
   __DATA.__objc_stublist: 0x98
-  __DATA.__bss: 0x11428
+  __DATA.__bss: 0x115a8
   __DATA.__common: 0x918
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/CloudKitCode.framework/CloudKitCode
+  - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
   - /System/Library/PrivateFrameworks/InternalSwiftProtobuf.framework/InternalSwiftProtobuf
   - /System/Library/PrivateFrameworks/KeychainCircle.framework/KeychainCircle
   - /System/Library/PrivateFrameworks/OctagonTrust.framework/OctagonTrust

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
   - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: BB3893D8-D027-3A59-8BA0-EFFB8D5A69CB
-  Functions: 8128
-  Symbols:   529
-  CStrings:  3477
+  UUID: 7AC2778A-965D-3B26-96DE-8CA8EFCD4B1F
+  Functions: 8134
+  Symbols:   525
+  CStrings:  3435
 
Symbols:
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
CStrings:
+ "<HealthCheckResult: postRepairCFU: %@, postEscrowCFU: %@, resetOctagon: %@, leaveTrust: %@, reroll: %@, totalEscrowRecords: %llu, collectableEscrowRecords: %llu, collectedEscrowRecords: %llu, escrowRecordGarbageCollectionEnabled: %@, totalTlkShares: %llu, collectableTlkShares: %llu, collectedTlkShares: %llu, tlkShareGarbageCollectionEnabled: %@, totalPeers: %llu, trustedPeers: %llu, superfluousPeers: %llu, peersCleanedup: %llu, superfluousPeersCleanupEnabled: %@>"
+ "@128@0:8B16B20B24B28B32Q36Q44Q52B60Q64Q72Q80B88Q92Q100Q108Q116B124"
+ "TestDisableEscrowCheck"
+ "TestDisableEscrowRepair"
+ "_caesarPeersCleanedUp"
+ "_caesarPeersCleanupEnabled"
+ "_fullyDanglingPeerCountValidationFails"
+ "_partiallyDanglingPeerCountValidationFails"
+ "caesar_peers_cleaned_up"
+ "caesar_peers_cleanup_enabled"
+ "disable_repair"
+ "disable_with_error"
+ "fully_dangling_peer_count_validation_fails"
+ "initWithPostRepairCFU:postEscrowCFU:resetOctagon:leaveTrust:reroll:totalEscrowRecords:collectableEscrowRecords:collectedEscrowRecords:escrowRecordGarbageCollectionEnabled:totalTlkShares:collectableTlkShares:collectedTlkShares:tlkShareGarbageCollectionEnabled:totalPeers:trustedPeers:superfluousPeers:peersCleanedup:superfluousPeersCleanupEnabled:"
+ "partially_dangling_peer_count_validation_fails"
+ "perform_caesar_peer_cleanup"
+ "repair_disabled"
+ "setRepairDisabled:"
- "\f"
- "<HealthCheckResult: postRepairCFU: %@, postEscrowCFU: %@, resetOctagon: %@, leaveTrust: %@, reroll: %@, moveRequest? %@, totalEscrowRecords: %llu, collectableEscrowRecords: %llu, collectedEscrowRecords: %llu, escrowRecordGarbageCollectionEnabled: %@, totalTlkShares: %llu, collectableTlkShares: %llu, collectedTlkShares: %llu, tlkShareGarbageCollectionEnabled: %@, totalPeers: %llu, trustedPeers: %llu, superfluousPeers: %llu, peersCleanedup: %llu, superfluousPeersCleanupEnabled: %@>"
- "@\"OTEscrowMoveRequestContext\""
- "@136@0:8B16B20B24B28B32@36Q44Q52Q60B68Q72Q80Q88B96Q100Q108Q116Q124B132"
- "T@\"NSData\",&,N,V_reserved1"
- "T@\"NSData\",&,N,V_reserved2"
- "T@\"NSData\",&,N,V_reserved3"
- "T@\"NSData\",&,N,V_reserved4"
- "T@\"NSData\",&,N,V_reserved5"
- "T@\"NSData\",&,N,V_reserved6"
- "T@\"NSData\",&,N,V_reserved7"
- "T@\"OTEscrowMoveRequestContext\",&,V_moveRequest"
- "_escrowRecordMoveRequest"
- "_moveRequest"
- "_reserved1"
- "_reserved2"
- "_reserved3"
- "_reserved4"
- "_reserved5"
- "_reserved6"
- "_reserved7"
- "hasReserved1"
- "hasReserved2"
- "hasReserved3"
- "hasReserved4"
- "hasReserved5"
- "hasReserved6"
- "hasReserved7"
- "initWithPostRepairCFU:postEscrowCFU:resetOctagon:leaveTrust:reroll:moveRequest:totalEscrowRecords:collectableEscrowRecords:collectedEscrowRecords:escrowRecordGarbageCollectionEnabled:totalTlkShares:collectableTlkShares:collectedTlkShares:tlkShareGarbageCollectionEnabled:totalPeers:trustedPeers:superfluousPeers:peersCleanedup:superfluousPeersCleanupEnabled:"
- "moveRequest"
- "reserved1"
- "reserved2"
- "reserved3"
- "reserved4"
- "reserved5"
- "reserved6"
- "reserved7"
- "setReserved1:"
- "setReserved2:"
- "setReserved3:"
- "setReserved4:"
- "setReserved5:"
- "setReserved6:"
- "setReserved7:"

```
