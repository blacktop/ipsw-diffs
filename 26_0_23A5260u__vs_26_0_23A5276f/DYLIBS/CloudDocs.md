## CloudDocs

> `/System/Library/PrivateFrameworks/CloudDocs.framework/CloudDocs`

```diff

-4140.0.0.502.2
-  __TEXT.__text: 0x8a67c
-  __TEXT.__auth_stubs: 0x1480
-  __TEXT.__objc_methlist: 0x672c
+4204.0.0.502.1
+  __TEXT.__text: 0x8b128
+  __TEXT.__auth_stubs: 0x13b0
+  __TEXT.__objc_methlist: 0x6734
   __TEXT.__const: 0x1c0
-  __TEXT.__gcc_except_tab: 0x4bb8
-  __TEXT.__cstring: 0xb695
-  __TEXT.__oslogstring: 0x95fc
+  __TEXT.__gcc_except_tab: 0x4bb0
+  __TEXT.__cstring: 0xb59b
+  __TEXT.__oslogstring: 0x951f
   __TEXT.__dlopen_cstrs: 0x4c
   __TEXT.__ustring: 0x8
-  __TEXT.__unwind_info: 0x26c8
+  __TEXT.__unwind_info: 0x26d0
   __TEXT.__objc_classname: 0xdd2
-  __TEXT.__objc_methname: 0x10f66
-  __TEXT.__objc_methtype: 0x3c75
-  __TEXT.__objc_stubs: 0xb1a0
-  __DATA_CONST.__got: 0x898
+  __TEXT.__objc_methname: 0x10fcf
+  __TEXT.__objc_methtype: 0x3c88
+  __TEXT.__objc_stubs: 0xb180
+  __DATA_CONST.__got: 0x890
   __DATA_CONST.__const: 0x2678
   __DATA_CONST.__objc_classlist: 0x310
   __DATA_CONST.__objc_catlist: 0xe8
   __DATA_CONST.__objc_protolist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x41f0
+  __DATA_CONST.__objc_selrefs: 0x41f8
   __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__objc_superrefs: 0x250
-  __DATA_CONST.__objc_arraydata: 0x58
-  __AUTH_CONST.__auth_got: 0xa50
+  __DATA_CONST.__objc_arraydata: 0x88
+  __AUTH_CONST.__auth_got: 0x9e8
   __AUTH_CONST.__const: 0x10e0
-  __AUTH_CONST.__cfstring: 0x5c00
-  __AUTH_CONST.__objc_const: 0xce88
-  __AUTH_CONST.__objc_arrayobj: 0x48
+  __AUTH_CONST.__cfstring: 0x5ca0
+  __AUTH_CONST.__objc_const: 0xce90
+  __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_intobj: 0x510
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH.__objc_data: 0x14f0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: F403EE27-7740-330D-9914-313CB6C82110
-  Functions: 3093
-  Symbols:   10822
-  CStrings:  6235
+  UUID: 6703F1F6-4E24-3F4A-8F24-F71F22F6A03E
+  Functions: 3089
+  Symbols:   10801
+  CStrings:  6240
 
Symbols:
+ +[NSError(BRAdditions) brc_errorDocumentWithFilename:size:isTooLargeToUpload:localizedDescription:]
+ +[NSString(BRCAdditions) br_newReadableFileSizeStringFromBytesCount:]
+ -[NSString(BRPathAdditions) _br_pathSafeFileSystemRepresentationWithDefaultValue:]
+ -[NSString(BRPathAdditions) br_filenameSafeFileSystemRepresentation]
+ -[NSString(BRPathAdditions) br_pathSafeFileSystemRepresentation]
+ -[NSString(BRPathAdditions) br_pathSafeFileSystemRepresentation].cold.1
+ ___block_literal_global.419
+ ___block_literal_global.431
+ ___block_literal_global.463
+ ___block_literal_global.480
+ _objc_msgSend$_br_pathSafeFileSystemRepresentationWithDefaultValue:
+ _objc_msgSend$br_pathSafeFileSystemRepresentation
- +[BRSpecialFolders internalDaemonContainerPath]
- +[BRSpecialFolders internalDaemonContainerPath].cold.1
- +[BRSpecialFolders internalDaemonContainerPath].cold.2
- +[BRSpecialFolders internalDaemonContainerPath].cold.3
- +[BRSpecialFolders internalDaemonContainerPath].cold.4
- +[BRSpecialFolders internalDaemonContainerPath].cold.5
- +[NSError(BRAdditions) brc_errorDocumentWithFilename:size:isTooLargeToUpload:]
- -[NSString(BRPathAdditions) _br_safeFileSystemRepresentationWithDefaultValue:]
- -[NSString(BRPathAdditions) _br_safeFileSystemRepresentationWithDefaultValue:].cold.1
- -[NSString(BRPathAdditions) br_safeFileSystemRepresentation]
- -[UMUserPersona(BRAdditions) br_personaIDWithDefault:]
- _CONTAINER_PERSONA_PRIMARY
- ___block_literal_global.418
- ___block_literal_global.430
- ___block_literal_global.462
- ___block_literal_global.479
- _container_copy_sandbox_token
- _container_copy_unlocalized_description
- _container_error_copy_unlocalized_description
- _container_get_path
- _container_query_create
- _container_query_free
- _container_query_get_last_error
- _container_query_get_single_result
- _container_query_operation_set_flags
- _container_query_set_class
- _container_query_set_identifiers
- _container_query_set_persona_unique_string
- _objc_msgSend$_br_safeFileSystemRepresentationWithDefaultValue:
- _objc_msgSend$br_personaIDWithDefault:
- _objc_msgSend$br_safeFileSystemRepresentation
- _xpc_string_create
CStrings:
+ "%.lf %@"
+ "-[NSString(BRPathAdditions) br_pathSafeFileSystemRepresentation]"
+ "4204.0.0.502.1"
+ "@48@0:8@16q24q32@40"
+ "GB"
+ "KB"
+ "MB"
+ "PB"
+ "TB"
+ "[DEBUG] Could not convert %@ to fileSystemRepresentation for reason: %@%@"
+ "[DEBUG] wrote plist %@ for container %@ at '%@' {\n  formatVersion = %@,\n  iconGenerationVersion = %@\n}%@"
+ "_br_pathSafeFileSystemRepresentationWithDefaultValue:"
+ "_t_getContainerMetadataForContainerID:reply:"
+ "br_filenameSafeFileSystemRepresentation"
+ "br_newReadableFileSizeStringFromBytesCount:"
+ "br_pathSafeFileSystemRepresentation"
+ "brc_errorDocumentWithFilename:size:isTooLargeToUpload:localizedDescription:"
+ "{?=\"sectionID\"Q\"function\"*\"line\"i\"ignorePersona\"B}"
- "+[BRSpecialFolders internalDaemonContainerPath]"
- "-[NSString(BRPathAdditions) _br_safeFileSystemRepresentationWithDefaultValue:]"
- "/Library/Caches/com.apple.xbs/Sources/CloudDocs/framework/foundation/BRSpecialFolders.m"
- "4140.0.0.502.2"
- "@40@0:8@16q24q32"
- "Failed to execute lookup query for daemon container: %s"
- "Got NULL container path for daemon data container %s"
- "[DEBUG] Could not convert %@ to fileSystemRepresentation for reason: %@ --> use bad filename alternative name instead%@"
- "[DEBUG] Failed to consume daemon container sandbox token: (%s)%@"
- "[DEBUG] Got user container URL %s from containermanagerd%@"
- "[DEBUG] container_copy_sandbox_token returned NULL!%@"
- "[DEBUG] wrote plist for container %@ at '%@' {\n  formatVersion = %@,\n  iconGenerationVersion = %@\n}%@"
- "_br_safeFileSystemRepresentationWithDefaultValue:"
- "br_personaIDWithDefault:"
- "br_safeFileSystemRepresentation"
- "brc_errorDocumentWithFilename:size:isTooLargeToUpload:"
- "file-write-data"
- "internalDaemonContainerPath"
- "{?=\"sectionID\"Q\"function\"*\"line\"i}"

```
