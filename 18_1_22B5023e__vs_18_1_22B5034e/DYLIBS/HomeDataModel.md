## HomeDataModel

> `/System/Library/PrivateFrameworks/HomeDataModel.framework/HomeDataModel`

```diff

-956.0.0.0.0
-  __TEXT.__text: 0x44c7c8
-  __TEXT.__auth_stubs: 0x2f90
+962.0.0.0.0
+  __TEXT.__text: 0x447540
+  __TEXT.__auth_stubs: 0x2fb0
   __TEXT.__objc_methlist: 0x9c8
-  __TEXT.__const: 0x225b8
-  __TEXT.__cstring: 0xecb6
-  __TEXT.__swift5_typeref: 0x980a
-  __TEXT.__constg_swiftt: 0x6fcc
-  __TEXT.__swift5_builtin: 0x2f8
-  __TEXT.__swift5_reflstr: 0x6b83
-  __TEXT.__swift5_fieldmd: 0x9648
-  __TEXT.__swift5_assocty: 0xe48
-  __TEXT.__swift5_proto: 0x212c
-  __TEXT.__swift5_types: 0x90c
-  __TEXT.__oslogstring: 0x3e7c
-  __TEXT.__swift5_mpenum: 0x1a8
-  __TEXT.__swift5_protos: 0x84
-  __TEXT.__swift5_capture: 0x177c
-  __TEXT.__swift5_types2: 0x10
-  __TEXT.__unwind_info: 0xdd60
-  __TEXT.__eh_frame: 0x1a3a4
+  __TEXT.__const: 0x22498
+  __TEXT.__cstring: 0xef3b
+  __TEXT.__swift5_typeref: 0x9310
+  __TEXT.__constg_swiftt: 0x6ff8
+  __TEXT.__swift5_builtin: 0x2d0
+  __TEXT.__swift5_reflstr: 0x6a33
+  __TEXT.__swift5_fieldmd: 0x95ac
+  __TEXT.__swift5_assocty: 0xf48
+  __TEXT.__swift5_proto: 0x21a4
+  __TEXT.__swift5_types: 0x8f8
+  __TEXT.__oslogstring: 0x41e3
+  __TEXT.__swift5_mpenum: 0x1b8
+  __TEXT.__swift5_protos: 0x88
+  __TEXT.__swift5_capture: 0x18cc
+  __TEXT.__swift5_types2: 0x14
+  __TEXT.__unwind_info: 0xdd28
+  __TEXT.__eh_frame: 0x1a214
   __TEXT.__objc_classname: 0x275
-  __TEXT.__objc_methname: 0x3e19
+  __TEXT.__objc_methname: 0x3e76
   __TEXT.__objc_methtype: 0xcc5
   __TEXT.__objc_stubs: 0x180
-  __DATA_CONST.__got: 0xbd0
-  __DATA_CONST.__const: 0xda0
+  __DATA_CONST.__got: 0xb90
+  __DATA_CONST.__const: 0xcd0
   __DATA_CONST.__objc_classlist: 0x150
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x170
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf60
+  __DATA_CONST.__objc_selrefs: 0xf78
   __DATA_CONST.__objc_protorefs: 0xb8
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x17d0
-  __AUTH_CONST.__auth_ptr: 0x12b8
-  __AUTH_CONST.__const: 0x16ca8
-  __AUTH_CONST.__cfstring: 0x40
-  __AUTH_CONST.__objc_const: 0x49a0
-  __AUTH.__objc_data: 0x1380
-  __AUTH.__data: 0x3780
-  __DATA.__data: 0x87d8
-  __DATA.__bss: 0x3ec80
-  __DATA.__common: 0x1d8
+  __AUTH_CONST.__auth_got: 0x17e0
+  __AUTH_CONST.__auth_ptr: 0x12a8
+  __AUTH_CONST.__const: 0x17248
+  __AUTH_CONST.__objc_const: 0x49e0
+  __AUTH.__objc_data: 0x1370
+  __AUTH.__data: 0x3980
+  __DATA.__data: 0x8540
+  __DATA.__bss: 0x3e670
+  __DATA.__common: 0x1c0
   __DATA_DIRTY.__objc_data: 0x448
-  __DATA_DIRTY.__data: 0x29a0
-  __DATA_DIRTY.__common: 0xf0
+  __DATA_DIRTY.__data: 0x29d0
+  __DATA_DIRTY.__common: 0xd0
   __DATA_DIRTY.__bss: 0x1600
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 17678
-  Symbols:   648
-  CStrings:  2621
+  Functions: 17689
+  Symbols:   658
+  CStrings:  2660
 
Symbols:
+ _dispatch_once
+ __os_log_error_impl
+ __NSConcreteGlobalBlock
+ _os_log_create
+ _objc_release_x1
- _OBJC_CLASS_$_HMWidgetManager
- _NSLog
- ___CFConstantStringClassReference
CStrings:
+ "NewControls"
+ "fetchStateForCharacteristics:completion:"
+ "Matter"
+ "_stream"
+ "perform(_:forKind:)"
+ "_ignoreNextUpdate"
+ "v24@?0@\"HMWidgetManagerFetchStateForActionSetsResponse\"8@\"NSError\"16"
+ "figure.walk.motion"
+ "uip_floating_tab_bar"
+ "_supportsBidirectionalAudio"
+ "removeDelegate:"
+ "fetchActionSets(configuration:_:isMonitoring:)"
+ "%!s(MISSING) Fetching actionSets: %!s(MISSING)"
+ "ControlCenter"
+ "Removing delegate for device (%!s(MISSING)) accessory: %!@(MISSING)"
+ "fetchState(for:)"
+ "stream(audioMode: "
+ "hdm_createDeviceWithController: Can't create MTRDevice for accessory (%!@(MISSING)) because it doesn't have a node ID!"
+ "unregisterForAccessories() has no effect in widgets context mode"
+ "registerForAccessories() has no effect in widgets context mode"
+ "%!s(MISSING) successfully delivered a response"
+ ",\navailability: "
+ "snapshot(snapshot: "
+ "v24@?0@\"HMWidgetManagerFetchStateResponse\"8@\"NSError\"16"
+ "updates"
+ "Setting up delegates for all devices in home: %!s(MISSING): %!s(MISSING)"
+ "_snapshot"
+ "unregisterForAccessories() called on %!s(MISSING)"
+ "removeMTRDeviceDelegates(in:)"
+ "%!s(MISSING):%!s(MISSING) device was expected to be of type MTRDevice %!s(MISSING)"
+ "supportsBidirectionalAudio"
+ "[%!s(MISSING)] %!s(MISSING) state: %!s(MISSING)"
+ "%!s(MISSING) Fetching characteristics: %!s(MISSING)"
+ "HomeDataModel/HomeKitMatterExtensions.swift"
+ "_configureMTRDeviceDelegate(for:shouldAdd:)"
+ "monitorAndFetchState(for:widgetIdentifier:kind:)"
+ "com.apple.Home"
+ "%!s(MISSING) error occured: %!@(MISSING)"
+ "[%!s(MISSING)] %!s(MISSING) mode: %!s(MISSING)"
+ "%!s(MISSING) Monitoring characteristics: %!s(MISSING)"
+ "%!s(MISSING) Monitoring actionSets: %!s(MISSING)"
+ "Removing delegates for all devices in home: %!s(MISSING): %!s(MISSING)"
+ "switch.programmable.square.fill"
+ "fetchCharacteristics(configuration:_:isMonitoring:)"
+ "registerForAccessories() called on %!s(MISSING)"
+ "%!s(MISSING) Failed to create device from HMAccessory (%!@(MISSING)). device: %!s(MISSING)"
+ "hdm_matterDevice: Failed to create matter device for accessory %!@(MISSING)"
+ "UIKit"
+ "HomeDataModel/DataModel+MatterDelegates.swift"
+ "_TtCC13HomeDataModel16CameraController5State"
+ "hdm_sharedMatterController: Failed to create MTRDeviceController for home (%!@(MISSING)) matterControllerID: (%!@(MISSING))"
+ "fetchStateForActionSets:completion:"
- "_TtCC13HomeDataModel16CameraController9ViewState"
- "[%!s(MISSING)] %!s(MISSING) %!s(MISSING)\nstreamState: %!s(MISSING) stream nil: %!{(MISSING)bool}d\")\nsnapshot nil: %!{(MISSING)bool}d snapshot date: %!s(MISSING)\navailability: %!s(MISSING)\nerror: %!s(MISSING)"
- "updatesContinuation"
- "modesContinuation"
- "Failed to create MTRDeviceController for home %!@(MISSING)"
- "Failed to create matter device for accessory %!@(MISSING)"
- "Setting up delegates for devices %!s(MISSING)"
- "monitor(for:configuration:)"
- "%!s(MISSING) Failed to get current characteristic values with error: %!@(MISSING)"
- "com.apple.Home.widget.interactive"
- "_streamSource"
- "viewState"
- "_snapshotSource"

```
