## PlatformSSO

> `/System/Library/OpenDirectory/Modules/PlatformSSO.bundle/Contents/MacOS/PlatformSSO`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA.__objc_selrefs`

```diff

-643.0.21.0.0
-  __TEXT.__text: 0x3dd4
+643.0.33.0.0
+  __TEXT.__text: 0x3f18
   __TEXT.__auth_stubs: 0x3c0
   __TEXT.__objc_stubs: 0x640
-  __TEXT.__const: 0x50
-  __TEXT.__gcc_except_tab: 0x1e0
-  __TEXT.__cstring: 0x298
-  __TEXT.__oslogstring: 0x5ee
+  __TEXT.__const: 0x58
+  __TEXT.__gcc_except_tab: 0x1f4
+  __TEXT.__cstring: 0x2c4
+  __TEXT.__oslogstring: 0x657
   __TEXT.__objc_methname: 0x3ce
   __TEXT.__unwind_info: 0x188
   __DATA_CONST.__const: 0x278
-  __DATA_CONST.__cfstring: 0x400
+  __DATA_CONST.__cfstring: 0x420
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_arraydata: 0x48
   __DATA_CONST.__objc_arrayobj: 0x60

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libodmodule.dylib
-  Functions: 93
+  Functions: 94
   Symbols:   112
-  CStrings:  127
+  CStrings:  129
 
CStrings:
+ "odm_RecordVerifyPassword: refusing verify: authorizationEnabled=%d hasLocalRecord=%d userName=%{public}@"
+ "verify password not permitted for this user"
```
