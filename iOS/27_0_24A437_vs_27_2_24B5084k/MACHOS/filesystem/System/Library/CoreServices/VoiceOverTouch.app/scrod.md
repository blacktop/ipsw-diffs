## scrod

> `/System/Library/CoreServices/VoiceOverTouch.app/scrod`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-329.0.0.0.0
-  __TEXT.__text: 0xbb8c
+330.1.0.0.0
+  __TEXT.__text: 0xb9c8
   __TEXT.__auth_stubs: 0x730
-  __TEXT.__objc_stubs: 0x1aa0
+  __TEXT.__objc_stubs: 0x1a00
   __TEXT.__objc_methlist: 0x850
   __TEXT.__const: 0x70
   __TEXT.__gcc_except_tab: 0x794
-  __TEXT.__objc_methname: 0x1c43
-  __TEXT.__cstring: 0x392
-  __TEXT.__oslogstring: 0x1325
+  __TEXT.__objc_methname: 0x1bbb
+  __TEXT.__cstring: 0x386
+  __TEXT.__oslogstring: 0x12f2
   __TEXT.__objc_classname: 0x12e
   __TEXT.__objc_methtype: 0x3d7
   __TEXT.__unwind_info: 0x388

   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__auth_got: 0x3a8
-  __DATA_CONST.__got: 0x318
-  __DATA.__objc_const: 0xac8
-  __DATA.__objc_selrefs: 0x8d8
-  __DATA.__objc_ivar: 0x7c
+  __DATA_CONST.__got: 0x310
+  __DATA.__objc_const: 0xaa8
+  __DATA.__objc_selrefs: 0x8b0
+  __DATA.__objc_ivar: 0x78
   __DATA.__objc_data: 0x190
   __DATA.__data: 0x300
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 159
-  Symbols:   225
-  CStrings:  526
+  Symbols:   224
+  CStrings:  518
 
Symbols:
- _OBJC_CLASS_$_SCROBrailleHandler
Functions:
~ sub_100001a60 : 280 -> 244
~ sub_100001c84 -> sub_100001c60 : 920 -> 636
~ sub_10000201c -> sub_100001edc : 356 -> 272
~ sub_100002180 -> sub_100001fec : 256 -> 208
CStrings:
+ "MSCRODMain using Swift BrailleServer"
- "Braille_XPC"
- "MSCRODMain using Mach transport"
- "MSCRODMain using XPC transport with Swift BrailleServer"
- "_usesXPCTransport"
- "detachNewThreadSelector:toTarget:withObject:"
- "initWithObjectsAndKeys:"
- "registerWithMach"
- "serverSource"
- "unregisterWithMach"
```
