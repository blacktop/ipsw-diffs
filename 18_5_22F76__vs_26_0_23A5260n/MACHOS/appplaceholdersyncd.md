## appplaceholdersyncd

> `/System/Library/CoreServices/appplaceholdersyncd`

```diff

-30.1.0.0.0
-  __TEXT.__text: 0x48f4
-  __TEXT.__auth_stubs: 0x7e0
-  __TEXT.__const: 0x17c
+41.0.0.0.0
+  __TEXT.__text: 0x4ff0
+  __TEXT.__auth_stubs: 0x7f0
+  __TEXT.__const: 0x1ac
   __TEXT.__swift5_typeref: 0x8a
-  __TEXT.__oslogstring: 0x320
+  __TEXT.__oslogstring: 0x340
   __TEXT.__swift5_capture: 0x20
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__cstring: 0x31e
   __TEXT.__swift_as_entry: 0x8
   __TEXT.__swift_as_ret: 0x4
+  __TEXT.__cstring: 0x30e
   __TEXT.__constg_swiftt: 0xe0
   __TEXT.__swift5_reflstr: 0x34
   __TEXT.__swift5_fieldmd: 0x60

   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_proto: 0x4
   __TEXT.__swift5_types: 0xc
-  __TEXT.__unwind_info: 0x120
+  __TEXT.__unwind_info: 0x138
   __TEXT.__eh_frame: 0x108
-  __DATA_CONST.__auth_got: 0x3f0
+  __DATA_CONST.__auth_got: 0x3f8
   __DATA_CONST.__got: 0x78
   __DATA_CONST.__auth_ptr: 0x68
-  __DATA_CONST.__const: 0x200
+  __DATA_CONST.__const: 0x268
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x170
   __DATA.__objc_selrefs: 0x20
-  __DATA.__data: 0x210
+  __DATA.__data: 0x1f0
   __DATA.__bss: 0x80
   __DATA.__common: 0x8
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AppPlaceholderSync.framework/AppPlaceholderSync
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAVFoundation.dylib
+  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
+  - /usr/lib/swift/libswiftCoreLocation.dylib
+  - /usr/lib/swift/libswiftCoreMIDI.dylib
+  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib

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
-  UUID: 3537CA94-2E41-3800-BA64-E14EDAF1B1D9
-  Functions: 69
-  Symbols:   186
-  CStrings:  46
+  UUID: AE03FD3F-461B-3B25-B238-EF7B8FC50A2A
+  Functions: 74
+  Symbols:   192
+  CStrings:  45
 
Symbols:
+ _$s18AppPlaceholderSync0C7ManagerC28syncReplicatorWithSubscriberyyFTj
+ _$s18AppPlaceholderSync0C7ManagerC5resetyyFZ
+ _$s18AppPlaceholderSync8DefaultsV11isResettingSbvg
+ _$sSS11utf8CStrings15ContiguousArrayVys4Int8VGvg
+ _$ss11_StringGutsV16_foreignCopyUTF84intoSiSgSrys5UInt8VG_tF
+ _$ss20__StaticArrayStorageCN
+ __swiftImmortalRefCount
+ __swift_FORCE_LOAD_$_swiftAVFoundation
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftCoreAudio
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftCoreLocation
+ __swift_FORCE_LOAD_$_swiftCoreMIDI
+ __swift_FORCE_LOAD_$_swiftCoreMedia
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ _os_eligibility_get_domain_answer
- _$ss11_StringGutsV8copyUTF84intoSiSgSrys5UInt8VG_tF
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd
- _objc_release_x28
- _swift_bridgeObjectRelease_n
- _swift_bridgeObjectRetain_n
- _swift_unknownObjectRetain_n
CStrings:
+ "%s: handle %s: eligible=%{bool}d"
+ "eligibility-changed"
- "Name"
- "UserInfo"
- "bundleIDs"

```
