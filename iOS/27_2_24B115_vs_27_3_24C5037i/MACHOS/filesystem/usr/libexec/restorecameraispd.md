## restorecameraispd

> `/usr/libexec/restorecameraispd`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_selrefs`

```diff

-20.111.0.0.0
-  __TEXT.__text: 0x1d764
+20.203.1.0.0
+  __TEXT.__text: 0x1d760
   __TEXT.__auth_stubs: 0xfb0
   __TEXT.__objc_stubs: 0x4a0
   __TEXT.__const: 0x16e0
-  __TEXT.__cstring: 0x350a
+  __TEXT.__cstring: 0x350c
   __TEXT.__gcc_except_tab: 0x4b4
   __TEXT.__oslogstring: 0x237c
   __TEXT.__objc_methname: 0x32c

   __DATA_CONST.__got: 0x148
   __DATA_CONST.__auth_ptr: 0x20
   __DATA.__objc_selrefs: 0x128
-  __DATA.__data: 0x5acc88
+  __DATA.__data: 0x5ace88
   __DATA.__common: 0x7
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libamsupport.dylib
+  - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
Functions:
~ sub_100000db0 -> sub_100000de8 : 1792 -> 1788
CStrings:
+ "20.203.1"
- "20.111"
```
