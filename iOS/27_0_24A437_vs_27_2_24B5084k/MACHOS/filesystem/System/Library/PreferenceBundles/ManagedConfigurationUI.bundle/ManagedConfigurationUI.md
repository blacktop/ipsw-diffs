## ManagedConfigurationUI

> `/System/Library/PreferenceBundles/ManagedConfigurationUI.bundle/ManagedConfigurationUI`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-113.2.5.0.0
+113.40.17.0.0
   __TEXT.__text: 0x48e8
   __TEXT.__auth_stubs: 0x830
   __TEXT.__objc_stubs: 0x160

   __TEXT.__objc_methname: 0xf5
   __TEXT.__unwind_info: 0x1c8
   __TEXT.__eh_frame: 0x168
-  __DATA_CONST.__const: 0x1e8
+  __DATA_CONST.__const: 0x1f0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__auth_got: 0x420

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 83
-  Symbols:   110
+  Symbols:   111
   CStrings:  16
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftAVFoundation
```
