## CompanionSetup

> `/Applications/CompanionSetup.app/CompanionSetup`

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
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-524.10.88.0.0
-  __TEXT.__text: 0x9d6f8
+524.10.94.0.0
+  __TEXT.__text: 0x9d7f4
   __TEXT.__auth_stubs: 0x27f0
   __TEXT.__objc_stubs: 0x2960
   __TEXT.__objc_methlist: 0x124c

   __TEXT.__swift5_protos: 0x40
   __TEXT.__unwind_info: 0x2580
   __TEXT.__eh_frame: 0x48d0
-  __DATA_CONST.__const: 0x85e0
+  __DATA_CONST.__const: 0x85e8
   __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftAppleArchive.dylib
   - /usr/lib/swift/libswiftCallKit.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - @rpath/AppleConnectClient.framework/AppleConnectClient
   Functions: 2489
-  Symbols:   1269
+  Symbols:   1270
   CStrings:  1411
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftAppleArchive
Functions:
~ sub_10005aea4 -> sub_10005aeec : 1116 -> 1200
~ sub_10005b300 -> sub_10005b39c : 1116 -> 1200
~ sub_10005b75c -> sub_10005b84c : 1116 -> 1200
```
