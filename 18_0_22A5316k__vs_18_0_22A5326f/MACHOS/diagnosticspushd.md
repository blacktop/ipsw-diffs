## diagnosticspushd

> `/usr/libexec/diagnosticspushd`

```diff

-9.0.0.0.0
-  __TEXT.__text: 0xab5c
-  __TEXT.__auth_stubs: 0x950
+11.0.0.0.0
+  __TEXT.__text: 0x8978
+  __TEXT.__auth_stubs: 0x8b0
   __TEXT.__objc_stubs: 0x60
   __TEXT.__objc_methlist: 0xa0
-  __TEXT.__const: 0x6f6
-  __TEXT.__oslogstring: 0x3af
-  __TEXT.__cstring: 0x701
-  __TEXT.__objc_methname: 0x5f7
-  __TEXT.__constg_swiftt: 0x27c
-  __TEXT.__swift5_typeref: 0x1cd
-  __TEXT.__swift5_reflstr: 0x1ba
-  __TEXT.__swift5_fieldmd: 0x25c
+  __TEXT.__const: 0x7f6
+  __TEXT.__oslogstring: 0x24f
+  __TEXT.__cstring: 0x5d6
+  __TEXT.__objc_methname: 0x4aa
+  __TEXT.__constg_swiftt: 0x24c
+  __TEXT.__swift5_typeref: 0x1fd
+  __TEXT.__swift5_reflstr: 0xfa
+  __TEXT.__swift5_fieldmd: 0x1ec
   __TEXT.__swift5_capture: 0x48
-  __TEXT.__swift5_proto: 0x44
-  __TEXT.__swift5_types: 0x30
+  __TEXT.__swift5_proto: 0x74
+  __TEXT.__swift5_types: 0x38
   __TEXT.__objc_classname: 0x1f
   __TEXT.__objc_methtype: 0x342
   __TEXT.__swift5_assocty: 0x30
-  __TEXT.__unwind_info: 0x2f8
-  __TEXT.__eh_frame: 0x120
-  __DATA_CONST.__auth_got: 0x4b0
-  __DATA_CONST.__got: 0x158
-  __DATA_CONST.__auth_ptr: 0x150
-  __DATA_CONST.__const: 0x500
-  __DATA_CONST.__objc_classlist: 0x30
+  __TEXT.__unwind_info: 0x348
+  __TEXT.__eh_frame: 0x240
+  __DATA_CONST.__auth_got: 0x460
+  __DATA_CONST.__got: 0x128
+  __DATA_CONST.__auth_ptr: 0x148
+  __DATA_CONST.__const: 0x6e8
+  __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA.__objc_const: 0x8a0
-  __DATA.__objc_selrefs: 0x138
-  __DATA.__objc_data: 0x188
-  __DATA.__data: 0x658
-  __DATA.__common: 0x90
-  __DATA.__bss: 0x880
+  __DATA.__objc_const: 0x710
+  __DATA.__objc_selrefs: 0xc8
+  __DATA.__objc_data: 0x178
+  __DATA.__data: 0x488
+  __DATA.__common: 0x80
+  __DATA.__bss: 0xe80
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /System/Library/PrivateFrameworks/ApplePushService.framework/ApplePushService
   - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 244
-  Symbols:   246
-  CStrings:  182
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 256
+  Symbols:   240
+  CStrings:  153
 
Symbols:
+ _$s10Foundation12URLQueryItemV4name5valueACSSh_SSSghtcfC
+ _$s10Foundation12URLQueryItemVMa
+ _$s10Foundation12URLQueryItemVMn
+ _$s10Foundation3URLV9appending10queryItemsACSayAA12URLQueryItemVG_tF
+ _$s10Foundation3URLVs23CustomStringConvertibleAAMc
+ _$sSDyxq_GSesSeRzSeR_rlMc
+ _$sSSSesWP
+ _$ss22KeyedDecodingContainerV6decode_6forKeyS2Sm_xtKF
+ _$ss23CustomStringConvertibleP11descriptionSSvgTj
+ _MobileGestalt_copy_serialNumber_obj
+ _MobileGestalt_get_current_device
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
+ _swift_arrayInitWithTakeBackToFront
+ _swift_arrayInitWithTakeFrontToBack
- _$s10Foundation3URLVSeAAMc
- _$s10Foundation4DateV19_bridgeToObjectiveCSo6NSDateCyF
- _$s10Foundation4DateVMa
- _$s10Foundation4DateVMn
- _$s10Foundation4DateVSeAAMc
- _$s10Foundation4UUIDV10uuidStringSSvg
- _$s10Foundation4UUIDVACycfC
- _$s10Foundation4UUIDVMa
- _$sSSSHsWP
- _$sSqMa
- _$ss11AnyHashableV13_rawHashValue4seedS2i_tF
- _$ss11AnyHashableV2eeoiySbAB_ABtFZ
- _$ss11AnyHashableVyABxcSHRzlufC
- _$ss22KeyedDecodingContainerV15decodeIfPresent_6forKeySSSgSSm_xtKF
- _$ss22KeyedDecodingContainerV15decodeIfPresent_6forKeySbSgSbm_xtKF
- _OBJC_CLASS_$_UNMutableNotificationContent
- _OBJC_CLASS_$_UNNotificationRequest
- _OBJC_CLASS_$_UNNotificationSound
- _OBJC_CLASS_$_UNUserNotificationCenter
- _swift_bridgeObjectRetain_n
- _swift_dynamicCast
- _swift_getEnumTagSinglePayloadGeneric
- _swift_getObjCClassFromMetadata
- _swift_getSingletonMetadata
- _swift_initStructMetadata
- _swift_storeEnumTagSinglePayloadGeneric
- _swift_updateClassMetadata2
CStrings:
+ "Division by zero"
+ "Division results in an overflow"
+ "Failed to decode push payload %!{(MISSING)public}s with error: %!{(MISSING)public}@"
+ "Opening URL %!s(MISSING)"
+ "Swift/IntegerTypes.swift"
+ "UnsafeMutablePointer.initialize with negative count"
+ "defaultActionParams"
+ "newSession"
- "Error posting user notification for Diagnostics: %!@(MISSING)"
- "Error posting user notification for Support App: %!@(MISSING)"
- "Failed to decode push payload %!s(MISSING) with error: %!@(MISSING)"
- "Failed to decode push payload: %!s(MISSING)"
- "User notifications are not authorized for Diagnostics: %!@(MISSING)"
- "User notifications are not authorized for Support App: %!@(MISSING)"
- "_TtC16diagnosticspushd33SupportAppUserNotificationManager"
- "_TtC16diagnosticspushd34DiagnosticsUserNotificationManager"
- "addNotificationRequest:withCompletionHandler:"
- "alert"
- "category is required in payload when style is notification"
- "com.apple.Diagnostics"
- "com.apple.supportapp.notifications"
- "defaultActionURL"
- "defaultLaunchDiagsURL"
- "defaultSound"
- "initWithBundleIdentifier:"
- "notification"
- "notificationCenter"
- "requestAuthorizationWithOptions:completionHandler:"
- "requestWithIdentifier:content:trigger:"
- "setBody:"
- "setDefaultActionURL:"
- "setExpirationDate:"
- "setInterruptionLevel:"
- "setShouldIgnoreDoNotDisturb:"
- "setShouldIgnoreDowntime:"
- "setSound:"
- "setSubtitle:"
- "setTitle:"
- "shouldIgnoreDoNotDisturb"
- "shouldIgnoreDowntime"
- "supportApp"
- "timberLorry"
- "userNotification"
- "v16@?0@\"NSError\"8"
- "v20@?0B8@\"NSError\"12"

```
