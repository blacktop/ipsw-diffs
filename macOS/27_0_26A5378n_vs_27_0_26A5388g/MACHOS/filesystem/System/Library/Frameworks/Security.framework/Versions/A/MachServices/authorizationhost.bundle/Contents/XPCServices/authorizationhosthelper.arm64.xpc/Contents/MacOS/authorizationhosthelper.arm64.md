## authorizationhosthelper.arm64

> `/System/Library/Frameworks/Security.framework/Versions/A/MachServices/authorizationhost.bundle/Contents/XPCServices/authorizationhosthelper.arm64.xpc/Contents/MacOS/authorizationhosthelper.arm64`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-55643.0.5.0.0
-  __TEXT.__text: 0x7e98
-  __TEXT.__auth_stubs: 0x720
-  __TEXT.__objc_stubs: 0xfe0
-  __TEXT.__objc_methlist: 0x77c
+55643.0.12.0.0
+  __TEXT.__text: 0x7d50
+  __TEXT.__auth_stubs: 0x740
+  __TEXT.__objc_stubs: 0x1000
+  __TEXT.__objc_methlist: 0x78c
   __TEXT.__const: 0xd8
-  __TEXT.__cstring: 0x4b1
+  __TEXT.__cstring: 0x4d1
   __TEXT.__objc_classname: 0x11a
-  __TEXT.__objc_methname: 0xe7f
-  __TEXT.__objc_methtype: 0x6be
+  __TEXT.__objc_methname: 0xea3
+  __TEXT.__objc_methtype: 0x6eb
   __TEXT.__oslogstring: 0xc2c
   __TEXT.__gcc_except_tab: 0xc4
   __TEXT.__unwind_info: 0x2b8
-  __DATA_CONST.__const: 0x290
+  __DATA_CONST.__const: 0x230
   __DATA_CONST.__cfstring: 0x220
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x40
-  __DATA_CONST.__auth_got: 0x3a0
+  __DATA_CONST.__auth_got: 0x3b0
   __DATA_CONST.__got: 0x130
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__objc_const: 0xb78
-  __DATA.__objc_selrefs: 0x528
-  __DATA.__objc_ivar: 0x74
+  __DATA.__objc_const: 0xb98
+  __DATA.__objc_selrefs: 0x530
+  __DATA.__objc_ivar: 0x78
   __DATA.__objc_data: 0x410
   __DATA.__data: 0xc1
   __DATA.__bss: 0x56

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 286
-  Symbols:   226
-  CStrings:  414
+  Functions: 283
+  Symbols:   229
+  CStrings:  419
 
Symbols:
+ OBJC_IVAR_$_AgentMechanism._stateLock
+ __os_feature_enabled_impl
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
- _dispatch_async
CStrings:
+ "SafePluginLoading"
+ "SecurityAgent"
+ "_stateLock"
+ "safePluginLoadingEnabled"
+ "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
```
