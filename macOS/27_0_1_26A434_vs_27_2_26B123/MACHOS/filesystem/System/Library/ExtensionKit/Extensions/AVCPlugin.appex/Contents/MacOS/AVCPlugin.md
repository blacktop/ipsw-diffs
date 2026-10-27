## AVCPlugin

> `/System/Library/ExtensionKit/Extensions/AVCPlugin.appex/Contents/MacOS/AVCPlugin`

### Sections with Same Size but Changed Content

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

-42.0.0.0.0
-  __TEXT.__text: 0x14a20
-  __TEXT.__auth_stubs: 0xfb0
+47.0.0.0.0
+  __TEXT.__text: 0x14ae4
+  __TEXT.__auth_stubs: 0xfc0
   __TEXT.__objc_stubs: 0x1e0
   __TEXT.__const: 0xe28
   __TEXT.__objc_classname: 0x41

   __TEXT.__swift5_entry: 0x8
   __TEXT.__unwind_info: 0x708
   __TEXT.__eh_frame: 0xee0
-  __DATA_CONST.__const: 0x9b8
+  __DATA_CONST.__const: 0x9c0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x7e0
-  __DATA_CONST.__got: 0x248
+  __DATA_CONST.__auth_got: 0x7e8
+  __DATA_CONST.__got: 0x250
   __DATA_CONST.__auth_ptr: 0x310
   __DATA.__objc_const: 0x168
   __DATA.__objc_selrefs: 0x78

   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
+  - /usr/lib/swift/libswiftCoreMediaIO.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftIntents.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 394
-  Symbols:   119
+  Symbols:   120
   CStrings:  50
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreMediaIO
Functions:
~ sub_10001261c -> sub_100012664 : 352 -> 424
~ sub_10001277c -> sub_10001280c : 1328 -> 1432
~ sub_100012d5c -> sub_100012e54 : 244 -> 256
~ sub_100014060 -> sub_100014164 : 660 -> 656
~ sub_1000150d8 -> sub_1000151d8 : 280 -> 292
```
