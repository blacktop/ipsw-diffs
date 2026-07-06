## MobileAssetDaemon

> `/System/Library/PrivateFrameworks/MobileAssetDaemon.framework/Versions/A/MobileAssetDaemon`

```diff

-  __TEXT.__text: 0x2861f4
-  __TEXT.__objc_methlist: 0x12a84
+  __TEXT.__text: 0x285090
+  __TEXT.__objc_methlist: 0x12a04
   __TEXT.__const: 0x155a
-  __TEXT.__cstring: 0x3f002
-  __TEXT.__oslogstring: 0x5c7a7
-  __TEXT.__gcc_except_tab: 0xd9e4
+  __TEXT.__cstring: 0x3ed82
+  __TEXT.__oslogstring: 0x5c937
+  __TEXT.__gcc_except_tab: 0xd874
   __TEXT.__constg_swiftt: 0xf0
   __TEXT.__swift5_typeref: 0x146
   __TEXT.__swift5_fieldmd: 0x3c

   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_proto: 0x24
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x45d8
+  __TEXT.__unwind_info: 0x4560
   __TEXT.__eh_frame: 0x10c
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xad58
+  __DATA_CONST.__objc_selrefs: 0xacf0
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x358
-  __DATA_CONST.__objc_arraydata: 0xec8
-  __DATA_CONST.__got: 0xfe8
+  __DATA_CONST.__objc_arraydata: 0xed0
+  __DATA_CONST.__got: 0x11f0
   __AUTH_CONST.__const: 0x3250
-  __AUTH_CONST.__cfstring: 0x326a0
-  __AUTH_CONST.__objc_const: 0x18a18
+  __AUTH_CONST.__cfstring: 0x32540
+  __AUTH_CONST.__objc_const: 0x18aa8
   __AUTH_CONST.__objc_arrayobj: 0x330
   __AUTH_CONST.__objc_intobj: 0x13b0
   __AUTH_CONST.__objc_dictobj: 0x2d0
   __AUTH_CONST.__auth_got: 0x1140
-  __AUTH.__objc_data: 0x8a0
-  __AUTH.__data: 0xe8
-  __DATA.__objc_ivar: 0x17cc
-  __DATA.__data: 0x1060
+  __AUTH.__objc_data: 0x828
+  __AUTH.__data: 0xc0
+  __DATA.__objc_ivar: 0x17d8
+  __DATA.__data: 0x1058
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x5a8
-  __DATA_DIRTY.__objc_data: 0x24b8
-  __DATA_DIRTY.__data: 0x78
-  __DATA_DIRTY.__bss: 0x518
+  __DATA.__bss: 0x550
+  __DATA_DIRTY.__objc_data: 0x2530
+  __DATA_DIRTY.__data: 0xa8
+  __DATA_DIRTY.__bss: 0x568
   - /System/Library/Frameworks/AuthenticationServices.framework/Versions/A/AuthenticationServices
   - /System/Library/Frameworks/CFNetwork.framework/Versions/A/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 7329
-  Symbols:   17027
-  CStrings:  17308
+  Functions: 7319
+  Symbols:   17007
+  CStrings:  17282
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
Symbols:
+ +[MADAnalyticsBiomeEventPayload biomePayloadPSUSComplete:]
+ +[MADAutoAssetControlManager preferenceStagerInjectAvailableAlreadyDownloaded]
+ +[MADAutoAssetSecure dedupAssetSelectors:dedupingSelectors:]
+ +[MADAutoAssetSecure doesPersonalizationErrorIndicateServerUnreachable:]
+ +[SecureMobileAssetBundle doesPersonalizationErrorIndicateServerUnreachable:]
+ -[MADAutoAssetControlManager _checkAndEmitPSUSCompletionIfNeeded]
+ -[MADAutoAssetControlManager _emitPSUSCompletionBiomeEvent]
+ -[MADAutoAssetControlManager assetPersonalizatonAttemptCompletePostEvent:withControlParam:justEncounteredError:]
+ -[MADAutoAssetControlManager preferenceStagerInjectAvailableAlreadyDownloaded]
+ -[MADAutoAssetControlManager psusCompletionEventEmitted]
+ -[MADAutoAssetControlManager setPreferenceStagerInjectAvailableAlreadyDownloaded:]
+ -[MADAutoAssetControlManager setPsusCompletionEventEmitted:]
+ -[MADAutoAssetJob addToPrePersonalizedSelectors:addingAssetSelector:]
+ -[MADAutoAssetJob nextSetAtomicEntryToDownload]
+ -[MADAutoAssetJob refreshOnFilesystemFromManagerPromotingIfStaged:promotingIfStaged:]
+ -[MADAutoAssetJob setAtomicEntriesToDownload]
+ -[MADAutoAssetJob setNextSetAtomicEntryToDownload:]
+ -[MADAutoAssetJob setSetAtomicEntriesToDownload:]
+ -[MADAutoAssetStager injectAvailableAlreadyDownloaded:]
+ GCC_except_table330
+ GCC_except_table338
+ GCC_except_table340
+ GCC_except_table342
+ GCC_except_table346
+ GCC_except_table348
+ GCC_except_table350
+ GCC_except_table351
+ GCC_except_table371
+ GCC_except_table372
+ GCC_except_table373
+ GCC_except_table377
+ GCC_except_table383
+ GCC_except_table386
+ GCC_except_table387
+ GCC_except_table388
+ GCC_except_table391
+ GCC_except_table392
+ GCC_except_table396
+ GCC_except_table427
+ GCC_except_table430
+ GCC_except_table460
+ GCC_except_table468
+ GCC_except_table469
+ GCC_except_table470
+ GCC_except_table471
+ GCC_except_table472
+ GCC_except_table473
+ GCC_except_table550
+ GCC_except_table552
+ GCC_except_table609
+ GCC_except_table610
+ GCC_except_table650
+ GCC_except_table654
+ GCC_except_table660
+ GCC_except_table675
+ GCC_except_table704
+ GCC_except_table838
+ GCC_except_table839
+ GCC_except_table840
+ GCC_except_table841
+ OBJC_IVAR_$_MADAutoAssetControlManager._preferenceStagerInjectAvailableAlreadyDownloaded
+ OBJC_IVAR_$_MADAutoAssetControlManager._psusCompletionEventEmitted
+ OBJC_IVAR_$_MADAutoAssetJob._nextSetAtomicEntryToDownload
+ OBJC_IVAR_$_MADAutoAssetJob._setAtomicEntriesToDownload
+ _OUTLINED_FUNCTION_48
+ _OUTLINED_FUNCTION_72
+ _OUTLINED_FUNCTION_75
+ _kMobileAssetPreferencesAutoAssetStagerInjectAvailableAlreadyDownloaded
+ _objc_msgSend$_checkAndEmitPSUSCompletionIfNeeded
+ _objc_msgSend$_emitPSUSCompletionBiomeEvent
+ _objc_msgSend$addToPrePersonalizedSelectors:addingAssetSelector:
+ _objc_msgSend$assetPersonalizatonAttemptCompletePostEvent:withControlParam:justEncounteredError:
+ _objc_msgSend$biomePayloadPSUSComplete:
+ _objc_msgSend$dedupAssetSelectors:dedupingSelectors:
+ _objc_msgSend$doesPersonalizationErrorIndicateServerUnreachable:
+ _objc_msgSend$injectAvailableAlreadyDownloaded:
+ _objc_msgSend$nextSetAtomicEntryToDownload
+ _objc_msgSend$preferenceStagerInjectAvailableAlreadyDownloaded
+ _objc_msgSend$psusCompletionEventEmitted
+ _objc_msgSend$refreshOnFilesystemFromManagerPromotingIfStaged:promotingIfStaged:
+ _objc_msgSend$setAtomicEntriesToDownload
+ _objc_msgSend$setNextSetAtomicEntryToDownload:
+ _objc_msgSend$setPsusCompletionEventEmitted:
+ _objc_msgSend$setSetAtomicEntriesToDownload:
- +[MADActivityManager transferOwnership:toOwner:reason:]
- +[MADAutoAssetStager migrateMismatchedPersistedSetPromotionVersion:forEntryID:withMismatchedState:]
- -[DownloadManager getBackoffParametersForError:base:max:]
- -[DownloadManager retryDelayForDownloadError:retryCount:]
- -[MADAutoAssetControlManager assetPersonalizatonAttemptCompletePostEvent:withControlParam:]
- -[MADAutoAssetControlManager doesSetDescriptor:coverAllForAtomicInstanceEntries:]
- -[MADAutoAssetControlManager findAtomicEntryForAssetType:forAssetSpecifier:representedByLookupResult:]
- -[MADAutoAssetControlManager findAtomicEntryForAssetType:forAssetSpecifier:representedByStatus:]
- -[MADAutoAssetControlManager findSetEntryForAssetType:forAssetSpecifier:representedByConfiguration:]
- -[MADAutoAssetControlManager locateSetDescriptorActiveJobPreferringByAtomicInstance:elseByClientDomain:forAssetSetIdentifier:]
- -[MADAutoAssetControlManager notifyLockerAsIndicatedByJob:]
- -[MADAutoAssetControlManager osTransactionNamePreviouslyInFlightJob:]
- -[MADAutoAssetJob action_RemoveClient:error:]
- -[MADAutoAssetJob action_SetLookupNoneContinue:error:]
- -[MADAutoAssetJob appendUniqueSelectorForDescriptor:toArray:]
- -[MADAutoAssetJob assetSetEntryForAssetMetadata:]
- -[MADAutoAssetJob nextSetSpecifierToDownload]
- -[MADAutoAssetJob refreshOnFilesystemFromManagerPromotingIfStaged:]
- -[MADAutoAssetJob setEntryBeingDownloaded]
- -[MADAutoAssetJob setNextSetSpecifierToDownload:]
- -[MADAutoAssetStager action_AddToStagedDecideMoreAvailable:error:]
- -[MADAutoAssetStager action_AlteredInvalAllAvailable:error:]
- -[MADAutoAssetStager action_AlteredInvalAllAvailableCancelActiveJob:error:]
- -[MADAutoAssetStager action_ClientAcceptEraseCancelActiveJob:error:]
- -[MADAutoAssetStager action_ClientNewerReplyEmptyDetermine:error:]
- -[MADAutoAssetStager action_DecideMoreAvailable:error:]
- -[MADAutoAssetStager action_ReplyNothingStagedEraseAll:error:]
- -[MADAutoAssetStager action_SetTargetInvalAllAvailable:error:]
- -[MADAutoAssetStager action_SetTargetInvalAllAvailableCancelActiveJob:error:]
- -[MADAutoAssetStager purgeAlreadyStagedNotApplicableForRequiredByTarget:andNotApplicableForOptionalByTarget:]
- GCC_except_table337
- GCC_except_table357
- GCC_except_table358
- GCC_except_table366
- GCC_except_table368
- GCC_except_table369
- GCC_except_table370
- GCC_except_table379
- GCC_except_table380
- GCC_except_table381
- GCC_except_table384
- GCC_except_table385
- GCC_except_table395
- GCC_except_table398
- GCC_except_table399
- GCC_except_table400
- GCC_except_table401
- GCC_except_table403
- GCC_except_table404
- GCC_except_table434
- GCC_except_table437
- GCC_except_table467
- GCC_except_table475
- GCC_except_table476
- GCC_except_table477
- GCC_except_table478
- GCC_except_table479
- GCC_except_table480
- GCC_except_table557
- GCC_except_table559
- GCC_except_table616
- GCC_except_table617
- GCC_except_table655
- GCC_except_table659
- GCC_except_table665
- GCC_except_table680
- GCC_except_table709
- GCC_except_table842
- GCC_except_table843
- GCC_except_table845
- GCC_except_table848
- OBJC_IVAR_$_MADAutoAssetJob._nextSetSpecifierToDownload
- _OUTLINED_FUNCTION_47
- _OUTLINED_FUNCTION_71
- _OUTLINED_FUNCTION_74
- _objc_msgSend$action_AddToStagedDecideMoreAvailable:error:
- _objc_msgSend$action_AlteredInvalAllAvailable:error:
- _objc_msgSend$action_AlteredInvalAllAvailableCancelActiveJob:error:
- _objc_msgSend$action_ClientAcceptEraseCancelActiveJob:error:
- _objc_msgSend$action_ClientNewerReplyEmptyDetermine:error:
- _objc_msgSend$action_DecideMoreAvailable:error:
- _objc_msgSend$action_RemoveClient:error:
- _objc_msgSend$action_ReplyNothingStagedEraseAll:error:
- _objc_msgSend$action_SetLookupNoneContinue:error:
- _objc_msgSend$action_SetTargetInvalAllAvailable:error:
- _objc_msgSend$action_SetTargetInvalAllAvailableCancelActiveJob:error:
- _objc_msgSend$assetPersonalizatonAttemptCompletePostEvent:withControlParam:
- _objc_msgSend$assignOwner:
- _objc_msgSend$getBackoffParametersForError:base:max:
- _objc_msgSend$nameOfLayer:
- _objc_msgSend$nextSetSpecifierToDownload
- _objc_msgSend$recordFailedOperation:fromLayer:forAssetID:withSelector:failingWithError:forTargetOSVersion:forTargetBuildVersion:
- _objc_msgSend$refreshOnFilesystemFromManagerPromotingIfStaged:
- _objc_msgSend$setNextSetSpecifierToDownload:
CStrings:
+ "%@:_setCalculateDownloadSpace"
+ "%@:newStagingInfoWithGroupsAvailableForStaging"
+ "%@:refreshOnFilesystemFromManagerPromotingIfStaged"
+ "%{public}@ | {%{public}@} auto-control-manager known descriptor count:%ld | specifierSelector:%{public}@, versionSelector:%{public}@"
+ "%{public}@ | {%{public}@} isOnFilesystem:%{public}@ | assetVersion:%{public}@ | candidate:%{public}@"
+ "%{public}@ | {remainingSetDescriptorToBeDownloaded} about to advance | nextSetAtomicEntryToDownload:%ld | totalEntriesToDownload:%ld"
+ "%{public}@ | {remainingSetDescriptorToBeDownloaded} done advancing | remaingToBeDownloaded:%@"
+ "%{public}@ | {remainingSetDescriptorToBeDownloaded} no newer to download | skipping nextEntryToDownload:%{public}@ | nextSetAtomicEntryToDownload:%ld"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ndbIMJ/Sources/MobileAssetDaemon/ControlManager.m"
+ "Loaded built-in MobileAssetDaemon_Framework Jun 27 2026 02:59:40"
+ "MAAIRB_NOTIF_PSUS_COMPLETE"
+ "MobileAssetPersonalizationServerURL"
+ "PSUS_ALL_WORK_COMPLETE     "
+ "[PSUS-COMPLETE] all PSUS promotion work complete"
+ "[SMA] Overridden signing server from SoftwareUpdate: %@"
+ "[SMA] SoftwareUpdate signing server override is set but invalid"
+ "[overall]instance:%@,selector:%@,UUID:%@,tasks:%lu,requests:%ld,table:%@,FSM:%@,sched:%@,NWFail:%@|beingCancled:%@|[earlier]sched:%@,NWFail:%@|bonded:%@|[active]instance:%@,desire:%@(awaitDownload:%@,checkAwait:%@),found:%@,end:%@,listen:%@,jobInfo:%@|[aggregated]policy:%@,clientRequested:%@|firstClientName:%@,triggeringLayer:%@|onFilesystemByVersion:%ld|[check]Base:%@,UUID:%@,lookupGrant:%@,rampFG:%@,rampLatch:%@,options:%@|[asset]base:%@,patch:%@,full:%@,newer:%@,downloading:%@,scheduler:%@,lookupRsp:%@(forConfig:%@),user:%@,boosting:%@,checking:%@,determining:%@,locking:%@,patched:%@|[installed]:version:%@,build:%@|[status]current:%@,progress:%@,lastPatch:%@|[results]selector:%@,instance:%@,found:%@,end:%@,listen:%@,[set]aggregatedPolicy:%@,descriptor:%@,setToDownload:%ld,next:%ld,found:%@,discardRampled:%@"
+ "com.apple.eligibilityd"
+ "invalid nextSetAtomicEntryToDownload value"
+ "nil prePersonalizedSelector provided to addToPrePersonalizedSelectors"
+ "no next to place | nextSetAtomicEntryToDownload:%ld, autoAssetEntries:%ld"
+ "psusCompletionEmitted"
+ "{%@} failed to build attributes/expected-bytes | groupName:%@"
+ "{%{public}@:injectAvailableAlreadyDownloaded} injecting already-downloaded auto-asset-descriptor | autoAssetDescriptor:%{public}@"
+ "{%{public}@} (%{public}@)\n[SET-DECIDE-FOUND] filtering of assets to be downloaded | assetType:%{public}@\n>>> AlreadyPersonalized:%{public}@\n>>> RequiresPersonalization:%{public}@\n>>> toBeDownloaded:%{public}@"
+ "{%{public}@} (%{public}@)\n[SET-DECIDE-FOUND] potential full selector | potentialDescriptor:%{public}@ | latestOnFilesystem:%{public}@"
+ "{%{public}@} deduped array of asset-selectors | toBeDedupedSelectors:%ld | duplicated:\n%{public}@"
+ "{%{public}@} prior to deduping available-for-staging that includes already-downloaded | indicateHaveAvailable:%{public}@ | targetLookupKey:%{public}@ | availableForStagingByTarget:%ld"
+ "{%{public}@} stripped out already-downloaded | indicateHaveAvailable:%{public}@ | targetLookupKey:%{public}@ | availableForStagingByTarget:%ld"
+ "{freshnessChangeNewLatestToVendClientDomainNames} __freshnessClientDomainNames:\n%{public}@"
- "%{public}@\n[AUTO-STAGER] {AddToStagedDecideMoreAvailable} asset-descriptor ALREADY-DOWNLOADED | self.activeJobDescriptor:%{public}@"
- "%{public}@\n[AUTO-STAGER] {ClientNewerReplyEmptyDetermine} [STAGING-CLIENT-REQUEST(DETERMINE)] when committed to other operation | [NO-CANDIDATES]"
- "%{public}@ %{public}@ OWNER %{public}@=>%{public}@ | %{public}@"
- "%{public}@ | {refreshOnFilesystemFromManagerPromotingIfStaged} auto-control-manager known descriptor count:%ld | specifierSelector:%{public}@, versionSelector:%{public}@"
- "%{public}@ | {refreshOnFilesystemFromManagerPromotingIfStaged} isOnFilesystem:%{public}@ | assetVersion:%{public}@ | candidate:%{public}@"
- "%{public}@ | {remainingSetDescriptorToBeDownloaded} no newer to download | skipping nextEntryToDownload:%{public}@"
- "(%{public}@)\n[SET-DECIDE-FOUND] potential full selector: %{public}@:potentialDescriptor:%{public}@,onFS:%{public}@"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Yb69OZ/Sources/MobileAssetDaemon/ControlManager.m"
- "AddToStagedDecideMoreAvailable"
- "AlteredInvalAllAvailable"
- "AlteredInvalAllAvailableCancelActiveJob"
- "ClientAcceptEraseCancelActiveJob"
- "ClientNewerReplyEmptyDetermine"
- "DecideMoreAvailable"
- "Loaded built-in MobileAssetDaemon_Framework Jun 13 2026 23:32:19"
- "MADJob:RemoveClient"
- "MADJob:SetLookupNoneContinue"
- "MADStager:AddToStagedDecideMoreAvailable"
- "MADStager:AlteredInvalAllAvailable"
- "MADStager:AlteredInvalAllAvailableCancelActiveJob"
- "MADStager:ClientAcceptEraseCancelActiveJob"
- "MADStager:ClientNewerReplyEmptyDetermine"
- "MADStager:DecideMoreAvailable"
- "MADStager:ReplyNothingStagedEraseAll"
- "MADStager:SetTargetInvalAllAvailable"
- "MADStager:SetTargetInvalAllAvailableCancelActiveJob"
- "ReplyNothingStagedEraseAll"
- "SetLookupNoneContinue"
- "SetTargetInvalAllAvailable"
- "SetTargetInvalAllAvailableCancelActiveJob"
- "[AUTO-ASSET] [LOCAL-CONTENT-URL] {notifyLockerAsIndicatedByJob} %{public}@"
- "[NOTIFY-LOCKER] found auto-asset without localContentURL and/or assetAttributes in response message"
- "[NOTIFY-LOCKER] no indication of found auto-asset in response message"
- "[overall]instance:%@,selector:%@,UUID:%@,tasks:%lu,requests:%ld,table:%@,FSM:%@,sched:%@,NWFail:%@|beingCancled:%@|[earlier]sched:%@,NWFail:%@|bonded:%@|[active]instance:%@,desire:%@(awaitDownload:%@,checkAwait:%@),found:%@,end:%@,listen:%@,jobInfo:%@|[aggregated]policy:%@,clientRequested:%@|firstClientName:%@,triggeringLayer:%@|onFilesystemByVersion:%ld|[check]Base:%@,UUID:%@,lookupGrant:%@,rampFG:%@,rampLatch:%@,options:%@|[asset]base:%@,patch:%@,full:%@,newer:%@,downloading:%@,scheduler:%@,lookupRsp:%@(forConfig:%@),user:%@,boosting:%@,checking:%@,determining:%@,locking:%@,patched:%@|[installed]:version:%@,build:%@|[status]current:%@,progress:%@,lastPatch:%@|[results]selector:%@,instance:%@,found:%@,end:%@,listen:%@,[set]aggregatedPolicy:%@,descriptor:%@,next:%ld,found:%@,discardRampled:%@"
- "auto-asset-job failed without providing operationError"
- "auto-asset-job has indicated failure to downloaded content"
- "com.apple.MobileAsset.AutoControlManager.Job.PreviouslyInFlight"
- "found by job yet no local content URL | found:%@"
- "invalid nextSetSpecifierToDownload value"
- "no next to place | nextSetSpecifierToDownload:%ld, autoAssetEntries:%ld"
- "notifyLockerAsIndicatedByJob"
- "purgeAlreadyStagedNotApplicableForRequiredByTarget"
- "{%@:newStagingInfoWithGroupsAvailableForStaging} failed to build attributes/expected-bytes | groupName:%@"
- "{notifyLockerAsIndicatedByJob} [NOTIFY-LOCKER] client lock request without desire for eventInfo:%@"
- "{notifyLockerAsIndicatedByJob} [NOTIFY-LOCKER] should never be called for set-job"

```
