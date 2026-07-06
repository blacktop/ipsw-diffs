## SecurityAgentHelper-arm64

> `/System/Library/Frameworks/Security.framework/Versions/A/MachServices/SecurityAgent.bundle/Contents/XPCServices/SecurityAgentHelper-arm64.xpc/Contents/MacOS/SecurityAgentHelper-arm64`

```diff

-  __TEXT.__text: 0x1ea6c
+  __TEXT.__text: 0x1eb8c
   __TEXT.__auth_stubs: 0xf30
   __TEXT.__objc_stubs: 0x47c0
-  __TEXT.__objc_methlist: 0x207c
+  __TEXT.__objc_methlist: 0x2084
   __TEXT.__const: 0x128
-  __TEXT.__objc_methname: 0x4dbb
-  __TEXT.__oslogstring: 0x2273
+  __TEXT.__objc_methname: 0x4de3
+  __TEXT.__oslogstring: 0x22d4
   __TEXT.__objc_classname: 0x32d
   __TEXT.__objc_methtype: 0x1718
-  __TEXT.__cstring: 0x1f72
+  __TEXT.__cstring: 0x1f85
   __TEXT.__gcc_except_tab: 0x3c4
   __TEXT.__ustring: 0xa86
   __TEXT.__dlopen_cstrs: 0xb0
-  __TEXT.__unwind_info: 0x7a0
+  __TEXT.__unwind_info: 0x7b0
   __DATA_CONST.__const: 0x758
   __DATA_CONST.__cfstring: 0x1a20
   __DATA_CONST.__objc_classlist: 0xe0

   __DATA_CONST.__objc_intobj: 0xa8
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__auth_got: 0x7a8
-  __DATA_CONST.__got: 0x410
+  __DATA_CONST.__got: 0x420
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA.__objc_const: 0x3170
-  __DATA.__objc_selrefs: 0x17f0
-  __DATA.__objc_ivar: 0x2b0
+  __DATA.__objc_const: 0x3190
+  __DATA.__objc_selrefs: 0x17f8
+  __DATA.__objc_ivar: 0x2b4
   __DATA.__objc_data: 0x8c0
   __DATA.__data: 0x4a0
   __DATA.__bss: 0x130

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 807
-  Symbols:   522
-  CStrings:  1970
+  Functions: 808
+  Symbols:   523
+  CStrings:  1974
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__objc_arrayobj : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
+ OBJC_IVAR_$_AgentMechanism._pluginUnavailable
CStrings:
+ "AgentMechanism [%{public}@:%{public}@] plugin unavailable, falling back to no-op"
+ "No plugin at path: %{public}@, errno: %d (%s)"
+ "_pluginUnavailable"
+ "plugin-unavailable"
+ "setPluginUnavailable"
- "No plugin at path: %{public}@"

```
