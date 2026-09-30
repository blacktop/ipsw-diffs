## Accounts

> `/System/Library/Frameworks/Accounts.framework/Accounts`

```diff

-1035.0.0.0.0
-  __TEXT.__text: 0x5edfc
+1036.0.0.0.0
+  __TEXT.__text: 0x5ee34
   __TEXT.__auth_stubs: 0xc60
   __TEXT.__objc_methlist: 0x42ec
   __TEXT.__const: 0xc8
   __TEXT.__gcc_except_tab: 0x3f18
-  __TEXT.__cstring: 0x3d20
+  __TEXT.__cstring: 0x3d35
   __TEXT.__oslogstring: 0x52c8
   __TEXT.__unwind_info: 0x1c88
   __TEXT.__objc_classname: 0x599

   __TEXT.__objc_methtype: 0x1523
   __TEXT.__objc_stubs: 0x65a0
   __DATA_CONST.__got: 0x340
-  __DATA_CONST.__const: 0x2518
+  __DATA_CONST.__const: 0x2520
   __DATA_CONST.__objc_classlist: 0x1a8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x60

   __DATA_CONST.__objc_arraydata: 0x38
   __AUTH_CONST.__auth_got: 0x640
   __AUTH_CONST.__const: 0x4a0
-  __AUTH_CONST.__cfstring: 0x48e0
+  __AUTH_CONST.__cfstring: 0x4900
   __AUTH_CONST.__objc_const: 0x5e40
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_intobj: 0x558

   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 74DE4E34-5065-3D30-AB0C-458618867C9F
+  UUID: 69E7C140-AC03-37EF-A55B-4A77A7C8CD25
   Functions: 1976
-  Symbols:   6847
-  CStrings:  3439
+  Symbols:   6848
+  CStrings:  3441
 
Symbols:
+ _ACCloudKitVideoTokenKey
Functions:
~ +[ACAccountCredential supportedKeysForAccountTypeIdentifier:credentialType:] : 1808 -> 1852
~ ___39+[ACAccountCredential allSupportedKeys]_block_invoke : 528 -> 540
CStrings:
+ "cloudkit-video-token"

```
