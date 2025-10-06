## UserNotificationsServices

> `/System/Library/PrivateFrameworks/UserNotificationsServices.framework/UserNotificationsServices`

```diff

-640.1.9.100.0
-  __TEXT.__text: 0x27284
-  __TEXT.__auth_stubs: 0xee0
+640.1.16.100.0
+  __TEXT.__text: 0x2719c
+  __TEXT.__auth_stubs: 0xf00
   __TEXT.__objc_methlist: 0x58c
   __TEXT.__const: 0x3894
   __TEXT.__gcc_except_tab: 0xf8
   __TEXT.__cstring: 0x10a6
-  __TEXT.__oslogstring: 0xddc
+  __TEXT.__oslogstring: 0xdbc
   __TEXT.__constg_swiftt: 0x1014
   __TEXT.__swift5_typeref: 0x80f
   __TEXT.__swift5_fieldmd: 0xc20

   __TEXT.__unwind_info: 0xba0
   __TEXT.__eh_frame: 0xa98
   __TEXT.__objc_classname: 0x119
-  __TEXT.__objc_methname: 0x1b60
+  __TEXT.__objc_methname: 0x1b41
   __TEXT.__objc_methtype: 0x2cf
   __TEXT.__objc_stubs: 0x1700
-  __DATA_CONST.__got: 0x360
-  __DATA_CONST.__const: 0x220
+  __DATA_CONST.__got: 0x358
+  __DATA_CONST.__const: 0x200
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x748
+  __DATA_CONST.__objc_selrefs: 0x738
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x780
-  __AUTH_CONST.__const: 0x1980
+  __AUTH_CONST.__auth_got: 0x790
+  __AUTH_CONST.__const: 0x19d0
   __AUTH_CONST.__cfstring: 0x380
   __AUTH_CONST.__objc_const: 0x980
   __AUTH.__objc_data: 0xf0

   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
-  - /System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/DoNotDisturb.framework/DoNotDisturb
   - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
-  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
-  - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
-  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 023273BC-6541-3F80-A5DC-9E0863A93073
+  UUID: 75DD6CAE-E635-3207-8627-A3D36F2173D3
   Functions: 1242
-  Symbols:   1060
-  CStrings:  538
+  Symbols:   1051
+  CStrings:  535
 
Symbols:
- _OBJC_CLASS_$_AFPreferences
- __swift_FORCE_LOAD_$_swiftAVFoundation
- __swift_FORCE_LOAD_$_swiftAVFoundation_$_UserNotificationsServices
- __swift_FORCE_LOAD_$_swiftCoreAudio
- __swift_FORCE_LOAD_$_swiftCoreAudio_$_UserNotificationsServices
- __swift_FORCE_LOAD_$_swiftCoreLocation
- __swift_FORCE_LOAD_$_swiftCoreLocation_$_UserNotificationsServices
- __swift_FORCE_LOAD_$_swiftCoreMedia
- __swift_FORCE_LOAD_$_swiftCoreMedia_$_UserNotificationsServices
Functions:
~ sub_26f786fcc -> sub_26f7abe3c : 1040 -> 808
~ ___swift_project_value_buffer -> sub_26f7ac248 : 56 -> 88
~ ___swift_destroy_boxed_opaque_existential_1Tm -> ___swift_project_value_buffer : 76 -> 56
~ sub_26f787598 -> ___swift_destroy_boxed_opaque_existential_1Tm : 88 -> 76
CStrings:
+ "Topic summaries enabled:%{bool,public}d = featureEnabled:%{bool,public}d && !(chinaRegion:%{bool,public}d) && (isAllowedLocale=%{bool}d(code=%{public}s) || internalInstall=%{bool,public}d)"
- "Failed get lanugage code"
- "Topic summaries enabled:%{bool,public}d = featureEnabled:%{bool,public}d && !(chinaRegion:%{bool,public}d) && (!excludedLanguage:%{bool,public}d(code=%s)||internalInstall:%{bool,public}d)"
- "languageCode"
- "sharedPreferences"

```
