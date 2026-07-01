## MobileAssetDaemon

> `/System/Library/PrivateFrameworks/MobileAssetDaemon.framework/MobileAssetDaemon`

```diff

-  __TEXT.__text: 0x292dd0
+  __TEXT.__text: 0x294490
   __TEXT.__auth_stubs: 0x22d0
-  __TEXT.__objc_methlist: 0x129c4
-  __TEXT.__const: 0x187a
-  __TEXT.__cstring: 0x3ee0d
-  __TEXT.__oslogstring: 0x5e216
-  __TEXT.__gcc_except_tab: 0xeb88
+  __TEXT.__objc_methlist: 0x12a1c
+  __TEXT.__const: 0x188a
+  __TEXT.__cstring: 0x3ef2d
+  __TEXT.__oslogstring: 0x5e866
+  __TEXT.__gcc_except_tab: 0xeb98
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__constg_swiftt: 0xf0
   __TEXT.__swift5_typeref: 0x146

   __TEXT.__unwind_info: 0x55d0
   __TEXT.__eh_frame: 0x90
   __TEXT.__objc_classname: 0x117e
-  __TEXT.__objc_methname: 0x47308
+  __TEXT.__objc_methname: 0x474f5
   __TEXT.__objc_methtype: 0x4844
-  __TEXT.__objc_stubs: 0x273c0
-  __DATA_CONST.__got: 0x1050
+  __TEXT.__objc_stubs: 0x274a0
+  __DATA_CONST.__got: 0x1058
   __DATA_CONST.__const: 0x32c0
   __DATA_CONST.__objc_classlist: 0x478
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xadb0
+  __DATA_CONST.__objc_selrefs: 0xade8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x350
   __DATA_CONST.__objc_arraydata: 0xd50
   __AUTH_CONST.__auth_got: 0x1178
   __AUTH_CONST.__const: 0xfa0
-  __AUTH_CONST.__cfstring: 0x32780
-  __AUTH_CONST.__objc_const: 0x18890
+  __AUTH_CONST.__cfstring: 0x328a0
+  __AUTH_CONST.__objc_const: 0x188f0
   __AUTH_CONST.__objc_arrayobj: 0x2e8
   __AUTH_CONST.__objc_intobj: 0x13c8
   __AUTH_CONST.__objc_dictobj: 0x1e0
   __AUTH.__objc_data: 0x2d08
   __AUTH.__data: 0x110
-  __DATA.__objc_ivar: 0x17a4
+  __DATA.__objc_ivar: 0x17ac
   __DATA.__data: 0x1170
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0xaa0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 7226
-  Symbols:   24186
-  CStrings:  26245
+  Functions: 7234
+  Symbols:   24212
+  CStrings:  26285
 
Sections:
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__unwind_info : content changed
~ __TEXT.__eh_frame : content changed
~ __TEXT.__objc_classname : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH.__objc_data : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
Symbols:
+ +[MADAutoAssetControlManager preferenceStagerInjectAvailableAlreadyDownloaded]
+ +[MADAutoAssetSecure dedupAssetSelectors:dedupingSelectors:]
+ -[MADAutoAssetControlManager preferenceStagerInjectAvailableAlreadyDownloaded]
+ -[MADAutoAssetControlManager setPreferenceStagerInjectAvailableAlreadyDownloaded:]
+ -[MADAutoAssetJob addToPrePersonalizedSelectors:addingAssetSelector:]
+ -[MADAutoAssetJob nextSetAtomicEntryToDownload]
+ -[MADAutoAssetJob refreshOnFilesystemFromManagerPromotingIfStaged:promotingIfStaged:]
+ -[MADAutoAssetJob setAtomicEntriesToDownload]
+ -[MADAutoAssetJob setNextSetAtomicEntryToDownload:]
+ -[MADAutoAssetJob setSetAtomicEntriesToDownload:]
+ -[MADAutoAssetStager emptySetTargetForAssetType:]
+ -[MADAutoAssetStager injectAvailableAlreadyDownloaded:]
+ GCC_except_table801
+ GCC_except_table804
+ _OBJC_IVAR_$_MADAutoAssetControlManager._preferenceStagerInjectAvailableAlreadyDownloaded
+ _OBJC_IVAR_$_MADAutoAssetJob._nextSetAtomicEntryToDownload
+ _OBJC_IVAR_$_MADAutoAssetJob._setAtomicEntriesToDownload
+ ___block_literal_global.2512
+ ___block_literal_global.5535
+ _kMobileAssetPreferencesAutoAssetStagerInjectAvailableAlreadyDownloaded
+ _objc_msgSend$addToPrePersonalizedSelectors:addingAssetSelector:
+ _objc_msgSend$dedupAssetSelectors:dedupingSelectors:
+ _objc_msgSend$emptySetTargetForAssetType:
+ _objc_msgSend$injectAvailableAlreadyDownloaded:
+ _objc_msgSend$nextSetAtomicEntryToDownload
+ _objc_msgSend$preferenceStagerInjectAvailableAlreadyDownloaded
+ _objc_msgSend$refreshOnFilesystemFromManagerPromotingIfStaged:promotingIfStaged:
+ _objc_msgSend$setAtomicEntriesToDownload
+ _objc_msgSend$setNextSetAtomicEntryToDownload:
+ _objc_msgSend$setSetAtomicEntriesToDownload:
- -[MADAutoAssetJob nextSetSpecifierToDownload]
- -[MADAutoAssetJob refreshOnFilesystemFromManagerPromotingIfStaged:]
- -[MADAutoAssetJob setEntryBeingDownloaded]
- -[MADAutoAssetJob setNextSetSpecifierToDownload:]
- GCC_except_table797
- GCC_except_table803
- _OBJC_IVAR_$_MADAutoAssetJob._nextSetSpecifierToDownload
- ___block_literal_global.2509
- ___block_literal_global.5523
- _objc_msgSend$nextSetSpecifierToDownload
- _objc_msgSend$refreshOnFilesystemFromManagerPromotingIfStaged:
- _objc_msgSend$setNextSetSpecifierToDownload:
CStrings:
+ "%@:_setCalculateDownloadSpace"
+ "%@:formAvailableForStagingByCombiningRequiredAndOptional"
+ "%@:newStagingInfoWithGroupsAvailableForStaging"
+ "%@:refreshOnFilesystemFromManagerPromotingIfStaged"
+ "%@~%@"
+ "%{public}@\n[AUTO-STAGER] {%{public}@} unable to allocate storedAvailableForStaging (dropped) | availableForStagingRequiredByTarget:%ld | availableForStagingOptionalByTarget:%ld"
+ "%{public}@\n[AUTO-STAGER] {FormCandidatesDecideDetermine} client-defined set-target for asset-type - not staging based on already-downloaded | candidateDescriptor:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {_extendLookupByAssetTypeWithDownloadedDescriptors} | final candidate summary\n>>> created[Client:%{public}@][No:%{public}@]]\n>>> appended:%{public}@\n>>> addedRequired:%{public}@\n>>> addedOptional:%{public}@\n>>> setTargetRemoves:%{public}@\n>>> noSetConfiguration:%{public}@\n>>> ignored(bySetTarget:%{public}@,NoSupport:%{public}@,EmptySetTarget:%{public}@)"
+ "%{public}@\n[AUTO-STAGER] {addToAvailableForStaging} | ignoring additional entry (different-version) | availableDescriptor:%{public}@ | alreadyTracked:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {addToAvailableForStaging} | ignoring additional entry (same-version) | availableDescriptor:%{public}@"
+ "%{public}@ | {%{public}@} auto-control-manager known descriptor count:%ld | specifierSelector:%{public}@, versionSelector:%{public}@"
+ "%{public}@ | {%{public}@} isOnFilesystem:%{public}@ | assetVersion:%{public}@ | candidate:%{public}@"
+ "%{public}@ | {remainingSetDescriptorToBeDownloaded} about to advance | nextSetAtomicEntryToDownload:%ld | totalEntriesToDownload:%ld"
+ "%{public}@ | {remainingSetDescriptorToBeDownloaded} done advancing | remaingToBeDownloaded:%@"
+ "%{public}@ | {remainingSetDescriptorToBeDownloaded} no newer to download | skipping nextEntryToDownload:%{public}@ | nextSetAtomicEntryToDownload:%ld"
+ "2.5.6"
+ "Loaded built-in MobileAssetDaemon_Framework Jun 21 2026 20:17:37"
+ "T@\"NSArray\",&,N,V_setAtomicEntriesToDownload"
+ "TB,N,V_preferenceStagerInjectAvailableAlreadyDownloaded"
+ "Tq,N,V_nextSetAtomicEntryToDownload"
+ "[FROM-AVAILABLE-FOR-STAGING] {%{public}@} duplicate OPTIONAL descriptor (filtered) | nextOptionalDescriptor:%{public}@"
+ "[FROM-AVAILABLE-FOR-STAGING] {%{public}@} duplicate REQUIRED descriptor (filtered) | nextRequiredDescriptor:%{public}@"
+ "[overall]instance:%@,selector:%@,UUID:%@,tasks:%lu,requests:%ld,table:%@,FSM:%@,sched:%@,NWFail:%@|beingCancled:%@|[earlier]sched:%@,NWFail:%@|bonded:%@|[active]instance:%@,desire:%@(awaitDownload:%@,checkAwait:%@),found:%@,end:%@,listen:%@,jobInfo:%@|[aggregated]policy:%@,clientRequested:%@|firstClientName:%@,triggeringLayer:%@|onFilesystemByVersion:%ld|[check]Base:%@,UUID:%@,lookupGrant:%@,rampFG:%@,rampLatch:%@,options:%@|[asset]base:%@,patch:%@,full:%@,newer:%@,downloading:%@,scheduler:%@,lookupRsp:%@(forConfig:%@),user:%@,boosting:%@,checking:%@,determining:%@,locking:%@,patched:%@|[installed]:version:%@,build:%@|[status]current:%@,progress:%@,lastPatch:%@|[results]selector:%@,instance:%@,found:%@,end:%@,listen:%@,[set]aggregatedPolicy:%@,descriptor:%@,setToDownload:%ld,next:%ld,found:%@,discardRampled:%@"
+ "_nextSetAtomicEntryToDownload"
+ "_preferenceStagerInjectAvailableAlreadyDownloaded"
+ "_setAtomicEntriesToDownload"
+ "addToPrePersonalizedSelectors:addingAssetSelector:"
+ "already-persisted no longer defined | alreadyDefinedSetTarget:%@"
+ "dedupAssetSelectors:dedupingSelectors:"
+ "emptySetTargetForAssetType:"
+ "injectAvailableAlreadyDownloaded:"
+ "invalid nextSetAtomicEntryToDownload value"
+ "nextSetAtomicEntryToDownload"
+ "nil prePersonalizedSelector provided to addToPrePersonalizedSelectors"
+ "no next to place | nextSetAtomicEntryToDownload:%ld, autoAssetEntries:%ld"
+ "not already defined | clientSpecifyingSetTarget:%@"
+ "preferenceStagerInjectAvailableAlreadyDownloaded"
+ "refreshOnFilesystemFromManagerPromotingIfStaged:promotingIfStaged:"
+ "set-target changed | clientSpecifyingSetTarget:%@ | alreadyDefinedSetTarget:%@"
+ "set-target had not been defined"
+ "setAtomicEntriesToDownload"
+ "setNextSetAtomicEntryToDownload:"
+ "setPreferenceStagerInjectAvailableAlreadyDownloaded:"
+ "setSetAtomicEntriesToDownload:"
+ "{%@} failed to build attributes/expected-bytes | groupName:%@"
+ "{%{public}@:injectAvailableAlreadyDownloaded} injecting already-downloaded auto-asset-descriptor | autoAssetDescriptor:%{public}@"
+ "{%{public}@} (%{public}@)\n[SET-DECIDE-FOUND] filtering of assets to be downloaded | assetType:%{public}@\n>>> AlreadyPersonalized:%{public}@\n>>> RequiresPersonalization:%{public}@\n>>> toBeDownloaded:%{public}@"
+ "{%{public}@} (%{public}@)\n[SET-DECIDE-FOUND] potential full selector | potentialDescriptor:%{public}@ | latestOnFilesystem:%{public}@"
+ "{%{public}@} deduped array of asset-selectors | toBeDedupedSelectors:%ld | duplicated:\n%{public}@"
+ "{%{public}@} prior to deduping available-for-staging that includes already-downloaded | indicateHaveAvailable:%{public}@ | targetLookupKey:%{public}@ | availableForStagingByTarget:%ld"
+ "{%{public}@} stripped out already-downloaded | indicateHaveAvailable:%{public}@ | targetLookupKey:%{public}@ | availableForStagingByTarget:%ld"
+ "{setTargetPersistedMatchesClientSpecified} | already-persisted no longer defined | mismatchReason:%{public}@ | setInfoInstance:%{public}@"
+ "{setTargetPersistedMatchesClientSpecified} | corrupted clientSpecifyingSetTargetsByOSRange container - treating as same set-target to preserve persisted | setInfoInstance:%{public}@"
+ "{setTargetPersistedMatchesClientSpecified} | duplicated set-target provided by client - treating as same set-target to preserve persisted | duplicatedSetTarget:%@ | setInfoInstance:%{public}@"
+ "{setTargetPersistedMatchesClientSpecified} | not already defined | mismatchReason:%{public}@ | setInfoInstance:%{public}@"
- "%{public}@\n[AUTO-STAGER] {%{public}@} [BY-GROP-MODE] | unable to allocate storedAvailableForStaging (dropped) | availableForStagingRequiredByTarget:%ld | availableForStagingOptionalByTarget:%ld"
- "%{public}@\n[AUTO-STAGER] {FormCandidatesDecideDetermine} client-defined set-target for asset-type - not staging based on alread-downloaded | descriptor:%{public}@"
- "%{public}@\n[AUTO-STAGER] {_extendLookupByAssetTypeWithDownloadedDescriptors} | final candidate summary\n>>> created[Client:%{public}@][No:%{public}@]]\n>>> appended:%{public}@\n>>> addedRequired:%{public}@\n>>> addedOptional:%{public}@\n>>> setTargetRemoves:%{public}@\n>>> noSetConfiguration:%{public}@\n>>> ignored(bySetTarget:%{public}@,NoSupport:%{public}@)"
- "%{public}@\n[AUTO-STAGER] {addToAvailableForStaging} | ignoring additional entry for descriptor:%{public}@"
- "%{public}@ | {refreshOnFilesystemFromManagerPromotingIfStaged} auto-control-manager known descriptor count:%ld | specifierSelector:%{public}@, versionSelector:%{public}@"
- "%{public}@ | {refreshOnFilesystemFromManagerPromotingIfStaged} isOnFilesystem:%{public}@ | assetVersion:%{public}@ | candidate:%{public}@"
- "%{public}@ | {remainingSetDescriptorToBeDownloaded} no newer to download | skipping nextEntryToDownload:%{public}@"
- "(%{public}@)\n[SET-DECIDE-FOUND] potential full selector: %{public}@:potentialDescriptor:%{public}@,onFS:%{public}@"
- "2.5.5"
- "Loaded built-in MobileAssetDaemon_Framework Jun  7 2026 21:35:31"
- "Tq,N,V_nextSetSpecifierToDownload"
- "[FROM-AVAILABLE-FOR-STAGING] {%{public}@:formAvailableForStagingByCombiningRequiredAndOptional} duplicate OPTIONAL descriptor (filtered) | nextOptionalDescriptor:%{public}@"
- "[FROM-AVAILABLE-FOR-STAGING] {%{public}@:formAvailableForStagingByCombiningRequiredAndOptional} duplicate REQUIRED descriptor (filtered) | nextRequiredDescriptor:%{public}@"
- "[overall]instance:%@,selector:%@,UUID:%@,tasks:%lu,requests:%ld,table:%@,FSM:%@,sched:%@,NWFail:%@|beingCancled:%@|[earlier]sched:%@,NWFail:%@|bonded:%@|[active]instance:%@,desire:%@(awaitDownload:%@,checkAwait:%@),found:%@,end:%@,listen:%@,jobInfo:%@|[aggregated]policy:%@,clientRequested:%@|firstClientName:%@,triggeringLayer:%@|onFilesystemByVersion:%ld|[check]Base:%@,UUID:%@,lookupGrant:%@,rampFG:%@,rampLatch:%@,options:%@|[asset]base:%@,patch:%@,full:%@,newer:%@,downloading:%@,scheduler:%@,lookupRsp:%@(forConfig:%@),user:%@,boosting:%@,checking:%@,determining:%@,locking:%@,patched:%@|[installed]:version:%@,build:%@|[status]current:%@,progress:%@,lastPatch:%@|[results]selector:%@,instance:%@,found:%@,end:%@,listen:%@,[set]aggregatedPolicy:%@,descriptor:%@,next:%ld,found:%@,discardRampled:%@"
- "_nextSetSpecifierToDownload"
- "invalid nextSetSpecifierToDownload value"
- "nextSetSpecifierToDownload"
- "no next to place | nextSetSpecifierToDownload:%ld, autoAssetEntries:%ld"
- "refreshOnFilesystemFromManagerPromotingIfStaged:"
- "set-target changed | clientDomainName:%@ | assetSetIdentifier:%@ | currentlyPersisted:%@ | clientProvided:%@ | minTargetOSMatch:%@ | maxTargetOSMatch:%@ | entriesMatch:%@"
- "setEntryBeingDownloaded"
- "setNextSetSpecifierToDownload:"
- "{%@:newStagingInfoWithGroupsAvailableForStaging} failed to build attributes/expected-bytes | groupName:%@"
- "{setTargetPersistedMatchesClientSpecified} | new set-target | setInfoInstance:%{public}@"

```
