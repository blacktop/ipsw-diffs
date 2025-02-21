## com.apple.CloudDocs.iCloudDriveFileProvider

> `/System/Library/PrivateFrameworks/CloudDocs.framework/PlugIns/com.apple.CloudDocs.iCloudDriveFileProvider.appex/com.apple.CloudDocs.iCloudDriveFileProvider`

```diff

-3097.82.2.0.0
-  __TEXT.__text: 0x28510
-  __TEXT.__auth_stubs: 0x660
-  __TEXT.__objc_stubs: 0x2ce0
-  __TEXT.__objc_methlist: 0x1184
+3437.100.323.0.5
+  __TEXT.__text: 0x2778c
+  __TEXT.__auth_stubs: 0x610
+  __TEXT.__objc_stubs: 0x2b40
+  __TEXT.__objc_methlist: 0x1dc4
   __TEXT.__const: 0xb0
-  __TEXT.__gcc_except_tab: 0x2c2c
-  __TEXT.__objc_methname: 0x515d
-  __TEXT.__cstring: 0x45bf
-  __TEXT.__oslogstring: 0x2315
-  __TEXT.__objc_classname: 0x7c4
+  __TEXT.__gcc_except_tab: 0x2da8
+  __TEXT.__objc_methname: 0x50ac
+  __TEXT.__cstring: 0x464c
+  __TEXT.__oslogstring: 0x2488
+  __TEXT.__objc_classname: 0x73d
   __TEXT.__objc_methtype: 0x3491
-  __TEXT.__unwind_info: 0xa88
-  __DATA_CONST.__auth_got: 0x340
-  __DATA_CONST.__got: 0x278
-  __DATA_CONST.__const: 0x1048
-  __DATA_CONST.__cfstring: 0x360
-  __DATA_CONST.__objc_classlist: 0x100
-  __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0xf8
+  __TEXT.__unwind_info: 0xaa8
+  __DATA_CONST.__auth_got: 0x318
+  __DATA_CONST.__got: 0x258
+  __DATA_CONST.__const: 0x1000
+  __DATA_CONST.__cfstring: 0x280
+  __DATA_CONST.__objc_classlist: 0xf0
+  __DATA_CONST.__objc_catlist: 0x10
+  __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0xe0
-  __DATA.__objc_const: 0xa288
-  __DATA.__objc_selrefs: 0xe60
-  __DATA.__objc_ivar: 0x148
-  __DATA.__objc_data: 0xa00
-  __DATA.__data: 0xba0
-  __DATA.__bss: 0xa8
+  __DATA_CONST.__objc_superrefs: 0xd0
+  __DATA.__objc_const: 0x8180
+  __DATA.__objc_selrefs: 0x11f0
+  __DATA.__objc_ivar: 0x140
+  __DATA.__objc_data: 0x960
+  __DATA.__data: 0xae0
+  __DATA.__bss: 0xb0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 656
-  Symbols:   208
-  CStrings:  1470
+  Functions: 624
+  Symbols:   183
+  CStrings:  1438
 
Symbols:
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
- _objc_retain_x27
CStrings:
+ "\x02\x12\x11"
+ "\x05D\x11"
+ "!"
+ "+[BRDaemonConnection(FPFSExtensionAdditions) registerPersonaDomainIdentifer:databaseID:delegate:]"
+ "+[BRDaemonConnection(FPFSExtensionAdditions) unregisterPersonaDomainIdentifierAndDatabaseIDForDelegate:]"
+ "-[BRDaemonConnection(FPFSExtensionAdditions) validateConnectionExtensionInfoForPersonaID:]"
+ "-[BRDaemonConnection(FPFSExtensionAdditions) validateConnectionExtensionInfoForPersonaID:]_block_invoke"
+ "-[BRICDExtensionInfo refreshDatabaseID]"
+ "-[ICDFileEnumerator initWithFileObjectID:itemIdentifier:recursive:request:fileProviderManager:]_block_invoke"
+ "-[ICDFileProviderExtension _refreshDatabaseIDForcingRefresh:]"
+ "-[ICDFileProviderExtension _waitForDomainSetup]"
+ "/Library/Caches/com.apple.xbs/Sources/CloudDocs_plugins/os-plugins/fileprovider-extension-iclouddrive/BRDaemonConnection+FPFSExtensionAdditions.m"
+ "<%@: %p dom:%@ dat:%@>"
+ "@20@0:8B16"
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
+ "accountDidChangeWithCellularEnabled:reply:"
+ "boolValue"
+ "br_contentEtag"
+ "br_contentSignature"
+ "br_fileProviderErrorForDownloadFlow"
+ "br_structureEtag"
+ "brc_errorShouldNotDownloadOverCellular"
+ "databaseID"
+ "defaultConnectionIfExists"
+ "defaultConnectionIfExistsForPersonaID:"
+ "delegates"
+ "getAvailableBytesForUploadOverCellularWithReply:"
+ "getEnhancedDrivePrivacyStatusForContainer:onServer:reply:"
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
+ "sharedReachabilityMonitor"
+ "unlimitedUpdatesOverCellularWithEnablementStatus:reply:"
+ "unregisterPersonaDomainIdentifierAndDatabaseIDForDelegate:"
+ "v36@0:8@\"NSString\"16B24@?<v@?B@\"NSError\">28"
+ "v36@0:8B16@\"NSString\"20@?<v@?@\"NSError\">28"
+ "v36@0:8B16@20@?28"
+ "v40@0:8@16@24@32"
+ "validateConnectionDomainWithDomainIdentifier:databaseID:reply:"
+ "validateConnectionExtensionInfoForPersonaID:"
+ "weakObjectsHashTable"
- "\x02\x13"
- "\x05D"
- "\x13"
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
- "v24@0:8q16"
- "v48@0:8@\"NSString\"16@\"NSString\"24@\"<BRFileProviderExtensionBackChannel>\"32@?<v@?@\"NSError\">40"
- "validateConnectionDomainWithDomainIdentifier:databaseID:backChannel:reply:"
- "versionIdentifier"
- "writeTo:"
- "{?=\"size\"b1}"

```
