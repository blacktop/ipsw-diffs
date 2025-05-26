## com.apple.sbd

> `/System/Library/PrivateFrameworks/CloudServices.framework/Helpers/com.apple.sbd`

```diff

-608.0.0.0.0
-  __TEXT.__text: 0x66f20
-  __TEXT.__auth_stubs: 0x1340
-  __TEXT.__objc_stubs: 0x7500
-  __TEXT.__objc_methlist: 0x3524
+611.0.0.0.0
+  __TEXT.__text: 0x680cc
+  __TEXT.__auth_stubs: 0x1350
+  __TEXT.__objc_stubs: 0x7560
+  __TEXT.__objc_methlist: 0x354c
   __TEXT.__const: 0xc50
-  __TEXT.__gcc_except_tab: 0x1bbc
-  __TEXT.__cstring: 0x5119
-  __TEXT.__objc_methname: 0x878d
+  __TEXT.__gcc_except_tab: 0x1c14
+  __TEXT.__cstring: 0x5153
+  __TEXT.__objc_methname: 0x87fb
   __TEXT.__objc_classname: 0x79a
   __TEXT.__objc_methtype: 0x11c9
-  __TEXT.__oslogstring: 0x9b8b
-  __TEXT.__unwind_info: 0x1168
-  __DATA_CONST.__auth_got: 0x9b0
+  __TEXT.__oslogstring: 0x9dd4
+  __TEXT.__unwind_info: 0x11a0
+  __DATA_CONST.__auth_got: 0x9b8
   __DATA_CONST.__got: 0x228
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x1b60
-  __DATA_CONST.__cfstring: 0x4ae0
+  __DATA_CONST.__const: 0x1b88
+  __DATA_CONST.__cfstring: 0x4b00
   __DATA_CONST.__objc_classlist: 0x1f0
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x78

   __DATA_CONST.__objc_arraydata: 0x1d0
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x78
-  __DATA.__objc_const: 0x6df0
-  __DATA.__objc_selrefs: 0x2150
+  __DATA.__objc_const: 0x6e10
+  __DATA.__objc_selrefs: 0x2170
   __DATA.__objc_protorefs: 0x10
   __DATA.__objc_classrefs: 0x358
   __DATA.__objc_superrefs: 0x160

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 1973
-  Symbols:   445
-  CStrings:  3415
+  Functions: 1988
+  Symbols:   446
+  CStrings:  3433
 
Symbols:
+ _SOSBSKBRemoveRecoveryKey
CStrings:
+ "-[SecureBackup removeRecoveryKeyFromBackup:]"
+ "PCSMasterKey"
+ "Recovery Key fails to verify against iCloudIdentity and PCSMasterKey keybags"
+ "about to remove recovery key from backup view %@"
+ "calling removeRecoveryKeyFromBackup in daemon"
+ "failed to create backupslicekeybag: %@"
+ "failed to encode backupslicekeybag: %@"
+ "failed to remove recovery from PCS MK bskb: %@"
+ "failed to remove recovery from iCloudIdentity bskb: %@"
+ "recovery key removed from iCloudIdentity and PCS keybags"
+ "recovery key verified against %@ keybag"
+ "recovery key verified against iCloudIdentity and PCSMasterKey keybags"
+ "removeRKFromKeyBag:error:"
+ "removeRecoveryKey:"
+ "removeRecoveryKeyFromBackup came back with %@"
+ "removeRecoveryKeyFromBackup:"
+ "removeRecoveryKeyFromBackup: invoked"
+ "removeRecoveryKeyFromBackup: remote proxy error: %ld"
+ "removeRecoveryKeyFromBackupInDaemon:"
+ "removed recovery key from bskb"
- "failed to creatae backupslicekeybag: %@"
- "recovery key verified against iCloudIdentity and PCS keybags"

```
