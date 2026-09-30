## authorizationhosthelper.x86_64

> `/System/Library/Frameworks/Security.framework/Versions/A/MachServices/authorizationhost.bundle/Contents/XPCServices/authorizationhosthelper.x86_64.xpc/Contents/MacOS/authorizationhosthelper.x86_64`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-55643.0.5.0.0
-  __TEXT.__text: 0x8310
-  __TEXT.__stubs: 0x29a
+55643.0.12.0.0
+  __TEXT.__text: 0x8280
+  __TEXT.__stubs: 0x2a6
   __TEXT.__const: 0x70
-  __TEXT.__cstring: 0x4b2
-  __TEXT.__objc_methname: 0xe7f
+  __TEXT.__cstring: 0x4d2
+  __TEXT.__objc_methname: 0xea3
   __TEXT.__objc_classname: 0x11a
-  __TEXT.__objc_methtype: 0x6be
+  __TEXT.__objc_methtype: 0x6eb
   __TEXT.__oslogstring: 0xe6b
   __TEXT.__gcc_except_tab: 0xb8
-  __TEXT.__unwind_info: 0x2f0
+  __TEXT.__unwind_info: 0x2e0
   __TEXT.__eh_frame: 0x58
-  __DATA_CONST.__const: 0x290
+  __DATA_CONST.__const: 0x230
   __DATA_CONST.__cfstring: 0x220
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x40
-  __DATA_CONST.__got: 0x4c0
-  __DATA.__objc_const: 0x1630
-  __DATA.__objc_selrefs: 0x410
-  __DATA.__objc_ivar: 0xe8
+  __DATA_CONST.__got: 0x4d0
+  __DATA.__objc_const: 0x1668
+  __DATA.__objc_selrefs: 0x418
+  __DATA.__objc_ivar: 0xf0
   __DATA.__objc_data: 0x778
   __DATA.__data: 0xc1
   __DATA.__bss: 0x56

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 277
-  Symbols:   225
-  CStrings:  414
+  Functions: 274
+  Symbols:   228
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
