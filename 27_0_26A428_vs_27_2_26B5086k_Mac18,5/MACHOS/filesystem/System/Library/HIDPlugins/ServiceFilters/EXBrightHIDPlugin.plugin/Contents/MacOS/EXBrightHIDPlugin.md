## EXBrightHIDPlugin

> `/System/Library/HIDPlugins/ServiceFilters/EXBrightHIDPlugin.plugin/Contents/MacOS/EXBrightHIDPlugin`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2300.1.2.0.0
-  __TEXT.__text: 0x2864
-  __TEXT.__auth_stubs: 0x4e0
+2300.40.37.0.0
+  __TEXT.__text: 0x2924
+  __TEXT.__auth_stubs: 0x4f0
   __TEXT.__objc_stubs: 0x140
   __TEXT.__objc_methlist: 0x28c
   __TEXT.__const: 0xba
   __TEXT.__objc_methname: 0x3ad
-  __TEXT.__cstring: 0x1d1
-  __TEXT.__oslogstring: 0x5ae
+  __TEXT.__cstring: 0x1e1
+  __TEXT.__oslogstring: 0x60e
   __TEXT.__objc_classname: 0x4c
   __TEXT.__objc_methtype: 0x359
   __TEXT.__swift5_typeref: 0x2e

   __DATA_CONST.__objc_arraydata: 0x50
   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA_CONST.__auth_got: 0x278
+  __DATA_CONST.__auth_got: 0x280
   __DATA_CONST.__got: 0x60
   __DATA_CONST.__auth_ptr: 0x18
   __DATA.__objc_const: 0x3b8

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 61
-  Symbols:   88
-  CStrings:  155
+  Functions: 63
+  Symbols:   89
+  CStrings:  157
 
Symbols:
+ _sysctlbyname
CStrings:
+ "[EXBright] Required support is not available (ret=%d, stage=%u)! Plugin will not be initialized."
+ "kern.exclaves_boot_stage"
```
