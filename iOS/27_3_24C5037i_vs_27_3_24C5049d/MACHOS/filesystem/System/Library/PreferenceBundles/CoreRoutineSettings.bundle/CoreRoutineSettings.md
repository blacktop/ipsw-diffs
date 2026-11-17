## CoreRoutineSettings

> `/System/Library/PreferenceBundles/CoreRoutineSettings.bundle/CoreRoutineSettings`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1123.0.6.0.0
-  __TEXT.__text: 0x11e3c
+1123.0.9.0.0
+  __TEXT.__text: 0x11e78
   __TEXT.__auth_stubs: 0xfc0
   __TEXT.__objc_stubs: 0xf40
   __TEXT.__objc_methlist: 0x514

   __TEXT.__gcc_except_tab: 0xac
   __TEXT.__oslogstring: 0x163
   __TEXT.__unwind_info: 0x578
-  __DATA_CONST.__const: 0xfd0
+  __DATA_CONST.__const: 0xfd8
   __DATA_CONST.__cfstring: 0xb60
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_catlist: 0x10

   - /System/Library/PrivateFrameworks/Preferences.framework/Preferences
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 411
-  Symbols:   287
+  Symbols:   288
   CStrings:  420
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftAccelerate
Functions:
~ sub_89e8 -> sub_8a30 : 1336 -> 1372
~ sub_a028 -> sub_a094 : 1232 -> 1256
```
