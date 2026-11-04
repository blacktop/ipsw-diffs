## SiriMessagesAppIntentsExtension

> `/System/Library/ExtensionKit/Extensions/SiriMessagesAppIntentsExtension.appex/SiriMessagesAppIntentsExtension`

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
- `__DATA.__objc_selrefs`

```diff

-3605.21.1.11.2
+3610.11.1.0.0
   __TEXT.__text: 0x684
   __TEXT.__auth_stubs: 0x190
   __TEXT.__objc_stubs: 0x40

   __TEXT.__objc_methname: 0x15
   __TEXT.__unwind_info: 0xd0
   __TEXT.__eh_frame: 0x40
-  __DATA_CONST.__const: 0xe0
+  __DATA_CONST.__const: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__auth_got: 0xd0
   __DATA_CONST.__got: 0x20

   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
+  - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 36
-  Symbols:   39
+  Symbols:   40
   CStrings:  2
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreMIDI
```
