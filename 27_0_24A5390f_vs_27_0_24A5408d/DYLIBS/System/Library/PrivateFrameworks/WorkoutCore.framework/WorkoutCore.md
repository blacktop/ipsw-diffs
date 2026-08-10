## WorkoutCore

> `/System/Library/PrivateFrameworks/WorkoutCore.framework/WorkoutCore`

### Sections with Same Size but Changed Content

- `__TEXT.__oslogstring`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_protos`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`

```diff

-2027.0.137.0.0
-  __TEXT.__text: 0x5f5230
-  __TEXT.__objc_methlist: 0xbb44
-  __TEXT.__const: 0x348c0
-  __TEXT.__cstring: 0xeeea
+2027.0.152.1.1
+  __TEXT.__text: 0x5f58f0
+  __TEXT.__objc_methlist: 0xbc34
+  __TEXT.__const: 0x34900
+  __TEXT.__cstring: 0xeeca
   __TEXT.__oslogstring: 0x20dd9
   __TEXT.__gcc_except_tab: 0xe90
   __TEXT.__dlopen_cstrs: 0x62
-  __TEXT.__constg_swiftt: 0x1173c
-  __TEXT.__swift5_typeref: 0xa448
+  __TEXT.__constg_swiftt: 0x11760
+  __TEXT.__swift5_typeref: 0xa452
   __TEXT.__swift5_builtin: 0x3c0
-  __TEXT.__swift5_reflstr: 0xd850
-  __TEXT.__swift5_fieldmd: 0xb734
+  __TEXT.__swift5_reflstr: 0xd910
+  __TEXT.__swift5_fieldmd: 0xb7a4
   __TEXT.__swift5_assocty: 0x1c10
   __TEXT.__swift5_proto: 0x1cd0
-  __TEXT.__swift5_types: 0xb1c
-  __TEXT.__swift5_capture: 0x5064
+  __TEXT.__swift5_types: 0xb20
+  __TEXT.__swift5_capture: 0x5024
   __TEXT.__swift_as_entry: 0x480
   __TEXT.__swift_as_ret: 0x4e4
   __TEXT.__swift_as_cont: 0xa50
   __TEXT.__swift5_mpenum: 0x74
   __TEXT.__swift5_protos: 0x1a8
-  __TEXT.__unwind_info: 0x14c10
-  __TEXT.__eh_frame: 0x19840
+  __TEXT.__unwind_info: 0x14c40
+  __TEXT.__eh_frame: 0x19850
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x4dd8
-  __DATA_CONST.__objc_classlist: 0xbc8
+  __DATA_CONST.__const: 0x4df8
+  __DATA_CONST.__objc_classlist: 0xbd0
   __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0x5e0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5748
+  __DATA_CONST.__objc_selrefs: 0x57e8
   __DATA_CONST.__objc_protorefs: 0x2b8
   __DATA_CONST.__objc_superrefs: 0x1d8
   __DATA_CONST.__objc_arraydata: 0x1a8
   __DATA_CONST.__got: 0x22b0
-  __AUTH_CONST.__const: 0x1c4b8
-  __AUTH_CONST.__cfstring: 0x3160
-  __AUTH_CONST.__objc_const: 0x1fbd8
+  __AUTH_CONST.__const: 0x1c418
+  __AUTH_CONST.__cfstring: 0x31c0
+  __AUTH_CONST.__objc_const: 0x1fd70
   __AUTH_CONST.__objc_intobj: 0x528
   __AUTH_CONST.__objc_arrayobj: 0x2e8
-  __AUTH_CONST.__auth_got: 0x2ea8
-  __AUTH.__objc_data: 0xd110
-  __AUTH.__data: 0xa498
+  __AUTH_CONST.__auth_got: 0x2eb0
+  __AUTH.__objc_data: 0xd200
+  __AUTH.__data: 0xa4b8
   __DATA.__objc_ivar: 0x5e8
-  __DATA.__data: 0xa520
+  __DATA.__data: 0xa500
   __DATA.__bss: 0x30840
   __DATA.__common: 0x3f8
-  __DATA_DIRTY.__objc_data: 0x4c90
-  __DATA_DIRTY.__data: 0x5c18
+  __DATA_DIRTY.__objc_data: 0x4c88
+  __DATA_DIRTY.__data: 0x5be8
   __DATA_DIRTY.__bss: 0x6850
   __DATA_DIRTY.__common: 0x208
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/MusicKitInternal.framework/MusicKitInternal
   - /System/Library/PrivateFrameworks/NanoPreferencesSync.framework/NanoPreferencesSync
-  - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
+  - /System/Library/PrivateFrameworks/PairedDeviceRegistry.framework/PairedDeviceRegistry
   - /System/Library/PrivateFrameworks/PairedUnlock.framework/PairedUnlock
   - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
   - /System/Library/PrivateFrameworks/Rapport.framework/Rapport

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 37257
-  Symbols:   62762
+  Functions: 37279
+  Symbols:   62815
   CStrings:  3625
 
Symbols:
+ -[NLAnalyticsWorkoutEventBuilder recordLocalConnectedMediaDuration:]
+ -[NLAnalyticsWorkoutEventBuilder recordLocalStandaloneMediaDuration:]
+ -[NLAnalyticsWorkoutEventBuilder recordRemoteConnectedMediaDuration:]
+ -[NLAnalyticsWorkoutEventBuilder recordStandaloneDuration:]
+ _$s11WorkoutCore0A22MediaStandaloneAccrualC014localConnectedC8DurationSdvg
+ _$s11WorkoutCore0A22MediaStandaloneAccrualC014localConnectedC8DurationSdvgTo
+ _$s11WorkoutCore0A22MediaStandaloneAccrualC014localConnectedC8DurationSdvpMV
+ _$s11WorkoutCore0A22MediaStandaloneAccrualC014localConnectedC8DurationSdvpWvd
+ _$s11WorkoutCore0A22MediaStandaloneAccrualC014localConnectedC8DurationSdvsTo
+ _$s11WorkoutCore0A22MediaStandaloneAccrualC015remoteConnectedC8DurationSdvg
+ _$s11WorkoutCore0A22MediaStandaloneAccrualC015remoteConnectedC8DurationSdvgTo
+ _$s11WorkoutCore0A22MediaStandaloneAccrualC015remoteConnectedC8DurationSdvpMV
+ _$s11WorkoutCore0A22MediaStandaloneAccrualC015remoteConnectedC8DurationSdvpWvd
+ _$s11WorkoutCore0A22MediaStandaloneAccrualC015remoteConnectedC8DurationSdvsTo
+ _$s11WorkoutCore0A22MediaStandaloneAccrualC05localdC8DurationSdvg
+ _$s11WorkoutCore0A22MediaStandaloneAccrualC05localdC8DurationSdvgTo
+ _$s11WorkoutCore0A22MediaStandaloneAccrualC05localdC8DurationSdvpMV
+ _$s11WorkoutCore0A22MediaStandaloneAccrualC05localdC8DurationSdvpWvd
+ _$s11WorkoutCore0A22MediaStandaloneAccrualC05localdC8DurationSdvsTo
+ _$s11WorkoutCore0A22MediaStandaloneAccrualC12applyPlaying_13atElapsedTimeySb_SdtF
+ _$s11WorkoutCore0A22MediaStandaloneAccrualC12applyPlaying_13atElapsedTimeySb_SdtFTo
+ _$s11WorkoutCore0A22MediaStandaloneAccrualC12encodedStateSSSgyF
+ _$s11WorkoutCore0A22MediaStandaloneAccrualC12encodedStateSSSgyFTo
+ _$s11WorkoutCore0A22MediaStandaloneAccrualC15companionNearby33_1D2F7B5D418DD7EC37940839E3B0B987LLSbvpWvd
+ _$s11WorkoutCore0A22MediaStandaloneAccrualC16applyLocalOrigin_13atElapsedTimeySb_SdtF
+ _$s11WorkoutCore0A22MediaStandaloneAccrualC16applyLocalOrigin_13atElapsedTimeySb_SdtFTo
+ _$s11WorkoutCore0A22MediaStandaloneAccrualC18standaloneDurationSdvg
+ _$s11WorkoutCore0A22MediaStandaloneAccrualC18standaloneDurationSdvgTo
+ _$s11WorkoutCore0A22MediaStandaloneAccrualC18standaloneDurationSdvpMV
+ _$s11WorkoutCore0A22MediaStandaloneAccrualC18standaloneDurationSdvpWvd
+ _$s11WorkoutCore0A22MediaStandaloneAccrualC18standaloneDurationSdvsTo
+ _$s11WorkoutCore0A22MediaStandaloneAccrualC20applyCompanionNearby_13atElapsedTimeySb_SdtF
+ _$s11WorkoutCore0A22MediaStandaloneAccrualC20applyCompanionNearby_13atElapsedTimeySb_SdtFTo
+ _$s11WorkoutCore0A22MediaStandaloneAccrualC21lastTransitionElapsed33_1D2F7B5D418DD7EC37940839E3B0B987LLSdvpWvd
+ _$s11WorkoutCore0A22MediaStandaloneAccrualC5close13atElapsedTimeySd_tF
+ _$s11WorkoutCore0A22MediaStandaloneAccrualC5close13atElapsedTimeySd_tFTo
+ _$s11WorkoutCore0A22MediaStandaloneAccrualC6accrue33_1D2F7B5D418DD7EC37940839E3B0B987LL5untilySd_tF
+ _$s11WorkoutCore0A22MediaStandaloneAccrualC7isLocal33_1D2F7B5D418DD7EC37940839E3B0B987LLSbSgvpWvd
+ _$s11WorkoutCore0A22MediaStandaloneAccrualC7restore16fromEncodedStateySS_tF
+ _$s11WorkoutCore0A22MediaStandaloneAccrualC7restore16fromEncodedStateySS_tFTo
+ _$s11WorkoutCore0A22MediaStandaloneAccrualC9isPlaying33_1D2F7B5D418DD7EC37940839E3B0B987LLSbvpWvd
+ _$s11WorkoutCore0A22MediaStandaloneAccrualCACycfC
+ _$s11WorkoutCore0A22MediaStandaloneAccrualCACycfc
+ _$s11WorkoutCore0A22MediaStandaloneAccrualCACycfcTo
+ _$s11WorkoutCore0A22MediaStandaloneAccrualCMF
+ _$s11WorkoutCore0A22MediaStandaloneAccrualCMa
+ _$s11WorkoutCore0A22MediaStandaloneAccrualCMf
+ _$s11WorkoutCore0A22MediaStandaloneAccrualCMn
+ _$s11WorkoutCore0A22MediaStandaloneAccrualCMo
+ _$s11WorkoutCore0A22MediaStandaloneAccrualCN
+ _$s11WorkoutCore0A22MediaStandaloneAccrualCfD
+ _$s11WorkoutCore15LocationManagerC6remove8observeryAA0cD8Observer_p_tFTf4en_nAA04RaceC8ProviderC_Tg5
+ _$s11WorkoutCore15LocationManagerC6remove8observeryAA0cD8Observer_p_tFTf4en_nAA0C19PositionAccumulatorC_Tg5
+ _$s11WorkoutCore15LocationManagerC6remove8observeryAA0cD8Observer_p_tFTf4en_nAA15GPSLockProviderC_Tg5Tm
+ _$s11WorkoutCore15LocationManagerC6remove8observeryAA0cD8Observer_p_tFyyYbcfU_
+ _$s11WorkoutCore15LocationManagerC6remove8observeryAA0cD8Observer_p_tFyyYbcfU_TA
+ _$s11WorkoutCore17DispatchUtilitiesC22ensureMainQueueOrAsync5blockyyyc_tFZ13$sIeyB_Ieg_TRIeyB_Tf1En_nTf4dn_n
+ _$s11WorkoutCore20UserDevicesBehaviorsC14hasPairedWatchSbvgToTm
+ _$s11WorkoutCore31DataLinkHealthKitHostConnectionC012sendMirroredg8IntervalA19ConfigurationUpdate_8sequence7closureyAA0kaL0C_10Foundation4UUIDVySb_s5Error_pSgtctF04$s11a6Core12cdg18C012sendMirrorede8k3A19lm31_12acknowledgedyAA0haI0C_ySb_s5R19_pSgtctFySb_AItcfU_SbAMIegyg_Tf1nnEn_n
+ _$s11WorkoutCore35CyclingPowerZonesConfigurationStoreC06createcdeF12FromAppleFTP33_B4BFFB0062EFA9F42DAC8E12BD49C0D5LL13configuration10completionyAA0cdeF0C_yAIctF04$s11a6Core35cdefG86C05fetchcdeF010completionyyAA0cdeF0Cc_tFy10Foundation4DataVSg_s5Error_pSgtcfU_yAGcfU0_AIIegg_Tf1nEn_nTm
+ _$s19FitnessIntelligence28InferenceTelemetryIdentifierV6DeviceO7defaultAEvgZ
+ _$s19FitnessIntelligence28InferenceTelemetryIdentifierV6DeviceOMa
+ _$s19FitnessIntelligence28InferenceTelemetryIdentifierV7FeatureO20workoutVoiceTTSAlertyA2EmFWC
+ _$s19FitnessIntelligence28InferenceTelemetryIdentifierV7FeatureOMa
+ _$s19FitnessIntelligence28InferenceTelemetryIdentifierV7feature6deviceA2C7FeatureO_AC6DeviceOtcfC
+ _$sSo27NLWorkoutRecoveryControllerC11WorkoutCoreE011handleCrashB033_EA8A5E8FD595D3C822F31B2CD26675EALL7session5error10completionySo16HKWorkoutSessionCSg_s5Error_pSgyyctF06$sSo27abc3C11de14E24recoverFromg33IfNeeded10completionyySbc_tFySo16uv6CSg_s5W33_pSgtYbcfU_ytSgyYaScMYccfU_yycfU_SbIegy_SbTf1nnEn_n
+ _$sSo9PDRDeviceCML
+ _$sSo9PDRDeviceCMa
+ _OBJC_CLASS_$_PDRDevice
+ _OBJC_CLASS_$_PDRRegistry
+ _OBJC_CLASS_$_WOMediaStandaloneAccrual
+ _OBJC_METACLASS_$_WOMediaStandaloneAccrual
+ _PDRDevicePropertyKeyProductType
+ _PDRDidActivateNotification
+ _PDRDidDeactivateNotification
+ _PDRDidPairNotification
+ _PDRDidUnpairNotification
+ __DATA_WOMediaStandaloneAccrual
+ __INSTANCE_METHODS_WOMediaStandaloneAccrual
+ __IVARS_WOMediaStandaloneAccrual
+ __METACLASS_DATA_WOMediaStandaloneAccrual
+ __PROPERTIES_WOMediaStandaloneAccrual
+ ___swift_closure_destructor.48Tm
+ _keypath_get.6Tm
+ _keypath_set.7Tm
+ _objc_msgSend$applicationIsInstalledOnDeviceWithPairingID:withBundleID:completion:
+ _objc_msgSend$getActivePairedDeviceIncludingAltAccount
+ _objc_msgSend$isAltAccount
+ _symbolic Sv
+ _symbolic _____ 11WorkoutCore0A22MediaStandaloneAccrualC
- _$s11WorkoutCore0A15DevicesProviderC16setAppForegroundyySbF
- _$s11WorkoutCore0A15DevicesProviderC16setAppForegroundyySbFTj
- _$s11WorkoutCore0A15DevicesProviderC16setAppForegroundyySbFTq
- _$s11WorkoutCore15LocationManagerC6remove8observeryAA0cD8Observer_p_tFyyXEfU_
- _$s11WorkoutCore15LocationManagerC6remove8observeryAA0cD8Observer_p_tFyyXEfU_TA
- _$s11WorkoutCore17DispatchUtilitiesC22ensureMainQueueOrAsync5blockyyyc_tFZ13$sIeyB_Ieg_TRIeyB_Tf1cn_nTf4dn_n
- _$s11WorkoutCore31DataLinkHealthKitHostConnectionC012sendMirroredg8IntervalA19ConfigurationUpdate_8sequence7closureyAA0kaL0C_10Foundation4UUIDVySb_s5Error_pSgtctF04$s11a6Core12cdg18C012sendMirrorede8k3A19lm31_12acknowledgedyAA0haI0C_ySb_s5R19_pSgtctFySb_AItcfU_SbAMIegyg_Tf1nncn_n
- _$s11WorkoutCore32MediaPlaybackDeviceCompatibilityV33NRDEVICECAPABILITY_NAPILI_ALIGNED33_ADDDDFEA13DE2CF8CFB5C03A9F9EAC0FLL10Foundation4UUIDVSgvpZ
- _$s11WorkoutCore32MediaPlaybackDeviceCompatibilityV33NRDEVICECAPABILITY_NAPILI_ALIGNED33_ADDDDFEA13DE2CF8CFB5C03A9F9EAC0FLL_WZ
- _$s11WorkoutCore32MediaPlaybackDeviceCompatibilityV33NRDEVICECAPABILITY_NAPILI_ALIGNED33_ADDDDFEA13DE2CF8CFB5C03A9F9EAC0FLL_Wz
- _$s11WorkoutCore32MediaPlaybackDeviceCompatibilityV34NRDEVICECAPABILITY_NAPILIB_ALIGNED33_ADDDDFEA13DE2CF8CFB5C03A9F9EAC0FLL10Foundation4UUIDVSgvpZ
- _$s11WorkoutCore32MediaPlaybackDeviceCompatibilityV34NRDEVICECAPABILITY_NAPILIB_ALIGNED33_ADDDDFEA13DE2CF8CFB5C03A9F9EAC0FLL_WZ
- _$s11WorkoutCore32MediaPlaybackDeviceCompatibilityV34NRDEVICECAPABILITY_NAPILIB_ALIGNED33_ADDDDFEA13DE2CF8CFB5C03A9F9EAC0FLL_Wz
- _$s11WorkoutCore35CyclingPowerZonesConfigurationStoreC06createcdeF12FromAppleFTP33_B4BFFB0062EFA9F42DAC8E12BD49C0D5LL13configuration10completionyAA0cdeF0C_yAIctF04$s11a6Core35cdefG86C05fetchcdeF010completionyyAA0cdeF0Cc_tFy10Foundation4DataVSg_s5Error_pSgtcfU_yAGcfU0_AIIegg_Tf1ncn_nTm
- _$s11WorkoutCore36DataLinkBackwardCompatibilityUtilityV19NAPILI_ALIGNED_UUID33_F4B4E6A3AC471180D632F6E561D9C101LL10Foundation0J0VSgvpZ
- _$s11WorkoutCore36DataLinkBackwardCompatibilityUtilityV19NAPILI_ALIGNED_UUID33_F4B4E6A3AC471180D632F6E561D9C101LL_WZ
- _$s11WorkoutCore36DataLinkBackwardCompatibilityUtilityV19NAPILI_ALIGNED_UUID33_F4B4E6A3AC471180D632F6E561D9C101LL_Wz
- _$s11WorkoutCore36DataLinkBackwardCompatibilityUtilityV19ORCHID_ALIGNED_UUID33_F4B4E6A3AC471180D632F6E561D9C101LL10Foundation0J0VSgvpZ
- _$s11WorkoutCore36DataLinkBackwardCompatibilityUtilityV19ORCHID_ALIGNED_UUID33_F4B4E6A3AC471180D632F6E561D9C101LL_WZ
- _$s11WorkoutCore36DataLinkBackwardCompatibilityUtilityV19ORCHID_ALIGNED_UUID33_F4B4E6A3AC471180D632F6E561D9C101LL_Wz
- _$s19FitnessIntelligence27DeviceInferenceAvailabilityVSgWOcTm
- _$sSo27NLWorkoutRecoveryControllerC11WorkoutCoreE011handleCrashB033_EA8A5E8FD595D3C822F31B2CD26675EALL7session5error10completionySo16HKWorkoutSessionCSg_s5Error_pSgyyctF06$sSo27abc3C11de14E24recoverFromg33IfNeeded10completionyySbc_tFySo16uv6CSg_s5W33_pSgtYbcfU_ytSgyYaScMYccfU_yycfU_SbIegy_SbTf1nncn_n
- _$sSo8NRDeviceCML
- _$sSo8NRDeviceCMa
- _FIGetActivePairedDevice
- _NRDevicePropertyIsAltAccount
- _NRDevicePropertyProductType
- _NRPairedDeviceRegistryDeviceDidBecomeActive
- _NRPairedDeviceRegistryDeviceDidBecomeInactive
- _NRPairedDeviceRegistryDeviceDidPairNotification
- _NRPairedDeviceRegistryDeviceDidUnpairNotification
- _OBJC_CLASS_$_NRDevice
- _OBJC_CLASS_$_NRPairedDeviceRegistry
- ___swift_closure_destructor.62Tm
- _objc_autoreleasePoolPop
- _objc_autoreleasePoolPush
- _objc_msgSend$applicationIsInstalledOnPairedDevice:withBundleID:completion:
CStrings:
+ "[Location Manager] Removing observer at %s"
+ "media_playback_local_connected_duration"
+ "media_playback_local_standalone_duration"
+ "media_playback_remote_connected_duration"
+ "watch_standalone_duration"
- "0B0171D3-B1DB-4B4A-BC75-14ACB7BB9592"
- "A781CB9F-0000-8000-8000-000000000000"
- "D5834418-F4A0-4C74-AA38-8ED5F7765BD1"
- "[Location Manager] Removing observer: %s"
- "c26ad300-9198-11ec-8bc2-0800200c9a66"
```
