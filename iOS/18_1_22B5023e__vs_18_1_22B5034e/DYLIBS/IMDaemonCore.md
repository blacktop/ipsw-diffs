## IMDaemonCore

> `/System/Library/PrivateFrameworks/IMDaemonCore.framework/IMDaemonCore`

```diff

-1402.200.8.0.0
-  __TEXT.__text: 0x278dc4
-  __TEXT.__auth_stubs: 0x3f90
+1402.200.35.0.0
+  __TEXT.__text: 0x279af8
+  __TEXT.__auth_stubs: 0x3f80
   __TEXT.__objc_methlist: 0x12b80
-  __TEXT.__const: 0x2348
-  __TEXT.__cstring: 0x15061
-  __TEXT.__gcc_except_tab: 0x25eb4
-  __TEXT.__oslogstring: 0x43687
+  __TEXT.__const: 0x2308
+  __TEXT.__cstring: 0x14fe1
+  __TEXT.__gcc_except_tab: 0x26020
+  __TEXT.__oslogstring: 0x439f7
   __TEXT.__ustring: 0x37a
   __TEXT.__dlopen_cstrs: 0xfa
-  __TEXT.__swift5_typeref: 0x130a
-  __TEXT.__constg_swiftt: 0xfa4
-  __TEXT.__swift5_reflstr: 0x808
-  __TEXT.__swift5_fieldmd: 0x944
+  __TEXT.__swift5_typeref: 0x12ee
+  __TEXT.__constg_swiftt: 0xf34
+  __TEXT.__swift5_reflstr: 0x7d8
+  __TEXT.__swift5_fieldmd: 0x910
   __TEXT.__swift5_builtin: 0xdc
   __TEXT.__swift5_assocty: 0x278
-  __TEXT.__swift5_capture: 0xb40
+  __TEXT.__swift5_capture: 0xb50
   __TEXT.__swift5_proto: 0x124
-  __TEXT.__swift5_types: 0xf8
+  __TEXT.__swift5_types: 0xf4
   __TEXT.__swift5_protos: 0x18
-  __TEXT.__unwind_info: 0xa830
+  __TEXT.__unwind_info: 0xa838
   __TEXT.__eh_frame: 0x1aec
   __TEXT.__objc_classname: 0x2c68
-  __TEXT.__objc_methname: 0x43ae0
-  __TEXT.__objc_methtype: 0x8e19
-  __TEXT.__objc_stubs: 0x2b260
-  __DATA_CONST.__got: 0x2870
-  __DATA_CONST.__const: 0x5bc0
-  __DATA_CONST.__objc_classlist: 0x798
+  __TEXT.__objc_methname: 0x43d94
+  __TEXT.__objc_methtype: 0x8ed9
+  __TEXT.__objc_stubs: 0x2b2e0
+  __DATA_CONST.__got: 0x2888
+  __DATA_CONST.__const: 0x5be0
+  __DATA_CONST.__objc_classlist: 0x790
   __DATA_CONST.__objc_catlist: 0xc8
   __DATA_CONST.__objc_protolist: 0x5d0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd140
+  __DATA_CONST.__objc_selrefs: 0xd170
   __DATA_CONST.__objc_protorefs: 0x1d0
   __DATA_CONST.__objc_superrefs: 0x4d8
   __DATA_CONST.__objc_arraydata: 0xb0
-  __AUTH_CONST.__auth_got: 0x1fd8
-  __AUTH_CONST.__auth_ptr: 0x7d8
-  __AUTH_CONST.__const: 0x51d8
-  __AUTH_CONST.__cfstring: 0xe2a0
-  __AUTH_CONST.__objc_const: 0x212a0
+  __AUTH_CONST.__auth_got: 0x1fd0
+  __AUTH_CONST.__auth_ptr: 0x7c0
+  __AUTH_CONST.__const: 0x5228
+  __AUTH_CONST.__cfstring: 0xe2e0
+  __AUTH_CONST.__objc_const: 0x211f8
   __AUTH_CONST.__objc_intobj: 0x8a0
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH.__objc_data: 0x2730
-  __AUTH.__data: 0x5c8
+  __AUTH.__objc_data: 0x2630
+  __AUTH.__data: 0x5a0
   __DATA.__objc_ivar: 0xdf8
-  __DATA.__data: 0x42f0
+  __DATA.__data: 0x42e0
   __DATA.__bss: 0x2210
-  __DATA.__common: 0xc0
+  __DATA.__common: 0xb8
   __DATA_DIRTY.__objc_data: 0x2e08
   __DATA_DIRTY.__data: 0xcb0
   __DATA_DIRTY.__bss: 0x868

   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /System/Library/PrivateFrameworks/ApplePushService.framework/ApplePushService
-  - /System/Library/PrivateFrameworks/AskToCore.framework/AskToCore
   - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
   - /System/Library/PrivateFrameworks/BlastDoor.framework/BlastDoor

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 9870
-  Symbols:   2613
-  CStrings:  17510
+  Functions: 9862
+  Symbols:   2615
+  CStrings:  17533
 
Symbols:
+ _IMSMSDefaultsDomain
+ _IMSMSDefaultsSystemVersionForLastRelayMICMigration
+ _IMDRelayMessageItemDictionaryDateKey
+ _IMSMSDefaultsDevicesWithMICEnabledKey
- _OBJC_CLASS_$_IMDAskToValidator
- _OBJC_METACLASS_$_IMDAskToValidator
CStrings:
+ "Relaying dict containing MMS to local device. %!{(MISSING)sensitive}@ "
+ "_relayMessageDict:messageID:forcedCallerID:didSendSMS:relayToWatchOnly:shouldDisableScreenTimeRestrictions:hasAttachments:requiredCapabilities:"
+ "_convertIMMessageItemToIncomingRelayDictionary:chat:overridingAttachmentData:"
+ "_maxWatchTransferSize"
+ "v32@?0@\"NSString\"8@\"IMDChat\"16@?<v@?>24"
+ "v64@0:8@16@24@32B40B44B48B52@56"
+ "Not relaying to device as it does not support required capability: %!@(MISSING)"
+ "releasePendingMessageWithGUID:serviceName:chat:completion:"
+ "_convergeGroupChatIfNeededWithServiceSession:account:replicationService:groupID:incomingParticipants:fromIdentifier:toIdentifier:receivedGroupParticipantVersion:receivedGroupProtocolVersion:messageTimeStamp:groupPhotoCreationTime:"
+ "> MiC is disabled, so no need to enroll device for SMS relay."
+ "v72@0:8@16q24@32@40B48B52^@56@64"
+ "_relayMessageToPeers:forChat:serviceName:requiredCapabilities:reflectOnly:excludesWatch:onlyWatch:overridingAttachmentData:"
+ "setMimeType:"
+ "relayDictionaryToPeers:requiresUpload:serviceName:requiredCapabilities:"
+ "B68@0:8@16@24@32@40B48B52B56@60"
+ "v32@0:8@\"NSString\"16@?<v@?B>24"
+ "> Last migration was for {%!@(MISSING)}, currently {%!@(MISSING)}."
+ "B44@0:8@16B24@28@36"
+ "_convergesParticipantsForReplicationService:"
+ "relayMessageGUID:completion:"
+ "_relayMessageDict:command:messageID:forcedCallerID:didSendSMS:relayToWatchOnly:shouldDisableScreenTimeRestrictions:hasAttachments:requiredCapabilities:"
+ "productVersion"
+ "requiredCapabilitiesForSMSRelay"
+ "_relayMessageDict:command:messageID:forcedCallerID:didSendSMS:relayToWatchOnly:shouldDisableScreenTimeRestrictions:hasAttachments:sentToDevices:requiredCapabilities:"
+ "relayMessage:chat:didSendSMS:attemptingReplication:forceReflection:relayToWatchOnly:shouldDisableScreenTimeRestrictions:callerID:iMessageCapability:requiredCapabilities:"
+ "__im_isChatBotUsingLocalCache"
+ "_convergesGroupPhotosForReplicationService:"
+ "v72@0:8@16q24@32@40B48B52B56B60@64"
+ "v104@0:8@16@24@32@40@48@56@64@72@80@88@96"
+ "Message %!@(MISSING) needs LQ transcode to go to watch - we will relay a low-quality transcoded result to the watch"
+ "_needsLowQualityTranscodeForMessage:"
+ "queued startTrackingRCSSwitchStates(). Heading back..."
+ "Relaying LQ transcode of transfer GUID %!@(MISSING) at path %!@(MISSING) size %!l(MISSING)lu to watch"
+ "utType"
+ "relayDictionaryToPeers:requiresUpload:serviceName:requiredCapabilities:excludesWatch:onlyWatch:"
+ "startTrackingRCSSwitchStates() took %!s(MISSING)"
+ "Checking if we need to enroll as an SMS relay device."
+ "Failed to transcode HQ asset %!@(MISSING) to LQ for watch relay with error %!@(MISSING)"
+ "v88@0:8@16q24@32@40B48B52B56B60^@64@72@80"
+ "Not converging participants, replication service does not permit it"
+ "> We have already completed SMS MiC relay migration."
+ "relayMessageToPeers:forChat:serviceName:reflectOnly:requiredCapabilities:"
+ "relayPartsFor:overridingAttachmentData:"
+ "B52@0:8@16@24@32B40@44"
+ "> Beginning flow to enroll device in SMS relay."
+ "v76@0:8@16@24B32B36B40B44B48@52q60@68"
+ "_forwardMessageToPeers:messageType:guid:originalSender:hasAttachment:watchOnly:sentToDevices:requiredCapabilities:"
+ "B52@0:8@16B24@28@36B44B48"
+ "com.apple.messages.SMSRelaySend"
+ "_relayMessageDict:command:messageID:forcedCallerID:didSendSMS:relayToWatchOnly:shouldDisableScreenTimeRestrictions:hasAttachments:sentToDevices:extraOptions:requiredCapabilities:"
+ "_convertIMMessageItemDictionaryToIMMessageItem:timestamp:"
+ "<IMFindChatProcessingPipelineComponent> Found pre-supplied chat: %!@(MISSING)"
- "v72@0:8@16q24@32@40B48B52B56B60^@64"
- "relayMessageToPeers:forChat:serviceName:reflectOnly:"
- "_relayMessageDict:command:messageID:forcedCallerID:didSendSMS:relayToWatchOnly:shouldDisableScreenTimeRestrictions:hasAttachments:sentToDevices:"
- "__im_isChatBot"
- "isSMSForwardingEnabled"
- "_convertIMMessageItemDictionaryToIMMessageItem:"
- "relayMessage:chat:didSendSMS:attemptingReplication:forceReflection:relayToWatchOnly:shouldDisableScreenTimeRestrictions:callerID:iMessageCapability:"
- "Relaying dict containing MMS to local device. %!@(MISSING) "
- "v68@0:8@16@24B32B36B40B44B48@52q60"
- "_convergeGroupChatIfNeededWithServiceSession:account:groupID:incomingParticipants:fromIdentifier:toIdentifier:receivedGroupParticipantVersion:receivedGroupProtocolVersion:messageTimeStamp:groupPhotoCreationTime:"
- "_relayMessageDict:messageID:forcedCallerID:didSendSMS:relayToWatchOnly:shouldDisableScreenTimeRestrictions:hasAttachments:"
- "IMDAskToValidator"
- "_relayMessageDict:command:messageID:forcedCallerID:didSendSMS:relayToWatchOnly:shouldDisableScreenTimeRestrictions:hasAttachments:"
- "v56@0:8@16@24@32B40B44B48B52"
- "hasValidAskToURL"
- "IMDaemonCore.AskToValidator"
- "_relayMessageDict:command:messageID:forcedCallerID:didSendSMS:relayToWatchOnly:shouldDisableScreenTimeRestrictions:hasAttachments:sentToDevices:extraOptions:"
- "releasePendingMessageWithGUID:serviceName:completion:"
- "hasMigratedSMSRelayForMIC"
- "_convertIMMessageItemToIncomingRelayDictionary:chat:"
- "isForFamily"
- "T@\"NSURL\",N,R"
- "v64@0:8@16q24@32@40B48B52B56B60"
- "v24@?0@\"NSString\"8@?<v@?>16"
- "relayPartsFor:"
- "v64@0:8@16q24@32@40B48B52^@56"
- "$__lazy_storage_$_payload"
- "forwardMessageToPeers:messageType:guid:originalSender:hasAttachment:watchOnly:sentToDevices:"

```
