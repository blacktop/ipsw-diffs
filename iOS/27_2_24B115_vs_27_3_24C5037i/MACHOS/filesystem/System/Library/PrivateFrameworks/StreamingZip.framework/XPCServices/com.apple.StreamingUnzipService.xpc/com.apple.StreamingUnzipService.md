## com.apple.StreamingUnzipService

> `/System/Library/PrivateFrameworks/StreamingZip.framework/XPCServices/com.apple.StreamingUnzipService.xpc/com.apple.StreamingUnzipService`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-260.0.0.0.0
-  __TEXT.__text: 0x154b8
+262.0.0.0.0
+  __TEXT.__text: 0x154a4
   __TEXT.__auth_stubs: 0xae0
   __TEXT.__objc_stubs: 0x2240
   __TEXT.__objc_methlist: 0xeec
   __TEXT.__const: 0x190
   __TEXT.__gcc_except_tab: 0x3c
-  __TEXT.__cstring: 0x3005
-  __TEXT.__oslogstring: 0x37fe
   __TEXT.__objc_classname: 0x1f1
+  __TEXT.__cstring: 0x2ffc
+  __TEXT.__oslogstring: 0x37fe
   __TEXT.__objc_methname: 0x2e8b
   __TEXT.__objc_methtype: 0xcb3
   __TEXT.__unwind_info: 0x338

   __DATA.__data: 0x370
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/Security.framework/Security
   - /usr/lib/libAppleArchive.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
Functions:
~ sub_100000ee8 -> sub_100000f40 : 940 -> 920
CStrings:
+ "Unknown Process Name"
- "Unknown Process Name (pid %d)"
```
