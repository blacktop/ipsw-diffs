## OctagonTrust

> `/System/Library/PrivateFrameworks/OctagonTrust.framework/OctagonTrust`

```diff

-61040.2.2.0.0
-  __TEXT.__text: 0x1ce44
-  __TEXT.__auth_stubs: 0x690
-  __TEXT.__objc_methlist: 0x162c
+61040.42.1.0.0
+  __TEXT.__text: 0x1dfd4
+  __TEXT.__auth_stubs: 0x6a0
+  __TEXT.__objc_methlist: 0x166c
   __TEXT.__const: 0xc0
-  __TEXT.__gcc_except_tab: 0x6fc
-  __TEXT.__cstring: 0x1376
+  __TEXT.__gcc_except_tab: 0x788
+  __TEXT.__cstring: 0x141d
   __TEXT.__dlopen_cstrs: 0xb0
-  __TEXT.__oslogstring: 0x24c7
-  __TEXT.__unwind_info: 0x694
+  __TEXT.__oslogstring: 0x2857
+  __TEXT.__unwind_info: 0x6bc
   __TEXT.__objc_classname: 0x1c0
-  __TEXT.__objc_methname: 0x371c
-  __TEXT.__objc_methtype: 0x50c
-  __TEXT.__objc_stubs: 0x2240
+  __TEXT.__objc_methname: 0x3868
+  __TEXT.__objc_methtype: 0x52d
+  __TEXT.__objc_stubs: 0x2320
   __DATA_CONST.__got: 0x78
   __DATA_CONST.__const: 0x280
   __DATA_CONST.__objc_classlist: 0x80

   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x1ae0
-  __DATA_CONST.__objc_selrefs: 0xd30
-  __AUTH_CONST.__cfstring: 0x1140
+  __DATA_CONST.__objc_selrefs: 0xd70
+  __AUTH_CONST.__cfstring: 0x1220
   __AUTH_CONST.__objc_const: 0x0
-  __AUTH_CONST.__auth_got: 0x358
+  __AUTH_CONST.__auth_got: 0x360
   __DATA.__objc_classrefs: 0x110
   __DATA.__objc_superrefs: 0x78
   __DATA.__objc_ivar: 0x158

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 31141E87-6C0F-3ABD-955A-798A8573411D
-  Functions: 571
-  Symbols:   1895
-  CStrings:  1167
+  UUID: B1EFB60A-4F01-3C17-815B-882B0A7A83F1
+  Functions: 578
+  Symbols:   1919
+  CStrings:  1206
 
Symbols:
+ +[OTClique(Framework) areRecoveryKeysDistrusted:error:]
+ +[OTClique(Framework) doesRecoveryKeyExistInOctagonAndIsCorrect:recoveryKey:error:]
+ +[OTClique(Framework) doesRecoveryKeyExistInSOSAndIsCorrect:recoveryKey:error:]
+ -[OTClique(Framework) removeRecoveryKeyFromSOSWhenInCircle:error:]
+ -[OTClique(Framework) removeRecoveryKeyFromSOSWhenNOTInCircle:error:]
+ GCC_except_table339
+ GCC_except_table364
+ GCC_except_table366
+ GCC_except_table375
+ GCC_except_table377
+ GCC_except_table380
+ GCC_except_table390
+ GCC_except_table392
+ GCC_except_table395
+ GCC_except_table398
+ _SOSCCPushResetCircle
+ ___55+[OTClique(Framework) areRecoveryKeysDistrusted:error:]_block_invoke
+ ___64+[OTClique(Framework) recoverWithRecoveryKey:recoveryKey:error:]_block_invoke.110
+ ___64+[OTClique(Framework) recoverWithRecoveryKey:recoveryKey:error:]_block_invoke.117
+ ___83+[OTClique(Framework) doesRecoveryKeyExistInOctagonAndIsCorrect:recoveryKey:error:]_block_invoke
+ ___getkSecureBackupRecordIDKeySymbolLoc_block_invoke.631
+ ___getkSecureBackupRecordLabelKeySymbolLoc_block_invoke.629
+ _getkSecureBackupRecordIDKeySymbolLoc.ptr.630
+ _getkSecureBackupRecordLabelKeySymbolLoc.ptr.628
+ _objc_msgSend$areRecoveryKeysDistrusted:reply:
+ _objc_msgSend$doesRecoveryKeyExistInOctagonAndIsCorrect:recoveryKey:error:
+ _objc_msgSend$doesRecoveryKeyExistInSOSAndIsCorrect:recoveryKey:error:
+ _objc_msgSend$removeRecoveryKeyFromBackup:
+ _objc_msgSend$removeRecoveryKeyFromSOSWhenInCircle:error:
+ _objc_msgSend$removeRecoveryKeyFromSOSWhenNOTInCircle:error:
+ _objc_msgSend$verifyRecoveryKey:error:
+ _objc_retain_x27
- GCC_except_table335
- GCC_except_table342
- GCC_except_table368
- GCC_except_table373
- GCC_except_table381
- GCC_except_table383
- GCC_except_table385
- GCC_except_table391
- ___64+[OTClique(Framework) recoverWithRecoveryKey:recoveryKey:error:]_block_invoke.102
- ___64+[OTClique(Framework) recoverWithRecoveryKey:recoveryKey:error:]_block_invoke.95
- ___getkSecureBackupRecordIDKeySymbolLoc_block_invoke.629
- ___getkSecureBackupRecordLabelKeySymbolLoc_block_invoke.627
- _getkSecureBackupRecordIDKeySymbolLoc.ptr.628
- _getkSecureBackupRecordLabelKeySymbolLoc.ptr.626
- _objc_release_x10
CStrings:
+ "NO"
+ "Octagon circle %@ distrusted recovery keys"
+ "Recovery key does not exist in Octagon"
+ "Recovery key is incorrect"
+ "Recovery key is not correct"
+ "Removing recovery key when device is in circle"
+ "Removing recovery key when not in circle"
+ "YES"
+ "areRecoveryKeysDistrusted errored: %@"
+ "areRecoveryKeysDistrusted invoked for context: %@"
+ "areRecoveryKeysDistrusted succeeded, octagon circle contains distrusted recovery keys: %@"
+ "areRecoveryKeysDistrusted:error:"
+ "areRecoveryKeysDistrusted:reply:"
+ "contains"
+ "does not contain"
+ "doesRecoveryKeyExistInOctagonAndIsCorrect:recoveryKey:error:"
+ "doesRecoveryKeyExistInSOSAndIsCorrect:recoveryKey:error:"
+ "octagon-contain-distrusted-recovery-keys"
+ "octagon-recover-with-rk: Recovery Key not registered in SOS: %@"
+ "octagon-recover-with-rk: joining with recovery key failed, recovery key is not correct in Octagon"
+ "octagon-recover-with-rk: recovery key not registered in Octagon, error: %@"
+ "octagon-recover-with-rk: recovery key will not work for both SOS and Octagon"
+ "octagon-recover-with-rk: unable to create otcontrol: %@"
+ "octagon-register-recovery-key, recovery key not registered in SOS: %@"
+ "octagon-remove-recovery-key, error checking SOS circle status: %@"
+ "octagon-remove-recovery-key, error removing recovery key from SOS: %@"
+ "octagon-remove-recovery-key: failed to push: %@"
+ "octagon-remove-recovery-key: failed to remove recovery key from the backup: %@"
+ "q40@0:8@16@24^@32"
+ "recovery key is NOT correct in SOS"
+ "recovery key is registered in Octagon, checking if it is correct"
+ "removeRecoveryKeyFromBackup:"
+ "removeRecoveryKeyFromSOSWhenInCircle:error:"
+ "removeRecoveryKeyFromSOSWhenNOTInCircle:error:"
+ "removed recovery key from the backup"
+ "successfully pushed a reset circle"
+ "v32@0:8@16^@24"
+ "verifyRecoveryKey:error:"
- "Recovery key not set in Octagon"
- "octagon-remove-recovery-key: failed to check if recovery key is set in Octagon: %@"
- "recovery key is NOT registered in Octagon"
- "recovery key is NOT registered in SOS"
- "recovery key is registered in Octagon"
- "recovery key not set in SOS, error: %@"

```
