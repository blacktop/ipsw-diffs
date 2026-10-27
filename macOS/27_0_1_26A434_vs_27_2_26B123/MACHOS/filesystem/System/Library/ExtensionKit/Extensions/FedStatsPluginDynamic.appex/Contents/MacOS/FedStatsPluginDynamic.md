## FedStatsPluginDynamic

> `/System/Library/ExtensionKit/Extensions/FedStatsPluginDynamic.appex/Contents/MacOS/FedStatsPluginDynamic`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_entry`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`

```diff

-42.0.0.0.0
+47.0.0.0.0
   __TEXT.__text: 0x54c
   __TEXT.__auth_stubs: 0xd0
   __TEXT.__const: 0x10a

   __TEXT.__swift_as_ret: 0xc
   __TEXT.__unwind_info: 0xa0
   __TEXT.__eh_frame: 0x98
-  __DATA_CONST.__const: 0xe8
+  __DATA_CONST.__const: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__auth_got: 0x68
   __DATA_CONST.__got: 0x20

   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
+  - /usr/lib/swift/libswiftCoreMediaIO.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftIntents.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 15
-  Symbols:   36
+  Symbols:   37
   CStrings:  1
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreMediaIO
```
