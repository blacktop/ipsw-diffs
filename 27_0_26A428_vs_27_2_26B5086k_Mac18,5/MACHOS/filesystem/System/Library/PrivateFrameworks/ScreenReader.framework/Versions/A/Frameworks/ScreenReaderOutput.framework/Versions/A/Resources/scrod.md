## scrod

> `/System/Library/PrivateFrameworks/ScreenReader.framework/Versions/A/Frameworks/ScreenReaderOutput.framework/Versions/A/Resources/scrod`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1048.3.0.0.0
-  __TEXT.__text: 0x95e4
-  __TEXT.__auth_stubs: 0x500
-  __TEXT.__objc_stubs: 0x1bc0
+1050.3.0.0.0
+  __TEXT.__text: 0x9340
+  __TEXT.__auth_stubs: 0x4f0
+  __TEXT.__objc_stubs: 0x1b20
   __TEXT.__objc_methlist: 0x7d0
   __TEXT.__dlopen_cstrs: 0x5c
-  __TEXT.__gcc_except_tab: 0x5c4
+  __TEXT.__gcc_except_tab: 0x5c0
   __TEXT.__const: 0x40
   __TEXT.__objc_classname: 0x11c
-  __TEXT.__objc_methname: 0x1d3c
+  __TEXT.__objc_methname: 0x1cb5
   __TEXT.__objc_methtype: 0x3d9
-  __TEXT.__cstring: 0x649
-  __TEXT.__oslogstring: 0x69a
+  __TEXT.__cstring: 0x62b
+  __TEXT.__oslogstring: 0x67b
   __TEXT.__unwind_info: 0x338
   __DATA_CONST.__const: 0x188
-  __DATA_CONST.__cfstring: 0x500
+  __DATA_CONST.__cfstring: 0x4e0
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x70
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__auth_got: 0x290
-  __DATA_CONST.__got: 0x3b0
-  __DATA.__objc_const: 0xa00
-  __DATA.__objc_selrefs: 0x938
-  __DATA.__objc_ivar: 0x54
+  __DATA_CONST.__auth_got: 0x288
+  __DATA_CONST.__got: 0x3a8
+  __DATA.__objc_const: 0x9e0
+  __DATA.__objc_selrefs: 0x910
+  __DATA.__objc_ivar: 0x50
   __DATA.__objc_data: 0x1e0
   __DATA.__data: 0x2a0
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 147
-  Symbols:   215
-  CStrings:  472
+  Symbols:   213
+  CStrings:  464
 
Symbols:
- _OBJC_CLASS_$_SCROBrailleHandler
- _isBrailleXPCOn
Functions:
~ sub_100008a78 : 324 -> 288
~ sub_100008cf4 -> sub_100008cd0 : 1200 -> 648
~ sub_1000091a4 -> sub_100008f58 : 352 -> 264
CStrings:
- "SCROD using XPC interface: %d"
- "SCRODMain using Mach transport"
- "_useXPCTransport"
- "detachNewThreadSelector:toTarget:withObject:"
- "initWithObjectsAndKeys:"
- "registerWithMach"
- "serverSource"
- "unregisterWithMach"
```
