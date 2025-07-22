## OctagonTrust

> `/System/Library/PrivateFrameworks/OctagonTrust.framework/OctagonTrust`

```diff

-61901.0.46.502.1
-  __TEXT.__text: 0x1ea70
+61901.0.56.0.1
+  __TEXT.__text: 0x1eadc
   __TEXT.__auth_stubs: 0x660
   __TEXT.__objc_methlist: 0x194c
   __TEXT.__const: 0xf8
   __TEXT.__gcc_except_tab: 0x7c4
-  __TEXT.__cstring: 0x1160
+  __TEXT.__cstring: 0x12a0
   __TEXT.__oslogstring: 0x293e
   __TEXT.__unwind_info: 0x548
   __TEXT.__objc_classname: 0x202
-  __TEXT.__objc_methname: 0x3f00
+  __TEXT.__objc_methname: 0x3f1b
   __TEXT.__objc_methtype: 0x5b3
-  __TEXT.__objc_stubs: 0x2860
+  __TEXT.__objc_stubs: 0x2880
   __DATA_CONST.__got: 0x350
   __DATA_CONST.__const: 0x260
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf28
+  __DATA_CONST.__objc_selrefs: 0xf30
   __DATA_CONST.__objc_superrefs: 0x88
   __AUTH_CONST.__auth_got: 0x340
-  __AUTH_CONST.__cfstring: 0x13e0
+  __AUTH_CONST.__cfstring: 0x1500
   __AUTH_CONST.__objc_const: 0x2448
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x184

   - /System/Library/PrivateFrameworks/SecurityFoundation.framework/SecurityFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 57EFB739-FCA5-3020-8568-8B6FDB096211
+  UUID: E5E56283-347B-3F0E-9B69-9CA7DB595A9A
   Functions: 554
-  Symbols:   1924
-  CStrings:  1281
+  Symbols:   1925
+  CStrings:  1300
 
Symbols:
+ ___64+[OTClique(Framework) recoverWithRecoveryKey:recoveryKey:error:]_block_invoke.144
+ ___64+[OTClique(Framework) recoverWithRecoveryKey:recoveryKey:error:]_block_invoke.151
+ ___72+[OTClique(Framework) registerRecoveryKeyWithContext:recoveryKey:error:]_block_invoke.97
+ _objc_msgSend$initWithUserActivityLabel:
- ___64+[OTClique(Framework) recoverWithRecoveryKey:recoveryKey:error:]_block_invoke.123
- ___64+[OTClique(Framework) recoverWithRecoveryKey:recoveryKey:error:]_block_invoke.130
- ___72+[OTClique(Framework) registerRecoveryKeyWithContext:recoveryKey:error:]_block_invoke.85
Functions:
~ -[OTClique(Framework) removeRecoveryKeyFromSOSWhenNOTInCircle:error:] : 712 -> 724
~ -[OTClique(Framework) removeRecoveryKeyFromSOSWhenInCircle:error:] : 872 -> 884
~ +[OTClique(Framework) recoverWithRecoveryKey:recoveryKey:error:] : 3124 -> 3136
~ +[OTClique(Framework) doesRecoveryKeyExistInSOSAndIsCorrect:recoveryKey:error:] : 684 -> 696
~ +[OTClique(Framework) isRecoveryKeySetInSOS:error:] : 492 -> 504
~ +[OTClique(Framework) registerRecoveryKeyInSOSAndBackup:recoveryKey:error:] : 1284 -> 1296
~ +[OTClique(Framework) performSilentEscrowRecovery:cdpContext:allRecords:error:] : 4296 -> 4308
~ +[OTClique(Framework) performEscrowRecovery:cdpContext:escrowRecord:error:] : 4484 -> 4496
~ +[OTClique(Framework) handleRecoveryResults:recoveredInformation:record:performedSilentBurn:error:] : 3988 -> 4000
CStrings:
+ "initWithUserActivityLabel:"
+ "octagon-trust-is-recovery-key-in-sos"
+ "octagon-trust-perform-recovery"
+ "octagon-trust-perform-silent-recovery"
+ "octagon-trust-recover-with-recovery-key"
+ "octagon-trust-register-recovery-key"
+ "octagon-trust-remove-recovery-key"
+ "octagon-trust-remove-recovery-key-not-in-circle"
+ "octagon-trust-restore"
+ "octagon-trust-verify-recovery-key"

```
