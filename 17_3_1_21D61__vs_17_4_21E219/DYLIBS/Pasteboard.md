## Pasteboard

> `/System/Library/PrivateFrameworks/Pasteboard.framework/Pasteboard`

```diff

-7202.0.0.0.0
-  __TEXT.__text: 0x24084
+7433.0.0.0.0
+  __TEXT.__text: 0x253c8
   __TEXT.__auth_stubs: 0x760
-  __TEXT.__objc_methlist: 0x1d60
+  __TEXT.__objc_methlist: 0x1e80
   __TEXT.__const: 0x80
-  __TEXT.__cstring: 0x1a0a
-  __TEXT.__gcc_except_tab: 0x6dc
+  __TEXT.__cstring: 0x1af9
+  __TEXT.__gcc_except_tab: 0x6e0
   __TEXT.__oslogstring: 0xc5b
   __TEXT.__ustring: 0xb0
-  __TEXT.__unwind_info: 0xd40
-  __TEXT.__objc_classname: 0x397
-  __TEXT.__objc_methname: 0x60f8
-  __TEXT.__objc_methtype: 0xdce
-  __TEXT.__objc_stubs: 0x34e0
+  __TEXT.__unwind_info: 0xd94
+  __TEXT.__objc_classname: 0x3c2
+  __TEXT.__objc_methname: 0x66a0
+  __TEXT.__objc_methtype: 0xe16
+  __TEXT.__objc_stubs: 0x36e0
   __DATA_CONST.__got: 0xa8
-  __DATA_CONST.__const: 0x1308
-  __DATA_CONST.__objc_classlist: 0xc8
+  __DATA_CONST.__const: 0x1420
+  __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x3978
-  __DATA_CONST.__objc_selrefs: 0x1370
+  __DATA_CONST.__objc_const: 0x3ac0
+  __DATA_CONST.__objc_selrefs: 0x1438
+  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__objc_classrefs: 0x1c8
+  __DATA_CONST.__objc_superrefs: 0xb8
   __DATA_CONST.__objc_arraydata: 0x40
-  __AUTH_CONST.__cfstring: 0x10e0
-  __AUTH_CONST.__objc_const: 0xc10
+  __AUTH_CONST.__cfstring: 0x1100
+  __AUTH_CONST.__objc_const: 0xc58
   __AUTH_CONST.__const: 0x480
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__auth_got: 0x3c0
   __AUTH.__data: 0x18
-  __DATA.__objc_protorefs: 0x18
-  __DATA.__objc_classrefs: 0x1c0
-  __DATA.__objc_superrefs: 0xb0
-  __DATA.__objc_ivar: 0x198
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0x1ac
   __DATA.__data: 0x420
   __DATA.__bss: 0x8
   __DATA_DIRTY.__objc_ivar: 0x38

   - /System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7D89C83F-0AC8-3226-9542-5B8EEADAEFBF
-  Functions: 994
-  Symbols:   3227
-  CStrings:  1495
+  UUID: 5927C151-5327-36CD-AF00-F8F55C48EB67
+  Functions: 1028
+  Symbols:   3329
+  CStrings:  1543
 
Symbols:
+ -[PBCoercionRegistry _member_registerCoercionFromRepresentationConformingToType:toRepresentationOfType:coercionBlock:]
+ -[PBCoercionRegistry loadCoercionOfRepresentation:fromType:toType:usingCoercion:completionBlock:]
+ -[PBCoercionRegistry member_representationCoercions]
+ -[PBCoercionRegistry registerCoercionFromRepresentationConformingToType:toRepresentationOfType:coercionBlock:]
+ -[PBCoercionRegistry setMember_representationCoercions:]
+ -[PBCoercionRegistry(Private) _member_enumerateAvailableCoercionLoaderBlocksForRepresentation:usingBlock:]
+ -[PBCoercionRegistry(Private) enumerateAvailableCoercionLoaderBlocksForRepresentation:usingBlock:]
+ -[PBItem _canInstantiateObjectOfClass:excludingCoercionsFromTypes:]
+ -[PBItem itemQueue_canInstantiateObjectOfClass:excludingCoercionsFromTypes:]
+ -[PBItem itemQueue_registerLocalAvailableDerivedRepresentations]
+ -[PBItem uikit_canInstantiateObjectOfClass:excludingCoercionsFromTypes:]
+ -[PBItemCollection registerLocalAvailableDerivedRepresentations]
+ -[PBItemRepresentation isDerivedRepresentation]
+ -[PBItemRepresentation setDerivedRepresentation:]
+ -[PBRepresentationToRepresentationCoercion .cxx_destruct]
+ -[PBRepresentationToRepresentationCoercion canCoerceToRepresentationOfType:]
+ -[PBRepresentationToRepresentationCoercion coerceRepresentationData:representationURL:toRepresentationOfType:completionBlock:]
+ -[PBRepresentationToRepresentationCoercion coercionBlock]
+ -[PBRepresentationToRepresentationCoercion destinationType]
+ -[PBRepresentationToRepresentationCoercion initWithSourceType:destinationType:conversionBlock:]
+ -[PBRepresentationToRepresentationCoercion setCoercionBlock:]
+ -[PBRepresentationToRepresentationCoercion setDestinationType:]
+ -[PBRepresentationToRepresentationCoercion setSourceType:]
+ -[PBRepresentationToRepresentationCoercion sourceType]
+ GCC_except_table101
+ GCC_except_table104
+ GCC_except_table108
+ GCC_except_table115
+ GCC_except_table119
+ GCC_except_table149
+ GCC_except_table37
+ GCC_except_table39
+ GCC_except_table73
+ GCC_except_table99
+ _OBJC_CLASS_$_PBRepresentationToRepresentationCoercion
+ _OBJC_IVAR_$_PBCoercionRegistry._member_representationCoercions
+ _OBJC_IVAR_$_PBItemRepresentation._derivedRepresentation
+ _OBJC_IVAR_$_PBRepresentationToRepresentationCoercion._coercionBlock
+ _OBJC_IVAR_$_PBRepresentationToRepresentationCoercion._destinationType
+ _OBJC_IVAR_$_PBRepresentationToRepresentationCoercion._sourceType
+ _OBJC_METACLASS_$_PBRepresentationToRepresentationCoercion
+ _PBCannotCoerceRepresentationOfTypeToRepresentationOfTypeError
+ __OBJC_$_INSTANCE_METHODS_PBRepresentationToRepresentationCoercion
+ __OBJC_$_INSTANCE_VARIABLES_PBRepresentationToRepresentationCoercion
+ __OBJC_$_PROP_LIST_PBRepresentationToRepresentationCoercion
+ __OBJC_CLASS_RO_$_PBRepresentationToRepresentationCoercion
+ __OBJC_METACLASS_RO_$_PBRepresentationToRepresentationCoercion
+ ___106-[PBCoercionRegistry(Private) _member_enumerateAvailableCoercionLoaderBlocksForRepresentation:usingBlock:]_block_invoke
+ ___110-[PBCoercionRegistry registerCoercionFromRepresentationConformingToType:toRepresentationOfType:coercionBlock:]_block_invoke
+ ___118-[PBCoercionRegistry _member_registerCoercionFromRepresentationConformingToType:toRepresentationOfType:coercionBlock:]_block_invoke
+ ___126-[PBRepresentationToRepresentationCoercion coerceRepresentationData:representationURL:toRepresentationOfType:completionBlock:]_block_invoke
+ ___53-[PBItem _loadObjectOfClass:context:completionBlock:]_block_invoke.53
+ ___64-[PBItem itemQueue_registerLocalAvailableDerivedRepresentations]_block_invoke
+ ___64-[PBItem itemQueue_registerLocalAvailableDerivedRepresentations]_block_invoke_2
+ ___64-[PBItem itemQueue_registerLocalAvailableDerivedRepresentations]_block_invoke_3
+ ___64-[PBItemCollection registerLocalAvailableDerivedRepresentations]_block_invoke
+ ___67-[PBItem _canInstantiateObjectOfClass:excludingCoercionsFromTypes:]_block_invoke
+ ___72-[PBCoercionRegistry loadRepresentationOfObject:asType:completionBlock:]_block_invoke.49
+ ___72-[PBCoercionRegistry loadRepresentationOfObject:asType:completionBlock:]_block_invoke_2.50
+ ___97-[PBCoercionRegistry loadCoercionOfRepresentation:fromType:toType:usingCoercion:completionBlock:]_block_invoke
+ ___98-[PBCoercionRegistry(Private) enumerateAvailableCoercionLoaderBlocksForRepresentation:usingBlock:]_block_invoke
+ ___Block_byref_object_copy_.47
+ ___Block_byref_object_dispose_.48
+ ___block_descriptor_48_e8_32s40s_e57_B32?0"PBRepresentationToRepresentationCoercion"8Q16^B24ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e65_v24?0"NSString"8?<"NSProgress"??<v?"NSData""NSError">>16ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e28_v24?0"NSData"8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48bs_e68_v40?0"NSData"8"PBSecurityScopedURLWrapper"16"NSError"24?<v?>32ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48r_e5_v8?0lr48l8s32l8u56l8s40l8
+ ___block_descriptor_72_e8_32s40s48s56s64s_e45_"NSProgress"16?0?<v?"NSData""NSError">8ls32l8s40l8s48l8s56l8s64l8
+ _objc_msgSend$_canInstantiateObjectOfClass:excludingCoercionsFromTypes:
+ _objc_msgSend$_member_enumerateAvailableCoercionLoaderBlocksForRepresentation:usingBlock:
+ _objc_msgSend$_member_registerCoercionFromRepresentationConformingToType:toRepresentationOfType:coercionBlock:
+ _objc_msgSend$coerceRepresentationData:representationURL:toRepresentationOfType:completionBlock:
+ _objc_msgSend$coercionBlock
+ _objc_msgSend$destinationType
+ _objc_msgSend$enumerateAvailableCoercionLoaderBlocksForRepresentation:usingBlock:
+ _objc_msgSend$indexOfObjectPassingTest:
+ _objc_msgSend$initWithSourceType:destinationType:conversionBlock:
+ _objc_msgSend$itemQueue_canInstantiateObjectOfClass:excludingCoercionsFromTypes:
+ _objc_msgSend$itemQueue_registerLocalAvailableDerivedRepresentations
+ _objc_msgSend$loadCoercionOfRepresentation:fromType:toType:usingCoercion:completionBlock:
+ _objc_msgSend$member_representationCoercions
+ _objc_msgSend$registerLocalAvailableDerivedRepresentations
+ _objc_msgSend$replaceObjectAtIndex:withObject:
+ _objc_msgSend$setDerivedRepresentation:
+ _objc_msgSend$setWithArray:
+ _objc_msgSend$sourceType
- -[PBItem itemQueue_canInstantiateObjectOfClass:]
- GCC_except_table103
- GCC_except_table109
- GCC_except_table113
- GCC_except_table137
- GCC_except_table25
- GCC_except_table31
- GCC_except_table40
- GCC_except_table61
- GCC_except_table91
- GCC_except_table93
- ___39-[PBItem _canInstantiateObjectOfClass:]_block_invoke
- ___53-[PBItem _loadObjectOfClass:context:completionBlock:]_block_invoke.51
- ___72-[PBCoercionRegistry loadRepresentationOfObject:asType:completionBlock:]_block_invoke.46
- ___72-[PBCoercionRegistry loadRepresentationOfObject:asType:completionBlock:]_block_invoke_2.47
- ___Block_byref_object_copy_.44
- ___Block_byref_object_dispose_.45
- _objc_msgSend$isBackedByFileProvider
- _objc_msgSend$itemQueue_canInstantiateObjectOfClass:
CStrings:
+ "\x05"
+ "@\"NSProgress\"16@?0@?<v@?@\"NSData\"@\"NSError\">8"
+ "@40@0:8@16@24@?32"
+ "@56@0:8@16@24@32@40@?48"
+ "@?16@0:8"
+ "B32@?0@\"PBRepresentationToRepresentationCoercion\"8Q16^B24"
+ "Cannot coerce representation of type %@ to representation of type %@"
+ "PBRepresentationToRepresentationCoercion"
+ "T@\"NSMutableArray\",&,N,V_member_representationCoercions"
+ "T@\"NSString\",&,N,V_destinationType"
+ "T@\"NSString\",&,N,V_sourceType"
+ "T@\"NSString\",?,R,C"
+ "T@?,C,N,V_coercionBlock"
+ "TB,N,GisDerivedRepresentation,V_derivedRepresentation"
+ "_canInstantiateObjectOfClass:excludingCoercionsFromTypes:"
+ "_coercionBlock"
+ "_derivedRepresentation"
+ "_destinationType"
+ "_member_enumerateAvailableCoercionLoaderBlocksForRepresentation:usingBlock:"
+ "_member_registerCoercionFromRepresentationConformingToType:toRepresentationOfType:coercionBlock:"
+ "_member_representationCoercions"
+ "_sourceType"
+ "canCoerceToRepresentationOfType:"
+ "coerceRepresentationData:representationURL:toRepresentationOfType:completionBlock:"
+ "coercionBlock"
+ "derivedRepresentation"
+ "destinationType"
+ "enumerateAvailableCoercionLoaderBlocksForRepresentation:usingBlock:"
+ "indexOfObjectPassingTest:"
+ "initWithSourceType:destinationType:conversionBlock:"
+ "isDerivedRepresentation"
+ "itemQueue_canInstantiateObjectOfClass:excludingCoercionsFromTypes:"
+ "itemQueue_registerLocalAvailableDerivedRepresentations"
+ "loadCoercionOfRepresentation:fromType:toType:usingCoercion:completionBlock:"
+ "member_representationCoercions"
+ "registerCoercionFromRepresentationConformingToType:toRepresentationOfType:coercionBlock:"
+ "registerLocalAvailableDerivedRepresentations"
+ "replaceObjectAtIndex:withObject:"
+ "setCoercionBlock:"
+ "setDerivedRepresentation:"
+ "setDestinationType:"
+ "setMember_representationCoercions:"
+ "setSourceType:"
+ "setWithArray:"
+ "sourceType"
+ "uikit_canInstantiateObjectOfClass:excludingCoercionsFromTypes:"
+ "v24@?0@\"NSString\"8@?<@\"NSProgress\"@?@?<v@?@\"NSData\"@\"NSError\">>16"
+ "v48@0:8@16@24@32@?40"
- "itemQueue_canInstantiateObjectOfClass:"

```
