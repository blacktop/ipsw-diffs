## CVMServer

> `/System/Library/Frameworks/OpenGL.framework/Versions/Current/Libraries/CVMServer`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`

```diff

-404.0.0.0.0
-  __TEXT.__text: 0x7980
+405.0.0.0.0
+  __TEXT.__text: 0x7958
   __TEXT.__auth_stubs: 0x910
   __TEXT.__const: 0xa0
   __TEXT.__cstring: 0x963

   __DATA_CONST.__auth_got: 0x488
   __DATA_CONST.__got: 0x80
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__data: 0x80
+  __DATA.__data: 0x78
   __DATA.__bss: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   Functions: 83
-  Symbols:   246
+  Symbols:   245
   CStrings:  135
 
Symbols:
- get_xprr_version.cached_xprr_version
Functions:
~ _heap_alloc : 528 -> 512
~ _cvmsAllocInitServerThread : 708 -> 696
~ _cvmsServerElementBuild : 2816 -> 2804
```
