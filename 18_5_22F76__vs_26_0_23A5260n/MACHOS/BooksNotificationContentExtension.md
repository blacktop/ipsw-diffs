## BooksNotificationContentExtension

> `/private/var/staged_system_apps/Books.app/PlugIns/BooksNotificationContentExtension.appex/BooksNotificationContentExtension`

```diff

-6382.0.0.0.0
+6448.11.0.0.0
   __TEXT.__text: 0x2de4
   __TEXT.__auth_stubs: 0x420
   __TEXT.__objc_stubs: 0xda0

   __DATA_CONST.__auth_got: 0x218
   __DATA_CONST.__got: 0x168
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x3b8
+  __DATA_CONST.__const: 0x3a0
   __DATA_CONST.__cfstring: 0x340
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_catlist: 0x8

   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /System/Library/Frameworks/UserNotificationsUI.framework/UserNotificationsUI
   - /System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices

   - /System/Library/PrivateFrameworks/BookDataStore.framework/BookDataStore
   - /System/Library/PrivateFrameworks/BookUtility.framework/BookUtility
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
-  - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
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
+  - /usr/lib/swift/libswiftIntents.dylib
+  - /usr/lib/swift/libswiftMLCompute.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftMetalKit.dylib
   - /usr/lib/swift/libswiftModelIO.dylib

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
   - @rpath/BookAnalytics.framework/BookAnalytics
   - @rpath/BookCore.framework/BookCore
   - @rpath/BookStoreUI.framework/BookStoreUI
   - @rpath/JSApp.framework/JSApp
   - @rpath/TemplateUI.framework/TemplateUI
-  UUID: 7E50E5D4-E17B-303D-842F-77EAE03D7BCD
+  UUID: FB464F2D-EC48-3024-8314-F7FB62E0930A
   Functions: 66
-  Symbols:   172
+  Symbols:   169
   CStrings:  283
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftAppleArchive
+ __swift_FORCE_LOAD_$_swiftIntents
+ __swift_FORCE_LOAD_$_swiftMLCompute
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

```
