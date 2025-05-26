## LocalAuthentication

> `/System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication`

```diff

-1394.40.33.0.0
-  __TEXT.__text: 0x2d110
+1394.62.1.0.0
+  __TEXT.__text: 0x2d124
   __TEXT.__auth_stubs: 0x890
-  __TEXT.__objc_methlist: 0x24cc
+  __TEXT.__objc_methlist: 0x24f4
   __TEXT.__const: 0xd0
   __TEXT.__gcc_except_tab: 0x7cc
-  __TEXT.__cstring: 0x1715
+  __TEXT.__cstring: 0x1731
   __TEXT.__dlopen_cstrs: 0x1cd
   __TEXT.__oslogstring: 0x2333
-  __TEXT.__unwind_info: 0xe90
+  __TEXT.__unwind_info: 0xe94
   __TEXT.__objc_classname: 0x79c
-  __TEXT.__objc_methname: 0x5633
-  __TEXT.__objc_methtype: 0x190e
+  __TEXT.__objc_methname: 0x5785
+  __TEXT.__objc_methtype: 0x1a0f
   __TEXT.__objc_stubs: 0x3ae0
-  __DATA_CONST.__got: 0x188
+  __DATA_CONST.__got: 0x180
   __DATA_CONST.__const: 0x18e0
   __DATA_CONST.__objc_classlist: 0x1f8
   __DATA_CONST.__objc_catlist: 0x0
   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x5a60
-  __DATA_CONST.__objc_selrefs: 0x1528
-  __AUTH_CONST.__cfstring: 0x15a0
+  __DATA_CONST.__objc_const: 0x5ae0
+  __DATA_CONST.__objc_selrefs: 0x1540
+  __AUTH_CONST.__cfstring: 0x15c0
   __AUTH_CONST.__objc_const: 0x1b0
   __AUTH_CONST.__objc_intobj: 0x1c8
-  __AUTH_CONST.__const: 0x20
+  __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__auth_got: 0x458
   __DATA.__objc_protorefs: 0x20
   __DATA.__objc_classrefs: 0x288

   __DATA.__objc_ivar: 0x22c
   __DATA.__data: 0x9c8
   __DATA.__bss: 0x178
-  __DATA_DIRTY.__const: 0x2a0
+  __DATA_DIRTY.__const: 0x280
   __DATA_DIRTY.__objc_const: 0x13f8
   __DATA_DIRTY.__objc_data: 0x13b0
   __DATA_DIRTY.__bss: 0xd0

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/LocalAuthentication.framework/Support/SharedUtils.framework/SharedUtils
   - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1167
-  Symbols:   4151
-  CStrings:  1717
+  Functions: 1170
+  Symbols:   4156
+  CStrings:  1730
 
Symbols:
+ +[LAStorage checkKey:supportsOperation:]
+ -[LAContext optionBiometryLockoutRecoveryRetries]
+ -[LAContext setOptionBiometryLockoutRecoveryRetries:]
+ GCC_except_table46
+ ___68-[LAStorage _callProxyBlock:authenticationPolicy:completionHandler:]_block_invoke.114
+ ___block_literal_global.213
- ___68-[LAStorage _callProxyBlock:authenticationPolicy:completionHandler:]_block_invoke.102
- ___block_literal_global.199
- _kLAServiceTypeSecureStorage
CStrings:
+ "B32@0:8q16q24"
+ "aclForKey:contextUUID:connection:completionHandler:"
+ "checkKey:supportsOperation:"
+ "kLAServiceTypeSecureStorage"
+ "objectForKey:contextUUID:connection:completionHandler:"
+ "optionBiometryLockoutRecoveryRetries"
+ "removeObjectForKey:contextUUID:connection:completionHandler:"
+ "setObject:acl:forKey:contextUUID:connection:completionHandler:"
+ "setOptionBiometryLockoutRecoveryRetries:"
+ "v48@0:8q16@\"NSUUID\"24@\"NSXPCConnection\"32@?<v@?@\"NSData\"@\"NSError\">40"
+ "v48@0:8q16@\"NSUUID\"24@\"NSXPCConnection\"32@?<v@?@@\"NSError\">40"
+ "v64@0:8@\"NSData\"16@\"NSData\"24q32@\"NSUUID\"40@\"NSXPCConnection\"48@?<v@?@@\"NSError\">56"
+ "v64@0:8@16@24q32@40@48@?56"

```
