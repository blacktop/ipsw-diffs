## TrustedPeersHelper

> `/System/Library/Frameworks/Security.framework/XPCServices/TrustedPeersHelper.xpc/TrustedPeersHelper`

```diff

-  __TEXT.__text: 0x2a0864
-  __TEXT.__auth_stubs: 0x22d0
-  __TEXT.__objc_stubs: 0x6060
-  __TEXT.__objc_methlist: 0x292c
-  __TEXT.__const: 0xd4a0
-  __TEXT.__cstring: 0x17a67
-  __TEXT.__swift5_typeref: 0x3fbc
-  __TEXT.__oslogstring: 0xd2f7
+  __TEXT.__text: 0x2a3ccc
+  __TEXT.__auth_stubs: 0x22e0
+  __TEXT.__objc_stubs: 0x6080
+  __TEXT.__objc_methlist: 0x2934
+  __TEXT.__const: 0xd4c0
+  __TEXT.__cstring: 0x17ab7
+  __TEXT.__swift5_typeref: 0x3fc6
+  __TEXT.__oslogstring: 0xd4a4
   __TEXT.__swift5_entry: 0x8
   __TEXT.__objc_classname: 0x147b
-  __TEXT.__objc_methname: 0x90e1
-  __TEXT.__objc_methtype: 0x29bf
+  __TEXT.__objc_methname: 0x9141
+  __TEXT.__objc_methtype: 0x29f0
   __TEXT.__constg_swiftt: 0x3c1c
-  __TEXT.__swift5_fieldmd: 0x2b80
-  __TEXT.__swift5_reflstr: 0x2647
+  __TEXT.__swift5_fieldmd: 0x2b8c
+  __TEXT.__swift5_reflstr: 0x2677
   __TEXT.__swift5_builtin: 0xc8
   __TEXT.__swift5_assocty: 0x420
   __TEXT.__swift5_proto: 0x98c
   __TEXT.__swift5_types: 0x2c8
   __TEXT.__swift5_mpenum: 0x18
   __TEXT.__gcc_except_tab: 0x178
-  __TEXT.__swift5_capture: 0x5090
+  __TEXT.__swift5_capture: 0x516c
   __TEXT.__dlopen_cstrs: 0x1c2
   __TEXT.__swift5_protos: 0x18
-  __TEXT.__unwind_info: 0x4f70
-  __TEXT.__eh_frame: 0x7f60
-  __DATA_CONST.__const: 0x14c70
+  __TEXT.__unwind_info: 0x4f78
+  __TEXT.__eh_frame: 0x7ef0
+  __DATA_CONST.__const: 0x14d88
   __DATA_CONST.__cfstring: 0x1880
   __DATA_CONST.__objc_classlist: 0x268
   __DATA_CONST.__objc_catlist: 0x20

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__objc_superrefs: 0xf0
-  __DATA_CONST.__auth_got: 0x1178
-  __DATA_CONST.__got: 0xa10
+  __DATA_CONST.__auth_got: 0x1180
+  __DATA_CONST.__got: 0xa40
   __DATA_CONST.__auth_ptr: 0x6f0
   __DATA.__objc_const: 0x6e78
-  __DATA.__objc_selrefs: 0x1ec0
+  __DATA.__objc_selrefs: 0x1ec8
   __DATA.__objc_ivar: 0x1fc
   __DATA.__objc_data: 0x2c90
   __DATA.__data: 0x84a0

   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /System/Library/PrivateFrameworks/SecurityFoundation.framework/SecurityFoundation
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
+  - /System/Library/PrivateFrameworks/StorageContainersPrivate.framework/StorageContainersPrivate
   - /System/Library/PrivateFrameworks/TrustedPeers.framework/TrustedPeers
   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 8885
-  Symbols:   570
-  CStrings:  3478
+  Functions: 8898
+  Symbols:   578
+  CStrings:  3486
 
Sections:
~ __TEXT.__swift5_entry : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift5_types : content changed
~ __TEXT.__swift5_mpenum : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__swift5_protos : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
~ __DATA.__bss : content changed
~ __DATA.__common : content changed
Symbols:
+ _kSecurityRTCEventNameRKSponsorSelection
+ _kSecurityRTCEventNameRecoverRKTLKShares
+ _kSecurityRTCEventNameTLKProofInvalid
+ _kSecurityRTCFieldAuthenticatedRKSponsorSelected
+ _kSecurityRTCFieldNumRKTLKShares
+ _kSecurityRTCFieldNumRKTLKSharesRecovered
+ _kSecurityRTCFieldPotentialRKSponsorsWithStableInfoFlagSet
+ _swift_projectBox
CStrings:
+ "@28@0:8@16B24"
+ "B52@0:8@16@24@32B40^@44"
+ "Couldn't verify signature of TLKShare (%@) that includes tlkOwnershipProof as part of dataForSigning; trying again without tlkOwnershipProof"
+ "No protected Container "
+ "UpdateTrust: failed to find ego peer information"
+ "couldn't generate stableInfo for walrus disable retry, cannot disable walrus"
+ "dataForSigning:includeProof:"
+ "disableWalrus retry failed: %{public}s"
+ "disableWalrus returned indicating that stableInfo contains extra modifications, trying fetch"
+ "v84@0:8@\"TPSpecificUser\"16@\"NSString\"24@\"NSString\"32@\"NSArray\"40@\"NSString\"48@\"NSString\"56@\"NSString\"64B72@?<v@?@\"NSData\"@\"NSData\"@\"NSArray\"B@\"TrustedPeersHelperTLKRecoveryResult\"@\"NSError\">76"
+ "verifySignature:verifyingPeer:ckrecord:acceptProoflessSig:error:"
+ "vouchWithRecoveryKey(recoveryKey:salt:tlkShares:altDSID:flowID:deviceSessionID:canSendMetrics:reply:)"
+ "vouchWithRecoveryKeyWithSpecificUser:recoveryKey:salt:tlkShares:altDSID:flowID:deviceSessionID:canSendMetrics:reply:"
- "B48@0:8@16@24@32^@40"
- "v56@0:8@\"TPSpecificUser\"16@\"NSString\"24@\"NSString\"32@\"NSArray\"40@?<v@?@\"NSData\"@\"NSData\"@\"NSArray\"B@\"TrustedPeersHelperTLKRecoveryResult\"@\"NSError\">48"
- "verifySignature:verifyingPeer:ckrecord:error:"
- "vouchWithRecoveryKey(recoveryKey:salt:tlkShares:reply:)"
- "vouchWithRecoveryKeyWithSpecificUser:recoveryKey:salt:tlkShares:reply:"

```
