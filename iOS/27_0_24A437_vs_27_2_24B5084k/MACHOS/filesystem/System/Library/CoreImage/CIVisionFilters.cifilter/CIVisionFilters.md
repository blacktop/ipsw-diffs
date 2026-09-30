## CIVisionFilters

> `/System/Library/CoreImage/CIVisionFilters.cifilter/CIVisionFilters`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__cstring`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`

```diff

-1667.22.1.0.0
-  __TEXT.__text: 0x1ed8
-  __TEXT.__auth_stubs: 0x450
-  __TEXT.__objc_stubs: 0x460
+1667.40.3.0.0
+  __TEXT.__text: 0x1f5c
+  __TEXT.__auth_stubs: 0x470
+  __TEXT.__objc_stubs: 0x420
   __TEXT.__objc_methlist: 0x148
   __TEXT.__const: 0x20
   __TEXT.__cstring: 0x2ec
-  __TEXT.__gcc_except_tab: 0x1c0
+  __TEXT.__gcc_except_tab: 0x1b0
   __TEXT.__objc_classname: 0x58
-  __TEXT.__objc_methname: 0x431
+  __TEXT.__objc_methname: 0x417
   __TEXT.__objc_methtype: 0xb1
   __TEXT.__oslogstring: 0x39
-  __TEXT.__unwind_info: 0x118
-  __DATA_CONST.__const: 0x68
+  __TEXT.__unwind_info: 0x128
+  __DATA_CONST.__const: 0xc8
   __DATA_CONST.__cfstring: 0x2a0
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_arraydata: 0x50
   __DATA_CONST.__objc_dictobj: 0xc8
   __DATA_CONST.__objc_intobj: 0x30
-  __DATA_CONST.__auth_got: 0x238
+  __DATA_CONST.__auth_got: 0x248
   __DATA_CONST.__got: 0xf8
   __DATA.__objc_const: 0x2f0
-  __DATA.__objc_selrefs: 0x178
+  __DATA.__objc_selrefs: 0x168
   __DATA.__objc_ivar: 0xc
   __DATA.__objc_data: 0x140
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/CoreVideo.framework/CoreVideo
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOSurface.framework/IOSurface
+  - /System/Library/Frameworks/Metal.framework/Metal
   - /System/Library/Frameworks/Vision.framework/Vision
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 37
-  Symbols:   113
-  CStrings:  88
+  Functions: 41
+  Symbols:   115
+  CStrings:  86
 
Symbols:
+ _MTLCreateSystemDefaultDevice
+ _objc_release
CStrings:
- "device"
- "metalCommandBuffer"
```
