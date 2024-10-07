## PrivacyAndSecuritySettings

> `/System/Library/PreferenceBundles/PrivacyAndSecuritySettings.bundle/PrivacyAndSecuritySettings`

```diff

-1203.1.3.0.0
-  __TEXT.__text: 0x492b0
-  __TEXT.__auth_stubs: 0x1ab0
+1203.1.5.0.0
+  __TEXT.__text: 0x47f18
+  __TEXT.__auth_stubs: 0x1bf0
   __TEXT.__objc_methlist: 0x13c
-  __TEXT.__const: 0x2324
-  __TEXT.__constg_swiftt: 0xd0c
-  __TEXT.__swift5_typeref: 0x226c
+  __TEXT.__const: 0x24c4
+  __TEXT.__constg_swiftt: 0xd28
+  __TEXT.__swift5_typeref: 0x2044
   __TEXT.__swift5_builtin: 0x78
-  __TEXT.__swift5_reflstr: 0x1076
-  __TEXT.__swift5_assocty: 0x258
-  __TEXT.__swift5_fieldmd: 0xdcc
-  __TEXT.__swift5_proto: 0x15c
-  __TEXT.__swift5_types: 0xdc
-  __TEXT.__cstring: 0x320a
-  __TEXT.__objc_methname: 0x1042
-  __TEXT.__swift5_capture: 0x614
-  __TEXT.__oslogstring: 0x655
+  __TEXT.__swift5_reflstr: 0x1071
+  __TEXT.__swift5_assocty: 0x288
+  __TEXT.__swift5_fieldmd: 0xdd0
   __TEXT.__swift5_mpenum: 0x54
+  __TEXT.__objc_methname: 0xf9d
+  __TEXT.__swift5_proto: 0x170
+  __TEXT.__swift5_types: 0xe0
+  __TEXT.__cstring: 0x32aa
+  __TEXT.__swift5_protos: 0x14
   __TEXT.__objc_classname: 0x6f
   __TEXT.__objc_methtype: 0x39e
-  __TEXT.__swift5_protos: 0x14
-  __TEXT.__unwind_info: 0xf28
-  __TEXT.__eh_frame: 0xfd0
-  __DATA_CONST.__auth_got: 0xd58
-  __DATA_CONST.__got: 0x730
-  __DATA_CONST.__auth_ptr: 0x9d8
-  __DATA_CONST.__const: 0x2008
-  __DATA_CONST.__objc_classlist: 0xb0
+  __TEXT.__swift5_capture: 0x59c
+  __TEXT.__oslogstring: 0x67d
+  __TEXT.__unwind_info: 0xea8
+  __TEXT.__eh_frame: 0xef0
+  __DATA_CONST.__auth_got: 0xdf8
+  __DATA_CONST.__got: 0x710
+  __DATA_CONST.__auth_ptr: 0xa90
+  __DATA_CONST.__const: 0x1f70
+  __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA.__objc_const: 0x22a0
-  __DATA.__objc_selrefs: 0x3b8
-  __DATA.__objc_data: 0x558
-  __DATA.__data: 0x2010
-  __DATA.__bss: 0x1fd8
+  __DATA.__objc_const: 0x2350
+  __DATA.__objc_selrefs: 0x380
+  __DATA.__objc_data: 0x5a8
+  __DATA.__data: 0x2060
+  __DATA.__bss: 0x2270
   __DATA.__common: 0xb0
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
+  - /System/Library/Frameworks/CoreTransferable.framework/CoreTransferable
   - /System/Library/Frameworks/FileProvider.framework/FileProvider
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/HealthKit.framework/HealthKit

   - /System/Library/Frameworks/SensorKit.framework/SensorKit
   - /System/Library/Frameworks/SwiftUI.framework/SwiftUI
   - /System/Library/Frameworks/UIKit.framework/UIKit
+  - /System/Library/PrivateFrameworks/AppProtection.framework/AppProtection
   - /System/Library/PrivateFrameworks/AppleMobileFileIntegrity.framework/AppleMobileFileIntegrity
   - /System/Library/PrivateFrameworks/CommunicationSafetySettingsUI.framework/CommunicationSafetySettingsUI
   - /System/Library/PrivateFrameworks/DeviceAccess.framework/DeviceAccess

   - /System/Library/PrivateFrameworks/SEService.framework/SEService
   - /System/Library/PrivateFrameworks/Settings.framework/Settings
   - /System/Library/PrivateFrameworks/Settings/PrivacySettingsUI.framework/PrivacySettingsUI
-  - /System/Library/PrivateFrameworks/ShareSheet.framework/ShareSheet
   - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation
   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
+  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1259
-  Symbols:   299
-  CStrings:  552
+  Functions: 1254
+  Symbols:   298
+  CStrings:  548
 
Symbols:
+ _NSTemporaryDirectory
+ _OBJC_CLASS_$_APApplication
+ _OBJC_CLASS_$_APGuard
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit
- _OBJC_CLASS_$_NSDateComponentsFormatter
- _OBJC_CLASS_$_NSFileManager
- _OBJC_CLASS_$_UIActivityViewController
- __swift_stdlib_bridgeErrorToNSError
- _objc_release_x10
CStrings:
+ "$__lazy_storage_$_transparencyReport"
+ "An error occured while evaluating app protection authentication: %!s(MISSING)"
+ "_TtC26PrivacyAndSecuritySettings32AppleIntelligenceReportViewModel"
+ "_presentStopRecordingAlert"
+ "applicationWithBundleIdentifier:"
+ "authenticateForSubject:completion:"
+ "sharedGuard"
- "An error occured while exporting %!s(MISSING) %!@(MISSING)"
- "defaultManager"
- "initWithActivityItems:applicationActivities:"
- "popoverPresentationController"
- "presentViewController:animated:completion:"
- "setAllowedUnits:"
- "setFormattingContext:"
- "setSourceView:"
- "setUnitsStyle:"
- "stringFromTimeInterval:"
- "temporaryDirectory"

```
