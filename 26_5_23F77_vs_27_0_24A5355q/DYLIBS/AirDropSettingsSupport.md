## AirDropSettingsSupport

> `/System/Library/PrivateFrameworks/AirDropSettingsSupport.framework/AirDropSettingsSupport`

```diff

-1230.5.1.0.0
-  __TEXT.__text: 0x4140
-  __TEXT.__auth_stubs: 0x4c0
+1257.0.0.0.0
+  __TEXT.__text: 0x3f90
   __TEXT.__objc_methlist: 0x184
   __TEXT.__const: 0x2da
   __TEXT.__swift5_typeref: 0x89

   __TEXT.__swift5_types: 0xc
   __TEXT.__swift_as_entry: 0xc
   __TEXT.__swift_as_ret: 0x10
+  __TEXT.__swift_as_cont: 0x20
   __TEXT.__oslogstring: 0xf1
   __TEXT.__cstring: 0x48
-  __TEXT.__unwind_info: 0x1d8
-  __TEXT.__eh_frame: 0x258
-  __TEXT.__objc_classname: 0xc6
-  __TEXT.__objc_methname: 0x46b
-  __TEXT.__objc_methtype: 0xea
-  __TEXT.__objc_stubs: 0x180
-  __DATA_CONST.__got: 0x68
-  __DATA_CONST.__const: 0x110
+  __TEXT.__unwind_info: 0x1d0
+  __TEXT.__eh_frame: 0x250
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x100
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x128
   __DATA_CONST.__objc_protorefs: 0x10
-  __AUTH_CONST.__auth_got: 0x268
+  __DATA_CONST.__got: 0x68
   __AUTH_CONST.__const: 0x48
   __AUTH_CONST.__objc_const: 0x2e8
-  __AUTH.__objc_data: 0x50
-  __AUTH.__data: 0xb0
-  __DATA.__data: 0x160
+  __AUTH_CONST.__auth_got: 0x298
+  __DATA.__data: 0x138
   __DATA.__bss: 0x1b0
-  __DATA.__common: 0x20
-  __DATA_DIRTY.__objc_data: 0xe8
-  __DATA_DIRTY.__data: 0x68
+  __DATA_DIRTY.__objc_data: 0x138
+  __DATA_DIRTY.__data: 0x138
   __DATA_DIRTY.__bss: 0x80
+  __DATA_DIRTY.__common: 0x20
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/SwiftUI.framework/SwiftUI
   - /System/Library/Frameworks/UIKit.framework/UIKit

   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
-  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
-  - /usr/lib/swift/libswiftVideoToolbox.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 64DCABB0-6726-3800-A775-A888E1520B4B
-  Functions: 119
-  Symbols:   175
-  CStrings:  79
+  UUID: F4F50079-D606-320D-847B-790C8A272433
+  Functions: 116
+  Symbols:   178
+  CStrings:  8
 
Symbols:
+ ___swift_async_cont_functlets
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x23
+ _swift_release_x24
+ _swift_release_x8
- ___chkstk_darwin
- __swift_FORCE_LOAD_$_swiftCoreMedia
- __swift_FORCE_LOAD_$_swiftCoreMedia_$_AirDropSettingsSupport
- __swift_FORCE_LOAD_$_swiftVideoToolbox
- __swift_FORCE_LOAD_$_swiftVideoToolbox_$_AirDropSettingsSupport
- _objc_retainAutoreleasedReturnValue
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@24@0:8:16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "AirDropSettingsSupport"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "NSObject"
- "Q16@0:8"
- "SFAirDropDiscoveryControllerDelegate"
- "T#,R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TQ,R"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_$observationRegistrar"
- "_TtC22AirDropSettingsSupport20AirDropSettingsState"
- "_TtC22AirDropSettingsSupport23KnownContactsDataSource"
- "_contacts"
- "airDropDiscoveryController"
- "autorelease"
- "class"
- "conformsToProtocol:"
- "dealloc"
- "debugDescription"
- "description"
- "discoverableMode"
- "discoveryControllerLegacyModePropertiesDidChange:"
- "discoveryControllerSettingsDidChange:"
- "discoveryControllerVisibilityDidChange:"
- "effectiveDiscoverableMode"
- "effectiveIsCellularUsageEnabled"
- "effectiveIsNearbySharingEnabled"
- "hash"
- "init"
- "invalidate"
- "isCellularUsageEnabled"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isNearbySharingEnabled"
- "isNearbySharingSupported"
- "isProxy"
- "isTimeLimitedEveryoneMode"
- "knownContactsDataSource"
- "logger"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "release"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "setCellularUsageEnabled:"
- "setDelegate:"
- "setDiscoverableMode:"
- "setNearbySharingEnabled:"
- "startNFCMonitoring"
- "superclass"
- "v16@0:8"
- "v24@0:8@\"SFAirDropDiscoveryController\"16"
- "v24@0:8@16"
- "zone"

```
