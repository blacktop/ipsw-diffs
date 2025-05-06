## AudioToolbox

> `/System/Library/Frameworks/AudioToolbox.framework/AudioToolbox`

```diff

   __TEXT.__const: 0x135c
   __TEXT.__dlopen_cstrs: 0x676
   __TEXT.__gcc_except_tab: 0x284b8
-  __TEXT.__cstring: 0x1d158
-  __TEXT.__oslogstring: 0x33f3e
+  __TEXT.__cstring: 0x1dd7a
+  __TEXT.__oslogstring: 0x35dbc
   __TEXT.__unwind_info: 0xc3f8
   __TEXT.__objc_classname: 0x3c0
   __TEXT.__objc_methname: 0x5710

   - /usr/lib/libobjc.A.dylib
   Functions: 9237
   Symbols:   25588
-  CStrings:  8310
+  CStrings:  8536
 
Symbols:
+ __XGetProperty.13161
+ __XSetProperty.13160
+ ___Block_byref_object_copy_.13279
+ ___Block_byref_object_dispose_.13280
+ ____ZN2AT13DispatchBlockEP16dispatch_queue_sU13block_pointerFvvEbPKcS5_iyy_block_invoke.12541
+ ___block_descriptor_tmp.10.9853
+ ___block_descriptor_tmp.101.13285
+ ___block_descriptor_tmp.11.12542
+ ___block_descriptor_tmp.11.4202
+ ___block_descriptor_tmp.12.9860
+ ___block_descriptor_tmp.12538
+ ___block_descriptor_tmp.13291
+ ___block_descriptor_tmp.151.13282
+ ___block_descriptor_tmp.156.13281
+ ___block_descriptor_tmp.18
+ ___block_descriptor_tmp.4.9842
+ ___block_descriptor_tmp.5.9847
+ ___block_descriptor_tmp.6.9848
+ ___block_descriptor_tmp.7.9849
+ ___block_descriptor_tmp.8.9850
+ ___block_descriptor_tmp.80.13290
+ ___block_descriptor_tmp.88.13289
+ ___block_descriptor_tmp.89.13288
+ ___block_descriptor_tmp.9.2562
+ ___block_descriptor_tmp.9.9851
+ ___block_descriptor_tmp.90.13287
+ ___block_descriptor_tmp.93.13286
+ ___block_descriptor_tmp.9833
- __XGetProperty.13162
- __XSetProperty.13161
- ___Block_byref_object_copy_.13280
- ___Block_byref_object_dispose_.13281
- ____ZN2AT13DispatchBlockEP16dispatch_queue_sU13block_pointerFvvEbPKcS5_iyy_block_invoke.12542
- ___block_descriptor_tmp.10.4202
- ___block_descriptor_tmp.10.9851
- ___block_descriptor_tmp.101.13286
- ___block_descriptor_tmp.11.4203
- ___block_descriptor_tmp.11.9853
- ___block_descriptor_tmp.12.12543
- ___block_descriptor_tmp.12539
- ___block_descriptor_tmp.13.9860
- ___block_descriptor_tmp.13292
- ___block_descriptor_tmp.151.13283
- ___block_descriptor_tmp.156.13282
- ___block_descriptor_tmp.19
- ___block_descriptor_tmp.5.9842
- ___block_descriptor_tmp.6.9847
- ___block_descriptor_tmp.7.9848
- ___block_descriptor_tmp.8.9849
- ___block_descriptor_tmp.80.13291
- ___block_descriptor_tmp.88.13290
- ___block_descriptor_tmp.89.13289
- ___block_descriptor_tmp.9.9850
- ___block_descriptor_tmp.90.13288
- ___block_descriptor_tmp.93.13287
- ___block_descriptor_tmp.9834
CStrings:
+ "%25s:%-5d ASSERTION FAILURE [(!\"Attempted to add same channel ID twice\") != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(!\"Attempted to add same instance ID twice\") != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(!\"Bad property size\") != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(!\"SHOULD NOT BE RECEIVING REC-STATE-DID-CHANGE NOTIFICATIONS\") != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(!\"Unexpected Property ID\") != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(!\"Unknown property\") != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(!BypassAudioSession() || IsTap()) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(!BypassAudioSession()) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(!audio || _audioPrewarmCount > 0) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(!audio || _audioRunningCount > 0) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(!haptics || _hapticsPrewarmCount > 0) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(!haptics || _hapticsRunningCount > 0) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(!isRunning()) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(!mInitialized) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(!mIsServer) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(!mIsTapSubmix && channel->GetSubmixGraph() == nullptr) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(!mIsTapSubmix && channel->GetSubmixGraph() == this) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(!mIsTapSubmix) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(!running()) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(!stopping()) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(!submixToConnect.mIsTapSubmix && !mainSubmix.mIsTapSubmix) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [((((1 && !0) && !0 && !0) && !CASIsDarwinOS())) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [((client.GetTopologyFlags() & kAudioQueueFlag_HardwarePassthrough) != 0) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(0 != (client.GetTopologyFlags() & kAudioQueueFlag_IsPhaseAQIONodeClient)) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(AudioTapUtilities::CanTapPhase(tapSpecifier())) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(IONodeClientCount() < 2) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(IsInput()) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(_IDBeingStarted == kNoSequenceID || _IDBeingStarted == inID) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(_IDBeingStarted == kNoSequenceID) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(__null != gUserList) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(__null != mCPMSSharedInstanceForHaptics) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(__objc_no != success) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(_channelIDsToBeDetached.size() == 0) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(_initCount > 0) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(_startCount == 0) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(_startCount > 0 && _startCount < 3) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(_state != Uninitialized || inState == Stopped) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(_state == Uninitialized) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(_stoppedDuringFlush == false) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(abl->mNumberBuffers == outputBuffers->mNumberBuffers) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(activeSoundInfo != nullptr) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(clientAudioOutput != nullptr) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(clientID != 9999999) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(clientsWithProcess != _processIndexMap.end()) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(cm == __null) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(currentBufferOffset <= int(inNumberFrames)) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(destABL.mBuffers[0].mDataByteSize >= inNumberFrames * mOutputFormat.mBytesPerFrame) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(e->mNumberParameters == 1) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(e->mParams[i].mID != kAudioQueueParam_PlayRate2) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(entry->stopped()) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(err == noErr) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(false) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(foundUserEvent == true) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(frameOffset < (SInt32)numFrames) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(id < (1UL << 31)) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(inAudioToken) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(inChannels.size() <= mChannelStatus.size()) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(inID != kAudioQueueParam_PlayRate2) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(inState != Starting || _state == Stopped) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(ioBufferList.mNumberBuffers == mRampBufferList->GetNumberBuffers()) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(ioByteSize <= mInputNumBytes) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(ioPackets <= mInputNumPackets) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(ioSize == sizeof(double)) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(it != mInputStates.end()) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(it != mMixerChannels.end()) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(it != mSubmixGraph->mMixerChannels.end()) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(keyrange.mHigh == keyrange.mLow) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(mActiveHighPowerHapticsClients >= 0) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(mActivePriorityClientCountMap[HapticPlayerPriority::ExclusivePriority] != 0) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(mActivePriorityClientCountMap[HapticPlayerPriority::HighPriority] != 0) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(mActivePriorityClientCountMap[HapticPlayerPriority::MediumPriority] != 0) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(mAudioOutput != nullptr) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(mBufferCapacity == 0 || nBytes <= mBufferCapacity) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(mBufferMemory == __null) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(mClientInfo != __null) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(mClientRunMode != kRunMode_NotRunning) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(mDestinationGraph == nullptr && !mIsTapSubmix) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(mDestinationTaps.empty()) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(mHapticOutput != nullptr) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(mIsServer) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(mNumAllocatedSlices == 0) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(mSSSClientEntryRunningCount != 0) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(mSynthRingBuffer != nullptr) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(mTapSources.empty()) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(mixerBus.has_value()) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(nullptr == propertyValue) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(outPreferences) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(pos <= int(inNumberFrames)) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(proc != nullptr) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(reachedOffset0) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(srcFormat.mSampleRate == destFormat.mSampleRate || mTimestampGenerator != __null) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(startingInterrupt) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(success == false) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(tapConnection.has_value()) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(track != 0) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(track != nullptr) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(ts2.mFlags & kAudioTimeStampHostTimeValid) != 0 is false]: "
+ "%25s:%-5d EXCEPTION (%d) [error != noErr is false]: \"\""
+ "AQInternalGetOfflineBufferCompletions"
+ "AQInternalPreflightOfflineRender"
+ "AQInternalScheduledStart"
+ "AQServer_AddPropertyListener"
+ "AQServer_CheckStopFromPause"
+ "AQServer_CreateTimeline"
+ "AQServer_DeviceGetCurrentTime"
+ "AQServer_DeviceGetNearestStartTime"
+ "AQServer_DeviceTranslateTime"
+ "AQServer_DisposeQueue_block_invoke"
+ "AQServer_DisposeTimeline"
+ "AQServer_EnqueueBuffer"
+ "AQServer_EnqueueSilence"
+ "AQServer_Flush"
+ "AQServer_FreeBuffer"
+ "AQServer_GetParameter"
+ "AQServer_GetPendingCallbackMessages"
+ "AQServer_GetProperty"
+ "AQServer_GetPropertySize"
+ "AQServer_MixerConnectQueue_block_invoke"
+ "AQServer_MixerDispose"
+ "AQServer_MixerGetProperty"
+ "AQServer_MixerGetPropertySize"
+ "AQServer_MixerNew"
+ "AQServer_MixerReset"
+ "AQServer_MixerSetProperty"
+ "AQServer_Pause_block_invoke"
+ "AQServer_Prime_block_invoke"
+ "AQServer_ProcessingTapDispose"
+ "AQServer_ProcessingTapInit"
+ "AQServer_ProcessingTapNew"
+ "AQServer_ProcessingTapPerformReply"
+ "AQServer_ProcessingTapRetrieveInfo"
+ "AQServer_QueueGetCurrentTime"
+ "AQServer_RemovePropertyListener"
+ "AQServer_Reset"
+ "AQServer_ScaleOrUnscaleSampleTime"
+ "AQServer_ScheduleParameters"
+ "AQServer_SetOfflineRenderFormat_block_invoke"
+ "AQServer_SetParameter"
+ "AQServer_SetProperty"
+ "AQServer_Start_block_invoke"
+ "AQServer_Stop_block_invoke"
+ "AddPropertyListener"
+ "AssignToSubmixTap_block_invoke"
+ "AudioQueueCheckSpatializationAfterRouteChange"
+ "AudioQueueDeassignFromSubmixTap_block_invoke"
+ "AudioQueueInternalDeliverProcessingNodeEvents"
+ "AudioQueueInternalNotifyRunning"
+ "AudioQueueInternalPause"
+ "AudioQueueInternalReleasePlayResources"
+ "AudioQueueInternalStop_Sync_block_invoke"
+ "AudioQueueNotifyReadyToRestart"
+ "AudioQueueSiriListeningPropertyChanged_block_invoke"
+ "CreateTimeline"
+ "DebugPrint"
+ "DeviceGetCurrentTime"
+ "DeviceGetNearestStartTime"
+ "DeviceIsRunning"
+ "DeviceTranslateTime"
+ "DisposeQueue_block_invoke"
+ "DisposeTimeline"
+ "Flush"
+ "GetCurrentTime"
+ "GetMaxIOBufferFrameSize"
+ "GetNearestStartTime"
+ "GetParameter"
+ "GetPendingCallbackMessages"
+ "GetProperty"
+ "GetPropertySize"
+ "GetSampleRate"
+ "GetStreamFormat"
+ "GetTotalNumberChannels"
+ "HandleAQGetParameter"
+ "HandleAQGetProperty"
+ "HandleAQScheduledParameters"
+ "HandleAQSetParameter"
+ "HandleAQSetProperty"
+ "Impl_AllocateBuffer"
+ "Impl_MixerRender"
+ "Impl_ProcessingTapGetSourceAudio"
+ "LatencySamples"
+ "MapSharedBuffers"
+ "MixerConnectQueue_block_invoke"
+ "MixerDispose"
+ "MixerGetProperty"
+ "MixerGetPropertySize"
+ "MixerNew"
+ "MixerRender"
+ "MixerReset"
+ "MixerSetProperty"
+ "NewQueue"
+ "Pause_block_invoke"
+ "Prime_block_invoke"
+ "ProcessingNodeDispose"
+ "ProcessingNodeInstantiate"
+ "ProcessingTapDispose"
+ "ProcessingTapInit"
+ "ProcessingTapNew"
+ "QueueGetCurrentTime"
+ "RemovePropertyListener"
+ "ScaleOrUnscaleSampleTime"
+ "SetAudioQueue_block_invoke"
+ "SetOfflineRenderFormat_block_invoke"
+ "SetParameter"
+ "SetRoutingBehavior"
+ "SetTopologyFlags"
+ "StartIO_Primitive"
+ "Start_block_invoke"
+ "Stop_block_invoke"
+ "TranslateTime"
+ "_InternalDispose_block_invoke"
+ "bluetoothAlternateTransportMode"
+ "bluetoothUserHeadTrackingModeForBundleID"
+ "bluetoothUserSpatialModeForBundleID"
+ "calibrationData"
+ "customHRTFMode"
+ "dynamicLatency"
+ "enableHeadTrackingMode"
+ "getHeadTracker"
+ "getHeadTrackingSupport"
+ "hasDefaultOutputSpeakerPort"
+ "setClockDevice"
+ "setSpatialStreamInfo"
+ "setVolumeScalar"
+ "triggerSPENOnAlternateTransportChange"
+ "volumeScalar"
+ "volumeScalarMappedToHWCurve"
+ "~AQRemoteClient"
+ "~RemoteClient"
- "%25s:%-5d ASSERTION FAILURE: "
- "%25s:%-5d EXCEPTION (%d): \"\""

```
