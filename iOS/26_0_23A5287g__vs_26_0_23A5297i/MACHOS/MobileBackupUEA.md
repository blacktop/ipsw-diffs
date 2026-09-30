## MobileBackupUEA

> `/System/Library/UserEventPlugins/MobileBackupUEA.plugin/MobileBackupUEA`

```diff

-2899.0.2.0.0
-  __TEXT.__text: 0x9578
+2899.0.8.0.0
+  __TEXT.__text: 0x98ec
   __TEXT.__auth_stubs: 0x6b0
-  __TEXT.__objc_stubs: 0x13a0
-  __TEXT.__objc_methlist: 0x6b4
+  __TEXT.__objc_stubs: 0x13e0
+  __TEXT.__objc_methlist: 0x6bc
   __TEXT.__const: 0x160
-  __TEXT.__oslogstring: 0xeb4
-  __TEXT.__cstring: 0x1944
+  __TEXT.__oslogstring: 0xf4b
+  __TEXT.__cstring: 0x19db
   __TEXT.__objc_classname: 0x85
-  __TEXT.__objc_methname: 0x195d
+  __TEXT.__objc_methname: 0x19b2
   __TEXT.__objc_methtype: 0x587
-  __TEXT.__gcc_except_tab: 0x134
-  __TEXT.__unwind_info: 0x208
+  __TEXT.__gcc_except_tab: 0x150
+  __TEXT.__unwind_info: 0x218
   __DATA.__auth_got: 0x368
-  __DATA.__got: 0x118
-  __DATA.__const: 0x2f0
+  __DATA.__got: 0x120
+  __DATA.__const: 0x330
   __DATA.__cfstring: 0x7c0
   __DATA.__objc_classlist: 0x18
   __DATA.__objc_catlist: 0x8
   __DATA.__objc_protolist: 0x18
   __DATA.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x848
-  __DATA.__objc_selrefs: 0x718
+  __DATA.__objc_const: 0x868
+  __DATA.__objc_selrefs: 0x728
   __DATA.__objc_superrefs: 0x10
-  __DATA.__objc_ivar: 0x64
+  __DATA.__objc_ivar: 0x68
   __DATA.__objc_data: 0xf0
   __DATA.__data: 0x120
   __DATA.__objc_arraydata: 0x30

   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 23BF036A-5A58-3095-AEAD-A088EFBECEF2
-  Functions: 143
-  Symbols:   189
-  CStrings:  688
+  UUID: 12EEAE55-5A05-3AC7-8B74-EAAEE33EF3D3
+  Functions: 146
+  Symbols:   191
+  CStrings:  697
 
Symbols:
+ OBJC_IVAR_$_MBUEAPlugin._manualBackupStartedToken
+ _kMBManagerManualBackupStartedNotification
CStrings:
+ "Failed to boost manual backup: %@"
+ "Manual backup boost finished successfully"
+ "Received manual backup started notification (%{public}@), boosting backupd"
+ "_boostManualBackup"
+ "_manualBackupStartedToken"
+ "boostManualBackupWithCompletionHandler:"

```
