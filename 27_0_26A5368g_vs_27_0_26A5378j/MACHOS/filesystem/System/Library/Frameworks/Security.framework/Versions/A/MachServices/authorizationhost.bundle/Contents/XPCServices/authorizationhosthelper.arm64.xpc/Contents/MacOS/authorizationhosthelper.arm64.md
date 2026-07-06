## authorizationhosthelper.arm64

> `/System/Library/Frameworks/Security.framework/Versions/A/MachServices/authorizationhost.bundle/Contents/XPCServices/authorizationhosthelper.arm64.xpc/Contents/MacOS/authorizationhosthelper.arm64`

```diff

-  __TEXT.__text: 0x7d90
-  __TEXT.__auth_stubs: 0x700
+  __TEXT.__text: 0x7e98
+  __TEXT.__auth_stubs: 0x720
   __TEXT.__objc_stubs: 0xfe0
-  __TEXT.__objc_methlist: 0x774
+  __TEXT.__objc_methlist: 0x77c
   __TEXT.__const: 0xd8
-  __TEXT.__cstring: 0x49e
+  __TEXT.__cstring: 0x4b1
   __TEXT.__objc_classname: 0x11a
-  __TEXT.__objc_methname: 0xe57
-  __TEXT.__objc_methtype: 0x6bc
-  __TEXT.__oslogstring: 0xbcb
+  __TEXT.__objc_methname: 0xe7f
+  __TEXT.__objc_methtype: 0x6be
+  __TEXT.__oslogstring: 0xc2c
   __TEXT.__gcc_except_tab: 0xc4
-  __TEXT.__unwind_info: 0x2b0
+  __TEXT.__unwind_info: 0x2b8
   __DATA_CONST.__const: 0x290
   __DATA_CONST.__cfstring: 0x220
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x40
-  __DATA_CONST.__auth_got: 0x390
-  __DATA_CONST.__got: 0x120
+  __DATA_CONST.__auth_got: 0x3a0
+  __DATA_CONST.__got: 0x130
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__objc_const: 0xb58
-  __DATA.__objc_selrefs: 0x520
-  __DATA.__objc_ivar: 0x70
+  __DATA.__objc_const: 0xb78
+  __DATA.__objc_selrefs: 0x528
+  __DATA.__objc_ivar: 0x74
   __DATA.__objc_data: 0x410
   __DATA.__data: 0xc1
   __DATA.__bss: 0x56

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 286
-  Symbols:   223
-  CStrings:  427
+  Symbols:   226
+  CStrings:  432
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
+ OBJC_IVAR_$_AgentMechanism._pluginUnavailable
+ ___error
+ _strerror
CStrings:
+ "AgentMechanism [%{public}@:%{public}@] plugin unavailable, falling back to no-op"
+ "B"
+ "No plugin at path: %{public}@, errno: %d (%s)"
+ "_pluginUnavailable"
+ "plugin-unavailable"
+ "setPluginUnavailable"
- "No plugin at path: %{public}@"

```
