## NewsNotificationServiceExtension

> `/private/var/staged_system_apps/News.app/PlugIns/NewsNotificationServiceExtension.appex/NewsNotificationServiceExtension`

```diff

-5681.0.0.0.0
-  __TEXT.__text: 0x19da4
-  __TEXT.__auth_stubs: 0xda0
+5718.1.0.0.0
+  __TEXT.__text: 0x185a0
+  __TEXT.__auth_stubs: 0xd70
   __TEXT.__objc_stubs: 0x11a0
   __TEXT.__objc_methlist: 0x514
   __TEXT.__objc_methname: 0x1850
   __TEXT.__objc_classname: 0x143
   __TEXT.__objc_methtype: 0x3ff
-  __TEXT.__const: 0xb50
+  __TEXT.__const: 0xc30
   __TEXT.__gcc_except_tab: 0x1a4
   __TEXT.__oslogstring: 0xdb3
   __TEXT.__cstring: 0xd87
   __TEXT.__constg_swiftt: 0x320
-  __TEXT.__swift5_typeref: 0x5f3
+  __TEXT.__swift5_typeref: 0x5e9
   __TEXT.__swift5_reflstr: 0x289
   __TEXT.__swift5_fieldmd: 0x4a8
   __TEXT.__swift5_types: 0x44

   __TEXT.__swift_as_ret: 0x40
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__unwind_info: 0x6b8
-  __TEXT.__eh_frame: 0xbd0
-  __DATA_CONST.__auth_got: 0x6e0
+  __TEXT.__eh_frame: 0xc10
+  __DATA_CONST.__auth_got: 0x6c8
   __DATA_CONST.__got: 0x330
-  __DATA_CONST.__auth_ptr: 0x1e0
-  __DATA_CONST.__const: 0xcc8
+  __DATA_CONST.__auth_ptr: 0x1c0
+  __DATA_CONST.__const: 0xcd0
   __DATA_CONST.__cfstring: 0x140
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_protolist: 0x40

   __DATA.__objc_selrefs: 0x660
   __DATA.__objc_ivar: 0x38
   __DATA.__objc_data: 0x580
-  __DATA.__data: 0x858
+  __DATA.__data: 0x780
   __DATA.__bss: 0xf90
   __DATA.__common: 0x58
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /System/Library/PrivateFrameworks/AppAnalytics.framework/AppAnalytics
   - /System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices

   - /System/Library/PrivateFrameworks/NewsServicesInternal.framework/NewsServicesInternal
   - /System/Library/PrivateFrameworks/TeaFoundation.framework/TeaFoundation
   - /System/Library/PrivateFrameworks/TeaSettings.framework/TeaSettings
-  - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftAppleArchive.dylib
+  - /usr/lib/swift/libswiftCallKit.dylib
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
   - /usr/lib/swift/libswiftGLKit.dylib
   - /usr/lib/swift/libswiftGameplayKit.dylib

   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftSpriteKit.dylib
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
-  UUID: CFDECC70-8AC3-33BA-AA18-F356A851E92C
-  Functions: 463
-  Symbols:   286
+  UUID: 5A3C2B23-24A9-3573-8D0B-9FDBD8B35C06
+  Functions: 459
+  Symbols:   278
   CStrings:  442
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCallKit
+ __swift_FORCE_LOAD_$_swiftVideoToolbox
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ _objc_retain_x9
- __swift_FORCE_LOAD_$_swiftCryptoTokenKit
- __swift_FORCE_LOAD_$_swiftDataDetection
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd
- _free
- _malloc
- _swift_bridgeObjectRelease_n
- _swift_initStackObject
- _swift_release_n

```
