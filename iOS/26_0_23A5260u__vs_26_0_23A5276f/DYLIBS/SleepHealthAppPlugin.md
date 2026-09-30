## SleepHealthAppPlugin

> `/System/Library/Health/FeedItemPlugins/SleepHealthAppPlugin.healthplugin/SleepHealthAppPlugin`

```diff

-6074.1.2.4.0
-  __TEXT.__text: 0x1046f8
-  __TEXT.__auth_stubs: 0x5ea0
-  __TEXT.__objc_methlist: 0xf48
-  __TEXT.__const: 0xa954
-  __TEXT.__cstring: 0x99d4
-  __TEXT.__constg_swiftt: 0x4bb0
-  __TEXT.__swift5_typeref: 0x318e
+6087.1.2.1.0
+  __TEXT.__text: 0x105f8c
+  __TEXT.__auth_stubs: 0x5ec0
+  __TEXT.__objc_methlist: 0xf78
+  __TEXT.__const: 0xa984
+  __TEXT.__cstring: 0x9a84
+  __TEXT.__constg_swiftt: 0x4bec
+  __TEXT.__swift5_typeref: 0x3194
   __TEXT.__swift5_reflstr: 0x29f3
-  __TEXT.__swift5_fieldmd: 0x2a10
+  __TEXT.__swift5_fieldmd: 0x2a20
   __TEXT.__swift5_builtin: 0xb4
   __TEXT.__swift5_assocty: 0x858
   __TEXT.__swift5_proto: 0x7f4
-  __TEXT.__swift5_types: 0x394
-  __TEXT.__swift5_capture: 0xed0
-  __TEXT.__oslogstring: 0x48c9
+  __TEXT.__swift5_types: 0x398
+  __TEXT.__swift5_capture: 0xf04
+  __TEXT.__oslogstring: 0x4879
   __TEXT.__swift5_protos: 0x64
   __TEXT.__swift_as_entry: 0x54
   __TEXT.__swift_as_ret: 0x60
-  __TEXT.__unwind_info: 0x30b0
+  __TEXT.__unwind_info: 0x30d8
   __TEXT.__eh_frame: 0x1b20
   __TEXT.__objc_classname: 0x2a6
-  __TEXT.__objc_methname: 0x3fe8
+  __TEXT.__objc_methname: 0x4033
   __TEXT.__objc_methtype: 0x15bd
-  __DATA_CONST.__got: 0x18e8
-  __DATA_CONST.__const: 0x120
-  __DATA_CONST.__objc_classlist: 0x170
+  __DATA_CONST.__got: 0x18e0
+  __DATA_CONST.__const: 0x100
+  __DATA_CONST.__objc_classlist: 0x178
   __DATA_CONST.__objc_catlist2: 0x8
   __DATA_CONST.__objc_protolist: 0x190
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1160
+  __DATA_CONST.__objc_selrefs: 0x1170
   __DATA_CONST.__objc_protorefs: 0xc8
-  __AUTH_CONST.__auth_got: 0x2f50
-  __AUTH_CONST.__const: 0x6b60
-  __AUTH_CONST.__objc_const: 0x4960
-  __AUTH.__objc_data: 0x25c0
-  __AUTH.__data: 0x24d0
-  __DATA.__data: 0x3598
+  __AUTH_CONST.__auth_got: 0x2f60
+  __AUTH_CONST.__const: 0x6bb0
+  __AUTH_CONST.__objc_const: 0x49a8
+  __AUTH.__objc_data: 0x2678
+  __AUTH.__data: 0x24f0
+  __DATA.__data: 0x3578
   __DATA.__objc_stublist: 0x80
   __DATA.__common: 0x370
   __DATA.__bss: 0xc980

   - /System/Library/Frameworks/SwiftUI.framework/SwiftUI
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
+  - /System/Library/Frameworks/WidgetKit.framework/WidgetKit
   - /System/Library/PrivateFrameworks/HealthAppHealthDaemonSupport.framework/HealthAppHealthDaemonSupport
   - /System/Library/PrivateFrameworks/HealthAppServices.framework/HealthAppServices
   - /System/Library/PrivateFrameworks/HealthArticlesGeneration.framework/HealthArticlesGeneration

   - /System/Library/PrivateFrameworks/Sleep.framework/Sleep
   - /System/Library/PrivateFrameworks/SleepHealth.framework/SleepHealth
   - /System/Library/PrivateFrameworks/SleepHealthUI.framework/SleepHealthUI
+  - /System/Library/PrivateFrameworks/SleepWidgetUI.framework/SleepWidgetUI
   - /System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftGLKit.dylib
   - /usr/lib/swift/libswiftIntents.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: D1061204-7901-3924-AC69-3D0385C45D5C
-  Functions: 4612
-  Symbols:   447
-  CStrings:  1904
+  UUID: 95481DC0-1C0C-3EE4-979E-50F8E43A49DC
+  Functions: 4626
+  Symbols:   444
+  CStrings:  1909
 
Symbols:
+ _HKSHSleepApneaRescindedNotificationRequestIdentifier
+ _HKSPSleepLaunchURLRouteOpenSleepApneaNotificationsRoom
- _OBJC_CLASS_$_HKDisplayCategory
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
CStrings:
+ "SleepHealthAppPlugin/HostingConfigurationCell.swift"
+ "You must override this!"
+ "[%s]: No navigation controller provided to open sleep room: %s"
+ "[%{public}s] Attempting to open sleep apnea notifications room"
+ "[%{public}s] Could not get view controller, not opening sleep apnea notifications room."
+ "_TtC20SleepHealthAppPlugin24HostingConfigurationCell"
+ "_bridgedUpdateConfigurationUsingState:"
+ "bounds"
+ "setAutomaticallyUpdatesContentConfiguration:"
- "[%{public}s] Found an existing %{public}s in the UINavigationController stack"
- "[%{public}s] No SleepRoomViewController found in the UINavigationController. Creating one."
- "[%{public}s] The presenting view controller doesn't have a navigationController set. Creating a new SleepRoomViewController."
- "categoryWithID:"

```
