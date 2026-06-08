## RPControlCenterModuleHQLR

> `/System/Library/ControlCenter/Bundles/RPControlCenterModuleHQLR.bundle/RPControlCenterModuleHQLR`

```diff

-710.1.1.0.0
-  __TEXT.__text: 0x1fcc4
-  __TEXT.__auth_stubs: 0xf30
-  __TEXT.__objc_stubs: 0x1c20
-  __TEXT.__objc_methlist: 0xcc8
-  __TEXT.__const: 0x13e8
-  __TEXT.__cstring: 0x18db
-  __TEXT.__objc_methname: 0x2e2d
-  __TEXT.__objc_classname: 0x338
-  __TEXT.__objc_methtype: 0x7e3
-  __TEXT.__gcc_except_tab: 0xbc
-  __TEXT.__oslogstring: 0x100e
-  __TEXT.__swift5_typeref: 0x114a
+740.44.1.0.0
+  __TEXT.__text: 0x1f7ac
+  __TEXT.__auth_stubs: 0x1110
+  __TEXT.__objc_stubs: 0x1ca0
+  __TEXT.__objc_methlist: 0xd30
+  __TEXT.__const: 0x1570
+  __TEXT.__cstring: 0x18cb
+  __TEXT.__objc_methname: 0x2f9d
+  __TEXT.__objc_classname: 0x328
+  __TEXT.__objc_methtype: 0x833
+  __TEXT.__gcc_except_tab: 0x68
+  __TEXT.__oslogstring: 0x107e
+  __TEXT.__swift5_typeref: 0x116a
   __TEXT.__swift5_capture: 0xf4
-  __TEXT.__swift5_reflstr: 0x347
-  __TEXT.__swift5_assocty: 0x140
-  __TEXT.__constg_swiftt: 0x8f4
-  __TEXT.__swift5_builtin: 0x64
-  __TEXT.__swift5_fieldmd: 0x398
-  __TEXT.__swift5_proto: 0x54
-  __TEXT.__swift5_types: 0x60
-  __TEXT.__unwind_info: 0x910
-  __DATA_CONST.__auth_got: 0x7a8
-  __DATA_CONST.__got: 0x2c0
-  __DATA_CONST.__auth_ptr: 0x320
+  __TEXT.__swift5_reflstr: 0x367
+  __TEXT.__swift5_assocty: 0x170
+  __TEXT.__constg_swiftt: 0x920
+  __TEXT.__swift5_builtin: 0x78
+  __TEXT.__swift5_fieldmd: 0x3b4
+  __TEXT.__swift5_proto: 0x6c
+  __TEXT.__swift5_types: 0x64
+  __TEXT.__unwind_info: 0x940
   __DATA_CONST.__const: 0xc88
   __DATA_CONST.__cfstring: 0x4c0
   __DATA_CONST.__objc_classlist: 0x68

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_intobj: 0x60
-  __DATA.__objc_const: 0x1c70
-  __DATA.__objc_selrefs: 0xb20
-  __DATA.__objc_ivar: 0xcc
+  __DATA_CONST.__auth_got: 0x898
+  __DATA_CONST.__got: 0x2c0
+  __DATA_CONST.__auth_ptr: 0x378
+  __DATA.__objc_const: 0x1d30
+  __DATA.__objc_selrefs: 0xb70
+  __DATA.__objc_ivar: 0xdc
   __DATA.__objc_data: 0x7c8
-  __DATA.__data: 0xd58
-  __DATA.__bss: 0xcf8
+  __DATA.__data: 0xd48
+  __DATA.__bss: 0x1008
   __DATA.__common: 0xe0
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
-  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 653B040A-F3F8-3C75-858D-F302AF95E2E5
-  Functions: 899
-  Symbols:   244
-  CStrings:  838
+  UUID: FCA578F3-E479-36BA-B96D-D45921E81B24
+  Functions: 917
+  Symbols:   272
+  CStrings:  858
 
Symbols:
+ _CFPreferencesGetAppBooleanValue
+ _OBJC_CLASS_$_CCUIContentModulePreviewProvider
+ _OBJC_CLASS_$_CCUIContentModuleTemplatePreviewDescription
+ __swift_FORCE_LOAD_$_swiftCompression
+ _objc_claimAutoreleasedReturnValue
+ _objc_opt_isKindOfClass
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x3
+ _os_variant_allows_internal_security_policies
+ _swift_release_x1
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x23
+ _swift_release_x24
+ _swift_release_x25
+ _swift_release_x26
+ _swift_release_x27
+ _swift_release_x8
+ _swift_retain_x1
+ _swift_retain_x19
+ _swift_retain_x2
+ _swift_retain_x20
+ _swift_retain_x22
+ _swift_retain_x23
+ _swift_retain_x26
+ _swift_retain_x27
+ _swift_retain_x3
- __swift_FORCE_LOAD_$_swiftCoreMedia
- _objc_retain_x28
CStrings:
+ " [DEBUG] %{public}s:%d no UIBackgroundModes in Info.plist"
+ " [INFO] %{public}s:%d backgroundModes=%@ hasScreenCapture=%d"
+ "-[NSBundle(RPExtensions) _rpHasScreenCaptureBackgroundMode]"
+ "/System/Library/Frameworks/ScreenCaptureKit.framework"
+ "@\"<CCUIContentModulePreviewProviding>\"24@0:8@\"CCUIContentModulePreviewContext\"16"
+ "DeviceSupportsAlwaysOnTime"
+ "SCKEnableSCKIOS"
+ "ScreenCaptureKitiOS"
+ "ScreenCaptureKitvisionOS"
+ "UIBackgroundModes"
+ "UTF8String"
+ "_backgroundReplacementEnabled"
+ "_edgeLightEnabled"
+ "_rpHasScreenCaptureBackgroundMode"
+ "_rpLocalizableTableName"
+ "_rpLocalizedStringFromFrameworkBundleWithKey:tableName:"
+ "_scFrameworkBundle"
+ "_screenCaptureKitiOS"
+ "_screenCaptureKitvisionOS"
+ "backgroundReplacementEnabled"
+ "com.apple.replayd"
+ "containsObject:"
+ "edgeLight"
+ "edgeLightEnabled"
+ "essonite_bg_ios"
+ "initWithDescription:"
+ "previewProviderForContext:"
+ "screen-capture"
+ "screenCaptureKitiOS"
+ "screenCaptureKitvisionOS"
+ "setGlyphPackageState:"
- "-[RPCCUICallRecordingModuleViewController presentCancelReadyToRecord]"
- "BROADCAST_FAILED_ALERT_OK_BUTTON"
- "CONTROL_CENTER_CANCEL_READY_STATE_ALERT_DESCRIPTION"
- "CONTROL_CENTER_CANCEL_READY_STATE_ALERT_TITLE"
- "CONTROL_CENTER_CANCEL_READY_STATE_NO"
- "CONTROL_CENTER_CANCEL_READY_STATE_YES"
- "cancelReadyToRecord"
- "j8/Omm6s1lsmTDFsXjsBfA"
- "presentAlertWithTitle:message:completion:"
- "presentCancelReadyToRecord"
- "v40@0:8@16@24@?32"

```
