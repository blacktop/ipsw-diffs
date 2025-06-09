## diagnosticspushd

> `/usr/libexec/diagnosticspushd`

```diff

-21.0.0.0.0
-  __TEXT.__text: 0x10be0
-  __TEXT.__auth_stubs: 0xc20
+23.0.0.0.0
+  __TEXT.__text: 0xee74
+  __TEXT.__auth_stubs: 0xc50
   __TEXT.__objc_stubs: 0x60
   __TEXT.__objc_methlist: 0x24c
-  __TEXT.__const: 0x1044
-  __TEXT.__oslogstring: 0x47d
+  __TEXT.__const: 0x1064
+  __TEXT.__oslogstring: 0x46d
   __TEXT.__cstring: 0x418
   __TEXT.__objc_methname: 0x549
   __TEXT.__constg_swiftt: 0x3a8
-  __TEXT.__swift5_typeref: 0x377
+  __TEXT.__swift5_typeref: 0x383
   __TEXT.__swift5_reflstr: 0x1bb
   __TEXT.__swift5_fieldmd: 0x3e8
   __TEXT.__swift5_capture: 0xa0

   __TEXT.__swift_as_entry: 0xc
   __TEXT.__swift_as_ret: 0x14
   __TEXT.__unwind_info: 0x510
-  __TEXT.__eh_frame: 0x680
-  __DATA_CONST.__auth_got: 0x618
+  __TEXT.__eh_frame: 0x620
+  __DATA_CONST.__auth_got: 0x630
   __DATA_CONST.__got: 0x1a0
-  __DATA_CONST.__auth_ptr: 0x198
-  __DATA_CONST.__const: 0xec0
+  __DATA_CONST.__auth_ptr: 0x190
+  __DATA_CONST.__const: 0xec8
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA.__objc_const: 0x538
   __DATA.__objc_selrefs: 0x1e0
   __DATA.__objc_data: 0x178
-  __DATA.__data: 0x7a0
+  __DATA.__data: 0x780
   __DATA.__common: 0x98
   __DATA.__bss: 0x1e00
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

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
-  UUID: FF44729A-647E-3B19-B1FF-33C4076F710D
-  Functions: 428
-  Symbols:   323
+  UUID: 36BEE215-C05F-3E93-A92A-D059D66F8B93
+  Functions: 424
+  Symbols:   320
   CStrings:  176
 
Symbols:
+ _$ss10_HashTableV11startBucketAB0D0Vvg
+ _$ss11_StringGutsV16_foreignCopyUTF84intoSiSgSrys5UInt8VG_tF
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ _objc_retain_x24
+ _swift_setDeallocating
- _$ss11_StringGutsV8copyUTF84intoSiSgSrys5UInt8VG_tF
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd
- _swift_bridgeObjectRelease_n
- _swift_bridgeObjectRetain_n
CStrings:
+ "Failed to decode push payload: %{public}@"
- "Failed to decode push payload %{public}s with error: %{public}@"

```
