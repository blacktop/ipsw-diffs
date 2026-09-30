## securityd

> `/usr/libexec/securityd`

```diff

-  __TEXT.__text: 0x26b4bc
+  __TEXT.__text: 0x26c4bc
   __TEXT.__auth_stubs: 0x4350
-  __TEXT.__objc_stubs: 0x1d880
-  __TEXT.__objc_methlist: 0x15e48
-  __TEXT.__const: 0x920
-  __TEXT.__cstring: 0x226e5
-  __TEXT.__objc_methname: 0x2e54b
-  __TEXT.__oslogstring: 0x2fbe2
-  __TEXT.__swift5_typeref: 0x378
+  __TEXT.__objc_stubs: 0x1d8c0
+  __TEXT.__objc_methlist: 0x15e50
+  __TEXT.__const: 0x910
+  __TEXT.__cstring: 0x2273b
+  __TEXT.__objc_methname: 0x2e5af
+  __TEXT.__oslogstring: 0x2fe5c
+  __TEXT.__swift5_typeref: 0x372
   __TEXT.__swift5_fieldmd: 0x120
   __TEXT.__objc_classname: 0x2548
-  __TEXT.__objc_methtype: 0xafbe
+  __TEXT.__objc_methtype: 0xb01a
   __TEXT.__constg_swiftt: 0x274
   __TEXT.__swift5_reflstr: 0xc3
   __TEXT.__swift5_capture: 0x1bc

   __TEXT.__swift_as_entry: 0x40
   __TEXT.__swift_as_ret: 0x3c
   __TEXT.__swift_as_cont: 0x48
-  __TEXT.__gcc_except_tab: 0x9f10
+  __TEXT.__gcc_except_tab: 0xa074
   __TEXT.__dlopen_cstrs: 0xb4
   __TEXT.__ustring: 0x28
-  __TEXT.__unwind_info: 0x6a50
+  __TEXT.__unwind_info: 0x6a58
   __TEXT.__eh_frame: 0xa60
-  __DATA_CONST.__const: 0x14920
-  __DATA_CONST.__cfstring: 0x1c480
+  __DATA_CONST.__const: 0x14948
+  __DATA_CONST.__cfstring: 0x1c4a0
   __DATA_CONST.__objc_classlist: 0x908
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0x260

   __DATA_CONST.__objc_dictobj: 0x78
   __DATA_CONST.__objc_arrayobj: 0x360
   __DATA_CONST.__auth_got: 0x21b8
-  __DATA_CONST.__got: 0x13e0
+  __DATA_CONST.__got: 0x1528
   __DATA_CONST.__auth_ptr: 0x1d8
   __DATA.__objc_const: 0x23c40
-  __DATA.__objc_selrefs: 0x9848
+  __DATA.__objc_selrefs: 0x9850
   __DATA.__objc_ivar: 0x1ae8
   __DATA.__objc_data: 0x5d48
-  __DATA.__data: 0x3158
+  __DATA.__data: 0x3150
   __DATA.__thread_vars: 0xc0
   __DATA.__thread_bss: 0x28
   __DATA.__bss: 0xed0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 9908
-  Symbols:   1889
-  CStrings:  20333
+  Functions: 9910
+  Symbols:   1890
+  CStrings:  20347
 
Sections:
~ __TEXT.__swift5_fieldmd : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_capture : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift5_types : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift_as_cont : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__objc_dictobj : content changed
~ __DATA_CONST.__objc_arrayobj : content changed
~ __DATA_CONST.__auth_got : content changed
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
+ "@\"OTCheckHealthOperation\""
+ "B52@0:8@16@24@32B40^@44"
+ "Couldn't verify signature of TLKShare (%@) that includes tlkOwnershipProof as part of dataForSigning; trying again without tlkOwnershipProof"
+ "Existing TLKShare's ownership proof for peer %@ from self %@ is invalid. Will update TLK Share %@"
+ "Existing TLKShare's signature for peer %@ from self %@ is invalid. Will update TLK Share %@"
+ "Finishing vouching with recovery key with %@"
+ "Proposed TLKShare(%@) supercedes existing TLKShare(%@)"
+ "Unable to generate TLK ownership proof: %@"
+ "_currentHealthCheckOp"
+ "active user: %d"
+ "com.apple.FileProvider.usermanager.sync"
+ "dataForSigning:includeProof:"
+ "onlyDelete: %{BOOL}d, copyCloudAuthToken: %{BOOL}d, copyMobileMail: %{BOOL}d, copyNSURLSession: %{BOOL}d, copyPCS: %{BOOL}d"
+ "unknown service: %@"
+ "v84@0:8@\"TPSpecificUser\"16@\"NSString\"24@\"NSString\"32@\"NSArray\"40@\"NSString\"48@\"NSString\"56@\"NSString\"64B72@?<v@?@\"NSData\"@\"NSData\"@\"NSArray\"B@\"TrustedPeersHelperTLKRecoveryResult\"@\"NSError\">76"
+ "verifySignature:verifyingPeer:acceptProoflessSig:error:"
+ "verifySignature:verifyingPeer:ckrecord:acceptProoflessSig:error:"
+ "vouchWithRecoveryKeyWithSpecificUser:recoveryKey:salt:tlkShares:altDSID:flowID:deviceSessionID:canSendMetrics:reply:"
- "-[CuttlefishXPCWrapper vouchWithRecoveryKeyWithSpecificUser:recoveryKey:salt:tlkShares:reply:]_block_invoke"
- "_healthCheckResults"
- "v56@0:8@\"TPSpecificUser\"16@\"NSString\"24@\"NSString\"32@\"NSArray\"40@?<v@?@\"NSData\"@\"NSData\"@\"NSArray\"B@\"TrustedPeersHelperTLKRecoveryResult\"@\"NSError\">48"
- "verifySignature:verifyingPeer:ckrecord:error:"
- "verifySignature:verifyingPeer:error:"
- "vouchWithRecoveryKeyWithSpecificUser:recoveryKey:salt:tlkShares:reply:"

```
