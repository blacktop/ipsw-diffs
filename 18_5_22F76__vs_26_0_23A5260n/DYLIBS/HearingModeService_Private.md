## HearingModeService_Private

> `/System/Library/PrivateFrameworks/HearingModeService_Private.framework/HearingModeService_Private`

```diff

-25.4.0.0.0
-  __TEXT.__text: 0x10d80
-  __TEXT.__auth_stubs: 0x490
-  __TEXT.__objc_methlist: 0xb3c
+30.45.3.0.0
+  __TEXT.__text: 0x12368
+  __TEXT.__auth_stubs: 0x4b0
+  __TEXT.__objc_methlist: 0xc34
   __TEXT.__const: 0x86
-  __TEXT.__gcc_except_tab: 0x4c4
-  __TEXT.__cstring: 0x4755
-  __TEXT.__unwind_info: 0x578
-  __TEXT.__objc_classname: 0x135
-  __TEXT.__objc_methname: 0x3168
-  __TEXT.__objc_methtype: 0x823
-  __TEXT.__objc_stubs: 0x2d20
-  __DATA_CONST.__got: 0x1d8
-  __DATA_CONST.__const: 0x808
-  __DATA_CONST.__objc_classlist: 0x30
+  __TEXT.__gcc_except_tab: 0x514
+  __TEXT.__cstring: 0x4dd9
+  __TEXT.__unwind_info: 0x5c8
+  __TEXT.__objc_classname: 0x14d
+  __TEXT.__objc_methname: 0x33f8
+  __TEXT.__objc_methtype: 0x8af
+  __TEXT.__objc_stubs: 0x2f20
+  __DATA_CONST.__got: 0x1e0
+  __DATA_CONST.__const: 0x858
+  __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd60
+  __DATA_CONST.__objc_selrefs: 0xde8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x258
-  __AUTH_CONST.__const: 0x140
-  __AUTH_CONST.__cfstring: 0x3e0
-  __AUTH_CONST.__objc_const: 0x1360
+  __DATA_CONST.__objc_superrefs: 0x30
+  __AUTH_CONST.__auth_got: 0x268
+  __AUTH_CONST.__const: 0x160
+  __AUTH_CONST.__cfstring: 0x6c0
+  __AUTH_CONST.__objc_const: 0x1498
   __AUTH_CONST.__objc_doubleobj: 0x80
-  __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0xb0
-  __DATA.__data: 0x380
+  __AUTH_CONST.__objc_intobj: 0x18
+  __AUTH.__objc_data: 0xf0
+  __DATA.__objc_ivar: 0xbc
+  __DATA.__data: 0x3f0
   __DATA_DIRTY.__objc_data: 0x140
   __DATA_DIRTY.__data: 0x150
-  __DATA_DIRTY.__bss: 0x50
+  __DATA_DIRTY.__bss: 0x60
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/PrivateFrameworks/ToneLibrary.framework/ToneLibrary
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7A1B088C-55B6-353F-A32F-119377DC560B
-  Functions: 395
-  Symbols:   1518
-  CStrings:  1000
+  UUID: 717ACE5A-8994-3EF5-B66A-158CDF3B9040
+  Functions: 423
+  Symbols:   1609
+  CStrings:  1091
 
Symbols:
+ +[HMSettingsTelemetry sharedInstance]
+ +[HMSettingsTelemetry sharedInstance].cold.1
+ -[HMDeviceManager _populateV1Struct:identifier:deviceRecord:hmSettingsStruct:]
+ -[HMDeviceManager _populateV1Struct:identifier:deviceRecord:hmSettingsStruct:].cold.1
+ -[HMDeviceManager _populateV1Struct:identifier:deviceRecord:hmSettingsStruct:].cold.2
+ -[HMDeviceManager _populateV1Struct:identifier:deviceRecord:hmSettingsStruct:].cold.3
+ -[HMDeviceManager _populateV1Struct:identifier:deviceRecord:hmSettingsStruct:].cold.4
+ -[HMDeviceManager _populateV1Struct:identifier:deviceRecord:hmSettingsStruct:].cold.5
+ -[HMDeviceManager _populateV1Struct:identifier:deviceRecord:hmSettingsStruct:].cold.6
+ -[HMDeviceManager _populateV1Struct:identifier:deviceRecord:hmSettingsStruct:].cold.7
+ -[HMDeviceManager _populateV1Struct:identifier:deviceRecord:hmSettingsStruct:].cold.8
+ -[HMDeviceManager _submitHearingFeaturesMetricFor:]
+ -[HMDeviceManager _submitHearingFeaturesMetricFor:].cold.1
+ -[HMDeviceManager _submitHearingFeaturesMetricFor:].cold.2
+ -[HMDeviceManager internalAAServicesDaemon]
+ -[HMDeviceManager setInternalAAServicesDaemon:]
+ -[HMHealthKitUtilities _regionSupportStatusForFeatureID:]
+ -[HMHealthKitUtilities _registerForRegionStatusUpdatesWithFeatureIdentifier:]
+ -[HMHealthKitUtilities _registerForRegionStatusUpdatesWithFeatureIdentifier:].cold.1
+ -[HMHealthKitUtilities _updateHMRegionStatusFromFeatureStatus:featureIdentifier:]
+ -[HMServiceDaemon internalAAServicesDaemon]
+ -[HMServiceDaemon setInternalAAServicesDaemon:]
+ -[HMServiceXPCConnection clientSyncFetchHearingModeDeviceRecordForIdentifier:recordHandler:]
+ -[HMSettingsTelemetry .cxx_destruct]
+ -[HMSettingsTelemetry _convertToServerBucketValue:]
+ -[HMSettingsTelemetry _sendSettingsChanges:record:]
+ -[HMSettingsTelemetry _sendSettingsChanges:record:].cold.1
+ -[HMSettingsTelemetry _submitFeaturesChangeMetrics:forFeature:forDevice:]
+ -[HMSettingsTelemetry dispatchQueue]
+ -[HMSettingsTelemetry init]
+ -[HMSettingsTelemetry sendSettingsChanges:record:]
+ -[HMSettingsTelemetry setDispatchQueue:]
+ GCC_except_table100
+ GCC_except_table30
+ GCC_except_table39
+ GCC_except_table41
+ GCC_except_table47
+ GCC_except_table49
+ GCC_except_table51
+ GCC_except_table61
+ GCC_except_table74
+ GCC_except_table81
+ GCC_except_table90
+ _CUMetricsLog
+ _OBJC_CLASS_$_HMSettingsTelemetry
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OBJC_IVAR_$_HMDeviceManager._internalAAServicesDaemon
+ _OBJC_IVAR_$_HMServiceDaemon._internalAAServicesDaemon
+ _OBJC_IVAR_$_HMSettingsTelemetry._dispatchQueue
+ _OBJC_METACLASS_$_HMSettingsTelemetry
+ __OBJC_$_CLASS_METHODS_HMSettingsTelemetry
+ __OBJC_$_INSTANCE_METHODS_HMSettingsTelemetry
+ __OBJC_$_INSTANCE_VARIABLES_HMSettingsTelemetry
+ __OBJC_$_PROP_LIST_HMSettingsTelemetry
+ __OBJC_CLASS_RO_$_HMSettingsTelemetry
+ __OBJC_METACLASS_RO_$_HMSettingsTelemetry
+ ___37+[HMSettingsTelemetry sharedInstance]_block_invoke
+ ___50-[HMSettingsTelemetry sendSettingsChanges:record:]_block_invoke
+ ___52-[HMDeviceManager _activateAHPSConnectionForDevice:]_block_invoke.cold.1
+ ___71+[HMHealthKitUtilities frequencyToHearingDecibelLevelMapFromAudiogram:]_block_invoke.307
+ ___81-[HMDeviceManager _sendHearingAidConfigOverAHPSConnection:identifier:completion:]_block_invoke.cold.1
+ ___92-[HMServiceXPCConnection clientSyncFetchHearingModeDeviceRecordForIdentifier:recordHandler:]_block_invoke
+ ___92-[HMServiceXPCConnection clientSyncFetchHearingModeDeviceRecordForIdentifier:recordHandler:]_block_invoke_2
+ ___block_descriptor_56_e8_32bs40r48r_e5_v8?0lr40l8s32l8r48l8
+ ___block_descriptor_56_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_literal_global.354
+ ___block_literal_global.357
+ ___block_literal_global.381
+ ___block_literal_global.437
+ ___block_literal_global.464
+ ___block_literal_global.481
+ _gLogCategory_HMSettingsTelemetry
+ _objc_msgSend$_convertToServerBucketValue:
+ _objc_msgSend$_populateV1Struct:identifier:deviceRecord:hmSettingsStruct:
+ _objc_msgSend$_regionSupportStatusForFeatureID:
+ _objc_msgSend$_registerForRegionStatusUpdatesWithFeatureIdentifier:
+ _objc_msgSend$_sendSettingsChanges:record:
+ _objc_msgSend$_submitFeaturesChangeMetrics:forFeature:forDevice:
+ _objc_msgSend$_submitHearingFeaturesMetricFor:
+ _objc_msgSend$_updateHMRegionStatusFromFeatureStatus:featureIdentifier:
+ _objc_msgSend$diagnosticMeasurementsCount
+ _objc_msgSend$featureIdentifier
+ _objc_msgSend$hearingAssistCapability
+ _objc_msgSend$internalAAServicesDaemon
+ _objc_msgSend$numberWithChar:
+ _objc_msgSend$numberWithUnsignedInt:
+ _objc_msgSend$sendSettingsChanges:record:
+ _objc_msgSend$setInternalAAServicesDaemon:
+ _objc_msgSend$setInternalServicesDaemon:
+ _objc_release_x28
- -[HMDeviceManager _sendHearingAidConfigOverAHPSConnection:identifier:completion:].cold.10
- -[HMDeviceManager _sendHearingAidConfigOverAHPSConnection:identifier:completion:].cold.3
- -[HMDeviceManager _sendHearingAidConfigOverAHPSConnection:identifier:completion:].cold.4
- -[HMDeviceManager _sendHearingAidConfigOverAHPSConnection:identifier:completion:].cold.5
- -[HMDeviceManager _sendHearingAidConfigOverAHPSConnection:identifier:completion:].cold.6
- -[HMDeviceManager _sendHearingAidConfigOverAHPSConnection:identifier:completion:].cold.7
- -[HMDeviceManager _sendHearingAidConfigOverAHPSConnection:identifier:completion:].cold.8
- -[HMDeviceManager _sendHearingAidConfigOverAHPSConnection:identifier:completion:].cold.9
- -[HMHealthKitUtilities _getHMRegionStatusFromFeatureStatus:featureIdentifier:]
- -[HMHealthKitUtilities getRegionSupportStatusForFeatureID:].cold.1
- GCC_except_table28
- GCC_except_table34
- GCC_except_table42
- GCC_except_table44
- GCC_except_table46
- GCC_except_table59
- GCC_except_table72
- GCC_except_table79
- GCC_except_table88
- GCC_except_table98
- ___71+[HMHealthKitUtilities frequencyToHearingDecibelLevelMapFromAudiogram:]_block_invoke.304
- ___block_literal_global.297
- ___block_literal_global.300
- ___block_literal_global.324
- ___block_literal_global.378
- ___block_literal_global.405
- ___block_literal_global.421
- _objc_msgSend$_getHMRegionStatusFromFeatureStatus:featureIdentifier:
CStrings:
+ "### compute occlusion result failed, missing record"
+ "### compute occlusion result failed, occlusion detection unsupported"
+ "### fetch HMDeviceRecord %{error}"
+ "-[HMDeviceManager _activateAHPSConnectionForDevice:]_block_invoke"
+ "-[HMDeviceManager _populateV1Struct:identifier:deviceRecord:hmSettingsStruct:]"
+ "-[HMDeviceManager _sendHearingAidConfigOverAHPSConnection:identifier:completion:]_block_invoke"
+ "-[HMDeviceManager _submitHearingFeaturesMetricFor:]"
+ "-[HMHealthKitUtilities _registerForRegionStatusUpdatesWithFeatureIdentifier:]"
+ "-[HMHealthKitUtilities _updateHMRegionStatusFromFeatureStatus:featureIdentifier:]"
+ "-[HMHealthKitUtilities featureStatusProviding:didUpdateFeatureStatus:]_block_invoke"
+ "-[HMServiceXPCConnection clientSyncFetchHearingModeDeviceRecordForIdentifier:recordHandler:]"
+ "-[HMServiceXPCConnection clientSyncFetchHearingModeDeviceRecordForIdentifier:recordHandler:]_block_invoke"
+ "-[HMSettingsTelemetry _sendSettingsChanges:record:]"
+ "@\"AAServicesDaemon\""
+ "AmbientNoiseReduction"
+ "Amplification"
+ "Balance"
+ "ConversationBoost"
+ "FeatureName"
+ "FeatureNewValue"
+ "HMSettingsTelemetry"
+ "HearingAid config data not found, creating new config with version %d"
+ "HearingAidEnabled"
+ "HearingAidEnrolled"
+ "HearingAidRegionSupport"
+ "HearingAssistEnabled"
+ "HearingProtectionLSR"
+ "HearingProtectionRegionSupport"
+ "HearingTestRegionSupport"
+ "Invalid data"
+ "MediaAssist"
+ "MediaAssistEnabled"
+ "OffListeningMode"
+ "PID"
+ "PMEMedia"
+ "PMEVoice"
+ "Region support NOT changed for identifier %@: %s, whyNotVisible: %@, whyWeCantUse: %@"
+ "Region support changed for identifier %@: %@"
+ "Skip sending hearing features snapshot for %@"
+ "Submitted hearing features snapshot for %@"
+ "Successfully sent settings to buds: %@. Attempt to send updated HMDeviceRecord to clients"
+ "SwipeControl"
+ "T@\"AAServicesDaemon\",&,N,V_internalAAServicesDaemon"
+ "Tone"
+ "Update from buds %@: %lu bytes received"
+ "_convertToServerBucketValue:"
+ "_internalAAServicesDaemon"
+ "_populateV1Struct:identifier:deviceRecord:hmSettingsStruct:"
+ "_regionSupportStatusForFeatureID:"
+ "_registerForRegionStatusUpdatesWithFeatureIdentifier:"
+ "_sendSettingsChanges:record:"
+ "_submitFeaturesChangeMetrics:forFeature:forDevice:"
+ "_submitHearingFeaturesMetricFor:"
+ "_updateHMRegionStatusFromFeatureStatus:featureIdentifier:"
+ "clientSyncFetchHearingModeDeviceRecordForIdentifier:recordHandler:"
+ "com.apple.HeadphoneFeaturesChange"
+ "com.apple.HearingFeaturesStatus"
+ "diagnosticMeasurementsCount"
+ "featureIdentifier"
+ "fetch HMDeviceRecord, returning %@"
+ "hearingAssistCapability"
+ "i"
+ "i24@0:8@16"
+ "internalAAServicesDaemon"
+ "numberWithChar:"
+ "numberWithUnsignedInt:"
+ "sendSettingsChanges:record:"
+ "sending settings to buds: %@ - version: %d, leftGain: %lf, rightGain: %lf, tone: %lf, amplification: %lf, balance: %lf, beamFormer: %lf, noiseSuppression: %lf"
+ "setInternalAAServicesDaemon:"
+ "setInternalServicesDaemon:"
+ "v32@0:8@\"NSString\"16@?<v@?@\"HMDeviceRecord\">24"
+ "v36@0:8I16@20@28"
+ "v48@0:8@16@24@32^{?=CCS{?=ffffffffffff}{?=ffffffffffff}}40"
- "-[HMHealthKitUtilities _getHMRegionStatusFromFeatureStatus:featureIdentifier:]"
- "-[HMHealthKitUtilities getRegionSupportStatusForFeatureID:]"
- "C32@0:8@16@24"
- "HearingAid config data not found, creating new config"
- "_getHMRegionStatusFromFeatureStatus:featureIdentifier:"
- "sending settings: leftGain: %lf, rightGain: %lf, tone: %lf, amplification: %lf, balance: %lf, beamFormer: %lf, noiseSuppression: %lf"

```
