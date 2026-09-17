## Vermillion

> `/System/Library/ExtensionKit/Extensions/Vermillion.appex/Contents/MacOS/Vermillion`

### Sections with Same Size but Changed Content

- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_mpenum`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`

```diff

-42.0.0.0.0
-  __TEXT.__text: 0x1014c
-  __TEXT.__auth_stubs: 0xe20
-  __TEXT.__objc_stubs: 0x2e0
-  __TEXT.__const: 0xe92
-  __TEXT.__swift5_typeref: 0x37f
+44.0.0.0.0
+  __TEXT.__text: 0x101b8
+  __TEXT.__auth_stubs: 0xdf0
+  __TEXT.__objc_stubs: 0x2c0
+  __TEXT.__const: 0xe90
+  __TEXT.__swift5_typeref: 0x38b
   __TEXT.__oslogstring: 0x15a
   __TEXT.__constg_swiftt: 0x288
   __TEXT.__swift5_builtin: 0x28

   __TEXT.__swift_as_ret: 0x6c
   __TEXT.__swift_as_cont: 0x74
   __TEXT.__objc_classname: 0x53
-  __TEXT.__objc_methname: 0x28f
-  __TEXT.__objc_methtype: 0x60
-  __TEXT.__cstring: 0x1a0
+  __TEXT.__objc_methname: 0x25c
+  __TEXT.__objc_methtype: 0x24
+  __TEXT.__cstring: 0x170
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__swift5_capture: 0x10
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x5f0
-  __TEXT.__eh_frame: 0xcf0
-  __DATA_CONST.__const: 0x799
+  __TEXT.__unwind_info: 0x5e0
+  __TEXT.__eh_frame: 0xd18
+  __DATA_CONST.__const: 0x741
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x718
+  __DATA_CONST.__auth_got: 0x700
   __DATA_CONST.__got: 0x1e0
-  __DATA_CONST.__auth_ptr: 0x360
+  __DATA_CONST.__auth_ptr: 0x370
   __DATA.__objc_const: 0x1f0
-  __DATA.__objc_selrefs: 0xb8
-  __DATA.__data: 0x4a0
+  __DATA.__objc_selrefs: 0xb0
+  __DATA.__data: 0x498
   __DATA.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/ExtensionFoundation.framework/Versions/A/ExtensionFoundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
-  - /usr/lib/swift/libswiftAppleArchive.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 319
-  Symbols:   115
-  CStrings:  59
+  Functions: 315
+  Symbols:   111
+  CStrings:  56
 
Symbols:
+ _swift_arrayInitWithCopy
+ _swift_arrayInitWithTakeBackToFront
+ _swift_arrayInitWithTakeFrontToBack
- _OBJC_CLASS_$_HKSampleQuery
- __objc_autoreleasePoolPop
- __objc_autoreleasePoolPush
- __swift_FORCE_LOAD_$_swiftAppleArchive
- _swift_continuation_await
- _swift_continuation_init
- _swift_deallocObject
CStrings:
+ "predicate"
- "executeQuery:"
- "initWithQueryDescriptors:limit:resultsHandler:"
- "querySamples(queryDescriptors:limit:)"
- "v32@?0@\"HKSampleQuery\"8@\"NSArray\"16@\"NSError\"24"
```
