## TVWidgetExtension

> `/private/var/staged_system_apps/AppleTV.app/PlugIns/TVWidgetExtension.appex/TVWidgetExtension`

```diff

-973.0.5.0.0
-  __TEXT.__text: 0xdc9fc
-  __TEXT.__auth_stubs: 0x2f80
+973.0.9.0.0
+  __TEXT.__text: 0xde758
+  __TEXT.__auth_stubs: 0x2fe0
   __TEXT.__objc_stubs: 0x10c0
   __TEXT.__objc_methlist: 0x3bc
-  __TEXT.__cstring: 0x5686
+  __TEXT.__cstring: 0x5456
   __TEXT.__objc_classname: 0x6b
   __TEXT.__objc_methtype: 0x132
-  __TEXT.__objc_methname: 0x12fa
-  __TEXT.__const: 0xb914
+  __TEXT.__objc_methname: 0x1290
+  __TEXT.__const: 0xb954
   __TEXT.__oslogstring: 0x6c5
   __TEXT.__gcc_except_tab: 0xf4
-  __TEXT.__constg_swiftt: 0x26f0
-  __TEXT.__swift5_typeref: 0x11b70
-  __TEXT.__swift5_builtin: 0x78
-  __TEXT.__swift5_reflstr: 0x372d
-  __TEXT.__swift5_fieldmd: 0x2790
-  __TEXT.__swift5_assocty: 0x1b20
+  __TEXT.__constg_swiftt: 0x2788
+  __TEXT.__swift5_typeref: 0x12168
+  __TEXT.__swift5_builtin: 0x64
+  __TEXT.__swift5_reflstr: 0x36bd
+  __TEXT.__swift5_fieldmd: 0x2758
+  __TEXT.__swift5_assocty: 0x1b50
   __TEXT.__swift5_proto: 0x934
-  __TEXT.__swift5_types: 0x2b0
+  __TEXT.__swift5_types: 0x2b4
   __TEXT.__swift5_protos: 0x18
-  __TEXT.__swift5_capture: 0x384
+  __TEXT.__swift5_capture: 0x388
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x3110
-  __TEXT.__eh_frame: 0x24ac
-  __DATA_CONST.__auth_got: 0x17d0
-  __DATA_CONST.__got: 0xa08
-  __DATA_CONST.__auth_ptr: 0x19b0
-  __DATA_CONST.__const: 0x4e98
+  __TEXT.__unwind_info: 0x31c0
+  __TEXT.__eh_frame: 0x250c
+  __DATA_CONST.__auth_got: 0x1800
+  __DATA_CONST.__got: 0xa10
+  __DATA_CONST.__auth_ptr: 0x19e0
+  __DATA_CONST.__const: 0x4e48
   __DATA_CONST.__cfstring: 0x5c0
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x30
   __DATA.__objc_const: 0xea8
-  __DATA.__objc_selrefs: 0x6a8
+  __DATA.__objc_selrefs: 0x680
   __DATA.__objc_ivar: 0x4c
   __DATA.__objc_data: 0x638
-  __DATA.__data: 0x6238
+  __DATA.__data: 0x6398
   __DATA.__bss: 0x12a38
   __DATA.__common: 0x728
-  - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
+  - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony
   - /System/Library/Frameworks/CoreText.framework/CoreText
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/MediaPlayer.framework/MediaPlayer

   - /System/Library/Frameworks/WidgetKit.framework/WidgetKit
   - /System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices
   - /System/Library/PrivateFrameworks/JetEngine.framework/JetEngine
-  - /System/Library/PrivateFrameworks/Preferences.framework/Preferences
   - /System/Library/PrivateFrameworks/SportsKit.framework/SportsKit
   - /System/Library/PrivateFrameworks/TVAppServices.framework/TVAppServices
   - /System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation

   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftMetalKit.dylib
   - /usr/lib/swift/libswiftModelIO.dylib
-  - /usr/lib/swift/libswiftNaturalLanguage.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4043
-  Symbols:   293
-  CStrings:  753
+  Functions: 4077
+  Symbols:   292
+  CStrings:  740
 
Symbols:
+ _UIGraphicsBeginImageContextWithOptions
+ _UIGraphicsEndImageContext
+ _UIGraphicsGetImageFromCurrentImageContext
+ _UIRectFill
+ __CTServerConnectionCreateAndLaunchWithIdentifier
+ __CTServerConnectionGetCellularDataIsEnabled
+ _kCFAllocatorDefault
+ _swift_getObjCClassFromMetadata
- _AVMakeRectWithAspectRatioInsideRect
- _OBJC_CLASS_$_NSFileManager
- _OBJC_CLASS_$_PSSystemPolicyForApp
- _OBJC_CLASS_$_UIGraphicsImageRenderer
- _OBJC_CLASS_$_UIGraphicsImageRendererFormat
- _UIImagePNGRepresentation
- __swift_FORCE_LOAD_$_swiftNaturalLanguage
- _objc_retain_x9
- _swift_isEscapingClosureAtFileLocation
CStrings:
+ "CGImage"
+ "TVSettingsEntity - could not create ct server object"
+ "audioLanguageCodeIncludingSentinel"
+ "downloadsCompatibileWithAVAdapter"
+ "initWithCGImage:"
+ "initWithRed:green:blue:alpha:"
+ "setFill"
- " is unexpected type"
- "The TVSettings.bundle for localization could not be found on the device."
- "The TVSettingsPreference key associated with the entity is nil"
- "The deeplink URL to settings is nil"
- "The language option is invalid. Make sure it does not exist if you are adding it, or it does exist if you are removing it."
- "The set operation failed for an unknown reason"
- "The value is not supported for this set operation"
- "The value that exists at the preferences store key: "
- "This feature is disabled. Please enable the stratocaster feature flag to use it."
- "URLsForDirectory:inDomains:"
- "defaultManager"
- "downloadsCompatbileWithAVAdapter"
- "drawInRect:"
- "imageWithActions:"
- "initWithBundleIdentifier:"
- "initWithSize:format:"
- "setScale:"
- "size"
- "specifiersForPolicyOptions:force:"
- "v16@?0@\"UIGraphicsImageRendererContext\"8"

```
