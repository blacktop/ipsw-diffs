## AudioToolbox

> `/System/Library/Frameworks/AudioToolbox.framework/AudioToolbox`

```diff

-1456.210.0.0.0
-  __TEXT.__text: 0x28f948
-  __TEXT.__auth_stubs: 0x3b90
-  __TEXT.__objc_methlist: 0x1610
-  __TEXT.__const: 0x126c
-  __TEXT.__gcc_except_tab: 0x268c0
-  __TEXT.__cstring: 0x1d997
-  __TEXT.__oslogstring: 0x349d4
+1456.336.30.1.0
+  __TEXT.__text: 0x292f3c
+  __TEXT.__auth_stubs: 0x3bb0
+  __TEXT.__objc_methlist: 0x1658
+  __TEXT.__const: 0x127c
+  __TEXT.__gcc_except_tab: 0x26d7c
+  __TEXT.__cstring: 0x1ce6b
+  __TEXT.__oslogstring: 0x33169
   __TEXT.__dlopen_cstrs: 0x676
-  __TEXT.__unwind_info: 0xc0f0
+  __TEXT.__unwind_info: 0xc240
   __TEXT.__objc_classname: 0x3c0
-  __TEXT.__objc_methname: 0x5658
-  __TEXT.__objc_methtype: 0x426e
-  __TEXT.__objc_stubs: 0x41c0
-  __DATA_CONST.__got: 0xd70
-  __DATA_CONST.__const: 0x32c8
+  __TEXT.__objc_methname: 0x5700
+  __TEXT.__objc_methtype: 0x42fb
+  __TEXT.__objc_stubs: 0x4200
+  __DATA_CONST.__got: 0xd78
+  __DATA_CONST.__const: 0x32a8
   __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1588
+  __DATA_CONST.__objc_selrefs: 0x15a8
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0xa8
+  __DATA_CONST.__objc_superrefs: 0xb0
   __DATA_CONST.__objc_arraydata: 0x358
-  __AUTH_CONST.__auth_got: 0x1de0
+  __AUTH_CONST.__auth_got: 0x1df0
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x10670
-  __AUTH_CONST.__cfstring: 0x5500
-  __AUTH_CONST.__objc_const: 0x3a90
+  __AUTH_CONST.__const: 0x10950
+  __AUTH_CONST.__cfstring: 0x5540
+  __AUTH_CONST.__objc_const: 0x3b38
   __AUTH_CONST.__objc_intobj: 0x5b8
   __AUTH_CONST.__objc_arrayobj: 0x408
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0xa0
   __AUTH.__data: 0x30
-  __DATA.__objc_ivar: 0x1f8
+  __DATA.__objc_ivar: 0x204
   __DATA.__data: 0x7f8
-  __DATA.__bss: 0x1fe1
+  __DATA.__bss: 0x20c1
   __DATA_DIRTY.__objc_data: 0x730
   __DATA_DIRTY.__data: 0x48
   __DATA_DIRTY.__bss: 0x2a70

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 9099
-  Symbols:   10702
-  CStrings:  8441
+  Functions: 9187
+  Symbols:   10794
+  CStrings:  8250
 
Symbols:
+ _AUVoiceIOSpeechActivityEventKey
+ __ZNSt3__118condition_variable10notify_allEv
+ _kTCCServiceMicrophoneInjection
+ _tcc_credential_singleton_for_self
CStrings:
+ "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE: "
+ "%!s(MISSING):%!d(MISSING) AudioSessionServer does not implement getSourceProcessAuditToken"
+ "%!s(MISSING):%!d(MISSING) AudioToolboxServerMixToTelephonyUplink; -> injectionMode: %!s(MISSING), session id: 0x%!x(MISSING)"
+ "%!s(MISSING):%!d(MISSING) AudioToolboxServerMixToTelephonyUplink; <- status: %!d(MISSING)"
+ "%!s(MISSING):%!d(MISSING) AudioToolboxServerRefreshMicrophoneInjectionPermissions for pid %!d(MISSING)"
+ "%!s(MISSING):%!d(MISSING) CreateMixTapToUplink(%!p(MISSING)); format: %!s(MISSING)"
+ "%!s(MISSING):%!d(MISSING) CreateMixTapToUplinkIfNeeded(%!p(MISSING)); ignoring audio format change b/c formats are equivalent. old format: %!s(MISSING), new format: %!s(MISSING)"
+ "%!s(MISSING):%!d(MISSING) CreateMixTapToUplinkIfNeeded(%!p(MISSING)); recreating mMixToUplink due to sample rate change. old format: %!s(MISSING), new format: %!s(MISSING)"
+ "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)): \"\""
+ "%!s(MISSING):%!d(MISSING) EnableMixTapToTelephonyUplink(%!p(MISSING)); Ignoring invalid audioSessionToTap = 0x%!x(MISSING)"
+ "%!s(MISSING):%!d(MISSING) EnableMixTapToTelephonyUplink(%!p(MISSING)); cannot be enabled while screen sharing!"
+ "%!s(MISSING):%!d(MISSING) EnableMixTapToTelephonyUplink(%!p(MISSING)); could not create tap. gInstance is null!"
+ "%!s(MISSING):%!d(MISSING) EnableMixTapToTelephonyUplink(%!p(MISSING)); could not create tap. mUplinkFormat is empty!"
+ "%!s(MISSING):%!d(MISSING) EnableMixTapToTelephonyUplink(%!p(MISSING)); failed to create tap"
+ "%!s(MISSING):%!d(MISSING) EnableMixTapToTelephonyUplink(%!p(MISSING)); gInstance is not initialized!"
+ "%!s(MISSING):%!d(MISSING) EnableMixTapToTelephonyUplink(%!p(MISSING)); successfully enabled tap"
+ "%!s(MISSING):%!d(MISSING) GetAudioSessionIDsToTapFromAudioSessionServer = %!s(MISSING)"
+ "%!s(MISSING):%!d(MISSING) GetAudioSessionIDsToTapFromAudioSessionServer = (none)"
+ "%!s(MISSING):%!d(MISSING) InitializeMixTapToTelephonyUplink; could not create tap. Null mUplinkStream"
+ "%!s(MISSING):%!d(MISSING) InitializeMixTapToTelephonyUplink; could not create tap. gInstance is null!"
+ "%!s(MISSING):%!d(MISSING) MixTapToUplink@%!p(MISSING)::CreateAQMETapConnector; AddRunningClient returned error = %!i(MISSING)"
+ "%!s(MISSING):%!d(MISSING) MixTapToUplink@%!p(MISSING)::CreateAQMETapConnector; created tap of session(s) %!s(MISSING) with format: %!s(MISSING)."
+ "%!s(MISSING):%!d(MISSING) MixTapToUplink@%!p(MISSING)::CreateAQMETapConnector; creating tap of session(s) %!s(MISSING) with format: %!s(MISSING)"
+ "%!s(MISSING):%!d(MISSING) MixTapToUplink@%!p(MISSING)::CreateTap; do any audio sessions bypass input mute? %!i(MISSING)"
+ "%!s(MISSING):%!d(MISSING) MixTapToUplinkHost@%!p(MISSING) IsMixTapToTelephonyUplinkDisabledByScreenSharing; mScreenSharingEnabledProvider is not set."
+ "%!s(MISSING):%!d(MISSING) MixTapToUplinkHost@%!p(MISSING) initialized speech detector: %!i(MISSING)"
+ "%!s(MISSING):%!d(MISSING) RegisterMutedSpeechActivityListener[%!p(MISSING)] listener=%!p(MISSING) asynchronousCallback=%!i(MISSING)."
+ "%!s(MISSING):%!d(MISSING) SetMixTapToTelephonyUplinkAllowedByUser(%!p(MISSING)); cannot be enabled while screen sharing!"
+ "%!s(MISSING):%!d(MISSING) SetMixToTelephonyUplink(%!p(MISSING)) cannot be enabled while screen sharing!"
+ "%!s(MISSING):%!d(MISSING) SetMixToTelephonyUplink; list of audio sessions to tap and audio format is unchanged. Number Of Sessions To Tap = %!i(MISSING)"
+ "%!s(MISSING):%!d(MISSING) SetMixToTelephonyUplink; list of audio sessions to tap is empty. Not creating tap."
+ "%!s(MISSING):%!d(MISSING) conclave launched"
+ "%!s(MISSING):%!d(MISSING) hasPermissionToMixTapToUplink; audioSessionToTap=0x%!x(MISSING) does not have permission to bypass the mic mute. Has entitlement? %!i(MISSING) Feature is enabled? %!i(MISSING)"
+ "%!s(MISSING):%!d(MISSING) hasPermissionToMixTapToUplink; the system setting to allow mix to uplink is disabled!"
+ "%!s(MISSING):%!d(MISSING) hasTCCPermissionToMixTapToUplink; an error occurred checking the kTCCServiceMicrophoneInjection permission for 0x%!x(MISSING)"
+ "%!s(MISSING):%!d(MISSING) hasTCCPermissionToMixTapToUplink; could not retrieve audit token for TCC permission check of session 0x%!x(MISSING)"
+ "%!s(MISSING):%!d(MISSING) hasTCCPermissionToMixTapToUplink; kTCCServiceMicrophoneInjection permission for 0x%!x(MISSING) was granted"
+ "%!s(MISSING):%!d(MISSING) hasTCCPermissionToMixTapToUplink; kTCCServiceMicrophoneInjection permission for 0x%!x(MISSING) was not granted"
+ "%!s(MISSING):%!d(MISSING) waiting for conclave launch"
+ "%!s(MISSING):%!d(MISSING) waiting for conclave launch timed out"
+ "%!s(MISSING)/RemoteAttentionRequest_Alert.caf"
+ "AUVoiceIOSpeechActivityEventKey"
+ "MixTapToUplinkBase"
+ "MixTapToUplinkHost.mm"
+ "MixToUplinkAPI_TCC"
+ "_conclaveLaunchCondVar"
+ "_conclaveLaunchMutex"
+ "_conclaveLaunched"
+ "conclaveLaunched"
+ "getSourceProcessAuditToken:"
+ "m2up"
+ "mixtouplink_verbose"
+ "refreshMicrophoneInjectionPermissions:"
+ "waitForConclaveLaunch"
+ "{condition_variable=\"__cv_\"{_opaque_pthread_cond_t=\"__sig\"q\"__opaque\"[40c]}}"
+ "{mutex=\"__m_\"{_opaque_pthread_mutex_t=\"__sig\"q\"__opaque\"[56c]}}"
- "%!s(MISSING):%!d(MISSING) %!s(MISSING): aq@%!p(MISSING): Missing %!u(MISSING) frames"
- "%!s(MISSING):%!d(MISSING) %!s(MISSING): aq@%!p(MISSING): Reducing frames to trim from %!l(MISSING)d to %!l(MISSING)d"
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(!\"Attempted to add same channel ID twice\") != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(!\"Attempted to add same instance ID twice\") != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(!\"Bad property size\") != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(!\"SHOULD NOT BE RECEIVING REC-STATE-DID-CHANGE NOTIFICATIONS\") != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(!\"Unexpected Property ID\") != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(!\"Unknown property\") != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(!BypassAudioSession() || IsTap()) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(!BypassAudioSession()) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(!audio || _audioPrewarmCount > 0) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(!audio || _audioRunningCount > 0) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(!haptics || _hapticsPrewarmCount > 0) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(!haptics || _hapticsRunningCount > 0) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(!isRunning()) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(!mInitialized) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(!mIsServer) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(!mIsTapSubmix && channel->GetSubmixGraph() == nullptr) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(!mIsTapSubmix && channel->GetSubmixGraph() == this) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(!mIsTapSubmix) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(!running()) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(!stopping()) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(!submixToConnect.mIsTapSubmix && !mainSubmix.mIsTapSubmix) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [((((1 && !0) && !0 && !0) && !CASIsDarwinOS())) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [((client.GetTopologyFlags() & kAudioQueueFlag_HardwarePassthrough) != 0) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(0 != (client.GetTopologyFlags() & kAudioQueueFlag_IsPhaseAQIONodeClient)) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(AudioTapUtilities::CanTapPhase(tapSpecifier())) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(IONodeClientCount() < 2) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(IsInput()) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(_IDBeingStarted == kNoSequenceID || _IDBeingStarted == inID) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(_IDBeingStarted == kNoSequenceID) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(__null != gUserList) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(__null != mCPMSSharedInstanceForHaptics) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(__objc_no != success) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(_channelIDsToBeDetached.size() == 0) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(_initCount > 0) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(_startCount == 0) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(_startCount > 0 && _startCount < 3) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(_state != Uninitialized || inState == Stopped) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(_state == Uninitialized) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(_stoppedDuringFlush == false) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(abl->mNumberBuffers == outputBuffers->mNumberBuffers) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(activeSoundInfo != nullptr) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(clientAudioOutput != nullptr) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(clientID != 9999999) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(clientsWithProcess != _processIndexMap.end()) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(cm == __null) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(currentBufferOffset <= int(inNumberFrames)) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(destABL.mBuffers[0].mDataByteSize >= inNumberFrames * mOutputFormat.mBytesPerFrame) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(e->mNumberParameters == 1) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(e->mParams[i].mID != kAudioQueueParam_PlayRate2) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(entry->stopped()) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(err == noErr) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(false) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(foundUserEvent == true) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(frameOffset < (SInt32)numFrames) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(id < (1UL << 31)) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(inAudioToken) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(inChannels.size() <= mChannelStatus.size()) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(inID != kAudioQueueParam_PlayRate2) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(inState != Starting || _state == Stopped) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(ioBufferList.mNumberBuffers == mRampBufferList->GetNumberBuffers()) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(ioByteSize <= mInputNumBytes) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(ioPackets <= mInputNumPackets) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(ioSize == sizeof(double)) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(it != mInputStates.end()) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(it != mMixerChannels.end()) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(it != mSubmixGraph->mMixerChannels.end()) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(keyrange.mHigh == keyrange.mLow) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(mActiveHighPowerHapticsClients >= 0) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(mActivePriorityClientCountMap[HapticPlayerPriority::ExclusivePriority] != 0) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(mActivePriorityClientCountMap[HapticPlayerPriority::HighPriority] != 0) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(mActivePriorityClientCountMap[HapticPlayerPriority::MediumPriority] != 0) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(mAudioOutput != nullptr) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(mBufferCapacity == 0 || nBytes <= mBufferCapacity) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(mBufferMemory == __null) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(mClientInfo != __null) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(mClientRunMode != kRunMode_NotRunning) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(mDestinationGraph == nullptr && !mIsTapSubmix) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(mDestinationTaps.empty()) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(mHapticOutput != nullptr) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(mIsServer) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(mNumAllocatedSlices == 0) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(mSSSClientEntryRunningCount != 0) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(mSynthRingBuffer != nullptr) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(mTapSources.empty()) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(mixerBus.has_value()) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(newVolume != nullptr) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(nullptr == propertyValue) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(outPreferences) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(pos <= int(inNumberFrames)) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(proc != nullptr) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(reachedOffset0) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(srcFormat.mSampleRate == destFormat.mSampleRate || mTimestampGenerator != __null) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(startingInterrupt) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(success == false) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(tapConnection.has_value()) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(track != 0) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(track != nullptr) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) ASSERTION FAILURE [(ts2.mFlags & kAudioTimeStampHostTimeValid) != 0 is false]: "
- "%!s(MISSING):%!d(MISSING) AudioToolboxServerMixToTelephonyUplink; injectionMode: %!s(MISSING), session id: 0x%!x(MISSING), status: %!d(MISSING)"
- "%!s(MISSING):%!d(MISSING) EXCEPTION (%!d(MISSING)) [error != noErr is false]: \"\""
- "%!s(MISSING):%!d(MISSING) EnableMixTapToTelephonyUplink; cannot be enabled while screen sharing!"
- "%!s(MISSING):%!d(MISSING) Ignoring invalid audioSessionToTap = 0x%!x(MISSING)"
- "%!s(MISSING):%!d(MISSING) MixTapToUplink@%!p(MISSING)::CreateTap; AddRunningClient returned error = %!i(MISSING)"
- "%!s(MISSING):%!d(MISSING) MixTapToUplink@%!p(MISSING)::CreateTap; created tap of session(s) %!s(MISSING) with format: %!s(MISSING). do any audio sessions bypass input mute? %!i(MISSING)"
- "%!s(MISSING):%!d(MISSING) MixTapToUplink@%!p(MISSING)::CreateTap; creating tap of session(s) %!s(MISSING) with format: %!s(MISSING)"
- "%!s(MISSING):%!d(MISSING) MixTapToUplink@%!p(MISSING)::FetchAndMix; discontinuityOccurredInMicTimeline"
- "%!s(MISSING):%!d(MISSING) RegisterMutedSpeechActivityListener[%!p(MISSING)] listener=%!p(MISSING)."
- "%!s(MISSING):%!d(MISSING) ReinitializeVPUplink; recreating mMixToUplink due to sample rate change. old format: %!s(MISSING), new format: %!s(MISSING)"
- "%!s(MISSING):%!d(MISSING) SetMixTapToTelephonyUplink audioSessionToTap=0x%!x(MISSING) does not have permission to bypass the mic mute. Has entitlement? %!i(MISSING) Feature is enabled? %!i(MISSING)"
- "%!s(MISSING):%!d(MISSING) SetMixTapToTelephonyUplink the system setting to allow mix to uplink is disabled!"
- "%!s(MISSING):%!d(MISSING) SetMixTapToTelephonyUplinkAllowedByUser; cannot be enabled while screen sharing!"
- "%!s(MISSING):%!d(MISSING) SetMixToTelephonyUplink cannot be enabled while screen sharing!"
- "%!s(MISSING):%!d(MISSING) SetMixToTelephonyUplink; could not create tap. Invalid audioSessionToTap = 0x%!x(MISSING)"
- "%!s(MISSING):%!d(MISSING) SetMixToTelephonyUplink; could not create tap. Null mUplinkStream"
- "%!s(MISSING):%!d(MISSING) SetMixToTelephonyUplink; could not create tap. gInstance is null!"
- "%!s(MISSING):%!d(MISSING) SetMixToTelephonyUplink; failed to create tap"
- "%!s(MISSING):%!d(MISSING) SetMixToTelephonyUplink; gInstance is not initialized!"
- "%!s(MISSING):%!d(MISSING) SetMixToTelephonyUplink; successfully enabled tap"
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
- "setClockDevice"
- "setSpatialStreamInfo"
- "setVolumeScalar"
- "volumeScalar"
- "volumeScalarMappedToHWCurve"
- "~AQRemoteClient"
- "~RemoteClient"

```
