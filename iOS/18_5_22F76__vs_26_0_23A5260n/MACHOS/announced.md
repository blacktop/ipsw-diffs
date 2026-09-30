## announced

> `/usr/libexec/announced`

```diff

-248.50.9.0.0
-  __TEXT.__text: 0x101c
+297.0.1.0.0
+  __TEXT.__text: 0x1108
   __TEXT.__auth_stubs: 0x330
   __TEXT.__const: 0x52
   __TEXT.__cstring: 0x39

   __TEXT.__swift5_typeref: 0x3a
   __TEXT.__swift5_entry: 0x8
   __TEXT.__swift5_capture: 0x10
-  __TEXT.__unwind_info: 0xa0
+  __TEXT.__unwind_info: 0xa8
   __DATA_CONST.__auth_got: 0x198
   __DATA_CONST.__got: 0x48
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0x158
+  __DATA_CONST.__const: 0x168
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x38
   __DATA.__data: 0x18
   __DATA.__common: 0x38
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/Announce.framework/Announce
   - /System/Library/PrivateFrameworks/AnnounceDaemon.framework/AnnounceDaemon
   - /System/Library/PrivateFrameworks/DropIn.framework/DropIn
   - /System/Library/PrivateFrameworks/DropInCore.framework/DropInCore
-  - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib

   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
-  - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
+  - /usr/lib/swift/libswiftMLCompute.dylib
+  - /usr/lib/swift/libswiftMapKit.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftNaturalLanguage.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
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
-  UUID: 35E0F7C2-AAA5-35E8-B022-5D12EDA6A5A3
-  Functions: 21
-  Symbols:   99
+  UUID: 06067A04-0D5B-34F7-8620-6BB09BFFBBFE
+  Functions: 22
+  Symbols:   98
   CStrings:  17
 
Symbols:
+ _$ss11_StringGutsV16_foreignCopyUTF84intoSiSgSrys5UInt8VG_tF
+ _$ss20__StaticArrayStorageCN
+ __swiftImmortalRefCount
+ __swift_FORCE_LOAD_$_swiftMLCompute
+ __swift_FORCE_LOAD_$_swiftMapKit
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- _$ss11_StringGutsV8copyUTF84intoSiSgSrys5UInt8VG_tF
- __swift_FORCE_LOAD_$_swiftDataDetection
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd

```
