## LinkMetadata

> `/System/Library/PrivateFrameworks/LinkMetadata.framework/LinkMetadata`

```diff

-257.1.0.0.0
-  __TEXT.__text: 0x10b3fc
+261.0.0.0.0
+  __TEXT.__text: 0x10ed98
   __TEXT.__auth_stubs: 0x2090
-  __TEXT.__objc_methlist: 0x6a1c
+  __TEXT.__objc_methlist: 0x6be4
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__const: 0xf570
-  __TEXT.__cstring: 0x90b4
-  __TEXT.__swift5_typeref: 0x43aa
-  __TEXT.__constg_swiftt: 0x28bc
+  __TEXT.__const: 0xf840
+  __TEXT.__cstring: 0x9210
+  __TEXT.__swift5_typeref: 0x44a8
+  __TEXT.__constg_swiftt: 0x2954
   __TEXT.__swift5_builtin: 0x2f8
   __TEXT.__swift5_mpenum: 0x5c
-  __TEXT.__swift5_reflstr: 0x1879
-  __TEXT.__swift5_fieldmd: 0x39d8
+  __TEXT.__swift5_reflstr: 0x1889
+  __TEXT.__swift5_fieldmd: 0x3ad8
   __TEXT.__swift5_assocty: 0x6a0
   __TEXT.__swift5_capture: 0x350
   __TEXT.__oslogstring: 0xb33
-  __TEXT.__swift5_proto: 0xfcc
-  __TEXT.__swift5_types: 0x43c
+  __TEXT.__swift5_proto: 0x1004
+  __TEXT.__swift5_types: 0x44c
   __TEXT.__swift5_protos: 0x10
   __TEXT.__gcc_except_tab: 0x3d0
-  __TEXT.__unwind_info: 0x4a80
-  __TEXT.__eh_frame: 0x5e7c
-  __TEXT.__objc_classname: 0xdbc
-  __TEXT.__objc_methname: 0xee82
-  __TEXT.__objc_methtype: 0x1931
-  __TEXT.__objc_stubs: 0x6a20
-  __DATA_CONST.__got: 0xc98
+  __TEXT.__unwind_info: 0x4b28
+  __TEXT.__eh_frame: 0x5ef4
+  __TEXT.__objc_classname: 0xde7
+  __TEXT.__objc_methname: 0xf641
+  __TEXT.__objc_methtype: 0x1a55
+  __TEXT.__objc_stubs: 0x6bc0
+  __DATA_CONST.__got: 0xca8
   __DATA_CONST.__const: 0xd48
-  __DATA_CONST.__objc_classlist: 0x430
+  __DATA_CONST.__objc_classlist: 0x440
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x25c8
+  __DATA_CONST.__objc_selrefs: 0x2640
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x3a0
+  __DATA_CONST.__objc_superrefs: 0x3b0
   __AUTH_CONST.__auth_got: 0x1058
-  __AUTH_CONST.__const: 0xa380
-  __AUTH_CONST.__cfstring: 0x5600
-  __AUTH_CONST.__objc_const: 0xc6a0
+  __AUTH_CONST.__const: 0xa550
+  __AUTH_CONST.__cfstring: 0x5700
+  __AUTH_CONST.__objc_const: 0xca30
   __AUTH_CONST.__objc_intobj: 0x678
-  __AUTH.__objc_data: 0xc08
-  __AUTH.__data: 0x628
-  __DATA.__objc_ivar: 0x5d0
-  __DATA.__data: 0x29b8
-  __DATA.__bss: 0x13cf0
+  __AUTH.__objc_data: 0xca8
+  __AUTH.__data: 0x640
+  __DATA.__objc_ivar: 0x5f4
+  __DATA.__data: 0x2a78
+  __DATA.__bss: 0x143f0
   __DATA.__common: 0x30
   __DATA_DIRTY.__objc_data: 0x1e50
-  __DATA_DIRTY.__data: 0x3340
+  __DATA_DIRTY.__data: 0x3310
   __DATA_DIRTY.__bss: 0xc510
   __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 2BC93C64-6EE7-3CBA-9B18-F74DF9BADF8B
-  Functions: 7474
-  Symbols:   10799
-  CStrings:  4044
+  UUID: B5C39F4F-DAF8-3BC2-BF6D-916A093BD7BB
+  Functions: 7568
+  Symbols:   10958
+  CStrings:  4089
 
Symbols:
+ +[LNTargetMetadata defaultTarget]
+ +[LNTargetMetadata mainTarget]
+ +[LNTargetMetadata supportsSecureCoding]
+ +[LNTargetMetadataCondition foregroundCondition]
+ +[LNTargetMetadataCondition supportsSecureCoding]
+ -[LNActionMetadata allowedTargets]
+ -[LNActionMetadata initWithIdentifier:mangledTypeName:mangledTypeNameByBundleIdentifier:effectiveBundleIdentifiers:bundleMetadataVersion:title:descriptionMetadata:deprecationMetadata:openAppWhenRun:supportedModes:explicitAuthenticationPolicy:outputType:outputFlags:parameters:systemProtocolMetadata:actionConfiguration:typeSpecificMetadata:customIntentClassName:availabilityAnnotations:shortcutsMetadata:requiredCapabilities:attributionBundleIdentifier:sideEffect:assistantDefinedSchemas:assistantDefinedSchemaTraits:visibilityMetadata:fullyQualifiedTypeName:constraints:allowedTargets:]
+ -[LNActionMetadata(Deprecated) initWithIdentifier:mangledTypeName:mangledTypeNameByBundleIdentifier:effectiveBundleIdentifiers:bundleMetadataVersion:title:descriptionMetadata:deprecationMetadata:openAppWhenRun:supportedModes:explicitAuthenticationPolicy:outputType:outputFlags:parameters:systemProtocolMetadata:actionConfiguration:typeSpecificMetadata:customIntentClassName:availabilityAnnotations:shortcutsMetadata:requiredCapabilities:attributionBundleIdentifier:sideEffect:assistantDefinedSchemas:assistantDefinedSchemaTraits:visibilityMetadata:fullyQualifiedTypeName:constraints:]
+ -[LNEntityIdentifier bundleIdentifier]
+ -[LNEntityIdentifier initWithTypeIdentifier:bundleIdentifier:instanceIdentifier:]
+ -[LNEntityMetadata allowedTargets]
+ -[LNEntityMetadata initWithIdentifier:transient:mangledTypeName:mangledTypeNameByBundleIdentifier:effectiveBundleIdentifiers:displayRepresentation:properties:customIntentTypeClassName:availabilityAnnotations:requiredCapabilities:systemProtocolMetadata:attributionBundleIdentifier:transferableContentTypes:assistantDefinedSchemas:fullyQualifiedTypeName:visibilityMetadata:defaultQueryIdentifier:allowedTargets:]
+ -[LNEntityMetadata(Deprecated) initWithIdentifier:transient:mangledTypeName:mangledTypeNameByBundleIdentifier:effectiveBundleIdentifiers:displayRepresentation:properties:customIntentTypeClassName:availabilityAnnotations:requiredCapabilities:systemProtocolMetadata:attributionBundleIdentifier:transferableContentTypes:assistantDefinedSchemas:fullyQualifiedTypeName:visibilityMetadata:defaultQueryIdentifier:]
+ -[LNEnumMetadata allowedTargets]
+ -[LNEnumMetadata initWithIdentifier:mangledTypeName:mangledTypeNameByBundleIdentifier:effectiveBundleIdentifiers:displayRepresentation:cases:customIntentEnumTypeName:availabilityAnnotations:system:fullyQualifiedTypeName:assistantDefinedSchemas:visibilityMetadata:allowedTargets:]
+ -[LNEnumMetadata(Deprecated) initWithIdentifier:mangledTypeName:mangledTypeNameByBundleIdentifier:effectiveBundleIdentifiers:displayRepresentation:cases:customIntentEnumTypeName:availabilityAnnotations:system:fullyQualifiedTypeName:assistantDefinedSchemas:visibilityMetadata:]
+ -[LNQueryMetadata allowedTargets]
+ -[LNQueryMetadata initWithIdentifier:inputValueType:resultValueType:mangledTypeName:mangledTypeNameByBundleIdentifier:effectiveBundleIdentifiers:parameters:sortingOptions:availabilityAnnotations:capabilities:descriptionMetadata:visibilityMetadata:defaultQueryForEntity:fullyQualifiedIdentifier:allowedTargets:]
+ -[LNQueryMetadata(Deprecated) initWithIdentifier:inputValueType:resultValueType:mangledTypeName:mangledTypeNameByBundleIdentifier:effectiveBundleIdentifiers:parameters:sortingOptions:availabilityAnnotations:capabilities:descriptionMetadata:visibilityMetadata:defaultQueryForEntity:fullyQualifiedIdentifier:]
+ -[LNTargetMetadata .cxx_destruct]
+ -[LNTargetMetadata bundleIdentifier]
+ -[LNTargetMetadata conditions]
+ -[LNTargetMetadata copyWithZone:]
+ -[LNTargetMetadata description]
+ -[LNTargetMetadata encodeWithCoder:]
+ -[LNTargetMetadata hash]
+ -[LNTargetMetadata initWithBundleIdentifier:conditions:]
+ -[LNTargetMetadata initWithCoder:]
+ -[LNTargetMetadata initWithType:bundleIdentifier:conditions:]
+ -[LNTargetMetadata isEqual:]
+ -[LNTargetMetadata type]
+ -[LNTargetMetadataCondition copyWithZone:]
+ -[LNTargetMetadataCondition description]
+ -[LNTargetMetadataCondition encodeWithCoder:]
+ -[LNTargetMetadataCondition hash]
+ -[LNTargetMetadataCondition identifier]
+ -[LNTargetMetadataCondition initWithCoder:]
+ -[LNTargetMetadataCondition initWithIdentifier:]
+ -[LNTargetMetadataCondition isEqual:]
+ GCC_except_table1158
+ GCC_except_table1385
+ GCC_except_table1850
+ GCC_except_table1853
+ GCC_except_table1854
+ GCC_except_table1878
+ GCC_except_table669
+ GCC_except_table671
+ GCC_except_table681
+ GCC_except_table683
+ GCC_except_table692
+ GCC_except_table694
+ GCC_except_table697
+ _OBJC_CLASS_$_LNTargetMetadata
+ _OBJC_CLASS_$_LNTargetMetadataCondition
+ _OBJC_IVAR_$_LNActionMetadata._allowedTargets
+ _OBJC_IVAR_$_LNEntityIdentifier._bundleIdentifier
+ _OBJC_IVAR_$_LNEntityMetadata._allowedTargets
+ _OBJC_IVAR_$_LNEnumMetadata._allowedTargets
+ _OBJC_IVAR_$_LNQueryMetadata._allowedTargets
+ _OBJC_IVAR_$_LNTargetMetadata._bundleIdentifier
+ _OBJC_IVAR_$_LNTargetMetadata._conditions
+ _OBJC_IVAR_$_LNTargetMetadata._type
+ _OBJC_IVAR_$_LNTargetMetadataCondition._identifier
+ _OBJC_METACLASS_$_LNTargetMetadata
+ _OBJC_METACLASS_$_LNTargetMetadataCondition
+ _OUTLINED_FUNCTION_182
+ _OUTLINED_FUNCTION_338
+ _OUTLINED_FUNCTION_414
+ _OUTLINED_FUNCTION_415
+ _OUTLINED_FUNCTION_416
+ _OUTLINED_FUNCTION_417
+ _OUTLINED_FUNCTION_418
+ _OUTLINED_FUNCTION_419
+ _OUTLINED_FUNCTION_420
+ _OUTLINED_FUNCTION_421
+ _OUTLINED_FUNCTION_422
+ _OUTLINED_FUNCTION_423
+ _OUTLINED_FUNCTION_424
+ _OUTLINED_FUNCTION_425
+ _OUTLINED_FUNCTION_426
+ _OUTLINED_FUNCTION_427
+ _OUTLINED_FUNCTION_428
+ _OUTLINED_FUNCTION_429
+ _OUTLINED_FUNCTION_430
+ _OUTLINED_FUNCTION_431
+ __OBJC_$_CLASS_METHODS_LNTargetMetadata
+ __OBJC_$_CLASS_METHODS_LNTargetMetadataCondition
+ __OBJC_$_CLASS_PROP_LIST_LNTargetMetadata
+ __OBJC_$_CLASS_PROP_LIST_LNTargetMetadataCondition
+ __OBJC_$_INSTANCE_METHODS_LNTargetMetadata
+ __OBJC_$_INSTANCE_METHODS_LNTargetMetadataCondition
+ __OBJC_$_INSTANCE_VARIABLES_LNTargetMetadata
+ __OBJC_$_INSTANCE_VARIABLES_LNTargetMetadataCondition
+ __OBJC_$_PROP_LIST_LNTargetMetadata
+ __OBJC_$_PROP_LIST_LNTargetMetadataCondition
+ __OBJC_CLASS_PROTOCOLS_$_LNTargetMetadata
+ __OBJC_CLASS_PROTOCOLS_$_LNTargetMetadataCondition
+ __OBJC_CLASS_RO_$_LNTargetMetadata
+ __OBJC_CLASS_RO_$_LNTargetMetadataCondition
+ __OBJC_METACLASS_RO_$_LNTargetMetadata
+ __OBJC_METACLASS_RO_$_LNTargetMetadataCondition
+ ___587-[LNActionMetadata initWithIdentifier:mangledTypeName:mangledTypeNameByBundleIdentifier:effectiveBundleIdentifiers:bundleMetadataVersion:title:descriptionMetadata:deprecationMetadata:openAppWhenRun:supportedModes:explicitAuthenticationPolicy:outputType:outputFlags:parameters:systemProtocolMetadata:actionConfiguration:typeSpecificMetadata:customIntentClassName:availabilityAnnotations:shortcutsMetadata:requiredCapabilities:attributionBundleIdentifier:sideEffect:assistantDefinedSchemas:assistantDefinedSchemaTraits:visibilityMetadata:fullyQualifiedTypeName:constraints:allowedTargets:]_block_invoke
+ ___Block_byref_object_copy_.8615
+ ___Block_byref_object_dispose_.8616
+ ___block_literal_global.10.6633
+ ___block_literal_global.12.1226
+ ___block_literal_global.12.6631
+ ___block_literal_global.1238
+ ___block_literal_global.14.1224
+ ___block_literal_global.14.4019
+ ___block_literal_global.14.6629
+ ___block_literal_global.1416
+ ___block_literal_global.16.1222
+ ___block_literal_global.16.6627
+ ___block_literal_global.168
+ ___block_literal_global.18.1220
+ ___block_literal_global.18.6625
+ ___block_literal_global.2.1236
+ ___block_literal_global.2.4265
+ ___block_literal_global.2.6641
+ ___block_literal_global.20.1218
+ ___block_literal_global.20.4023
+ ___block_literal_global.20.6623
+ ___block_literal_global.22.1216
+ ___block_literal_global.22.6621
+ ___block_literal_global.2345
+ ___block_literal_global.24.1214
+ ___block_literal_global.24.6619
+ ___block_literal_global.26.4025
+ ___block_literal_global.26.6617
+ ___block_literal_global.28.6615
+ ___block_literal_global.30.6613
+ ___block_literal_global.32.6611
+ ___block_literal_global.3258
+ ___block_literal_global.38.6609
+ ___block_literal_global.38.8624
+ ___block_literal_global.3980
+ ___block_literal_global.4.1234
+ ___block_literal_global.4.4263
+ ___block_literal_global.4.6639
+ ___block_literal_global.4013
+ ___block_literal_global.4267
+ ___block_literal_global.4999
+ ___block_literal_global.5061
+ ___block_literal_global.6.1232
+ ___block_literal_global.6.6637
+ ___block_literal_global.6057
+ ___block_literal_global.6643
+ ___block_literal_global.7199
+ ___block_literal_global.8.1228
+ ___block_literal_global.8.4017
+ ___block_literal_global.8.6635
+ ___block_literal_global.8061
+ ___block_literal_global.8635
+ ___block_literal_global.8955
+ ___block_literal_global.9432
+ ___block_literal_global.964
+ ___swift_get_extra_inhabitant_index.415Tm
+ ___swift_store_extra_inhabitant_index.416Tm
+ _allProtocolsByIdentifier.onceToken.8951
+ _allProtocolsByIdentifier.protocolsByIdentifier.8952
+ _associated conformance So16LNTargetMetadataC04LinkB0E14CodableWrapper33_8F5A22252D2EEFBD74C1473F6DDC7E6CLLV10CodingKeysOSHACSQ
+ _associated conformance So16LNTargetMetadataC04LinkB0E14CodableWrapper33_8F5A22252D2EEFBD74C1473F6DDC7E6CLLV10CodingKeysOs0N3KeyACs23CustomStringConvertible
+ _associated conformance So16LNTargetMetadataC04LinkB0E14CodableWrapper33_8F5A22252D2EEFBD74C1473F6DDC7E6CLLV10CodingKeysOs0N3KeyACs28CustomDebugStringConvertible
+ _associated conformance So25LNTargetMetadataConditionC04LinkB0E14CodableWrapper33_8F5A22252D2EEFBD74C1473F6DDC7E6CLLV10CodingKeysOSHACSQ
+ _associated conformance So25LNTargetMetadataConditionC04LinkB0E14CodableWrapper33_8F5A22252D2EEFBD74C1473F6DDC7E6CLLV10CodingKeysOs0O3KeyACs23CustomStringConvertible
+ _associated conformance So25LNTargetMetadataConditionC04LinkB0E14CodableWrapper33_8F5A22252D2EEFBD74C1473F6DDC7E6CLLV10CodingKeysOs0O3KeyACs28CustomDebugStringConvertible
+ _objc_msgSend$JSONObjectWithData:options:error:
+ _objc_msgSend$allowedTargets
+ _objc_msgSend$conditions
+ _objc_msgSend$dataUsingEncoding:
+ _objc_msgSend$dataWithJSONObject:options:error:
+ _objc_msgSend$hasPrefix:
+ _objc_msgSend$initWithData:encoding:
+ _objc_msgSend$initWithIdentifier:inputValueType:resultValueType:mangledTypeName:mangledTypeNameByBundleIdentifier:effectiveBundleIdentifiers:parameters:sortingOptions:availabilityAnnotations:capabilities:descriptionMetadata:visibilityMetadata:defaultQueryForEntity:fullyQualifiedIdentifier:allowedTargets:
+ _objc_msgSend$initWithIdentifier:mangledTypeName:mangledTypeNameByBundleIdentifier:effectiveBundleIdentifiers:bundleMetadataVersion:title:descriptionMetadata:deprecationMetadata:openAppWhenRun:supportedModes:explicitAuthenticationPolicy:outputType:outputFlags:parameters:systemProtocolMetadata:actionConfiguration:typeSpecificMetadata:customIntentClassName:availabilityAnnotations:shortcutsMetadata:requiredCapabilities:attributionBundleIdentifier:sideEffect:assistantDefinedSchemas:assistantDefinedSchemaTraits:visibilityMetadata:fullyQualifiedTypeName:constraints:allowedTargets:
+ _objc_msgSend$initWithIdentifier:mangledTypeName:mangledTypeNameByBundleIdentifier:effectiveBundleIdentifiers:displayRepresentation:cases:customIntentEnumTypeName:availabilityAnnotations:system:fullyQualifiedTypeName:assistantDefinedSchemas:visibilityMetadata:allowedTargets:
+ _objc_msgSend$initWithIdentifier:transient:mangledTypeName:mangledTypeNameByBundleIdentifier:effectiveBundleIdentifiers:displayRepresentation:properties:customIntentTypeClassName:availabilityAnnotations:requiredCapabilities:systemProtocolMetadata:attributionBundleIdentifier:transferableContentTypes:assistantDefinedSchemas:fullyQualifiedTypeName:visibilityMetadata:defaultQueryIdentifier:allowedTargets:
+ _objc_msgSend$initWithType:bundleIdentifier:conditions:
+ _objc_msgSend$initWithTypeIdentifier:bundleIdentifier:instanceIdentifier:
+ _objectClassesForCoding.objectClassesForCoding.3981
+ _objectClassesForCoding.onceToken.3979
+ _stringValueType.onceToken.963
+ _stringValueType.value.965
+ _symbolic Say_____G So16LNTargetMetadataC04LinkB0E14CodableWrapper33_8F5A22252D2EEFBD74C1473F6DDC7E6CLLV
+ _symbolic Say_____G So25LNTargetMetadataConditionC04LinkB0E14CodableWrapper33_8F5A22252D2EEFBD74C1473F6DDC7E6CLLV
+ _symbolic Say_____GSg So16LNTargetMetadataC04LinkB0E14CodableWrapper33_8F5A22252D2EEFBD74C1473F6DDC7E6CLLV
+ _symbolic Say_____GSg So25LNTargetMetadataConditionC04LinkB0E14CodableWrapper33_8F5A22252D2EEFBD74C1473F6DDC7E6CLLV
+ _symbolic So16LNTargetMetadataC
+ _symbolic So25LNTargetMetadataConditionC
+ _symbolic _____ So16LNTargetMetadataC04LinkB0E14CodableWrapper33_8F5A22252D2EEFBD74C1473F6DDC7E6CLLV
+ _symbolic _____ So16LNTargetMetadataC04LinkB0E14CodableWrapper33_8F5A22252D2EEFBD74C1473F6DDC7E6CLLV10CodingKeysO
+ _symbolic _____ So25LNTargetMetadataConditionC04LinkB0E14CodableWrapper33_8F5A22252D2EEFBD74C1473F6DDC7E6CLLV
+ _symbolic _____ So25LNTargetMetadataConditionC04LinkB0E14CodableWrapper33_8F5A22252D2EEFBD74C1473F6DDC7E6CLLV10CodingKeysO
+ _symbolic _____y_____G s22KeyedDecodingContainerV So16LNTargetMetadataC04LinkE0E14CodableWrapper33_8F5A22252D2EEFBD74C1473F6DDC7E6CLLV10CodingKeysO
+ _symbolic _____y_____G s22KeyedDecodingContainerV So25LNTargetMetadataConditionC04LinkE0E14CodableWrapper33_8F5A22252D2EEFBD74C1473F6DDC7E6CLLV10CodingKeysO
+ _symbolic _____y_____G s22KeyedEncodingContainerV So16LNTargetMetadataC04LinkE0E14CodableWrapper33_8F5A22252D2EEFBD74C1473F6DDC7E6CLLV10CodingKeysO
+ _symbolic _____y_____G s22KeyedEncodingContainerV So25LNTargetMetadataConditionC04LinkE0E14CodableWrapper33_8F5A22252D2EEFBD74C1473F6DDC7E6CLLV10CodingKeysO
+ _symbolic _____y_____G s23_ContiguousArrayStorageC So16LNTargetMetadataC04LinkE0E14CodableWrapper33_8F5A22252D2EEFBD74C1473F6DDC7E6CLLV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC So25LNTargetMetadataConditionC04LinkE0E14CodableWrapper33_8F5A22252D2EEFBD74C1473F6DDC7E6CLLV
+ _type_layout_string So16LNTargetMetadataC04LinkB0E14CodableWrapper33_8F5A22252D2EEFBD74C1473F6DDC7E6CLLV
+ _urlRepresentableProtocol.onceToken.8953
+ _urlRepresentableProtocol.value.8954
- -[LNActionMetadata initWithIdentifier:mangledTypeName:mangledTypeNameByBundleIdentifier:effectiveBundleIdentifiers:bundleMetadataVersion:title:descriptionMetadata:deprecationMetadata:openAppWhenRun:supportedModes:explicitAuthenticationPolicy:outputType:outputFlags:parameters:systemProtocolMetadata:actionConfiguration:typeSpecificMetadata:customIntentClassName:availabilityAnnotations:shortcutsMetadata:requiredCapabilities:attributionBundleIdentifier:sideEffect:assistantDefinedSchemas:assistantDefinedSchemaTraits:visibilityMetadata:fullyQualifiedTypeName:constraints:]
- -[LNEntityMetadata initWithIdentifier:transient:mangledTypeName:mangledTypeNameByBundleIdentifier:effectiveBundleIdentifiers:displayRepresentation:properties:customIntentTypeClassName:availabilityAnnotations:requiredCapabilities:systemProtocolMetadata:attributionBundleIdentifier:transferableContentTypes:assistantDefinedSchemas:fullyQualifiedTypeName:visibilityMetadata:defaultQueryIdentifier:]
- -[LNEnumMetadata initWithIdentifier:mangledTypeName:mangledTypeNameByBundleIdentifier:effectiveBundleIdentifiers:displayRepresentation:cases:customIntentEnumTypeName:availabilityAnnotations:system:fullyQualifiedTypeName:assistantDefinedSchemas:visibilityMetadata:]
- -[LNQueryMetadata initWithIdentifier:inputValueType:resultValueType:mangledTypeName:mangledTypeNameByBundleIdentifier:effectiveBundleIdentifiers:parameters:sortingOptions:availabilityAnnotations:capabilities:descriptionMetadata:visibilityMetadata:defaultQueryForEntity:fullyQualifiedIdentifier:]
- GCC_except_table1129
- GCC_except_table1354
- GCC_except_table1815
- GCC_except_table1818
- GCC_except_table1819
- GCC_except_table1843
- GCC_except_table665
- GCC_except_table667
- GCC_except_table675
- GCC_except_table677
- GCC_except_table684
- GCC_except_table686
- GCC_except_table693
- _OUTLINED_FUNCTION_188
- _OUTLINED_FUNCTION_351
- ___572-[LNActionMetadata initWithIdentifier:mangledTypeName:mangledTypeNameByBundleIdentifier:effectiveBundleIdentifiers:bundleMetadataVersion:title:descriptionMetadata:deprecationMetadata:openAppWhenRun:supportedModes:explicitAuthenticationPolicy:outputType:outputFlags:parameters:systemProtocolMetadata:actionConfiguration:typeSpecificMetadata:customIntentClassName:availabilityAnnotations:shortcutsMetadata:requiredCapabilities:attributionBundleIdentifier:sideEffect:assistantDefinedSchemas:assistantDefinedSchemaTraits:visibilityMetadata:fullyQualifiedTypeName:constraints:]_block_invoke
- ___Block_byref_object_copy_.8479
- ___Block_byref_object_dispose_.8480
- ___block_literal_global.10.6501
- ___block_literal_global.12.1220
- ___block_literal_global.12.6499
- ___block_literal_global.1232
- ___block_literal_global.14.1218
- ___block_literal_global.14.3913
- ___block_literal_global.14.6497
- ___block_literal_global.1410
- ___block_literal_global.16.1216
- ___block_literal_global.16.6495
- ___block_literal_global.164
- ___block_literal_global.18.1214
- ___block_literal_global.18.6493
- ___block_literal_global.2.1230
- ___block_literal_global.2.4158
- ___block_literal_global.2.6509
- ___block_literal_global.20.1212
- ___block_literal_global.20.3917
- ___block_literal_global.20.6491
- ___block_literal_global.22.1210
- ___block_literal_global.22.6489
- ___block_literal_global.2346
- ___block_literal_global.24.1208
- ___block_literal_global.24.6487
- ___block_literal_global.26.3919
- ___block_literal_global.26.6485
- ___block_literal_global.28.6483
- ___block_literal_global.30.6481
- ___block_literal_global.3156
- ___block_literal_global.32.6479
- ___block_literal_global.38.6477
- ___block_literal_global.38.8488
- ___block_literal_global.3874
- ___block_literal_global.3907
- ___block_literal_global.4.1228
- ___block_literal_global.4.4156
- ___block_literal_global.4.6507
- ___block_literal_global.4160
- ___block_literal_global.4884
- ___block_literal_global.4946
- ___block_literal_global.5930
- ___block_literal_global.6.1226
- ___block_literal_global.6.6505
- ___block_literal_global.6511
- ___block_literal_global.7067
- ___block_literal_global.7917
- ___block_literal_global.8.1222
- ___block_literal_global.8.3911
- ___block_literal_global.8.6503
- ___block_literal_global.8500
- ___block_literal_global.8810
- ___block_literal_global.9279
- ___block_literal_global.949
- ___swift_get_extra_inhabitant_index.409Tm
- ___swift_store_extra_inhabitant_index.410Tm
- _allProtocolsByIdentifier.onceToken.8806
- _allProtocolsByIdentifier.protocolsByIdentifier.8807
- _objectClassesForCoding.objectClassesForCoding.3875
- _objectClassesForCoding.onceToken.3873
- _stringValueType.onceToken.948
- _stringValueType.value.950
- _urlRepresentableProtocol.onceToken.8808
- _urlRepresentableProtocol.value.8809
CStrings:
+ "\r"
+ "<%@: %p, bundleIdentifier: %@, conditions: %@>"
+ "<%@: %p, displayRepresentation: %@, mangledTypeNameByBundleIdentifier: %@, effectiveBundleIdentifiers: [%@], allowedTargets: [%@], availabilityAnnotations: %@, fullyQualifiedTypeName: %@, assistantDefinedSchemas: %@, visibility: %@>"
+ "<%@: %p, identifier: %@, effectiveBundleIdentifiers: [%@], allowedTargets: [%@],bundleMetadataVersion: %@, title: %@, description: %@, deprecation: %@,parameters: [%@], openAppWhenRun: %@, supportedModes: %@, visibility: %@, explicitAuthenticationPolicy: %@, outputType: %@, systemProtocolMetadata: [%@], actionConfiguration: %@, typeSpecificMetadata: %@, customIntentClassName: %@, mangledTypeNameByBundleIdentifier: %@, availabilityAnnotations: %@, shortcutsMetadata: %@, requiredCapabilities: %@, attributionBundleIdentifier: %@, sideEffect: %@, assistantDefinedSchemas: %@, assistantDefinedSchemaTraits: %@, fullyQualifiedTypeName: %@>"
+ "<%@: %p, identifier: %@, inputValueType: %@, resultValueType: %@, effectiveBundleIdentifiers: [%@], allowedTargets: [%@], mangledTypeNameByBundleIdentifier: %@, parameters: [%@], sortingOptions: [%@], availabilityAnnotations: %@, descriptionMetadata: %@, visibility: %@, defaultEntityQuery: %@>"
+ "<%@: %p, identifier: %@, transient: %@, displayRepresentation: %@, effectiveBundleIdentifiers: [%@], allowedTargets: [%@], mangledTypeNameByBundleIdentifier: %@, properties: [%@], availabilityAnnotations: %@, requiredCapabilities: %@, systemProtocolMetadata: %@, attributionBundleIdentifier: %@, assistantDefinedSchemas: %@, fullyQualifiedTypeName: %@, visibility: %@, query: %@>"
+ "<%@: %p, type: %@, conditions: %@>"
+ "@120@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112"
+ "@132@0:8@16@24@32@40@48@56@64@72@80Q88@96@104B112@116@124"
+ "@156@0:8@16B24@28@36@44@52@60@68@76@84@92@100@108@116@124@132@140@148"
+ "@244@0:8@16@24@32@40q48@56@64@72B80Q84@92@100Q108@116@124@132@140@148@156@164@172@180@188@196@204@212@220@228@236"
+ "BundleIdentifier"
+ "Foreground"
+ "LNTargetMetadata"
+ "LNTargetMetadataCondition"
+ "Main"
+ "T@\"LNTargetMetadata\",R,N"
+ "T@\"LNTargetMetadataCondition\",R,N"
+ "T@\"NSArray\",R,C,N,V_allowedTargets"
+ "T@\"NSArray\",R,N,V_conditions"
+ "T@\"NSString\",R,N,V_bundleIdentifier"
+ "Tq,R,N,V_identifier"
+ "_allowedTargets"
+ "_conditions"
+ "allowedTargets"
+ "com.apple.private.appintents.enabled"
+ "conditions"
+ "dataUsingEncoding:"
+ "defaultTarget"
+ "foregroundCondition"
+ "hasPrefix:"
+ "initWithBundleIdentifier:conditions:"
+ "initWithData:encoding:"
+ "initWithIdentifier:inputValueType:resultValueType:mangledTypeName:mangledTypeNameByBundleIdentifier:effectiveBundleIdentifiers:parameters:sortingOptions:availabilityAnnotations:capabilities:descriptionMetadata:visibilityMetadata:defaultQueryForEntity:fullyQualifiedIdentifier:allowedTargets:"
+ "initWithIdentifier:mangledTypeName:mangledTypeNameByBundleIdentifier:effectiveBundleIdentifiers:bundleMetadataVersion:title:descriptionMetadata:deprecationMetadata:openAppWhenRun:supportedModes:explicitAuthenticationPolicy:outputType:outputFlags:parameters:systemProtocolMetadata:actionConfiguration:typeSpecificMetadata:customIntentClassName:availabilityAnnotations:shortcutsMetadata:requiredCapabilities:attributionBundleIdentifier:sideEffect:assistantDefinedSchemas:assistantDefinedSchemaTraits:visibilityMetadata:fullyQualifiedTypeName:constraints:allowedTargets:"
+ "initWithIdentifier:mangledTypeName:mangledTypeNameByBundleIdentifier:effectiveBundleIdentifiers:displayRepresentation:cases:customIntentEnumTypeName:availabilityAnnotations:system:fullyQualifiedTypeName:assistantDefinedSchemas:visibilityMetadata:allowedTargets:"
+ "initWithIdentifier:transient:mangledTypeName:mangledTypeNameByBundleIdentifier:effectiveBundleIdentifiers:displayRepresentation:properties:customIntentTypeClassName:availabilityAnnotations:requiredCapabilities:systemProtocolMetadata:attributionBundleIdentifier:transferableContentTypes:assistantDefinedSchemas:fullyQualifiedTypeName:visibilityMetadata:defaultQueryIdentifier:allowedTargets:"
+ "initWithType:bundleIdentifier:conditions:"
+ "initWithTypeIdentifier:bundleIdentifier:instanceIdentifier:"
+ "mainTarget"
+ "{"
- "\f"
- "<%@: %p, displayRepresentation: %@, mangledTypeNameByBundleIdentifier: %@, availabilityAnnotations: %@, fullyQualifiedTypeName: %@, assistantDefinedSchemas: %@, visibility: %@>"
- "<%@: %p, identifier: %@, effectiveBundleIdentifiers: [%@], bundleMetadataVersion: %@, title: %@, description: %@, deprecation: %@,parameters: [%@], openAppWhenRun: %@, supportedModes: %@, visibility: %@, explicitAuthenticationPolicy: %@, outputType: %@, systemProtocolMetadata: [%@], actionConfiguration: %@, typeSpecificMetadata: %@, customIntentClassName: %@, mangledTypeNameByBundleIdentifier: %@, availabilityAnnotations: %@, shortcutsMetadata: %@, requiredCapabilities: %@, attributionBundleIdentifier: %@, sideEffect: %@, assistantDefinedSchemas: %@, assistantDefinedSchemaTraits: %@, fullyQualifiedTypeName: %@>"
- "<%@: %p, identifier: %@, inputValueType: %@, resultValueType: %@, mangledTypeNameByBundleIdentifier: %@, parameters: [%@], sortingOptions: [%@], availabilityAnnotations: %@, descriptionMetadata: %@, visibility: %@, defaultEntityQuery: %@>"
- "<%@: %p, identifier: %@, transient: %@, displayRepresentation: %@, mangledTypeNameByBundleIdentifier: %@, properties: [%@], availabilityAnnotations: %@, requiredCapabilities: %@, systemProtocolMetadata: %@, attributionBundleIdentifier: %@, assistantDefinedSchemas: %@, fullyQualifiedTypeName: %@, visibility: %@, query: %@>"
- "Localizable-LUCKIERC_FEATURES"

```
