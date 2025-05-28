## HearingUtilities

> `/System/Library/PrivateFrameworks/HearingUtilities.framework/HearingUtilities`

```diff

-406.1.3.0.0
-  __TEXT.__text: 0x7dd6c
+406.1.12.0.0
+  __TEXT.__text: 0x7e430
   __TEXT.__auth_stubs: 0xd20
   __TEXT.__objc_methlist: 0x5870
   __TEXT.__const: 0x1a8
-  __TEXT.__gcc_except_tab: 0x1a3c
-  __TEXT.__cstring: 0xabc2
-  __TEXT.__oslogstring: 0x1a1a
+  __TEXT.__gcc_except_tab: 0x1aa4
+  __TEXT.__cstring: 0xac3b
+  __TEXT.__oslogstring: 0x1a25
   __TEXT.__dlopen_cstrs: 0x4dc
-  __TEXT.__unwind_info: 0x1b64
+  __TEXT.__unwind_info: 0x1b98
   __TEXT.__objc_classname: 0x6ca
-  __TEXT.__objc_methname: 0xf09b
+  __TEXT.__objc_methname: 0xf07d
   __TEXT.__objc_methtype: 0x1b48
   __TEXT.__objc_stubs: 0xb0e0
   __DATA_CONST.__got: 0x248
-  __DATA_CONST.__const: 0x25a0
+  __DATA_CONST.__const: 0x25c8
   __DATA_CONST.__objc_classlist: 0x180
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0xc730
-  __DATA_CONST.__objc_selrefs: 0x3540
+  __DATA_CONST.__objc_selrefs: 0x3538
   __DATA_CONST.__objc_arraydata: 0x330
-  __AUTH_CONST.__const: 0x9c0
-  __AUTH_CONST.__cfstring: 0x74a0
+  __AUTH_CONST.__const: 0x9e0
+  __AUTH_CONST.__cfstring: 0x74e0
   __AUTH_CONST.__objc_const: 0x15c8
   __AUTH_CONST.__objc_intobj: 0x738
   __AUTH_CONST.__objc_arrayobj: 0x198

   __AUTH_CONST.__objc_doubleobj: 0x1450
   __AUTH_CONST.__auth_got: 0x6a0
   __AUTH.__objc_data: 0xcd0
-  __DATA.__objc_classrefs: 0x340
+  __DATA.__objc_classrefs: 0x338
   __DATA.__objc_superrefs: 0x160
   __DATA.__objc_ivar: 0x760
   __DATA.__data: 0x9e0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2617
-  Symbols:   8757
-  CStrings:  4301
+  Functions: 2620
+  Symbols:   8767
+  CStrings:  4303
 
Symbols:
+ ___37-[HUNearbyHearingAidController start]_block_invoke.101
+ ___37-[HUNearbyHearingAidController start]_block_invoke.108
+ ___37-[HUNearbyHearingAidController start]_block_invoke_2.109
+ ___43-[HUComfortSoundsController hasCurrentCall]_block_invoke
+ ___52-[HUNearbyHearingAidController callStatusDidChange:]_block_invoke_2
+ ___54-[HUNearbyHearingAidController requestHandoffForMedia]_block_invoke.45
+ ___57-[HUNearbyHearingAidController device:didReceiveMessage:]_block_invoke.157
+ ___59-[HUNearbyHearingAidController requestConnectionForReason:]_block_invoke.58
+ ___68-[HUNearbyHearingAidController checkConnectionRequestedAfterTimeout]_block_invoke.47
+ ___68-[HUNearbyHearingAidController shouldRelinquishConnectionForReason:]_block_invoke
+ ___71-[HUNearbyHearingAidController checkConnectionRelinquishedAfterTimeout]_block_invoke.72
+ ___block_descriptor_32_e25_B16?0"BluetoothDevice"8l
+ ___block_descriptor_64_e8_32r40r48r56r_e17_v24?0B8B12B16B20lr32l8r40l8r48l8r56l8
+ ___block_descriptor_72_e8_32bs40r48r56r64r_e5_v8?0lr40l8r48l8r56l8r64l8s32l8
+ ___block_literal_global.159
+ ___block_literal_global.191
+ ___block_literal_global.232
+ ___block_literal_global.97
+ _objc_msgSend$bluetoothState
+ _objc_msgSend$setSession:
- GCC_except_table55
- _OBJC_CLASS_$_CBDiscovery
- ___37-[HUNearbyHearingAidController start]_block_invoke.100
- ___37-[HUNearbyHearingAidController start]_block_invoke.107
- ___37-[HUNearbyHearingAidController start]_block_invoke_2.108
- ___54-[HUNearbyHearingAidController requestHandoffForMedia]_block_invoke.44
- ___57-[HUNearbyHearingAidController device:didReceiveMessage:]_block_invoke.156
- ___59-[HUNearbyHearingAidController requestConnectionForReason:]_block_invoke.57
- ___68-[HUNearbyHearingAidController checkConnectionRequestedAfterTimeout]_block_invoke.46
- ___71-[HUNearbyHearingAidController checkConnectionRelinquishedAfterTimeout]_block_invoke.71
- ___block_descriptor_40_e8_32r_e25_v32?0"CBDevice"8Q16^B24lr32l8
- ___block_descriptor_64_e5_v8?0l
- ___block_literal_global.158
- ___block_literal_global.231
- _objc_msgSend$deviceFlags
- _objc_msgSend$devicesWithDiscoveryFlags:error:
CStrings:
+ "-[AXHALiveListenController _setupSession]"
+ "Discovered new devices: %@, all devices: %@"
+ "LiveListen created auxiliarySession: %@"
+ "LiveListen will release auxiliarySession: %@"
+ "bluetoothState"
+ "v24@?0B8B12B16B20"
+ "void pairedWithDevicesSupportingListeningModes(__strong AXBoolBlock _Nonnull)_block_invoke_2"
- "Discovered new devices count: %@"
- "deviceFlags"
- "devicesWithDiscoveryFlags:error:"
- "v32@?0@\"CBDevice\"8Q16^B24"
- "void pairedWithDevicesSupportingListeningModes(__strong AXBoolBlock _Nonnull)_block_invoke"

```
