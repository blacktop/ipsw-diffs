## AXTapToSpeakTime

> `/System/Library/PrivateFrameworks/AXTapToSpeakTime.framework/AXTapToSpeakTime`

```diff

-3191.35.0.0.0
-  __TEXT.__text: 0x7970
-  __TEXT.__auth_stubs: 0x550
+3229.1.6.0.0
+  __TEXT.__text: 0x6e68
   __TEXT.__objc_methlist: 0x87c
-  __TEXT.__const: 0xc2
-  __TEXT.__cstring: 0x8f7
+  __TEXT.__const: 0xb8
+  __TEXT.__gcc_except_tab: 0xe0
   __TEXT.__oslogstring: 0xdfc
-  __TEXT.__gcc_except_tab: 0xf8
-  __TEXT.__unwind_info: 0x278
-  __TEXT.__objc_classname: 0xb4
-  __TEXT.__objc_methname: 0x1b96
-  __TEXT.__objc_methtype: 0x463
-  __TEXT.__objc_stubs: 0x1720
-  __DATA_CONST.__got: 0x1a8
+  __TEXT.__cstring: 0x900
+  __TEXT.__unwind_info: 0x240
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x3a0
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x18

   __DATA_CONST.__objc_selrefs: 0x810
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_arraydata: 0x50
-  __AUTH_CONST.__auth_got: 0x2b8
+  __DATA_CONST.__got: 0x1a0
   __AUTH_CONST.__const: 0x100
   __AUTH_CONST.__cfstring: 0xae0
   __AUTH_CONST.__objc_const: 0x910
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_arrayobj: 0x60
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x190
   __DATA.__objc_ivar: 0x5c
   __DATA.__data: 0x120

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreAudio_Private.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
-  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: DFF2EE1E-748A-3CC0-8129-3F4B432F3BCA
-  Functions: 196
-  Symbols:   894
-  CStrings:  636
+  UUID: 74F85DC7-0B17-3ECC-A8E4-2A21B49B4E54
+  Functions: 165
+  Symbols:   831
+  CStrings:  268
 
Symbols:
+ GCC_except_table144
+ GCC_except_table73
+ GCC_except_table90
+ GCC_except_table94
+ ___32-[AXTapticChimesScheduler _init]_block_invoke.412
+ ___32-[AXTapticChimesScheduler _init]_block_invoke.415
+ ___63-[AXTapticChimesScheduler _outputTapticChime:atDate:isPreview:]_block_invoke.481
+ ___block_literal_global.139
+ ___block_literal_global.416
+ ___block_literal_global.433
+ ___block_literal_global.439
+ ___block_literal_global.509
+ ___block_literal_global.63
+ ___block_literal_global.78
+ __swift_FORCE_LOAD_$_swiftCompression
+ __swift_FORCE_LOAD_$_swiftCompression_$_AXTapToSpeakTime
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$isSiriVoice
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x8
+ _sharedInstance._Shared.140
+ _sharedInstance._Shared.79
+ _sharedInstance.onceToken.138
+ _sharedInstance.onceToken.62
+ _sharedInstance.onceToken.77
- +[AXFaceOutputManager sharedInstance].cold.1
- +[AXTapToSpeakTimeManager sharedInstance].cold.1
- +[AXTapticChimeAsset hourAssetForType:hour:].cold.1
- +[AXTapticChimeAsset quarterHourAssetForType:minute:].cold.1
- +[AXTapticChimesScheduler sharedInstance].cold.1
- +[AXTimeOutputPreferences sharedInstance].cold.1
- -[AXTapToSpeakTimeManager _canOutputPremiumVoice].cold.1
- -[AXTapticChimeAsset _initWithChimeSoundType:audioFilePath:hapticsFilePath:].cold.1
- -[AXTapticChimesScheduler _chimeDidFinishPlaying].cold.1
- -[AXTapticChimesScheduler _clearChimeTimer].cold.1
- -[AXTapticChimesScheduler _clearChimeTimer].cold.2
- -[AXTapticChimesScheduler _init].cold.1
- -[AXTapticChimesScheduler _outputTapticChime:atDate:isPreview:].cold.1
- -[AXTapticChimesScheduler _outputTapticChime:atDate:isPreview:].cold.2
- -[AXTapticChimesScheduler _outputTapticChime:atDate:isPreview:].cold.3
- -[AXTapticChimesScheduler _outputTapticChime:atDate:isPreview:].cold.4
- -[AXTapticChimesScheduler audioPlayerDidFinishPlaying:successfully:].cold.1
- -[AXTimeOutputPreferences _npsValueForPreferenceKey:expectedClass:].cold.1
- -[AXTimeOutputPreferences _npsValueForPreferenceKey:expectedClass:].cold.2
- -[AXTimeOutputPreferences _setNPSValue:preferenceKey:].cold.1
- -[AXTimeOutputPreferences _setNPSValue:preferenceKey:].cold.2
- -[AXTimeOutputPreferences _setNPSValue:preferenceKey:].cold.3
- -[AXTimeOutputPreferences localizedStringForKey:].cold.1
- -[AXTimeOutputPreferences unity25_localizedStringForKey:].cold.1
- GCC_except_table26
- GCC_except_table3
- GCC_except_table4
- GCC_except_table8
- _OBJC_CLASS_$_TTSAlternativeVoices
- _OUTLINED_FUNCTION_0
- _OUTLINED_FUNCTION_1
- _OUTLINED_FUNCTION_2
- _OUTLINED_FUNCTION_3
- _OUTLINED_FUNCTION_4
- _OUTLINED_FUNCTION_5
- ___32-[AXTapticChimesScheduler _init]_block_invoke.349
- ___32-[AXTapticChimesScheduler _init]_block_invoke.352
- ___63-[AXTapticChimesScheduler _outputTapticChime:atDate:isPreview:]_block_invoke.418
- ___block_literal_global.354
- ___block_literal_global.370
- ___block_literal_global.376
- ___block_literal_global.446
- __swift_FORCE_LOAD_$_swiftCoreMedia
- __swift_FORCE_LOAD_$_swiftCoreMedia_$_AXTapToSpeakTime
- _objc_msgSend$isSiriVoiceIdentifier:
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x23
- _objc_retain_x24
CStrings:
+ "Default to system voice for current language: %@"
- "#16@0:8"
- ".cxx_destruct"
- "@\"AVAudioPlayer\""
- "@\"AVSpeechSynthesizer\""
- "@\"AXTapticChimeAsset\""
- "@\"AXTapticTimeManager\""
- "@\"NSDate\""
- "@\"NSDateFormatter\""
- "@\"NSDictionary\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"PCSimpleTimer\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8q16"
- "@32@0:8:16@24"
- "@32@0:8@16#24"
- "@32@0:8q16@24"
- "@32@0:8q16Q24"
- "@40@0:8:16@24@32"
- "@40@0:8q16@24@32"
- "@48@0:8@16q24q32^d40"
- "AVAudioPlayerDelegate"
- "AVSpeechSynthesizerDelegate"
- "AXFaceOutputManager"
- "AXTapToSpeakTimeManager"
- "AXTapticChimeAsset"
- "AXTapticChimesScheduler"
- "AXTimeOutputPreferences"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B28@0:8@16B24"
- "B32@0:8@16@24"
- "B32@0:8Q16Q24"
- "B36@0:8@16@24B32"
- "Default to system voice for current langauge: %@"
- "I"
- "I24@0:8d16"
- "I32@0:8@16d24"
- "NSObject"
- "Q16@0:8"
- "T#,R"
- "T@\"AVSpeechSynthesizer\",R,N,V_avSpeechSynthesizer"
- "T@\"AXTapticTimeManager\",R,N,V_tapticTimeManager"
- "T@\"NSArray\",R,N"
- "T@\"NSDateFormatter\",R,N,V_dateFormatter"
- "T@\"NSDictionary\",R,N,V_hapticDictionary"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,N,V_audioFilePath"
- "TQ,R"
- "Td,R,N,V_prePlayTimeInterval"
- "Tf,N,V_lastMediaVolume"
- "Tf,R,N,V_volume"
- "URLWithString:"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_assetPathForChimeSoundType:fileName:"
- "_audioFilePath"
- "_audioPlaybackPowerAssertionID"
- "_audioPlayer"
- "_avSpeechSynthesizer"
- "_cachedRingerIsMuted"
- "_canOutputPremiumVoice"
- "_canSpeakTimeForVoice:andGesture:"
- "_canTapticTime"
- "_chimeDidFinishPlaying"
- "_chimeTimer"
- "_chimeWakeTimerFired:"
- "_clearChimeTimer"
- "_createPowerAssertionWithName:timeout:"
- "_currentChimeAsset"
- "_currentDate"
- "_currentLanguageCode"
- "_dateFormatter"
- "_denormalizeVolumeIfNecessary"
- "_getPreferredSpeechSynthesisVoice"
- "_hapticDictionary"
- "_init"
- "_initWithChimeSoundType:audioFilePath:hapticsFilePath:"
- "_lastActualChimeTime"
- "_lastActualWakeTime"
- "_lastExpectedChimeTime"
- "_lastExpectedWakeTime"
- "_lastMediaVolume"
- "_mediaQueue"
- "_normalizeVolumeIfNecessary"
- "_npsBoolValueForPreferenceKey:defaultValue:"
- "_npsIntegerValueForPreferenceKey:defaultValue:"
- "_npsValueForPreferenceKey:"
- "_npsValueForPreferenceKey:expectedClass:"
- "_outputTapticChime:atDate:"
- "_outputTapticChime:atDate:isPreview:"
- "_outputTapticTime:"
- "_pcServiceIdentifier"
- "_prePlayAudioTimeInterval"
- "_prePlayTimeInterval"
- "_preWakeTimeInterval"
- "_previewChimes"
- "_previewChimesForStartDate:chimeDate:frequency:soundType:"
- "_previousAudioSessionCategory"
- "_queue"
- "_registerForNotifications"
- "_releasePowerAssertionIfPossible:"
- "_ringerStateChanged"
- "_ringerStateNotifyToken"
- "_scheduleChimeTimer"
- "_setNPSValue:preferenceKey:"
- "_setVoiceOverTapticChimesUnity25SoundType:"
- "_setupAudioSessionForVoice:"
- "_speakTime:preferredVoice:"
- "_speakTime:withCharacterVoiceIdentifier:"
- "_speechVoicesIncludingSiri"
- "_syncWithStandardVoiceOverTapticChimesSoundType:"
- "_syncWithUnity25VoiceOverTapticChimesSoundType:"
- "_tapticChimesStateDidChange:"
- "_tapticTimeManager"
- "_unregisterForNotifications"
- "_voiceOverIsEnabled"
- "_voiceOverIsInTripleClick"
- "_voiceOverTapticChimesUnity25SoundType"
- "_volume"
- "accessibilityDomainAccessor"
- "addObject:"
- "addObserverForName:object:queue:usingBlock:"
- "array"
- "arrayWithArray:"
- "arrayWithObjects:count:"
- "audioFilePath"
- "audioPlayerBeginInterruption:"
- "audioPlayerDecodeErrorDidOccur:error:"
- "audioPlayerDidFinishPlaying:successfully:"
- "audioPlayerEndInterruption:"
- "audioPlayerEndInterruption:withFlags:"
- "audioPlayerEndInterruption:withOptions:"
- "autorelease"
- "autoupdatingCurrentLocale"
- "avSpeechSynthesizer"
- "ax_firstObjectUsingBlock:"
- "boolValue"
- "bundleForClass:"
- "bundlePath"
- "canOutputTime"
- "canPlayScheduledTapticChime"
- "canPlayTapticChime"
- "canScheduleTapticChimes"
- "category"
- "class"
- "components:fromDate:"
- "componentsJoinedByString:"
- "conformsToProtocol:"
- "containsString:"
- "countByEnumeratingWithState:objects:count:"
- "createSystemSoundIDForStartTime:"
- "currentCalendar"
- "d"
- "d16@0:8"
- "date"
- "dateByAddingTimeInterval:"
- "dateFormatFromTemplate:options:locale:"
- "dateFormatter"
- "dateFromComponents:"
- "dateWithTimeInterval:sinceDate:"
- "dateWithTimeIntervalSinceNow:"
- "dealloc"
- "debugDescription"
- "defaultCenter"
- "description"
- "deviceCurrentTime"
- "dictionaryWithContentsOfFile:"
- "dictionaryWithDictionary:"
- "dictionaryWithObjects:forKeys:count:"
- "domain"
- "doubleValue"
- "f"
- "f16@0:8"
- "floatValue"
- "hapticAtomEntries"
- "hapticDictionary"
- "hasPrefix:"
- "hash"
- "hour"
- "hourAssetForType:hour:"
- "i"
- "identifier"
- "indexOfObject:"
- "init"
- "initWithCalendarIdentifier:"
- "initWithContentsOfURL:error:"
- "initWithDomain:"
- "initWithTimeInterval:serviceIdentifier:target:selector:userInfo:"
- "initializeDrumMachine"
- "initializeIfNeeded"
- "integerValue"
- "invalidate"
- "isAllowedToChimeAt:"
- "isCurrentlyOutputting"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isSiriVoiceIdentifier:"
- "isSpeaking"
- "language"
- "languageCode"
- "lastMediaVolume"
- "lastObject"
- "length"
- "localeIdentifier"
- "localizedStringForKey:"
- "localizedStringForKey:value:table:"
- "localizedStringForTapToSpeakTimeAvailability:"
- "localizedStringForTapticChimesFrequencyEncoding:"
- "localizedStringForTapticChimesSoundType:"
- "localizedStringForTapticTimeEncoding:"
- "lowercaseString"
- "mainQueue"
- "mainRunLoop"
- "minute"
- "mutableCopy"
- "name"
- "nextChimeAssetForStartDate:frequency:soundType:timeIntervalUntilChime:"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithInteger:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "outputHoursAndMinutes:"
- "outputTime:"
- "outputTime:preferredVoice:"
- "outputTime:preferredVoice:withGesture:"
- "outputVoice"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "playAtTime:"
- "playDrumMachineSound:"
- "prePlayTimeInterval"
- "preferenceKeyForSelector:"
- "prepareToPlay"
- "processIsAllowedToInterfaceWithNanoMediaRemote"
- "processIsAllowedToScheduleChimes"
- "q16@0:8"
- "q32@0:8@16q24"
- "quality"
- "quarterHourAssetForType:minute:"
- "registerUpdateBlock:forRetrieveSelector:withListener:"
- "release"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "scheduleInRunLoop:"
- "second"
- "self"
- "setActive:error:"
- "setActive:withOptions:error:"
- "setCategory:error:"
- "setCategory:withOptions:error:"
- "setDateFormat:"
- "setDelegate:"
- "setIsInternalSynth:"
- "setLastMediaVolume:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setTapToSpeakTimeAvailability:"
- "setTapToSpeakTimeEnabled:"
- "setTimeZone:"
- "setUserVisible:"
- "setVoice:"
- "setVoiceOverTapticChimesEnabled:"
- "setVoiceOverTapticChimesFrequencyEncoding:"
- "setVoiceOverTapticChimesSoundType:"
- "setVoiceOverTapticChimesSoundTypeForCurrentFace:"
- "setVoiceOverTapticChimesUnity25Active:"
- "setVoiceOverTapticTimeEncoding:"
- "setVoiceOverTapticTimeMode:"
- "setVolume:"
- "setWithArray:"
- "sharedInstance"
- "sharedPreferences"
- "sortUsingComparator:"
- "speakUtterance:"
- "speechOutputDidComplete"
- "speechSynthesizer:didCancelSpeechUtterance:"
- "speechSynthesizer:didContinueSpeechUtterance:"
- "speechSynthesizer:didFinishSpeechUtterance:"
- "speechSynthesizer:didPauseSpeechUtterance:"
- "speechSynthesizer:didStartSpeechUtterance:"
- "speechSynthesizer:willSpeakMarker:utterance:"
- "speechSynthesizer:willSpeakRangeOfSpeechString:utterance:"
- "speechUtteranceWithString:"
- "stop"
- "stopCurrentOutput"
- "stopOutput"
- "stopSpeakingAtBoundary:"
- "stringByAppendingPathComponent:"
- "stringFromDate:"
- "stringWithFormat:"
- "superclass"
- "synchronize"
- "synchronizeNanoDomain:keys:"
- "systemLanguageID"
- "tapToSpeakAvailabilityOptions"
- "tapToSpeakTimeAvailability"
- "tapToSpeakTimeEnabled"
- "tapToSpeakTimeLocalizedDescription"
- "tapToSpeakTimeLocalizedTitle"
- "tapticChimesFrequencyOptions"
- "tapticChimesLocalizedCurrentFrequency"
- "tapticChimesLocalizedCurrentSounds"
- "tapticChimesLocalizedDescription"
- "tapticChimesLocalizedTitle"
- "tapticChimesScheduleLocalizedTitle"
- "tapticChimesSoundsLocalizedTitle"
- "tapticChimesSoundsOptions"
- "tapticTimeEncodingOptions"
- "tapticTimeIsAvailable"
- "tapticTimeLocalizedCurrentMode"
- "tapticTimeLocalizedDescription"
- "tapticTimeLocalizedTitle"
- "tapticTimeManager"
- "tapticTimeModeLocalizedDescription"
- "tearDownDrumMachine"
- "timeIntervalSinceDate:"
- "timeIntervalSinceNow"
- "timeZoneWithAbbreviation:"
- "unity25_localizedStringForKey:"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8I16"
- "v20@0:8f16"
- "v24@0:8@\"AVAudioPlayer\"16"
- "v24@0:8@16"
- "v24@0:8Q16"
- "v24@0:8q16"
- "v28@0:8@\"AVAudioPlayer\"16B24"
- "v28@0:8@16B24"
- "v32@0:8@\"AVAudioPlayer\"16@\"NSError\"24"
- "v32@0:8@\"AVAudioPlayer\"16Q24"
- "v32@0:8@\"AVSpeechSynthesizer\"16@\"AVSpeechUtterance\"24"
- "v32@0:8@16@24"
- "v32@0:8@16Q24"
- "v40@0:8@\"AVSpeechSynthesizer\"16@\"AVSpeechSynthesisMarker\"24@\"AVSpeechUtterance\"32"
- "v40@0:8@16@24@32"
- "v40@0:8@16Q24Q32"
- "v48@0:8@\"AVSpeechSynthesizer\"16{_NSRange=QQ}24@\"AVSpeechUtterance\"40"
- "v48@0:8@16@24q32q40"
- "v48@0:8@16{_NSRange=QQ}24@40"
- "voiceOverTapticChimesEnabled"
- "voiceOverTapticChimesFrequencyEncoding"
- "voiceOverTapticChimesScheduleDateEnd"
- "voiceOverTapticChimesScheduleDateStart"
- "voiceOverTapticChimesScheduleEnabled"
- "voiceOverTapticChimesSoundType"
- "voiceOverTapticChimesSoundTypeForCurrentFace"
- "voiceOverTapticChimesUnity25Active"
- "voiceOverTapticChimesUnity25SoundType"
- "voiceOverTapticTimeEncoding"
- "voiceOverTapticTimeMode"
- "voiceWithLanguage:"
- "volume"
- "zone"

```
