## FileProviderDaemon

> `/System/Library/PrivateFrameworks/FileProviderDaemon.framework/Versions/A/FileProviderDaemon`

```diff

-2727.0.0.0.0
-  __TEXT.__text: 0xe45fc
+2732.0.26.0.0
+  __TEXT.__text: 0xe4e4c
   __TEXT.__auth_stubs: 0x1240
-  __TEXT.__objc_methlist: 0x5438
+  __TEXT.__objc_methlist: 0x5458
   __TEXT.__const: 0x1e0
-  __TEXT.__cstring: 0xd036
-  __TEXT.__oslogstring: 0xda65
-  __TEXT.__gcc_except_tab: 0xd704
+  __TEXT.__cstring: 0xd128
+  __TEXT.__oslogstring: 0xda01
+  __TEXT.__gcc_except_tab: 0xd80c
   __TEXT.__ustring: 0x184c
   __TEXT.__dlopen_cstrs: 0x50
-  __TEXT.__unwind_info: 0x3a80
-  __TEXT.__objc_classname: 0xa1c
-  __TEXT.__objc_methname: 0x151cd
-  __TEXT.__objc_methtype: 0x5496
-  __TEXT.__objc_stubs: 0xdc00
+  __TEXT.__unwind_info: 0x3a98
+  __TEXT.__objc_classname: 0xa1d
+  __TEXT.__objc_methname: 0x15259
+  __TEXT.__objc_methtype: 0x550a
+  __TEXT.__objc_stubs: 0xdc60
   __DATA_CONST.__got: 0x8c8
   __DATA_CONST.__const: 0x3a0
   __DATA_CONST.__objc_classlist: 0x268
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x41b8
+  __DATA_CONST.__objc_selrefs: 0x41d8
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x200
   __DATA_CONST.__objc_arraydata: 0xf0
   __AUTH_CONST.__auth_got: 0x930
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x42d0
-  __AUTH_CONST.__cfstring: 0x5b00
-  __AUTH_CONST.__objc_const: 0x12058
+  __AUTH_CONST.__cfstring: 0x5b40
+  __AUTH_CONST.__objc_const: 0x120d8
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH.__objc_data: 0x11d0
-  __DATA.__objc_ivar: 0x938
+  __DATA.__objc_ivar: 0x93c
   __DATA.__data: 0xdb0
   __DATA.__bss: 0x218
   __DATA_DIRTY.__objc_data: 0x640

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprequelite.dylib
-  Functions: 3612
-  Symbols:   8833
-  CStrings:  1213
+  Functions: 3615
+  Symbols:   8843
+  CStrings:  1218
 
Symbols:
+ -[FPDDomain accumulatedSizeOfItems]
+ -[FPDSharedScheduler initWithLabel:options:criteria:]
+ -[FPDSharedScheduler initWithLabel:options:criteriaBuilder:]
+ -[FPDVolume _computeSystemDirectoryForRole:]
+ -[FPDVolume _computeSystemDirectoryForRole:].cold.1
+ -[FPDVolume _computeSystemDirectoryForRole:].cold.2
+ -[FPDVolume _computeSystemDirectoryForRole:].cold.3
+ -[FPDXPCServicer accumulatedSizeOfItemsInDomain:completion:]
+ -[FPDXPCServicer createDomainServicerForProviderDomainID:provider:enumerateEntitlementRequired:error:]
+ -[FPDXPCServicer startAccessingServiceWithName:itemID:domain:connection:enumerateEntitlementRequired:completionHandler:]
+ GCC_except_table174
+ GCC_except_table187
+ GCC_except_table245
+ GCC_except_table248
+ GCC_except_table252
+ GCC_except_table255
+ GCC_except_table259
+ GCC_except_table260
+ GCC_except_table263
+ GCC_except_table270
+ GCC_except_table273
+ GCC_except_table276
+ GCC_except_table281
+ GCC_except_table288
+ GCC_except_table293
+ GCC_except_table294
+ GCC_except_table299
+ GCC_except_table348
+ GCC_except_table351
+ GCC_except_table355
+ GCC_except_table362
+ GCC_except_table363
+ GCC_except_table384
+ GCC_except_table385
+ GCC_except_table390
+ GCC_except_table393
+ GCC_except_table396
+ GCC_except_table399
+ GCC_except_table402
+ GCC_except_table409
+ GCC_except_table410
+ GCC_except_table415
+ GCC_except_table416
+ GCC_except_table423
+ GCC_except_table426
+ GCC_except_table427
+ GCC_except_table437
+ GCC_except_table442
+ GCC_except_table455
+ GCC_except_table463
+ GCC_except_table464
+ GCC_except_table91
+ OBJC_IVAR_$_FPDSharedScheduler._options
+ OBJC_IVAR_$_FPDVolume._systemDirectory
+ __109-[FPDProvider dumpAllDomains:domains:auditToken:request:providerFilter:limitNumberOfItems:completionHandler:]_block_invoke.265
+ __120-[FPDXPCServicer startAccessingServiceWithName:itemID:domain:connection:enumerateEntitlementRequired:completionHandler:]_block_invoke.94
+ __120-[FPDXPCServicer startAccessingServiceWithName:itemID:domain:connection:enumerateEntitlementRequired:completionHandler:]_block_invoke.94.cold.1
+ __120-[FPDXPCServicer startAccessingServiceWithName:itemID:domain:connection:enumerateEntitlementRequired:completionHandler:]_block_invoke.cold.1
+ __40-[FPDProvider materializeRootForDomain:]_block_invoke.96
+ __98-[FPDProvider dumpStateTo:auditToken:request:providerFilter:limitNumberOfItems:completionHandler:]_block_invoke.320
+ __98-[FPDProvider dumpStateTo:auditToken:request:providerFilter:limitNumberOfItems:completionHandler:]_block_invoke.327
+ ___120-[FPDXPCServicer startAccessingServiceWithName:itemID:domain:connection:enumerateEntitlementRequired:completionHandler:]_block_invoke
+ ___53-[FPDSharedScheduler initWithLabel:options:criteria:]_block_invoke
+ ___60-[FPDSharedScheduler initWithLabel:options:criteriaBuilder:]_block_invoke
+ ___60-[FPDXPCServicer accumulatedSizeOfItemsInDomain:completion:]_block_invoke
+ __block_literal_global.721
+ __block_literal_global.724
+ _objc_msgSend$_computeSystemDirectoryForRole:
+ _objc_msgSend$accumulatedSizeOfItems
+ _objc_msgSend$createDomainServicerForProviderDomainID:provider:enumerateEntitlementRequired:error:
+ _objc_msgSend$initWithLabel:options:criteria:
+ _objc_msgSend$initWithLabel:options:criteriaBuilder:
+ _objc_msgSend$startAccessingServiceWithName:itemID:domain:connection:enumerateEntitlementRequired:completionHandler:
+ _objc_msgSend$uid
- -[FPDSharedScheduler initWithLabel:forceCriteria:criteria:]
- -[FPDSharedScheduler initWithLabel:forceCriteria:criteriaBuilder:]
- -[FPDVolume systemDirectory].cold.1
- -[FPDVolume systemDirectory].cold.2
- -[FPDXPCServicer createDomainServicerForProviderDomainID:enumerateEntitlementRequired:error:]
- -[FPDXPCServicer startAccessingServiceWithName:itemID:connection:enumerateEntitlementRequired:completionHandler:]
- GCC_except_table128
- GCC_except_table175
- GCC_except_table188
- GCC_except_table249
- GCC_except_table250
- GCC_except_table256
- GCC_except_table257
- GCC_except_table261
- GCC_except_table262
- GCC_except_table265
- GCC_except_table274
- GCC_except_table277
- GCC_except_table278
- GCC_except_table283
- GCC_except_table290
- GCC_except_table297
- GCC_except_table301
- GCC_except_table304
- GCC_except_table350
- GCC_except_table353
- GCC_except_table357
- GCC_except_table379
- GCC_except_table382
- GCC_except_table386
- GCC_except_table389
- GCC_except_table392
- GCC_except_table397
- GCC_except_table400
- GCC_except_table401
- GCC_except_table408
- GCC_except_table411
- GCC_except_table412
- GCC_except_table421
- GCC_except_table422
- GCC_except_table425
- GCC_except_table435
- GCC_except_table436
- GCC_except_table451
- GCC_except_table456
- GCC_except_table459
- OBJC_IVAR_$_FPDSharedScheduler._forceCriteria
- __109-[FPDProvider dumpAllDomains:domains:auditToken:request:providerFilter:limitNumberOfItems:completionHandler:]_block_invoke.263
- __113-[FPDXPCServicer startAccessingServiceWithName:itemID:connection:enumerateEntitlementRequired:completionHandler:]_block_invoke.94
- __113-[FPDXPCServicer startAccessingServiceWithName:itemID:connection:enumerateEntitlementRequired:completionHandler:]_block_invoke.94.cold.1
- __113-[FPDXPCServicer startAccessingServiceWithName:itemID:connection:enumerateEntitlementRequired:completionHandler:]_block_invoke.cold.1
- __40-[FPDProvider materializeRootForDomain:]_block_invoke.90
- __40-[FPDProvider materializeRootForDomain:]_block_invoke.94
- __98-[FPDProvider dumpStateTo:auditToken:request:providerFilter:limitNumberOfItems:completionHandler:]_block_invoke.318
- __98-[FPDProvider dumpStateTo:auditToken:request:providerFilter:limitNumberOfItems:completionHandler:]_block_invoke.325
- ___113-[FPDXPCServicer startAccessingServiceWithName:itemID:connection:enumerateEntitlementRequired:completionHandler:]_block_invoke
- ___59-[FPDSharedScheduler initWithLabel:forceCriteria:criteria:]_block_invoke
- ___66-[FPDSharedScheduler initWithLabel:forceCriteria:criteriaBuilder:]_block_invoke
- __block_literal_global.719
- __block_literal_global.722
- _objc_msgSend$createDomainServicerForProviderDomainID:enumerateEntitlementRequired:error:
- _objc_msgSend$initWithLabel:forceCriteria:criteria:
- _objc_msgSend$initWithLabel:forceCriteria:criteriaBuilder:
- _objc_msgSend$startAccessingServiceWithName:itemID:connection:enumerateEntitlementRequired:completionHandler:
CStrings:
+ "-[FPDVolume _computeSystemDirectoryForRole:]"
+ "-[FPDXPCServicer accumulatedSizeOfItemsInDomain:completion:]"
+ "-[FPDXPCServicer accumulatedSizeOfItemsInDomain:completion:]_block_invoke"
+ "-[FPDXPCServicer startAccessingServiceWithName:itemID:domain:connection:enumerateEntitlementRequired:completionHandler:]_block_invoke"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FileProvider_executables/app-library/FPDFetchAppLibraryIconOperation.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FileProvider_executables/fileproviderd/FPDAccessRight.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FileProvider_executables/fileproviderd/FPDDomain.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FileProvider_executables/fileproviderd/FPDDomainExtensionBackend.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FileProvider_executables/fileproviderd/FPDDomainIndexer/FPDDomainIndexer.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FileProvider_executables/fileproviderd/FPDExtensionManager.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FileProvider_executables/fileproviderd/FPDExtensionRequestRecord.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FileProvider_executables/fileproviderd/FPDExtensionSession.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FileProvider_executables/fileproviderd/FPDFilePresenter.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FileProvider_executables/fileproviderd/FPDKnownFolderAlertPresenter.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FileProvider_executables/fileproviderd/FPDProcessMonitor.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FileProvider_executables/fileproviderd/FPDProvider.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FileProvider_executables/fileproviderd/FPDPushConnection.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FileProvider_executables/fileproviderd/FPDSharedScheduler.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FileProvider_executables/fileproviderd/FPDVolume.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FileProvider_executables/fileproviderd/FPDVolumeManager.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FileProvider_executables/fileproviderd/FPDXPCServicer.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FileProvider_executables/fileproviderd/action operation engine/FPActionOperationLocator+Daemon.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FileProvider_executables/fileproviderd/action operation engine/FPDActionOperation.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FileProvider_executables/fileproviderd/action operation engine/FPDActionOperationEngine.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FileProvider_executables/fileproviderd/action operation engine/FPDItemIterator.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FileProvider_executables/fileproviderd/action operation engine/FPDIterator.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FileProvider_executables/fileproviderd/action operation engine/download/FPDDownloadManager.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FileProvider_executables/fileproviderd/action operation engine/move/FPDMoveReader.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FileProvider_executables/fileproviderd/action operation engine/move/FPDMoveWriter.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FileProvider_executables/fileproviderd/action operation engine/move/FPDMoveWriterToProvider.m"
+ "root"
+ "unexpected persona %!@(MISSING) (%!i(MISSING)) instead of expected %!@(MISSING)"
- "-[FPDXPCServicer startAccessingServiceWithName:itemID:connection:enumerateEntitlementRequired:completionHandler:]_block_invoke"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FileProvider_executables/app-library/FPDFetchAppLibraryIconOperation.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FileProvider_executables/fileproviderd/FPDAccessRight.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FileProvider_executables/fileproviderd/FPDDomain.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FileProvider_executables/fileproviderd/FPDDomainExtensionBackend.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FileProvider_executables/fileproviderd/FPDDomainIndexer/FPDDomainIndexer.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FileProvider_executables/fileproviderd/FPDExtensionManager.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FileProvider_executables/fileproviderd/FPDExtensionRequestRecord.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FileProvider_executables/fileproviderd/FPDExtensionSession.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FileProvider_executables/fileproviderd/FPDFilePresenter.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FileProvider_executables/fileproviderd/FPDKnownFolderAlertPresenter.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FileProvider_executables/fileproviderd/FPDProcessMonitor.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FileProvider_executables/fileproviderd/FPDProvider.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FileProvider_executables/fileproviderd/FPDPushConnection.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FileProvider_executables/fileproviderd/FPDSharedScheduler.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FileProvider_executables/fileproviderd/FPDVolume.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FileProvider_executables/fileproviderd/FPDVolumeManager.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FileProvider_executables/fileproviderd/FPDXPCServicer.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FileProvider_executables/fileproviderd/action operation engine/FPActionOperationLocator+Daemon.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FileProvider_executables/fileproviderd/action operation engine/FPDActionOperation.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FileProvider_executables/fileproviderd/action operation engine/FPDActionOperationEngine.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FileProvider_executables/fileproviderd/action operation engine/FPDItemIterator.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FileProvider_executables/fileproviderd/action operation engine/FPDIterator.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FileProvider_executables/fileproviderd/action operation engine/download/FPDDownloadManager.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FileProvider_executables/fileproviderd/action operation engine/move/FPDMoveReader.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FileProvider_executables/fileproviderd/action operation engine/move/FPDMoveWriter.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FileProvider_executables/fileproviderd/action operation engine/move/FPDMoveWriterToProvider.m"

```
