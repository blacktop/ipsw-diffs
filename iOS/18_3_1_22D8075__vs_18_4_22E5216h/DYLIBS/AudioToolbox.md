## AudioToolbox

> `/System/Library/Frameworks/AudioToolbox.framework/AudioToolbox`

```diff

-1456.404.0.0.0
-  __TEXT.__text: 0x294f50
-  __TEXT.__auth_stubs: 0x3bc0
-  __TEXT.__objc_methlist: 0x1658
-  __TEXT.__const: 0x1294
-  __TEXT.__gcc_except_tab: 0x26f7c
-  __TEXT.__cstring: 0x1db2d
-  __TEXT.__oslogstring: 0x35605
+1456.530.0.0.0
+  __TEXT.__text: 0x296f30
+  __TEXT.__auth_stubs: 0x3bb0
+  __TEXT.__objc_methlist: 0x1d4c
+  __TEXT.__const: 0x1344
   __TEXT.__dlopen_cstrs: 0x676
-  __TEXT.__unwind_info: 0xc2d8
+  __TEXT.__gcc_except_tab: 0x28458
+  __TEXT.__cstring: 0x1d12f
+  __TEXT.__oslogstring: 0x33d3f
+  __TEXT.__unwind_info: 0xc3c8
   __TEXT.__objc_classname: 0x3c0
-  __TEXT.__objc_methname: 0x5700
-  __TEXT.__objc_methtype: 0x42fb
+  __TEXT.__objc_methname: 0x5710
+  __TEXT.__objc_methtype: 0x42db
   __TEXT.__objc_stubs: 0x4200
-  __DATA_CONST.__got: 0xd78
-  __DATA_CONST.__const: 0x32a8
+  __DATA_CONST.__got: 0xd68
+  __DATA_CONST.__const: 0x3298
   __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x15a8
+  __DATA_CONST.__objc_selrefs: 0x1648
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0xb0
   __DATA_CONST.__objc_arraydata: 0x358
-  __AUTH_CONST.__auth_got: 0x1df8
-  __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x10a78
-  __AUTH_CONST.__cfstring: 0x5560
-  __AUTH_CONST.__objc_const: 0x3b38
+  __AUTH_CONST.__auth_got: 0x1df0
+  __AUTH_CONST.__auth_ptr: 0x20
+  __AUTH_CONST.__const: 0x10bb8
+  __AUTH_CONST.__cfstring: 0x5540
+  __AUTH_CONST.__objc_const: 0x2e70
   __AUTH_CONST.__objc_intobj: 0x5b8
   __AUTH_CONST.__objc_arrayobj: 0x408
   __AUTH_CONST.__objc_dictobj: 0x28

   __AUTH.__data: 0x30
   __DATA.__objc_ivar: 0x204
   __DATA.__data: 0x7f8
-  __DATA.__bss: 0x20d1
+  __DATA.__bss: 0x20e1
   __DATA_DIRTY.__objc_data: 0x730
   __DATA_DIRTY.__data: 0x48
-  __DATA_DIRTY.__bss: 0x2a80
+  __DATA_DIRTY.__bss: 0x2a70
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreAudio.framework/CoreAudio
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 9227
-  Symbols:   10835
-  CStrings:  8496
+  Functions: 9229
+  Symbols:   10946
+  CStrings:  8302
 
Symbols:
+ _ATSubmixTapNew_CMClient
+ _ATSubmixTapNew_CMServer
+ __ZN17BorealisManagerV210InitializeEv
+ __ZN17BorealisManagerV210initializeEv
+ __ZN17BorealisManagerV214HeySiriEnabledEv
+ __ZN17BorealisManagerV214hasBorealisXPCEv
+ __ZN17BorealisManagerV216useBorealisRouteEv
+ __ZN17BorealisManagerV225SpeechDetectionVADCreatedEv
+ __ZN17BorealisManagerV228SiriClientRecordStateChangedEb
+ __ZN17BorealisManagerV228hardwareSupportsVoiceTriggerEv
+ __ZN17BorealisManagerV28instanceEv
+ __ZN17BorealisManagerV2C1Ev
+ __ZN17BorealisManagerV2C2Ev
+ __ZNSt3__117bad_function_callD1Ev
+ __ZTVNSt3__117bad_function_callE
- __ZNSt3__115system_categoryEv
- _kMXSystemControllerProperty_CurrentlyActiveCategory
CStrings:
+ "%25s:%-5d      GetIONodeClientIsAllowlistedForEnhanceDialogue: AQIONodeClient %p is a VoiceOver client"
+ "%25s:%-5d      GetIONodeClientIsAllowlistedForEnhanceDialogue: AQIONodeClient %p is a ZenAQIONodeClient"
+ "%25s:%-5d      GetIONodeClientIsAllowlistedForEnhanceDialogue: AQIONodeClient %p is a system sound"
+ "%25s:%-5d      GetIONodeClientIsAllowlistedForEnhanceDialogue: AQIONodeClient %p sessionID 0x%x with audio session mode %s is subsession muted"
+ "%25s:%-5d      MEMixerChannel@%p %sconnection triggering enhanceDialogueModeChanged"
+ "%25s:%-5d %s: %@ now available, VAD object ID: %u"
+ "%25s:%-5d %s: %@ now unavailable"
+ "%25s:%-5d %s: Active Audio Route: %@"
+ "%25s:%-5d %s: Adding volume change listener for %@, object ID: %u"
+ "%25s:%-5d %s: Cannot add volume change listener for %@ because object ID is unknown"
+ "%25s:%-5d %s: ERROR: %d, could not add VAD volume listener for %@"
+ "%25s:%-5d %s: Volume changed for %@, objectID: %u, new volume: %.2f"
+ "%25s:%-5d %s: inVADObjectID %u is neither Default nor System Local VAD. No-op"
+ "%25s:%-5d %s: inVADObjectID is invalid! No-op"
+ "%25s:%-5d ** ATSubmixTapNew_CMClient"
+ "%25s:%-5d ** ATSubmixTapNew_CMServer(inClientPID %u, inFlags 0x%x)"
+ "%25s:%-5d ** AudioQueueProcessingTapNew_CMClient"
+ "%25s:%-5d ** AudioQueueProcessingTapNew_CMServer"
+ "%25s:%-5d ASSERTION FAILURE: "
+ "%25s:%-5d AlternateTransport = %d"
+ "%25s:%-5d Assistant enabled(%d) wasEnabled(%d) force(%d)"
+ "%25s:%-5d Assistant voice trigger enabled(%d)"
+ "%25s:%-5d Borealis runningClientCount: %d"
+ "%25s:%-5d EXCEPTION (%d): \"\""
+ "%25s:%-5d Re-Notifying AOP listening state"
+ "%25s:%-5d Re-Notifying AOP listening state failed -- device not found"
+ "%25s:%-5d RemoteIOClient::Start: Error: null ionode! enable %d, valid [%d %d], connected [%d %d]"
+ "%25s:%-5d RemoteIOClient::Start: null ionode, trying to reconnect, enable %d, valid [%d %d], connected [%d %d]"
+ "%25s:%-5d aqmeio@%p: get kBluetoothAudioDevicePropertyAlternateTransport to %d.  err = %d"
+ "%25s:%-5d codec.GetProperty('cori') returns unknown OS type: %d, defaulting"
+ "%25s:%-5d codec.GetProperty('cori') returns unknown source: %d, defaulting"
+ "%25s:%-5d error %d getting kBluetoothAudioDevicePropertyAlternateTransport."
+ "%25s:%-5d error %d setting param with id:%u"
+ "%25s:%-5d getActiveOutputPortType() returns unknown type: %d (%s), defaulting route key"
+ "%25s:%-5d getEnhanceDialogueMovieModeSessionType(notifyOnClientFormatMismatch = %s) = %s [lastMovieModeClient = %p, %d clients]"
+ "%25s:%-5d handling alternate Transport property change: %s"
+ "/System/AppleInternal/Library/Frameworks/AVFAudio.framework/AVFAudio"
+ "/System/AppleInternal/Library/Frameworks/PHASE.framework/PHASE"
+ "/System/AppleInternal/Library/Frameworks/PowerLog.framework/PowerLog"
+ "Couldn't find AOP device so we can't check if we should register VT handler or not. assistantPref(%d), assistantVTPref(%d)"
+ "Mismatch detected at startup between Assistant VT prefs and AOP state. assistantPref(%d), assistantVTPref(%d), aopConfig(%d), aopEnabled(%d)"
+ "T = "
+ "acknowledgeVADVolumeChange"
+ "acknowledgeVolumeChange"
+ "addVolumeChangeListener"
+ "dis"
+ "enhance_dialogue_480_blksz.propstrip"
+ "isAssistantVoiceTriggerEnabled"
+ "{AQMESession=\"mProcessID\"i\"mSessionID\"I\"mSourceSessionID\"{optional<unsigned int>=\"\"(?=\"__null_state_\"c\"__val_\"I)\"__engaged_\"B}\"mSubsessionRef\"{ObjectRef<const void *>=\"mCFObject\"^v}\"mSubsessionID\"Q\"mDescription\"{basic_string<char, std::char_traits<char>, std::allocator<char>>=\"__r_\"{__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=\"__value_\"(__rep=\"__s\"{__short=\"__data_\"[23c]\"__padding_\"[0C]\"__size_\"b7\"__is_long_\"b1}\"__l\"{__long=\"__data_\"*\"__size_\"Q\"__cap_\"b63\"__is_long_\"b1})}}\"mOneWordID\"i\"mBundleID\"{optional<applesauce::CF::StringRef>=\"\"(?=\"__null_state_\"c\"__val_\"{StringRef=\"mObject\"{ObjectRef<const __CFString *>=\"mCFObject\"^{__CFString}}})\"__engaged_\"B}}"
- "%25s:%-5d      getEnhanceDialogueMovieModeSessionType: Allow-list AQIONodeClient %p as VoiceOver client"
- "%25s:%-5d      getEnhanceDialogueMovieModeSessionType: Allow-list AQIONodeClient %p as ZenAQIONodeClient"
- "%25s:%-5d      getEnhanceDialogueMovieModeSessionType: Allow-list AQIONodeClient %p as a system sound"
- "%25s:%-5d      getEnhanceDialogueMovieModeSessionType: Allow-list subsession-muted AQIONodeClient %p sessionID 0x%x with audio session mode %s"
- "%25s:%-5d %s: SystemLocal VAD (vsyl) now %s"
- "%25s:%-5d %s: SystemVolumeDidChange: new volume: %.2f, currentlyActiveCategory: %@, activeAudioRoute: %@"
- "%25s:%-5d ASSERTION FAILURE [(!\"Attempted to add same channel ID twice\") != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(!\"Attempted to add same instance ID twice\") != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(!\"Bad property size\") != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(!\"SHOULD NOT BE RECEIVING REC-STATE-DID-CHANGE NOTIFICATIONS\") != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(!\"Unexpected Property ID\") != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(!\"Unknown property\") != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(!BypassAudioSession() || IsTap()) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(!BypassAudioSession()) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(!audio || _audioPrewarmCount > 0) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(!audio || _audioRunningCount > 0) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(!haptics || _hapticsPrewarmCount > 0) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(!haptics || _hapticsRunningCount > 0) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(!isRunning()) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(!mInitialized) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(!mIsServer) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(!mIsTapSubmix && channel->GetSubmixGraph() == nullptr) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(!mIsTapSubmix && channel->GetSubmixGraph() == this) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(!mIsTapSubmix) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(!running()) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(!stopping()) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(!submixToConnect.mIsTapSubmix && !mainSubmix.mIsTapSubmix) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [((((1 && !0) && !0 && !0) && !CASIsDarwinOS())) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [((client.GetTopologyFlags() & kAudioQueueFlag_HardwarePassthrough) != 0) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(0 != (client.GetTopologyFlags() & kAudioQueueFlag_IsPhaseAQIONodeClient)) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(AudioTapUtilities::CanTapPhase(tapSpecifier())) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(IONodeClientCount() < 2) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(IsInput()) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(_IDBeingStarted == kNoSequenceID || _IDBeingStarted == inID) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(_IDBeingStarted == kNoSequenceID) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(__null != gUserList) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(__null != mCPMSSharedInstanceForHaptics) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(__objc_no != success) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(_channelIDsToBeDetached.size() == 0) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(_initCount > 0) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(_startCount == 0) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(_startCount > 0 && _startCount < 3) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(_state != Uninitialized || inState == Stopped) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(_state == Uninitialized) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(_stoppedDuringFlush == false) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(abl->mNumberBuffers == outputBuffers->mNumberBuffers) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(activeSoundInfo != nullptr) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(clientAudioOutput != nullptr) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(clientID != 9999999) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(clientsWithProcess != _processIndexMap.end()) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(cm == __null) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(currentBufferOffset <= int(inNumberFrames)) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(destABL.mBuffers[0].mDataByteSize >= inNumberFrames * mOutputFormat.mBytesPerFrame) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(e->mNumberParameters == 1) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(e->mParams[i].mID != kAudioQueueParam_PlayRate2) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(entry->stopped()) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(err == noErr) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(false) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(foundUserEvent == true) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(frameOffset < (SInt32)numFrames) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(id < (1UL << 31)) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(inAudioToken) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(inChannels.size() <= mChannelStatus.size()) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(inID != kAudioQueueParam_PlayRate2) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(inState != Starting || _state == Stopped) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(ioBufferList.mNumberBuffers == mRampBufferList->GetNumberBuffers()) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(ioByteSize <= mInputNumBytes) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(ioPackets <= mInputNumPackets) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(ioSize == sizeof(double)) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(it != mInputStates.end()) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(it != mMixerChannels.end()) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(it != mSubmixGraph->mMixerChannels.end()) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(keyrange.mHigh == keyrange.mLow) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(mActiveHighPowerHapticsClients >= 0) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(mActivePriorityClientCountMap[HapticPlayerPriority::ExclusivePriority] != 0) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(mActivePriorityClientCountMap[HapticPlayerPriority::HighPriority] != 0) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(mActivePriorityClientCountMap[HapticPlayerPriority::MediumPriority] != 0) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(mAudioOutput != nullptr) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(mBufferCapacity == 0 || nBytes <= mBufferCapacity) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(mBufferMemory == __null) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(mClientInfo != __null) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(mClientRunMode != kRunMode_NotRunning) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(mDestinationGraph == nullptr && !mIsTapSubmix) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(mDestinationTaps.empty()) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(mHapticOutput != nullptr) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(mIsServer) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(mNumAllocatedSlices == 0) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(mSSSClientEntryRunningCount != 0) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(mSynthRingBuffer != nullptr) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(mTapSources.empty()) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(mixerBus.has_value()) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(newVolume != nullptr) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(nullptr == propertyValue) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(outPreferences) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(pos <= int(inNumberFrames)) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(proc != nullptr) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(reachedOffset0) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(srcFormat.mSampleRate == destFormat.mSampleRate || mTimestampGenerator != __null) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(startingInterrupt) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(success == false) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(tapConnection.has_value()) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(track != 0) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(track != nullptr) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(ts2.mFlags & kAudioTimeStampHostTimeValid) != 0 is false]: "
- "%25s:%-5d EXCEPTION (%d) [error != noErr is false]: \"\""
- "%25s:%-5d RemoteIOClient::Start: null ionode! enable %d, valid [%d %d], connected [%d %d]"
- "%25s:%-5d Siri enabled(%d) wasEnabled(%d) force(%d)"
- "%25s:%-5d getEnhanceDialogueMovieModeSessionType(notifyOnClientFormatMismatch = %s) = %s [lastMovieModeClient = %p]"
- "%25s:%-5d runningClientCount: %d"
- "AQInternalGetOfflineBufferCompletions"
- "AQInternalPreflightOfflineRender"
- "AQInternalScheduledStart"
- "AQServer_AddPropertyListener"
- "AQServer_CheckStopFromPause"
- "AQServer_CreateTimeline"
- "AQServer_DeviceGetCurrentTime"
- "AQServer_DeviceGetNearestStartTime"
- "AQServer_DeviceTranslateTime"
- "AQServer_DisposeQueue_block_invoke"
- "AQServer_DisposeTimeline"
- "AQServer_EnqueueBuffer"
- "AQServer_EnqueueSilence"
- "AQServer_Flush"
- "AQServer_FreeBuffer"
- "AQServer_GetParameter"
- "AQServer_GetPendingCallbackMessages"
- "AQServer_GetProperty"
- "AQServer_GetPropertySize"
- "AQServer_MixerConnectQueue_block_invoke"
- "AQServer_MixerDispose"
- "AQServer_MixerGetProperty"
- "AQServer_MixerGetPropertySize"
- "AQServer_MixerNew"
- "AQServer_MixerReset"
- "AQServer_MixerSetProperty"
- "AQServer_Pause_block_invoke"
- "AQServer_Prime_block_invoke"
- "AQServer_ProcessingTapDispose"
- "AQServer_ProcessingTapInit"
- "AQServer_ProcessingTapNew"
- "AQServer_ProcessingTapPerformReply"
- "AQServer_ProcessingTapRetrieveInfo"
- "AQServer_QueueGetCurrentTime"
- "AQServer_RemovePropertyListener"
- "AQServer_Reset"
- "AQServer_ScaleOrUnscaleSampleTime"
- "AQServer_ScheduleParameters"
- "AQServer_SetOfflineRenderFormat_block_invoke"
- "AQServer_SetParameter"
- "AQServer_SetProperty"
- "AQServer_Start_block_invoke"
- "AQServer_Stop_block_invoke"
- "AddPropertyListener"
- "AssignToSubmixTap_block_invoke"
- "AudioQueueCheckSpatializationAfterRouteChange"
- "AudioQueueDeassignFromSubmixTap_block_invoke"
- "AudioQueueInternalDeliverProcessingNodeEvents"
- "AudioQueueInternalNotifyRunning"
- "AudioQueueInternalPause"
- "AudioQueueInternalReleasePlayResources"
- "AudioQueueInternalStop_Sync_block_invoke"
- "AudioQueueNotifyReadyToRestart"
- "AudioQueueSiriListeningPropertyChanged_block_invoke"
- "Couldn't find AOP device so we can't check if we should register VT handler or not. SiriPref(%d), SiriVTPref(%d)"
- "CreateTimeline"
- "DebugPrint"
- "DeviceGetCurrentTime"
- "DeviceGetNearestStartTime"
- "DeviceIsRunning"
- "DeviceTranslateTime"
- "DisposeQueue_block_invoke"
- "DisposeTimeline"
- "Flush"
- "GetCurrentTime"
- "GetMaxIOBufferFrameSize"
- "GetNearestStartTime"
- "GetParameter"
- "GetPendingCallbackMessages"
- "GetProperty"
- "GetPropertySize"
- "GetSampleRate"
- "GetStreamFormat"
- "GetTotalNumberChannels"
- "HandleAQGetParameter"
- "HandleAQGetProperty"
- "HandleAQScheduledParameters"
- "HandleAQSetParameter"
- "HandleAQSetProperty"
- "Impl_AllocateBuffer"
- "Impl_MixerRender"
- "Impl_ProcessingTapGetSourceAudio"
- "LatencySamples"
- "MapSharedBuffers"
- "Mismatch detected at startup between SiriVTPref and AOP state. SiriPref(%d), SiriVTPref(%d), aopConfig(%d), aopEnabled(%d)"
- "MixerConnectQueue_block_invoke"
- "MixerDispose"
- "MixerGetProperty"
- "MixerGetPropertySize"
- "MixerNew"
- "MixerRender"
- "MixerReset"
- "MixerSetProperty"
- "NewQueue"
- "Pause_block_invoke"
- "Prime_block_invoke"
- "ProcessingNodeDispose"
- "ProcessingNodeInstantiate"
- "ProcessingTapDispose"
- "ProcessingTapInit"
- "ProcessingTapNew"
- "QueueGetCurrentTime"
- "RemovePropertyListener"
- "ScaleOrUnscaleSampleTime"
- "SetAudioQueue_block_invoke"
- "SetOfflineRenderFormat_block_invoke"
- "SetParameter"
- "SetRoutingBehavior"
- "SetTopologyFlags"
- "StartIO_Primitive"
- "Start_block_invoke"
- "Stop_block_invoke"
- "SystemSoundsAndHaptics"
- "TranslateTime"
- "_InternalDispose_block_invoke"
- "bluetoothUserHeadTrackingModeForBundleID"
- "bluetoothUserSpatialModeForBundleID"
- "calibrationData"
- "customHRTFMode"
- "dynamicLatency"
- "enableHeadTrackingMode"
- "getHeadTracker"
- "getHeadTrackingSupport"
- "hasDefaultOutputSpeakerPort"
- "heySiriEnabled"
- "setClockDevice"
- "setSpatialStreamInfo"
- "setVolumeScalar"
- "unavailable"
- "volumeScalar"
- "volumeScalarMappedToHWCurve"
- "{AQMESession=\"mProcessID\"i\"mSessionID\"I\"mSourceSessionID\"{optional<unsigned int>=\"\"(?=\"__null_state_\"c\"__val_\"I)\"__engaged_\"B}\"mSubsessionRef\"{ObjectRef<const void *>=\"mCFObject\"^v}\"mSubsessionID\"Q\"mDescription\"{basic_string<char, std::char_traits<char>, std::allocator<char>>=\"__r_\"{__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=\"__value_\"{__rep=\"\"(?=\"__s\"{__short=\"__data_\"[23c]\"__padding_\"[0C]\"__size_\"b7\"__is_long_\"b1}\"__l\"{__long=\"__data_\"*\"__size_\"Q\"__cap_\"b63\"__is_long_\"b1}\"__r\"{__raw=\"__words\"[3Q]})}}}\"mOneWordID\"i\"mBundleID\"{optional<applesauce::CF::StringRef>=\"\"(?=\"__null_state_\"c\"__val_\"{StringRef=\"mObject\"{ObjectRef<const __CFString *>=\"mCFObject\"^{__CFString}}})\"__engaged_\"B}}"
- "~AQRemoteClient"
- "~RemoteClient"

```
