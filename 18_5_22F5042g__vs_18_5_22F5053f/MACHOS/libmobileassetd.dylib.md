## libmobileassetd.dylib

> `/usr/lib/libmobileassetd.dylib`

```diff

-1487.120.46.0.0
-  __TEXT.__text: 0x27804c
+1487.120.52.0.0
+  __TEXT.__text: 0x278c0c
   __TEXT.__auth_stubs: 0x2430
-  __TEXT.__objc_stubs: 0x22800
-  __TEXT.__objc_methlist: 0x10514
+  __TEXT.__objc_stubs: 0x22860
+  __TEXT.__objc_methlist: 0x10534
   __TEXT.__const: 0x489e
-  __TEXT.__cstring: 0x37cec
-  __TEXT.__objc_methname: 0x3db35
+  __TEXT.__cstring: 0x37e0c
+  __TEXT.__objc_methname: 0x3dbb2
   __TEXT.__objc_classname: 0xe6d
   __TEXT.__objc_methtype: 0x3ba8
-  __TEXT.__oslogstring: 0x4c8a1
-  __TEXT.__gcc_except_tab: 0x3014
+  __TEXT.__oslogstring: 0x4cb41
+  __TEXT.__gcc_except_tab: 0x3030
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__swift5_typeref: 0x1093
   __TEXT.__constg_swiftt: 0x14fc

   __DATA_CONST.__got: 0x680
   __DATA_CONST.__auth_ptr: 0xa20
   __DATA_CONST.__const: 0x6828
-  __DATA_CONST.__cfstring: 0x2bb20
+  __DATA_CONST.__cfstring: 0x2bbe0
   __DATA_CONST.__objc_classlist: 0x3f0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x98f0
+  __DATA_CONST.__objc_selrefs: 0x9908
   __DATA_CONST.__objc_arraydata: 0xb98
   __DATA_CONST.__objc_arrayobj: 0x270
   __DATA_CONST.__objc_intobj: 0x570
   __DATA_CONST.__objc_dictobj: 0x118
   __DATA.__objc_const: 0x15120
   __DATA.__objc_protorefs: 0x18
-  __DATA.__objc_classrefs: 0x800
+  __DATA.__objc_classrefs: 0x808
   __DATA.__objc_superrefs: 0x2f0
   __DATA.__objc_ivar: 0x13f0
   __DATA.__objc_data: 0xdb0

   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
   - /System/Library/PrivateFrameworks/MobileAssetExclaveServices.framework/MobileAssetExclaveServices
+  - /System/Library/PrivateFrameworks/MobileInBoxUpdate.framework/MobileInBoxUpdate
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 8359
-  Symbols:   15440
-  CStrings:  16807
+  Functions: 8361
+  Symbols:   15446
+  CStrings:  16823
 
Symbols:
+ -[DownloadManager getBaseURLOverrideForAssetType:]
+ -[MADAutoAssetControlManager atomicInstanceUUIDForNewSetJob:forReason:]
+ -[MADAutoAssetControlManager isAtomicEntry:desiredForAutoAssetSetEntries:]
+ -[MADAutoAssetJob rebuildLastestDescriptorsOnFilesystem:]
+ GCC_except_table136
+ GCC_except_table143
+ GCC_except_table176
+ GCC_except_table257
+ GCC_except_table421
+ GCC_except_table610
+ GCC_except_table612
+ GCC_except_table618
+ GCC_except_table620
+ GCC_except_table634
+ GCC_except_table767
+ _OBJC_CLASS_$_MIBUClient
+ __110-[DownloadManager pallasRequestV2:normalizedType:withPurpose:options:using:with:autoAssetJob:clientName:then:]_block_invoke.2134
+ __149-[DownloadManager registerCatalogDownloadJob:withPurpose:usingDownloadOptions:usingXPCConnection:withXPCMessage:performingAutoAssetJob:asClientName:]_block_invoke.2311
+ __184-[DownloadManager startDownloadAndUpdateState:for:startingAt:withLength:extractWith:modified:options:downloadSize:using:with:clientName:autoAssetJob:ofJobType:notify:spaceCheckedUUID:]_block_invoke.2245
+ __184-[DownloadManager startDownloadAndUpdateState:for:startingAt:withLength:extractWith:modified:options:downloadSize:using:with:clientName:autoAssetJob:ofJobType:notify:spaceCheckedUUID:]_block_invoke.2257
+ __287-[DownloadManager registerAssetDownloadJob:withPurpose:usingDownloadOptions:forAssetId:withBase:relativeTo:startingAt:withLength:extractWith:allocateExtractorIfNecessary:usingXPCConnection:withXPCMessage:clientName:performingAutoAssetJob:notify:withCatalogMetadata:withSpaceCheckedUUID:]_block_invoke.2292
+ __37-[DownloadManager startDownloadTimer]_block_invoke.1720
+ __47-[DownloadManager getCurrentInflightDownloads:]_block_invoke.2189
+ __47-[DownloadManager getCurrentInflightDownloads:]_block_invoke.2190
+ __51-[DownloadManager queryNSUrlSessiondAndUpdateState]_block_invoke.1875
+ __51-[DownloadManager queryNSUrlSessiondAndUpdateState]_block_invoke.1876
+ __51-[DownloadManager queryNSUrlSessiondAndUpdateState]_block_invoke.1882
+ __52-[DownloadManager reportDownloadAttemptResult:with:]_block_invoke.1836
+ __94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke.3313
+ __94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke_2.3314
+ __block_literal_global.1123
+ __block_literal_global.1578
+ __block_literal_global.1617
+ __block_literal_global.2048
+ __block_literal_global.2070
+ __block_literal_global.2231
+ __block_literal_global.2240
+ __block_literal_global.2338
+ __block_literal_global.2366
+ __block_literal_global.2368
+ __block_literal_global.3973
+ __block_literal_global.4996
+ _objc_msgSend$atomicInstanceUUIDForNewSetJob:forReason:
+ _objc_msgSend$getBaseURLOverrideForAssetType:
+ _objc_msgSend$isAtomicEntry:desiredForAutoAssetSetEntries:
+ _objc_msgSend$isInBoxUpdateMode:
+ _objc_msgSend$rebuildLastestDescriptorsOnFilesystem:
- -[MADAutoAssetControlManager atomicInstanceUUIDForNewSetJob:]
- -[MADAutoAssetJob rebuildLastestOnFS:]
- GCC_except_table135
- GCC_except_table142
- GCC_except_table175
- GCC_except_table256
- GCC_except_table420
- GCC_except_table609
- GCC_except_table611
- GCC_except_table617
- GCC_except_table619
- GCC_except_table633
- GCC_except_table766
- __110-[DownloadManager pallasRequestV2:normalizedType:withPurpose:options:using:with:autoAssetJob:clientName:then:]_block_invoke.2119
- __149-[DownloadManager registerCatalogDownloadJob:withPurpose:usingDownloadOptions:usingXPCConnection:withXPCMessage:performingAutoAssetJob:asClientName:]_block_invoke.2292
- __184-[DownloadManager startDownloadAndUpdateState:for:startingAt:withLength:extractWith:modified:options:downloadSize:using:with:clientName:autoAssetJob:ofJobType:notify:spaceCheckedUUID:]_block_invoke.2230
- __184-[DownloadManager startDownloadAndUpdateState:for:startingAt:withLength:extractWith:modified:options:downloadSize:using:with:clientName:autoAssetJob:ofJobType:notify:spaceCheckedUUID:]_block_invoke.2242
- __287-[DownloadManager registerAssetDownloadJob:withPurpose:usingDownloadOptions:forAssetId:withBase:relativeTo:startingAt:withLength:extractWith:allocateExtractorIfNecessary:usingXPCConnection:withXPCMessage:clientName:performingAutoAssetJob:notify:withCatalogMetadata:withSpaceCheckedUUID:]_block_invoke.2273
- __37-[DownloadManager startDownloadTimer]_block_invoke.1702
- __47-[DownloadManager getCurrentInflightDownloads:]_block_invoke.2174
- __47-[DownloadManager getCurrentInflightDownloads:]_block_invoke.2175
- __51-[DownloadManager queryNSUrlSessiondAndUpdateState]_block_invoke.1857
- __51-[DownloadManager queryNSUrlSessiondAndUpdateState]_block_invoke.1858
- __51-[DownloadManager queryNSUrlSessiondAndUpdateState]_block_invoke.1864
- __52-[DownloadManager reportDownloadAttemptResult:with:]_block_invoke.1818
- __94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke.3307
- __94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke_2.3308
- __block_literal_global.1105
- __block_literal_global.1560
- __block_literal_global.1599
- __block_literal_global.2033
- __block_literal_global.2055
- __block_literal_global.2216
- __block_literal_global.2225
- __block_literal_global.2319
- __block_literal_global.2347
- __block_literal_global.2349
- __block_literal_global.3967
- __block_literal_global.4987
- _objc_msgSend$atomicInstanceUUIDForNewSetJob:
- _objc_msgSend$rebuildLastestOnFS:
CStrings:
+ "%@:rebuildLastestDescriptorsOnFilesystem"
+ "%@:requestDownloadManagerCatalogLookup"
+ "%{public}@ {%{public}@}\n[BUILD-DESCRIPTORS] cleared latestAssetDescriptorOnFilesystemBySpecifier"
+ "%{public}@ {%{public}@}\n[BUILD-DESCRIPTORS] downloaded descriptor is not really on the filesystem - not adding to latestAssetDescriptorOnFilesystemBySpecifier list | latestDownloadedDescriptor:%{public}@"
+ "%{public}@ {%{public}@}\n[BUILD-DESCRIPTORS] latest downloaded descriptor is not really on the filesystem - not adding to latestAssetDescriptorOnFilesystemBySpecifier list | latestDownloadedDescriptor:%{public}@,"
+ "%{public}@ {%{public}@}\n[BUILD-DESCRIPTORS] latest version on filesystem | assetSpecifier:%{public}@ | assetVersion:%{public}@"
+ "%{public}@ {%{public}@} | SIMULATE_OPERATION(%lld) | call to registerCatalogDownloadJob postponed"
+ "%{public}@ {%{public}@} | SIMULATE_OPERATION(%{public}@) | call to registerCatalogDownloadJob postponed"
+ "Starting built-in MobileAsset brain built Apr  7 2025 02:53:10"
+ "Starting downloaded MobileAsset brain (version: %@) built Apr  7 2025 02:53:10"
+ "Using Knox url from asset to construct asset download URL: %{public}@"
+ "Using base url from request to construct asset download URL: %{public}@"
+ "Using baseURL from supplied override to construct asset download URL: %{public}@"
+ "[BaseURLOverride]: Failed to determine inBoxUpdateMode: %{public}@"
+ "[BaseURLOverride]: Final baseURLOverride for asset(%@) is %@"
+ "[BaseURLOverride]: Running in inBoxUpdateMode."
+ "[BaseURLOverride]: Using baseURLOverride from asset specific default(%{public}@) for asset(%{public}@)"
+ "[BaseURLOverride]: Using baseURLOverride from global default(%{public}@) for asset(%{public}@)"
+ "[BaseURLOverride]: Using inBoxUpdaterServer URL for asset(%{public}@)"
+ "atomicInstanceUUIDForNewSetJob(%@)"
+ "atomicInstanceUUIDForNewSetJob:forReason:"
+ "getBaseURLOverrideForAssetType:"
+ "http://localhost:8080"
+ "isAtomicEntry:desiredForAutoAssetSetEntries:"
+ "isInBoxUpdateMode:"
+ "rebuildLastestDescriptorsOnFilesystem:"
+ "{%{public}@} (%{public}@)\n[SET-DECIDE-FOUND] considering potential descriptors | potentialDescriptorCount:%lu,alreadyOnFilesystem:%{public}@"
+ "{%{public}@} (%{public}@)\n[SET-DECIDE-FOUND] set-catalog lookup summary | catalogCount:%lu | patchDescriptorCount:%lu | fullDescriptorCount:%lu"
+ "{AUTO-LOOKUP-CACHE[%{public}@]:cachedLookupResultForSelector} | lookup-cache non-pallas disabled | selector:%{public}@"
+ "{AUTO-LOOKUP-CACHE[%{public}@]:recordLookupResult:forSelector:} | auto-asset-lookup-cache non-pallas disabled | selector:%{public}@"
+ "{AUTO-LOOKUP-CACHE[%{public}@]:recordLookupResult:forSetConfiguration:} | by-set-configuration non-pallas disabled | selector:%{public}@"
+ "{isAtomicEntry:desiredForAutoAssetSetEntries} nil atomic-entry provided"
+ "{isAtomicEntry:desiredForAutoAssetSetEntries} nil auto-asset-set-entries provided"
- "%{public}@ {%{public}@:rebuildLastestOnFS} latest downloaded descriptor is not really on filesystem. Not adding to latestAssetDescriptorOnFilesystemBySpecifier list. Descriptor :%{public}@,"
- "%{public}@ {%{public}@:rebuildLastestOnFS} latest version on filesystem | assetVersion:%{public}@, for assetSpecifier:%{public}@,"
- "%{public}@ {%{public}@:requestDownloadManagerCatalogLookup} downloaded descriptor is not really on filesystem. Not adding to latestAssetDescriptorOnFilesystemBySpecifier list. Descriptor: %{public}@"
- "%{public}@ {%{public}@:requestDownloadManagerCatalogLookup} latest version on filesystem | assetVersion:%{public}@, for assetSpecifier:%{public}@,"
- "%{public}@ {%{public}@:requestDownloadManagerCatalogLookup} | SIMULATE_OPERATION(%lld) | call to registerCatalogDownloadJob postponed"
- "%{public}@ {%{public}@:requestDownloadManagerCatalogLookup} | SIMULATE_OPERATION(%{public}@) | call to registerCatalogDownloadJob postponed"
- "Starting built-in MobileAsset brain built Mar 22 2025 02:19:22"
- "Starting downloaded MobileAsset brain (version: %@) built Mar 22 2025 02:19:22"
- "Using Knox url from asset: %{public}@"
- "Using base url from default: %{public}@"
- "Using base url from request: %{public}@"
- "Using value set in asset specific default(%@) for baseURL(%@)"
- "Using value set in global default(%@) for baseURL(%@) for asset %@"
- "atomicInstanceUUIDForNewSetJob:"
- "rebuildLastestOnFS:"
- "{%{public}@} (%{public}@)\n[SET-DECIDE-FOUND] considering potential descriptors | potentialDescriptorCount:%{public}lu,alreadyOnFilesystem:%{public}@"
- "{{public}@} (%{public}@)\n[SET-DECIDE-FOUND] set-catalog lookup summary: %{public}@:catalogCount:%{public}lu,patchDescriptorCount:%{public}lu,fullDescriptorCount:%{public}lu"

```
