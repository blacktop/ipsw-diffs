## AXCoreUtilities

> `/System/Library/PrivateFrameworks/AXCoreUtilities.framework/Versions/A/AXCoreUtilities`

```diff

-3148.7.15.0.0
-  __TEXT.__text: 0x94644
-  __TEXT.__auth_stubs: 0x2530
-  __TEXT.__objc_methlist: 0x2864
+3148.15.11.1.0
+  __TEXT.__text: 0x92b34
+  __TEXT.__auth_stubs: 0x2520
+  __TEXT.__objc_methlist: 0x2a9c
   __TEXT.__const: 0x2ce4
-  __TEXT.__gcc_except_tab: 0x6ec
+  __TEXT.__gcc_except_tab: 0x6dc
   __TEXT.__cstring: 0x620c
   __TEXT.__dlopen_cstrs: 0x19e
   __TEXT.__oslogstring: 0xd66
   __TEXT.__ustring: 0x8
   __TEXT.__constg_swiftt: 0x1560
-  __TEXT.__swift5_typeref: 0x1271
+  __TEXT.__swift5_typeref: 0x1257
   __TEXT.__swift5_builtin: 0x118
   __TEXT.__swift5_reflstr: 0x50b
   __TEXT.__swift5_fieldmd: 0x944

   __TEXT.__swift5_proto: 0x198
   __TEXT.__swift5_types: 0xc4
   __TEXT.__swift5_capture: 0xf50
+  __TEXT.__swift_as_entry: 0x48
+  __TEXT.__swift_as_ret: 0x54
   __TEXT.__swift5_protos: 0x3c
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x27a8
-  __TEXT.__eh_frame: 0x3520
+  __TEXT.__unwind_info: 0x2720
+  __TEXT.__eh_frame: 0x33f8
   __TEXT.__objc_classname: 0x71c
   __TEXT.__objc_methname: 0x6f57
   __TEXT.__objc_methtype: 0xbd4
   __TEXT.__objc_stubs: 0x4c40
-  __DATA_CONST.__got: 0x7b0
-  __DATA_CONST.__const: 0xba8
+  __DATA_CONST.__got: 0x828
+  __DATA_CONST.__const: 0xbb8
   __DATA_CONST.__objc_classlist: 0x2a0
   __DATA_CONST.__objc_nlclslist: 0x8
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1bc0
+  __DATA_CONST.__objc_selrefs: 0x1c28
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x88
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x12a8
-  __AUTH_CONST.__const: 0x52d8
-  __AUTH_CONST.__cfstring: 0x5580
-  __AUTH_CONST.__objc_const: 0x5730
+  __AUTH_CONST.__auth_got: 0x12a0
+  __AUTH_CONST.__const: 0x5380
+  __AUTH_CONST.__cfstring: 0x55a0
+  __AUTH_CONST.__objc_const: 0x5338
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x15d0
   __AUTH.__data: 0x1230
   __DATA.__objc_ivar: 0x1b4
-  __DATA.__data: 0x1388
+  __DATA.__data: 0x1380
   __DATA.__bss: 0x3fe0
   __DATA.__common: 0xb0
   __DATA_DIRTY.__objc_data: 0x280

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: F14488D6-BD44-386B-AC10-D58CE772D193
-  Functions: 3910
-  Symbols:   5223
-  CStrings:  3167
+  UUID: 8F11458E-A72D-30F2-90CE-E971AD59E6CF
+  Functions: 4157
+  Symbols:   5522
+  CStrings:  3169
 
Symbols:
+ +[AXBinaryMonitor sharedInstance].cold.1
+ +[AXCodeItem _codeItemQueue].cold.1
+ +[AXCodeLoader defaultLoader].cold.1
+ +[AXLogColorizer defaultColorizer].cold.1
+ +[AXLoggingSubsystem initialize].cold.1
+ +[AXValidationManager sharedInstance].cold.1
+ +[_AXDyldImageMonitor sharedInstance].cold.1
+ +[_NSObject_SwiftObject_SafeSwiftValuesSupport load].cold.1
+ -[AXBaseSettings _registerForNotification:].cold.1
+ -[AXBaseSettings _registerUpdateBlock:forPreferenceKey:withListener:].cold.1
+ -[AXBaseSettings _userDefaultsStoreForDomainName:].cold.1
+ -[AXCodeLoader _accessibilityBundleMapURLs].cold.1
+ -[NSObject(AXSideStorage) _axDictionaryQueue].cold.1
+ -[NSProxy(AXSideStorage) _axDictionaryQueue].cold.1
+ ASTLogCommon.cold.1
+ ASTLogMouse.cold.1
+ AXApplicationGetMainBundleIdentifier.cold.1
+ AXApplicationIsViewService.cold.1
+ AXBackgroundLog.cold.1
+ AXCArrayCreate.cold.1
+ AXCArrayGetTypeID.cold.1
+ AXCLanguageToFallbacks.cold.1
+ AXCLanguageToLocales.cold.1
+ AXCUApplicationGetMainBundleIdentifier.cold.1
+ AXCUProcessIsAXUIServer.cold.1
+ AXCUProcessIsAssistiveTouch.cold.1
+ AXCUProcessIsMagnifierAngel.cold.1
+ AXCUProcessIsPreferences.cold.1
+ AXCUProcessIsVoiceOverTouch.cold.1
+ AXCUProcessIsVoiceOverUtilityApp.cold.1
+ AXCurrentRootDescription.cold.1
+ AXCurrentRootLooksLikeBNI.cold.1
+ AXDeviceGetType.cold.1
+ AXDeviceIsBigPadIdiom.cold.1
+ AXDeviceIsBigWatchIdiom.cold.1
+ AXDeviceIsPad.cold.1
+ AXDeviceIsPadMiniIdiom.cold.1
+ AXDeviceIsPhone.cold.1
+ AXDeviceIsPhoneIdiom.cold.1
+ AXDeviceIsPod.cold.1
+ AXDeviceIsSmallPhoneIdiom.cold.1
+ AXDeviceIsSmallWatchIdiom.cold.1
+ AXDeviceIsTallPhoneIdiom.cold.1
+ AXDeviceIsVM.cold.1
+ AXDeviceIsVM.onceToken
+ AXDeviceIsVM.result
+ AXDeviceIsWatch.cold.1
+ AXDeviceSupportsAdaptiveVoiceShortcuts.cold.1
+ AXDeviceSupportsVoiceBankingSpeech.cold.1
+ AXDeviceSupportsVoiceBankingTraining.cold.1
+ AXFormatNumber.cold.1
+ AXFormatNumberWithOptions.cold.1
+ AXInstalledApps.cold.1
+ AXIsInternalInstall.cold.1
+ AXIsLookingGlassAvailable.cold.1
+ AXLoadAccessibilityDebuggerIfNeeded.cold.1
+ AXLoadAccessibilityDebuggerIfNeeded.cold.2
+ AXLogAVS.cold.1
+ AXLogAccessories.cold.1
+ AXLogAggregate.cold.1
+ AXLogAirPodSettings.cold.1
+ AXLogAppAccessibility.cold.1
+ AXLogAppCompareGeometry.cold.1
+ AXLogAssertions.cold.1
+ AXLogAssetDaemon.cold.1
+ AXLogAssetLoader.cold.1
+ AXLogAudioRouting.cold.1
+ AXLogBackboardServer.cold.1
+ AXLogBluetooth.cold.1
+ AXLogBrailleHW.cold.1
+ AXLogBrokenHomeButton.cold.1
+ AXLogCharacterVoices.cold.1
+ AXLogCommon.cold.1
+ AXLogContextKit.cold.1
+ AXLogDataMigrator.cold.1
+ AXLogDisplay.cold.1
+ AXLogDisplayFilters.cold.1
+ AXLogDragging.cold.1
+ AXLogElementTraversal.cold.1
+ AXLogEscape.cold.1
+ AXLogEventTap.cold.1
+ AXLogFirstElement.cold.1
+ AXLogFocusEngine.cold.1
+ AXLogHearingTest.cold.1
+ AXLogHitTest.cold.1
+ AXLogIDS.cold.1
+ AXLogIPC.cold.1
+ AXLogInvertColors.cold.1
+ AXLogInvertColorsLoadBundles.cold.1
+ AXLogInvertColorsTraversal.cold.1
+ AXLogLiveTranscription.cold.1
+ AXLogLoading.cold.1
+ AXLogLocCaptionPanel.cold.1
+ AXLogLookingGlass.cold.1
+ AXLogLookingGlassUI.cold.1
+ AXLogMIDI.cold.1
+ AXLogMemoryProfile.cold.1
+ AXLogMuseAccessibility.cold.1
+ AXLogOpaqueElements.cold.1
+ AXLogOrator.cold.1
+ AXLogPerfTesting.cold.1
+ AXLogPhysicalInteraction.cold.1
+ AXLogPronunciations.cold.1
+ AXLogPunctuationStorage.cold.1
+ AXLogRTT.cold.1
+ AXLogRemoteElement.cold.1
+ AXLogScrollToVisible.cold.1
+ AXLogSettings.cold.1
+ AXLogSiriShortcuts.cold.1
+ AXLogSoundBoard.cold.1
+ AXLogSpeakFingerManager.cold.1
+ AXLogSpeakScreen.cold.1
+ AXLogSpeakSelection.cold.1
+ AXLogSpeakTyping.cold.1
+ AXLogSpeechAssetDownload.cold.1
+ AXLogSpeechSynthesis.cold.1
+ AXLogSpokenContentTextProcessing.cold.1
+ AXLogSpringboardServer.cold.1
+ AXLogSystemApp.cold.1
+ AXLogTapticTime.cold.1
+ AXLogTemp.cold.1
+ AXLogTimeProfile.cold.1
+ AXLogTouchAccommodations.cold.1
+ AXLogUI.cold.1
+ AXLogUIA.cold.1
+ AXLogUIViewService.cold.1
+ AXLogUnitTesting.cold.1
+ AXLogUserInterfaceService.cold.1
+ AXLogValidationRunner.cold.1
+ AXLogValidations.cold.1
+ AXLogVectorKit.cold.1
+ AXLogVisibleFrame.cold.1
+ AXLogVisualAlerts.cold.1
+ AXLoggerForFacility.cold.1
+ AXMachTimeToNanoseconds.cold.1
+ AXMediaLogCaptionDescriptions.cold.1
+ AXMediaLogCommon.cold.1
+ AXMediaLogDiagnostics.cold.1
+ AXMediaLogElementVision.cold.1
+ AXMediaLogEngineCache.cold.1
+ AXMediaLogEnginePriority.cold.1
+ AXMediaLogHaptics.cold.1
+ AXMediaLogLanguageTranslation.cold.1
+ AXMediaLogMLElement.cold.1
+ AXMediaLogOCR.cold.1
+ AXMediaLogOutput.cold.1
+ AXMediaLogResults.cold.1
+ AXMediaLogScreenGrab.cold.1
+ AXMediaLogService.cold.1
+ AXMediaLogSettings.cold.1
+ AXMediaLogSounds.cold.1
+ AXMediaLogSpeech.cold.1
+ AXMediaLogTextLayout.cold.1
+ AXMediaLogTextProcessing.cold.1
+ AXMediaLogTracking.cold.1
+ AXPerformValidationChecks.cold.1
+ AXPlatformTranslationLogCommon.cold.1
+ AXProcessGetName.cold.1
+ AXProcessIsAXAssetsd.cold.1
+ AXProcessIsAXSettingsShortcutsPlugin.cold.1
+ AXProcessIsAccessibilityAppIntents.cold.1
+ AXProcessIsAppleTVApp.cold.1
+ AXProcessIsAxctl.cold.1
+ AXProcessIsBackboard.cold.1
+ AXProcessIsCarPlay.cold.1
+ AXProcessIsCarousel.cold.1
+ AXProcessIsCheckerBoard.cold.1
+ AXProcessIsChronod.cold.1
+ AXProcessIsClarityBoard.cold.1
+ AXProcessIsClockFace.cold.1
+ AXProcessIsCommandAndControl.cold.1
+ AXProcessIsFullKeyboardAccess.cold.1
+ AXProcessIsInCallService.cold.1
+ AXProcessIsInputUI.cold.1
+ AXProcessIsLiveSpeech.cold.1
+ AXProcessIsMobileMail.cold.1
+ AXProcessIsMomentsUIService.cold.1
+ AXProcessIsPhotos.cold.1
+ AXProcessIsPineBoard.cold.1
+ AXProcessIsPosterBoard.cold.1
+ AXProcessIsPreBoard.cold.1
+ AXProcessIsPreferences.cold.1
+ AXProcessIsRTTNotificationContentExtension.cold.1
+ AXProcessIsSafari.cold.1
+ AXProcessIsSetup.cold.1
+ AXProcessIsShortcuts.cold.1
+ AXProcessIsSiri.cold.1
+ AXProcessIsSpotlight.cold.1
+ AXProcessIsSpringBoard.cold.1
+ AXProcessIsStickerPickerService.cold.1
+ AXProcessIsSurfBoard.cold.1
+ AXProcessIsSystemApplication.cold.1
+ AXProcessIsSystemApplication.cold.2
+ AXProcessIsSystemApplication.cold.3
+ AXProcessIsSystemApplication.cold.4
+ AXProcessIsSystemApplication.cold.5
+ AXProcessIsSystemApplication.cold.6
+ AXProcessIsVoicebankingd.cold.1
+ AXProcessIsWidgetRenderer.cold.1
+ AXProcessMacOSSettingsExtension.cold.1
+ AXRuntimeCheck_HasANE.cold.1
+ AXRuntimeCheck_LargeTextMac.cold.1
+ AXRuntimeCheck_MauiSSE.cold.1
+ AXRuntimeCheck_MauiSSE.cold.2
+ AXRuntimeCheck_MauiSSEOnly.cold.1
+ AXRuntimeCheck_PerVoiceSettings.cold.1
+ AXRuntimeCheck_ScreenRecognitionSupport.cold.1
+ AXRuntimeCheck_SiriSSEOnly.cold.1
+ AXRuntimeCheck_SpeakUp.cold.1
+ AXRuntimeCheck_SupportsDoseAnalysis.cold.1
+ AXRuntimeCheck_SupportsLiveCaptions.cold.1
+ AXRuntimeCheck_SupportsLiveCaptions.cold.2
+ AXRuntimeCheck_SupportsMacAXV2.cold.1
+ AXRuntimeCheck_VoiceOverSupportsNeuralVoices.cold.1
+ AXRuntimeCheck_isANEDeviceH13plus.cold.1
+ AXRuntimeLogCommon.cold.1
+ AXRuntimeLogElementFetcher.cold.1
+ AXRuntimeLogNotifications.cold.1
+ AXRuntimeLogPID.cold.1
+ AXRuntimeLogSerialization.cold.1
+ AXSharedInertMetric.cold.1
+ AXShouldLogValidationErrors.cold.1
+ AXSupportLogCommon.cold.1
+ AXSystemGetVersion.cold.1
+ AXSystemIsBrighton.cold.1
+ AXSystemIsInnsbruck.cold.1
+ AXSystemIsSundance.cold.1
+ AXSystemVersionEqualTo.cold.1
+ AXSystemVersionEqualToOrGreaterThan.cold.1
+ AXSystemVersionEqualToOrLessThan.cold.1
+ AXTTSLogCommon.cold.1
+ AXTTSLogKona.cold.1
+ AXTTSLogRange.cold.1
+ AXTTSLogResourceManager.cold.1
+ AXTTSLogResourceMigration.cold.1
+ AXTTSLogVoiceBank.cold.1
+ BRLLogTranslation.cold.1
+ CLFLogCommon.cold.1
+ CLFLogSettings.cold.1
+ FKALogCommon.cold.1
+ GAXLogAppLaunching.cold.1
+ GAXLogBlockedTouches.cold.1
+ GAXLogCommon.cold.1
+ GAXLogIntegrity.cold.1
+ GAXLogTimeRestrictions.cold.1
+ GCC_except_table23
+ GCC_except_table44
+ LiveSpeechLogCommon.cold.1
+ MAGLogBrightness.cold.1
+ MAGLogCommon.cold.1
+ SWCHLogCommon.cold.1
+ SWCHLogElementNav.cold.1
+ SWCHLogHW.cold.1
+ SWCHLogMenu.cold.1
+ SWCHLogPauseResume.cold.1
+ VOTLogActivities.cold.1
+ VOTLogAudio.cold.1
+ VOTLogBraille.cold.1
+ VOTLogBrailleGestures.cold.1
+ VOTLogCommands.cold.1
+ VOTLogCommon.cold.1
+ VOTLogElement.cold.1
+ VOTLogEvent.cold.1
+ VOTLogHandwriting.cold.1
+ VOTLogIAP.cold.1
+ VOTLogICloud.cold.1
+ VOTLogKeyboard.cold.1
+ VOTLogLayoutChange.cold.1
+ VOTLogLifeCycle.cold.1
+ VOTLogMagicTap.cold.1
+ VOTLogNotifications.cold.1
+ VOTLogQuickSettings.cold.1
+ VOTLogRotor.cold.1
+ VOTLogSimpleTap.cold.1
+ VOTLogSpeech.cold.1
+ VOTLogTVExplorer.cold.1
+ VOTLogTVFocus.cold.1
+ VOTLogWebPageMovement.cold.1
+ ZOOMLogCommon.cold.1
+ ZOOMLogEvents.cold.1
+ _AXDeviceIsVM
+ _AXInitializeSafeSwiftValueSupport.cold.1
+ _AXLogWithFacility.cold.1
+ _AXLogWithFacilityV.cold.1
+ _AXSVoiceOverTapticChimesUnity25SoundTypeDefault
+ __AXCurrentRootDescription_block_invoke.cold.1
+ __AXRuntimeCheck_ScreenRecognitionSupport_block_invoke.cold.1
+ __AXRuntimeCheck_VoiceOverSupportsNeuralVoices_block_invoke.cold.1
+ __AXSafeSwiftDoubleForKeyTm
+ __AXSafeSwiftOptionalCGSizeForKeyTm
+ __AXSafeSwiftOptionalIntForKeyTm
+ __UIAccessibilityHandleValidationErrorWithDescription.cold.2
+ ___AXDeviceIsVM_block_invoke
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
- GCC_except_table21
- GCC_except_table42
- _fmod
- _symbolic ______pSg 15AXCoreUtilities15AXSettingsStoreP
- _symbolic _____ySS_SaySSGtG s23_ContiguousArrayStorageC
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AccessibilityLibraries"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AccessibilityLibraries/Source/AXCoreUtilities/source/DataStructures/AXIndexMap.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AccessibilityLibraries/Source/AXCoreUtilities/source/DataStructures/NSArray+AXExtensions.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AccessibilityLibraries/Source/AXCoreUtilities/source/DataStructures/NSObject+AXCollectionsExtensions.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AccessibilityLibraries/Source/AXCoreUtilities/source/Logging/AXLoggingSubsystem.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AccessibilityLibraries/Source/AXCoreUtilities/source/Swizzling/AXSideStorage_Implementation.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AccessibilityLibraries/Source/AXCoreUtilities/source/Swizzling/Loading/AXCodeLoader.m"
+ "IsVirtualDevice"
- "/AppleInternal/Library/BuildRoots/91509d18-d3bf-11ef-a177-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AccessibilityLibraries"
- "/AppleInternal/Library/BuildRoots/91509d18-d3bf-11ef-a177-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AccessibilityLibraries/Source/AXCoreUtilities/source/DataStructures/AXIndexMap.m"
- "/AppleInternal/Library/BuildRoots/91509d18-d3bf-11ef-a177-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AccessibilityLibraries/Source/AXCoreUtilities/source/DataStructures/NSArray+AXExtensions.m"
- "/AppleInternal/Library/BuildRoots/91509d18-d3bf-11ef-a177-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AccessibilityLibraries/Source/AXCoreUtilities/source/DataStructures/NSObject+AXCollectionsExtensions.m"
- "/AppleInternal/Library/BuildRoots/91509d18-d3bf-11ef-a177-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AccessibilityLibraries/Source/AXCoreUtilities/source/Logging/AXLoggingSubsystem.m"
- "/AppleInternal/Library/BuildRoots/91509d18-d3bf-11ef-a177-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AccessibilityLibraries/Source/AXCoreUtilities/source/Swizzling/AXSideStorage_Implementation.m"
- "/AppleInternal/Library/BuildRoots/91509d18-d3bf-11ef-a177-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AccessibilityLibraries/Source/AXCoreUtilities/source/Swizzling/Loading/AXCodeLoader.m"

```
