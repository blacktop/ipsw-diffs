## CloudDocs

> `/System/Library/PrivateFrameworks/CloudDocs.framework/CloudDocs`

```diff

-3437.120.20.0.0
-  __TEXT.__text: 0x8a330
-  __TEXT.__auth_stubs: 0x13c0
-  __TEXT.__objc_methlist: 0x6a4c
-  __TEXT.__const: 0x1c8
-  __TEXT.__gcc_except_tab: 0x4c10
-  __TEXT.__cstring: 0xb55c
-  __TEXT.__oslogstring: 0x95a9
+4140.0.0.502.2
+  __TEXT.__text: 0x8a67c
+  __TEXT.__auth_stubs: 0x1480
+  __TEXT.__objc_methlist: 0x672c
+  __TEXT.__const: 0x1c0
+  __TEXT.__gcc_except_tab: 0x4bb8
+  __TEXT.__cstring: 0xb695
+  __TEXT.__oslogstring: 0x95fc
   __TEXT.__dlopen_cstrs: 0x4c
   __TEXT.__ustring: 0x8
-  __TEXT.__unwind_info: 0x2708
-  __TEXT.__objc_classname: 0xdf5
-  __TEXT.__objc_methname: 0x11618
-  __TEXT.__objc_methtype: 0x441a
-  __TEXT.__objc_stubs: 0xafc0
-  __DATA_CONST.__got: 0x8b0
-  __DATA_CONST.__const: 0x2698
-  __DATA_CONST.__objc_classlist: 0x308
+  __TEXT.__unwind_info: 0x26c8
+  __TEXT.__objc_classname: 0xdd2
+  __TEXT.__objc_methname: 0x10f66
+  __TEXT.__objc_methtype: 0x3c75
+  __TEXT.__objc_stubs: 0xb1a0
+  __DATA_CONST.__got: 0x898
+  __DATA_CONST.__const: 0x2678
+  __DATA_CONST.__objc_classlist: 0x310
   __DATA_CONST.__objc_catlist: 0xe8
-  __DATA_CONST.__objc_protolist: 0x130
+  __DATA_CONST.__objc_protolist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x42e8
-  __DATA_CONST.__objc_protorefs: 0x70
-  __DATA_CONST.__objc_classrefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x260
+  __DATA_CONST.__objc_selrefs: 0x41f0
+  __DATA_CONST.__objc_protorefs: 0x68
+  __DATA_CONST.__objc_superrefs: 0x250
   __DATA_CONST.__objc_arraydata: 0x58
-  __AUTH_CONST.__auth_got: 0x9f0
+  __AUTH_CONST.__auth_got: 0xa50
   __AUTH_CONST.__const: 0x10e0
-  __AUTH_CONST.__cfstring: 0x5c20
-  __AUTH_CONST.__objc_const: 0xdf28
+  __AUTH_CONST.__cfstring: 0x5c00
+  __AUTH_CONST.__objc_const: 0xce88
   __AUTH_CONST.__objc_arrayobj: 0x48
-  __AUTH_CONST.__objc_intobj: 0x4f8
+  __AUTH_CONST.__objc_intobj: 0x510
   __AUTH_CONST.__objc_doubleobj: 0x30
-  __AUTH.__objc_data: 0x1400
+  __AUTH.__objc_data: 0x14f0
   __AUTH.__data: 0xa8
-  __DATA.__objc_ivar: 0x658
-  __DATA.__data: 0xeb0
+  __DATA.__objc_ivar: 0x654
+  __DATA.__data: 0xdf0
   __DATA.__bss: 0x3c8
-  __DATA.__common: 0x10
-  __DATA_DIRTY.__objc_data: 0xa50
+  __DATA.__common: 0x8
+  __DATA_DIRTY.__objc_data: 0x9b0
   __DATA_DIRTY.__data: 0x28
-  __DATA_DIRTY.__bss: 0x298
+  __DATA_DIRTY.__bss: 0x290
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 2CAD0DDC-41EA-30EA-8FDD-35496426DB38
-  Functions: 3104
-  Symbols:   10888
-  CStrings:  6301
+  UUID: F403EE27-7740-330D-9914-313CB6C82110
+  Functions: 3093
+  Symbols:   10822
+  CStrings:  6235
 
Symbols:
+ +[BRFeatureFlags requestForAccessEnabled]
+ +[BRNSDataWrapper dataWithContentsOfURL:]
+ +[BRNSDataWrapper writeData:toURL:atomically:]
+ +[BRSpecialFolders internalDaemonContainerPath]
+ +[BRSpecialFolders internalDaemonContainerPath].cold.1
+ +[BRSpecialFolders internalDaemonContainerPath].cold.2
+ +[BRSpecialFolders internalDaemonContainerPath].cold.3
+ +[BRSpecialFolders internalDaemonContainerPath].cold.4
+ +[BRSpecialFolders internalDaemonContainerPath].cold.5
+ +[NSError(BRAdditions) brc_errorFunctionNotImplemented:]
+ +[NSError(BRAdditions) brc_errorFunctionNotImplemented:].cold.1
+ +[NSError(BRAdditions) brc_errorOperationNotImplemented:]
+ +[NSError(BRAdditions) brc_errorOperationNotImplemented:].cold.1
+ +[NSError(BRFPAdditions) _getFirstCloudKitUnderlyingError:]
+ +[UMUserManager(BRAdditions) _isInSyncBubble]
+ -[BRAutoShareAcceptOperation main]
+ -[BRAutoShareAcceptOperation main].cold.1
+ -[BRMangledID isReservedMangedID]
+ -[BRNotificationReceiver receiveUpdates:reply:]
+ -[BRPair description]
+ -[BRQueryItem updateContentVersion:]
+ -[NSURL(BRCPathAdditions) brc_appBundleID]
+ -[NSURL(BRCPathAdditions) brc_appContainerID]
+ -[UMUserPersona(BRAdditions) br_personaIDWithDefault:]
+ GCC_except_table108
+ GCC_except_table116
+ GCC_except_table117
+ GCC_except_table133
+ GCC_except_table158
+ GCC_except_table176
+ GCC_except_table179
+ GCC_except_table182
+ GCC_except_table237
+ GCC_except_table35
+ GCC_except_table50
+ GCC_except_table54
+ GCC_except_table56
+ GCC_except_table58
+ GCC_except_table64
+ GCC_except_table70
+ GCC_except_table80
+ GCC_except_table83
+ GCC_except_table93
+ GCC_except_table96
+ GCC_except_table99
+ OBJC_IVAR_$_BRShareAcceptOperation._shareLink
+ _BRCanGetCKRecordID
+ _BREntitlementAutoAcceptShare
+ _BRGetCKRecordIDsForFPItems
+ _CONTAINER_PERSONA_PRIMARY
+ _NSFileProviderErrorRetryAfterKey
+ _NSStringFromClass
+ _OBJC_CLASS_$_BRAutoShareAcceptOperation
+ _OBJC_CLASS_$_BRFeatureFlags
+ _OBJC_CLASS_$_BRNSDataWrapper
+ _OBJC_CLASS_$_FPEvictOperation
+ _OBJC_IVAR_$_BRProcessMonitor._weakObserver
+ _OBJC_METACLASS_$_BRAutoShareAcceptOperation
+ _OBJC_METACLASS_$_BRFeatureFlags
+ _OBJC_METACLASS_$_BRNSDataWrapper
+ __OBJC_$_CLASS_METHODS_BRFeatureFlags
+ __OBJC_$_CLASS_METHODS_BRNSDataWrapper
+ __OBJC_$_CLASS_METHODS_BRQuery
+ __OBJC_$_INSTANCE_METHODS_BRAutoShareAcceptOperation
+ __OBJC_CLASS_RO_$_BRAutoShareAcceptOperation
+ __OBJC_CLASS_RO_$_BRFeatureFlags
+ __OBJC_CLASS_RO_$_BRNSDataWrapper
+ __OBJC_METACLASS_RO_$_BRAutoShareAcceptOperation
+ __OBJC_METACLASS_RO_$_BRFeatureFlags
+ __OBJC_METACLASS_RO_$_BRNSDataWrapper
+ ___34-[BRAutoShareAcceptOperation main]_block_invoke
+ ___38-[BRQuery _processProgressUpdateBatch]_block_invoke.138
+ ___40-[BRQuery _applicationWillResignActive:]_block_invoke.160
+ ___40-[BRQuery _applicationWillResignActive:]_block_invoke.160.cold.1
+ ___46-[BRQuery itemCollectionGathererDidInvalidate]_block_invoke.144
+ ___46-[BRQuery itemCollectionGathererDidInvalidate]_block_invoke.144.cold.1
+ ___47-[BRNotificationReceiver receiveUpdates:reply:]_block_invoke
+ ___47-[BRNotificationReceiver receiveUpdates:reply:]_block_invoke.cold.1
+ ___BREvictItemAtURL_block_invoke
+ ___BREvictItemAtURL_block_invoke_2
+ ___BRGetCKRecordIDsForFPItems_block_invoke
+ ___BRGetCKRecordIDsForFPItems_block_invoke_2
+ ___BRiWorkSharingSetSharingState_block_invoke.84
+ ___block_descriptor_32_e19_24?0"FPItem"8Q16l
+ ___block_descriptor_40_e8_32bs_e28_v24?0"FPItem"8"NSError"16ls32l8
+ ___block_descriptor_52_e8_32s40s_e40_v16?0"<RBSProcessMonitorConfiguring>"8ls32l8s40l8
+ ___block_descriptor_52_e8_32s40s_e74_v32?0"RBSProcessMonitor"8"RBSProcessHandle"16"RBSProcessStateUpdate"24ls32l8s40l8
+ ___block_literal_global.116
+ ___block_literal_global.128
+ ___block_literal_global.130
+ ___block_literal_global.132
+ ___block_literal_global.159
+ ___block_literal_global.173
+ ___block_literal_global.217
+ ___block_literal_global.220
+ ___block_literal_global.234
+ ___block_literal_global.240
+ ___block_literal_global.418
+ ___block_literal_global.430
+ ___block_literal_global.462
+ ___block_literal_global.479
+ ___block_literal_global.69
+ __os_feature_enabled_impl
+ _container_copy_sandbox_token
+ _container_copy_unlocalized_description
+ _container_error_copy_unlocalized_description
+ _container_get_path
+ _container_query_create
+ _container_query_free
+ _container_query_get_last_error
+ _container_query_get_single_result
+ _container_query_operation_set_flags
+ _container_query_set_class
+ _container_query_set_identifiers
+ _container_query_set_persona_unique_string
+ _objc_msgSend$_getFirstCloudKitUnderlyingError:
+ _objc_msgSend$_isInSyncBubble
+ _objc_msgSend$_setError
+ _objc_msgSend$br_personaIDWithDefault:
+ _objc_msgSend$br_suggestedRetryDate
+ _objc_msgSend$br_suggestedRetryTimeInterval
+ _objc_msgSend$brc_applicationBundleIDForExtension:
+ _objc_msgSend$brc_applicationContainerIDForExtension:
+ _objc_msgSend$brc_errorFunctionNotImplemented:
+ _objc_msgSend$brc_errorOperationNotImplemented:
+ _objc_msgSend$containerMetadataMangledID
+ _objc_msgSend$data
+ _objc_msgSend$dataWithContentsOfURL:
+ _objc_msgSend$fetchItemForURL:completionHandler:
+ _objc_msgSend$getBytes:range:
+ _objc_msgSend$getCKRecordIDsForFPItems:reply:
+ _objc_msgSend$hasError
+ _objc_msgSend$position
+ _objc_msgSend$scheduleAction:
+ _objc_msgSend$setActionCompletionBlock:
+ _objc_msgSend$setPosition:
+ _objc_msgSend$sideCarMangledID
+ _objc_msgSend$startOperation:toAutoAcceptShareLink:reply:
+ _objc_msgSend$stringWithCString:encoding:
+ _objc_msgSend$writeToURL:atomically:
+ _objc_msgSend$zoneHealthMangledID
+ _xpc_string_create
- +[BRDocObjectID supportsSecureCoding]
- +[BRFileObjectID fileObjectIDForURL:allocateDocID:error:]
- +[BRInodeObjectID supportsSecureCoding]
- +[BRQuery(BRQueryStitching) didEndPossibleFileOperation:]
- +[BRQuery(BRQueryStitching) willBeginPossibleCreationOfItemAtURL:]
- +[BRQuery(BRQueryStitching) willBeginPossibleDeletionOfItemAtURL:]
- +[BRQuery(BRQueryStitching) willBeginPossibleMoveOfItemAtURL:toURL:]
- +[UMUserManager(BRAdditions) br_isInSyncBubble].cold.1
- -[BRDaemonConnection newLegacySyncProxy]
- -[BRDaemonConnection newLegacySyncProxy].cold.1
- -[BRDocObjectID asString]
- -[BRDocObjectID description]
- -[BRDocObjectID documentID]
- -[BRDocObjectID encodeWithCoder:]
- -[BRDocObjectID initWithCoder:]
- -[BRDocObjectID initWithDocID:]
- -[BRDocObjectID initWithDocIDNumber:]
- -[BRDocObjectID isDocumentID]
- -[BRDocObjectID isFpfsItem]
- -[BRDocObjectID rawID]
- -[BRDocObjectID type]
- -[BRInodeObjectID asString]
- -[BRInodeObjectID description]
- -[BRInodeObjectID encodeWithCoder:]
- -[BRInodeObjectID folderID]
- -[BRInodeObjectID initWithCoder:]
- -[BRInodeObjectID initWithFileID:]
- -[BRInodeObjectID isFolderOrAliasID]
- -[BRInodeObjectID isFpfsItem]
- -[BRInodeObjectID rawID]
- -[BRInodeObjectID type]
- -[BRNotificationReceiver receiveUpdates:logicalExtensions:physicalExtensions:reply:]
- -[BROperation remoteLegacyObject]
- -[BROperation remoteLegacyObject].cold.1
- -[NSComparisonPredicate(BRQueryItemAdditions_Private) br_fileObjectIDWithWatchedChildren]
- GCC_except_table102
- GCC_except_table112
- GCC_except_table115
- GCC_except_table132
- GCC_except_table144
- GCC_except_table157
- GCC_except_table159
- GCC_except_table163
- GCC_except_table175
- GCC_except_table178
- GCC_except_table236
- GCC_except_table31
- GCC_except_table39
- GCC_except_table45
- GCC_except_table49
- GCC_except_table55
- GCC_except_table57
- GCC_except_table60
- GCC_except_table63
- GCC_except_table66
- GCC_except_table67
- GCC_except_table69
- GCC_except_table74
- GCC_except_table79
- GCC_except_table84
- GCC_except_table88
- GCC_except_table90
- GCC_except_table98
- OBJC_IVAR_$_BRDocObjectID._docID
- OBJC_IVAR_$_BRInodeObjectID._ino
- OBJC_IVAR_$_PBDataReader._bytes
- OBJC_IVAR_$_PBDataReader._error
- OBJC_IVAR_$_PBDataReader._length
- OBJC_IVAR_$_PBDataReader._pos
- _BRRegisterInitialSyncHandlerForContainer.cold.1
- _OBJC_CLASS_$_BRDocObjectID
- _OBJC_CLASS_$_BRInodeObjectID
- _OBJC_IVAR_$_BRShareAcceptOperation._shareLink
- _OBJC_METACLASS_$_BRDocObjectID
- _OBJC_METACLASS_$_BRInodeObjectID
- __OBJC_$_CLASS_METHODS_BRDocObjectID
- __OBJC_$_CLASS_METHODS_BRInodeObjectID
- __OBJC_$_CLASS_METHODS_BRQuery(BRQueryStitching)
- __OBJC_$_INSTANCE_METHODS_BRDocObjectID
- __OBJC_$_INSTANCE_METHODS_BRInodeObjectID
- __OBJC_$_INSTANCE_VARIABLES_BRDocObjectID
- __OBJC_$_INSTANCE_VARIABLES_BRInodeObjectID
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_BRProtocolLegacy
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_BRShareOperationLegacyProtocol
- __OBJC_$_PROTOCOL_METHOD_TYPES_BRProtocolLegacy
- __OBJC_$_PROTOCOL_METHOD_TYPES_BRShareOperationLegacyProtocol
- __OBJC_$_PROTOCOL_REFS_BRProtocolLegacy
- __OBJC_$_PROTOCOL_REFS_BRShareOperationLegacyProtocol
- __OBJC_CLASS_RO_$_BRDocObjectID
- __OBJC_CLASS_RO_$_BRInodeObjectID
- __OBJC_LABEL_PROTOCOL_$_BRProtocolLegacy
- __OBJC_LABEL_PROTOCOL_$_BRShareOperationLegacyProtocol
- __OBJC_METACLASS_RO_$_BRDocObjectID
- __OBJC_METACLASS_RO_$_BRInodeObjectID
- __OBJC_PROTOCOL_$_BRProtocolLegacy
- __OBJC_PROTOCOL_$_BRShareOperationLegacyProtocol
- __OBJC_PROTOCOL_REFERENCE_$_BRProtocolLegacy
- ___32-[BRFileProvidingOperation main]_block_invoke
- ___32-[BRFileProvidingOperation main]_block_invoke_2
- ___34-[BRSharingCopyEtagOperation main]_block_invoke
- ___38-[BRQuery _processProgressUpdateBatch]_block_invoke.146
- ___39-[BRSharingCopyShareInfoOperation main]_block_invoke
- ___40-[BRQuery _applicationWillResignActive:]_block_invoke.168
- ___40-[BRQuery _applicationWillResignActive:]_block_invoke.168.cold.1
- ___46-[BRQuery itemCollectionGathererDidInvalidate]_block_invoke.152
- ___46-[BRQuery itemCollectionGathererDidInvalidate]_block_invoke.152.cold.1
- ___59+[NSURL(BRAdditions) br_documentURLFromFileObjectID:error:]_block_invoke
- ___84-[BRNotificationReceiver receiveUpdates:logicalExtensions:physicalExtensions:reply:]_block_invoke
- ___84-[BRNotificationReceiver receiveUpdates:logicalExtensions:physicalExtensions:reply:]_block_invoke.cold.1
- ___BRiWorkSharingSetSharingState_block_invoke.86
- ___block_descriptor_40_e8_32s_e36_v32?0"NSString"8B16B20"NSError"24ls32l8
- ___block_descriptor_40_e8_32s_e59_v48?0"NSURL"8"NSData"16"NSURL"24"NSData"32"NSError"40ls32l8
- ___block_descriptor_60_e8_32s40s48w_e40_v16?0"<RBSProcessMonitorConfiguring>"8ls32l8w48l8s40l8
- ___block_descriptor_60_e8_32s40s48w_e74_v32?0"RBSProcessMonitor"8"RBSProcessHandle"16"RBSProcessStateUpdate"24lw48l8s32l8s40l8
- ___block_descriptor_72_e8_32s40s48s56s64bs_e5_v8?0ls32l8s64l8s40l8s48l8s56l8
- ___block_literal_global.114
- ___block_literal_global.140
- ___block_literal_global.175
- ___block_literal_global.215
- ___block_literal_global.218
- ___block_literal_global.229
- ___block_literal_global.235
- ___block_literal_global.414
- ___block_literal_global.426
- ___block_literal_global.460
- ___block_literal_global.474
- ___block_literal_global.67
- _brc_activity_block_remember_persona
- _fchflags
- _fgetxattr
- _gBRActiveQueriesSet
- _objc_msgSend$attachLogicalExtension:physicalExtension:
- _objc_msgSend$decodeInt32ForKey:
- _objc_msgSend$encodeInt32:forKey:
- _objc_msgSend$initWithDocID:
- _objc_msgSend$initWithFileID:
- _objc_msgSend$newLegacySyncProxy
- _objc_msgSend$remoteLegacyObject
- _objc_msgSend$resolveFileObjectIDToURL:reply:
- _objc_msgSend$startOperation:toCopyEtagAtURL:reply:
- _objc_msgSend$startOperation:toCopyShareInfoAtURL:reply:
- _objc_msgSend$startOperation:toDownloadItemAtURL:readingOptions:wantsCurrentVersion:reply:
- _strtoull
CStrings:
+ "(%@, %@)"
+ "+[BRSpecialFolders internalDaemonContainerPath]"
+ "+[NSError(BRAdditions) brc_errorFunctionNotImplemented:]"
+ "+[NSError(BRAdditions) brc_errorOperationNotImplemented:]"
+ "-[BRAutoShareAcceptOperation main]"
+ "-[BRNotificationReceiver receiveUpdates:reply:]"
+ "-[BRNotificationReceiver receiveUpdates:reply:]_block_invoke"
+ "/Library/Caches/com.apple.xbs/Sources/CloudDocs/framework/foundation/BRSpecialFolders.m"
+ "4140.0.0.502.2"
+ "@\"<BRProcessMonitorDelegate>\""
+ "@\"NSProgress\"48@0:8@\"NSSecurityScopedURLWrapper\"16@\"NSFileProviderItemVersion\"24Q32@?<v@?@\"NSFileProviderItemVersion\"@\"NSError\">40"
+ "@\"NSProgress\"56@0:8@\"BRFileObjectID\"16@\"FPSandboxingURLWrapper\"24Q32@\"NSString\"40@?<v@?@\"NSDictionary\"@\"NSError\">48"
+ "@\"NSProgress\"60@0:8@\"NSString\"16@\"NSSecurityScopedURLWrapper\"24@\"NSFileProviderItemVersion\"32B40Q44@?<v@?@\"NSFileProviderItemVersion\"@\"NSError\">52"
+ "@24@?0@\"FPItem\"8Q16"
+ "@48@0:8@16@24Q32@?40"
+ "@56@0:8@16@24Q32@40@?48"
+ "@60@0:8@16@24@32B40Q44@?52"
+ "BRAutoShareAcceptOperation"
+ "BRFeatureFlags"
+ "BRGetCKRecordIDsForFPItems"
+ "BRNSDataWrapper"
+ "Failed to execute lookup query for daemon container: %s"
+ "Got NULL container path for daemon data container %s"
+ "[DEBUG] Auto accepting share link %@%@"
+ "[DEBUG] Failed to consume daemon container sandbox token: (%s)%@"
+ "[DEBUG] Got user container URL %s from containermanagerd%@"
+ "[DEBUG] container_copy_sandbox_token returned NULL!%@"
+ "[ERROR] function not implemented: %@%@"
+ "[ERROR] operation not implemented: %@%@"
+ "_getFirstCloudKitUnderlyingError:"
+ "_isInSyncBubble"
+ "_setError"
+ "_weakObserver"
+ "accountDidChangeWithCellularEnabled:isUnlimitedUpdatesEnabled:reply:"
+ "br_personaIDWithDefault:"
+ "br_suggestedRetryDate"
+ "br_suggestedRetryTimeInterval"
+ "brc_appBundleID"
+ "brc_appContainerID"
+ "brc_applicationBundleIDForExtension:"
+ "brc_applicationContainerIDForExtension:"
+ "brc_errorFunctionNotImplemented:"
+ "brc_errorOperationNotImplemented:"
+ "com.apple.private.clouddocs.auto-accept-share"
+ "com.apple.private.clouddocs.can-get-ckrecordid"
+ "data"
+ "dataWithContentsOfURL:"
+ "fetchItemForURL:completionHandler:"
+ "file-write-data"
+ "getBGSystemTaskActivitiesDefaultConfig:"
+ "getBytes:range:"
+ "getCKRecordIDsForFPItems:reply:"
+ "handleAcceptingCKShareMetadata:reply:"
+ "hasError"
+ "iCloudDrive"
+ "internalDaemonContainerPath"
+ "isReservedMangedID"
+ "position"
+ "printShareRequests:personaID:isPending:asJSON:reply:"
+ "receiveUpdates:reply:"
+ "requestForAccess"
+ "requestForAccessEnabled"
+ "scheduleAction:"
+ "setActionCompletionBlock:"
+ "setPosition:"
+ "startDownloadFileObject:existingContents:options:etagIfLoser:reply:"
+ "startOperation:toAutoAcceptShareLink:reply:"
+ "stringWithCString:encoding:"
+ "updateContentVersion:"
+ "uploadContents:baseVersion:options:reply:"
+ "uploadItemIdentifier:withContents:baseVersion:basedOnOriginalVersion:options:reply:"
+ "v40@0:8@\"NSObject<BROperationClient>\"16@\"NSURL\"24@?<v@?@\"FPSandboxingURLWrapper\"@\"NSError\">32"
+ "v48@0:8@\"NSFileHandle\"16@\"NSString\"24B32B36@?<v@?@\"NSError\">40"
+ "v48@0:8@16@24B32B36@?40"
+ "writeData:toURL:atomically:"
+ "writeToURL:atomically:"
- "+[BRFileObjectID fileObjectIDForURL:allocateDocID:error:]"
- "-[BRDaemonConnection newLegacySyncProxy]"
- "-[BRNotificationReceiver receiveUpdates:logicalExtensions:physicalExtensions:reply:]"
- "-[BRNotificationReceiver receiveUpdates:logicalExtensions:physicalExtensions:reply:]_block_invoke"
- "-[BROperation remoteLegacyObject]"
- "3437.120.20"
- "<doc-id %x>"
- "<ino %llx>"
- "@\"NSProgress\"48@0:8@\"BRFileObjectID\"16Q24@\"NSString\"32@?<v@?@\"NSDictionary\"@\"NSError\">40"
- "@\"NSProgress\"52@0:8@\"NSString\"16@\"NSSecurityScopedURLWrapper\"24@\"NSFileProviderItemVersion\"32B40@?<v@?@\"NSFileProviderItemVersion\"@\"NSError\">44"
- "@48@0:8@16Q24@32@?40"
- "@52@0:8@16@24@32B40@?44"
- "BRDocObjectID"
- "BREvictItemAtURL"
- "BRInodeObjectID"
- "BRProtocolLegacy"
- "BRQueryStitching"
- "BRShareOperationLegacyProtocol"
- "Vv20@0:8B16"
- "[CRIT] UNREACHABLE: Can't use the legacy sync proxy when fpfs is enabled%@"
- "[DEBUG] Failed evicting url %@ - %@%@"
- "[DEBUG] received extensions\nlogical:%@\nphysical:%@%@"
- "[WARNING] Can't read xattr at '%s' %{errno}d%@"
- "_docID"
- "_ino"
- "accountDidChangeWithCellularEnabled:reply:"
- "boostFilePresenterAtURL:reply:"
- "broken legacy proxy"
- "capabilityWhenTryingToReparentItemAtURL:toNewParent:reply:"
- "checkIfItemIsShareableWithInode:reply:"
- "checkinAskClientIfUsingUbiquity:"
- "copyBulkShareIDsAtURLs:reply:"
- "copyCollaborationIdentifierForItemAtURL:reply:"
- "createSharingInfoForURL:reply:"
- "d%x"
- "decodeInt32ForKey:"
- "didEndPossibleFileOperation:"
- "encodeInt32:forKey:"
- "enumerateAllFoldersWithSortOrder:offset:limit:completion:"
- "evictItemAtURL:options:reply:"
- "fetchLatestVersionForFileAtURL:reply:"
- "fileObjectIDForURL:allocateDocID:error:"
- "forceConflictForURL:bookmarkData:forcedEtag:reply:"
- "gatherInformationForPath:reply:"
- "getAttributeValues:forItemAtURL:reply:"
- "getBackReferencingContainerIDsForURLs:reply:"
- "getBookmarkDataForURL:onlyAllowItemKnowByServer:allowAccessByBundleID:reply:"
- "getCreatorNameComponentsForURL:reply:"
- "getEvictableSpaceWithReply:"
- "getNonLocalVersionSenderWithReceiver:documentURL:includeCachedVersions:reply:"
- "getPausedFilesList:reply:"
- "getPublishedURLForItemAtURL:forStreaming:requestedTTL:reply:"
- "getQueryItemForURL:reply:"
- "getURLForItemIdentifier:reply:"
- "getiWorkNeedsShareMigrateAtURL:reply:"
- "getiWorkPublishingBadgingStatusAtURL:reply:"
- "getiWorkPublishingInfoAtURL:reply:"
- "i%llx"
- "initWithDocID:"
- "initWithDocIDNumber:"
- "initWithFileID:"
- "listFilesIngested:reply:"
- "moveBRSecurityBookmarkAtURL:toURL:reply:"
- "newLegacySyncProxy"
- "overwriteAccessTimeForItemAtURL:atime:reply:"
- "pauseSyncForFileAtURL:timeout:options:reply:"
- "presentAcceptDialogsForShareMetadata:reply:"
- "readerThrottleBackoffForDocumentAtPath:containerID:reply:"
- "receiveUpdates:logicalExtensions:physicalExtensions:reply:"
- "removeItemFromDisk:reply:"
- "resolveConflictWithName:atURL:reply:"
- "resolveFileObjectIDToURL:reply:"
- "resumeSyncForFileAtURL:dropLocalChanges:reply:"
- "scheduleDeepScanForContainer:reply:"
- "setiWorkPublishingInfoAtURL:publish:readonly:reply:"
- "startDownloadFileObject:options:etagIfLoser:reply:"
- "startDownloadItemsAtURLs:options:reply:"
- "startOperation:toCopyEtagAtURL:reply:"
- "startOperation:toCopyParticipantTokenAtURL:reply:"
- "startOperation:toCopyShareInfoAtURL:reply:"
- "startOperation:toCopySharingAccessToken:reply:"
- "startOperation:toCopySharingInfoAtURL:reply:"
- "startOperation:toCopyShortTokenAtURL:reply:"
- "startOperation:toDownloadItemAtURL:readingOptions:wantsCurrentVersion:reply:"
- "startOperation:toEvictItemAtURL:reply:"
- "startOperation:toModifyRecordAccessAtURL:allowAccess:reply:"
- "startOperation:toPrepFolderForSharingAt:reply:"
- "startOperation:toProcessSubitemsAtURL:maxSubsharesFailures:processType:reply:"
- "thumbnailChangedForItemAtURL:reply:"
- "trashItemAtURL:reply:"
- "unlimitedUpdatesOverCellularWithEnablementStatus:reply:"
- "updateItemFromURL:reply:"
- "uploadItemIdentifier:withContents:baseVersion:basedOnOriginalVersion:reply:"
- "v"
- "v32@0:8@\"BRFileObjectID\"16@?<v@?@\"NSURL\"@\"NSData\"@\"NSURL\"@\"NSData\"@\"NSError\">24"
- "v32@0:8@\"BRGetPausedFileListUpdater\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSArray\"16@?<v@?@\"NSArray\"@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSURL\"@\"NSError\">24"
- "v32@0:8@\"NSURL\"16@?<v@?@\"BRQueryItem\"@\"NSError\">24"
- "v32@0:8@\"NSURL\"16@?<v@?@\"CKShare\"@\"NSError\">24"
- "v32@0:8@\"NSURL\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSURL\"16@?<v@?@\"NSPersonNameComponents\"@\"NSError\">24"
- "v32@0:8@\"NSURL\"16@?<v@?@\"NSString\"@\"NSError\">24"
- "v32@0:8@\"NSURL\"16@?<v@?@\"NSURL\"@\"NSError\">24"
- "v32@0:8@\"NSURL\"16@?<v@?B@\"NSError\">24"
- "v32@0:8@\"NSURL\"16@?<v@?BB@\"NSString\"@\"NSError\">24"
- "v32@0:8@\"NSURL\"16@?<v@?i@\"NSError\">24"
- "v32@0:8Q16@?<v@?B@\"NSError\">24"
- "v36@0:8@\"NSURL\"16B24@?<v@?@\"NSError\">28"
- "v40@0:8@\"NSArray\"16@\"NSURL\"24@?<v@?@\"NSMutableDictionary\"@\"NSError\">32"
- "v40@0:8@\"NSArray\"16Q24@?<v@?@\"NSError\">32"
- "v40@0:8@\"NSObject<BROperationClient>\"16@\"NSURL\"24@?<v@?@\"CKShare\"@\"NSURL\"@\"NSError\">32"
- "v40@0:8@\"NSObject<BROperationClient>\"16@\"NSURL\"24@?<v@?@\"NSData\"@\"NSString\"@\"NSError\">32"
- "v40@0:8@\"NSObject<BROperationClient>\"16@\"NSURL\"24@?<v@?@\"NSError\">32"
- "v40@0:8@\"NSObject<BROperationClient>\"16@\"NSURL\"24@?<v@?@\"NSString\"@\"NSError\">32"
- "v40@0:8@\"NSObject<BROperationClient>\"16@\"NSURL\"24@?<v@?@\"NSString\"@\"NSString\"@\"NSError\">32"
- "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?d@\"NSError\">32"
- "v40@0:8@\"NSString\"16@\"NSURL\"24@?<v@?@\"NSError\">32"
- "v40@0:8@\"NSURL\"16@\"NSURL\"24@?<v@?@\"NSError\">32"
- "v40@0:8@\"NSURL\"16@\"NSURL\"24@?<v@?S@\"NSError\">32"
- "v40@0:8@\"NSURL\"16B24B28@?<v@?@\"NSError\">32"
- "v40@0:8@\"NSURL\"16Q24@?<v@?@\"NSError\">32"
- "v44@0:8@\"<BRNonLocalVersionReceiving>\"16@\"NSURL\"24B32@?<v@?@\"<BRNonLocalVersionSending>\"@\"NSURL\"@\"NSError\">36"
- "v44@0:8@\"NSObject<BROperationClient>\"16@\"NSURL\"24B32@?<v@?@\"NSData\"@\"NSString\"@\"NSError\">36"
- "v44@0:8@\"NSURL\"16B24@\"NSString\"28@?<v@?@\"NSString\"@\"NSString\"@\"NSError\">36"
- "v44@0:8@\"NSURL\"16B24Q28@?<v@?@\"NSURL\"@\"NSDate\"@\"NSError\">36"
- "v44@0:8@16B24@28@?36"
- "v44@0:8C16Q20Q28@?36"
- "v44@0:8C16Q20Q28@?<v@?@\"NSArray\"Q@\"NSError\">36"
- "v48@0:8@\"NSArray\"16@\"NSDictionary\"24@\"NSDictionary\"32@?<v@?>40"
- "v48@0:8@\"NSURL\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSError\">40"
- "v48@0:8@\"NSURL\"16d24q32@?<v@?@\"NSError\">40"
- "v48@0:8@16@24@32@?40"
- "v48@0:8@16d24q32@?40"
- "v52@0:8@\"NSObject<BROperationClient>\"16@\"NSURL\"24Q32B40@?<v@?@\"NSError\">44"
- "v52@0:8@16@24Q32B40@?44"
- "v56@0:8@\"NSObject<BROperationClient>\"16@\"NSURL\"24Q32Q40@?<v@?@\"NSError\">48"
- "waitForFileSystemChangeProcessingWithReply:"
- "willBeginPossibleCreationOfItemAtURL:"
- "willBeginPossibleDeletionOfItemAtURL:"
- "willBeginPossibleMoveOfItemAtURL:toURL:"

```
