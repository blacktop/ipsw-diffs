## BackgroundTaskManagement

> `/System/Library/PrivateFrameworks/BackgroundTaskManagement.framework/Versions/A/BackgroundTaskManagement`

```diff

-294.9.0.0.0
-  __TEXT.__text: 0x205c4
+302.3.0.0.0
+  __TEXT.__text: 0x1fc9c
   __TEXT.__auth_stubs: 0x4d0
-  __TEXT.__objc_methlist: 0x131c
+  __TEXT.__objc_methlist: 0x17c4
   __TEXT.__const: 0xe0
   __TEXT.__oslogstring: 0x1962
   __TEXT.__cstring: 0x1a6e
-  __TEXT.__gcc_except_tab: 0xcc8
-  __TEXT.__unwind_info: 0x938
+  __TEXT.__gcc_except_tab: 0xce0
+  __TEXT.__unwind_info: 0x980
   __TEXT.__objc_classname: 0x1ed
   __TEXT.__objc_methname: 0x3b8c
   __TEXT.__objc_methtype: 0x108f

   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf48
+  __DATA_CONST.__objc_selrefs: 0xff8
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x68
   __AUTH_CONST.__auth_got: 0x278
   __AUTH_CONST.__const: 0xb30
   __AUTH_CONST.__cfstring: 0x1380
-  __AUTH_CONST.__objc_const: 0x2830
+  __AUTH_CONST.__objc_const: 0x1f68
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x410
   __DATA.__objc_ivar: 0x110

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libTLE.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A3DD0080-8E6B-3DE9-BA99-A0337CBC0E59
-  Functions: 769
-  Symbols:   1770
+  UUID: 9EC53D34-7098-3523-B816-102B6CAAE74D
+  Functions: 790
+  Symbols:   1957
   CStrings:  1406
 
Symbols:
+ +[BTMAgentConnection sharedInstance].cold.1
+ +[BTMBackgroundTaskManager sharedInstance].cold.1
+ +[NSData(BTMAdditions) __btm_bookmarkDataWithURL:].cold.2
+ -[BTMAgentConnection addLoginItem:reply:].cold.2
+ -[BTMAgentConnection connection].cold.1
+ -[BTMAgentConnection getBackgroundItemsWithReply:].cold.2
+ -[BTMAgentConnection getLoginItemsWithTypeMask:reply:].cold.2
+ -[BTMAgentConnection importSFLLoginItemsAndDeleteWhenDone:].cold.2
+ -[BTMAgentConnection openLoginItemsWithReply:].cold.2
+ -[BTMAgentConnection removeLoginItem:reply:].cold.2
+ -[BTMAgentConnection setUserElection:forBackgroundItem:reply:].cold.3
+ -[BTMAgentConnection setUserElection:forBackgroundItem:reply:].cold.4
+ -[BTMAgentConnection setUserElection:forURL:reply:].cold.2
+ -[BTMBackgroundItem initWithURL:].cold.2
+ -[BTMBackgroundItemController _setBackgroundItems:].cold.2
+ -[BTMBackgroundItemController handleBackgroundItemsChangeNotification:].cold.2
+ -[BTMBackgroundItemController initWithDelegate:].cold.2
+ -[BTMCodeSignInfo initWithURL:error:].cold.1
+ -[BTMCodeSignInfo lightweightCodeRequirement].cold.2
+ -[BTMFetchResult initWithCode:items:].cold.1
+ -[BTMFetchResult initWithCode:items:].cold.2
+ -[BTMFetchResult initWithCoder:].cold.1
+ -[BTMFetchResult initWithCoder:].cold.2
+ -[BTMItem effectiveDisposition].cold.4
+ -[BTMItem effectiveDisposition].cold.5
+ -[BTMItem effectiveDisposition].cold.6
+ -[BTMItem fullPath].cold.2
+ -[BTMItem localizedName].cold.1
+ -[BTMItem setPropertiesWithBTMConfig:].cold.2
+ -[BTMItem syncURLAndBookmark].cold.10
+ -[BTMItem syncURLAndBookmark].cold.6
+ -[BTMItem syncURLAndBookmark].cold.7
+ -[BTMItem syncURLAndBookmark].cold.8
+ -[BTMItem syncURLAndBookmark].cold.9
+ -[BTMList addListObserver:].cold.2
+ -[BTMList refresh].cold.2
+ -[BTMList removeListObserver:].cold.2
+ -[BTMLoginItem initWithURL:hidden:].cold.2
+ -[BTMLoginItemController _setLoginItems:].cold.2
+ -[BTMLoginItemController handleLoginItemsChangeNotification:].cold.2
+ -[BTMLoginItemController initWithTypeMask:delegate:].cold.2
+ -[BTMManager addSFLItemWithURL:type:global:managed:error:].cold.1
+ -[BTMManager addUserItemForURL:uid:error:].cold.4
+ -[BTMManager addUserItemForURL:uid:error:].cold.5
+ -[BTMManager addUserItemForURL:uid:error:].cold.6
+ -[BTMManager addUserItemForURL:uid:error:].cold.7
+ -[BTMManager canLaunchItemWithAppURL:type:relativeURL:configuration:].cold.2
+ -[BTMManager eraseDatabaseWithAuthorization:error:].cold.1
+ -[BTMManager fetchItemWithAppURL:type:relativeURL:configuration:uid:].cold.2
+ -[BTMManager fetchItemWithAppURL:type:relativeURL:configuration:uid:].cold.3
+ -[BTMManager fetchItemWithAppURL:type:relativeURL:configuration:uid:].cold.4
+ -[BTMManager fetchItemWithAppURL:type:relativeURL:configuration:uid:].cold.5
+ -[BTMManager getAlwaysPostNotifications:].cold.1
+ -[BTMManager getEffectiveDisposition:andLWCR:forAppURL:type:relativeURL:configuration:uid:].cold.2
+ -[BTMManager getEffectiveDisposition:andLWCR:forAppURL:type:relativeURL:configuration:uid:].cold.3
+ -[BTMManager getEffectiveDisposition:andLWCR:withAuditToken:type:relativeURL:configuration:uid:].cold.2
+ -[BTMManager getEffectiveDisposition:andLWCR:withAuditToken:type:relativeURL:configuration:uid:].cold.3
+ -[BTMManager getItemDisposition:withAppURL:type:relativeURL:configuration:uid:].cold.2
+ -[BTMManager getItemsMatching:uid:error:].cold.2
+ -[BTMManager handleNotificationResponseWithIdentifier:action:].cold.2
+ -[BTMManager handleUserDataDidChangeNotification:].cold.1
+ -[BTMManager handleUserDataDidChangeNotification:].cold.2
+ -[BTMManager handleUserDataDidChangeNotification:].cold.3
+ -[BTMManager handleUserDataDidChangeNotification:].cold.4
+ -[BTMManager importSFLLoginItemFromURL:uid:deleteWhenDone:].cold.2
+ -[BTMManager invalidateLaunchItemWithBundleURL:type:itemURL:configuration:uid:].cold.2
+ -[BTMManager mdmPayloadForIdentifier:].cold.2
+ -[BTMManager removeItem:uid:error:].cold.2
+ -[BTMManager removeManagedJobAtPath:error:].cold.2
+ -[BTMManager removeManagedJobWithLabel:error:].cold.2
+ -[BTMManager removeSFLItem:error:].cold.1
+ -[BTMManager setAlwaysPostNotifications:].cold.1
+ -[BTMManager setMDMPayload:identifier:updateImmediately:].cold.2
+ -[BTMManager submitManagedJobAtPath:error:].cold.2
+ -[BTMManager updateItems:uid:error:].cold.2
+ -[BTMManager updateSFLItem:error:].cold.1
+ -[BTMRegistrar fetchItemWithAppURL:type:relativeURL:configuration:uid:].cold.2
+ -[BTMRegistrar getEffectiveDisposition:andLWCR:forAppURL:type:relativeURL:configuration:uid:].cold.2
+ -[BTMRegistrar getEffectiveDisposition:andLWCR:forAppURL:type:relativeURL:configuration:uid:].cold.3
+ -[NSData(BTMAdditions) __btm_resolveBookmarkWithOptions:relativeToURL:bookmarkDataIsStale:error:].cold.2
+ AttributionsByLabel.cold.1
+ AttributionsContainsLabelOrAttributionValue.cold.1
+ BTMGetEnablementStatusForSubsystemAndUID.cold.3
+ BTMGetEnablementStatusForSubsystemAndUID.cold.4
+ BTMHaveEnablementStatusForSubsystemAndUID.cold.3
+ BTMHaveEnablementStatusForSubsystemAndUID.cold.4
+ BTMResetEnablementStatusForSubsystemAndUID.cold.2
+ BTMSetEnablementStatusForSubsystemAndUID.cold.3
+ BTMSetEnablementStatusForSubsystemAndUID.cold.4
+ CuratedAssociatedBundleIdentifiersForLabelAndTeamID.cold.2
+ CuratedAssociatedBundleIdentifiersForLabelAndTeamID.cold.3
+ CuratedDeveloperNameForLabelAndTeamID.cold.2
+ CuratedInternalAssociatedBundleIdentifiersForLabel.cold.2
+ CuratedInternalAssociatedBundleIdentifiersForLabel.cold.3
+ CuratedInternalNameForLabel.cold.2
+ InternalAttributionsByLabel.cold.1
+ ItemIdentifierWithRegistrationInfo.cold.1
+ __31-[BTMManager noteLogoutForUID:]_block_invoke.156.cold.2
+ __31-[BTMManager noteLogoutForUID:]_block_invoke.cold.2
+ __31-[BTMManager saveUserSettings:]_block_invoke.43.cold.2
+ __31-[BTMManager saveUserSettings:]_block_invoke.cold.2
+ __32-[BTMManager addItem:uid:error:]_block_invoke_2.cold.1
+ __33-[BTMManager launchdDidScanPath:]_block_invoke.cold.2
+ __33-[BTMManager userSettingsForUID:]_block_invoke.37.cold.2
+ __33-[BTMManager userSettingsForUID:]_block_invoke.cold.2
+ __34-[BTMManager launchdWillScanPath:]_block_invoke.cold.2
+ __34-[BTMManager removeSFLItem:error:]_block_invoke.130.cold.2
+ __34-[BTMManager removeSFLItem:error:]_block_invoke.cold.2
+ __34-[BTMManager updateSFLItem:error:]_block_invoke.129.cold.2
+ __34-[BTMManager updateSFLItem:error:]_block_invoke.cold.2
+ __36-[BTMManager updateItems:uid:error:]_block_invoke_2.cold.2
+ __36-[BTMManager userIdentifiersAndUIDs]_block_invoke.cold.2
+ __38-[BTMItem setPropertiesWithBTMConfig:]_block_invoke.157.cold.2
+ __38-[BTMItem setPropertiesWithBTMConfig:]_block_invoke.cold.2
+ __38-[BTMItem setPropertiesWithBTMConfig:]_block_invoke.cold.3
+ __38-[BTMManager mdmPayloadForIdentifier:]_block_invoke.cold.2
+ __39-[BTMLoginItemController addLoginItem:]_block_invoke.cold.2
+ __39-[BTMManager scheduleGarbageCollection]_block_invoke.cold.2
+ __41-[BTMAgentConnection addLoginItem:reply:]_block_invoke.cold.2
+ __41-[BTMLoginItemController fetchLoginItems]_block_invoke.cold.2
+ __41-[BTMManager getAlwaysPostNotifications:]_block_invoke.cold.2
+ __41-[BTMManager setAlwaysPostNotifications:]_block_invoke.cold.2
+ __42-[BTMLoginItemController removeLoginItem:]_block_invoke.cold.2
+ __42-[BTMManager _getItemsMatching:uid:error:]_block_invoke.111.cold.2
+ __42-[BTMManager _getItemsMatching:uid:error:]_block_invoke.cold.2
+ __42-[BTMManager addUserItemForURL:uid:error:]_block_invoke.121.cold.2
+ __42-[BTMManager addUserItemForURL:uid:error:]_block_invoke.cold.2
+ __42-[BTMManager fetchItemWithUUID:uid:error:]_block_invoke.cold.2
+ __42-[BTMManager fetchSFLItemsMatching:error:]_block_invoke.124.cold.2
+ __42-[BTMManager fetchSFLItemsMatching:error:]_block_invoke.cold.2
+ __43-[BTMManager removeManagedJobAtPath:error:]_block_invoke.152.cold.2
+ __43-[BTMManager removeManagedJobAtPath:error:]_block_invoke.cold.2
+ __43-[BTMManager submitManagedJobAtPath:error:]_block_invoke.151.cold.2
+ __43-[BTMManager submitManagedJobAtPath:error:]_block_invoke.cold.2
+ __44-[BTMAgentConnection removeLoginItem:reply:]_block_invoke.cold.2
+ __46-[BTMAgentConnection openLoginItemsWithReply:]_block_invoke.12.cold.2
+ __46-[BTMAgentConnection openLoginItemsWithReply:]_block_invoke.cold.2
+ __46-[BTMManager getItemWithIdentifier:uid:error:]_block_invoke.cold.2
+ __46-[BTMManager removeManagedJobWithLabel:error:]_block_invoke.153.cold.2
+ __46-[BTMManager removeManagedJobWithLabel:error:]_block_invoke.cold.2
+ __47-[BTMLoginItemController _notifyDidChangeItems]_block_invoke.cold.2
+ __50-[BTMAgentConnection getBackgroundItemsWithReply:]_block_invoke.9.cold.2
+ __50-[BTMAgentConnection getBackgroundItemsWithReply:]_block_invoke.cold.2
+ __50-[BTMManager dumpDatabaseWithAuthorization:error:]_block_invoke.cold.2
+ __51-[BTMAgentConnection setUserElection:forURL:reply:]_block_invoke.cold.2
+ __51-[BTMBackgroundItemController fetchBackgroundTasks]_block_invoke.cold.2
+ __51-[BTMManager eraseDatabaseWithAuthorization:error:]_block_invoke.cold.2
+ __52-[BTMBackgroundItemController _notifyDidChangeItems]_block_invoke.cold.2
+ __54-[BTMAgentConnection getLoginItemsWithTypeMask:reply:]_block_invoke.5.cold.2
+ __54-[BTMAgentConnection getLoginItemsWithTypeMask:reply:]_block_invoke.cold.2
+ __57-[BTMBackgroundTaskManager openLoginItemsWithCompletion:]_block_invoke.cold.2
+ __57-[BTMItem setExecutablePathFromLauncherTargetWithConfig:]_block_invoke.cold.2
+ __57-[BTMManager setMDMPayload:identifier:updateImmediately:]_block_invoke.148.cold.2
+ __57-[BTMManager setMDMPayload:identifier:updateImmediately:]_block_invoke.cold.2
+ __58-[BTMManager addSFLItemWithURL:type:global:managed:error:]_block_invoke.125.cold.2
+ __58-[BTMManager addSFLItemWithURL:type:global:managed:error:]_block_invoke.125.cold.3
+ __58-[BTMManager addSFLItemWithURL:type:global:managed:error:]_block_invoke.cold.2
+ __59-[BTMAgentConnection importSFLLoginItemsAndDeleteWhenDone:]_block_invoke.15.cold.2
+ __59-[BTMAgentConnection importSFLLoginItemsAndDeleteWhenDone:]_block_invoke.cold.2
+ __62-[BTMAgentConnection setUserElection:forBackgroundItem:reply:]_block_invoke.cold.2
+ __63-[BTMManager unregisterItemWithBundleURL:type:relativeURL:uid:]_block_invoke.cold.2
+ __64-[BTMManager unregisterItemWithAuditToken:type:relativeURL:uid:]_block_invoke.cold.2
+ __65-[BTMBackgroundItemController setUserElection:forURL:completion:]_block_invoke.cold.2
+ __69-[BTMManager fetchItemWithAppURL:type:relativeURL:configuration:uid:]_block_invoke.cold.2
+ __69-[BTMManager unregisterLaunchItemWithBundleURL:type:relativeURL:uid:]_block_invoke.65.cold.2
+ __69-[BTMManager unregisterLaunchItemWithBundleURL:type:relativeURL:uid:]_block_invoke.cold.2
+ __70-[BTMManager unregisterLaunchItemWithAuditToken:type:relativeURL:uid:]_block_invoke.68.cold.2
+ __70-[BTMManager unregisterLaunchItemWithAuditToken:type:relativeURL:uid:]_block_invoke.cold.2
+ __71-[BTMRegistrar fetchItemWithAppURL:type:relativeURL:configuration:uid:]_block_invoke.cold.2
+ __76-[BTMBackgroundItemController setUserElection:forBackgroundItem:completion:]_block_invoke.cold.2
+ __76-[BTMManager registerItem:withBundleURL:type:relativeURL:configuration:uid:]_block_invoke.cold.2
+ __77-[BTMManager registerItem:withAuditToken:type:relativeURL:configuration:uid:]_block_invoke.cold.2
+ __78-[BTMRegistrar registerItem:withBundleURL:type:relativeURL:configuration:uid:]_block_invoke.cold.2
+ __79-[BTMManager getItemDisposition:withAppURL:type:relativeURL:configuration:uid:]_block_invoke.cold.2
+ __79-[BTMManager invalidateLaunchItemWithBundleURL:type:itemURL:configuration:uid:]_block_invoke.cold.2
+ __81-[BTMManager registerLaunchItemWithBundleURL:type:relativeURL:configuration:uid:]_block_invoke.57.cold.2
+ __81-[BTMManager registerLaunchItemWithBundleURL:type:relativeURL:configuration:uid:]_block_invoke.cold.2
+ __82-[BTMManager registerLaunchItemWithAuditToken:type:relativeURL:configuration:uid:]_block_invoke.62.cold.2
+ __82-[BTMManager registerLaunchItemWithAuditToken:type:relativeURL:configuration:uid:]_block_invoke.cold.2
+ __90-[BTMManager _canLaunchItemWithAppURL:type:relativeURL:configuration:uid:canLaunch:error:]_block_invoke.cold.2
+ __91-[BTMManager getEffectiveDisposition:andLWCR:forAppURL:type:relativeURL:configuration:uid:]_block_invoke.cold.2
+ __93-[BTMRegistrar getEffectiveDisposition:andLWCR:forAppURL:type:relativeURL:configuration:uid:]_block_invoke.cold.2
+ __96-[BTMManager getEffectiveDisposition:andLWCR:withAuditToken:type:relativeURL:configuration:uid:]_block_invoke.cold.2
+ __BTMGetEnablementStatusForSubsystemAndUID_block_invoke.cold.2
+ __BTMHaveEnablementStatusForSubsystemAndUID_block_invoke.cold.2
+ __BTMResetEnablementStatusForSubsystemAndUID_block_invoke.301.cold.2
+ __BTMResetEnablementStatusForSubsystemAndUID_block_invoke.cold.2
+ __BTMSetEnablementStatusForSubsystemAndUID_block_invoke.cold.2
+ __RegisterParentApps_block_invoke.cold.2
- _OUTLINED_FUNCTION_13

```
