## AVCPlugin

> `/System/Library/ExtensionKit/Extensions/AVCPlugin.appex/AVCPlugin`

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
-  __TEXT.__text: 0x147b8
-  __TEXT.__auth_stubs: 0x1170
+44.0.0.0.0
+  __TEXT.__text: 0x14874
+  __TEXT.__auth_stubs: 0x1190
   __TEXT.__objc_stubs: 0x1e0
   __TEXT.__const: 0xe28
   __TEXT.__objc_classname: 0x41

   __TEXT.__swift5_entry: 0x8
   __TEXT.__unwind_info: 0x708
   __TEXT.__eh_frame: 0xee0
-  __DATA_CONST.__const: 0x9b8
+  __DATA_CONST.__const: 0x9b0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x8c0
-  __DATA_CONST.__got: 0x248
+  __DATA_CONST.__auth_got: 0x8d0
+  __DATA_CONST.__got: 0x250
   __DATA_CONST.__auth_ptr: 0x310
   __DATA.__objc_const: 0x168
   __DATA.__objc_selrefs: 0x78

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
-  - /usr/lib/swift/libswiftAppleArchive.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
Symbols:
+ _swift_retain_x27
- __swift_FORCE_LOAD_$_swiftAppleArchive
Functions:
~ sub_100012398 -> sub_100012350 : 352 -> 424
~ sub_1000124f8 : 1316 -> 1420
~ sub_100012acc -> sub_100012b34 : 228 -> 240
```
