## powerdatad

> `/usr/libexec/powerdatad`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`

```diff

-2043.0.13.502.1
+2043.0.31.0.0
   __TEXT.__text: 0x7588
   __TEXT.__auth_stubs: 0x6d0
   __TEXT.__objc_stubs: 0xfa0
   __TEXT.__objc_methlist: 0x300
   __TEXT.__const: 0x100
-  __TEXT.__cstring: 0x6a9
+  __TEXT.__cstring: 0x6e9
   __TEXT.__oslogstring: 0xfda
   __TEXT.__gcc_except_tab: 0x320
   __TEXT.__objc_methname: 0xd92

   __TEXT.__dlopen_cstrs: 0x5e
   __TEXT.__unwind_info: 0x238
   __DATA_CONST.__const: 0x328
-  __DATA_CONST.__cfstring: 0xa80
+  __DATA_CONST.__cfstring: 0xb40
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x18

   __DATA.__objc_selrefs: 0x468
   __DATA.__objc_ivar: 0x30
   __DATA.__objc_data: 0xf0
-  __DATA.__data: 0x208
+  __DATA.__data: 0x248
   __DATA.__bss: 0x48
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libobjc.A.dylib
   Functions: 163
   Symbols:   153
-  CStrings:  408
+  CStrings:  414
 
CStrings:
+ "M0CPU"
+ "M1CPU"
+ "MACC0_V_T"
+ "MACC1_V_T"
+ "lts.m0cpu.plist"
+ "lts.m1cpu.plist"
```
