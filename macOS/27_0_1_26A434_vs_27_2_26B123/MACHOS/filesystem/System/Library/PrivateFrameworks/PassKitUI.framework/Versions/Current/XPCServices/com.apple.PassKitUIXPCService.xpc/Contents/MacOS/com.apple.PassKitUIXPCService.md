## com.apple.PassKitUIXPCService

> `/System/Library/PrivateFrameworks/PassKitUI.framework/Versions/Current/XPCServices/com.apple.PassKitUIXPCService.xpc/Contents/MacOS/com.apple.PassKitUIXPCService`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-387.0.0.0.0
-  __TEXT.__text: 0x22e0
-  __TEXT.__auth_stubs: 0x270
+388.0.0.0.0
+  __TEXT.__text: 0x2484
+  __TEXT.__auth_stubs: 0x300
   __TEXT.__objc_stubs: 0x8c0
   __TEXT.__objc_methlist: 0x374
-  __TEXT.__const: 0x58
-  __TEXT.__cstring: 0x3bf
-  __TEXT.__oslogstring: 0x1cc
+  __TEXT.__const: 0x68
+  __TEXT.__cstring: 0x3dd
+  __TEXT.__oslogstring: 0x261
   __TEXT.__objc_classname: 0x3c
   __TEXT.__objc_methtype: 0x263
   __TEXT.__objc_methname: 0xcce
   __TEXT.__unwind_info: 0x118
   __DATA_CONST.__const: 0x180
-  __DATA_CONST.__cfstring: 0x260
+  __DATA_CONST.__cfstring: 0x280
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__auth_got: 0x140
+  __DATA_CONST.__auth_got: 0x188
   __DATA_CONST.__got: 0xc8
   __DATA.__objc_const: 0x420
   __DATA.__objc_selrefs: 0x390

   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
+  - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /System/Library/PrivateFrameworks/AppleAccount.framework/Versions/A/AppleAccount
   - /System/Library/PrivateFrameworks/Bom.framework/Versions/A/Bom
   - /System/Library/PrivateFrameworks/PassKitCore.framework/Versions/A/PassKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 46
-  Symbols:   82
-  CStrings:  208
+  Symbols:   91
+  CStrings:  211
 
Symbols:
+ _CFBooleanGetTypeID
+ _CFBooleanGetValue
+ _CFGetTypeID
+ _CFRelease
+ _SecTaskCopyValueForEntitlement
+ _SecTaskCreateWithAuditToken
+ _xpc_connection_cancel
+ _xpc_connection_get_audit_token
+ _xpc_connection_get_pid
Functions:
~ sub_100002ee0 -> sub_100002f40 : 152 -> 572
CStrings:
+ "[PassKitUIXPCService] failed to read entitlement for peer pid %d: %{public}@"
+ "[PassKitUIXPCService] refusing connection from unentitled peer, pid %d."
+ "com.apple.passes.add-silently"
```
