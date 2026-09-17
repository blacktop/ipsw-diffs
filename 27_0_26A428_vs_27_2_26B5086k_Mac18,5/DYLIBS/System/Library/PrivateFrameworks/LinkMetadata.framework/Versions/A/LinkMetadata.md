## LinkMetadata

> `/System/Library/PrivateFrameworks/LinkMetadata.framework/Versions/A/LinkMetadata`

```diff

-301.0.51.1.404
-  __TEXT.__text: 0x13ff54
-  __TEXT.__objc_methlist: 0x8b0c
-  __TEXT.__const: 0x131d0
+301.1.9.1.401
+  __TEXT.__text: 0x149408
+  __TEXT.__objc_methlist: 0x8fd4
+  __TEXT.__const: 0x13790
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__cstring: 0xbd2c
-  __TEXT.__swift5_typeref: 0x5154
+  __TEXT.__cstring: 0xbfad
+  __TEXT.__swift5_typeref: 0x5394
   __TEXT.__swift5_capture: 0x620
-  __TEXT.__constg_swiftt: 0x31d4
+  __TEXT.__constg_swiftt: 0x328c
   __TEXT.__swift5_builtin: 0x3ac
   __TEXT.__swift5_mpenum: 0x78
-  __TEXT.__swift5_reflstr: 0x1ed0
-  __TEXT.__swift5_fieldmd: 0x4548
+  __TEXT.__swift5_reflstr: 0x1fc1
+  __TEXT.__swift5_fieldmd: 0x4798
   __TEXT.__swift5_assocty: 0x820
-  __TEXT.__oslogstring: 0x100a
-  __TEXT.__swift5_proto: 0x1264
-  __TEXT.__swift5_types: 0x4fc
+  __TEXT.__oslogstring: 0x1472
+  __TEXT.__swift5_proto: 0x12b8
+  __TEXT.__swift5_types: 0x514
   __TEXT.__swift5_protos: 0x14
-  __TEXT.__swift5_types2: 0x4
-  __TEXT.__gcc_except_tab: 0x588
+  __TEXT.__swift5_types2: 0x8
+  __TEXT.__gcc_except_tab: 0x5a0
   __TEXT.__ustring: 0x10
-  __TEXT.__unwind_info: 0x7478
-  __TEXT.__eh_frame: 0x613c
+  __TEXT.__unwind_info: 0x7748
+  __TEXT.__eh_frame: 0x6314
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xaa8
-  __DATA_CONST.__objc_classlist: 0x548
-  __DATA_CONST.__objc_catlist: 0x70
+  __DATA_CONST.__const: 0xa80
+  __DATA_CONST.__objc_classlist: 0x560
+  __DATA_CONST.__objc_catlist: 0xc8
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2e08
+  __DATA_CONST.__objc_selrefs: 0x2f28
   __DATA_CONST.__objc_protorefs: 0x40
-  __DATA_CONST.__objc_superrefs: 0x490
-  __DATA_CONST.__got: 0xe48
-  __AUTH_CONST.__const: 0xcbf8
-  __AUTH_CONST.__cfstring: 0x6aa0
-  __AUTH_CONST.__objc_const: 0x107e0
+  __DATA_CONST.__objc_superrefs: 0x4a8
+  __DATA_CONST.__got: 0xe70
+  __AUTH_CONST.__const: 0xcf78
+  __AUTH_CONST.__cfstring: 0x6ca0
+  __AUTH_CONST.__objc_const: 0x11190
   __AUTH_CONST.__objc_intobj: 0x6c0
-  __AUTH_CONST.__auth_got: 0x12e0
-  __AUTH.__objc_data: 0xf30
-  __AUTH.__data: 0xc10
-  __DATA.__objc_ivar: 0x880
-  __DATA.__data: 0x3d88
-  __DATA.__common: 0x28
-  __DATA_DIRTY.__objc_data: 0x2790
-  __DATA_DIRTY.__data: 0x2800
+  __AUTH_CONST.__auth_got: 0x1300
+  __AUTH.__objc_data: 0xfa8
+  __AUTH.__data: 0xc88
+  __DATA.__objc_ivar: 0x8cc
+  __DATA.__data: 0x4078
+  __DATA.__common: 0x50
+  __DATA_DIRTY.__objc_data: 0x2718
+  __DATA_DIRTY.__data: 0x2880
   __DATA_DIRTY.__bss: 0x7900
   __DATA_DIRTY.__common: 0x38
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/Versions/A/UniformTypeIdentifiers
   - /System/Library/PrivateFrameworks/AppIntentSchemas.framework/Versions/A/AppIntentSchemas
-  - /System/Library/PrivateFrameworks/AppSupport.framework/Versions/A/AppSupport
   - /System/Library/PrivateFrameworks/BaseBoard.framework/Versions/A/BaseBoard
   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
+  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftIntents.dylib

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 10150
-  Symbols:   10408
-  CStrings:  1589
+  Functions: 10334
+  Symbols:   10655
+  CStrings:  1621
 
Symbols:
+ +[LNActionMigrationMapping mappingFromParameter:]
+ +[LNActionMigrationMapping mappingWithDefaultValue:]
+ +[LNActionMigrationMapping supportsSecureCoding]
+ +[LNActionMigrationMetadata supportsSecureCoding]
+ +[LNActionMigrationNode dynamicMigrationFromIntent:toIntent:migratorMangledTypeName:fromVersion:toVersion:availabilityAnnotations:]
+ +[LNActionMigrationNode staticMigrationFromIntent:toIntent:mappings:fromVersion:toVersion:availabilityAnnotations:]
+ +[LNActionMigrationNode supportsSecureCoding]
+ -[LNActionMetadata actionMetadataWithDeprecationMetadata:]
+ -[LNActionMetadata actionMetadataWithMigrationMetadata:]
+ -[LNActionMetadata migrationMetadata]
+ -[LNActionMetadataBuilder migrationMetadata]
+ -[LNActionMetadataBuilder setMigrationMetadata:]
+ -[LNActionMigrationMapping .cxx_destruct]
+ -[LNActionMigrationMapping copyWithZone:]
+ -[LNActionMigrationMapping defaultValue]
+ -[LNActionMigrationMapping description]
+ -[LNActionMigrationMapping encodeWithCoder:]
+ -[LNActionMigrationMapping hash]
+ -[LNActionMigrationMapping initWithCoder:]
+ -[LNActionMigrationMapping initWithSourceKind:sourceParameterName:defaultValue:]
+ -[LNActionMigrationMapping isEqual:]
+ -[LNActionMigrationMapping sourceKind]
+ -[LNActionMigrationMapping sourceParameterName]
+ -[LNActionMigrationMetadata .cxx_destruct]
+ -[LNActionMigrationMetadata copyWithZone:]
+ -[LNActionMigrationMetadata description]
+ -[LNActionMigrationMetadata encodeWithCoder:]
+ -[LNActionMigrationMetadata hash]
+ -[LNActionMigrationMetadata initWithCoder:]
+ -[LNActionMigrationMetadata initWithSourceIntentIdentifier:version:nodes:]
+ -[LNActionMigrationMetadata isEqual:]
+ -[LNActionMigrationMetadata nodes]
+ -[LNActionMigrationMetadata sourceIntentIdentifier]
+ -[LNActionMigrationMetadata version]
+ -[LNActionMigrationNode .cxx_destruct]
+ -[LNActionMigrationNode availabilityAnnotations]
+ -[LNActionMigrationNode copyWithZone:]
+ -[LNActionMigrationNode description]
+ -[LNActionMigrationNode encodeWithCoder:]
+ -[LNActionMigrationNode fromVersion]
+ -[LNActionMigrationNode hash]
+ -[LNActionMigrationNode initWithCoder:]
+ -[LNActionMigrationNode initWithKind:sourceIntentIdentifier:targetIntentIdentifier:migratorMangledTypeName:mappings:fromVersion:toVersion:availabilityAnnotations:]
+ -[LNActionMigrationNode isEqual:]
+ -[LNActionMigrationNode kind]
+ -[LNActionMigrationNode mappings]
+ -[LNActionMigrationNode migratorMangledTypeName]
+ -[LNActionMigrationNode sourceIntentIdentifier]
+ -[LNActionMigrationNode targetIntentIdentifier]
+ -[LNActionMigrationNode toVersion]
+ -[LNDaemonRecord attributionBundleIdentifier]
+ -[LNDaemonRecord initWithBundleIdentifier:attributionBundleIdentifier:]
+ -[LNDisplayRepresentation hasDeferredImage]
+ -[LNDisplayRepresentation initWithTitle:subtitle:image:synonyms:descriptionText:snippetPluginModel:hasDeferredImage:]
+ -[LNEnumMetadata _casesByFillingInDisplayRepresentationsFromEnum:]
+ -[LNStaticDeferredLocalizedString _missingBundleFallback]
+ -[LNStaticDeferredLocalizedString bundleClassName]
+ -[LNStaticDeferredLocalizedString initWithKey:defaultValue:table:bundleURL:bundleClassName:]
+ -[NSArray(LNTypedNSCopying) ln_typedCopy]
+ -[NSArray(LNTypedNSCopying) ln_typedMutableCopy]
+ -[NSAttributedString(LNTypedNSCopying) ln_typedCopy]
+ -[NSAttributedString(LNTypedNSCopying) ln_typedMutableCopy]
+ -[NSCharacterSet(LNTypedNSCopying) ln_typedCopy]
+ -[NSCharacterSet(LNTypedNSCopying) ln_typedMutableCopy]
+ -[NSCoder(LNSafeDecoding) ln_decodeNullableObjectOfClasses:forKey:failureReason:]
+ -[NSData(LNTypedNSCopying) ln_typedCopy]
+ -[NSData(LNTypedNSCopying) ln_typedMutableCopy]
+ -[NSDateComponents(LNTypedNSCopying) ln_typedCopy]
+ -[NSDictionary(LNTypedNSCopying) ln_typedCopy]
+ -[NSDictionary(LNTypedNSCopying) ln_typedMutableCopy]
+ -[NSHashTable(LNTypedNSCopying) ln_typedCopy]
+ -[NSIndexSet(LNTypedNSCopying) ln_typedCopy]
+ -[NSIndexSet(LNTypedNSCopying) ln_typedMutableCopy]
+ -[NSMapTable(LNTypedNSCopying) ln_typedCopy]
+ -[NSOrderedSet(LNTypedNSCopying) ln_typedCopy]
+ -[NSOrderedSet(LNTypedNSCopying) ln_typedMutableCopy]
+ -[NSSet(LNTypedNSCopying) ln_typedCopy]
+ -[NSSet(LNTypedNSCopying) ln_typedMutableCopy]
+ -[NSString(LNStaticDeferredLocalizedString) bundleClassName]
+ -[NSString(LNTypedNSCopying) ln_typedCopy]
+ -[NSString(LNTypedNSCopying) ln_typedMutableCopy]
+ -[NSURLComponents(LNTypedNSCopying) ln_typedCopy]
+ -[NSURLRequest(LNTypedNSCopying) ln_typedCopy]
+ -[NSURLRequest(LNTypedNSCopying) ln_typedMutableCopy]
+ GCC_except_table1114
+ GCC_except_table1117
+ GCC_except_table1118
+ GCC_except_table1148
+ GCC_except_table1293
+ GCC_except_table1295
+ GCC_except_table1303
+ GCC_except_table1305
+ GCC_except_table1307
+ GCC_except_table1313
+ GCC_except_table1315
+ GCC_except_table1317
+ GCC_except_table1319
+ GCC_except_table1323
+ GCC_except_table1679
+ GCC_except_table1693
+ GCC_except_table2048
+ GCC_except_table2053
+ GCC_except_table2059
+ GCC_except_table2063
+ GCC_except_table2065
+ GCC_except_table2068
+ GCC_except_table2070
+ GCC_except_table2525
+ GCC_except_table2526
+ GCC_except_table2567
+ GCC_except_table2910
+ GCC_except_table2942
+ OBJC_IVAR_$_LNActionMetadata._migrationMetadata
+ OBJC_IVAR_$_LNActionMetadataBuilder._migrationMetadata
+ OBJC_IVAR_$_LNActionMigrationMapping._defaultValue
+ OBJC_IVAR_$_LNActionMigrationMapping._sourceKind
+ OBJC_IVAR_$_LNActionMigrationMapping._sourceParameterName
+ OBJC_IVAR_$_LNActionMigrationMetadata._nodes
+ OBJC_IVAR_$_LNActionMigrationMetadata._sourceIntentIdentifier
+ OBJC_IVAR_$_LNActionMigrationMetadata._version
+ OBJC_IVAR_$_LNActionMigrationNode._availabilityAnnotations
+ OBJC_IVAR_$_LNActionMigrationNode._fromVersion
+ OBJC_IVAR_$_LNActionMigrationNode._kind
+ OBJC_IVAR_$_LNActionMigrationNode._mappings
+ OBJC_IVAR_$_LNActionMigrationNode._migratorMangledTypeName
+ OBJC_IVAR_$_LNActionMigrationNode._sourceIntentIdentifier
+ OBJC_IVAR_$_LNActionMigrationNode._targetIntentIdentifier
+ OBJC_IVAR_$_LNActionMigrationNode._toVersion
+ OBJC_IVAR_$_LNDaemonRecord._attributionBundleIdentifier
+ OBJC_IVAR_$_LNDisplayRepresentation._hasDeferredImage
+ OBJC_IVAR_$_LNStaticDeferredLocalizedString._bundleClassName
+ _OBJC_CLASS_$_LNActionMigrationMapping
+ _OBJC_CLASS_$_LNActionMigrationMetadata
+ _OBJC_CLASS_$_LNActionMigrationNode
+ _OBJC_CLASS_$_NSHashTable
+ _OBJC_CLASS_$_NSIndexSet
+ _OBJC_CLASS_$_NSURLComponents
+ _OBJC_CLASS_$_NSURLRequest
+ _OBJC_METACLASS_$_LNActionMigrationMapping
+ _OBJC_METACLASS_$_LNActionMigrationMetadata
+ _OBJC_METACLASS_$_LNActionMigrationNode
+ _OUTLINED_FUNCTION_1387
+ _OUTLINED_FUNCTION_1388
+ _OUTLINED_FUNCTION_1389
+ _OUTLINED_FUNCTION_1390
+ _OUTLINED_FUNCTION_1391
+ _OUTLINED_FUNCTION_1392
+ _OUTLINED_FUNCTION_1393
+ _OUTLINED_FUNCTION_1394
+ _OUTLINED_FUNCTION_1395
+ _OUTLINED_FUNCTION_1396
+ _OUTLINED_FUNCTION_1397
+ _OUTLINED_FUNCTION_1398
+ _OUTLINED_FUNCTION_259
+ _OUTLINED_FUNCTION_673
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSArray_$_LNTypedNSCopying
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSCharacterSet_$_LNTypedNSCopying
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSData_$_LNTypedNSCopying
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSDateComponents_$_LNTypedNSCopying
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSHashTable_$_LNTypedNSCopying
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSIndexSet_$_LNTypedNSCopying
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSMapTable_$_LNTypedNSCopying
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSOrderedSet_$_LNTypedNSCopying
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSSet_$_LNTypedNSCopying
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSURLComponents_$_LNTypedNSCopying
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSURLRequest_$_LNTypedNSCopying
+ __OBJC_$_CATEGORY_NSArray_$_LNTypedNSCopying
+ __OBJC_$_CATEGORY_NSAttributedString_$_LNTypedNSCopying
+ __OBJC_$_CATEGORY_NSCharacterSet_$_LNTypedNSCopying
+ __OBJC_$_CATEGORY_NSData_$_LNTypedNSCopying
+ __OBJC_$_CATEGORY_NSDateComponents_$_LNTypedNSCopying
+ __OBJC_$_CATEGORY_NSHashTable_$_LNTypedNSCopying
+ __OBJC_$_CATEGORY_NSIndexSet_$_LNTypedNSCopying
+ __OBJC_$_CATEGORY_NSMapTable_$_LNTypedNSCopying
+ __OBJC_$_CATEGORY_NSOrderedSet_$_LNTypedNSCopying
+ __OBJC_$_CATEGORY_NSSet_$_LNTypedNSCopying
+ __OBJC_$_CATEGORY_NSURLComponents_$_LNTypedNSCopying
+ __OBJC_$_CATEGORY_NSURLRequest_$_LNTypedNSCopying
+ __OBJC_$_CLASS_METHODS_LNActionMigrationMapping
+ __OBJC_$_CLASS_METHODS_LNActionMigrationMetadata
+ __OBJC_$_CLASS_METHODS_LNActionMigrationNode
+ __OBJC_$_CLASS_PROP_LIST_LNActionMigrationMapping
+ __OBJC_$_CLASS_PROP_LIST_LNActionMigrationMetadata
+ __OBJC_$_CLASS_PROP_LIST_LNActionMigrationNode
+ __OBJC_$_INSTANCE_METHODS_LNActionMigrationMapping
+ __OBJC_$_INSTANCE_METHODS_LNActionMigrationMetadata
+ __OBJC_$_INSTANCE_METHODS_LNActionMigrationNode
+ __OBJC_$_INSTANCE_METHODS_NSAttributedString(LNTypedNSCopying|SecureCoding)
+ __OBJC_$_INSTANCE_METHODS_NSDictionary(Deduplication|LNTypedNSCopying)
+ __OBJC_$_INSTANCE_METHODS_NSString(LinkMetadata|LNStaticDeferredLocalizedString|LNTypedNSCopying)
+ __OBJC_$_INSTANCE_VARIABLES_LNActionMigrationMapping
+ __OBJC_$_INSTANCE_VARIABLES_LNActionMigrationMetadata
+ __OBJC_$_INSTANCE_VARIABLES_LNActionMigrationNode
+ __OBJC_$_PROP_LIST_LNActionMigrationMapping
+ __OBJC_$_PROP_LIST_LNActionMigrationMetadata
+ __OBJC_$_PROP_LIST_LNActionMigrationNode
+ __OBJC_CLASS_PROTOCOLS_$_LNActionMigrationMapping
+ __OBJC_CLASS_PROTOCOLS_$_LNActionMigrationMetadata
+ __OBJC_CLASS_PROTOCOLS_$_LNActionMigrationNode
+ __OBJC_CLASS_PROTOCOLS_$_NSString(LinkMetadata|LNStaticDeferredLocalizedString|LNTypedNSCopying)
+ __OBJC_CLASS_RO_$_LNActionMigrationMapping
+ __OBJC_CLASS_RO_$_LNActionMigrationMetadata
+ __OBJC_CLASS_RO_$_LNActionMigrationNode
+ __OBJC_METACLASS_RO_$_LNActionMigrationMapping
+ __OBJC_METACLASS_RO_$_LNActionMigrationMetadata
+ __OBJC_METACLASS_RO_$_LNActionMigrationNode
+ ___swift_memcpy88_8
+ ___unnamed_1
+ _associated conformance So21LNActionMigrationNodeC12LinkMetadataE14CodableWrapperV10CodingKeys33_57963B6478BD0DE6EA28D515C9DACEFALLOSHACSQ
+ _associated conformance So21LNActionMigrationNodeC12LinkMetadataE14CodableWrapperV10CodingKeys33_57963B6478BD0DE6EA28D515C9DACEFALLOs0H3KeyACs23CustomStringConvertible
+ _associated conformance So21LNActionMigrationNodeC12LinkMetadataE14CodableWrapperV10CodingKeys33_57963B6478BD0DE6EA28D515C9DACEFALLOs0H3KeyACs28CustomDebugStringConvertible
+ _associated conformance So24LNActionMigrationMappingC12LinkMetadataE14CodableWrapperV10CodingKeys33_57963B6478BD0DE6EA28D515C9DACEFALLOSHACSQ
+ _associated conformance So24LNActionMigrationMappingC12LinkMetadataE14CodableWrapperV10CodingKeys33_57963B6478BD0DE6EA28D515C9DACEFALLOs0H3KeyACs23CustomStringConvertible
+ _associated conformance So24LNActionMigrationMappingC12LinkMetadataE14CodableWrapperV10CodingKeys33_57963B6478BD0DE6EA28D515C9DACEFALLOs0H3KeyACs28CustomDebugStringConvertible
+ _associated conformance So25LNActionMigrationMetadataC04LinkC0E14CodableWrapperV10CodingKeys33_57963B6478BD0DE6EA28D515C9DACEFALLOSHACSQ
+ _associated conformance So25LNActionMigrationMetadataC04LinkC0E14CodableWrapperV10CodingKeys33_57963B6478BD0DE6EA28D515C9DACEFALLOs0G3KeyACs23CustomStringConvertible
+ _associated conformance So25LNActionMigrationMetadataC04LinkC0E14CodableWrapperV10CodingKeys33_57963B6478BD0DE6EA28D515C9DACEFALLOs0G3KeyACs28CustomDebugStringConvertible
+ _objc_msgSend$__swift_setObject:forKeyedSubscript:
+ _objc_msgSend$_casesByFillingInDisplayRepresentationsFromEnum:
+ _objc_msgSend$_missingBundleFallback
+ _objc_msgSend$arrayWithCapacity:
+ _objc_msgSend$audioContextTypeRawValue
+ _objc_msgSend$bundleClassName
+ _objc_msgSend$contextTypeRawValue
+ _objc_msgSend$dictionaryWithCapacity:
+ _objc_msgSend$fromVersion
+ _objc_msgSend$hasDeferredImage
+ _objc_msgSend$initWithBundleIdentifier:attributionBundleIdentifier:
+ _objc_msgSend$initWithContextTypeRawValue:audioContextTypeRawValue:workoutActivityTypeRawValue:
+ _objc_msgSend$initWithKey:defaultValue:table:bundleURL:bundleClassName:
+ _objc_msgSend$initWithKind:sourceIntentIdentifier:targetIntentIdentifier:migratorMangledTypeName:mappings:fromVersion:toVersion:availabilityAnnotations:
+ _objc_msgSend$initWithSourceIntentIdentifier:version:nodes:
+ _objc_msgSend$initWithSourceKind:sourceParameterName:defaultValue:
+ _objc_msgSend$initWithTitle:subtitle:image:synonyms:descriptionText:snippetPluginModel:hasDeferredImage:
+ _objc_msgSend$ln_decodeNullableObjectOfClasses:forKey:failureReason:
+ _objc_msgSend$ln_typedCopy
+ _objc_msgSend$ln_typedMutableCopy
+ _objc_msgSend$mappingFromParameter:
+ _objc_msgSend$mappingWithDefaultValue:
+ _objc_msgSend$mappings
+ _objc_msgSend$migrationMetadata
+ _objc_msgSend$migratorMangledTypeName
+ _objc_msgSend$nodes
+ _objc_msgSend$setMigrationMetadata:
+ _objc_msgSend$sourceIntentIdentifier
+ _objc_msgSend$sourceParameterName
+ _objc_msgSend$targetIntentIdentifier
+ _objc_msgSend$toVersion
+ _objc_msgSend$validatedWithAuditToken:requiresSignedBundle:
+ _objc_msgSend$workoutActivityTypeRawValue
+ _objc_msgSend$workoutAudioContextType
+ _symbolic SDySS_____G 10Foundation3URLV
+ _symbolic SDySS_____G So24LNActionMigrationMappingC12LinkMetadataE14CodableWrapperV
+ _symbolic SDySS_____GSg So24LNActionMigrationMappingC12LinkMetadataE14CodableWrapperV
+ _symbolic SDy__________G So13audit_token_ta s5Int32V
+ _symbolic SDyx_____G s5Int32V
+ _symbolic SS3key______5valuet So24LNActionMigrationMappingC12LinkMetadataE14CodableWrapperV
+ _symbolic SS6enumID_SS8caseNamet
+ _symbolic Say_____G So21LNActionMigrationNodeC12LinkMetadataE14CodableWrapperV
+ _symbolic So21LNActionMigrationNodeC
+ _symbolic So24LNActionMigrationMappingC
+ _symbolic So25LNActionMigrationMetadataC
+ _symbolic _____ 12LinkMetadata8LRUCacheV
+ _symbolic _____ 12LinkMetadata8LRUCacheV4Node33_BE6A19AD7A34B16B3FC027FC88D27B71LLV
+ _symbolic _____ So21LNActionMigrationNodeC12LinkMetadataE14CodableWrapperV
+ _symbolic _____ So21LNActionMigrationNodeC12LinkMetadataE14CodableWrapperV10CodingKeys33_57963B6478BD0DE6EA28D515C9DACEFALLO
+ _symbolic _____ So24LNActionMigrationMappingC12LinkMetadataE14CodableWrapperV
+ _symbolic _____ So24LNActionMigrationMappingC12LinkMetadataE14CodableWrapperV10CodingKeys33_57963B6478BD0DE6EA28D515C9DACEFALLO
+ _symbolic _____ So25LNActionMigrationMetadataC04LinkC0E14CodableWrapperV
+ _symbolic _____ So25LNActionMigrationMetadataC04LinkC0E14CodableWrapperV10CodingKeys33_57963B6478BD0DE6EA28D515C9DACEFALLO
+ _symbolic _____ s5Int32V
+ _symbolic _____Sg So25LNActionMigrationMetadataC04LinkC0E14CodableWrapperV
+ _symbolic _____ySSSo24LNActionMigrationMappingCG s18_DictionaryStorageC
+ _symbolic _____ySS_____G s18_DictionaryStorageC So24LNActionMigrationMappingC12LinkMetadataE14CodableWrapperV
+ _symbolic _____y_____G s22KeyedDecodingContainerV So21LNActionMigrationNodeC12LinkMetadataE14CodableWrapperV10CodingKeys33_57963B6478BD0DE6EA28D515C9DACEFALLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV So24LNActionMigrationMappingC12LinkMetadataE14CodableWrapperV10CodingKeys33_57963B6478BD0DE6EA28D515C9DACEFALLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV So25LNActionMigrationMetadataC04LinkF0E14CodableWrapperV10CodingKeys33_57963B6478BD0DE6EA28D515C9DACEFALLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV So21LNActionMigrationNodeC12LinkMetadataE14CodableWrapperV10CodingKeys33_57963B6478BD0DE6EA28D515C9DACEFALLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV So24LNActionMigrationMappingC12LinkMetadataE14CodableWrapperV10CodingKeys33_57963B6478BD0DE6EA28D515C9DACEFALLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV So25LNActionMigrationMetadataC04LinkF0E14CodableWrapperV10CodingKeys33_57963B6478BD0DE6EA28D515C9DACEFALLO
+ _symbolic _____y_____G s23_ContiguousArrayStorageC So21LNActionMigrationNodeC12LinkMetadataE14CodableWrapperV
+ _symbolic _____y__________G s17_NativeDictionaryV So13audit_token_ta s5Int32V
+ _symbolic _____y___________G 12LinkMetadata8LRUCacheV4Node33_BE6A19AD7A34B16B3FC027FC88D27B71LLV So13audit_token_ta AA29LNBundleValidationInformationC
+ _symbolic _____y_____y___________GG s23_ContiguousArrayStorageC 12LinkMetadata8LRUCacheV4Node33_BE6A19AD7A34B16B3FC027FC88D27B71LLV So13audit_token_ta AC29LNBundleValidationInformationC
+ _symbolic _____y_____yxq__GG s15ContiguousArrayV 12LinkMetadata8LRUCacheV4Node33_BE6A19AD7A34B16B3FC027FC88D27B71LLV
+ _type_layout_string So21LNActionMigrationNodeC12LinkMetadataE14CodableWrapperV
+ _type_layout_string So25LNActionMigrationMetadataC04LinkC0E14CodableWrapperV
- -[LNDaemonRecord initWithBundleIdentifier:]
- GCC_except_table1063
- GCC_except_table1066
- GCC_except_table1067
- GCC_except_table1097
- GCC_except_table1241
- GCC_except_table1243
- GCC_except_table1251
- GCC_except_table1253
- GCC_except_table1255
- GCC_except_table1260
- GCC_except_table1262
- GCC_except_table1264
- GCC_except_table1266
- GCC_except_table1269
- GCC_except_table1622
- GCC_except_table1636
- GCC_except_table1967
- GCC_except_table1972
- GCC_except_table1978
- GCC_except_table1982
- GCC_except_table1984
- GCC_except_table1987
- GCC_except_table1989
- GCC_except_table2443
- GCC_except_table2444
- GCC_except_table2485
- GCC_except_table2828
- GCC_except_table2860
- _OUTLINED_FUNCTION_264
- _OUTLINED_FUNCTION_675
- __OBJC_$_CATEGORY_INSTANCE_METHODS_NSAttributedString_$_SecureCoding
- __OBJC_$_CATEGORY_INSTANCE_METHODS_NSDictionary_$_Deduplication
- __OBJC_$_CATEGORY_NSAttributedString_$_SecureCoding
- __OBJC_$_INSTANCE_METHODS_NSString(LinkMetadata|LNStaticDeferredLocalizedString)
- __OBJC_CLASS_PROTOCOLS_$_NSString(LinkMetadata|LNStaticDeferredLocalizedString)
- _objc_msgSend$initWithAuditToken:requiresSignedBundle:
- _objc_msgSend$initWithBundleIdentifier:
- _symbolic _____ 12LinkMetadata18LNAppEntityContextC
- _type_layout_string So28LNAssistantAppEntityMetadataC04LinkD0E14CodableWrapperV
CStrings:
+ "<%@: %p, default: %@>"
+ "<%@: %p, identifier: %@, effectiveBundleIdentifiers: [%@], allowedTargets: [%@],bundleMetadataVersion: %@, title: %@, description: %@, deprecation: %@, migration: %@,parameters: [%@], openAppWhenRun: %@, supportedModes: %@, visibility: %@, explicitAuthenticationPolicy: %@, outputType: %@, systemProtocolMetadata: [%@], actionConfiguration: %@, typeSpecificMetadata: %@, customIntentClassName: %@, mangledTypeNameByBundleIdentifier: %@, availabilityAnnotations: %@, shortcutsMetadata: %@, requiredCapabilities: %@, attributionBundleIdentifier: %@, sideEffect: %@, assistantDefinedSchemas: %@, assistantDefinedSchemaTraits: %@, fullyQualifiedTypeName: %@>"
+ "<%@: %p, kind: %ld, source: %@, target: %@, migrator: %@, mappings: %@, fromVersion: %ld, toVersion: %ld, availability: %@>"
+ "<%@: %p, parameter: %@>"
+ "<%@: %p, source: %@, version: %ld, nodes: %@>"
+ "<%@: %p, title: %@, subtitle: %@, image: %@, synonyms: %@, descriptionText: %@, snippetPluginModel: %@, hasDeferredImage: %@>"
+ "Cache hit for %s from %s"
+ "Cache insert for %s from %s"
+ "Cached bundle for %s was not fully validated, rechecking..."
+ "Could not resolve '%{public}s' to a framework bundle. The framework may not be embedded in this host app, or its module name may differ from the class's module. Strings will fall back to the LSR's defaultValue (or key when default is empty)."
+ "Decoded migration metadata for “%{public}s”: version %{public}ld, %{public}ld node(s)"
+ "Decoded “%{public}s” with no migration metadata"
+ "Dropping migration from “%{public}s” to “%{public}s”: kind %{public}ld with a mismatched payload"
+ "Dropping migration from “%{public}s” to “%{public}s”: undecodable mappings"
+ "Dropping migration mapping with unknown source kind %{public}ld"
+ "Dropping migration mapping: default kind with a mismatched payload"
+ "Dropping migration mapping: default value the archive can't rebuild"
+ "Dropping migration mapping: parameter kind with a mismatched payload"
+ "Failed to decode LNValue: its %{public}@ payload could not be decoded"
+ "LNActionMigrationMetadata.m"
+ "LNStaticDeferredLocalizedString.indexingBundleURLByClassName"
+ "LinkProgrammaticInterface-301.1.9.1.401"
+ "_display_representation"
+ "bundleClassName"
+ "cross-bundle-localization"
+ "fromVersion"
+ "hasDeferredImage"
+ "mappings"
+ "migrationMetadata"
+ "migratorMangledTypeName"
+ "nodes"
+ "sourceIntentIdentifier"
+ "sourceParameterName"
+ "targetIntentIdentifier"
+ "toVersion"
- "<%@: %p, identifier: %@, effectiveBundleIdentifiers: [%@], allowedTargets: [%@],bundleMetadataVersion: %@, title: %@, description: %@, deprecation: %@,parameters: [%@], openAppWhenRun: %@, supportedModes: %@, visibility: %@, explicitAuthenticationPolicy: %@, outputType: %@, systemProtocolMetadata: [%@], actionConfiguration: %@, typeSpecificMetadata: %@, customIntentClassName: %@, mangledTypeNameByBundleIdentifier: %@, availabilityAnnotations: %@, shortcutsMetadata: %@, requiredCapabilities: %@, attributionBundleIdentifier: %@, sideEffect: %@, assistantDefinedSchemas: %@, assistantDefinedSchemaTraits: %@, fullyQualifiedTypeName: %@>"
- "<%@: %p, title: %@, subtitle: %@, image: %@, synonyms: %@, descriptionText: %@, snippetPluginModel: %@>"
- "LinkProgrammaticInterface-301.0.51.1.404"
```
