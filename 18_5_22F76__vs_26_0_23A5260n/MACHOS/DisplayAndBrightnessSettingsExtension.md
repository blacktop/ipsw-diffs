## DisplayAndBrightnessSettingsExtension

> `/System/Library/ExtensionKit/Extensions/DisplayAndBrightnessSettingsExtension.appex/DisplayAndBrightnessSettingsExtension`

```diff

-1149.5.1.0.0
-  __TEXT.__text: 0xcab4
-  __TEXT.__auth_stubs: 0x660
-  __TEXT.__const: 0x1a12
-  __TEXT.__cstring: 0x3063
-  __TEXT.__swift5_typeref: 0x776
-  __TEXT.__swift5_reflstr: 0x442
+1170.101.0.0.0
+  __TEXT.__text: 0xdab4
+  __TEXT.__auth_stubs: 0x700
+  __TEXT.__objc_stubs: 0x140
+  __TEXT.__objc_methlist: 0x80
+  __TEXT.__const: 0x1b62
+  __TEXT.__cstring: 0x2cb3
+  __TEXT.__objc_classname: 0x9
+  __TEXT.__objc_methname: 0x1c7
+  __TEXT.__objc_methtype: 0x26
+  __TEXT.__swift5_typeref: 0x76c
+  __TEXT.__swift5_reflstr: 0x453
   __TEXT.__swift5_assocty: 0x318
   __TEXT.__constg_swiftt: 0x1cc
-  __TEXT.__swift5_fieldmd: 0x2e0
-  __TEXT.__objc_methname: 0x40
+  __TEXT.__swift5_fieldmd: 0x2d4
   __TEXT.__swift5_proto: 0x170
   __TEXT.__swift5_types: 0x40
   __TEXT.__swift_as_entry: 0x94
   __TEXT.__swift_as_ret: 0x58
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x550
-  __TEXT.__eh_frame: 0x520
-  __DATA_CONST.__auth_got: 0x330
-  __DATA_CONST.__got: 0xc8
-  __DATA_CONST.__auth_ptr: 0x508
-  __DATA_CONST.__const: 0x9e8
+  __TEXT.__unwind_info: 0x568
+  __TEXT.__eh_frame: 0x4b8
+  __DATA_CONST.__auth_got: 0x388
+  __DATA_CONST.__got: 0xd0
+  __DATA_CONST.__auth_ptr: 0x500
+  __DATA_CONST.__const: 0x958
+  __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_selrefs: 0x20
-  __DATA.__data: 0x578
+  __DATA_CONST.__objc_intobj: 0x30
+  __DATA.__objc_const: 0x40
+  __DATA.__objc_selrefs: 0xb8
+  __DATA.__data: 0x478
   __DATA.__common: 0x90
   __DATA.__bss: 0x2e20
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
+  - /System/Library/Frameworks/CoreMotion.framework/CoreMotion
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/UIKit.framework/UIKit
+  - /System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness
+  - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
+  - /System/Library/PrivateFrameworks/Pegasus.framework/Pegasus
   - /System/Library/PrivateFrameworks/Preferences.framework/Preferences
-  - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib

   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
-  - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib
-  - /usr/lib/swift/libswiftNaturalLanguage.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
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
-  UUID: 6AB2792C-0EAA-3497-AE12-937634300C29
-  Functions: 428
-  Symbols:   72
-  CStrings:  154
+  UUID: B6EE4683-7ECE-3287-8B6A-592B7464CB45
+  Functions: 433
+  Symbols:   81
+  CStrings:  172
 
Symbols:
+ _MCFeatureAutoLockTime
+ _MCSettingParameterRangeMaximumKey
+ _MobileGestalt_get_blueLightReductionSupported
+ _MobileGestalt_get_current_device
+ _MobileGestalt_get_deviceSupportsAlwaysOnTime
+ _MobileGestalt_get_deviceSupportsEnhancedMultitasking
+ _MobileGestalt_get_hallEffectSensorCapability
+ _OBJC_CLASS_$_CBClient
+ _OBJC_CLASS_$_CMWakeGestureManager
+ _OBJC_CLASS_$_MCProfileConnection
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OBJC_CLASS_$_PGPictureInPictureProxy
+ _PSIsInEDUMode
+ __swift_FORCE_LOAD_$_swiftSpatial
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ _objc_autoreleaseReturnValue
+ _objc_claimAutoreleasedReturnValue
+ _objc_release
+ _objc_release_x20
+ _objc_retain_x19
+ _objc_retain_x2
+ _swift_coroFrameAlloc
- _OBJC_CLASS_$_PSCapabilityManager
- _PSPictureInPictureCapability
- _PSRaiseToWakeCapability
- _PSStageManagerCapability
- __swift_FORCE_LOAD_$_swiftDataDetection
- __swift_FORCE_LOAD_$_swiftNaturalLanguage
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd
- _objc_release_x22
- _objc_release_x26
CStrings:
+ "#ALLOW_RECENTS"
+ "#APP_DOWNLOADS_GO_TO"
+ "#BADGES_IN_APP_LIBRARY"
+ "#BOLD_TEXT"
+ "#BRIGHTNESS"
+ "#DEVICE_APPEARANCE"
+ "#RAISE_TO_WAKE"
+ "#SHOW_APP_LIBRARY"
+ "#SHOW_SEARCH_ON_HOME_SCREEN"
+ "#SMART_CASE_LOCK_SPEC"
+ "#USE_LARGE_APP_ICONS"
+ "#WHITE_BALANCE"
+ "/ALWAYS_ON"
+ "/StageManagerDock"
+ "/StageManagerRecentApps"
+ "@16@0:8"
+ "AutoLock"
+ "B16@0:8"
+ "B24@0:8@16"
+ "Description text for the Show on Home Screen in Search control of the Home Screen & App Library Settings pane"
+ "Description text for the Use Large App Icons control of the Home Screen & App Library Settings pane"
+ "Show on Home Screen"
+ "This is the Show on Home Screen in Search control of the Home Screen & App Library Settings pane. When enabled, Search will be visible on the home screen of your device."
+ "This is the Use Large App Icons control of the Home Screen & App Library Settings pane where you can choose if the app icons on your home screen are displayed as large or the default size."
+ "Use Large App Icons"
+ "_autoLockTimeDefault"
+ "_isImmediately:"
+ "_isNever:"
+ "_isUnset:"
+ "autoLockTime"
+ "autoLockTimeMaximum"
+ "com.apple.graphic-icon.apps-on-iphone"
+ "effectiveParametersForValueSetting:"
+ "effectiveValueForSetting:"
+ "i"
+ "intValue"
+ "isAutoLockEnabled"
+ "isAutoLockOn:"
+ "isAutoLockRestricted"
+ "isPictureInPictureSupported"
+ "isValueSettingLockedDownByRestrictions:"
+ "isWakeGestureAvailable"
+ "objectForKey:"
+ "setAutoLockTime:"
+ "setValue:forSetting:"
+ "sf_deviceSupportsDisplayZoom"
+ "sharedConnection"
+ "supportsAdaptation"
+ "v24@0:8@16"
- "/ALWAYS_ON#ALWAYS_ON"
- "/APP_DOWNLOADS_GO_TO"
- "/BADGES_IN_APP_LIBRARY"
- "/BOLD_TEXT"
- "/COMPATIBLE_APPEARANCE_TITLE"
- "/DISPLAY_ZOOM_GROUP"
- "/HOME_SCREEN_DOCK"
- "/HOME_SCREEN_DOCK#ALLOW_RECENTS"
- "/MULTITASKING_DOCK#SHOW_APP_LIBRARY"
- "/Multitasking?OneAppAtATime"
- "/Multitasking?SplitViewSlideOver"
- "/Multitasking?StageManager"
- "/Multitasking?StageManagerDock"
- "/Multitasking?StageManagerRecentApps"
- "/RAISE_TO_WAKE"
- "/SMART_CASE_LOCK_SPEC"
- "Description text for the Display section of the Display & Brightness Settings pane"
- "Description text for the Dock section of the Home Screen & App Library Settings pane"
- "Description text for the Multitasking Off control of the Home Screen & App Library Settings pane"
- "Description text for the Multitasking Split View & Slide Over control of the Home Screen & App Library Settings pane"
- "Description text for the Multitasking Stage Manager control of the Home Screen & App Library Settings pane"
- "Multitasking Off"
- "Multitasking Split View & Slide Over"
- "Multitasking Stage Manager"
- "This is the Display section of the Display & Brightness Settings pane, where you can set controls related to the display, like the Display Zoom"
- "This is the Dock section of the Home Screen & App Library Settings pane where you can manage setting related to the home screen dock on your device."
- "This is the Multitasking Off control of the Multitasking & Gestures Settings pane. When selected, you can only display a single app on screen at a time."
- "This is the Multitasking Split View & Slide Over control of the Multitasking & Gestures Settings pane. When selected, you can display apps side by side on your screen at the same time."
- "This is the Multitasking Stage Manager control of the Multitasking & Gestures Settings pane. When selected, you can use the Stage Manager feature to manage multiple apps at the same time."
- "hasCapabilities:"
- "sharedManager"

```
