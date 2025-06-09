## BaseBoard

> `/System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard`

```diff

-694.5.5.0.0
-  __TEXT.__text: 0x994d8
-  __TEXT.__auth_stubs: 0x2030
-  __TEXT.__objc_methlist: 0x6c0c
-  __TEXT.__const: 0x2f8
+731.0.0.0.0
+  __TEXT.__text: 0xa2564
+  __TEXT.__auth_stubs: 0x2100
+  __TEXT.__objc_methlist: 0x6e5c
+  __TEXT.__const: 0x308
   __TEXT.__dlopen_cstrs: 0xe8
-  __TEXT.__gcc_except_tab: 0x109c8
-  __TEXT.__cstring: 0x7f9d
-  __TEXT.__oslogstring: 0x300b
+  __TEXT.__gcc_except_tab: 0x118a0
+  __TEXT.__cstring: 0x8d09
+  __TEXT.__oslogstring: 0x3053
   __TEXT.__ustring: 0x20
-  __TEXT.__unwind_info: 0x4f58
-  __TEXT.__objc_classname: 0xf61
-  __TEXT.__objc_methname: 0xb1b9
-  __TEXT.__objc_methtype: 0x2143
-  __TEXT.__objc_stubs: 0x6ea0
-  __DATA_CONST.__got: 0x830
-  __DATA_CONST.__const: 0x1bf8
-  __DATA_CONST.__objc_classlist: 0x418
+  __TEXT.__unwind_info: 0x5028
+  __TEXT.__objc_classname: 0xffd
+  __TEXT.__objc_methname: 0xb618
+  __TEXT.__objc_methtype: 0x22a5
+  __TEXT.__objc_stubs: 0x72c0
+  __DATA_CONST.__got: 0x848
+  __DATA_CONST.__const: 0x1ca8
+  __DATA_CONST.__objc_classlist: 0x430
   __DATA_CONST.__objc_catlist: 0xc0
-  __DATA_CONST.__objc_protolist: 0x140
+  __DATA_CONST.__objc_protolist: 0x168
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3060
-  __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x2d0
+  __DATA_CONST.__objc_selrefs: 0x3180
+  __DATA_CONST.__objc_protorefs: 0x28
+  __DATA_CONST.__objc_superrefs: 0x2d8
   __DATA_CONST.__objc_arraydata: 0x40
-  __AUTH_CONST.__auth_got: 0x1028
-  __AUTH_CONST.__const: 0xac0
-  __AUTH_CONST.__cfstring: 0x81a0
-  __AUTH_CONST.__objc_const: 0xcd60
+  __AUTH_CONST.__auth_got: 0x1090
+  __AUTH_CONST.__const: 0xbe0
+  __AUTH_CONST.__cfstring: 0x8bc0
+  __AUTH_CONST.__objc_const: 0xd140
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0x1310
-  __DATA.__objc_ivar: 0x7ec
-  __DATA.__data: 0xf20
-  __DATA.__crash_info: 0x40
+  __DATA.__objc_ivar: 0x810
+  __DATA.__data: 0x1108
+  __DATA.__crash_info: 0x148
   __DATA.__common: 0x40
-  __DATA.__bss: 0x48
+  __DATA.__bss: 0x50
   __DATA_DIRTY.__objc_ivar: 0x38
-  __DATA_DIRTY.__objc_data: 0x15e0
+  __DATA_DIRTY.__objc_data: 0x16d0
   __DATA_DIRTY.__data: 0x88
-  __DATA_DIRTY.__bss: 0x480
+  __DATA_DIRTY.__bss: 0x4b4
   __DATA_DIRTY.__common: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 370138F2-A6C4-3A87-8F0D-CF39877CF578
-  Functions: 2925
-  Symbols:   10562
-  CStrings:  5294
+  UUID: 7974D33C-78DF-38F8-BD30-D3956F03BD5A
+  Functions: 2981
+  Symbols:   10779
+  CStrings:  5533
 
Symbols:
+ +[BSActionResponse initialize]
+ +[BSAuditToken initialize]
+ +[BSCanonicalOrientationMapResolver initialize]
+ +[BSColor initialize]
+ +[BSCornerRadiusConfiguration initialize]
+ +[BSDescriptionBuilder builderWithClass:]
+ +[BSObjCIvar ivarWithName:ivar:containedClasses:alternateNames:]
+ +[BSProcessHandle initialize]
+ +[BSXPCAutoCoder supportsSecureCoding]
+ +[BSXPCCoder testEncodeAndDecodeObject:ofClass:]
+ +[NSObject(BSXPCAutoCoding) supportedCodings]
+ -[BSActionResponse awakeFromCoder]
+ -[BSActionResponse membersForCoder]
+ -[BSAnimationSettings _initWithStoredDuration:storedDurationIsDirty:delay:frameInterval:frameRange:highFrameRateReason:timingFunction:speed:beginTime:mass:stiffness:damping:epsilon:initialVelocity:isSpring:]
+ -[BSAnimationSettings beginTime]
+ -[BSAuditToken awakeFromCoder]
+ -[BSAuditToken membersForCoder]
+ -[BSCanonicalOrientationMapResolver membersForCoder]
+ -[BSColor membersForCoder]
+ -[BSCornerRadiusConfiguration membersForCoder]
+ -[BSDescriptionBuilder init]
+ -[BSKeyedSettings _applyToSettings:preserveDiffs:]
+ -[BSKeyedSettingsDiff copyApplyingDiff:]
+ -[BSMutableAnimationSettings setBeginTime:]
+ -[BSMutableSpringAnimationSettings setBeginTime:]
+ -[BSObjCIvar .cxx_destruct]
+ -[BSObjCIvar description]
+ -[BSObjCIvar hash]
+ -[BSObjCIvar isEqual:]
+ -[BSProcessHandle membersForCoder]
+ -[BSSettings _applyToSettings:preserveDiffs:]
+ -[BSSettingsDiff copyApplyingDiff:]
+ -[BSSimpleAssertion _appendDescriptionToFormatter:]
+ -[BSSimpleAssertion _initWithReason:identifier:queue:type:block:]
+ -[BSSimpleAssertion _initWithReason:identifier:requiredInvalidationQueue:deallocPolicy:invalidatedWithContextBlock:]
+ -[BSSimpleAssertion appendDescriptionToStream:]
+ -[BSSimpleAssertion assertion]
+ -[BSSimpleAssertion initWithReason:identifier:requiredInvalidationQueue:deallocPolicy:invalidatedWithContextBlock:]
+ -[BSSimpleAssertion initWithReason:invalidatedBlock:]
+ -[BSSimpleAssertion initWithReason:invalidatedWithContextBlock:]
+ -[BSSimpleAssertion init]
+ -[BSSimpleAssertion wasExplicit]
+ -[BSXPCAutoCoder encodeWithCoder:]
+ -[BSXPCAutoCoder initWithCoder:]
+ -[BSXPCAutoCodingOptions addSupportedCoding:]
+ -[BSXPCAutoCodingOptions dealloc]
+ -[BSXPCAutoCodingOptions init]
+ -[BSXPCAutoCodingOptions setSupportedCodings:]
+ -[BSXPCAutoCodingOptions supportedCodings]
+ -[BSXPCCoder decodeStruct:withObjCType:forKey:]
+ -[BSXPCCoder decodeValueWithObjCType:forKey:]
+ -[BSXPCCoder encodeStruct:withObjCType:forKey:]
+ -[BSXPCCodingArray copyWithZone:]
+ -[BSXPCCodingArray description]
+ -[BSXPCCodingArray hash]
+ -[BSXPCCodingArray isEqual:]
+ -[NSCoder(BSXPCCoder) decodeCGPointForKey:]
+ -[NSCoder(BSXPCCoder) decodeCGRectForKey:]
+ -[NSCoder(BSXPCCoder) decodeCGSizeForKey:]
+ -[NSCoder(BSXPCCoder) decodeCollectionOfClass:containingClass:forKey:]
+ -[NSCoder(BSXPCCoder) decodeDictionaryOfClass:forKey:]
+ -[NSCoder(BSXPCCoder) decodeStringForKey:]
+ -[NSCoder(BSXPCCoder) decodeStruct:withObjCType:forKey:]
+ -[NSCoder(BSXPCCoder) decodeUInt64ForKey:]
+ -[NSCoder(BSXPCCoder) decodeValueWithObjCType:forKey:]
+ -[NSCoder(BSXPCCoder) encodeCGPoint:forKey:]
+ -[NSCoder(BSXPCCoder) encodeCGRect:forKey:]
+ -[NSCoder(BSXPCCoder) encodeCGSize:forKey:]
+ -[NSCoder(BSXPCCoder) encodeCollection:forKey:]
+ -[NSCoder(BSXPCCoder) encodeDictionary:forKey:]
+ -[NSCoder(BSXPCCoder) encodeStruct:withObjCType:forKey:]
+ -[NSCoder(BSXPCCoder) encodeUInt64:forKey:]
+ -[NSObject(BSCoding) bs_isPlist]
+ GCC_except_table182
+ _BSKernelAuditToken
+ _BSObjCClassGetMetaClass
+ _BSObjCClassImplementsSelector
+ _BSTestSerializeAndDeserializeBSXPCEncodableObject
+ _BSXPCAutoCodingGetIvars
+ _BSXPCAutoCodingInitialize
+ _BSXPCAutoCodingVerify
+ _BSXPCAutoCodingsDefault
+ _BSXPCLegacyCoding
+ _BSXPCSecureCoding
+ _NSHashInsertKnownAbsent
+ _NSInvalidArchiveOperationException
+ _NSSecureArchiving
+ _NSXPCSecureCoding
+ _OBJC_CLASS_$_BSObjCIvar
+ _OBJC_CLASS_$_BSXPCAutoCoder
+ _OBJC_CLASS_$_BSXPCAutoCodingOptions
+ _OBJC_IVAR_$_BSAnimationSettings._lock_beginTime
+ _OBJC_IVAR_$_BSObjCIvar._alternateNames
+ _OBJC_IVAR_$_BSObjCIvar._ivar
+ _OBJC_IVAR_$_BSObjCIvar._name
+ _OBJC_IVAR_$_BSObjCIvar._offset
+ _OBJC_IVAR_$_BSObjCIvar._value
+ _OBJC_IVAR_$_BSSimpleAssertion._invalidationType
+ _OBJC_IVAR_$_BSSimpleAssertion._wasExplicit
+ _OBJC_IVAR_$_BSXPCAutoCodingOptions._supportedCodings
+ _OBJC_METACLASS_$_BSObjCIvar
+ _OBJC_METACLASS_$_BSXPCAutoCoder
+ _OBJC_METACLASS_$_BSXPCAutoCodingOptions
+ __BSAutoMember
+ __BSXPCAutoCodingInitialize
+ __BSXPCDecodeIvarsForObject
+ __BSXPCEncodeIvarsForObject
+ __NSIsNSData
+ __NSIsNSDate
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSCoder_$_BSXPCCoder
+ __OBJC_$_CATEGORY_NSCoder_$_BSXPCCoder
+ __OBJC_$_CATEGORY_NSObject_$_BSXPCAutoCoding
+ __OBJC_$_CLASS_METHODS_BSCornerRadiusConfiguration
+ __OBJC_$_CLASS_METHODS_BSXPCAutoCoder
+ __OBJC_$_CLASS_METHODS_NSObject(BSXPCAutoCoding|BSXPCObjectUtilitiesIndirect|BSCoding|BSXPCSecureCoding)
+ __OBJC_$_INSTANCE_METHODS_BSObjCIvar
+ __OBJC_$_INSTANCE_METHODS_BSXPCAutoCoder
+ __OBJC_$_INSTANCE_METHODS_BSXPCAutoCodingOptions
+ __OBJC_$_INSTANCE_METHODS_NSObject(BSXPCAutoCoding|BSXPCObjectUtilitiesIndirect|BSCoding|BSXPCSecureCoding)
+ __OBJC_$_INSTANCE_VARIABLES_BSObjCIvar
+ __OBJC_$_INSTANCE_VARIABLES_BSXPCAutoCodingOptions
+ __OBJC_$_PROP_LIST_BSSimpleAssertionInvalidationContext
+ __OBJC_$_PROP_LIST_BSXPCAutoCodingOptions
+ __OBJC_$_PROP_LIST_NSCoder_$_BSXPCCoder
+ __OBJC_$_PROTOCOL_CLASS_METHODS_OPT_BSXPCAutoCoding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BSDescriptionStreaming
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BSSimpleAssertionInvalidationContext
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BSXPCAutoCoding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BSXPCAutoCodingConfiguring
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_BSXPCAutoCoding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BSDescriptionStreaming
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BSSimpleAssertionInvalidationContext
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BSXPCAutoCoding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BSXPCAutoCodingConfiguring
+ __OBJC_$_PROTOCOL_REFS_BSDescriptionStreaming
+ __OBJC_$_PROTOCOL_REFS_BSXPCAutoCoding
+ __OBJC_CATEGORY_PROTOCOLS_$_NSCoder_$_BSXPCCoder
+ __OBJC_CLASS_PROTOCOLS_$_BSXPCAutoCodingOptions
+ __OBJC_CLASS_RO_$_BSObjCIvar
+ __OBJC_CLASS_RO_$_BSXPCAutoCoder
+ __OBJC_CLASS_RO_$_BSXPCAutoCodingOptions
+ __OBJC_LABEL_PROTOCOL_$_BSDescriptionStreaming
+ __OBJC_LABEL_PROTOCOL_$_BSSimpleAssertionInvalidationContext
+ __OBJC_LABEL_PROTOCOL_$_BSXPCAutoCoding
+ __OBJC_LABEL_PROTOCOL_$_BSXPCAutoCodingConfiguring
+ __OBJC_LABEL_PROTOCOL_$_NSXPCSecureCoding
+ __OBJC_METACLASS_RO_$_BSObjCIvar
+ __OBJC_METACLASS_RO_$_BSXPCAutoCoder
+ __OBJC_METACLASS_RO_$_BSXPCAutoCodingOptions
+ __OBJC_PROTOCOL_$_BSDescriptionStreaming
+ __OBJC_PROTOCOL_$_BSSimpleAssertionInvalidationContext
+ __OBJC_PROTOCOL_$_BSXPCAutoCoding
+ __OBJC_PROTOCOL_$_BSXPCAutoCodingConfiguring
+ __OBJC_PROTOCOL_$_NSXPCSecureCoding
+ __OBJC_PROTOCOL_REFERENCE_$_BSXPCCoding
+ __OBJC_PROTOCOL_REFERENCE_$_BSXPCSecureCoding
+ __OBJC_PROTOCOL_REFERENCE_$_NSXPCSecureCoding
+ ___21+[BSColor initialize]_block_invoke
+ ___25-[BSSimpleAssertion init]_block_invoke
+ ___26+[BSAuditToken initialize]_block_invoke
+ ___29+[BSProcessHandle initialize]_block_invoke
+ ___30+[BSActionResponse initialize]_block_invoke
+ ___41+[BSCornerRadiusConfiguration initialize]_block_invoke
+ ___45-[BSSettings _applyToSettings:preserveDiffs:]_block_invoke
+ ___45-[BSSettings _applyToSettings:preserveDiffs:]_block_invoke_2
+ ___47+[BSCanonicalOrientationMapResolver initialize]_block_invoke
+ ___47-[BSSimpleAssertion appendDescriptionToStream:]_block_invoke
+ ___BSXPCAutoCodingsDefault_block_invoke
+ ___OriginalIMP
+ ____BSXPCAutoCodingInitialize_block_invoke
+ ____BSXPCDecodeObject_block_invoke.311
+ ____BSXPCEncodeIvarsForObject_block_invoke
+ ____BSXPCEncodeIvarsForObject_block_invoke_2
+ ___block_descriptor_32_e38_v16?0"<BSXPCAutoCodingConfiguring>"8l
+ ___block_descriptor_32_e48_v16?0"<BSSimpleAssertionInvalidationContext>"8l
+ ___block_descriptor_40_ea8_32bs_e33_v16?0"NSObject<OS_xpc_object>"8ls32l8
+ ___block_descriptor_40_ea8_32s_e37_B24?0r*8"NSObject<OS_xpc_object>"16ls32l8
+ ___block_descriptor_41_ea8_32s_e15_v32?0Q816^B24ls32l8
+ ___block_descriptor_57_ea8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_literal_global.137
+ ___block_literal_global.175
+ ___block_literal_global.210
+ ___block_literal_global.26
+ ___block_literal_global.29
+ ___block_literal_global.31
+ ___getkCAAnimationNonZeroSymbolLoc_block_invoke
+ __objc_msgForward
+ _bs_cleanup_cftype
+ _bs_cleanup_malloc
+ _class_addProtocol
+ _class_copyIvarList
+ _class_getMethodImplementation
+ _class_replaceMethod
+ _getkCAAnimationNonZeroSymbolLoc.ptr
+ _memcmp
+ _objc_msgSend$_applyToSettings:preserveDiffs:
+ _objc_msgSend$_setError
+ _objc_msgSend$_testEncodeAndDecodeObject:ofClass:
+ _objc_msgSend$addSupportedCoding:
+ _objc_msgSend$arrayByAddingObject:
+ _objc_msgSend$awakeAfterUsingCoder:
+ _objc_msgSend$bs_array
+ _objc_msgSend$bs_isPlist
+ _objc_msgSend$bs_set
+ _objc_msgSend$copyApplyingDiff:
+ _objc_msgSend$data
+ _objc_msgSend$decodeBoolForKey:
+ _objc_msgSend$decodeDictionaryOfClass:forKey:
+ _objc_msgSend$decodeStruct:withObjCType:forKey:
+ _objc_msgSend$decodeValueWithObjCType:forKey:
+ _objc_msgSend$encodeBool:forKey:
+ _objc_msgSend$encodeStruct:withObjCType:forKey:
+ _objc_msgSend$getBytes:range:
+ _objc_msgSend$getValue:size:
+ _objc_msgSend$hasError
+ _objc_msgSend$objectClass
+ _objc_msgSend$objectContainedClasses
+ _objc_msgSend$pointerValue
+ _objc_msgSend$punctuationCharacterSet
+ _objc_msgSend$replacementObjectForCoder:
+ _objc_msgSend$setBeginTime:
+ _objc_msgSend$setBeginTimeMode:
+ _objc_msgSend$setPosition:
+ _objc_msgSend$setSupportedCodings:
+ _objc_msgSend$size
+ _objc_msgSend$string
+ _objc_msgSend$supportedCodings
+ _objc_msgSend$valueWithPointer:
+ _object_getIvar
+ _object_setIvarWithStrongDefault
+ _strcmp
+ _xpc_dictionary_get_dictionary
- +[BSActionResponse supportsBSXPCSecureCoding]
- +[BSAuditToken supportsBSXPCSecureCoding]
- +[BSAuditToken supportsSecureCoding]
- +[BSCanonicalOrientationMapResolver supportsBSXPCSecureCoding]
- +[BSColor supportsBSXPCSecureCoding]
- +[BSColor supportsSecureCoding]
- +[BSProcessHandle supportsSecureCoding]
- -[BSActionResponse _initWithInfo:error:]
- -[BSActionResponse encodeWithBSXPCCoder:]
- -[BSActionResponse encodeWithXPCDictionary:]
- -[BSActionResponse initWithBSXPCCoder:]
- -[BSActionResponse initWithXPCDictionary:]
- -[BSAnimationSettings _initWithStoredDuration:storedDurationIsDirty:delay:frameInterval:frameRange:highFrameRateReason:timingFunction:speed:mass:stiffness:damping:epsilon:initialVelocity:isSpring:]
- -[BSAuditToken _auditTokenAsData]
- -[BSAuditToken _initWithData:bundleID:]
- -[BSAuditToken encodeWithBSXPCCoder:]
- -[BSAuditToken encodeWithCoder:]
- -[BSAuditToken encodeWithXPCDictionary:]
- -[BSAuditToken initWithBSXPCCoder:]
- -[BSAuditToken initWithCoder:]
- -[BSAuditToken initWithXPCDictionary:]
- -[BSCanonicalOrientationMapResolver encodeWithBSXPCCoder:]
- -[BSCanonicalOrientationMapResolver initWithBSXPCCoder:]
- -[BSColor encodeWithBSXPCCoder:]
- -[BSColor encodeWithCoder:]
- -[BSColor encodeWithXPCDictionary:]
- -[BSColor initWithBSXPCCoder:]
- -[BSColor initWithCoder:]
- -[BSColor initWithXPCDictionary:]
- -[BSCornerRadiusConfiguration encodeWithXPCDictionary:]
- -[BSCornerRadiusConfiguration initWithXPCDictionary:]
- -[BSKeyedSettings _applyToSettings:]
- -[BSProcessHandle encodeWithCoder:]
- -[BSProcessHandle encodeWithXPCDictionary:]
- -[BSProcessHandle initWithCoder:]
- -[BSProcessHandle initWithXPCDictionary:]
- -[NSCoder(BSXPCCoderExtras) decodeCGPointForKey:]
- -[NSCoder(BSXPCCoderExtras) decodeCGRectForKey:]
- -[NSCoder(BSXPCCoderExtras) decodeCGSizeForKey:]
- -[NSCoder(BSXPCCoderExtras) decodeCollectionOfClass:containingClass:forKey:]
- -[NSCoder(BSXPCCoderExtras) decodeStringForKey:]
- -[NSCoder(BSXPCCoderExtras) decodeUInt64ForKey:]
- -[NSCoder(BSXPCCoderExtras) encodeCGPoint:forKey:]
- -[NSCoder(BSXPCCoderExtras) encodeCGRect:forKey:]
- -[NSCoder(BSXPCCoderExtras) encodeCGSize:forKey:]
- -[NSCoder(BSXPCCoderExtras) encodeCollection:forKey:]
- -[NSCoder(BSXPCCoderExtras) encodeUInt64:forKey:]
- OBJC_IVAR_$_PBDataReader._bytes
- OBJC_IVAR_$_PBDataReader._error
- OBJC_IVAR_$_PBDataReader._length
- OBJC_IVAR_$_PBDataReader._pos
- _BSInvalidAuditTokenFieldValue
- _BSXPCMessageEncodedObjectClassNameKey
- __OBJC_$_CATEGORY_INSTANCE_METHODS_NSCoder_$_BSXPCCoderExtras
- __OBJC_$_CATEGORY_NSCoder_$_BSXPCCoderExtras
- __OBJC_$_CATEGORY_NSObject_$_BSXPCObjectUtilitiesIndirect
- __OBJC_$_CLASS_METHODS_NSObject(BSXPCObjectUtilitiesIndirect|BSCoding|BSXPCSecureCoding)
- __OBJC_$_CLASS_PROP_LIST_BSAuditToken
- __OBJC_$_CLASS_PROP_LIST_BSColor
- __OBJC_$_CLASS_PROP_LIST_BSProcessHandle
- __OBJC_$_INSTANCE_METHODS_NSObject(BSXPCObjectUtilitiesIndirect|BSCoding|BSXPCSecureCoding)
- __OBJC_$_PROP_LIST_NSCoder_$_BSXPCCoderExtras
- __OBJC_CATEGORY_PROTOCOLS_$_NSCoder_$_BSXPCCoderExtras
- ___31-[BSSettings _applyToSettings:]_block_invoke
- ___31-[BSSettings _applyToSettings:]_block_invoke_2
- ____BSXPCDecodeObject_block_invoke.242
- ___block_descriptor_40_ea8_32s_e15_v32?0Q816^B24ls32l8
- ___block_literal_global.208
- ___block_literal_global.27
- ___block_literal_global.32
CStrings:
+ "\"%@\" is not the name of a real class"
+ "\"a\""
+ "\"b\""
+ "\"g\""
+ "\"r\""
+ "%@ does not support %@"
+ "%@ does not support encoding XPC objects (ivar: %@)"
+ "%@ encoded no ivars"
+ "%@ is not a supported coding"
+ "%@ is not a supported collection for ivar \"%@\""
+ "%@ provided no supported codings"
+ "%@ returned invalid array for member: %@"
+ "%@ returned invalid member: \"%@\""
+ "%@ returned invalid sub-member of \"%@\" that does is not a key name and does not map to a realized class: %@"
+ "%@ returned invalid sub-member of \"%@\": \"%@\""
+ "%@ returned multiple ivars with the same name"
+ "%@ returned multiple members named %@"
+ "%@ will auto-code: %@"
+ "(?=\"withArgs\"@?\"noArgs\"@?\"value\"@)"
+ "(ptr != ((void*)0)) && (size > 0)"
+ "-[BSXPCAutoCoder encodeWithCoder:]"
+ "<%@:%p duration=%f delay=%f interval=%f range={%f,%f,%f} reason=%i timing=%@ speed=%f beginTime=%f>"
+ "<%@:%p mass=%f stiffness=%f damping=%f epsilon=%f initialVelocity=%f %@delay=%f interval=%f range={%f,%f,%f} reason=%i timing=%@ speed=%f beginTime=%f>"
+ "<BSObjCIvar: %p; \"%@\" (%@)>"
+ "@\""
+ "@\"BSSimpleAssertion\"16@0:8"
+ "@\"NSValue\"32@0:8r*16@\"NSString\"24"
+ "@56@0:8@16@24@32q40@?48"
+ "@@:@"
+ "Already encoded an ivar named: %@"
+ "Auto-coding class \"%@\" still implements %@; migrate to -[<BSXPCAutoCoding> decodeWithCoder:]."
+ "Auto-coding class \"%@\" still implements %@; migrate to -[<BSXPCAutoCoding> encodeWithCoder:]."
+ "B40@0:8o^v16r*24@\"NSString\"32"
+ "B40@0:8o^v16r*24@32"
+ "B@:"
+ "BOOL _BSMemoryIsZeroed(uint8_t * _Nonnull, size_t)"
+ "BOOL _BSXPCAutoCodingInitialize(Class, BSXPCAutoCodingOptions *)"
+ "BSDescriptionStreaming"
+ "BSObjCIvar"
+ "BSSimpleAssertionInvalidationContext"
+ "BSXPCAutoCoder"
+ "BSXPCAutoCoding"
+ "BSXPCAutoCoding.m"
+ "BSXPCAutoCodingConfiguring"
+ "BSXPCAutoCodingOptions"
+ "Client code must invalidate <%@:%p> (%@) before dealloc"
+ "Collection ivar %@ must be declared with a contained class using the special BSXPC protocol-based generics syntax (eg, NSArray<__NSString__> *_array;) or by explicitly defining the contained types in -membersForCoder"
+ "Collection ivar %@ must specifcy a well-defined-but-not-NSObject contained class"
+ "Decoded NSData for \"%@\" does not match expected encoding \"%s\" (%lu vs %lu)"
+ "Decoded NSValue for \"%@\" does not match expected encoding \"%s\""
+ "Dictionary ivar %@ does not specify its keys as NSString"
+ "Dictionary ivar %@ must not specify a collection type as its value class"
+ "Dictionary ivar %@ specifies incorrect number of contained classes (must be zero or two)"
+ "Invalid security task for checking entitlement %{public}@"
+ "Invalid security task for getting entitlement %{public}@"
+ "Ivar %@ is not supported"
+ "Ivar %@ must have a well-defined-but-not-NSObject class"
+ "NSNumber"
+ "NSSet<BSObjCIvar *> * _Nonnull BSXPCAutoCodingGetIvars(NSObject<BSXPCAutoCoding> * _Nonnull, Class _Nonnull)"
+ "NSString *getkCAAnimationNonZero(void)"
+ "NSXPCSecureCoding"
+ "OS_xpc_%@"
+ "Object of class \"%@\" returned nil from +alloc"
+ "Object of class \"%@\" returned nil from -awakeAfterUsingCoder:"
+ "Object of class \"%@\" returned nil from -init"
+ "Object of class \"%@\" returned nil from -initWithBSXPCCoder:"
+ "Object of class \"%@\" returned nil from -initWithXPCDictionary:"
+ "T@\"BSSimpleAssertion\",R,N"
+ "T@\"NSArray\",R,C,N,V_supportedCodings"
+ "TB,R,N,V_wasExplicit"
+ "The value of ivar \"%@\" is not an object (%@), so cannot specify any class(es): %@"
+ "Unable to determine class of ivar %@{public} from encoding: %s"
+ "Unable to get entitlement %{public}@ for security task. Error: %{public}@"
+ "Unable to parse xpc type from \"%@\""
+ "Unsupported ivar: %@ (%@)"
+ "Unsupported type encoding (%@) for ivar %@"
+ "Unsupported type encoding (%s) for ivar %@"
+ "[object respondsToSelector:@selector(membersForCoder)]"
+ "^{objc_ivar=}"
+ "_alternateNames"
+ "_applyToSettings:preserveDiffs:"
+ "_initWithReason:identifier:queue:type:block:"
+ "_initWithReason:identifier:requiredInvalidationQueue:deallocPolicy:invalidatedWithContextBlock:"
+ "_initWithStoredDuration:storedDurationIsDirty:delay:frameInterval:frameRange:highFrameRateReason:timingFunction:speed:beginTime:mass:stiffness:damping:epsilon:initialVelocity:isSpring:"
+ "_invalidationType"
+ "_ivar"
+ "_lock_beginTime"
+ "_offset"
+ "_setError"
+ "_supportedCodings"
+ "_wasExplicit"
+ "addSupportedCoding:"
+ "arrayByAddingObject:"
+ "assertion"
+ "awakeAfterUsingCoder:"
+ "awakeFromCoder"
+ "beginTime"
+ "bs_isPlist"
+ "bsx_auto"
+ "builderWithClass:"
+ "bytes != NULL"
+ "calling -[super %@] is not supported"
+ "cannot apply a keyed diff to a non-keyed diff"
+ "cannot apply a non-keyed diff to a keyed diff"
+ "cannot map @selector(%@) to IVAR(%@) because a member already exists with that name"
+ "class doesn't return YES from +%@"
+ "coding"
+ "coding != ((void *)0)"
+ "copyApplyingDiff:"
+ "decodeStruct:withObjCType:forKey:"
+ "decodeValueWithObjCType:forKey:"
+ "decodeWithCoder:"
+ "encodeStruct:withObjCType:forKey:"
+ "encoding != NULL"
+ "failed to add %@ to %@"
+ "getBytes:range:"
+ "getValue:size:"
+ "hasError"
+ "id _BSAutoMemberV(NSString *, va_list)"
+ "implicit"
+ "initWithReason:identifier:requiredInvalidationQueue:deallocPolicy:invalidatedWithContextBlock:"
+ "initWithReason:invalidatedBlock:"
+ "initWithReason:invalidatedWithContextBlock:"
+ "invalid-init"
+ "ivarWithName:ivar:containedClasses:alternateNames:"
+ "kCAAnimationNonZero"
+ "membersForCoder"
+ "no invalidation block found for <%@:%p> (%@) in implicit invalidation in dealloc"
+ "object does not respond to -membersForCoder"
+ "property %@ from %@ has no ivar"
+ "punctuationCharacterSet"
+ "replacementObjectForCoder:"
+ "setBeginTime:"
+ "setBeginTimeMode:"
+ "setPosition:"
+ "setSupportedCodings:"
+ "string"
+ "supportedCodings"
+ "supportedCodings != ((void *)0)"
+ "t0"
+ "testEncodeAndDecodeObject:ofClass:"
+ "unknown deallocPolicy %li"
+ "v16@?0@\"<BSSimpleAssertionInvalidationContext>\"8"
+ "v16@?0@\"<BSXPCAutoCodingConfiguring>\"8"
+ "v24@0:8@\"BSDescriptionStream\"16"
+ "v24@0:8@\"NSObject<BSXPCDecoding>\"16"
+ "v24@0:8@\"NSObject<BSXPCEncoding>\"16"
+ "v28@0:8@16B24"
+ "v40@0:8rn^v16r*24@\"NSString\"32"
+ "v40@0:8rn^v16r*24@32"
+ "v@:@"
+ "valueWithPointer:"
+ "void _BSXPCAutoCodingImplementCoder(Class, Protocol *)"
+ "void _BSXPCDecodeIvarsForObject(NSObject<BSXPCAutoCoding> *const __strong _Nonnull, const __strong id _Nonnull)"
+ "void _BSXPCEncodeIvarsForObject(NSObject<BSXPCAutoCoding> *const __strong _Nonnull, const __strong id _Nonnull)"
+ "wasExplicit"
+ "xpc"
+ "xpc_"
- "%@ could not encode object %@ because it supports neither BSXPC[Secure]Coding nor NSSecureCoding."
- "<%@:%p duration=%f delay=%f interval=%f range={%f,%f,%f} reason=%i timing=%@ speed=%f>"
- "<%@:%p mass=%f stiffness=%f damping=%f epsilon=%f initialVelocity=%f %@delay=%f interval=%f range={%f,%f,%f} reason=%i timing=%@ speed=%f>"
- "BSCornerRadiusConfigurationBottomLeftKey"
- "BSCornerRadiusConfigurationBottomRightKey"
- "BSCornerRadiusConfigurationTopLeftKey"
- "BSCornerRadiusConfigurationTopRightKey"
- "BSXPCCoderExtras"
- "Client code must invalidate <%@:%p> (%@: %@) before dealloc"
- "Unable to get entitlement for an invalid secTask"
- "Unable to get entitlements for client task. Error: %{public}@"
- "Unable to get security task"
- "_initWithStoredDuration:storedDurationIsDirty:delay:frameInterval:frameRange:highFrameRateReason:timingFunction:speed:mass:stiffness:damping:epsilon:initialVelocity:isSpring:"
- "auditTokenValue"
- "bs_class"
- "currentOrientation"
- "fallbackOrientations"
- "invalidationBlock"
- "targetOrientation"

```
