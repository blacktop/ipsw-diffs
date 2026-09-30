## mobile_obliterator

> `/usr/libexec/mobile_obliterator`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`

```diff

 402.0.0.0.0
-  __TEXT.__text: 0x1b76c
+  __TEXT.__text: 0x1ba48
   __TEXT.__auth_stubs: 0x1540
   __TEXT.__objc_stubs: 0x920
   __TEXT.__objc_methlist: 0x1fc
-  __TEXT.__cstring: 0xad42
-  __TEXT.__const: 0x6f8
+  __TEXT.__cstring: 0xadf4
+  __TEXT.__const: 0x708
   __TEXT.__gcc_except_tab: 0x144
   __TEXT.__objc_methname: 0x809
   __TEXT.__objc_classname: 0x5b
   __TEXT.__objc_methtype: 0x159
-  __TEXT.__unwind_info: 0x408
+  __TEXT.__unwind_info: 0x420
   __DATA_CONST.__const: 0x678
   __DATA_CONST.__cfstring: 0x2140
   __DATA_CONST.__objc_classlist: 0x18

   __DATA.__objc_selrefs: 0x308
   __DATA.__objc_ivar: 0x8
   __DATA.__objc_data: 0xf0
-  __DATA.__data: 0x250
+  __DATA.__data: 0x248
   __DATA.__common: 0x200
-  __DATA.__bss: 0x2a30
+  __DATA.__bss: 0x2a48
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 276
+  Functions: 277
   Symbols:   402
-  CStrings:  1407
+  CStrings:  1411
 
CStrings:
+ "%s: Got a non-CFData return value from IORegistryEntryCreateCFProperty for property %s\n"
+ "Will use display %s (ctx %d)\n"
+ "aux image path set: %s\n"
+ "ctx[%d] rotation: %d\n"
+ "display-boot-rotation (MG) = %d\n"
+ "ramrod_copy_value_from_IONode"
- "Will use display %s\n"
- "display-boot-rotation = %d\n"
```
