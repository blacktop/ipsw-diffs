## PhotosAppIntentsExtension

> `/System/Library/ExtensionKit/Extensions/PhotosAppIntentsExtension.appex/PhotosAppIntentsExtension`

```diff

-760.6.150.0.0
-  __TEXT.__text: 0x6250
-  __TEXT.__auth_stubs: 0x450
-  __TEXT.__const: 0x5ea
-  __TEXT.__cstring: 0xd94
+800.14.111.0.0
+  __TEXT.__text: 0x697c
+  __TEXT.__auth_stubs: 0x4a0
+  __TEXT.__const: 0x60a
+  __TEXT.__cstring: 0xfa4
   __TEXT.__swift5_typeref: 0x2cc
-  __TEXT.__swift5_reflstr: 0x1b2
+  __TEXT.__swift5_reflstr: 0x1fe
   __TEXT.__swift5_assocty: 0xa8
   __TEXT.__constg_swiftt: 0x88
-  __TEXT.__swift5_fieldmd: 0xe4
+  __TEXT.__swift5_fieldmd: 0xfc
   __TEXT.__swift5_proto: 0x5c
   __TEXT.__swift5_types: 0xc
   __TEXT.__swift_as_entry: 0x8
   __TEXT.__swift_as_ret: 0x4
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x218
+  __TEXT.__unwind_info: 0x228
   __TEXT.__eh_frame: 0x68
-  __DATA_CONST.__auth_got: 0x228
-  __DATA_CONST.__got: 0x70
-  __DATA_CONST.__auth_ptr: 0x370
-  __DATA_CONST.__const: 0x380
+  __DATA_CONST.__auth_got: 0x250
+  __DATA_CONST.__got: 0x78
+  __DATA_CONST.__auth_ptr: 0x378
+  __DATA_CONST.__const: 0x3a0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__data: 0x170
+  __DATA.__data: 0x160
   __DATA.__bss: 0xbb0
   __DATA.__common: 0x50
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit
   - /System/Library/PrivateFrameworks/PhotosUICore.framework/PhotosUICore
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
   - /usr/lib/swift/libswiftMapKit.dylib
   - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftNaturalLanguage.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
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
-  UUID: 574D82D1-4AEA-345E-AA38-795B05D2C93E
-  Functions: 156
-  Symbols:   60
-  CStrings:  66
+  UUID: C7B997B8-3DF3-326A-B747-4C9C12641F9D
+  Functions: 157
+  Symbols:   62
+  CStrings:  74
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftMLCompute
+ __swift_FORCE_LOAD_$_swiftNaturalLanguage
+ __swift_FORCE_LOAD_$_swiftVideoToolbox
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ _swift_arrayDestroy
+ _swift_coroFrameAlloc
+ _swift_deallocClassInstance
+ _swift_setDeallocating
- __swift_FORCE_LOAD_$_swiftDataDetection
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd
CStrings:
+ "PHOTOS_SETTINGS_CONTROL_FOR_CREATING_SPATIAL_PHOTOS_DESCRIPTION"
+ "PHOTOS_SETTINGS_CONTROL_FOR_CREATING_SPATIAL_PHOTOS_TITLE"
+ "PHOTOS_SETTINGS_ENHANCED_VISUAL_SEARCH_DESCRIPTION"
+ "PHOTOS_SETTINGS_ENHANCED_VISUAL_SEARCH_TITLE"
+ "controlForCreatingSpatialPhotos"
+ "enhancedVisualSearch"
+ "settings-navigation://com.apple.Settings.Apps/com.apple.mobileslideshow#AlchemizeButtonEnabledSwitch"
+ "settings-navigation://com.apple.Settings.Apps/com.apple.mobileslideshow#VisualSearchSwitch"

```
