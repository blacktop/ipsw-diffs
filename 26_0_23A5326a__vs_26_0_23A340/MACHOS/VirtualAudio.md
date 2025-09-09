## VirtualAudio

> `/Library/Audio/Plug-Ins/HAL/VirtualAudio.plugin/VirtualAudio`

```diff

-1364.124.34.0.0
-  __TEXT.__text: 0x5054e0
+1364.124.36.0.0
+  __TEXT.__text: 0x507e50
   __TEXT.__auth_stubs: 0x26f0
-  __TEXT.__objc_stubs: 0x9e0
+  __TEXT.__objc_stubs: 0xb00
   __TEXT.__init_offsets: 0x4dc
   __TEXT.__objc_methlist: 0x124
-  __TEXT.__const: 0xb0b12
-  __TEXT.__gcc_except_tab: 0x5dbf4
-  __TEXT.__cstring: 0x287a1
+  __TEXT.__const: 0xb0b32
+  __TEXT.__gcc_except_tab: 0x5e054
+  __TEXT.__cstring: 0x28814
   __TEXT.__objc_classname: 0x34
   __TEXT.__swift5_typeref: 0x133
   __TEXT.__swift5_capture: 0x178
-  __TEXT.__oslogstring: 0x4e504
-  __TEXT.__objc_methname: 0x710
+  __TEXT.__oslogstring: 0x4e7b6
+  __TEXT.__objc_methname: 0x7c8
   __TEXT.__constg_swiftt: 0xf8
   __TEXT.__swift5_reflstr: 0x4c
   __TEXT.__swift5_fieldmd: 0x68

   __TEXT.__dof_VirtualAu: 0x340
   __TEXT.__dof_Aggregate: 0x5ec
   __TEXT.__dof_VirtualA0: 0x2aa
-  __TEXT.__unwind_info: 0x11348
+  __TEXT.__unwind_info: 0x11408
   __TEXT.__eh_frame: 0x7a0
   __DATA_CONST.__auth_got: 0x1390
-  __DATA_CONST.__got: 0x4d8
+  __DATA_CONST.__got: 0x4e0
   __DATA_CONST.__auth_ptr: 0x70
-  __DATA_CONST.__const: 0x27b48
+  __DATA_CONST.__const: 0x27d10
   __DATA_CONST.__cfstring: 0x2de0
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA.__objc_const: 0x378
-  __DATA.__objc_selrefs: 0x2b0
+  __DATA.__objc_selrefs: 0x2f8
   __DATA.__objc_ivar: 0x14
   __DATA.__objc_data: 0x268
   __DATA.__data: 0x340
-  __DATA.__bss: 0x24bc0
+  __DATA.__bss: 0x24bd0
   __DATA.__common: 0x18
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: FE1199AA-4D0F-3B52-9C48-2A1A4ED18A3B
-  Functions: 11496
-  Symbols:   773
-  CStrings:  11286
+  UUID: A9A509EC-D694-368B-B450-94FAF07BB518
+  Functions: 11526
+  Symbols:   774
+  CStrings:  11310
 
Symbols:
+ _OBJC_CLASS_$_HMServiceClient
CStrings:
+ "%25s:%-5d Adding Hearing Mode Service IO delegate %s"
+ "%25s:%-5d Central Hearing Mode Service SPI handler is created"
+ "%25s:%-5d Central Hearing Mode Service SPI handler is destroyed"
+ "%25s:%-5d Destroying Hearing Mode Service IO delegate for chain %s"
+ "%25s:%-5d Disabling HAL AirPods offload DSP for VP or FarField use case"
+ "%25s:%-5d Enable Far-Field Input on route: %u"
+ "%25s:%-5d Failed to activate Hearing Mode client"
+ "%25s:%-5d Failed to add Hearing Mode Service IO delegate for chain %s to central SPI handler"
+ "%25s:%-5d Handling Hearing Mode Service IO delegate for chain %s. Enabling? %s. Cap? %.2f"
+ "%25s:%-5d Hearing Mode Server was interrupted, restart client"
+ "%25s:%-5d Using cached far field preference: %u"
+ "%25s:%-5d enable %d, cap %.2f for device %@"
+ "@@ Strips Aug 26 2025 20:29:41"
+ "HearingModeServiceIODelegate.mm"
+ "activateWithCompletion:"
+ "bluetoothUUID"
+ "code"
+ "far field input"
+ "floatValue"
+ "hearingProtectionPPECapLevel"
+ "hearingProtectionPPEEnabled"
+ "kBluetoothAudioDeviceFeatureFarfieldInput"
+ "setDeviceRecordChangedHandler:"
+ "setDispatchQueue:"
+ "setInterruptionHandler:"
+ "v16@?0@\"HMDeviceRecord\"8"
+ "v16@?0@\"NSError\"8"
- "%25s:%-5d Disabling HAL AirPods offload DSP for VP use case"
- "@@ Strips Aug 12 2025 22:59:21"
- "PortManager mutex"

```
