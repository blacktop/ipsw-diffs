## FileProviderDaemon

> `/System/Library/PrivateFrameworks/FileProviderDaemon.framework/FileProviderDaemon`

```diff

-1681.0.14.0.0
-  __TEXT.__text: 0xb7bd4
-  __TEXT.__auth_stubs: 0x1070
-  __TEXT.__objc_methlist: 0x49a4
-  __TEXT.__cstring: 0xab8a
-  __TEXT.__oslogstring: 0xbf7d
+1703.42.2.0.0
+  __TEXT.__text: 0xb80b8
+  __TEXT.__auth_stubs: 0x1090
+  __TEXT.__objc_methlist: 0x49c4
+  __TEXT.__cstring: 0xab86
+  __TEXT.__oslogstring: 0xc0aa
   __TEXT.__const: 0xc8
-  __TEXT.__gcc_except_tab: 0xbad4
+  __TEXT.__gcc_except_tab: 0xbb08
   __TEXT.__ustring: 0x1796
   __TEXT.__dlopen_cstrs: 0x50
-  __TEXT.__unwind_info: 0x3350
+  __TEXT.__unwind_info: 0x3354
   __TEXT.__objc_classname: 0x867
-  __TEXT.__objc_methname: 0x126bb
-  __TEXT.__objc_methtype: 0x498d
-  __TEXT.__objc_stubs: 0xc7e0
-  __DATA_CONST.__got: 0x2f8
-  __DATA_CONST.__const: 0x34a8
+  __TEXT.__objc_methname: 0x127a9
+  __TEXT.__objc_methtype: 0x49c5
+  __TEXT.__objc_stubs: 0xc8a0
+  __DATA_CONST.__got: 0x2f0
+  __DATA_CONST.__const: 0x34d0
   __DATA_CONST.__objc_classlist: 0x200
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xedf0
-  __DATA_CONST.__objc_selrefs: 0x3b18
+  __DATA_CONST.__objc_const: 0xede0
+  __DATA_CONST.__objc_selrefs: 0x3b40
   __DATA_CONST.__objc_arraydata: 0xb0
-  __AUTH_CONST.__cfstring: 0x4c40
+  __AUTH_CONST.__cfstring: 0x4c00
   __AUTH_CONST.__const: 0x9a0
   __AUTH_CONST.__objc_const: 0x1778
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__auth_got: 0x848
+  __AUTH_CONST.__auth_got: 0x858
   __AUTH.__objc_data: 0x730
   __DATA.__objc_protorefs: 0x38
   __DATA.__objc_classrefs: 0x528

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprequelite.dylib
-  Functions: 3780
-  Symbols:   11966
-  CStrings:  5195
+  Functions: 3788
+  Symbols:   11988
+  CStrings:  5203
 
Symbols:
+ +[FPDFilePresenter presenter:withItemID:auditToken:urlHint:domain:]
+ -[FPDDomain _providedItemAtURL:didGainPresenterWithInfo:]
+ -[FPDDomain _providedItemAtURL:didGainPresenterWithInfo:].cold.1
+ -[FPDDomain callExtensionForItemDidChange:request:completionHandler:]
+ -[FPDDomainDeadEndBackend listRemoteVersionsOfItemAtURL:includeCachedVersions:completionHandler:]
+ -[FPDDomainExtensionBackend listRemoteVersionsOfItemAtURL:includeCachedVersions:completionHandler:]
+ -[FPDExtensionManager domainForURL:reason:]
+ -[FPDExtensionManager domainFromItemID:reason:]
+ -[FPDExtensionManager domainWithID:reason:]
+ -[FPDExtensionManager providerWithIdentifier:reason:]
+ -[FPDFileCoordinationProvider _providedItemAtURL:didGainPresenterWithInfo:]
+ -[FPDFilePresenter auditToken]
+ -[FPDFilePresenter initWithIdentifier:itemID:auditToken:urlHint:domain:]
+ -[FPDFilePresenter setAuditToken:]
+ -[FPDPresenterManager addPresenter:itemID:urlHint:auditToken:promiseID:]
+ -[FPDPresenterManager presenterWithID:]
+ -[FPDProvider domainForIdentifier:reason:]
+ -[FPDProvider domainForIdentifier:reason:].cold.1
+ -[FPDVersionsFileCoordinationProviderDelegate _providedItemAtURL:didGainPresenterWithInfo:]
+ -[FPDXPCDomainServicer domainOrNil:]
+ -[FPDXPCDomainServicer providerOrNilWithReason:]
+ -[FPDXPCServicer listRemoteVersionsOfItemAtURL:includeCachedVersions:completionHandler:]
+ -[FPDXPCServicer listRemoteVersionsOfItemAtURL:includeCachedVersions:completionHandler:].cold.1
+ -[FPDXPCServicer listRemoteVersionsOfItemAtURL:includeCachedVersions:completionHandler:].cold.2
+ -[FPDXPCServicer listRemoteVersionsOfItemAtURL:includeCachedVersions:completionHandler:].cold.3
+ -[FPDXPCServicer setAlternateContentsURL:onDocumentURL:completionHandler:].cold.7
+ _FPEntitlementValueForAuditToken
+ _FPExecutableNameForAuditToken
+ _FPFSD2DRestorePluginIsEnabled
+ _FPPassivePresenterEntitlement
+ _OBJC_IVAR_$_FPDFilePresenter._auditToken
+ _OBJC_IVAR_$_FPDFilePresenter._passivePresenterRequested
+ ___39-[FPDPresenterManager presenterWithID:]_block_invoke
+ ___40-[FPDProvider materializeRootForDomain:]_block_invoke.cold.1
+ ___55-[FPDDomain didChangeItemID:request:completionHandler:]_block_invoke_2
+ ___57-[FPDDomain _providedItemAtURL:didGainPresenterWithInfo:]_block_invoke
+ ___57-[FPDDomain _providedItemAtURL:didGainPresenterWithInfo:]_block_invoke.cold.1
+ ___59-[FPDXPCServicer appHasNonUploadedFiles:completionHandler:]_block_invoke.265
+ ___63-[FPDXPCServicer fetchDaemonOperationIDsWithCompletionHandler:]_block_invoke.318
+ ___68-[FPDXPCServicer scheduleActionOperationWithInfo:completionHandler:]_block_invoke.316
+ ___69-[FPDDomain callExtensionForItemDidChange:request:completionHandler:]_block_invoke
+ ___69-[FPDDomain callExtensionForItemDidChange:request:completionHandler:]_block_invoke.cold.1
+ ___70-[FPDXPCServicer copyDatabaseForFPCKStartingAtPath:completionHandler:]_block_invoke.308
+ ___70-[FPDXPCServicer reindexAllSearchableItemsWithAcknowledgementHandler:]_block_invoke.313
+ ___71-[FPDXPCServicer waitForStabilizationOfDomainWithID:completionHandler:]_block_invoke.312
+ ___71-[FPDXPCServicer waitForStabilizationOfDomainWithID:completionHandler:]_block_invoke.312.cold.1
+ ___72-[FPDPresenterManager addPresenter:itemID:urlHint:auditToken:promiseID:]_block_invoke
+ ___72-[FPDPresenterManager addPresenter:itemID:urlHint:auditToken:promiseID:]_block_invoke.cold.1
+ ___73-[FPDXPCServicer waitForChangesOnItemsBelowItemWithID:completionHandler:]_block_invoke.311
+ ___73-[FPDXPCServicer waitForChangesOnItemsBelowItemWithID:completionHandler:]_block_invoke.311.cold.1
+ ___74-[FPDPresenterManager noteItemBecameFrontmost:inWindow:completionHandler:]_block_invoke_3
+ ___74-[FPDXPCServicer startAccessingServiceWithName:itemURL:completionHandler:]_block_invoke.328
+ ___74-[FPDXPCServicer startAccessingServiceWithName:itemURL:completionHandler:]_block_invoke.328.cold.1
+ ___78-[FPDXPCServicer _test_callRemoveTrashedItemsOlderThanDate:completionHandler:]_block_invoke.359
+ ___78-[FPDXPCServicer _test_callRemoveTrashedItemsOlderThanDate:completionHandler:]_block_invoke.359.cold.1
+ ___82-[FPDXPCServicer dumpStateTo:limitNumberOfItems:providerFilter:completionHandler:]_block_invoke.290
+ ___82-[FPDXPCServicer fetchAndStartEnumeratingWithSettings:observer:completionHandler:]_block_invoke.335
+ ___88-[FPDXPCServicer listRemoteVersionsOfItemAtURL:includeCachedVersions:completionHandler:]_block_invoke
+ ___88-[FPDXPCServicer listRemoteVersionsOfItemAtURL:includeCachedVersions:completionHandler:]_block_invoke.227
+ ___88-[FPDXPCServicer listRemoteVersionsOfItemAtURL:includeCachedVersions:completionHandler:]_block_invoke.cold.1
+ ___92-[FPDVersionsFileCoordinationProviderDelegate _provideItemAtURL:withInfo:completionHandler:]_block_invoke.31
+ ___92-[FPDVersionsFileCoordinationProviderDelegate _provideItemAtURL:withInfo:completionHandler:]_block_invoke.31.cold.1
+ ___block_descriptor_104_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_128_e8_32s40s48s56s64s72s80s88s96s104s112bs_e55_v32?0"FPSandboxingURLWrapper"8"NSData"16"NSError"24ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s112l8s88l8s96l8s104l8
+ ___block_descriptor_56_e8_32s40s48r_e5_v8?0lr48l8s32l8s40l8
+ ___block_descriptor_96_e8_32s40s48s_e30_v24?0"FPItemID"8"NSError"16ls32l8s40l8s48l8
+ ___block_literal_global.221
+ ___block_literal_global.321
+ ___block_literal_global.655
+ ___block_literal_global.658
+ _objc_msgSend$_providedItemAtURL:didGainPresenterWithInfo:
+ _objc_msgSend$addPresenter:itemID:urlHint:auditToken:promiseID:
+ _objc_msgSend$callExtensionForItemDidChange:request:completionHandler:
+ _objc_msgSend$domainForIdentifier:reason:
+ _objc_msgSend$domainForURL:reason:
+ _objc_msgSend$domainFromItemID:reason:
+ _objc_msgSend$domainOrNil:
+ _objc_msgSend$domainWithID:reason:
+ _objc_msgSend$fp_isDatalessWithError:
+ _objc_msgSend$initWithIdentifier:itemID:auditToken:urlHint:domain:
+ _objc_msgSend$listRemoteVersionsOfItemAtURL:includeCachedVersions:completionHandler:
+ _objc_msgSend$presenter:withItemID:auditToken:urlHint:domain:
+ _objc_msgSend$presenterAuditToken
+ _objc_msgSend$presenterID
+ _objc_msgSend$presenterWithID:
+ _objc_msgSend$providerOrNilWithReason:
+ _objc_msgSend$providerWithIdentifier:reason:
+ _objc_msgSend$restoreWithCompletionHandler:
+ _objc_msgSend$scheduleFPCKRun:domainUserInfo:databasesBackupsPath:urls:options:reason:fpfs:iCDPackageDetection:completionHandler:
- +[FPDFilePresenter presenter:withItemID:pid:urlHint:domain:]
- -[FPDDomain _providedItemAtURL:didGainPresenterWithID:]
- -[FPDDomain _providedItemAtURL:didGainPresenterWithID:].cold.1
- -[FPDDomainDeadEndBackend listRemoteVersionsOfItemAtURL:completionHandler:]
- -[FPDDomainExtensionBackend listRemoteVersionsOfItemAtURL:completionHandler:]
- -[FPDExtensionManager domainForURL:]
- -[FPDExtensionManager domainFromItemID:]
- -[FPDExtensionManager domainWithID:]
- -[FPDExtensionManager providerWithIdentifier:]
- -[FPDFileCoordinationProvider _providedItemAtURL:didGainPresenterWithID:]
- -[FPDFilePresenter initWithIdentifier:itemID:pid:urlHint:domain:]
- -[FPDFilePresenter presenterPid]
- -[FPDFilePresenter setPresenterPid:]
- -[FPDPresenterManager addPresenter:itemID:urlHint:pid:promiseID:]
- -[FPDProvider domainForIdentifier:]
- -[FPDProvider domainForIdentifier:].cold.1
- -[FPDVersionsFileCoordinationProviderDelegate _providedItemAtURL:didGainPresenterWithID:]
- -[FPDXPCDomainServicer domainOrNil]
- -[FPDXPCDomainServicer providerOrNil]
- -[FPDXPCServicer listRemoteVersionsOfItemAtURL:completionHandler:]
- -[FPDXPCServicer listRemoteVersionsOfItemAtURL:completionHandler:].cold.1
- -[FPDXPCServicer listRemoteVersionsOfItemAtURL:completionHandler:].cold.2
- -[FPDXPCServicer listRemoteVersionsOfItemAtURL:completionHandler:].cold.3
- _FPLoc
- _NSDebugDescriptionErrorKey
- _NSLocalizedDescriptionKey
- _OBJC_IVAR_$_FPDFilePresenter._presenterPid
- _OBJC_IVAR_$_FPDFilePresenter._requestEffectivePID
- ___55-[FPDDomain _providedItemAtURL:didGainPresenterWithID:]_block_invoke
- ___55-[FPDDomain _providedItemAtURL:didGainPresenterWithID:]_block_invoke.cold.1
- ___55-[FPDDomain didChangeItemID:request:completionHandler:]_block_invoke.193.cold.1
- ___59-[FPDXPCServicer appHasNonUploadedFiles:completionHandler:]_block_invoke.263
- ___63-[FPDXPCServicer fetchDaemonOperationIDsWithCompletionHandler:]_block_invoke.316
- ___65-[FPDPresenterManager addPresenter:itemID:urlHint:pid:promiseID:]_block_invoke
- ___65-[FPDPresenterManager addPresenter:itemID:urlHint:pid:promiseID:]_block_invoke.cold.1
- ___66-[FPDXPCServicer listRemoteVersionsOfItemAtURL:completionHandler:]_block_invoke
- ___66-[FPDXPCServicer listRemoteVersionsOfItemAtURL:completionHandler:]_block_invoke.227
- ___66-[FPDXPCServicer listRemoteVersionsOfItemAtURL:completionHandler:]_block_invoke.cold.1
- ___68-[FPDXPCServicer scheduleActionOperationWithInfo:completionHandler:]_block_invoke.314
- ___70-[FPDXPCServicer copyDatabaseForFPCKStartingAtPath:completionHandler:]_block_invoke.306
- ___70-[FPDXPCServicer reindexAllSearchableItemsWithAcknowledgementHandler:]_block_invoke.311
- ___71-[FPDXPCServicer waitForStabilizationOfDomainWithID:completionHandler:]_block_invoke.310
- ___71-[FPDXPCServicer waitForStabilizationOfDomainWithID:completionHandler:]_block_invoke.310.cold.1
- ___73-[FPDXPCServicer waitForChangesOnItemsBelowItemWithID:completionHandler:]_block_invoke.309
- ___73-[FPDXPCServicer waitForChangesOnItemsBelowItemWithID:completionHandler:]_block_invoke.309.cold.1
- ___74-[FPDPresenterManager noteItemBecameFrontmost:inWindow:completionHandler:]_block_invoke.8
- ___74-[FPDXPCServicer startAccessingServiceWithName:itemURL:completionHandler:]_block_invoke.326
- ___74-[FPDXPCServicer startAccessingServiceWithName:itemURL:completionHandler:]_block_invoke.326.cold.1
- ___78-[FPDXPCServicer _test_callRemoveTrashedItemsOlderThanDate:completionHandler:]_block_invoke.357
- ___78-[FPDXPCServicer _test_callRemoveTrashedItemsOlderThanDate:completionHandler:]_block_invoke.357.cold.1
- ___82-[FPDXPCServicer dumpStateTo:limitNumberOfItems:providerFilter:completionHandler:]_block_invoke.288
- ___82-[FPDXPCServicer fetchAndStartEnumeratingWithSettings:observer:completionHandler:]_block_invoke.333
- ___92-[FPDVersionsFileCoordinationProviderDelegate _provideItemAtURL:withInfo:completionHandler:]_block_invoke.27.cold.1
- ___92-[FPDVersionsFileCoordinationProviderDelegate _provideItemAtURL:withInfo:completionHandler:]_block_invoke.36
- ___block_descriptor_56_e8_32s40s48s_e55_v32?0"FPSandboxingURLWrapper"8"NSData"16"NSError"24ls32l8s40l8s48l8
- ___block_descriptor_68_e8_32s40s48s_e30_v24?0"FPItemID"8"NSError"16ls32l8s40l8s48l8
- ___block_descriptor_76_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
- ___block_literal_global.220
- ___block_literal_global.319
- ___block_literal_global.653
- ___block_literal_global.656
- _objc_msgSend$_providedItemAtURL:didGainPresenterWithID:
- _objc_msgSend$addPresenter:itemID:urlHint:pid:promiseID:
- _objc_msgSend$didChangeItemID:
- _objc_msgSend$domainForIdentifier:
- _objc_msgSend$domainFromItemID:
- _objc_msgSend$domainOrNil
- _objc_msgSend$domainWithID:
- _objc_msgSend$initWithIdentifier:itemID:pid:urlHint:domain:
- _objc_msgSend$listRemoteVersionsOfItemAtURL:completionHandler:
- _objc_msgSend$presenter:withItemID:pid:urlHint:domain:
- _objc_msgSend$providerOrNil
- _objc_msgSend$providerWithIdentifier:
- _objc_msgSend$scheduleFPCKRun:databasesBackupsPath:urls:options:reason:fpfs:iCDPackageDetection:completionHandler:
CStrings:
+ "\x16\x13"
+ "-[FPDProvider domainForIdentifier:reason:]"
+ "-[FPDXPCServicer listRemoteVersionsOfItemAtURL:includeCachedVersions:completionHandler:]"
+ "-[FPDXPCServicer listRemoteVersionsOfItemAtURL:includeCachedVersions:completionHandler:]_block_invoke"
+ "@24@0:8^Q16"
+ "@32@0:8@16^Q24"
+ "@80@0:8@16@24{?=[8I]}32@64@72"
+ "T{?=[8I]},N,V_auditToken"
+ "[ERROR] Move of a presenter %@ from %@ to %@ notified but no previous presenter existed"
+ "[ERROR] [Mat] Tried to materialize nil root for domain %@"
+ "[INFO] Associated thumbnail data for %{public}@ for identifier: %@, version: %@"
+ "[INFO] [Mat] Tried to materialize invalidated domain %@"
+ "[INFO] failed to download thumbnail for version %@: %{public}@"
+ "[INFO] ignoring presenter for item %@ because process requested passive presenters"
+ "_auditToken"
+ "_passivePresenterRequested"
+ "addPresenter:itemID:urlHint:auditToken:promiseID:"
+ "callExtensionForItemDidChange:request:completionHandler:"
+ "domainForIdentifier:reason:"
+ "domainForURL:reason:"
+ "domainFromItemID:reason:"
+ "domainOrNil:"
+ "domainWithID:reason:"
+ "fp_isDatalessWithError:"
+ "initWithIdentifier:itemID:auditToken:urlHint:domain:"
+ "listRemoteVersionsOfItemAtURL:includeCachedVersions:completionHandler:"
+ "presenter:withItemID:auditToken:urlHint:domain:"
+ "presenterAuditToken"
+ "presenterID"
+ "presenterWithID:"
+ "providerOrNilWithReason:"
+ "providerWithIdentifier:reason:"
+ "restoreWithCompletionHandler:"
+ "scheduleFPCKRun:domainUserInfo:databasesBackupsPath:urls:options:reason:fpfs:iCDPackageDetection:completionHandler:"
+ "setAuditToken:"
+ "v32@0:8@\"FPItemID\"16@?<v@?>24"
+ "v36@0:8@\"NSURL\"16B24@?<v@?@\"FPItem\"@\"NSArray\"@\"NSError\">28"
+ "v36@0:8@\"NSURL\"16B24@?<v@?B@\"FPItem\"@\"NSArray\"@\"NSError\">28"
+ "v80@0:8@16@24@32{?=[8I]}40Q72"
- "\x16#"
- "-[FPDProvider domainForIdentifier:]"
- "-[FPDXPCServicer listRemoteVersionsOfItemAtURL:completionHandler:]"
- "-[FPDXPCServicer listRemoteVersionsOfItemAtURL:completionHandler:]_block_invoke"
- "<%@ %p %@ presented by pid %@%s>"
- "@52@0:8@16@24i32@36@44"
- "ProviderNotRegistered"
- "T@\"FPDDomain\",R,N"
- "Ti,N,V_presenterPid"
- "Ti,R,V_requestEffectivePID"
- "[INFO] Associated thumbnail data for %@ for identifier: %@, version: %@"
- "[INFO] failed to download thumbnail for version %@: %@"
- "_presenterPid"
- "addPresenter:itemID:urlHint:pid:promiseID:"
- "didChangeItemID:"
- "domainForIdentifier:"
- "domainFromItemID:"
- "domainOrNil"
- "domainWithID:"
- "initWithIdentifier:itemID:pid:urlHint:domain:"
- "listRemoteVersionsOfItemAtURL:completionHandler:"
- "presenter:withItemID:pid:urlHint:domain:"
- "presenterPid"
- "providerOrNil"
- "providerWithIdentifier:"
- "scheduleFPCKRun:databasesBackupsPath:urls:options:reason:fpfs:iCDPackageDetection:completionHandler:"
- "setPresenterPid:"
- "v24@0:8@\"FPItemID\"16"
- "v32@0:8@\"NSURL\"16@?<v@?@\"FPItem\"@\"NSArray\"@\"NSError\">24"
- "v32@0:8@\"NSURL\"16@?<v@?B@\"FPItem\"@\"NSArray\"@\"NSError\">24"
- "v52@0:8@16@24@32i40Q44"

```
