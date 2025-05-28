## OctagonTrust

> `/System/Library/PrivateFrameworks/OctagonTrust.framework/OctagonTrust`

```diff

-61040.82.1.0.0
-  __TEXT.__text: 0x1dfe0
+61123.100.169.0.0
+  __TEXT.__text: 0x1e064
   __TEXT.__auth_stubs: 0x6a0
-  __TEXT.__objc_methlist: 0x166c
+  __TEXT.__objc_methlist: 0x16b4
   __TEXT.__const: 0xc0
-  __TEXT.__gcc_except_tab: 0x788
-  __TEXT.__cstring: 0x141d
+  __TEXT.__gcc_except_tab: 0x64c
+  __TEXT.__cstring: 0x1453
   __TEXT.__dlopen_cstrs: 0xb0
-  __TEXT.__oslogstring: 0x2857
-  __TEXT.__unwind_info: 0x6bc
+  __TEXT.__oslogstring: 0x281e
+  __TEXT.__unwind_info: 0x6d4
   __TEXT.__objc_classname: 0x1c0
-  __TEXT.__objc_methname: 0x3868
-  __TEXT.__objc_methtype: 0x52d
-  __TEXT.__objc_stubs: 0x2320
+  __TEXT.__objc_methname: 0x390e
+  __TEXT.__objc_methtype: 0x531
+  __TEXT.__objc_stubs: 0x2380
   __DATA_CONST.__got: 0x78
   __DATA_CONST.__const: 0x280
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1ae0
-  __DATA_CONST.__objc_selrefs: 0xd70
+  __DATA_CONST.__objc_const: 0x1b20
+  __DATA_CONST.__objc_selrefs: 0xd98
+  __DATA_CONST.__objc_classrefs: 0x110
+  __DATA_CONST.__objc_superrefs: 0x78
   __AUTH_CONST.__cfstring: 0x1220
   __AUTH_CONST.__objc_const: 0x0
   __AUTH_CONST.__auth_got: 0x360
-  __DATA.__objc_classrefs: 0x110
-  __DATA.__objc_superrefs: 0x78
-  __DATA.__objc_ivar: 0x158
-  __DATA.__data: 0x138
-  __DATA.__bss: 0x148
+  __DATA.__objc_ivar: 0x15c
+  __DATA.__data: 0x1c8
+  __DATA.__bss: 0xc8
   __DATA_DIRTY.__objc_const: 0x618
   __DATA_DIRTY.__objc_data: 0x500
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 578
-  Symbols:   1919
-  CStrings:  1061
+  Functions: 586
+  Symbols:   1943
+  CStrings:  1067
 
Symbols:
+ +[OTClique(Framework) ensureBackupKeyExistsinSOS:]
+ +[OTClique(Framework) registerRecoveryKeyInSOSAndBackup:recoveryKey:error:]
+ -[OTCDPRecoveryInformation hasNonViableRepair]
+ -[OTCDPRecoveryInformation nonViableRepair]
+ -[OTCDPRecoveryInformation setHasNonViableRepair:]
+ -[OTCDPRecoveryInformation setNonViableRepair:]
+ GCC_except_table196
+ GCC_except_table197
+ GCC_except_table212
+ GCC_except_table213
+ GCC_except_table214
+ GCC_except_table215
+ GCC_except_table338
+ GCC_except_table343
+ GCC_except_table349
+ GCC_except_table351
+ GCC_except_table353
+ GCC_except_table355
+ GCC_except_table357
+ GCC_except_table359
+ GCC_except_table361
+ GCC_except_table363
+ GCC_except_table365
+ GCC_except_table367
+ GCC_except_table369
+ GCC_except_table373
+ GCC_except_table378
+ GCC_except_table383
+ GCC_except_table386
+ GCC_except_table394
+ GCC_except_table396
+ GCC_except_table399
+ GCC_except_table402
+ OBJC_IVAR_$_OTCDPRecoveryInformation._nonViableRepair
+ _CloudServicesLibrary.605
+ _CloudServicesLibraryCore.frameworkLibrary.606
+ ___64+[OTClique(Framework) recoverWithRecoveryKey:recoveryKey:error:]_block_invoke.109
+ ___64+[OTClique(Framework) recoverWithRecoveryKey:recoveryKey:error:]_block_invoke.116
+ ___72+[OTClique(Framework) registerRecoveryKeyWithContext:recoveryKey:error:]_block_invoke.71
+ ___CloudServicesLibraryCore_block_invoke.607
+ ___getkSecureBackupNonViableRepairKeySymbolLoc_block_invoke
+ ___getkSecureBackupSilentRecoveryAttemptKeySymbolLoc_block_invoke
+ _audit_stringCloudServices.609
+ _getkSecureBackupNonViableRepairKey
+ _getkSecureBackupNonViableRepairKeySymbolLoc.ptr
+ _getkSecureBackupSilentRecoveryAttemptKey
+ _getkSecureBackupSilentRecoveryAttemptKeySymbolLoc.ptr
+ _objc_msgSend$ensureBackupKeyExistsinSOS:
+ _objc_msgSend$nonViableRepair
+ _objc_msgSend$registerRecoveryKeyInSOSAndBackup:recoveryKey:error:
+ _objc_msgSend$setNonViableRepair:
- GCC_except_table203
- GCC_except_table204
- GCC_except_table205
- GCC_except_table206
- GCC_except_table334
- GCC_except_table339
- GCC_except_table344
- GCC_except_table346
- GCC_except_table348
- GCC_except_table350
- GCC_except_table352
- GCC_except_table354
- GCC_except_table356
- GCC_except_table358
- GCC_except_table360
- GCC_except_table362
- GCC_except_table364
- GCC_except_table366
- GCC_except_table370
- GCC_except_table375
- GCC_except_table377
- GCC_except_table388
- GCC_except_table390
- GCC_except_table395
- GCC_except_table398
- _CloudServicesLibrary.602
- _CloudServicesLibraryCore.frameworkLibrary.603
- ___54-[OTClique(Framework) deliverAKDeviceListDelta:error:]_block_invoke
- ___64+[OTClique(Framework) recoverWithRecoveryKey:recoveryKey:error:]_block_invoke.110
- ___64+[OTClique(Framework) recoverWithRecoveryKey:recoveryKey:error:]_block_invoke.117
- ___72+[OTClique(Framework) registerRecoveryKeyWithContext:recoveryKey:error:]_block_invoke.64
- ___72+[OTClique(Framework) registerRecoveryKeyWithContext:recoveryKey:error:]_block_invoke.69
- ___CloudServicesLibraryCore_block_invoke.604
- _audit_stringCloudServices.606
- _objc_msgSend$deliverAKDeviceListDelta:reply:
CStrings:
+ "TB,N,V_nonViableRepair"
+ "Unimplemented deliverAKDeviceListDelta for context:%@"
+ "_nonViableRepair"
+ "device is not participating in SOS, skipping recovery key registration"
+ "ensureBackupKeyExistsinSOS:"
+ "hasNonViableRepair"
+ "kSecureBackupNonViableRepairKey"
+ "kSecureBackupSilentRecoveryAttemptKey"
+ "nonViableRepair"
+ "non_viable_repair"
+ "registerRecoveryKeyInSOSAndBackup:recoveryKey:error:"
+ "setHasNonViableRepair:"
+ "setNonViableRepair:"
+ "{?=\"containsIcdpData\"b1\"nonViableRepair\"b1\"silentRecoveryAttempt\"b1\"useCachedSecret\"b1\"usePreviouslyCachedRecoveryKey\"b1\"usesMultipleIcsc\"b1}"
- "AKDeviceList change delivery errored: %@"
- "AKDeviceList change delivery succeeded"
- "Delivering authkit payload for context:%@"
- "SecureBackupSilentRecoveryAttempt"
- "deliverAKDeviceListDelta:reply:"
- "octagon-register-recovery-key: removeRecoveryKey failed: %@"
- "v32@0:8@16^@24"
- "{?=\"containsIcdpData\"b1\"silentRecoveryAttempt\"b1\"useCachedSecret\"b1\"usePreviouslyCachedRecoveryKey\"b1\"usesMultipleIcsc\"b1}"

```
