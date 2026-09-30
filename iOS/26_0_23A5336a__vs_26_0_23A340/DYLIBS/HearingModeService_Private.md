## HearingModeService_Private

> `/System/Library/PrivateFrameworks/HearingModeService_Private.framework/HearingModeService_Private`

```diff

 30.59.1.9.0
-  __TEXT.__text: 0x12414
+  __TEXT.__text: 0x12e98
   __TEXT.__auth_stubs: 0x4b0
-  __TEXT.__objc_methlist: 0xc3c
+  __TEXT.__objc_methlist: 0xc64
   __TEXT.__const: 0x86
   __TEXT.__gcc_except_tab: 0x514
-  __TEXT.__cstring: 0x4dd8
-  __TEXT.__unwind_info: 0x5d8
+  __TEXT.__cstring: 0x50e2
+  __TEXT.__unwind_info: 0x5f0
   __TEXT.__objc_classname: 0x14d
-  __TEXT.__objc_methname: 0x3449
-  __TEXT.__objc_methtype: 0x8af
-  __TEXT.__objc_stubs: 0x2f80
-  __DATA_CONST.__got: 0x1e0
+  __TEXT.__objc_methname: 0x367e
+  __TEXT.__objc_methtype: 0x8ef
+  __TEXT.__objc_stubs: 0x3200
+  __DATA_CONST.__got: 0x1f0
   __DATA_CONST.__const: 0x858
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe00
+  __DATA_CONST.__objc_selrefs: 0xea0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x30
   __AUTH_CONST.__auth_got: 0x268
   __AUTH_CONST.__const: 0x160
-  __AUTH_CONST.__cfstring: 0x6c0
+  __AUTH_CONST.__cfstring: 0x700
   __AUTH_CONST.__objc_const: 0x1498
   __AUTH_CONST.__objc_doubleobj: 0x80
   __AUTH_CONST.__objc_intobj: 0x18

   - /System/Library/PrivateFrameworks/ToneLibrary.framework/ToneLibrary
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 182C3E3F-6BB1-3D73-9D09-AF290AF86E60
-  Functions: 423
-  Symbols:   1612
-  CStrings:  1094
+  UUID: C0E39102-AE3E-333E-8A91-6A896F6F55B3
+  Functions: 435
+  Symbols:   1658
+  CStrings:  1133
 
Symbols:
+ -[HMDeviceManager _deviceRescindHearingProtectionPPE:]
+ -[HMDeviceManager _deviceRescindHearingProtectionPPE:].cold.1
+ -[HMDeviceManager _populateV2Struct:identifier:deviceRecord:hmSettingsStruct:]
+ -[HMDeviceManager _populateV2Struct:identifier:deviceRecord:hmSettingsStruct:].cold.1
+ -[HMDeviceManager _sendHAv2RegionStatus:]
+ -[HMDeviceManager _sendHearingAidConfigOverAHPSConnection:identifier:completion:].cold.3
+ GCC_except_table107
+ GCC_except_table66
+ GCC_except_table79
+ GCC_except_table86
+ GCC_except_table95
+ _HKFeatureIdentifierHearingAidV2
+ _HKFeatureIdentifierHearingProtectionPPE
+ _OUTLINED_FUNCTION_5
+ ___41-[HMDeviceManager _sendHAv2RegionStatus:]_block_invoke
+ ___41-[HMDeviceManager _sendHAv2RegionStatus:]_block_invoke.cold.1
+ ___54-[HMDeviceManager _deviceRescindHearingProtectionPPE:]_block_invoke
+ ___54-[HMDeviceManager _deviceRescindHearingProtectionPPE:]_block_invoke.cold.1
+ ___68-[HMDeviceManager _modifyDeviceConfiguration:identifier:completion:]_block_invoke_2
+ ___block_literal_global.363
+ ___block_literal_global.394
+ ___block_literal_global.452
+ ___block_literal_global.479
+ ___block_literal_global.496
+ _objc_msgSend$_deviceRescindHearingProtectionPPE:
+ _objc_msgSend$_populateV2Struct:identifier:deviceRecord:hmSettingsStruct:
+ _objc_msgSend$_sendHAv2RegionStatus:
+ _objc_msgSend$enableHearingProtectionPPE
+ _objc_msgSend$haRegionStatusV2
+ _objc_msgSend$hearingAidV2Capability
+ _objc_msgSend$hearingAidV2RegionStatus
+ _objc_msgSend$hearingProtectionPPEEnabled
+ _objc_msgSend$hearingProtectionPPERegionStatus
+ _objc_msgSend$hpPPERegionStatus
+ _objc_msgSend$ownVoiceLevelGain
+ _objc_msgSend$setEnableHearingProtectionPPE:
+ _objc_msgSend$setHaRegionStatusV2:
+ _objc_msgSend$setHearingAidV2RegionStatus:
+ _objc_msgSend$setHearingAidV2SourceRegionSupport:
+ _objc_msgSend$setHearingProtectionPPERegionStatus:
+ _objc_msgSend$setHpPPERegionStatus:
+ _objc_msgSend$setSharedRegionStatus:
+ _objc_msgSend$setupConfigsForPPEIfNeeded:completion:
+ _objc_msgSend$sharedRegionStatus
- GCC_except_table101
- GCC_except_table62
- GCC_except_table75
- GCC_except_table82
- GCC_except_table91
- ___block_literal_global.357
- ___block_literal_global.384
- ___block_literal_global.440
- ___block_literal_global.467
- ___block_literal_global.484
CStrings:
+ "### AADeviceManager failed to send HAv2 region status config %@ to device with identifier: %@"
+ "-[HMDeviceManager _deviceRescindHearingProtectionPPE:]"
+ "-[HMDeviceManager _deviceRescindHearingProtectionPPE:]_block_invoke"
+ "-[HMDeviceManager _populateV2Struct:identifier:deviceRecord:hmSettingsStruct:]"
+ "-[HMDeviceManager _sendHAv2RegionStatus:]"
+ "-[HMDeviceManager _sendHAv2RegionStatus:]_block_invoke"
+ "AADeviceManager: sending HAv2 region status config %@ to device with identifier: %@"
+ "Device identifier: %@, updating ownVoiceLevelGain %f --> %f"
+ "Feature rescinded but PPE not enabled to begin with: %@"
+ "HAv2 Capability not supported for %@"
+ "HAv2 Feature not supported"
+ "HearingAidV2"
+ "HearingProtectionPPE"
+ "OwnVoiceLevelGain"
+ "OwnVoiceSlider"
+ "_deviceRescindHearingProtectionPPE:"
+ "_populateV2Struct:identifier:deviceRecord:hmSettingsStruct:"
+ "_sendHAv2RegionStatus:"
+ "enableHearingProtectionPPE"
+ "haRegionStatusV2"
+ "hearingAidV2Capability"
+ "hearingAidV2RegionStatus"
+ "hearingProtectionPPEEnabled"
+ "hearingProtectionPPERegionStatus"
+ "hpPPERegionStatus"
+ "ownVoiceLevelGain"
+ "sending settings to buds: %@ - ownVoiceLevelGain: %lf"
+ "setEnableHearingProtectionPPE:"
+ "setHaRegionStatusV2:"
+ "setHearingAidV2RegionStatus:"
+ "setHearingAidV2SourceRegionSupport:"
+ "setHearingProtectionPPERegionStatus:"
+ "setHpPPERegionStatus:"
+ "setSharedRegionStatus:"
+ "setupConfigsForPPEIfNeeded:completion:"
+ "sharedRegionStatus"
+ "v48@0:8@16@24@32^{?={?=CCS{?=ffffffffffff}{?=ffffffffffff}}f}40"

```
