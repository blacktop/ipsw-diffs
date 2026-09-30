## AudioToolbox

> `/System/Library/Frameworks/AudioToolbox.framework/AudioToolbox`

```diff

 1456.126.2.0.0
-  __TEXT.__text: 0x28c758
-  __TEXT.__auth_stubs: 0x3b40
+  __TEXT.__text: 0x28f17c
+  __TEXT.__auth_stubs: 0x3b90
   __TEXT.__objc_methlist: 0x1610
-  __TEXT.__const: 0x1244
-  __TEXT.__gcc_except_tab: 0x26628
-  __TEXT.__cstring: 0x1caad
-  __TEXT.__oslogstring: 0x325c2
+  __TEXT.__const: 0x125c
+  __TEXT.__gcc_except_tab: 0x2684c
+  __TEXT.__cstring: 0x1d906
+  __TEXT.__oslogstring: 0x3477f
   __TEXT.__dlopen_cstrs: 0x676
-  __TEXT.__unwind_info: 0xc068
+  __TEXT.__unwind_info: 0xc0d0
   __TEXT.__objc_classname: 0x3c0
   __TEXT.__objc_methname: 0x5653
   __TEXT.__objc_methtype: 0x426e
   __TEXT.__objc_stubs: 0x41a0
   __DATA_CONST.__got: 0xd68
-  __DATA_CONST.__const: 0x3168
+  __DATA_CONST.__const: 0x32c8
   __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1580
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0xa8
-  __DATA_CONST.__objc_arraydata: 0x348
-  __AUTH_CONST.__auth_got: 0x1db8
+  __DATA_CONST.__objc_arraydata: 0x358
+  __AUTH_CONST.__auth_got: 0x1de0
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x10670
-  __AUTH_CONST.__cfstring: 0x53e0
+  __AUTH_CONST.__cfstring: 0x5480
   __AUTH_CONST.__objc_const: 0x3a90
-  __AUTH_CONST.__objc_intobj: 0x5a0
-  __AUTH_CONST.__objc_arrayobj: 0x3f0
+  __AUTH_CONST.__objc_intobj: 0x5b8
+  __AUTH_CONST.__objc_arrayobj: 0x408
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0xa0
   __AUTH.__data: 0x30

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 9081
-  Symbols:   10677
-  CStrings:  8166
+  Functions: 9096
+  Symbols:   10698
+  CStrings:  8424
 
Symbols:
+ __ZN4APAC32ImmersiveRendererData_V2_Manager13getACLPointerERKNS_29ImmersiveRendererData_V2_ImplE
+ __ZN4APAC32ImmersiveRendererData_V2_Manager4packERNSt3__16vectorISt4byteNS1_9allocatorIS3_EEEEjRK18AudioChannelLayoutPK28ImmersiveRendererDescriptionjRKNS_8Metadata14MetadataConfigE
+ __ZN4APAC32ImmersiveRendererData_V2_Manager38getImmersiveRendererDescriptionPointerERKNS_29ImmersiveRendererData_V2_ImplE
+ __ZN4APAC32ImmersiveRendererData_V2_Manager26getNumRendererDescriptionsERKNS_29ImmersiveRendererData_V2_ImplE
+ __ZN4APAC32ImmersiveRendererData_V2_Manager14getACLByteSizeERKNS_29ImmersiveRendererData_V2_ImplE
CStrings:
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(_channelIDsToBeDetached.size() == 0) != 0 is false]: "
+ "AQServer_DeviceGetNearestStartTime"
+ "CinematicAudioAmbienceLoudness"
+ "AQServer_CreateTimeline"
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(IONodeClientCount() < 2) != 0 is false]: "
+ "AQServer_SetParameter"
+ "AQServer_DeviceGetCurrentTime"
+ "%!s(MISSING):%!d(MISSING) %!s(MISSING): could not get gain from codec, error %!d(MISSING) (%!s(MISSING))"
+ "customHRTFMode"
+ "AQServer_ScheduleParameters"
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(!\"Attempted to add same channel ID twice\") != 0 is false]: "
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(!\"SHOULD NOT BE RECEIVING REC-STATE-DID-CHANGE NOTIFICATIONS\") != 0 is false]: "
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(!audio || _audioRunningCount > 0) != 0 is false]: "
+ "AQServer_Prime_block_invoke"
+ "MixerGetProperty"
+ "SetOfflineRenderFormat_block_invoke"
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(_startCount > 0 && _startCount < 3) != 0 is false]: "
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(!stopping()) != 0 is false]: "
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(foundUserEvent == true) != 0 is false]: "
+ "CinematicAudioDialogLoudness"
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(clientsWithProcess != _processIndexMap.end()) != 0 is false]: "
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(tapConnection.has_value()) != 0 is false]: "
+ "HandleAQSetProperty"
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(!\"Attempted to add same instance ID twice\") != 0 is false]: "
+ "SetParameter"
+ "AQServer_ProcessingTapRetrieveInfo"
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(_startCount == 0) != 0 is false]: "
+ "%!s(MISSING):%!d(MISSING) error %!d(MISSING) setting output element count for cinematic audio unit."
+ "SetRoutingBehavior"
+ "AQServer_ProcessingTapInit"
+ "StartIO_Primitive"
+ "AQInternalPreflightOfflineRender"
+ "volumeScalarMappedToHWCurve"
+ "%!s(MISSING):%!d(MISSING) error %!d(MISSING) setting cinematic audio unit property strip."
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(ioSize == sizeof(double)) != 0 is false]: "
+ "DeviceGetNearestStartTime"
+ "Stop_block_invoke"
+ "ProcessingNodeInstantiate"
+ "AQServer_QueueGetCurrentTime"
+ "DebugPrint"
+ "separate_and_remix.austrip"
+ "calibrationData"
+ "DeviceGetCurrentTime"
+ "DisposeQueue_block_invoke"
+ "GetTotalNumberChannels"
+ "CreateTimeline"
+ "AudioQueueDeassignFromSubmixTap_block_invoke"
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(ioPackets <= mInputNumPackets) != 0 is false]: "
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(frameOffset < (SInt32)numFrames) != 0 is false]: "
+ "AQServer_RemovePropertyListener"
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(!\"Unknown property\") != 0 is false]: "
+ "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)) [error != noErr is false]: \"\""
+ "MixerConnectQueue_block_invoke"
+ "AQServer_Reset"
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(mNumAllocatedSlices == 0) != 0 is false]: "
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(!submixToConnect.mIsTapSubmix && !mainSubmix.mIsTapSubmix) != 0 is false]: "
+ "QueueGetCurrentTime"
+ "GetParameter"
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(newVolume != nullptr) != 0 is false]: "
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(it != mSubmixGraph->mMixerChannels.end()) != 0 is false]: "
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(!running()) != 0 is false]: "
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(mSSSClientEntryRunningCount != 0) != 0 is false]: "
+ "MixerNew"
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(clientID != 9999999) != 0 is false]: "
+ "~RemoteClient"
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(AudioTapUtilities::CanTapPhase(tapSpecifier())) != 0 is false]: "
+ "GetPropertySize"
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(outPreferences) != 0 is false]: "
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(!mIsTapSubmix) != 0 is false]: "
+ "AudioQueueSiriListeningPropertyChanged_block_invoke"
+ "hasDefaultOutputSpeakerPort"
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(_state != Uninitialized || inState == Stopped) != 0 is false]: "
+ "getHeadTrackingSupport"
+ "AQServer_CheckStopFromPause"
+ "AssignToSubmixTap_block_invoke"
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(IsInput()) != 0 is false]: "
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(inChannels.size() <= mChannelStatus.size()) != 0 is false]: "
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(!BypassAudioSession() || IsTap()) != 0 is false]: "
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(!mIsTapSubmix && channel->GetSubmixGraph() == nullptr) != 0 is false]: "
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(mActivePriorityClientCountMap[HapticPlayerPriority::MediumPriority] != 0) != 0 is false]: "
+ "Prime_block_invoke"
+ "DeviceIsRunning"
+ "MapSharedBuffers"
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(!\"Unexpected Property ID\") != 0 is false]: "
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(mTapSources.empty()) != 0 is false]: "
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(mClientInfo != __null) != 0 is false]: "
+ "bluetoothUserSpatialModeForBundleID"
+ "%!s(MISSING):%!d(MISSING) error %!d(MISSING) getting output element count property info for cinematic audio unit."
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(ioByteSize <= mInputNumBytes) != 0 is false]: "
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(err == noErr) != 0 is false]: "
+ "AQServer_Pause_block_invoke"
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(entry->stopped()) != 0 is false]: "
+ "t8140"
+ "%!s(MISSING):%!d(MISSING) error %!d(MISSING) setting cinematic audio unit property strip resource path."
+ "GetMaxIOBufferFrameSize"
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(!mIsTapSubmix && channel->GetSubmixGraph() == this) != 0 is false]: "
+ "AQServer_EnqueueBuffer"
+ "AQServer_GetParameter"
+ "ScaleOrUnscaleSampleTime"
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(inID != kAudioQueueParam_PlayRate2) != 0 is false]: "
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(id < (1UL << 31)) != 0 is false]: "
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(_state == Uninitialized) != 0 is false]: "
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(e->mNumberParameters == 1) != 0 is false]: "
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(!haptics || _hapticsRunningCount > 0) != 0 is false]: "
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(ts2.mFlags & kAudioTimeStampHostTimeValid) != 0 is false]: "
+ "CinematicAudioBypass"
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [((client.GetTopologyFlags() & kAudioQueueFlag_HardwarePassthrough) != 0) != 0 is false]: "
+ "CinematicAudioRemixAmount"
+ "AQServer_Start_block_invoke"
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(mActivePriorityClientCountMap[HapticPlayerPriority::HighPriority] != 0) != 0 is false]: "
+ "%!s(MISSING):%!d(MISSING) error %!d(MISSING) setting input element count for cinematic audio unit."
+ "AQInternalGetOfflineBufferCompletions"
+ "NewQueue"
+ "HandleAQGetProperty"
+ "HandleAQGetParameter"
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(_IDBeingStarted == kNoSequenceID) != 0 is false]: "
+ "AQServer_ProcessingTapDispose"
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(mActiveHighPowerHapticsClients >= 0) != 0 is false]: "
+ "LatencySamples"
+ "AQServer_MixerDispose"
+ "AudioQueueCheckSpatializationAfterRouteChange"
+ "setClockDevice"
+ "Flush"
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(false) != 0 is false]: "
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(srcFormat.mSampleRate == destFormat.mSampleRate || mTimestampGenerator != __null) != 0 is false]: "
+ "CinematicAudioAmbienceLevel"
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(!BypassAudioSession()) != 0 is false]: "
+ "AudioQueueInternalStop_Sync_block_invoke"
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(cm == __null) != 0 is false]: "
+ "GetProperty"
+ "GetPendingCallbackMessages"
+ "AQServer_AddPropertyListener"
+ "AQServer_DisposeQueue_block_invoke"
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(__objc_no != success) != 0 is false]: "
+ "DeviceTranslateTime"
+ "CinematicAudioRecordingLoudness"
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(abl->mNumberBuffers == outputBuffers->mNumberBuffers) != 0 is false]: "
+ "%!s(MISSING):%!d(MISSING) error %!d(MISSING) setting cinematic audio unit austrip."
+ "AQServer_DisposeTimeline"
+ "TranslateTime"
+ "%!s(MISSING):%!d(MISSING) error %!d(MISSING) setting cinematic audio unit dsp graph text path."
+ "AQInternalScheduledStart"
+ "Impl_AllocateBuffer"
+ "AQServer_ProcessingTapPerformReply"
+ "HandleAQSetParameter"
+ "~AQRemoteClient"
+ "AQServer_MixerGetPropertySize"
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(reachedOffset0) != 0 is false]: "
+ "AQServer_Flush"
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(success == false) != 0 is false]: "
+ "%!s(MISSING)/RegattaTimer.caf"
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(track != nullptr) != 0 is false]: "
+ "bluetoothUserHeadTrackingModeForBundleID"
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(__null != mCPMSSharedInstanceForHaptics) != 0 is false]: "
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(startingInterrupt) != 0 is false]: "
+ "AQServer_GetPendingCallbackMessages"
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(activeSoundInfo != nullptr) != 0 is false]: "
+ "ProcessingTapDispose"
+ "AudioQueueInternalReleasePlayResources"
+ "AQServer_MixerReset"
+ "AddPropertyListener"
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(_IDBeingStarted == kNoSequenceID || _IDBeingStarted == inID) != 0 is false]: "
+ "_InternalDispose_block_invoke"
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(keyrange.mHigh == keyrange.mLow) != 0 is false]: "
+ "dynamicLatency"
+ "%!s(MISSING):%!d(MISSING) error %!d(MISSING) getting input element count property info for cinematic audio unit."
+ "separate_and_remix.propstrip"
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(ioBufferList.mNumberBuffers == mRampBufferList->GetNumberBuffers()) != 0 is false]: "
+ "MixerRender"
+ "DisposeTimeline"
+ "setSpatialStreamInfo"
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(mAudioOutput != nullptr) != 0 is false]: "
+ "APACImmersiveRendererDataV2.h"
+ "AQServer_MixerGetProperty"
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(pos <= int(inNumberFrames)) != 0 is false]: "
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(destABL.mBuffers[0].mDataByteSize >= inNumberFrames * mOutputFormat.mBytesPerFrame) != 0 is false]: "
+ "AQServer_ScaleOrUnscaleSampleTime"
+ "ProcessingTapNew"
+ "CinematicAudioDialogLevel"
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(mDestinationGraph == nullptr && !mIsTapSubmix) != 0 is false]: "
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(proc != nullptr) != 0 is false]: "
+ "volumeScalar"
+ "AQServer_MixerSetProperty"
+ "AVAudioSessionModeSpatialCapture"
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(0 != (client.GetTopologyFlags() & kAudioQueueFlag_IsPhaseAQIONodeClient)) != 0 is false]: "
+ "%!s(MISSING)AUDSPGraph_CinematicAudio: "
+ "MixerReset"
+ "cinematic-audio-enabled"
+ "/Library/Audio/Tunings/Generic/CinematicSeparation/shared"
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(!mIsServer) != 0 is false]: "
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(clientAudioOutput != nullptr) != 0 is false]: "
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(!mInitialized) != 0 is false]: "
+ "separate_and_remix.dspg"
+ "Impl_ProcessingTapGetSourceAudio"
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(!haptics || _hapticsPrewarmCount > 0) != 0 is false]: "
+ "GetSampleRate"
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(mClientRunMode != kRunMode_NotRunning) != 0 is false]: "
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(mDestinationTaps.empty()) != 0 is false]: "
+ "AQServer_SetProperty"
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(inState != Starting || _state == Stopped) != 0 is false]: "
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(mBufferMemory == __null) != 0 is false]: "
+ "SetTopologyFlags"
+ "AQServer_EnqueueSilence"
+ "AudioQueueInternalPause"
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(mActivePriorityClientCountMap[HapticPlayerPriority::ExclusivePriority] != 0) != 0 is false]: "
+ "Impl_MixerRender"
+ "AQServer_DeviceTranslateTime"
+ "getHeadTracker"
+ "MixerDispose"
+ "RemovePropertyListener"
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(nullptr == propertyValue) != 0 is false]: "
+ "%!s(MISSING):%!d(MISSING) error %!d(MISSING) setting cinematic audio unit input format"
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(e->mParams[i].mID != kAudioQueueParam_PlayRate2) != 0 is false]: "
+ "SetAudioQueue_block_invoke"
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(__null != gUserList) != 0 is false]: "
+ "GetStreamFormat"
+ "AQServer_Stop_block_invoke"
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(mSynthRingBuffer != nullptr) != 0 is false]: "
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(mIsServer) != 0 is false]: "
+ "AQServer_SetOfflineRenderFormat_block_invoke"
+ "MixerGetPropertySize"
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(currentBufferOffset <= int(inNumberFrames)) != 0 is false]: "
+ "HandleAQScheduledParameters"
+ "GetCurrentTime"
+ "%!s(MISSING):%!d(MISSING) %!s(MISSING): could not set loudness, error %!d(MISSING) (%!s(MISSING))"
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(!\"Bad property size\") != 0 is false]: "
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(mBufferCapacity == 0 || nBytes <= mBufferCapacity) != 0 is false]: "
+ "AQServer_MixerConnectQueue_block_invoke"
+ "computedWrapperByteSize"
+ "AQServer_FreeBuffer"
+ "Pause_block_invoke"
+ "inIRD.mVersion == kIRDVersion"
+ "setVolumeScalar"
+ "AQServer_ProcessingTapNew"
+ "SpatialCapture"
+ "AQServer_GetPropertySize"
+ "Start_block_invoke"
+ "/Library/Audio/Tunings/Generic/CinematicSeparation/Tunings"
+ "AudioQueueInternalDeliverProcessingNodeEvents"
+ "ProcessingTapInit"
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(it != mInputStates.end()) != 0 is false]: "
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(track != 0) != 0 is false]: "
+ "AudioQueueInternalNotifyRunning"
+ "enableHeadTrackingMode"
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(mixerBus.has_value()) != 0 is false]: "
+ "AudioQueueNotifyReadyToRestart"
+ "AQServer_GetProperty"
+ "GetNearestStartTime"
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(inAudioToken) != 0 is false]: "
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(mHapticOutput != nullptr) != 0 is false]: "
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(!audio || _audioPrewarmCount > 0) != 0 is false]: "
+ "MixerSetProperty"
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [((((1 && !0) && !0 && !0) && !CASIsDarwinOS())) != 0 is false]: "
+ "ProcessingNodeDispose"
+ "AQServer_MixerNew"
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(it != mMixerChannels.end()) != 0 is false]: "
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(!isRunning()) != 0 is false]: "
+ "support_secure_platform_t8140"
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(_initCount > 0) != 0 is false]: "
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(_stoppedDuringFlush == false) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE: "
- "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)): \"\""

```
