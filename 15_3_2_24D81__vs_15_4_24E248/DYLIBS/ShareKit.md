## ShareKit

> `/System/Library/PrivateFrameworks/ShareKit.framework/Versions/A/ShareKit`

```diff

-2060.40.21.0.0
-  __TEXT.__text: 0x75528
+2060.50.171.1.2
+  __TEXT.__text: 0x764c8
   __TEXT.__auth_stubs: 0xc70
-  __TEXT.__objc_methlist: 0x48d0
+  __TEXT.__objc_methlist: 0x54cc
   __TEXT.__const: 0x1d4
-  __TEXT.__cstring: 0x4356
-  __TEXT.__gcc_except_tab: 0x1664
+  __TEXT.__cstring: 0x4396
+  __TEXT.__gcc_except_tab: 0x169c
   __TEXT.__oslogstring: 0x56b9
   __TEXT.__ustring: 0x128
   __TEXT.__dlopen_cstrs: 0x52
-  __TEXT.__unwind_info: 0x1978
-  __TEXT.__objc_classname: 0xb52
-  __TEXT.__objc_methname: 0x11c3a
-  __TEXT.__objc_methtype: 0x2d13
-  __TEXT.__objc_stubs: 0xe380
-  __DATA_CONST.__got: 0x7f0
+  __TEXT.__unwind_info: 0x1a80
+  __TEXT.__objc_classname: 0xb68
+  __TEXT.__objc_methname: 0x11e0c
+  __TEXT.__objc_methtype: 0x2d36
+  __TEXT.__objc_stubs: 0xe480
+  __DATA_CONST.__got: 0x7f8
   __DATA_CONST.__const: 0x3e0
   __DATA_CONST.__objc_classlist: 0x240
   __DATA_CONST.__objc_catlist: 0x70
-  __DATA_CONST.__objc_protolist: 0xf0
+  __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4038
+  __DATA_CONST.__objc_selrefs: 0x43e8
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x190
   __DATA_CONST.__objc_arraydata: 0x68
   __AUTH_CONST.__auth_got: 0x648
-  __AUTH_CONST.__const: 0x2ba0
+  __AUTH_CONST.__const: 0x2c00
   __AUTH_CONST.__cfstring: 0x48e0
-  __AUTH_CONST.__objc_const: 0xb870
+  __AUTH_CONST.__objc_const: 0xa2c0
   __AUTH_CONST.__objc_doubleobj: 0x70
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0xa8

   __AUTH.__objc_data: 0x5f0
   __AUTH.__data: 0x80
   __DATA.__objc_ivar: 0x4e0
-  __DATA.__data: 0xbc0
+  __DATA.__data: 0xc20
   __DATA.__bss: 0x4c0
   __DATA_DIRTY.__objc_data: 0x1090
   __DATA_DIRTY.__data: 0xc0

   - /System/Library/PrivateFrameworks/ViewBridge.framework/Versions/A/ViewBridge
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E67E4A13-DB1F-39AD-A9BF-2A55A4459F93
-  Functions: 2280
-  Symbols:   6307
-  CStrings:  4953
+  UUID: FD9B0C16-F3EB-326E-B301-47F5761478CB
+  Functions: 2378
+  Symbols:   6452
+  CStrings:  4966
 
Symbols:
+ +[NSSharingExtensionContext _extensionAuxiliaryHostProtocol].cold.1
+ +[NSSharingExtensionContext _extensionAuxiliaryVendorProtocol].cold.1
+ +[NSSharingExtensionContext assertBundleInformationIsComplete].cold.1
+ +[NSSharingExtensionContext assertBundleInformationIsComplete].cold.2
+ +[NSSharingExtensionContext assertBundleInformationIsComplete].cold.3
+ +[NSSharingExtensionContext assertBundleInformationIsComplete].cold.4
+ +[NSSharingPlugInHelper _addParticipantEmails:phoneNumbers:asReadWrite:allowParticipantsToInvite:toShare:inContainer:withURL:completionHandler:].cold.1
+ +[NSSharingPlugInHelper _removeParticipants:fromShare:inContainer:completionHandler:].cold.1
+ +[SHKBuiltInSharingServicesHelper workQueue].cold.1
+ +[SHKHostExtensionContext _extensionAuxiliaryHostProtocol].cold.1
+ +[SHKHostExtensionContext _extensionAuxiliaryVendorProtocol].cold.1
+ +[SHKMarzipanRemoteViewController requestMarzipanViewControllerForExtensionWithIdentifier:fromServiceWithBundleIdentifier:connectionHandler:].cold.1
+ +[SHKRemoteViewController requestViewControllerFromServiceWithBundleIdentifier:withConnectionHandler:].cold.1
+ +[SHKSharePlaySharingService sharePlayIsAvailable].cold.1
+ +[SHKSharingService descriptionForSharingServiceDict:bundle:attributeStore:].cold.4
+ +[SHKSharingService ensurePlugInCacheInitialized].cold.1
+ +[SHKSharingService serviceIdentifierWithBundle:serviceDictionary:multiplexed:].cold.1
+ +[SHKSharingService sharingServicesForFilteredItems:invokedByPicker:allowInactive:onlyViewerOrEditor:completion:].cold.2
+ +[SHKSharingService sharingServicesForFilteredItems:mask:invokedByPicker:allowInactive:completion:].cold.1
+ +[SHKSharingService sharingServicesOnMainQueueForItems:invokedByPicker:allowInactive:onlyViewerOrEditor:completion:].cold.1
+ +[SHKSharingService sharingServicesOnMainQueueForItems:mask:invokedByPicker:allowInactive:completion:].cold.1
+ +[SHK_CAAnimationDelegate sharedDelegate].cold.1
+ -[NSItemProvider(ShareKit) getImageForKeyPointer:].cold.1
+ -[NSItemProvider(ShareKit) setImage:forKeyPointer:].cold.1
+ -[NSSharingAddressBookNameExtractor _matchingPersonsBestMatchOnly:].cold.1
+ -[NSSharingContainerViewController init].cold.1
+ -[NSSharingContainerViewController init].cold.2
+ -[NSSharingExtensionContext performServiceWithOptionsDictionaryData:completion:].cold.1
+ -[NSSharingItem coordinatedURLWithError:].cold.2
+ -[NSSharingUIExtensionContext getPreviewImageForAttachments:block:timeoutBlock:].cold.1
+ -[NSSharingUIExtensionContext getPreviewImageForAttachments:block:timeoutBlock:].cold.2
+ -[NSSharingUIExtensionContext viewController].cold.1
+ -[SHKAutoLayoutConstraintPair initWithFirstConstraint:secondConstraint:].cold.1
+ -[SHKAutoLayoutConstraintPair initWithFirstConstraint:secondConstraint:].cold.2
+ -[SHKBlockQueue removeAndExecuteBlockWithUUID:size:completionBlock:].cold.1
+ -[SHKCollaborationService canShareFileURL:]
+ -[SHKItemAttributeStore initWithShareItem:].cold.1
+ -[SHKItemAttributeStore initWithShareItem:].cold.2
+ -[SHKRemoteViewController exportedObject].cold.1
+ -[SHKRemoteWindowController setHostWindowFrame:withClientWindowSync:blurAndShadowSync:].cold.1
+ -[SHKSaveToFilesSharingService temporaryFileURLForData:typeIdentifier:].cold.4
+ -[SHKSaveToFilesSharingService temporaryFileURLForData:typeIdentifier:].cold.5
+ -[SHKSharingService _commonInit].cold.1
+ -[SHKSharingService getAppIDWithCompletion:].cold.1
+ -[SHKSharingService handleIOSMacExtensionWithExtensionItem:].cold.1
+ -[SHKSharingService launchCount].cold.1
+ -[SHKSharingService registerPotentially].cold.1
+ -[SHKSharingService registerWithItems:].cold.1
+ -[SHKSharingServicePicker _collaborationModeRestriction].cold.1
+ -[SHKSharingServicePicker _delimiterAttributes].cold.1
+ -[SHKSharingServicePicker _handleAddParticipantsCompletedSharingWithShareURL:ckShare:].cold.1
+ -[SHKSharingServicePicker _subtitleAttributes].cold.1
+ -[SHKSharingServicePicker _titleAttributes].cold.1
+ -[SHKSharingServicePicker emptyMenuImage].cold.1
+ -[SHKSharingServicePicker menuWithCompletion:].cold.1
+ -[SHKSharingServicePicker queryPickerMenuItemsAndServicesWithCompletion:].cold.1
+ -[SHKSharingServicePicker setTestingSnapshot:]
+ -[SHKSharingServicePicker showRelativeToRect:ofView:preferredEdge:].cold.1
+ -[SHKSharingServicePicker testingSnapshot]
+ -[SHKSharingViewService setViewOptions:].cold.1
+ -[SHKSharingViewService setViewOptions:].cold.2
+ -[SHKSharingViewService setViewOptions:].cold.3
+ -[SHKSharingViewService setViewOptions:].cold.4
+ -[SHKSharingViewService setup].cold.1
+ GCC_except_table105
+ GCC_except_table113
+ GCC_except_table115
+ GCC_except_table118
+ GCC_except_table124
+ GCC_except_table132
+ GCC_except_table138
+ GCC_except_table145
+ GCC_except_table152
+ GCC_except_table165
+ GCC_except_table174
+ GCC_except_table177
+ GCC_except_table203
+ GCC_except_table209
+ GCC_except_table224
+ GCC_except_table230
+ GCC_except_table242
+ GCC_except_table254
+ GCC_except_table266
+ GCC_except_table366
+ GCC_except_table83
+ GCC_except_table96
+ OBJC_IVAR_$_SHKSharingServicePicker._testingSnapshot
+ SHKAppHasGelatoEntitlement.cold.1
+ SHKMetricsLog.cold.1
+ SHK_AlwaysAllowPerformingServices.cold.1
+ SHK_AlwaysAllowQueryingServices.cold.1
+ SHK_CachedFileHandleFromImage.cold.5
+ SHK_RunningInPlugin.cold.1
+ _OBJC_CLASS_$_SFShareSheetSessionTestingSnapshot
+ _OUTLINED_FUNCTION_10
+ __51-[SHKSharingService handleMacExtensionWithOptions:]_block_invoke.628.cold.2
+ __51-[SHKSharingService handleMacExtensionWithOptions:]_block_invoke_2.cold.1
+ __55-[SHKSharingService executeHandler:onTimeoutInSeconds:]_block_invoke.cold.1
+ __60-[SHKSharingService handleIOSMacExtensionWithExtensionItem:]_block_invoke.cold.3
+ __62-[SHKSharingService launchExtensionWithExtensionItem:options:]_block_invoke_2.cold.2
+ __62-[SHKSharingService launchExtensionWithExtensionItem:options:]_block_invoke_2.cold.3
+ __62-[SHKSharingService launchExtensionWithExtensionItem:options:]_block_invoke_2.cold.4
+ __68-[SHKSharingServicePicker _configureShareSheetRemoteViewController:]_block_invoke.448
+ __68-[SHKSharingServicePicker _configureShareSheetRemoteViewController:]_block_invoke.452
+ __68-[SHKSharingServicePicker _configureShareSheetRemoteViewController:]_block_invoke_2.453
+ __80-[NSSharingUIExtensionContext getPreviewImageForAttachments:block:timeoutBlock:]_block_invoke.130.cold.4
+ __85-[SHKSharingServicePicker showPopoverRelativeToRect:ofView:preferredEdge:completion:]_block_invoke.422
+ __85-[SHKSharingServicePicker showPopoverRelativeToRect:ofView:preferredEdge:completion:]_block_invoke.441
+ __85-[SHKSharingServicePicker showPopoverRelativeToRect:ofView:preferredEdge:completion:]_block_invoke.441.cold.1
+ __85-[SHKSharingServicePicker showPopoverRelativeToRect:ofView:preferredEdge:completion:]_block_invoke.442
+ __87-[SHKRemoteWindowController setHostWindowFrame:withClientWindowSync:blurAndShadowSync:]_block_invoke.cold.1
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SFActivityItemsService
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SFActivityItemsService
+ __OBJC_$_PROTOCOL_REFS_SFActivityItemsService
+ __OBJC_LABEL_PROTOCOL_$_SFActivityItemsService
+ __OBJC_PROTOCOL_$_SFActivityItemsService
+ ___43-[SHKCollaborationService canShareFileURL:]_block_invoke
+ ___86-[SHKSharingServicePicker _populateCollaborativeSharingServicesForPopoverPresentation]_block_invoke
+ ___89-[SHKSharingServicePicker _populateNonCollaborativeSharingServicesForPopoverPresentation]_block_invoke
+ ___block_descriptor_40_e8_32r_e8_v12?0B8l
+ ___block_descriptor_48_e8_32s40s_e34_v32?0"SHKSharingService"8Q16^B24l
+ __block_literal_global.1024
+ __block_literal_global.318
+ __block_literal_global.320
+ __block_literal_global.323
+ __block_literal_global.325
+ __block_literal_global.986
+ __block_literal_global.990
+ _objc_msgSend$canShareFileURL:completion:
+ _objc_msgSend$enumerateObjectsUsingBlock:
+ _objc_msgSend$initWithItems:applicationBundleID:pid:
+ _objc_msgSend$setTestingSnapshot:
+ _objc_msgSend$shareSheetSessionEndedWithTestingSnapshot:
+ _objc_msgSend$testingSnapshot
+ _objc_msgSend$updateWithDiscoveredShareActivities:visibleShareActivities:actionActivities:visibleActionActivities:forCollaboration:
+ _objc_msgSend$updateWithFinalItems:forActivityType:forCollaboration:
+ _objc_msgSend$updateWithPlaceholderItems:collaborationItem:supportsCollaboration:supportsSendCopy:
+ _wrappedError.cold.1
+ framework_log.cold.1
+ initAnalyticsSendEvent.cold.1
+ initCKAsset.cold.1
+ initCKContainerID.cold.1
+ initCKContainerSetupInfo.cold.1
+ initCKEncryptedDate.cold.1
+ initCKEncryptedDouble.cold.1
+ initCKEncryptedLocation.cold.1
+ initCKEncryptedLongLong.cold.1
+ initCKEncryptedReference.cold.1
+ initCKEncryptedString.cold.1
+ initCKRecordID.cold.1
+ initCKRecordValueStore.cold.1
+ initCKRecordZoneID.cold.1
+ initCKReference.cold.1
+ initCKShare.cold.1
+ initCKShareParticipant.cold.1
+ initCKUserIdentity.cold.1
+ initCKUserIdentityLookupInfo.cold.1
+ initCSAddParticipantsViewController.cold.1
+ initIMHandle.cold.1
+ initLPImage.cold.1
+ initLPLinkMetadata.cold.1
+ initSLCollaborationFooterViewModel.cold.1
+ initSOCompletionResult.cold.1
+ initTUCallCenter.cold.1
+ init_NSPersonNameComponentsData.cold.1
+ init_SWCollaborationMetadata.cold.1
+ init_SWCollaborationOptionsGroup.cold.1
+ init_SWCollaborationShareOptions.cold.1
+ init_SWPendingCollaboration.cold.1
+ plugin_log.cold.1
- -[SHKSharingService setActivityType:]
- GCC_except_table104
- GCC_except_table112
- GCC_except_table117
- GCC_except_table123
- GCC_except_table131
- GCC_except_table136
- GCC_except_table144
- GCC_except_table151
- GCC_except_table164
- GCC_except_table173
- GCC_except_table176
- GCC_except_table202
- GCC_except_table207
- GCC_except_table222
- GCC_except_table229
- GCC_except_table241
- GCC_except_table253
- GCC_except_table265
- GCC_except_table364
- GCC_except_table95
- OBJC_IVAR_$_SHKSharingService._activityType
- __68-[SHKSharingServicePicker _configureShareSheetRemoteViewController:]_block_invoke.446
- __68-[SHKSharingServicePicker _configureShareSheetRemoteViewController:]_block_invoke.450
- __68-[SHKSharingServicePicker _configureShareSheetRemoteViewController:]_block_invoke_2.451
- __85-[SHKSharingServicePicker showPopoverRelativeToRect:ofView:preferredEdge:completion:]_block_invoke.420
- __85-[SHKSharingServicePicker showPopoverRelativeToRect:ofView:preferredEdge:completion:]_block_invoke.439
- __85-[SHKSharingServicePicker showPopoverRelativeToRect:ofView:preferredEdge:completion:]_block_invoke.439.cold.1
- __85-[SHKSharingServicePicker showPopoverRelativeToRect:ofView:preferredEdge:completion:]_block_invoke.440
- __block_literal_global.1014
- __block_literal_global.317
- __block_literal_global.322
- __block_literal_global.324
- __block_literal_global.976
- __block_literal_global.980
- _objc_msgSend$setActivityType:
CStrings:
+ "@\"SFShareSheetSessionTestingSnapshot\""
+ "B24@0:8@\"NSURL\"16"
+ "SFActivityItemsService"
+ "ShareSheetSnapshotCollection"
+ "T@\"NSString\",R,C,N"
+ "T@\"SFShareSheetSessionTestingSnapshot\",&,N,V_testingSnapshot"
+ "_testingSnapshot"
+ "canShareFileURL:"
+ "canShareFileURL:completion:"
+ "enumerateObjectsUsingBlock:"
+ "initWithItems:applicationBundleID:pid:"
+ "setTestingSnapshot:"
+ "shareSheetSessionEndedWithTestingSnapshot:"
+ "testingSnapshot"
+ "updateWithDiscoveredShareActivities:visibleShareActivities:actionActivities:visibleActionActivities:forCollaboration:"
+ "updateWithFinalItems:forActivityType:forCollaboration:"
+ "updateWithPlaceholderItems:collaborationItem:supportsCollaboration:supportsSendCopy:"
+ "v32@?0@\"SHKSharingService\"8Q16^B24"
- "T@\"NSString\",C,N"
- "T@\"NSString\",C,N,V_activityType"
- "_activityType"
- "setActivityType:"
- "v24@0:8@\"NSString\"16"

```
