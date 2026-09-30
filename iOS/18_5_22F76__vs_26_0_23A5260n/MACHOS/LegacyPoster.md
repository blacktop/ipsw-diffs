## LegacyPoster

> `/System/Library/ExtensionKit/Extensions/LegacyPoster.appex/LegacyPoster`

```diff

-228.5.12.0.0
+276.105.0.0.0
   __TEXT.__text: 0x18c4
   __TEXT.__auth_stubs: 0x410
   __TEXT.__objc_stubs: 0x780
-  __TEXT.__objc_methlist: 0x424
+  __TEXT.__objc_methlist: 0x4b4
   __TEXT.__const: 0xc2
-  __TEXT.__objc_methname: 0xde6
+  __TEXT.__objc_methname: 0xfcc
   __TEXT.__cstring: 0xdb
   __TEXT.__oslogstring: 0xa9
   __TEXT.__objc_classname: 0x55
-  __TEXT.__objc_methtype: 0x6c6
+  __TEXT.__objc_methtype: 0x7e9
   __TEXT.__swift5_typeref: 0x59
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constg_swiftt: 0x50

   __DATA_CONST.__auth_got: 0x210
   __DATA_CONST.__got: 0xa8
   __DATA_CONST.__auth_ptr: 0x50
-  __DATA_CONST.__const: 0x198
+  __DATA_CONST.__const: 0x188
   __DATA_CONST.__cfstring: 0xe0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA.__objc_const: 0x438
-  __DATA.__objc_selrefs: 0x3e8
+  __DATA.__objc_const: 0x498
+  __DATA.__objc_selrefs: 0x448
   __DATA.__objc_ivar: 0x14
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x1c0

   - /System/Library/Frameworks/ExtensionKit.framework/ExtensionKit
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UIKit.framework/UIKit
-  - /System/Library/PrivateFrameworks/AppPredictionClient.framework/AppPredictionClient
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/BaseBoardUI.framework/BaseBoardUI
   - /System/Library/PrivateFrameworks/PaperBoardUI.framework/PaperBoardUI
   - /System/Library/PrivateFrameworks/PosterKit.framework/PosterKit
-  - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
+  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
-  - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib

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
-  UUID: E009FDDD-3501-3610-B587-3A2192DA2CFC
+  UUID: 3DA0296B-FADB-3E16-8BD2-4352AE91C252
   Functions: 45
-  Symbols:   105
-  CStrings:  226
+  Symbols:   103
+  CStrings:  246
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCompression
+ __swift_FORCE_LOAD_$_swiftCoreAudio
+ __swift_FORCE_LOAD_$_swiftCoreMedia
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swiftDataDetection
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd
CStrings:
+ "B32@0:8@\"PRRenderer\"16@\"NSUUID\"24"
+ "additionalControlsForEditor:"
+ "editor:didUpdateColors:"
+ "initialColorsForEditor:"
+ "posterDidUpdateWantsMotionEvents:"
+ "renderer:completedSnapshotForHandle:"
+ "renderer:didReceiveTransitionState:"
+ "renderer:failedToSnapshotWithError:handle:"
+ "renderer:shouldAttemptSnapshotForHandle:"
+ "v24@0:8@\"PLKLegibilityEnvironment\"16"
+ "v24@0:8d16"
+ "v32@0:8@\"PREditor\"16@\"NSArray\"24"
+ "v32@0:8@\"PRRenderer\"16@\"NSUUID\"24"
+ "v32@0:8@\"PRRenderer\"16@\"PRRenderingTransitionState\"24"
+ "v40@0:8@\"PRRenderer\"16@\"NSError\"24@\"NSUUID\"32"
+ "v48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
+ "wallpaperDidUpdateAdaptiveTimeHonorsPreferredSalientContentRectangle:"
+ "wallpaperDidUpdatePreferredDeviceMotionUpdateInterval:"
+ "wallpaperDidUpdatePreferredSalientContentRectangle:"
+ "wallpaperLegibilityEnvironmentDidChange:"

```
