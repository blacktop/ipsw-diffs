## BTAudioHALPlugin

> `/System/Library/Audio/Plug-Ins/HAL/BTAudioHALPlugin.driver/BTAudioHALPlugin`

```diff

-185.7.0.0.0
-  __TEXT.__text: 0x7244c
-  __TEXT.__auth_stubs: 0x12d0
-  __TEXT.__objc_stubs: 0x2640
-  __TEXT.__init_offsets: 0x9c
-  __TEXT.__objc_methlist: 0x112c
-  __TEXT.__gcc_except_tab: 0x1ecc
-  __TEXT.__const: 0x17cc
-  __TEXT.__cstring: 0x466a
-  __TEXT.__oslogstring: 0x1218a
+190.40.1.2.0
+  __TEXT.__text: 0x7f5c0
+  __TEXT.__auth_stubs: 0x12a0
+  __TEXT.__objc_stubs: 0x26e0
+  __TEXT.__init_offsets: 0xa4
+  __TEXT.__objc_methlist: 0x1144
+  __TEXT.__gcc_except_tab: 0x204c
+  __TEXT.__const: 0x1a0c
+  __TEXT.__cstring: 0x49dc
+  __TEXT.__oslogstring: 0x145de
   __TEXT.__objc_classname: 0x155
-  __TEXT.__objc_methname: 0x3cf0
-  __TEXT.__objc_methtype: 0x11bf
-  __TEXT.__unwind_info: 0x1908
+  __TEXT.__objc_methname: 0x3d9a
+  __TEXT.__objc_methtype: 0x10d5
+  __TEXT.__unwind_info: 0x1b48
   __TEXT.__eh_frame: 0x50
-  __DATA_CONST.__auth_got: 0x978
-  __DATA_CONST.__got: 0x2b8
+  __DATA_CONST.__auth_got: 0x960
+  __DATA_CONST.__got: 0x2c8
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x4410
-  __DATA_CONST.__cfstring: 0x1440
+  __DATA_CONST.__const: 0x5328
+  __DATA_CONST.__cfstring: 0x1520
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x58
-  __DATA_CONST.__objc_intobj: 0x60
-  __DATA.__objc_const: 0x1f08
-  __DATA.__objc_selrefs: 0xdc0
-  __DATA.__objc_ivar: 0x180
+  __DATA_CONST.__objc_intobj: 0x78
+  __DATA.__objc_const: 0x1f38
+  __DATA.__objc_selrefs: 0xde8
+  __DATA.__objc_ivar: 0x184
   __DATA.__objc_data: 0x410
   __DATA.__data: 0xb08
-  __DATA.__bss: 0xae90
+  __DATA.__bss: 0x21008
   __DATA.__common: 0x10
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprotobuf.dylib
-  UUID: A5E20017-9D57-3D49-B32B-542CE3E789C1
-  Functions: 2431
-  Symbols:   464
-  CStrings:  2791
+  UUID: 5434EE2D-F03F-36BF-9F66-C69B260CA043
+  Functions: 2731
+  Symbols:   463
+  CStrings:  2981
 
Symbols:
+ _OBJC_CLASS_$_NSDistributedNotificationCenter
+ _OBJC_CLASS_$_NSNotification
- _CFDataCreateCopy
- __Znwm
- _wmemchr
CStrings:
+ "#Error BTAudioXpcConnection::BTAudioMsgIdSelectInputDataSource null msg"
+ "#Error BTAudioXpcConnection::BTAudioMsgIdSelectInputDataSource null values[0]"
+ "#Error BTAudioXpcConnection::BTAudioMsgIdSelectInputDataSource null values[1]"
+ "#Error BTAudioXpcConnection::SendAMPAudioFeedbackMsg null msg"
+ "#Error BTAudioXpcConnection::SendAMPAudioFeedbackMsg null values[0]"
+ "#Error BTAudioXpcConnection::SendHeadtrackingAvailablityChanged null args"
+ "#Error BTAudioXpcConnection::SendHeadtrackingAvailablityChanged null values[0]"
+ "#Error BTAudioXpcConnection::kBTAudioMsgPropertyAmpAvgSkipDurationInSecond null msg"
+ "#Error BTAudioXpcConnection::kBTAudioMsgPropertyAmpAvgSkipDurationInSecond null values[0]"
+ "/private/var/mobile/tmp/com.apple.audiomxd/AudioCapture/"
+ "===== AMPAudioInput still building jitter, return silence ===== "
+ "A2DP Device XPC connection for UID %s connected to[ %d ] "
+ "AMPAudioInput AMP chunktype invalid"
+ "AMPAudioInput DecodeAMPacket: Bytes read too small: bytesRead %lu"
+ "AMPAudioInput DecodeAMPackets am %u, dsp %u %u %u %u, consume [%u ~ %u], decodeFL %u, ring %zu, total %zu"
+ "AMPAudioInput Destroy SessionSummary dispatched after disconnection"
+ "AMPAudioInput DspTimestampGapCheck update dispatched after disconnection"
+ "AMPAudioInput HandleProfileTransition %s => %s , reason %s， Need Transport Ready %s"
+ "AMPAudioInput IOOperationReadInput requested 0 Bytes read"
+ "AMPAudioInput Relinquishing Audio for mAudioObjectID %d"
+ "AMPAudioInput SendSessionSummary %llu, %llu, %u"
+ "AMPAudioInput SessionSummary already destroyed"
+ "AMPAudioInput Transport is %s, IO read unblocked"
+ "AMPAudioInput TriggerAudioStream: Request AMP %s "
+ "AMPAudioInput aaceldFrameSize invalid %u, trigger PLC, decoded %zu"
+ "AMPAudioInput amp remote data aaceldFrameCount invalid %u"
+ "AMPAudioInput anchor mDspTsLastEffective dspTs @ %u"
+ "AMPAudioInput build jitter done with %zu frm"
+ "AMPAudioInput build jitter drain Frame, got %zu bytes, Ring has %zu frames"
+ "AMPAudioInput check jitter, %zu frame in queue"
+ "AMPAudioInput create SessionSummary after disconnection"
+ "AMPAudioInput created SessionSummary"
+ "AMPAudioInput decode mismatch dspDecodeFL %u, dspConsumeFL %u, leftinQ %lu, expect %lu, bytesToHAL %lu"
+ "AMPAudioInput decoded less data %zu : %zu bytes"
+ "AMPAudioInput destroyed SessionSummary"
+ "AMPAudioInput deviate gap %d, DSPTs %u-%u, threshold %u"
+ "AMPAudioInput deviated audio curr %u decodeFL %u, am %u"
+ "AMPAudioInput dspTs jump @ %u vs %u"
+ "AMPAudioInput flush trigger PLC, decoded %zu, decodeFL %u, currDspTs %u, leftdata %zu, am %u"
+ "AMPAudioInput init install decoder to %p"
+ "AMPAudioInput jitter build done but no data in mRingInput"
+ "AMPAudioInput jitter exhausted: trigger PLC, decodeFL %u, ConsumeEnd %u, output %zu bytes, PCM %zu, %ust exhaust"
+ "AMPAudioInput need to decode %zu bytes"
+ "AMPAudioInput no decoder installed"
+ "AMPAudioInput send SessionSummary dispatched after disconnection"
+ "AMPAudioInput set TriggerAMPAudio : %s, codecID %u, owned %d"
+ "AMPAudioInput stream start, %zu frame in queue"
+ "AMPAudioInput timeline (re)Anchored, gap %d, dsp curr %u, consumeStart %u, decodeFL %u, amFL %u"
+ "AMPAudioInput timeline Anchored, dsp curr %u, consumeStart %u, decodeFL %u, amFL %u, PCM %zu"
+ "AMPAudioInput toHAL: dspDecodeFL %u, dspConsumeFL %u, left %lu, expect %lu, bytesToHAL %lu"
+ "AMPAudioInput: A2IPerformPropertyChange"
+ "AMPAudioInput: A2IRequestConfigChange"
+ "AMPAudioInput: BTHAL AccessoryAudio Device XPC connection for UID %s connected to[ %d ], deviceUid: %s"
+ "AMPAudioInput: GetSampleRate %f"
+ "AirPodsStudioVoiceMic"
+ "AppleAudioAccessoryDevice ClearSilenceGeneration with output device not ready"
+ "AppleAudioAccessoryDevice ConnectIODevices"
+ "AppleAudioAccessoryDevice FormatChangeRequired with output device not ready"
+ "AppleAudioAccessoryDevice FormatChangeSupported with output device not ready"
+ "AppleAudioAccessoryDevice GetDbVolume with output device not ready"
+ "AppleAudioAccessoryDevice GetDbVolumeFromScalar with output device not ready"
+ "AppleAudioAccessoryDevice GetDeviceCategory with output device not ready"
+ "AppleAudioAccessoryDevice GetLatency with input device not ready"
+ "AppleAudioAccessoryDevice GetLatency with output device not ready"
+ "AppleAudioAccessoryDevice GetMaxDbVolume with output device not ready"
+ "AppleAudioAccessoryDevice GetMinDbVolume with output device not ready"
+ "AppleAudioAccessoryDevice GetScalarVolume with output device not ready"
+ "AppleAudioAccessoryDevice GetScalarVolumeFromDb with output device not ready"
+ "AppleAudioAccessoryDevice GetScalarVolumeWithBalance with output device not ready"
+ "AppleAudioAccessoryDevice HandleTransportOnRouteChange with output device not ready"
+ "AppleAudioAccessoryDevice NotifyManualVolumeChanged with output device not ready"
+ "AppleAudioAccessoryDevice NotifyPostProfileUpdateProperty with output device not ready"
+ "AppleAudioAccessoryDevice ProcessInputAudio with output device not ready"
+ "AppleAudioAccessoryDevice Profile Transition %s => %s , reason %s, Need Transport Ready %s"
+ "AppleAudioAccessoryDevice Publishing with StudioMic %s"
+ "AppleAudioAccessoryDevice Publishing with enhancedAccessoryEQ %s"
+ "AppleAudioAccessoryDevice ResetTransition with output device not ready"
+ "AppleAudioAccessoryDevice SendDosimetrySensitivity with output device not ready"
+ "AppleAudioAccessoryDevice SendSetListenMode with output device not ready"
+ "AppleAudioAccessoryDevice SetDbVolume with output device not ready"
+ "AppleAudioAccessoryDevice SetLinkLatency with output device not ready"
+ "AppleAudioAccessoryDevice SetVolumeFromBTS with output device not ready"
+ "AppleAudioAccessoryDevice SetVolumeFromCA with output device not ready"
+ "AppleAudioAccessoryDevice StopIO on invalid input device"
+ "AppleAudioAccessoryDevice StopIO on invalid output device"
+ "AppleAudioAccessoryDevice TriggerAudioStream on invalid input device"
+ "AppleAudioAccessoryDevice TriggerAudioStream on invalid output device"
+ "AppleAudioAccessoryDevice UpdatePhysicalFormatList with output device not ready"
+ "AppleAudioAccessoryDevice UpdateSampleRate with output device not ready"
+ "AppleAudioAccessoryDevice UpdateSamplingRate with output device not ready"
+ "AppleAudioAccessoryDevice UpdateVolumeBalance with output device not ready"
+ "AppleAudioAccessoryDevice VolumeConfirmationsEnabled with output device not ready"
+ "AppleAudioAccessoryDevice XPC connection for UID %s connected to[ %d ] "
+ "AppleAudioAccessoryDevice convertScalarVolumeToDB with output device not ready"
+ "AppleAudioAccessoryDevice input device already installed"
+ "AppleAudioAccessoryDevice input startIO"
+ "AppleAudioAccessoryDevice installed %p"
+ "AppleAudioAccessoryDevice not ready to install IO device"
+ "AppleAudioAccessoryDevice output device installed to %p"
+ "AppleAudioAccessoryDevice output device not ready"
+ "AppleAudioAccessoryDevice output device startIO"
+ "AppleAudioAccessoryDevice startIO on invalid input device"
+ "AppleAudioAccessoryDevice startIO on invalid output device"
+ "AppleAudioAccessoryDevice valid check %p"
+ "AppleAudioAccessoryDevice valid check output: %p, input: %p"
+ "B56@0:8@16{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}24@48"
+ "BTAudioAccessoryDevice: mSupportedFeatureDictionary doesn't exist"
+ "BTAudioMsgIdAMPAudioFeedback"
+ "BTAudioMsgIdAMPSkipDuration"
+ "BTAudioMsgIdSelectInputDataSource"
+ "BTUnifiedAudioDevice : Sent device config change for %{public}s on %d, result %s"
+ "BTUnifiedAudioDevice : unhandled failure to send device config change for %{public}s, result %s"
+ "BTUnifiedAudioDevice: No profile/reason change for AMP [%{public}@ ] , profile %{public}s => %{public}s reason %{public}s = > %{public}s "
+ "BTUnifiedAudioDevice: [%{public}@ ] Perform Route change for AMP, profile %{public}s => %{public}s reason %{public}s = > %{public}s "
+ "Calling HeadtrackingAvailablityChanged %d on XPC from AppleAudioAccessoryDevice"
+ "Created & Initialize AMPAudioInput Device, input sharememory %zu"
+ "DSPOffload Available Options set to %@"
+ "DSPOffload Supported set to %d for mAudioObjectID %d"
+ "DSPOffload support =  %{public}s"
+ "Delayed Transport Disconnect: Disconnect Timer Fired..Disconnect CIS"
+ "Delayed Transport Disconnect: cisConnected = %d. Transport = %d"
+ "Device is already owned, still updating ownership"
+ "Device sample rate changed %f -> %f [encoder = %d, decoder = %d]"
+ "DoIOOperation not allowed right now because mAudioObjectID %d is not accepting I/O"
+ "Found box object with modelName %@ and boxUID %@ %@"
+ "GetMute"
+ "HFP Codec selected %u/%u, game %d, hid %d, sfer %d, currCodec %u"
+ "HFP Device XPC connection for UID %s connected to[ %d ] "
+ "InEarStatusPrimary"
+ "InEarStatusSecondary"
+ "Input Decode: Bytes read is 0 bytesRead %lu"
+ "IsAppleDevice"
+ "IsOwned"
+ "IsVolumeSupported"
+ "LC3"
+ "LC3 decoder init to AACELD"
+ "LEA Device XPC connection for UID %s connected to[ %d ] "
+ "LECA Device XPC connection for UID %s connected to[ %d ] "
+ "LECA StartIO CIS Already up"
+ "LECA StartIO returns %x (%llu)"
+ "LECA Starting IO on profile %{public}s, activeIO:%llu to %{public}@ mAudioObjectID: %u Wait IO Start %d"
+ "LECA StopIO %{public}s, activeIO:%llu, need immediate CIS disconnect:%d"
+ "LECA StopIO returns noErr (%llu)"
+ "LECA StopIO: failed to stop because the ref count was already 0"
+ "LECA: Codec Update completed Input = %{public}s Decoder = %d , Output = %{public}s Encoder = %d"
+ "LECA: Direction %x Stream state output = %d input = %d"
+ "LECA: Setting Supported Codecs"
+ "LECA: UpdateSamplingRate minRate %f, maxRate %f"
+ "LECA: Updating Codecs Input = %{public}s Decoder = %d , Output = %{public}s Encoder = %d"
+ "NA"
+ "Negotiated Frame Size, HAL Request : %d BTHAL Proposed %d "
+ "Not disconnecting CIS"
+ "Ready"
+ "Request For route Change to AppleAudioAccessoryDevice for ampi"
+ "Send headtracking availability changed %d"
+ "Spatial Profile Info no longer required in plugin: Trigger Release %d"
+ "Status : IO = %{public}s. CIS Up = %{public}s. Delayed Transport Disconnect: %{public}s"
+ "Stop AMPAudioInput AUDIO!"
+ "StudioMic %s"
+ "StudioMic DSPOffload Available Dict nil, return true"
+ "Ti,N,V_usbcOnlyMetricCounter"
+ "UpdateCurrentBTAudioDevice kBluetoothAudioDeviceTypeA3D returning early for virtual device"
+ "UpdateCurrentBTAudioDevice, logging for kBluetoothAudioDeviceTypeA3D"
+ "UpdateCurrentBTAudioDevice, switch to kBluetoothAudioDeviceTypeA3D"
+ "UpdateCurrentBTAudioDeviceFromSampleRate LE Connected Audio  %f = %f"
+ "Updated EnhancedAccessoryDSPEQ, begin to %s"
+ "Updated Personalized Volume DRC Coef to: %d"
+ "Updated StudioMic, begin to %s AMPAudioInput"
+ "XPC Send AMP Data Source, reason:%s codecID: %u"
+ "XPC Send AMP Metric avgFlush %u(ms)"
+ "XPC Send AMPAudioInput Audio feedback"
+ "[%{public}@] Deleting BTAudioDevice %{public}s"
+ "[%{public}@] Deleting Internal BTAudioDevice %{public}s"
+ "_usbcOnlyMetricCounter"
+ "address"
+ "airpods content creation recording"
+ "airpods noise suppression for studio mic"
+ "audioCategory"
+ "com.apple.audioaccessoryd.usageSummary.volumeChange"
+ "defaultCenter"
+ "getPropertyData: not enough space for the return value of kAudioDevicePropertyCalculateBufferFrameSize for the device"
+ "getPropertyData: not enough space for the return value of kBluetoothAudioDevicePropertyPersonalizedVolumeDRCPrslCoef"
+ "kBTAudioMsgAccessoryEnhancedDSPEQSupported"
+ "kBTAudioMsgPropertyAmpAudioFeedBack"
+ "kBTAudioMsgPropertyAmpAvgSkipDurationInSecond"
+ "kBTAudioMsgPropertyAmpCodecID"
+ "kBTAudioMsgPropertyAmpIsEnabled"
+ "kBTAudioMsgPropertyAmpRouteReason"
+ "kBTAudioMsgPropertyAmpStatus"
+ "kBTAudioMsgPropertyMaxChannels"
+ "kBTAudioMsgPropertyPersonalizedVolumeDRCCoef"
+ "kBTAudioMsgStudioMicSupported"
+ "kBTHeadtrackingAvailabilityChanged"
+ "kBluetoothAudioDeviceFeatureStudioMicInput"
+ "mDevicePropertyDSPOffloadDict update for enhancedEQ to %@"
+ "mPVDRCPrslCoef set to %d"
+ "mSupportedFeaturesDict in update doesn't exist"
+ "mUnifiedAudioDevice is null %s - returning 0"
+ "mUnifiedAudioDevice is null %s - returning false"
+ "notificationWithName:object:userInfo:"
+ "perform kBluetoothAudioDevicePropertyDeviceType, %s -> %s"
+ "postNotification:"
+ "setUsbcOnlyMetricCounter:"
+ "usbcOnlyMetricCounter"
+ "v40@0:8{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}16"
+ "v48@0:8{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}16@40"
+ "xpc_get_type(maxChannelsProp) == XPC_TYPE_INT64"
- "/private/var/mobile/tmp/com.apple.audiomxd"
- "A2DP Device XPC connection for UID %@ connected to[ %d ] "
- "Accessory mInEarStatusPrimary set to %d for mAudioObjectID %d"
- "Accessory mInEarStatusSecondary set to %u for mAudioObjectID %u"
- "AppleAudioAccessoryDevice XPC connection for UID %@ connected to[ %d ] "
- "B56@0:8@16{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}24@48"
- "BTUnifiedAudioDevice : Sending device config change for %{public}s on %d"
- "Error, did NOT find HAL device for UID: %s, handling msg\n"
- "Found USB device with modelName %@ and boxUID %@ %@"
- "HFP Device XPC connection for UID %@ connected to[ %d ] "
- "HFPStereo config no pending for hid, currCodec %u"
- "HFPStereo config no pending for sfer, currCodec %u"
- "HFPStereo config policy nopending for game"
- "HFPStereo config policy picked HAoS, currCodec %u, device %{public}s"
- "HFPStereo config policy picked high stereo for sfer, currCodec %u, device %{public}s"
- "HFPStereo config policy picked mono for hid, currCodec %u"
- "HFPStereo config policy picked mono, currCodec %u, device %{public}s, game %u, sfer %d"
- "LC3 decoder init to AACELD 48K"
- "LEA Device XPC connection for UID %@ connected to[ %d ] "
- "[%{public}@] Deleting BTAudioDevice %{public}@"
- "dsp offload support =  %{public}s"
- "mHostedDSPOffloadSupported set to %d for mAudioObjectID %d"
- "v40@0:8{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}16"
- "v48@0:8{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}16@40"

```
