## Diagnostic-6004

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6004.appex/Diagnostic-6004`

```diff

-820.82.2.0.0
-  __TEXT.__text: 0x13518
-  __TEXT.__auth_stubs: 0xc60
+820.100.56.0.0
+  __TEXT.__text: 0x12088
+  __TEXT.__auth_stubs: 0xbe0
   __TEXT.__objc_stubs: 0x160
-  __TEXT.__objc_methlist: 0x20c
-  __TEXT.__cstring: 0xfe9
+  __TEXT.__objc_methlist: 0x364
+  __TEXT.__cstring: 0xef9
   __TEXT.__objc_methname: 0x8f6
   __TEXT.__objc_classname: 0x45
   __TEXT.__objc_methtype: 0xce
-  __TEXT.__const: 0x898
-  __TEXT.__swift5_typeref: 0x1510
+  __TEXT.__const: 0x9c8
+  __TEXT.__swift5_typeref: 0x149a
   __TEXT.__constg_swiftt: 0x664
   __TEXT.__swift5_reflstr: 0x5a3
   __TEXT.__swift5_fieldmd: 0x3ac

   __TEXT.__oslogstring: 0x9e
   __TEXT.__swift5_proto: 0x18
   __TEXT.__swift5_types: 0x34
-  __TEXT.__unwind_info: 0x4b0
-  __TEXT.__eh_frame: 0x108
-  __DATA_CONST.__auth_got: 0x638
+  __TEXT.__unwind_info: 0x460
+  __TEXT.__eh_frame: 0x120
+  __DATA_CONST.__auth_got: 0x5f8
   __DATA_CONST.__got: 0x260
-  __DATA_CONST.__auth_ptr: 0x2e0
-  __DATA_CONST.__const: 0xd28
+  __DATA_CONST.__auth_ptr: 0x2d8
+  __DATA_CONST.__const: 0xe00
   __DATA_CONST.__cfstring: 0x20
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA.__objc_const: 0xca0
-  __DATA.__objc_selrefs: 0x300
+  __DATA.__objc_const: 0xa28
+  __DATA.__objc_selrefs: 0x398
   __DATA.__objc_data: 0x6d8
-  __DATA.__data: 0xb28
+  __DATA.__data: 0xae8
   __DATA.__bss: 0x400
   __DATA.__common: 0x30
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 474
+  Functions: 452
   Symbols:   160
-  CStrings:  264
+  CStrings:  258
 
Symbols:
+ _swift_generic_assignWithCopy
+ _swift_generic_assignWithTake
+ _swift_generic_destroy
+ _swift_generic_initWithCopy
+ _swift_generic_initializeBufferWithCopyOfBuffer
- __swift_FORCE_LOAD_$_swiftFileProvider
- _memset
- _objc_retain_x27
- _swift_arrayDestroy
- _swift_initStackObject
CStrings:
- "Can't construct Array with count < 0"
- "Fatal error"
- "Swift/Array.swift"
- "Swift/UnsafePointer.swift"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"

```
