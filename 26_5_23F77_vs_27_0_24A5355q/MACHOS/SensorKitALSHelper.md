## SensorKitALSHelper

> `/usr/libexec/SensorKitALSHelper`

```diff

-972.0.21.0.0
-  __TEXT.__text: 0x13e20
+1025.0.0.0.0
+  __TEXT.__text: 0x15218
   __TEXT.__auth_stubs: 0x720
-  __TEXT.__objc_stubs: 0x2b40
-  __TEXT.__objc_methlist: 0xb14
-  __TEXT.__const: 0x198
-  __TEXT.__gcc_except_tab: 0x460
-  __TEXT.__cstring: 0x120e
-  __TEXT.__objc_classname: 0x155
-  __TEXT.__objc_methname: 0x29e8
-  __TEXT.__objc_methtype: 0x532
-  __TEXT.__oslogstring: 0x2757
-  __TEXT.__unwind_info: 0x430
-  __DATA_CONST.__auth_got: 0x3a0
-  __DATA_CONST.__got: 0x4f8
-  __DATA_CONST.__const: 0xa40
-  __DATA_CONST.__cfstring: 0x14c0
-  __DATA_CONST.__objc_classlist: 0x70
+  __TEXT.__objc_stubs: 0x3300
+  __TEXT.__objc_methlist: 0xd2c
+  __TEXT.__const: 0x1b0
+  __TEXT.__gcc_except_tab: 0x3ac
+  __TEXT.__cstring: 0x157f
+  __TEXT.__objc_classname: 0x17a
+  __TEXT.__objc_methname: 0x31e8
+  __TEXT.__objc_methtype: 0x5d0
+  __TEXT.__oslogstring: 0x2afa
+  __TEXT.__unwind_info: 0x498
+  __DATA_CONST.__const: 0xbb8
+  __DATA_CONST.__cfstring: 0x1620
+  __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x70
+  __DATA_CONST.__objc_superrefs: 0x80
   __DATA_CONST.__objc_intobj: 0x660
   __DATA_CONST.__objc_arraydata: 0x180
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_doubleobj: 0x80
   __DATA_CONST.__objc_arrayobj: 0x48
-  __DATA.__objc_const: 0x1e70
-  __DATA.__objc_selrefs: 0xbf0
-  __DATA.__objc_ivar: 0x190
-  __DATA.__objc_data: 0x460
+  __DATA_CONST.__auth_got: 0x3a0
+  __DATA_CONST.__got: 0x528
+  __DATA.__objc_const: 0x2318
+  __DATA.__objc_selrefs: 0xde0
+  __DATA.__objc_ivar: 0x1c8
+  __DATA.__objc_data: 0x500
   __DATA.__data: 0x1e0
-  __DATA.__bss: 0xf8
+  __DATA.__bss: 0x100
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation
   - /System/Library/Frameworks/CoreMotion.framework/CoreMotion

   - /System/Library/Frameworks/SensorKit.framework/SensorKit
   - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
   - /System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities
+  - /System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices
   - /System/Library/PrivateFrameworks/AudioDataAnalysis.framework/AudioDataAnalysis
   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/BiomePubSub.framework/BiomePubSub

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreDuet.framework/CoreDuet
   - /System/Library/PrivateFrameworks/CoreRoutine.framework/CoreRoutine
+  - /System/Library/PrivateFrameworks/HearingModeService.framework/HearingModeService
   - /System/Library/PrivateFrameworks/HearingUtilities.framework/HearingUtilities
-  - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
   - /System/Library/PrivateFrameworks/PersonalAudio.framework/PersonalAudio
   - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 392DFAE9-2EB7-31C6-891D-CEA8B5CBD54B
-  Functions: 280
-  Symbols:   287
-  CStrings:  1124
+  UUID: B8F806DC-45D6-3748-AB57-D47316426E5D
+  Functions: 338
+  Symbols:   293
+  CStrings:  1270
 
Symbols:
+ _OBJC_CLASS_$_AADeviceManager
+ _OBJC_CLASS_$_BTCloudServicesClient
+ _OBJC_CLASS_$_HMServiceClient
+ _OBJC_CLASS_$_SRHeadphoneSettings
+ _OBJC_CLASS_$_SRSourceDevice
+ _SRSensorHeadphoneSettings
CStrings:
+ "%@ (%p): (\n  adaptiveAudioStrength: %d,\n  listeningMode: %ld,\n  personalizedVolumeEnabled: %ld,\n  hearingAidEnabled: %ld,\n  coversationAwarenessEnabled: %ld,\n  spatialAudioEnabled: %ld,\n  mediaAssistEnabled: %ld,\n  adjustMediaEnabled: %ld,\n  adjustVoiceEnabled: %ld,\n  hearingProtectionEnabled: %ld,\n  hearingAidAmplification: %f,\n  hearingAidBalance: %f,\n  hearingAidTone: %f,\n  conversationAwarenessEnabled: %ld,\n  conversationBoostEnabled: %ld,\n  ambientNoiseReduction: %f,\n  personalizedSpatialAudioEnabled: %ld,\n)"
+ "%{public}@"
+ "?"
+ "@\"AADeviceManager\""
+ "@\"AudioAccessoryDevice\""
+ "@\"BTCloudServicesClient\""
+ "@\"HMDeviceRecord\""
+ "@\"HMServiceClient\""
+ "@64@0:8@16@24@32@40@48@56"
+ "AADeviceManager interrupted"
+ "AADeviceManager invalidated"
+ "Apple"
+ "BTCloudServicesClient interrupted"
+ "BTCloudServicesClient invalidated"
+ "Failed to activate AADeviceManager because %{public}@"
+ "Failed to activate HMServiceClient because %{public}@"
+ "Failed to create SRHeadphoneSettings from %{private}@"
+ "Failed to set source because %{public}@"
+ "Failed to write settings because %{public}@, settings: %{private}@"
+ "Found AADevice with identifier %{private}@: %{private}@"
+ "Found HMDevice with identifier %{private}@: %{private}@"
+ "Found cloud sound profile: %{private}@"
+ "HMServiceClient interrupted"
+ "HMServiceClient invalidated"
+ "HeadphoneSettingsCollector"
+ "I16@0:8"
+ "Invalid"
+ "LG"
+ "MS"
+ "SRDeviceRecord"
+ "SmartTech"
+ "Sony"
+ "Stopped monitoring for %{public}@"
+ "T@\"AudioAccessoryDevice\",&,N,V_aaDevice"
+ "T@\"HMDeviceRecord\",&,N,V_hmDevice"
+ "T@\"NSString\",&,N,V_identifier"
+ "T@\"PASettings\",&,N,V_paSettings"
+ "TI,R,N"
+ "Td,R,N"
+ "Tq,R,N"
+ "Tq,R,N,V_personalizedSpatialAudioEnabled"
+ "Unsupported AAAutoANCStrength (%{public}d}"
+ "Unsupported AAListeningMode (%{public}d}"
+ "Unsupported AAMultiState (%{public}d} for %{public}@"
+ "Will start monitoring for %{public}@"
+ "Writing SRDeviceRecord: %{private}@"
+ "_aaDevice"
+ "_cloudServicesClient"
+ "_currentSourceIdentifier"
+ "_deviceManager"
+ "_deviceRecords"
+ "_dirty"
+ "_headphoneClient"
+ "_hmDevice"
+ "_identifier"
+ "_personalizedSpatialAudioEnabled"
+ "_writer"
+ "aaDevice"
+ "activateWithCompletion:"
+ "adaptiveAudioStrength"
+ "adaptiveVolumeConfig"
+ "adjustMediaEnabled"
+ "adjustVoiceEnabled"
+ "ambientNoiseReduction"
+ "amplification"
+ "autoANCStrength"
+ "balance"
+ "bluetoothAddress"
+ "bluetoothUUID"
+ "com.apple.bluetooth.discovery"
+ "consume"
+ "conversationAwarenessEnabled"
+ "conversationBoostEnabled"
+ "conversationDetectConfig"
+ "coversationAwarenessEnabled"
+ "deviceRecordWithIdentifier:"
+ "doubleValue"
+ "fetchCloudRecordForRecord:completion:"
+ "fetchSoundProfileRecordWithCompletion:"
+ "firmwareVersion"
+ "foundAADevice:"
+ "foundHMDevice:"
+ "hearingAidAmplification"
+ "hearingAidBalance"
+ "hearingAidEnabled"
+ "hearingAidTone"
+ "hearingProtectionEnabled"
+ "hmDevice"
+ "initWithIdentifier:manufacturer:model:hardwareVersion:firmwareVersion:"
+ "initWithListeningMode:adaptiveAudioStrength:personalizedVolumeEnabled:hearingAidEnabled:conversationAwarenessEnabled:spatialAudioEnabled:mediaAssistEnabled:adjustMediaEnabled:adjustVoiceEnabled:hearingProtectionEnabled:conversationBoostEnabled:hearingAidAmplification:hearingAidBalance:hearingAidTone:ambientNoiseReduction:personalizedSpatialAudioEnabled:"
+ "initWithQueue:deviceManager:hmServiceClient:cloudServicesClient:paSettings:writer:"
+ "listeningMode"
+ "mediaAssistEnabled"
+ "paSettings"
+ "personalizedSpatialAudioEnabled"
+ "personalizedVolumeEnabled"
+ "pmeMediaEnabled"
+ "pmeVoiceEnabled"
+ "productName"
+ "q16@0:8"
+ "ready to write: %d hmdevice: %p, aadevice: %p, personalized: %ld, dirty: %d"
+ "readyToWrite"
+ "setAaDevice:"
+ "setDeviceFoundHandler:"
+ "setDeviceRecordChangedHandler:"
+ "setDispatchQueue:"
+ "setHmDevice:"
+ "setIdentifier:"
+ "setPaSettings:"
+ "setPersonalizedSpatialAudioEnabled:"
+ "setSourceDevice:error:"
+ "soundProfileFileURL"
+ "spatialAudioAllowed"
+ "spatialAudioEnabled"
+ "startMonitoring"
+ "stopMonitoring"
+ "stringWithUTF8String:"
+ "tone"
+ "transparencyBeamformingForAddress:"
+ "transparencyNoiseSupressorForAddress:"
+ "v16@?0@\"AudioAccessoryDevice\"8"
+ "v16@?0@\"HMDeviceRecord\"8"
+ "v24@0:8q16"
+ "v24@?0@\"BTCloudSoundProfileRecord\"8@\"NSError\"16"
+ "vendorID"
+ "writeDeviceRecordIfComplete:"

```
