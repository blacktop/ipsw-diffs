## PFLASLArcadeRetention

> `/System/Library/ExtensionKit/Extensions/PFLASLArcadeRetention.appex/PFLASLArcadeRetention`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_entry`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-1.5.4.0.0
+1.5.6.0.0
   __TEXT.__text: 0x22910
   __TEXT.__auth_stubs: 0x890
   __TEXT.__objc_stubs: 0x1b80

   __TEXT.__swift5_assocty: 0x18
   __TEXT.__unwind_info: 0x2e0
   __TEXT.__eh_frame: 0x268
-  __DATA_CONST.__const: 0x110
+  __DATA_CONST.__const: 0x118
   __DATA_CONST.__cfstring: 0x1860
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 211
-  Symbols:   521
+  Symbols:   522
   CStrings:  546
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCompression
```
