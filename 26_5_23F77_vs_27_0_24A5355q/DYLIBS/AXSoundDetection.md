## AXSoundDetection

> `/System/Library/PrivateFrameworks/AXSoundDetection.framework/AXSoundDetection`

```diff

-496.22.0.0.0
-  __TEXT.__text: 0x42e4
-  __TEXT.__auth_stubs: 0x2b0
-  __TEXT.__objc_methlist: 0x380
-  __TEXT.__const: 0x78
-  __TEXT.__cstring: 0xe50
-  __TEXT.__oslogstring: 0x2e1
-  __TEXT.__unwind_info: 0x1b8
-  __TEXT.__objc_classname: 0x22
-  __TEXT.__objc_methname: 0xe3a
-  __TEXT.__objc_methtype: 0xba
-  __TEXT.__objc_stubs: 0xd40
-  __DATA_CONST.__got: 0x1c0
-  __DATA_CONST.__const: 0x1b0
-  __DATA_CONST.__objc_classlist: 0x10
+527.0.0.0.0
+  __TEXT.__text: 0x7784
+  __TEXT.__objc_methlist: 0x828
+  __TEXT.__const: 0x80
+  __TEXT.__dlopen_cstrs: 0x6a
+  __TEXT.__gcc_except_tab: 0x44
+  __TEXT.__cstring: 0x1060
+  __TEXT.__oslogstring: 0x663
+  __TEXT.__unwind_info: 0x298
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x210
+  __DATA_CONST.__objc_classlist: 0x20
+  __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x490
-  __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x160
-  __AUTH_CONST.__const: 0xc0
-  __AUTH_CONST.__cfstring: 0x1560
-  __AUTH_CONST.__objc_const: 0x398
-  __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x18
-  __DATA.__data: 0xd8
-  __DATA.__bss: 0x20
+  __DATA_CONST.__objc_selrefs: 0x870
+  __DATA_CONST.__objc_superrefs: 0x20
+  __DATA_CONST.__got: 0x220
+  __AUTH_CONST.__const: 0xe0
+  __AUTH_CONST.__cfstring: 0x1780
+  __AUTH_CONST.__objc_const: 0x7f0
+  __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__objc_data: 0xf0
+  __DATA.__objc_ivar: 0x40
+  __DATA.__data: 0x198
+  __DATA.__bss: 0x48
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CoreML.framework/CoreML
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/AXAssetLoader.framework/AXAssetLoader
   - /System/Library/PrivateFrameworks/AXCoreUtilities.framework/AXCoreUtilities
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
   - /System/Library/PrivateFrameworks/HearingCore.framework/HearingCore
   - /System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience
+  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/ToneLibrary.framework/ToneLibrary
   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F98ED470-3A88-3CD2-BD9C-09091D9A71FC
-  Functions: 112
-  Symbols:   521
-  CStrings:  553
+  UUID: 415DFDBF-7099-37D9-83A7-70A328231D8D
+  Functions: 194
+  Symbols:   859
+  CStrings:  419
 
Symbols:
+ +[AXSDKShotDetector supportsSecureCoding]
+ -[AXSDDetector .cxx_destruct]
+ -[AXSDDetector _isInBuild]
+ -[AXSDDetector category]
+ -[AXSDDetector compatibilityVersion]
+ -[AXSDDetector contentVersion]
+ -[AXSDDetector debugDescription]
+ -[AXSDDetector description]
+ -[AXSDDetector identifier]
+ -[AXSDDetector initWithIdentifier:]
+ -[AXSDDetector initWithIdentifier:andName:]
+ -[AXSDDetector initWithModel:]
+ -[AXSDDetector initWithType:]
+ -[AXSDDetector isCompatiable]
+ -[AXSDDetector isCustom]
+ -[AXSDDetector isDownloading]
+ -[AXSDDetector isEnabled]
+ -[AXSDDetector isInstalled]
+ -[AXSDDetector isOlderThanDetector:]
+ -[AXSDDetector isUsingSoundPrint]
+ -[AXSDDetector modelURLString]
+ -[AXSDDetector modelURL]
+ -[AXSDDetector model]
+ -[AXSDDetector name]
+ -[AXSDDetector needsUpdate]
+ -[AXSDDetector properties]
+ -[AXSDDetector setIdentifier:]
+ -[AXSDDetector setIsEnabled:]
+ -[AXSDDetector setModelFailed:]
+ -[AXSDDetector setNeedsUpdate:]
+ -[AXSDKShotDetector .cxx_destruct]
+ -[AXSDKShotDetector addRecording:]
+ -[AXSDKShotDetector category]
+ -[AXSDKShotDetector compatibilityVersion]
+ -[AXSDKShotDetector contentVersion]
+ -[AXSDKShotDetector debugDescription]
+ -[AXSDKShotDetector description]
+ -[AXSDKShotDetector encodeWithCoder:]
+ -[AXSDKShotDetector hash]
+ -[AXSDKShotDetector initWithCoder:]
+ -[AXSDKShotDetector initWithName:]
+ -[AXSDKShotDetector initWithName:andIdentifier:]
+ -[AXSDKShotDetector isCustom]
+ -[AXSDKShotDetector isEqual:]
+ -[AXSDKShotDetector isEqualToKShotDetector:]
+ -[AXSDKShotDetector isModelReady]
+ -[AXSDKShotDetector isTrainingComplete]
+ -[AXSDKShotDetector lastAttemptedTrainingDate]
+ -[AXSDKShotDetector mlModel]
+ -[AXSDKShotDetector modelFailed]
+ -[AXSDKShotDetector modelURLString]
+ -[AXSDKShotDetector modelURL]
+ -[AXSDKShotDetector name]
+ -[AXSDKShotDetector recordings]
+ -[AXSDKShotDetector setCategory:]
+ -[AXSDKShotDetector setLastAttemptedTrainingDate:]
+ -[AXSDKShotDetector setModelFailed:]
+ -[AXSDKShotDetector setName:]
+ -[AXSDKShotDetector setRecordings:]
+ -[AXSDKShotDetector setTrainings:]
+ -[AXSDKShotDetector shouldRetrain]
+ -[AXSDKShotDetector trainings]
+ -[AXSDSettings(AXSoundDetectionUIAdditions) _shouldActivateVoiceTriggerSupportForSwitchControl]
+ -[AXSDSettings(AXSoundDetectionUIAdditions) _shouldActivateVoiceTriggerSupportForSystem]
+ -[AXSDSettings(AXSoundDetectionUIAdditions) _shouldActivateVoiceTriggerSupportForVoiceOver]
+ -[AXSDSettings(AXSoundDetectionUIAdditions) _shouldActiveVoiceTriggerSupportForAssistiveTouch]
+ -[AXSDSettings(AXSoundDetectionUIAdditions) addKShotDetector:]
+ -[AXSDSettings(AXSoundDetectionUIAdditions) decodeKShotDetectors:]
+ -[AXSDSettings(AXSoundDetectionUIAdditions) decodedKShotDetectors]
+ -[AXSDSettings(AXSoundDetectionUIAdditions) deleteModelForDetector:]
+ -[AXSDSettings(AXSoundDetectionUIAdditions) deleteRecordingLinksForDetector:]
+ -[AXSDSettings(AXSoundDetectionUIAdditions) deleteTrainingFilesForDetector:]
+ -[AXSDSettings(AXSoundDetectionUIAdditions) detectorForIdentifier:]
+ -[AXSDSettings(AXSoundDetectionUIAdditions) disableDetector:]
+ -[AXSDSettings(AXSoundDetectionUIAdditions) disableKShotDetector:]
+ -[AXSDSettings(AXSoundDetectionUIAdditions) editKShotDetectorName:newName:]
+ -[AXSDSettings(AXSoundDetectionUIAdditions) enableDetector:]
+ -[AXSDSettings(AXSoundDetectionUIAdditions) encodeAndSaveKShotDetectors:]
+ -[AXSDSettings(AXSoundDetectionUIAdditions) encodeKShotDetectors:]
+ -[AXSDSettings(AXSoundDetectionUIAdditions) hasCustomHapticForKshotDetector:]
+ -[AXSDSettings(AXSoundDetectionUIAdditions) hasCustomToneForKshotDetector:]
+ -[AXSDSettings(AXSoundDetectionUIAdditions) kShotCategoryForDetectionType:]
+ -[AXSDSettings(AXSoundDetectionUIAdditions) kShotSoundRecordingsForDetector:]
+ -[AXSDSettings(AXSoundDetectionUIAdditions) removeAllKShotDetectors]
+ -[AXSDSettings(AXSoundDetectionUIAdditions) removeKShotDetector:]
+ -[AXSDSettings(AXSoundDetectionUIAdditions) setDetectorIsEnabled:isEnabled:]
+ -[AXSDSettings(AXSoundDetectionUIAdditions) setKShotDetectorIsEnabled:isEnabled:]
+ -[AXSDSettings(AXSoundDetectionUIAdditions) setKShotDetectorModelFailed:modelFailed:]
+ -[AXSDSettings(AXSoundDetectionUIAdditions) shouldBeListeningForSoundActions]
+ -[AXSDSettings(AXSoundDetectionUIAdditions) shouldBeListeningForSoundRecognitionCustomSounds]
+ -[AXSDSettings(AXSoundDetectionUIAdditions) shouldBeListeningForSoundRecognitionSystemSounds]
+ -[AXSDSettings(AXSoundDetectionUIAdditions) updateKShotDetector:]
+ GCC_except_table86
+ GCC_except_table91
+ _AXLogUltronKShot
+ _AXSDKShotIsValidIdentifier
+ _AXSDKShotIsValidIdentifier.disallowedCharacters
+ _AXSDKShotIsValidIdentifier.onceToken
+ _AXSDKShotSafePathWithinBase
+ _AXSDSoundDetectionLocalizedStringForTypeFromSource
+ _AccessibilityUtilitiesLibraryCore.frameworkLibrary
+ _NSFileProtectionCompleteUntilFirstUserAuthentication
+ _NSFileProtectionKey
+ _NSStringFromBOOL
+ _OBJC_CLASS_$_AXAssetMetadataStore
+ _OBJC_CLASS_$_AXSDDetector
+ _OBJC_CLASS_$_AXSDKShotDetector
+ _OBJC_CLASS_$_AXUltronModelAssetPolicy
+ _OBJC_CLASS_$_MLModel
+ _OBJC_CLASS_$_NSCharacterSet
+ _OBJC_CLASS_$_NSKeyedArchiver
+ _OBJC_CLASS_$_NSKeyedUnarchiver
+ _OBJC_CLASS_$_NSMutableDictionary
+ _OBJC_CLASS_$_NSURL
+ _OBJC_CLASS_$_NSUUID
+ _OBJC_IVAR_$_AXSDDetector._enabled
+ _OBJC_IVAR_$_AXSDDetector._identifier
+ _OBJC_IVAR_$_AXSDDetector._model
+ _OBJC_IVAR_$_AXSDDetector._modelName
+ _OBJC_IVAR_$_AXSDDetector._needsUpdate
+ _OBJC_IVAR_$_AXSDKShotDetector._customName
+ _OBJC_IVAR_$_AXSDKShotDetector._kshotCategory
+ _OBJC_IVAR_$_AXSDKShotDetector._lastAttemptedTrainingDate
+ _OBJC_IVAR_$_AXSDKShotDetector._modelFailed
+ _OBJC_IVAR_$_AXSDKShotDetector._trainings
+ _OBJC_METACLASS_$_AXSDDetector
+ _OBJC_METACLASS_$_AXSDKShotDetector
+ __AXSAssistiveTouchEnabled
+ __AXSAssistiveTouchScannerEnabled
+ __Block_object_dispose
+ __OBJC_$_CLASS_METHODS_AXSDKShotDetector
+ __OBJC_$_CLASS_PROP_LIST_AXSDKShotDetector
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding
+ __OBJC_$_INSTANCE_METHODS_AXSDDetector
+ __OBJC_$_INSTANCE_METHODS_AXSDKShotDetector
+ __OBJC_$_INSTANCE_METHODS_AXSDSettings(AXSoundDetectionUIAdditions)
+ __OBJC_$_INSTANCE_VARIABLES_AXSDDetector
+ __OBJC_$_INSTANCE_VARIABLES_AXSDKShotDetector
+ __OBJC_$_PROP_LIST_AXSDDetector
+ __OBJC_$_PROP_LIST_AXSDKShotDetector
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding
+ __OBJC_CLASS_PROTOCOLS_$_AXSDKShotDetector
+ __OBJC_CLASS_RO_$_AXSDDetector
+ __OBJC_CLASS_RO_$_AXSDKShotDetector
+ __OBJC_LABEL_PROTOCOL_$_NSCoding
+ __OBJC_LABEL_PROTOCOL_$_NSSecureCoding
+ __OBJC_METACLASS_RO_$_AXSDDetector
+ __OBJC_METACLASS_RO_$_AXSDKShotDetector
+ __OBJC_PROTOCOL_$_NSCoding
+ __OBJC_PROTOCOL_$_NSSecureCoding
+ __Unwind_Resume
+ ___AXSDKShotIsValidIdentifier_block_invoke
+ ___AccessibilityUtilitiesLibraryCore_block_invoke
+ ___block_descriptor_40_e5_v8?0l
+ ___block_descriptor_40_e8_32r_e5_v8?0lr32l8
+ ___block_literal_global.29
+ ___block_literal_global.305
+ ___getAXSettingsClass_block_invoke
+ ___getSCATSwitchSourceSoundSymbolLoc_block_invoke
+ ___objc_personality_v0
+ __sl_dlopen
+ _abort_report_np
+ _audit_stringAccessibilityUtilities
+ _dlerror
+ _dlsym
+ _free
+ _getAXSettingsClass
+ _getAXSettingsClass.softClass
+ _getSCATSwitchSourceSoundSymbolLoc.ptr
+ _objc_claimAutoreleasedReturnValue
+ _objc_enumerationMutation
+ _objc_getClass
+ _objc_msgSend$URLWithString:
+ _objc_msgSend$UUID
+ _objc_msgSend$UUIDString
+ _objc_msgSend$_isInBuild
+ _objc_msgSend$_shouldActivateVoiceTriggerSupportForSwitchControl
+ _objc_msgSend$_shouldActivateVoiceTriggerSupportForSystem
+ _objc_msgSend$_shouldActivateVoiceTriggerSupportForVoiceOver
+ _objc_msgSend$_shouldActiveVoiceTriggerSupportForAssistiveTouch
+ _objc_msgSend$addCharactersInString:
+ _objc_msgSend$addSoundDetectionType:
+ _objc_msgSend$alphanumericCharacterSet
+ _objc_msgSend$archivedDataWithRootObject:requiringSecureCoding:error:
+ _objc_msgSend$assetId
+ _objc_msgSend$assistiveTouchActionsBySoundAction
+ _objc_msgSend$assistiveTouchSwitches
+ _objc_msgSend$category
+ _objc_msgSend$compatibilityVersion
+ _objc_msgSend$compileModelAtURL:error:
+ _objc_msgSend$containsObject:
+ _objc_msgSend$contentVersion
+ _objc_msgSend$countByEnumeratingWithState:objects:count:
+ _objc_msgSend$decodeBoolForKey:
+ _objc_msgSend$decodeKShotDetectors:
+ _objc_msgSend$decodeObjectForKey:
+ _objc_msgSend$decodedKShotDetectors
+ _objc_msgSend$deleteModelForDetector:
+ _objc_msgSend$deleteRecordingLinksForDetector:
+ _objc_msgSend$deleteTrainingFilesForDetector:
+ _objc_msgSend$description
+ _objc_msgSend$encodeAndSaveKShotDetectors:
+ _objc_msgSend$encodeBool:forKey:
+ _objc_msgSend$encodeKShotDetectors:
+ _objc_msgSend$encodeObject:forKey:
+ _objc_msgSend$fileExistsAtPath:
+ _objc_msgSend$fileURLWithPath:
+ _objc_msgSend$hasPrefix:
+ _objc_msgSend$hasSuffix:
+ _objc_msgSend$hash
+ _objc_msgSend$identifier
+ _objc_msgSend$initWithArray:
+ _objc_msgSend$initWithIdentifier:
+ _objc_msgSend$initWithIdentifier:andName:
+ _objc_msgSend$invertedSet
+ _objc_msgSend$isCustom
+ _objc_msgSend$isDownloading
+ _objc_msgSend$isEqualToKShotDetector:
+ _objc_msgSend$isInstalled
+ _objc_msgSend$isModelReady
+ _objc_msgSend$isSoundActionsNeededByAST
+ _objc_msgSend$isTrainingComplete
+ _objc_msgSend$isUsingSoundPrint
+ _objc_msgSend$kShotDetectors
+ _objc_msgSend$kShotSoundRecordings
+ _objc_msgSend$kShotSoundRecordingsForDetector:
+ _objc_msgSend$lastAttemptedTrainingDate
+ _objc_msgSend$length
+ _objc_msgSend$localURL
+ _objc_msgSend$maximumCompatibilityVersion
+ _objc_msgSend$minimumCompatibilityVersion
+ _objc_msgSend$model
+ _objc_msgSend$modelFailed
+ _objc_msgSend$modelURL
+ _objc_msgSend$modelURLString
+ _objc_msgSend$modelWithContentsOfURL:error:
+ _objc_msgSend$name
+ _objc_msgSend$numberWithUnsignedInteger:
+ _objc_msgSend$path
+ _objc_msgSend$properties
+ _objc_msgSend$rangeOfCharacterFromSet:
+ _objc_msgSend$rangeOfString:
+ _objc_msgSend$recordings
+ _objc_msgSend$removeItemAtURL:error:
+ _objc_msgSend$removeObjectForKey:
+ _objc_msgSend$removeSoundDetectionType:
+ _objc_msgSend$setCategory:
+ _objc_msgSend$setEnabledKShotDetectorIdentifiers:
+ _objc_msgSend$setIdentifier:
+ _objc_msgSend$setKShotDetectorIsEnabled:isEnabled:
+ _objc_msgSend$setKShotDetectors:
+ _objc_msgSend$setKShotSoundRecordings:
+ _objc_msgSend$setLastAttemptedTrainingDate:
+ _objc_msgSend$setModelFailed:
+ _objc_msgSend$setName:
+ _objc_msgSend$setRecordings:
+ _objc_msgSend$setTrainings:
+ _objc_msgSend$setValue:forKey:
+ _objc_msgSend$setValue:forKey:forAssetType:
+ _objc_msgSend$store
+ _objc_msgSend$stringByAppendingPathExtension:
+ _objc_msgSend$stringByAppendingString:
+ _objc_msgSend$stringByResolvingSymlinksInPath
+ _objc_msgSend$stringByStandardizingPath
+ _objc_msgSend$trainings
+ _objc_msgSend$ultronAssetType
+ _objc_msgSend$ultronModelName
+ _objc_msgSend$unarchivedDictionaryWithKeysOfClasses:objectsOfClasses:fromData:error:
+ _objc_msgSend$unsignedIntegerValue
+ _objc_msgSend$valueForKey:forAssetType:
+ _objc_opt_isKindOfClass
+ _objc_opt_respondsToSelector
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x23
+ _objc_retain_x3
+ _objc_retain_x8
+ _objc_retain_x9
- +[AXSDSettings sharedInstance].cold.1
- -[AXSDSettings hasCustomHapticForDetector:].cold.1
- -[AXSDSettings hasCustomToneForDetector:].cold.1
- -[AXSDSettings keysMonitoredForUpdates].cold.1
- -[AXSDSettings logMessage:].cold.1
- -[AXSDSettings preferenceKeyForSelector:].cold.1
- -[AXSDSettings setSoundDetectionState:].cold.1
- _AXSDSoundDetectionBundle.cold.1
- _AXSDSoundDetectionHandleNotificationsForResponse.cold.1
- _AXSDSoundDetectionLocalizedStringForType.cold.1
- _AXSDSoundDetectionTypeForIdentifier.cold.1
- _AXSDSoundDetectionTypesForCategory.cold.1
- _OUTLINED_FUNCTION_0
- _OUTLINED_FUNCTION_1
- _OUTLINED_FUNCTION_2
- _OUTLINED_FUNCTION_3
- __OBJC_$_INSTANCE_METHODS_AXSDSettings
- __OBJC_$_PROP_LIST_AXSDSettings
- ____AXSDSoundDetectionGatherFilesAndGenerateRadarForNotificationAt_block_invoke.cold.1
- _objc_msgSend$set
- _objc_msgSend$sharedAVSystemController
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "%@, Model URL: %@"
+ "%@, Name: %@, Category: %@, Is Ready: %@, Model URL: %@, Recordings: %@, Model Failed: %@, Trainings: %@, Last Attempted Training Date: %@"
+ "%s"
+ "(nil)"
+ "-_."
+ "."
+ ".."
+ "/"
+ "/var/mobile/Library/Accessibility/SoundDetectionKShot/TrainingFiles"
+ "AXSettings"
+ "AXUltronAssetsInUse"
+ "Cannot delete model: invalid detector identifier."
+ "Cannot delete training files: invalid detector identifier."
+ "Deleted model at path: %@ for detector: %@"
+ "Deleted training files at path: %@ for detector: %@"
+ "DeviceSupportsTelephonyOverUSB"
+ "Error decoding KShot detectors: %@"
+ "Error deleting model for detector: %@ error: %@"
+ "Error deleting training directory for detector: %@ error: %@"
+ "Error encoding KShot detectors: %@"
+ "KShot: blocked invalid identifier: %{public}@"
+ "KShot: path escapes base directory for identifier: %{public}@"
+ "No model found for detector: %@ %@ at URL %@"
+ "No need to delete model for detector: %@, since the model does not exist"
+ "No need to delete training files for detector: %@, since the directory does not exist"
+ "SCATSwitchSourceSound"
+ "Setting sound detection state from an unknown source; if you are in the call stack of this fault, please update your usage of AXSDSettings"
+ "Trying to check custom haptic for detector identifier that doesn't exist!"
+ "Trying to check custom tone for detector identifier that doesn't exist!"
+ "Unable to compile MLModel for detector %@ %@. error: %@"
+ "Unable to find class %s"
+ "[%@] Identifier: %@"
+ "[%@] Name: %@, Identifier: %@, Category: %@, Compat Version: %lu, Version: %lu, Is Installed: %@"
+ "category"
+ "identifier"
+ "lastAttemptedTrainingDate"
+ "modelFailed"
+ "name"
+ "softlink:r:path:/System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities"
+ "trainings"
- ".cxx_destruct"
- "@\"NSArray\""
- "@\"NSDate\""
- "@\"NSString\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8q16"
- "@32@0:8q16@24"
- "AXSDSettings"
- "AXSDSettingsEvent"
- "B16@0:8"
- "B24@0:8@16"
- "Setting sound detection state from an unknown source; if you are in the callstack of this fault, please update your usage of AXSDSettings"
- "T@\"NSArray\",&,D,N"
- "T@\"NSArray\",&,N"
- "T@\"NSArray\",R,D,N"
- "T@\"NSArray\",R,N,V_enabledCustomSounds"
- "T@\"NSArray\",R,N,V_enabledSystemSounds"
- "T@\"NSData\",R,D,N"
- "T@\"NSDate\",R,N,V_timestamp"
- "T@\"NSMutableDictionary\",&,D,N"
- "T@\"NSMutableDictionary\",R,D,N"
- "T@\"NSString\",R,D,N"
- "T@\"NSString\",R,N,V_processName"
- "T@\"NSString\",R,N,V_source"
- "TB,D,N"
- "TB,R,N"
- "Tq,D,N"
- "Tq,N"
- "Tq,R,N,V_state"
- "URL"
- "YiUtBQygkHRhLcdO3LFB4A"
- "_enabledCustomSounds"
- "_enabledSystemSounds"
- "_processName"
- "_setSoundDetectionState:"
- "_soundDetectionState"
- "_source"
- "_state"
- "_timestamp"
- "absoluteString"
- "actionIdentifier"
- "addObject:"
- "addSnoozeDateToSnoozeDictionary:forKey:"
- "addSoundDetectionType:"
- "allObjects"
- "array"
- "arrayWithObjects:count:"
- "attributeForKey:"
- "attributesOfItemAtPath:error:"
- "ax_mappedArrayUsingBlock:"
- "boolValue"
- "boolValueForPreferenceKey:withDefaultValue:"
- "bundleForClass:"
- "callStackSymbols"
- "componentsJoinedByString:"
- "content"
- "count"
- "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
- "currentToneIdentifierForAlertType:topic:"
- "currentVibrationIdentifierForAlertType:topic:"
- "data"
- "date"
- "dateWithTimeIntervalSinceNow:"
- "defaultManager"
- "defaultToneIdentifierForAlertType:topic:"
- "defaultVibrationIdentifierForAlertType:topic:"
- "defaultWorkspace"
- "dictionary"
- "dictionaryRepresentation"
- "dictionaryWithObjects:forKeys:count:"
- "enabledCustomSounds"
- "enabledKShotDetectorIdentifiers"
- "enabledSoundDetectionTypes"
- "enabledSystemSounds"
- "enumeratorAtPath:"
- "fileCreationDate"
- "fileExistsAtPath:isDirectory:"
- "forceMedinaSupport"
- "hasCustomHapticForDetector:"
- "hasCustomToneForDetector:"
- "hasValidCustomDetector"
- "init"
- "initWithDictionaryRepresentation:"
- "initWithObjectsAndKeys:"
- "initWithState:source:"
- "initialize"
- "integerValue"
- "integerValueForKey:withDefaultValue:"
- "isActivelyTrainingAKShotModel"
- "isEqualToString:"
- "kShotDetectors"
- "kShotShouldSaveCurrentSound"
- "kShotSoundRecordings"
- "keysMonitoredForUpdates"
- "keysToSync"
- "laterDate:"
- "latestSettingsEvents"
- "latestSettingsEventsDictionaries"
- "localizedCompare:"
- "localizedNameForSoundDetectionType:"
- "localizedStringForKey:value:table:"
- "localizedStringWithFormat:"
- "logMessage:"
- "lowercaseString"
- "micDisabled"
- "mutableCopy"
- "nextObject"
- "notification"
- "now"
- "numberWithBool:"
- "numberWithInteger:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "objectValueForKey:withClass:andDefaultValue:"
- "openURL:withOptions:"
- "pipeFile:"
- "pipedInFile"
- "preferenceDomainForPreferenceKey:"
- "preferenceKeyForSelector:"
- "processInfo"
- "q"
- "q16@0:8"
- "queryItemWithName:value:"
- "registerSettingsEvent:"
- "removeAllSoundDetectionTypes"
- "removeObject:"
- "removeObjectsInRange:"
- "removeSoundDetectionType:"
- "request"
- "retrainModelIdentifier"
- "retrainModelWithIdentifier:"
- "set"
- "setEnabledKShotDetectorIdentifiers:"
- "setEnabledSoundDetectionTypes:"
- "setForceMedinaSupport:"
- "setHost:"
- "setIsActivelyTrainingAKShotModel:"
- "setKShotDetectors:"
- "setKShotShouldSaveCurrentSound:"
- "setKShotSoundRecordings:"
- "setLatestSettingsEvents:"
- "setLatestSettingsEventsDictionaries:"
- "setMicDisabled:"
- "setObject:forKey:"
- "setPipedInFile:"
- "setQueryItems:"
- "setRetrainModelIdentifier:"
- "setScheme:"
- "setSoundDetectionKShotListeningState:"
- "setSoundDetectionSnoozeDictionary:"
- "setSoundDetectionState:"
- "setSoundDetectionState:source:"
- "setSupportedSoundDetectionTypes:"
- "setUltronIsRunning:"
- "setUltronSupportEnabled:"
- "setValue:forPreferenceKey:"
- "setWithArray:"
- "setWithObjects:"
- "sharedAVSystemController"
- "sharedInstance"
- "sharedToneManager"
- "sharedVibrationManager"
- "shouldStoreLocally"
- "sortedArrayUsingComparator:"
- "sortedSupportedSoundDetectionTypes"
- "soundAlertTopicForSoundDetectionType:"
- "soundDetectionEnabled"
- "soundDetectionKShotListeningState"
- "soundDetectionSnoozeDictionary"
- "soundDetectionState"
- "string"
- "stringByAppendingPathComponent:"
- "stringForSoundDetectionState:"
- "stringWithFormat:"
- "supportedSoundDetectionTypes"
- "timeIntervalSinceDate:"
- "ultronIsRunning"
- "ultronSupportEnabled"
- "userInfo"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@16"
- "v24@0:8q16"
- "v32@0:8@16@24"
- "v32@0:8q16@24"

```
