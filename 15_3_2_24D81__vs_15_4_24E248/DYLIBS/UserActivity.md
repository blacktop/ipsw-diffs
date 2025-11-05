## UserActivity

> `/System/Library/PrivateFrameworks/UserActivity.framework/Versions/A/UserActivity`

```diff

-587.1.0.0.0
-  __TEXT.__text: 0x4abd0
-  __TEXT.__auth_stubs: 0x8b0
-  __TEXT.__objc_methlist: 0x255c
+594.0.0.0.0
+  __TEXT.__text: 0x4a87c
+  __TEXT.__auth_stubs: 0x8a0
+  __TEXT.__objc_methlist: 0x2b48
   __TEXT.__const: 0x1c8
-  __TEXT.__cstring: 0x2781
+  __TEXT.__cstring: 0x277f
   __TEXT.__oslogstring: 0x4f61
-  __TEXT.__gcc_except_tab: 0x5324
+  __TEXT.__gcc_except_tab: 0x52f4
   __TEXT.__dof_UA: 0x1c51
-  __TEXT.__unwind_info: 0x15d8
+  __TEXT.__unwind_info: 0x15c0
   __TEXT.__objc_classname: 0x67f
   __TEXT.__objc_methname: 0x7cf9
   __TEXT.__objc_methtype: 0x1182

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1ce0
+  __DATA_CONST.__objc_selrefs: 0x1d80
   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_superrefs: 0x88
   __DATA_CONST.__objc_arraydata: 0xe0
-  __AUTH_CONST.__auth_got: 0x470
+  __AUTH_CONST.__auth_got: 0x468
   __AUTH_CONST.__const: 0x1c00
   __AUTH_CONST.__cfstring: 0x2400
-  __AUTH_CONST.__objc_const: 0x7dd0
+  __AUTH_CONST.__objc_const: 0x7310
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x78

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 49BE8BDF-DF45-36DD-9CFE-BAFEA96B67B2
-  Functions: 1323
-  Symbols:   3488
-  CStrings:  2544
+  UUID: 2FABCC51-4CC6-3496-9EAB-5F20E8E8431B
+  Functions: 1360
+  Symbols:   3564
+  CStrings:  2543
 
Symbols:
+ +[UASharedPasteboard remotePasteboard].cold.1
+ +[UASharedPasteboardIRManager sharedIRManager].cold.1
+ +[UASharedPasteboardManager sharedManager].cold.1
+ +[UAUserActivity addUserActivityObserver:].cold.1
+ +[UAUserActivity(Internal) allowedWebpageURLSchemes].cold.1
+ +[UAUserActivity(UAUserActivitySiriActions) mainBundleIdentifier].cold.1
+ +[UAUserActivityManager defaultManager].cold.1
+ -[UAUserActivity becomeCurrent].cold.1
+ -[UAUserActivity becomeCurrent].cold.2
+ -[UAUserActivity invalidate].cold.1
+ -[UAUserActivity resignCurrent].cold.1
+ -[UAUserActivity setDirty:].cold.1
+ -[UAUserActivity setNeedsSave:].cold.1
+ -[UAUserActivity setUserInfo:].cold.1
+ -[UAUserActivity(Internal) displayInDtrace].cold.1
+ -[UAUserActivity(Internal) scheduleSendUserActivityInfoToLSUserActivityd].cold.1
+ -[UAUserActivity(Internal) sendUserActivityInfoToLSUserActivityd:onAsyncQueue:].cold.1
+ -[UAUserActivity(Internal) tellDaemonAboutNewLSUserActivity].cold.1
+ -[UAUserActivity(Legacy) addContentAttribute:forKey:].cold.1
+ -[UAUserActivity(Legacy) addContentAttribute:forKey:].cold.2
+ -[UAUserActivity(Legacy) contentAttributes].cold.1
+ -[UAUserActivity(Legacy) contentAttributes].cold.2
+ -[UAUserActivity(Legacy) contentType].cold.1
+ -[UAUserActivity(Legacy) contentType].cold.2
+ -[UAUserActivity(Legacy) removeContentAttribute:].cold.1
+ -[UAUserActivity(Legacy) removeContentAttribute:].cold.2
+ -[UAUserActivity(Legacy) setContentAttributes:].cold.1
+ -[UAUserActivity(Legacy) setContentAttributes:].cold.2
+ -[UAUserActivity(Legacy) setContentType:].cold.1
+ -[UAUserActivity(Legacy) setContentType:].cold.2
+ -[UAUserActivity(Legacy) setSubtitle:].cold.1
+ -[UAUserActivity(Legacy) setSubtitle:].cold.2
+ -[UAUserActivity(Legacy) subtitle].cold.1
+ -[UAUserActivity(Legacy) subtitle].cold.2
+ -[UAUserActivity(UAUserActivityCoreSpotlightIndexingSupport) indexActivity:forceIndexing:].cold.1
+ -[UAUserActivityInfo initWithCoder:].cold.1
+ -[UAUserActivityInfo initWithCoder:].cold.2
+ -[UAUserActivityManager askClientUserActivityToSave:].cold.1
+ -[UAUserActivityManager askClientUserActivityToSave:completionHandler:].cold.1
+ -[UAUserActivityManager connection].cold.1
+ -[UAUserActivityManager sendUserActivityInfoToLSUserActivityd:makeCurrent:].cold.1
+ -[UAUserActivityManager tellClientUserActivityItWasResumed:].cold.1
+ -[UAUserActivityManager tellClientUserActivityItWasResumed:].cold.2
+ _LSGetBestAppSuggestionManagerProtocolInterface.cold.1
+ _LSGetBestAppSuggestionManagerResponseProtocolInterface.cold.1
+ _LSGetResumableActivitiesAdministrativeProtocolInterface.cold.1
+ _LSGetResumableActivitiesSysdiagnoseSupportProtocolInterface.cold.1
+ _LSGetUserActivityClientProtocolInterface.cold.1
+ _LSGetUserActivityClientResponseProtocolInterface.cold.1
+ _UAGetSharedPasteboardAUXProtocolInterface.cold.1
+ _UAGetSharedPasteboardControllProtocolInterface.cold.1
+ _UAGetSharedPasteboardManagerProtocolInterface.cold.1
+ _UAGetSharedPasteboardManagerResponseProtocolInterface.cold.1
+ _Z23_UAGetAuditTokenForSelfv.cold.1
+ _ZL20getIndexPendingQueuev.cold.1
+ _ZL22initSYActivityObserverv.cold.1
+ _ZL24uaUserActivityObjectsMapv.cold.1
+ _ZL25initSFCompanionAdvertiserv.cold.1
+ _ZL26suggestedActionNudgesQueuev.cold.1
+ _ZL35getSupportsContinuationStreamsQueuev.cold.1
+ _ZL36getUAUserActivityToNSUserActivityMapv.cold.1
+ __109-[UAUserActivity(Internal) callWillSaveDelegateIfDirtyAndPackageUpData:options:clearDirty:completionHandler:]_block_invoke.cold.1
+ __109-[UAUserActivity(Internal) callWillSaveDelegateIfDirtyAndPackageUpData:options:clearDirty:completionHandler:]_block_invoke.cold.2
+ __109-[UAUserActivity(Internal) callWillSaveDelegateIfDirtyAndPackageUpData:options:clearDirty:completionHandler:]_block_invoke.cold.3
+ __35-[UAUserActivityManager connection]_block_invoke.cold.1
+ __35-[UAUserActivityManager connection]_block_invoke_2.cold.1
+ __44-[UAUserActivity(Internal) copyWithNewUUID:]_block_invoke.cold.1
+ __44-[UAUserActivity(Internal) copyWithNewUUID:]_block_invoke.cold.2
+ __91-[UAUserActivity(Internal) callWillSaveDelegateIfDirtyAndPackageUpData:options:clearDirty:]_block_invoke.cold.1
+ __91-[UAUserActivity(Internal) callWillSaveDelegateIfDirtyAndPackageUpData:options:clearDirty:]_block_invoke.cold.2
+ __91-[UAUserActivity(Internal) callWillSaveDelegateIfDirtyAndPackageUpData:options:clearDirty:]_block_invoke.cold.3
+ __97-[UAUserActivityManager fetchUUID:intervalToWaitForDocumentSynchonization:withCompletionHandler:]_block_invoke.37.cold.1
+ __97-[UAUserActivityManager fetchUUID:intervalToWaitForDocumentSynchonization:withCompletionHandler:]_block_invoke.39.cold.1
+ __97-[UAUserActivityManager fetchUUID:intervalToWaitForDocumentSynchonization:withCompletionHandler:]_block_invoke.39.cold.2
+ biomeInfoLogging.cold.1
+ initSFPeerDevice.cold.1
- _strcmp

```
