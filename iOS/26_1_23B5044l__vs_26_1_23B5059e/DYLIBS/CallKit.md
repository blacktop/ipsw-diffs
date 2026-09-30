## CallKit

> `/System/Library/Frameworks/CallKit.framework/CallKit`

```diff

-1367.200.12.0.0
-  __TEXT.__text: 0x68598
-  __TEXT.__auth_stubs: 0x940
-  __TEXT.__objc_methlist: 0x900c
+1367.200.41.0.0
+  __TEXT.__text: 0x67d5c
+  __TEXT.__auth_stubs: 0x960
+  __TEXT.__objc_methlist: 0x8fec
   __TEXT.__const: 0x120
-  __TEXT.__cstring: 0x6300
-  __TEXT.__oslogstring: 0x36eb
+  __TEXT.__cstring: 0x62ad
+  __TEXT.__oslogstring: 0x36c6
   __TEXT.__gcc_except_tab: 0x778
-  __TEXT.__unwind_info: 0x1cc8
+  __TEXT.__unwind_info: 0x1cb0
   __TEXT.__objc_classname: 0x1471
-  __TEXT.__objc_methname: 0x11b1f
-  __TEXT.__objc_methtype: 0x3de8
+  __TEXT.__objc_methname: 0x11ae7
+  __TEXT.__objc_methtype: 0x3e0e
   __TEXT.__objc_stubs: 0xaa60
   __DATA_CONST.__got: 0x4e0
   __DATA_CONST.__const: 0xd40

   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x1f0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x33e8
+  __DATA_CONST.__objc_selrefs: 0x33e0
   __DATA_CONST.__objc_protorefs: 0xb8
   __DATA_CONST.__objc_superrefs: 0x370
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__auth_got: 0x4b0
+  __AUTH_CONST.__auth_got: 0x4c0
   __AUTH_CONST.__const: 0x580
-  __AUTH_CONST.__cfstring: 0x42a0
-  __AUTH_CONST.__objc_const: 0xebe0
+  __AUTH_CONST.__cfstring: 0x42e0
+  __AUTH_CONST.__objc_const: 0xec00
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH.__objc_data: 0x1c20
-  __DATA.__objc_ivar: 0x91c
+  __DATA.__objc_ivar: 0x920
   __DATA.__data: 0x1740
   __DATA.__bss: 0x110
   __DATA_DIRTY.__objc_data: 0xb40

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 5F00DD1E-80E0-3234-9217-FC1D05A5A5BE
-  Functions: 3187
-  Symbols:   10416
-  CStrings:  4695
+  UUID: 8AFB1AD1-26B0-3AF0-8328-235E4EDBFA98
+  Functions: 3179
+  Symbols:   10397
+  CStrings:  4699
 
Symbols:
+ -[CXCallUpdate setShouldSilentlyRegisterIMAVCall:]
+ -[CXCallUpdate shouldSilentlyRegisterIMAVCall]
+ _OBJC_IVAR_$_CXCallUpdate._shouldSilentlyRegisterIMAVCall
+ ___49-[CXCallSource reportCallWithUUID:updated:reply:]_block_invoke.21
+ ___49-[CXCallSource reportCallWithUUID:updated:reply:]_block_invoke.22
+ ___50-[CXCallSource actionCompleted:completionHandler:]_block_invoke.98
+ ___50-[CXCallSource actionCompleted:completionHandler:]_block_invoke.99
+ ___53-[CXCallSource requestTransaction:completionHandler:]_block_invoke.91
+ ___53-[CXCallSource requestTransaction:completionHandler:]_block_invoke.92
+ ___57-[CXCallSource reportAudioFinishedForCallWithUUID:reply:]_block_invoke.62
+ ___57-[CXCallSource reportAudioFinishedForCallWithUUID:reply:]_block_invoke.63
+ ___60-[CXCallSource reportCallWithUUID:receivedDTMFUpdate:reply:]_block_invoke.28
+ ___60-[CXCallSource reportCallWithUUID:receivedDTMFUpdate:reply:]_block_invoke.32
+ ___60-[CXCallSource reportCallWithUUID:receivedDTMFUpdate:reply:]_block_invoke.33
+ ___62-[CXProvider reportNewIncomingCallWithUUID:update:completion:]_block_invoke.162
+ ___65-[CXCallSource reportOutgoingCallWithUUID:connectedAtDate:reply:]_block_invoke.56
+ ___65-[CXCallSource reportOutgoingCallWithUUID:connectedAtDate:reply:]_block_invoke.57
+ ___70-[CXCallSource reportOutgoingCallWithUUID:sentInvitationAtDate:reply:]_block_invoke.44
+ ___70-[CXCallSource reportOutgoingCallWithUUID:sentInvitationAtDate:reply:]_block_invoke.45
+ ___72-[CXCallSource reportCallWithUUID:changedMeterLevel:forDirection:reply:]_block_invoke.74
+ ___72-[CXCallSource reportCallWithUUID:changedMeterLevel:forDirection:reply:]_block_invoke.75
+ ___73-[CXCallSource reportOutgoingCallWithUUID:startedConnectingAtDate:reply:]_block_invoke.50
+ ___73-[CXCallSource reportOutgoingCallWithUUID:startedConnectingAtDate:reply:]_block_invoke.51
+ ___75-[CXCallSource reportCallWithUUID:changedFrequencyData:forDirection:reply:]_block_invoke.68
+ ___75-[CXCallSource reportCallWithUUID:changedFrequencyData:forDirection:reply:]_block_invoke.69
+ ___82-[CXCallSource reportCallWithUUID:endedAtDate:privateReason:failureContext:reply:]_block_invoke.38
+ ___82-[CXCallSource reportCallWithUUID:endedAtDate:privateReason:failureContext:reply:]_block_invoke.39
+ ___86-[CXCallSource reportCallWithUUID:crossDeviceIdentifier:changedBytesOfDataUsed:reply:]_block_invoke.81
+ ___86-[CXCallSource reportCallWithUUID:crossDeviceIdentifier:changedBytesOfDataUsed:reply:]_block_invoke.82
+ ___block_literal_global.35
+ ___block_literal_global.41
+ ___block_literal_global.47
+ ___block_literal_global.53
+ ___block_literal_global.59
+ ___block_literal_global.65
+ ___block_literal_global.71
+ ___block_literal_global.77
+ __os_signpost_emit_with_name_impl
+ _objc_msgSend$setShouldSilentlyRegisterIMAVCall:
+ _objc_msgSend$shouldSilentlyRegisterIMAVCall
+ _os_signpost_enabled
- -[CXCallSource reportNewIncomingProtectedIMAVCallWithUUID:update:reply:]
- -[CXCallSource reportNewIncomingProtectedIMAVCallWithUUID:update:reply:].cold.1
- -[CXCallSource reportNewIncomingProtectedIMAVCallWithUUID:update:reply:].cold.2
- -[CXCallSource reportNewIncomingProtectedIMAVCallWithUUID:update:reply:].cold.3
- -[CXCallSourceManager callSource:reportedNewIncomingProtectedIMAVCallWithUUID:update:completion:]
- -[CXProvider reportNewIncomingProtectedIMAVCallWithUUID:update:completion:]
- ___49-[CXCallSource reportCallWithUUID:updated:reply:]_block_invoke.24
- ___49-[CXCallSource reportCallWithUUID:updated:reply:]_block_invoke.25
- ___50-[CXCallSource actionCompleted:completionHandler:]_block_invoke.100
- ___50-[CXCallSource actionCompleted:completionHandler:]_block_invoke.101
- ___53-[CXCallSource requestTransaction:completionHandler:]_block_invoke.93
- ___53-[CXCallSource requestTransaction:completionHandler:]_block_invoke.94
- ___57-[CXCallSource reportAudioFinishedForCallWithUUID:reply:]_block_invoke.64
- ___57-[CXCallSource reportAudioFinishedForCallWithUUID:reply:]_block_invoke.65
- ___60-[CXCallSource reportCallWithUUID:receivedDTMFUpdate:reply:]_block_invoke.30
- ___60-[CXCallSource reportCallWithUUID:receivedDTMFUpdate:reply:]_block_invoke.34
- ___60-[CXCallSource reportCallWithUUID:receivedDTMFUpdate:reply:]_block_invoke.35
- ___62-[CXProvider reportNewIncomingCallWithUUID:update:completion:]_block_invoke.163
- ___65-[CXCallSource reportOutgoingCallWithUUID:connectedAtDate:reply:]_block_invoke.58
- ___65-[CXCallSource reportOutgoingCallWithUUID:connectedAtDate:reply:]_block_invoke.59
- ___70-[CXCallSource reportOutgoingCallWithUUID:sentInvitationAtDate:reply:]_block_invoke.46
- ___70-[CXCallSource reportOutgoingCallWithUUID:sentInvitationAtDate:reply:]_block_invoke.47
- ___72-[CXCallSource reportCallWithUUID:changedMeterLevel:forDirection:reply:]_block_invoke.76
- ___72-[CXCallSource reportCallWithUUID:changedMeterLevel:forDirection:reply:]_block_invoke.77
- ___72-[CXCallSource reportNewIncomingProtectedIMAVCallWithUUID:update:reply:]_block_invoke
- ___72-[CXCallSource reportNewIncomingProtectedIMAVCallWithUUID:update:reply:]_block_invoke.16
- ___72-[CXCallSource reportNewIncomingProtectedIMAVCallWithUUID:update:reply:]_block_invoke.17
- ___73-[CXCallSource reportOutgoingCallWithUUID:startedConnectingAtDate:reply:]_block_invoke.52
- ___73-[CXCallSource reportOutgoingCallWithUUID:startedConnectingAtDate:reply:]_block_invoke.53
- ___75-[CXCallSource reportCallWithUUID:changedFrequencyData:forDirection:reply:]_block_invoke.70
- ___75-[CXCallSource reportCallWithUUID:changedFrequencyData:forDirection:reply:]_block_invoke.71
- ___75-[CXProvider reportNewIncomingProtectedIMAVCallWithUUID:update:completion:]_block_invoke
- ___75-[CXProvider reportNewIncomingProtectedIMAVCallWithUUID:update:completion:]_block_invoke.165
- ___75-[CXProvider reportNewIncomingProtectedIMAVCallWithUUID:update:completion:]_block_invoke_2
- ___82-[CXCallSource reportCallWithUUID:endedAtDate:privateReason:failureContext:reply:]_block_invoke.40
- ___82-[CXCallSource reportCallWithUUID:endedAtDate:privateReason:failureContext:reply:]_block_invoke.41
- ___86-[CXCallSource reportCallWithUUID:crossDeviceIdentifier:changedBytesOfDataUsed:reply:]_block_invoke.83
- ___86-[CXCallSource reportCallWithUUID:crossDeviceIdentifier:changedBytesOfDataUsed:reply:]_block_invoke.84
- ___97-[CXCallSourceManager callSource:reportedNewIncomingProtectedIMAVCallWithUUID:update:completion:]_block_invoke
- ___block_literal_global.20
- ___block_literal_global.27
- ___block_literal_global.37
- ___block_literal_global.43
- ___block_literal_global.49
- ___block_literal_global.55
- ___block_literal_global.61
- ___block_literal_global.67
- ___block_literal_global.73
- ___block_literal_global.79
- _objc_msgSend$callSource:reportedNewIncomingProtectedIMAVCallWithUUID:update:completion:
- _objc_msgSend$reportNewIncomingProtectedIMAVCallWithUUID:update:reply:
CStrings:
+ " shouldSilentlyRegisterIMAVCall=%d"
+ "TB,N,V_shouldSilentlyRegisterIMAVCall"
+ "T{CXCallUpdateHasSet=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1},N,V_hasSet"
+ "_shouldSilentlyRegisterIMAVCall"
+ "reportCallWithUUIDUpdated-%{public}@"
+ "setShouldSilentlyRegisterIMAVCall:"
+ "shouldSilentlyRegisterIMAVCall"
+ "v28@0:8{CXCallUpdateHasSet=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}16"
+ "{CXCallUpdateHasSet=\"account\"b1\"activeRemoteParticipant\"b1\"remoteMember\"b1\"localizedCallerName\"b1\"localizedCallerImageURL\"b1\"emergency\"b1\"failureExpected\"b1\"supportsEmergencyFallback\"b1\"usingBaseband\"b1\"blocked\"b1\"ttyType\"b1\"supportsTTYWithVoice\"b1\"mayRequireBreakBeforeMake\"b1\"hasVideo\"b1\"isUpgradeToVideo\"b1\"audioCategory\"b1\"audioMode\"b1\"audioInterruptionProvider\"b1\"audioInterruptionOperationMode\"b1\"verificationStatus\"b1\"priority\"b1\"requiresInCallSounds\"b1\"inCallSoundRegion\"b1\"supportsHolding\"b1\"supportsGrouping\"b1\"supportsUngrouping\"b1\"supportsDTMF\"b1\"supportsDTMFUpdates\"b1\"supportsSharePlay\"b1\"supportsScreenShare\"b1\"supportsUnambiguousMultiPartyState\"b1\"supportsAddCall\"b1\"supportsSendingToVoicemail\"b1\"supportsRecording\"b1\"isUnderlyingLinksConnected\"b1\"videoStreamToken\"b1\"callTokens\"b1\"announceProviderIdentifier\"b1\"initiator\"b1\"crossDeviceIdentifier\"b1\"ISOCountryCode\"b1\"localSenderIdentityUUID\"b1\"localSenderIdentityAccountUUID\"b1\"localMemberHandleValue\"b1\"localSenderSubscriptionIdentifier\"b1\"participantGroupUUID\"b1\"remoteParticipantHandles\"b1\"otherInvitedHandles\"b1\"activeRemoteParticipantHandles\"b1\"handoffContext\"b1\"screenShareAttributes\"b1\"context\"b1\"prefersExclusiveAccessToCellularNetwork\"b1\"remoteUplinkMuted\"b1\"shouldSuppressInCallUI\"b1\"launchInBackground\"b1\"requiresAuthentication\"b1\"mutuallyExclusiveCall\"b1\"junkConfidence\"b1\"identificationCategory\"b1\"conversation\"b1\"mixesVoiceWithMedia\"b1\"prefersToPlayDuringWombat\"b1\"mediaPlaybackOnExternalDevice\"b1\"oneToOneModeEnabled\"b1\"sharingScreen\"b1\"bluetoothAudioFormat\"b1\"ignoresBluetoothDeviceUID\"b1\"serviceStatus\"b1\"transmissionMode\"b1\"accessoryButtonEventsEnabled\"b1\"sendingVideo\"b1\"hasBeenRedirected\"b1\"isKnownCaller\"b1\"filteredOutReason\"b1\"silencingUserInfo\"b1\"isReRing\"b1\"suppressRingtone\"b1\"callSubType\"b1\"supportsScreening\"b1\"supportsRecents\"b1\"screenSharingIntention\"b1\"screenSharingType\"b1\"isSharePlayCapable\"b1\"anyRemoteSupportsRequestToScreenShare\"b1\"nearbyMode\"b1\"commTrustScore\"b1\"specialUnknown\"b1\"conversationGroupUUID\"b1\"startCallMuted\"b1\"shouldSilentlyRegisterIMAVCall\"b1}"
+ "{CXCallUpdateHasSet=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}16@0:8"
- "-[CXCallSource reportNewIncomingProtectedIMAVCallWithUUID:update:reply:]"
- "-[CXProvider reportNewIncomingProtectedIMAVCallWithUUID:update:completion:]"
- "Provider %@ was asked to report a new incoming protected call with UUID: %@ update: %@"
- "T{CXCallUpdateHasSet=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1},N,V_hasSet"
- "callSource:reportedNewIncomingProtectedIMAVCallWithUUID:update:completion:"
- "reportNewIncomingProtectedIMAVCallWithUUID:update:completion:"
- "reportNewIncomingProtectedIMAVCallWithUUID:update:reply:"
- "v28@0:8{CXCallUpdateHasSet=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}16"
- "{CXCallUpdateHasSet=\"account\"b1\"activeRemoteParticipant\"b1\"remoteMember\"b1\"localizedCallerName\"b1\"localizedCallerImageURL\"b1\"emergency\"b1\"failureExpected\"b1\"supportsEmergencyFallback\"b1\"usingBaseband\"b1\"blocked\"b1\"ttyType\"b1\"supportsTTYWithVoice\"b1\"mayRequireBreakBeforeMake\"b1\"hasVideo\"b1\"isUpgradeToVideo\"b1\"audioCategory\"b1\"audioMode\"b1\"audioInterruptionProvider\"b1\"audioInterruptionOperationMode\"b1\"verificationStatus\"b1\"priority\"b1\"requiresInCallSounds\"b1\"inCallSoundRegion\"b1\"supportsHolding\"b1\"supportsGrouping\"b1\"supportsUngrouping\"b1\"supportsDTMF\"b1\"supportsDTMFUpdates\"b1\"supportsSharePlay\"b1\"supportsScreenShare\"b1\"supportsUnambiguousMultiPartyState\"b1\"supportsAddCall\"b1\"supportsSendingToVoicemail\"b1\"supportsRecording\"b1\"isUnderlyingLinksConnected\"b1\"videoStreamToken\"b1\"callTokens\"b1\"announceProviderIdentifier\"b1\"initiator\"b1\"crossDeviceIdentifier\"b1\"ISOCountryCode\"b1\"localSenderIdentityUUID\"b1\"localSenderIdentityAccountUUID\"b1\"localMemberHandleValue\"b1\"localSenderSubscriptionIdentifier\"b1\"participantGroupUUID\"b1\"remoteParticipantHandles\"b1\"otherInvitedHandles\"b1\"activeRemoteParticipantHandles\"b1\"handoffContext\"b1\"screenShareAttributes\"b1\"context\"b1\"prefersExclusiveAccessToCellularNetwork\"b1\"remoteUplinkMuted\"b1\"shouldSuppressInCallUI\"b1\"launchInBackground\"b1\"requiresAuthentication\"b1\"mutuallyExclusiveCall\"b1\"junkConfidence\"b1\"identificationCategory\"b1\"conversation\"b1\"mixesVoiceWithMedia\"b1\"prefersToPlayDuringWombat\"b1\"mediaPlaybackOnExternalDevice\"b1\"oneToOneModeEnabled\"b1\"sharingScreen\"b1\"bluetoothAudioFormat\"b1\"ignoresBluetoothDeviceUID\"b1\"serviceStatus\"b1\"transmissionMode\"b1\"accessoryButtonEventsEnabled\"b1\"sendingVideo\"b1\"hasBeenRedirected\"b1\"isKnownCaller\"b1\"filteredOutReason\"b1\"silencingUserInfo\"b1\"isReRing\"b1\"suppressRingtone\"b1\"callSubType\"b1\"supportsScreening\"b1\"supportsRecents\"b1\"screenSharingIntention\"b1\"screenSharingType\"b1\"isSharePlayCapable\"b1\"anyRemoteSupportsRequestToScreenShare\"b1\"nearbyMode\"b1\"commTrustScore\"b1\"specialUnknown\"b1\"conversationGroupUUID\"b1\"startCallMuted\"b1}"
- "{CXCallUpdateHasSet=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}16@0:8"

```
