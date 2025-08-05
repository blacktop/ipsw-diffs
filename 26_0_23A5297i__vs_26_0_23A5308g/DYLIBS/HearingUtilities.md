## HearingUtilities

> `/System/Library/PrivateFrameworks/HearingUtilities.framework/HearingUtilities`

```diff

-492.1.0.0.0
-  __TEXT.__text: 0xa6054
+494.0.0.0.0
+  __TEXT.__text: 0xa6af0
   __TEXT.__auth_stubs: 0x1110
-  __TEXT.__objc_methlist: 0x7c74
+  __TEXT.__objc_methlist: 0x7d2c
   __TEXT.__const: 0x3da
-  __TEXT.__gcc_except_tab: 0x3178
-  __TEXT.__cstring: 0xe4ab
+  __TEXT.__gcc_except_tab: 0x31a8
+  __TEXT.__cstring: 0xe59b
   __TEXT.__oslogstring: 0x35fd
   __TEXT.__dlopen_cstrs: 0x7a7
   __TEXT.__swift5_typeref: 0x46

   __TEXT.__swift5_reflstr: 0xb
   __TEXT.__swift5_fieldmd: 0x38
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x2590
+  __TEXT.__unwind_info: 0x25d0
   __TEXT.__eh_frame: 0x48
-  __TEXT.__objc_classname: 0x840
-  __TEXT.__objc_methname: 0x13ee6
+  __TEXT.__objc_classname: 0x841
+  __TEXT.__objc_methname: 0x141b9
   __TEXT.__objc_methtype: 0x2183
-  __TEXT.__objc_stubs: 0xebe0
+  __TEXT.__objc_stubs: 0xed00
   __DATA_CONST.__got: 0x648
-  __DATA_CONST.__const: 0x33f0
+  __DATA_CONST.__const: 0x3420
   __DATA_CONST.__objc_classlist: 0x1c0
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x48e0
+  __DATA_CONST.__objc_selrefs: 0x4960
   __DATA_CONST.__objc_superrefs: 0x180
   __DATA_CONST.__objc_arraydata: 0x430
   __AUTH_CONST.__auth_got: 0x898
   __AUTH_CONST.__const: 0xd98
-  __AUTH_CONST.__cfstring: 0x8da0
-  __AUTH_CONST.__objc_const: 0xa4c8
+  __AUTH_CONST.__cfstring: 0x8e40
+  __AUTH_CONST.__objc_const: 0xa5d8
   __AUTH_CONST.__objc_intobj: 0xa80
   __AUTH_CONST.__objc_arrayobj: 0x1f8
   __AUTH_CONST.__objc_dictobj: 0x410
   __AUTH_CONST.__objc_doubleobj: 0xed0
   __AUTH.__objc_data: 0xfa8
   __AUTH.__data: 0x50
-  __DATA.__objc_ivar: 0x8e4
+  __DATA.__objc_ivar: 0x8f8
   __DATA.__data: 0xc20
   __DATA.__bss: 0x3e8
   __DATA_DIRTY.__objc_data: 0x2d0

   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
+  - /usr/lib/swift/libswiftCoreAudio_Private.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 1D453466-031C-3D3F-8174-EBC3088605EA
-  Functions: 3507
-  Symbols:   11320
-  CStrings:  6802
+  UUID: DF8EB8C0-67A3-3AD4-AB69-B45A0900584B
+  Functions: 3529
+  Symbols:   11383
+  CStrings:  6838
 
Symbols:
+ -[AXHeardController updateLiveListenWithAccommodationTypes]
+ -[HUAccessoryHearingSyncManager ignoreHPTimer]
+ -[HUAccessoryHearingSyncManager ignoreHPUpdates]
+ -[HUAccessoryHearingSyncManager setIgnoreHPTimer:]
+ -[HUAccessoryHearingSyncManager setIgnoreHPUpdates:]
+ -[HUAccessoryManager aaAvailableDevices]
+ -[HUAccessoryManager setAaAvailableDevices:]
+ -[HUHearingSettings liveListenAnyRouteEnabled]
+ -[HUHearingSettings setLiveListenAnyRouteEnabled:]
+ -[HUHearingSettings setShouldShowSSLFooterInCC:]
+ -[HUHearingSettings shouldShowSSLFooterInCC]
+ -[HULiveListenController personalAudioMediaAccommodationsEnabled]
+ -[HULiveListenController setPersonalAudioMediaAccommodationsEnabled:]
+ -[HUNearbyLiveListenController setTranscriptionLock:]
+ -[HUNearbyLiveListenController transcriptionLock]
+ -[HUUtilities _shouldBypassLiveListenRouteCheck]
+ GCC_except_table132
+ GCC_except_table137
+ GCC_except_table142
+ GCC_except_table147
+ GCC_except_table153
+ GCC_except_table166
+ GCC_except_table172
+ GCC_except_table174
+ GCC_except_table68
+ GCC_except_table92
+ _OBJC_IVAR_$_HUAccessoryHearingSyncManager._ignoreHPTimer
+ _OBJC_IVAR_$_HUAccessoryHearingSyncManager._ignoreHPUpdates
+ _OBJC_IVAR_$_HUAccessoryManager._aaAvailableDevices
+ _OBJC_IVAR_$_HULiveListenController._personalAudioMediaAccommodationsEnabled
+ _OBJC_IVAR_$_HUNearbyLiveListenController._transcriptionLock
+ ___107-[HUNoiseController checkToSurfaceAnalyticsNotificationForSPL:withDuration:andBuffer:forTime:andThreshold:]_block_invoke.536
+ ___107-[HUNoiseController checkToSurfaceAnalyticsNotificationForSPL:withDuration:andBuffer:forTime:andThreshold:]_block_invoke.549
+ ___107-[HUNoiseController checkToSurfaceAnalyticsNotificationForSPL:withDuration:andBuffer:forTime:andThreshold:]_block_invoke.557
+ ___107-[HUNoiseController checkToSurfaceAnalyticsNotificationForSPL:withDuration:andBuffer:forTime:andThreshold:]_block_invoke.566
+ ___25-[HUNoiseController init]_block_invoke.325
+ ___37-[HUNoiseController restartADAMTimer]_block_invoke.414
+ ___42-[HUAccessoryManager setupAADeviceManager]_block_invoke_7
+ ___42-[HUAccessoryManager setupAADeviceManager]_block_invoke_8
+ ___42-[HUAccessoryManager setupAADeviceManager]_block_invoke_9
+ ___51-[HUNoiseController subscribeToSharedNotifications]_block_invoke.639
+ ___53-[HUNoiseController readEnvironmentalDosimetryLevels]_block_invoke.440
+ ___54-[HUAccessoryHearingSyncManager sendUpdateToAccessory]_block_invoke.135
+ ___55-[HUUtilities pauseNowPlaying:withQueue:andCompletion:]_block_invoke.50
+ ___55-[HUUtilities pauseNowPlaying:withQueue:andCompletion:]_block_invoke_2.51
+ ___69-[HUAccessoryHearingSyncManager sendListeningModesIDSMessageIfNeeded]_block_invoke.153
+ ___71-[HUAccessoryHearingSyncManager shouldUpdateWatchesWithListeningModes:]_block_invoke.146
+ ___85-[HUNoiseController checkToSurfaceNotificationForSPL:withDuration:andBuffer:forTime:]_block_invoke.480
+ ___85-[HUNoiseController checkToSurfaceNotificationForSPL:withDuration:andBuffer:forTime:]_block_invoke.500
+ ___block_descriptor_48_e8_32s40w_e40_v32?0"NSString"8"CBUUID"16"NSData"24ls32l8w40l8
+ ___block_descriptor_56_e8_32s40s48s_e17_v16?0"NSArray"8ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48s_e25_v32?0"NSString"8Q16^B24ls32l8s40l8s48l8
+ ___block_literal_global.151
+ ___block_literal_global.297
+ ___block_literal_global.404
+ ___block_literal_global.551
+ ___block_literal_global.559
+ ___block_literal_global.568
+ ___block_literal_global.596
+ ___block_literal_global.606
+ ___block_literal_global.685
+ __swift_FORCE_LOAD_$_swiftCoreAudio_Private
+ __swift_FORCE_LOAD_$_swiftCoreAudio_Private_$_HearingUtilities
+ _getPAYodelConfigDidUpdate
+ _getPAYodelConfigDidUpdate.cold.1
+ _objc_msgSend$_shouldBypassLiveListenRouteCheck
+ _objc_msgSend$aaAvailableDevices
+ _objc_msgSend$ignoreHPTimer
+ _objc_msgSend$ignoreHPUpdates
+ _objc_msgSend$liveListenAnyRouteEnabled
+ _objc_msgSend$setAaAvailableDevices:
+ _objc_msgSend$setDeviceLostHandler:
+ _objc_msgSend$setIgnoreHPTimer:
+ _objc_msgSend$setIgnoreHPUpdates:
+ _objc_msgSend$setPersonalAudioMediaAccommodationsEnabled:
+ _objc_msgSend$updateLiveListenWithAccommodationTypes
- GCC_except_table138
- GCC_except_table143
- GCC_except_table149
- GCC_except_table158
- GCC_except_table168
- GCC_except_table170
- GCC_except_table58
- GCC_except_table84
- GCC_except_table90
- ___107-[HUNoiseController checkToSurfaceAnalyticsNotificationForSPL:withDuration:andBuffer:forTime:andThreshold:]_block_invoke.533
- ___107-[HUNoiseController checkToSurfaceAnalyticsNotificationForSPL:withDuration:andBuffer:forTime:andThreshold:]_block_invoke.546
- ___107-[HUNoiseController checkToSurfaceAnalyticsNotificationForSPL:withDuration:andBuffer:forTime:andThreshold:]_block_invoke.554
- ___107-[HUNoiseController checkToSurfaceAnalyticsNotificationForSPL:withDuration:andBuffer:forTime:andThreshold:]_block_invoke.563
- ___25-[HUNoiseController init]_block_invoke.322
- ___37-[HUNoiseController restartADAMTimer]_block_invoke.411
- ___42-[HUAccessoryManager setupAADeviceManager]_block_invoke_2.cold.1
- ___51-[HUNoiseController subscribeToSharedNotifications]_block_invoke.636
- ___53-[HUNoiseController readEnvironmentalDosimetryLevels]_block_invoke.437
- ___55-[HUUtilities pauseNowPlaying:withQueue:andCompletion:]_block_invoke.48
- ___55-[HUUtilities pauseNowPlaying:withQueue:andCompletion:]_block_invoke_2.49
- ___71-[HUAccessoryHearingSyncManager shouldUpdateWatchesWithListeningModes:]_block_invoke.145
- ___85-[HUNoiseController checkToSurfaceNotificationForSPL:withDuration:andBuffer:forTime:]_block_invoke.477
- ___85-[HUNoiseController checkToSurfaceNotificationForSPL:withDuration:andBuffer:forTime:]_block_invoke.497
- ___block_descriptor_40_e8_32w_e40_v32?0"NSString"8"CBUUID"16"NSData"24lw32l8
- ___block_descriptor_48_e8_32s40s_e25_v32?0"NSString"8Q16^B24ls32l8s40l8
- ___block_literal_global.107
- ___block_literal_global.148
- ___block_literal_global.294
- ___block_literal_global.401
- ___block_literal_global.548
- ___block_literal_global.556
- ___block_literal_global.565
- ___block_literal_global.593
- ___block_literal_global.603
- ___block_literal_global.682
- _objc_msgSend$aaDeviceManager
- _objc_msgSend$discoveredDevices
CStrings:
+ "-[HULiveListenController setPersonalAudioMediaAccommodationsEnabled:]"
+ "AA controller found %@ address: %@"
+ "AA controller lost %@, address: %@"
+ "PA media accommodations turned off, stopping live listen"
+ "T@\"AXDispatchTimer\",&,N,V_ignoreHPTimer"
+ "T@\"NSLock\",&,N,V_transcriptionLock"
+ "T@\"NSMutableDictionary\",&,N,V_aaAvailableDevices"
+ "TB,N,V_personalAudioMediaAccommodationsEnabled"
+ "TB,V_ignoreHPUpdates"
+ "_aaAvailableDevices"
+ "_ignoreHPTimer"
+ "_ignoreHPUpdates"
+ "_personalAudioMediaAccommodationsEnabled"
+ "_shouldBypassLiveListenRouteCheck"
+ "_transcriptionLock"
+ "aaAvailableDevices"
+ "ignoreHPTimer"
+ "ignoreHPUpdates"
+ "liveListenAnyRouteEnabled"
+ "personalAudioMediaAccommodationsEnabled"
+ "setAaAvailableDevices:"
+ "setDeviceLostHandler:"
+ "setIgnoreHPTimer:"
+ "setIgnoreHPUpdates:"
+ "setLiveListenAnyRouteEnabled:"
+ "setPersonalAudioMediaAccommodationsEnabled:"
+ "setShouldShowSSLFooterInCC:"
+ "setTranscriptionLock:"
+ "shouldShowSSLFooterInCC"
+ "transcriptionLock"
+ "updateLiveListenWithAccommodationTypes"
- "$"
- "discoveredDevices"

```
