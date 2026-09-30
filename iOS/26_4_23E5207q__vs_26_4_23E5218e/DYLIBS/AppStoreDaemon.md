## AppStoreDaemon

> `/System/Library/PrivateFrameworks/AppStoreDaemon.framework/AppStoreDaemon`

```diff

-12.4.20.2.1
-  __TEXT.__text: 0x88a70
+12.4.22.0.0
+  __TEXT.__text: 0x89354
   __TEXT.__auth_stubs: 0xba0
-  __TEXT.__objc_methlist: 0xaed4
-  __TEXT.__const: 0x390
-  __TEXT.__dlopen_cstrs: 0xb1
-  __TEXT.__cstring: 0x5614
+  __TEXT.__objc_methlist: 0xb00c
+  __TEXT.__const: 0x398
+  __TEXT.__dlopen_cstrs: 0x5b
+  __TEXT.__cstring: 0x5856
   __TEXT.__constg_swiftt: 0x7c
   __TEXT.__swift5_typeref: 0x59
   __TEXT.__swift5_builtin: 0x28

   __TEXT.__swift5_fieldmd: 0x44
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__oslogstring: 0x4d6c
-  __TEXT.__gcc_except_tab: 0x1080
-  __TEXT.__unwind_info: 0x2900
-  __TEXT.__objc_classname: 0x18df
-  __TEXT.__objc_methname: 0x14ac8
-  __TEXT.__objc_methtype: 0x352e
-  __TEXT.__objc_stubs: 0x8920
-  __DATA_CONST.__got: 0x640
-  __DATA_CONST.__const: 0x27f8
-  __DATA_CONST.__objc_classlist: 0x5f0
+  __TEXT.__gcc_except_tab: 0x1028
+  __TEXT.__unwind_info: 0x2910
+  __TEXT.__objc_classname: 0x18ec
+  __TEXT.__objc_methname: 0x14e14
+  __TEXT.__objc_methtype: 0x3548
+  __TEXT.__objc_stubs: 0x8ae0
+  __DATA_CONST.__got: 0x650
+  __DATA_CONST.__const: 0x27e0
+  __DATA_CONST.__objc_classlist: 0x5f8
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x210
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x44f0
+  __DATA_CONST.__objc_selrefs: 0x4590
   __DATA_CONST.__objc_protorefs: 0x158
   __DATA_CONST.__objc_superrefs: 0x4a0
   __DATA_CONST.__objc_arraydata: 0xc8
   __AUTH_CONST.__auth_got: 0x5e0
-  __AUTH_CONST.__const: 0x8c0
-  __AUTH_CONST.__cfstring: 0x6b40
-  __AUTH_CONST.__objc_const: 0x15d18
+  __AUTH_CONST.__const: 0x900
+  __AUTH_CONST.__cfstring: 0x6d40
+  __AUTH_CONST.__objc_const: 0x15ed8
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0x1720
-  __DATA.__objc_ivar: 0xd84
+  __AUTH.__objc_data: 0x1770
+  __DATA.__objc_ivar: 0xd90
   __DATA.__data: 0x18f8
   __DATA.__bss: 0x310
-  __DATA_DIRTY.__objc_ivar: 0x194
+  __DATA_DIRTY.__objc_ivar: 0x1a0
   __DATA_DIRTY.__objc_data: 0x2440
   __DATA_DIRTY.__data: 0x50
-  __DATA_DIRTY.__bss: 0x2a0
+  __DATA_DIRTY.__bss: 0x290
   __DATA_DIRTY.__common: 0x168
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/InstalledContentLibrary.framework/InstalledContentLibrary
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MobileInstallation.framework/MobileInstallation
+  - /System/Library/PrivateFrameworks/PairedDeviceRegistry.framework/PairedDeviceRegistry
   - /System/Library/PrivateFrameworks/PlugInKit.framework/PlugInKit
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: FC017554-DB92-3310-A47B-66BA20083BD7
-  Functions: 4387
-  Symbols:   13390
-  CStrings:  6468
+  UUID: 11513A40-A70F-3844-A93D-CD1B5DADFB97
+  Functions: 4411
+  Symbols:   13462
+  CStrings:  6529
 
Symbols:
+ +[ASDAnalytics getClientIdentifier]
+ +[ASDAnalytics reportDeprecatedAPIToInstallationService:]
+ +[ASDAnalytics reportDeprecatedAPIToLibraryService:]
+ +[ASDAppLibrary launchApp:onDeviceWithPairingID:]
+ +[ASDAppLibrary launchApp:onDeviceWithPairingID:withResultHandler:]
+ +[ASDAppQuery queryForBetaAppsOnDeviceWithPairingID:]
+ +[ASDAppQuery queryForSystemAppsOnDeviceWithPairingID:]
+ +[ASDAppQuery queryWithPredicate:onDeviceWithPairingID:]
+ +[ASDAppQueryExecutor _executeQueryWithPredicate:isForUpdates:reloadingFromServer:onDeviceWithPairingID:remoteDeviceID:usingServiceBroker:withResultHandler:]
+ +[ASDInstallApps _installApps:onDeviceWithPairingID:withCompletionHandler:]
+ +[ASDInstallApps installApp:onDeviceWithPairingID:withCompletionHandler:]
+ +[ASDInstallApps installApps:onDeviceWithPairingID:withCompletionHandler:]
+ -[ASDAppQuery _executeQueryWithPredicate:onDeviceWithPairingID:withCompletion:]
+ -[ASDAppQuery initWithPredicate:onDeviceWithPairingID:]
+ -[ASDAppQueryExecutor executeQueryWithPredicate:onDeviceWithPairingID:remoteDeviceID:withResultHandler:]
+ -[ASDAppQueryExecutor executeUpdatesQueryWithPredicateReloadingFromServer:onDeviceWithPairingID:remoteDeviceID:withResultHandler:]
+ -[ASDSystemAppMetadata isOneShot]
+ -[ASDSystemAppMetadata isUserWaiting]
+ -[ASDSystemAppMetadata setOneShot:]
+ -[ASDSystemAppMetadata setSuppressDialogs:]
+ -[ASDSystemAppMetadata setUserWaiting:]
+ -[ASDSystemAppMetadata suppressDialogs]
+ -[ASDSystemAppRequest isOneShot]
+ -[ASDSystemAppRequest isUserWaiting]
+ -[ASDSystemAppRequest setOneShot:]
+ -[ASDSystemAppRequest setSuppressDialogs:]
+ -[ASDSystemAppRequest setUserWaiting:]
+ -[ASDSystemAppRequest suppressDialogs]
+ GCC_except_table23
+ GCC_except_table51
+ _OBJC_CLASS_$_ASDAnalytics
+ _OBJC_CLASS_$_NSProcessInfo
+ _OBJC_CLASS_$_PDRRegistry
+ _OBJC_IVAR_$_ASDAppQuery._pairingID
+ _OBJC_IVAR_$_ASDSystemAppMetadata._oneShot
+ _OBJC_IVAR_$_ASDSystemAppMetadata._suppressDialogs
+ _OBJC_IVAR_$_ASDSystemAppMetadata._userWaiting
+ _OBJC_METACLASS_$_ASDAnalytics
+ __OBJC_$_CLASS_METHODS_ASDAnalytics
+ __OBJC_CLASS_RO_$_ASDAnalytics
+ __OBJC_METACLASS_RO_$_ASDAnalytics
+ ___104-[ASDAppQueryExecutor executeQueryWithPredicate:onDeviceWithPairingID:remoteDeviceID:withResultHandler:]_block_invoke
+ ___104-[ASDAppQueryExecutor executeQueryWithPredicate:onDeviceWithPairingID:remoteDeviceID:withResultHandler:]_block_invoke.3
+ ___104-[ASDAppQueryExecutor executeQueryWithPredicate:onDeviceWithPairingID:remoteDeviceID:withResultHandler:]_block_invoke.6
+ ___104-[ASDAppQueryExecutor executeQueryWithPredicate:onDeviceWithPairingID:remoteDeviceID:withResultHandler:]_block_invoke.8
+ ___130-[ASDAppQueryExecutor executeUpdatesQueryWithPredicateReloadingFromServer:onDeviceWithPairingID:remoteDeviceID:withResultHandler:]_block_invoke
+ ___130-[ASDAppQueryExecutor executeUpdatesQueryWithPredicateReloadingFromServer:onDeviceWithPairingID:remoteDeviceID:withResultHandler:]_block_invoke.14
+ ___130-[ASDAppQueryExecutor executeUpdatesQueryWithPredicateReloadingFromServer:onDeviceWithPairingID:remoteDeviceID:withResultHandler:]_block_invoke.15
+ ___130-[ASDAppQueryExecutor executeUpdatesQueryWithPredicateReloadingFromServer:onDeviceWithPairingID:remoteDeviceID:withResultHandler:]_block_invoke.16
+ ___157+[ASDAppQueryExecutor _executeQueryWithPredicate:isForUpdates:reloadingFromServer:onDeviceWithPairingID:remoteDeviceID:usingServiceBroker:withResultHandler:]_block_invoke
+ ___157+[ASDAppQueryExecutor _executeQueryWithPredicate:isForUpdates:reloadingFromServer:onDeviceWithPairingID:remoteDeviceID:usingServiceBroker:withResultHandler:]_block_invoke.17
+ ___157+[ASDAppQueryExecutor _executeQueryWithPredicate:isForUpdates:reloadingFromServer:onDeviceWithPairingID:remoteDeviceID:usingServiceBroker:withResultHandler:]_block_invoke_2
+ ___157+[ASDAppQueryExecutor _executeQueryWithPredicate:isForUpdates:reloadingFromServer:onDeviceWithPairingID:remoteDeviceID:usingServiceBroker:withResultHandler:]_block_invoke_2.18
+ ___157+[ASDAppQueryExecutor _executeQueryWithPredicate:isForUpdates:reloadingFromServer:onDeviceWithPairingID:remoteDeviceID:usingServiceBroker:withResultHandler:]_block_invoke_3
+ ___157+[ASDAppQueryExecutor _executeQueryWithPredicate:isForUpdates:reloadingFromServer:onDeviceWithPairingID:remoteDeviceID:usingServiceBroker:withResultHandler:]_block_invoke_3.19
+ ___157+[ASDAppQueryExecutor _executeQueryWithPredicate:isForUpdates:reloadingFromServer:onDeviceWithPairingID:remoteDeviceID:usingServiceBroker:withResultHandler:]_block_invoke_4
+ ___157+[ASDAppQueryExecutor _executeQueryWithPredicate:isForUpdates:reloadingFromServer:onDeviceWithPairingID:remoteDeviceID:usingServiceBroker:withResultHandler:]_block_invoke_5
+ ___157+[ASDAppQueryExecutor _executeQueryWithPredicate:isForUpdates:reloadingFromServer:onDeviceWithPairingID:remoteDeviceID:usingServiceBroker:withResultHandler:]_block_invoke_6
+ ___34-[ASDAppQuery _handlePauseForApp:]_block_invoke.80
+ ___35-[ASDAppQuery _handleResumeForApp:]_block_invoke.82
+ ___45+[ASDAppLibrary launchApp:withResultHandler:]_block_invoke.6
+ ___45+[ASDAppLibrary launchApp:withResultHandler:]_block_invoke.7
+ ___45-[ASDAppQuery executeQueryWithResultHandler:]_block_invoke.68
+ ___45-[ASDAppQuery executeQueryWithResultHandler:]_block_invoke_2.69
+ ___49+[ASDAppLibrary launchApp:onDeviceWithPairingID:]_block_invoke
+ ___49+[ASDAppLibrary launchApp:onDeviceWithPairingID:]_block_invoke_2
+ ___50-[ASDAppQuery _handleCancelForApp:reportRemotely:]_block_invoke.84
+ ___50-[ASDAppQuery _handleCancelForApp:reportRemotely:]_block_invoke.85
+ ___50-[ASDAppQuery _handleCancelForApp:reportRemotely:]_block_invoke.86
+ ___52+[ASDAnalytics reportDeprecatedAPIToLibraryService:]_block_invoke
+ ___56-[ASDAppQuery notificationCenter:receivedNotifications:]_block_invoke.70
+ ___57+[ASDAnalytics reportDeprecatedAPIToInstallationService:]_block_invoke
+ ___65+[ASDAppLibrary launchMessagesExtensionForApp:withResultHandler:]_block_invoke.14
+ ___65+[ASDAppLibrary launchMessagesExtensionForApp:withResultHandler:]_block_invoke.15
+ ___67+[ASDAppLibrary launchApp:onDeviceWithPairingID:withResultHandler:]_block_invoke
+ ___67+[ASDAppLibrary launchApp:onDeviceWithPairingID:withResultHandler:]_block_invoke.12
+ ___67+[ASDAppLibrary launchApp:onDeviceWithPairingID:withResultHandler:]_block_invoke.13
+ ___67+[ASDAppLibrary launchApp:onDeviceWithPairingID:withResultHandler:]_block_invoke_2
+ ___72+[ASDAppLibrary uninstallApp:requestUserConfirmation:withResultHandler:]_block_invoke.26
+ ___72+[ASDAppLibrary uninstallApp:requestUserConfirmation:withResultHandler:]_block_invoke.27
+ ___73+[ASDInstallApps installApp:onDeviceWithPairingID:withCompletionHandler:]_block_invoke
+ ___75+[ASDInstallApps _installApps:onDeviceWithPairingID:withCompletionHandler:]_block_invoke
+ ___75+[ASDInstallApps _installApps:onDeviceWithPairingID:withCompletionHandler:]_block_invoke.104
+ ___75+[ASDInstallApps _installApps:onDeviceWithPairingID:withCompletionHandler:]_block_invoke.96
+ ___75+[ASDInstallApps _installApps:onDeviceWithPairingID:withCompletionHandler:]_block_invoke_2
+ ___75+[ASDInstallApps _installApps:onDeviceWithPairingID:withCompletionHandler:]_block_invoke_3
+ ___75+[ASDInstallApps _installApps:onDeviceWithPairingID:withCompletionHandler:]_block_invoke_4
+ ___75+[ASDInstallApps _installApps:onDeviceWithPairingID:withCompletionHandler:]_block_invoke_5
+ ___75+[ASDInstallApps _installApps:onDeviceWithPairingID:withCompletionHandler:]_block_invoke_6
+ ___79-[ASDAppQuery _executeQueryWithPredicate:onDeviceWithPairingID:withCompletion:]_block_invoke
+ ___79-[ASDAppQuery _executeQueryWithPredicate:onDeviceWithPairingID:withCompletion:]_block_invoke.77
+ ___84+[ASDAppLibrary lookupBundleIDsForDeletableSystemAppsWithItemIDs:withResultHandler:]_block_invoke.16
+ ___84+[ASDAppLibrary lookupBundleIDsForDeletableSystemAppsWithItemIDs:withResultHandler:]_block_invoke.17
+ ___84+[ASDAppLibrary lookupItemIDsForDeletableSystemAppsWithBundleIDs:withResultHandler:]_block_invoke.19
+ ___84+[ASDAppLibrary lookupItemIDsForDeletableSystemAppsWithBundleIDs:withResultHandler:]_block_invoke.20
+ ___92+[ASDAppLibrary lookupBundleIDsForDeletableSystemAppsForWatchWithItemIDs:withResultHandler:]_block_invoke.21
+ ___92+[ASDAppLibrary lookupBundleIDsForDeletableSystemAppsForWatchWithItemIDs:withResultHandler:]_block_invoke.22
+ ___92+[ASDAppLibrary lookupItemIDsForDeletableSystemAppsForWatchWithBundleIDs:withResultHandler:]_block_invoke.23
+ ___92+[ASDAppLibrary lookupItemIDsForDeletableSystemAppsForWatchWithBundleIDs:withResultHandler:]_block_invoke.24
+ ___block_literal_global.15
+ _objc_msgSend$executeQueryWithPredicate:onDeviceWithPairingID:remoteDeviceID:withResultHandler:
+ _objc_msgSend$executeUpdatesQueryWithPredicateReloadingFromServer:onDeviceWithPairingID:remoteDeviceID:withResultHandler:
+ _objc_msgSend$getActivePairedDeviceExcludingAltAccount
+ _objc_msgSend$getClientIdentifier
+ _objc_msgSend$initWithPredicate:onDeviceWithPairingID:
+ _objc_msgSend$installApps:onDeviceWithPairingID:withCompletionHandler:
+ _objc_msgSend$launchApp:onDeviceWithPairingID:
+ _objc_msgSend$launchApp:onDeviceWithPairingID:withResultHandler:
+ _objc_msgSend$mainBundle
+ _objc_msgSend$processInfo
+ _objc_msgSend$processName
+ _objc_msgSend$queryForBetaAppsOnDeviceWithPairingID:
+ _objc_msgSend$queryWithPredicate:onDeviceWithPairingID:
+ _objc_msgSend$reportDeprecatedAPIToInstallationService:
+ _objc_msgSend$reportDeprecatedAPIToLibraryService:
+ _objc_msgSend$sendAnalyticsEventWithDictionary:topic:
+ _objc_msgSend$setOneShot:
+ _objc_msgSend$setSuppressDialogs:
+ _objc_msgSend$setUserWaiting:
- +[ASDAppQueryExecutor _executeQueryWithPredicate:isForUpdates:reloadingFromServer:onPairedDevice:remoteDeviceID:usingServiceBroker:withResultHandler:]
- +[ASDInstallApps _installApps:onPairedDevice:withCompletionHandler:]
- -[ASDAppQuery _executeQueryWithPredicate:onPairedDevice:withCompletion:]
- -[ASDAppQueryExecutor executeQueryWithPredicate:onPairedDevice:remoteDeviceID:withResultHandler:]
- -[ASDAppQueryExecutor executeUpdatesQueryWithPredicateReloadingFromServer:onPairedDevice:remoteDeviceID:withResultHandler:]
- GCC_except_table49
- _OBJC_IVAR_$_ASDAppQuery._device
- ___123-[ASDAppQueryExecutor executeUpdatesQueryWithPredicateReloadingFromServer:onPairedDevice:remoteDeviceID:withResultHandler:]_block_invoke
- ___123-[ASDAppQueryExecutor executeUpdatesQueryWithPredicateReloadingFromServer:onPairedDevice:remoteDeviceID:withResultHandler:]_block_invoke.14
- ___123-[ASDAppQueryExecutor executeUpdatesQueryWithPredicateReloadingFromServer:onPairedDevice:remoteDeviceID:withResultHandler:]_block_invoke.15
- ___123-[ASDAppQueryExecutor executeUpdatesQueryWithPredicateReloadingFromServer:onPairedDevice:remoteDeviceID:withResultHandler:]_block_invoke.16
- ___150+[ASDAppQueryExecutor _executeQueryWithPredicate:isForUpdates:reloadingFromServer:onPairedDevice:remoteDeviceID:usingServiceBroker:withResultHandler:]_block_invoke
- ___150+[ASDAppQueryExecutor _executeQueryWithPredicate:isForUpdates:reloadingFromServer:onPairedDevice:remoteDeviceID:usingServiceBroker:withResultHandler:]_block_invoke.17
- ___150+[ASDAppQueryExecutor _executeQueryWithPredicate:isForUpdates:reloadingFromServer:onPairedDevice:remoteDeviceID:usingServiceBroker:withResultHandler:]_block_invoke_2
- ___150+[ASDAppQueryExecutor _executeQueryWithPredicate:isForUpdates:reloadingFromServer:onPairedDevice:remoteDeviceID:usingServiceBroker:withResultHandler:]_block_invoke_2.18
- ___150+[ASDAppQueryExecutor _executeQueryWithPredicate:isForUpdates:reloadingFromServer:onPairedDevice:remoteDeviceID:usingServiceBroker:withResultHandler:]_block_invoke_3
- ___150+[ASDAppQueryExecutor _executeQueryWithPredicate:isForUpdates:reloadingFromServer:onPairedDevice:remoteDeviceID:usingServiceBroker:withResultHandler:]_block_invoke_3.19
- ___150+[ASDAppQueryExecutor _executeQueryWithPredicate:isForUpdates:reloadingFromServer:onPairedDevice:remoteDeviceID:usingServiceBroker:withResultHandler:]_block_invoke_4
- ___150+[ASDAppQueryExecutor _executeQueryWithPredicate:isForUpdates:reloadingFromServer:onPairedDevice:remoteDeviceID:usingServiceBroker:withResultHandler:]_block_invoke_5
- ___150+[ASDAppQueryExecutor _executeQueryWithPredicate:isForUpdates:reloadingFromServer:onPairedDevice:remoteDeviceID:usingServiceBroker:withResultHandler:]_block_invoke_6
- ___34-[ASDAppQuery _handlePauseForApp:]_block_invoke.64
- ___35-[ASDAppQuery _handleResumeForApp:]_block_invoke.66
- ___42+[ASDAppLibrary launchApp:onPairedDevice:]_block_invoke
- ___42+[ASDAppLibrary launchApp:onPairedDevice:]_block_invoke_2
- ___45+[ASDAppLibrary launchApp:withResultHandler:]_block_invoke.4
- ___45+[ASDAppLibrary launchApp:withResultHandler:]_block_invoke.5
- ___45-[ASDAppQuery executeQueryWithResultHandler:]_block_invoke.52
- ___45-[ASDAppQuery executeQueryWithResultHandler:]_block_invoke_2.53
- ___50-[ASDAppQuery _handleCancelForApp:reportRemotely:]_block_invoke.67
- ___50-[ASDAppQuery _handleCancelForApp:reportRemotely:]_block_invoke.68
- ___50-[ASDAppQuery _handleCancelForApp:reportRemotely:]_block_invoke.69
- ___56-[ASDAppQuery notificationCenter:receivedNotifications:]_block_invoke.54
- ___60+[ASDAppLibrary launchApp:onPairedDevice:withResultHandler:]_block_invoke
- ___60+[ASDAppLibrary launchApp:onPairedDevice:withResultHandler:]_block_invoke.7
- ___60+[ASDAppLibrary launchApp:onPairedDevice:withResultHandler:]_block_invoke.8
- ___60+[ASDAppLibrary launchApp:onPairedDevice:withResultHandler:]_block_invoke_2
- ___65+[ASDAppLibrary launchMessagesExtensionForApp:withResultHandler:]_block_invoke.10
- ___65+[ASDAppLibrary launchMessagesExtensionForApp:withResultHandler:]_block_invoke.9
- ___68+[ASDInstallApps _installApps:onPairedDevice:withCompletionHandler:]_block_invoke
- ___68+[ASDInstallApps _installApps:onPairedDevice:withCompletionHandler:]_block_invoke.86
- ___68+[ASDInstallApps _installApps:onPairedDevice:withCompletionHandler:]_block_invoke.94
- ___68+[ASDInstallApps _installApps:onPairedDevice:withCompletionHandler:]_block_invoke_2
- ___68+[ASDInstallApps _installApps:onPairedDevice:withCompletionHandler:]_block_invoke_3
- ___68+[ASDInstallApps _installApps:onPairedDevice:withCompletionHandler:]_block_invoke_4
- ___68+[ASDInstallApps _installApps:onPairedDevice:withCompletionHandler:]_block_invoke_5
- ___68+[ASDInstallApps _installApps:onPairedDevice:withCompletionHandler:]_block_invoke_6
- ___72+[ASDAppLibrary uninstallApp:requestUserConfirmation:withResultHandler:]_block_invoke.21
- ___72+[ASDAppLibrary uninstallApp:requestUserConfirmation:withResultHandler:]_block_invoke.22
- ___72-[ASDAppQuery _executeQueryWithPredicate:onPairedDevice:withCompletion:]_block_invoke
- ___72-[ASDAppQuery _executeQueryWithPredicate:onPairedDevice:withCompletion:]_block_invoke.61
- ___84+[ASDAppLibrary lookupBundleIDsForDeletableSystemAppsWithItemIDs:withResultHandler:]_block_invoke.11
- ___84+[ASDAppLibrary lookupBundleIDsForDeletableSystemAppsWithItemIDs:withResultHandler:]_block_invoke.12
- ___84+[ASDAppLibrary lookupItemIDsForDeletableSystemAppsWithBundleIDs:withResultHandler:]_block_invoke.14
- ___84+[ASDAppLibrary lookupItemIDsForDeletableSystemAppsWithBundleIDs:withResultHandler:]_block_invoke.15
- ___92+[ASDAppLibrary lookupBundleIDsForDeletableSystemAppsForWatchWithItemIDs:withResultHandler:]_block_invoke.16
- ___92+[ASDAppLibrary lookupBundleIDsForDeletableSystemAppsForWatchWithItemIDs:withResultHandler:]_block_invoke.17
- ___92+[ASDAppLibrary lookupItemIDsForDeletableSystemAppsForWatchWithBundleIDs:withResultHandler:]_block_invoke.18
- ___92+[ASDAppLibrary lookupItemIDsForDeletableSystemAppsForWatchWithBundleIDs:withResultHandler:]_block_invoke.19
- ___97-[ASDAppQueryExecutor executeQueryWithPredicate:onPairedDevice:remoteDeviceID:withResultHandler:]_block_invoke
- ___97-[ASDAppQueryExecutor executeQueryWithPredicate:onPairedDevice:remoteDeviceID:withResultHandler:]_block_invoke.3
- ___97-[ASDAppQueryExecutor executeQueryWithPredicate:onPairedDevice:remoteDeviceID:withResultHandler:]_block_invoke.6
- ___97-[ASDAppQueryExecutor executeQueryWithPredicate:onPairedDevice:remoteDeviceID:withResultHandler:]_block_invoke.8
- ___NanoRegistryLibraryCore_block_invoke
- ___getNRPairedDeviceRegistryClass_block_invoke
- _audit_stringNanoRegistry
- _objc_msgSend$executeQueryWithPredicate:onPairedDevice:remoteDeviceID:withResultHandler:
- _objc_msgSend$executeUpdatesQueryWithPredicateReloadingFromServer:onPairedDevice:remoteDeviceID:withResultHandler:
- _objc_msgSend$getActivePairedDevice
- _objc_msgSend$initWithPredicate:onPairedDevice:
- _objc_msgSend$installApps:onPairedDevice:withCompletionHandler:
CStrings:
+ "%@ {bundleID = %@, oneShot= %@, suppressDialogs = %@, userInitiated = %@, userWaiting = %@%@}"
+ "(unknown)"
+ "+[ASDAppLibrary launchApp:onPairedDevice:]"
+ "+[ASDAppLibrary launchApp:onPairedDevice:withResultHandler:]"
+ "+[ASDAppQuery queryDefaultPairedWatchForBetaApps:]"
+ "+[ASDAppQuery queryForBetaAppsOnPairedDevice:]"
+ "+[ASDAppQuery queryForSystemAppsOnPairedDevice:]"
+ "+[ASDAppQuery queryWithPredicate:onPairedDevice:]"
+ "+[ASDInstallApps installApp:onPairedDevice:withCompletionHandler:]"
+ "+[ASDInstallApps installApps:onPairedDevice:withCompletionHandler:]"
+ "-[ASDAppQuery initWithPredicate:onPairedDevice:]"
+ "ASDAnalytics"
+ "Caller"
+ "OS"
+ "SD"
+ "SI"
+ "Symbol"
+ "TB,GisOneShot,V_oneShot"
+ "TB,GisUserWaiting,V_userWaiting"
+ "TB,N,GisOneShot,V_oneShot"
+ "TB,N,GisUserWaiting,V_userWaiting"
+ "TB,N,V_suppressDialogs"
+ "UW"
+ "Unimplemented at /Library/Caches/com.apple.xbs/CD4C037E-4AB3-49D8-A294-9FAB7C95D8E1/TemporaryDirectory.cxXf35/Sources/AppStoreDaemonFramework/Libraries/AppStoreDaemon/XPC/Updates/ASDSoftwareUpdatesStore.m:384 : Not supported on iOS"
+ "Unimplemented at /Library/Caches/com.apple.xbs/CD4C037E-4AB3-49D8-A294-9FAB7C95D8E1/TemporaryDirectory.cxXf35/Sources/AppStoreDaemonFramework/Libraries/AppStoreDaemon/XPC/Updates/ASDSoftwareUpdatesStore.m:81 : Not supported on iOS"
+ "Unimplemented at /Library/Caches/com.apple.xbs/CD4C037E-4AB3-49D8-A294-9FAB7C95D8E1/TemporaryDirectory.cxXf35/Sources/AppStoreDaemonFramework/Libraries/AppStoreDaemon/XPC/Updates/ASDSoftwareUpdatesStore.m:85 : Not supported on iOS"
+ "Unimplemented at /Library/Caches/com.apple.xbs/CD4C037E-4AB3-49D8-A294-9FAB7C95D8E1/TemporaryDirectory.cxXf35/Sources/AppStoreDaemonFramework/Libraries/AppStoreDaemon/XPC/Updates/ASDSoftwareUpdatesStore.m:90 : Not supported on iOS"
+ "_oneShot"
+ "_pairingID"
+ "_suppressDialogs"
+ "_userWaiting"
+ "com.apple.appstored.deprecatedAPITracker"
+ "executeQueryWithPredicate:onDeviceWithPairingID:remoteDeviceID:withResultHandler:"
+ "executeUpdatesQueryWithPredicateReloadingFromServer:onDeviceWithPairingID:remoteDeviceID:withResultHandler:"
+ "getActivePairedDeviceExcludingAltAccount"
+ "getClientIdentifier"
+ "initWithPredicate:onDeviceWithPairingID:"
+ "installApp:onDeviceWithPairingID:withCompletionHandler:"
+ "installApps:onDeviceWithPairingID:withCompletionHandler:"
+ "isOneShot"
+ "isUserWaiting"
+ "launchApp:onDeviceWithPairingID:"
+ "launchApp:onDeviceWithPairingID:withResultHandler:"
+ "mainBundle"
+ "oneShot"
+ "processInfo"
+ "queryForBetaAppsOnDeviceWithPairingID:"
+ "queryForSystemAppsOnDeviceWithPairingID:"
+ "queryWithPredicate:onDeviceWithPairingID:"
+ "reportDeprecatedAPIToInstallationService:"
+ "reportDeprecatedAPIToLibraryService:"
+ "sendAnalyticsEventWithDictionary:topic:"
+ "setOneShot:"
+ "setSuppressDialogs:"
+ "setUserWaiting:"
+ "suppressDialogs"
+ "userWaiting"
+ "v32@0:8@\"NSDictionary\"16@\"NSString\"24"
- "%@ {bundleID = %@, userInitiated = %@%@}"
- "@\"NRDevice\""
- "NRPairedDeviceRegistry"
- "Unimplemented at /Library/Caches/com.apple.xbs/D25EB013-D769-40DC-A731-1A4595ECE85E/TemporaryDirectory.WeFgR0/Sources/AppStoreDaemonFramework/Libraries/AppStoreDaemon/XPC/Updates/ASDSoftwareUpdatesStore.m:384 : Not supported on iOS"
- "Unimplemented at /Library/Caches/com.apple.xbs/D25EB013-D769-40DC-A731-1A4595ECE85E/TemporaryDirectory.WeFgR0/Sources/AppStoreDaemonFramework/Libraries/AppStoreDaemon/XPC/Updates/ASDSoftwareUpdatesStore.m:81 : Not supported on iOS"
- "Unimplemented at /Library/Caches/com.apple.xbs/D25EB013-D769-40DC-A731-1A4595ECE85E/TemporaryDirectory.WeFgR0/Sources/AppStoreDaemonFramework/Libraries/AppStoreDaemon/XPC/Updates/ASDSoftwareUpdatesStore.m:85 : Not supported on iOS"
- "Unimplemented at /Library/Caches/com.apple.xbs/D25EB013-D769-40DC-A731-1A4595ECE85E/TemporaryDirectory.WeFgR0/Sources/AppStoreDaemonFramework/Libraries/AppStoreDaemon/XPC/Updates/ASDSoftwareUpdatesStore.m:90 : Not supported on iOS"
- "_device"
- "executeQueryWithPredicate:onPairedDevice:remoteDeviceID:withResultHandler:"
- "executeUpdatesQueryWithPredicateReloadingFromServer:onPairedDevice:remoteDeviceID:withResultHandler:"
- "getActivePairedDevice"
- "softlink:r:path:/System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry"

```
