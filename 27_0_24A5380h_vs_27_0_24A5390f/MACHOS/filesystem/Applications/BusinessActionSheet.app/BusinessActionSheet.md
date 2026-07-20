## BusinessActionSheet

> `/Applications/BusinessActionSheet.app/BusinessActionSheet`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__constg_swiftt`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-3066.100.3.0.0
+3068.100.3.0.0
   __TEXT.__text: 0xd1cc
   __TEXT.__auth_stubs: 0x890
   __TEXT.__objc_stubs: 0x2880

   __TEXT.__swift5_types: 0x8
   __TEXT.__unwind_info: 0x388
   __TEXT.__eh_frame: 0x238
-  __DATA_CONST.__const: 0x620
+  __DATA_CONST.__const: 0x630
   __DATA_CONST.__cfstring: 0x680
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_protolist: 0x30

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
+  - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftMLCompute.dylib
+  - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 320
-  Symbols:   231
+  Symbols:   233
   CStrings:  824
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftCompression
+ __swift_FORCE_LOAD_$_swiftIntents
- __swift_FORCE_LOAD_$_swiftMLCompute
```
