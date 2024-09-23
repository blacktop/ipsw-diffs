## pcsstatus

> `/usr/libexec/pcsstatus`

```diff

-1037.40.12.0.0
-  __TEXT.__text: 0xd8d0
-  __TEXT.__auth_stubs: 0x9a0
-  __TEXT.__objc_stubs: 0x1bc0
+1037.40.65.0.0
+  __TEXT.__text: 0xdc90
+  __TEXT.__auth_stubs: 0x9b0
+  __TEXT.__objc_stubs: 0x1c60
   __TEXT.__objc_methlist: 0x628
   __TEXT.__const: 0x98
-  __TEXT.__objc_methname: 0x1dee
-  __TEXT.__cstring: 0xd3c
+  __TEXT.__objc_methname: 0x1e50
+  __TEXT.__cstring: 0xda0
   __TEXT.__objc_classname: 0x76
   __TEXT.__objc_methtype: 0x5df
-  __TEXT.__gcc_except_tab: 0xb68
+  __TEXT.__gcc_except_tab: 0xb88
   __TEXT.__oslogstring: 0xdb0
-  __TEXT.__unwind_info: 0x398
-  __DATA_CONST.__auth_got: 0x4e0
-  __DATA_CONST.__got: 0x290
-  __DATA_CONST.__const: 0x6f8
-  __DATA_CONST.__cfstring: 0x1100
+  __TEXT.__unwind_info: 0x3b0
+  __DATA_CONST.__auth_got: 0x4e8
+  __DATA_CONST.__got: 0x2b8
+  __DATA_CONST.__const: 0x720
+  __DATA_CONST.__cfstring: 0x1160
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA.__objc_const: 0xcf8
-  __DATA.__objc_selrefs: 0x878
+  __DATA.__objc_selrefs: 0x8a0
   __DATA.__objc_ivar: 0x78
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x228

   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount
   - /System/Library/PrivateFrameworks/ApplePushService.framework/ApplePushService
+  - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
+  - /System/Library/PrivateFrameworks/CloudServices.framework/CloudServices
   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
   - /System/Library/PrivateFrameworks/ProtectedCloudStorage.framework/ProtectedCloudStorage
   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 223
-  Symbols:   247
-  CStrings:  706
+  Functions: 227
+  Symbols:   253
+  CStrings:  714
 
Symbols:
+ _exit
+ _fputc
+ _AKAuthenticationUsernameKey
+ _AKAuthenticationPasswordKey
+ _OBJC_CLASS_$_AKAppleIDAuthenticationController
+ _AKAuthenticationDSIDKey
+ _OBJC_CLASS_$_AKAppleIDAuthenticationContext
+ _kSecureBackupStingrayMetadataKey
- _printf
- _kPCSSecureBackupCFStingrayMetadataKey
CStrings:
+ "authentication error: username mismatch"
+ "setAuthenticationType:"
+ "setIsUsernameEditable:"
+ "Must provide either an AppleID to fetch a PET"
+ "setUsername:"
+ "authentication error: %!@(MISSING)"
+ "authentication error: dsid mismatch"
+ "authenticateWithContext:completion:"
+ "stringValue"
+ "_setPassword:"
- "initWithData:encoding:"
- "CFDictionaryCreateMutableForCFTypesWith failed"

```
