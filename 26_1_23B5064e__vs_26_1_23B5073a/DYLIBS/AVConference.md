## AVConference

> `/System/Library/PrivateFrameworks/AVConference.framework/AVConference`

```diff

-2175.13.1.0.0
-  __TEXT.__text: 0x798dd0
+2175.14.1.1.0
+  __TEXT.__text: 0x799808
   __TEXT.__auth_stubs: 0x5630
-  __TEXT.__objc_methlist: 0x35c60
+  __TEXT.__objc_methlist: 0x35cb8
   __TEXT.__const: 0xc780
-  __TEXT.__cstring: 0x8f835
-  __TEXT.__oslogstring: 0x10f908
+  __TEXT.__cstring: 0x8f98e
+  __TEXT.__oslogstring: 0x10f99c
   __TEXT.__gcc_except_tab: 0x2abc
   __TEXT.__ustring: 0x2d4
-  __TEXT.__unwind_info: 0x108f0
+  __TEXT.__unwind_info: 0x10910
   __TEXT.__objc_classname: 0x4eb2
-  __TEXT.__objc_methname: 0x7e027
-  __TEXT.__objc_methtype: 0x2831e
-  __TEXT.__objc_stubs: 0x4efc0
+  __TEXT.__objc_methname: 0x7e10a
+  __TEXT.__objc_methtype: 0x283a6
+  __TEXT.__objc_stubs: 0x4f080
   __DATA_CONST.__got: 0x1a60
   __DATA_CONST.__const: 0x6b10
   __DATA_CONST.__objc_classlist: 0x12e8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x488
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x16a40
+  __DATA_CONST.__objc_selrefs: 0x16a70
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x10e8
   __DATA_CONST.__objc_arraydata: 0x2628
   __AUTH_CONST.__auth_got: 0x2b30
   __AUTH_CONST.__const: 0x3ca8
-  __AUTH_CONST.__cfstring: 0x264e0
-  __AUTH_CONST.__objc_const: 0x638d0
+  __AUTH_CONST.__cfstring: 0x265c0
+  __AUTH_CONST.__objc_const: 0x63910
   __AUTH_CONST.__objc_intobj: 0x4a10
   __AUTH_CONST.__objc_arrayobj: 0x1b48
   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x180
   __AUTH_CONST.__objc_dictobj: 0x2d0
   __AUTH.__objc_data: 0x1590
-  __DATA.__objc_ivar: 0x6cbc
+  __DATA.__objc_ivar: 0x6cc4
   __DATA.__data: 0x78b0
   __DATA.__bss: 0xd78
   __DATA.__common: 0x55

   - /usr/lib/libspindump.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 26C7289A-3D07-37F4-B0EC-FC93011AAE6B
-  Functions: 31633
-  Symbols:   97544
-  CStrings:  57328
+  UUID: D9351289-FBA8-3903-997C-D35B44EB903A
+  Functions: 31644
+  Symbols:   97574
+  CStrings:  57358
 
Symbols:
+ +[VCAudioRelayIOController terminateWithReason:]
+ -[VCConnection setPreviousLinkFlags:]
+ -[VCConnection setPreviousRemoteLinkFlags:]
+ -[VCConnectionIDS applyLinkFlagsOverride:isLocal:]
+ -[VCSession reportSatelliteNetworkStatusForConnection:]
+ -[VCSessionParticipantLocal feedbackDelegate]
+ GCC_except_table203
+ _OBJC_IVAR_$_VCConnection._previousLinkFlags
+ _OBJC_IVAR_$_VCConnection._previousRemoteLinkFlags
+ _VCConnectionIDS_ReportingSatelliteNetwork
+ _VCConnectionIDS_ReportingSatelliteNetwork.cold.1
+ ___40-[VCConnectionManagerIDS addConnection:]_block_invoke.51
+ ___45-[VCSessionParticipantLocal feedbackDelegate]_block_invoke
+ ___55-[AVCTextStream registerBlocksForDelegateNotifications]_block_invoke.100
+ ___55-[AVCTextStream registerBlocksForDelegateNotifications]_block_invoke.104
+ ___55-[AVCTextStream registerBlocksForDelegateNotifications]_block_invoke.108
+ ___55-[AVCTextStream registerBlocksForDelegateNotifications]_block_invoke.72
+ ___55-[AVCTextStream registerBlocksForDelegateNotifications]_block_invoke.80
+ ___55-[AVCTextStream registerBlocksForDelegateNotifications]_block_invoke.82
+ ___55-[AVCTextStream registerBlocksForDelegateNotifications]_block_invoke.89
+ ___55-[AVCTextStream registerBlocksForDelegateNotifications]_block_invoke.96
+ _objc_msgSend$applyLinkFlagsOverride:isLocal:
+ _objc_msgSend$feedbackDelegate
+ _objc_msgSend$reportSatelliteNetworkStatusForConnection:
+ _objc_msgSend$setPreviousLinkFlags:
+ _objc_msgSend$setPreviousRemoteLinkFlags:
+ _objc_msgSend$terminateWithReason:
- ___40-[VCConnectionManagerIDS addConnection:]_block_invoke.50
- ___55-[AVCTextStream registerBlocksForDelegateNotifications]_block_invoke.101
- ___55-[AVCTextStream registerBlocksForDelegateNotifications]_block_invoke.105
- ___55-[AVCTextStream registerBlocksForDelegateNotifications]_block_invoke.69
- ___55-[AVCTextStream registerBlocksForDelegateNotifications]_block_invoke.77
- ___55-[AVCTextStream registerBlocksForDelegateNotifications]_block_invoke.79
- ___55-[AVCTextStream registerBlocksForDelegateNotifications]_block_invoke.86
- ___55-[AVCTextStream registerBlocksForDelegateNotifications]_block_invoke.93
- ___55-[AVCTextStream registerBlocksForDelegateNotifications]_block_invoke.97
CStrings:
+ " [%s] %s:%d Overriding %s link flags: 0x%04x -> 0x%04x"
+ " [%s] %s:%d Set previous link flags='%08x'"
+ " [%s] %s:%d Set previous remote link flags='%08x'"
+ "-[VCConnection setPreviousLinkFlags:]"
+ "-[VCConnection setPreviousRemoteLinkFlags:]"
+ "-[VCConnectionIDS applyLinkFlagsOverride:isLocal:]"
+ "2175.14.1.1"
+ "<%s:%p> Token (%d) Link (%d): %s <-> %s (%s, %s), priority %d, uplink bitrate cap (%u), downlink bitrate cap (%u), uplink audio only bitrate cap = (%u), uplink OneToOne bitrate cap = (%u), isLocalConstrained (%d), isRemoteConstrained (%d), isLocalExpensive (%d) isRemoteExpensive (%d) isLocalDelegated (%d) isRemoteDelegated (%d) isLocalUltraConstrained (%d) isRemoteUltraConstrained (%d) isVirtualRelayLink (%d) reportingIPVersion(%d) TransportLayerEncryption=%d relayProtocolStackDescrption(%@) channelDataBaseProtocolStackDescription(%@) _isHopByHopEncryptionSupported=%d"
+ "LSAT"
+ "RSAT"
+ "S24@0:8S16B20"
+ "Sink IO timout"
+ "Source IO timout"
+ "T^{_VCAudioIOControllerIOState=BdIIdQ{_VCSingleLinkedList=^{_VCSingleLinkedListEntry}B^?Q}{os_unfair_lock_s=I}^{opaqueCMSimpleQueue}^{opaqueVCAudioLimiter}^{opaqueVCAudioBufferList}^{opaqueVCAudioBufferList}IQQ[40c]BBBdBC^{opaqueVCVoiceDetector}},R,N"
+ "VCConnectionIDS_ReportingSatelliteNetwork"
+ "^{_VCAudioIOControllerIOState=BdIIdQ{_VCSingleLinkedList=^{_VCSingleLinkedListEntry}B^?Q}{os_unfair_lock_s=I}^{opaqueCMSimpleQueue}^{opaqueVCAudioLimiter}^{opaqueVCAudioBufferList}^{opaqueVCAudioBufferList}IQQ[40c]BBBdBC^{opaqueVCVoiceDetector}}16@0:8"
+ "_previousLinkFlags"
+ "_previousRemoteLinkFlags"
+ "applyLinkFlagsOverride:isLocal:"
+ "feedbackDelegate"
+ "linkFlagsOverride"
+ "remoteLinkFlagsOverride"
+ "reportSatelliteNetworkStatusForConnection:"
+ "setPreviousLinkFlags:"
+ "setPreviousRemoteLinkFlags:"
+ "terminateWithReason:"
+ "v24@0:8^{_VCAudioIOControllerIOState=BdIIdQ{_VCSingleLinkedList=^{_VCSingleLinkedListEntry}B^?Q}{os_unfair_lock_s=I}^{opaqueCMSimpleQueue}^{opaqueVCAudioLimiter}^{opaqueVCAudioBufferList}^{opaqueVCAudioBufferList}IQQ[40c]BBBdBC^{opaqueVCVoiceDetector}}16"
+ "v32@0:8^{_VCAudioIOControllerClientIO=^v^?@III^{opaqueVCAudioBufferList}BB}16^{_VCAudioIOControllerIOState=BdIIdQ{_VCSingleLinkedList=^{_VCSingleLinkedListEntry}B^?Q}{os_unfair_lock_s=I}^{opaqueCMSimpleQueue}^{opaqueVCAudioLimiter}^{opaqueVCAudioBufferList}^{opaqueVCAudioBufferList}IQQ[40c]BBBdBC^{opaqueVCVoiceDetector}}24"
+ "{_VCAudioIOControllerIOState=\"timestampInitialized\"B\"lastHostTime\"d\"lastInputTimestamp\"I\"lastInputSampleCount\"I\"lastBlockSize\"d\"lastTimestamp\"Q\"clientIOList\"{_VCSingleLinkedList=\"head\"^{_VCSingleLinkedListEntry}\"initialized\"B\"compare\"^?\"countEntries\"Q}\"clientIOListLock\"{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}\"eventQueue\"^{opaqueCMSimpleQueue}\"audioLimiter\"^{opaqueVCAudioLimiter}\"secondarySampleBuffer\"^{opaqueVCAudioBufferList}\"interruptMixDownSampleBuffer\"^{opaqueVCAudioBufferList}\"audioSessionId\"I\"channelStateBitmap\"Q\"prevUsedChannelStateBitmap\"Q\"logPrefix\"[40c]\"isMuted\"B\"isVoiceActivityEnabled\"B\"isMediaPriorityEnabled\"B\"forcedMediaPriorityLastUpdateTime\"d\"isForcedMediaPriorityEnabled\"B\"forcedMediaPriority\"C\"voiceDetector\"^{opaqueVCVoiceDetector}}"
- "2175.13.1"
- "<%s:%p> Token (%d) Link (%d): %s <-> %s (%s, %s), priority %d, uplink bitrate cap (%u), downlink bitrate cap (%u), uplink audio only bitrate cap = (%u), uplink OneToOne bitrate cap = (%u), isLocalConstrained (%d), isRemoteConstrained (%d), isLocalExpensive (%d) isRemoteExpensive (%d) isLocalDelegated (%d) isRemoteDelegated (%d) isVirtualRelayLink (%d) reportingIPVersion(%d) TransportLayerEncryption=%d relayProtocolStackDescrption(%@) channelDataBaseProtocolStackDescription(%@) _isHopByHopEncryptionSupported=%d"
- "T^{_VCAudioIOControllerIOState=BdIIdQ{_VCSingleLinkedList=^{_VCSingleLinkedListEntry}B^?Q}^{opaqueCMSimpleQueue}^{opaqueVCAudioLimiter}^{opaqueVCAudioBufferList}^{opaqueVCAudioBufferList}IQQ[40c]BBBdBC^{opaqueVCVoiceDetector}},R,N"
- "^{_VCAudioIOControllerIOState=BdIIdQ{_VCSingleLinkedList=^{_VCSingleLinkedListEntry}B^?Q}^{opaqueCMSimpleQueue}^{opaqueVCAudioLimiter}^{opaqueVCAudioBufferList}^{opaqueVCAudioBufferList}IQQ[40c]BBBdBC^{opaqueVCVoiceDetector}}16@0:8"
- "v24@0:8^{_VCAudioIOControllerIOState=BdIIdQ{_VCSingleLinkedList=^{_VCSingleLinkedListEntry}B^?Q}^{opaqueCMSimpleQueue}^{opaqueVCAudioLimiter}^{opaqueVCAudioBufferList}^{opaqueVCAudioBufferList}IQQ[40c]BBBdBC^{opaqueVCVoiceDetector}}16"
- "v32@0:8^{_VCAudioIOControllerClientIO=^v^?@III^{opaqueVCAudioBufferList}BB}16^{_VCAudioIOControllerIOState=BdIIdQ{_VCSingleLinkedList=^{_VCSingleLinkedListEntry}B^?Q}^{opaqueCMSimpleQueue}^{opaqueVCAudioLimiter}^{opaqueVCAudioBufferList}^{opaqueVCAudioBufferList}IQQ[40c]BBBdBC^{opaqueVCVoiceDetector}}24"
- "{_VCAudioIOControllerIOState=\"timestampInitialized\"B\"lastHostTime\"d\"lastInputTimestamp\"I\"lastInputSampleCount\"I\"lastBlockSize\"d\"lastTimestamp\"Q\"clientIOList\"{_VCSingleLinkedList=\"head\"^{_VCSingleLinkedListEntry}\"initialized\"B\"compare\"^?\"countEntries\"Q}\"eventQueue\"^{opaqueCMSimpleQueue}\"audioLimiter\"^{opaqueVCAudioLimiter}\"secondarySampleBuffer\"^{opaqueVCAudioBufferList}\"interruptMixDownSampleBuffer\"^{opaqueVCAudioBufferList}\"audioSessionId\"I\"channelStateBitmap\"Q\"prevUsedChannelStateBitmap\"Q\"logPrefix\"[40c]\"isMuted\"B\"isVoiceActivityEnabled\"B\"isMediaPriorityEnabled\"B\"forcedMediaPriorityLastUpdateTime\"d\"isForcedMediaPriorityEnabled\"B\"forcedMediaPriority\"C\"voiceDetector\"^{opaqueVCVoiceDetector}}"

```
