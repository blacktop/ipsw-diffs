## SafariSharedUI

> `/System/Library/PrivateFrameworks/SafariSharedUI.framework/SafariSharedUI`

```diff

-616.1.27.10.16
-  __TEXT.__text: 0x16d3b0
+616.2.9.10.10
+  __TEXT.__text: 0x16effc
   __TEXT.__auth_stubs: 0x1430
-  __TEXT.__objc_methlist: 0xc7c4
-  __TEXT.__gcc_except_tab: 0x1e8ec
+  __TEXT.__objc_methlist: 0xc81c
+  __TEXT.__gcc_except_tab: 0x1ebd0
   __TEXT.__const: 0xd70
-  __TEXT.__cstring: 0x18059
-  __TEXT.__oslogstring: 0xade2
+  __TEXT.__cstring: 0x18207
+  __TEXT.__oslogstring: 0xae31
   __TEXT.__ustring: 0x1f00
   __TEXT.__dlopen_cstrs: 0x3f8
-  __TEXT.__unwind_info: 0x9c24
+  __TEXT.__unwind_info: 0x9cf8
   __TEXT.__eh_frame: 0x38
   __TEXT.__objc_classname: 0x27f6
-  __TEXT.__objc_methname: 0x30c99
-  __TEXT.__objc_methtype: 0x797c
-  __TEXT.__objc_stubs: 0x1c400
+  __TEXT.__objc_methname: 0x30eed
+  __TEXT.__objc_methtype: 0x79c0
+  __TEXT.__objc_stubs: 0x1c4c0
   __DATA_CONST.__got: 0x7d0
-  __DATA_CONST.__const: 0x7210
+  __DATA_CONST.__const: 0x7258
   __DATA_CONST.__objc_classlist: 0x7c0
   __DATA_CONST.__objc_catlist: 0xe8
   __DATA_CONST.__objc_protolist: 0x270
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x18cd0
-  __DATA_CONST.__objc_selrefs: 0x8b80
+  __DATA_CONST.__objc_const: 0x18d80
+  __DATA_CONST.__objc_selrefs: 0x8bb0
   __DATA_CONST.__objc_arraydata: 0x2160
   __AUTH_CONST.__objc_const: 0x61d0
-  __AUTH_CONST.__cfstring: 0x175a0
-  __AUTH_CONST.__const: 0x3bf0
+  __AUTH_CONST.__cfstring: 0x176e0
+  __AUTH_CONST.__const: 0x3c08
   __AUTH_CONST.__objc_intobj: 0xc18
   __AUTH_CONST.__objc_arrayobj: 0x888
   __AUTH_CONST.__objc_doubleobj: 0x50

   __DATA.__objc_protorefs: 0x30
   __DATA.__objc_classrefs: 0xca0
   __DATA.__objc_superrefs: 0x590
-  __DATA.__objc_ivar: 0x1378
+  __DATA.__objc_ivar: 0x1384
   __DATA.__data: 0x1f68
-  __DATA.__bss: 0x1020
+  __DATA.__bss: 0x1040
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x3c0
   __DATA_DIRTY.__bss: 0x29

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 922B6596-F178-3D15-8F35-DFE11D4CCA87
-  Functions: 7506
-  Symbols:   26928
-  CStrings:  14710
+  UUID: 263EAC79-3338-367D-8714-B8350BF84C27
+  Functions: 7535
+  Symbols:   27015
+  CStrings:  14745
 
Symbols:
+ -[WBSStartPageBackgroundManager _isGeneratedBackgroundImageInImageSource:]
+ -[WBSStartPageBackgroundManager getHasGeneratedBackgroundImage:forProfileWithIdentifier:completionHandler:]
+ -[WBSWebExtensionAPIStorageAreaObjC setAccessLevelWithAccessOptions:browserContextController:completionHandler:outExceptionString:]
+ -[WBSWebExtensionAPIStorageAreaObjC setAccessLevelWithAccessOptions:browserContextController:completionHandler:outExceptionString:].cold.1
+ -[WBSWebExtensionAPIStorageObjC isPropertyAllowed:inBrowsingContext:]
+ -[WBSWebExtensionData _readSessionStorageAllowedInContentScriptsValueFromDisk]
+ -[WBSWebExtensionData isSessionStorageAllowedInContentScripts]
+ -[WBSWebExtensionData sessionStorageAllowedInContentScripts]
+ -[WBSWebExtensionData setSessionStorageAllowedInContentScripts:]
+ -[WBSWebExtensionsController setSessionStorageAccessLevel:forExtensionWithUniqueIdentifier:completionHandler:]
+ -[WBSWebExtensionsControllerSelectorForwarder setSessionStorageAccessLevel:forExtensionWithUniqueIdentifier:completionHandler:]
+ GCC_except_table301
+ GCC_except_table307
+ GCC_except_table338
+ GCC_except_table384
+ GCC_except_table390
+ GCC_except_table392
+ GCC_except_table395
+ GCC_except_table399
+ GCC_except_table405
+ GCC_except_table412
+ GCC_except_table414
+ GCC_except_table419
+ _OBJC_IVAR_$_WBSStartPageBackgroundManager._imageReadWriteQueue
+ _OBJC_IVAR_$_WBSStartPageBackgroundManager._imageURLToTileRequired
+ _OBJC_IVAR_$_WBSWebExtensionData._isSessionStorageAllowedInContentScriptsValuePopulated
+ _OBJC_IVAR_$_WBSWebExtensionData._sessionStorageAllowedInContentScripts
+ _WBSWebExtensionStateSessionStorageAllowedInContentScriptsKey
+ _WBSWebExtensionStorageAreaAccessLevel
+ _WBSWebExtensionStorageAreaAccessLevelTrustedAndUntrustedContexts
+ _WBSWebExtensionStorageAreaAccessLevelTrustedContexts
+ __ZGVZ131-[WBSWebExtensionAPIStorageAreaObjC setAccessLevelWithAccessOptions:browserContextController:completionHandler:outExceptionString:]E12requiredKeys
+ __ZGVZ131-[WBSWebExtensionAPIStorageAreaObjC setAccessLevelWithAccessOptions:browserContextController:completionHandler:outExceptionString:]E8keyTypes
+ __ZN12SafariShared27JSWBSWebExtensionAPIStorage11getPropertyEPK15OpaqueJSContextP13OpaqueJSValueP14OpaqueJSStringPPKS4_
+ __ZN12SafariShared27JSWBSWebExtensionAPIStorage11hasPropertyEPK15OpaqueJSContextP13OpaqueJSValueP14OpaqueJSString
+ __ZN12SafariShared27JSWBSWebExtensionAPIStorage16getPropertyNamesEPK15OpaqueJSContextP13OpaqueJSValueP31OpaqueJSPropertyNameAccumulator
+ __ZN12SafariShared31JSWBSWebExtensionAPIStorageArea14setAccessLevelEPK15OpaqueJSContextP13OpaqueJSValueS5_mPKPKS4_PS7_
+ __ZZ131-[WBSWebExtensionAPIStorageAreaObjC setAccessLevelWithAccessOptions:browserContextController:completionHandler:outExceptionString:]E12requiredKeys
+ __ZZ131-[WBSWebExtensionAPIStorageAreaObjC setAccessLevelWithAccessOptions:browserContextController:completionHandler:outExceptionString:]E8keyTypes
+ ___107-[WBSStartPageBackgroundManager getHasGeneratedBackgroundImage:forProfileWithIdentifier:completionHandler:]_block_invoke
+ ___107-[WBSStartPageBackgroundManager getHasGeneratedBackgroundImage:forProfileWithIdentifier:completionHandler:]_block_invoke_2
+ ___109-[WBSWebExtensionData _updateDeclarativeNetRequestRulesInStorage:byRemovingRules:addRules:completionHandler:]_block_invoke.467.cold.1
+ ___109-[WBSWebExtensionData _updateDeclarativeNetRequestRulesInStorage:byRemovingRules:addRules:completionHandler:]_block_invoke.468
+ ___109-[WBSWebExtensionData _updateDeclarativeNetRequestRulesInStorage:byRemovingRules:addRules:completionHandler:]_block_invoke.468.cold.1
+ ___109-[WBSWebExtensionData _updateDeclarativeNetRequestRulesInStorage:byRemovingRules:addRules:completionHandler:]_block_invoke.469
+ ___109-[WBSWebExtensionData _updateDeclarativeNetRequestRulesInStorage:byRemovingRules:addRules:completionHandler:]_block_invoke.470
+ ___109-[WBSWebExtensionData _updateDeclarativeNetRequestRulesInStorage:byRemovingRules:addRules:completionHandler:]_block_invoke_2.474
+ ___109-[WBSWebExtensionData _updateDeclarativeNetRequestRulesInStorage:byRemovingRules:addRules:completionHandler:]_block_invoke_2.474.cold.1
+ ___115-[WBSStartPageBackgroundManager _readImagePropertiesFromImageSource:forImageIdentifier:isNonGlobalBackgroundImage:]_block_invoke_2
+ ___115-[WBSStartPageBackgroundManager _readImagePropertiesFromImageSource:forImageIdentifier:isNonGlobalBackgroundImage:]_block_invoke_3
+ ___116-[WBSWebExtensionAPIStorageAreaObjC setItems:browserContextController:context:completionHandler:outExceptionString:]_block_invoke.82
+ ___118-[WBSWebExtensionsController setKeyedData:inStorageOfType:forExtensionWithUniqueIdentifier:webView:completionHandler:]_block_invoke.341
+ ___121-[WBSWebExtensionAPIStorageAreaObjC getBytesInUseForItems:browserContextController:completionHandler:outExceptionString:]_block_invoke.76
+ ___131-[WBSWebExtensionAPIStorageAreaObjC setAccessLevelWithAccessOptions:browserContextController:completionHandler:outExceptionString:]_block_invoke
+ ___134-[WBSStartPageBackgroundManager _commitImage:appearanceName:luminance:forIdentifier:isGeneratedImage:withinProfile:completionHandler:]_block_invoke_3
+ ___50-[WBSStartPageBackgroundManager initWithImageURL:]_block_invoke
+ ___50-[WBSWebExtensionData _loadBackgroundPageWithURL:]_block_invoke.565
+ ___54-[WBSWebExtensionData _populateWebAccessibleResources]_block_invoke.350
+ ___54-[WBSWebExtensionData _populateWebAccessibleResources]_block_invoke.350.cold.1
+ ___65-[WBSStartPageBackgroundManager _loadImageFromDiskForIdentifier:]_block_invoke_3
+ ___77-[WBSWebExtensionsController postMessage:fromPortWithID:fromExtensionWithID:]_block_invoke.295
+ ___78-[WBSStartPageBackgroundManager reloadProfileSpecificBackgroundImageFromDisk:]_block_invoke
+ ___79-[WBSStartPageBackgroundManager reloadTabGroupSpecificBackgroundImageFromDisk:]_block_invoke
+ ___79-[WBSWebExtensionsController _deleteStorageForExtensionWithComposedIdentifier:]_block_invoke.168
+ ___80-[WBSStartPageBackgroundManager tabGroupManager:didRemoveProfileWithIdentifier:]_block_invoke
+ ___82-[WBSStartPageBackgroundManager _setImageOnAnyQueue:withAppearance:forIdentifier:]_block_invoke.101
+ ___82-[WBSStartPageBackgroundManager _setImageOnAnyQueue:withAppearance:forIdentifier:]_block_invoke_2
+ ___84-[WBSWebExtensionData loadRegisteredContentScriptsFromStorageWithCompletionHandler:]_block_invoke.483
+ ___86-[WBSWebExtensionData loadDeclarativeNetRequestRulesetsIfNeededWithCompletionHandler:]_block_invoke.419
+ ___86-[WBSWebExtensionData loadDeclarativeNetRequestRulesetsIfNeededWithCompletionHandler:]_block_invoke.419.cold.1
+ ___91-[WBSWebExtensionsController _loadPermissionsFromStorageForWebExtension:completionHandler:]_block_invoke.299
+ ___block_descriptor_56_ea8_32s40s48c31_ZTSN3WTF9RetainPtrIP7CGImageEE_e5_v8?0l
+ ___block_descriptor_57_ea8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_literal_global.110
+ ___block_literal_global.124
+ ___block_literal_global.197
+ ___block_literal_global.239
+ ___block_literal_global.255
+ ___block_literal_global.297
+ ___block_literal_global.304
+ ___block_literal_global.311
+ ___block_literal_global.321
+ ___block_literal_global.326
+ ___block_literal_global.355
+ ___block_literal_global.378
+ ___block_literal_global.398
+ ___block_literal_global.455
+ ___block_literal_global.462
+ ___block_literal_global.485
+ ___block_literal_global.493
+ ___block_literal_global.507
+ ___block_literal_global.517
+ ___block_literal_global.519
+ ___block_literal_global.540
+ ___block_literal_global.558
+ ___copy_helper_block_ea8_48c31_ZTSN3WTF9RetainPtrIP7CGImageEE
+ ___destroy_helper_block_ea8_48c31_ZTSN3WTF9RetainPtrIP7CGImageEE
+ __unnamed_array_storage.1357
+ __unnamed_array_storage.1492
+ __unnamed_array_storage.421
+ __unnamed_array_storage.451
+ __unnamed_array_storage.498
+ _objc_msgSend$_isGeneratedBackgroundImageInImageSource:
+ _objc_msgSend$_readSessionStorageAllowedInContentScriptsValueFromDisk
+ _objc_msgSend$data
+ _objc_msgSend$getHasGeneratedBackgroundImage:forProfileWithIdentifier:completionHandler:
+ _objc_msgSend$isSessionStorageAllowedInContentScripts
+ _objc_msgSend$setSessionStorageAccessLevel:forExtensionWithUniqueIdentifier:completionHandler:
+ _objc_msgSend$setSessionStorageAllowedInContentScripts:
- -[WBSStartPageBackgroundManager hasGeneratedBackgroundImage:forProfileWithIdentifier:]
- GCC_except_table302
- GCC_except_table339
- GCC_except_table386
- GCC_except_table391
- GCC_except_table394
- GCC_except_table396
- GCC_except_table400
- GCC_except_table407
- GCC_except_table413
- GCC_except_table417
- _OBJC_IVAR_$_WBSStartPageBackgroundManager._imageSavingQueue
- ___109-[WBSWebExtensionData _updateDeclarativeNetRequestRulesInStorage:byRemovingRules:addRules:completionHandler:]_block_invoke.464
- ___109-[WBSWebExtensionData _updateDeclarativeNetRequestRulesInStorage:byRemovingRules:addRules:completionHandler:]_block_invoke.464.cold.1
- ___109-[WBSWebExtensionData _updateDeclarativeNetRequestRulesInStorage:byRemovingRules:addRules:completionHandler:]_block_invoke.465
- ___109-[WBSWebExtensionData _updateDeclarativeNetRequestRulesInStorage:byRemovingRules:addRules:completionHandler:]_block_invoke.465.cold.1
- ___109-[WBSWebExtensionData _updateDeclarativeNetRequestRulesInStorage:byRemovingRules:addRules:completionHandler:]_block_invoke.466
- ___109-[WBSWebExtensionData _updateDeclarativeNetRequestRulesInStorage:byRemovingRules:addRules:completionHandler:]_block_invoke_2.471
- ___109-[WBSWebExtensionData _updateDeclarativeNetRequestRulesInStorage:byRemovingRules:addRules:completionHandler:]_block_invoke_2.471.cold.1
- ___116-[WBSWebExtensionAPIStorageAreaObjC setItems:browserContextController:context:completionHandler:outExceptionString:]_block_invoke.71
- ___118-[WBSWebExtensionsController setKeyedData:inStorageOfType:forExtensionWithUniqueIdentifier:webView:completionHandler:]_block_invoke.338
- ___121-[WBSWebExtensionAPIStorageAreaObjC getBytesInUseForItems:browserContextController:completionHandler:outExceptionString:]_block_invoke.65
- ___50-[WBSWebExtensionData _loadBackgroundPageWithURL:]_block_invoke.562
- ___54-[WBSWebExtensionData _populateWebAccessibleResources]_block_invoke.347
- ___54-[WBSWebExtensionData _populateWebAccessibleResources]_block_invoke.347.cold.1
- ___77-[WBSWebExtensionsController postMessage:fromPortWithID:fromExtensionWithID:]_block_invoke.292
- ___79-[WBSWebExtensionsController _deleteStorageForExtensionWithComposedIdentifier:]_block_invoke.165
- ___84-[WBSWebExtensionData loadRegisteredContentScriptsFromStorageWithCompletionHandler:]_block_invoke.480
- ___86-[WBSWebExtensionData loadDeclarativeNetRequestRulesetsIfNeededWithCompletionHandler:]_block_invoke.416
- ___86-[WBSWebExtensionData loadDeclarativeNetRequestRulesetsIfNeededWithCompletionHandler:]_block_invoke.416.cold.1
- ___91-[WBSWebExtensionsController _loadPermissionsFromStorageForWebExtension:completionHandler:]_block_invoke.296
- ___block_literal_global.108
- ___block_literal_global.194
- ___block_literal_global.205
- ___block_literal_global.236
- ___block_literal_global.252
- ___block_literal_global.294
- ___block_literal_global.301
- ___block_literal_global.308
- ___block_literal_global.318
- ___block_literal_global.323
- ___block_literal_global.352
- ___block_literal_global.375
- ___block_literal_global.395
- ___block_literal_global.452
- ___block_literal_global.459
- ___block_literal_global.479
- ___block_literal_global.490
- ___block_literal_global.501
- ___block_literal_global.514
- ___block_literal_global.516
- ___block_literal_global.537
- ___block_literal_global.555
- __unnamed_array_storage.1346
- __unnamed_array_storage.1481
- __unnamed_array_storage.363
- __unnamed_array_storage.448
- __unnamed_array_storage.495
- _objc_msgSend$hasGeneratedBackgroundImage:forProfileWithIdentifier:
CStrings:
+ "\x02\x12\x113"
+ "8616.2.9.10.10"
+ "B24@0:8^{CGImageSource=}16"
+ "Invalid 'accessLevel' value passed to session.setAccessLevel(): %@"
+ "Invalid 'accessOptions' value passed to storageArea.setAccessLevel(). Expected an object."
+ "Invalid call to session.setAccessLevel() for extension %{private}@. %{public}@"
+ "Invalid call to session.setAccessLevel(). %@"
+ "Invalid call to storageArea.setAccessLevel(). A required argument is missing."
+ "SessionStorageAllowedInContentScripts"
+ "TB,N,GisSessionStorageAllowedInContentScripts,V_sessionStorageAllowedInContentScripts"
+ "TRUSTED_AND_UNTRUSTED_CONTEXTS"
+ "TRUSTED_CONTEXTS"
+ "_imageReadWriteQueue"
+ "_imageURLToTileRequired"
+ "_isGeneratedBackgroundImageInImageSource:"
+ "_isSessionStorageAllowedInContentScriptsValuePopulated"
+ "_readSessionStorageAllowedInContentScriptsValueFromDisk"
+ "_sessionStorageAllowedInContentScripts"
+ "accessLevel"
+ "getHasGeneratedBackgroundImage:forProfileWithIdentifier:completionHandler:"
+ "isSessionStorageAllowedInContentScripts"
+ "sessionStorageAllowedInContentScripts"
+ "setAccessLevel"
+ "setSessionStorageAccessLevel:forExtensionWithUniqueIdentifier:completionHandler:"
+ "setSessionStorageAllowedInContentScripts:"
+ "tabGroupManager:didFinishSyncForScopedBookmarkList:"
+ "v40@0:8@\"NSString\"16@\"NSUUID\"24@?<v@?>32"
- "\x02\"!\x12"
- "8616.1.27.10.16"
- "hasGeneratedBackgroundImage:forProfileWithIdentifier:"

```
