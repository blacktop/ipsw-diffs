## AppStoreFoundation

> `/System/Library/PrivateFrameworks/AppStoreFoundation.framework/AppStoreFoundation`

```diff

-12.3.3.0.0
-  __TEXT.__text: 0x41d4
-  __TEXT.__auth_stubs: 0x550
-  __TEXT.__objc_methlist: 0x2e4
-  __TEXT.__const: 0x88
-  __TEXT.__swift5_typeref: 0x5e
-  __TEXT.__swift5_fieldmd: 0x10
-  __TEXT.__constg_swiftt: 0x24
-  __TEXT.__swift5_capture: 0x40
+12.4.20.2.1
+  __TEXT.__text: 0xd390
+  __TEXT.__auth_stubs: 0xac0
+  __TEXT.__objc_methlist: 0x258
+  __TEXT.__const: 0x5cc
+  __TEXT.__swift5_typeref: 0x1a6
+  __TEXT.__swift5_fieldmd: 0x400
+  __TEXT.__constg_swiftt: 0x240
+  __TEXT.__swift5_capture: 0x50
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__swift5_proto: 0x4
-  __TEXT.__cstring: 0x14a
-  __TEXT.__oslogstring: 0x427
-  __TEXT.__gcc_except_tab: 0x24
-  __TEXT.__unwind_info: 0x128
-  __TEXT.__objc_classname: 0x94
-  __TEXT.__objc_methname: 0x95e
-  __TEXT.__objc_methtype: 0x97
-  __TEXT.__objc_stubs: 0x4a0
-  __DATA_CONST.__got: 0xb8
-  __DATA_CONST.__const: 0xa0
-  __DATA_CONST.__objc_classlist: 0x40
-  __DATA_CONST.__objc_protolist: 0x8
+  __TEXT.__swift5_proto: 0x2c
+  __TEXT.__swift5_types: 0x2c
+  __TEXT.__cstring: 0x2cd
+  __TEXT.__swift5_reflstr: 0x312
+  __TEXT.__swift5_assocty: 0x30
+  __TEXT.__oslogstring: 0x64
+  __TEXT.__unwind_info: 0x350
+  __TEXT.__eh_frame: 0x388
+  __TEXT.__objc_classname: 0xd8
+  __TEXT.__objc_methname: 0x4c6
+  __TEXT.__objc_methtype: 0x39
+  __TEXT.__objc_stubs: 0x280
+  __DATA_CONST.__got: 0x118
+  __DATA_CONST.__const: 0x40
+  __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x250
-  __DATA_CONST.__objc_superrefs: 0x38
-  __AUTH_CONST.__auth_got: 0x2b8
-  __AUTH_CONST.__const: 0x98
-  __AUTH_CONST.__cfstring: 0x1e0
-  __AUTH_CONST.__objc_const: 0xc70
-  __DATA.__objc_ivar: 0xac
-  __DATA.__data: 0x60
-  __DATA_DIRTY.__objc_data: 0x280
-  __DATA_DIRTY.__data: 0x10
-  __DATA_DIRTY.__bss: 0x20
+  __DATA_CONST.__objc_selrefs: 0x1b0
+  __AUTH_CONST.__auth_got: 0x568
+  __AUTH_CONST.__const: 0x3c0
+  __AUTH_CONST.__objc_const: 0x430
+  __AUTH.__objc_data: 0x130
+  __AUTH.__data: 0x328
+  __DATA.__data: 0x188
+  __DATA.__bss: 0x500
+  __DATA_DIRTY.__objc_data: 0x50
+  __DATA_DIRTY.__data: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/PrivateFrameworks/SwiftASN1Internal.framework/SwiftASN1Internal
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  UUID: E337FCF4-F355-3D28-9B1A-DD3945F2FFE1
-  Functions: 78
-  Symbols:   414
-  CStrings:  237
+  - /usr/lib/swift/libswiftos.dylib
+  UUID: 39F1FA16-D5FB-3279-B52A-F4976EB7E18C
+  Functions: 286
+  Symbols:   234
+  CStrings:  106
 
Symbols:
+ +[ASFReceipt(Factory) receiptFromBundleAtPath:]
+ +[ASFReceipt(Factory) receiptFromBundleAtURL:]
+ +[ASFReceipt(Factory) receiptWithContentsOfFile:]
+ +[ASFReceipt(Factory) receiptWithData:]
+ _CMSDecoderCopyAllCerts
+ _CMSDecoderCopyContent
+ _CMSDecoderCreate
+ _CMSDecoderFinalizeMessage
+ _CMSDecoderUpdateMessage
+ _OBJC_CLASS_$_NSFileManager
+ _OBJC_CLASS_$_NSISO8601DateFormatter
+ _OBJC_CLASS_$__TtCs12_SwiftObject
+ _OBJC_METACLASS_$__TtCs12_SwiftObject
+ _SecCopyErrorMessageString
+ _SecPolicyCreateMacAppStoreReceipt
+ __DATA_ASFIAPItem
+ __DATA_ASFReceipt
+ __DATA__TtCE18AppStoreFoundationCSo10ASFIAPItemP33_AF09DD73141AA81D391F3328CADFFE907Storage
+ __DATA__TtCE18AppStoreFoundationCSo10ASFReceiptP33_3CEB2F4D486FC6CA854E7237D99D471D7Storage
+ __INSTANCE_METHODS_ASFIAPItem
+ __INSTANCE_METHODS_ASFReceipt
+ __IVARS_ASFIAPItem
+ __IVARS_ASFReceipt
+ __IVARS__TtCE18AppStoreFoundationCSo10ASFIAPItemP33_AF09DD73141AA81D391F3328CADFFE907Storage
+ __IVARS__TtCE18AppStoreFoundationCSo10ASFReceiptP33_3CEB2F4D486FC6CA854E7237D99D471D7Storage
+ __METACLASS_DATA_ASFIAPItem
+ __METACLASS_DATA_ASFReceipt
+ __METACLASS_DATA__TtCE18AppStoreFoundationCSo10ASFIAPItemP33_AF09DD73141AA81D391F3328CADFFE907Storage
+ __METACLASS_DATA__TtCE18AppStoreFoundationCSo10ASFReceiptP33_3CEB2F4D486FC6CA854E7237D99D471D7Storage
+ __OBJC_$_CLASS_METHODS_ASFReceipt(Helpers|Factory)
+ __PROPERTIES_ASFIAPItem
+ __PROPERTIES_ASFReceipt
+ ___swift_allocate_value_buffer
+ ___swift_destroy_boxed_opaque_existential_0
+ ___swift_destroy_boxed_opaque_existential_1
+ ___swift_instantiateConcreteTypeFromMangledNameAbstractV2
+ ___swift_instantiateConcreteTypeFromMangledNameV2
+ ___swift_memcpy1_1
+ ___swift_memcpy49_8
+ ___swift_noop_void_return
+ ___swift_project_boxed_opaque_existential_1
+ ___swift_project_value_buffer
+ __swiftEmptyArrayStorage
+ __swiftEmptyDictionarySingleton
+ __swiftImmortalRefCount
+ __swift_FORCE_LOAD_$_swiftOSLog
+ __swift_FORCE_LOAD_$_swiftOSLog_$_AppStoreFoundation
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftos_$_AppStoreFoundation
+ __swift_stdlib_bridgeErrorToNSError
+ __swift_stdlib_malloc_size
+ __swift_stdlib_reportUnimplementedInitializer
+ _associated conformance 18AppStoreFoundation0aB12ReceiptErrorV0E4CodeOSHAASQ
+ _associated conformance 18AppStoreFoundation0aB7ReceiptV0D4TypeOSHAASQ
+ _associated conformance 18AppStoreFoundation16ReceiptAttribute33_16340A2AAB0AE6628EAC475C43FDA413LLOSHAASQ
+ _bzero
+ _malloc_size
+ _memcpy
+ _memmove
+ _objc_allocWithZone
+ _objc_msgSend$URL
+ _objc_msgSend$defaultManager
+ _objc_msgSend$fileExistsAtPath:
+ _objc_msgSend$init
+ _objc_msgSend$isExpired
+ _objc_msgSend$isRevoked
+ _objc_msgSend$isVPPLicensed
+ _objc_msgSend$receiptData
+ _objc_msgSend$receiptURLForBundleAtURL:
+ _objc_msgSend$vppStateFlags
+ _objc_retain_x23
+ _swift_allocError
+ _swift_arrayInitWithCopy
+ _swift_arrayInitWithTakeBackToFront
+ _swift_arrayInitWithTakeFrontToBack
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRetain
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_deallocClassInstance
+ _swift_deallocPartialClassInstance
+ _swift_deletedMethodError
+ _swift_dynamicCastObjCClass
+ _swift_errorRelease
+ _swift_errorRetain
+ _swift_getEnumTagSinglePayloadGeneric
+ _swift_getForeignTypeMetadata
+ _swift_getObjCClassFromMetadata
+ _swift_getObjCClassMetadata
+ _swift_getObjectType
+ _swift_getSingletonMetadata
+ _swift_getTypeByMangledNameInContext2
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _swift_getWitnessTable
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_once
+ _swift_retain
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_storeEnumTagSinglePayloadGeneric
+ _swift_unknownObjectRelease
+ _swift_unknownObjectRetain
+ _swift_updateClassMetadata2
+ _swift_willThrow
+ _symbolic $sSY
+ _symbolic SS
+ _symbolic SSSg
+ _symbolic Say_____G 18AppStoreFoundation0aB7ReceiptV3IAPV
+ _symbolic So10ASFIAPItemC
+ _symbolic So10ASFReceiptC
+ _symbolic So8NSObjectCSg
+ _symbolic Su
+ _symbolic _____ 10Foundation4DataV
+ _symbolic _____ 10Foundation4DateV
+ _symbolic _____ 17SwiftASN1Internal0B11OctetStringV
+ _symbolic _____ 18AppStoreFoundation0aB12ReceiptErrorV
+ _symbolic _____ 18AppStoreFoundation0aB12ReceiptErrorV0E4CodeO
+ _symbolic _____ 18AppStoreFoundation0aB7ReceiptV
+ _symbolic _____ 18AppStoreFoundation0aB7ReceiptV0D4TypeO
+ _symbolic _____ 18AppStoreFoundation0aB7ReceiptV3IAPV
+ _symbolic _____ 18AppStoreFoundation12ReceiptField33_16340A2AAB0AE6628EAC475C43FDA413LLV
+ _symbolic _____ 18AppStoreFoundation16ReceiptAttribute33_16340A2AAB0AE6628EAC475C43FDA413LLO
+ _symbolic _____ So10ASFIAPItemC18AppStoreFoundationE7Storage33_AF09DD73141AA81D391F3328CADFFE90LLC
+ _symbolic _____ So10ASFReceiptC18AppStoreFoundationE7Storage33_3CEB2F4D486FC6CA854E7237D99D471DLLC
+ _symbolic _____ s12StaticStringV
+ _symbolic _____ s5Int64V
+ _symbolic _____Sg 10Foundation3URLV
+ _symbolic _____Sg 10Foundation4DataV
+ _symbolic _____Sg 10Foundation4DateV
+ _symbolic _____Sg 17SwiftASN1Internal0B4NodeV
+ _symbolic _____Sg s5Int64V
+ _symbolic _____Sg_ABt 10Foundation4DateV
+ _symbolic _____y_____G s10ArraySliceV s5UInt8V
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 18AppStoreFoundation0dE7ReceiptV3IAPV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 18AppStoreFoundation12ReceiptField33_16340A2AAB0AE6628EAC475C43FDA413LLV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC s5UInt8V
+ _symbolic _____y_____Say_____GG s18_DictionaryStorageC s5Int64V 18AppStoreFoundation12ReceiptField33_16340A2AAB0AE6628EAC475C43FDA413LLV
+ _symbolic _____yyXlG s23_ContiguousArrayStorageC
+ _type_layout_string 18AppStoreFoundation0aB12ReceiptErrorV
- +[ASFAsn1ReceiptIAPToken readFromBuffer:]
- +[ASFAsn1ReceiptToken readFromBuffer:]
- +[ASFAsn1Token readTokenFromBuffer:length:]
- +[ASFAsn1Token readTokenFromBuffer:opaque:length:]
- +[ASFReceipt receiptFromBundleAtPath:]
- +[ASFReceipt receiptFromBundleAtURL:]
- +[ASFReceipt receiptWithContentsOfFile:]
- +[ASFReceipt receiptWithData:]
- -[ASFAsn1IntegerToken description]
- -[ASFAsn1OSToken .cxx_destruct]
- -[ASFAsn1OSToken stringValue]
- -[ASFAsn1ReceiptIAPToken .cxx_destruct]
- -[ASFAsn1ReceiptIAPToken _initWithType:typeVersion:contentToken:]
- -[ASFAsn1ReceiptIAPToken description]
- -[ASFAsn1ReceiptIAPToken integerValue]
- -[ASFAsn1ReceiptIAPToken stringValue]
- -[ASFAsn1ReceiptToken .cxx_destruct]
- -[ASFAsn1ReceiptToken contentIsAnInteger]
- -[ASFAsn1ReceiptToken description]
- -[ASFAsn1ReceiptToken integerValue]
- -[ASFAsn1ReceiptToken stringValue]
- -[ASFAsn1SetToken .cxx_destruct]
- -[ASFAsn1SetToken description]
- -[ASFAsn1SetToken nextToken]
- -[ASFAsn1Token .cxx_destruct]
- -[ASFAsn1Token description]
- -[ASFIAPItem .cxx_destruct]
- -[ASFIAPItem copyWithZone:]
- -[ASFIAPItem originalPurchaseDate]
- -[ASFIAPItem originalTransactionID]
- -[ASFIAPItem productID]
- -[ASFIAPItem purchaseDate]
- -[ASFIAPItem quantity]
- -[ASFIAPItem transactionID]
- -[ASFReceipt .cxx_destruct]
- -[ASFReceipt bundleIDData]
- -[ASFReceipt bundleID]
- -[ASFReceipt bundleVersion]
- -[ASFReceipt cancellationReason]
- -[ASFReceipt creationDate]
- -[ASFReceipt developerID]
- -[ASFReceipt downloadID]
- -[ASFReceipt expirationDate]
- -[ASFReceipt frAppVersion]
- -[ASFReceipt frToolVersion]
- -[ASFReceipt hwtype]
- -[ASFReceipt iaps]
- -[ASFReceipt initWithContentsOfFile:]
- -[ASFReceipt initWithData:]
- -[ASFReceipt installerVersionID]
- -[ASFReceipt isDSIDless]
- -[ASFReceipt isRevoked]
- -[ASFReceipt isVPPLicensed]
- -[ASFReceipt itemID]
- -[ASFReceipt opaqueDSIDData]
- -[ASFReceipt opaqueDSIDString]
- -[ASFReceipt organizationDisplayName]
- -[ASFReceipt parentalControls]
- -[ASFReceipt path]
- -[ASFReceipt purchaseDate]
- -[ASFReceipt receiptDataString]
- -[ASFReceipt receiptData]
- -[ASFReceipt receiptType]
- -[ASFReceipt renewalDate]
- -[ASFReceipt sha1]
- GCC_except_table0
- _ASFLogHandleForCategory
- _ASFLogHandleForCategory.logHandles.0
- _ASFLogHandleForCategory.logHandles.1
- _ASFLogHandleForCategory.onceToken
- _CFArrayAppendValue
- _CFArrayCreateMutable
- _CFDataCreate
- _CFDictionaryAddValue
- _CFDictionaryCreateMutable
- _CFRelease
- _NSCocoaErrorDomain
- _NSLog
- _OBJC_CLASS_$_ASFAsn1IntegerToken
- _OBJC_CLASS_$_ASFAsn1OSToken
- _OBJC_CLASS_$_ASFAsn1ReceiptIAPToken
- _OBJC_CLASS_$_ASFAsn1ReceiptToken
- _OBJC_CLASS_$_ASFAsn1SetToken
- _OBJC_CLASS_$_ASFAsn1Token
- _OBJC_CLASS_$_NSData
- _OBJC_CLASS_$_NSDateFormatter
- _OBJC_CLASS_$_NSLocale
- _OBJC_CLASS_$_NSMutableArray
- _OBJC_CLASS_$_NSNumber
- _OBJC_IVAR_$_ASFAsn1IntegerToken.mValue
- _OBJC_IVAR_$_ASFAsn1OSToken.mValue
- _OBJC_IVAR_$_ASFAsn1ReceiptIAPToken.mContentToken
- _OBJC_IVAR_$_ASFAsn1ReceiptIAPToken.mType
- _OBJC_IVAR_$_ASFAsn1ReceiptIAPToken.mTypeVersion
- _OBJC_IVAR_$_ASFAsn1ReceiptToken.mContentToken
- _OBJC_IVAR_$_ASFAsn1ReceiptToken.mType
- _OBJC_IVAR_$_ASFAsn1ReceiptToken.mTypeVersion
- _OBJC_IVAR_$_ASFAsn1SetToken.mReadData
- _OBJC_IVAR_$_ASFAsn1Token.mClass
- _OBJC_IVAR_$_ASFAsn1Token.mData
- _OBJC_IVAR_$_ASFAsn1Token.mIdentifier
- _OBJC_IVAR_$_ASFIAPItem._originalPurchaseDate
- _OBJC_IVAR_$_ASFIAPItem._originalTransactionID
- _OBJC_IVAR_$_ASFIAPItem._productID
- _OBJC_IVAR_$_ASFIAPItem._purchaseDate
- _OBJC_IVAR_$_ASFIAPItem._quantity
- _OBJC_IVAR_$_ASFIAPItem._transactionID
- _OBJC_IVAR_$_ASFReceipt._bundleID
- _OBJC_IVAR_$_ASFReceipt._bundleIDData
- _OBJC_IVAR_$_ASFReceipt._bundleVersion
- _OBJC_IVAR_$_ASFReceipt._cancellationReason
- _OBJC_IVAR_$_ASFReceipt._creationDate
- _OBJC_IVAR_$_ASFReceipt._developerID
- _OBJC_IVAR_$_ASFReceipt._downloadID
- _OBJC_IVAR_$_ASFReceipt._expirationDate
- _OBJC_IVAR_$_ASFReceipt._frAppVersion
- _OBJC_IVAR_$_ASFReceipt._frToolVersion
- _OBJC_IVAR_$_ASFReceipt._hwtype
- _OBJC_IVAR_$_ASFReceipt._iaps
- _OBJC_IVAR_$_ASFReceipt._installerVersionID
- _OBJC_IVAR_$_ASFReceipt._itemID
- _OBJC_IVAR_$_ASFReceipt._mutableIAPs
- _OBJC_IVAR_$_ASFReceipt._opaqueDSIDData
- _OBJC_IVAR_$_ASFReceipt._opaqueDSIDString
- _OBJC_IVAR_$_ASFReceipt._organizationDisplayName
- _OBJC_IVAR_$_ASFReceipt._parentalControls
- _OBJC_IVAR_$_ASFReceipt._path
- _OBJC_IVAR_$_ASFReceipt._purchaseDate
- _OBJC_IVAR_$_ASFReceipt._receiptType
- _OBJC_IVAR_$_ASFReceipt._renewalDate
- _OBJC_IVAR_$_ASFReceipt._sha1
- _OBJC_IVAR_$_ASFReceipt._verbose
- _OBJC_METACLASS_$_ASFAsn1IntegerToken
- _OBJC_METACLASS_$_ASFAsn1OSToken
- _OBJC_METACLASS_$_ASFAsn1ReceiptIAPToken
- _OBJC_METACLASS_$_ASFAsn1ReceiptToken
- _OBJC_METACLASS_$_ASFAsn1SetToken
- _OBJC_METACLASS_$_ASFAsn1Token
- _SecCertificateCreateWithData
- _SecCmsContentInfoGetContent
- _SecCmsContentInfoGetContentTypeTag
- _SecCmsDecoderCreate
- _SecCmsDecoderDestroy
- _SecCmsDecoderFinish
- _SecCmsDecoderUpdate
- _SecCmsMessageContentLevel
- _SecCmsMessageContentLevelCount
- _SecCmsMessageDestroy
- _SecCmsMessageGetContent
- _SecCmsSignedDataGetCertificateList
- _SecPolicyCreateWithProperties
- __Block_object_dispose
- __NSConcreteGlobalBlock
- __NSConcreteStackBlock
- __OBJC_$_CLASS_METHODS_ASFReceipt
- __OBJC_$_INSTANCE_METHODS_ASFAsn1IntegerToken
- __OBJC_$_INSTANCE_METHODS_ASFAsn1OSToken
- __OBJC_$_INSTANCE_METHODS_ASFAsn1ReceiptIAPToken
- __OBJC_$_INSTANCE_METHODS_ASFAsn1ReceiptToken
- __OBJC_$_INSTANCE_METHODS_ASFAsn1SetToken
- __OBJC_$_INSTANCE_METHODS_ASFAsn1Token
- __OBJC_$_INSTANCE_METHODS_ASFIAPItem
- __OBJC_$_INSTANCE_METHODS_ASFReceipt
- __OBJC_$_INSTANCE_VARIABLES_ASFAsn1IntegerToken
- __OBJC_$_INSTANCE_VARIABLES_ASFAsn1OSToken
- __OBJC_$_INSTANCE_VARIABLES_ASFAsn1ReceiptIAPToken
- __OBJC_$_INSTANCE_VARIABLES_ASFAsn1ReceiptToken
- __OBJC_$_INSTANCE_VARIABLES_ASFAsn1SetToken
- __OBJC_$_INSTANCE_VARIABLES_ASFAsn1Token
- __OBJC_$_INSTANCE_VARIABLES_ASFIAPItem
- __OBJC_$_INSTANCE_VARIABLES_ASFReceipt
- __OBJC_$_PROP_LIST_ASFIAPItem
- __OBJC_$_PROP_LIST_ASFReceipt
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying
- __OBJC_CLASS_PROTOCOLS_$_ASFIAPItem
- __OBJC_CLASS_RO_$_ASFAsn1IntegerToken
- __OBJC_CLASS_RO_$_ASFAsn1OSToken
- __OBJC_CLASS_RO_$_ASFAsn1ReceiptIAPToken
- __OBJC_CLASS_RO_$_ASFAsn1ReceiptToken
- __OBJC_CLASS_RO_$_ASFAsn1SetToken
- __OBJC_CLASS_RO_$_ASFAsn1Token
- __OBJC_CLASS_RO_$_ASFIAPItem
- __OBJC_CLASS_RO_$_ASFReceipt
- __OBJC_LABEL_PROTOCOL_$_NSCopying
- __OBJC_METACLASS_RO_$_ASFAsn1IntegerToken
- __OBJC_METACLASS_RO_$_ASFAsn1OSToken
- __OBJC_METACLASS_RO_$_ASFAsn1ReceiptIAPToken
- __OBJC_METACLASS_RO_$_ASFAsn1ReceiptToken
- __OBJC_METACLASS_RO_$_ASFAsn1SetToken
- __OBJC_METACLASS_RO_$_ASFAsn1Token
- __OBJC_METACLASS_RO_$_ASFIAPItem
- __OBJC_METACLASS_RO_$_ASFReceipt
- __OBJC_PROTOCOL_$_NSCopying
- __Unwind_Resume
- ___ASFLogHandleForCategory_block_invoke
- ___CFConstantStringClassReference
- ___block_descriptor_32_e5_v8?0l
- ___block_descriptor_48_e8_32r_e29_v40?0r^v8{_NSRange=QQ}16^B32lr32l8
- ___block_descriptor_56_e8_32r_e29_v40?0r^v8{_NSRange=QQ}16^B32lr32l8
- ___block_literal_global
- ___objc_personality_v0
- ___readIdentifier_block_invoke
- ___readLength_block_invoke
- __os_log_disabled
- __os_log_error_impl
- __readStringDate
- _dispatch_once
- _kCFAllocatorDefault
- _kCFTypeArrayCallBacks
- _kCFTypeDictionaryKeyCallBacks
- _kCFTypeDictionaryValueCallBacks
- _kSecPolicyAppleRevocation
- _kSecPolicyAppleX509Basic
- _kSecPolicyMacAppStoreReceipt
- _kSecPolicyRevocationFlags
- _objc_alloc_init
- _objc_autoreleasePoolPop
- _objc_autoreleasePoolPush
- _objc_claimAutoreleasedReturnValue
- _objc_getProperty
- _objc_msgSend$URLByAppendingPathComponent:isDirectory:
- _objc_msgSend$addObject:
- _objc_msgSend$base64EncodedStringWithOptions:
- _objc_msgSend$bytes
- _objc_msgSend$code
- _objc_msgSend$copy
- _objc_msgSend$copyWithZone:
- _objc_msgSend$count
- _objc_msgSend$dataWithContentsOfFile:
- _objc_msgSend$dataWithContentsOfFile:options:error:
- _objc_msgSend$domain
- _objc_msgSend$enumerateByteRangesUsingBlock:
- _objc_msgSend$getBytes:length:
- _objc_msgSend$hasSuffix:
- _objc_msgSend$initWithBytes:length:
- _objc_msgSend$initWithData:encoding:
- _objc_msgSend$initWithLocaleIdentifier:
- _objc_msgSend$isEqualToString:
- _objc_msgSend$length
- _objc_msgSend$numberWithUnsignedLong:
- _objc_msgSend$numberWithUnsignedLongLong:
- _objc_msgSend$receiptWithContentsOfFile:
- _objc_msgSend$setDateFormat:
- _objc_msgSend$setLocale:
- _objc_msgSend$stringValue
- _objc_msgSend$stringWithFormat:
- _objc_msgSend$subdataWithRange:
- _objc_opt_class
- _objc_opt_isKindOfClass
- _objc_opt_new
- _objc_release
- _objc_release_x1
- _objc_release_x28
- _objc_release_x9
- _objc_retainAutorelease
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x21
- _objc_retain_x22
- _objc_setProperty_atomic_copy
- _objc_storeStrong
- _os_log_create
CStrings:
+ " was not initialized"
+ "' failed, no value set"
+ "' failed, unexpected type "
+ "?"
+ "AppStoreFoundation.ASFReceipt"
+ "AppStoreFoundation/AppStoreReceipt.swift"
+ "Copy all certs"
+ "Copy content"
+ "Could not understand the receipt type '"
+ "Create decoder"
+ "Create trust"
+ "Decoding attribute '"
+ "Decoding required attribute '"
+ "Error evaluating trust: "
+ "Factory"
+ "Failed to create policy"
+ "Failed to parse node for attribute "
+ "Failed to parse receipt at %{public}s: %{public}@"
+ "Failed to parse receipt: %{public}@"
+ "Finalize message"
+ "Helpers"
+ "Production"
+ "ProductionStub"
+ "ProductionVPP"
+ "Provided receipt data was empty"
+ "Q16@0:8"
+ "Q24@0:8@16"
+ "Set policies"
+ "Set verify date"
+ "T@\"NSArray\",N,R"
+ "T@\"NSData\",N,R"
+ "T@\"NSDate\",N,R"
+ "T@\"NSNumber\",N,R"
+ "T@\"NSString\",N,R"
+ "TB,N,R"
+ "TQ,N,R"
+ "URL"
+ "Unknown trust evaluation failure"
+ "Update message"
+ "_TtCE18AppStoreFoundationCSo10ASFIAPItemP33_AF09DD73141AA81D391F3328CADFFE907Storage"
+ "_TtCE18AppStoreFoundationCSo10ASFReceiptP33_3CEB2F4D486FC6CA854E7237D99D471D7Storage"
+ "_storage"
+ "defaultManager"
+ "fileExistsAtPath:"
+ "iap"
+ "init()"
+ "isExpired"
+ "receiptURLForBundleAtURL:"
+ "vppStateFlags"
+ "vppStateFlagsWithRecord:"
- "!"
- "%lld"
- "0"
- "@\"ASFAsn1Token\""
- "@\"NSArray\""
- "@\"NSData\""
- "@\"NSDate\""
- "@\"NSMutableArray\""
- "@\"NSNumber\""
- "@\"NSString\""
- "@24@0:8^{_NSZone=}16"
- "ASFAsn1IntegerToken"
- "ASFAsn1OSToken"
- "ASFAsn1ReceiptIAPToken"
- "ASFAsn1ReceiptToken"
- "ASFAsn1SetToken"
- "ASFAsn1Token"
- "AdamID: %{public}@"
- "Allowing invalid receipt because it is a stub receipt [%{iec-bytes}ld]"
- "Allowing invalid receipt because it is an StoreKit testing receipt [%{iec-bytes}ld]"
- "Application version: %{public}@"
- "B"
- "BundleID: %{public}@"
- "Byte count would result in overflow: %d"
- "C"
- "Cancellation reason: %{public}@"
- "Could not create decoder"
- "Could not create trust"
- "Could not parse data"
- "Could not read certificates"
- "Could not read data"
- "Could not set verification date"
- "DSID: %{public}@"
- "Decode iaps failed"
- "Default"
- "DeveloperID: %{public}@"
- "DownloadID: %{public}@"
- "Error evaluating trust: %{public}@"
- "Error reading receipt: %{public}@"
- "FR app version: %{public}@"
- "FR tool version: %{public}@"
- "Failed to evaluate trust"
- "Failed to load data"
- "Failed to parse data"
- "Failed to update policies"
- "HW type: %{public}@"
- "INT Token. Value:%lld (%llx)"
- "Installer versionID: %{public}@"
- "Invalid receipt [%{iec-bytes}ld]"
- "NSCopying"
- "No content"
- "Organization display name: %{public}@"
- "Parental controls: %{public}@"
- "Parsing receipt"
- "Q"
- "Receipt created: %{public}@"
- "Receipt expires: %{public}@"
- "Receipt renewal: %{public}@"
- "Receipt type: %{public}@"
- "SET Token. (length:%ld)"
- "SHA1: %{public}@"
- "Signpost"
- "StoreKit"
- "Stub"
- "T@\"NSArray\",R,V_iaps"
- "T@\"NSData\",R"
- "T@\"NSData\",R,V_bundleIDData"
- "T@\"NSData\",R,V_opaqueDSIDData"
- "T@\"NSData\",R,V_sha1"
- "T@\"NSDate\",R"
- "T@\"NSDate\",R,V_creationDate"
- "T@\"NSDate\",R,V_expirationDate"
- "T@\"NSDate\",R,V_purchaseDate"
- "T@\"NSDate\",R,V_renewalDate"
- "T@\"NSNumber\",R"
- "T@\"NSNumber\",R,V_frToolVersion"
- "T@\"NSNumber\",R,V_itemID"
- "T@\"NSString\",R"
- "T@\"NSString\",R,V_bundleID"
- "T@\"NSString\",R,V_bundleVersion"
- "T@\"NSString\",R,V_cancellationReason"
- "T@\"NSString\",R,V_developerID"
- "T@\"NSString\",R,V_downloadID"
- "T@\"NSString\",R,V_frAppVersion"
- "T@\"NSString\",R,V_hwtype"
- "T@\"NSString\",R,V_installerVersionID"
- "T@\"NSString\",R,V_opaqueDSIDString"
- "T@\"NSString\",R,V_organizationDisplayName"
- "T@\"NSString\",R,V_parentalControls"
- "T@\"NSString\",R,V_path"
- "T@\"NSString\",R,V_receiptType"
- "TB,R"
- "Token of class:%d ID:%ld length:%ld data:%@"
- "Transaction date: %{public}@"
- "Type:%ld Version:%ld Data:%@"
- "URLByAppendingPathComponent:isDirectory:"
- "Xcode"
- "_bundleID"
- "_bundleIDData"
- "_bundleVersion"
- "_cancellationReason"
- "_creationDate"
- "_developerID"
- "_downloadID"
- "_expirationDate"
- "_frAppVersion"
- "_frToolVersion"
- "_hwtype"
- "_iaps"
- "_installerVersionID"
- "_itemID"
- "_mutableIAPs"
- "_opaqueDSIDData"
- "_opaqueDSIDString"
- "_organizationDisplayName"
- "_originalPurchaseDate"
- "_originalTransactionID"
- "_parentalControls"
- "_path"
- "_productID"
- "_purchaseDate"
- "_quantity"
- "_receiptType"
- "_renewalDate"
- "_sha1"
- "_transactionID"
- "_verbose"
- "addObject:"
- "base64EncodedStringWithOptions:"
- "bytes"
- "code"
- "copy"
- "copyWithZone:"
- "count"
- "dataWithContentsOfFile:"
- "dataWithContentsOfFile:options:error:"
- "description"
- "domain"
- "en_US_POSIX"
- "enumerateByteRangesUsingBlock:"
- "getBytes:length:"
- "hasSuffix:"
- "initWithBytes:length:"
- "initWithData:encoding:"
- "initWithLocaleIdentifier:"
- "isEqualToString:"
- "length"
- "mClass"
- "mContentToken"
- "mData"
- "mIdentifier"
- "mReadData"
- "mType"
- "mTypeVersion"
- "mValue"
- "numberWithUnsignedLong:"
- "numberWithUnsignedLongLong:"
- "sandboxReceipt"
- "setDateFormat:"
- "setLocale:"
- "stringValue"
- "stringWithFormat:"
- "subdataWithRange:"
- "v40@?0r^v8{_NSRange=QQ}16^B32"
- "v8@?0"
- "yyyy-MM-dd'T'HH:mm:ssZ"

```
