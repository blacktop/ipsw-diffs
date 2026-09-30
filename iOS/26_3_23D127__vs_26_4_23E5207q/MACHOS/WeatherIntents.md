## WeatherIntents

> `/private/var/staged_system_apps/Weather.app/PlugIns/WeatherIntents.appex/WeatherIntents`

```diff

-1104.0.0.0.0
-  __TEXT.__text: 0xda8c
+1316.0.0.0.0
+  __TEXT.__text: 0xd3b8
   __TEXT.__auth_stubs: 0xf30
-  __TEXT.__objc_stubs: 0x140
-  __TEXT.__objc_methlist: 0x3f8
-  __TEXT.__objc_classname: 0x37
-  __TEXT.__objc_methname: 0x796
-  __TEXT.__objc_methtype: 0x146
+  __TEXT.__objc_stubs: 0x560
+  __TEXT.__objc_methlist: 0x380
   __TEXT.__const: 0x620
-  __TEXT.__cstring: 0x7d4
+  __TEXT.__objc_methname: 0xb03
+  __TEXT.__cstring: 0x161
   __TEXT.__oslogstring: 0x65a
   __TEXT.__swift5_typeref: 0x3f4
+  __TEXT.__objc_classname: 0x1e0
+  __TEXT.__objc_methtype: 0x37a
   __TEXT.__constg_swiftt: 0x2d8
   __TEXT.__swift5_reflstr: 0x2cf
   __TEXT.__swift5_fieldmd: 0x200

   __TEXT.__swift_as_ret: 0x14
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__unwind_info: 0x488
+  __TEXT.__unwind_info: 0x478
   __TEXT.__eh_frame: 0x350
   __DATA_CONST.__auth_got: 0x7a0
   __DATA_CONST.__got: 0x1c8
   __DATA_CONST.__auth_ptr: 0x1b0
-  __DATA_CONST.__const: 0x548
+  __DATA_CONST.__const: 0x590
   __DATA_CONST.__objc_classlist: 0x48
-  __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA.__objc_const: 0x998
-  __DATA.__objc_selrefs: 0x2e0
+  __DATA.__objc_const: 0x878
+  __DATA.__objc_selrefs: 0x298
   __DATA.__objc_data: 0x4c0
   __DATA.__data: 0x580
   __DATA.__common: 0x18

   - /System/Library/PrivateFrameworks/TeaDB.framework/TeaDB
   - /System/Library/PrivateFrameworks/TeaFoundation.framework/TeaFoundation
   - /System/Library/PrivateFrameworks/TeaSettings.framework/TeaSettings
+  - /System/Library/PrivateFrameworks/WeatherAppSupport.framework/WeatherAppSupport
   - /System/Library/PrivateFrameworks/WeatherCore.framework/WeatherCore
   - /System/Library/PrivateFrameworks/WeatherDaemon.framework/WeatherDaemon
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftAppleArchive.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
+  - /usr/lib/swift/libswiftCoreMIDI.dylib
+  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftGLKit.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMapKit.dylib
   - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftMetalKit.dylib
+  - /usr/lib/swift/libswiftModelIO.dylib
   - /usr/lib/swift/libswiftNaturalLanguage.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftSceneKit.dylib
+  - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 63BFF208-CA00-3782-A322-4797E383A34E
-  Functions: 397
-  Symbols:   153
-  CStrings:  204
+  UUID: 5D5E0EB5-8DF0-3875-93C7-93CA87AD6A78
+  Functions: 387
+  Symbols:   161
+  CStrings:  188
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftAVFoundation
+ __swift_FORCE_LOAD_$_swiftCoreAudio
+ __swift_FORCE_LOAD_$_swiftCoreMIDI
+ __swift_FORCE_LOAD_$_swiftCoreMedia
+ __swift_FORCE_LOAD_$_swiftGLKit
+ __swift_FORCE_LOAD_$_swiftMetalKit
+ __swift_FORCE_LOAD_$_swiftModelIO
+ __swift_FORCE_LOAD_$_swiftSceneKit
+ __swift_FORCE_LOAD_$_swiftSpatial
+ _objc_retain_x26
+ _swift_bridgeObjectRelease_n
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x25
- _objc_retain_x28
CStrings:
+ "WeatherIntent"
+ "WeatherIntentResponse"
+ "WeatherLocation"
+ "WeatherLocationResolutionResult"
+ "w_applyLocalitiesAndLandmarksFilterType"
+ "w_calloutTitle"
+ "w_get:"
+ "w_mapItem"
- "B24@0:8^{CLLocationCoordinate2D=dd}16"
- "T@\"MKMapItem\",R,N"
- "T@\"NSString\",R,N"
- "_setPrivateFilterType:"
- "_weatherDisplayName"
- "_weatherLocationName"
- "calloutTitle"
- "getCoordinate:"
- "length"
- "locality"
- "mapItem"
- "wc_localityName"
- "wi_applyLocalitiesAndLandmarksFilterType"
- "wi_calloutTitle"
- "wi_getCoordinate:"
- "wi_mapItem"

```
