## ScreenshotServicesSettings

> `/System/Library/PreferenceBundles/ScreenshotServicesSettings.bundle/ScreenshotServicesSettings`

```diff

-417.4.4.0.0
-  __TEXT.__text: 0x7df8
-  __TEXT.__auth_stubs: 0x940
+437.100.0.0.0
+  __TEXT.__text: 0xa2b4
+  __TEXT.__auth_stubs: 0xc30
   __TEXT.__objc_stubs: 0x100
   __TEXT.__objc_methlist: 0x2c
-  __TEXT.__const: 0x8a8
-  __TEXT.__objc_classname: 0xe6
-  __TEXT.__objc_methname: 0x17b
-  __TEXT.__objc_methtype: 0x14
-  __TEXT.__constg_swiftt: 0x34c
-  __TEXT.__swift5_typeref: 0x546
-  __TEXT.__swift5_fieldmd: 0x134
-  __TEXT.__swift5_types: 0x20
-  __TEXT.__cstring: 0x3e5
-  __TEXT.__swift5_reflstr: 0x165
-  __TEXT.__swift5_assocty: 0x78
-  __TEXT.__swift5_capture: 0x64
-  __TEXT.__swift5_proto: 0x1c
+  __TEXT.__const: 0xb20
+  __TEXT.__cstring: 0x3c5
+  __TEXT.__swift5_typeref: 0x76e
+  __TEXT.__swift5_capture: 0x74
+  __TEXT.__objc_methtype: 0x28
+  __TEXT.__oslogstring: 0x22e
+  __TEXT.__swift5_reflstr: 0x1c5
+  __TEXT.__swift5_assocty: 0xa8
+  __TEXT.__objc_classname: 0x126
+  __TEXT.__constg_swiftt: 0x3f0
+  __TEXT.__swift5_fieldmd: 0x188
+  __TEXT.__swift5_proto: 0x34
+  __TEXT.__swift5_types: 0x2c
+  __TEXT.__objc_methname: 0x18b
   __TEXT.__swift_as_entry: 0xc
-  __TEXT.__oslogstring: 0x160
+  __TEXT.__swift_as_cont: 0x8
   __TEXT.__swift_as_ret: 0x4
-  __TEXT.__unwind_info: 0x2d0
-  __TEXT.__eh_frame: 0x190
-  __DATA_CONST.__auth_got: 0x4a8
-  __DATA_CONST.__got: 0x128
-  __DATA_CONST.__auth_ptr: 0x230
-  __DATA_CONST.__const: 0x278
-  __DATA_CONST.__objc_classlist: 0x18
+  __TEXT.__unwind_info: 0x360
+  __TEXT.__eh_frame: 0x168
+  __DATA_CONST.__const: 0x4e8
+  __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x208
+  __DATA_CONST.__auth_got: 0x620
+  __DATA_CONST.__got: 0x190
+  __DATA_CONST.__auth_ptr: 0x2d0
+  __DATA.__objc_const: 0x2b8
   __DATA.__objc_selrefs: 0x58
   __DATA.__objc_data: 0x100
-  __DATA.__data: 0x4f8
+  __DATA.__data: 0x670
+  __DATA.__bss: 0x7f0
   __DATA.__common: 0x8
-  __DATA.__bss: 0x4b0
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/DeveloperToolsSupport.framework/DeveloperToolsSupport
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/SwiftUI.framework/SwiftUI
   - /System/Library/Frameworks/UIKit.framework/UIKit
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/Preferences.framework/Preferences
   - /System/Library/PrivateFrameworks/ScreenshotServices.framework/ScreenshotServices
   - /System/Library/PrivateFrameworks/Settings.framework/Settings

   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
-  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F7F80509-6606-3E4E-A93A-718916967DC5
-  Functions: 200
-  Symbols:   121
-  CStrings:  48
+  UUID: A3C08AB3-6C18-362C-BBE3-04FC9E153A51
+  Functions: 270
+  Symbols:   157
+  CStrings:  55
 
Symbols:
+ _AnalyticsSendEventLazy
+ _OBJC_CLASS_$_NSString
+ __Block_copy
+ __Block_release
+ __NSConcreteStackBlock
+ __SSEnableHighQualityCapture
+ __SSHighQualityCaptureEnabled
+ __swiftEmptyDictionarySingleton
+ __swiftImmortalRefCount
+ _malloc_size
+ _memcpy
+ _memmove
+ _objc_autoreleaseReturnValue
+ _objc_release_x20
+ _objc_release_x9
+ _objc_retain
+ _objc_retain_x23
+ _objc_retain_x24
+ _swift_arrayDestroy
+ _swift_initStackObject
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_release_n
+ _swift_release_x1
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x23
+ _swift_release_x24
+ _swift_release_x25
+ _swift_release_x8
+ _swift_retain_n
+ _swift_retain_x19
+ _swift_retain_x2
+ _swift_retain_x20
+ _swift_retain_x22
+ _swift_retain_x23
+ _swift_retain_x24
+ _swift_retain_x25
+ _swift_setDeallocating
- __swift_FORCE_LOAD_$_swiftCoreMedia
- _objc_release_x26
- _objc_retain_x19
- _objc_retain_x22
CStrings:
+ "@\"NSDictionary\"8@?0"
+ "Accessing Environment<%s>'s value outside of being installed on a View. This will always read the default value and will not update."
+ "High Quality Screen Capture"
+ "Reporting Engagement Event: %s"
+ "UserInteractionEnabledSetting"
+ "_TtC26ScreenshotServicesSettings22CoreAnalyticsReporting"
+ "_highQualityEnabled"
+ "com.apple.screenshotservices.engagement"
+ "update settings, fullScreenPreviewEnabled: %{bool}d, hdrEnabled: %{bool}d, visualLookUpEnabled: %{bool}d, viSupported: %{bool}d, highQualityEnabled: %{bool}d"
- "Accessing Environment's value outside of being installed on a View. This will always read the default value and will not update."
- "update settings, fullScreenPreviewEnabled: %{bool}d, hdrEnabled: %{bool}d, visualLookUpEnabled: %{bool}d, viSupported: %{bool}d"

```
