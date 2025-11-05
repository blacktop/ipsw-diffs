## MessagesSettingsUI

> `/System/Library/PrivateFrameworks/MessagesSettingsUI.framework/Versions/A/MessagesSettingsUI`

```diff

-1402.400.131.1.3
-  __TEXT.__text: 0x1a8e8
-  __TEXT.__auth_stubs: 0xf30
-  __TEXT.__objc_methlist: 0x790
-  __TEXT.__const: 0x15c4
-  __TEXT.__cstring: 0x1c47
+1402.500.181.1.1
+  __TEXT.__text: 0x19794
+  __TEXT.__auth_stubs: 0xf00
+  __TEXT.__objc_methlist: 0x8fc
+  __TEXT.__const: 0x1564
+  __TEXT.__cstring: 0x1a07
   __TEXT.__gcc_except_tab: 0x644
   __TEXT.__oslogstring: 0x583
   __TEXT.__dlopen_cstrs: 0x58
   __TEXT.__constg_swiftt: 0xf18
-  __TEXT.__swift5_typeref: 0x25b8
+  __TEXT.__swift5_typeref: 0x25a8
   __TEXT.__swift5_reflstr: 0x825
   __TEXT.__swift5_fieldmd: 0x664
   __TEXT.__swift5_proto: 0xac

   __TEXT.__swift5_assocty: 0x180
   __TEXT.__swift5_capture: 0xac
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x6b0
+  __TEXT.__unwind_info: 0x718
   __TEXT.__eh_frame: 0x40
   __TEXT.__objc_classname: 0x12c
   __TEXT.__objc_methname: 0x1aa7
   __TEXT.__objc_methtype: 0x465
   __TEXT.__objc_stubs: 0x11a0
   __DATA_CONST.__got: 0x410
-  __DATA_CONST.__const: 0x1d8
+  __DATA_CONST.__const: 0x208
   __DATA_CONST.__objc_classlist: 0x100
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x660
+  __DATA_CONST.__objc_selrefs: 0x728
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x7a8
+  __AUTH_CONST.__auth_got: 0x790
   __AUTH_CONST.__const: 0x988
   __AUTH_CONST.__cfstring: 0x9a0
-  __AUTH_CONST.__objc_const: 0x24c8
+  __AUTH_CONST.__objc_const: 0x2220
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH.__objc_data: 0x628
   __AUTH.__data: 0x1588
   __DATA.__objc_ivar: 0x58
-  __DATA.__data: 0x8b0
+  __DATA.__data: 0x8a8
   __DATA.__bss: 0x1728
-  __DATA.__common: 0xd0
+  __DATA.__common: 0xb0
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/AppleAccount.framework/Versions/A/AppleAccount
   - /System/Library/PrivateFrameworks/AppleAccountUI.framework/Versions/A/AppleAccountUI
   - /System/Library/PrivateFrameworks/FTServices.framework/Versions/A/FTServices
+  - /System/Library/PrivateFrameworks/GeoServices.framework/Versions/A/GeoServices
   - /System/Library/PrivateFrameworks/IMCore.framework/Versions/A/IMCore
   - /System/Library/PrivateFrameworks/IMFoundation.framework/Versions/A/IMFoundation
   - /System/Library/PrivateFrameworks/IMSharedUtilities.framework/Versions/A/IMSharedUtilities
   - /System/Library/PrivateFrameworks/IconServices.framework/Versions/A/IconServices
   - /System/Library/PrivateFrameworks/InputAnalytics.framework/Versions/A/InputAnalytics
   - /System/Library/PrivateFrameworks/Marco.framework/Versions/A/Marco
+  - /System/Library/PrivateFrameworks/PowerLog.framework/Versions/A/PowerLog
   - /System/Library/PrivateFrameworks/RegulatoryDomain.framework/Versions/A/RegulatoryDomain
   - /System/Library/PrivateFrameworks/SafetyMonitor.framework/Versions/A/SafetyMonitor
   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking

   - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftVideoToolbox.dylib
-  - /usr/lib/swift/libswiftWebKit.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_errno.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: B527EAC5-E456-3DCB-8734-73864308BD26
-  Functions: 699
-  Symbols:   972
-  CStrings:  677
+  UUID: 871FF4D7-7552-3CD2-BB1D-F4EFDC40D17F
+  Functions: 684
+  Symbols:   974
+  CStrings:  666
 
Symbols:
+ +[CKSharedSettingsHelper sharedInstance].cold.1
+ +[CKiCloudSettingsUtils lastSyncedDateStringForDate:inContext:].cold.1
+ +[CKiCloudSettingsUtils sharedNumberFormatter].cold.1
+ -[CKSharedSettingsHelper isRaiseGestureSupported].cold.1
+ __os_feature_enabled_impl
+ __swift_FORCE_LOAD_$_swiftDataDetection
+ __swift_FORCE_LOAD_$_swiftDataDetection_$_MessagesSettingsUI
- __swift_FORCE_LOAD_$_swiftFileProvider
- __swift_FORCE_LOAD_$_swiftFileProvider_$_MessagesSettingsUI
- __swift_FORCE_LOAD_$_swiftWebKit
- __swift_FORCE_LOAD_$_swiftWebKit_$_MessagesSettingsUI
- _symbolic _____y_____GSg 7SwiftUI11AnyLocationC 016MessagesSettingsB015CheckInDataViewV5ModelC
CStrings:
+ "Zelkova"
+ "Zelkova_Korea"
- "Fatal error"
- "Insufficient space allocated to copy string contents"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "invalid Collection: less than 'count' elements in collection"

```
