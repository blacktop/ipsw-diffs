## TrustedPeersHelper

> `/System/Library/Frameworks/Security.framework/Versions/A/XPCServices/TrustedPeersHelper.xpc/Contents/MacOS/TrustedPeersHelper`

```diff

-  __TEXT.__text: 0x2b3f4c
-  __TEXT.__auth_stubs: 0x2060
-  __TEXT.__objc_stubs: 0x6040
-  __TEXT.__objc_methlist: 0x292c
-  __TEXT.__const: 0xd4d0
-  __TEXT.__cstring: 0x17b89
-  __TEXT.__swift5_typeref: 0x3fe4
-  __TEXT.__oslogstring: 0xd3e4
+  __TEXT.__text: 0x2b705c
+  __TEXT.__auth_stubs: 0x2070
+  __TEXT.__objc_stubs: 0x6060
+  __TEXT.__objc_methlist: 0x2934
+  __TEXT.__const: 0xd4f0
+  __TEXT.__cstring: 0x17bd9
+  __TEXT.__swift5_typeref: 0x3fee
+  __TEXT.__oslogstring: 0xd591
   __TEXT.__swift5_entry: 0x8
   __TEXT.__objc_classname: 0x147b
-  __TEXT.__objc_methname: 0x90d1
-  __TEXT.__objc_methtype: 0x29bf
+  __TEXT.__objc_methname: 0x9131
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
   __TEXT.__unwind_info: 0x50a8
-  __TEXT.__eh_frame: 0x7f18
-  __DATA_CONST.__const: 0x14d20
+  __TEXT.__eh_frame: 0x7ea8
+  __DATA_CONST.__const: 0x14e38
   __DATA_CONST.__cfstring: 0x18e0
   __DATA_CONST.__objc_classlist: 0x268
   __DATA_CONST.__objc_catlist: 0x20

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__objc_superrefs: 0xf0
-  __DATA_CONST.__auth_got: 0x1040
-  __DATA_CONST.__got: 0xa08
+  __DATA_CONST.__auth_got: 0x1048
+  __DATA_CONST.__got: 0xa38
   __DATA_CONST.__auth_ptr: 0x6f8
   __DATA.__objc_const: 0x6e78
-  __DATA.__objc_selrefs: 0x1eb8
+  __DATA.__objc_selrefs: 0x1ec0
   __DATA.__objc_ivar: 0x1fc
   __DATA.__objc_data: 0x2c90
   __DATA.__data: 0x84d0

   - /System/Library/PrivateFrameworks/OctagonTrust.framework/Versions/A/OctagonTrust
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/Versions/A/ProtocolBuffer
   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
+  - /System/Library/PrivateFrameworks/StorageContainersPrivate.framework/Versions/A/StorageContainersPrivate
   - /System/Library/PrivateFrameworks/TrustedPeers.framework/Versions/A/TrustedPeers
   - /System/Library/PrivateFrameworks/UserManagement.framework/Versions/A/UserManagement
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 8904
-  Symbols:   530
-  CStrings:  3495
+  Functions: 8917
+  Symbols:   538
+  CStrings:  3503
 
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
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
~ __DATA.__objc_stublist : content changed
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
