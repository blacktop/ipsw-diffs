## AudioAccessoryServices

> `/System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices`

```diff

-21.9.1.0.0
-  __TEXT.__text: 0x23d6c
+21.13.3.1.3
+  __TEXT.__text: 0x26a34
   __TEXT.__auth_stubs: 0x7d0
-  __TEXT.__objc_methlist: 0x2664
+  __TEXT.__objc_methlist: 0x2b0c
   __TEXT.__const: 0x140
-  __TEXT.__gcc_except_tab: 0xa24
-  __TEXT.__cstring: 0x798b
-  __TEXT.__unwind_info: 0x920
-  __TEXT.__objc_classname: 0x33d
-  __TEXT.__objc_methname: 0x5cdc
-  __TEXT.__objc_methtype: 0xe81
-  __TEXT.__objc_stubs: 0x25c0
-  __DATA_CONST.__got: 0x120
+  __TEXT.__gcc_except_tab: 0xb0c
+  __TEXT.__cstring: 0x80cb
+  __TEXT.__unwind_info: 0x978
+  __TEXT.__objc_classname: 0x35c
+  __TEXT.__objc_methname: 0x6f88
+  __TEXT.__objc_methtype: 0xf24
+  __TEXT.__objc_stubs: 0x2820
+  __DATA_CONST.__got: 0x128
   __DATA_CONST.__const: 0xa98
-  __DATA_CONST.__objc_classlist: 0xc0
+  __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1280
+  __DATA_CONST.__objc_selrefs: 0x1528
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x98
   __AUTH_CONST.__auth_got: 0x3f8
   __AUTH_CONST.__const: 0x80
-  __AUTH_CONST.__cfstring: 0xde0
-  __AUTH_CONST.__objc_const: 0x5a60
-  __AUTH.__objc_data: 0x4b0
+  __AUTH_CONST.__cfstring: 0x12e0
+  __AUTH_CONST.__objc_const: 0x6418
+  __AUTH.__objc_data: 0x460
   __AUTH.__data: 0xc0
-  __DATA.__objc_ivar: 0x524
-  __DATA.__data: 0x970
+  __DATA.__objc_ivar: 0x5d4
+  __DATA.__data: 0x900
   __DATA.__common: 0x8
   __DATA.__bss: 0x34
-  __DATA_DIRTY.__objc_data: 0x2d0
-  __DATA_DIRTY.__data: 0x150
+  __DATA_DIRTY.__objc_data: 0x370
+  __DATA_DIRTY.__data: 0x1c0
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/Sharing.framework/Sharing
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1030
-  Symbols:   1232
-  CStrings:  2199
+  Functions: 1136
+  Symbols:   1340
+  CStrings:  2474
 
Symbols:
+ _OBJC_CLASS_$_HMDeviceCloudRecordInfo
+ _OBJC_METACLASS_$_HMDeviceCloudRecordInfo
CStrings:
+ "-[AACloudServicesClient removeHMDeviceCloudRecordInfoForDeviceWithAddress:completion:]_block_invoke_2"
+ "enableHearingAssist"
+ "setHearingAssistVersion:"
+ "setFrontVentFaultCountLeft:"
+ "rvfl"
+ ", HA Top Level %!s(MISSING)"
+ "Tc,N,V_enableHearingAidGainSwipe"
+ "TC,R,N,V_hearingAidConfig"
+ ", Rvnt flt L %!@(MISSING)"
+ ", Tmi flt L %!@(MISSING)"
+ "_frontVentFaultCountRight"
+ "_innerMicFaultCountRight"
+ "haGS"
+ ", Spk flt R %!@(MISSING)"
+ "removeHMDeviceCloudRecordInfoForDeviceWithAddress:completion:"
+ ", HR Ast %!l(MISSING)lu"
+ "T@\"NSNumber\",&,N,V_speakerFaultCountLeft"
+ "v32@0:8@\"NSString\"16@?<v@?@\"HMDeviceCloudRecordInfo\"@\"NSError\">24"
+ "TC,N,V_hearingAidCapability"
+ "@\"NSNumber\""
+ "tmfr"
+ "thdl"
+ "hOf"
+ "latestDiagnosticTimestampLeft"
+ "_innerMicFaultCountLeft"
+ "setSwipeGainEnabled:"
+ "agET"
+ "-[AACloudServicesClient fetchHMDeviceCloudRecordInfoWithAddress:completion:]_block_invoke_2"
+ ", En HA GS %!s(MISSING)"
+ "rearVentFaultCountLeft"
+ "imfr"
+ ", En Tp HA %!s(MISSING)"
+ "_pmeVoiceEnabled"
+ "eHSS"
+ "fafl"
+ ", IMi flt R %!@(MISSING)"
+ "htcp"
+ "dimc"
+ "diagnosticMeasurementsCount"
+ "totalHarmonicDistortionFaultCountLeft"
+ "T@?,C,N,V_hmDeviceCloudRecordUpdateHandler"
+ "\x11\x11\x15"
+ "setHearingTestVersion:"
+ "hpRegionStatus"
+ "\x1f\x05"
+ "mediaAssistEnabled"
+ "setPmeVoiceEnabled:"
+ ", Fvnt flt L %!@(MISSING)"
+ "frontVentFaultCountRight"
+ "setRearVentFaultCountLeft:"
+ "@\"NSDate\""
+ "_hmDeviceCloudRecordUpdateHandler"
+ "_hearingAssistEnabled"
+ "setTotalHarmonicDistortionFaultCountRight:"
+ "setInnerMicFaultCountLeft:"
+ ", Tmi flt R %!@(MISSING)"
+ "Tc,N,V_hearingAidEnabled"
+ ", Frq Acc L %!@(MISSING)"
+ ", HA GS %!s(MISSING)"
+ ", HA Cfg %!s(MISSING)"
+ "setFreqAccuracyFaultCountLeft:"
+ "thdr"
+ "frontVentFaultCountLeft"
+ "_hearingAidGainSwipeEnabled"
+ "_hearingProtectionCapability"
+ ", IMi flt L %!@(MISSING)"
+ "hearingAidConfig"
+ "TC,N,V_hearingProtectionCapability"
+ "TC,N,V_hearingTestCapability"
+ "bmfl"
+ "hearingAidEnabled"
+ "setFrontVentFaultCountRight:"
+ "eHAS"
+ ", AG EnrolledTime '%!@(MISSING)'"
+ ", HR Tst %!l(MISSING)lu"
+ ", ltst dg T L %!@(MISSING)"
+ "hearingProtectionCapability"
+ "setHpRegionStatus:"
+ "ldtr"
+ "setPmeMediaEnabled:"
+ "_latestDiagnosticTimestampRight"
+ ", Swp Gn En %!d(MISSING)"
+ ", HA rgn St %!d(MISSING)"
+ "_hearingAidEnabled"
+ "setFreqAccuracyFaultCountRight:"
+ "setInnerMicFaultCountRight:"
+ "_enableHearingAssist"
+ "hideOffListeningModeCapability"
+ ", PME-V En %!d(MISSING)"
+ "_hearingTestCapability"
+ "_topMicFaultCountLeft"
+ "setHearingAidEnabled:"
+ ", ltst dg T R %!@(MISSING)"
+ "HearingAid"
+ "swGn"
+ "_hearingAidCapability"
+ "T@\"NSDate\",C,N,V_audiogramEnrolledTimestamp"
+ "setTotalHarmonicDistortionFaultCountLeft:"
+ ", Rvnt flt R %!@(MISSING)"
+ "setLatestDiagnosticTimestampLeft:"
+ "ConnectedAudio"
+ "sfcl"
+ "topMicFaultCountLeft"
+ "_haRegionStatus"
+ ", Spk flt L %!@(MISSING)"
+ "Tc,N,V_hearingAssistEnabled"
+ "_topMicFaultCountRight"
+ "speakerFaultCountRight"
+ "Nil HMDeviceCloudRecordInfo"
+ "Tc,N,V_enableHearingAssist"
+ "haCp"
+ "_totalHarmonicDistortionFaultCountLeft"
+ "haRegionStatus"
+ "v32@0:8@\"HMDeviceCloudRecordInfo\"16@?<v@?@\"NSError\">24"
+ "rvfr"
+ "T@\"NSNumber\",&,N,V_totalHarmonicDistortionFaultCountRight"
+ "_hearingAidToggle"
+ "TC,N,V_hideOffListeningModeCapability"
+ "setRearVentFaultCountRight:"
+ "Tc,V_mediaAssistEnabled"
+ ", Hr Aid En %!s(MISSING)"
+ "_latestDiagnosticTimestampLeft"
+ "hearingAidGainSwipeEnabled"
+ "_speakerFaultCountLeft"
+ "hearingTestVersion"
+ "bmfr"
+ "pmME"
+ "T@\"NSNumber\",&,N,V_freqAccuracyFaultCountRight"
+ "Tc,N,V_hearingAidEnrolled"
+ "setHearingProtectionCapability:"
+ "T@\"NSNumber\",&,N,V_topMicFaultCountRight"
+ "haRS"
+ "CID 0x%!X(MISSING), reporting %!d(MISSING) updates for HMDeviceCloudRecordInfo"
+ ", Dg Ms Cnt %!@(MISSING)"
+ "_totalHarmonicDistortionFaultCountRight"
+ "hAT"
+ "T@\"NSNumber\",&,N,V_innerMicFaultCountRight"
+ "_freqAccuracyFaultCountLeft"
+ "Tc,N,V_hearingAidGainSwipeEnabled"
+ "_enableHearingAidGainSwipe"
+ ", HP Cap %!s(MISSING)"
+ "hgTs"
+ "hmDeviceCloudRecordInfosUpdated:"
+ "HearingProtection"
+ "hpCp"
+ "setTopMicFaultCountLeft:"
+ "TC,V_hpRegionStatus"
+ "\x85"
+ "setHearingAssistEnabled:"
+ "_mediaAssistEnabled"
+ "T@\"NSDate\",&,N,V_latestDiagnosticTimestampRight"
+ "### Modify HMDeviceCloudRecordInfo failed: %!@(MISSING), %!{(MISSING)error}"
+ "T@\"NSNumber\",&,N,V_diagnosticMeasurementsCount"
+ "TC,V_haRegionStatus"
+ "T@\"NSNumber\",&,N,V_speakerFaultCountRight"
+ "bottomMicFaultCountLeft"
+ "hearingAidEnrolled"
+ "fvfr"
+ ", HA Cap %!s(MISSING)"
+ "-[AACloudServicesClient modifyHMDeviceCloudRecordInfo:completion:]_block_invoke"
+ "haEn"
+ "fetchHMDeviceCloudRecordInfoWithAddress:completion:"
+ "fvfl"
+ ", MA En  %!d(MISSING)"
+ "innerMicFaultCountRight"
+ "T@\"NSNumber\",&,N,V_frontVentFaultCountLeft"
+ "setHearingAidGainSwipeEnabled:"
+ "T@\"NSNumber\",&,N,V_bottomMicFaultCountRight"
+ "-[AACloudServicesClient modifyHMDeviceCloudRecordInfo:completion:]_block_invoke_2"
+ "HearingTest"
+ "rearVentFaultCountRight"
+ "setAudiogramEnrolledTimestamp:"
+ "-[AACloudServicesClient removeHMDeviceCloudRecordInfoForDeviceWithAddress:completion:]_block_invoke"
+ "setHaRegionStatus:"
+ "_rearVentFaultCountRight"
+ "setHearingAidCapability:"
+ "setHearingAidEnrolled:"
+ "setMediaAssistEnabled:"
+ "b"
+ "setHmDeviceCloudRecordUpdateHandler:"
+ "_audiogramEnrolledTimestamp"
+ "_swipeGainEnabled"
+ ", BMi flt R %!@(MISSING)"
+ "tmfl"
+ "setBottomMicFaultCountLeft:"
+ "No HMDeviceCloudRecordInfo update handler set for client ID 0x%!X(MISSING)"
+ "pmeMediaEnabled"
+ "Modify HMDeviceCloudRecordInfo: %!@(MISSING)"
+ "_pmeMediaEnabled"
+ "setHearingAidToggle:"
+ "setSpeakerFaultCountLeft:"
+ "ldtl"
+ ", HT Cap %!s(MISSING)"
+ "-[AACloudServicesClient hmDeviceCloudRecordInfosUpdated:]"
+ "T@\"NSNumber\",&,N,V_rearVentFaultCountRight"
+ "setTopMicFaultCountRight:"
+ "TQ,V_hearingAssistVersion"
+ "topMicFaultCountRight"
+ "haCg"
+ "### Failed to fetch HMDeviceCloudRecordInfo, %!{(MISSING)error}"
+ "T@\"NSNumber\",&,N,V_rearVentFaultCountLeft"
+ "hearingAidCapability"
+ "T@\"NSNumber\",&,N,V_frontVentFaultCountRight"
+ "_hpRegionStatus"
+ "_hearingAidConfig"
+ "hgAs"
+ "innerMicFaultCountLeft"
+ "fafr"
+ ", HP rgn St %!d(MISSING)"
+ "pmVE"
+ "hearingAssistVersion"
+ "maEn"
+ "setEnableHearingAssist:"
+ "_speakerFaultCountRight"
+ ", HA Enr %!s(MISSING)"
+ ", PME-M En %!d(MISSING)"
+ "_bottomMicFaultCountLeft"
+ "enableHearingAidGainSwipe"
+ "TQ,V_hearingTestVersion"
+ "hearingAidToggle"
+ ", Fvnt flt R %!@(MISSING)"
+ "hpRS"
+ "totalHarmonicDistortionFaultCountRight"
+ "setSpeakerFaultCountRight:"
+ "_hideOffListeningModeCapability"
+ "setEnableHearingAidGainSwipe:"
+ "_rearVentFaultCountLeft"
+ "pmeVoiceEnabled"
+ "T@\"NSNumber\",&,N,V_bottomMicFaultCountLeft"
+ "modifyHMDeviceCloudRecordInfo:completion:"
+ "setHideOffListeningModeCapability:"
+ ", THrm Dst L %!@(MISSING)"
+ "audiogramEnrolledTimestamp"
+ "_hearingAidEnrolled"
+ "### Failed to remove HMDeviceCloudRecordInfo, %!{(MISSING)error}"
+ "Tc,N,V_hearingAidToggle"
+ "imfl"
+ "HMDeviceCloudRecordInfo"
+ "Tc,V_pmeMediaEnabled"
+ "_freqAccuracyFaultCountRight"
+ "Fetching HMDeviceCloudRecordInfo"
+ "setBottomMicFaultCountRight:"
+ "Removing HMDeviceCloudRecordInfo"
+ "freqAccuracyFaultCountRight"
+ "setDiagnosticMeasurementsCount:"
+ "_hearingTestVersion"
+ "swipeGainEnabled"
+ "T@\"NSNumber\",&,N,V_topMicFaultCountLeft"
+ "hearingAssistEnabled"
+ "_bottomMicFaultCountRight"
+ "T@\"NSNumber\",&,N,V_totalHarmonicDistortionFaultCountLeft"
+ "Tc,V_pmeVoiceEnabled"
+ "freqAccuracyFaultCountLeft"
+ "hAE"
+ ", Frq Acc R %!@(MISSING)"
+ "sfcr"
+ "_diagnosticMeasurementsCount"
+ "_hearingAssistVersion"
+ "setLatestDiagnosticTimestampRight:"
+ "hearingTestCapability"
+ "bottomMicFaultCountRight"
+ ", BMi flt L %!@(MISSING)"
+ "T@\"NSNumber\",&,N,V_freqAccuracyFaultCountLeft"
+ "hmDeviceCloudRecordInfosRemoved:"
+ "-[AACloudServicesClient fetchHMDeviceCloudRecordInfoWithAddress:completion:]_block_invoke"
+ "hmDeviceCloudRecordUpdateHandler"
+ "speakerFaultCountLeft"
+ "Tc,V_swipeGainEnabled"
+ "_frontVentFaultCountLeft"
+ "hrAE"
+ "setHearingTestCapability:"
+ "T@\"NSDate\",&,N,V_latestDiagnosticTimestampLeft"
+ "T@\"NSNumber\",&,N,V_innerMicFaultCountLeft"
+ ", Hide Off Cap %!s(MISSING)"
+ ", THrm Dst R %!@(MISSING)"
+ "v24@0:8@\"NSArray\"16"
+ "latestDiagnosticTimestampRight"
- "t"
- "a"

```
