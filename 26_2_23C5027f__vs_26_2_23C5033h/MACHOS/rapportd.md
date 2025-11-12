## rapportd

> `/usr/libexec/rapportd`

```diff

-716.300.51.0.0
-  __TEXT.__text: 0x14d090
-  __TEXT.__auth_stubs: 0x36e0
+716.300.121.0.0
+  __TEXT.__text: 0x157ad8
+  __TEXT.__auth_stubs: 0x3710
   __TEXT.__objc_stubs: 0x10920
-  __TEXT.__objc_methlist: 0x86e4
-  __TEXT.__const: 0x5aa0
-  __TEXT.__cstring: 0x2f4b1
+  __TEXT.__objc_methlist: 0x86f4
+  __TEXT.__const: 0x5ce0
+  __TEXT.__cstring: 0x2f6a1
   __TEXT.__objc_classname: 0xaa1
-  __TEXT.__objc_methtype: 0x3d1b
+  __TEXT.__objc_methtype: 0x3d73
   __TEXT.__gcc_except_tab: 0x2094
-  __TEXT.__objc_methname: 0x17e4d
-  __TEXT.__oslogstring: 0x27c2
-  __TEXT.__swift5_typeref: 0x1454
-  __TEXT.__swift5_capture: 0xa8c
-  __TEXT.__swift5_reflstr: 0xd64
+  __TEXT.__objc_methname: 0x17e8d
+  __TEXT.__oslogstring: 0x2912
+  __TEXT.__swift5_typeref: 0x1534
+  __TEXT.__swift5_capture: 0xb40
+  __TEXT.__swift5_reflstr: 0xde4
   __TEXT.__swift5_assocty: 0x130
-  __TEXT.__constg_swiftt: 0xbd8
+  __TEXT.__constg_swiftt: 0xc18
   __TEXT.__swift5_builtin: 0x64
-  __TEXT.__swift5_fieldmd: 0xdec
+  __TEXT.__swift5_fieldmd: 0xe44
   __TEXT.__swift5_proto: 0x1dc
-  __TEXT.__swift5_types: 0xf0
-  __TEXT.__swift_as_entry: 0x1fc
-  __TEXT.__swift_as_ret: 0x240
+  __TEXT.__swift5_types: 0xf4
+  __TEXT.__swift_as_entry: 0x210
+  __TEXT.__swift_as_ret: 0x25c
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__swift5_acfuncs: 0xc8
+  __TEXT.__swift5_acfuncs: 0x104
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x4b88
-  __TEXT.__eh_frame: 0x4684
-  __DATA_CONST.__auth_got: 0x1b80
-  __DATA_CONST.__got: 0x988
-  __DATA_CONST.__auth_ptr: 0x5b0
-  __DATA_CONST.__const: 0x7580
-  __DATA_CONST.__cfstring: 0x5ea0
+  __TEXT.__unwind_info: 0x4cc8
+  __TEXT.__eh_frame: 0x4c1c
+  __DATA_CONST.__auth_got: 0x1b98
+  __DATA_CONST.__got: 0x980
+  __DATA_CONST.__auth_ptr: 0x5a8
+  __DATA_CONST.__const: 0x7620
+  __DATA_CONST.__cfstring: 0x5ec0
   __DATA_CONST.__objc_classlist: 0x2f8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x160

   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA.__objc_const: 0xef80
-  __DATA.__objc_selrefs: 0x5230
+  __DATA.__objc_const: 0xefa8
+  __DATA.__objc_selrefs: 0x5238
   __DATA.__objc_ivar: 0xe8c
   __DATA.__objc_data: 0x24b8
-  __DATA.__data: 0x33b8
-  __DATA.__bss: 0x47b0
+  __DATA.__data: 0x34f8
+  __DATA.__bss: 0x4740
   __DATA.__common: 0xc8
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 04DB1E50-2308-3587-9549-91247C66E6A5
-  Functions: 7077
-  Symbols:   1362
-  CStrings:  10338
+  UUID: 11C608CB-49E5-30B5-BF80-79A7D61C2295
+  Functions: 7141
+  Symbols:   1364
+  CStrings:  10353
 
Symbols:
+ _$sSS14_fromSubstringySSSshFZ
+ _$sSS5index_8offsetBy07limitedC0SS5IndexVSgAE_SiAEtF
+ _$sScTMa
+ _swift_release_n
- _$s11Distributed0A5ActorP15unownedExecutorScevgTj
- _$sSo8NSObjectCs23CustomStringConvertible10FoundationMc
CStrings:
+ ", serverIdentity: "
+ "Another processPairVerifyData call is already in progress for this session"
+ "Legacy resolveBonjourEncrypted using session %s"
+ "Legacy startPairVerify created session %s"
+ "No legacy session available for encrypted resolveBonjour"
+ "No pairing session found for session "
+ "PairVerify session "
+ "PairVerify session already completed"
+ "PairVerify session not initialized (call startPairVerify first)"
+ "PairVerify timeout for session %s"
+ "RPPairingDistributedActor-"
+ "Received data to send with no client to send to for session %s"
+ "Server PairVerify completed for session %s: %s"
+ "Server PairVerify failed for session %s: %@"
+ "Server PairVerify identity expired for session %s, failing: %@"
+ "Server PairVerify session %s activated and ready"
+ "Server PairVerify succeeded for session %s: %@"
+ "Server PairVerifySign failed for session %s: %@"
+ "Server PairVerifySign succeeded for session %s"
+ "Server encryption stream created on-demand for session %s"
+ "Server resolveBonjourEncrypted for session %s"
+ "Session %s already completed, cannot process more data"
+ "Session %s already has a pending processPairVerifyData call"
+ "Starting PairVerify with session tracking (createEncryptionStream %{bool}d)"
+ "Successfully processed encrypted resolveBonjour request for session %s"
+ "legacySessionID"
+ "pairVerifySessions"
+ "pendingContinuation"
+ "performPairVerifyExchange (sessionID: %s, createEncryptionStream: %{bool}d)"
+ "performPairVerifyExchange(with:sessionID:for:createEncryptionStream:)"
+ "processPairVerifyDataWithSessionID(_:sessionID:)"
+ "rapport:rdid:"
+ "service:account:didReceiveLocalNetworkHandshake:fromID:context:"
+ "v52@0:8@\"IDSService\"16@\"IDSAccount\"24B32@\"NSString\"36@\"NSData\"44"
+ "v52@0:8@16@24B32@36@44"
- "No pairing session available"
- "PairVerify session not initialized"
- "Received data to send with no client to send to"
- "Resetting session state"
- "Server PairVerify completed: %s"
- "Server PairVerify failed: %@"
- "Server PairVerify identity expired, failing: %@"
- "Server PairVerify session activated and ready"
- "Server PairVerify succeeded: %@"
- "Server PairVerifySign failed: %@"
- "Server PairVerifySign succeeded"
- "Server encryption stream created on-demand"
- "Server resolveBonjourEncrypted"
- "Session already completed, cannot process more data"
- "Starting PairVerify (createEncryptionStream %{bool}d)"
- "Successfully processed encrypted resolveBonjour request"
- "performPairVerifyExchange (createEncryptionStream: %{bool}d)"
- "performPairVerifyExchange(with:for:createEncryptionStream:)"
- "processPairVerifyData(_:)"
- "timeoutTask"

```
