## AppStoreDaemon

> `/System/Library/PrivateFrameworks/AppStoreDaemon.framework/AppStoreDaemon`

```diff

-12.3.3.0.0
-  __TEXT.__text: 0x839fc
-  __TEXT.__auth_stubs: 0xc00
-  __TEXT.__objc_methlist: 0xacec
-  __TEXT.__const: 0x360
+12.4.20.2.1
+  __TEXT.__text: 0x88a70
+  __TEXT.__auth_stubs: 0xba0
+  __TEXT.__objc_methlist: 0xaed4
+  __TEXT.__const: 0x390
   __TEXT.__dlopen_cstrs: 0xb1
-  __TEXT.__cstring: 0x53fa
+  __TEXT.__cstring: 0x5614
   __TEXT.__constg_swiftt: 0x7c
   __TEXT.__swift5_typeref: 0x59
   __TEXT.__swift5_builtin: 0x28
-  __TEXT.__swift5_reflstr: 0x64
+  __TEXT.__swift5_reflstr: 0x44
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_proto: 0x18
   __TEXT.__swift5_types: 0xc
-  __TEXT.__swift5_fieldmd: 0x50
+  __TEXT.__swift5_fieldmd: 0x44
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__oslogstring: 0x487a
-  __TEXT.__gcc_except_tab: 0x1048
-  __TEXT.__unwind_info: 0x2770
-  __TEXT.__eh_frame: 0x70
-  __TEXT.__objc_classname: 0x18ac
-  __TEXT.__objc_methname: 0x147f8
-  __TEXT.__objc_methtype: 0x3534
-  __TEXT.__objc_stubs: 0x87c0
-  __DATA_CONST.__got: 0x628
-  __DATA_CONST.__const: 0x2800
-  __DATA_CONST.__objc_classlist: 0x5d8
+  __TEXT.__oslogstring: 0x4d6c
+  __TEXT.__gcc_except_tab: 0x1080
+  __TEXT.__unwind_info: 0x2900
+  __TEXT.__objc_classname: 0x18df
+  __TEXT.__objc_methname: 0x14ac8
+  __TEXT.__objc_methtype: 0x352e
+  __TEXT.__objc_stubs: 0x8920
+  __DATA_CONST.__got: 0x640
+  __DATA_CONST.__const: 0x27f8
+  __DATA_CONST.__objc_classlist: 0x5f0
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x210
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4468
+  __DATA_CONST.__objc_selrefs: 0x44f0
   __DATA_CONST.__objc_protorefs: 0x158
-  __DATA_CONST.__objc_superrefs: 0x488
+  __DATA_CONST.__objc_superrefs: 0x4a0
   __DATA_CONST.__objc_arraydata: 0xc8
-  __AUTH_CONST.__auth_got: 0x610
-  __AUTH_CONST.__const: 0x8a0
-  __AUTH_CONST.__cfstring: 0x6900
-  __AUTH_CONST.__objc_const: 0x15850
+  __AUTH_CONST.__auth_got: 0x5e0
+  __AUTH_CONST.__const: 0x8c0
+  __AUTH_CONST.__cfstring: 0x6b40
+  __AUTH_CONST.__objc_const: 0x15d18
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0x16d0
-  __DATA.__objc_ivar: 0xd44
+  __AUTH.__objc_data: 0x1720
+  __DATA.__objc_ivar: 0xd84
   __DATA.__data: 0x18f8
   __DATA.__bss: 0x310
-  __DATA_DIRTY.__objc_ivar: 0x19c
-  __DATA_DIRTY.__objc_data: 0x23a0
+  __DATA_DIRTY.__objc_ivar: 0x194
+  __DATA_DIRTY.__objc_data: 0x2440
   __DATA_DIRTY.__data: 0x50
-  __DATA_DIRTY.__bss: 0x290
+  __DATA_DIRTY.__bss: 0x2a0
   __DATA_DIRTY.__common: 0x168
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
-  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 111BA31A-5C62-3C9B-B985-E44E18890191
-  Functions: 4372
-  Symbols:   13298
-  CStrings:  6382
+  UUID: FC017554-DB92-3310-A47B-66BA20083BD7
+  Functions: 4387
+  Symbols:   13390
+  CStrings:  6468
 
Symbols:
+ +[ASDAppLedger sharedLedger]
+ +[ASDAppLedgerItem supportsSecureCoding]
+ +[ASDAppLedgerQuery supportsSecureCoding]
+ -[ASDAppLedger initPrivate]
+ -[ASDAppLedger itemsMatchingQuery:completionHandler:]
+ -[ASDAppLedger itemsWithCompletionHandler:]
+ -[ASDAppLedgerItem .cxx_destruct]
+ -[ASDAppLedgerItem bundleID]
+ -[ASDAppLedgerItem bundleVersion]
+ -[ASDAppLedgerItem description]
+ -[ASDAppLedgerItem encodeWithCoder:]
+ -[ASDAppLedgerItem initWithBundleID:bundleVersion:itemID:versionID:installDate:lastLaunchDate:]
+ -[ASDAppLedgerItem initWithCoder:]
+ -[ASDAppLedgerItem installDate]
+ -[ASDAppLedgerItem itemID]
+ -[ASDAppLedgerItem lastLaunchDate]
+ -[ASDAppLedgerItem versionID]
+ -[ASDAppLedgerQuery .cxx_destruct]
+ -[ASDAppLedgerQuery copyWithZone:]
+ -[ASDAppLedgerQuery description]
+ -[ASDAppLedgerQuery encodeWithCoder:]
+ -[ASDAppLedgerQuery genreID]
+ -[ASDAppLedgerQuery genre]
+ -[ASDAppLedgerQuery initWithCoder:]
+ -[ASDAppLedgerQuery init]
+ -[ASDAppLedgerQuery installedSinceDate]
+ -[ASDAppLedgerQuery neverLaunched]
+ -[ASDAppLedgerQuery resultLimit]
+ -[ASDAppLedgerQuery setGenre:]
+ -[ASDAppLedgerQuery setGenreID:]
+ -[ASDAppLedgerQuery setInstalledSinceDate:]
+ -[ASDAppLedgerQuery setNeverLaunched:]
+ -[ASDAppLedgerQuery setResultLimit:]
+ -[ASDAppLedgerQuery setSortOrder:]
+ -[ASDAppLedgerQuery sortOrder]
+ -[ASDAppQuery _newProgressForApp:fromRemoteProgress:]
+ -[ASDAppQuery description]
+ -[ASDAppReviewAppMetadata bundleDirectoryName]
+ -[ASDAppReviewAppMetadata setBundleDirectoryName:]
+ -[ASDTestFlightAppMetadata bundleDirectoryName]
+ -[ASDTestFlightAppMetadata setBundleDirectoryName:]
+ _OBJC_CLASS_$_ASDAppLedger
+ _OBJC_CLASS_$_ASDAppLedgerItem
+ _OBJC_CLASS_$_ASDAppLedgerQuery
+ _OBJC_IVAR_$_ASDAppLedgerItem._bundleID
+ _OBJC_IVAR_$_ASDAppLedgerItem._bundleVersion
+ _OBJC_IVAR_$_ASDAppLedgerItem._installDate
+ _OBJC_IVAR_$_ASDAppLedgerItem._itemID
+ _OBJC_IVAR_$_ASDAppLedgerItem._lastLaunchDate
+ _OBJC_IVAR_$_ASDAppLedgerItem._versionID
+ _OBJC_IVAR_$_ASDAppLedgerQuery._genre
+ _OBJC_IVAR_$_ASDAppLedgerQuery._genreID
+ _OBJC_IVAR_$_ASDAppLedgerQuery._installedSinceDate
+ _OBJC_IVAR_$_ASDAppLedgerQuery._neverLaunched
+ _OBJC_IVAR_$_ASDAppLedgerQuery._resultLimit
+ _OBJC_IVAR_$_ASDAppLedgerQuery._sortOrder
+ _OBJC_IVAR_$_ASDAppReviewAppMetadata._bundleDirectoryName
+ _OBJC_IVAR_$_ASDLazyPromise._executor
+ _OBJC_IVAR_$_ASDLazyPromise._scheduler
+ _OBJC_IVAR_$_ASDTestFlightAppMetadata._bundleDirectoryName
+ _OBJC_METACLASS_$_ASDAppLedger
+ _OBJC_METACLASS_$_ASDAppLedgerItem
+ _OBJC_METACLASS_$_ASDAppLedgerQuery
+ __OBJC_$_CLASS_METHODS_ASDAppLedger
+ __OBJC_$_CLASS_METHODS_ASDAppLedgerItem
+ __OBJC_$_CLASS_METHODS_ASDAppLedgerQuery
+ __OBJC_$_CLASS_PROP_LIST_ASDAppLedger
+ __OBJC_$_CLASS_PROP_LIST_ASDAppLedgerItem
+ __OBJC_$_CLASS_PROP_LIST_ASDAppLedgerQuery
+ __OBJC_$_INSTANCE_METHODS_ASDAppLedger
+ __OBJC_$_INSTANCE_METHODS_ASDAppLedgerItem
+ __OBJC_$_INSTANCE_METHODS_ASDAppLedgerQuery
+ __OBJC_$_INSTANCE_VARIABLES_ASDAppLedgerItem
+ __OBJC_$_INSTANCE_VARIABLES_ASDAppLedgerQuery
+ __OBJC_$_PROP_LIST_ASDAppLedgerItem
+ __OBJC_$_PROP_LIST_ASDAppLedgerQuery
+ __OBJC_CLASS_PROTOCOLS_$_ASDAppLedgerItem
+ __OBJC_CLASS_PROTOCOLS_$_ASDAppLedgerQuery
+ __OBJC_CLASS_RO_$_ASDAppLedger
+ __OBJC_CLASS_RO_$_ASDAppLedgerItem
+ __OBJC_CLASS_RO_$_ASDAppLedgerQuery
+ __OBJC_METACLASS_RO_$_ASDAppLedger
+ __OBJC_METACLASS_RO_$_ASDAppLedgerItem
+ __OBJC_METACLASS_RO_$_ASDAppLedgerQuery
+ ___28+[ASDAppLedger sharedLedger]_block_invoke
+ ___34-[ASDAppQuery _handlePauseForApp:]_block_invoke.64
+ ___35-[ASDAppQuery _handleResumeForApp:]_block_invoke.66
+ ___45-[ASDAppQuery executeQueryWithResultHandler:]_block_invoke.52
+ ___45-[ASDAppQuery executeQueryWithResultHandler:]_block_invoke_2.53
+ ___50-[ASDAppQuery _handleCancelForApp:reportRemotely:]_block_invoke.67
+ ___50-[ASDAppQuery _handleCancelForApp:reportRemotely:]_block_invoke.68
+ ___50-[ASDAppQuery _handleCancelForApp:reportRemotely:]_block_invoke.69
+ ___53-[ASDAppLedger itemsMatchingQuery:completionHandler:]_block_invoke
+ ___53-[ASDAppLedger itemsMatchingQuery:completionHandler:]_block_invoke.4
+ ___53-[ASDAppLedger itemsMatchingQuery:completionHandler:]_block_invoke.5
+ ___53-[ASDAppLedger itemsMatchingQuery:completionHandler:]_block_invoke_2
+ ___53-[ASDAppQuery _newProgressForApp:fromRemoteProgress:]_block_invoke
+ ___53-[ASDAppQuery _newProgressForApp:fromRemoteProgress:]_block_invoke_2
+ ___53-[ASDAppQuery _newProgressForApp:fromRemoteProgress:]_block_invoke_3
+ ___56-[ASDAppQuery notificationCenter:receivedNotifications:]_block_invoke.54
+ ___72-[ASDAppQuery _executeQueryWithPredicate:onPairedDevice:withCompletion:]_block_invoke.61
+ ___block_descriptor_56_e8_32s40s48bs_e72_v24?0"<ASDAppLibraryServiceProtocol><NSXPCProxyCreating>"8"NSError"16ls32l8s48l8s40l8
+ ___swift_memcpy0_1
+ _objc_msgSend$genre
+ _objc_msgSend$initPrivate
+ _objc_msgSend$initWithURL:
+ _objc_msgSend$installedSinceDate
+ _objc_msgSend$itemsMatchingQuery:completionHandler:
+ _objc_msgSend$neverLaunched
+ _objc_msgSend$progressPhase
+ _objc_msgSend$queryAppLedger:replyHandler:
+ _objc_msgSend$resultLimit
+ _objc_msgSend$setGenre:
+ _objc_msgSend$setGenreID:
+ _objc_msgSend$setInstalledSinceDate:
+ _objc_msgSend$setNeverLaunched:
+ _objc_msgSend$setResultLimit:
+ _objc_msgSend$setSortOrder:
+ _objc_msgSend$sortOrder
+ _objc_msgSend$updateCodedPropertiesFromApp:
- -[ASDAppQuery _newProgressForApp:fromRemoteProgress:usingServiceBroker:]
- -[ASDAppQuery _replaceCachedResultsWithResults:]
- GCC_except_table69
- ___34-[ASDAppQuery _handlePauseForApp:]_block_invoke.50
- ___35-[ASDAppQuery _handleResumeForApp:]_block_invoke.52
- ___35-[ASDSubscriptionEntitlements init]_block_invoke_10
- ___44-[ASDPersonalizationStore getGroupingToken:]_block_invoke
- ___44-[ASDPersonalizationStore getGroupingToken:]_block_invoke_2
- ___44-[ASDPersonalizationStore getGroupingToken:]_block_invoke_3
- ___45-[ASDAppQuery executeQueryWithResultHandler:]_block_invoke_3
- ___45-[ASDAppQuery executeQueryWithResultHandler:]_block_invoke_4
- ___48-[ASDPersonalizationStore getTasteProfileToken:]_block_invoke
- ___48-[ASDPersonalizationStore getTasteProfileToken:]_block_invoke_2
- ___48-[ASDPersonalizationStore getTasteProfileToken:]_block_invoke_3
- ___50-[ASDAppQuery _handleCancelForApp:reportRemotely:]_block_invoke.53
- ___50-[ASDAppQuery _handleCancelForApp:reportRemotely:]_block_invoke.54
- ___50-[ASDAppQuery _handleCancelForApp:reportRemotely:]_block_invoke.55
- ___54-[ASDPersonalizationStore tasteProfileFeatureEnabled:]_block_invoke
- ___54-[ASDPersonalizationStore tasteProfileFeatureEnabled:]_block_invoke_2
- ___54-[ASDPersonalizationStore tasteProfileFeatureEnabled:]_block_invoke_3
- ___56-[ASDAppQuery notificationCenter:receivedNotifications:]_block_invoke.41
- ___61-[ASDPersonalizationStore setClusterMapping:completionBlock:]_block_invoke
- ___61-[ASDPersonalizationStore setClusterMapping:completionBlock:]_block_invoke_2
- ___61-[ASDPersonalizationStore setClusterMapping:completionBlock:]_block_invoke_3
- ___62-[ASDPersonalizationStore setClusterMappings:completionBlock:]_block_invoke
- ___62-[ASDPersonalizationStore setClusterMappings:completionBlock:]_block_invoke_2
- ___62-[ASDPersonalizationStore setClusterMappings:completionBlock:]_block_invoke_3
- ___65-[ASDPersonalizationStore getClusterMappingsWithCompletionBlock:]_block_invoke
- ___65-[ASDPersonalizationStore getClusterMappingsWithCompletionBlock:]_block_invoke_2
- ___65-[ASDPersonalizationStore getClusterMappingsWithCompletionBlock:]_block_invoke_3
- ___68-[ASDPersonalizationStore reloadClusterMappingsWithCompletionBlock:]_block_invoke
- ___68-[ASDPersonalizationStore reloadClusterMappingsWithCompletionBlock:]_block_invoke_2
- ___68-[ASDPersonalizationStore reloadClusterMappingsWithCompletionBlock:]_block_invoke_3
- ___72-[ASDAppQuery _executeQueryWithPredicate:onPairedDevice:withCompletion:]_block_invoke_2
- ___72-[ASDAppQuery _newProgressForApp:fromRemoteProgress:usingServiceBroker:]_block_invoke
- ___72-[ASDAppQuery _newProgressForApp:fromRemoteProgress:usingServiceBroker:]_block_invoke_2
- ___72-[ASDAppQuery _newProgressForApp:fromRemoteProgress:usingServiceBroker:]_block_invoke_3
- ___block_descriptor_40_e8_32bs_e30_v24?0"NSString"8"NSError"16ls32l8
- ___swift_memcpy1_1
- __swift_FORCE_LOAD_$_swiftCompression
- __swift_FORCE_LOAD_$_swiftCompression_$_AppStoreDaemon
- _objc_msgSend$getClusterMappingsWithCompletionBlock:
- _objc_msgSend$getGroupingToken:
- _objc_msgSend$reloadClusterMappingsWithCompletionBlock:
- _objc_msgSend$setClusterMapping:completionBlock:
- _objc_msgSend$setClusterMappings:completionBlock:
- _objc_msgSend$tasteProfileFeatureEnabledWithCompletionBlock:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x7
CStrings:
+ "%@ {%@}"
+ "%{public}@: Encountered result with no bundleID: %{public}@"
+ "%{public}@: Forcing query refresh following broker connection"
+ "%{public}@: Found untracked progress for remote install: %{public}@"
+ "%{public}@: Handling app error notification action: %{public}@"
+ "%{public}@: Handling apps refreshed notification"
+ "%{public}@: Handling apps registered notification"
+ "%{public}@: Handling apps unregistered notification"
+ "%{public}@: Handling device specific notification: %{public}@"
+ "%{public}@: Ignoring notification for unmatched device: %{public}@"
+ "%{public}@: Ignoring notifications until query has been run at least once"
+ "%{public}@: Ignoring progress for ASDAppProgressPhaseNoProgress: %{public}@"
+ "%{public}@: Ignoring progress for installed: %{public}@"
+ "%{public}@: Ignoring progress until query has been run at least once"
+ "%{public}@: Ignoring untracked progress for: %{public}@"
+ "%{public}@: Progress complete for: %{public}@"
+ "%{public}@: Query complete, returning %lu results"
+ "%{public}@: Received refresh notification but refresh failed: %{public}@"
+ "%{public}@: Received unexpected notification: %{public}@"
+ "%{public}@: Received unhandled action: %{public}@"
+ "%{public}@: Setting %.2f for: %{public}@"
+ "%{public}@: Starting query execution"
+ "%{public}@: Starting query execution (updates, reloadFromServer=%d)"
+ "%{public}@: _handleAppsReplacedWithResults with results %{public}@"
+ "%{public}@: _handleAppsUpdatedWithResults %{public}@"
+ "%{public}@: _handleNotificationRefreshWithUserInfo Update with returned results %{public}@"
+ "%{public}@: _handleNotificationRefreshWithUserInfo replace with returned results %{public}@"
+ "%{public}@: _removeCachedResultsForBundleIDs removed %{public}@"
+ "%{public}@: _sendResultsChangedWithResults: %{public}@ to observer"
+ "%{public}@: _updateCachedResultsWithResults created new progress for %{public}@"
+ "%{public}@: _updateCachedResultsWithResults receive update with no remote progress, but app %{public}@ is not installed"
+ "%{public}@: _updateCachedResultsWithResults set progress to nil for cached result %{public}@ with error %{public}@"
+ "%{public}@: _updateCachedResultsWithResults set progress to nil for installed app: %{public}@ "
+ "%{public}@: _updateCachedResultsWithResults updated cached progress from %lld to %lld"
+ "(null)"
+ "<%@: %p> bundleID=%@ bundleVersion=%@ itemID=%@ versionID=%@ installDate=%@ lastLaunchDate=%@"
+ "@64@0:8@16@24@32@40@48@56"
+ "ASDAppLedger"
+ "ASDAppLedgerItem"
+ "ASDAppLedgerQuery"
+ "BD"
+ "Command no longer supported"
+ "LL"
+ "NewestToOldest"
+ "OldestToNewest"
+ "T@\"ASDAppLedger\",R,N"
+ "T@\"NSDate\",C,N,V_installedSinceDate"
+ "T@\"NSDate\",R,N,V_installDate"
+ "T@\"NSDate\",R,N,V_lastLaunchDate"
+ "T@\"NSNumber\",R,N,V_itemID"
+ "T@\"NSNumber\",R,N,V_versionID"
+ "T@\"NSString\",C,N,V_bundleDirectoryName"
+ "TB,N,V_neverLaunched"
+ "TQ,N,V_resultLimit"
+ "Tq,N,V_sortOrder"
+ "Unimplemented at /Library/Caches/com.apple.xbs/D25EB013-D769-40DC-A731-1A4595ECE85E/TemporaryDirectory.WeFgR0/Sources/AppStoreDaemonFramework/Libraries/AppStoreDaemon/XPC/Updates/ASDSoftwareUpdatesStore.m:384 : Not supported on iOS"
+ "Unimplemented at /Library/Caches/com.apple.xbs/D25EB013-D769-40DC-A731-1A4595ECE85E/TemporaryDirectory.WeFgR0/Sources/AppStoreDaemonFramework/Libraries/AppStoreDaemon/XPC/Updates/ASDSoftwareUpdatesStore.m:81 : Not supported on iOS"
+ "Unimplemented at /Library/Caches/com.apple.xbs/D25EB013-D769-40DC-A731-1A4595ECE85E/TemporaryDirectory.WeFgR0/Sources/AppStoreDaemonFramework/Libraries/AppStoreDaemon/XPC/Updates/ASDSoftwareUpdatesStore.m:85 : Not supported on iOS"
+ "Unimplemented at /Library/Caches/com.apple.xbs/D25EB013-D769-40DC-A731-1A4595ECE85E/TemporaryDirectory.WeFgR0/Sources/AppStoreDaemonFramework/Libraries/AppStoreDaemon/XPC/Updates/ASDSoftwareUpdatesStore.m:90 : Not supported on iOS"
+ "VI"
+ "[%{public}@] Failed to query app ledger with error: %{public}@"
+ "[%{public}@] Taste profile no longer supported"
+ "[%{public}@] getClusterMappingsWithCompletionBlock no longer supported"
+ "[%{public}@] getGroupingToken no longer supported"
+ "[%{public}@] getTasteProfileToken no longer supported"
+ "[%{public}@] resetMetricsWithCompletionBlock no longer supported"
+ "[%{public}@] setClusterMapping no longer supported"
+ "[%{public}@] setClusterMappings no longer supported"
+ "_bundleDirectoryName"
+ "_installedSinceDate"
+ "_lastLaunchDate"
+ "_neverLaunched"
+ "_resultLimit"
+ "_sortOrder"
+ "_versionID"
+ "betaExternalVersionID = %lld"
+ "bundleDirectoryName"
+ "bundleShortVersion = %@"
+ "bundleVersion = %@"
+ "genre = %@"
+ "genreID = %@"
+ "initPrivate"
+ "initWithBundleID:bundleVersion:itemID:versionID:installDate:lastLaunchDate:"
+ "installedSinceDate"
+ "installedSinceDate = %@"
+ "itemsMatchingQuery:completionHandler:"
+ "itemsWithCompletionHandler:"
+ "lastLaunchDate"
+ "neverLaunched"
+ "neverLaunched = %@"
+ "queryAppLedger:replyHandler:"
+ "resultLimit"
+ "resultLimit = %lu"
+ "setBundleDirectoryName:"
+ "setInstalledSinceDate:"
+ "setNeverLaunched:"
+ "setResultLimit:"
+ "setSortOrder:"
+ "sharedLedger"
+ "sortOrder"
+ "sortOrder = %@"
+ "v32@0:8@\"ASDAppLedgerQuery\"16@?<v@?@\"NSArray\"@\"NSError\">24"
+ "versionID"
- "EphemeralAccount"
- "Unimplemented at /Library/Caches/com.apple.xbs/Sources/AppStoreDaemonFramework/Libraries/AppStoreDaemon/XPC/Updates/ASDSoftwareUpdatesStore.m:384 : Not supported on iOS"
- "Unimplemented at /Library/Caches/com.apple.xbs/Sources/AppStoreDaemonFramework/Libraries/AppStoreDaemon/XPC/Updates/ASDSoftwareUpdatesStore.m:81 : Not supported on iOS"
- "Unimplemented at /Library/Caches/com.apple.xbs/Sources/AppStoreDaemonFramework/Libraries/AppStoreDaemon/XPC/Updates/ASDSoftwareUpdatesStore.m:85 : Not supported on iOS"
- "Unimplemented at /Library/Caches/com.apple.xbs/Sources/AppStoreDaemonFramework/Libraries/AppStoreDaemon/XPC/Updates/ASDSoftwareUpdatesStore.m:90 : Not supported on iOS"
- "[%{public}@]: Encountered result with no bundleID: %{public}@"
- "[%{public}@]: Forcing query refresh following broker connection"
- "[%{public}@]: Found untracked progress for remote install: %{public}@"
- "[%{public}@]: Handling app error notification action: %{public}@"
- "[%{public}@]: Handling apps refreshed notification"
- "[%{public}@]: Handling apps registered notification"
- "[%{public}@]: Handling apps unregistered notification"
- "[%{public}@]: Handling device specific notification: %{public}@"
- "[%{public}@]: Ignoring notification for unmatched device: %{public}@"
- "[%{public}@]: Ignoring notifications until query has been run at least once"
- "[%{public}@]: Ignoring progress for installed: %{public}@"
- "[%{public}@]: Ignoring progress until query has been run at least once"
- "[%{public}@]: Ignoring untracked progress for: %{public}@"
- "[%{public}@]: Progress complete for: %{public}@"
- "[%{public}@]: Progress started for: %{public}@"
- "[%{public}@]: Received refresh notification but refresh failed: %{public}@"
- "[%{public}@]: Received unexpected notification: %{public}@"
- "[%{public}@]: Received unhandled action: %{public}@"
- "[%{public}@]: Setting %.2f for: %{public}@"
- "[%{public}@]: Taste profile enabled"
- "[%{public}@]: getClusterMappingsWithCompletionBlock"
- "[%{public}@]: getGroupingToken"
- "[%{public}@]: getTasteProfileToken"
- "[%{public}@]: resetMetricsWithCompletionBlock"
- "[%{public}@]: setClusterMapping"
- "[%{public}@]: setClusterMappings"
- "tasteProfileFeatureEnabledWithCompletionBlock:"
- "v24@0:8@?<v@?@\"NSString\"@\"NSError\">16"
- "v24@?0@\"NSString\"8@\"NSError\"16"
- "v32@0:8@\"ASDAppClusterMapping\"16@?<v@?B@\"NSError\">24"

```
