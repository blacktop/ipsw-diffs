## securityd

> `/usr/libexec/securityd`

```diff

-61901.100.267.0.2
-  __TEXT.__text: 0x27d928
-  __TEXT.__auth_stubs: 0x4220
-  __TEXT.__objc_stubs: 0x1cc40
-  __TEXT.__objc_methlist: 0x15638
+61901.100.281.0.1
+  __TEXT.__text: 0x27d0f4
+  __TEXT.__auth_stubs: 0x4210
+  __TEXT.__objc_stubs: 0x1cc60
+  __TEXT.__objc_methlist: 0x15670
   __TEXT.__const: 0x921
-  __TEXT.__cstring: 0x214d7
-  __TEXT.__objc_methname: 0x2ccb8
-  __TEXT.__oslogstring: 0x2e54d
+  __TEXT.__cstring: 0x214d6
+  __TEXT.__objc_methname: 0x2cd98
+  __TEXT.__oslogstring: 0x2e6cb
   __TEXT.__swift5_typeref: 0x378
   __TEXT.__swift5_fieldmd: 0x120
   __TEXT.__objc_classname: 0x2555
-  __TEXT.__objc_methtype: 0xa7e3
+  __TEXT.__objc_methtype: 0xa80d
   __TEXT.__constg_swiftt: 0x274
   __TEXT.__swift5_reflstr: 0xc3
   __TEXT.__swift5_capture: 0x1bc

   __TEXT.__swift5_types: 0x20
   __TEXT.__swift_as_entry: 0x40
   __TEXT.__swift_as_ret: 0x3c
-  __TEXT.__gcc_except_tab: 0xb3dc
+  __TEXT.__gcc_except_tab: 0xb448
   __TEXT.__dlopen_cstrs: 0xb4
   __TEXT.__ustring: 0x28
-  __TEXT.__unwind_info: 0x6eb8
+  __TEXT.__unwind_info: 0x6ea0
   __TEXT.__eh_frame: 0xa58
-  __DATA_CONST.__auth_got: 0x2120
+  __DATA_CONST.__auth_got: 0x2118
   __DATA_CONST.__got: 0x1388
   __DATA_CONST.__auth_ptr: 0x1d8
-  __DATA_CONST.__const: 0x145e0
-  __DATA_CONST.__cfstring: 0x1bbe0
+  __DATA_CONST.__const: 0x14548
+  __DATA_CONST.__cfstring: 0x1bb40
   __DATA_CONST.__objc_classlist: 0x8e0
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0x250

   __DATA_CONST.__objc_arraydata: 0x400
   __DATA_CONST.__objc_dictobj: 0x78
   __DATA_CONST.__objc_arrayobj: 0x360
-  __DATA.__objc_const: 0x22ff0
-  __DATA.__objc_selrefs: 0x9478
-  __DATA.__objc_ivar: 0x1a4c
+  __DATA.__objc_const: 0x23030
+  __DATA.__objc_selrefs: 0x9488
+  __DATA.__objc_ivar: 0x1a50
   __DATA.__objc_data: 0x5bb8
-  __DATA.__data: 0x30a8
+  __DATA.__data: 0x3098
   __DATA.__thread_vars: 0xc0
   __DATA.__thread_bss: 0x28
   __DATA.__bss: 0xe98

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 5DD0348D-0F65-38EC-8FE9-EC2A3760ED43
-  Functions: 9748
-  Symbols:   1859
-  CStrings:  19888
+  UUID: 1D45B65F-035D-3E98-993C-1224185A34F9
+  Functions: 9743
+  Symbols:   1858
+  CStrings:  19887
 
Symbols:
- _aks_unlock_bag
CStrings:
+ "-[CuttlefishXPCWrapper performPeerSecretsFixUpsWithSpecificUser:reply:]_block_invoke"
+ "/Library/Caches/com.apple.xbs/BFFB2279-F3E0-47A0-BD38-A44DAD2DFC5B/TemporaryDirectory.pT4o9R/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
+ "/Library/Caches/com.apple.xbs/BFFB2279-F3E0-47A0-BD38-A44DAD2DFC5B/TemporaryDirectory.pT4o9R/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
+ "Continuing despite fixup error: %@"
+ "Device is locked during fixup (errSecInteractionNotAllowed: %@), waiting for unlock"
+ "Device is locked during fixup, waiting for unlock"
+ "Successfully performed peer secrets accessibility fixup"
+ "Successfully persisted peer secrets accessibility fixup state"
+ "TB,N,V_peerSecretsAccessibilityFixUpPerformed"
+ "TPH reports having a different egoPeerID from Octagon"
+ "Trying to perform peer secrets accessibility fixup"
+ "_peerSecretsAccessibilityFixUpPerformed"
+ "com.apple.securityd.weekly"
+ "hasPeerSecretsAccessibilityFixUpPerformed"
+ "octagon, Failed to perform peer secrets accessibility fixup: %@"
+ "octagon, Failed to persist peer secrets accessibility fixup state: %@"
+ "octagon: Mismatch between TPH's egoPeerID (%@) and Octagon's self peerID (%@)"
+ "peerSecretsAccessibilityFixUpPerformed"
+ "performPeerSecretsFixUpsWithSpecificUser:reply:"
+ "setHasPeerSecretsAccessibilityFixUpPerformed:"
+ "setPeerSecretsAccessibilityFixUpPerformed:"
+ "{?=\"epoch\"b1\"escrowRepairAttemptVersion\"b1\"lastEscrowRepairAttempted\"b1\"lastEscrowRepairTriggered\"b1\"lastHealthCheckup\"b1\"attemptedJoin\"b1\"cdpState\"b1\"icloudAccountState\"b1\"sendingMetricsPermitted\"b1\"trustState\"b1\"isInheritedAccount\"b1\"peerSecretsAccessibilityFixUpPerformed\"b1\"warmedEscrowCache\"b1\"warnedTooManyPeers\"b1}"
- "/Library/Caches/com.apple.xbs/91704D56-10B0-4F78-9261-2D8182226F2A/TemporaryDirectory.Ypy3IC/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
- "/Library/Caches/com.apple.xbs/91704D56-10B0-4F78-9261-2D8182226F2A/TemporaryDirectory.Ypy3IC/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
- "aks_unlock_bag failed"
- "backup %@ not a dictionary"
- "com.apple.securityd.kcsharing.weekly"
- "enableWithError:"
- "enableWithSecureBackup:error:"
- "escrowSigningPublicKey"
- "failed to obtain manifest for keychain: %@"
- "keybag %@ not a data"
- "keychain_backup_syncable"
- "keychain_restore_syncable"
- "password %@ not a data"
- "password not a data"
- "restore %{private}@ failed %@"
- "restore %{private}@ not replacing existing item"
- "restore %{private}@ skipping corrupted item %@"
- "titc"
- "{?=\"epoch\"b1\"escrowRepairAttemptVersion\"b1\"lastEscrowRepairAttempted\"b1\"lastEscrowRepairTriggered\"b1\"lastHealthCheckup\"b1\"attemptedJoin\"b1\"cdpState\"b1\"icloudAccountState\"b1\"sendingMetricsPermitted\"b1\"trustState\"b1\"isInheritedAccount\"b1\"warmedEscrowCache\"b1\"warnedTooManyPeers\"b1}"

```
