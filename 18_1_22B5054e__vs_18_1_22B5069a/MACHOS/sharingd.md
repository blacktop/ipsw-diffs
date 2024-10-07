## sharingd

> `/usr/libexec/sharingd`

```diff

-1968.20.31.0.0
-  __TEXT.__text: 0x6726cc
+1968.20.61.2.1
+  __TEXT.__text: 0x673608
   __TEXT.__auth_stubs: 0x90a0
-  __TEXT.__objc_stubs: 0x345c0
-  __TEXT.__objc_methlist: 0x1c524
-  __TEXT.__const: 0x1011c
-  __TEXT.__cstring: 0x457a3
-  __TEXT.__objc_methname: 0x49221
-  __TEXT.__oslogstring: 0x39409
+  __TEXT.__objc_stubs: 0x345a0
+  __TEXT.__objc_methlist: 0x1c4fc
+  __TEXT.__const: 0x101a4
+  __TEXT.__cstring: 0x45703
+  __TEXT.__objc_methname: 0x491f0
+  __TEXT.__oslogstring: 0x39459
   __TEXT.__objc_classname: 0x2dbb
   __TEXT.__objc_methtype: 0xa1be
-  __TEXT.__gcc_except_tab: 0x6ad8
+  __TEXT.__gcc_except_tab: 0x6aa8
   __TEXT.__ustring: 0x94
   __TEXT.__dlopen_cstrs: 0x31b
-  __TEXT.__swift5_typeref: 0x83fc
+  __TEXT.__swift5_typeref: 0x841a
   __TEXT.__swift5_fieldmd: 0x67d4
-  __TEXT.__constg_swiftt: 0x88bc
-  __TEXT.__swift5_builtin: 0x2d0
+  __TEXT.__constg_swiftt: 0x88cc
+  __TEXT.__swift5_builtin: 0x2e4
   __TEXT.__swift5_reflstr: 0x5c37
-  __TEXT.__swift5_assocty: 0xea0
+  __TEXT.__swift5_assocty: 0xeb8
   __TEXT.__swift5_protos: 0x1a0
-  __TEXT.__swift5_proto: 0xe1c
-  __TEXT.__swift5_types: 0x67c
-  __TEXT.__swift5_capture: 0x3b54
+  __TEXT.__swift5_proto: 0xe24
+  __TEXT.__swift5_types: 0x680
+  __TEXT.__swift5_capture: 0x3bac
   __TEXT.__swift5_mpenum: 0x14
-  __TEXT.__unwind_info: 0x12a50
-  __TEXT.__eh_frame: 0x1ea48
+  __TEXT.__unwind_info: 0x12aa8
+  __TEXT.__eh_frame: 0x1ebb0
   __DATA_CONST.__auth_got: 0x4860
   __DATA_CONST.__got: 0x31e0
-  __DATA_CONST.__auth_ptr: 0x1e40
-  __DATA_CONST.__const: 0x19c50
-  __DATA_CONST.__cfstring: 0x197a0
+  __DATA_CONST.__auth_ptr: 0x1e38
+  __DATA_CONST.__const: 0x19cf8
+  __DATA_CONST.__cfstring: 0x19740
   __DATA_CONST.__objc_classlist: 0xe58
-  __DATA_CONST.__objc_catlist: 0x40
+  __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x6d0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x250

   __DATA_CONST.__objc_dictobj: 0x16f8
   __DATA_CONST.__objc_arrayobj: 0x6f0
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA.__objc_const: 0x3e4d0
-  __DATA.__objc_selrefs: 0x107a8
+  __DATA.__objc_const: 0x3e490
+  __DATA.__objc_selrefs: 0x10798
   __DATA.__objc_ivar: 0x2a68
   __DATA.__objc_data: 0xac60
-  __DATA.__data: 0x16898
-  __DATA.__bss: 0x11b38
+  __DATA.__data: 0x168a0
+  __DATA.__bss: 0x11c38
   __DATA.__common: 0x9c0
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts

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
-  Functions: 24400
-  Symbols:   4187
-  CStrings:  27650
+  Functions: 24412
+  Symbols:   4188
+  CStrings:  27642
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit
CStrings:
+ "AirDrop not ready: wifi=%!d(MISSING), bluetooth=%!d(MISSING), carplay=%!d(MISSING), receivingEnabled=%!d(MISSING), isVirtualMachine=%!d(MISSING) isMulticastAdvertisementsDisabled=%!d(MISSING)"
+ "Asked to list all eligible devices for: %!s(MISSING)"
+ "Requesting new banner while previous banner dismissal was requested but not completed. Cleaning up previous banner"
+ "UNLOCK_WATCH_46MM_SIZE"
+ "WifiModeChange: wirelessAccessPoint: %!d(MISSING) computerToComputer: %!d(MISSING)"
+ "WifiPowerChange: wirelessEnabled: %!d(MISSING)"
+ "WifiState: wirelessEnabled: %!@(MISSING) - isUsing2GHz: %!@(MISSING) - isWifiPersonalHotspot: %!@(MISSING)\n"
+ "listEligibleDevices for %!s(MISSING) returning eligible %!s(MISSING) devices: %!{(MISSING)public}s"
+ "listEligibleDevicesFor:completionHandler:"
+ "v32@0:8Q16@?<v@?@\"NSSet\">24"
- "AIRDROP_PERSONAL_HOTSPOT_SUBTITLE"
- "AIRDROP_PERSONAL_HOTSPOT_TITLE"
- "AirDrop not ready: wifi=%!d(MISSING), bluetooth=%!d(MISSING), hotspot=%!d(MISSING), carplay=%!d(MISSING), receivingEnabled=%!d(MISSING), isVirtualMachine=%!d(MISSING) isMulticastAdvertisementsDisabled=%!d(MISSING)"
- "Asking user to disable Personal Hotspot"
- "DaemoniOSLibrary"
- "ENABLE_BUTTON_TITLE"
- "Error presenting disable Personal Hotspot alert %!@(MISSING)"
- "Localizable-N217"
- "Turning on AirDrop, disabling Personal Hotspot"
- "WILL_TURN_OFF_PERSONAL_HOTSPOT_BODY"
- "WILL_TURN_OFF_PERSONAL_HOTSPOT_TITLE"
- "WifiMode: wirelessAccessPoint: %!d(MISSING) computerToComputer: %!d(MISSING)"
- "WifiPowerOn: _wirelessEnabled: %!d(MISSING)"
- "WifiState: isUsing2GHz: %!@(MISSING) - isWifiPersonalHotspot: %!@(MISSING)\n"
- "listEligibleDevices for %!s(MISSING) returning eligible %!s(MISSING) devices: %!s(MISSING)"
- "listEligibleDevicesFor:completion:"
- "personalHotspotAlert"
- "presentDisablePersonalHotspotAlert"

```
