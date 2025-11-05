## com.apple.CloudDocs.iCloudDriveFileProvider

> `/System/Library/PrivateFrameworks/CloudDocs.framework/PlugIns/com.apple.CloudDocs.iCloudDriveFileProvider.appex/Contents/MacOS/com.apple.CloudDocs.iCloudDriveFileProvider`

```diff

-3097.81.2.0.0
-  __TEXT.__text: 0x2d1c0
-  __TEXT.__auth_stubs: 0x4b0
-  __TEXT.__objc_stubs: 0x2d60
-  __TEXT.__objc_methlist: 0x11a4
+3437.101.1.0.0
+  __TEXT.__text: 0x2c7f0
+  __TEXT.__auth_stubs: 0x470
+  __TEXT.__objc_stubs: 0x2c60
+  __TEXT.__objc_methlist: 0x1e5c
   __TEXT.__const: 0xb0
-  __TEXT.__gcc_except_tab: 0x2c50
-  __TEXT.__objc_methname: 0x5350
-  __TEXT.__cstring: 0x45d4
-  __TEXT.__oslogstring: 0x2378
-  __TEXT.__objc_classname: 0x811
-  __TEXT.__objc_methtype: 0x359b
-  __TEXT.__unwind_info: 0xac8
-  __DATA_CONST.__auth_got: 0x268
-  __DATA_CONST.__got: 0x288
-  __DATA_CONST.__const: 0x1290
-  __DATA_CONST.__cfstring: 0x3c0
-  __DATA_CONST.__objc_classlist: 0x100
-  __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x108
+  __TEXT.__gcc_except_tab: 0x2dd8
+  __TEXT.__objc_methname: 0x5306
+  __TEXT.__cstring: 0x46ab
+  __TEXT.__oslogstring: 0x2529
+  __TEXT.__objc_classname: 0x78a
+  __TEXT.__objc_methtype: 0x35b6
+  __TEXT.__unwind_info: 0xaf0
+  __DATA_CONST.__auth_got: 0x248
+  __DATA_CONST.__got: 0x278
+  __DATA_CONST.__const: 0x1270
+  __DATA_CONST.__cfstring: 0x2e0
+  __DATA_CONST.__objc_classlist: 0xf0
+  __DATA_CONST.__objc_catlist: 0x10
+  __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0xe0
-  __DATA.__objc_const: 0xa538
-  __DATA.__objc_selrefs: 0xe98
-  __DATA.__objc_ivar: 0x148
-  __DATA.__objc_data: 0xa00
-  __DATA.__data: 0xc60
-  __DATA.__bss: 0xa8
+  __DATA_CONST.__objc_superrefs: 0xd0
+  __DATA.__objc_const: 0x8300
+  __DATA.__objc_selrefs: 0x1278
+  __DATA.__objc_ivar: 0x140
+  __DATA.__objc_data: 0x960
+  __DATA.__data: 0xba0
+  __DATA.__bss: 0xb0
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/ApplicationServices.framework/Versions/A/ApplicationServices

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: D5C91F27-B7B3-3A43-88B2-3EC3E42C90FD
-  Functions: 698
-  Symbols:   183
-  CStrings:  1519
+  UUID: 6E02AE65-8916-31C6-BF13-54C5DCBFDF39
+  Functions: 668
+  Symbols:   161
+  CStrings:  1487
 
Symbols:
+ _NSProgressFileOperationKindUploading
+ _NSProgressKindFile
+ _OBJC_CLASS_$_BRReachabilityMonitor
+ _abc_report_panic_with_signature
+ _brc_append_system_info_to_message
+ _objc_opt_isKindOfClass
- OBJC_IVAR_$_BRFieldContentSignature._contentSignature
- OBJC_IVAR_$_BRFieldContentSignature._has
- OBJC_IVAR_$_BRFieldContentSignature._oldVersionIdentifier
- OBJC_IVAR_$_BRFieldContentSignature._size
- OBJC_IVAR_$_BRFieldContentSignature._versionIdentifier
- OBJC_IVAR_$_BRFieldStructureSignature._oldVersionIdentifier
- OBJC_IVAR_$_BRFieldStructureSignature._versionIdentifier
- OBJC_IVAR_$_PBDataReader._bytes
- OBJC_IVAR_$_PBDataReader._error
- OBJC_IVAR_$_PBDataReader._length
- OBJC_IVAR_$_PBDataReader._pos
- _BRFieldContentSignatureReadFrom
- _BRFieldStructureSignatureReadFrom
- _FPIsCloudDocsWithFPFSEnabled
- _OBJC_CLASS_$_BRFieldStructureSignature
- _OBJC_CLASS_$_NSFileProviderItemVersion
- _OBJC_CLASS_$_NSNumber
- _OBJC_CLASS_$_PBCodable
- _OBJC_METACLASS_$_BRFieldContentSignature
- _OBJC_METACLASS_$_BRFieldStructureSignature
- _OBJC_METACLASS_$_PBCodable
- _PBDataWriterWriteDataField
- _PBDataWriterWriteInt64Field
- _PBDataWriterWriteStringField
- _PBReaderReadData
- _PBReaderReadString
- _PBReaderSkipValueWithTag
- _kBRCMachServiceName
CStrings:
+ "!"
+ "+[BRDaemonConnection(FPFSExtensionAdditions) registerPersonaDomainIdentifer:databaseID:delegate:]"
+ "+[BRDaemonConnection(FPFSExtensionAdditions) unregisterPersonaDomainIdentifierAndDatabaseIDForDelegate:]"
+ "-[BRDaemonConnection(FPFSExtensionAdditions) validateConnectionExtensionInfoForPersonaID:]"
+ "-[BRDaemonConnection(FPFSExtensionAdditions) validateConnectionExtensionInfoForPersonaID:]_block_invoke"
+ "-[BRICDExtensionInfo refreshDatabaseID]"
+ "-[ICDFileEnumerator initWithFileObjectID:itemIdentifier:recursive:request:fileProviderManager:]_block_invoke"
+ "-[ICDFileProviderExtension _refreshDatabaseIDForcingRefresh:]"
+ "-[ICDFileProviderExtension _waitForDomainSetup]"
+ "/AppleInternal/Library/BuildRoots/656826c2-0194-11f0-9fc9-122ba06eff56/Library/Caches/com.apple.xbs/Sources/CloudDocs_executables/os-plugins/fileprovider-extension-iclouddrive/BRDaemonConnection+FPFSExtensionAdditions.m"
+ "<%@: %p dom:%@ dat:%@>"
+ "@\"NSProgress\"52@0:8@\"NSString\"16@\"NSSecurityScopedURLWrapper\"24@\"NSFileProviderItemVersion\"32B40@?<v@?@\"NSFileProviderItemVersion\"@\"NSError\">44"
+ "@20@0:8B16"
+ "@52@0:8@16@24@32B40@?44"
+ "@52@0:8@16@24B32@36@44"
+ "BRICDExtensionInfo"
+ "BRICDExtensionInfoDelegate"
+ "Can't add domain info for persona when one already exists!"
+ "T@\"NSHashTable\",R,N,V_delegates"
+ "T@\"NSString\",R,N,V_databaseID"
+ "T@\"NSString\",R,N,V_domainIdentifier"
+ "[CRIT] %@%@"
+ "[CRIT] Assertion failed: _finishedDomainSetup%@"
+ "[CRIT] Assertion failed: extensionInfo%@"
+ "[CRIT] UNREACHABLE: Can't locate domain identifier. Exiting the extension%@"
+ "[CRIT] UNREACHABLE: No delegate %@ found in extensionInfo %@%@"
+ "[DEBUG] %@ - Registered connection with %@%@"
+ "[DEBUG] Added delegate %@ to existing extension infos %@%@"
+ "[DEBUG] Got an error while computing URL item identifier %@%@"
+ "[DEBUG] Refreshing databaseID because it's nil%@"
+ "[DEBUG] Registered extensionInfo %@ for persona %@ for delegate %@%@"
+ "[DEBUG] Removed delegate %@ from extensionInfo %@%@"
+ "[DEBUG] Should not download speculative items on cellular network%@"
+ "[DEBUG] Unregistered extension info for persona %@%@"
+ "[DEBUG] Updated databaseID from %@ to %@%@"
+ "[DEBUG] We still have registered extension instances for persona %@%@"
+ "[ERROR] Can't validate connection without extension info for persona %@ existing infos %@%@"
+ "[ERROR] Received reply that we can't register connection with %@ - %@%@"
+ "_databaseID"
+ "_delegates"
+ "_finishedDomainSetup"
+ "_refreshDatabaseIDForcingRefresh:"
+ "_waitForDomainSetup"
+ "boolValue"
+ "br_contentEtag"
+ "br_contentSignature"
+ "br_fileProviderErrorForDownloadFlow"
+ "br_isCocoaErrorCode:"
+ "br_structureEtag"
+ "brc_errorShouldNotDownloadOverCellular"
+ "databaseID"
+ "defaultConnectionIfExists"
+ "defaultConnectionIfExistsForPersonaID:"
+ "delegates"
+ "getAvailableBytesForUploadOverCellularWithReply:"
+ "getEnhancedDrivePrivacyStatusForContainer:onServer:reply:"
+ "getIdentifierForUserVisibleFileAtURL:completionHandler:"
+ "initWithDomainIdentifier:databaseID:delegate:"
+ "initWithFileObjectID:itemIdentifier:recursive:fileProviderManager:"
+ "initWithFileObjectID:itemIdentifier:recursive:request:fileProviderManager:"
+ "initWithFileProviderManager:"
+ "isCellularNetwork"
+ "isEqualToExtensionInfo:"
+ "lookupCollectionGathererPacerMinFireInterval:"
+ "overrideUploadOnCellularConstraintsWithReply:"
+ "refreshDatabaseID"
+ "registerPersonaDomainIdentifer:databaseID:delegate:"
+ "result"
+ "secondaryConnectionIfExists"
+ "secondaryConnectionIfExistsForPersonaID:"
+ "setBoolResult:error:"
+ "setEnhancedDrivePrivacySupported:forContainer:reply:"
+ "setFileOperationKind:"
+ "setKind:"
+ "sharedReachabilityMonitor"
+ "totalUnitCount"
+ "unlimitedUpdatesOverCellularWithEnablementStatus:reply:"
+ "unregisterPersonaDomainIdentifierAndDatabaseIDForDelegate:"
+ "uploadItemIdentifier:withContents:baseVersion:basedOnOriginalVersion:reply:"
+ "v36@0:8@\"NSString\"16B24@?<v@?B@\"NSError\">28"
+ "v36@0:8B16@\"NSString\"20@?<v@?@\"NSError\">28"
+ "v36@0:8B16@20@?28"
+ "v40@0:8@16@24@32"
+ "validateConnectionDomainWithDomainIdentifier:databaseID:reply:"
+ "validateConnectionExtensionInfoForPersonaID:"
+ "weakObjectsHashTable"
- "%@ %@"
- "+[ICDFileProviderExtension initialize]"
- "-[BRDaemonConnection(FPFSExtensionAdditions) _initUsingUserLocalDaemonWithDomainIdentifier:databaseID:backChannel:]_block_invoke"
- "-[BRFieldContentSignature writeTo:]"
- "-[BRFieldContentSignature(BRAdditions) isEquivalentToSignature:]"
- "-[BRFieldStructureSignature writeTo:]"
- "-[ICDFileEnumerator initWithFileObjectID:itemIdentifier:recursive:request:]_block_invoke"
- "-[ICDFileProviderExtension _startWaitingForDomainToBeFullySetup]_block_invoke"
- "-[ICDFileProviderExtension initWithDomain:]"
- ";"
- "<ct %@|%@ sz:%llu sig:%@>"
- "<st %@|%@>"
- "@\"BRDaemonConnection\"8@?0"
- "@\"NSProgress\"48@0:8@\"NSString\"16@\"NSSecurityScopedURLWrapper\"24@\"NSFileProviderItemVersion\"32@?<v@?@\"NSFileProviderItemVersion\"@\"NSError\">40"
- "@36@0:8@16@24B32"
- "BRAdditions"
- "BRFieldContentSignature"
- "BRFieldContentSignature.m"
- "BRFieldStructureSignature"
- "BRFieldStructureSignature.m"
- "BRFieldVersionSignature"
- "BRFileProviderExtensionBackChannel"
- "BRItemAdditions"
- "ICDFileProviderExtensionBackChannel"
- "NSCopying"
- "Q24@0:8@16"
- "T@\"NSData\",&,N,V_contentSignature"
- "T@\"NSString\",&,N,V_oldVersionIdentifier"
- "T@\"NSString\",&,N,V_versionIdentifier"
- "T@\"NSString\",R,N"
- "TB,N"
- "TB,R,N"
- "Tq,N,V_size"
- "[%@,%@]"
- "[CRIT] UNREACHABLE: Signatures are equivalent but content is different %@ vs %@%@"
- "[DEBUG] %@ - Registered connection with domainID %@%@"
- "[DEBUG] FPFS is not enabled%@"
- "[DEBUG] Found Database ID after %lu retries%@"
- "[DEBUG] Unexpected import notification on non-ciconia domain%@"
- "[ERROR] Received reply that we can't register connection with domainID %@ - %@%@"
- "[ERROR] can't register connection with domainID %@ - %@%@"
- "[WARNING] Didn't find Database ID after %lu retries%@"
- "[WARNING] Not allowing fpfs domain (%@) to start when not running fpfs%@"
- "_contentSignature"
- "_extension"
- "_has"
- "_initUsingUserLocalDaemonWithDomainIdentifier:databaseID:backChannel:"
- "_localEditCounter"
- "_oldVersionEtag"
- "_oldVersionIdentifier"
- "_oldVersionLocalEditCounter"
- "_setupAndResumeForKey:"
- "_size"
- "_versionIdentifier"
- "allocWithZone:"
- "br_sharedProviderManager"
- "br_sharedProviderManagerWithDomainID:"
- "brc_signatureIsPackage"
- "componentsSeparatedByString:"
- "contentSignature"
- "copyTo:"
- "defaultConnectionForKey:initializer:"
- "defaultConnectionIfExistsForKey:"
- "defaultConnectionIfExistsWithDomainIdentifier:"
- "defaultConnectionWithDomainIdentifier:databaseID:backChannel:"
- "dictionary"
- "dictionaryRepresentation"
- "etag"
- "hasContentSignature"
- "hasOldVersionIdentifier"
- "hasSize"
- "initWithExtension:"
- "initWithFileObjectID:itemIdentifier:recursive:"
- "initWithFileObjectID:itemIdentifier:recursive:request:"
- "initWithMachServiceName:options:"
- "initialize"
- "isEquivalentToSignature:"
- "length"
- "localEditCounterFromVersionIdentifier:"
- "longLongValue"
- "mergeFrom:"
- "metadataVersion"
- "nil != self->_versionIdentifier"
- "numberWithLongLong:"
- "objectAtIndex:"
- "oldVersionIdentifier"
- "q"
- "q16@0:8"
- "readFrom:"
- "secondaryConnectionForKey:initializer:"
- "secondaryConnectionIfExistsForKey:"
- "secondaryConnectionIfExistsWithDomainIdentifier:"
- "secondaryConnectionWithDomainIdentifier:databaseID:backChannel:"
- "setContentSignature:"
- "setHasSize:"
- "setOldVersionIdentifier:"
- "setSize:"
- "setVersionIdentifier:"
- "size"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "uploadItemIdentifier:withContents:baseVersion:reply:"
- "v24@0:8q16"
- "v48@0:8@\"NSString\"16@\"NSString\"24@\"<BRFileProviderExtensionBackChannel>\"32@?<v@?@\"NSError\">40"
- "validateConnectionDomainWithDomainIdentifier:databaseID:backChannel:reply:"
- "versionIdentifier"
- "writeTo:"
- "{?=\"size\"b1}"

```
