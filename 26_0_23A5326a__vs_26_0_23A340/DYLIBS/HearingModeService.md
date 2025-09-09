## HearingModeService

> `/System/Library/PrivateFrameworks/HearingModeService.framework/HearingModeService`

```diff

 30.59.1.9.0
-  __TEXT.__text: 0x13fe8
+  __TEXT.__text: 0x14c1c
   __TEXT.__auth_stubs: 0x4a0
-  __TEXT.__objc_methlist: 0x163c
+  __TEXT.__objc_methlist: 0x16dc
   __TEXT.__const: 0x70
-  __TEXT.__cstring: 0x4622
+  __TEXT.__cstring: 0x48f5
   __TEXT.__gcc_except_tab: 0x1bc
   __TEXT.__unwind_info: 0x470
   __TEXT.__objc_classname: 0x130
-  __TEXT.__objc_methname: 0x5552
+  __TEXT.__objc_methname: 0x58f5
   __TEXT.__objc_methtype: 0x8bf
-  __TEXT.__objc_stubs: 0x20e0
+  __TEXT.__objc_stubs: 0x21a0
   __DATA_CONST.__got: 0x128
   __DATA_CONST.__const: 0x610
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xff0
+  __DATA_CONST.__objc_selrefs: 0x1058
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x30
   __AUTH_CONST.__auth_got: 0x260
   __AUTH_CONST.__const: 0x20
-  __AUTH_CONST.__cfstring: 0x15e0
-  __AUTH_CONST.__objc_const: 0x2d28
+  __AUTH_CONST.__cfstring: 0x16c0
+  __AUTH_CONST.__objc_const: 0x2ed8
   __AUTH_CONST.__objc_doubleobj: 0xa0
-  __AUTH_CONST.__objc_intobj: 0x198
+  __AUTH_CONST.__objc_intobj: 0x240
   __AUTH.__objc_data: 0x190
-  __DATA.__objc_ivar: 0x304
+  __DATA.__objc_ivar: 0x328
   __DATA.__data: 0x4d0
   __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0xf0

   - /System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 91617629-B71B-3039-8E16-6123E0B5CDD4
-  Functions: 572
-  Symbols:   1886
-  CStrings:  1702
+  UUID: 3943F8A3-1ECA-3F4F-B558-9919740FC4A8
+  Functions: 592
+  Symbols:   1943
+  CStrings:  1761
 
Symbols:
+ -[HMDeviceConfigurations enableHearingProtectionPPE]
+ -[HMDeviceConfigurations needsUpdateToAHPSConnectionManagerForDevice:].cold.6
+ -[HMDeviceConfigurations needsUpdateToDeviceManagerForDevice:].cold.6
+ -[HMDeviceConfigurations ownVoiceLevelGain]
+ -[HMDeviceConfigurations setEnableHearingProtectionPPE:]
+ -[HMDeviceConfigurations setOwnVoiceLevelGain:]
+ -[HMDeviceConfigurations setupConfigsForPPEIfNeeded:completion:]
+ -[HMDeviceConfigurations setupConfigsForPPEIfNeeded:completion:].cold.1
+ -[HMDeviceRecord hearingAidV2Capability]
+ -[HMDeviceRecord hearingAidV2RegionStatus]
+ -[HMDeviceRecord hearingProtectionPPECapLevel]
+ -[HMDeviceRecord hearingProtectionPPECapability]
+ -[HMDeviceRecord hearingProtectionPPEEnabled]
+ -[HMDeviceRecord hearingProtectionPPERegionStatus]
+ -[HMDeviceRecord ownVoiceLevelGain]
+ -[HMDeviceRecord setHearingAidV2RegionStatus:]
+ -[HMDeviceRecord setHearingProtectionPPERegionStatus:]
+ -[HMInfo setConstantsWith:].cold.4
+ _OBJC_IVAR_$_HMDeviceConfigurations._enableHearingProtectionPPE
+ _OBJC_IVAR_$_HMDeviceConfigurations._ownVoiceLevelGain
+ _OBJC_IVAR_$_HMDeviceRecord._hearingAidV2Capability
+ _OBJC_IVAR_$_HMDeviceRecord._hearingAidV2RegionStatus
+ _OBJC_IVAR_$_HMDeviceRecord._hearingProtectionPPECapLevel
+ _OBJC_IVAR_$_HMDeviceRecord._hearingProtectionPPECapability
+ _OBJC_IVAR_$_HMDeviceRecord._hearingProtectionPPEEnabled
+ _OBJC_IVAR_$_HMDeviceRecord._hearingProtectionPPERegionStatus
+ _OBJC_IVAR_$_HMDeviceRecord._ownVoiceLevelGain
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _objc_msgSend$hearingAidV2Capability
+ _objc_msgSend$hearingProtectionPPECapLevel
+ _objc_msgSend$hearingProtectionPPECapability
+ _objc_msgSend$hearingProtectionPPEEnabled
+ _objc_msgSend$ownVoiceLevelGain
+ _objc_msgSend$updateVolumeIOS:completion:
CStrings:
+ ", En HPPPE %s"
+ ", HP PPE CapLvl %@"
+ ", HP PPE Cp %s"
+ ", HP PPE En %s"
+ ", HP PPE Reg St %s"
+ ", Hr Aidv2 Cp %s"
+ ", Hr Aidv2 Reg St %s"
+ ", Own Vc LG %@"
+ "-[HMDeviceConfigurations setupConfigsForPPEIfNeeded:completion:]"
+ "/"
+ "HMDeviceRecord UUID %@, settings received: version: %d, LEFT ear loss_01_dBHL: %lf, RIGHT ear loss_01_dBHL: %lf, leftGain: %lf, rightGain: %lf, tone: %lf, amplification: %lf, balance: %lf, beamFormer: %lf, noiseSuppression: %lf, ownVoiceLevelGain: %lf"
+ "HMInfo creating safety information values for B788"
+ "HearingAidV2"
+ "HearingProtectionPPE"
+ "Setup PPE Configs for UUID: %@ - Enable LSR and Disable OFF"
+ "T@\"NSNumber\",&,N,V_ownVoiceLevelGain"
+ "T@\"NSNumber\",R,N,V_hearingProtectionPPECapLevel"
+ "T@\"NSNumber\",R,N,V_ownVoiceLevelGain"
+ "TC,N,V_hearingAidV2RegionStatus"
+ "TC,N,V_hearingProtectionPPERegionStatus"
+ "Tc,N,V_enableHearingProtectionPPE"
+ "Tc,R,N,V_hearingAidV2Capability"
+ "Tc,R,N,V_hearingProtectionPPECapability"
+ "Tc,R,N,V_hearingProtectionPPEEnabled"
+ "_enableHearingProtectionPPE"
+ "_hearingAidV2Capability"
+ "_hearingAidV2RegionStatus"
+ "_hearingProtectionPPECapLevel"
+ "_hearingProtectionPPECapability"
+ "_hearingProtectionPPEEnabled"
+ "_hearingProtectionPPERegionStatus"
+ "_ownVoiceLevelGain"
+ "changing enable Hearing Protection PPE mode %s --> %s"
+ "changing ownVoiceLevelGain %@ --> %@"
+ "enableHearingProtectionPPE"
+ "hV2R"
+ "haV2"
+ "hearingAidV2Capability"
+ "hearingAidV2RegionStatus"
+ "hearingProtectionPPECapLevel"
+ "hearingProtectionPPECapability"
+ "hearingProtectionPPEEnabled"
+ "hearingProtectionPPERegionStatus"
+ "oVLG"
+ "ownVoiceLevelGain"
+ "ppeC"
+ "ppeE"
+ "ppeL"
+ "ppeR"
+ "setEnableHearingProtectionPPE:"
+ "setHearingAidV2RegionStatus:"
+ "setHearingProtectionPPERegionStatus:"
+ "setOwnVoiceLevelGain:"
+ "setupConfigsForPPEIfNeeded:completion:"
- "."
- "_\f"

```
