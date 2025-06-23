## UserManagementLayout

> `/System/Library/PrivateFrameworks/UserManagementLayout.framework/UserManagementLayout`

```diff

-452.0.0.0.0
-  __TEXT.__text: 0x1446c
-  __TEXT.__auth_stubs: 0x840
-  __TEXT.__objc_methlist: 0xb14
+458.0.0.502.1
+  __TEXT.__text: 0x144c8
+  __TEXT.__auth_stubs: 0x860
+  __TEXT.__objc_methlist: 0xb24
   __TEXT.__const: 0xd0
-  __TEXT.__oslogstring: 0x2704
+  __TEXT.__oslogstring: 0x2761
   __TEXT.__cstring: 0x62f
   __TEXT.__unwind_info: 0x1f8
   __TEXT.__objc_classname: 0xe1
-  __TEXT.__objc_methname: 0x1b58
+  __TEXT.__objc_methname: 0x1b98
   __TEXT.__objc_methtype: 0x6b3
   __TEXT.__objc_stubs: 0x1620
   __DATA_CONST.__got: 0xf0

   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x710
+  __DATA_CONST.__objc_selrefs: 0x718
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x428
-  __AUTH_CONST.__const: 0x140
+  __AUTH_CONST.__auth_got: 0x438
+  __AUTH_CONST.__const: 0x160
   __AUTH_CONST.__cfstring: 0x840
-  __AUTH_CONST.__objc_const: 0x1110
+  __AUTH_CONST.__objc_const: 0x1118
   __AUTH.__objc_data: 0x190
   __DATA.__objc_ivar: 0xe0
   __DATA.__data: 0x128
   __DATA.__bss: 0x68
   __DATA_DIRTY.__objc_data: 0xa0
-  __DATA_DIRTY.__bss: 0x50
+  __DATA_DIRTY.__bss: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /System/Library/PrivateFrameworks/AppleKeyStore.framework/AppleKeyStore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2346A1EE-E0DD-3A90-BDE0-0AFF82A12E86
-  Functions: 273
-  Symbols:   176
-  CStrings:  797
+  UUID: F40F0F29-DA41-3EE5-BEAB-622AD71A1AF7
+  Functions: 277
+  Symbols:   178
+  CStrings:  800
 
Symbols:
+ _aks_verify_password
+ _aks_verify_password_with_acm
CStrings:
+ "Calling aks_verify_password for user:%d"
+ "Calling aks_verify_password_with_acm for user:%d"
+ "aks_verify_password(-%u) failed: %{mach.errno}d"
+ "verified AKS identity in session %u"
+ "verifyIdentityPasswordInSession:passcode:isACMCredential:error:"
- "Failed to unload AKS Identity with error %@"
- "unloaded AKS identity on error path"

```
