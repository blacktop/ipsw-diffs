## visionhwserverd

> `/usr/libexec/visionhwserverd`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__got`
- `__DATA.__objc_selrefs`

```diff

-4.4.10.0.0
-  __TEXT.__text: 0x4d8
-  __TEXT.__auth_stubs: 0x1b0
+4.4.12.0.0
+  __TEXT.__text: 0x5c0
+  __TEXT.__auth_stubs: 0x1a0
   __TEXT.__objc_stubs: 0x40
   __TEXT.__const: 0x30
-  __TEXT.__gcc_except_tab: 0x74
-  __TEXT.__cstring: 0xd4
-  __TEXT.__oslogstring: 0xb8
+  __TEXT.__gcc_except_tab: 0x90
+  __TEXT.__cstring: 0xc5
+  __TEXT.__oslogstring: 0x11a
   __TEXT.__objc_methname: 0x27
   __TEXT.__unwind_info: 0x78
   __DATA_CONST.__const: 0x28
   __DATA_CONST.__cfstring: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0xe8
+  __DATA_CONST.__auth_got: 0xe0
   __DATA_CONST.__got: 0x30
   __DATA.__objc_selrefs: 0x10
   __DATA.__bss: 0x18

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 6
-  Symbols:   38
+  Functions: 7
+  Symbols:   37
   CStrings:  15
 
Symbols:
- __os_feature_enabled_impl
Functions:
~ sub_1000032f8 : 1016 -> 1164
+ sub_100003824
CStrings:
+ "Loading VisionHWAccelerationServices.framework..."
+ "Now launching the VisionHWAccelerationServices XPC service framework"
+ "VisionHWServerStop"
- "AppleCVHWA"
- "VisionHWA XPCService"
- "enable_visionhwserverd"
```
