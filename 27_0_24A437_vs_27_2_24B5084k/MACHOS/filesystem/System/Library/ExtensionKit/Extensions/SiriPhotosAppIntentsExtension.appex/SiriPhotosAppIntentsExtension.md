## SiriPhotosAppIntentsExtension

> `/System/Library/ExtensionKit/Extensions/SiriPhotosAppIntentsExtension.appex/SiriPhotosAppIntentsExtension`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_entry`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__data`

```diff

-3600.17.2.0.0
+3605.2.1.0.0
   __TEXT.__text: 0x3f74
   __TEXT.__auth_stubs: 0x4f0
   __TEXT.__const: 0xa70

   __TEXT.__swift5_entry: 0x8
   __TEXT.__unwind_info: 0x2f0
   __TEXT.__eh_frame: 0x228
-  __DATA_CONST.__const: 0x280
+  __DATA_CONST.__const: 0x288
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__auth_got: 0x278
   __DATA_CONST.__got: 0xd8

   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
+  - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 193
-  Symbols:   51
+  Symbols:   52
   CStrings:  21
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreMIDI
```
