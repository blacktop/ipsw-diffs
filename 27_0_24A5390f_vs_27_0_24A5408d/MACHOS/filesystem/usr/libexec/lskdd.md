## lskdd

> `/usr/libexec/lskdd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`

```diff

 0.0.0.0.0
-  __TEXT.__text: 0x10b9900
+  __TEXT.__text: 0x10bc304
   __TEXT.__auth_stubs: 0x270
   __TEXT.__objc_stubs: 0x600
   __TEXT.__objc_methlist: 0x100
   __TEXT.__cstring: 0x17a
-  __TEXT.__const: 0x3d3bc0
+  __TEXT.__const: 0x3d3af0
   __TEXT.__gcc_except_tab: 0xf0
   __TEXT.__objc_methname: 0x5b4
   __TEXT.__objc_classname: 0x31
   __TEXT.__objc_methtype: 0x18b
-  __TEXT.__unwind_info: 0xb40
+  __TEXT.__unwind_info: 0xb48
   __TEXT.__eh_frame: 0x1e8
-  __DATA_CONST.__const: 0x50de8
+  __DATA_CONST.__const: 0x50d78
   __DATA_CONST.__cfstring: 0x120
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x8

   __DATA.__objc_selrefs: 0x1c0
   __DATA.__objc_ivar: 0xc
   __DATA.__objc_data: 0x50
-  __DATA.__data: 0x2a38
+  __DATA.__data: 0x2a58
   __DATA.__bss: 0x58
-  __DATA.__common: 0x941bc
+  __DATA.__common: 0x941b4
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
```
