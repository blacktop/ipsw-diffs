## authorizationhosthelper.arm64

> `/System/Library/Frameworks/Security.framework/Versions/A/MachServices/authorizationhost.bundle/Contents/XPCServices/authorizationhosthelper.arm64.xpc/Contents/MacOS/authorizationhosthelper.arm64`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-55600.160.5.0.1
-  __TEXT.__text: 0x8f58
-  __TEXT.__auth_stubs: 0x7d0
-  __TEXT.__objc_stubs: 0xfa0
-  __TEXT.__objc_methlist: 0x774
+55600.160.6.0.1
+  __TEXT.__text: 0x8f98
+  __TEXT.__auth_stubs: 0x7e0
+  __TEXT.__objc_stubs: 0xfc0
+  __TEXT.__objc_methlist: 0x784
   __TEXT.__const: 0xf0
-  __TEXT.__cstring: 0x68b
+  __TEXT.__cstring: 0x6ab
   __TEXT.__objc_classname: 0x121
-  __TEXT.__objc_methname: 0xdf4
+  __TEXT.__objc_methname: 0xe0d
   __TEXT.__objc_methtype: 0x6c0
   __TEXT.__oslogstring: 0xc37
   __TEXT.__gcc_except_tab: 0xa8
   __TEXT.__dlopen_cstrs: 0x5d
   __TEXT.__unwind_info: 0x300
-  __DATA_CONST.__auth_got: 0x3f8
+  __DATA_CONST.__auth_got: 0x400
   __DATA_CONST.__got: 0x120
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x398

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x40
   __DATA.__objc_const: 0xb58
-  __DATA.__objc_selrefs: 0x510
+  __DATA.__objc_selrefs: 0x518
   __DATA.__objc_ivar: 0x70
   __DATA.__objc_data: 0x410
   __DATA.__data: 0xc1

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 313
-  Symbols:   236
-  CStrings:  435
+  Functions: 314
+  Symbols:   237
+  CStrings:  438
 
Symbols:
+ __os_feature_enabled_impl
Functions:
~ sub_100006f28 : 1408 -> 1412
+ sub_100008004
CStrings:
+ "SafePluginLoading"
+ "SecurityAgent"
+ "safePluginLoadingEnabled"
```
