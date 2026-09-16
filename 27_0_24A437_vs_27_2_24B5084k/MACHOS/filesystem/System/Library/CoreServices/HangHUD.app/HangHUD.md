## HangHUD

> `/System/Library/CoreServices/HangHUD.app/HangHUD`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-426.0.0.0.0
-  __TEXT.__text: 0x30518
-  __TEXT.__auth_stubs: 0xc70
-  __TEXT.__objc_stubs: 0x5c80
+430.0.0.0.0
+  __TEXT.__text: 0x3094c
+  __TEXT.__auth_stubs: 0xc90
+  __TEXT.__objc_stubs: 0x5c60
   __TEXT.__objc_methlist: 0x33dc
-  __TEXT.__const: 0x510
-  __TEXT.__gcc_except_tab: 0x41c
-  __TEXT.__objc_methname: 0xa928
+  __TEXT.__const: 0x4e0
+  __TEXT.__gcc_except_tab: 0x43c
+  __TEXT.__objc_methname: 0xa91a
   __TEXT.__cstring: 0x3930
   __TEXT.__objc_classname: 0x46d
-  __TEXT.__objc_methtype: 0x1a3e
-  __TEXT.__oslogstring: 0x51f3
-  __TEXT.__unwind_info: 0x1220
-  __DATA_CONST.__const: 0x1c70
+  __TEXT.__objc_methtype: 0x1a2f
+  __TEXT.__oslogstring: 0x5309
+  __TEXT.__unwind_info: 0x1240
+  __DATA_CONST.__const: 0x1c98
   __DATA_CONST.__cfstring: 0x5300
   __DATA_CONST.__objc_classlist: 0x178
   __DATA_CONST.__objc_protolist: 0x68

   __DATA_CONST.__objc_doubleobj: 0x20
   __DATA_CONST.__objc_arraydata: 0x180
   __DATA_CONST.__objc_arrayobj: 0x60
-  __DATA_CONST.__auth_got: 0x648
+  __DATA_CONST.__auth_got: 0x658
   __DATA_CONST.__got: 0x308
-  __DATA.__objc_const: 0x6c10
-  __DATA.__objc_selrefs: 0x21a8
+  __DATA.__objc_const: 0x6c08
+  __DATA.__objc_selrefs: 0x21a0
   __DATA.__objc_ivar: 0x63c
   __DATA.__objc_data: 0xeb0
   __DATA.__data: 0x518

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1558
-  Symbols:   303
-  CStrings:  3127
+  Functions: 1563
+  Symbols:   305
+  CStrings:  3130
 
Symbols:
+ _CFAutorelease
+ _objc_retainAutoreleasedReturnValue
CStrings:
+ "Display:%@ has no available modes (%lu modes total), dropping from display array: %@"
+ "Enumerating display:%@ of type:%ld"
+ "Failed to create a HUDContext for displayId=%u"
+ "Ignoring non-approved display:%@ due to type:%ld"
+ "Refusing to create a HUDContext with no display to render to."
+ "allTaskingPrefNames"
- "B32@0:8Q16^@24"
- "mainDisplay"
- "setCLPCTrialID:error:"
```
