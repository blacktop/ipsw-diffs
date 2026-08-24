## Erase Assistant

> `/System/Library/CoreServices/Erase Assistant.app/Contents/MacOS/Erase Assistant`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methtype`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-282.0.0.0.0
-  __TEXT.__text: 0xd1e8
-  __TEXT.__auth_stubs: 0x3a0
-  __TEXT.__objc_stubs: 0x2ba0
-  __TEXT.__objc_methlist: 0x1020
+285.0.0.0.0
+  __TEXT.__text: 0xd3e8
+  __TEXT.__auth_stubs: 0x3b0
+  __TEXT.__objc_stubs: 0x2bc0
+  __TEXT.__objc_methlist: 0x1060
   __TEXT.__const: 0x90
-  __TEXT.__cstring: 0xdde
-  __TEXT.__oslogstring: 0x791
+  __TEXT.__cstring: 0xde1
+  __TEXT.__oslogstring: 0x800
   __TEXT.__objc_classname: 0x290
-  __TEXT.__objc_methname: 0x31f2
+  __TEXT.__objc_methname: 0x3265
   __TEXT.__objc_methtype: 0xac2
   __TEXT.__gcc_except_tab: 0x58
   __TEXT.__dlopen_cstrs: 0x64
-  __TEXT.__unwind_info: 0x340
+  __TEXT.__unwind_info: 0x348
   __DATA_CONST.__const: 0x550
   __DATA_CONST.__cfstring: 0x12a0
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x30
+  __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA_CONST.__auth_got: 0x1e0
+  __DATA_CONST.__auth_got: 0x1e8
   __DATA_CONST.__got: 0x2c0
-  __DATA.__objc_const: 0x1b10
-  __DATA.__objc_selrefs: 0xea0
-  __DATA.__objc_ivar: 0xd0
+  __DATA.__objc_const: 0x1b70
+  __DATA.__objc_selrefs: 0xea8
+  __DATA.__objc_ivar: 0xd8
   __DATA.__objc_data: 0x550
   __DATA.__data: 0x3c0
   __DATA.__bss: 0x28

   - /System/Library/PrivateFrameworks/TimeMachine.framework/Versions/A/TimeMachine
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 294
-  Symbols:   163
-  CStrings:  903
+  Functions: 299
+  Symbols:   164
+  CStrings:  906
 
Symbols:
+ _objc_opt_respondsToSelector
CStrings:
+ "Skipping Find My sign out; in repair mode"
+ "Skipping find my sign out as repair mode should not turn off find my"
+ "T@\"DKSharedRepairModeProvider\",&,V_repairModeProvider"
+ "initWithWindowController:repairModeProvider:"
+ "initWithWindowNibName:repairModeProvider:"
- "C"
- "initWithWindowController:"
```
