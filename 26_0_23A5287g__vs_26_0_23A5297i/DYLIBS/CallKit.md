## CallKit

> `/System/Library/Frameworks/CallKit.framework/CallKit`

```diff

-1362.100.1.0.0
-  __TEXT.__text: 0x67a58
+1364.100.4.0.0
+  __TEXT.__text: 0x67ba0
   __TEXT.__auth_stubs: 0x940
-  __TEXT.__objc_methlist: 0x8fbc
+  __TEXT.__objc_methlist: 0x8fd4
   __TEXT.__const: 0x120
-  __TEXT.__cstring: 0x6200
+  __TEXT.__cstring: 0x6250
   __TEXT.__oslogstring: 0x3694
   __TEXT.__gcc_except_tab: 0x778
   __TEXT.__unwind_info: 0x1ca0
   __TEXT.__objc_classname: 0x1471
-  __TEXT.__objc_methname: 0x1193c
-  __TEXT.__objc_methtype: 0x3dc7
-  __TEXT.__objc_stubs: 0xa9c0
+  __TEXT.__objc_methname: 0x119e2
+  __TEXT.__objc_methtype: 0x3df4
+  __TEXT.__objc_stubs: 0xaa00
   __DATA_CONST.__got: 0x4e0
   __DATA_CONST.__const: 0xd40
   __DATA_CONST.__objc_classlist: 0x3f0
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x1f0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x33b0
+  __DATA_CONST.__objc_selrefs: 0x33c0
   __DATA_CONST.__objc_protorefs: 0xb8
   __DATA_CONST.__objc_superrefs: 0x370
   __DATA_CONST.__objc_arraydata: 0x18
   __AUTH_CONST.__auth_got: 0x4b0
   __AUTH_CONST.__const: 0x580
-  __AUTH_CONST.__cfstring: 0x4240
-  __AUTH_CONST.__objc_const: 0xebc0
+  __AUTH_CONST.__cfstring: 0x4280
+  __AUTH_CONST.__objc_const: 0xebf0
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH.__objc_data: 0x19a0
-  __DATA.__objc_ivar: 0x91c
+  __DATA.__objc_ivar: 0x920
   __DATA.__data: 0x1740
   __DATA.__bss: 0x110
   __DATA_DIRTY.__objc_data: 0xdc0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 6558D23F-D1B1-301D-90FA-1265D9216323
-  Functions: 3175
-  Symbols:   10381
-  CStrings:  4675
+  UUID: 3DF7A23F-5014-35B9-9C23-EFDC8646B913
+  Functions: 3177
+  Symbols:   10388
+  CStrings:  4683
 
Symbols:
+ -[CXCallUpdate anyRemoteSupportsRequestToScreenShare]
+ -[CXCallUpdate setAnyRemoteSupportsRequestToScreenShare:]
+ _OBJC_IVAR_$_CXCallUpdate._anyRemoteSupportsRequestToScreenShare
+ _objc_msgSend$anyRemoteSupportsRequestToScreenShare
+ _objc_msgSend$setAnyRemoteSupportsRequestToScreenShare:
Functions:
~ -[CXCallUpdate description] : 3984 -> 4024
+ -[CXCallUpdate anyRemoteSupportsRequestToScreenShare]
+ -[CXCallUpdate conversationGroupUUID]
~ -[CXCallUpdate updateWithUpdate:] : 3212 -> 3244
~ -[CXCallUpdate updateCopy:withZone:] : 4340 -> 4388
~ -[CXCallUpdate initWithCoder:] : 4724 -> 4756
~ -[CXCallUpdate encodeWithCoder:] : 4004 -> 4044
CStrings:
+ " anyRemoteSupportsRequestToScreenShare=%d"
+ "TB,N,V_anyRemoteSupportsRequestToScreenShare"
+ "T{CXCallUpdateHasSet=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1},N,V_hasSet"
+ "_anyRemoteSupportsRequestToScreenShare"
+ "anyRemoteSupportsRequestToScreenShare"
+ "setAnyRemoteSupportsRequestToScreenShare:"
+ "v28@0:8{CXCallUpdateHasSet=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}16"
+ "{CXCallUpdateHasSet=\"account\"b1\"activeRemoteParticipant\"b1\"remoteMember\"b1\"localizedCallerName\"b1\"localizedCallerImageURL\"b1\"emergency\"b1\"failureExpected\"b1\"supportsEmergencyFallback\"b1\"usingBaseband\"b1\"blocked\"b1\"ttyType\"b1\"supportsTTYWithVoice\"b1\"mayRequireBreakBeforeMake\"b1\"hasVideo\"b1\"isUpgradeToVideo\"b1\"audioCategory\"b1\"audioMode\"b1\"audioInterruptionProvider\"b1\"audioInterruptionOperationMode\"b1\"verificationStatus\"b1\"priority\"b1\"requiresInCallSounds\"b1\"inCallSoundRegion\"b1\"supportsHolding\"b1\"supportsGrouping\"b1\"supportsUngrouping\"b1\"supportsDTMF\"b1\"supportsDTMFUpdates\"b1\"supportsSharePlay\"b1\"supportsScreenShare\"b1\"supportsUnambiguousMultiPartyState\"b1\"supportsAddCall\"b1\"supportsSendingToVoicemail\"b1\"supportsRecording\"b1\"isUnderlyingLinksConnected\"b1\"videoStreamToken\"b1\"callTokens\"b1\"announceProviderIdentifier\"b1\"initiator\"b1\"crossDeviceIdentifier\"b1\"ISOCountryCode\"b1\"localSenderIdentityUUID\"b1\"localSenderIdentityAccountUUID\"b1\"localMemberHandleValue\"b1\"localSenderSubscriptionIdentifier\"b1\"participantGroupUUID\"b1\"remoteParticipantHandles\"b1\"otherInvitedHandles\"b1\"activeRemoteParticipantHandles\"b1\"handoffContext\"b1\"screenShareAttributes\"b1\"context\"b1\"prefersExclusiveAccessToCellularNetwork\"b1\"remoteUplinkMuted\"b1\"shouldSuppressInCallUI\"b1\"launchInBackground\"b1\"requiresAuthentication\"b1\"mutuallyExclusiveCall\"b1\"junkConfidence\"b1\"identificationCategory\"b1\"conversation\"b1\"mixesVoiceWithMedia\"b1\"prefersToPlayDuringWombat\"b1\"mediaPlaybackOnExternalDevice\"b1\"oneToOneModeEnabled\"b1\"sharingScreen\"b1\"bluetoothAudioFormat\"b1\"ignoresBluetoothDeviceUID\"b1\"serviceStatus\"b1\"transmissionMode\"b1\"accessoryButtonEventsEnabled\"b1\"sendingVideo\"b1\"hasBeenRedirected\"b1\"isKnownCaller\"b1\"filteredOutReason\"b1\"silencingUserInfo\"b1\"isReRing\"b1\"suppressRingtone\"b1\"callSubType\"b1\"supportsScreening\"b1\"supportsRecents\"b1\"screenSharingIntention\"b1\"screenSharingType\"b1\"isSharePlayCapable\"b1\"anyRemoteSupportsRequestToScreenShare\"b1\"nearbyMode\"b1\"commTrustScore\"b1\"specialUnknown\"b1\"conversationGroupUUID\"b1\"startCallMuted\"b1}"
+ "{CXCallUpdateHasSet=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}16@0:8"
- "T{CXCallUpdateHasSet=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1},N,V_hasSet"
- "v28@0:8{CXCallUpdateHasSet=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}16"
- "{CXCallUpdateHasSet=\"account\"b1\"activeRemoteParticipant\"b1\"remoteMember\"b1\"localizedCallerName\"b1\"localizedCallerImageURL\"b1\"emergency\"b1\"failureExpected\"b1\"supportsEmergencyFallback\"b1\"usingBaseband\"b1\"blocked\"b1\"ttyType\"b1\"supportsTTYWithVoice\"b1\"mayRequireBreakBeforeMake\"b1\"hasVideo\"b1\"isUpgradeToVideo\"b1\"audioCategory\"b1\"audioMode\"b1\"audioInterruptionProvider\"b1\"audioInterruptionOperationMode\"b1\"verificationStatus\"b1\"priority\"b1\"requiresInCallSounds\"b1\"inCallSoundRegion\"b1\"supportsHolding\"b1\"supportsGrouping\"b1\"supportsUngrouping\"b1\"supportsDTMF\"b1\"supportsDTMFUpdates\"b1\"supportsSharePlay\"b1\"supportsScreenShare\"b1\"supportsUnambiguousMultiPartyState\"b1\"supportsAddCall\"b1\"supportsSendingToVoicemail\"b1\"supportsRecording\"b1\"isUnderlyingLinksConnected\"b1\"videoStreamToken\"b1\"callTokens\"b1\"announceProviderIdentifier\"b1\"initiator\"b1\"crossDeviceIdentifier\"b1\"ISOCountryCode\"b1\"localSenderIdentityUUID\"b1\"localSenderIdentityAccountUUID\"b1\"localMemberHandleValue\"b1\"localSenderSubscriptionIdentifier\"b1\"participantGroupUUID\"b1\"remoteParticipantHandles\"b1\"otherInvitedHandles\"b1\"activeRemoteParticipantHandles\"b1\"handoffContext\"b1\"screenShareAttributes\"b1\"context\"b1\"prefersExclusiveAccessToCellularNetwork\"b1\"remoteUplinkMuted\"b1\"shouldSuppressInCallUI\"b1\"launchInBackground\"b1\"requiresAuthentication\"b1\"mutuallyExclusiveCall\"b1\"junkConfidence\"b1\"identificationCategory\"b1\"conversation\"b1\"mixesVoiceWithMedia\"b1\"prefersToPlayDuringWombat\"b1\"mediaPlaybackOnExternalDevice\"b1\"oneToOneModeEnabled\"b1\"sharingScreen\"b1\"bluetoothAudioFormat\"b1\"ignoresBluetoothDeviceUID\"b1\"serviceStatus\"b1\"transmissionMode\"b1\"accessoryButtonEventsEnabled\"b1\"sendingVideo\"b1\"hasBeenRedirected\"b1\"isKnownCaller\"b1\"filteredOutReason\"b1\"silencingUserInfo\"b1\"isReRing\"b1\"suppressRingtone\"b1\"callSubType\"b1\"supportsScreening\"b1\"supportsRecents\"b1\"screenSharingIntention\"b1\"screenSharingType\"b1\"isSharePlayCapable\"b1\"nearbyMode\"b1\"commTrustScore\"b1\"specialUnknown\"b1\"conversationGroupUUID\"b1\"startCallMuted\"b1}"
- "{CXCallUpdateHasSet=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}16@0:8"

```
