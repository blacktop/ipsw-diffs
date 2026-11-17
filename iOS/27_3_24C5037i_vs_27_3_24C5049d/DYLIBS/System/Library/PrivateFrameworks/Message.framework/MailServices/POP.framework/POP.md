## POP

> `/System/Library/PrivateFrameworks/Message.framework/MailServices/POP.framework/POP`

```diff

-3901.300.26.0.0
-  __TEXT.__text: 0x89a4
-  __TEXT.__objc_methlist: 0x76c
-  __TEXT.__gcc_except_tab: 0x13dc
-  __TEXT.__cstring: 0x3fa
-  __TEXT.__ustring: 0x2fc
+3901.300.60.0.0
+  __TEXT.__text: 0x8378
+  __TEXT.__objc_methlist: 0x718
+  __TEXT.__gcc_except_tab: 0x12dc
+  __TEXT.__cstring: 0x3e0
   __TEXT.__const: 0xa8
-  __TEXT.__oslogstring: 0x27f
-  __TEXT.__unwind_info: 0x4a8
+  __TEXT.__oslogstring: 0x227
+  __TEXT.__ustring: 0x22c
+  __TEXT.__unwind_info: 0x478
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xe8
-  __DATA_CONST.__objc_classlist: 0x40
+  __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa88
-  __DATA_CONST.__objc_superrefs: 0x30
+  __DATA_CONST.__objc_selrefs: 0xa50
+  __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_arraydata: 0x8
-  __DATA_CONST.__got: 0x1c0
+  __DATA_CONST.__got: 0x1b8
   __AUTH_CONST.__const: 0x20
-  __AUTH_CONST.__cfstring: 0x5c0
-  __AUTH_CONST.__objc_const: 0x920
+  __AUTH_CONST.__cfstring: 0x580
+  __AUTH_CONST.__objc_const: 0x870
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x280
-  __DATA.__objc_ivar: 0x88
+  __AUTH.__objc_data: 0x230
+  __DATA.__objc_ivar: 0x84
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight

   - /System/Library/PrivateFrameworks/MessageSupport.framework/MessageSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 157
-  Symbols:   451
-  CStrings:  79
+  Functions: 151
+  Symbols:   437
+  CStrings:  76
 
Symbols:
+ GCC_except_table27
+ GCC_except_table29
+ GCC_except_table46
- -[MFAPOPAuthScheme canAuthenticateAccountClass:connection:]
- -[MFAPOPAuthScheme connectionClassForAccountClass:]
- -[MFAPOPConnection authenticateUsingAccount:]
- -[POPAccount setPreferredAuthScheme:]
- -[POPAccount setShouldAttemptAPOP:]
- -[POPAccount shouldAttemptAPOP]
- GCC_except_table30
- GCC_except_table43
- GCC_except_table45
- GCC_except_table49
- GCC_except_table50
- _OBJC_CLASS_$_MFAPOPConnection
- _OBJC_IVAR_$_POPAccount._shouldAttemptAPOP
- _OBJC_METACLASS_$_MFAPOPConnection
- __OBJC_$_INSTANCE_METHODS_MFAPOPConnection
- __OBJC_CLASS_RO_$_MFAPOPConnection
- __OBJC_METACLASS_RO_$_MFAPOPConnection
CStrings:
- "<Account:%{public}@> Login Successful. Setting AuthScheme to ECAuthenticationSchemeAPOP"
- "AUTH_NOT_SUPPORTED_FORMAT"
- "The %@ server “%@” doesn’t support %@ authentication. Please check your account settings and try again."
```
