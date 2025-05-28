## com.apple.sbd

> `/System/Library/PrivateFrameworks/CloudServices.framework/Helpers/com.apple.sbd`

```diff

-611.60.5.0.0
-  __TEXT.__text: 0x68120
+626.100.1.0.0
+  __TEXT.__text: 0x673dc
   __TEXT.__auth_stubs: 0x1350
-  __TEXT.__objc_stubs: 0x7560
-  __TEXT.__objc_methlist: 0x354c
+  __TEXT.__objc_stubs: 0x7660
+  __TEXT.__objc_methlist: 0x35dc
   __TEXT.__const: 0xc50
-  __TEXT.__gcc_except_tab: 0x1c14
-  __TEXT.__cstring: 0x5153
-  __TEXT.__objc_methname: 0x87fb
-  __TEXT.__objc_classname: 0x79a
-  __TEXT.__objc_methtype: 0x11c9
-  __TEXT.__oslogstring: 0x9dd4
-  __TEXT.__unwind_info: 0x11a0
+  __TEXT.__gcc_except_tab: 0x1a8c
+  __TEXT.__cstring: 0x526c
+  __TEXT.__objc_methname: 0x894f
+  __TEXT.__objc_classname: 0x7b6
+  __TEXT.__objc_methtype: 0x11f5
+  __TEXT.__oslogstring: 0x9bab
+  __TEXT.__unwind_info: 0x118c
   __DATA_CONST.__auth_got: 0x9b8
   __DATA_CONST.__got: 0x228
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x1b88
-  __DATA_CONST.__cfstring: 0x4b00
-  __DATA_CONST.__objc_classlist: 0x1f0
+  __DATA_CONST.__const: 0x1c48
+  __DATA_CONST.__cfstring: 0x4a40
+  __DATA_CONST.__objc_classlist: 0x1f8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_classrefs: 0x360
+  __DATA_CONST.__objc_superrefs: 0x160
   __DATA_CONST.__objc_intobj: 0xd8
   __DATA_CONST.__objc_arraydata: 0x1d0
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x78
-  __DATA.__objc_const: 0x6e10
-  __DATA.__objc_selrefs: 0x2170
-  __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x358
-  __DATA.__objc_superrefs: 0x160
-  __DATA.__objc_ivar: 0x3c8
-  __DATA.__objc_data: 0x1360
+  __DATA.__objc_const: 0x6fa0
+  __DATA.__objc_selrefs: 0x21c0
+  __DATA.__objc_ivar: 0x3dc
+  __DATA.__objc_data: 0x13b0
   __DATA.__data: 0x5b0
   __DATA.__bss: 0x150
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 1988
+  Functions: 1987
   Symbols:   446
-  CStrings:  3433
+  CStrings:  3449
 
Symbols:
+ _calloc
- _SecRKCreateRecoveryKey
CStrings:
+ "@\"EscrowService\""
+ "@\"NSMutableArray\""
+ "@?16@0:8"
+ "Failed to invalidate escrow cache: %@"
+ "SecureBackupDeletionContext"
+ "T@\"EscrowService\",&,V_escrowService"
+ "T@\"NSError\",&,V_deleteError"
+ "T@\"NSMutableArray\",&,V_recordIDs"
+ "T@\"NSString\",?,R,C"
+ "T@\"SecureBackup\",&,V_request"
+ "T@?,C,V_completionBlock"
+ "_completionBlock"
+ "_deleteAlliCDPRecordsWithContext:"
+ "_deleteError"
+ "_escrowService"
+ "_recordIDs"
+ "_request"
+ "completionBlock"
+ "deleteError"
+ "escrowService"
+ "objectAtIndex:"
+ "recordIDs"
+ "removeObjectAtIndex:"
+ "request"
+ "setCompletionBlock:"
+ "setDeleteError:"
+ "setEscrowService:"
+ "setRecordIDs:"
+ "setRequest:"
+ "v24@?0@\"EscrowAccountInfoResponse\"8@\"NSError\"16"
+ "v24@?0@\"EscrowCertificateResponse\"8@\"NSError\"16"
+ "v24@?0@\"EscrowChangeSMSTargetResponse\"8@\"NSError\"16"
+ "v24@?0@\"EscrowDeleteResponse\"8@\"NSError\"16"
+ "v24@?0@\"EscrowEnrollmentResponse\"8@\"NSError\"16"
+ "v24@?0@\"EscrowGetCountrySMSCodesResponse\"8@\"NSError\"16"
+ "v24@?0@\"EscrowListSMSTargetsResponse\"8@\"NSError\"16"
+ "v24@?0@\"EscrowLogRecoveryResponse\"8@\"NSError\"16"
+ "v24@?0@\"EscrowRecoveryResponse\"8@\"NSError\"16"
+ "v24@?0@\"EscrowSMSChallengeResponse\"8@\"NSError\"16"
+ "v24@?0@\"EscrowSRPResponse\"8@\"NSError\"16"
+ "v24@?0@\"EscrowUpdateMetadataResponse\"8@\"NSError\"16"
- "Can't get escrow cert from keychain"
- "E_backupKeychainView: scrow no longer trusted"
- "Escrow cert is newer than trust policy; ignoring for now."
- "Escrow cert no longer trusted"
- "Escrow no longer trusted"
- "Failed to recovery with recovery key"
- "Performing recovery key recovery"
- "SecureBackupEscrowTrustStatus"
- "_backupCloudIdentityKeychainViewAndPushToKVS: Escrow cert is newer than trust policy; ignoring for now."
- "_checkEscrowTrust"
- "check escrow trust"
- "com.apple.EscrowSecurityAlert.server"
- "enableWithRequest contains a recoveryKey"
- "invalid/malformed recovery key"
- "recoverWithRecoveryKey failed. Result of call: %{BOOL}d, error: %@"
- "recoverWithRecoveryKey succeeded!"
- "recoverWithRecoveryKey:recoveryKey:error:"
- "setNewRecoveryKeyWithData() failed: %@"
- "setNewRecoveryKeyWithData() succeeded!"
- "setNewRecoveryKeyWithData() timed out"
- "setNewRecoveryKeyWithData:recoveryKey:reply:"
- "v24@?0@\"LakituResponse\"8@\"NSError\"16"
- "v24@?0@\"SecRecoveryKey\"8@\"NSError\"16"

```
