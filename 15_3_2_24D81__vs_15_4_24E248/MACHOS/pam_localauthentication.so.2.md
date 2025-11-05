## pam_localauthentication.so.2

> `/usr/lib/pam/pam_localauthentication.so.2`

```diff

 213.0.0.0.0
-  __TEXT.__text: 0x241c
+  __TEXT.__text: 0x23f8
   __TEXT.__auth_stubs: 0x2d0
   __TEXT.__objc_stubs: 0x320
+  __TEXT.__objc_methlist: 0x194
   __TEXT.__cstring: 0x359
   __TEXT.__const: 0x50
   __TEXT.__gcc_except_tab: 0xc0
   __TEXT.__oslogstring: 0xee
   __TEXT.__objc_classname: 0x16
   __TEXT.__objc_methname: 0x58b
-  __TEXT.__objc_methtype: 0x3d5
+  __TEXT.__objc_methtype: 0x3d8
   __TEXT.__dlopen_cstrs: 0x5d
   __TEXT.__unwind_info: 0x128
   __DATA_CONST.__auth_got: 0x178

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x458
-  __DATA.__objc_selrefs: 0xc8
+  __DATA.__objc_const: 0x158
+  __DATA.__objc_selrefs: 0x1b0
   __DATA.__data: 0xc0
   __DATA.__bss: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpam.2.dylib
-  UUID: 126AA5DB-CEDB-351A-AA6B-A973F99845E6
-  Functions: 53
-  Symbols:   173
+  UUID: 1B141342-3A73-35B8-8CFF-9AF811A691D0
+  Functions: 54
+  Symbols:   174
   CStrings:  146
 
Symbols:
+ LA_LOG_coreauthd_client.cold.1
Functions:
~ ___LAUpdateAccessControl_block_invoke : 480 -> 472
~ _LA_LOG_coreauthd_client : 84 -> 68
~ _LASetCredential : 132 -> 128
~ _LAIsCredentialSet : 116 -> 112
~ _getLAContextClass : 228 -> 224
~ _getLAClientClass : 228 -> 224
~ _LABootstrapSEP : 488 -> 480
~ _LAVerifySEP : 724 -> 716
+ LA_LOG_coreauthd_client.cold.1
CStrings:
+ "v24@0:8@?<v@?@\"<LACAgentProxyXPC>\"@\"NSError\">16"
+ "v48@0:8@\"NSData\"16@\"<LACContextCallbackXPC>\"24Q32@?<v@?@\"<LAContextXPC>\"@\"NSUUID\"@\"NSString\"@\"NSError\">40"
+ "v64@0:8@\"NSUUID\"16@\"<LACContextCallbackXPC>\"24Q32@\"NSData\"40@\"NSData\"48@?<v@?@\"<LAContextXPC>\"@\"NSString\"@\"NSError\">56"
- "v24@0:8@?<v@?@\"<LAAgentProxyXPC>\"@\"NSError\">16"
- "v48@0:8@\"NSData\"16@\"<LAContextCallbackXPC>\"24Q32@?<v@?@\"<LAContextXPC>\"@\"NSUUID\"@\"NSString\"@\"NSError\">40"
- "v64@0:8@\"NSUUID\"16@\"<LAContextCallbackXPC>\"24Q32@\"NSData\"40@\"NSData\"48@?<v@?@\"<LAContextXPC>\"@\"NSString\"@\"NSError\">56"

```
