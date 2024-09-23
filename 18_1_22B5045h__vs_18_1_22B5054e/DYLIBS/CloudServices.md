## CloudServices

> `/System/Library/PrivateFrameworks/CloudServices.framework/CloudServices`

```diff

-638.40.20.502.1
-  __TEXT.__text: 0x2465c
-  __TEXT.__auth_stubs: 0xa10
-  __TEXT.__objc_methlist: 0x19ac
+638.40.26.0.0
+  __TEXT.__text: 0x2480c
+  __TEXT.__auth_stubs: 0xa20
+  __TEXT.__objc_methlist: 0x19fc
   __TEXT.__const: 0xc90
-  __TEXT.__cstring: 0x1f27
-  __TEXT.__gcc_except_tab: 0x59c
-  __TEXT.__oslogstring: 0x1fa4
+  __TEXT.__cstring: 0x1f70
+  __TEXT.__gcc_except_tab: 0x5a8
+  __TEXT.__oslogstring: 0x1fc2
   __TEXT.__unwind_info: 0x810
   __TEXT.__objc_classname: 0x27e
-  __TEXT.__objc_methname: 0x42c1
+  __TEXT.__objc_methname: 0x43a6
   __TEXT.__objc_methtype: 0xc8b
-  __TEXT.__objc_stubs: 0x2de0
+  __TEXT.__objc_stubs: 0x2ea0
   __DATA_CONST.__got: 0x250
-  __DATA_CONST.__const: 0xa10
+  __DATA_CONST.__const: 0xa20
   __DATA_CONST.__objc_classlist: 0x90
+  __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x10d0
+  __DATA_CONST.__objc_selrefs: 0x1108
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x78
   __DATA_CONST.__objc_arraydata: 0x30
-  __AUTH_CONST.__auth_got: 0x518
+  __AUTH_CONST.__auth_got: 0x520
   __AUTH_CONST.__auth_ptr: 0x10
   __AUTH_CONST.__const: 0xc0
-  __AUTH_CONST.__cfstring: 0x1fe0
-  __AUTH_CONST.__objc_const: 0x2f10
+  __AUTH_CONST.__cfstring: 0x2020
+  __AUTH_CONST.__objc_const: 0x2fc0
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x48
-  __AUTH.__objc_data: 0x320
-  __DATA.__objc_ivar: 0x1e0
-  __DATA.__data: 0x2a8
+  __AUTH.__objc_data: 0x230
+  __DATA.__objc_ivar: 0x1e8
+  __DATA.__data: 0x2a0
   __DATA.__bss: 0x30
-  __DATA_DIRTY.__objc_data: 0x280
+  __DATA_DIRTY.__objc_data: 0x370
+  __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__bss: 0x40
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 864
-  Symbols:   435
-  CStrings:  1439
+  Functions: 872
+  Symbols:   438
+  CStrings:  1452
 
Symbols:
+ _kSecureBackupAuthenticationRawPassword
+ _kSecureBackupKeybagSHA256Key
+ __os_log_fault_impl
CStrings:
+ "hasBackupKeybagSHA256"
+ "iCloudPassword must be a PET, not a raw password"
+ "SecureBackupAuthenticationRawPassword"
+ "_backupKeybagSHA256"
+ "rawPassword"
+ "PET"
+ "T@\"NSData\",&,N,V_backupKeybagSHA256"
+ "hasSuffix:"
+ "setBackupKeybagSHA256:"
+ "_rawPassword"
+ "backupKeybagSHA256"
+ "isPasswordEquivalentToken"
+ "fail to decode plist"
+ "setRawPassword:"
+ "T@\"NSString\",C,N,V_rawPassword"
+ "BackupKeybagSHA256"
+ "rawPassword must not be a PET"
+ "?\x0f\t"
- "BackupVersion"
- "?\x0f\b"
- "Trying fallback: %!@(MISSING)"
- "Error deserializing data: %!@(MISSING)"
- "dummy-label"
- "1"

```
