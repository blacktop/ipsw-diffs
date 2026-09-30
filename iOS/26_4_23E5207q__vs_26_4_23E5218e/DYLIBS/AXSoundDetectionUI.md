## AXSoundDetectionUI

> `/System/Library/PrivateFrameworks/AXSoundDetectionUI.framework/AXSoundDetectionUI`

```diff

-496.13.0.0.0
-  __TEXT.__text: 0x5bfc8
-  __TEXT.__auth_stubs: 0x1260
+496.15.0.0.0
+  __TEXT.__text: 0x5bd38
+  __TEXT.__auth_stubs: 0x1250
   __TEXT.__objc_methlist: 0x274c
   __TEXT.__const: 0xa40
   __TEXT.__gcc_except_tab: 0x3f4
-  __TEXT.__oslogstring: 0x6284
-  __TEXT.__cstring: 0x11e2
+  __TEXT.__oslogstring: 0x6244
+  __TEXT.__cstring: 0x1152
   __TEXT.__dlopen_cstrs: 0x1a8
   __TEXT.__swift5_typeref: 0x79a
   __TEXT.__swift5_capture: 0x2ec

   __TEXT.__swift5_types: 0x38
   __TEXT.__swift_as_entry: 0x14
   __TEXT.__swift_as_ret: 0x2c
-  __TEXT.__unwind_info: 0x1378
+  __TEXT.__unwind_info: 0x1370
   __TEXT.__eh_frame: 0x8c0
   __TEXT.__objc_classname: 0x947
   __TEXT.__objc_methname: 0x577d

   __DATA_CONST.__objc_selrefs: 0x1728
   __DATA_CONST.__objc_protorefs: 0x80
   __DATA_CONST.__objc_superrefs: 0xb8
-  __AUTH_CONST.__auth_got: 0x940
+  __AUTH_CONST.__auth_got: 0x938
   __AUTH_CONST.__const: 0x1118
-  __AUTH_CONST.__cfstring: 0x1160
+  __AUTH_CONST.__cfstring: 0x10e0
   __AUTH_CONST.__objc_const: 0x3918
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH.__objc_data: 0x15b8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: E6D33CFC-3CC4-3C57-B7F2-B5420EFC2F9E
+  UUID: 7157EFE5-BD9E-366A-B078-9E0D229BBBAB
   Functions: 1771
-  Symbols:   3868
-  CStrings:  1927
+  Symbols:   3867
+  CStrings:  1912
 
Symbols:
+ _AXSoundDetectionSupportsVirtualAudioDevice
+ ___38-[AXSDListenEngine _interruptCarPlay:]_block_invoke.89
+ ___38-[AXSDListenEngine addListenDelegate:]_block_invoke.6
+ ___38-[AXSDListenEngine addListenDelegate:]_block_invoke.7
+ ___41-[AXSDListenEngine removeListenDelegate:]_block_invoke.14
- _MGGetBoolAnswer
- _MGGetSInt32Answer
- ___38-[AXSDListenEngine _interruptCarPlay:]_block_invoke.105
- ___38-[AXSDListenEngine addListenDelegate:]_block_invoke.20
- ___38-[AXSDListenEngine addListenDelegate:]_block_invoke.21
- ___41-[AXSDListenEngine removeListenDelegate:]_block_invoke.28
Functions:
~ -[AXSDListenEngine supportsVirtualAudioDevice] : 484 -> 4
~ sub_245a6bd00 -> sub_245b44b20 : 668 -> 652
~ sub_245a6c004 -> sub_245b44e14 : 776 -> 788
~ sub_245a71758 -> sub_245b4a574 : 1332 -> 1320
~ sub_245a728b0 -> sub_245b4b6c0 : 2992 -> 3032
~ sub_245a755e0 -> sub_245b4e418 : 1196 -> 1172
~ sub_245a76e6c -> sub_245b4fc8c : 1392 -> 1396
~ sub_245a788f4 -> sub_245b51718 : 3588 -> 3496
~ sub_245a7a000 -> sub_245b52dc8 : 5260 -> 5264
~ sub_245a7c3e8 -> sub_245b551b4 : 768 -> 780
~ sub_245a7d35c -> sub_245b56134 : 776 -> 788
~ sub_245a7fbf0 -> sub_245b589d4 : 1256 -> 1252
~ sub_245a80218 -> sub_245b58ff8 : 2516 -> 2520
~ sub_245a82314 -> sub_245b5b0f8 : 1392 -> 1380
~ sub_245a84a40 -> sub_245b5d818 : 1764 -> 1768
~ sub_245a867a4 -> sub_245b5f580 : 796 -> 808
~ sub_245a87114 -> sub_245b5fefc : 1288 -> 1272
~ sub_245a8bdec -> sub_245b64bc4 : 2368 -> 2372
~ sub_245a8c72c -> sub_245b65508 : 1908 -> 1912
~ sub_245a8d1e4 -> sub_245b65fc4 : 920 -> 924
~ sub_245a8ed88 -> sub_245b67b6c : 1820 -> 1816
~ sub_245a8f770 -> sub_245b68550 : 1524 -> 1536
~ sub_245a8fd64 -> sub_245b68b50 : 1740 -> 1752
~ sub_245a90570 -> sub_245b69368 : 1112 -> 1100
~ sub_245a90b20 -> sub_245b6990c : 1592 -> 1604
~ sub_245a91588 -> sub_245b6a380 : 2964 -> 2956
~ sub_245a930c8 -> sub_245b6beb8 : 2420 -> 2412
~ sub_245a94374 -> sub_245b6d15c : 1704 -> 1656
~ sub_245a99bfc -> sub_245b729b4 : 960 -> 944
~ sub_245a99fbc -> sub_245b72d64 : 1304 -> 1260
~ sub_245a9a670 -> sub_245b733ec : 1456 -> 1448
~ sub_245a9ae1c -> sub_245b73b90 : 1036 -> 1028
~ sub_245a9bd24 -> sub_245b74a90 : 2744 -> 2736
~ sub_245a9edb0 -> sub_245b77b14 : 576 -> 588
CStrings:
- "Device supports VAD: NO"
- "DeviceClassNumber"
- "DeviceSupportsIndependentOutputOnSpeaker"
- "DeviceSupportsUSBTypeC"
- "NO"
- "VirtualAudio"
- "YES"
- "YiUtBQygkHRhLcdO3LFB4A"
- "additive_routing"
- "iPad supports VAD: %s"
- "iPhone supports VAD: %s"

```
