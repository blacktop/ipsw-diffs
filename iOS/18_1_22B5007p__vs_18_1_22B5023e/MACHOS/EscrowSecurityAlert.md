## EscrowSecurityAlert

> `/System/Library/CoreServices/EscrowSecurityAlert.app/EscrowSecurityAlert`

```diff

-638.0.5.0.0
-  __TEXT.__text: 0x7b70
-  __TEXT.__auth_stubs: 0x6b0
-  __TEXT.__objc_stubs: 0x17c0
-  __TEXT.__objc_methlist: 0x7b8
+638.40.5.0.0
+  __TEXT.__text: 0x7328
+  __TEXT.__auth_stubs: 0x690
+  __TEXT.__objc_stubs: 0x1720
+  __TEXT.__objc_methlist: 0x750
   __TEXT.__const: 0x98
   __TEXT.__cstring: 0xca3
-  __TEXT.__objc_methname: 0x1c13
-  __TEXT.__objc_classname: 0x12f
-  __TEXT.__objc_methtype: 0x339
-  __TEXT.__oslogstring: 0x5cd
+  __TEXT.__objc_methname: 0x1b14
+  __TEXT.__objc_classname: 0x11c
+  __TEXT.__objc_methtype: 0x2df
+  __TEXT.__oslogstring: 0x5d0
   __TEXT.__gcc_except_tab: 0x50
   __TEXT.__dlopen_cstrs: 0x5b
-  __TEXT.__unwind_info: 0x240
-  __DATA_CONST.__auth_got: 0x368
-  __DATA_CONST.__got: 0x238
+  __TEXT.__unwind_info: 0x220
+  __DATA_CONST.__auth_got: 0x358
+  __DATA_CONST.__got: 0x1f8
   __DATA_CONST.__const: 0x280
   __DATA_CONST.__cfstring: 0xde0
-  __DATA_CONST.__objc_classlist: 0x50
+  __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_intobj: 0x78
   __DATA_CONST.__objc_arraydata: 0x40
   __DATA_CONST.__objc_dictobj: 0xa0
-  __DATA.__objc_const: 0x1220
-  __DATA.__objc_selrefs: 0x780
+  __DATA.__objc_const: 0x1190
+  __DATA.__objc_selrefs: 0x730
   __DATA.__objc_ivar: 0x88
-  __DATA.__objc_data: 0x320
-  __DATA.__data: 0x188
+  __DATA.__objc_data: 0x2d0
+  __DATA.__data: 0x180
   __DATA.__bss: 0x80
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount
+  - /System/Library/PrivateFrameworks/AppleIDAuthSupport.framework/AppleIDAuthSupport
   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
   - /System/Library/PrivateFrameworks/CloudServices.framework/CloudServices
   - /System/Library/PrivateFrameworks/CoreCDP.framework/CoreCDP

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 188
-  Symbols:   192
-  CStrings:  596
+  Functions: 178
+  Symbols:   181
+  CStrings:  579
 
Symbols:
+ _CloudServicesInitializeLogging
+ _CloudServicesLog
+ _OBJC_CLASS_$_CloudServicesError
- _NSCocoaErrorDomain
- _NSFilePathErrorKey
- _NSLocalizedDescriptionKey
- _NSPOSIXErrorDomain
- _NSURLErrorDomain
- _NSURLErrorKey
- _NSUnderlyingErrorKey
- ___error
- __os_log_default
- _kCloudServicesErrorDomain
- _kEscrowServiceErrorDomain
- _objc_retain_x4
- _objc_retain_x5
- _strerror
CStrings:
+ "Error looking up authKitAccount: %!@(MISSING)"
+ "authKitAccountWithAltDSID:error:"
- "@32@0:8q16@24"
- "@40@0:8@16q24@32"
- "@40@0:8q16@24@32"
- "@48@0:8q16@24@32@40"
- "CloudServicesError"
- "No code for POSIX error: %!s(MISSING) (%!d(MISSING))"
- "authKitAccountWithAltDSID:"
- "codeForErrno:"
- "codeForNSError:"
- "dictionaryWithObjectsAndKeys:"
- "errorForNSError:path:format:"
- "errorWithCode:URL:format:"
- "errorWithCode:error:URL:format:"
- "errorWithCode:error:format:"
- "errorWithDomain:code:format:"
- "errorWithDomain:code:userInfo:"
- "initWithFormat:arguments:"
- "q24@0:8@16"
- "q24@0:8q16"

```
