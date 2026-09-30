## PlatformSSOToken

> `/System/Library/ExtensionKit/Extensions/PlatformSSOToken.appex/Contents/MacOS/PlatformSSOToken`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-643.0.21.0.0
-  __TEXT.__text: 0x2958
-  __TEXT.__auth_stubs: 0x1c0
-  __TEXT.__objc_stubs: 0x840
-  __TEXT.__objc_methlist: 0x414
-  __TEXT.__const: 0x68
+643.0.33.0.0
+  __TEXT.__text: 0x2a40
+  __TEXT.__auth_stubs: 0x1e0
+  __TEXT.__objc_stubs: 0x8a0
+  __TEXT.__objc_methlist: 0x42c
+  __TEXT.__const: 0x60
   __TEXT.__objc_classname: 0xe1
-  __TEXT.__objc_methname: 0x9bc
-  __TEXT.__objc_methtype: 0x4d6
-  __TEXT.__cstring: 0x36a
-  __TEXT.__oslogstring: 0x1be
+  __TEXT.__objc_methname: 0xa08
+  __TEXT.__objc_methtype: 0x4e8
+  __TEXT.__cstring: 0x370
+  __TEXT.__oslogstring: 0x255
   __TEXT.__unwind_info: 0x118
   __DATA_CONST.__const: 0xe8
-  __DATA_CONST.__cfstring: 0x260
+  __DATA_CONST.__cfstring: 0x280
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA_CONST.__objc_arraydata: 0x180
-  __DATA_CONST.__objc_arrayobj: 0x90
+  __DATA_CONST.__objc_arraydata: 0x80
+  __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA_CONST.__auth_got: 0xe8
+  __DATA_CONST.__auth_got: 0xf8
   __DATA_CONST.__got: 0xc8
   __DATA.__objc_const: 0xf50
-  __DATA.__objc_selrefs: 0x320
+  __DATA.__objc_selrefs: 0x338
   __DATA.__objc_ivar: 0x2c
   __DATA.__objc_data: 0x280
   __DATA.__data: 0x1e0

   - /System/Library/PrivateFrameworks/PlatformSSOCore.framework/Versions/A/PlatformSSOCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 87
-  Symbols:   69
-  CStrings:  230
+  Functions: 89
+  Symbols:   71
+  CStrings:  238
 
Symbols:
+ _SecTaskCopyTeamIdentifier
+ _SecTaskGetCodeSignStatus
CStrings:
+ "Apple"
+ "B48@0:8{?=[8I]}16"
+ "Caller not allowed: %{public}@"
+ "Caller team not allowed: %{public}@"
+ "isAllowedCallerForAuditToken:"
+ "isEqualToString:"
+ "teamIdentifier: SecTaskCopyTeamIdentifier() failed %{public}@"
+ "teamIdentifier: SecTaskCreateWithAuditToken() failed"
+ "teamIdentifierForAuditToken:"
- "Caller not allowed: %{publoc}@"
```
