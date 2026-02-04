## com.apple.sbd

> `/System/Library/PrivateFrameworks/CloudServices.framework/Helpers/com.apple.sbd`

```diff

 694.80.7.0.0
-  __TEXT.__text: 0x4d858
-  __TEXT.__auth_stubs: 0xff0
-  __TEXT.__objc_stubs: 0x6a60
-  __TEXT.__objc_methlist: 0x2d94
+  __TEXT.__text: 0x4f538
+  __TEXT.__auth_stubs: 0x1000
+  __TEXT.__objc_stubs: 0x6d20
+  __TEXT.__objc_methlist: 0x2edc
   __TEXT.__const: 0x150
-  __TEXT.__gcc_except_tab: 0x1c88
-  __TEXT.__cstring: 0x3f78
-  __TEXT.__objc_methname: 0x74d6
-  __TEXT.__oslogstring: 0x7c7e
+  __TEXT.__gcc_except_tab: 0x1c90
+  __TEXT.__cstring: 0x417f
+  __TEXT.__objc_methname: 0x772a
+  __TEXT.__oslogstring: 0x7fac
   __TEXT.__objc_classname: 0x74c
-  __TEXT.__objc_methtype: 0x10a6
-  __TEXT.__unwind_info: 0xc70
-  __DATA_CONST.__auth_got: 0x808
-  __DATA_CONST.__got: 0x6a0
+  __TEXT.__objc_methtype: 0x10e2
+  __TEXT.__unwind_info: 0xcb8
+  __DATA_CONST.__auth_got: 0x810
+  __DATA_CONST.__got: 0x6e0
   __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__const: 0x14b8
-  __DATA_CONST.__cfstring: 0x3a20
+  __DATA_CONST.__cfstring: 0x3b80
   __DATA_CONST.__objc_classlist: 0x1c0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x130
+  __DATA_CONST.__objc_superrefs: 0x138
   __DATA_CONST.__objc_arraydata: 0x1a0
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_intobj: 0xf0
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x5090
-  __DATA.__objc_selrefs: 0x1e88
-  __DATA.__objc_ivar: 0x2a4
+  __DATA.__objc_const: 0x5188
+  __DATA.__objc_selrefs: 0x1f38
+  __DATA.__objc_ivar: 0x2b0
   __DATA.__objc_data: 0x1180
   __DATA.__data: 0x5a8
   __DATA.__bss: 0x130

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: DE53E489-B560-33BD-AD3C-76C266ADF42D
-  Functions: 1334
-  Symbols:   480
-  CStrings:  3304
+  UUID: D2FC9106-2AC0-32A1-A658-AC5E7B64FD5A
+  Functions: 1366
+  Symbols:   489
+  CStrings:  3374
 
Symbols:
+ _OBJC_CLASS_$_AppleIDPasswordMetadata
+ _OBJC_CLASS_$_CSFDERecord
+ _OBJC_CLASS_$_NSUserDefaults
+ _SecureBackupIsDBREnabled
+ _kEscrowServiceDBRFDELabel
+ _kEscrowServiceDBRLabel
+ _kSecureBackupContainsFDEiCloudIdentityKey
+ _kSecureBackupFDEMetadataHashKey
+ _kSecureBackupFDEMetadataKey
CStrings:
+ "%s: DBR flag set -- looking for %@"
+ "%s: getting account info with DBR fde flag set"
+ "-[SecureBackupDaemon _getAccountInfoWithRequest:reply:]_block_invoke"
+ "-[SecureBackupDaemon recoverFDERecordWithRequest:reply:]"
+ "=== FDE Identity Escrow record ===\nTime of escrow: %@\nEscrow version: %@\nKeybag SHA256: %@\nProtectedData: %@"
+ "@\"AppleIDPasswordMetadata\""
+ "@\"AppleIDPasswordMetadata\"16@0:8"
+ "DBR-RecoveryFail"
+ "Disallowing %@ operation for label %@ (due to com.apple.cloudservices/DBR-RecoveryFail)"
+ "Disallowing %@ operation for label %@ (due to com.apple.cloudservices/PCS-NoRecord)"
+ "Disallowing %@ operation for label %@ (due to com.apple.cloudservices/PCS-UpdateDisabled)"
+ "FDE identity recovery returned: %@"
+ "FDE record data is incomplete, returning"
+ "FDE record data version does not match version in escrow"
+ "FDE record in full (recover path) :%@"
+ "Filtering PCS record label %@ (due to com.apple.cloudservices/PCS-NoRecord)"
+ "PCS-NoRecord"
+ "PCS-UpdateDisabled"
+ "Performing FDE Record recovery"
+ "T@\"AppleIDPasswordMetadata\",R,N"
+ "T@\"AppleIDPasswordMetadata\",R,N,V_appleIDPasswordMetadata"
+ "TB,R,N,V_dbr"
+ "TB,R,N,V_dbrFDE"
+ "_appleIDPasswordMetadata"
+ "_checkFetchOperationWithHandler:"
+ "_checkReadOperationWithHandler:"
+ "_checkUpdateOperationWithHandler:"
+ "_dbr"
+ "_dbrFDE"
+ "appleIDPasswordMetadata"
+ "artificial error injected (com.apple.cloudservices/DBR-RecoveryFail)"
+ "artificial error injected (com.apple.cloudservices/PCS-NoRecord)"
+ "artificial error injected (com.apple.cloudservices/PCS-UpdateDisabled)"
+ "com.apple.cloudservices"
+ "dbr"
+ "dbrFDE"
+ "dbrRecoveryFail"
+ "error parsing DBR record: %@"
+ "error parsing FDE record: %@"
+ "initFromResponseFilterPCS:"
+ "initWithProto:salt:iterations:"
+ "initWithSuiteName:"
+ "isDbrRecord"
+ "isPcsRecord"
+ "iterations"
+ "pcsNoRecord"
+ "pcsUpdateDisabled"
+ "proto"
+ "rawPassword not provided"
+ "recoverFDERecordWithRequest:reply:"
+ "salt"
+ "setAppleIDPasswordMetadata:"
+ "setDbrRecord:"
+ "setFdeRecord:"
+ "setPasswordMetadataWithRequest:response:ses:"

```
