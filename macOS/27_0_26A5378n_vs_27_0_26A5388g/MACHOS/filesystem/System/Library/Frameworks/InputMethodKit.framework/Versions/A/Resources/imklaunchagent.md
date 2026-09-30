## imklaunchagent

> `/System/Library/Frameworks/InputMethodKit.framework/Versions/A/Resources/imklaunchagent`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-570.0.0.0.0
-  __TEXT.__text: 0x81c0
-  __TEXT.__auth_stubs: 0x860
-  __TEXT.__objc_stubs: 0xb80
+571.0.0.0.0
+  __TEXT.__text: 0x84e0
+  __TEXT.__auth_stubs: 0x8b0
+  __TEXT.__objc_stubs: 0xbe0
   __TEXT.__objc_methlist: 0x36c
-  __TEXT.__const: 0xb8
+  __TEXT.__const: 0xc8
   __TEXT.__gcc_except_tab: 0x4c
   __TEXT.__cstring: 0x1165
-  __TEXT.__objc_methname: 0xad6
+  __TEXT.__objc_methname: 0xaf6
   __TEXT.__objc_classname: 0xff
   __TEXT.__objc_methtype: 0x256
-  __TEXT.__oslogstring: 0xcc2
-  __TEXT.__unwind_info: 0x240
+  __TEXT.__oslogstring: 0xd86
+  __TEXT.__unwind_info: 0x248
   __DATA_CONST.__const: 0x710
   __DATA_CONST.__cfstring: 0x960
   __DATA_CONST.__objc_classlist: 0x28

   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA_CONST.__auth_got: 0x440
-  __DATA_CONST.__got: 0x110
+  __DATA_CONST.__auth_got: 0x468
+  __DATA_CONST.__got: 0x118
   __DATA.__objc_const: 0x6f0
-  __DATA.__objc_selrefs: 0x3c0
+  __DATA.__objc_selrefs: 0x3d8
   __DATA.__objc_ivar: 0x30
   __DATA.__objc_data: 0x190
   __DATA.__data: 0x1f8

   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/InputMethodKit.framework/Versions/A/InputMethodKit
+  - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /System/Library/PrivateFrameworks/PlugInKit.framework/Versions/A/PlugInKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 199
-  Symbols:   178
-  CStrings:  353
+  Functions: 203
+  Symbols:   183
+  CStrings:  358
 
Symbols:
+ _SecTaskCopySigningIdentifier
+ _SecTaskCreateWithAuditToken
+ __os_log_fault_impl
+ _objc_opt_class
+ _objc_opt_isKindOfClass
CStrings:
+ "auditToken"
+ "isEqualToString:"
+ "requestIMKXPCEndpointInvalid: pid %d has not received endpoint for %{private}@, rejected"
+ "set"
+ "setIMKXPCEndpoint: pid %d (signing-id=%{public}@) attempted to register endpoint for %{private}@, rejected"
```
