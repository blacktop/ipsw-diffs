## PowerUIAgent

> `/usr/libexec/PowerUIAgent`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`

```diff

-753.0.15.0.0
-  __TEXT.__text: 0x828
+753.0.17.0.0
+  __TEXT.__text: 0x858
   __TEXT.__auth_stubs: 0x240
-  __TEXT.__objc_stubs: 0x260
+  __TEXT.__objc_stubs: 0x280
   __TEXT.__const: 0x10
   __TEXT.__cstring: 0x211
   __TEXT.__oslogstring: 0x7c
-  __TEXT.__objc_methname: 0x173
+  __TEXT.__objc_methname: 0x193
   __TEXT.__unwind_info: 0x78
   __DATA_CONST.__const: 0xd0
   __DATA_CONST.__cfstring: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__auth_got: 0x128
-  __DATA_CONST.__got: 0x90
-  __DATA.__objc_selrefs: 0x98
+  __DATA_CONST.__got: 0x98
+  __DATA.__objc_selrefs: 0xa0
   __DATA.__bss: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 6
-  Symbols:   59
-  CStrings:  43
+  Symbols:   60
+  CStrings:  44
 
Symbols:
+ _kIBLMUnusualDrainNotification
Functions:
~ sub_100000b38 : 380 -> 428
CStrings:
+ "displayUnusualDrainNotification"
```
