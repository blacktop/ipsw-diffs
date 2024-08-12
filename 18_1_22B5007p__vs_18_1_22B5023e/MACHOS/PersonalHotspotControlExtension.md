## PersonalHotspotControlExtension

> `/System/Library/ExtensionKit/Extensions/PersonalHotspotControlExtension.appex/PersonalHotspotControlExtension`

```diff

-980.90.0.0.0
-  __TEXT.__text: 0x4838
-  __TEXT.__auth_stubs: 0x660
-  __TEXT.__objc_methlist: 0x14
-  __TEXT.__const: 0x364
+980.101.0.0.0
+  __TEXT.__text: 0x5cc8
+  __TEXT.__auth_stubs: 0x6e0
+  __TEXT.__objc_methlist: 0x20
+  __TEXT.__const: 0x374
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x1a8
-  __TEXT.__swift5_typeref: 0x17c
-  __TEXT.__swift5_fieldmd: 0x74
-  __TEXT.__swift5_reflstr: 0x3c
+  __TEXT.__constg_swiftt: 0x1f0
+  __TEXT.__swift5_typeref: 0x1b8
+  __TEXT.__swift5_fieldmd: 0x98
+  __TEXT.__swift5_reflstr: 0xa8
   __TEXT.__swift5_assocty: 0x68
-  __TEXT.__objc_methname: 0x18
+  __TEXT.__objc_methname: 0x28
   __TEXT.__swift5_proto: 0x1c
   __TEXT.__swift5_types: 0x14
-  __TEXT.__cstring: 0x5ff
-  __TEXT.__oslogstring: 0x4e3
+  __TEXT.__cstring: 0x75f
+  __TEXT.__oslogstring: 0x57c
   __TEXT.__swift5_capture: 0x20
-  __TEXT.__unwind_info: 0x190
-  __TEXT.__eh_frame: 0x40
-  __DATA_CONST.__auth_got: 0x330
-  __DATA_CONST.__got: 0xa0
-  __DATA_CONST.__auth_ptr: 0x1a8
-  __DATA_CONST.__const: 0x260
+  __TEXT.__unwind_info: 0x1b8
+  __TEXT.__eh_frame: 0x68
+  __DATA_CONST.__auth_got: 0x370
+  __DATA_CONST.__got: 0xb8
+  __DATA_CONST.__auth_ptr: 0x1b8
+  __DATA_CONST.__const: 0x250
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0xd8
-  __DATA.__objc_selrefs: 0x18
-  __DATA.__objc_data: 0x108
-  __DATA.__data: 0x180
+  __DATA.__objc_const: 0x140
+  __DATA.__objc_selrefs: 0x20
+  __DATA.__objc_data: 0x168
+  __DATA.__data: 0x1d8
   __DATA.__bss: 0x380
-  __DATA.__common: 0x30
+  __DATA.__common: 0x80
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
-  - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/SwiftUI.framework/SwiftUI
   - /System/Library/Frameworks/WidgetKit.framework/WidgetKit
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/MobileWiFi.framework/MobileWiFi
   - /System/Library/PrivateFrameworks/Netrb.framework/Netrb
   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore

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
-  Functions: 108
-  Symbols:   100
-  CStrings:  62
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 117
+  Symbols:   112
+  CStrings:  76
 
Symbols:
+ _AnalyticsSendEventLazy
+ _OBJC_CLASS_$_NSString
+ __swiftEmptyDictionarySingleton
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
+ _objc_autoreleaseReturnValue
+ _objc_retain_x23
+ _objc_retain_x26
+ _swift_initStackObject
- _kCFAllocatorDefault
- _objc_release_x24
- _objc_retain_x27
CStrings:
+ "$__lazy_storage_$_cellularClient"
+ "$__lazy_storage_$_misClient"
+ "$__lazy_storage_$_wifiClient"
+ "%!s(MISSING): MIS state=%!{(MISSING)bool}d"
+ "%!s(MISSING): cellular states: capable:%!{(MISSING)bool}d, enabled: %!{(MISSING)bool}d, airplaneMode: %!{(MISSING)bool}d"
+ "%!s(MISSING): current global service state=%!u(MISSING), reason=%!u(MISSING)"
+ "%!s(MISSING): failed to get cellular connection"
+ "%!s(MISSING): failed to get wifiClient"
+ "%!s(MISSING): failed to get wifiClient, defaulting to widget disabled"
+ "%!s(MISSING): getting global service state=%!u(MISSING), MIS discovery state=%!{(MISSING)bool}d, connectionCount=%!l(MISSING)d"
+ "%!s(MISSING): getting subtitle='%!s(MISSING)' global service state=%!u(MISSING), getting discoverable state=%!{(MISSING)bool}d, connectionCount=%!l(MISSING)d"
+ "%!s(MISSING): global service state=%!u(MISSING), widget using icon='%!s(MISSING)'"
+ "%!s(MISSING): gobal service state=%!u(MISSING)"
+ "%!s(MISSING): setting GlobalServiceState to ON"
+ "%!s(MISSING): setting MIS state to='%!{(MISSING)bool}d'"
+ "%!s(MISSING): setting global service state to='%!u(MISSING)'"
+ "%!s(MISSING): updating connections count=%!u(MISSING)"
+ "%!s(MISSING): widiget disabled=%!{(MISSING)bool}d, phModificationDisabled=%!{(MISSING)bool}d, phIsInoperative=%!{(MISSING)bool}d"
+ "@\"NSDictionary\"8@?0"
+ "Display name for control center widget"
+ "Turn off Personal Hotspot"
+ "cellularDataEnabled()"
+ "com.apple.wifi.ui.event"
+ "hint text to turn off personal hotspot"
+ "hint text to turn on personal hotspot"
+ "initWithString:"
+ "toggle-ph-control-center"
+ "v16@0:8"
- "%!s(MISSING): Turning on GlobalServiceState"
- "%!s(MISSING): Widget is disabled: %!{(MISSING)bool}d, phModificationDisabled:%!{(MISSING)bool}d, phIsInoperative:%!{(MISSING)bool}d"
- "%!s(MISSING): current global service state: %!u(MISSING), reason: %!u(MISSING)"
- "%!s(MISSING): getting MIS state: %!{(MISSING)bool}d"
- "%!s(MISSING): getting global service state: %!u(MISSING), getting MIS state: %!{(MISSING)bool}d, connectionCount: %!l(MISSING)d"
- "%!s(MISSING): getting subtitle(%!s(MISSING)) from: global service state: %!u(MISSING), getting disCoverable state: %!{(MISSING)bool}d, connectionCount: %!l(MISSING)d"
- "%!s(MISSING): global service state: %!u(MISSING), widget using icon:%!s(MISSING)"
- "%!s(MISSING): gobal service state: %!u(MISSING) when user toggles widget"
- "%!s(MISSING): setting MIS state to %!{(MISSING)bool}d"
- "%!s(MISSING): setting global service state to %!u(MISSING)"
- "%!s(MISSING): start setting MIS state"
- "%!s(MISSING): updating connections count to %!u(MISSING)"
- "Turn Off Personal Hotspot"
- "subtitle for global service off state"

```
