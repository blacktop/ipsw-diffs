## uarphidd

> `/usr/libexec/uarphidd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__cstring`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1587.40.28.0.0
-  __TEXT.__text: 0x57d4
-  __TEXT.__auth_stubs: 0x580
-  __TEXT.__objc_stubs: 0xd80
+1587.40.33.0.0
+  __TEXT.__text: 0x5ab4
+  __TEXT.__auth_stubs: 0x5d0
+  __TEXT.__objc_stubs: 0xda0
   __TEXT.__objc_methlist: 0x424
   __TEXT.__const: 0x50
+  __TEXT.__gcc_except_tab: 0x9c
   __TEXT.__cstring: 0x846
-  __TEXT.__objc_methname: 0xeea
-  __TEXT.__oslogstring: 0x8f9
+  __TEXT.__objc_methname: 0xf00
+  __TEXT.__oslogstring: 0x96c
   __TEXT.__objc_classname: 0x74
   __TEXT.__objc_methtype: 0x26a
-  __TEXT.__unwind_info: 0x258
-  __DATA_CONST.__const: 0x178
+  __TEXT.__unwind_info: 0x268
+  __DATA_CONST.__const: 0x1a0
   __DATA_CONST.__cfstring: 0x7e0
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_intobj: 0x90
-  __DATA_CONST.__auth_got: 0x2c8
-  __DATA_CONST.__got: 0xc8
+  __DATA_CONST.__auth_got: 0x2f8
+  __DATA_CONST.__got: 0xc0
   __DATA.__objc_const: 0xa08
-  __DATA.__objc_selrefs: 0x418
+  __DATA.__objc_selrefs: 0x420
   __DATA.__objc_ivar: 0xc4
   __DATA.__objc_data: 0xf0
   __DATA.__data: 0x180

   - /System/Library/PrivateFrameworks/UARPKit.framework/UARPKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 155
-  Symbols:   120
-  CStrings:  388
+  Functions: 157
+  Symbols:   126
+  CStrings:  392
 
Symbols:
+ __Unwind_Resume
+ ___objc_personality_v0
+ _objc_copyWeak
+ _objc_destroyWeak
+ _objc_initWeak
+ _objc_loadWeakRetained
CStrings:
+ "%s: Allow VID=0x%04x PID=0x%04x"
+ "%s: Ignore VID=0x%04x PID=0x%04x"
+ "%s: VID=0x%04x PID=0x%04x has no serial number is ioreg ?!?"
+ "%s: entry has nil serial number ?! %@"
+ "%s: known entry matching dict %@"
+ "removeObjectsInArray:"
+ "weak self was nil"
- "%s: Allow PID=0x%04x PID=0x%04x"
- "%s: Ignore PID=0x%04x PID=0x%04x"
- "%s: known entrey matching dict %@"
```
