## MigrationKit

> `/System/Library/PrivateFrameworks/MigrationKit.framework/MigrationKit`

```diff

-17.3.4.0.0
-  __TEXT.__text: 0x30650
-  __TEXT.__auth_stubs: 0xc30
-  __TEXT.__objc_methlist: 0x34bc
+17.4.19.0.0
+  __TEXT.__text: 0x30900
+  __TEXT.__auth_stubs: 0xc20
+  __TEXT.__objc_methlist: 0x353c
   __TEXT.__const: 0x44c
-  __TEXT.__cstring: 0x3025
-  __TEXT.__oslogstring: 0x236e
+  __TEXT.__cstring: 0x3045
+  __TEXT.__oslogstring: 0x232f
   __TEXT.__gcc_except_tab: 0xc24
-  __TEXT.__unwind_info: 0xce0
+  __TEXT.__unwind_info: 0xcec
   __TEXT.__eh_frame: 0x38
-  __TEXT.__objc_classname: 0x810
-  __TEXT.__objc_methname: 0x6f4e
-  __TEXT.__objc_methtype: 0xf78
-  __TEXT.__objc_stubs: 0x6e80
+  __TEXT.__objc_classname: 0x813
+  __TEXT.__objc_methname: 0x70be
+  __TEXT.__objc_methtype: 0xf9e
+  __TEXT.__objc_stubs: 0x6f80
   __DATA_CONST.__got: 0x158
   __DATA_CONST.__const: 0x5c0
   __DATA_CONST.__objc_classlist: 0x330
-  __DATA_CONST.__objc_catlist: 0x10
+  __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x6ad8
-  __DATA_CONST.__objc_selrefs: 0x1e10
+  __DATA_CONST.__objc_const: 0x6b98
+  __DATA_CONST.__objc_selrefs: 0x1e50
+  __DATA_CONST.__objc_classrefs: 0x510
+  __DATA_CONST.__objc_superrefs: 0x250
   __DATA_CONST.__objc_arraydata: 0x480
   __AUTH_CONST.__objc_intobj: 0xc18
-  __AUTH_CONST.__cfstring: 0x4580
-  __AUTH_CONST.__objc_const: 0x1f28
+  __AUTH_CONST.__cfstring: 0x4600
+  __AUTH_CONST.__objc_const: 0x1f68
   __AUTH_CONST.__objc_arrayobj: 0x1e0
   __AUTH_CONST.__const: 0x3e0
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x630
+  __AUTH_CONST.__auth_got: 0x628
   __AUTH.__objc_data: 0x1f90
-  __DATA.__objc_classrefs: 0x510
-  __DATA.__objc_superrefs: 0x250
-  __DATA.__objc_ivar: 0x584
+  __DATA.__objc_ivar: 0x594
   __DATA.__data: 0x540
   __DATA.__bss: 0x1b0
   __DATA_DIRTY.__objc_data: 0x50

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 8DD764E7-0162-31FA-A54F-BAF10832EBB5
-  Functions: 1343
-  Symbols:   5221
-  CStrings:  3214
+  UUID: 4AD3B8DE-0555-329E-82FF-D6FF22ECCF7A
+  Functions: 1352
+  Symbols:   5252
+  CStrings:  3237
 
Symbols:
+ -[MKAPIServer router:didReceiveContainer:signature:chunk:filename:offset:length:total:required:excludedFromBackup:complete:]
+ -[MKAPIServer router:didReceiveFileChunk:filename:offset:length:total:complete:]
+ -[MKAPIServer router:didReceiveImageChunk:identifier:offset:length:total:filename:collection:originalFilename:complete:]
+ -[MKAPIServer router:didReceiveVideoChunk:identifier:offset:length:total:filename:collection:originalFilename:complete:]
+ -[MKApp isSupported:]
+ -[MKApp isiPadApp]
+ -[MKApp isiPhoneApp]
+ -[MKApp isiPodApp]
+ -[MKApp setIsiPadApp:]
+ -[MKApp setIsiPhoneApp:]
+ -[MKApp setIsiPodApp:]
+ -[MKContainerMigrator import:signature:chunk:filename:offset:length:total:required:excludedFromBackup:complete:]
+ -[MKContainerMigrator import:signature:chunk:filename:offset:length:total:required:excludedFromBackup:complete:].cold.1
+ -[MKContainerMigrator import:signature:chunk:filename:offset:length:total:required:excludedFromBackup:complete:].cold.2
+ -[MKContainerMigrator import:signature:chunk:filename:offset:length:total:required:excludedFromBackup:complete:].cold.3
+ -[MKContainerMigrator import:signature:chunk:filename:offset:length:total:required:excludedFromBackup:complete:].cold.4
+ -[MKContainerMigrator import:signature:chunk:filename:offset:length:total:required:excludedFromBackup:complete:].cold.5
+ -[MKContainerMigrator import:signature:chunk:filename:offset:length:total:required:excludedFromBackup:complete:].cold.6
+ -[MKContainerMigrator import:signature:chunk:filename:offset:length:total:required:excludedFromBackup:complete:].cold.7
+ -[MKContainerMigrator import:signature:chunk:filename:offset:length:total:required:excludedFromBackup:complete:].cold.8
+ -[MKContainerMigrator import:signature:chunk:filename:offset:length:total:required:excludedFromBackup:complete:].cold.9
+ -[MKContainerMigrator importContainer:signature:chunk:filename:offset:length:total:required:excludedFromBackup:complete:]
+ -[MKDevice setType:]
+ -[MKDevice type]
+ -[MKFileMigrator import:filename:offset:length:total:complete:]
+ -[MKFileMigrator import:filename:offset:length:total:complete:].cold.1
+ -[MKFileMigrator import:filename:offset:length:total:complete:].cold.2
+ -[MKFileMigrator import:filename:offset:length:total:complete:].cold.3
+ -[MKFileMigrator import:filename:offset:length:total:complete:].cold.4
+ -[MKFileMigrator importChunk:filename:offset:length:total:complete:]
+ -[MKHTTPRequest chunkedTransferCompleted]
+ -[MKHTTPRequest setChunkedTransferCompleted:]
+ -[MKPhotoLibraryMigrator import:identifier:offset:length:total:filename:collection:originalFilename:complete:]
+ -[MKPhotoLibraryMigrator import:identifier:offset:length:total:filename:collection:originalFilename:complete:].cold.1
+ -[MKPhotoLibraryMigrator import:identifier:offset:length:total:filename:collection:originalFilename:complete:].cold.2
+ -[MKPhotoLibraryMigrator import:identifier:offset:length:total:filename:collection:originalFilename:complete:].cold.3
+ -[MKPhotoLibraryMigrator import:identifier:offset:length:total:filename:collection:originalFilename:complete:].cold.4
+ -[MKPhotoLibraryMigrator importChunk:identifier:offset:length:total:filename:collection:originalFilename:complete:]
+ -[NSFileManager(Size) mk_fileSizeAtPath:]
+ _OBJC_IVAR_$_MKApp._isiPadApp
+ _OBJC_IVAR_$_MKApp._isiPhoneApp
+ _OBJC_IVAR_$_MKApp._isiPodApp
+ _OBJC_IVAR_$_MKDevice._type
+ _OBJC_IVAR_$_MKHTTPRequest._chunkedTransferCompleted
+ __OBJC_$_CATEGORY_NSFileManager_$_Size
+ __OBJC_$_INSTANCE_METHODS_NSFileManager(Size)
+ __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ue170006Ev
+ __ZNKSt3__113__string_hashIcNS_9allocatorIcEEEclB8ue170006ERKNS_12basic_stringIcNS_11char_traitsIcEES2_EE
+ __ZNKSt3__121__murmur2_or_cityhashImLm64EEclB8ue170006EPKvm
+ __ZNKSt3__18equal_toINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEclB8ue170006ERKS6_S9_
+ __ZNSt12length_errorC1B8ue170006EPKc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE25__init_copy_ctor_externalEPKcm
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ue170006ILi0EEEPKc
+ __ZNSt3__113unordered_mapINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE3sigNS_4hashIS6_EENS_8equal_toIS6_EENS4_INS_4pairIKS6_S7_EEEEED1B8ue170006Ev
+ __ZNSt3__117__call_once_proxyB8ue170006INS_5tupleIJOZN12migrationkit9signature14get_identifierEPKhmE3$_0EEEEEvPv
+ __ZNSt3__120__throw_length_errorB8ue170006EPKc
+ __ZNSt3__121__murmur2_or_cityhashImLm64EE18__hash_len_0_to_16B8ue170006EPKcm
+ __ZNSt3__121__murmur2_or_cityhashImLm64EE19__hash_len_17_to_32B8ue170006EPKcm
+ __ZNSt3__121__murmur2_or_cityhashImLm64EE19__hash_len_33_to_64B8ue170006EPKcm
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEE3sigEEPvEEEEEclB8ue170006EPSC_
+ __ZSt28__throw_bad_array_new_lengthB8ue170006v
+ ___110-[MKPhotoLibraryMigrator import:identifier:offset:length:total:filename:collection:originalFilename:complete:]_block_invoke
+ ___block_descriptor_48_e8_32bs_e36_v24?0"AMSMediaResult"8"NSError"16ls32l8
+ _objc_msgSend$chunkedTransferCompleted
+ _objc_msgSend$import:filename:offset:length:total:complete:
+ _objc_msgSend$import:identifier:offset:length:total:filename:collection:originalFilename:complete:
+ _objc_msgSend$import:signature:chunk:filename:offset:length:total:required:excludedFromBackup:complete:
+ _objc_msgSend$importChunk:filename:offset:length:total:complete:
+ _objc_msgSend$importChunk:identifier:offset:length:total:filename:collection:originalFilename:complete:
+ _objc_msgSend$importContainer:signature:chunk:filename:offset:length:total:required:excludedFromBackup:complete:
+ _objc_msgSend$isSupported:
+ _objc_msgSend$isiPadApp
+ _objc_msgSend$isiPhoneApp
+ _objc_msgSend$isiPodApp
+ _objc_msgSend$mk_fileSizeAtPath:
+ _objc_msgSend$router:didReceiveContainer:signature:chunk:filename:offset:length:total:required:excludedFromBackup:complete:
+ _objc_msgSend$router:didReceiveFileChunk:filename:offset:length:total:complete:
+ _objc_msgSend$router:didReceiveImageChunk:identifier:offset:length:total:filename:collection:originalFilename:complete:
+ _objc_msgSend$router:didReceiveVideoChunk:identifier:offset:length:total:filename:collection:originalFilename:complete:
+ _objc_msgSend$setChunkedTransferCompleted:
+ _objc_msgSend$setIsiPadApp:
+ _objc_msgSend$setIsiPhoneApp:
+ _objc_msgSend$setIsiPodApp:
- -[MKAPIServer router:didReceiveContainer:signature:chunk:filename:offset:length:total:required:excludedFromBackup:]
- -[MKAPIServer router:didReceiveFileChunk:filename:offset:length:total:]
- -[MKAPIServer router:didReceiveImageChunk:identifier:offset:length:total:filename:collection:originalFilename:]
- -[MKAPIServer router:didReceiveVideoChunk:identifier:offset:length:total:filename:collection:originalFilename:]
- -[MKContainerMigrator import:signature:chunk:filename:offset:length:total:required:excludedFromBackup:]
- -[MKContainerMigrator import:signature:chunk:filename:offset:length:total:required:excludedFromBackup:].cold.1
- -[MKContainerMigrator import:signature:chunk:filename:offset:length:total:required:excludedFromBackup:].cold.2
- -[MKContainerMigrator import:signature:chunk:filename:offset:length:total:required:excludedFromBackup:].cold.3
- -[MKContainerMigrator import:signature:chunk:filename:offset:length:total:required:excludedFromBackup:].cold.4
- -[MKContainerMigrator import:signature:chunk:filename:offset:length:total:required:excludedFromBackup:].cold.5
- -[MKContainerMigrator import:signature:chunk:filename:offset:length:total:required:excludedFromBackup:].cold.6
- -[MKContainerMigrator import:signature:chunk:filename:offset:length:total:required:excludedFromBackup:].cold.7
- -[MKContainerMigrator import:signature:chunk:filename:offset:length:total:required:excludedFromBackup:].cold.8
- -[MKContainerMigrator import:signature:chunk:filename:offset:length:total:required:excludedFromBackup:].cold.9
- -[MKContainerMigrator importContainer:signature:chunk:filename:offset:length:total:required:excludedFromBackup:]
- -[MKDevice isiPhone]
- -[MKDevice setIsiPhone:]
- -[MKFileMigrator import:filename:offset:length:total:]
- -[MKFileMigrator import:filename:offset:length:total:].cold.1
- -[MKFileMigrator import:filename:offset:length:total:].cold.2
- -[MKFileMigrator import:filename:offset:length:total:].cold.3
- -[MKFileMigrator import:filename:offset:length:total:].cold.4
- -[MKFileMigrator import:filename:offset:length:total:].cold.5
- -[MKFileMigrator importChunk:filename:offset:length:total:]
- -[MKPhotoLibraryMigrator import:identifier:offset:length:total:filename:collection:originalFilename:]
- -[MKPhotoLibraryMigrator import:identifier:offset:length:total:filename:collection:originalFilename:].cold.1
- -[MKPhotoLibraryMigrator import:identifier:offset:length:total:filename:collection:originalFilename:].cold.2
- -[MKPhotoLibraryMigrator import:identifier:offset:length:total:filename:collection:originalFilename:].cold.3
- -[MKPhotoLibraryMigrator import:identifier:offset:length:total:filename:collection:originalFilename:].cold.4
- -[MKPhotoLibraryMigrator import:identifier:offset:length:total:filename:collection:originalFilename:].cold.5
- -[MKPhotoLibraryMigrator importChunk:identifier:offset:length:total:filename:collection:originalFilename:]
- _OBJC_IVAR_$_MKDevice._isiPhone
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB7v160006Ev
- __ZNKSt3__113__string_hashIcNS_9allocatorIcEEEclERKNS_12basic_stringIcNS_11char_traitsIcEES2_EE
- __ZNKSt3__18equal_toINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEclB7v160006ERKS6_S9_
- __ZNSt12length_errorC1B7v160006EPKc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1ERKS5_
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B7v160006IDnEEPKc
- __ZNSt3__113unordered_mapINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE3sigNS_4hashIS6_EENS_8equal_toIS6_EENS4_INS_4pairIKS6_S7_EEEEED1B7v160006Ev
- __ZNSt3__117__call_once_proxyB7v160006INS_5tupleIJOZN12migrationkit9signature14get_identifierEPKhmE3$_0EEEEEvPv
- __ZNSt3__120__throw_length_errorB7v160006EPKc
- __ZNSt3__121__murmur2_or_cityhashImLm64EE18__hash_len_0_to_16EPKcm
- __ZNSt3__121__murmur2_or_cityhashImLm64EE19__hash_len_17_to_32EPKcm
- __ZNSt3__121__murmur2_or_cityhashImLm64EE19__hash_len_33_to_64EPKcm
- __ZNSt3__121__murmur2_or_cityhashImLm64EEclEPKvm
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEE3sigEEPvEEEEEclB7v160006EPSC_
- __ZSt28__throw_bad_array_new_lengthB7v160006v
- ___101-[MKPhotoLibraryMigrator import:identifier:offset:length:total:filename:collection:originalFilename:]_block_invoke
- ___block_descriptor_40_e8_32bs_e36_v24?0"AMSMediaResult"8"NSError"16ls32l8
- _objc_msgSend$import:filename:offset:length:total:
- _objc_msgSend$import:identifier:offset:length:total:filename:collection:originalFilename:
- _objc_msgSend$import:signature:chunk:filename:offset:length:total:required:excludedFromBackup:
- _objc_msgSend$importChunk:filename:offset:length:total:
- _objc_msgSend$importChunk:identifier:offset:length:total:filename:collection:originalFilename:
- _objc_msgSend$importContainer:signature:chunk:filename:offset:length:total:required:excludedFromBackup:
- _objc_msgSend$isiPhone
- _objc_msgSend$router:didReceiveContainer:signature:chunk:filename:offset:length:total:required:excludedFromBackup:
- _objc_msgSend$router:didReceiveFileChunk:filename:offset:length:total:
- _objc_msgSend$router:didReceiveImageChunk:identifier:offset:length:total:filename:collection:originalFilename:
- _objc_msgSend$router:didReceiveVideoChunk:identifier:offset:length:total:filename:collection:originalFilename:
- _objc_msgSend$setIsiPhone:
CStrings:
+ "B24@0:8q16"
+ "T@\"NSString\",?,R,C"
+ "TB,N,V_chunkedTransferCompleted"
+ "TB,N,V_isiPadApp"
+ "TB,N,V_isiPhoneApp"
+ "TB,N,V_isiPodApp"
+ "_chunkedTransferCompleted"
+ "_isiPadApp"
+ "_isiPhoneApp"
+ "_isiPodApp"
+ "chunkedTransferCompleted"
+ "deviceFamilies"
+ "file=%@, offset=%lld, length=%lld, total=%lld"
+ "import:filename:offset:length:total:complete:"
+ "import:identifier:offset:length:total:filename:collection:originalFilename:complete:"
+ "import:signature:chunk:filename:offset:length:total:required:excludedFromBackup:complete:"
+ "importChunk:filename:offset:length:total:complete:"
+ "importChunk:identifier:offset:length:total:filename:collection:originalFilename:complete:"
+ "importContainer:signature:chunk:filename:offset:length:total:required:excludedFromBackup:complete:"
+ "ipad"
+ "iphone"
+ "ipod"
+ "isSupported:"
+ "isiPadApp"
+ "isiPhoneApp"
+ "isiPodApp"
+ "mk_fileSizeAtPath:"
+ "offset=%lld, length=%lld, total=%lld"
+ "router:didReceiveContainer:signature:chunk:filename:offset:length:total:required:excludedFromBackup:complete:"
+ "router:didReceiveFileChunk:filename:offset:length:total:complete:"
+ "router:didReceiveImageChunk:identifier:offset:length:total:filename:collection:originalFilename:complete:"
+ "router:didReceiveVideoChunk:identifier:offset:length:total:filename:collection:originalFilename:complete:"
+ "setChunkedTransferCompleted:"
+ "setIsiPadApp:"
+ "setIsiPhoneApp:"
+ "setIsiPodApp:"
+ "v60@0:8@16@24Q32Q40Q48B56"
+ "v68@0:8@\"MKPUTRouter\"16@\"NSData\"24@\"NSString\"32Q40Q48Q56B64"
+ "v68@0:8@16@24@32Q40Q48Q56B64"
+ "v84@0:8@16@24@32@40Q48Q56Q64B72B76B80"
+ "v84@0:8@16@24Q32Q40Q48@56@64@72B80"
+ "v92@0:8@\"MKPUTRouter\"16@\"NSData\"24@\"NSString\"32Q40Q48Q56@\"NSString\"64@\"NSString\"72@\"NSString\"80B88"
+ "v92@0:8@\"MKPUTRouter\"16@\"NSString\"24@\"NSString\"32@\"NSData\"40@\"NSString\"48Q56Q64Q72B80B84B88"
+ "v92@0:8@16@24@32@40@48Q56Q64Q72B80B84B88"
+ "v92@0:8@16@24@32Q40Q48Q56@64@72@80B88"
- "\x15"
- "%@ can't continue to import a media file because the file size is 0."
- "TB,N,V_isiPhone"
- "_isiPhone"
- "file=%@, offset=%ld, length=%ld, total=%ld"
- "import:filename:offset:length:total:"
- "import:identifier:offset:length:total:filename:collection:originalFilename:"
- "import:signature:chunk:filename:offset:length:total:required:excludedFromBackup:"
- "importChunk:filename:offset:length:total:"
- "importChunk:identifier:offset:length:total:filename:collection:originalFilename:"
- "importContainer:signature:chunk:filename:offset:length:total:required:excludedFromBackup:"
- "isiPhone"
- "offset=%ld, length=%ld, total=%ld"
- "router:didReceiveContainer:signature:chunk:filename:offset:length:total:required:excludedFromBackup:"
- "router:didReceiveFileChunk:filename:offset:length:total:"
- "router:didReceiveImageChunk:identifier:offset:length:total:filename:collection:originalFilename:"
- "router:didReceiveVideoChunk:identifier:offset:length:total:filename:collection:originalFilename:"
- "setIsiPhone:"
- "v56@0:8@16@24Q32Q40Q48"
- "v64@0:8@\"MKPUTRouter\"16@\"NSData\"24@\"NSString\"32Q40Q48Q56"
- "v64@0:8@16@24@32Q40Q48Q56"
- "v80@0:8@16@24@32@40Q48Q56Q64B72B76"
- "v80@0:8@16@24Q32Q40Q48@56@64@72"
- "v88@0:8@\"MKPUTRouter\"16@\"NSData\"24@\"NSString\"32Q40Q48Q56@\"NSString\"64@\"NSString\"72@\"NSString\"80"
- "v88@0:8@\"MKPUTRouter\"16@\"NSString\"24@\"NSString\"32@\"NSData\"40@\"NSString\"48Q56Q64Q72B80B84"
- "v88@0:8@16@24@32@40@48Q56Q64Q72B80B84"
- "v88@0:8@16@24@32Q40Q48Q56@64@72@80"

```
