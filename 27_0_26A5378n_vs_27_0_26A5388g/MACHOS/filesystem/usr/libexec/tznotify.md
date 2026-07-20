## tznotify

> `/usr/libexec/tznotify`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_entry`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_types`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__auth_ptr`

```diff

-89.0.0.0.0
-  __TEXT.__text: 0x6d28
-  __TEXT.__auth_stubs: 0x640
+90.0.0.0.0
+  __TEXT.__text: 0x6e84
+  __TEXT.__auth_stubs: 0x670
   __TEXT.__objc_stubs: 0x320
-  __TEXT.__objc_methlist: 0x1cc
-  __TEXT.__const: 0x1b8
-  __TEXT.__cstring: 0x7f3
+  __TEXT.__objc_methlist: 0x17c
+  __TEXT.__const: 0x1a8
+  __TEXT.__objc_classname: 0x88
+  __TEXT.__cstring: 0x923
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__objc_classname: 0xad
-  __TEXT.__objc_methname: 0x5bc
-  __TEXT.__objc_methtype: 0x264
+  __TEXT.__objc_methname: 0x516
+  __TEXT.__objc_methtype: 0x202
   __TEXT.__constg_swiftt: 0x74
-  __TEXT.__swift5_typeref: 0x1d7
+  __TEXT.__swift5_typeref: 0x1a5
   __TEXT.__swift5_reflstr: 0x59
   __TEXT.__swift5_fieldmd: 0x74
-  __TEXT.__swift5_capture: 0x80
+  __TEXT.__swift5_capture: 0x9c
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x1d0
+  __TEXT.__unwind_info: 0x1d8
   __TEXT.__eh_frame: 0x1c8
-  __DATA_CONST.__const: 0x2d8
-  __DATA_CONST.__objc_classlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x70
+  __DATA_CONST.__const: 0x2f8
+  __DATA_CONST.__objc_classlist: 0x10
+  __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x38
-  __DATA_CONST.__auth_got: 0x328
-  __DATA_CONST.__got: 0x130
+  __DATA_CONST.__objc_protorefs: 0x20
+  __DATA_CONST.__auth_got: 0x340
+  __DATA_CONST.__got: 0x140
   __DATA_CONST.__auth_ptr: 0x70
-  __DATA.__objc_const: 0x588
-  __DATA.__objc_selrefs: 0x1b0
-  __DATA.__objc_data: 0xd0
-  __DATA.__data: 0x458
+  __DATA.__objc_const: 0x558
+  __DATA.__objc_selrefs: 0x190
+  __DATA.__objc_data: 0x120
+  __DATA.__data: 0x338
   __DATA.__common: 0x80
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/UserNotifications.framework/Versions/A/UserNotifications
-  - /System/Library/PrivateFrameworks/ChronoServices.framework/Versions/A/ChronoServices
+  - /System/Library/PrivateFrameworks/MobileTimer.framework/Versions/A/MobileTimer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
-  - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
-  - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib
-  - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
-  - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
-  - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 108
-  Symbols:   176
-  CStrings:  138
+  Functions: 113
+  Symbols:   175
+  CStrings:  129
 
Symbols:
+ _$sSS10describingSSx_tclufC
+ _$sSa10FoundationE34_conditionallyBridgeFromObjectiveC_6resultSbSo7NSArrayC_SayxGSgztFZ
+ _$sSo8NSStringC10FoundationE13stringLiteralABs12StaticStringV_tcfC
+ _OBJC_CLASS_$_MTWidgetUtilities
+ _OBJC_CLASS_$_NSString
+ _OBJC_CLASS_$_UNNotificationIcon
+ __CFPreferencesCopyAppValueWithContainer
+ _objc_claimAutoreleasedReturnValue
+ _swift_errorRetain
+ _swift_getObjectType
- _$sSa10FoundationE36_unconditionallyBridgeFromObjectiveCySayxGSo7NSArrayCSgFZ
- _$ss12_ArrayBufferV19_getElementSlowPathyyXlSiFyXl_Ts5
- _$ss18_CocoaArrayWrapperV8endIndexSivg
- _CFPreferencesCopyAppValue
- _OBJC_CLASS_$_CHSWidgetConfigurationReader
- __swift_FORCE_LOAD_$_swiftAccelerate
- __swift_FORCE_LOAD_$_swiftCoreLocation
- __swift_FORCE_LOAD_$_swiftIntents
- __swift_FORCE_LOAD_$_swiftOSLog
- __swift_FORCE_LOAD_$_swiftQuartzCore
- __swift_FORCE_LOAD_$_swiftsimd
CStrings:
+ "TZNotificationIcon"
+ "Widget zones returned as nil"
+ "Widget zones returned as unexpected type: %{public}@"
+ "World clock cities not in correct format: %{public}@"
+ "World clock preferences missing from Clock.app container"
+ "World clock time zones: %{public}@"
+ "addCompletionBlock:"
+ "com.apple.systempreferences"
+ "iconForApplicationIdentifier:"
+ "setIcon:"
+ "setIconForApplicationIdentifier:onContent:"
+ "stringByExpandingTildeInPath"
+ "timeZonesForCurrentClockWidgets"
+ "timeZonesForCurrentClockWidgets() returned error %{public}@"
+ "~/Library/Containers/com.apple.clock/Data"
- "@\"CHSWidget\"16@0:8"
- "@\"NSArray\"16@0:8"
- "@\"NSArray\"24@0:8@\"NSString\"16"
- "@24@0:8@16"
- "@24@0:8^{_NSZone=}16"
- "CHSWidgetConfigurationHost"
- "CHSWidgetConfigurationReference"
- "ClocksSingleIntent"
- "NSCopying"
- "T@\"CHSWidget\",R,C,N"
- "T@\"NSArray\",R,C,N"
- "T@\"NSString\",R,C,N"
- "World clock cities not in correct format"
- "World clock preferences missing"
- "_className"
- "allConfiguredWidgetsWithCompletion:"
- "copyWithZone:"
- "identifier"
- "intent"
- "uniqueIdentifier"
- "valueForKey:"
- "widget"
- "widgetConfigurations"
- "widgetConfigurationsForApplicationContainerBundleIdentifier:"
```
