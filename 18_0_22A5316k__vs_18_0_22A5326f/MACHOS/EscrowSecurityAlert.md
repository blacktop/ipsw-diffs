## EscrowSecurityAlert

> `/System/Library/CoreServices/EscrowSecurityAlert.app/EscrowSecurityAlert`

```diff

-638.0.5.0.0
-  __TEXT.__text: 0x7b70
+638.0.9.0.0
+  __TEXT.__text: 0x7c34
   __TEXT.__auth_stubs: 0x6b0
   __TEXT.__objc_stubs: 0x17c0
   __TEXT.__objc_methlist: 0x7b8
   __TEXT.__const: 0x98
   __TEXT.__cstring: 0xca3
-  __TEXT.__objc_methname: 0x1c13
+  __TEXT.__objc_methname: 0x1c19
   __TEXT.__objc_classname: 0x12f
   __TEXT.__objc_methtype: 0x339
-  __TEXT.__oslogstring: 0x5cd
+  __TEXT.__oslogstring: 0x5f1
   __TEXT.__gcc_except_tab: 0x50
   __TEXT.__dlopen_cstrs: 0x5b
   __TEXT.__unwind_info: 0x240

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
+  Functions: 189
   Symbols:   192
-  CStrings:  596
+  CStrings:  597
 
CStrings:
+ "Error looking up authKitAccount: %!@(MISSING)"
+ "authKitAccountWithAltDSID:error:"
- "authKitAccountWithAltDSID:"

```
