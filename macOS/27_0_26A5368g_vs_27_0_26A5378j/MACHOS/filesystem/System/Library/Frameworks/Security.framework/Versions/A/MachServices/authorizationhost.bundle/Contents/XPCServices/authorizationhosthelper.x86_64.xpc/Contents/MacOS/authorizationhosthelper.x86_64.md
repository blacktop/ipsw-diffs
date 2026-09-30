## authorizationhosthelper.x86_64

> `/System/Library/Frameworks/Security.framework/Versions/A/MachServices/authorizationhost.bundle/Contents/XPCServices/authorizationhosthelper.x86_64.xpc/Contents/MacOS/authorizationhosthelper.x86_64`

```diff

-  __TEXT.__text: 0x81f0
-  __TEXT.__stubs: 0x28e
+  __TEXT.__text: 0x8310
+  __TEXT.__stubs: 0x29a
   __TEXT.__const: 0x70
-  __TEXT.__cstring: 0x49f
-  __TEXT.__objc_methname: 0xe57
+  __TEXT.__cstring: 0x4b2
+  __TEXT.__objc_methname: 0xe7f
   __TEXT.__objc_classname: 0x11a
-  __TEXT.__objc_methtype: 0x6bc
-  __TEXT.__oslogstring: 0xdfb
+  __TEXT.__objc_methtype: 0x6be
+  __TEXT.__oslogstring: 0xe6b
   __TEXT.__gcc_except_tab: 0xb8
-  __TEXT.__unwind_info: 0x2e0
+  __TEXT.__unwind_info: 0x2f0
   __TEXT.__eh_frame: 0x58
   __DATA_CONST.__const: 0x290
   __DATA_CONST.__cfstring: 0x220

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x40
-  __DATA_CONST.__got: 0x4b0
-  __DATA.__objc_const: 0x15f8
-  __DATA.__objc_selrefs: 0x408
-  __DATA.__objc_ivar: 0xe0
+  __DATA_CONST.__got: 0x4c0
+  __DATA.__objc_const: 0x1630
+  __DATA.__objc_selrefs: 0x410
+  __DATA.__objc_ivar: 0xe8
   __DATA.__objc_data: 0x778
   __DATA.__data: 0xc1
   __DATA.__bss: 0x56

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 276
-  Symbols:   222
-  CStrings:  427
+  Functions: 277
+  Symbols:   225
+  CStrings:  432
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
+ OBJC_IVAR_$_AgentMechanism._pluginUnavailable
+ ___error
+ _strerror
CStrings:
+ "AgentMechanism [%{public}@:%{public}@] plugin unavailable, falling back to no-op"
+ "No plugin at path: %{public}@, errno: %d (%s)"
+ "_pluginUnavailable"
+ "c"
+ "plugin-unavailable"
+ "setPluginUnavailable"
- "No plugin at path: %{public}@"

```
