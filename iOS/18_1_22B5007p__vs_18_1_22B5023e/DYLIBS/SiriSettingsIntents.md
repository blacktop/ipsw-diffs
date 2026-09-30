## SiriSettingsIntents

> `/System/Library/PrivateFrameworks/SiriSettingsIntents.framework/SiriSettingsIntents`

```diff

-3400.100.1.0.0
-  __TEXT.__text: 0x2fe900
-  __TEXT.__auth_stubs: 0x3140
+3401.9.1.0.0
+  __TEXT.__text: 0x2ef2c4
+  __TEXT.__auth_stubs: 0x3180
   __TEXT.__objc_methlist: 0x150
-  __TEXT.__const: 0xfb84
-  __TEXT.__swift5_typeref: 0x331c
+  __TEXT.__const: 0xfc64
+  __TEXT.__gcc_except_tab: 0x20
+  __TEXT.__cstring: 0x160b8
+  __TEXT.__swift5_typeref: 0x3328
   __TEXT.__swift5_capture: 0x2734
   __TEXT.__oslogstring: 0xd94
-  __TEXT.__swift5_fieldmd: 0x6468
-  __TEXT.__constg_swiftt: 0x7728
+  __TEXT.__swift5_fieldmd: 0x64d8
+  __TEXT.__constg_swiftt: 0x7764
   __TEXT.__swift5_builtin: 0x1b8
-  __TEXT.__swift5_reflstr: 0x67cb
-  __TEXT.__swift5_assocty: 0x11c0
+  __TEXT.__swift5_reflstr: 0x67fb
+  __TEXT.__swift5_assocty: 0x11d8
   __TEXT.__swift5_protos: 0x4c
-  __TEXT.__swift5_proto: 0xb4c
-  __TEXT.__swift5_types: 0x6ac
-  __TEXT.__cstring: 0x15e28
+  __TEXT.__swift5_proto: 0xb58
+  __TEXT.__swift5_types: 0x6b0
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x4380
-  __TEXT.__eh_frame: 0x6bf0
+  __TEXT.__unwind_info: 0x4370
+  __TEXT.__eh_frame: 0x6b28
   __TEXT.__objc_classname: 0x148
   __TEXT.__objc_methname: 0x1b41
   __TEXT.__objc_methtype: 0x9b8
   __DATA_CONST.__got: 0xb38
-  __DATA_CONST.__const: 0x160
+  __DATA_CONST.__const: 0x208
   __DATA_CONST.__objc_classlist: 0x560
   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x6e8
   __DATA_CONST.__objc_protorefs: 0x80
-  __AUTH_CONST.__auth_got: 0x18a0
-  __AUTH_CONST.__auth_ptr: 0x1490
-  __AUTH_CONST.__const: 0xcc68
+  __AUTH_CONST.__auth_got: 0x18c8
+  __AUTH_CONST.__auth_ptr: 0x1220
+  __AUTH_CONST.__const: 0xcd00
   __AUTH_CONST.__objc_const: 0xc680
   __AUTH.__objc_data: 0xe20
   __AUTH.__data: 0x9938
-  __DATA.__data: 0x5480
-  __DATA.__bss: 0x12528
+  __DATA.__data: 0x54b0
+  __DATA.__bss: 0x126b8
   __DATA.__common: 0x1668
   __DATA_DIRTY.__data: 0x790
-  __DATA_DIRTY.__common: 0xa
+  __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony

   - /System/Library/PrivateFrameworks/SiriReferenceResolutionDataModel.framework/SiriReferenceResolutionDataModel
   - /System/Library/PrivateFrameworks/SiriUtilities.framework/SiriUtilities
   - /System/Library/PrivateFrameworks/SnippetKit.framework/SnippetKit
+  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices
   - /System/Library/PrivateFrameworks/UserNotificationsSettings.framework/UserNotificationsSettings

   - /usr/lib/swift/libswiftSwiftOnoneSupport.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 9062
-  Symbols:   390
-  CStrings:  2305
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 9090
+  Symbols:   411
+  CStrings:  2317
 
Symbols:
+ _SetAXMotionCuesWithBanner
+ __Block_object_dispose
+ __Unwind_Resume
+ ___objc_personality_v0
+ __sl_dlopen
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
+ _abort_report_np
+ _dlerror
CStrings:
+ "%!s(MISSING)"
+ "/usr/lib/libAccessibility.dylib"
+ "/usr/local/lib/libAccessibility.dylib"
+ "GetBinarySettingTemplatingService getSettingName | binarySettingPageName CAT failed"
+ "SetAXClassicInvertColorsHandler handleSet | not supported on this device"
+ "SetAXInvertColorsHandler handleSet | not supported on this device"
+ "SetAXReduceWhitePointHandler handleSet | not supported on this device"
+ "SetBinarySettingTemplatingService getSettingName | binarySettingPageName CAT failed"
+ "SettingIntent#BinarySettingPageName"
+ "_AXSSetMotionCuesModeAndShowBanner"
+ "com.apple.graphic-icon.microphone"
+ "secondLabel"

```
