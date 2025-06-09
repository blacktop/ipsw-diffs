## countryd

> `/usr/libexec/countryd`

```diff

-61.0.1.0.0
-  __TEXT.__text: 0xc414
-  __TEXT.__auth_stubs: 0x9f0
-  __TEXT.__objc_stubs: 0x860
+63.0.0.0.0
+  __TEXT.__text: 0xc5bc
+  __TEXT.__auth_stubs: 0xa10
+  __TEXT.__objc_stubs: 0x880
   __TEXT.__objc_methlist: 0x4dc
-  __TEXT.__const: 0x110
+  __TEXT.__const: 0x180
   __TEXT.__cstring: 0x4b4
-  __TEXT.__objc_methname: 0xa3a
+  __TEXT.__objc_methname: 0xa51
   __TEXT.__swift5_typeref: 0x234
-  __TEXT.__oslogstring: 0x10a8
+  __TEXT.__oslogstring: 0x1151
   __TEXT.__constg_swiftt: 0xe8
   __TEXT.__swift5_fieldmd: 0x50
   __TEXT.__swift5_reflstr: 0x2b

   __TEXT.__gcc_except_tab: 0x40
   __TEXT.__objc_classname: 0x9c
   __TEXT.__objc_methtype: 0x2e2
-  __TEXT.__unwind_info: 0x328
-  __TEXT.__eh_frame: 0x550
-  __DATA_CONST.__auth_got: 0x508
-  __DATA_CONST.__got: 0x1e0
+  __TEXT.__unwind_info: 0x330
+  __TEXT.__eh_frame: 0x520
+  __DATA_CONST.__auth_got: 0x518
+  __DATA_CONST.__got: 0x1e8
   __DATA_CONST.__auth_ptr: 0x80
-  __DATA_CONST.__const: 0x368
+  __DATA_CONST.__const: 0x388
   __DATA_CONST.__cfstring: 0x1a0
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x30

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA.__objc_const: 0x768
-  __DATA.__objc_selrefs: 0x3a0
+  __DATA.__objc_selrefs: 0x3a8
   __DATA.__objc_ivar: 0x1c
   __DATA.__objc_data: 0x338
-  __DATA.__data: 0x460
+  __DATA.__data: 0x3f0
   __DATA.__bss: 0x28
   __DATA.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: C170BDE9-B91F-3CDC-AD52-60CF119F4DAB
-  Functions: 193
-  Symbols:   161
-  CStrings:  294
+  UUID: 47D66206-BFC5-3D04-B8A5-B24731A7C077
+  Functions: 194
+  Symbols:   162
+  CStrings:  297
 
Symbols:
+ __swiftImmortalRefCount
+ __swift_FORCE_LOAD_$_swiftCompression
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftOSLog
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ _kRDPriorityGEOIP
+ _swift_release_n
- __mh_execute_header
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd
CStrings:
+ "setCountriesFromGeoIP:"
+ "{\"msg%{public}.0s\":\"Geo IP update\", \"countryCode\":%{public, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"Geo IP update\", \"countryCodes\":%{public, location:escape_only}@}"

```
