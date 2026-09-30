## AmbientSettingsAppIntentsExtension

> `/System/Library/ExtensionKit/Extensions/AmbientSettingsAppIntentsExtension.appex/AmbientSettingsAppIntentsExtension`

```diff

-79.0.0.0.0
-  __TEXT.__text: 0x2c88
-  __TEXT.__auth_stubs: 0x3a0
-  __TEXT.__const: 0x6aa
-  __TEXT.__cstring: 0x4c7
-  __TEXT.__swift5_typeref: 0x2ce
-  __TEXT.__swift5_reflstr: 0xc5
-  __TEXT.__swift5_assocty: 0xc0
+80.0.0.0.0
+  __TEXT.__text: 0x3cac
+  __TEXT.__auth_stubs: 0x4a0
+  __TEXT.__const: 0x96e
+  __TEXT.__cstring: 0x666
+  __TEXT.__swift5_typeref: 0x2fc
+  __TEXT.__swift5_reflstr: 0x12f
+  __TEXT.__swift5_assocty: 0x118
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x60
-  __TEXT.__swift5_fieldmd: 0x6c
-  __TEXT.__swift5_proto: 0x5c
-  __TEXT.__swift5_types: 0xc
-  __TEXT.__swift_as_entry: 0x8
-  __TEXT.__swift_as_ret: 0x4
-  __TEXT.__unwind_info: 0x1a8
-  __TEXT.__eh_frame: 0x68
-  __DATA_CONST.__auth_got: 0x1d0
-  __DATA_CONST.__got: 0x70
-  __DATA_CONST.__auth_ptr: 0x368
-  __DATA_CONST.__const: 0x228
+  __TEXT.__constg_swiftt: 0xa4
+  __TEXT.__swift5_fieldmd: 0xc8
+  __TEXT.__swift5_proto: 0x7c
+  __TEXT.__swift5_types: 0x14
+  __TEXT.__objc_methname: 0x21
+  __TEXT.__swift_as_entry: 0x2c
+  __TEXT.__swift_as_ret: 0x24
+  __TEXT.__unwind_info: 0x218
+  __TEXT.__eh_frame: 0x1b8
+  __DATA_CONST.__auth_got: 0x250
+  __DATA_CONST.__got: 0x80
+  __DATA_CONST.__auth_ptr: 0x470
+  __DATA_CONST.__const: 0x288
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__data: 0x158
-  __DATA.__bss: 0xb80
-  __DATA.__common: 0x48
+  __DATA.__objc_selrefs: 0x10
+  __DATA.__data: 0x208
+  __DATA.__bss: 0xf80
+  __DATA.__common: 0x30
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/UIKit.framework/UIKit
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
+  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 051246D6-8433-3AC6-9090-258C05B48438
-  Functions: 116
-  Symbols:   46
-  CStrings:  20
+  UUID: 5873C963-0D88-3250-9860-B4E6315A0597
+  Functions: 151
+  Symbols:   67
+  CStrings:  24
 
Symbols:
+ _MobileGestalt_get_current_device
+ _MobileGestalt_get_deviceSupportsAlwaysOnTime
+ _OBJC_CLASS_$_UIDevice
+ __swift_FORCE_LOAD_$_swiftCoreAudio
+ __swift_FORCE_LOAD_$_swiftCoreMedia
+ __swift_FORCE_LOAD_$_swiftSpatial
+ __swift_FORCE_LOAD_$_swiftUIKit
+ _malloc_size
+ _objc_msgSend
+ _objc_opt_self
+ _objc_release_x21
+ _objc_retainAutoreleasedReturnValue
+ _swift_arrayInitWithCopy
+ _swift_arrayInitWithTakeBackToFront
+ _swift_arrayInitWithTakeFrontToBack
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_getEnumTagSinglePayloadGeneric
+ _swift_getSingletonMetadata
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_storeEnumTagSinglePayloadGeneric
+ _swift_task_switch
- __swiftEmptyDictionarySingleton
- _swift_arrayDestroy
- _swift_deallocClassInstance
- _swift_release
- _swift_retain
- _swift_setDeallocating
CStrings:
+ "#AMBIENT_MODE_ENABLED"
+ "#NOTIFICATIONS_ENABLED"
+ "#NOTIFICATIONS_PREVIEW"
+ "/"
+ "/ALWAYS_ON_DISPLAY_OPTIONS"
+ "/ALWAYS_ON_DISPLAY_OPTIONS#MOTION_TO_WAKE_ENABLED"
+ "/ALWAYS_ON_DISPLAY_OPTIONS#NIGHT_MODE_ENABLED"
+ "Open StandBy Settings"
+ "Show Notifications control under the root settings pane for StandBy. This setting toggles if critical notifications will show while in StandBy."
+ "Show Preview on Tap Only control under the root settings pane for StandBy. This setting toggles if a preview of a notification is hidden until the user taps on it."
+ "StandBy control under the root settings pane for StandBy. This setting toggles if StandBy will turn on when iPhone is placed on its side while charging."
+ "StandBy → Display"
+ "The Motion To Wake Control under the Displays settings pane for StandBy. This setting toggles if StandBy will turn the display on when motion is detected at night."
+ "The Night Mode Control under the Displays settings pane for StandBy. This setting toggles if StandBy will display with a red tint in low ambient lighting."
+ "Turn Display Off Control under the Displays settings pane for StandBy. This setting toggles if the display will turn off when in StandBy on devices that support Always On Display."
+ "currentDevice"
+ "userInterfaceIdiom"
- "Open Standby Settings"
- "Show Notifications control under the root settings pane for StandBy.  This setting toggles if critical notifications will show while in StandBy."
- "Show Preview on Tap Only control under the root settings pane for StandBy.  This setting toggles if a preview of a notification is hidden until the user taps on it."
- "Stand By settings"
- "StandBy control under the root settings pane for StandBy.  This setting toggles if StandBy will turn on when iPhone is placed on its side while charging."
- "Standby Settings"
- "root"
- "settings-navigation://com.apple.Settings.StandBy#AMBIENT_MODE_ENABLED"
- "settings-navigation://com.apple.Settings.StandBy#NOTIFICATIONS_ENABLED"
- "settings-navigation://com.apple.Settings.StandBy#NOTIFICATIONS_PREVIEW"
- "showNotifications"
- "showPreviewOnTapOnly"
- "standBy"

```
