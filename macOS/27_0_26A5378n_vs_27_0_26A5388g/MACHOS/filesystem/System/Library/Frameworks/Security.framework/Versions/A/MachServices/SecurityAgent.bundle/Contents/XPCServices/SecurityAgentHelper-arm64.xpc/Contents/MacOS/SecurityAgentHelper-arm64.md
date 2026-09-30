## SecurityAgentHelper-arm64

> `/System/Library/Frameworks/Security.framework/Versions/A/MachServices/SecurityAgent.bundle/Contents/XPCServices/SecurityAgentHelper-arm64.xpc/Contents/MacOS/SecurityAgentHelper-arm64`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-55643.0.5.0.0
-  __TEXT.__text: 0x1eb8c
-  __TEXT.__auth_stubs: 0xf30
-  __TEXT.__objc_stubs: 0x47c0
-  __TEXT.__objc_methlist: 0x2084
-  __TEXT.__const: 0x128
-  __TEXT.__objc_methname: 0x4de3
+55643.0.12.0.0
+  __TEXT.__text: 0x1ee48
+  __TEXT.__auth_stubs: 0xf50
+  __TEXT.__objc_stubs: 0x4880
+  __TEXT.__objc_methlist: 0x208c
+  __TEXT.__const: 0x130
+  __TEXT.__objc_methname: 0x4e58
   __TEXT.__oslogstring: 0x22d4
   __TEXT.__objc_classname: 0x32d
-  __TEXT.__objc_methtype: 0x1718
-  __TEXT.__cstring: 0x1f85
-  __TEXT.__gcc_except_tab: 0x3c4
+  __TEXT.__objc_methtype: 0x1745
+  __TEXT.__cstring: 0x1f97
+  __TEXT.__gcc_except_tab: 0x3e4
   __TEXT.__ustring: 0xa86
   __TEXT.__dlopen_cstrs: 0xb0
-  __TEXT.__unwind_info: 0x7b0
-  __DATA_CONST.__const: 0x758
+  __TEXT.__unwind_info: 0x7b8
+  __DATA_CONST.__const: 0x788
   __DATA_CONST.__cfstring: 0x1a20
   __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_arrayobj: 0x60
   __DATA_CONST.__objc_intobj: 0xa8
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA_CONST.__auth_got: 0x7a8
-  __DATA_CONST.__got: 0x420
+  __DATA_CONST.__auth_got: 0x7b8
+  __DATA_CONST.__got: 0x430
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA.__objc_const: 0x3190
-  __DATA.__objc_selrefs: 0x17f8
-  __DATA.__objc_ivar: 0x2b4
+  __DATA.__objc_const: 0x31b0
+  __DATA.__objc_selrefs: 0x1828
+  __DATA.__objc_ivar: 0x2b8
   __DATA.__objc_data: 0x8c0
   __DATA.__data: 0x4a0
   __DATA.__bss: 0x130

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 808
-  Symbols:   523
-  CStrings:  1774
+  Functions: 810
+  Symbols:   527
+  CStrings:  1783
 
Symbols:
+ OBJC_IVAR_$_AgentMechanism._stateLock
+ _OBJC_CLASS_$_NSInvocation
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
CStrings:
+ "SafePluginLoading"
+ "_stateLock"
+ "beginSheetModalForWindow:completionHandler:"
+ "invocationWithMethodSignature:"
+ "methodSignatureForSelector:"
+ "safePluginLoadingEnabled"
+ "setArgument:atIndex:"
+ "setSelector:"
+ "setTarget:"
+ "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
- "beginSheetModalForWindow:modalDelegate:didEndSelector:contextInfo:"
```
