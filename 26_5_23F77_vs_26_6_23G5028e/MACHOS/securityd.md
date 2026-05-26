## securityd

> `/usr/libexec/securityd`

```diff

-61901.120.67.0.0
-  __TEXT.__text: 0x280cc0
-  __TEXT.__auth_stubs: 0x4210
-  __TEXT.__objc_stubs: 0x1d0c0
-  __TEXT.__objc_methlist: 0x15908
+61901.160.29.0.0
+  __TEXT.__text: 0x282cfc
+  __TEXT.__auth_stubs: 0x4230
+  __TEXT.__objc_stubs: 0x1d200
+  __TEXT.__objc_methlist: 0x159c8
   __TEXT.__const: 0x919
-  __TEXT.__cstring: 0x21755
-  __TEXT.__objc_methname: 0x2d338
-  __TEXT.__oslogstring: 0x2ee4f
+  __TEXT.__cstring: 0x2180d
+  __TEXT.__objc_methname: 0x2d593
+  __TEXT.__oslogstring: 0x2efe2
   __TEXT.__swift5_typeref: 0x378
   __TEXT.__swift5_fieldmd: 0x120
   __TEXT.__objc_classname: 0x25d7
-  __TEXT.__objc_methtype: 0xa9d2
+  __TEXT.__objc_methtype: 0xa9ef
   __TEXT.__constg_swiftt: 0x274
   __TEXT.__swift5_reflstr: 0xc3
   __TEXT.__swift5_capture: 0x1bc

   __TEXT.__swift5_types: 0x20
   __TEXT.__swift_as_entry: 0x40
   __TEXT.__swift_as_ret: 0x3c
-  __TEXT.__gcc_except_tab: 0xb5dc
+  __TEXT.__gcc_except_tab: 0xb760
   __TEXT.__dlopen_cstrs: 0xb4
   __TEXT.__ustring: 0x28
-  __TEXT.__unwind_info: 0x6f20
+  __TEXT.__unwind_info: 0x6f48
   __TEXT.__eh_frame: 0xa58
-  __DATA_CONST.__auth_got: 0x2118
-  __DATA_CONST.__got: 0x13b0
+  __DATA_CONST.__auth_got: 0x2128
+  __DATA_CONST.__got: 0x13c0
   __DATA_CONST.__auth_ptr: 0x1d8
-  __DATA_CONST.__const: 0x145a8
-  __DATA_CONST.__cfstring: 0x1bd40
+  __DATA_CONST.__const: 0x14768
+  __DATA_CONST.__cfstring: 0x1be40
   __DATA_CONST.__objc_classlist: 0x8f8
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0x258
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__objc_superrefs: 0x810
-  __DATA_CONST.__objc_intobj: 0x1350
-  __DATA_CONST.__objc_arraydata: 0x400
+  __DATA_CONST.__objc_intobj: 0x1380
+  __DATA_CONST.__objc_arraydata: 0x408
   __DATA_CONST.__objc_dictobj: 0x78
   __DATA_CONST.__objc_arrayobj: 0x360
-  __DATA.__objc_const: 0x233e8
-  __DATA.__objc_selrefs: 0x95d0
-  __DATA.__objc_ivar: 0x1a68
+  __DATA.__objc_const: 0x234c8
+  __DATA.__objc_selrefs: 0x9638
+  __DATA.__objc_ivar: 0x1a78
   __DATA.__objc_data: 0x5ca8
   __DATA.__data: 0x30f8
   __DATA.__thread_vars: 0xc0
   __DATA.__thread_bss: 0x28
-  __DATA.__bss: 0xe88
+  __DATA.__bss: 0xe98
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 7E96606F-1C0C-30FD-9CD1-40152F33FAC6
-  Functions: 9801
-  Symbols:   1863
-  CStrings:  20015
+  UUID: B1943F84-C699-3AAB-8203-1CD52EA68395
+  Functions: 9820
+  Symbols:   1867
+  CStrings:  20060
 
Symbols:
+ _cchkdf
+ _cchmac
+ _kSecurityRTCEventNameTLKOwnershipProofsGenerated
+ _kSecurityRTCEventNameTLKOwnershipSetInStableInfo
CStrings:
+ "$$"
+ "-[CuttlefishXPCWrapper updateWithSpecificUser:forceRefetch:deviceName:serialNumber:osVersion:policyVersion:policySecrets:syncUserControllableViews:secureElementIdentity:walrusSetting:webAccess:tlkProofsSet:reply:]_block_invoke"
+ "@112@0:8@16@24@32@40q48Q56q64q72@80@88@96@104"
+ "@128@0:8@16@24@32@40@48q56Q64q72q80@88@96@104@112@120"
+ "@84@0:8@16@24@32@40@48@56B64@68@76"
+ "Adding flag now that CKKS has backfilled TLK Proofs"
+ "Asking state machine to update stable info now that tlk proofs are set."
+ "Couldn't find missing shares because self peers aren't available for trust state (%@): %@"
+ "Couldn't find missing shares because trusted peers aren't available for trust state (%@): %@"
+ "Couldn't generate tlk(%@) proof for peer(%@) "
+ "Couldn't re-generate self-tlk proof for %@, skipping"
+ "Errored on loading TLK from keychain: %@"
+ "Missing or invalid tlk proof for self share, need to upload new TLK Share for %@"
+ "OctagonRKTLKOwnershipProof"
+ "OctagonRKTLKOwnershipProof is %s"
+ "OctagonStateTLKProofsSet"
+ "Recovery Key - Peer Authentication Key"
+ "SELECT agrp,                                  SUM(1 - tomb) AS count_tomb_0,                                  SUM(tomb) AS count_tomb_1                                  FROM %@                                  GROUP BY agrp"
+ "T@\"CKKSNearFutureScheduler\",&,V_tlkProofSetNotifier"
+ "T@\"NSData\",&,V_tlkOwnershipProof"
+ "T@\"NSNumber\",&,V_tlkProofsSet"
+ "TB,V_tlkProofsBackfillRequested"
+ "_tlkOwnershipProof"
+ "_tlkProofSetNotifier"
+ "_tlkProofsBackfillRequested"
+ "_tlkProofsSet"
+ "allFor:from:contextID:error:"
+ "allFor:from:keyUUID:contextID:error:"
+ "ckks-set-tlk-proofs"
+ "couldn't create tlk proof %@"
+ "createFromCKRecord:"
+ "generateOwnershipProof:tlk:error:"
+ "initForKey:contextID:senderPeerID:recieverPeerID:receiverEncPublicKeySPKI:curve:version:epoch:poisoned:wrappedKey:signature:zoneID:encodedCKRecord:tlkOwnershipProof:"
+ "initForKey:senderPeerID:recieverPeerID:receiverEncPublicKeySPKI:curve:version:epoch:poisoned:wrappedKey:signature:zoneID:tlkOwnershipProof:"
+ "initWithDependencies:deviceInfo:intendedState:peerUnknownState:determineCDPState:errorState:forceRefetch:retryFlag:tlkProofsSet:"
+ "octagon-tlk-proofs-set"
+ "setTLKProofNotifier:"
+ "setTlkOwnershipProof:"
+ "setTlkProofSetNotifier:"
+ "setTlkProofsBackfillRequested:"
+ "setTlkProofsSet:"
+ "tlk-share-healing"
+ "tlkOwnershipProof"
+ "tlkProofSetNotifier"
+ "tlkProofsBackfillRequested"
+ "tlkProofsSet"
+ "tlk_proofs_set"
+ "updateWithSpecificUser:forceRefetch:deviceName:serialNumber:osVersion:policyVersion:policySecrets:syncUserControllableViews:secureElementIdentity:walrusSetting:webAccess:tlkProofsSet:reply:"
+ "v116@0:8@\"TPSpecificUser\"16B24@\"NSString\"28@\"NSString\"36@\"NSString\"44@\"NSNumber\"52@\"NSDictionary\"60@\"NSNumber\"68@\"TrustedPeersHelperIntendedTPPBSecureElementIdentity\"76@\"TPPBPeerStableInfoSetting\"84@\"TPPBPeerStableInfoSetting\"92@\"NSNumber\"100@?<v@?@\"TrustedPeersHelperPeerState\"@\"TPSyncingPolicy\"@\"NSError\">108"
+ "v116@0:8@16B24@28@36@44@52@60@68@76@84@92@100@?108"
- "$#"
- "-[CuttlefishXPCWrapper updateWithSpecificUser:forceRefetch:deviceName:serialNumber:osVersion:policyVersion:policySecrets:syncUserControllableViews:secureElementIdentity:walrusSetting:webAccess:reply:]_block_invoke"
- "@104@0:8@16@24@32@40q48Q56q64q72@80@88@96"
- "@120@0:8@16@24@32@40@48q56Q64q72q80@88@96@104@112"
- "@76@0:8@16@24@32@40@48@56B64@68"
- "Couldn't find missing shares because self peers aren't available: %@"
- "Couldn't find missing shares because trusted peers aren't available: %@"
- "SELECT agrp,                                  SUM(CASE WHEN tomb = 0 THEN 1 ELSE 0 END) AS count_tomb_0,                                  SUM(CASE WHEN tomb = 1 THEN 1 ELSE 0 END) AS count_tomb_1                                  FROM %@                                  GROUP BY agrp"
- "initForKey:contextID:senderPeerID:recieverPeerID:receiverEncPublicKeySPKI:curve:version:epoch:poisoned:wrappedKey:signature:zoneID:encodedCKRecord:"
- "initForKey:senderPeerID:recieverPeerID:receiverEncPublicKeySPKI:curve:version:epoch:poisoned:wrappedKey:signature:zoneID:"
- "initWithDependencies:deviceInfo:intendedState:peerUnknownState:determineCDPState:errorState:forceRefetch:retryFlag:"
- "updateWithSpecificUser:forceRefetch:deviceName:serialNumber:osVersion:policyVersion:policySecrets:syncUserControllableViews:secureElementIdentity:walrusSetting:webAccess:reply:"
- "v108@0:8@\"TPSpecificUser\"16B24@\"NSString\"28@\"NSString\"36@\"NSString\"44@\"NSNumber\"52@\"NSDictionary\"60@\"NSNumber\"68@\"TrustedPeersHelperIntendedTPPBSecureElementIdentity\"76@\"TPPBPeerStableInfoSetting\"84@\"TPPBPeerStableInfoSetting\"92@?<v@?@\"TrustedPeersHelperPeerState\"@\"TPSyncingPolicy\"@\"NSError\">100"
- "v108@0:8@16B24@28@36@44@52@60@68@76@84@92@?100"

```
