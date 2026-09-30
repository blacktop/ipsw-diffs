## PersonalAudio

> `/System/Library/PrivateFrameworks/PersonalAudio.framework/PersonalAudio`

```diff

-452.3.0.0.0
-  __TEXT.__text: 0x12788
+452.5.0.0.0
+  __TEXT.__text: 0x1436c
   __TEXT.__auth_stubs: 0x510
-  __TEXT.__objc_methlist: 0xb74
+  __TEXT.__objc_methlist: 0xc44
   __TEXT.__const: 0xb0
-  __TEXT.__gcc_except_tab: 0x478
-  __TEXT.__cstring: 0x1e3f
+  __TEXT.__gcc_except_tab: 0x47c
+  __TEXT.__cstring: 0x1fe9
   __TEXT.__oslogstring: 0x246
   __TEXT.__dlopen_cstrs: 0x163
-  __TEXT.__unwind_info: 0x4c0
+  __TEXT.__unwind_info: 0x518
   __TEXT.__objc_classname: 0xdb
-  __TEXT.__objc_methname: 0x27d8
+  __TEXT.__objc_methname: 0x2ab0
   __TEXT.__objc_methtype: 0x3cc
-  __TEXT.__objc_stubs: 0x2880
+  __TEXT.__objc_stubs: 0x2a80
   __DATA_CONST.__got: 0x168
-  __DATA_CONST.__const: 0x728
+  __DATA_CONST.__const: 0x800
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc28
+  __DATA_CONST.__objc_selrefs: 0xd10
   __DATA_CONST.__objc_superrefs: 0x40
   __AUTH_CONST.__auth_got: 0x298
-  __AUTH_CONST.__const: 0x320
-  __AUTH_CONST.__cfstring: 0x1ae0
-  __AUTH_CONST.__objc_const: 0xf20
+  __AUTH_CONST.__const: 0x300
+  __AUTH_CONST.__cfstring: 0x1c20
+  __AUTH_CONST.__objc_const: 0xf50
   __AUTH_CONST.__objc_doubleobj: 0x80
   __AUTH_CONST.__objc_intobj: 0x48
-  __AUTH.__data: 0x8
-  __DATA.__objc_ivar: 0x94
+  __AUTH.__data: 0x10
+  __DATA.__objc_ivar: 0x98
   __DATA.__data: 0xc0
-  __DATA.__bss: 0xc8
+  __DATA.__bss: 0xd0
   __DATA_DIRTY.__objc_data: 0x320
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__bss: 0xb8

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 369
-  Symbols:   553
-  CStrings:  846
+  Functions: 398
+  Symbols:   583
+  CStrings:  891
 
Symbols:
+ _dispatch_sync
+ _PAYodelConfigDidUpdate
- _paAnyRouteSupportsAudioAccommodationsIgnoringPlaybackState
- _objc_retain_x26
- _paCurrentRouteSupportsAudioAccommodationsIgnoringPlaybackState
CStrings:
+ "yodelEnabledForAddress:"
+ "balance"
+ "setTone:"
+ "-[PAAccessoryManager sendPMEConfigurationToAccessory]"
+ "setAmplification:"
+ "com.apple.personalaudio.yodel.updated"
+ "Checking Yodel %!d(MISSING) = %!@(MISSING)"
+ "noiseSuppression"
+ "Not a Yodel device. Clearing state %!@(MISSING)"
+ "setBalance:"
+ "Couldn't find identifier %!@(MISSING)"
+ "amplificationForAddress:"
+ "NSArray<NSDictionary *> *paRoutesOfSubtypeOrProduct(NSSet *__strong, NSSet *__strong, BOOL)"
+ "sendPMEConfigurationToAccessory"
+ "v12@?0B8"
+ "-[PAAccessoryManager sendPMEConfigurationToAccessory]_block_invoke_4"
+ "toggleHearingAidForAddress:"
+ "setEnableHearingAid:"
+ "getAudioOwnershipForAddress:withCompletion:"
+ "setNoiseSupressor:forAddress:"
+ "amplification"
+ "setNoiseSuppression:"
+ "setBeamforming:forAddress:"
+ "Updated %!@(MISSING) with error: %!@(MISSING)"
+ "balanceForAddress:"
+ "hearingAssistEnabled"
+ "Speech enabled %!@(MISSING)"
+ "beamFormer"
+ "setAmplification:forAddress:"
+ "setBalance:forAddress:"
+ "beamformingForAddress:"
+ "Setting types %!d(MISSING) = %!@(MISSING) - %!@(MISSING)"
+ "\x03"
+ "Skipping update. No address"
+ "-[PAHMSManager sendConfigUpdate:forAddress:]_block_invoke"
+ "yodelDeviceRecordByAddress"
+ "setBeamFormer:"
+ "noiseSupressorForAddress:"
+ "setAccommodationType:forAddress:"
+ "T@\"NSMutableDictionary\",&,N,V_yodelDeviceRecordByAddress"
+ "_yodelDeviceRecordByAddress"
+ "toneForAddress:"
+ "setYodelDeviceRecordByAddress:"
+ "hearingAidEnabledForAddress:"
+ "-[PAAccessoryManager sendPMEConfigurationToAccessory]_block_invoke"
+ "hearingAidEnabled"
+ "postNotificationName:object:"
+ "Skipping update to unsupported device %!@(MISSING)"
+ "-[PAHMSManager sendConfigUpdate:forAddress:]"
+ "Media enabled %!@(MISSING)"
+ "Device isn't supported [%!d(MISSING), %!d(MISSING), %!d(MISSING)] %!@(MISSING)"
+ "setTone:forAddress:"
+ "NSArray<NSDictionary *> *paRoutesOfSubtypeOrProduct(NSSet *__strong, NSSet *__strong, BOOL)_block_invoke"
+ "Skipping Yodel %!@(MISSING)"
+ "sendConfigUpdate:forAddress:"
+ "-[PAHMSManager sendConfigUpdate:forAddress:]_block_invoke_2"
- "-[PAAccessoryManager sendPMEConfigurationToAccessory:]_block_invoke_3"
- "-[PAAccessoryManager sendPMEConfigurationToAccessory:]_block_invoke"
- "NSArray<NSDictionary *> *paRoutesOfSubtypeOrProduct(NSSet *__strong, NSSet *__strong, BOOL, BOOL)"
- "sendPMEConfigurationToAccessory:"
- "Not updating enabled - same value %!@(MISSING)"
- "Device isn't supported [%!d(MISSING), %!d(MISSING)] %!@(MISSING)"
- "NSArray<NSDictionary *> *paRoutesOfSubtypeOrProduct(NSSet *__strong, NSSet *__strong, BOOL, BOOL)_block_invoke"
- "objectForKeyedSubscript:"
- "-[PAAccessoryManager sendPMEConfigurationToAccessory:]"
- "currentPickableAudioRoutes:"
- "\x02"

```
