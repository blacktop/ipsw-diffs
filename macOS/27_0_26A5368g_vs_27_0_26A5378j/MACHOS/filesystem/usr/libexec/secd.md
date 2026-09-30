## secd

> `/usr/libexec/secd`

```diff

-  __TEXT.__text: 0x289404
+  __TEXT.__text: 0x28a2d8
   __TEXT.__auth_stubs: 0x40e0
-  __TEXT.__objc_stubs: 0x1d780
-  __TEXT.__objc_methlist: 0x15e48
-  __TEXT.__const: 0x930
+  __TEXT.__objc_stubs: 0x1d7c0
+  __TEXT.__objc_methlist: 0x15e50
+  __TEXT.__const: 0x920
   __TEXT.__objc_classname: 0x24f5
-  __TEXT.__objc_methname: 0x2e3f6
-  __TEXT.__objc_methtype: 0xaf85
+  __TEXT.__objc_methname: 0x2e46a
+  __TEXT.__objc_methtype: 0xafe1
   __TEXT.__constg_swiftt: 0x274
-  __TEXT.__swift5_typeref: 0x364
+  __TEXT.__swift5_typeref: 0x35e
   __TEXT.__swift5_reflstr: 0xc7
   __TEXT.__swift5_fieldmd: 0x120
   __TEXT.__swift5_assocty: 0x48
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_proto: 0x24
   __TEXT.__swift5_types: 0x20
-  __TEXT.__cstring: 0x2189e
-  __TEXT.__oslogstring: 0x2f7a2
+  __TEXT.__cstring: 0x218cc
+  __TEXT.__oslogstring: 0x2f97c
   __TEXT.__swift5_capture: 0x1bc
   __TEXT.__swift_as_entry: 0x40
   __TEXT.__swift_as_ret: 0x3c
   __TEXT.__swift_as_cont: 0x48
-  __TEXT.__gcc_except_tab: 0x9f44
+  __TEXT.__gcc_except_tab: 0xa0a8
   __TEXT.__dlopen_cstrs: 0xb4
-  __TEXT.__unwind_info: 0x6980
+  __TEXT.__unwind_info: 0x6988
   __TEXT.__eh_frame: 0xa60
   __DATA_CONST.__const: 0x15988
   __DATA_CONST.__cfstring: 0x1b9c0

   __DATA_CONST.__objc_dictobj: 0x78
   __DATA_CONST.__objc_arrayobj: 0x360
   __DATA_CONST.__auth_got: 0x2080
-  __DATA_CONST.__got: 0x1318
+  __DATA_CONST.__got: 0x1460
   __DATA_CONST.__auth_ptr: 0x1d8
   __DATA.__objc_const: 0x23c38
-  __DATA.__objc_selrefs: 0x9800
+  __DATA.__objc_selrefs: 0x9808
   __DATA.__objc_ivar: 0x1ae8
   __DATA.__objc_data: 0x5d48
-  __DATA.__data: 0x30a0
+  __DATA.__data: 0x3098
   __DATA.__thread_vars: 0xc0
   __DATA.__thread_bss: 0x30
   __DATA.__bss: 0x12a8

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 10029
-  Symbols:   1842
-  CStrings:  20110
+  Functions: 10030
+  Symbols:   1843
+  CStrings:  20119
 
Sections:
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_fieldmd : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift5_types : content changed
~ __TEXT.__swift5_capture : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift_as_cont : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__thread_vars : content changed
~ __DATA.__bss : content changed
Symbols:
+ _kSecurityRTCEventNameVouchWithRK
+ _kSecurityRTCFieldDistrustEveryoneOnJoin
- _swift_runtimeSupportsNoncopyableTypes
CStrings:
+ "-[CuttlefishXPCWrapper vouchWithRecoveryKeyWithSpecificUser:recoveryKey:salt:tlkShares:altDSID:flowID:deviceSessionID:canSendMetrics:reply:]_block_invoke"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wifYPg/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wifYPg/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
+ "@\"OTCheckHealthOperation\""
+ "B52@0:8@16@24@32B40^@44"
+ "Couldn't verify signature of TLKShare (%@) that includes tlkOwnershipProof as part of dataForSigning; trying again without tlkOwnershipProof"
+ "Existing TLKShare's ownership proof for peer %@ from self %@ is invalid. Will update TLK Share %@"
+ "Existing TLKShare's signature for peer %@ from self %@ is invalid. Will update TLK Share %@"
+ "Finishing vouching with recovery key with %@"
+ "Proposed TLKShare(%@) supercedes existing TLKShare(%@)"
+ "Unable to generate TLK ownership proof: %@"
+ "_currentHealthCheckOp"
+ "dataForSigning:includeProof:"
+ "v84@0:8@\"TPSpecificUser\"16@\"NSString\"24@\"NSString\"32@\"NSArray\"40@\"NSString\"48@\"NSString\"56@\"NSString\"64B72@?<v@?@\"NSData\"@\"NSData\"@\"NSArray\"B@\"TrustedPeersHelperTLKRecoveryResult\"@\"NSError\">76"
+ "verifySignature:verifyingPeer:acceptProoflessSig:error:"
+ "verifySignature:verifyingPeer:ckrecord:acceptProoflessSig:error:"
+ "vouchWithRecoveryKeyWithSpecificUser:recoveryKey:salt:tlkShares:altDSID:flowID:deviceSessionID:canSendMetrics:reply:"
- "-[CuttlefishXPCWrapper vouchWithRecoveryKeyWithSpecificUser:recoveryKey:salt:tlkShares:reply:]_block_invoke"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6yKJWu/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6yKJWu/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
- "_healthCheckResults"
- "v56@0:8@\"TPSpecificUser\"16@\"NSString\"24@\"NSString\"32@\"NSArray\"40@?<v@?@\"NSData\"@\"NSData\"@\"NSArray\"B@\"TrustedPeersHelperTLKRecoveryResult\"@\"NSError\">48"
- "verifySignature:verifyingPeer:ckrecord:error:"
- "verifySignature:verifyingPeer:error:"
- "vouchWithRecoveryKeyWithSpecificUser:recoveryKey:salt:tlkShares:reply:"

```
