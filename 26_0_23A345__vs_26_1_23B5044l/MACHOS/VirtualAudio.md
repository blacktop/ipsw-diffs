## VirtualAudio

> `/Library/Audio/Plug-Ins/HAL/VirtualAudio.plugin/VirtualAudio`

```diff

-1364.124.36.0.0
-  __TEXT.__text: 0x507e50
+1364.207.1.0.0
+  __TEXT.__text: 0x50c6e0
   __TEXT.__auth_stubs: 0x26f0
-  __TEXT.__objc_stubs: 0xb00
+  __TEXT.__objc_stubs: 0xb20
   __TEXT.__init_offsets: 0x4dc
   __TEXT.__objc_methlist: 0x124
-  __TEXT.__const: 0xb0b32
-  __TEXT.__gcc_except_tab: 0x5e054
-  __TEXT.__cstring: 0x28814
+  __TEXT.__const: 0xb0b92
+  __TEXT.__gcc_except_tab: 0x5e99c
+  __TEXT.__cstring: 0x288bc
   __TEXT.__objc_classname: 0x34
   __TEXT.__swift5_typeref: 0x133
   __TEXT.__swift5_capture: 0x178
-  __TEXT.__oslogstring: 0x4e7b6
-  __TEXT.__objc_methname: 0x7c8
+  __TEXT.__oslogstring: 0x4e92d
+  __TEXT.__objc_methname: 0x7d4
   __TEXT.__constg_swiftt: 0xf8
   __TEXT.__swift5_reflstr: 0x4c
   __TEXT.__swift5_fieldmd: 0x68

   __TEXT.__dof_VirtualAu: 0x340
   __TEXT.__dof_Aggregate: 0x5ec
   __TEXT.__dof_VirtualA0: 0x2aa
-  __TEXT.__unwind_info: 0x11408
+  __TEXT.__unwind_info: 0x115a0
   __TEXT.__eh_frame: 0x7a0
   __DATA_CONST.__auth_got: 0x1390
   __DATA_CONST.__got: 0x4e0
   __DATA_CONST.__auth_ptr: 0x70
-  __DATA_CONST.__const: 0x27d10
+  __DATA_CONST.__const: 0x280e8
   __DATA_CONST.__cfstring: 0x2de0
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA.__objc_const: 0x378
-  __DATA.__objc_selrefs: 0x2f8
+  __DATA.__objc_selrefs: 0x300
   __DATA.__objc_ivar: 0x14
   __DATA.__objc_data: 0x268
   __DATA.__data: 0x340
-  __DATA.__bss: 0x24bd0
+  __DATA.__bss: 0x25328
   __DATA.__common: 0x18
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
-  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: A9A509EC-D694-368B-B450-94FAF07BB518
-  Functions: 11526
-  Symbols:   774
-  CStrings:  11310
+  UUID: 4ACEDC28-461F-3021-BB99-3A410E025347
+  Functions: 11641
+  Symbols:   773
+  CStrings:  11323
 
Symbols:
- __swift_FORCE_LOAD_$_swiftCoreImage
CStrings:
+ "%25s:%-5d Defaults %s/%s defined to %s"
+ "%25s:%-5d EXCEPTION (std::runtime_error): \"Could not lock BT device weak_ref.\""
+ "%25s:%-5d EXCEPTION (std::runtime_error): \"Unable to lock owning BT device\""
+ "%25s:%-5d Expired port in port update list."
+ "%25s:%-5d Object with ID %lu has other references."
+ "%25s:%-5d Port sub-type has been updated to '%s' with tuning sub-type '%s'"
+ "%25s:%-5d Port update is all unroutable outputs. Dropping user preferred input."
+ "%25s:%-5d PortUpdate has unroutable output ports only: %d"
+ "%25s:%-5d Simulated device %s has already posted tapstream -- we still need to enable HAL tapstream control"
+ "%25s:%-5d Skipping initializing mic mode preferences for SpringBoard session"
+ "@@ Strips Sep 17 2025 00:08:20"
+ "AudioIssueDetectorFlush"
+ "AudioSession"
+ "Bluetooth port must be a headset-type"
+ "Could not lock BT device weak_ref."
+ "HP_ObjectManager.cpp"
+ "MultiRouteExpansion"
+ "Port endpoint type inclusion policy: %s"
+ "RunTimeDefaults.mm"
+ "Unable to lock owning BT device"
+ "boolForKey:"
- "%25s:%-5d Port update is all unroutables. Dropping user preferred BT input"
- "%25s:%-5d Simulated device %s has already posted tapstream -- skipping tapstream enablement"
- "%25s:%-5d VirtualAudio_DevicePropertyManager has expired. Ignoring property changed notifications."
- "%25s:%-5d portupdate has unroutable ports: %d"
- "@@ Strips Aug 26 2025 20:29:41"
- "Empty route change dictionary"
- "Property Listener Mutex"
- "RunTimeDefaults.cpp"

```
