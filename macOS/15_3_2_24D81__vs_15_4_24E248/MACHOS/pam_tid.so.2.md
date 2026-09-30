## pam_tid.so.2

> `/usr/lib/pam/pam_tid.so.2`

```diff

 213.0.0.0.0
-  __TEXT.__text: 0x24d0
+  __TEXT.__text: 0x24a8
   __TEXT.__auth_stubs: 0x310
   __TEXT.__objc_stubs: 0x320
+  __TEXT.__objc_methlist: 0x194
   __TEXT.__cstring: 0x36c
   __TEXT.__const: 0x50
   __TEXT.__gcc_except_tab: 0xc0
   __TEXT.__oslogstring: 0xee
   __TEXT.__objc_classname: 0x16
   __TEXT.__objc_methname: 0x58b
-  __TEXT.__objc_methtype: 0x3d5
+  __TEXT.__objc_methtype: 0x3d8
   __TEXT.__dlopen_cstrs: 0x5d
-  __TEXT.__unwind_info: 0x128
+  __TEXT.__unwind_info: 0x130
   __DATA_CONST.__auth_got: 0x198
   __DATA_CONST.__got: 0x58
   __DATA_CONST.__const: 0x218

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
-  UUID: 7A8E7C32-A62A-3F23-B02A-4021E6A2AE45
-  Functions: 53
-  Symbols:   177
+  UUID: 5BD701C4-0A18-304B-91EF-BE96819C9BD5
+  Functions: 54
+  Symbols:   178
   CStrings:  145
 
Symbols:
+ LA_LOG_coreauthd_client.cold.1
Functions:
~ _pam_sm_authenticate : 1032 -> 1028
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
