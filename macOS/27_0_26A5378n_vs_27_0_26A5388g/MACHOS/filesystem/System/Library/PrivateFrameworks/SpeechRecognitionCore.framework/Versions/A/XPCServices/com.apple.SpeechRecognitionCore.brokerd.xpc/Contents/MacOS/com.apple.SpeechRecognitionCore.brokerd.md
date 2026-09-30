## com.apple.SpeechRecognitionCore.brokerd

> `/System/Library/PrivateFrameworks/SpeechRecognitionCore.framework/Versions/A/XPCServices/com.apple.SpeechRecognitionCore.brokerd.xpc/Contents/MacOS/com.apple.SpeechRecognitionCore.brokerd`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-38.0.0.0.0
+39.0.0.0.0
   __TEXT.__text: 0x12b14
   __TEXT.__auth_stubs: 0xda0
   __TEXT.__objc_stubs: 0x14c0

   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
   __TEXT.__unwind_info: 0x538
-  __DATA_CONST.__const: 0x9a8
+  __DATA_CONST.__const: 0x9b0
   __DATA_CONST.__cfstring: 0x1060
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_catlist: 0x8

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
+  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 310
-  Symbols:   315
+  Symbols:   316
   CStrings:  566
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftAccelerate
```
