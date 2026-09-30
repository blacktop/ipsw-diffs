## AppleAccountRUIHooks

> `/System/Library/RemoteUI/Plugins/AppleAccountRUIHooks.bundle/Contents/MacOS/AppleAccountRUIHooks`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-583.0.0.0.0
+584.0.0.0.0
   __TEXT.__text: 0x2afd8
   __TEXT.__auth_stubs: 0x980
   __TEXT.__objc_stubs: 0xf00

   __TEXT.__swift5_assocty: 0x60
   __TEXT.__unwind_info: 0xa98
   __TEXT.__eh_frame: 0x2398
-  __DATA_CONST.__const: 0x1020
+  __DATA_CONST.__const: 0x1028
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
+  - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftIntents.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 668
-  Symbols:   141
+  Symbols:   142
   CStrings:  337
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreMIDI
```
