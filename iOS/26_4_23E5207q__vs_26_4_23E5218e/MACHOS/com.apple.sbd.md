## com.apple.sbd

> `/System/Library/PrivateFrameworks/CloudServices.framework/Helpers/com.apple.sbd`

```diff

-694.100.32.0.0
-  __TEXT.__text: 0x52064
-  __TEXT.__auth_stubs: 0xf90
-  __TEXT.__objc_stubs: 0x6f00
-  __TEXT.__objc_methlist: 0x2f6c
+694.100.36.0.0
+  __TEXT.__text: 0x528b4
+  __TEXT.__auth_stubs: 0xfb0
+  __TEXT.__objc_stubs: 0x6f60
+  __TEXT.__objc_methlist: 0x2f98
   __TEXT.__const: 0x150
-  __TEXT.__gcc_except_tab: 0x1c6c
-  __TEXT.__cstring: 0x4199
-  __TEXT.__objc_methname: 0x78be
-  __TEXT.__oslogstring: 0x8056
+  __TEXT.__gcc_except_tab: 0x1d04
+  __TEXT.__cstring: 0x4208
+  __TEXT.__objc_methname: 0x7952
+  __TEXT.__oslogstring: 0x810d
   __TEXT.__objc_classname: 0x74c
-  __TEXT.__objc_methtype: 0x10e2
-  __TEXT.__unwind_info: 0xe28
-  __DATA_CONST.__auth_got: 0x7d8
+  __TEXT.__objc_methtype: 0x1128
+  __TEXT.__unwind_info: 0xe38
+  __DATA_CONST.__auth_got: 0x7e8
   __DATA_CONST.__got: 0x780
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x14c0
-  __DATA_CONST.__cfstring: 0x3ba0
+  __DATA_CONST.__const: 0x14e8
+  __DATA_CONST.__cfstring: 0x3be0
   __DATA_CONST.__objc_classlist: 0x1c0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x78

   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_intobj: 0xf0
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x5248
-  __DATA.__objc_selrefs: 0x1fb0
+  __DATA.__objc_const: 0x5250
+  __DATA.__objc_selrefs: 0x1fd0
   __DATA.__objc_ivar: 0x2c0
   __DATA.__objc_data: 0x1180
   __DATA.__data: 0x5a8

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 11A2008C-D7E2-3940-8902-62C8CA719953
-  Functions: 1397
-  Symbols:   502
-  CStrings:  3403
+  UUID: 598D0D1E-0B25-38F6-99CE-455C0BA981DD
+  Functions: 1403
+  Symbols:   504
+  CStrings:  3417
 
Symbols:
+ _SecCertificateCopyData
+ _SecCertificateCopyKey
CStrings:
+ "-[SecureBackupDaemon wrapDataToFedKeyWithRequest:reply:]"
+ "@32@0:8@16B24B28"
+ "DBR-TerminalRecord"
+ "Failed to create blob: %@"
+ "Failed to find LRC fed certificate"
+ "Failed to find the LRC fed certificate"
+ "Modifying record label %@ (due to com.apple.cloudservices/DBR-TerminalRecord)"
+ "attempted to store stingray identities, with invalid parameters: %@, %@nil iCloud password, %@nil auth token, %@nil iCloud identity data, serializedRecord: %@"
+ "createDataWrappedToFedKeyWithRequest:error:"
+ "dbrTerminalRecord"
+ "fedCertificate:altDSID:inEnvironment:"
+ "initFromResponse:filterPCS:dbrTerminal:"
+ "v32@0:8@\"SecureBackup\"16@?<v@?@\"NSData\"@\"NSError\">24"
+ "wrapDataToFedKeyWithRequest:reply:"
- "initFromResponseFilterPCS:"

```
