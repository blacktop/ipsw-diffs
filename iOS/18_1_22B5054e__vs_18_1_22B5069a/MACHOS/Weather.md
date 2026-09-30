## Weather

> `/private/var/staged_system_apps/Weather.app/Weather`

```diff

-787.0.0.0.0
-  __TEXT.__text: 0xbe5c4c
-  __TEXT.__auth_stubs: 0x11dc0
+789.3.0.0.0
+  __TEXT.__text: 0xbe670c
+  __TEXT.__auth_stubs: 0x11de0
   __TEXT.__objc_stubs: 0x180
   __TEXT.__objc_methlist: 0xfb8
   __TEXT.__const: 0x5e354
-  __TEXT.__oslogstring: 0x9f67
+  __TEXT.__oslogstring: 0xa177
   __TEXT.__objc_classname: 0x199
   __TEXT.__objc_methname: 0x4b22
   __TEXT.__objc_methtype: 0x1aa2
-  __TEXT.__cstring: 0x2d326
+  __TEXT.__cstring: 0x2d376
   __TEXT.__swift5_typeref: 0x8c35e
   __TEXT.__constg_swiftt: 0x1f444
   __TEXT.__swift5_builtin: 0x35c
-  __TEXT.__swift5_reflstr: 0x1a828
-  __TEXT.__swift5_fieldmd: 0x1e664
+  __TEXT.__swift5_reflstr: 0x1a838
+  __TEXT.__swift5_fieldmd: 0x1e670
   __TEXT.__swift5_assocty: 0x42d0
   __TEXT.__swift5_proto: 0x4f70
   __TEXT.__swift5_types: 0x21c8
-  __TEXT.__swift5_capture: 0x7ed0
+  __TEXT.__swift5_capture: 0x7f10
   __TEXT.__swift5_protos: 0x510
   __TEXT.__swift5_mpenum: 0x120
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x1d420
+  __TEXT.__unwind_info: 0x1d440
   __TEXT.__eh_frame: 0x17d88
-  __DATA_CONST.__auth_got: 0x8ee8
-  __DATA_CONST.__got: 0x5120
-  __DATA_CONST.__auth_ptr: 0x8e08
-  __DATA_CONST.__const: 0x35c58
+  __DATA_CONST.__auth_got: 0x8ef8
+  __DATA_CONST.__got: 0x5140
+  __DATA_CONST.__auth_ptr: 0x8bb8
+  __DATA_CONST.__const: 0x35d00
   __DATA_CONST.__objc_classlist: 0xf10
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x130
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xa0
-  __DATA.__objc_const: 0x1c6f0
+  __DATA.__objc_const: 0x1c710
   __DATA.__objc_selrefs: 0x1010
   __DATA.__objc_data: 0x4870
-  __DATA.__data: 0x56c88
+  __DATA.__data: 0x56c68
   __DATA.__objc_stublist: 0x8
   __DATA.__bss: 0x953d0
   __DATA.__common: 0x19e0

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
-  Functions: 47383
-  Symbols:   8205
-  CStrings:  5016
+  Functions: 47399
+  Symbols:   8211
+  CStrings:  5024
 
Symbols:
+ _$s11WeatherCore25SavedLocationsManagerTypeP10dataStatusAA0cde4DataH0OvgTj
+ _$s11WeatherCore31SavedLocationsManagerDataStatusO5readyyA2CmFWC
+ _$s11WeatherCore31SavedLocationsManagerDataStatusO7pendingyA2CmFWC
+ _$s11WeatherCore31SavedLocationsManagerDataStatusOMa
+ _$s7SwiftUI4ViewPAAE16_fullScreenSheet11isPresented9onDismiss7contentQrAA7BindingVySbG_yycSgqd__yctAaBRd__lF
+ _$s7SwiftUI4ViewPAAE16_fullScreenSheet11isPresented9onDismiss7contentQrAA7BindingVySbG_yycSgqd__yctAaBRd__lFQOMQ
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit
- _$sSo17OS_dispatch_queueC13WeatherDaemonE13notificationsABvgZ
CStrings:
+ "SavedLocationsMonitor: saved locations data is still pending, ignore applicationWillEnterForeground event"
+ "Self deallocated in NotificationSubscriptionMonitor.applicationWillEnterForeground"
+ "Self deallocated in NotificationSubscriptionMonitor.notificationAvailabilityChange"
+ "Self deallocated in NotificationSubscriptionMonitor.subscribed"
+ "Self deallocated in NotificationSubscriptionMonitor.unsubscribed"
+ "Unhandled case in SavedLocationsMonitor.applicationWillEnterForeground"
+ "com.apple.weather.notificationSubscriptionMonitor.operation"
+ "operationQueue"

```
