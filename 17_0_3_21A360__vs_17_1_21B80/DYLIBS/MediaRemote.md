## MediaRemote

> `/System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote`

```diff

-4023.110.7.0.0
-  __TEXT.__text: 0x28d290
-  __TEXT.__auth_stubs: 0x1540
-  __TEXT.__objc_methlist: 0x23780
-  __TEXT.__const: 0x348
-  __TEXT.__cstring: 0x272c6
-  __TEXT.__oslogstring: 0xca6a
-  __TEXT.__gcc_except_tab: 0x4d48
+4023.210.1.0.0
+  __TEXT.__text: 0x298634
+  __TEXT.__auth_stubs: 0x1610
+  __TEXT.__objc_methlist: 0x244b8
+  __TEXT.__const: 0x378
+  __TEXT.__cstring: 0x279da
+  __TEXT.__oslogstring: 0xcacd
+  __TEXT.__gcc_except_tab: 0x4e0c
   __TEXT.__ustring: 0x12
-  __TEXT.__unwind_info: 0x9d78
-  __TEXT.__objc_classname: 0x430b
-  __TEXT.__objc_methname: 0x40e24
-  __TEXT.__objc_methtype: 0x8188
-  __TEXT.__objc_stubs: 0x22280
-  __DATA_CONST.__got: 0x1c8
-  __DATA_CONST.__const: 0x9f90
-  __DATA_CONST.__objc_classlist: 0xf48
+  __TEXT.__unwind_info: 0x9ff8
+  __TEXT.__objc_classname: 0x4483
+  __TEXT.__objc_methname: 0x42222
+  __TEXT.__objc_methtype: 0x82aa
+  __TEXT.__objc_stubs: 0x22c20
+  __DATA_CONST.__got: 0x1c0
+  __DATA_CONST.__const: 0x9ff8
+  __DATA_CONST.__objc_classlist: 0xfa8
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x230
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x33088
-  __DATA_CONST.__objc_selrefs: 0xc7f8
-  __DATA_CONST.__objc_arraydata: 0x1b0
-  __AUTH_CONST.__cfstring: 0x1bfc0
-  __AUTH_CONST.__objc_const: 0xb1a8
+  __DATA_CONST.__objc_const: 0x33fb0
+  __DATA_CONST.__objc_selrefs: 0xcba0
+  __DATA_CONST.__objc_arraydata: 0x1d0
+  __AUTH_CONST.__cfstring: 0x1c5e0
+  __AUTH_CONST.__objc_const: 0xb628
   __AUTH_CONST.__const: 0x3000
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__objc_intobj: 0x390
-  __AUTH_CONST.__objc_arrayobj: 0xf0
+  __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0xab0
-  __AUTH.__objc_data: 0x6fe0
-  __AUTH.__data: 0x1b0
+  __AUTH_CONST.__auth_got: 0xb18
+  __AUTH.__objc_data: 0x73a0
+  __AUTH.__data: 0x1d0
   __DATA.__objc_protorefs: 0x88
-  __DATA.__objc_classrefs: 0x1078
-  __DATA.__objc_superrefs: 0xd98
-  __DATA.__objc_ivar: 0x2b4c
-  __DATA.__data: 0x1d10
-  __DATA.__bss: 0x490
+  __DATA.__objc_classrefs: 0x10d0
+  __DATA.__objc_superrefs: 0xdf0
+  __DATA.__objc_ivar: 0x2c0c
+  __DATA.__data: 0x1d00
+  __DATA.__bss: 0x4e0
   __DATA.__common: 0x0
   __DATA_DIRTY.__objc_data: 0x28f0
   __DATA_DIRTY.__data: 0x210

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 17451
-  Symbols:   47420
-  CStrings:  17131
+  Functions: 17745
+  Symbols:   48253
+  CStrings:  17384
 
Symbols:
+ +[MRGroupTopologyModificationRequest supportsSecureCoding]
+ +[MRPlaybackQueueParticipant expectedIdentifierForUserIdentity:withRandomData:]
+ +[MRPlaybackQueueParticipant fetchParticipantsWithRequest:forPlayerPath:queue:completion:]
+ +[MRPlaybackQueueParticipant fetchPlaybackQueueParticipantIdentifierForLocalAccountWithDSID:completion:]
+ +[MRPlaybackQueueParticipantRequest defaultRequest]
+ +[MRPlaybackQueueRequest defaultArtworkHeight]
+ +[MRUserIdentity fetchIdentityForDSID:completion:]
+ +[_MRContentItemProtobuf availableArtworkFormatsType]
+ +[_MRContentItemProtobuf availableRemoteArtworkFormatsType]
+ +[_MRContentItemProtobuf dataArtworksType]
+ +[_MRContentItemProtobuf remoteArtworksType]
+ +[_MRGroupTopologyModificationRequestProtobuf outputDeviceUIDsType]
+ +[_MRPlaybackQueueRequestProtobuf requestedArtworkFormatsType]
+ +[_MRPlaybackQueueRequestProtobuf requestedRemoteArtworkFormatsType]
+ +[_MRPlayerClientParticipantsUpdateMessageProtobuf participantsType]
+ -[MRAVConcreteOutputContext modifyTopologyWithRequest:withReplyQueue:completion:]
+ -[MRAVDistantRoutingDiscoverySession _notifyEndpointsChanged]
+ -[MRAVDistantRoutingDiscoverySession _resolveDistantEndpoints:]
+ -[MRAVDistantRoutingDiscoverySession _resolveEndpoints:]
+ -[MRAVDistantRoutingDiscoverySession distantLocalEndpoint]
+ -[MRAVDistantRoutingDiscoverySession localEndpoint]
+ -[MRAVDistantRoutingDiscoverySession setDistantLocalEndpoint:]
+ -[MRAVDistantRoutingDiscoverySession setLocalEndpoint:]
+ -[MRAVEndpoint _modifyTopologyWithRequest:withReplyQueue:completion:]
+ -[MRAVEndpoint modifyTopologyWithRequest:withReplyQueue:completion:]
+ -[MRAVEndpoint(Deprecated) addOutputDevices:initiator:fadeAudio:withReplyQueue:completion:]
+ -[MRAVEndpoint(Deprecated) addOutputDevices:initiator:fadeAudio:withReplyQueue:completion:].cold.1
+ -[MRAVEndpoint(Deprecated) addOutputDevices:initiator:withReplyQueue:completion:]
+ -[MRAVEndpoint(Deprecated) removeOutputDevices:initiator:fadeAudio:withReplyQueue:completion:]
+ -[MRAVEndpoint(Deprecated) removeOutputDevices:initiator:fadeAudio:withReplyQueue:completion:].cold.1
+ -[MRAVEndpoint(Deprecated) removeOutputDevices:initiator:withReplyQueue:completion:]
+ -[MRAVEndpoint(Deprecated) setOutputDevices:initiator:fadeAudio:withReplyQueue:completion:]
+ -[MRAVEndpoint(Deprecated) setOutputDevices:initiator:fadeAudio:withReplyQueue:completion:].cold.1
+ -[MRAVEndpoint(Deprecated) setOutputDevices:initiator:withReplyQueue:completion:]
+ -[MRAVOutputContext modifyTopologyWithRequest:withReplyQueue:completion:]
+ -[MRAVOutputContext(Deprecated) addOutputDevices:initiator:fadeAudio:withCallbackQueue:block:]
+ -[MRAVOutputContext(Deprecated) addOutputDevices:initiator:withCallbackQueue:block:]
+ -[MRAVOutputContext(Deprecated) addOutputDevices:withCallbackQueue:block:]
+ -[MRAVOutputContext(Deprecated) removeAllOutputDevicesWithCallbackQueue:block:]
+ -[MRAVOutputContext(Deprecated) removeOutputDevices:initiator:fadeAudio:withCallbackQueue:block:]
+ -[MRAVOutputContext(Deprecated) removeOutputDevices:initiator:withCallbackQueue:block:]
+ -[MRAVOutputContext(Deprecated) removeOutputDevices:withCallbackQueue:block:]
+ -[MRAVOutputContext(Deprecated) setOutputDevices:initiator:password:fadeAudio:withCallbackQueue:block:]
+ -[MRAVOutputContext(Deprecated) setOutputDevices:initiator:withCallbackQueue:block:]
+ -[MRAVOutputContext(Deprecated) setOutputDevices:withCallbackQueue:block:]
+ -[MRAVOutputContext(Deprecated) setOutputDevices:withPassword:withCallbackQueue:block:]
+ -[MRAVOutputContextEndpoint _modifyTopologyWithRequest:withReplyQueue:completion:]
+ -[MRAVOutputContextModification discoveredConcreteOutputDevices]
+ -[MRAVOutputContextModification discoveredOutputDeviceUIDs]
+ -[MRAVOutputContextModification initWithRequest:]
+ -[MRAVOutputContextModification request]
+ -[MRAVOutputDevice isB238Device]
+ -[MRAVOutputDevice isB620Device]
+ -[MRAVRoutingDiscoverySession endpointsSnapshot]
+ -[MRAVRoutingDiscoverySession notifyAvailableEndpointsChanged:discoveredEndpoints:]
+ -[MRAVRoutingDiscoverySession outputDevicesSnapshot]
+ -[MRAVRoutingDiscoverySession setEndpointsSnapshot:]
+ -[MRAVRoutingDiscoverySession setOutputDevicesSnapshot:]
+ -[MRClient isAirPlay]
+ -[MRContentItem artworks]
+ -[MRContentItem availableArtworkFormats]
+ -[MRContentItem availableRemoteArtworkFormats]
+ -[MRContentItem remoteArtworks]
+ -[MRContentItem setArtworks:]
+ -[MRContentItem setAvailableArtworkFormats:]
+ -[MRContentItem setAvailableRemoteArtworkFormats:]
+ -[MRContentItem setRemoteArtworks:]
+ -[MRDataArtwork .cxx_destruct]
+ -[MRDataArtwork copyWithZone:]
+ -[MRDataArtwork description]
+ -[MRDataArtwork dimensions]
+ -[MRDataArtwork imageData]
+ -[MRDataArtwork initWithImageData:]
+ -[MRDataArtwork initWithImageData:].cold.1
+ -[MRDataArtwork initWithProtobuf:]
+ -[MRDistantExternalDevice modifyTopologyWithRequest:withReplyQueue:completion:]
+ -[MRExternalDevice modifyTopologyWithRequest:withReplyQueue:completion:]
+ -[MRGroupTopologyModificationRequest .cxx_destruct]
+ -[MRGroupTopologyModificationRequest copyWithOutputDeviceUIDs:]
+ -[MRGroupTopologyModificationRequest copyWithType:outputDeviceUIDs:]
+ -[MRGroupTopologyModificationRequest copyWithZone:]
+ -[MRGroupTopologyModificationRequest data]
+ -[MRGroupTopologyModificationRequest encodeWithCoder:]
+ -[MRGroupTopologyModificationRequest fadeAudio]
+ -[MRGroupTopologyModificationRequest initWithCoder:]
+ -[MRGroupTopologyModificationRequest initWithData:]
+ -[MRGroupTopologyModificationRequest initWithProtobuf:]
+ -[MRGroupTopologyModificationRequest initWithRequestDetails:type:outputDeviceUIDs:]
+ -[MRGroupTopologyModificationRequest initWithRequestDetails:type:outputDevices:]
+ -[MRGroupTopologyModificationRequest outputDeviceUIDs]
+ -[MRGroupTopologyModificationRequest outputDevices]
+ -[MRGroupTopologyModificationRequest password]
+ -[MRGroupTopologyModificationRequest protobuf]
+ -[MRGroupTopologyModificationRequest requestDetails]
+ -[MRGroupTopologyModificationRequest setFadeAudio:]
+ -[MRGroupTopologyModificationRequest setPassword:]
+ -[MRGroupTopologyModificationRequest setShouldNotPauseIfLastDeviceRemoved:]
+ -[MRGroupTopologyModificationRequest setSuppressErrorDialog:]
+ -[MRGroupTopologyModificationRequest shouldNotPauseIfLastDeviceRemoved]
+ -[MRGroupTopologyModificationRequest suppressErrorDialog]
+ -[MRGroupTopologyModificationRequest type]
+ -[MRMediaRemoteService fetchParticipantsWithRequest:playerPath:queue:completion:]
+ -[MRMediaRemoteService userIdentityForDSID:queue:completion:]
+ -[MRMediaSuggestion _processedIntentWithRouteIdentifiers:]
+ -[MRMediaSuggestion playWithAirPlayRouteIdentifiers:completion:]
+ -[MRMediaSuggestionElectedDeviceObserver .cxx_destruct]
+ -[MRMediaSuggestionElectedDeviceObserver delegate]
+ -[MRMediaSuggestionElectedDeviceObserver deviceAvailableForMediaSuggestionsNotification:]
+ -[MRMediaSuggestionElectedDeviceObserver electedDeviceIdentifier]
+ -[MRMediaSuggestionElectedDeviceObserver initWithDelegate:]
+ -[MRMediaSuggestionElectedDeviceObserver setDelegate:]
+ -[MRMediaSuggestionElectedDeviceObserver start]
+ -[MRMediaSuggestionElectedDeviceObserver stop]
+ -[MRModifyOutputContextRequestMessage .cxx_destruct]
+ -[MRModifyOutputContextRequestMessage initWithRequest:]
+ -[MRModifyOutputContextRequestMessage request]
+ -[MRNowPlayingAudioFormatController faceTimeBundleSet]
+ -[MRNowPlayingAudioFormatController firstContentInfoMatchingSet:contentInfos:]
+ -[MRNowPlayingPlayerClientCallbacks availableArtworkFormatsCallbacks]
+ -[MRNowPlayingPlayerClientCallbacks formattedArtworkCallbacks]
+ -[MRPlaybackQueueParticipant .cxx_destruct]
+ -[MRPlaybackQueueParticipant copyWithZone:]
+ -[MRPlaybackQueueParticipant description]
+ -[MRPlaybackQueueParticipant dictionaryRepresentation]
+ -[MRPlaybackQueueParticipant identifier]
+ -[MRPlaybackQueueParticipant identity]
+ -[MRPlaybackQueueParticipant initWithIdentifier:identity:]
+ -[MRPlaybackQueueParticipant initWithProtobuf:]
+ -[MRPlaybackQueueParticipant initWithProtobufData:]
+ -[MRPlaybackQueueParticipant protobufData]
+ -[MRPlaybackQueueParticipant protobufWithEncoding:]
+ -[MRPlaybackQueueParticipant setIdentifier:]
+ -[MRPlaybackQueueParticipant setIdentity:]
+ -[MRPlaybackQueueRequest hasIncludeAvailableArtworkFormats]
+ -[MRPlaybackQueueRequest includeAvailableArtworkFormats]
+ -[MRPlaybackQueueRequest includeRemoteArtwork]
+ -[MRPlaybackQueueRequest requestedArtworkFormats]
+ -[MRPlaybackQueueRequest requestedRemoteArtworkFormats]
+ -[MRPlaybackQueueRequest setHasIncludeAvailableArtworkFormats:]
+ -[MRPlaybackQueueRequest setIncludeAvailableArtworkFormats:]
+ -[MRPlaybackQueueRequest setRequestedArtworkFormats:]
+ -[MRPlaybackQueueRequest setRequestedRemoteArtworkFormats:]
+ -[MRPlayerClientParticipantsUpdateMessage initWithPlayerPath:participants:]
+ -[MRPlayerClientParticipantsUpdateMessage participants]
+ -[MRPlayerClientParticipantsUpdateMessage playerPath]
+ -[MRPlayerClientParticipantsUpdateMessage type]
+ -[MRRemoteArtwork .cxx_destruct]
+ -[MRRemoteArtwork artworkURLString]
+ -[MRRemoteArtwork artworkURLTemplateData]
+ -[MRRemoteArtwork copyWithZone:]
+ -[MRRemoteArtwork description]
+ -[MRRemoteArtwork initWithArtworkURLString:templateData:]
+ -[MRRemoteArtwork initWithProtobuf:]
+ -[MRSharedSettings suppressScreenMirroringErrors]
+ -[MRUserSettings groupSessionAttributionValidityDuration]
+ -[MRUserSettings recentGroupSessionParticipantsPepper]
+ -[MRUserSettings supportElectedPlayer]
+ -[MRUserSettings supportGroupSessionAttribution]
+ -[MRUserSettings supportGroupSessionAutoApproval]
+ -[MRUserSettings supportSystemEndpoints]
+ -[MRUserSettings suppressScreenMirroringErrors]
+ -[NSArray(MRAVAdditions) mr_distantEndpoints]
+ -[NSArray(MRAVAdditions) mr_distantOutputDevices]
+ -[NSArray(MRAVAdditions) mr_replaceEndpointsWithEndpoints:]
+ -[NSArray(MRAVAdditions) mr_replaceOutputDevicesWithOutputDevices:]
+ -[_MRAVModifyOutputContextRequestProtobuf hasRequest]
+ -[_MRAVModifyOutputContextRequestProtobuf request]
+ -[_MRAVModifyOutputContextRequestProtobuf setRequest:]
+ -[_MRCommandOptionsProtobuf associatedParticipantIdentifier]
+ -[_MRCommandOptionsProtobuf hasAssociatedParticipantIdentifier]
+ -[_MRCommandOptionsProtobuf setAssociatedParticipantIdentifier:]
+ -[_MRContentItemProtobuf addAvailableArtworkFormats:]
+ -[_MRContentItemProtobuf addAvailableRemoteArtworkFormats:]
+ -[_MRContentItemProtobuf addDataArtworks:]
+ -[_MRContentItemProtobuf addRemoteArtworks:]
+ -[_MRContentItemProtobuf availableArtworkFormatsAtIndex:]
+ -[_MRContentItemProtobuf availableArtworkFormatsCount]
+ -[_MRContentItemProtobuf availableArtworkFormats]
+ -[_MRContentItemProtobuf availableRemoteArtworkFormatsAtIndex:]
+ -[_MRContentItemProtobuf availableRemoteArtworkFormatsCount]
+ -[_MRContentItemProtobuf availableRemoteArtworkFormats]
+ -[_MRContentItemProtobuf clearAvailableArtworkFormats]
+ -[_MRContentItemProtobuf clearAvailableRemoteArtworkFormats]
+ -[_MRContentItemProtobuf clearDataArtworks]
+ -[_MRContentItemProtobuf clearRemoteArtworks]
+ -[_MRContentItemProtobuf dataArtworksAtIndex:]
+ -[_MRContentItemProtobuf dataArtworksCount]
+ -[_MRContentItemProtobuf dataArtworks]
+ -[_MRContentItemProtobuf remoteArtworksAtIndex:]
+ -[_MRContentItemProtobuf remoteArtworksCount]
+ -[_MRContentItemProtobuf remoteArtworks]
+ -[_MRContentItemProtobuf setAvailableArtworkFormats:]
+ -[_MRContentItemProtobuf setAvailableRemoteArtworkFormats:]
+ -[_MRContentItemProtobuf setDataArtworks:]
+ -[_MRContentItemProtobuf setRemoteArtworks:]
+ -[_MRDataArtworkProtobuf .cxx_destruct]
+ -[_MRDataArtworkProtobuf copyTo:]
+ -[_MRDataArtworkProtobuf copyWithZone:]
+ -[_MRDataArtworkProtobuf description]
+ -[_MRDataArtworkProtobuf dictionaryRepresentation]
+ -[_MRDataArtworkProtobuf hasImageData]
+ -[_MRDataArtworkProtobuf hasType]
+ -[_MRDataArtworkProtobuf hash]
+ -[_MRDataArtworkProtobuf imageData]
+ -[_MRDataArtworkProtobuf isEqual:]
+ -[_MRDataArtworkProtobuf mergeFrom:]
+ -[_MRDataArtworkProtobuf readFrom:]
+ -[_MRDataArtworkProtobuf setImageData:]
+ -[_MRDataArtworkProtobuf setType:]
+ -[_MRDataArtworkProtobuf type]
+ -[_MRDataArtworkProtobuf writeTo:]
+ -[_MRGroupTopologyModificationRequestProtobuf .cxx_destruct]
+ -[_MRGroupTopologyModificationRequestProtobuf StringAsType:]
+ -[_MRGroupTopologyModificationRequestProtobuf addOutputDeviceUIDs:]
+ -[_MRGroupTopologyModificationRequestProtobuf clearOutputDeviceUIDs]
+ -[_MRGroupTopologyModificationRequestProtobuf copyTo:]
+ -[_MRGroupTopologyModificationRequestProtobuf copyWithZone:]
+ -[_MRGroupTopologyModificationRequestProtobuf description]
+ -[_MRGroupTopologyModificationRequestProtobuf details]
+ -[_MRGroupTopologyModificationRequestProtobuf dictionaryRepresentation]
+ -[_MRGroupTopologyModificationRequestProtobuf fadeAudio]
+ -[_MRGroupTopologyModificationRequestProtobuf hasDetails]
+ -[_MRGroupTopologyModificationRequestProtobuf hasFadeAudio]
+ -[_MRGroupTopologyModificationRequestProtobuf hasPassword]
+ -[_MRGroupTopologyModificationRequestProtobuf hasShouldNotPauseIfLastDeviceRemoved]
+ -[_MRGroupTopologyModificationRequestProtobuf hasSuppressErrorDialog]
+ -[_MRGroupTopologyModificationRequestProtobuf hasType]
+ -[_MRGroupTopologyModificationRequestProtobuf hash]
+ -[_MRGroupTopologyModificationRequestProtobuf isEqual:]
+ -[_MRGroupTopologyModificationRequestProtobuf mergeFrom:]
+ -[_MRGroupTopologyModificationRequestProtobuf outputDeviceUIDsAtIndex:]
+ -[_MRGroupTopologyModificationRequestProtobuf outputDeviceUIDsCount]
+ -[_MRGroupTopologyModificationRequestProtobuf outputDeviceUIDs]
+ -[_MRGroupTopologyModificationRequestProtobuf password]
+ -[_MRGroupTopologyModificationRequestProtobuf readFrom:]
+ -[_MRGroupTopologyModificationRequestProtobuf setDetails:]
+ -[_MRGroupTopologyModificationRequestProtobuf setFadeAudio:]
+ -[_MRGroupTopologyModificationRequestProtobuf setHasFadeAudio:]
+ -[_MRGroupTopologyModificationRequestProtobuf setHasShouldNotPauseIfLastDeviceRemoved:]
+ -[_MRGroupTopologyModificationRequestProtobuf setHasSuppressErrorDialog:]
+ -[_MRGroupTopologyModificationRequestProtobuf setHasType:]
+ -[_MRGroupTopologyModificationRequestProtobuf setOutputDeviceUIDs:]
+ -[_MRGroupTopologyModificationRequestProtobuf setPassword:]
+ -[_MRGroupTopologyModificationRequestProtobuf setShouldNotPauseIfLastDeviceRemoved:]
+ -[_MRGroupTopologyModificationRequestProtobuf setSuppressErrorDialog:]
+ -[_MRGroupTopologyModificationRequestProtobuf setType:]
+ -[_MRGroupTopologyModificationRequestProtobuf shouldNotPauseIfLastDeviceRemoved]
+ -[_MRGroupTopologyModificationRequestProtobuf suppressErrorDialog]
+ -[_MRGroupTopologyModificationRequestProtobuf typeAsString:]
+ -[_MRGroupTopologyModificationRequestProtobuf type]
+ -[_MRGroupTopologyModificationRequestProtobuf writeTo:]
+ -[_MRMediaRemoteMessageProtobuf hasPlayerClientParticipantsUpdateMessage]
+ -[_MRMediaRemoteMessageProtobuf playerClientParticipantsUpdateMessage]
+ -[_MRMediaRemoteMessageProtobuf setPlayerClientParticipantsUpdateMessage:]
+ -[_MRPlaybackQueueParticipantProtobuf .cxx_destruct]
+ -[_MRPlaybackQueueParticipantProtobuf copyTo:]
+ -[_MRPlaybackQueueParticipantProtobuf copyWithZone:]
+ -[_MRPlaybackQueueParticipantProtobuf description]
+ -[_MRPlaybackQueueParticipantProtobuf dictionaryRepresentation]
+ -[_MRPlaybackQueueParticipantProtobuf hasIdentifier]
+ -[_MRPlaybackQueueParticipantProtobuf hasIdentity]
+ -[_MRPlaybackQueueParticipantProtobuf hash]
+ -[_MRPlaybackQueueParticipantProtobuf identifier]
+ -[_MRPlaybackQueueParticipantProtobuf identity]
+ -[_MRPlaybackQueueParticipantProtobuf isEqual:]
+ -[_MRPlaybackQueueParticipantProtobuf mergeFrom:]
+ -[_MRPlaybackQueueParticipantProtobuf readFrom:]
+ -[_MRPlaybackQueueParticipantProtobuf setIdentifier:]
+ -[_MRPlaybackQueueParticipantProtobuf setIdentity:]
+ -[_MRPlaybackQueueParticipantProtobuf writeTo:]
+ -[_MRPlaybackQueueRequestProtobuf addRequestedArtworkFormats:]
+ -[_MRPlaybackQueueRequestProtobuf addRequestedRemoteArtworkFormats:]
+ -[_MRPlaybackQueueRequestProtobuf clearRequestedArtworkFormats]
+ -[_MRPlaybackQueueRequestProtobuf clearRequestedRemoteArtworkFormats]
+ -[_MRPlaybackQueueRequestProtobuf hasIncludeAvailableArtworkFormats]
+ -[_MRPlaybackQueueRequestProtobuf includeAvailableArtworkFormats]
+ -[_MRPlaybackQueueRequestProtobuf requestedArtworkFormatsAtIndex:]
+ -[_MRPlaybackQueueRequestProtobuf requestedArtworkFormatsCount]
+ -[_MRPlaybackQueueRequestProtobuf requestedArtworkFormats]
+ -[_MRPlaybackQueueRequestProtobuf requestedRemoteArtworkFormatsAtIndex:]
+ -[_MRPlaybackQueueRequestProtobuf requestedRemoteArtworkFormatsCount]
+ -[_MRPlaybackQueueRequestProtobuf requestedRemoteArtworkFormats]
+ -[_MRPlaybackQueueRequestProtobuf setHasIncludeAvailableArtworkFormats:]
+ -[_MRPlaybackQueueRequestProtobuf setIncludeAvailableArtworkFormats:]
+ -[_MRPlaybackQueueRequestProtobuf setRequestedArtworkFormats:]
+ -[_MRPlaybackQueueRequestProtobuf setRequestedRemoteArtworkFormats:]
+ -[_MRPlayerClientParticipantsUpdateMessageProtobuf .cxx_destruct]
+ -[_MRPlayerClientParticipantsUpdateMessageProtobuf addParticipants:]
+ -[_MRPlayerClientParticipantsUpdateMessageProtobuf clearParticipants]
+ -[_MRPlayerClientParticipantsUpdateMessageProtobuf copyTo:]
+ -[_MRPlayerClientParticipantsUpdateMessageProtobuf copyWithZone:]
+ -[_MRPlayerClientParticipantsUpdateMessageProtobuf description]
+ -[_MRPlayerClientParticipantsUpdateMessageProtobuf dictionaryRepresentation]
+ -[_MRPlayerClientParticipantsUpdateMessageProtobuf hasPlayerPath]
+ -[_MRPlayerClientParticipantsUpdateMessageProtobuf hash]
+ -[_MRPlayerClientParticipantsUpdateMessageProtobuf isEqual:]
+ -[_MRPlayerClientParticipantsUpdateMessageProtobuf mergeFrom:]
+ -[_MRPlayerClientParticipantsUpdateMessageProtobuf participantsAtIndex:]
+ -[_MRPlayerClientParticipantsUpdateMessageProtobuf participantsCount]
+ -[_MRPlayerClientParticipantsUpdateMessageProtobuf participants]
+ -[_MRPlayerClientParticipantsUpdateMessageProtobuf playerPath]
+ -[_MRPlayerClientParticipantsUpdateMessageProtobuf readFrom:]
+ -[_MRPlayerClientParticipantsUpdateMessageProtobuf setParticipants:]
+ -[_MRPlayerClientParticipantsUpdateMessageProtobuf setPlayerPath:]
+ -[_MRPlayerClientParticipantsUpdateMessageProtobuf writeTo:]
+ -[_MRRemoteArtworkProtobuf .cxx_destruct]
+ -[_MRRemoteArtworkProtobuf artworkURLString]
+ -[_MRRemoteArtworkProtobuf artworkURLTemplateData]
+ -[_MRRemoteArtworkProtobuf copyTo:]
+ -[_MRRemoteArtworkProtobuf copyWithZone:]
+ -[_MRRemoteArtworkProtobuf description]
+ -[_MRRemoteArtworkProtobuf dictionaryRepresentation]
+ -[_MRRemoteArtworkProtobuf hasArtworkURLString]
+ -[_MRRemoteArtworkProtobuf hasArtworkURLTemplateData]
+ -[_MRRemoteArtworkProtobuf hasType]
+ -[_MRRemoteArtworkProtobuf hash]
+ -[_MRRemoteArtworkProtobuf isEqual:]
+ -[_MRRemoteArtworkProtobuf mergeFrom:]
+ -[_MRRemoteArtworkProtobuf readFrom:]
+ -[_MRRemoteArtworkProtobuf setArtworkURLString:]
+ -[_MRRemoteArtworkProtobuf setArtworkURLTemplateData:]
+ -[_MRRemoteArtworkProtobuf setType:]
+ -[_MRRemoteArtworkProtobuf type]
+ -[_MRRemoteArtworkProtobuf writeTo:]
+ GCC_except_table109
+ GCC_except_table196
+ GCC_except_table197
+ GCC_except_table248
+ GCC_except_table283
+ OBJC_IVAR_$__MRAVModifyOutputContextRequestProtobuf._request
+ OBJC_IVAR_$__MRCommandOptionsProtobuf._associatedParticipantIdentifier
+ OBJC_IVAR_$__MRContentItemProtobuf._availableArtworkFormats
+ OBJC_IVAR_$__MRContentItemProtobuf._availableRemoteArtworkFormats
+ OBJC_IVAR_$__MRContentItemProtobuf._dataArtworks
+ OBJC_IVAR_$__MRContentItemProtobuf._remoteArtworks
+ OBJC_IVAR_$__MRDataArtworkProtobuf._imageData
+ OBJC_IVAR_$__MRDataArtworkProtobuf._type
+ OBJC_IVAR_$__MRGroupTopologyModificationRequestProtobuf._details
+ OBJC_IVAR_$__MRGroupTopologyModificationRequestProtobuf._fadeAudio
+ OBJC_IVAR_$__MRGroupTopologyModificationRequestProtobuf._has
+ OBJC_IVAR_$__MRGroupTopologyModificationRequestProtobuf._outputDeviceUIDs
+ OBJC_IVAR_$__MRGroupTopologyModificationRequestProtobuf._password
+ OBJC_IVAR_$__MRGroupTopologyModificationRequestProtobuf._shouldNotPauseIfLastDeviceRemoved
+ OBJC_IVAR_$__MRGroupTopologyModificationRequestProtobuf._suppressErrorDialog
+ OBJC_IVAR_$__MRGroupTopologyModificationRequestProtobuf._type
+ OBJC_IVAR_$__MRMediaRemoteMessageProtobuf._playerClientParticipantsUpdateMessage
+ OBJC_IVAR_$__MRPlaybackQueueParticipantProtobuf._identifier
+ OBJC_IVAR_$__MRPlaybackQueueParticipantProtobuf._identity
+ OBJC_IVAR_$__MRPlaybackQueueRequestProtobuf._includeAvailableArtworkFormats
+ OBJC_IVAR_$__MRPlaybackQueueRequestProtobuf._requestedArtworkFormats
+ OBJC_IVAR_$__MRPlaybackQueueRequestProtobuf._requestedRemoteArtworkFormats
+ OBJC_IVAR_$__MRPlayerClientParticipantsUpdateMessageProtobuf._participants
+ OBJC_IVAR_$__MRPlayerClientParticipantsUpdateMessageProtobuf._playerPath
+ OBJC_IVAR_$__MRRemoteArtworkProtobuf._artworkURLString
+ OBJC_IVAR_$__MRRemoteArtworkProtobuf._artworkURLTemplateData
+ OBJC_IVAR_$__MRRemoteArtworkProtobuf._type
+ _AVOutputContextAddOutputDeviceOptionDidFailToConnectToOutputDeviceUserInfoFunction
+ _AVOutputContextRemoveOutputDeviceOptionDidFailToConnectToOutputDeviceUserInfoFunction
+ _AVOutputContextSetOutputDeviceDidFailToConnectToOutputDeviceUserInfoKeyFunction
+ _AVOutputContextSetOutputDevicesOptionDidFailToConnectToOutputDeviceUserInfoFunction
+ _CC_MD5_Final
+ _CC_MD5_Update
+ _CC_SHA1_Final
+ _CC_SHA1_Init
+ _CC_SHA1_Update
+ _CC_SHA256_Final
+ _CC_SHA256_Update
+ _CC_SHA512_Final
+ _CC_SHA512_Update
+ _CFStringCreateWithBytes
+ _MRAVOutputDeviceB238ModelID
+ _MRAVOutputDeviceB620ModelID
+ _MRContentItemArtworkFormatStandard
+ _MRContentItemMerge.cold.1
+ _MRGroupTopologyModificationRequestTypeDescription
+ _MRIRServiceTokenKey
+ _MRMediaRemotePlaybackQueueDataSourceAddContentItemAvailableArtworkFormatsCallback
+ _MRMediaRemotePlaybackQueueDataSourceAddContentItemAvailableArtworkFormatsCallbackForPlayer
+ _MRMediaRemotePlaybackQueueDataSourceAddContentItemFormattedArtworkCallback
+ _MRMediaRemotePlaybackQueueDataSourceAddContentItemFormattedArtworkCallbackForPlayer
+ _MRPlaybackQueueParticipantsDidChangeForPlayerNotification
+ _MSVFastHexStringFromBytes.hexCharacters
+ _MSVNanoIDCreateTaggedPointer
+ _OBJC_CLASS_$_MRDataArtwork
+ _OBJC_CLASS_$_MRGroupTopologyModificationRequest
+ _OBJC_CLASS_$_MRMediaSuggestionElectedDeviceObserver
+ _OBJC_CLASS_$_MRPlaybackQueueParticipant
+ _OBJC_CLASS_$_MRPlaybackQueueParticipantRequest
+ _OBJC_CLASS_$_MRPlayerClientParticipantsUpdateMessage
+ _OBJC_CLASS_$_MRRemoteArtwork
+ _OBJC_CLASS_$__MRDataArtworkProtobuf
+ _OBJC_CLASS_$__MRGroupTopologyModificationRequestProtobuf
+ _OBJC_CLASS_$__MRPlaybackQueueParticipantProtobuf
+ _OBJC_CLASS_$__MRPlayerClientParticipantsUpdateMessageProtobuf
+ _OBJC_CLASS_$__MRRemoteArtworkProtobuf
+ _OBJC_IVAR_$_MRAVDistantRoutingDiscoverySession._distantLocalEndpoint
+ _OBJC_IVAR_$_MRAVDistantRoutingDiscoverySession._localEndpoint
+ _OBJC_IVAR_$_MRAVOutputContextModification._discoveredConcreteOutputDevices
+ _OBJC_IVAR_$_MRAVOutputContextModification._request
+ _OBJC_IVAR_$_MRAVRoutingClientController._callbackQueue
+ _OBJC_IVAR_$_MRAVRoutingDiscoverySession._endpointsSnapshot
+ _OBJC_IVAR_$_MRAVRoutingDiscoverySession._outputDevicesSnapshot
+ _OBJC_IVAR_$_MRContentItem._artworks
+ _OBJC_IVAR_$_MRContentItem._availableArtworkFormats
+ _OBJC_IVAR_$_MRContentItem._availableRemoteArtworkFormats
+ _OBJC_IVAR_$_MRContentItem._remoteArtworks
+ _OBJC_IVAR_$_MRDataArtwork._dimensions
+ _OBJC_IVAR_$_MRDataArtwork._imageData
+ _OBJC_IVAR_$_MRGroupTopologyModificationRequest._fadeAudio
+ _OBJC_IVAR_$_MRGroupTopologyModificationRequest._outputDeviceUIDs
+ _OBJC_IVAR_$_MRGroupTopologyModificationRequest._outputDevices
+ _OBJC_IVAR_$_MRGroupTopologyModificationRequest._password
+ _OBJC_IVAR_$_MRGroupTopologyModificationRequest._requestDetails
+ _OBJC_IVAR_$_MRGroupTopologyModificationRequest._shouldNotPauseIfLastDeviceRemoved
+ _OBJC_IVAR_$_MRGroupTopologyModificationRequest._suppressErrorDialog
+ _OBJC_IVAR_$_MRGroupTopologyModificationRequest._type
+ _OBJC_IVAR_$_MRMediaSuggestionElectedDeviceObserver._delegate
+ _OBJC_IVAR_$_MRMediaSuggestionElectedDeviceObserver._electedDeviceIdentifier
+ _OBJC_IVAR_$_MRModifyOutputContextRequestMessage._request
+ _OBJC_IVAR_$_MRNowPlayingPlayerClientCallbacks._availableArtworkFormatsCallbacks
+ _OBJC_IVAR_$_MRNowPlayingPlayerClientCallbacks._formattedArtworkCallbacks
+ _OBJC_IVAR_$_MRPlaybackQueueParticipant._identifier
+ _OBJC_IVAR_$_MRPlaybackQueueParticipant._identity
+ _OBJC_IVAR_$_MRPlaybackQueueRequest._hasIncludeAvailableArtworkFormats
+ _OBJC_IVAR_$_MRPlaybackQueueRequest._includeAvailableArtworkFormats
+ _OBJC_IVAR_$_MRPlaybackQueueRequest._requestedArtworkFormats
+ _OBJC_IVAR_$_MRPlaybackQueueRequest._requestedRemoteArtworkFormats
+ _OBJC_IVAR_$_MRRemoteArtwork._artworkURLString
+ _OBJC_IVAR_$_MRRemoteArtwork._artworkURLTemplateData
+ _OBJC_METACLASS_$_MRDataArtwork
+ _OBJC_METACLASS_$_MRGroupTopologyModificationRequest
+ _OBJC_METACLASS_$_MRMediaSuggestionElectedDeviceObserver
+ _OBJC_METACLASS_$_MRPlaybackQueueParticipant
+ _OBJC_METACLASS_$_MRPlaybackQueueParticipantRequest
+ _OBJC_METACLASS_$_MRPlayerClientParticipantsUpdateMessage
+ _OBJC_METACLASS_$_MRRemoteArtwork
+ _OBJC_METACLASS_$__MRDataArtworkProtobuf
+ _OBJC_METACLASS_$__MRGroupTopologyModificationRequestProtobuf
+ _OBJC_METACLASS_$__MRPlaybackQueueParticipantProtobuf
+ _OBJC_METACLASS_$__MRPlayerClientParticipantsUpdateMessageProtobuf
+ _OBJC_METACLASS_$__MRRemoteArtworkProtobuf
+ __MRDataArtworkProtobufReadFrom
+ __MRGroupTopologyModificationRequestProtobufReadFrom
+ __MRMediaRemoteDeviceAvailableForMediaSuggestionsNotification
+ __MRPlaybackQueueParticipantProtobufReadFrom
+ __MRPlayerClientParticipantsUpdateMessageProtobufReadFrom
+ __MRRemoteArtworkProtobufReadFrom
+ __OBJC_$_CLASS_METHODS_MRAVOutputContext(Deprecated)
+ __OBJC_$_CLASS_METHODS_MRGroupTopologyModificationRequest
+ __OBJC_$_CLASS_METHODS_MRPlaybackQueueParticipant
+ __OBJC_$_CLASS_METHODS_MRPlaybackQueueParticipantRequest
+ __OBJC_$_CLASS_METHODS__MRGroupTopologyModificationRequestProtobuf
+ __OBJC_$_CLASS_METHODS__MRPlayerClientParticipantsUpdateMessageProtobuf
+ __OBJC_$_CLASS_PROP_LIST_MRGroupTopologyModificationRequest
+ __OBJC_$_INSTANCE_METHODS_MRAVOutputContext(Deprecated)
+ __OBJC_$_INSTANCE_METHODS_MRDataArtwork
+ __OBJC_$_INSTANCE_METHODS_MRGroupTopologyModificationRequest
+ __OBJC_$_INSTANCE_METHODS_MRMediaSuggestionElectedDeviceObserver
+ __OBJC_$_INSTANCE_METHODS_MRPlaybackQueueParticipant
+ __OBJC_$_INSTANCE_METHODS_MRPlayerClientParticipantsUpdateMessage
+ __OBJC_$_INSTANCE_METHODS_MRRemoteArtwork
+ __OBJC_$_INSTANCE_METHODS__MRDataArtworkProtobuf
+ __OBJC_$_INSTANCE_METHODS__MRGroupTopologyModificationRequestProtobuf
+ __OBJC_$_INSTANCE_METHODS__MRPlaybackQueueParticipantProtobuf
+ __OBJC_$_INSTANCE_METHODS__MRPlayerClientParticipantsUpdateMessageProtobuf
+ __OBJC_$_INSTANCE_METHODS__MRRemoteArtworkProtobuf
+ __OBJC_$_INSTANCE_VARIABLES_MRDataArtwork
+ __OBJC_$_INSTANCE_VARIABLES_MRGroupTopologyModificationRequest
+ __OBJC_$_INSTANCE_VARIABLES_MRMediaSuggestionElectedDeviceObserver
+ __OBJC_$_INSTANCE_VARIABLES_MRModifyOutputContextRequestMessage
+ __OBJC_$_INSTANCE_VARIABLES_MRPlaybackQueueParticipant
+ __OBJC_$_INSTANCE_VARIABLES_MRRemoteArtwork
+ __OBJC_$_INSTANCE_VARIABLES__MRDataArtworkProtobuf
+ __OBJC_$_INSTANCE_VARIABLES__MRGroupTopologyModificationRequestProtobuf
+ __OBJC_$_INSTANCE_VARIABLES__MRPlaybackQueueParticipantProtobuf
+ __OBJC_$_INSTANCE_VARIABLES__MRPlayerClientParticipantsUpdateMessageProtobuf
+ __OBJC_$_INSTANCE_VARIABLES__MRRemoteArtworkProtobuf
+ __OBJC_$_PROP_LIST_MRDataArtwork
+ __OBJC_$_PROP_LIST_MRGroupTopologyModificationRequest
+ __OBJC_$_PROP_LIST_MRMediaSuggestionElectedDeviceObserver
+ __OBJC_$_PROP_LIST_MRPlaybackQueueParticipant
+ __OBJC_$_PROP_LIST_MRPlayerClientParticipantsUpdateMessage
+ __OBJC_$_PROP_LIST_MRRemoteArtwork
+ __OBJC_$_PROP_LIST__MRDataArtworkProtobuf
+ __OBJC_$_PROP_LIST__MRGroupTopologyModificationRequestProtobuf
+ __OBJC_$_PROP_LIST__MRPlaybackQueueParticipantProtobuf
+ __OBJC_$_PROP_LIST__MRPlayerClientParticipantsUpdateMessageProtobuf
+ __OBJC_$_PROP_LIST__MRRemoteArtworkProtobuf
+ __OBJC_CLASS_PROTOCOLS_$_MRDataArtwork
+ __OBJC_CLASS_PROTOCOLS_$_MRGroupTopologyModificationRequest
+ __OBJC_CLASS_PROTOCOLS_$_MRPlaybackQueueParticipant
+ __OBJC_CLASS_PROTOCOLS_$_MRRemoteArtwork
+ __OBJC_CLASS_PROTOCOLS_$__MRDataArtworkProtobuf
+ __OBJC_CLASS_PROTOCOLS_$__MRGroupTopologyModificationRequestProtobuf
+ __OBJC_CLASS_PROTOCOLS_$__MRPlaybackQueueParticipantProtobuf
+ __OBJC_CLASS_PROTOCOLS_$__MRPlayerClientParticipantsUpdateMessageProtobuf
+ __OBJC_CLASS_PROTOCOLS_$__MRRemoteArtworkProtobuf
+ __OBJC_CLASS_RO_$_MRDataArtwork
+ __OBJC_CLASS_RO_$_MRGroupTopologyModificationRequest
+ __OBJC_CLASS_RO_$_MRMediaSuggestionElectedDeviceObserver
+ __OBJC_CLASS_RO_$_MRPlaybackQueueParticipant
+ __OBJC_CLASS_RO_$_MRPlaybackQueueParticipantRequest
+ __OBJC_CLASS_RO_$_MRPlayerClientParticipantsUpdateMessage
+ __OBJC_CLASS_RO_$_MRRemoteArtwork
+ __OBJC_CLASS_RO_$__MRDataArtworkProtobuf
+ __OBJC_CLASS_RO_$__MRGroupTopologyModificationRequestProtobuf
+ __OBJC_CLASS_RO_$__MRPlaybackQueueParticipantProtobuf
+ __OBJC_CLASS_RO_$__MRPlayerClientParticipantsUpdateMessageProtobuf
+ __OBJC_CLASS_RO_$__MRRemoteArtworkProtobuf
+ __OBJC_METACLASS_RO_$_MRDataArtwork
+ __OBJC_METACLASS_RO_$_MRGroupTopologyModificationRequest
+ __OBJC_METACLASS_RO_$_MRMediaSuggestionElectedDeviceObserver
+ __OBJC_METACLASS_RO_$_MRPlaybackQueueParticipant
+ __OBJC_METACLASS_RO_$_MRPlaybackQueueParticipantRequest
+ __OBJC_METACLASS_RO_$_MRPlayerClientParticipantsUpdateMessage
+ __OBJC_METACLASS_RO_$_MRRemoteArtwork
+ __OBJC_METACLASS_RO_$__MRDataArtworkProtobuf
+ __OBJC_METACLASS_RO_$__MRGroupTopologyModificationRequestProtobuf
+ __OBJC_METACLASS_RO_$__MRPlaybackQueueParticipantProtobuf
+ __OBJC_METACLASS_RO_$__MRPlayerClientParticipantsUpdateMessageProtobuf
+ __OBJC_METACLASS_RO_$__MRRemoteArtworkProtobuf
+ ___103-[MRAVOutputContext(Deprecated) setOutputDevices:initiator:password:fadeAudio:withCallbackQueue:block:]_block_invoke
+ ___104+[MRPlaybackQueueParticipant fetchPlaybackQueueParticipantIdentifierForLocalAccountWithDSID:completion:]_block_invoke
+ ___122-[MRDistantExternalDevice _onSerialQueue_prepareToConnectWithOptions:userInfo:connectionAttemptDetails:connectionHandler:]_block_invoke.270
+ ___122-[MRDistantExternalDevice _onSerialQueue_prepareToConnectWithOptions:userInfo:connectionAttemptDetails:connectionHandler:]_block_invoke_2.271
+ ___36+[MRIRRoute routeWithOutputDevices:]_block_invoke.106
+ ___37-[MRDistantExternalDevice deviceInfo]_block_invoke.213
+ ___37-[MRDistantExternalDevice deviceInfo]_block_invoke_2.214
+ ___39-[MRDistantExternalDevice customOrigin]_block_invoke.217
+ ___39-[MRDistantExternalDevice customOrigin]_block_invoke_2.219
+ ___43-[MRUserSettings calculateDiscoveryUpdates]_block_invoke
+ ___45-[NSArray(MRAVAdditions) mr_distantEndpoints]_block_invoke
+ ___46-[MRGroupTopologyModificationRequest protobuf]_block_invoke
+ ___48-[MRAVRoutingDiscoverySession endpointsSnapshot]_block_invoke
+ ___48-[MRDistantExternalDevice externalOutputContext]_block_invoke.210
+ ___48-[MRDistantExternalDevice personalOutputDevices]_block_invoke.288
+ ___49-[NSArray(MRAVAdditions) mr_distantOutputDevices]_block_invoke
+ ___50+[MRUserIdentity fetchIdentityForDSID:completion:]_block_invoke
+ ___51-[MRAVDistantRoutingDiscoverySession localEndpoint]_block_invoke
+ ___52-[MRAVRoutingDiscoverySession outputDevicesSnapshot]_block_invoke
+ ___52-[MRAVRoutingDiscoverySession setEndpointsSnapshot:]_block_invoke
+ ___54-[MRNowPlayingAudioFormatController faceTimeBundleSet]_block_invoke
+ ___54-[MRUserSettings recentGroupSessionParticipantsPepper]_block_invoke
+ ___55-[MRAVDistantRoutingDiscoverySession setDiscoveryMode:]_block_invoke.75
+ ___56-[MRAVDistantRoutingDiscoverySession _resolveEndpoints:]_block_invoke
+ ___57-[MRAVConcreteOutputContext attemptLogicalDeviceRecovery]_block_invoke.62
+ ___57-[MRAVConcreteOutputContext attemptLogicalDeviceRecovery]_block_invoke.62.cold.1
+ ___57-[MRAVConcreteOutputContext attemptLogicalDeviceRecovery]_block_invoke.62.cold.2
+ ___57-[MRAVConcreteOutputContext attemptLogicalDeviceRecovery]_block_invoke.62.cold.3
+ ___57-[MRAVConcreteOutputContext attemptLogicalDeviceRecovery]_block_invoke.68
+ ___57-[MRAVConcreteOutputContext attemptLogicalDeviceRecovery]_block_invoke.68.cold.1
+ ___58-[MRAVDistantRoutingDiscoverySession distantLocalEndpoint]_block_invoke
+ ___59-[MRAVOutputContextModification discoveredOutputDeviceUIDs]_block_invoke
+ ___60-[MRAVDistantRoutingDiscoverySession devicePresenceDetected]_block_invoke.77
+ ___60-[MRAVDistantRoutingDiscoverySession devicePresenceDetected]_block_invoke.77.cold.1
+ ___60-[MRAVDistantRoutingDiscoverySession initWithConfiguration:]_block_invoke
+ ___61-[MRAVDistantRoutingDiscoverySession _notifyEndpointsChanged]_block_invoke
+ ___61-[MRMediaRemoteService userIdentityForDSID:queue:completion:]_block_invoke
+ ___63-[MRAVDistantRoutingDiscoverySession _resolveDistantEndpoints:]_block_invoke
+ ___64-[MRMediaSuggestion playWithAirPlayRouteIdentifiers:completion:]_block_invoke
+ ___65-[MRDistantExternalDevice hostedExternalDeviceEndpointDidChange:]_block_invoke.292
+ ___66-[MRDistantExternalDevice connectWithOptions:userInfo:completion:]_block_invoke.254
+ ___66-[MRDistantExternalDevice hostedExternalDeviceDidAddOutputDevice:]_block_invoke.297
+ ___67-[MRDistantExternalDevice hostedExternalDeviceDeviceInfoDidChange:]_block_invoke.290
+ ___68-[MRAVEndpoint modifyTopologyWithRequest:withReplyQueue:completion:]_block_invoke
+ ___69-[MRAVEndpoint _modifyTopologyWithRequest:withReplyQueue:completion:]_block_invoke
+ ___69-[MRAVEndpoint _modifyTopologyWithRequest:withReplyQueue:completion:]_block_invoke_2
+ ___69-[MRAVEndpoint _modifyTopologyWithRequest:withReplyQueue:completion:]_block_invoke_3
+ ___69-[MRAVEndpoint _modifyTopologyWithRequest:withReplyQueue:completion:]_block_invoke_4
+ ___69-[MRDistantExternalDevice hostedExternalDeviceDidChangeOutputDevice:]_block_invoke.298
+ ___69-[MRDistantExternalDevice hostedExternalDeviceDidRemoveOutputDevice:]_block_invoke.299
+ ___71-[MRAVOutputContextModification _notifyWillAddDevices:toOutputContext:]_block_invoke.180
+ ___72-[MRAVDistantRoutingDiscoverySession setHostedRoutingSessionConnection:]_block_invoke.79
+ ___72-[MRAVDistantRoutingDiscoverySession setHostedRoutingSessionConnection:]_block_invoke_2.81
+ ___74-[MRAVOutputContextModification modifyWithOutputContext:queue:completion:]_block_invoke.34
+ ___75-[MRAVOutputContextModification _modifyWithOutputContext:queue:completion:]_block_invoke.51
+ ___76-[MRAVOutputContextModification _notifyRequestToAddDevices:toOutputContext:]_block_invoke.173
+ ___76-[MRAVOutputContextModification _notifyWillRemoveDevices:fromOutputContext:]_block_invoke.194
+ ___77-[MRDistantExternalDevice hostedExternalDeviceDidReceiveCustomData:withName:]_block_invoke.291
+ ___79-[MRAVOutputContext(Deprecated) removeAllOutputDevicesWithCallbackQueue:block:]_block_invoke
+ ___79-[MRDistantExternalDevice hostedExternalDeviceVolumeDidChange:forOutputDevice:]_block_invoke.295
+ ___79-[MRDistantExternalDevice modifyTopologyWithRequest:withReplyQueue:completion:]_block_invoke
+ ___79-[MRDistantExternalDevice modifyTopologyWithRequest:withReplyQueue:completion:]_block_invoke_2
+ ___79-[MRDistantExternalDevice modifyTopologyWithRequest:withReplyQueue:completion:]_block_invoke_3
+ ___80-[MRDistantExternalDevice hostedExternalDeviceIsMutedDidChange:forOutputDevice:]_block_invoke.296
+ ___80-[MRGroupTopologyModificationRequest initWithRequestDetails:type:outputDevices:]_block_invoke
+ ___81-[MRAVOutputContextModification _notifyRequestToRemoveDevices:fromOutputContext:]_block_invoke.187
+ ___81-[MRMediaRemoteService fetchParticipantsWithRequest:playerPath:queue:completion:]_block_invoke
+ ___81-[MRMediaRemoteService fetchParticipantsWithRequest:playerPath:queue:completion:]_block_invoke_2
+ ___87-[MRAVOutputContextModification performModificationWithOutputContext:queue:completion:]_block_invoke.105
+ ___87-[MRAVOutputContextModification performModificationWithOutputContext:queue:completion:]_block_invoke.105.cold.1
+ ___87-[MRAVOutputContextModification performModificationWithOutputContext:queue:completion:]_block_invoke.106
+ ___87-[MRAVOutputContextModification performModificationWithOutputContext:queue:completion:]_block_invoke.113
+ ___87-[MRAVOutputContextModification performModificationWithOutputContext:queue:completion:]_block_invoke.120
+ ___87-[MRAVOutputContextModification performModificationWithOutputContext:queue:completion:]_block_invoke.126
+ ___87-[MRAVOutputContextModification performModificationWithOutputContext:queue:completion:]_block_invoke.134
+ ___87-[MRAVOutputContextModification performModificationWithOutputContext:queue:completion:]_block_invoke.140
+ ___87-[MRAVOutputContextModification performModificationWithOutputContext:queue:completion:]_block_invoke.158
+ ___87-[MRAVOutputContextModification performModificationWithOutputContext:queue:completion:]_block_invoke_2.135
+ ___87-[MRAVOutputContextModification performModificationWithOutputContext:queue:completion:]_block_invoke_2.150
+ ___87-[MRAVOutputContextModification performModificationWithOutputContext:queue:completion:]_block_invoke_2.159
+ ___90+[MRPlaybackQueueParticipant fetchParticipantsWithRequest:forPlayerPath:queue:completion:]_block_invoke
+ ___90+[MRPlaybackQueueParticipant fetchParticipantsWithRequest:forPlayerPath:queue:completion:]_block_invoke.20
+ ___90+[MRPlaybackQueueParticipant fetchParticipantsWithRequest:forPlayerPath:queue:completion:]_block_invoke.22
+ ___90+[MRPlaybackQueueParticipant fetchParticipantsWithRequest:forPlayerPath:queue:completion:]_block_invoke_2
+ ___90-[MRDistantExternalDevice setOutputDeviceVolume:outputDeviceUID:details:queue:completion:]_block_invoke.277
+ ___91-[MRDistantExternalDevice hostedExternalDeviceVolumeCapabilitiesDidChange:forOutputDevice:]_block_invoke.294
+ ___91-[MRDistantExternalDevice muteOutputDeviceVolume:outputDeviceUID:details:queue:completion:]_block_invoke.286
+ ___93-[MRDistantExternalDevice adjustOutputDeviceVolume:outputDeviceUID:details:queue:completion:]_block_invoke.282
+ ___94-[MRAVOutputContext(Deprecated) addOutputDevices:initiator:fadeAudio:withCallbackQueue:block:]_block_invoke
+ ___97-[MRAVOutputContext(Deprecated) removeOutputDevices:initiator:fadeAudio:withCallbackQueue:block:]_block_invoke
+ ___99-[MRAVOutputContextModification waitForOutputContextModificationVerification:initiator:completion:]_block_invoke.72
+ ___99-[MRAVOutputContextModification waitForOutputContextModificationVerification:initiator:completion:]_block_invoke.76
+ ___MRAVEndpointGetMyGroupLeaderWithTimeout_block_invoke.166
+ ___MRAVEndpointModifyOutputDevicesInGroup_block_invoke.129
+ ___MRAVEndpointModifyOutputDevicesInGroup_block_invoke.129.cold.1
+ ___MRAVEndpointModifyOutputDevicesInGroup_block_invoke.139
+ ___MRAVEndpointModifyOutputDevicesInGroup_block_invoke.143
+ ___MRAVEndpointModifyOutputDevicesInGroup_block_invoke.145
+ ___MRAVEndpointModifyOutputDevicesInGroup_block_invoke.145.cold.1
+ ___MRAVEndpointModifyOutputDevicesInGroup_block_invoke.155
+ ___MRAVEndpointModifyOutputDevicesInGroup_block_invoke.157
+ ___MRAVEndpointModifyOutputDevicesInGroup_block_invoke.89
+ ___MRAVEndpointModifyOutputDevicesInGroup_block_invoke.92
+ ___MRAVEndpointModifyOutputDevicesInGroup_block_invoke.99
+ ___MRAVEndpointModifyOutputDevicesInGroup_block_invoke.cold.1
+ ___MRCreateDecodedUserInfo_block_invoke.103
+ ___MRCreateDecodedUserInfo_block_invoke.94
+ ___MRCreateDecodedUserInfo_block_invoke_2.108
+ ___MRCreateDecodedUserInfo_block_invoke_2.97
+ ___MRCreateDecodedUserInfo_block_invoke_3.100
+ ___MRCreateDecodedUserInfo_block_invoke_3.111
+ ___MRCreateDecodedUserInfo_block_invoke_4.114
+ ___MRCreateDecodedUserInfo_block_invoke_5.117
+ ___MRCreateEncodedUserInfo_block_invoke.145
+ ___MRCreateEncodedUserInfo_block_invoke_2.149
+ ___MRCreateEncodedUserInfo_block_invoke_3.152
+ ___MRCreateEncodedUserInfo_block_invoke_4.156
+ ___MRCreateEncodedUserInfo_block_invoke_5.160
+ ___MRCreateEncodedUserInfo_block_invoke_6.164
+ ___MRMediaRemoteGetMediaPlaybackVolumeForOrigin_block_invoke.117
+ ___MRMediaRemoteGetPickedRoutedVolumeControlCapabilities_block_invoke.82
+ ___MRMediaRemoteGetPickedRoutedVolumeControlCapabilities_block_invoke.94
+ ___MRNowPlayingSessionManagerStartSession_block_invoke.67
+ ____MRHandlePlaybackQueueRequest_block_invoke.55
+ ____onQueue_MRInvokeClientAssetCallbacks_block_invoke_7
+ ____onQueue_MRInvokeClientAssetCallbacks_block_invoke_8
+ ___block_descriptor_40_e8_32bs_e36_v24?0"MRUserIdentity"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32s_e29_16?0"MRAVDistantEndpoint"8ls32l8
+ ___block_descriptor_40_e8_32s_e29_B16?0"MRAVDistantEndpoint"8ls32l8
+ ___block_descriptor_48_e8_32s40s_e33_B16?0"MRAVDistantOutputDevice"8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e45_v24?0"NSObject<OS_xpc_object>"8"NSError"16ls32l8s48l8s40l8
+ ___block_descriptor_64_e8_32s40s48bs56r_e17_v16?0"NSError"8lr56l8s32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e24_v24?0^v8^{__CFError=}16ls32l8s56l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e45_v24?0"NSObject<OS_xpc_object>"8"NSError"16ls32l8s40l8s48l8s56l8
+ ___block_descriptor_68_e8_32s40s48bs_e17_v16?0"NSError"8ls32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e34_v24?0"MRDeviceInfo"8"NSError"16ls64l8s32l8s40l8s48l8s56l8
+ ___block_descriptor_96_e8_32s40s48s56s64s72s80bs_e46_v32?0"MRAVEndpoint"8"NSArray"16"NSError"24ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
+ ___block_literal_global.104
+ ___block_literal_global.134
+ ___block_literal_global.151
+ ___block_literal_global.157
+ ___block_literal_global.164
+ ___block_literal_global.168
+ ___block_literal_global.170
+ ___block_literal_global.171
+ ___block_literal_global.173
+ ___block_literal_global.174
+ ___block_literal_global.176
+ ___block_literal_global.177
+ ___block_literal_global.179
+ ___block_literal_global.184
+ ___block_literal_global.186
+ ___block_literal_global.189
+ ___block_literal_global.191
+ ___block_literal_global.193
+ ___block_literal_global.196
+ ___block_literal_global.202
+ ___block_literal_global.207
+ ___block_literal_global.232
+ ___block_literal_global.242
+ ___block_literal_global.39
+ ___block_literal_global.54
+ ___block_literal_global.62
+ ___block_literal_global.677
+ ___block_literal_global.70
+ ___block_literal_global.88
+ ___block_literal_global.91
+ ___block_literal_global.93
+ ___block_literal_global.96
+ _calculateDiscoveryUpdates.onceToken
+ _calculateDiscoveryUpdates.support
+ _constantValAVOutputContextAddOutputDeviceOptionDidFailToConnectToOutputDeviceUserInfo
+ _constantValAVOutputContextRemoveOutputDeviceOptionDidFailToConnectToOutputDeviceUserInfo
+ _constantValAVOutputContextSetOutputDeviceDidFailToConnectToOutputDeviceUserInfoKey
+ _constantValAVOutputContextSetOutputDevicesOptionDidFailToConnectToOutputDeviceUserInfo
+ _faceTimeBundleSet.__set
+ _faceTimeBundleSet.onceToken
+ _getAVOutputContextAddOutputDeviceOptionDidFailToConnectToOutputDeviceUserInfo
+ _getAVOutputContextRemoveOutputDeviceOptionDidFailToConnectToOutputDeviceUserInfo
+ _getAVOutputContextSetOutputDeviceDidFailToConnectToOutputDeviceUserInfoKey
+ _getAVOutputContextSetOutputDevicesOptionDidFailToConnectToOutputDeviceUserInfo
+ _initValAVOutputContextAddOutputDeviceOptionDidFailToConnectToOutputDeviceUserInfo
+ _initValAVOutputContextRemoveOutputDeviceOptionDidFailToConnectToOutputDeviceUserInfo
+ _initValAVOutputContextSetOutputDeviceDidFailToConnectToOutputDeviceUserInfoKey
+ _initValAVOutputContextSetOutputDevicesOptionDidFailToConnectToOutputDeviceUserInfo
+ _kMRMediaRemoteOptionAssociatedParticipantIdentifier
+ _ldiv
+ _lldiv
+ _malloc_type_calloc
+ _objc_msgSend$_modifyTopologyWithRequest:withReplyQueue:completion:
+ _objc_msgSend$_notifyEndpointsChanged
+ _objc_msgSend$_resolveDistantEndpoints:
+ _objc_msgSend$_resolveEndpoints:
+ _objc_msgSend$addAvailableArtworkFormats:
+ _objc_msgSend$addAvailableRemoteArtworkFormats:
+ _objc_msgSend$addDataArtworks:
+ _objc_msgSend$addOutputDevices:initiator:fadeAudio:withReplyQueue:completion:
+ _objc_msgSend$addRemoteArtworks:
+ _objc_msgSend$addRequestedArtworkFormats:
+ _objc_msgSend$addRequestedRemoteArtworkFormats:
+ _objc_msgSend$artworkURLString
+ _objc_msgSend$artworkURLTemplateData
+ _objc_msgSend$artworks
+ _objc_msgSend$availableArtworkFormats
+ _objc_msgSend$availableArtworkFormatsAtIndex:
+ _objc_msgSend$availableArtworkFormatsCallbacks
+ _objc_msgSend$availableArtworkFormatsCount
+ _objc_msgSend$availableRemoteArtworkFormats
+ _objc_msgSend$availableRemoteArtworkFormatsAtIndex:
+ _objc_msgSend$availableRemoteArtworkFormatsCount
+ _objc_msgSend$clearAvailableArtworkFormats
+ _objc_msgSend$clearAvailableRemoteArtworkFormats
+ _objc_msgSend$clearDataArtworks
+ _objc_msgSend$clearRemoteArtworks
+ _objc_msgSend$clearRequestedArtworkFormats
+ _objc_msgSend$clearRequestedRemoteArtworkFormats
+ _objc_msgSend$copyWithOutputDeviceUIDs:
+ _objc_msgSend$copyWithType:outputDeviceUIDs:
+ _objc_msgSend$dataArtworks
+ _objc_msgSend$dataArtworksAtIndex:
+ _objc_msgSend$dataArtworksCount
+ _objc_msgSend$dimensions
+ _objc_msgSend$discoveredConcreteOutputDevices
+ _objc_msgSend$distantLocalEndpoint
+ _objc_msgSend$endpointsSnapshot
+ _objc_msgSend$expectedIdentifierForUserIdentity:withRandomData:
+ _objc_msgSend$faceTimeBundleSet
+ _objc_msgSend$fadeAudio
+ _objc_msgSend$fetchParticipantsWithRequest:playerPath:queue:completion:
+ _objc_msgSend$firstContentInfoMatchingSet:contentInfos:
+ _objc_msgSend$formattedArtworkCallbacks
+ _objc_msgSend$hasIncludeAvailableArtworkFormats
+ _objc_msgSend$hasRequest
+ _objc_msgSend$includeAvailableArtworkFormats
+ _objc_msgSend$includeRemoteArtwork
+ _objc_msgSend$initWithArtworkURLString:templateData:
+ _objc_msgSend$initWithBytesNoCopy:length:encoding:freeWhenDone:
+ _objc_msgSend$initWithImageData:
+ _objc_msgSend$initWithRequestDetails:type:outputDeviceUIDs:
+ _objc_msgSend$initWithRequestDetails:type:outputDevices:
+ _objc_msgSend$isAirPlay
+ _objc_msgSend$localEndpoint
+ _objc_msgSend$mediaSuggestionElectedDeviceObserverDeviceDidChange:
+ _objc_msgSend$modifyTopologyWithRequest:completion:
+ _objc_msgSend$modifyTopologyWithRequest:withReplyQueue:completion:
+ _objc_msgSend$mr_distantEndpoints
+ _objc_msgSend$mr_distantOutputDevices
+ _objc_msgSend$mr_replaceEndpointsWithEndpoints:
+ _objc_msgSend$mr_replaceOutputDevicesWithOutputDevices:
+ _objc_msgSend$notifyAvailableEndpointsChanged:discoveredEndpoints:
+ _objc_msgSend$objCType
+ _objc_msgSend$playerClientParticipantsUpdateMessage
+ _objc_msgSend$remoteArtworks
+ _objc_msgSend$remoteArtworksAtIndex:
+ _objc_msgSend$remoteArtworksCount
+ _objc_msgSend$requestDetails
+ _objc_msgSend$requestedArtworkFormats
+ _objc_msgSend$requestedArtworkFormatsAtIndex:
+ _objc_msgSend$requestedArtworkFormatsCount
+ _objc_msgSend$requestedRemoteArtworkFormats
+ _objc_msgSend$requestedRemoteArtworkFormatsAtIndex:
+ _objc_msgSend$requestedRemoteArtworkFormatsCount
+ _objc_msgSend$setArtworkURLString:
+ _objc_msgSend$setArtworkURLTemplateData:
+ _objc_msgSend$setArtworks:
+ _objc_msgSend$setAvailableArtworkFormats:
+ _objc_msgSend$setAvailableRemoteArtworkFormats:
+ _objc_msgSend$setEndpointsSnapshot:
+ _objc_msgSend$setFadeAudio:
+ _objc_msgSend$setHasIncludeAvailableArtworkFormats:
+ _objc_msgSend$setIncludeAvailableArtworkFormats:
+ _objc_msgSend$setOutputDevicesSnapshot:
+ _objc_msgSend$setPlayerClientParticipantsUpdateMessage:
+ _objc_msgSend$setRemoteArtworks:
+ _objc_msgSend$setRequestedArtworkFormats:
+ _objc_msgSend$setRequestedRemoteArtworkFormats:
+ _objc_msgSend$setShouldNotPauseIfLastDeviceRemoved:
+ _objc_msgSend$setSuppressErrorDialog:
+ _objc_msgSend$shouldNotPauseIfLastDeviceRemoved
+ _objc_msgSend$stringForKey:
+ _objc_msgSend$supportSystemEndpoints
+ _objc_msgSend$suppressErrorDialog
+ _objc_msgSend$suppressScreenMirroringErrors
+ _objc_msgSend$userIdentityForDSID:queue:completion:
+ _recentGroupSessionParticipantsPepper.onceToken
+ _recentGroupSessionParticipantsPepper.pepper
+ _strcmp
- +[MRPlaybackQueueRequest defaultArtwortHeight]
- -[MRAVConcreteOutputContext addOutputDevices:initiator:fadeAudio:withCallbackQueue:block:]
- -[MRAVConcreteOutputContext removeAllOutputDevicesWithCallbackQueue:block:]
- -[MRAVConcreteOutputContext removeOutputDevices:initiator:fadeAudio:withCallbackQueue:block:]
- -[MRAVConcreteOutputContext setOutputDevices:initiator:password:fadeAudio:withCallbackQueue:block:]
- -[MRAVDistantRoutingDiscoverySession setDistantEndpoints:]
- -[MRAVDistantRoutingDiscoverySession setDistantOutputDevices:]
- -[MRAVEndpoint _requestSharedAudioPresentationOutputContextModificationWithAddingDevices:removingDevices:settingDevices:replyQueue:completion:]
- -[MRAVEndpoint addOutputDevices:initiator:fadeAudio:withReplyQueue:completion:]
- -[MRAVEndpoint addOutputDevices:initiator:fadeAudio:withReplyQueue:completion:].cold.1
- -[MRAVEndpoint addOutputDevices:initiator:withReplyQueue:completion:]
- -[MRAVEndpoint removeOutputDevices:initiator:withReplyQueue:completion:]
- -[MRAVEndpoint setOutputDevices:initiator:fadeAudio:withReplyQueue:completion:]
- -[MRAVEndpoint setOutputDevices:initiator:fadeAudio:withReplyQueue:completion:].cold.1
- -[MRAVEndpoint setOutputDevices:initiator:withReplyQueue:completion:]
- -[MRAVOutputContext addOutputDevices:initiator:fadeAudio:withCallbackQueue:block:]
- -[MRAVOutputContext addOutputDevices:initiator:withCallbackQueue:block:]
- -[MRAVOutputContext addOutputDevices:withCallbackQueue:block:]
- -[MRAVOutputContext removeAllOutputDevicesWithCallbackQueue:block:]
- -[MRAVOutputContext removeOutputDevices:initiator:fadeAudio:withCallbackQueue:block:]
- -[MRAVOutputContext removeOutputDevices:initiator:withCallbackQueue:block:]
- -[MRAVOutputContext removeOutputDevices:withCallbackQueue:block:]
- -[MRAVOutputContext setOutputDevices:initiator:password:fadeAudio:withCallbackQueue:block:]
- -[MRAVOutputContext setOutputDevices:initiator:withCallbackQueue:block:]
- -[MRAVOutputContext setOutputDevices:withCallbackQueue:block:]
- -[MRAVOutputContext setOutputDevices:withPassword:withCallbackQueue:block:]
- -[MRAVOutputContextEndpoint addOutputDevices:initiator:withReplyQueue:completion:]
- -[MRAVOutputContextEndpoint removeOutputDevices:initiator:withReplyQueue:completion:]
- -[MRAVOutputContextEndpoint setOutputDevices:initiator:fadeAudio:withReplyQueue:completion:]
- -[MRAVOutputContextEndpoint setOutputDevices:initiator:withReplyQueue:completion:]
- -[MRAVOutputContextModification concreteOutputDevices]
- -[MRAVOutputContextModification initWithType:devices:]
- -[MRAVOutputContextModification initiator]
- -[MRAVOutputContextModification modificationType]
- -[MRAVOutputContextModification outputDeviceUIDs]
- -[MRAVOutputContextModification outputDevices]
- -[MRAVOutputContextModification password]
- -[MRAVOutputContextModification setInitiator:]
- -[MRAVOutputContextModification setPassword:]
- -[MRAVOutputContextModification setShouldFadeAudio:]
- -[MRAVOutputContextModification shouldFadeAudio]
- -[MRAVRoutingDiscoverySession endpoints]
- -[MRAVRoutingDiscoverySession outputDevices]
- -[MRAVRoutingDiscoverySession setEndpoints:]
- -[MRAVRoutingDiscoverySession setOutputDevices:]
- -[MRDistantExternalDevice modifyByAddingDeviceUIDs:removingDeviceUIDs:settingDeviceUIDs:addingClusterAwareDeviceUIDs:removingClusterAwareDeviceUIDs:settingClusterAwareDeviceUIDs:withReplyQueue:completion:]
- -[MRExternalDevice modifyByAddingDeviceUIDs:removingDeviceUIDs:settingDeviceUIDs:addingClusterAwareDeviceUIDs:removingClusterAwareDeviceUIDs:settingClusterAwareDeviceUIDs:withReplyQueue:completion:]
- -[MRModifyOutputContextRequestMessage description]
- -[MRModifyOutputContextRequestMessage initWithAddingDeviceUIDs:removingDeviceUIDs:settingDeviceUIDs:clusterAwareAddingOutputDeviceUIDs:clusterAwareRemovingOutputDeviceUIDs:clusterAwareSettingOutputDeviceUIDs:]
- -[MRNowPlayingPlayerClientCallbacks createParticipantsCallbacks]
- -[MRPlaybackQueue participantForIdentifier:]
- -[MRPlaybackQueue participants]
- -[MRPlaybackQueue setParticipants:]
- -[MRPlaybackQueueRequest hasIncludeParticipants]
- -[MRPlaybackQueueRequest includeParticipants]
- -[MRPlaybackQueueRequest setHasIncludeParticipants:]
- -[MRPlaybackQueueRequest setIncludeParticipants:]
- -[MRUserSettings useProactiveEndpoint]
- -[MRVirtualOutputContext removeAllOutputDevicesWithCallbackQueue:block:]
- GCC_except_table119
- GCC_except_table206
- GCC_except_table207
- GCC_except_table278
- _MRAVOutputContextModificationTypeDescription
- _MRContentItemArtworkSatisfiesRequest
- _OBJC_IVAR_$_MRAVOutputContextModification._concreteOutputDevices
- _OBJC_IVAR_$_MRAVOutputContextModification._identifier
- _OBJC_IVAR_$_MRAVOutputContextModification._initiator
- _OBJC_IVAR_$_MRAVOutputContextModification._modificationType
- _OBJC_IVAR_$_MRAVOutputContextModification._outputDevices
- _OBJC_IVAR_$_MRAVOutputContextModification._password
- _OBJC_IVAR_$_MRAVOutputContextModification._shouldFadeAudio
- _OBJC_IVAR_$_MRAVRoutingDiscoverySession._endpoints
- _OBJC_IVAR_$_MRAVRoutingDiscoverySession._outputDevices
- _OBJC_IVAR_$_MRNowPlayingPlayerClientCallbacks._createParticipantsCallbacks
- _OBJC_IVAR_$_MRPlaybackQueue._participants
- _OBJC_IVAR_$_MRPlaybackQueueRequest._hasIncludeParticipants
- _OBJC_IVAR_$_MRPlaybackQueueRequest._includeParticipants
- __OBJC_$_CLASS_METHODS_MRAVOutputContext
- __OBJC_$_INSTANCE_METHODS_MRAVOutputContext
- ___122-[MRDistantExternalDevice _onSerialQueue_prepareToConnectWithOptions:userInfo:connectionAttemptDetails:connectionHandler:]_block_invoke.271
- ___122-[MRDistantExternalDevice _onSerialQueue_prepareToConnectWithOptions:userInfo:connectionAttemptDetails:connectionHandler:]_block_invoke_2.272
- ___143-[MRAVEndpoint _requestSharedAudioPresentationOutputContextModificationWithAddingDevices:removingDevices:settingDevices:replyQueue:completion:]_block_invoke
- ___143-[MRAVEndpoint _requestSharedAudioPresentationOutputContextModificationWithAddingDevices:removingDevices:settingDevices:replyQueue:completion:]_block_invoke_2
- ___143-[MRAVEndpoint _requestSharedAudioPresentationOutputContextModificationWithAddingDevices:removingDevices:settingDevices:replyQueue:completion:]_block_invoke_3
- ___143-[MRAVEndpoint _requestSharedAudioPresentationOutputContextModificationWithAddingDevices:removingDevices:settingDevices:replyQueue:completion:]_block_invoke_4
- ___143-[MRAVEndpoint _requestSharedAudioPresentationOutputContextModificationWithAddingDevices:removingDevices:settingDevices:replyQueue:completion:]_block_invoke_5
- ___205-[MRDistantExternalDevice modifyByAddingDeviceUIDs:removingDeviceUIDs:settingDeviceUIDs:addingClusterAwareDeviceUIDs:removingClusterAwareDeviceUIDs:settingClusterAwareDeviceUIDs:withReplyQueue:completion:]_block_invoke
- ___205-[MRDistantExternalDevice modifyByAddingDeviceUIDs:removingDeviceUIDs:settingDeviceUIDs:addingClusterAwareDeviceUIDs:removingClusterAwareDeviceUIDs:settingClusterAwareDeviceUIDs:withReplyQueue:completion:]_block_invoke_2
- ___205-[MRDistantExternalDevice modifyByAddingDeviceUIDs:removingDeviceUIDs:settingDeviceUIDs:addingClusterAwareDeviceUIDs:removingClusterAwareDeviceUIDs:settingClusterAwareDeviceUIDs:withReplyQueue:completion:]_block_invoke_3
- ___32-[MRPlaybackQueue copyWithZone:]_block_invoke_2
- ___36+[MRIRRoute routeWithOutputDevices:]_block_invoke.103
- ___36-[MRPlaybackQueue initWithProtobuf:]_block_invoke_2
- ___37-[MRDistantExternalDevice deviceInfo]_block_invoke.214
- ___37-[MRDistantExternalDevice deviceInfo]_block_invoke_2.215
- ___38-[MRUserSettings useProactiveEndpoint]_block_invoke
- ___39-[MRDistantExternalDevice customOrigin]_block_invoke.218
- ___39-[MRDistantExternalDevice customOrigin]_block_invoke_2.220
- ___40-[MRAVRoutingDiscoverySession endpoints]_block_invoke
- ___40-[MRPlaybackQueue protobufWithEncoding:]_block_invoke_2
- ___43-[MRPlaybackQueue dictionaryRepresentation]_block_invoke_2
- ___44-[MRAVRoutingDiscoverySession outputDevices]_block_invoke
- ___44-[MRAVRoutingDiscoverySession setEndpoints:]_block_invoke
- ___44-[MRAVRoutingDiscoverySession setEndpoints:]_block_invoke_2
- ___48-[MRAVRoutingDiscoverySession setOutputDevices:]_block_invoke
- ___48-[MRAVRoutingDiscoverySession setOutputDevices:]_block_invoke_2
- ___48-[MRDistantExternalDevice externalOutputContext]_block_invoke.211
- ___48-[MRDistantExternalDevice personalOutputDevices]_block_invoke.289
- ___49-[MRAVOutputContextModification encodeWithCoder:]_block_invoke
- ___49-[MRAVOutputContextModification outputDeviceUIDs]_block_invoke
- ___55-[MRAVDistantRoutingDiscoverySession setDiscoveryMode:]_block_invoke.76
- ___57-[MRAVConcreteOutputContext attemptLogicalDeviceRecovery]_block_invoke.63.cold.1
- ___57-[MRAVConcreteOutputContext attemptLogicalDeviceRecovery]_block_invoke.63.cold.2
- ___57-[MRAVConcreteOutputContext attemptLogicalDeviceRecovery]_block_invoke.63.cold.3
- ___57-[MRAVConcreteOutputContext attemptLogicalDeviceRecovery]_block_invoke.64
- ___57-[MRAVConcreteOutputContext attemptLogicalDeviceRecovery]_block_invoke.69
- ___57-[MRAVConcreteOutputContext attemptLogicalDeviceRecovery]_block_invoke.69.cold.1
- ___58-[MRAVDistantRoutingDiscoverySession setDistantEndpoints:]_block_invoke
- ___60-[MRAVDistantRoutingDiscoverySession devicePresenceDetected]_block_invoke.78
- ___60-[MRAVDistantRoutingDiscoverySession devicePresenceDetected]_block_invoke.78.cold.1
- ___62-[MRAVDistantRoutingDiscoverySession setDistantOutputDevices:]_block_invoke
- ___65-[MRDistantExternalDevice hostedExternalDeviceEndpointDidChange:]_block_invoke.293
- ___66-[MRDistantExternalDevice connectWithOptions:userInfo:completion:]_block_invoke.255
- ___66-[MRDistantExternalDevice hostedExternalDeviceDidAddOutputDevice:]_block_invoke.298
- ___67-[MRDistantExternalDevice hostedExternalDeviceDeviceInfoDidChange:]_block_invoke.291
- ___69-[MRAVEndpoint addOutputDevices:initiator:withReplyQueue:completion:]_block_invoke
- ___69-[MRAVEndpoint setOutputDevices:initiator:withReplyQueue:completion:]_block_invoke
- ___69-[MRDistantExternalDevice hostedExternalDeviceDidChangeOutputDevice:]_block_invoke.299
- ___69-[MRDistantExternalDevice hostedExternalDeviceDidRemoveOutputDevice:]_block_invoke.300
- ___71-[MRAVOutputContextModification _notifyWillAddDevices:toOutputContext:]_block_invoke.202
- ___72-[MRAVDistantRoutingDiscoverySession setHostedRoutingSessionConnection:]_block_invoke.81
- ___72-[MRAVDistantRoutingDiscoverySession setHostedRoutingSessionConnection:]_block_invoke_2.82
- ___72-[MRAVEndpoint removeOutputDevices:initiator:withReplyQueue:completion:]_block_invoke
- ___74-[MRAVOutputContextModification modifyWithOutputContext:queue:completion:]_block_invoke.56
- ___75-[MRAVOutputContextModification _modifyWithOutputContext:queue:completion:]_block_invoke.73
- ___76-[MRAVOutputContextModification _notifyRequestToAddDevices:toOutputContext:]_block_invoke.195
- ___76-[MRAVOutputContextModification _notifyWillRemoveDevices:fromOutputContext:]_block_invoke.216
- ___77-[MRDistantExternalDevice hostedExternalDeviceDidReceiveCustomData:withName:]_block_invoke.292
- ___79-[MRDistantExternalDevice hostedExternalDeviceVolumeDidChange:forOutputDevice:]_block_invoke.296
- ___80-[MRAVDistantRoutingDiscoverySession _registerForPerRoutingContextNotifications]_block_invoke_6
- ___80-[MRDistantExternalDevice hostedExternalDeviceIsMutedDidChange:forOutputDevice:]_block_invoke.297
- ___81-[MRAVOutputContextModification _notifyRequestToRemoveDevices:fromOutputContext:]_block_invoke.209
- ___82-[MRAVOutputContextEndpoint addOutputDevices:initiator:withReplyQueue:completion:]_block_invoke
- ___82-[MRAVOutputContextEndpoint setOutputDevices:initiator:withReplyQueue:completion:]_block_invoke
- ___85-[MRAVOutputContextEndpoint removeOutputDevices:initiator:withReplyQueue:completion:]_block_invoke
- ___87-[MRAVOutputContextModification performModificationWithOutputContext:queue:completion:]_block_invoke.128
- ___87-[MRAVOutputContextModification performModificationWithOutputContext:queue:completion:]_block_invoke.128.cold.1
- ___87-[MRAVOutputContextModification performModificationWithOutputContext:queue:completion:]_block_invoke.129
- ___87-[MRAVOutputContextModification performModificationWithOutputContext:queue:completion:]_block_invoke.136
- ___87-[MRAVOutputContextModification performModificationWithOutputContext:queue:completion:]_block_invoke.143
- ___87-[MRAVOutputContextModification performModificationWithOutputContext:queue:completion:]_block_invoke.149
- ___87-[MRAVOutputContextModification performModificationWithOutputContext:queue:completion:]_block_invoke.157
- ___87-[MRAVOutputContextModification performModificationWithOutputContext:queue:completion:]_block_invoke.163
- ___87-[MRAVOutputContextModification performModificationWithOutputContext:queue:completion:]_block_invoke.181
- ___87-[MRAVOutputContextModification performModificationWithOutputContext:queue:completion:]_block_invoke_2.158
- ___87-[MRAVOutputContextModification performModificationWithOutputContext:queue:completion:]_block_invoke_2.173
- ___87-[MRAVOutputContextModification performModificationWithOutputContext:queue:completion:]_block_invoke_2.182
- ___90-[MRAVConcreteOutputContext addOutputDevices:initiator:fadeAudio:withCallbackQueue:block:]_block_invoke
- ___90-[MRDistantExternalDevice setOutputDeviceVolume:outputDeviceUID:details:queue:completion:]_block_invoke.278
- ___91-[MRDistantExternalDevice hostedExternalDeviceVolumeCapabilitiesDidChange:forOutputDevice:]_block_invoke.295
- ___91-[MRDistantExternalDevice muteOutputDeviceVolume:outputDeviceUID:details:queue:completion:]_block_invoke.287
- ___92-[MRAVOutputContextEndpoint setOutputDevices:initiator:fadeAudio:withReplyQueue:completion:]_block_invoke
- ___93-[MRAVConcreteOutputContext removeOutputDevices:initiator:fadeAudio:withCallbackQueue:block:]_block_invoke
- ___93-[MRDistantExternalDevice adjustOutputDeviceVolume:outputDeviceUID:details:queue:completion:]_block_invoke.283
- ___99-[MRAVConcreteOutputContext setOutputDevices:initiator:password:fadeAudio:withCallbackQueue:block:]_block_invoke
- ___99-[MRAVOutputContextModification waitForOutputContextModificationVerification:initiator:completion:]_block_invoke.94
- ___99-[MRAVOutputContextModification waitForOutputContextModificationVerification:initiator:completion:]_block_invoke.98
- ___MRAVEndpointGetMyGroupLeaderWithTimeout_block_invoke.177
- ___MRAVEndpointModifyOutputDevicesInGroup_block_invoke.100
- ___MRAVEndpointModifyOutputDevicesInGroup_block_invoke.103
- ___MRAVEndpointModifyOutputDevicesInGroup_block_invoke.110
- ___MRAVEndpointModifyOutputDevicesInGroup_block_invoke.140
- ___MRAVEndpointModifyOutputDevicesInGroup_block_invoke.140.cold.1
- ___MRAVEndpointModifyOutputDevicesInGroup_block_invoke.156
- ___MRAVEndpointModifyOutputDevicesInGroup_block_invoke.156.cold.1
- ___MRAVEndpointModifyOutputDevicesInGroup_block_invoke.161
- ___MRAVEndpointModifyOutputDevicesInGroup_block_invoke.165
- ___MRAVEndpointModifyOutputDevicesInGroup_block_invoke.166
- ___MRAVEndpointModifyOutputDevicesInGroup_block_invoke.168
- ___MRAVEndpointModifyOutputDevicesInGroup_block_invoke.74
- ___MRAVEndpointModifyOutputDevicesInGroup_block_invoke.74.cold.1
- ___MRCreateDecodedUserInfo_block_invoke.87
- ___MRCreateDecodedUserInfo_block_invoke.96
- ___MRCreateDecodedUserInfo_block_invoke_2.101
- ___MRCreateDecodedUserInfo_block_invoke_2.90
- ___MRCreateDecodedUserInfo_block_invoke_3.104
- ___MRCreateDecodedUserInfo_block_invoke_3.93
- ___MRCreateDecodedUserInfo_block_invoke_4.107
- ___MRCreateDecodedUserInfo_block_invoke_5.110
- ___MRCreateEncodedUserInfo_block_invoke.138
- ___MRCreateEncodedUserInfo_block_invoke_2.142
- ___MRCreateEncodedUserInfo_block_invoke_3.145
- ___MRCreateEncodedUserInfo_block_invoke_4.149
- ___MRCreateEncodedUserInfo_block_invoke_5.153
- ___MRCreateEncodedUserInfo_block_invoke_6.157
- ___MRMediaRemoteGetMediaPlaybackVolumeForOrigin_block_invoke.114
- ___MRMediaRemoteGetPickedRoutedVolumeControlCapabilities_block_invoke.79
- ___MRMediaRemoteGetPickedRoutedVolumeControlCapabilities_block_invoke.91
- ____MRHandlePlaybackQueueRequest_block_invoke.57
- ____onQueue_MRLoadContentItemParticipants_block_invoke
- ___block_descriptor_104_e8_32s40s48s56s64s72s80bs88bs_e46_v32?0"MRAVEndpoint"8"NSArray"16"NSError"24ls32l8s40l8s48l8s56l8s80l8s64l8s72l8s88l8
- ___block_descriptor_32_e18_"NSString"16?0Q8l
- ___block_descriptor_40_e55_v32?0"NSArray"8"NSMutableArray"16"NSMutableArray"24l
- ___block_descriptor_48_e8_32s40r_e22_16?0"MRAVEndpoint"8lr40l8s32l8
- ___block_descriptor_48_e8_32s40s_e26_B16?0"MRAVOutputDevice"8ls32l8s40l8
- ___block_descriptor_76_e8_32s40s48s56bs_e17_v16?0"NSError"8ls56l8s32l8s40l8s48l8
- ___block_descriptor_80_e8_32s40s48s56s64s72bs_e21_v16?0^{__CFString=}8ls32l8s40l8s48l8s56l8s64l8s72l8
- ___block_descriptor_80_e8_32s40s48s56s64s72bs_e34_v24?0"MRDeviceInfo"8"NSError"16ls72l8s32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_96_e8_32s40s48s56s64s72s80s88bs_e5_v8?0ls32l8s88l8s40l8s48l8s56l8s64l8s72l8s80l8
- ___block_literal_global.103
- ___block_literal_global.107
- ___block_literal_global.108
- ___block_literal_global.115
- ___block_literal_global.117
- ___block_literal_global.118
- ___block_literal_global.127
- ___block_literal_global.133
- ___block_literal_global.135
- ___block_literal_global.141
- ___block_literal_global.152
- ___block_literal_global.156
- ___block_literal_global.160
- ___block_literal_global.162
- ___block_literal_global.169
- ___block_literal_global.180
- ___block_literal_global.19
- ___block_literal_global.192
- ___block_literal_global.194
- ___block_literal_global.197
- ___block_literal_global.199
- ___block_literal_global.200
- ___block_literal_global.201
- ___block_literal_global.203
- ___block_literal_global.204
- ___block_literal_global.208
- ___block_literal_global.218
- ___block_literal_global.234
- ___block_literal_global.282
- ___block_literal_global.33
- ___block_literal_global.46
- ___block_literal_global.58
- ___block_literal_global.63
- ___block_literal_global.65
- ___block_literal_global.673
- ___block_literal_global.72
- ___block_literal_global.80
- ___block_literal_global.95
- __dispatch_queue_attr_concurrent
- __onQueue_MRLoadContentItemParticipants
- _dispatch_barrier_async
- _dispatch_barrier_sync
- _objc_msgSend$addingOutputDeviceUIDs
- _objc_msgSend$createParticipantsCallbacks
- _objc_msgSend$hasIncludeParticipants
- _objc_msgSend$includeParticipants
- _objc_msgSend$initWithType:devices:
- _objc_msgSend$modificationType
- _objc_msgSend$modifyByAddingDeviceUIDs:removingDeviceUIDs:settingDeviceUIDs:addingClusterAwareDeviceUIDs:removingClusterAwareDeviceUIDs:settingClusterAwareDeviceUIDs:withReplyQueue:completion:
- _objc_msgSend$modifyByAddingDeviceUIDs:removingDeviceUIDs:settingDeviceUIDs:addingClusterDeviceUIDs:removingClusterDeviceUIDs:settingClusterDeviceUIDs:completion:
- _objc_msgSend$removingOutputDeviceUIDs
- _objc_msgSend$setAddingOutputDeviceUIDs:
- _objc_msgSend$setHasIncludeParticipants:
- _objc_msgSend$setIncludeParticipants:
- _objc_msgSend$setParticipants:
- _objc_msgSend$setRemovingOutputDeviceUIDs:
- _objc_msgSend$setSettingOutputDeviceUIDs:
- _objc_msgSend$setShouldFadeAudio:
- _objc_msgSend$settingOutputDeviceUIDs
- _objc_msgSend$shouldFadeAudio
- _useProactiveEndpoint.__value
- _useProactiveEndpoint.onceToken
CStrings:
+ "\x01\x11\x13\x15"
+ "\x02\x1f"
+ "\x0f\f"
+ "\x1f\x01\x1f\x0f\x0f\x0f\b\x1d"
+ "%@OutputDevices"
+ "-[MRAVOutputContext modifyTopologyWithRequest:withReplyQueue:completion:]"
+ "-[MRExternalDevice modifyTopologyWithRequest:withReplyQueue:completion:]"
+ "-[MRPlayerPath initWithOrigin:client:player:]"
+ "-[MRPlayerPath setClient:]"
+ "-[MRPlayerPath setOrigin:]"
+ "-[MRPlayerPath setPlayer:]"
+ "/AF"
+ "/FA[%ld]"
+ "/RFA[%ld]"
+ "0123456789abcdef"
+ "3\x14"
+ "<%@: %p | session id: %@ | audio format: %@ - %@ | channel #: %@ | available: %@ | eligible: %@ | active: %@ | intended :%ld | resolved :%ld | pid: %i | bundleID: %@>"
+ "<%@: data=%@, dim={%g,%g}"
+ "<%@: identifier=%@, identity=%@"
+ "<%@: url=%@, templates=%@"
+ "<MRAVOutputContextModification (%@) discovered=%@"
+ "<origin:%@:%d%@>"
+ "@\"<MRMediaSuggestionElectedDeviceObserverDelegate>\""
+ "@\"MRAVLocalEndpoint\""
+ "@\"MRGroupTopologyModificationRequest\""
+ "@\"MRRequestDetails\""
+ "@\"_MRGroupTopologyModificationRequestProtobuf\""
+ "@\"_MRPlayerClientParticipantsUpdateMessageProtobuf\""
+ "@16@?0@\"MRAVDistantEndpoint\"8"
+ "@40@0:8@16Q24@32"
+ "AVOutputContextAddOutputDeviceOptionDidFailToConnectToOutputDeviceUserInfo"
+ "AVOutputContextRemoveOutputDeviceOptionDidFailToConnectToOutputDeviceUserInfo"
+ "AVOutputContextSetOutputDeviceDidFailToConnectToOutputDeviceUserInfoKey"
+ "AVOutputContextSetOutputDevicesOptionDidFailToConnectToOutputDeviceUserInfo"
+ "AudioAccessory6"
+ "B16@?0@\"MRAVDistantEndpoint\"8"
+ "B16@?0@\"MRAVDistantOutputDevice\"8"
+ "Cannot append to unknown hasher algorithm"
+ "Cannot finalize unknown hasher algorithm"
+ "Cannot obtain digest from unknown hasher algorithm"
+ "Endpoint.addOutputDevices"
+ "Endpoint.modifyTopologyWithRequest"
+ "Endpoint.removeOutputDevices"
+ "Endpoint.setOutputDevices"
+ "FAULT: No type for artwork protobuf %@ in content item %@"
+ "GroupSessionAttribution"
+ "GroupSessionAttributionValidityDuration"
+ "IRServiceToken"
+ "MRAVRoutingDiscoverySession.m"
+ "MRContentItemArtworkFormatStandard"
+ "MRDataArtwork"
+ "MRExternalDeviceRequestOutputContextModification"
+ "MRGroupTopologyModificationRequest"
+ "MRMediaSuggestionElectedDeviceObserver"
+ "MRPlaybackQueueParticipant"
+ "MRPlaybackQueueParticipantRequest"
+ "MRPlaybackQueueParticipantsDidChangeForPlayerNotification"
+ "MRPlayerClientParticipantsUpdateMessage"
+ "MRRemoteArtwork"
+ "MRRemoteArtwork.m"
+ "MRXPC_DSID_KEY"
+ "MRXPC_PLAYBACKQUEUE_PARTICIPANTS"
+ "MSVHash _MSVHasherFinalize(MSVHasher * _Nonnull)"
+ "MSVHasher+Algorithms.h"
+ "Mismatch between available and discovered endpoint counts"
+ "NSString * _Nonnull _MSVHashGetDigest(MSVHash)"
+ "No artwork for requested format: %@"
+ "No remote artwork for requested format: %@"
+ "OutputContext.addOutputDevices"
+ "OutputContext.removeAllOutputDevices"
+ "OutputContext.removeOutputDevices"
+ "OutputContext.setOutputDevices"
+ "Posting Notification %@"
+ "Receieved Notification %@"
+ "RecentGroupSessionParticipantsPepper"
+ "SuppressScreenMirroringErrors"
+ "T@\"<MRMediaSuggestionElectedDeviceObserverDelegate>\",W,N,V_delegate"
+ "T@\"MRAVDistantEndpoint\",&,N,V_distantLocalEndpoint"
+ "T@\"MRAVLocalEndpoint\",&,N,V_localEndpoint"
+ "T@\"MRGroupTopologyModificationRequest\",R,N"
+ "T@\"MRGroupTopologyModificationRequest\",R,N,V_request"
+ "T@\"MRMediaControlsConfiguration\",R,N"
+ "T@\"MRRequestDetails\",R,N,V_requestDetails"
+ "T@\"MSVMultiCallback\",R,N,V_availableArtworkFormatsCallbacks"
+ "T@\"MSVMultiCallback\",R,N,V_formattedArtworkCallbacks"
+ "T@\"NSArray\",&,N,V_availableArtworkFormats"
+ "T@\"NSArray\",&,N,V_availableRemoteArtworkFormats"
+ "T@\"NSArray\",C,N,V_outputDevicesSnapshot"
+ "T@\"NSArray\",C,N,V_requestedArtworkFormats"
+ "T@\"NSArray\",C,N,V_requestedRemoteArtworkFormats"
+ "T@\"NSArray\",R,N,V_discoveredConcreteOutputDevices"
+ "T@\"NSArray\",R,N,V_outputDeviceUIDs"
+ "T@\"NSData\",&,N,V_artworkURLTemplateData"
+ "T@\"NSData\",R,N,V_artworkURLTemplateData"
+ "T@\"NSData\",R,N,V_imageData"
+ "T@\"NSDictionary\",&,N,V_artworks"
+ "T@\"NSDictionary\",&,N,V_remoteArtworks"
+ "T@\"NSMutableArray\",&,N,V_availableArtworkFormats"
+ "T@\"NSMutableArray\",&,N,V_availableRemoteArtworkFormats"
+ "T@\"NSMutableArray\",&,N,V_dataArtworks"
+ "T@\"NSMutableArray\",&,N,V_remoteArtworks"
+ "T@\"NSMutableArray\",&,N,V_requestedArtworkFormats"
+ "T@\"NSMutableArray\",&,N,V_requestedRemoteArtworkFormats"
+ "T@\"NSString\",&,N,V_artworkURLString"
+ "T@\"NSString\",N,V_password"
+ "T@\"NSString\",R,C,N,V_electedDeviceIdentifier"
+ "T@\"NSString\",R,N,V_artworkURLString"
+ "T@\"_MRGroupTopologyModificationRequestProtobuf\",&,N,V_request"
+ "T@\"_MRGroupTopologyModificationRequestProtobuf\",R,N"
+ "T@\"_MRPlaybackQueueContextProtobuf\",C,N,V_context"
+ "T@\"_MRPlayerClientParticipantsUpdateMessageProtobuf\",&,N,V_playerClientParticipantsUpdateMessage"
+ "TB,N,V_fadeAudio"
+ "TB,N,V_hasIncludeAvailableArtworkFormats"
+ "TB,N,V_includeAvailableArtworkFormats"
+ "TB,N,V_shouldNotPauseIfLastDeviceRemoved"
+ "TB,N,V_suppressErrorDialog"
+ "TB,R,N,GisAirPlay"
+ "TQ,R,N,V_type"
+ "T{CGSize=dd},R,N,V_dimensions"
+ "Unkown"
+ "Updating Endpoint: %{public}@ | %{public}@ bt output device: %{public}@ | %{public}@ | %{public}@"
+ "V"
+ "[MRNowPlayingPlayerClientRequests] %{public}@ UpdatingCache: clearing formatted data artworks for %{public}@"
+ "[MRNowPlayingPlayerClientRequests] %{public}@ UpdatingCache: clearing formatted remote artworks for %{public}@"
+ "[MRPlaybackQueueParticipantRequest]<%@> Response: %@"
+ "[MRPlaybackQueueParticipantRequest]<%@> for playerPath: %@"
+ "_MRDataArtworkProtobuf"
+ "_MRGroupTopologyModificationRequestProtobuf"
+ "_MRMediaRemoteDeviceAvailableForMediaSuggestionsNotification"
+ "_MRPlaybackQueueParticipantProtobuf"
+ "_MRPlayerClientParticipantsUpdateMessageProtobuf"
+ "_MRRemoteArtworkProtobuf"
+ "_artworkURLString"
+ "_artworkURLTemplateData"
+ "_artworks"
+ "_availableArtworkFormats"
+ "_availableArtworkFormatsCallbacks"
+ "_availableRemoteArtworkFormats"
+ "_dataArtworks"
+ "_dimensions"
+ "_discoveredConcreteOutputDevices"
+ "_distantLocalEndpoint"
+ "_electedDeviceIdentifier"
+ "_endpointsSnapshot"
+ "_fadeAudio"
+ "_formattedArtworkCallbacks"
+ "_hasIncludeAvailableArtworkFormats"
+ "_includeAvailableArtworkFormats"
+ "_localEndpoint"
+ "_modifyTopologyWithRequest:withReplyQueue:completion:"
+ "_notifyEndpointsChanged"
+ "_playerClientParticipantsUpdateMessage"
+ "_remoteArtworks"
+ "_requestDetails"
+ "_requestedArtworkFormats"
+ "_requestedRemoteArtworkFormats"
+ "_resolveDistantEndpoints:"
+ "_resolveEndpoints:"
+ "_shouldNotPauseIfLastDeviceRemoved"
+ "_suppressErrorDialog"
+ "addAvailableArtworkFormats:"
+ "addAvailableRemoteArtworkFormats:"
+ "addDataArtworks:"
+ "addOutputDevices:initiator:fadeAudio:withReplyQueue:completion:"
+ "addRemoteArtworks:"
+ "addRequestedArtworkFormats:"
+ "addRequestedRemoteArtworkFormats:"
+ "airPlay"
+ "artworkURLString"
+ "artworkURLString != nil || templateData != nil"
+ "artworkURLTemplateData"
+ "artworks"
+ "availableArtworkFormats"
+ "availableArtworkFormatsAtIndex:"
+ "availableArtworkFormatsCallbacks"
+ "availableArtworkFormatsCount"
+ "availableArtworkFormatsType"
+ "availableRemoteArtworkFormats"
+ "availableRemoteArtworkFormatsAtIndex:"
+ "availableRemoteArtworkFormatsCount"
+ "availableRemoteArtworkFormatsType"
+ "clearAvailableArtworkFormats"
+ "clearAvailableRemoteArtworkFormats"
+ "clearDataArtworks"
+ "clearRemoteArtworks"
+ "clearRequestedArtworkFormats"
+ "clearRequestedRemoteArtworkFormats"
+ "com.apple.MediaRemote.MRMediaRemoteServiceClient.accessQueue"
+ "com.apple.mediaremote.MRAVRoutingClientController.callbackQueue"
+ "com.apple.tvairplayd"
+ "copyWithOutputDeviceUIDs:"
+ "copyWithType:outputDeviceUIDs:"
+ "dataArtworks"
+ "dataArtworksAtIndex:"
+ "dataArtworksCount"
+ "dataArtworksType"
+ "defaultArtworkHeight"
+ "deviceAvailableForMediaSuggestionsNotification:"
+ "dimensions"
+ "discoveredConcreteOutputDevices"
+ "distantLocalEndpoint"
+ "electedDeviceIdentifier"
+ "endpointsSnapshot"
+ "expectedIdentifierForUserIdentity:withRandomData:"
+ "faceTimeBundleSet"
+ "fadeAudio"
+ "fetchIdentityForDSID:completion:"
+ "fetchParticipantsWithRequest:forPlayerPath:queue:completion:"
+ "fetchParticipantsWithRequest:playerPath:queue:completion:"
+ "fetchPlaybackQueueParticipantIdentifierForLocalAccountWithDSID:completion:"
+ "firstContentInfoMatchingSet:contentInfos:"
+ "formattedArtworkCallbacks"
+ "groupSessionAttributionValidityDuration"
+ "hasArtworkURLString"
+ "hasArtworkURLTemplateData"
+ "hasFadeAudio"
+ "hasIncludeAvailableArtworkFormats"
+ "hasPlayerClientParticipantsUpdateMessage"
+ "hasShouldNotPauseIfLastDeviceRemoved"
+ "hasSuppressErrorDialog"
+ "includeAvailableArtworkFormats"
+ "includeRemoteArtwork"
+ "initWithArtworkURLString:templateData:"
+ "initWithBytesNoCopy:length:encoding:freeWhenDone:"
+ "initWithImageData:"
+ "initWithPlayerPath:participants:"
+ "initWithRequestDetails:type:outputDeviceUIDs:"
+ "initWithRequestDetails:type:outputDevices:"
+ "isAirPlay"
+ "isB238Device"
+ "isB620Device"
+ "kMRMediaRemoteOptionAssociatedParticipantIdentifier"
+ "mediaSuggestionElectedDeviceObserverDeviceDidChange:"
+ "modifyTopologyWithRequest:completion:"
+ "modifyTopologyWithRequest:withReplyQueue:completion:"
+ "mr_distantEndpoints"
+ "mr_distantOutputDevices"
+ "mr_replaceEndpointsWithEndpoints:"
+ "mr_replaceOutputDevicesWithOutputDevices:"
+ "notifyAvailableEndpointsChanged:discoveredEndpoints:"
+ "o\x05$\x13\x11\x11\"\x12\x15"
+ "objCType"
+ "playWithAirPlayRouteIdentifiers:completion:"
+ "playerClientParticipantsUpdateMessage"
+ "recentGroupSessionParticipantsPepper"
+ "remoteArtworks"
+ "remoteArtworksAtIndex:"
+ "remoteArtworksCount"
+ "remoteArtworksType"
+ "removeOutputDevices:initiator:fadeAudio:withReplyQueue:completion:"
+ "requestDetails"
+ "requestedArtworkFormats"
+ "requestedArtworkFormatsAtIndex:"
+ "requestedArtworkFormatsCount"
+ "requestedArtworkFormatsType"
+ "requestedRemoteArtworkFormats"
+ "requestedRemoteArtworkFormatsAtIndex:"
+ "requestedRemoteArtworkFormatsCount"
+ "requestedRemoteArtworkFormatsType"
+ "setArtworkURLString:"
+ "setArtworkURLTemplateData:"
+ "setArtworks:"
+ "setAvailableArtworkFormats:"
+ "setAvailableRemoteArtworkFormats:"
+ "setDataArtworks:"
+ "setDistantLocalEndpoint:"
+ "setEndpointsSnapshot:"
+ "setFadeAudio:"
+ "setHasFadeAudio:"
+ "setHasIncludeAvailableArtworkFormats:"
+ "setHasShouldNotPauseIfLastDeviceRemoved:"
+ "setHasSuppressErrorDialog:"
+ "setIncludeAvailableArtworkFormats:"
+ "setLocalEndpoint:"
+ "setOutputDevicesSnapshot:"
+ "setPlayerClientParticipantsUpdateMessage:"
+ "setRemoteArtworks:"
+ "setRequestedArtworkFormats:"
+ "setRequestedRemoteArtworkFormats:"
+ "setShouldNotPauseIfLastDeviceRemoved:"
+ "setSuppressErrorDialog:"
+ "shouldNotPauseIfLastDeviceRemoved"
+ "stringForKey:"
+ "supportElectedPlayer"
+ "supportGroupSessionAttribution"
+ "supportGroupSessionAutoApproval"
+ "supportSystemEndpoints"
+ "suppressErrorDialog"
+ "suppressScreenMirroringErrors"
+ "sync-%@-%d"
+ "userIdentityForDSID:queue:completion:"
+ "v24@?0@\"MRUserIdentity\"8@\"NSError\"16"
+ "v32@0:8@\"MRGroupTopologyModificationRequest\"16@?<v@?@\"NSError\">24"
+ "void MRAddPlayerPathToUserInfo(NSMutableDictionary *__strong, MRPlayerPath *__strong)"
+ "void MRAddPlayerPathToXPCMessage(__strong xpc_object_t, MRNowPlayingPlayerPathRef)"
+ "void _MSVHasherAppendBytes(MSVHasher * _Nonnull, const void * _Nonnull, size_t)"
+ "wrangler_auto_approval"
+ "xpc error, likely mediaremoted crash, so retrying.."
+ "{?=\"artworkHeight\"b1\"artworkWidth\"b1\"cachingPolicy\"b1\"length\"b1\"location\"b1\"includeAvailableArtworkFormats\"b1\"includeInfo\"b1\"includeLanguageOptions\"b1\"includeLyrics\"b1\"includeMetadata\"b1\"includeParticipants\"b1\"includeSections\"b1\"isLegacyNowPlayingInfoRequest\"b1\"returnContentItemAssetsInUserCompletion\"b1}"
+ "{?=\"type\"b1\"fadeAudio\"b1\"shouldNotPauseIfLastDeviceRemoved\"b1\"suppressErrorDialog\"b1}"
+ "{CGSize=\"width\"d\"height\"d}"
+ "{CGSize=dd}16@0:8"
- "\x01\x11\x13\x13"
- "\x01%"
- "\x02\x1b"
- "\x04\x12"
- "\x0f\v"
- "\x1f\x01\x1f\x0f\x0f\x0f\a\x1d"
- "-[MRAVOutputContext addOutputDevices:initiator:fadeAudio:withCallbackQueue:block:]"
- "-[MRAVOutputContext removeAllOutputDevicesWithCallbackQueue:block:]"
- "-[MRAVOutputContext removeOutputDevices:initiator:fadeAudio:withCallbackQueue:block:]"
- "-[MRAVOutputContext setOutputDevices:initiator:password:fadeAudio:withCallbackQueue:block:]"
- "-[MRExternalDevice modifyByAddingDeviceUIDs:removingDeviceUIDs:settingDeviceUIDs:addingClusterAwareDeviceUIDs:removingClusterAwareDeviceUIDs:settingClusterAwareDeviceUIDs:withReplyQueue:completion:]"
- "/P"
- "3\x12"
- "<%@: %p | session id: %@ | audio format: %@ - %@ | channel #: %@ | available: %@ | eligible: %@ | active: %@ | pid: %i | bundleID: %@>"
- "<%@:%p identifier=%@ type=%@, addingDevices=%@, removingDevices=%@ settingDevices=%@ | cluster aware: addingDevices=%@, removingDevices=%@ settingDevices=%@>"
- "<MRAVOutputContextModification (%@): %@ - shouldFadeAudio: %@ passwordProvided: %@ devices: %@>"
- "<origin:%@:%u%@>"
- "@\"NSString\"16@?0Q8"
- "@64@0:8@16@24@32@40@48@56"
- "Move"
- "Posting Notification %{public}@"
- "Receieved Notification %{public}@"
- "T"
- "T@\"MRMediaControlsConfiguration\",R,N,V_configuration"
- "T@\"MSVMultiCallback\",R,N,V_createParticipantsCallbacks"
- "T@\"NSArray\",C,N,V_participants"
- "T@\"NSArray\",R,N,V_concreteOutputDevices"
- "T@\"NSString\",C,N,V_initiator"
- "T@\"NSString\",C,N,V_password"
- "TB,N,V_hasIncludeParticipants"
- "TB,N,V_shouldFadeAudio"
- "TQ,R,N,V_modificationType"
- "TVExperience"
- "[ConcreteOutputContext] Requesting to add output device(s) %{public}@ to context: %{public}@"
- "[ConcreteOutputContext] Requesting to remove all output devices from context: %{public}@"
- "[ConcreteOutputContext] Requesting to remove output device(s) %{public}@ from context: %{public}@"
- "[ConcreteOutputContext] Requesting to set output device(s) %{public}@ on context: %{public}@"
- "_createParticipantsCallbacks"
- "_hasIncludeParticipants"
- "_modificationType"
- "_shouldFadeAudio"
- "com.apple.MediaRemote.MRMediaRemoteServiceClient"
- "createParticipantsCallbacks"
- "defaultArtwortHeight"
- "initWithAddingDeviceUIDs:removingDeviceUIDs:settingDeviceUIDs:clusterAwareAddingOutputDeviceUIDs:clusterAwareRemovingOutputDeviceUIDs:clusterAwareSettingOutputDeviceUIDs:"
- "initWithType:devices:"
- "modificationType"
- "modifyByAddingDeviceUIDs:removingDeviceUIDs:settingDeviceUIDs:addingClusterAwareDeviceUIDs:removingClusterAwareDeviceUIDs:settingClusterAwareDeviceUIDs:withReplyQueue:completion:"
- "modifyByAddingDeviceUIDs:removingDeviceUIDs:settingDeviceUIDs:addingClusterDeviceUIDs:removingClusterDeviceUIDs:settingClusterDeviceUIDs:completion:"
- "o\x04$\x13\x11\x11\"\x12\x15"
- "removeOutputDevicesWithoutPausing"
- "setDistantEndpoints:"
- "setShouldFadeAudio:"
- "shouldFadeAudio"
- "useProactiveEndpoint"
- "v16@?0^{__CFString=}8"
- "v32@?0@\"NSArray\"8@\"NSMutableArray\"16@\"NSMutableArray\"24"
- "v72@0:8@\"NSArray\"16@\"NSArray\"24@\"NSArray\"32@\"NSArray\"40@\"NSArray\"48@\"NSArray\"56@?<v@?@\"NSError\">64"
- "v72@0:8@16@24@32@40@48@56@?64"
- "v80@0:8@16@24@32@40@48@56@64@?72"
- "void _onQueue_MRLoadContentItemParticipants(MRNowPlayingPlayerClient *__strong, MRPlaybackQueueRequest *__strong, MRPlaybackQueue *__strong)"
- "{?=\"artworkHeight\"b1\"artworkWidth\"b1\"cachingPolicy\"b1\"length\"b1\"location\"b1\"includeInfo\"b1\"includeLanguageOptions\"b1\"includeLyrics\"b1\"includeMetadata\"b1\"includeParticipants\"b1\"includeSections\"b1\"isLegacyNowPlayingInfoRequest\"b1\"returnContentItemAssetsInUserCompletion\"b1}"

```
