## DeviceDiscoveryUISettings

> `/System/Library/Settings/DeviceDiscoveryUISettings.settings/DeviceDiscoveryUISettings`

```diff

-2084.10.7.2.5
-  __TEXT.__text: 0x10e48
-  __TEXT.__auth_stubs: 0xbc0
+2086.10.3.2.2
+  __TEXT.__text: 0x11d4c
+  __TEXT.__auth_stubs: 0xc90
   __TEXT.__objc_stubs: 0x20
-  __TEXT.__const: 0x5b2
-  __TEXT.__objc_methname: 0x182
-  __TEXT.__cstring: 0x62f
+  __TEXT.__const: 0x5d2
+  __TEXT.__objc_methname: 0x1a8
+  __TEXT.__cstring: 0x92e
   __TEXT.__constg_swiftt: 0x178
-  __TEXT.__swift5_typeref: 0xeda
-  __TEXT.__swift5_reflstr: 0x151
-  __TEXT.__swift5_fieldmd: 0x160
+  __TEXT.__swift5_typeref: 0xf1c
+  __TEXT.__swift5_reflstr: 0x161
+  __TEXT.__swift5_fieldmd: 0x16c
   __TEXT.__swift5_assocty: 0xb0
-  __TEXT.__swift5_capture: 0x184
-  __TEXT.__oslogstring: 0x2a6
+  __TEXT.__swift5_capture: 0x198
+  __TEXT.__oslogstring: 0x246
   __TEXT.__swift5_proto: 0x2c
   __TEXT.__swift5_types: 0x1c
-  __TEXT.__swift_as_entry: 0x30
-  __TEXT.__swift_as_ret: 0x30
-  __TEXT.__unwind_info: 0x470
-  __TEXT.__eh_frame: 0x848
-  __DATA_CONST.__auth_got: 0x5e8
-  __DATA_CONST.__got: 0x1e8
-  __DATA_CONST.__auth_ptr: 0x280
-  __DATA_CONST.__const: 0x668
+  __TEXT.__swift_as_entry: 0x34
+  __TEXT.__swift_as_ret: 0x38
+  __TEXT.__unwind_info: 0x480
+  __TEXT.__eh_frame: 0x8c8
+  __DATA_CONST.__auth_got: 0x650
+  __DATA_CONST.__got: 0x1f0
+  __DATA_CONST.__auth_ptr: 0x288
+  __DATA_CONST.__const: 0x698
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x1a0
-  __DATA.__objc_selrefs: 0x90
+  __DATA.__objc_selrefs: 0xa0
   __DATA.__objc_data: 0x50
-  __DATA.__data: 0x4e8
+  __DATA.__data: 0x508
   __DATA.__bss: 0x600
   - /System/Library/Frameworks/AccessorySetupKit.framework/AccessorySetupKit
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/PrivateFrameworks/DeviceDiscoveryUICore.framework/DeviceDiscoveryUICore
   - /System/Library/PrivateFrameworks/IconServices.framework/IconServices
   - /System/Library/PrivateFrameworks/Settings.framework/Settings
+  - /System/Library/PrivateFrameworks/Sharing.framework/Sharing
   - /System/Library/PrivateFrameworks/_IconServices_SwiftUI.framework/_IconServices_SwiftUI
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: FE02385C-4812-300A-9A23-9588432CBF8D
-  Functions: 298
-  Symbols:   136
-  CStrings:  59
+  UUID: CA6B38AF-1BF9-31DA-9754-629554588439
+  Functions: 311
+  Symbols:   140
+  CStrings:  66
 
Symbols:
+ _SFIsGreenTeaDevice
+ __Block_copy
+ __Block_release
+ __swiftEmptyDictionarySingleton
+ _objc_release_x26
+ _objc_retain_x20
+ _objc_retain_x26
+ _swift_bridgeObjectRetain_n
+ _swift_retain_n
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- _objc_claimAutoreleasedReturnValue
CStrings:
+ "Accessing Environment's value outside of being installed on a View. This will always read the default value and will not update."
+ "All paired devices and WLAN accessories will be forgotten, and will no longer detect when this iPad is nearby and connect automatically."
+ "Filtering out %@ due to activating state: %s"
+ "Paired devices use this iPad’s WLAN Identifier to detect when it is nearby and to connect automatically in compatible apps."
+ "Paired devices use this iPhone’s WLAN Identifier to detect when it is nearby and to connect automatically in compatible apps."
+ "This device will no longer connect automatically using WLAN, but will still be able to determine when this iPad is nearby."
+ "This device will no longer connect automatically using WLAN, but will still be able to determine when this iPhone is nearby."
+ "resetWiFiButtonTitle"
+ "setEventHandler:"
+ "v16@?0@\"DAEvent\"8"
- "Accessing Environment<%s>'s value outside of being installed on a View. This will always read the default value and will not update."
- "Optional<Binding<EditMode>>"
- "Reset Wi-Fi Identifier"

```
