## DiagnosticExtensions

> `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/DiagnosticExtensions`

```diff

-138.0.0.0.0
-  __TEXT.__text: 0x169e0
-  __TEXT.__auth_stubs: 0x960
-  __TEXT.__objc_methlist: 0x10ac
-  __TEXT.__const: 0x120
-  __TEXT.__cstring: 0x103a
-  __TEXT.__oslogstring: 0x291f
-  __TEXT.__gcc_except_tab: 0x5a8
-  __TEXT.__unwind_info: 0x6d8
-  __TEXT.__objc_classname: 0x229
-  __TEXT.__objc_methname: 0x3132
-  __TEXT.__objc_methtype: 0x591
-  __TEXT.__objc_stubs: 0x2540
-  __DATA_CONST.__got: 0x228
-  __DATA_CONST.__const: 0x700
-  __DATA_CONST.__objc_classlist: 0xa8
+146.0.0.0.0
+  __TEXT.__text: 0x17b0c
+  __TEXT.__objc_methlist: 0x121c
+  __TEXT.__const: 0x13a
+  __TEXT.__oslogstring: 0x32b9
+  __TEXT.__cstring: 0x1256
+  __TEXT.__gcc_except_tab: 0x50c
+  __TEXT.__unwind_info: 0x6b0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x770
+  __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xce0
+  __DATA_CONST.__objc_selrefs: 0xdb0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_arraydata: 0xc0
-  __AUTH_CONST.__auth_got: 0x4c0
-  __AUTH_CONST.__const: 0x360
-  __AUTH_CONST.__cfstring: 0xf40
-  __AUTH_CONST.__objc_const: 0x25e8
-  __AUTH_CONST.__objc_intobj: 0x18
+  __DATA_CONST.__got: 0x240
+  __AUTH_CONST.__const: 0x3a0
+  __AUTH_CONST.__cfstring: 0x10e0
+  __AUTH_CONST.__objc_const: 0x27a0
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __DATA.__objc_ivar: 0xc8
+  __AUTH_CONST.__objc_intobj: 0x18
+  __AUTH_CONST.__auth_got: 0x590
+  __DATA.__objc_ivar: 0xd0
   __DATA.__data: 0x2a0
-  __DATA.__bss: 0x10
-  __DATA_DIRTY.__objc_data: 0x690
-  __DATA_DIRTY.__bss: 0xd8
+  __DATA.__bss: 0x20
+  __DATA_DIRTY.__objc_data: 0x730
+  __DATA_DIRTY.__bss: 0xe8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
-  - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/Bom.framework/Bom
   - /System/Library/PrivateFrameworks/LoggingSupport.framework/LoggingSupport
   - /System/Library/PrivateFrameworks/PlugInKit.framework/PlugInKit
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
+  - /usr/lib/libAppleArchive.dylib
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4DCA04C4-4FA4-3218-9A5E-B5F49970604B
-  Functions: 526
-  Symbols:   2027
-  CStrings:  1122
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  UUID: 76EDE35A-1310-362A-8BE2-4505487EAB7D
+  Functions: 591
+  Symbols:   2248
+  CStrings:  570
 
Symbols:
+ +[DEAppleArchiveReader extractArchiveAt:toDirectory:error:]
+ +[DEAppleArchiveReader extractArchiveAt:toDirectory:error:].cold.1
+ +[DEAppleArchiveReader extractArchiveAt:toDirectory:error:].cold.2
+ +[DEAppleArchiveReader extractArchiveAt:toDirectory:error:].cold.3
+ +[DEAppleArchiveReader extractArchiveAt:toDirectory:error:].cold.4
+ +[DEAppleArchiveReader extractArchiveAt:toDirectory:error:].cold.5
+ +[DEAppleArchiveReader extractArchiveAt:toDirectory:error:].cold.6
+ +[DEAppleArchiveReader listContentsOfArchive:error:]
+ +[DEAppleArchiveReader listContentsOfArchive:error:].cold.1
+ +[DEAppleArchiveReader listContentsOfArchive:error:].cold.2
+ +[DEAppleArchiveReader listContentsOfArchive:error:].cold.3
+ +[DEAppleArchiveReader listContentsOfArchive:error:].cold.4
+ +[DEAppleArchiveReader openArchiveDecoderForArchive:readStream:decompressionStream:decoder:error:]
+ +[DEAppleArchiveReader openArchiveDecoderForArchive:readStream:decompressionStream:decoder:error:].cold.1
+ +[DEAppleArchiveReader openArchiveDecoderForArchive:readStream:decompressionStream:decoder:error:].cold.2
+ +[DEAppleArchiveReader openArchiveDecoderForArchive:readStream:decompressionStream:decoder:error:].cold.3
+ +[DEAppleArchiveReader openArchiveDecoderForArchive:readStream:decompressionStream:decoder:error:].cold.4
+ +[DEAppleArchiver archiveDirectoryAt:]
+ +[DEAppleArchiver archiveDirectoryAt:deleteOriginal:]
+ +[DEAppleArchiver archiveDirectoryAt:deleteOriginal:progressHandler:]
+ +[DEAppleArchiver archiveFile:]
+ +[DEAppleArchiver archiveFile:deleteOriginal:]
+ +[DEAppleArchiver archiveFile:deleteOriginal:progressHandler:]
+ +[DEAppleArchiver archiveFile:deleteOriginal:progressHandler:].cold.1
+ +[DEAppleArchiver compressWithAppleArchive:deleteOriginal:progressHandler:]
+ +[DEAppleArchiver compressWithAppleArchive:deleteOriginal:progressHandler:].cold.1
+ +[DEAppleArchiver compressWithAppleArchive:deleteOriginal:progressHandler:].cold.10
+ +[DEAppleArchiver compressWithAppleArchive:deleteOriginal:progressHandler:].cold.11
+ +[DEAppleArchiver compressWithAppleArchive:deleteOriginal:progressHandler:].cold.12
+ +[DEAppleArchiver compressWithAppleArchive:deleteOriginal:progressHandler:].cold.13
+ +[DEAppleArchiver compressWithAppleArchive:deleteOriginal:progressHandler:].cold.14
+ +[DEAppleArchiver compressWithAppleArchive:deleteOriginal:progressHandler:].cold.15
+ +[DEAppleArchiver compressWithAppleArchive:deleteOriginal:progressHandler:].cold.16
+ +[DEAppleArchiver compressWithAppleArchive:deleteOriginal:progressHandler:].cold.2
+ +[DEAppleArchiver compressWithAppleArchive:deleteOriginal:progressHandler:].cold.3
+ +[DEAppleArchiver compressWithAppleArchive:deleteOriginal:progressHandler:].cold.4
+ +[DEAppleArchiver compressWithAppleArchive:deleteOriginal:progressHandler:].cold.5
+ +[DEAppleArchiver compressWithAppleArchive:deleteOriginal:progressHandler:].cold.6
+ +[DEAppleArchiver compressWithAppleArchive:deleteOriginal:progressHandler:].cold.7
+ +[DEAppleArchiver compressWithAppleArchive:deleteOriginal:progressHandler:].cold.8
+ +[DEAppleArchiver compressWithAppleArchive:deleteOriginal:progressHandler:].cold.9
+ +[DEAppleArchiver directorySizeOf:]
+ +[DEUtils copyItem:toDestinationDir:zipped:useAppleArchive:]
+ +[DEUtils copyItem:toDestinationDir:zipped:useAppleArchive:].cold.1
+ +[DEUtils copyItem:toDestinationDir:zipped:useAppleArchive:].cold.2
+ +[DEUtils copyItem:toDestinationDir:zipped:useAppleArchive:].cold.3
+ -[DEAttachmentGroup attachToDestinationDir:useAppleArchive:]
+ -[DEAttachmentGroup attachToDestinationDir:useAppleArchive:].cold.1
+ -[DEAttachmentGroup attachToDestinationDir:useAppleArchive:].cold.2
+ -[DEAttachmentGroup attachToDestinationDir:useAppleArchive:].cold.3
+ -[DEAttachmentItem attachToDestinationDir:useAppleArchive:]
+ -[DEExtension accessBundleWithSynchronousHandler:].cold.5
+ -[DEExtension adapter]
+ -[DEExtension extensionInterruptionHandler]
+ -[DEExtension extensionProcessID]
+ -[DEExtension extensionProxy]
+ -[DEExtension isExtensionKitBacked]
+ -[DEExtension loggingProfileURLs]
+ -[DEExtension setAdapter:]
+ -[DEExtension setExtensionInterruptionHandler:]
+ -[DEExtension setExtensionProxy:]
+ -[DEExtension setIsExtensionKitBacked:]
+ -[DEExtension terminateExtensionProcess]
+ -[DEExtensionContext pingWithHandler:]
+ -[DEExtensionHostContext didReceiveXPCReply]
+ GCC_except_table14
+ GCC_except_table15
+ GCC_except_table19
+ GCC_except_table40
+ GCC_except_table47
+ GCC_except_table49
+ GCC_except_table58
+ GCC_except_table60
+ GCC_except_table9
+ _AAArchiveStreamClose
+ _AAArchiveStreamProcess
+ _AAArchiveStreamReadHeader
+ _AAArchiveStreamWritePathList
+ _AAByteStreamClose
+ _AACompressionOutputStreamOpen
+ _AADecodeArchiveInputStreamOpen
+ _AADecompressionInputStreamOpen
+ _AAEncodeArchiveOutputStreamOpen
+ _AAExtractArchiveOutputStreamOpen
+ _AAFieldKeySetCreateWithString
+ _AAFieldKeySetDestroy
+ _AAFileStreamOpenWithPath
+ _AAHeaderClear
+ _AAHeaderCreate
+ _AAHeaderDestroy
+ _AAHeaderGetFieldString
+ _AAHeaderGetKeyIndex
+ _AAPathListCreateWithDirectoryContents
+ _AAPathListDestroy
+ _DEAppleArchiveErrorDomain
+ _DEExtensionClientEntitlementHostKey
+ _DEExtensionClientEntitlementKey
+ _DEUtilsConnectionHasEntitlement
+ _DEUtilsConnectionHasEntitlement.cold.1
+ _DEUtilsConnectionHasEntitlement.cold.2
+ _Log.once
+ _NSFilePathErrorKey
+ _OBJC_CLASS_$_DEAppleArchiveReader
+ _OBJC_CLASS_$_DEAppleArchiver
+ _OBJC_CLASS_$_NSUUID
+ _OBJC_IVAR_$_DEExtension._adapter
+ _OBJC_IVAR_$_DEExtension._isExtensionKitBacked
+ _OBJC_METACLASS_$_DEAppleArchiveReader
+ _OBJC_METACLASS_$_DEAppleArchiver
+ __OBJC_$_CLASS_METHODS_DEAppleArchiveReader
+ __OBJC_$_CLASS_METHODS_DEAppleArchiver
+ __OBJC_CLASS_RO_$_DEAppleArchiveReader
+ __OBJC_CLASS_RO_$_DEAppleArchiver
+ __OBJC_METACLASS_RO_$_DEAppleArchiveReader
+ __OBJC_METACLASS_RO_$_DEAppleArchiver
+ ___31-[DEExtension checkAndTeardown]_block_invoke.107
+ ___31-[DEExtension checkAndTeardown]_block_invoke_2.108
+ ___35-[DEExtension initWithNSExtension:]_block_invoke.74
+ ___38-[DEExtension performWithHostContext:]_block_invoke.100
+ ___38-[DEExtension performWithHostContext:]_block_invoke.97
+ ___38-[DEExtension performWithHostContext:]_block_invoke.98
+ ___38-[DEExtension performWithHostContext:]_block_invoke.99
+ ___52-[DEExtension createExtensionHostContextCompletion:]_block_invoke.90
+ ___52-[DEExtension createExtensionHostContextCompletion:]_block_invoke.90.cold.1
+ ___52-[DEExtension createExtensionHostContextCompletion:]_block_invoke.90.cold.2
+ ___52-[DEExtension createExtensionHostContextCompletion:]_block_invoke.90.cold.3
+ ___52-[DEExtension createExtensionHostContextCompletion:]_block_invoke.92
+ ___52-[DEExtension createExtensionHostContextCompletion:]_block_invoke.93
+ ___71-[DEExtension attachmentsForParameters:withProgressHandler:andHandler:]_block_invoke.103
+ ___72-[DEExtensionHostContext annotatedAttachmentsForParameters:withHandler:]_block_invoke.141
+ ___83-[DEExtensionHostContext attachmentsForParameters:withProgressHandler:withHandler:]_block_invoke.143
+ ___block_descriptor_48_e8_32bs40w_e32_v16?0"DEExtensionHostContext"8lw40l8s32l8
+ ___block_literal_global.106
+ ___block_literal_global.114
+ ___block_literal_global.118
+ ___block_literal_global.125
+ ___block_literal_global.132
+ ___block_literal_global.140
+ ___block_literal_global.146
+ ___block_literal_global.148
+ ___block_literal_global.193
+ ___block_literal_global.273
+ ___block_literal_global.62
+ ___block_literal_global.77
+ ___block_literal_global.86
+ ___block_literal_global.89
+ ___swift_reflection_version
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_DiagnosticExtensions
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftDispatch_$_DiagnosticExtensions
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation_$_DiagnosticExtensions
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_DiagnosticExtensions
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftXPC_$_DiagnosticExtensions
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_Builtin_float_$_DiagnosticExtensions
+ _dispatch_queue_attr_make_with_autorelease_frequency
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$UUID
+ _objc_msgSend$UUIDString
+ _objc_msgSend$adapter
+ _objc_msgSend$attachToDestinationDir:useAppleArchive:
+ _objc_msgSend$compressWithAppleArchive:deleteOriginal:progressHandler:
+ _objc_msgSend$copyItem:toDestinationDir:zipped:useAppleArchive:
+ _objc_msgSend$createContextWithCompletion:
+ _objc_msgSend$directorySizeOf:
+ _objc_msgSend$extensionBundle
+ _objc_msgSend$extensionInterruptionHandler
+ _objc_msgSend$extensionProcessID
+ _objc_msgSend$extensionProxy
+ _objc_msgSend$isDeletableFileAtPath:
+ _objc_msgSend$isWritableFileAtPath:
+ _objc_msgSend$loggingProfileURLs
+ _objc_msgSend$openArchiveDecoderForArchive:readStream:decompressionStream:decoder:error:
+ _objc_msgSend$setExtensionInterruptionHandler:
+ _objc_msgSend$setExtensionProxy:
+ _objc_msgSend$stringByAppendingFormat:
+ _objc_msgSend$temporaryDirectory
+ _objc_msgSend$terminateExtensionProcess
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x5
- +[DEUtils copyItem:toDestinationDir:zipped:].cold.1
- +[DEUtils copyItem:toDestinationDir:zipped:].cold.2
- +[DEUtils copyItem:toDestinationDir:zipped:].cold.3
- +[DEUtils createDirectoryWithClassCDataProtection:].cold.2
- -[DEAttachmentGroup attachToDestinationDir:].cold.1
- -[DEAttachmentGroup attachToDestinationDir:].cold.2
- -[DEAttachmentGroup attachToDestinationDir:].cold.3
- GCC_except_table12
- GCC_except_table13
- GCC_except_table37
- GCC_except_table44
- GCC_except_table46
- GCC_except_table55
- GCC_except_table57
- GCC_except_table8
- GCC_except_table92
- GCC_except_table94
- _OUTLINED_FUNCTION_10
- _OUTLINED_FUNCTION_11
- _OUTLINED_FUNCTION_12
- _OUTLINED_FUNCTION_13
- _OUTLINED_FUNCTION_14
- ___31-[DEExtension checkAndTeardown]_block_invoke.112
- ___31-[DEExtension checkAndTeardown]_block_invoke_2.113
- ___35-[DEExtension initWithNSExtension:]_block_invoke.80
- ___38-[DEExtension performWithHostContext:]_block_invoke.101
- ___38-[DEExtension performWithHostContext:]_block_invoke.102
- ___38-[DEExtension performWithHostContext:]_block_invoke.103
- ___38-[DEExtension performWithHostContext:]_block_invoke.104
- ___52-[DEExtension createExtensionHostContextCompletion:]_block_invoke.96
- ___52-[DEExtension createExtensionHostContextCompletion:]_block_invoke.97
- ___52-[DEExtension createExtensionHostContextCompletion:]_block_invoke.cold.2
- ___52-[DEExtension createExtensionHostContextCompletion:]_block_invoke.cold.3
- ___71-[DEExtension attachmentsForParameters:withProgressHandler:andHandler:]_block_invoke.108
- ___72-[DEExtensionHostContext annotatedAttachmentsForParameters:withHandler:]_block_invoke.145
- ___83-[DEExtensionHostContext attachmentsForParameters:withProgressHandler:withHandler:]_block_invoke.147
- ___block_literal_global.111
- ___block_literal_global.119
- ___block_literal_global.122
- ___block_literal_global.129
- ___block_literal_global.136
- ___block_literal_global.144
- ___block_literal_global.152
- ___block_literal_global.154
- ___block_literal_global.196
- ___block_literal_global.258
- ___block_literal_global.68
- ___block_literal_global.83
- ___block_literal_global.91
- ___block_literal_global.94
- _objc_msgSend$attachToDestinationDir:
- _objc_msgSend$copyItem:toDestinationDir:zipped:
- _objc_msgSend$unsignedLongLongValue
- _objc_retain_x27
CStrings:
+ ".%@"
+ "Adapter returned nil bundle for [%{public}@]"
+ "Adapter returned nil context for extension: %{public}@"
+ "Apple Archive compression failed - writeResult=%d, closeEncoder=%d, closeCompression=%d, closeWrite=%d"
+ "Apple Archive extraction failed - processResult=%zd, closeExtract=%d, closeDecoder=%d, closeDecompression=%d, closeRead=%d"
+ "AppleArchive"
+ "AppleArchiveReader"
+ "Archive extraction failed (code: %zd)"
+ "Archive file does not exist: %{private}s [%{public}s]"
+ "Archive file not found"
+ "Archive path is a directory, expected a file"
+ "Archive path is a directory, not a file: %{private}s [%{public}s]"
+ "Connection missing required entitlement: %{public}@"
+ "Created destination directory: %{private}s [%{public}s]"
+ "DEAppleArchiveErrorDomain"
+ "Deleted original after compression: %{private}s [%{public}s]"
+ "Destination path exists but is not a directory: %{private}s [%{public}s]"
+ "Destination path is not a directory"
+ "Destination: %{private}s [%{public}s]"
+ "Error reading archive headers: %d"
+ "Extracting archive: %{private}s [%{public}s]"
+ "Failed to copy file to temp directory: %{public}@"
+ "Failed to create Apple Archive decoder - archive may be corrupted or invalid format"
+ "Failed to create Apple Archive encoder"
+ "Failed to create LZFSE compression stream"
+ "Failed to create LZFSE decompression stream"
+ "Failed to create archive decoder - invalid archive format"
+ "Failed to create decompression stream - archive may be corrupted"
+ "Failed to create destination directory: %{public}@"
+ "Failed to create extract stream for destination: %{private}s [%{public}s]"
+ "Failed to create extraction stream"
+ "Failed to create field key set"
+ "Failed to create header for reading"
+ "Failed to create header for reading archive contents"
+ "Failed to create path list for directory: %{private}s [%{public}s]"
+ "Failed to create path list for temp directory"
+ "Failed to create temp directory: %{public}@"
+ "Failed to decode path as UTF-8, skipping entry"
+ "Failed to delete original after compression: %{public}@"
+ "Failed to open archive file"
+ "Failed to open archive file for reading: %{private}s [%{public}s]"
+ "Failed to read archive headers (error: %d)"
+ "Failed to remove temp directory after archiving file: %{public}@"
+ "Listed %lu items from archive: %{private}s [%{public}s]"
+ "Listing contents of archive: %{private}s [%{public}s]"
+ "No connection available for entitlement check"
+ "Progress tracking not yet implemented for Apple Archive"
+ "Starting Apple Archive compression of: %{private}s [%{public}s]"
+ "Starting extraction to: %{private}s [%{public}s]"
+ "Successfully created Apple Archive: %{private}s [%{public}s]"
+ "Successfully extracted archive: %{private}s [%{public}s] (%zd entries)"
+ "TYP,PAT,LNK,DEV,DAT,UID,GID,MOD,FLG,MTM,BTM,CTM"
+ "Write stream failed - cannot overwrite existing file: %{private}s [%{public}s]"
+ "Write stream failed - no write permission to directory: %{private}s [%{public}s]"
+ "Write stream failed - output directory does not exist: %{private}s [%{public}s]"
+ "Write stream failed - unknown reason for path: %{private}s [%{public}s]"
+ "aar"
+ "archiveFile called on directory: %{private}s [%{public}s]"
- "#16@0:8"
- ".cxx_destruct"
- "@\"<PKModularService>\"16@0:8"
- "@\"<PKModularService>\"24@0:8@\"NSDictionary\"16"
- "@\"DEExtensionHostContext\""
- "@\"NSArray\""
- "@\"NSDate\""
- "@\"NSDictionary\""
- "@\"NSExtension\""
- "@\"NSMutableArray\""
- "@\"NSNumber\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_xpc_object>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSURL\""
- "@16@0:8"
- "@20@0:8i16"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8^@16"
- "@24@0:8d16"
- "@28@0:8@16B24"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16@?24"
- "@32@0:8@16^@24"
- "@32@0:8d16@24"
- "@36@0:8@16@24B32"
- "@36@0:8@16B24@?28"
- "@36@0:8@16B24^@28"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@40@0:8@16@24^@32"
- "@48@0:8@16@24@32@40"
- "@56@0:8@16@24@32@40@48"
- "@?"
- "@?16@0:8"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B32@0:8@16*24"
- "B32@0:8@16@24"
- "B36@0:8@16@24B32"
- "B40@0:8@16@24@32"
- "B40@0:8@16@24@?32"
- "DEAnnotatedGroup"
- "DEAnnotation"
- "DEArchive"
- "DEArchiveReader"
- "DEArchiver"
- "DEAttachmentGroup"
- "DEAttachmentItem"
- "DEAttachmentItemSandboxExtensionHandle"
- "DECollectionProgress"
- "DEDaemonHelper"
- "DEExtension"
- "DEExtensionContext"
- "DEExtensionHostContext"
- "DEExtensionHostProtocol"
- "DEExtensionManager"
- "DEExtensionProvider"
- "DEExtensionTracker"
- "DEExtensionVendorProtocol"
- "DELogMover"
- "DELogging"
- "DELoggingPreferences"
- "DESandboxExtension"
- "DEURLPathEscaping"
- "DEUtils"
- "DiagnosticExtensions_Subsystem"
- "NSCoding"
- "NSExtensionRequestHandling"
- "NSObject"
- "NSSecureCoding"
- "PKModularService"
- "Q16@0:8"
- "Q24@0:8@16"
- "Setting Class C for [%{public}@]"
- "T#,R"
- "T@\"DEExtensionHostContext\",&,V_context"
- "T@\"NSArray\",&,N,V_attachmentItems"
- "T@\"NSArray\",&,N,V_extensions"
- "T@\"NSArray\",&,V_items"
- "T@\"NSDate\",&,N,V_modificationDate"
- "T@\"NSDictionary\",&,V_additionalInfo"
- "T@\"NSExtension\",&,N,V_extension"
- "T@\"NSMutableArray\",&,V_contextFetchHandlers"
- "T@\"NSNumber\",&,N,V_estimatedTimeRemaining"
- "T@\"NSNumber\",&,N,V_filesize"
- "T@\"NSNumber\",&,N,V_shouldCompress"
- "T@\"NSNumber\",&,V_cachedRequiresDataClassBAccessToRun"
- "T@\"NSNumber\",C,N,V_deleteOnAttach"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_initialLoadQueue"
- "T@\"NSObject<OS_dispatch_queue>\",R,V_serialQueue"
- "T@\"NSString\",&,N,V_attachmentsName"
- "T@\"NSString\",&,N,V_displayName"
- "T@\"NSString\",&,N,V_identifier"
- "T@\"NSString\",&,N,V_loggingConsent"
- "T@\"NSString\",&,N,V_statusString"
- "T@\"NSString\",&,V_displayName"
- "T@\"NSString\",&,V_iconType"
- "T@\"NSString\",&,V_localizedDescription"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,N,V_attachmentType"
- "T@\"NSString\",C,N,V_loggingConsent"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,N,V__sandboxExtensionToken"
- "T@\"NSString\",R,N,V_serviceName"
- "T@\"NSURL\",&,N,V_attachedPath"
- "T@\"NSURL\",&,N,V_itemURL"
- "T@\"NSURL\",&,N,V_path"
- "T@\"NSURL\",&,N,V_rootURL"
- "T@\"NSURL\",&,V_sourceDir"
- "T@\"NSURL\",&,V_tarGzUrl"
- "T@?,C,N,V_afterExtendedBlock"
- "T@?,C,V_progressHandler"
- "TB,N,V_allowUserAttachmentSelection"
- "TB,N,V_canGenerateNewAttachment"
- "TB,N,V_didInit"
- "TB,N,V_extendedLoaded"
- "TB,N,V_isEnhancedLoggingStateOn"
- "TB,R"
- "TB,R,N"
- "TB,V_adoptsExtensionTrackerFlow"
- "TB,V_isFetchingExtensionHostContext"
- "TQ,R"
- "Td,N,V_percentComplete"
- "Tq,R,V__handle"
- "Tq,V_callCount"
- "URLByAppendingPathComponent:"
- "URLByAppendingPathComponent:isDirectory:"
- "URLByAppendingPathExtension:"
- "URLByDeletingLastPathComponent"
- "URLByDeletingPathExtension"
- "URLByResolvingSymlinksInPath"
- "URLByStandardizingPath"
- "URLForDirectory:inDomain:appropriateForURL:create:error:"
- "URLForResource:withExtension:subdirectory:"
- "URLForResource:withExtension:subdirectory:localization:"
- "URLPathAllowedCharacterSet"
- "URLWithString:"
- "UTF8String"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "^{archive=}"
- "^{archive=}24@0:8@16"
- "_UUID"
- "__handle"
- "__sandboxExtensionToken"
- "_additionalInfo"
- "_adoptsExtensionTrackerFlow"
- "_afterExtendedBlock"
- "_allowUserAttachmentSelection"
- "_archive"
- "_attachedPath"
- "_attachmentItems"
- "_attachmentType"
- "_attachmentsName"
- "_auxiliaryConnection"
- "_cachedRequiresDataClassBAccessToRun"
- "_callCount"
- "_canGenerateNewAttachment"
- "_conn"
- "_context"
- "_contextFetchHandlers"
- "_deleteOnAttach"
- "_didInit"
- "_displayName"
- "_estimatedTimeRemaining"
- "_extendedLoaded"
- "_extension"
- "_extensionAuxiliaryHostProtocol"
- "_extensionAuxiliaryVendorProtocol"
- "_extensionContextForUUID:"
- "_extensions"
- "_fileContentsFromPlistWithKey:localization:"
- "_filesize"
- "_generateSandboxExtensionTokenForPID:"
- "_getHostname"
- "_handle"
- "_hasClosedArchive"
- "_iconType"
- "_identifier"
- "_initUniqueWithURL:"
- "_initialLoadQueue"
- "_isEnhancedLoggingStateOn"
- "_isFetchingExtensionHostContext"
- "_itemURL"
- "_items"
- "_localizedDescription"
- "_localizedStringFromPlistWithKey:localization:"
- "_localizedTextFromLocalizedStringKey:fallbackFileContentsKey:localization:"
- "_loggingConsent"
- "_modificationDate"
- "_path"
- "_percentComplete"
- "_plugIn"
- "_principalObject"
- "_progressHandler"
- "_rootURL"
- "_sandboxExtensionToken"
- "_serialQueue"
- "_serviceName"
- "_shouldCompress"
- "_sourceDir"
- "_startListening"
- "_statusString"
- "_subsystemPayloadForURL:error:"
- "_tarGzUrl"
- "_updateExtensionExpirationDateWithIdentifier:expirationDate:"
- "_updateXPCActivityDate"
- "absoluteString"
- "accessBundleWithSynchronousHandler:"
- "accessPlugIns:synchronously:flags:extensions:"
- "accessWithSandboxExtension:inBlock:"
- "addFile:withPathName:"
- "addFile:withPathName:progressHandler:"
- "addObject:"
- "addObjectsFromArray:"
- "adoptsExtensionTrackerFlow"
- "afterExtendedBlock"
- "allKeys"
- "allowUserAttachmentSelection"
- "annotateURL:displayName:description:iconType:additionalInfo:error:"
- "annotatedAttachmentsForParameters:"
- "annotatedAttachmentsForParameters:andHandler:"
- "annotatedAttachmentsForParameters:withHandler:"
- "applicationSupportDirectoryForApp:"
- "archiveDirectoryAt:"
- "archiveDirectoryAt:deleteOriginal:"
- "archiveDirectoryAt:deleteOriginal:progressHandler:"
- "archiveFile:"
- "archiveFile:deleteOriginal:"
- "archiveFile:deleteOriginal:progressHandler:"
- "archiverForUrl:"
- "array"
- "arrayWithArray:"
- "arrayWithObjects:count:"
- "attachToDestinationDir:"
- "attachedPath"
- "attachmentItems"
- "attachmentList"
- "attachmentListWithHandler:"
- "attachmentType"
- "attachmentWithPath:"
- "attachmentWithPath:withDisplayName:modificationDate:andFilesize:"
- "attachmentWithPathURL:"
- "attachmentsForParameters:"
- "attachmentsForParameters:andHandler:"
- "attachmentsForParameters:withHandler:"
- "attachmentsForParameters:withProgressHandler:"
- "attachmentsForParameters:withProgressHandler:andHandler:"
- "attachmentsForParameters:withProgressHandler:withHandler:"
- "attachmentsName"
- "attributes"
- "autorelease"
- "beginExtensionRequestWithInputItems:completion:"
- "beginRequestWithExtensionContext:"
- "beginUsing:withBundle:"
- "boolValue"
- "cStringUsingEncoding:"
- "cachedRequiresDataClassBAccessToRun"
- "callCount"
- "canGenerateNewAttachment"
- "cancelExtensionRequestWithIdentifier:"
- "cancelRequestWithError:"
- "caseInsensitiveCompare:"
- "checkAndTeardown"
- "checkIn"
- "checkResourceIsReachableAndReturnError:"
- "class"
- "closeArchive"
- "collectionDidUpdateWithProgress:"
- "combinedLoggingPayloadForURLs:error:"
- "communicationsFailed:"
- "compare:"
- "componentsByRemovingComponentsBeforeComponent:sourceURL:keepingComponent:"
- "componentsJoinedByString:"
- "componentsSeparatedByString:"
- "conformsToProtocol:"
- "containsObject:"
- "contentsOfDirectoryAtURL:includingPropertiesForKeys:options:error:"
- "context"
- "contextFetchHandlers"
- "copy"
- "copyAllFilesFromDir:toDir:"
- "copyAllFilesFromDir:toDir:keepSourceDir:"
- "copyAndReturn:toDir:"
- "copyAndReturn:toDir:withNewFileName:"
- "copyFile:toDir:"
- "copyItem:toDestinationDir:zipped:"
- "copyItemAtURL:toURL:error:"
- "copyPath:toDestinationDir:zipped:"
- "copyPaths:toDestinationDir:withZipName:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createDirectoryAtURL:withIntermediateDirectories:attributes:error:"
- "createDirectoryWithClassCDataProtection:"
- "createExtensionHostContextCompletion:"
- "createUserOwnedDirectoryAtUrl:"
- "createWithName:rootURL:"
- "createWithName:rootURL:attachmentItems:"
- "criteria:"
- "currentLoggingExtensions"
- "d"
- "d16@0:8"
- "date"
- "dateByAddingTimeInterval:"
- "dealloc"
- "debugDescription"
- "decodeDoubleForKey:"
- "decodeObjectForKey:"
- "decodeObjectOfClass:forKey:"
- "decreaseRetainCountWithIdentifier:session:"
- "defaultHost"
- "defaultManager"
- "deleteOnAttach"
- "description"
- "detach"
- "dictionaryForKey:"
- "dictionaryWithDictionary:"
- "dictionaryWithObjects:forKeys:count:"
- "didInit"
- "dirForTarGz:"
- "directorySizeOf:"
- "distantFuture"
- "encodeDouble:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "endUsing:"
- "endUsingExtension"
- "enumerateKeysAndObjectsUsingBlock:"
- "enumeratorAtURL:includingPropertiesForKeys:options:errorHandler:"
- "enumeratorForAllItems:"
- "errorWithDomain:code:userInfo:"
- "errorWithMessage:"
- "escape"
- "estimatedTimeRemaining"
- "excludeFromBackup:"
- "extendedLoaded"
- "extensionForIdentifier:"
- "extensionTrackerClass"
- "extensionTrackerCleanup"
- "extensions"
- "extensionsWithFilter:"
- "extensionsWithMatchingAttributes:completion:"
- "fileExistsAtPath:"
- "fileExistsAtPath:isDirectory:"
- "fileSystemRepresentation"
- "fileURLWithPath:"
- "fileURLWithPath:isDirectory:"
- "fileURLWithPathComponents:"
- "filesInDir:matchingPattern:excludingPattern:"
- "filesize"
- "findAllItems:includeDirs:"
- "findAllfiles:"
- "findEntriesInDirectory:createdAfter:matchingPattern:"
- "firstMatchInString:options:range:"
- "firstObject"
- "fwHandle"
- "generateSandboxExtensionForProcess:"
- "generateSandboxExtensionWithDestinationDir:pingTarget:"
- "getDirectorySize:"
- "getFileSystemItemSize:"
- "getResourceValue:forKey:error:"
- "hasEntitlement"
- "hasInactiveLoggingSession:"
- "hasPrefix:"
- "hash"
- "identifier"
- "increaseRetainCountWithIdentifier:session:"
- "indexOfObject:"
- "infoDictionary"
- "init"
- "initForPlugInKit"
- "initForPlugInKitWithOptions:"
- "initWithArray:"
- "initWithArray:copyItems:"
- "initWithCapacity:"
- "initWithCoder:"
- "initWithContentsOfURL:"
- "initWithDisplayName:localizedDescription:iconType:additionalInfo:attachmentItems:"
- "initWithNSExtension:"
- "initWithPath:"
- "initWithPath:withDisplayName:modificationDate:andFilesize:"
- "initWithPathURL:"
- "initWithPathURL:shouldCheckURLAttributes:"
- "initWithPercentComplete:"
- "initWithPercentComplete:withEstimatedTimeRemaining:"
- "initWithSandboxExtensionToken:itemURL:errorOut:"
- "initWithServiceName:"
- "initWithSuiteName:"
- "initWithURL:"
- "installLoggingProfile:sessionIdentifier:extensionIdentifier:error:"
- "installLoggingProfileWithSessionID:"
- "intValue"
- "integerValue"
- "interfaceWithProtocol:"
- "isEnhancedLoggingStateOn"
- "isEqual:"
- "isEqualToString:"
- "isExtensionEnhancedLoggingStateOnWithHandler:"
- "isFetchingExtensionHostContext"
- "isKindOfClass:"
- "isLoggingEnabled"
- "isMemberOfClass:"
- "isProxy"
- "isValidDirectory:"
- "itemURL"
- "lastObject"
- "lastPathComponent"
- "laterDate:"
- "length"
- "listContainedPaths"
- "loadExtensions"
- "localizedConsentTextWithLocalization:"
- "localizedCustomerConsentTextWithLocalization:"
- "localizedDataCollectedExplanationWithLocalization:"
- "localizedDataCollectedSummaryWithLocalization:"
- "localizedStringForKey:value:table:"
- "loggingConsent"
- "loggingPayloadForURL:error:"
- "loggingProfileURLsFromExtension"
- "lsDir:"
- "lsDir:sorted:"
- "managedLoggingProfilesDirectory"
- "managedLoggingProfilesDirectoryForSessionIdentifier:createIfNeeded:error:"
- "matchesInString:options:range:"
- "modificationDate"
- "moveItem:toDestinationDir:"
- "moveItemAtURL:toURL:error:"
- "moveSystemLogsWithExtensions:"
- "mutableCopy"
- "numberOfManagedLoggingPreferences"
- "numberOfMatchesInString:options:range:"
- "numberWithBool:"
- "numberWithInt:"
- "numberWithInteger:"
- "numberWithUnsignedInteger:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "path"
- "pathComponents"
- "pathComponentsInURL:removingBaseURLComponents:keepingFirstComponent:"
- "pathExtension"
- "pathWithComponents:"
- "percentComplete"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "performWithHostContext:"
- "ping:"
- "processErrorResponse:"
- "processIdentifier"
- "progressHandler"
- "q"
- "q16@0:8"
- "rangeAtIndex:"
- "readExtendedAttributeInURL:forKey:error:"
- "regularExpressionWithPattern:options:error:"
- "release"
- "remoteObjectProxyWithErrorHandler:"
- "removeAllObjects"
- "removeFile:"
- "removeItemAtURL:error:"
- "removeLoggingProfileForSessionIdentifier:extensionIdentifier:error:"
- "removeLoggingProfileWithSessionID:"
- "removeObjectsInRange:"
- "requiresDataClassBAccessToRun"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "rootURL"
- "sandboxExtensionHandleWithErrorOut:"
- "saveCurrentLoggingExtensionsWithDictionary:"
- "scheduleXPCActivity"
- "self"
- "sendRequestReturningBooleanResponse:withSuccessKey:"
- "serialQueue"
- "serviceName"
- "setAdditionalInfo:"
- "setAdoptsExtensionTrackerFlow:"
- "setAfterExtendedBlock:"
- "setAllowUserAttachmentSelection:"
- "setAttachedPath:"
- "setAttachmentItems:"
- "setAttachmentType:"
- "setAttachmentsName:"
- "setCachedRequiresDataClassBAccessToRun:"
- "setCallCount:"
- "setCanGenerateNewAttachment:"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setContext:"
- "setContextFetchHandlers:"
- "setDateFormat:"
- "setDeleteOnAttach:"
- "setDidInit:"
- "setDisplayName:"
- "setEstimatedTimeRemaining:"
- "setExtendedLoaded:"
- "setExtension:"
- "setExtensions:"
- "setFilesize:"
- "setIconType:"
- "setIdentifier:"
- "setInitialLoadQueue:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setIsEnhancedLoggingStateOn:"
- "setIsFetchingExtensionHostContext:"
- "setItemURL:"
- "setItems:"
- "setLocalizedDescription:"
- "setLoggingConsent:"
- "setModificationDate:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setPath:"
- "setPercentComplete:"
- "setProgressHandler:"
- "setRequestCancellationBlock:"
- "setRequestCompletionBlock:"
- "setResourceValue:forKey:error:"
- "setResourceValues:error:"
- "setRootURL:"
- "setShouldCompress:"
- "setSourceDir:"
- "setStatusString:"
- "setTarGzUrl:"
- "setWithObjects:"
- "setWithSet:"
- "setupForParameters:withHandler:"
- "setupWithParameters:"
- "setupWithParameters:session:"
- "setupWithParameters:session:expirationDate:"
- "setupWithParameters:withHandler:"
- "sharedInstance"
- "sharedSerialQueue"
- "shouldCompress"
- "shouldSetupWithIdentifier:session:expirationDate:"
- "shouldTeardownWithIdentifier:session:"
- "sortedArrayUsingComparator:"
- "sourceDir"
- "standardUserDefaults"
- "statusString"
- "stringByAddingPercentEncodingWithAllowedCharacters:"
- "stringByAppendingPathExtension:"
- "stringByAppendingString:"
- "stringByReplacingOccurrencesOfString:withString:"
- "stringFromByteCount:countStyle:"
- "stringFromDate:"
- "stringWithCString:encoding:"
- "stringWithContentsOfURL:encoding:error:"
- "stringWithFormat:"
- "stringWithString:"
- "stringWithUTF8String:"
- "subarrayWithRange:"
- "substringWithRange:"
- "superclass"
- "supportsSecureCoding"
- "synchronize"
- "tarGzForDirectoryUrl:"
- "tarGzForDirectoryUrl:validatesUrl:"
- "tarGzUrl"
- "teardownForParameters:withHandler:"
- "teardownWithParameters:"
- "teardownWithParameters:session:"
- "teardownWithParameters:withHandler:"
- "timeIntervalSinceNow"
- "uniqueDateString"
- "uniqueTemporaryDirectory"
- "unsignedIntegerValue"
- "unsignedLongLongValue"
- "updateExpirationDateWithIdentifier:expirationDate:"
- "updateRetainCountWithIdentifier:session:offsetBy:"
- "updatedParametersWithExtensionFileNameFromParameters:"
- "urlByRemovingComponentsBefore:source:keepComponent:"
- "userDefaults"
- "userLibraryDirectoryForApp:"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8i16"
- "v24@0:8@\"<PKSubsystemServicePersonality>\"16"
- "v24@0:8@\"DECollectionProgress\"16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSExtensionContext\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSArray\">16"
- "v24@0:8@?<v@?B>16"
- "v24@0:8d16"
- "v24@0:8q16"
- "v32@0:8@\"<PKSubsystemServicePersonality>\"16@\"NSBundle\"24"
- "v32@0:8@\"NSDictionary\"16@?<v@?>24"
- "v32@0:8@\"NSDictionary\"16@?<v@?@\"DEAnnotatedGroup\">24"
- "v32@0:8@\"NSDictionary\"16@?<v@?@\"NSArray\">24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v36@0:8@16@24i32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@?24@?32"
- "v48@0:8@16@24@32^@40"
- "v64@0:8@16@24@32@40@48^@56"
- "valueForEntitlement:"
- "valueForKey:"
- "writeExtendedAttributeInURL:forKey:value:"
- "writeToURL:error:"
- "xpcActivityTimeInterval"
- "zone"

```
