## IOKit

> `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__objc_const`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-100288.0.8.0.0
-  __TEXT.__text: 0xa2818
+100288.0.9.0.0
+  __TEXT.__text: 0xa2880
   __TEXT.__objc_methlist: 0x150
   __TEXT.__const: 0x104bc
   __TEXT.__oslogstring: 0x5630
-  __TEXT.__cstring: 0xbd59
+  __TEXT.__cstring: 0xbd7e
   __TEXT.__unwind_info: 0x2298
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2cc8
+  __DATA_CONST.__const: 0x2ce8
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__got: 0x1e0
-  __AUTH_CONST.__const: 0x1e30
-  __AUTH_CONST.__cfstring: 0x75a0
+  __AUTH_CONST.__const: 0x1e50
+  __AUTH_CONST.__cfstring: 0x75c0
   __AUTH_CONST.__objc_const: 0x508
   __AUTH_CONST.__auth_got: 0x10b8
   __AUTH.__objc_data: 0x190

   __DATA.__common: 0x100
   __DATA_DIRTY.__objc_data: 0xa0
   __DATA_DIRTY.__data: 0xc8
-  __DATA_DIRTY.__bss: 0x240
+  __DATA_DIRTY.__bss: 0x250
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/libenergytrace.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 3572
-  Symbols:   3960
-  CStrings:  2577
+  Functions: 3573
+  Symbols:   3961
+  CStrings:  2578
 
Symbols:
+ ___IOHIDRequestAccess_block_invoke_2
Functions:
~ ___IOHIDRequestAccess_block_invoke : 36 -> 148
+ ___IOHIDRequestAccess_block_invoke_2
~ _IOHIDRequestAccess : 352 -> 320
CStrings:
+ "OSKEXT_BUILD_DATE 21:25:34 Aug  3 2026"
+ "_kTCCAccessRequestOptionSyncCallback"
- "OSKEXT_BUILD_DATE 21:46:15 Jul 10 2026"
```
