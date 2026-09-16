## BulletinDistributorCompanion

> `/System/Library/PrivateFrameworks/BulletinDistributorCompanion.framework/BulletinDistributorCompanion`

```diff

-382.0.16.1.0
-  __TEXT.__text: 0x8a418
-  __TEXT.__objc_methlist: 0xa29c
-  __TEXT.__cstring: 0x4477
-  __TEXT.__const: 0x672
-  __TEXT.__gcc_except_tab: 0x728
-  __TEXT.__oslogstring: 0x6865
+382.1.1.0.0
+  __TEXT.__text: 0x8b320
+  __TEXT.__objc_methlist: 0xa314
+  __TEXT.__cstring: 0x4527
+  __TEXT.__const: 0x692
+  __TEXT.__gcc_except_tab: 0x720
+  __TEXT.__oslogstring: 0x71a5
   __TEXT.__ustring: 0x4
   __TEXT.__swift5_typeref: 0x13f
   __TEXT.__swift5_capture: 0x2c

   __TEXT.__swift_as_entry: 0x10
   __TEXT.__swift_as_ret: 0x14
   __TEXT.__swift_as_cont: 0x14
-  __TEXT.__unwind_info: 0x29c0
+  __TEXT.__unwind_info: 0x2a18
   __TEXT.__eh_frame: 0x330
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x1ed8
-  __DATA_CONST.__objc_classlist: 0x4d0
+  __DATA_CONST.__objc_classlist: 0x4d8
   __DATA_CONST.__objc_catlist: 0xc0
   __DATA_CONST.__objc_protolist: 0x190
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4778
+  __DATA_CONST.__objc_selrefs: 0x47d8
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x3f8
+  __DATA_CONST.__objc_superrefs: 0x400
   __DATA_CONST.__objc_arraydata: 0x1c8
-  __DATA_CONST.__got: 0xa18
-  __AUTH_CONST.__const: 0x728
-  __AUTH_CONST.__cfstring: 0x4000
-  __AUTH_CONST.__objc_const: 0x1a5a8
+  __DATA_CONST.__got: 0xa20
+  __AUTH_CONST.__const: 0x748
+  __AUTH_CONST.__cfstring: 0x4100
+  __AUTH_CONST.__objc_const: 0x1a690
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_intobj: 0x3f0
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x858
-  __AUTH.__objc_data: 0xaa0
-  __DATA.__objc_ivar: 0xaf0
+  __AUTH_CONST.__auth_got: 0x870
+  __AUTH.__objc_data: 0xaf0
+  __DATA.__objc_ivar: 0xaf4
   __DATA.__data: 0x1220
   __DATA_DIRTY.__objc_data: 0x2618
   __DATA_DIRTY.__data: 0x118

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3892
-  Symbols:   8198
-  CStrings:  1191
+  Functions: 3917
+  Symbols:   8234
+  CStrings:  1205
 
Symbols:
+ -[BBBulletin(SafeLogging) blt_logProxy]
+ -[BLTBBBulletinLogProxy .cxx_destruct]
+ -[BLTBBBulletinLogProxy bulletin]
+ -[BLTBBBulletinLogProxy description]
+ -[BLTBBBulletinLogProxy initWithBulletin:]
+ -[BLTBBBulletinLogProxy redactedDescription]
+ -[BLTSectionInfoListBridgeProvider _createDomainAccessor]
+ -[BLTSectionInfoListBridgeProvider _domainAccessor]
+ -[BLTSectionInfoListBridgeProvider _loadOverridesChangedSince:domainAccessor:]
+ -[BLTSectionInfoListBridgeProvider _lock_domainAccessor]
+ _BBStringFromBBSystemSetting
+ _BLTActivePairedDeviceDescription
+ _BLTLogID
+ _BLTPrivateLoggingEnabled
+ _BLTPrivateLoggingEnabled.__privateLoggingEnabled
+ _BLTPrivateLoggingEnabled.onceToken
+ _CFPreferencesGetAppBooleanValue
+ _OBJC_CLASS_$_BLTBBBulletinLogProxy
+ _OBJC_IVAR_$_BLTBBBulletinLogProxy._bulletin
+ _OBJC_METACLASS_$_BLTBBBulletinLogProxy
+ __OBJC_$_INSTANCE_METHODS_BBBulletin(Date|VOIPCall|UniqueKey|SafeLogging|ExpirationHack|BLTCleanup|MatchID)
+ __OBJC_$_INSTANCE_METHODS_BLTBBBulletinLogProxy
+ __OBJC_$_INSTANCE_VARIABLES_BLTBBBulletinLogProxy
+ __OBJC_$_PROP_LIST_BLTBBBulletinLogProxy
+ __OBJC_CLASS_RO_$_BLTBBBulletinLogProxy
+ __OBJC_METACLASS_RO_$_BLTBBBulletinLogProxy
+ ___BLTPrivateLoggingEnabled_block_invoke
+ _objc_msgSend$_createDomainAccessor
+ _objc_msgSend$_domainAccessor
+ _objc_msgSend$_loadOverridesChangedSince:domainAccessor:
+ _objc_msgSend$_lock_domainAccessor
+ _objc_msgSend$blt_logProxy
+ _objc_msgSend$getActivePairedDeviceExcludingAltAccount
+ _objc_msgSend$initWithBulletin:
+ _objc_msgSend$isActive
+ _objc_msgSend$isPaired
+ _objc_msgSend$isSetup
+ _objc_msgSend$un_logDigest
+ _os_variant_has_internal_diagnostics
- -[BLTSectionInfoListBridgeProvider _loadOverridesChangedSince:]
- __OBJC_$_INSTANCE_METHODS_BBBulletin(Date|VOIPCall|UniqueKey|ExpirationHack|BLTCleanup|MatchID)
- _objc_msgSend$_loadOverridesChangedSince:
CStrings:
+ "%@(%@)"
+ "%s gizmo of bulletin with publisherMatchID: %{public}@ forFeed: %lu playLightsAndSirens: %s"
+ "%s: matched response %{public}@, executing block"
+ "%s: no ack block found for response %{public}@, ignoring"
+ "%{public}@ : %{public}@ blt_removeIconVariantsWithRootPath: %@"
+ "%{public}@ : %{public}@ blt_removeIconVariantsWithRootPath: nothing at: %@"
+ "%{public}@ Image attachment processing failed for: %@"
+ "%{public}@ Image attachment processing: %@"
+ "%{public}@ Image attachment will be sent scaled: %@"
+ "%{public}@ Image attachment will be sent without scaling: %@"
+ "%{public}@ _handleClientReplyTimeout - no _clientReplyTimeouts"
+ "%{public}@ _handleClientReplyTimeout: %@"
+ "%{public}@ _reloadBulletins: obsoletionDate: %@"
+ "%{public}@ _reloadBulletins: obsoletionDate: %@ bulletinFetcher: %@"
+ "%{public}@ _reloadBulletins: obsoletionDate: %@ complete"
+ "%{public}@ _sendCurrentBulletinIdentifiers: bulletinIdentifiersBySectionID: %@"
+ "%{public}@ _sendCurrentBulletinIdentifiers: fullList: %@"
+ "%{public}@ _setupBBObserver"
+ "%{public}@ _setupBBObserver: %@"
+ "%{public}@ _storeIconVariantsForSectionInfo: skipping variant: %@"
+ "%{public}@ _storeIconVariantsForSectionInfo: variant.imagePath: %@"
+ "%{public}@ _writeData:toFileHandle: %@ data write failed with error: %@"
+ "%{public}@ _writeData:toFileHandle: %@ dataLengthData write failed with error: %@"
+ "%{public}@ add:type:messageIdentifier: sendURL is nil"
+ "%{public}@ add:type:messageIdentifier: sendURL: %@ fileSystemRepresentation: %s"
+ "%{public}@ blt_ProtobufWithScale: dateComponentDetails error: %@"
+ "%{public}@ blt_protobuf: %@"
+ "%{public}@ checkAndThenSendGlobalSettings: %@ - not sending"
+ "%{public}@ checkAndThenSendGlobalSettings: %@ - sending"
+ "%{public}@ handleAction: %@"
+ "%{public}@ handleAction: %@ bulletins: %@"
+ "%{public}@ handleAction: FAILED: actionInfo: %@ at sending response %@"
+ "%{public}@ handleAction: SUCCESS: actionInfo: %@ at sending response %@"
+ "%{public}@ handleAction: followActivityAction: %@ response: %@"
+ "%{public}@ handleAction: no followActivityAction for response: %@"
+ "%{public}@ initWithLocalEndpoint: %@ remoteEndpoint: %@"
+ "%{public}@ initWithProvider: %@"
+ "%{public}@ needsSend: !remoteSettings"
+ "%{public}@ needsSend: UNEXPECTED: globalScheduledDeliverySetting == BBScheduledDeliverySettingDefault && globalSummarizationSetting == BBSystemSettingDefault - not sending and this should never happen"
+ "%{public}@ needsSend: remoteSettings: %@ SHOULD NOT SEND"
+ "%{public}@ needsSend: remoteSettings: %@ SHOULD SEND"
+ "%{public}@ not sending DEFAULT received from BB: %@"
+ "%{public}@ objectForKey: %{public}@ error: %@ unarchiving in %{public}@"
+ "%{public}@ objectForKey: %{public}@ exception: %@ loading in %{public}@"
+ "%{public}@ objectForKey: %{public}@ not found in %{public}@"
+ "%{public}@ observer: %@ globalSettings: %@"
+ "%{public}@ observer: %@ modifyBulletin: %@ feed: %lu"
+ "%{public}@ observer: %@ removeBulletin: %@ feed: %lu"
+ "%{public}@ observer: %@ removeBulletin: %@ feed: %lu - lock screen feed only - ignoring"
+ "%{public}@ observer: %@ updateGlobalSettings: %@ UPDATING"
+ "%{public}@ remoteGlobalSettingsSyncServer: %@ sendChangeset: %@"
+ "%{public}@ removeBulletinWithPublisherBulletinID: %{public}@ recordID: %{public}@ phoneSectionID: %{public}@ - failed no bulletin found"
+ "%{public}@ removeBulletinWithPublisherBulletinID: %{public}@ recordID: %{public}@ phoneSectionID: %{public}@ bulletin: %@"
+ "%{public}@ removeBulletinWithPublisherBulletinID: %{public}@ recordID: %{public}@ sectionID: %{public}@"
+ "%{public}@ removeBulletinWithPublisherBulletinID: %{public}@ recordID: %{public}@ sectionID: %{public}@ - failed no bulletin found"
+ "%{public}@ removeBulletinWithPublisherBulletinID: %{public}@ recordID: %{public}@ sectionID: %{public}@ bulletin: %@"
+ "%{public}@ removeObjectForKey: %{public}@ path: %{public}@ error: %@"
+ "%{public}@ sendInitialChangsetWithCompletion"
+ "%{public}@ sendInitialChangsetWithCompletion: %@"
+ "%{public}@ sendSuccess: infoFile: %@ saveSuccess: %{BOOL}u"
+ "%{public}@ setSendFileURL: %@"
+ "%{public}@ storeObject:withKey: archiving/writing failed for: %{public}@ path: %{public}@ with exception: %@"
+ "%{public}@ storeObject:withKey: createDirectoryAtPath failed for: %{public}@ at path: %{public}@ error: %@"
+ "%{public}@ storeObject:withKey: failed to create archiver for: %{public}@ path: %{public}@"
+ "%{public}@ storeObject:withKey: object nil for: %{public}@"
+ "%{public}@ storeObject:withKey: wrote for: %{public}@ path: %{public}@"
+ "%{public}@ updateGlobalSettings: %@"
+ "%{public}@ updateLocalSettingsWithProvider: %@ remoteChangeSet: %@ NOT UPDATING"
+ "%{public}@ updateLocalSettingsWithProvider: %@ remoteChangeSet: %@ UPDATING"
+ "%{public}@ willSendLightsAndSirensWithPublisherBulletinID: %{public}@ recordID: %{public}@ phoneSectionID: %{public}@"
+ "%{public}@.%{public}@.GizmoToCompanionDelay: %f"
+ "%{public}@.%{public}@.PublicationToReplayDelay: %f"
+ "(digest failed)"
+ "(empty)"
+ "(null)"
+ "Add client reply timer (%@) for bulletin %{public}@ in section %{public}@"
+ "Attempting to send subsection parameter icons for section ID %{public}@"
+ "BLT send remove: sectionID=%{public}@ publisherBulletinID=%{public}@"
+ "BLTBulletinDistributor _notifyGizmoOfBulletin with publisherMatchID: %{public}@ forFeed: %lu playLightsAndSirens: %s"
+ "BLTBulletinDistributor _notifyGizmoOfCancelBulletin with publisherMatchID: %{public}@ in universal section: %{public}@ forFeed: %lu timeout: %f%s"
+ "BLTBulletinDistributor _subscriberWillAllowBulletin not timed out, returning %{public}@"
+ "BLTBulletinDistributor addBulletin: %@ (publisherMatchID: %{public}@) forFeed: %lu playLightsAndSirens: %s turnsOnDisplay: %s willPresentNotification: %@"
+ "BLTBulletinDistributor clearReplyBlockForReplyToken: %{public}@"
+ "BLTBulletinDistributor handleDidPlayLightsAndSirens: %s forReplyToken: %{public}@ bulletin: %{public}@ inSection: %{public}@"
+ "BLTBulletinDistributor setReplyBlock: forSection: %{public}@ bulletin: %{public}@"
+ "BLTPBFileURLMetaData initWithSequenceNumberManager %{public}@: transportData was nil!"
+ "BLTPBGetPNGIconDataFromAppIcon: No UIImage for: %{public}@"
+ "BLTPBGetPNGIconDataFromAppIcon: No cgImage for: %{public}@"
+ "BLTPBGetPNGIconDataFromAppIcon: No isImage for: %{public}@"
+ "BLTPBTransportData transportDataWithSequenceNumberManager %{public}@: nextSendSequenceNumber returned nil!"
+ "BLTSectionInfoListDisableAllProvider: applying disabled override for %{public}@"
+ "BLTSectionInfoListDisableAllProvider: section removed %{public}@"
+ "BLTSectionInfoListEnableAllProvider: applying enabled override for %{public}@"
+ "BLTSectionInfoListEnableAllProvider: section removed %{public}@"
+ "Bulletin already mapped: %{public}@"
+ "Bulletin in section %{public}@ with matchID %{public}@ sent to observers now on feed %lu with lightsandsirens: %s initSyncComplete: %s wkAppsLoaded: %s"
+ "Bulletin with id: %{public}@ has no message and was sent to sounds feed only. Should not coordinate"
+ "Checking if notification with subsections will present in sectionInfo that has no subsections! Falling back to checking against sectionInfo. sectionID:%{public}@ subsectionIDs:%@ sectionInfo:%@"
+ "Creating new settings for app %{public}@"
+ "Detected a duplicate message on %{public}@ with identifer %{public}@"
+ "Did not find action with identifier: %{public}@. Synthesizing action."
+ "Disabling notification in bridge for %{public}@"
+ "Enqueuing section ID %{public}@ for future resend attempt"
+ "Error: Trying to cache lights and sirens value for unknown replyToken: %{public}@"
+ "Error: Unable to delete icon variant.imagePath: %@ for %{public}@: %@"
+ "Error: Unable to store icon %@ for %{public}@: %@"
+ "Expecting number or string type for sectionSubtype in legacy map for %{public}@"
+ "Failed to create NPSDomainAccessor for domain %{public}@. activePairedDevice: %{public}@"
+ "Failed to find matching action for %@ for publisherBulletinD: %{public}@, recordID: %{public}@, sectionID: %{public}@"
+ "Failed to send section info so abandoning with section ID %{public}@"
+ "Fetching app icons for %{public}@"
+ "Fetching apps for paired device %p id: %{public}@"
+ "Fetching icons for BBSectionInfo to BLTPBSectionInfo conversion of %{public}@"
+ "Found default paired device %{public}@"
+ "Gateway returned summarization setting %{public}@"
+ "IDS error sending request with identifier %{public}@ (paired device ready: %{BOOL}u): %@"
+ "IDS success sending request: %{public}@"
+ "Loaded actual section info for %{public}@"
+ "Looking for action with identifier: %{public}@"
+ "Max send attempts exceeded for section ID %{public}@; dropping settings"
+ "Moving %{public}@ to front of send queue"
+ "No Bridge settings could be found. hasDomainAccessor: %{public}@; activePairedDevice: %{public}@"
+ "No handler for %@ for publisherBulletinD: %{public}@, recordID: %{public}@, sectionID: %{public}@"
+ "No sectionInfo icon. app icon for %{public}@ not found"
+ "Not building custom settings for %{public}@ without a domain accessor"
+ "Not enabling custom settings for %{public}@ without a domain accessor"
+ "Not persisting custom settings for %{public}@ without a domain accessor"
+ "Not persisting mirrored settings for %{public}@ without a domain accessor"
+ "Not removing section %{public}@ without a domain accessor"
+ "Not sending settings for %{public}@ as it has no override and is not alerting"
+ "Not setting notifications level %ld in bridge for %{public}@ without a domain accessor"
+ "On reload, retrieved section info for %{public}@"
+ "Out of order message received from IDS on %{public}@ with identifer %{public}@"
+ "Performing pending update type %@ for %{public}@"
+ "Phone section not found: %{public}@. Must be watch section only"
+ "Received %@ action for publisherBulletinD: %{public}@, recordID: %{public}@, sectionID: %{public}@"
+ "Received message with IDS identifier: %{public}@ and incoming response id: %{public}@"
+ "Received removeSection from BB for %{public}@"
+ "Received resource with IDS identifier: %{public}@"
+ "Received updated section info for %{public}@"
+ "Reloaded %{public}@ section IDs"
+ "Removing section info cache info for %{public}@"
+ "Removing sync supported app %{public}@"
+ "Requesting initial sync state for %{public}@"
+ "Requesting section info for unknown section %{public}@"
+ "Retrieved nil sectionInfo from BB updated section info: %{public}@"
+ "Section %{public}@ hasn't completed sync'ing"
+ "Section settings for %{public}@ overridden by factory section %{public}@"
+ "Sending bb section info for sync supported app %{public}@"
+ "Sending fake section info for sync supported app %{public}@"
+ "Sending remove section %{public}@"
+ "Sending section icon for section %{public}@, subtype %ld"
+ "Sending sectionSubtypeParameters icon (%@) for %{public}@ %@"
+ "Sending sectionSubtypeParameters icon (%@) for %{public}@ defaults"
+ "Sending sectionSubtypeParameters icons for %{public}@"
+ "Sending single section infos %{public}@"
+ "Sending single section settings override for %{public}@"
+ "Sent %sIDS %s %@ got identifier: %{public}@ %s"
+ "Sent section info but nano failed to acknowledge with section ID %{public}@"
+ "Sequence number attached to incoming fileURL on service %{public}@: %llu session: %{public}@ state: %s"
+ "Sequence number attached to incoming protobuf on service %{public}@: %llu session: %{public}@ state: %s"
+ "Sequence number attached to outgoing protobuf on service %{public}@: %{public}@"
+ "Sequence numbers written. Send: %llu session: %{public}@ Recv: %llu session: %{public}@"
+ "Setting custom settings for watch app %{public}@"
+ "Setting notification level for %{public}@ to %{public}@"
+ "Settings not found for app %{public}@"
+ "SkipInternalDiagnostics"
+ "Updated summarization setting to %{public}@"
+ "addBulletin hasSummary=%{BOOL}u hasThreadSummary=%{BOOL}u connectionStatus=%s isTrafficRestricted=%{BOOL}u watchNearby=%{BOOL}u matchID=%{public}@ sectionID=%{public}@"
+ "com.apple.bulletindistributord"
+ "makeAuthorizationPermanentForSectionID sendSectionInfosWithSectionIDs complete %{public}@"
+ "makeAuthorizationPermanentForSectionID settingsGateway saved %{public}@"
+ "pairingID: %@; isPaired: %@; isActive: %@; isSetup: %@; hasPairingStorePath: %@"
- "%@ : %@ blt_removeIconVariantsWithRootPath: %@"
- "%@ : %@ blt_removeIconVariantsWithRootPath: nothing at: %@"
- "%@ Image attachment processing failed for: %@"
- "%@ Image attachment processing: %@"
- "%@ Image attachment will be sent scaled: %@"
- "%@ Image attachment will be sent without scaling: %@"
- "%@ _handleClientReplyTimeout - no _clientReplyTimeouts"
- "%@ _handleClientReplyTimeout: %@"
- "%@ _reloadBulletins: obsoletionDate: %@"
- "%@ _reloadBulletins: obsoletionDate: %@ bulletinFetcher: %@"
- "%@ _reloadBulletins: obsoletionDate: %@ complete"
- "%@ _sendCurrentBulletinIdentifiers: bulletinIdentifiersBySectionID: %@"
- "%@ _sendCurrentBulletinIdentifiers: fullList: %@"
- "%@ _setupBBObserver"
- "%@ _setupBBObserver: %@"
- "%@ _storeIconVariantsForSectionInfo: skipping variant: %@"
- "%@ _storeIconVariantsForSectionInfo: variant.imagePath: %@"
- "%@ _writeData:toFileHandle: %@ data write failed with error: %@"
- "%@ _writeData:toFileHandle: %@ dataLengthData write failed with error: %@"
- "%@ add:type:messageIdentifier: sendURL is nil"
- "%@ add:type:messageIdentifier: sendURL: %@ fileSystemRepresentation: %s"
- "%@ blt_ProtobufWithScale: dateComponentDetails error: %@"
- "%@ blt_protobuf: %@"
- "%@ checkAndThenSendGlobalSettings: %@ - not sending"
- "%@ checkAndThenSendGlobalSettings: %@ - sending"
- "%@ handleAction: %@"
- "%@ handleAction: %@ bulletins: %@"
- "%@ handleAction: FAILED: actionInfo: %@ at sending response %@"
- "%@ handleAction: SUCCESS: actionInfo: %@ at sending response %@"
- "%@ handleAction: followActivityAction: %@ response: %@"
- "%@ handleAction: no followActivityAction for response: %@"
- "%@ initWithLocalEndpoint: %@ remoteEndpoint: %@"
- "%@ initWithProvider: %@"
- "%@ needsSend: !remoteSettings"
- "%@ needsSend: UNEXPECTED: globalScheduledDeliverySetting == BBScheduledDeliverySettingDefault && globalSummarizationSetting == BBSystemSettingDefault - not sending and this should never happen"
- "%@ needsSend: remoteSettings: %@ SHOULD NOT SEND"
- "%@ needsSend: remoteSettings: %@ SHOULD SEND"
- "%@ not sending DEFAULT received from BB: %@"
- "%@ objectForKey: %@ error: %@ unarchiving %@"
- "%@ objectForKey: %@ exception: %@ loading %@"
- "%@ objectForKey: %@ not found at %@"
- "%@ observer: %@ globalSettings: %@"
- "%@ observer: %@ modifyBulletin: %@ feed: %lu"
- "%@ observer: %@ removeBulletin: %@ feed: %lu"
- "%@ observer: %@ removeBulletin: %@ feed: %lu - lock screen feed only - ignoring"
- "%@ observer: %@ updateGlobalSettings: %@ UPDATING"
- "%@ remoteGlobalSettingsSyncServer: %@ sendChangeset: %@"
- "%@ removeBulletinWithPublisherBulletinID: %@ recordID: %@ phoneSectionID: %@ - failed no bulletin found"
- "%@ removeBulletinWithPublisherBulletinID: %@ recordID: %@ phoneSectionID: %@ bulletin: %@"
- "%@ removeBulletinWithPublisherBulletinID: %@ recordID: %@ sectionID: %@"
- "%@ removeBulletinWithPublisherBulletinID: %@ recordID: %@ sectionID: %@ - failed no bulletin found"
- "%@ removeBulletinWithPublisherBulletinID: %@ recordID: %@ sectionID: %@ bulletin: %@"
- "%@ removeObjectForKey: %@ path: %@ error: %@"
- "%@ sendInitialChangsetWithCompletion"
- "%@ sendInitialChangsetWithCompletion: %@"
- "%@ sendSuccess: infoFile: %@ saveSuccess: %{BOOL}u"
- "%@ setSendFileURL: %@"
- "%@ storeObject:withKey: archiving/writing failed for: %@ path: %@ with exception: %@"
- "%@ storeObject:withKey: createDirectoryAtPath failed for: %@ at path: %@ error: %@"
- "%@ storeObject:withKey: failed to create archiver for: %@ path: %@"
- "%@ storeObject:withKey: object nil for: %@"
- "%@ storeObject:withKey: wrote for: %@ path: %@"
- "%@ updateGlobalSettings: %@"
- "%@ updateLocalSettingsWithProvider: %@ remoteChangeSet: %@ NOT UPDATING"
- "%@ updateLocalSettingsWithProvider: %@ remoteChangeSet: %@ UPDATING"
- "%@ willSendLightsAndSirensWithPublisherBulletinID: %@ recordID: %@ phoneSectionID: %@"
- "%@.%@.GizmoToCompanionDelay: %f"
- "%@.%@.PublicationToReplayDelay: %f"
- "%s gizmo of bulletin with publisherMatchID: %@ forFeed: %lu playLightsAndSirens: %s"
- "%s: matched response %@, executing block"
- "%s: no ack block found for response %@, ignoring"
- "Add client reply timer (%@) for bulletin %@ in section %@"
- "Attempting to send subsection parameter icons for section ID %@"
- "BLT send remove: sectionID=%{public}@ publisherBulletinID=%@"
- "BLTBulletinDistributor _notifyGizmoOfBulletin with publisherMatchID: %@ forFeed: %lu playLightsAndSirens: %s"
- "BLTBulletinDistributor _notifyGizmoOfCancelBulletin with publisherMatchID: %@ in universal section: %@ forFeed: %lu timeout: %f%s"
- "BLTBulletinDistributor _subscriberWillAllowBulletin not timed out, returning %@"
- "BLTBulletinDistributor addBulletin: %@ (publisherMatchID: %@) forFeed: %lu playLightsAndSirens: %s turnsOnDisplay: %s willPresentNotification: %@"
- "BLTBulletinDistributor clearReplyBlockForReplyToken: %@"
- "BLTBulletinDistributor handleDidPlayLightsAndSirens: %s forReplyToken: %@ bulletin: %@ inSection: %@"
- "BLTBulletinDistributor setReplyBlock: forSection: %@ bulletin: %@"
- "BLTPBFileURLMetaData initWithSequenceNumberManager %@: transportData was nil!"
- "BLTPBGetPNGIconDataFromAppIcon: No UIImage for: %@"
- "BLTPBGetPNGIconDataFromAppIcon: No cgImage for: %@"
- "BLTPBGetPNGIconDataFromAppIcon: No isImage for: %@"
- "BLTPBTransportData transportDataWithSequenceNumberManager %@: nextSendSequenceNumber returned nil!"
- "BLTSectionInfoListDisableAllProvider: applying disabled override for %@"
- "BLTSectionInfoListDisableAllProvider: section removed %@"
- "BLTSectionInfoListEnableAllProvider: applying enabled override for %@"
- "BLTSectionInfoListEnableAllProvider: section removed %@"
- "Bulletin already mapped: %@"
- "Bulletin in section %@ with matchID %@ sent to observers now on feed %lu with lightsandsirens: %s initSyncComplete: %s wkAppsLoaded: %s"
- "Bulletin with id: %@ has no message and was sent to sounds feed only. Should not coordinate"
- "Checking if notification with subsections will present in sectionInfo that has no subsections! Falling back to checking against sectionInfo. sectionID:%@ subsectionIDs:%@ sectionInfo:%@"
- "Creating new settings for app %@"
- "Detected a duplicate message!"
- "Did not find action with identifier: %@. Synthesizing action."
- "Disabling notification in bridge for %@"
- "Enqueuing section ID %@ for future resend attempt"
- "Error: Trying to cache lights and sirens value for unknown replyToken: %@"
- "Error: Unable to delete icon variant.imagePath: %@ for %@: %@"
- "Error: Unable to store icon %@ for %@: %@"
- "Expecting number or string type for sectionSubtype in legacy map for %@"
- "Failed to find matching action for %@ for publisherBulletinD: %@, recordID: %@, sectionID: %@"
- "Failed to send section info so abandoning with section ID %@"
- "Fetching app icons for %@"
- "Fetching apps for paired device %p id: %@"
- "Fetching icons for BBSectionInfo to BLTPBSectionInfo conversion of %@"
- "Found default paired device %@"
- "Gateway returned summarization setting %@"
- "IDS error sending request with identifier %@ (paired device ready: %{BOOL}u): %@"
- "IDS success sending request: %@"
- "Loaded actual section info for %@"
- "Looking for action with identifier: %@"
- "Max send attempts exceeded for section ID %@; dropping settings"
- "Moving %@ to front of send queue"
- "No Bridge settings could be found"
- "No handler for %@ for publisherBulletinD: %@, recordID: %@, sectionID: %@"
- "No sectionInfo icon. app icon for %@ not found"
- "Not sending settings for %@ as it has no override and is not alerting"
- "On reload, retrieved section info for %@"
- "Out of order message received from IDS on %@ with identifer %@"
- "Performing pending update type %@ for %@"
- "Phone section not found: %@. Must be watch section only"
- "Received %@ action for publisherBulletinD: %@, recordID: %@, sectionID: %@"
- "Received message with IDS identifier: %@ and incoming response id: %@"
- "Received removeSection from BB for %@"
- "Received resource with IDS identifier: %@"
- "Received updated section info for %@"
- "Reloaded %@ section IDs"
- "Removing section info cache info for %@"
- "Removing sync supported app %@"
- "Requesting initial sync state for %@"
- "Requesting section info for unknown section %@"
- "Retrieved nil sectionInfo from BB updated section info: %@"
- "Section %@ hasn't completed sync'ing"
- "Section settings for %@ overridden by factory section %@"
- "Sending bb section info for sync supported app %@"
- "Sending fake section info for sync supported app %@"
- "Sending remove section %@"
- "Sending section icon for section %@, subtype %ld"
- "Sending sectionSubtypeParameters icon (%@) for %@ %@"
- "Sending sectionSubtypeParameters icon (%@) for %@ defaults"
- "Sending sectionSubtypeParameters icons for %@"
- "Sending single section infos %@"
- "Sending single section settings override for %@"
- "Sent %sIDS %s %@ got identifier: %@ %s"
- "Sent section info but nano failed to acknowledge with section ID %@"
- "Sequence number attached to incoming fileURL on service %@: %llu session: %@ state: %s"
- "Sequence number attached to incoming protobuf on service %@: %llu session: %@ state: %s"
- "Sequence number attached to outgoing protobuf on service %@: %@"
- "Sequence numbers written. Send: %llu session: %@ Recv: %llu session: %@"
- "Setting custom settings for watch app %@"
- "Setting notification level for %@ to %@"
- "Settings not found for app %@"
- "Updated summarization setting to %@"
- "addBulletin hasSummary=%{BOOL}u hasThreadSummary=%{BOOL}u connectionStatus=%s isTrafficRestricted=%{BOOL}u watchNearby=%{BOOL}u matchID=%@ sectionID=%@"
- "makeAuthorizationPermanentForSectionID sendSectionInfosWithSectionIDs complete %@"
- "makeAuthorizationPermanentForSectionID settingsGateway saved %@"
```
