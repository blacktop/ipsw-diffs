## SecurityAgentHelper-x86_64

> `/System/Library/Frameworks/Security.framework/Versions/A/MachServices/SecurityAgent.bundle/Contents/XPCServices/SecurityAgentHelper-x86_64.xpc/Contents/MacOS/SecurityAgentHelper-x86_64`

```diff

-  __TEXT.__text: 0x22014
+  __TEXT.__text: 0x22134
   __TEXT.__stubs: 0x5a6
   __TEXT.__const: 0xe0
-  __TEXT.__objc_methname: 0x4f12
-  __TEXT.__oslogstring: 0x28d1
+  __TEXT.__objc_methname: 0x4f3a
+  __TEXT.__oslogstring: 0x2941
   __TEXT.__objc_classname: 0x32d
   __TEXT.__objc_methtype: 0x1723
-  __TEXT.__cstring: 0x1f72
+  __TEXT.__cstring: 0x1f85
   __TEXT.__gcc_except_tab: 0x3c4
   __TEXT.__ustring: 0xa86
   __TEXT.__dlopen_cstrs: 0xbd
-  __TEXT.__unwind_info: 0x768
+  __TEXT.__unwind_info: 0x778
   __TEXT.__eh_frame: 0x58
   __DATA_CONST.__const: 0x748
   __DATA_CONST.__cfstring: 0x1a20

   __DATA_CONST.__objc_intobj: 0xa8
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__got: 0xbc0
-  __DATA.__objc_const: 0x6c48
-  __DATA.__objc_selrefs: 0x12f8
-  __DATA.__objc_ivar: 0x560
+  __DATA.__objc_const: 0x6c80
+  __DATA.__objc_selrefs: 0x1300
+  __DATA.__objc_ivar: 0x568
   __DATA.__objc_data: 0xc48
   __DATA.__data: 0x4a0
   __DATA.__bss: 0x130

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 781
-  Symbols:   522
-  CStrings:  1989
+  Functions: 782
+  Symbols:   523
+  CStrings:  1993
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA_CONST.__got : content changed
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
