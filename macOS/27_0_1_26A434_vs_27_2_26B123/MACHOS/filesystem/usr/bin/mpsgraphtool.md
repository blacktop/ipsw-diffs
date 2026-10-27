## mpsgraphtool

> `/usr/bin/mpsgraphtool`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-7.0.80.0.0
-  __TEXT.__text: 0x1c6c4
+7.1.6.0.0
+  __TEXT.__text: 0x1c5cc
   __TEXT.__auth_stubs: 0x690
-  __TEXT.__objc_stubs: 0x11a0
+  __TEXT.__objc_stubs: 0x11c0
   __TEXT.__objc_methlist: 0x1e8
   __TEXT.__const: 0xf0
-  __TEXT.__cstring: 0x3e96
-  __TEXT.__gcc_except_tab: 0x22e4
-  __TEXT.__objc_methname: 0x106f
+  __TEXT.__cstring: 0x3eeb
+  __TEXT.__gcc_except_tab: 0x22f8
+  __TEXT.__objc_methname: 0x107a
   __TEXT.__objc_classname: 0x2f
   __TEXT.__objc_methtype: 0x1d8
   __TEXT.__unwind_info: 0x448

   __DATA_CONST.__got: 0x130
   __DATA_CONST.__auth_ptr: 0x10
   __DATA.__objc_const: 0x2f0
-  __DATA.__objc_selrefs: 0x550
+  __DATA.__objc_selrefs: 0x558
   __DATA.__objc_ivar: 0x10
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x178

   - /usr/lib/libncurses.5.4.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 151
-  Symbols:   576
-  CStrings:  605
+  Symbols:   577
+  CStrings:  607
 
Symbols:
+ _objc_msgSend$getSoCName
Functions:
~ __Z10printUsageb : 2348 -> 2388
~ _main : 20800 -> 20512
CStrings:
+ "getSoCName"
+ "getSoCName: get the SoC name for current device that MPSGraph recognizes\n"
```
