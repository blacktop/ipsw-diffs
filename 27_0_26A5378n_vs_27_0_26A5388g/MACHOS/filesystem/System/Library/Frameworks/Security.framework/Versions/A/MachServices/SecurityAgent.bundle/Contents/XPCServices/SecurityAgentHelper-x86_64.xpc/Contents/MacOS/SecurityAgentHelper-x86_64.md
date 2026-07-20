## SecurityAgentHelper-x86_64

> `/System/Library/Frameworks/Security.framework/Versions/A/MachServices/SecurityAgent.bundle/Contents/XPCServices/SecurityAgentHelper-x86_64.xpc/Contents/MacOS/SecurityAgentHelper-x86_64`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-55643.0.5.0.0
-  __TEXT.__text: 0x22134
-  __TEXT.__stubs: 0x5a6
+55643.0.12.0.0
+  __TEXT.__text: 0x224a4
+  __TEXT.__stubs: 0x5b2
   __TEXT.__const: 0xe0
-  __TEXT.__objc_methname: 0x4f3a
+  __TEXT.__objc_methname: 0x4faf
   __TEXT.__oslogstring: 0x2941
   __TEXT.__objc_classname: 0x32d
-  __TEXT.__objc_methtype: 0x1723
-  __TEXT.__cstring: 0x1f85
-  __TEXT.__gcc_except_tab: 0x3c4
+  __TEXT.__objc_methtype: 0x1750
+  __TEXT.__cstring: 0x1f97
+  __TEXT.__gcc_except_tab: 0x3e4
   __TEXT.__ustring: 0xa86
   __TEXT.__dlopen_cstrs: 0xbd
-  __TEXT.__unwind_info: 0x778
+  __TEXT.__unwind_info: 0x788
   __TEXT.__eh_frame: 0x58
-  __DATA_CONST.__const: 0x748
+  __DATA_CONST.__const: 0x778
   __DATA_CONST.__cfstring: 0x1a20
   __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_arrayobj: 0x60
   __DATA_CONST.__objc_intobj: 0xa8
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA_CONST.__got: 0xbc0
-  __DATA.__objc_const: 0x6c80
-  __DATA.__objc_selrefs: 0x1300
-  __DATA.__objc_ivar: 0x568
+  __DATA_CONST.__got: 0xbd8
+  __DATA.__objc_const: 0x6cb8
+  __DATA.__objc_selrefs: 0x1330
+  __DATA.__objc_ivar: 0x570
   __DATA.__objc_data: 0xc48
   __DATA.__data: 0x4a0
   __DATA.__bss: 0x130

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 782
-  Symbols:   523
-  CStrings:  1792
+  Functions: 784
+  Symbols:   527
+  CStrings:  1801
 
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
