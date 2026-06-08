## PersonalAudio

> `/System/Library/PrivateFrameworks/PersonalAudio.framework/PersonalAudio`

```diff

-496.22.0.0.0
-  __TEXT.__text: 0x153f8
-  __TEXT.__auth_stubs: 0x4f0
-  __TEXT.__objc_methlist: 0xeb0
+527.0.0.0.0
+  __TEXT.__text: 0x13f88
+  __TEXT.__objc_methlist: 0xec8
   __TEXT.__const: 0x110
-  __TEXT.__gcc_except_tab: 0x39c
-  __TEXT.__cstring: 0x1247
-  __TEXT.__oslogstring: 0xd79
   __TEXT.__dlopen_cstrs: 0x163
-  __TEXT.__unwind_info: 0x5f0
-  __TEXT.__objc_classname: 0xdb
-  __TEXT.__objc_methname: 0x32f6
-  __TEXT.__objc_methtype: 0x419
-  __TEXT.__objc_stubs: 0x2ec0
-  __DATA_CONST.__got: 0x190
-  __DATA_CONST.__const: 0x720
+  __TEXT.__gcc_except_tab: 0x39c
+  __TEXT.__cstring: 0x1253
+  __TEXT.__oslogstring: 0xdb8
+  __TEXT.__unwind_info: 0x560
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x6d0
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xea8
+  __DATA_CONST.__objc_selrefs: 0xed8
   __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_arraydata: 0x40
-  __AUTH_CONST.__auth_got: 0x288
+  __DATA_CONST.__got: 0x198
   __AUTH_CONST.__const: 0x300
   __AUTH_CONST.__cfstring: 0x1500
-  __AUTH_CONST.__objc_const: 0x1038
+  __AUTH_CONST.__objc_const: 0x1068
   __AUTH_CONST.__objc_doubleobj: 0x80
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_arrayobj: 0x18
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__data: 0x18
-  __DATA.__objc_ivar: 0xa8
+  __DATA.__objc_ivar: 0xac
   __DATA.__data: 0xc0
-  __DATA.__bss: 0x98
+  __DATA.__bss: 0xe0
   __DATA_DIRTY.__objc_data: 0x320
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0xd0
+  __DATA_DIRTY.__bss: 0x88
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6565B3B6-CE9B-3F9A-9D1D-BCA2915B8355
-  Functions: 441
-  Symbols:   1646
-  CStrings:  1081
+  UUID: F8BA366C-B704-379D-BDD2-5D710762EEF0
+  Functions: 406
+  Symbols:   1580
+  CStrings:  448
 
Symbols:
+ -[PAAccessoryManager foundDeviceAddresses]
+ -[PAAccessoryManager setFoundDeviceAddresses:]
+ GCC_except_table106
+ GCC_except_table162
+ GCC_except_table163
+ GCC_except_table18
+ GCC_except_table218
+ GCC_except_table229
+ GCC_except_table240
+ GCC_except_table300
+ GCC_except_table315
+ GCC_except_table337
+ GCC_except_table378
+ GCC_except_table388
+ GCC_except_table391
+ GCC_except_table394
+ GCC_except_table46
+ GCC_except_table60
+ GCC_except_table69
+ _HMDeviceConfigurationsFunction.492
+ _HearingModeServiceLibrary.sLib.496
+ _HearingModeServiceLibrary.sOnce.488
+ _HearingUtilitiesLibraryCore.frameworkLibrary.393
+ _HearingUtilitiesLibraryCore.frameworkLibrary.472
+ _OBJC_CLASS_$_NSMutableSet
+ _OBJC_IVAR_$_PAAccessoryManager._foundDeviceAddresses
+ ___26-[PAAccessoryManager init]_block_invoke.12
+ ___26-[PAAccessoryManager init]_block_invoke.15
+ ___26-[PAAccessoryManager init]_block_invoke.19
+ ___26-[PAAccessoryManager init]_block_invoke.22
+ ___26-[PAAccessoryManager init]_block_invoke.6
+ ___26-[PAAccessoryManager init]_block_invoke.9
+ ___53-[PAAccessoryManager sendPMEConfigurationToAccessory]_block_invoke.40
+ ___53-[PAAccessoryManager sendPMEConfigurationToAccessory]_block_invoke.45
+ ___73+[PAAudiogramUtilities normalizedOffsetsFromLeftOffsets:andRightOffsets:]_block_invoke.118
+ ___HearingModeServiceLibrary_block_invoke.494
+ ___HearingUtilitiesLibraryCore_block_invoke.394
+ ___HearingUtilitiesLibraryCore_block_invoke.473
+ ___block_descriptor_48_e8_32s40w_e29_v24?0"NSArray"8"NSArray"16lw40l8s32l8
+ ___block_literal_global.122
+ ___block_literal_global.133
+ ___block_literal_global.149
+ ___block_literal_global.174
+ ___block_literal_global.24
+ ___block_literal_global.262
+ ___block_literal_global.30
+ ___block_literal_global.31
+ ___block_literal_global.411
+ ___block_literal_global.42
+ ___block_literal_global.48
+ ___block_literal_global.513
+ ___block_literal_global.570
+ ___block_literal_global.77
+ ___getHUAccessoryManagerClass_block_invoke.392
+ ___getHUAccessoryManagerClass_block_invoke.471
+ _audit_stringHearingUtilities.398
+ _audit_stringHearingUtilities.478
+ _classHMDeviceConfigurations.490
+ _getHMDeviceConfigurationsClass.485
+ _getHUAccessoryManagerClass.464
+ _getHUAccessoryManagerClass.softClass.391
+ _getHUAccessoryManagerClass.softClass.470
+ _initHMDeviceConfigurations.487
+ _objc_claimAutoreleasedReturnValue
+ _objc_enumerationMutation
+ _objc_msgSend$addObjectsFromArray:
+ _objc_msgSend$connect:to:format:error:
+ _objc_msgSend$countByEnumeratingWithState:objects:count:
+ _objc_msgSend$foundDeviceAddresses
+ _objc_msgSend$installTapOnBus:bufferSize:format:error:block:
+ _objc_msgSend$playAndReturnError:
+ _objc_msgSend$removeObject:
+ _objc_msgSend$set
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x4
+ _objc_retain_x8
+ _objc_retain_x9
+ _sharedInstance.onceToken.132
+ _sharedInstance.onceToken.410
+ _sharedInstance.onceToken.512
- +[PAAccessoryManager sharedInstance].cold.1
- +[PADatabaseManager sharedManager].cold.1
- +[PAEnrollment sharedInstance].cold.1
- +[PAHMSManager sharedInstance].cold.1
- +[PASettings sharedInstance].cold.1
- +[PAStimulus louderSinStimulus].cold.1
- +[PAStimulus musicStimulus].cold.1
- +[PAStimulus sinStimulus].cold.1
- -[PAConfiguration initWithCoder:].cold.1
- -[PAConfiguration initWithCoder:].cold.2
- -[PAConfiguration initWithCoder:].cold.3
- -[PAConfiguration readSettingsFromPreset:].cold.1
- -[PAConfiguration readSettingsFromPreset:].cold.2
- -[PAConfiguration settingsFromConfiguration:].cold.1
- -[PASettings archivedDataFromConfiguration:].cold.1
- -[PASettings configurationFromData:].cold.1
- -[PASettings keysToSync].cold.1
- -[PASettings preferenceKeyForSelector:].cold.1
- -[PAStimulus play].cold.1
- GCC_except_table11
- GCC_except_table12
- GCC_except_table15
- GCC_except_table16
- GCC_except_table2
- GCC_except_table21
- GCC_except_table3
- GCC_except_table4
- GCC_except_table5
- GCC_except_table50
- GCC_except_table51
- GCC_except_table7
- GCC_except_table9
- _HealthKitLibrary
- _HearingUtilitiesLibrary
- _OUTLINED_FUNCTION_0
- _OUTLINED_FUNCTION_1
- _OUTLINED_FUNCTION_2
- _OUTLINED_FUNCTION_3
- _OUTLINED_FUNCTION_4
- _PARegionSupportsHearingAid.cold.1
- ___26-[PAAccessoryManager init]_block_invoke.11
- ___26-[PAAccessoryManager init]_block_invoke.14
- ___26-[PAAccessoryManager init]_block_invoke.18
- ___26-[PAAccessoryManager init]_block_invoke.26
- ___26-[PAAccessoryManager init]_block_invoke.5
- ___26-[PAAccessoryManager init]_block_invoke.8
- ___53-[PAAccessoryManager sendPMEConfigurationToAccessory]_block_invoke.39
- ___53-[PAAccessoryManager sendPMEConfigurationToAccessory]_block_invoke.42
- ___53-[PAAccessoryManager sendPMEConfigurationToAccessory]_block_invoke_2.cold.1
- ___73+[PAAudiogramUtilities normalizedOffsetsFromLeftOffsets:andRightOffsets:]_block_invoke.52
- ___block_descriptor_48_e8_32s40w_e29_v24?0"NSArray"8"NSArray"16ls32l8w40l8
- ___block_descriptor_56_e8_32s40s48r_e5_v8?0lr48l8s32l8s40l8
- ___block_descriptor_56_e8_32s40s48r_e5_v8?0ls32l8s40l8r48l8
- ___block_literal_global.22
- ___block_literal_global.41
- ___block_literal_global.47
- ___block_literal_global.56
- ___block_literal_global.78
- ___block_literal_global.83
- ___getAXHeardControllerClass_block_invoke.cold.1
- ___getHKUnitClass_block_invoke.cold.1
- ___getHUAccessoryManagerClass_block_invoke.cold.1
- _initHMDeviceConfigurations.cold.1
- _initHMHealthKitUtilities.cold.1
- _initHMServiceClient.cold.1
- _objc_autorelease
- _objc_msgSend$connect:to:format:
- _objc_msgSend$installTapOnBus:bufferSize:format:block:
- _objc_msgSend$play
- _objc_msgSend$sharedAVSystemController
- _objc_retain_x25
- _objc_retain_x26
- _objc_retain_x27
CStrings:
+ "New devivce found, reading transparency settings from buds: %@"
- ".cxx_destruct"
- "@\"AVAudioEngine\""
- "@\"AVAudioFile\""
- "@\"AVAudioPCMBuffer\""
- "@\"AVAudioPlayerNode\""
- "@\"AXDispatchTimer\""
- "@\"HMServiceClient\""
- "@\"NSArray\""
- "@\"NSDictionary\""
- "@\"NSMutableDictionary\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\""
- "@\"NSURL\""
- "@\"PAConfiguration\""
- "@16@0:8"
- "@20@0:8B16"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8Q16"
- "@24@0:8^{?=ffffffffffffffffffffffffffffffffffffffff}16"
- "@24@0:8f16i20"
- "@28@0:8@16B24"
- "@32@0:8@16@24"
- "@32@0:8Q16Q24"
- "@40@0:8Q16Q24@32"
- "@48@0:8@16@24@32@40"
- "@48@0:8Q16Q24Q32Q40"
- "@?"
- "B"
- "B16@0:8"
- "B24@0:8@16"
- "B32@0:8@16@24"
- "CoreDataProperties"
- "NSCoding"
- "NSSecureCoding"
- "PAAccessoryManager"
- "PAAudiogramUtilities"
- "PAConfiguration"
- "PADatabaseManager"
- "PAEnrollment"
- "PAEnrollmentNode"
- "PAHMSManager"
- "PASettings"
- "PAStimulus"
- "Q"
- "Q16@0:8"
- "Q24@0:8@16"
- "T@\"AVAudioEngine\",&,N,V_engine"
- "T@\"AVAudioFile\",&,N,V_audioFile"
- "T@\"AVAudioPCMBuffer\",&,N,V_audioPCMBuffer"
- "T@\"AVAudioPlayerNode\",&,N,V_audioPlayerNode"
- "T@\"AXDispatchTimer\",&,N,V_pmeHysteresisTimer"
- "T@\"AXDispatchTimer\",&,N,V_timer"
- "T@\"HMServiceClient\",&,N,V_hmsClient"
- "T@\"NSArray\",&,N,V_options"
- "T@\"NSArray\",&,N,V_stimuli"
- "T@\"NSData\",&,D,N"
- "T@\"NSDictionary\",&,D,N"
- "T@\"NSDictionary\",&,N,V_audiogramSettings"
- "T@\"NSDictionary\",&,N,V_preset"
- "T@\"NSDictionary\",&,N,V_presetAdjustments"
- "T@\"NSMutableDictionary\",&,N,V_enrollmentHandlers"
- "T@\"NSMutableDictionary\",&,N,V_hearingAidEnabledByAddress"
- "T@\"NSMutableDictionary\",&,N,V_yodelDeviceRecordByAddress"
- "T@\"NSNumber\",&,D,N"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_hmsQueue"
- "T@\"NSString\",&,N,V_heading"
- "T@\"NSString\",&,N,V_instructions"
- "T@\"NSString\",&,N,V_name"
- "T@\"NSString\",&,N,V_tuningDescription"
- "T@\"NSURL\",&,N,V_filePath"
- "T@\"PAConfiguration\",&,N"
- "T@\"PAConfiguration\",&,N,V_audiogramPreset"
- "T@\"PAConfiguration\",&,N,V_configuration"
- "TB,D,N"
- "TB,N"
- "TB,N,GisSelected,V_selected"
- "TB,N,V_audiogramValidForPSE"
- "TB,N,V_hideVisualizer"
- "TB,N,V_isEnrollingPSE"
- "TB,N,V_shouldSendUpdate"
- "TB,R"
- "TQ,D,N"
- "TQ,N"
- "TQ,N,V_currentDevicePSEVersion"
- "TQ,N,V_index"
- "TQ,N,V_level"
- "TQ,N,V_progress"
- "TQ,N,V_section"
- "TQ,N,V_selectedLevel"
- "TQ,N,V_shape"
- "TQ,N,V_totalSteps"
- "TQ,N,V_type"
- "Td,N,V_levelMultiplier"
- "Td,N,V_rampStep"
- "UUIDWithString:"
- "^{?=ffffffffffffffffffffffffffffffffffffffff}20@0:8B16"
- "^{?=ffffffffffffffffffffffffffffffffffffffff}24@0:8@16"
- "^{?=f{?=ffffffffffff}{?=ffffffffffff}f}24@0:8@16"
- "^{?=f{?=ffffffffffff}{?=ffffffffffff}}24@0:8@16"
- "_audioFile"
- "_audioPCMBuffer"
- "_audioPlayerNode"
- "_audiogramPreset"
- "_audiogramSettings"
- "_audiogramValidForPSE"
- "_bucketCount"
- "_configuration"
- "_currentConfigurations"
- "_currentDevicePSEVersion"
- "_engine"
- "_enrollmentHandlers"
- "_filePath"
- "_heading"
- "_hearingAidEnabledByAddress"
- "_hideVisualizer"
- "_hmsClient"
- "_hmsQueue"
- "_index"
- "_instructions"
- "_isEnrollingPSE"
- "_level"
- "_levelMultiplier"
- "_name"
- "_options"
- "_pmeHysteresisTimer"
- "_preset"
- "_presetAdjustments"
- "_progress"
- "_rampStep"
- "_ramping"
- "_section"
- "_selected"
- "_selectedLevel"
- "_shape"
- "_shouldSendUpdate"
- "_stimuli"
- "_stimulusMagnitudesCallback"
- "_timer"
- "_totalSteps"
- "_tuningDescription"
- "_type"
- "_yodelDeviceRecordByAddress"
- "accommodationTypesForRouteUID:"
- "activateWithCompletion:"
- "addEnrollmentStepForSection:comparing:withOption:andBlock:"
- "addEntriesFromDictionary:"
- "addHandlers"
- "addLevelEnrollmentStepsStartingWith:"
- "addObserver:selector:name:object:"
- "addOffEnrollmentStepComparing:"
- "additionalInfoForPrefenceUpdate"
- "afterDelay:processBlock:"
- "allKeys"
- "amplification"
- "amplificationForAddress:"
- "appendBytes:length:"
- "appendData:"
- "archivedDataFromConfiguration:"
- "array"
- "arrayWithObjects:count:"
- "attachNode:"
- "audioFile"
- "audioPCMBuffer"
- "audioPlayerNode"
- "audioSessionWasInterrupted:"
- "audioSettings"
- "audiogramConfiguration"
- "audiogramConfigurationForRouteUID:"
- "audiogramPreset"
- "audiogramSettings"
- "audiogramValidForPSE"
- "balance"
- "balanceForAddress:"
- "beamFormer"
- "beamformingForAddress:"
- "bluetoothAddress"
- "bluetoothManagerQueue"
- "boolValue"
- "boolValueForPreferenceKey:withDefaultValue:"
- "bundleForClass:"
- "calculateFFTForBuffer:"
- "cancel"
- "cloudKitContainer"
- "code"
- "compare:"
- "componentsSeparatedByString:"
- "configuration"
- "configurationFromAudiogramSample:"
- "configurationFromData:"
- "configurationFromType:"
- "configurationWithAudiogram:"
- "configurationWithLeftMediaLoss:rightMediaLoss:leftSpeechLoss:andRightSpeechLoss:"
- "configurationWithLevel:andShape:"
- "configurationWithMediaOffsets:andSpeechOffsets:"
- "configurationWithPreset:andAdjustments:"
- "configurationWithRawAdjustment:"
- "connect:to:format:"
- "containerIdentifier"
- "containsObject:"
- "containsValueForKey:"
- "contentDidUpdate:"
- "contentDidUpdateRemotely:"
- "copy"
- "count"
- "currentDevicePSEVersion"
- "currentPMEConfiguration"
- "currentPSEConfiguration"
- "customTransparencyConfiguration"
- "customTransparencyConfigurationForRouteUID:"
- "d"
- "d16@0:8"
- "d24@0:8@16"
- "dataFromPreset:"
- "dataWithBytes:length:"
- "dataWithLength:"
- "decibelHearingLevelUnit"
- "decodeBoolForKey:"
- "decodeIntegerForKey:"
- "decodeObjectOfClasses:forKey:"
- "decodeTopLevelObjectOfClasses:forKey:error:"
- "defaultCenter"
- "description"
- "dictionary"
- "dictionaryWithContentsOfFile:"
- "dictionaryWithDictionary:"
- "dictionaryWithObject:forKey:"
- "dictionaryWithObjects:forKeys:count:"
- "doubleValue"
- "doubleValueForUnit:"
- "encodeBool:forKey:"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "encodedData"
- "engine"
- "enrollmentHandlers"
- "enrollmentNodeAfter:withSelectedNode:"
- "enrollmentWithAudiogram:"
- "entryFromData:atIndex:"
- "enumerateKeysAndObjectsUsingBlock:"
- "enumerateObjectsUsingBlock:"
- "executeFetchRequest:error:"
- "f16@0:8"
- "f20@0:8B16"
- "fetchRequestWithEntityName:"
- "filePath"
- "fileURLWithPath:"
- "finishEncoding"
- "firstObject"
- "floatValue"
- "frequency"
- "frequencyDictionaryFromOffsets:"
- "getAudioOwnershipForAddress:withCompletion:"
- "getAvailableAddressesSupportingCharacteristic:withCompletion:"
- "getBytes:length:"
- "getBytes:range:"
- "getCurrentRouteSupportingHeadphoneAccommodationsWithCompletion:"
- "getIdentifiersFromAddresses:withCompletion:"
- "getPMEEverywhereSupportStateForAddress:withCompletion:"
- "getPSEVersionForAddress:withCompletion:"
- "getRegionSupportStatusForFeatureID:"
- "hcSafeAddObject:"
- "heading"
- "headphoneStateChangedNotification:"
- "hearingAidEnabled"
- "hearingAidEnabledByAddress"
- "hearingAidEnabledForAddress:"
- "hearingAidV2Capability"
- "hearingAidV2RegionStatus"
- "hearingAssistEnabled"
- "hearingAssistRegionStatus"
- "hearingProtectionPPEEnabled"
- "hearingProtectionPPERegionStatus"
- "hearingProtectionRegionStatus"
- "hertzUnit"
- "hideVisualizer"
- "hmsClient"
- "hmsQueue"
- "index"
- "indexOfObject:"
- "init"
- "initForReading:error:"
- "initForReadingFromData:error:"
- "initRequiringSecureCoding:"
- "initWithCoder:"
- "initWithFile:"
- "initWithObjects:"
- "initWithObjectsAndKeys:"
- "initWithPCMFormat:frameCapacity:"
- "initWithTargetSerialQueue:"
- "insertNewObjectForEntityForName:inManagedObjectContext:"
- "installTapOnBus:bufferSize:format:block:"
- "instructions"
- "intValue"
- "integerValueForKey:withDefaultValue:"
- "isEnrollingPSE"
- "isEqual:"
- "isEqualToDictionary:"
- "isEqualToNumber:"
- "isEqualToString:"
- "isInternalInstall"
- "isPending"
- "isPlaying"
- "isSelected"
- "isTransparencyUpdatePending"
- "key"
- "keysToSync"
- "lastObject"
- "leftConfiguration"
- "leftEarSensitivity"
- "length"
- "levelMultiplier"
- "localizedFormat"
- "localizedStringForKey:value:table:"
- "logMessage:"
- "lossArrayFromDictionary:forLeft:"
- "louderSinStimulus"
- "magnitudesWithLevelMultiplier:count:"
- "mainMixerNode"
- "managedObjectContext"
- "managedObjectModelName"
- "mediaLossArrayLeft"
- "mediaLossArrayRight"
- "mediaPureToneAverage"
- "mediaServerDied"
- "modifyDeviceConfig:identifier:completion:"
- "musicStimulus"
- "mutableCopy"
- "name"
- "nodeWithSection:andType:comparing:with:"
- "nodeWithSection:type:andConfiguration:"
- "noiseSuppression"
- "noiseSupressorForAddress:"
- "normalizedOffsetsFromAudiogram:"
- "normalizedOffsetsFromLeftOffsets:andRightOffsets:"
- "numberWithBool:"
- "numberWithChar:"
- "numberWithDouble:"
- "numberWithFloat:"
- "numberWithUnsignedChar:"
- "numberWithUnsignedInteger:"
- "objectAtIndex:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectValueForKey:withClass:andDefaultValue:"
- "objectsForKeys:notFoundMarker:"
- "offsetsSortedByFrequency:"
- "onBudsMediaSettingsForRoute:"
- "options"
- "outputFormatForBus:"
- "ownVoiceForAddress:"
- "ownVoiceLevelGain"
- "ownVoiceSupportedForAddress:"
- "paramDataWithValue:andOffset:"
- "pathForResource:ofType:"
- "performBlockAndWait:"
- "performSelector:withObject:afterDelay:"
- "personalAudioAccommodationTypes"
- "personalMediaAutomationMockAudiogramAvailable"
- "personalMediaAutomationMockNonYodelRegion"
- "personalMediaAutomationMockTransparencyAvailable"
- "personalMediaAutomationMockTransparencyCustomized"
- "personalMediaAutomationSkipHeadphoneRequirement"
- "personalMediaConfiguration"
- "personalMediaConfigurationForRouteUID:"
- "personalMediaDebugMode"
- "personalMediaEnabled"
- "personalMediaEnabledForRouteUID:"
- "play"
- "pmeHysteresisTimer"
- "postNotificationName:object:"
- "ppeEnrolledForAddress:"
- "ppeRegionSupportedForAddress:"
- "preferenceDomainForPreferenceKey:"
- "preferenceKeyForSelector:"
- "preset"
- "presetAdjustments"
- "presetDictionaryForSpeech:"
- "presetFrequencies"
- "processingFormat"
- "progress"
- "progressDescription"
- "ptaFrequencies"
- "pureToneAverageForSpeech:"
- "rampStep"
- "rampVolumeUp:"
- "readIntoBuffer:error:"
- "readSettingsFromPreset:"
- "readValueForCharacteristicUUID:"
- "regionSupportedForHearingProtection:"
- "regionSupportsHearingAssistForAddress:"
- "registerDiscoveryBlock:withListener:"
- "registerListener:forBucketCount:"
- "registerLoggingBlock:withListener:"
- "registerNotifications"
- "registerUpdateBlock:forCharacteristicUUIDs:withListener:"
- "registerUpdateBlock:forRetrieveSelector:withListener:"
- "removeObjectForKey:"
- "removeObjectsForKeys:"
- "removeObjectsInRange:"
- "removeObserver:"
- "removeTapOnBus:"
- "replaceBytesInRange:withBytes:"
- "resetValueForSelector:forAddress:"
- "rightConfiguration"
- "rightEarSensitivity"
- "routesDidChange:"
- "sanitizedRouteUID:"
- "saveIfPossible"
- "savePMEConfiguration:pseConfiguration:"
- "scheduleBuffer:atTime:options:completionHandler:"
- "section"
- "selected"
- "selectedLevel"
- "sendConfigUpdate:forAddress:"
- "sendConfigUpdate:forIdentifier:withCompletion:"
- "sendPMEConfigurationToAccessory"
- "sendUpdateToAccessory"
- "sensitivityPoints"
- "setAccommodationType:forAddress:"
- "setAccommodationTypes:forRouteUID:"
- "setAccommodationTypesByRouteUID:"
- "setActive:error:"
- "setAmplification:"
- "setAmplification:forAddress:"
- "setAttribute:forKey:error:"
- "setAudioFile:"
- "setAudioPCMBuffer:"
- "setAudioPlayerNode:"
- "setAudioSettings:"
- "setAudiogramConfiguration:"
- "setAudiogramConfiguration:forRouteUID:"
- "setAudiogramConfigurationByRouteUID:"
- "setAudiogramPreset:"
- "setAudiogramSettings:"
- "setAudiogramValidForPSE:"
- "setBalance:"
- "setBalance:forAddress:"
- "setBeamFormer:"
- "setBeamforming:forAddress:"
- "setCategory:error:"
- "setConfiguration:"
- "setConfigurationCameFromEnrollment:"
- "setConfigurationCameFromUser:"
- "setCurrentDevicePSEVersion:"
- "setCurrentEnrollmentProgress:"
- "setCustomTransparencyConfiguration:"
- "setCustomTransparencyConfiguration:forRouteUID:"
- "setCustomTransparencyConfigurationByRouteUID:"
- "setDeviceRecordChangedHandler:"
- "setDispatchQueue:"
- "setEnableHearingAid:"
- "setEnablePMEMedia:"
- "setEnablePMEVoice:"
- "setEngine:"
- "setEnrollPMEVoice:"
- "setEnrollmentHandlers:"
- "setFilePath:"
- "setHeading:"
- "setHearingAidEnabledByAddress:"
- "setHideVisualizer:"
- "setHmsClient:"
- "setHmsQueue:"
- "setIndex:"
- "setInstructions:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setIsEnrollingPSE:"
- "setLevel:"
- "setLevelMultiplier:"
- "setMediaLossArrayLeft:"
- "setMediaLossArrayRight:"
- "setName:"
- "setNoiseSuppression:"
- "setNoiseSupressor:forAddress:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setOptions:"
- "setOwnVoice:forAddress:"
- "setOwnVoiceLevelGain:"
- "setPersonalAudioAccommodationTypes:"
- "setPersonalMediaAutomationMockAudiogramAvailable:"
- "setPersonalMediaAutomationMockNonYodelRegion:"
- "setPersonalMediaAutomationMockTransparencyAvailable:"
- "setPersonalMediaAutomationMockTransparencyCustomized:"
- "setPersonalMediaAutomationSkipHeadphoneRequirement:"
- "setPersonalMediaConfiguration:"
- "setPersonalMediaConfiguration:forRouteUID:"
- "setPersonalMediaConfigurationByRouteUID:"
- "setPersonalMediaDebugMode:"
- "setPersonalMediaEnabled:"
- "setPersonalMediaEnabled:forRouteUID:"
- "setPersonalMediaEnabledByRouteUID:"
- "setPersonalSoundVisible:"
- "setPmeHysteresisTimer:"
- "setPreset:"
- "setPresetAdjustments:"
- "setProgress:"
- "setRampStep:"
- "setReturnsObjectsAsFaults:"
- "setSection:"
- "setSelected:"
- "setSelectedLevel:"
- "setShape:"
- "setShouldSendUpdate:"
- "setShouldUpdateAccessory:"
- "setSslEnabled:"
- "setSslEnabled:forAddress:"
- "setStimuli:"
- "setTimer:"
- "setTone:"
- "setTone:forAddress:"
- "setTotalSteps:"
- "setTransparencyAmplification:"
- "setTransparencyAmplification:forAddress:"
- "setTransparencyAutobeamformer:"
- "setTransparencyAutobeamformer:forAddress:"
- "setTransparencyBalance:"
- "setTransparencyBalance:forAddress:"
- "setTransparencyBeamforming:"
- "setTransparencyBeamforming:forAddress:"
- "setTransparencyCustomized:"
- "setTransparencyCustomized:forAddress:"
- "setTransparencyNoiseSupressor:"
- "setTransparencyNoiseSupressor:forAddress:"
- "setTransparencyOwnVoice:"
- "setTransparencyOwnVoice:forAddress:"
- "setTransparencyTone:"
- "setTransparencyTone:forAddress:"
- "setTuningDescription:"
- "setType:"
- "setValue:forKey:"
- "setValue:forPreferenceKey:"
- "setVersion:"
- "setVoiceLossArrayLeft:"
- "setVoiceLossArrayRight:"
- "setVolume:"
- "setWithObjects:"
- "setYodelDeviceRecordByAddress:"
- "settingsFromConfiguration:"
- "setupDatabase"
- "setupHearingModeService"
- "sharedAVSystemController"
- "sharedInstance"
- "sharedManager"
- "sharedQueue"
- "sharedServer"
- "shouldSendUpdate"
- "shouldStoreLocally"
- "sinStimulus"
- "sortedArrayUsingComparator:"
- "speechPureToneAverage"
- "sslEnabledForAddress:"
- "startAndReturnError:"
- "stimuli"
- "stop"
- "stringValue"
- "stringWithFormat:"
- "supportsSecureCoding"
- "timer"
- "toggleHearingAidForAddress:"
- "tone"
- "toneForAddress:"
- "totalSteps"
- "transparencyAmplificationForAddress:"
- "transparencyAutobeamformerForAddress:"
- "transparencyBalanceForAddress:"
- "transparencyBeamformingForAddress:"
- "transparencyCustomizedForAddress:"
- "transparencyNoiseSupressorForAddress:"
- "transparencyOwnVoiceForAddress:"
- "transparencySettingsForAddress:"
- "transparencySettingsv4ForAddress:"
- "transparencyToneForAddress:"
- "tuningDescription"
- "type"
- "unregisterListener"
- "unsignedIntegerValue"
- "updateConfiguration:forRouteID:"
- "updateConfiguration:forRouteUID:"
- "updateHeadphoneState"
- "updatePersonalAudioSettings"
- "userInfo"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@16"
- "v24@0:8Q16"
- "v24@0:8d16"
- "v28@0:8B16@20"
- "v32@0:8:16@24"
- "v32@0:8@16@24"
- "v32@0:8@?16Q24"
- "v32@0:8Q16@24"
- "v32@0:8^{?=BB@@@@}16@24"
- "v32@0:8^{?={?=CC}[8f][8f]}16@24"
- "v32@0:8d16@24"
- "v40@0:8@16@24@?32"
- "v48@0:8Q16Q24Q32@?40"
- "valueForKey:"
- "valueForRouteUID:fromCombinedValue:"
- "version"
- "voiceLossArrayLeft"
- "voiceLossArrayRight"
- "volume"
- "writeValue:forCharacteristicUUID:andAddress:"
- "yodelDeviceRecordByAddress"
- "yodelEnabledForAddress:"
- "{?=II}28@0:8@16I24"

```
