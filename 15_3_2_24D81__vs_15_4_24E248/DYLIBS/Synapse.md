## Synapse

> `/System/Library/PrivateFrameworks/Synapse.framework/Versions/A/Synapse`

```diff

-137.100.0.0.0
-  __TEXT.__text: 0x3ce0c
+137.301.0.0.0
+  __TEXT.__text: 0x3dca0
   __TEXT.__auth_stubs: 0x590
-  __TEXT.__objc_methlist: 0x2b68
+  __TEXT.__objc_methlist: 0x3154
   __TEXT.__const: 0x168
-  __TEXT.__gcc_except_tab: 0xb54
+  __TEXT.__gcc_except_tab: 0xb90
   __TEXT.__cstring: 0x2c12
   __TEXT.__oslogstring: 0x44df
   __TEXT.__ustring: 0x16e
   __TEXT.__dlopen_cstrs: 0x3bc
-  __TEXT.__unwind_info: 0x10c8
+  __TEXT.__unwind_info: 0x1198
   __TEXT.__objc_classname: 0xac2
   __TEXT.__objc_methname: 0x81c3
   __TEXT.__objc_methtype: 0x130c

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1bb0
+  __DATA_CONST.__objc_selrefs: 0x1c80
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x168
   __DATA_CONST.__objc_arraydata: 0x40
   __AUTH_CONST.__auth_got: 0x2d8
   __AUTH_CONST.__const: 0x1650
   __AUTH_CONST.__cfstring: 0x2380
-  __AUTH_CONST.__objc_const: 0xcec8
+  __AUTH_CONST.__objc_const: 0xc4a8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x14f0
   __DATA.__objc_ivar: 0x2b0

   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/Versions/A/ProtocolBuffer
   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /System/Library/PrivateFrameworks/URLFormatting.framework/Versions/A/URLFormatting
-  - /System/Library/PrivateFrameworks/UserActivity.framework/Versions/A/UserActivity
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EBA917B4-8241-3D9E-B366-000E9718C976
-  Functions: 1417
-  Symbols:   3810
+  UUID: 3884CBBE-79A7-329A-AA0F-A8DF95408FB0
+  Functions: 1486
+  Symbols:   3885
   CStrings:  2490
 
Symbols:
+ +[NSUserActivity(SYInternalExtensions) _syFetchCurrentUserActivityWithCompletion:].cold.1
+ +[SYActivityObserver loadSynapseObserver].cold.1
+ +[SYActivityObserver sharedInstance].cold.1
+ +[SYBacklinkIndicatorClient clientWithDomainIdentifiers:linkIdentifiers:].cold.1
+ +[SYBacklinkIndicatorService sharedInstance].cold.1
+ +[SYBacklinkIndicatorUsageService sharedInstance].cold.1
+ +[SYContentItemManager sharedManager].cold.1
+ +[SYContentItemPreviewManager _loadPreviewUsingLPForItem:fullDetail:completion:].cold.1
+ +[SYDocumentFetchRequest _fetchDocumentsWithReason:queryString:completion:].cold.2
+ +[SYDocumentWorkflowsDisabledDataStore _disabledRepositoryError].cold.1
+ +[SYFeatureEligibility supportsQuickNote].cold.1
+ +[SYFormFillingDocumentAttributes _formFillingDocumentAttributesForFileAtURL:completion:].cold.1
+ +[SYItemIndexingManager _customKeyForKey:].cold.1
+ +[SYItemIndexingManager _fetchIndexedActivitiesWithActivityType:completion:].cold.1
+ +[SYItemIndexingManager _fetchIndexedActivitiesWithActivityType:completion:].cold.2
+ +[SYItemIndexingManager _fetchIndexedItemsLinkedToUserActivity:extraFetchAttributes:completion:].cold.3
+ +[SYItemIndexingManager _fetchIndexedItemsLinkedToUserActivity:extraFetchAttributes:completion:].cold.4
+ +[SYItemIndexingManager searchableItemLinkingContentItem:toContainerIdentifier:uniqueIdentifier:relatedIdentifier:domainIdentifier:].cold.2
+ +[SYItemIndexingManager searchableItemLinkingContentItem:toContainerIdentifier:uniqueIdentifier:relatedIdentifier:domainIdentifier:].cold.3
+ +[SYLastModifiedDocumentFetchRequest fetchLastModifiedDocument:completion:].cold.2
+ +[SYSerializationSupport archiveDataFromData:formatIdentifier:majorVersion:minorVersion:].cold.1
+ +[SYSerializationSupport archiveDataFromData:formatIdentifier:majorVersion:minorVersion:].cold.2
+ +[SYSerializationSupport itemDataFromArchiveData:majorVersion:minorVersion:error:].cold.1
+ -[SYAddLinkContextClient _configureConnectionAndResume].cold.1
+ -[SYAddLinkContextService listener:shouldAcceptNewConnection:].cold.2
+ -[SYBacklinkIndicatorClient _configureConnectionAndResume].cold.1
+ -[SYBacklinkIndicatorService listener:shouldAcceptNewConnection:].cold.1
+ -[SYBacklinkIndicatorUsageService listener:shouldAcceptNewConnection:].cold.1
+ -[SYBacklinkMonitor _beginNewOperation].cold.1
+ -[SYBacklinkMonitor backlinkMonitorOperationDidFinish:].cold.1
+ -[SYBacklinkMonitorClient _configureConnectionAndResume].cold.1
+ -[SYBacklinkMonitorService _evaluateAndBeginPendingOperations].cold.1
+ -[SYBacklinkMonitorService listener:shouldAcceptNewConnection:].cold.1
+ -[SYContentItem initWithData:error:].cold.2
+ -[SYContentItem initWithDisplayTitle:sourceIdentifier:sourceName:itemURL:identifier:].cold.1
+ -[SYContentItem initWithDisplayTitle:sourceIdentifier:sourceName:itemURL:identifier:].cold.2
+ -[SYContentItem initWithItemIdentifier:displayTitle:sourceIdentifier:sourceName:itemURL:activityType:activityCanonicalURL:activityTargetContentIdentifier:activityPersistentIdentifier:userActivity:].cold.1
+ -[SYContentItem initWithItemIdentifier:displayTitle:sourceIdentifier:sourceName:itemURL:activityType:activityCanonicalURL:activityTargetContentIdentifier:activityPersistentIdentifier:userActivity:].cold.2
+ -[SYContentItem initWithItemIdentifier:displayTitle:sourceIdentifier:sourceName:itemURL:activityType:activityCanonicalURL:activityTargetContentIdentifier:activityPersistentIdentifier:userActivity:].cold.3
+ -[SYContentItem initWithUserActivity:sourceAppID:sourceAppName:identifier:].cold.1
+ -[SYContentItem initWithUserActivity:sourceAppID:sourceAppName:identifier:].cold.2
+ -[SYContentItemManager _navigateToURL:completion:].cold.1
+ -[SYContentItemManager _navigateToUserActivity:completion:].cold.1
+ -[SYDefaultsClient _configureConnectionAndResume].cold.1
+ -[SYDocumentSenderAvatar fetchThumbnailImages].cold.1
+ -[SYDocumentSenderAvatar fetchThumbnailImages].cold.2
+ -[SYLinkContextClient _configureConnectionAndResume].cold.1
+ -[SYLinkContextClient _processFetchLinkContextsRequestForUserActivity:serviceProxy:completion:].cold.2
+ -[SYLinkContextClient _processFetchLinkContextsRequestForUserActivity:serviceProxy:completion:].cold.3
+ -[SYLinkContextClient _processFetchLinkContextsRequestForUserActivity:serviceProxy:completion:].cold.4
+ -[SYLinkContextClient _sendRequestToCreateLinkWithContentItemData:preferNewDocument:completion:].cold.1
+ -[SYLinkContextClient createAndShowContextualLinkWithUserActivity:linkPreviewMetadata:preferNewDocument:completion:].cold.1
+ -[SYLinkContextClient createAndShowContextualLinkWithUserActivity:linkPreviewMetadata:preferNewDocument:completion:].cold.2
+ -[SYLinkContextClient fetchLinkContextsForUserActivity:completion:].cold.1
+ -[SYLinkContextClient fetchLinkContextsForUserActivity:completion:].cold.2
+ -[SYLinkContextClient insertImagesData:completion:].cold.1
+ -[SYLinkContextClient insertImagesData:completion:].cold.2
+ -[SYLinkContextService listener:shouldAcceptNewConnection:].cold.2
+ -[SYLinkableContentItemFinder _fetchActiveLinkableUserActivitiesExcluding:completion:].cold.2
+ -[SYNotesActivationCommand _loadDataFromFileURLs:withCompletion:].cold.1
+ -[SYRunningApplicationsObserver startObservingRunningApplicationsWithHandler:].cold.1
+ -[SYUserActivityIdentifierInfo initWithActivityType:].cold.1
+ GCC_except_table30
+ GCC_except_table88
+ SYIsMailApp.cold.1
+ SYIsPreviewApp.cold.1
+ SYIsiWorkApp.cold.1
+ SYSupportedLinkContextInfoClasses.cold.1
+ _OUTLINED_FUNCTION_5
+ _SYBundle.cold.1
+ __87-[SYLinkableContentItemFinder fetchLinkableContentItemsExcludingActivities:completion:]_block_invoke_2.cold.1
- GCC_except_table29
- GCC_except_table77

```
