## TVAppExtension

> `/System/Library/ExtensionKit/Extensions/TVAppExtension.appex/TVAppExtension`

```diff

-973.50.8.0.0
-  __TEXT.__text: 0x6c68
-  __TEXT.__auth_stubs: 0x8b0
-  __TEXT.__objc_methlist: 0xc4
-  __TEXT.__const: 0x4d0
-  __TEXT.__swift5_entry: 0x8
-  __TEXT.__swift5_typeref: 0x2ca
+1046.0.0.0.7
+  __TEXT.__text: 0x7044
+  __TEXT.__auth_stubs: 0x940
+  __TEXT.__objc_methlist: 0xd8
+  __TEXT.__const: 0x4e8
+  __TEXT.__cstring: 0x3f6
+  __TEXT.__constg_swiftt: 0x428
+  __TEXT.__swift5_typeref: 0x2f7
+  __TEXT.__swift5_reflstr: 0x113
   __TEXT.__swift5_fieldmd: 0x160
-  __TEXT.__constg_swiftt: 0x400
-  __TEXT.__cstring: 0x3d2
-  __TEXT.__swift5_reflstr: 0x117
   __TEXT.__swift5_assocty: 0xb0
-  __TEXT.__swift5_capture: 0x3c
-  __TEXT.__objc_methname: 0x21d
-  __TEXT.__oslogstring: 0x2d3
-  __TEXT.__swift5_protos: 0x8
+  __TEXT.__oslogstring: 0x325
   __TEXT.__swift5_proto: 0x28
   __TEXT.__swift5_types: 0x20
+  __TEXT.__objc_methname: 0x256
+  __TEXT.__swift5_capture: 0x3c
   __TEXT.__swift_as_entry: 0x8
   __TEXT.__swift_as_ret: 0xc
-  __TEXT.__unwind_info: 0x2c0
+  __TEXT.__swift5_entry: 0x8
+  __TEXT.__swift5_protos: 0x8
+  __TEXT.__unwind_info: 0x2e0
   __TEXT.__eh_frame: 0x240
-  __DATA_CONST.__auth_got: 0x458
-  __DATA_CONST.__got: 0xe0
-  __DATA_CONST.__auth_ptr: 0x1d0
-  __DATA_CONST.__const: 0x2a0
+  __DATA_CONST.__auth_got: 0x4a0
+  __DATA_CONST.__got: 0x118
+  __DATA_CONST.__auth_ptr: 0x1c0
+  __DATA_CONST.__const: 0x2b8
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA.__objc_const: 0x378
-  __DATA.__objc_selrefs: 0xf0
-  __DATA.__objc_data: 0x310
+  __DATA.__objc_const: 0x380
+  __DATA.__objc_selrefs: 0x108
+  __DATA.__objc_data: 0x338
   __DATA.__data: 0x448
   __DATA.__common: 0x28
   __DATA.__bss: 0x4a8

   - /System/Library/Frameworks/ExtensionKit.framework/ExtensionKit
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/SwiftUI.framework/SwiftUI
-  - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
+  - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/VideosUI.framework/VideosUI
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftAppleArchive.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
-  - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
+  - /usr/lib/swift/libswiftMLCompute.dylib
+  - /usr/lib/swift/libswiftMapKit.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftMetalKit.dylib
   - /usr/lib/swift/libswiftModelIO.dylib

   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
+  - /usr/lib/swift/libswiftVideoToolbox.dylib
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
-  UUID: 9C6FD82E-94DC-31CD-9C38-E3FF64295E06
-  Functions: 178
-  Symbols:   133
-  CStrings:  79
+  UUID: 98BFDBBB-07D2-3C0D-B68F-161B01616641
+  Functions: 187
+  Symbols:   132
+  CStrings:  85
 
Symbols:
+ _VUITVAppExtensionDidPlayTrailerNotification
+ _VUITVAppExtensionTrailerPlayablesKey
+ __swiftImmortalRefCount
+ __swift_FORCE_LOAD_$_swiftAppleArchive
+ __swift_FORCE_LOAD_$_swiftMLCompute
+ __swift_FORCE_LOAD_$_swiftMapKit
+ __swift_FORCE_LOAD_$_swiftVideoToolbox
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swiftCryptoTokenKit
- __swift_FORCE_LOAD_$_swiftDataDetection
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd
- _objc_release_x27
- _objc_retain_x3
CStrings:
+ "Notification did not contain playables"
+ "Proxy did play trailer"
+ "playTrailer:"
+ "playTrailerWithPlayableData:"
+ "serializedData"
+ "v24@0:8@\"NSData\"16"

```
