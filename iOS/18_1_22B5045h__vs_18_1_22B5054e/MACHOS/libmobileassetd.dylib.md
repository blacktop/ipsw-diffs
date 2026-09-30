## libmobileassetd.dylib

> `/usr/lib/libmobileassetd.dylib`

```diff

-1309.40.57.0.3
-  __TEXT.__text: 0x25b38c
+1309.40.57.522.1
+  __TEXT.__text: 0x25d4bc
   __TEXT.__auth_stubs: 0x2370
-  __TEXT.__objc_stubs: 0x1f6a0
-  __TEXT.__objc_methlist: 0xede8
+  __TEXT.__objc_stubs: 0x1f7a0
+  __TEXT.__objc_methlist: 0xee58
   __TEXT.__const: 0x494e
-  __TEXT.__objc_methname: 0x366e7
-  __TEXT.__cstring: 0x4c1dc
+  __TEXT.__objc_methname: 0x36880
+  __TEXT.__cstring: 0x4c70c
   __TEXT.__objc_classname: 0xd7b
-  __TEXT.__objc_methtype: 0x340b
-  __TEXT.__oslogstring: 0x2fb6e
-  __TEXT.__gcc_except_tab: 0x251c
+  __TEXT.__objc_methtype: 0x3428
+  __TEXT.__oslogstring: 0x300c0
+  __TEXT.__gcc_except_tab: 0x2544
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__swift5_typeref: 0x10c4
   __TEXT.__constg_swiftt: 0x1530

   __TEXT.__swift5_protos: 0x60
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_capture: 0x10
-  __TEXT.__unwind_info: 0x46f0
+  __TEXT.__unwind_info: 0x4718
   __TEXT.__eh_frame: 0x30c4
   __DATA_CONST.__auth_got: 0x11c8
   __DATA_CONST.__got: 0x6c8
   __DATA_CONST.__auth_ptr: 0x9c8
-  __DATA_CONST.__const: 0x6660
-  __DATA_CONST.__cfstring: 0x31280
+  __DATA_CONST.__const: 0x6688
+  __DATA_CONST.__cfstring: 0x31580
   __DATA_CONST.__objc_classlist: 0x3e0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8a48
+  __DATA_CONST.__objc_selrefs: 0x8a90
   __DATA_CONST.__objc_intobj: 0x3f0
   __DATA_CONST.__objc_arraydata: 0x988
   __DATA_CONST.__objc_arrayobj: 0x1b0
   __DATA_CONST.__objc_dictobj: 0xf0
-  __DATA.__objc_const: 0x14378
+  __DATA.__objc_const: 0x143d8
   __DATA.__objc_classrefs: 0x7a0
   __DATA.__objc_superrefs: 0x2e8
-  __DATA.__objc_ivar: 0x125c
+  __DATA.__objc_ivar: 0x1264
   __DATA.__objc_data: 0xd10
   __DATA.__data: 0x2608
   __DATA.__bss: 0x53a0

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 8224
-  Symbols:   14758
-  CStrings:  15644
+  Functions: 8236
+  Symbols:   14783
+  CStrings:  15693
 
Symbols:
+ _objc_msgSend$jobDescriptorOnFilesystemConfirmed:
+ GCC_except_table540
+ _objc_msgSend$_logPersistedSetConfiguration:operation:forPersistedEntryID:withSetConfiguration:historyOperation:message:
+ -[MADAutoAssetControlManager loadPersistedCrossCheckTrimSetDescriptors].cold.4
+ _objc_msgSend$isAtomicEntry:alreadyInAtomicEntries:
+ GCC_except_table535
+ __block_literal_global.2002
+ __block_literal_global.2029
+ __block_literal_global.2045
+ _objc_msgSend$_logPersistedSetConfiguration:operation:forPersistedEntryID:withSetConfiguration:historyOperation:recordingSpecifiers:message:
+ _objc_msgSend$setAtomicEntriesRemoveDuplicates:dedupingAtomicEntries:
+ -[MADAutoAssetJob setTryPersonalizeSuccess:]
+ __94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke_2.2849
+ -[MADAutoAssetControlManager persistSetDescriptorDownloadedJob:fromLocation:]
+ __block_literal_global.2037
+ __94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke.2848
+ +[MADAutoAssetControlManager jobDescriptorOnFilesystemConfirmed:]
+ GCC_except_table542
+ __block_literal_global.4170
+ __69-[MADAutoAssetControlManager action_LoadPersistedResumeLocker:error:]_block_invoke.2080
+ -[MADAutoAssetControlManager _logPersistedSetConfiguration:operation:forPersistedEntryID:withSetConfiguration:historyOperation:recordingSpecifiers:message:]
+ -[MADAutoAssetJob setBecameLatestToVend:]
+ GCC_except_table556
+ __block_literal_global.2013
+ _objc_msgSend$tryPersonalizeSuccess
+ -[MADAutoAssetControlManager setAtomicEntriesRemoveDuplicates:dedupingAtomicEntries:]
+ ___block_descriptor_72_e8_32s40s48s56s64r_e5_v8?0ls32l8s40l8s48l8r64l8s56l8
+ _objc_msgSend$setTryPersonalizeSuccess:
+ ___65+[MADAutoAssetControlManager jobDescriptorOnFilesystemConfirmed:]_block_invoke
+ __block_literal_global.3426
+ _objc_msgSend$becameLatestToVend
+ __block_literal_global.2061
+ _objc_msgSend$setBecameLatestToVend:
+ -[MADAutoAssetJob tryPersonalizeSuccess]
+ __block_literal_global.2021
+ _objc_msgSend$persistSetDescriptorDownloadedJob:fromLocation:
+ -[MADAutoAssetControlManager loadPersistedCrossCheckTrimSetDescriptors].cold.5
+ _objc_msgSend$setDescriptorVerifyNoDuplicates:
+ -[MADAutoAssetJob becameLatestToVend]
+ -[MADAutoAssetControlManager setDescriptorVerifyNoDuplicates:]
+ OBJC_IVAR_$_MADAutoAssetJob._becameLatestToVend
+ __block_literal_global.2053
+ -[MADAutoAssetJob isAtomicEntry:alreadyInAtomicEntries:]
+ OBJC_IVAR_$_MADAutoAssetJob._tryPersonalizeSuccess
+ __block_literal_global.2069
+ -[MADAutoAssetControlManager setDescriptorDedupDownloadedEntries:forSetDescriptor:]
+ _objc_msgSend$setDescriptorDedupDownloadedEntries:forSetDescriptor:
+ -[MADAutoAssetControlManager _logPersistedSetConfiguration:operation:forPersistedEntryID:withSetConfiguration:historyOperation:message:]
- -[MADAutoAssetControlManager _logPersistedSetConfiguration:operation:forPersistedEntryID:withSetConfiguration:message:]
- __block_literal_global.2059
- GCC_except_table539
- __block_literal_global.2051
- __block_literal_global.2043
- __block_literal_global.3419
- __94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke.2841
- __block_literal_global.2011
- GCC_except_table534
- __block_literal_global.2003
- __block_literal_global.1992
- -[MADAutoAssetControlManager _logPersistedSetConfiguration:operation:forPersistedEntryID:withSetConfiguration:recordingSpecifiers:message:]
- _objc_msgSend$_logPersistedSetConfiguration:operation:forPersistedEntryID:withSetConfiguration:recordingSpecifiers:message:
- -[MADAutoAssetControlManager persistSetDescriptorDownloadedJob:fromLocation:issuingDownloadedNotification:]
- _objc_msgSend$_logPersistedSetConfiguration:operation:forPersistedEntryID:withSetConfiguration:message:
- __block_literal_global.4143
- _objc_msgSend$loadPersistedSetActiveJobDescriptors
- __block_literal_global.2019
- __block_literal_global.2027
- __block_literal_global.2035
- _objc_msgSend$persistSetDescriptorDownloadedJob:fromLocation:issuingDownloadedNotification:
- __94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke_2.2842
- __69-[MADAutoAssetControlManager action_LoadPersistedResumeLocker:error:]_block_invoke.2068
CStrings:
+ "_logPersistedSetConfiguration:operation:forPersistedEntryID:withSetConfiguration:historyOperation:recordingSpecifiers:message:"
+ "B84@0:8@16@24B32@36@44B52B56B60B64q68@76"
+ "{loadPersistedCrossCheckTrimSetDescriptors} [DROP-SET-DESCRIPTOR] set-descriptor without set-configuration | setDescriptor:%!{(MISSING)public}@"
+ "becameLatestToVend"
+ "tryPersonalizeSuccess"
+ "found no newer content server-side"
+ "{updateSetDescriptorDownloaded} downloaded atomic-entry already tracked (ignoring duplicate) | downloadedAtomicEntry:%!@(MISSING), downloadedAssetDescriptor:%!@(MISSING)"
+ "removing all tracking of set-job downloads in-flight [not yet fully implemented]"
+ "%!{(MISSING)public}@ | {refreshSetFoundToManager} set-job just became set-configuration's latest-to-vend"
+ "found same content server-side already downloaded (and available to client)"
+ "unable to personalize secure asset(s) of the set"
+ "{%!{(MISSING)public}@} set-job current-set-status incomplete | downloadedAtomicInstance:%!{(MISSING)public}@ | latestDownloadedEntries:%!l(MISSING)d | setJobDescriptor:%!{(MISSING)public}@"
+ "Should not"
+ "setAtomicEntriesRemoveDuplicates:dedupingAtomicEntries:"
+ "setBecameLatestToVend:"
+ "SET_CONFIG_NEED_FOR_ATOMIC "
+ "TB,N,V_tryPersonalizeSuccess"
+ "_logPersistedSetConfiguration:operation:forPersistedEntryID:withSetConfiguration:historyOperation:message:"
+ "STA_STARTUP_BEGINNING      "
+ "v64@0:8@16@24@32@40q48@56"
+ "SET_CONFIG_LOAD_PERSISTED  "
+ "{alreadyHaveSetDescriptorMatching} nextEntry localContent URL: %!@(MISSING), checkEntry localContent URL: %!@(MISSING)"
+ "{alreadyHaveSetDescriptorMatching} skipping set-descriptor because it's staged. Descriptor: %!{(MISSING)public}@"
+ "SET_CONFIG_LATEST_VEND_SET "
+ "{%!@(MISSING)} empty set-descriptor | setDescriptor:%!@(MISSING)"
+ "{%!@(MISSING)} atomic-instance entry no longer on the filesystem | nextAtomicEntry:%!@(MISSING)| setDescriptor:%!@(MISSING)"
+ "{%!{(MISSING)public}@}\n[LATEST-TO-VEND] [NO_CHANGE] atomic-instance entry requiring personalization | nextAtomicEntry:%!{(MISSING)public}@ | setDescriptor:%!{(MISSING)public}@"
+ "{%!{(MISSING)public}@}: %!@(MISSING) adopt as latest. jobAtomicInstance: %!@(MISSING)"
+ "_becameLatestToVend"
+ "%!{(MISSING)public}@ {%!{(MISSING)public}@:rebuildLastestOnFS} latest version on filesystem | assetVersion:%!{(MISSING)public}@, for assetSpecifier:%!{(MISSING)public}@,"
+ "%!{(MISSING)public}@ {%!{(MISSING)public}@:rebuildLastestOnFS} latest downloaded descriptor is not really on filesystem. Not adding to latestAssetDescriptorOnFilesystemBySpecifier list. Descriptor :%!{(MISSING)public}@,"
+ "SET_CONFIG_LOAD_SET_TARGET "
+ "{%!@(MISSING)} duplicate nextAtomicEntry ignored | nextAtomicEntry:%!@(MISSING) | setInfoInstance:%!@(MISSING)"
+ "SET_CONFIG_LATEST_VEND_CLR "
+ "{loadPersistedCrossCheckTrimSetDescriptors} [DROP-SET-DESCRIPTOR] set-descriptor not vended when other being vended | nextSetDescriptorToDrop:%!{(MISSING)public}@"
+ "{persistSetJobDescriptor}: found existing-atomic instance representing assets in job descriptor: %!{(MISSING)public}@"
+ "Starting built-in MobileAsset brain built Sep 17 2024 17:06:24"
+ "VLD_LOAD_LOCAL_URL_PRESENT "
+ "persistSetDescriptorDownloadedJob:fromLocation:"
+ "v68@0:8@16@24@32@40q48B56@60"
+ "isAtomicEntry:alreadyInAtomicEntries:"
+ "setDescriptorDedupDownloadedEntries:forSetDescriptor:"
+ "jobDescriptorOnFilesystemConfirmed:"
+ "{%!@(MISSING):setAtomicEntriesRemoveDuplicates} atomic-entries needed dedup | dropped selectorKey:%!@(MISSING)"
+ "{alreadyHaveSetDescriptorMatching} Set atomic entries with identical asset type, specifier and version has different paths on the filesystem. foundEntry: %!@(MISSING), persistedEntry:%!@(MISSING)"
+ "2.2.17"
+ "%!{(MISSING)public}@ | {refreshDownloadedToManager} set-job just became set-configuration's latest-to-vend"
+ "Starting downloaded MobileAsset brain (version: %!@(MISSING)) built Sep 17 2024 17:06:24"
+ "%!{(MISSING)public}@ {%!{(MISSING)public}@:requestDownloadManagerCatalogLookup} downloaded descriptor is not really on filesystem. Not adding to latestAssetDescriptorOnFilesystemBySpecifier list. Descriptor: %!{(MISSING)public}@"
+ "setTryPersonalizeSuccess:"
+ "Should"
+ "QUIET_OPERATION            "
+ "_tryPersonalizeSuccess"
+ "{%!@(MISSING)} Latest-to-vend for set %!@(MISSING), %!@(MISSING), has atomic entries that are missing from filesystem.  Missing atomic entry: %!@(MISSING). "
+ "{%!{(MISSING)public}@}\n[LATEST-TO-VEND] [NO_CHANGE] no asset-versions are available to the client | setDescriptor:%!{(MISSING)public}@"
+ "TB,N,V_becameLatestToVend"
+ "setDescriptorVerifyNoDuplicates:"
+ "{%!{(MISSING)public}@}\n[LATEST-TO-VEND] not setting latestAtomicInstanceToVend (requiresPersonalization) | setJobDescriptor:%!{(MISSING)public}@"
+ "[%!{(MISSING)public}@] {loadPersistedSetDownloadedDescriptors}\n[SELF-HEAL] deduped setDescriptor:%!{(MISSING)public}@"
+ "{%!@(MISSING):newSetDescriptorFromAlreadyDownloaded} duplicate nextAtomicEntry ignored | nextAtomicEntry:%!@(MISSING) | setInfoInstance:%!@(MISSING), newSetDescriptor:%!@(MISSING)"
+ "SET_CONFIG_IMPLIED_REQUEST "
+ "SET_CONFIG_CHANGED         "
+ "{%!@(MISSING)} about to adopt as latest-to-vend yet not on filesystem | setJobDescriptor:%!@(MISSING)"
+ "{IssueClientReplySetJob}\n[LATEST-TO-VEND] same version found when no previous latestAtomicInstanceToVend | setConfiguration:%!{(MISSING)public}@"
+ "{setDescriptorVerifyNoDuplicates} set-descriptor has not yet been deduped | setDescriptor:%!@(MISSING)"
- "%!{(MISSING)public}@ {%!{(MISSING)public}@:isSetFoundAlreadyOnFilesystem} latest version on filesystem | assetVersion:%!{(MISSING)public}@, for assetSpecifier:%!{(MISSING)public}@,"
- "persistSetDescriptorDownloadedJob:fromLocation:issuingDownloadedNotification:"
- "{%!@(MISSING)} atomic-instance entry no longer on the filesystem  | nextAtomicEntry:%!@(MISSING)| setDescriptor:%!@(MISSING)"
- "v84@0:8@16@24B32@36@44B52B56B60B64q68@76"
- "{%!@(MISSING)} set-job current-set-status does not include latestDowloadedEntries | downloadedAtomicInstance:%!@(MISSING) | latestDowloadedEntries:%!l(MISSING)d | setJobDescriptor:%!@(MISSING) | currentSetStatus:%!@(MISSING)"
- "v60@0:8@16@24@32@40B48@52"
- "Starting built-in MobileAsset brain built Sep 12 2024 18:31:55"
- "[%!{(MISSING)public}@] {%!{(MISSING)public}@} persist of set-descriptor that has previously issued atomic-instance downloaded notification | setJobDescriptor:%!{(MISSING)public}@"
- "_logPersistedSetConfiguration:operation:forPersistedEntryID:withSetConfiguration:recordingSpecifiers:message:"
- "2.2.14"
- "Starting downloaded MobileAsset brain (version: %!@(MISSING)) built Sep 12 2024 18:31:55"
- "_logPersistedSetConfiguration:operation:forPersistedEntryID:withSetConfiguration:message:"
- "{%!{(MISSING)public}@}\n[LATEST-TO-VEND] atomic-instance entry requiring personalization | nextAtomicEntry:%!{(MISSING)public}@ | setDescriptor:%!{(MISSING)public}@"
- "{persistSetJobDescriptor}: found existing-atomic instance represending assets in job descriptor: %!{(MISSING)public}@"
- "{%!{(MISSING)public}@}\n[LATEST-TO-VEND] unable to replace latestAtomicInstanceToVend (unable to fully personalize) | setConfiguration:%!{(MISSING)public}@"
- "{%!{(MISSING)public}@}\n[LATEST-TO-VEND] no asset-versions are available to the client | setDescriptor:%!{(MISSING)public}@"

```
