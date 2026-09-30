## authd

> `/System/Library/Frameworks/Security.framework/Versions/Current/XPCServices/authd.xpc/Contents/MacOS/authd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-62460.1.3.0.0
-  __TEXT.__text: 0x25e98
+62460.40.49.501.1
+  __TEXT.__text: 0x25f20
   __TEXT.__auth_stubs: 0x1380
   __TEXT.__lazy_helpers: 0x63c
   __TEXT.__objc_stubs: 0xc00
   __TEXT.__objc_methlist: 0x154
-  __TEXT.__const: 0xb10
+  __TEXT.__const: 0xb20
   __TEXT.__cstring: 0x2ea9
-  __TEXT.__oslogstring: 0x4bda
+  __TEXT.__oslogstring: 0x4c23
   __TEXT.__dlopen_cstrs: 0x5d
-  __TEXT.__gcc_except_tab: 0xd70
+  __TEXT.__gcc_except_tab: 0xd74
   __TEXT.__objc_methname: 0x9c0
   __TEXT.__objc_classname: 0xf
   __TEXT.__objc_methtype: 0x140

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 465
+  Functions: 463
   Symbols:   397
-  CStrings:  1046
+  CStrings:  1047
 
CStrings:
+ "authorization_copy_prelogin_userdb: denying non-first-party process [%s]"
```
