## coreautha

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/coreautha.bundle/Contents/MacOS/coreautha`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_ivar`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2319.0.63.0.0
-  __TEXT.__text: 0x147bc
-  __TEXT.__auth_stubs: 0x530
-  __TEXT.__objc_stubs: 0x38e0
+2319.40.29.0.0
+  __TEXT.__text: 0x14804
+  __TEXT.__auth_stubs: 0x510
+  __TEXT.__objc_stubs: 0x3960
   __TEXT.__objc_methlist: 0x192c
   __TEXT.__const: 0x180
-  __TEXT.__objc_methname: 0x3dad
+  __TEXT.__objc_methname: 0x3df3
   __TEXT.__objc_classname: 0x388
-  __TEXT.__objc_methtype: 0xfc3
+  __TEXT.__objc_methtype: 0xfd2
   __TEXT.__gcc_except_tab: 0x1b0
   __TEXT.__oslogstring: 0x116c
   __TEXT.__cstring: 0x1777

   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x90
   __DATA_CONST.__objc_intobj: 0x120
-  __DATA_CONST.__auth_got: 0x2a8
-  __DATA_CONST.__got: 0x340
+  __DATA_CONST.__auth_got: 0x298
+  __DATA_CONST.__got: 0x348
   __DATA.__objc_const: 0x4b30
-  __DATA.__objc_selrefs: 0x1278
+  __DATA.__objc_selrefs: 0x1298
   __DATA.__objc_ivar: 0x184
   __DATA.__objc_data: 0x780
   __DATA.__data: 0x7e0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 490
-  Symbols:   207
-  CStrings:  1242
+  Symbols:   206
+  CStrings:  1246
 
Symbols:
+ _OBJC_CLASS_$_LACUICallerIcon
- __LAUIAuthenticationIconForPath
- __LAUIAuthenticationIconShouldBeShownForPath
Functions:
~ sub_100007614 : 252 -> 240
~ sub_10000acd4 -> sub_10000acc8 : 220 -> 252
~ sub_10000e258 -> sub_10000e26c : 232 -> 284
CStrings:
+ "iconForPath:"
+ "iconForPath:bundleIdentifier:"
+ "image"
+ "initWithIcon:scaleFactor:"
+ "shouldBeShownForPath:"
+ "v32@0:8@\"LACUIIconConfiguration\"16@\"LACUIIconConfiguration\"24"
- "initWithImage:scaleFactor:"
- "v32@0:8@\"LACUIIconConfiguration\"16@\"NSImage\"24"
```
