## HomeEnergyWidgetsExtension

> `/private/var/staged_system_apps/Home.app/PlugIns/HomeEnergyWidgetsExtension.appex/HomeEnergyWidgetsExtension`

```diff

-946.5.0.0.0
-  __TEXT.__text: 0x33678
-  __TEXT.__auth_stubs: 0x14d0
+956.0.0.0.0
+  __TEXT.__text: 0x38a6c
+  __TEXT.__auth_stubs: 0x15d0
   __TEXT.__objc_methlist: 0x20
   __TEXT.__const: 0x13b4
-  __TEXT.__swift5_typeref: 0xe46
-  __TEXT.__swift5_capture: 0x130
-  __TEXT.__cstring: 0xfdf
+  __TEXT.__cstring: 0x102f
   __TEXT.__constg_swiftt: 0x52c
-  __TEXT.__objc_methname: 0x380
+  __TEXT.__swift5_typeref: 0xf42
+  __TEXT.__objc_methname: 0x34d
   __TEXT.__swift5_reflstr: 0x406
   __TEXT.__swift5_fieldmd: 0x3c0
-  __TEXT.__oslogstring: 0x1258
+  __TEXT.__swift5_capture: 0xf4
+  __TEXT.__oslogstring: 0x13a8
   __TEXT.__swift5_proto: 0xf8
   __TEXT.__swift5_types: 0x60
   __TEXT.__objc_classname: 0x1f

   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x990
-  __TEXT.__eh_frame: 0x115c
-  __DATA_CONST.__auth_got: 0xa68
-  __DATA_CONST.__got: 0x430
-  __DATA_CONST.__auth_ptr: 0x680
-  __DATA_CONST.__const: 0x808
+  __TEXT.__unwind_info: 0x9d0
+  __TEXT.__eh_frame: 0x1194
+  __DATA_CONST.__auth_got: 0xae8
+  __DATA_CONST.__got: 0x410
+  __DATA_CONST.__auth_ptr: 0x698
+  __DATA_CONST.__const: 0x790
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA.__objc_const: 0x570
-  __DATA.__objc_selrefs: 0xb8
+  __DATA.__objc_selrefs: 0xa8
   __DATA.__objc_data: 0xd8
-  __DATA.__data: 0xd80
+  __DATA.__data: 0xdb8
   __DATA.__common: 0xb8
   __DATA.__bss: 0x1f58
   - /System/Library/Frameworks/AppIntents.framework/AppIntents

   - /System/Library/Frameworks/HomeKit.framework/HomeKit
   - /System/Library/Frameworks/SwiftUI.framework/SwiftUI
   - /System/Library/Frameworks/WidgetKit.framework/WidgetKit
-  - /System/Library/Frameworks/_AppIntents_UIKit.framework/_AppIntents_UIKit
   - /System/Library/PrivateFrameworks/CalendarFoundation.framework/CalendarFoundation
   - /System/Library/PrivateFrameworks/EnergyKit.framework/EnergyKit
   - /System/Library/PrivateFrameworks/EnergyKitFoundation.framework/EnergyKitFoundation

   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 668
-  Symbols:   161
-  CStrings:  261
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 686
+  Symbols:   166
+  CStrings:  266
 
Symbols:
+ __os_signpost_emit_with_name_impl
+ __swiftEmptyDictionarySingleton
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
+ _bzero
- _OBJC_CLASS_$_CLGeocoder
- _OBJC_CLASS_$_CLPlacemark
- _swift_continuation_await
- _swift_continuation_init
- _swift_continuation_throwingResume
- _swift_continuation_throwingResumeWithError
CStrings:
+ "%!s(MISSING) (%!l(MISSING)d homes available."
+ "%!s(MISSING) Creating entity for home '%!s(MISSING)' with energySiteID: %!s(MISSING) & multiHome: %!{(MISSING)bool}d"
+ "%!s(MISSING) Found %!l(MISSING)d home(s) with an onboarded utility)"
+ "%!s(MISSING) No SiteDetail provided. ***Attempting Fallback to first onboarded home***"
+ "%!s(MISSING) No onboarded homes found! (returning error SiteDetail: <NO ONBOARDED HOMES ERROR>)"
+ "%!s(MISSING) Site %!s(MISSING) found, but home not onboarded: ignoring"
+ "%!s(MISSING) Site %!s(MISSING) onboarded for '%!s(MISSING)', adding to list..."
+ "%!s(MISSING) Site can not be found for home'%!s(MISSING)': ignoring"
+ "%!s(MISSING) SiteDetail provided with non-nil siteID: %!s(MISSING)"
+ "%!s(MISSING) filtering for utility onboarded homes with these IDs: %!s(MISSING), FOUND %!l(MISSING)d: %!s(MISSING)"
+ "%!s(MISSING) found %!l(MISSING)d onboarded homes"
+ "%!s(MISSING) returning all utility onboarded homes: %!s(MISSING)"
+ "%!s(MISSING) returning: %!s(MISSING)"
+ "%!s(MISSING): No site for available, erroring out widget. asking for 60 minute reload %!@(MISSING)"
+ "%!s(MISSING): Retrieved week snapshot for widget %!s(MISSING)"
+ "%!s(MISSING): Subscription disconnected, erroring out widget. Asking for 60 minute reload"
+ "%!s(MISSING): historical usage loading failed, erroring out widget, asking for 60 minute reload: %!@(MISSING)"
+ "<NO ONBOARDED HOMES ERROR>"
+ "HistoricalUsageWidgetConfiguration init without siteDetail..."
+ "HomeManagerWarmUp"
+ "WidgetConf with site detail: "
+ "[Error] Interval already ended"
+ "homesOnboardedForUtilityFeatures()"
+ "utilityOnboardedHomes()"
- "%!s(MISSING) Creating entity for home '%!s(MISSING)' with energySiteID: %!s(MISSING)"
- "%!s(MISSING) Found %!l(MISSING)d homes setting multiHome to %!{(MISSING)bool}d"
- "%!s(MISSING) Found %!l(MISSING)d onboarded home(s)"
- "%!s(MISSING) NO onboarded homes found!, returning error SiteDetail"
- "%!s(MISSING) Site can not be found for home: '%!s(MISSING)'... skipping"
- "%!s(MISSING) Unable to get timezone"
- "%!s(MISSING) no location found, skipping update ..."
- "%!s(MISSING) updating timeZone..."
- "%!s(MISSING) updating to location... %!s(MISSING)"
- "%!s(MISSING): No site for available, erroring out widget. Unrecoverable error: %!@(MISSING)"
- "%!s(MISSING): Unrecoverable error, will not reload: %!@(MISSING)"
- "%!s(MISSING): historical usage loading failed, erroring out widget. Unrecoverable error: %!@(MISSING)"
- "Error while trying to update location or timezone: %!@(MISSING)"
- "Error: Not geocoding due to invalid location: %!s(MISSING)"
- "configuredHomes()"
- "reverseGeocodeLocation:completionHandler:"
- "timeZone"
- "updateTimeZoneAndLocationForEnergySite(_:location:)"
- "v24@?0@\"NSArray\"8@\"NSError\"16"

```
