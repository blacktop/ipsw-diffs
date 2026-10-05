## bookassetd

> `/System/Library/PrivateFrameworks/BookLibraryCore.framework/Support/bookassetd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2353.0.0.0.0
-  __TEXT.__text: 0xe1054
-  __TEXT.__auth_stubs: 0xdb0
+2354.0.0.0.0
+  __TEXT.__text: 0xe1208
+  __TEXT.__auth_stubs: 0xdc0
   __TEXT.__objc_stubs: 0xd560
   __TEXT.__objc_methlist: 0x6480
   __TEXT.__const: 0xdb00
   __TEXT.__objc_classname: 0xd7b
-  __TEXT.__cstring: 0x3ae1
+  __TEXT.__cstring: 0x3b0a
   __TEXT.__objc_methname: 0x11bd7
-  __TEXT.__oslogstring: 0xc63b
+  __TEXT.__oslogstring: 0xc6ae
   __TEXT.__objc_methtype: 0x31a9
   __TEXT.__gcc_except_tab: 0x1a18
   __TEXT.__dlopen_cstrs: 0x66
   __TEXT.__unwind_info: 0x1ee8
   __TEXT.__eh_frame: 0x48
-  __DATA_CONST.__const: 0x7ea0
+  __DATA_CONST.__const: 0x7ec0
   __DATA_CONST.__cfstring: 0x3ac0
   __DATA_CONST.__objc_classlist: 0x330
   __DATA_CONST.__objc_catlist: 0x48

   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA_CONST.__auth_got: 0x6f0
+  __DATA_CONST.__auth_got: 0x6f8
   __DATA_CONST.__got: 0x918
   __DATA_CONST.__auth_ptr: 0x18
   __DATA.__objc_const: 0xb4d8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2440
-  Symbols:   589
-  CStrings:  4626
+  Functions: 2442
+  Symbols:   590
+  CStrings:  4631
 
Symbols:
+ _sysctlbyname
Functions:
~ sub_1000c29f4 : 240 -> 412
+ sub_1000c2bc8
+ sub_1000e2b48
CStrings:
+ "FairPlay decrypt failed: %d (sample size %u)"
+ "FairPlay decrypt path: %{public}s (kern.hv_vmm_present=%d, status=%d)"
+ "chunks"
+ "kern.hv_vmm_present"
+ "single-sample"
```
