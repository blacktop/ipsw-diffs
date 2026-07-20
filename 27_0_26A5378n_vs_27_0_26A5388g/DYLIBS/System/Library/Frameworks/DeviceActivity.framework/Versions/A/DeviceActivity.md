## DeviceActivity

> `/System/Library/Frameworks/DeviceActivity.framework/Versions/A/DeviceActivity`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift_as_ret`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`

```diff

-405.0.0.0.0
+406.0.0.0.0
   __TEXT.__text: 0x93ef0
   __TEXT.__objc_methlist: 0x490
   __TEXT.__const: 0x38b8

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x110
+  __DATA_CONST.__const: 0x118
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8

   __AUTH_CONST.__cfstring: 0x40
   __AUTH_CONST.__objc_const: 0xbd8
   __AUTH_CONST.__auth_got: 0xb90
-  __AUTH.__objc_data: 0x280
-  __AUTH.__data: 0x6e8
-  __DATA.__data: 0x8d0
-  __DATA.__bss: 0x4080
-  __DATA.__common: 0x30
-  __DATA_DIRTY.__objc_data: 0xd0
-  __DATA_DIRTY.__data: 0xe80
-  __DATA_DIRTY.__bss: 0x1400
-  __DATA_DIRTY.__common: 0x80
+  __AUTH.__objc_data: 0x120
+  __AUTH.__data: 0x600
+  __DATA.__data: 0x868
+  __DATA.__bss: 0x4000
+  __DATA.__common: 0x18
+  __DATA_DIRTY.__objc_data: 0x230
+  __DATA_DIRTY.__data: 0xfd8
+  __DATA_DIRTY.__bss: 0x1480
+  __DATA_DIRTY.__common: 0x98
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 2408
-  Symbols:   922
+  Symbols:   924
   CStrings:  177
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreAudio
+ __swift_FORCE_LOAD_$_swiftCoreAudio_$_DeviceActivity
```
