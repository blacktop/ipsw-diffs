## HomeWidgetLockScreen

> `/private/var/staged_system_apps/Home.app/PlugIns/HomeWidgetLockScreen.appex/HomeWidgetLockScreen`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_entry`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-1238.0.0.0.0
+1241.1.7.1.2
   __TEXT.__text: 0x65630
   __TEXT.__auth_stubs: 0x1fd0
   __TEXT.__objc_stubs: 0x500

   __TEXT.__swift5_entry: 0x8
   __TEXT.__unwind_info: 0x13f8
   __TEXT.__eh_frame: 0x29ac
-  __DATA_CONST.__const: 0x10d0
+  __DATA_CONST.__const: 0x10d8
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCallKit.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 1457
-  Symbols:   207
+  Symbols:   208
   CStrings:  372
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCallKit
```
