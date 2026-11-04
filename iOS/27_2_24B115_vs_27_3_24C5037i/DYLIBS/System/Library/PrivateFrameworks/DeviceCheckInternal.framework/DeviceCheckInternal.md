## DeviceCheckInternal

> `/System/Library/PrivateFrameworks/DeviceCheckInternal.framework/DeviceCheckInternal`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_imageinfo`

```diff

-158.0.0.0.0
-  __TEXT.__text: 0x157b4
-  __TEXT.__objc_methlist: 0x6ec
-  __TEXT.__const: 0x10383
-  __TEXT.__cstring: 0xd12
-  __TEXT.__oslogstring: 0x136e
+162.1.0.0.0
+  __TEXT.__text: 0x22138
+  __TEXT.__objc_methlist: 0x8d4
+  __TEXT.__const: 0x10d73
+  __TEXT.__cstring: 0x10b3
+  __TEXT.__oslogstring: 0x1d33
   __TEXT.__gcc_except_tab: 0x218
-  __TEXT.__unwind_info: 0x528
+  __TEXT.__swift5_typeref: 0x272
+  __TEXT.__constg_swiftt: 0x2fc
+  __TEXT.__swift5_reflstr: 0x191
+  __TEXT.__swift5_fieldmd: 0x2f0
+  __TEXT.__swift5_builtin: 0x28
+  __TEXT.__swift5_mpenum: 0x10
+  __TEXT.__swift5_proto: 0x50
+  __TEXT.__swift5_types: 0x48
+  __TEXT.__swift_as_entry: 0x34
+  __TEXT.__swift_as_ret: 0x38
+  __TEXT.__swift_as_cont: 0x4c
+  __TEXT.__swift5_capture: 0x80
+  __TEXT.__unwind_info: 0x9c0
+  __TEXT.__eh_frame: 0x680
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x4688
-  __DATA_CONST.__objc_classlist: 0x78
+  __DATA_CONST.__const: 0x4738
+  __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x570
-  __DATA_CONST.__objc_superrefs: 0x30
-  __DATA_CONST.__got: 0x150
-  __AUTH_CONST.__const: 0x260
-  __AUTH_CONST.__cfstring: 0x420
-  __AUTH_CONST.__objc_const: 0x1038
-  __AUTH_CONST.__auth_got: 0x490
-  __DATA.__objc_ivar: 0x64
-  __DATA.__data: 0x208
+  __DATA_CONST.__objc_selrefs: 0x698
+  __DATA_CONST.__objc_superrefs: 0x38
+  __DATA_CONST.__got: 0x2a8
+  __AUTH_CONST.__const: 0x8e0
+  __AUTH_CONST.__cfstring: 0x4c0
+  __AUTH_CONST.__objc_const: 0x1530
+  __AUTH_CONST.__auth_got: 0x958
+  __AUTH.__objc_data: 0x400
+  __AUTH.__data: 0x128
+  __DATA.__objc_ivar: 0x70
+  __DATA.__data: 0x350
+  __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x4b0
-  __DATA_DIRTY.__bss: 0xd8
+  __DATA_DIRTY.__bss: 0xe8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CryptoKit.framework/CryptoKit
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Security.framework/Security

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 370
-  Symbols:   1193
-  CStrings:  166
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  Functions: 693
+  Symbols:   1474
+  CStrings:  233
 
Symbols:
+ +[FeatureFlagsManager isExtensionAttestationEnabled]
+ +[FeatureFlagsManager isKeyRotationEnabled]
+ +[FeatureFlagsManager isMacEnabled]
+ +[FeatureFlagsManager isModernizationEnabled]
+ -[DCServerKeyURLsAsset .cxx_destruct]
+ -[DCServerKeyURLsAsset description]
+ -[DCServerKeyURLsAsset initWithFilePath:]
+ -[DCServerKeyURLsAsset productionURL]
+ -[DCServerKeyURLsAsset qaURL]
+ -[DCServerKeyURLsAsset setProductionURL:]
+ -[DCServerKeyURLsAsset setQaURL:]
+ -[DCServerKeyURLsAsset urlForKey:inDictionary:]
+ -[DCServerKeyURLsAsset urlsDictionaryAtFilePath:]
+ -[DCUAFDeviceCheckAsset serverKeyURLsAsset]
+ -[DCUAFDeviceCheckAsset setServerKeyURLsAsset:]
+ _AAInternalLogSystem.log
+ _AAInternalLogSystem.onceToken
+ _OBJC_CLASS_$_DCServerKeyURLsAsset
+ _OBJC_CLASS_$_FeatureFlagsManager
+ _OBJC_CLASS_$_NSHTTPURLResponse
+ _OBJC_CLASS_$_NSLock
+ _OBJC_CLASS_$_NSURLSession
+ _OBJC_CLASS_$_NSURLSessionConfiguration
+ _OBJC_CLASS_$__TtC19DeviceCheckInternal16DCServerKeyStore
+ _OBJC_CLASS_$__TtC19DeviceCheckInternal17DCKeyFetchService
+ _OBJC_CLASS_$__TtC19DeviceCheckInternal17DCServerPublicKey
+ _OBJC_CLASS_$__TtC19DeviceCheckInternal18DCServerKeyRefresh
+ _OBJC_IVAR_$_DCServerKeyURLsAsset._productionURL
+ _OBJC_IVAR_$_DCServerKeyURLsAsset._qaURL
+ _OBJC_IVAR_$_DCUAFDeviceCheckAsset._serverKeyURLsAsset
+ _OBJC_METACLASS_$_DCServerKeyURLsAsset
+ _OBJC_METACLASS_$_FeatureFlagsManager
+ _OBJC_METACLASS_$__TtC19DeviceCheckInternal16DCServerKeyStore
+ _OBJC_METACLASS_$__TtC19DeviceCheckInternal17DCKeyFetchService
+ _OBJC_METACLASS_$__TtC19DeviceCheckInternal17DCServerPublicKey
+ _OBJC_METACLASS_$__TtC19DeviceCheckInternal18DCServerKeyRefresh
+ _SecItemAdd
+ _SecItemCopyMatching
+ _SecItemDelete
+ __Block_copy
+ __Block_release
+ __CLASS_METHODS__TtC19DeviceCheckInternal17DCKeyFetchService
+ __CLASS_METHODS__TtC19DeviceCheckInternal18DCServerKeyRefresh
+ __CLASS_PROPERTIES__TtC19DeviceCheckInternal17DCKeyFetchService
+ __CLASS_PROPERTIES__TtC19DeviceCheckInternal18DCServerKeyRefresh
+ __DATA__TtC19DeviceCheckInternal16DCServerKeyStore
+ __DATA__TtC19DeviceCheckInternal17DCKeyFetchService
+ __DATA__TtC19DeviceCheckInternal17DCServerPublicKey
+ __DATA__TtC19DeviceCheckInternal18DCServerKeyRefresh
+ __INSTANCE_METHODS__TtC19DeviceCheckInternal16DCServerKeyStore
+ __INSTANCE_METHODS__TtC19DeviceCheckInternal17DCKeyFetchService
+ __INSTANCE_METHODS__TtC19DeviceCheckInternal17DCServerPublicKey
+ __INSTANCE_METHODS__TtC19DeviceCheckInternal18DCServerKeyRefresh
+ __IVARS__TtC19DeviceCheckInternal16DCServerKeyStore
+ __IVARS__TtC19DeviceCheckInternal17DCKeyFetchService
+ __IVARS__TtC19DeviceCheckInternal17DCServerPublicKey
+ __IVARS__TtC19DeviceCheckInternal18DCServerKeyRefresh
+ __METACLASS_DATA__TtC19DeviceCheckInternal16DCServerKeyStore
+ __METACLASS_DATA__TtC19DeviceCheckInternal17DCKeyFetchService
+ __METACLASS_DATA__TtC19DeviceCheckInternal17DCServerPublicKey
+ __METACLASS_DATA__TtC19DeviceCheckInternal18DCServerKeyRefresh
+ __OBJC_$_CLASS_METHODS_FeatureFlagsManager
+ __OBJC_$_INSTANCE_METHODS_DCServerKeyURLsAsset
+ __OBJC_$_INSTANCE_VARIABLES_DCServerKeyURLsAsset
+ __OBJC_$_PROP_LIST_DCServerKeyURLsAsset
+ __OBJC_CLASS_RO_$_DCServerKeyURLsAsset
+ __OBJC_CLASS_RO_$_FeatureFlagsManager
+ __OBJC_METACLASS_RO_$_DCServerKeyURLsAsset
+ __OBJC_METACLASS_RO_$_FeatureFlagsManager
+ __PROPERTIES__TtC19DeviceCheckInternal17DCServerPublicKey
+ ___35+[FeatureFlagsManager isMacEnabled]_block_invoke
+ ___43+[FeatureFlagsManager isKeyRotationEnabled]_block_invoke
+ ___45+[FeatureFlagsManager isModernizationEnabled]_block_invoke
+ ___52+[FeatureFlagsManager isExtensionAttestationEnabled]_block_invoke
+ ___AAInternalLogSystem_block_invoke
+ ___block_descriptor_33_e5_v8?0l
+ ___block_descriptor_40_e8_32bs_e5_v8?0ls32l8
+ ___swift_allocate_boxed_opaque_existential_0
+ ___swift_async_cont_functlets
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ ___swift_closure_destructor
+ ___swift_closure_destructor.15Tm
+ ___swift_destroy_boxed_opaque_existential_0
+ ___swift_destroy_boxed_opaque_existential_0Tm
+ ___swift_instantiateConcreteTypeFromMangledNameV2
+ ___swift_memcpy16_8
+ ___swift_memcpy1_1
+ ___swift_memcpy32_8
+ ___swift_memcpy64_8
+ ___swift_memcpy9_8
+ ___swift_noop_void_return
+ ___swift_project_boxed_opaque_existential_1
+ ___swift_project_boxed_opaque_existential_1Tm
+ ___swift_reflection_version
+ __os_feature_enabled_impl
+ __swiftEmptyArrayStorage
+ __swiftEmptyDictionarySingleton
+ __swiftImmortalRefCount
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_DeviceCheckInternal
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftDispatch_$_DeviceCheckInternal
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation_$_DeviceCheckInternal
+ __swift_FORCE_LOAD_$_swiftOSLog
+ __swift_FORCE_LOAD_$_swiftOSLog_$_DeviceCheckInternal
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_DeviceCheckInternal
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftXPC_$_DeviceCheckInternal
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_Builtin_float_$_DeviceCheckInternal
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftos_$_DeviceCheckInternal
+ __swift_stdlib_malloc_size
+ __swift_stdlib_reportUnimplementedInitializer
+ _associated conformance 19DeviceCheckInternal15DCKeyFetchErrorO10Foundation13CustomNSErrorAAs0F0
+ _associated conformance 19DeviceCheckInternal16DCServerKeyStoreC12StoredRecordV10CodingKeys33_537BDB6772B86CC49A1B7719CD10942FLLOSHAASQ
+ _associated conformance 19DeviceCheckInternal16DCServerKeyStoreC12StoredRecordV10CodingKeys33_537BDB6772B86CC49A1B7719CD10942FLLOs0iE0AAs23CustomStringConvertible
+ _associated conformance 19DeviceCheckInternal16DCServerKeyStoreC12StoredRecordV10CodingKeys33_537BDB6772B86CC49A1B7719CD10942FLLOs0iE0AAs28CustomDebugStringConvertible
+ _associated conformance 19DeviceCheckInternal17DCKeyFetchServiceC11KeyResponseV10CodingKeys33_A119271955FA97891C8C37D92FDCD179LLOSHAASQ
+ _associated conformance 19DeviceCheckInternal17DCKeyFetchServiceC11KeyResponseV10CodingKeys33_A119271955FA97891C8C37D92FDCD179LLOs0iG0AAs23CustomStringConvertible
+ _associated conformance 19DeviceCheckInternal17DCKeyFetchServiceC11KeyResponseV10CodingKeys33_A119271955FA97891C8C37D92FDCD179LLOs0iG0AAs28CustomDebugStringConvertible
+ _associated conformance 19DeviceCheckInternal17DCKeyStorageErrorO10Foundation13CustomNSErrorAAs0F0
+ _associated conformance So11CFStringRefa14CoreFoundation9_CFObjectSCSH
+ _associated conformance So11CFStringRefaSHSCSQ
+ _block_copy_helper
+ _block_descriptor
+ _block_destroy_helper
+ _get_enum_tag_for_layout_string 19DeviceCheckInternal15DCKeyFetchErrorO
+ _get_enum_tag_for_layout_string 19DeviceCheckInternal17DCKeyStorageErrorO
+ _isExtensionAttestationEnabled.onceToken
+ _isKeyRotationEnabled.onceToken
+ _isMacEnabled.onceToken
+ _isModernizationEnabled.onceToken
+ _kSecAttrAccessGroup
+ _kSecAttrAccessible
+ _kSecAttrAccessibleAlwaysThisDeviceOnlyPrivate
+ _kSecAttrAccount
+ _kSecAttrGeneric
+ _kSecAttrLabel
+ _kSecAttrService
+ _kSecClass
+ _kSecClassGenericPassword
+ _kSecReturnData
+ _kSecUseDataProtectionKeychain
+ _kSecUseSystemKeychain
+ _kSecValueData
+ _malloc_size
+ _memmove
+ _objc_allocWithZone
+ _objc_opt_self
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x26
+ _objc_retain_x27
+ _objc_retain_x28
+ _swift_allocBox
+ _swift_allocError
+ _swift_allocObject
+ _swift_arrayDestroy
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRelease_n
+ _swift_bridgeObjectRetain
+ _swift_bridgeObjectRetain_n
+ _swift_continuation_await
+ _swift_continuation_init
+ _swift_continuation_throwingResume
+ _swift_continuation_throwingResumeWithError
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_enumFn_getEnumTag
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_deallocObject
+ _swift_deallocPartialClassInstance
+ _swift_dynamicCast
+ _swift_dynamicCastObjCClass
+ _swift_errorRelease
+ _swift_errorRetain
+ _swift_getEnumTagSinglePayloadGeneric
+ _swift_getErrorValue
+ _swift_getForeignTypeMetadata
+ _swift_getObjCClassMetadata
+ _swift_getObjectType
+ _swift_getSingletonMetadata
+ _swift_getTypeByMangledNameInContext2
+ _swift_getWitnessTable
+ _swift_initStackObject
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_isaMask
+ _swift_lookUpClassMethod
+ _swift_once
+ _swift_release
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x25
+ _swift_release_x8
+ _swift_release_x9
+ _swift_retain
+ _swift_retain_x20
+ _swift_retain_x21
+ _swift_retain_x22
+ _swift_retain_x24
+ _swift_retain_x25
+ _swift_setDeallocating
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_storeEnumTagSinglePayloadGeneric
+ _swift_task_alloc
+ _swift_task_create
+ _swift_task_dealloc
+ _swift_task_switch
+ _swift_unknownObjectRelease
+ _swift_unknownObjectRetain
+ _swift_updateClassMetadata2
+ _swift_willThrow
+ _symbolic IeAgH_
+ _symbolic IeghH_
+ _symbolic IeyB_
+ _symbolic SS
+ _symbolic SS_SSt
+ _symbolic SS_ypt
+ _symbolic ScA_pSg
+ _symbolic ScPSg
+ _symbolic ScTyyt_____GSg s5NeverO
+ _symbolic SccySo14DCUAFAssetInfoC______pG s5ErrorP
+ _symbolic Si
+ _symbolic Si10statusCode_t
+ _symbolic Si6length_t
+ _symbolic So6NSLockC
+ _symbolic So8NSObjectC
+ _symbolic _____ 10Foundation4DataV
+ _symbolic _____ 10Foundation4DateV
+ _symbolic _____ 19DeviceCheckInternal15DCKeyFetchErrorO
+ _symbolic _____ 19DeviceCheckInternal15DCKeyFetchErrorO9ConstantsO
+ _symbolic _____ 19DeviceCheckInternal16DCServerKeyStoreC
+ _symbolic _____ 19DeviceCheckInternal16DCServerKeyStoreC12StoredRecordV
+ _symbolic _____ 19DeviceCheckInternal16DCServerKeyStoreC12StoredRecordV10CodingKeys33_537BDB6772B86CC49A1B7719CD10942FLLO
+ _symbolic _____ 19DeviceCheckInternal16DCServerKeyStoreC9ConstantsO
+ _symbolic _____ 19DeviceCheckInternal17DCKeyFetchServiceC
+ _symbolic _____ 19DeviceCheckInternal17DCKeyFetchServiceC11KeyResponseV
+ _symbolic _____ 19DeviceCheckInternal17DCKeyFetchServiceC11KeyResponseV10CodingKeys33_A119271955FA97891C8C37D92FDCD179LLO
+ _symbolic _____ 19DeviceCheckInternal17DCKeyFetchServiceC7ContextV
+ _symbolic _____ 19DeviceCheckInternal17DCKeyFetchServiceC9ConstantsO
+ _symbolic _____ 19DeviceCheckInternal17DCKeyStorageErrorO
+ _symbolic _____ 19DeviceCheckInternal17DCKeyStorageErrorO9ConstantsO
+ _symbolic _____ 19DeviceCheckInternal17DCServerPublicKeyC
+ _symbolic _____ 19DeviceCheckInternal18DCServerKeyRefreshC
+ _symbolic _____ 19DeviceCheckInternal18DCServerKeyRefreshC7ContextV
+ _symbolic _____ 19DeviceCheckInternal18DCServerKeyRefreshC9ConstantsO
+ _symbolic _____ 2os6LoggerV
+ _symbolic _____6prefix_t s5UInt8V
+ _symbolic _____6status_t s5Int32V
+ _symbolic _____Sg 10Foundation3URLV
+ _symbolic ______p s5ErrorP
+ _symbolic ______p10underlying_t s5ErrorP
+ _symbolic ______pSg10underlying_t s5ErrorP
+ _symbolic ______ypt So11CFStringRefa
+ _symbolic _____yS2SG s18_DictionaryStorageC
+ _symbolic _____ySS_yptG s23_ContiguousArrayStorageC
+ _symbolic _____ySSypG s18_DictionaryStorageC
+ _symbolic _____yYaKc 19DeviceCheckInternal17DCServerPublicKeyC
+ _symbolic _____y_____G s22KeyedDecodingContainerV 19DeviceCheckInternal16DCServerKeyStoreC12StoredRecordV10CodingKeys33_537BDB6772B86CC49A1B7719CD10942FLLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 19DeviceCheckInternal17DCKeyFetchServiceC11KeyResponseV10CodingKeys33_A119271955FA97891C8C37D92FDCD179LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 19DeviceCheckInternal16DCServerKeyStoreC12StoredRecordV10CodingKeys33_537BDB6772B86CC49A1B7719CD10942FLLO
+ _symbolic _____y_____G s23_ContiguousArrayStorageC s5UInt8V
+ _symbolic _____y______yptG s23_ContiguousArrayStorageC So11CFStringRefa
+ _symbolic _____y_____ypG s18_DictionaryStorageC So11CFStringRefa
+ _symbolic _____yc 10Foundation4DateV
+ _symbolic ytIeAgHr_
+ _type_layout_string 19DeviceCheckInternal15DCKeyFetchErrorO
+ _type_layout_string 19DeviceCheckInternal17DCKeyFetchServiceC11KeyResponseV
+ _type_layout_string 19DeviceCheckInternal17DCKeyFetchServiceC7ContextV
+ _type_layout_string 19DeviceCheckInternal17DCKeyStorageErrorO
+ _type_layout_string 19DeviceCheckInternal18DCServerKeyRefreshC7ContextV
CStrings:
+ "%25s:%-5d App Attest Extension Support feature flag enabled { enabled=%d }."
+ "%25s:%-5d App Attest Modernization feature flag enabled { enabled=%d }."
+ "%25s:%-5d DeviceCheck Key Rotation feature flag enabled { enabled=%d }."
+ "%25s:%-5d Failed to find Two Bit dictionary in configurations. { filePath=%@ }"
+ "%25s:%-5d Failed to find URL in configurations. { key=%@ }"
+ "%25s:%-5d Failed to find URLs dictionary in configurations. { filePath=%@ }"
+ "%25s:%-5d Failed to parse configurations file. { filePath=%@, error=%@ }"
+ "%25s:%-5d Failed to read configurations file data. { filePath=%@ }"
+ "%25s:%-5d Ignoring malformed URL in configurations. { key=%@, url=%@ }"
+ "%25s:%-5d Mac feature flag enabled { enabled=%d }."
+ "%25s:%-5d No stored server public key, configuring fallback."
+ "%25s:%-5d Using stored server public key. { keyVersion=%@ }"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/TwoBit/DeviceCheckInternal/Source/Core/Mobile Asset/DCServerKeyURLsAsset.m"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/TwoBit/FeatureFlags/FeatureFlagsManager.m"
+ "Applying key fetch URL override. { url=%s }"
+ "Applying local asset override. { filePath=%s }"
+ "DCKeyFetchServiceErrorDomain"
+ "DCKeyFetchServiceStatusCode"
+ "DCServerKeyStoreErrorDomain"
+ "DCServerKeyStoreKeyLength"
+ "DCServerKeyStoreOSStatus"
+ "DCServerKeyStorePointPrefix"
+ "DCServerPublicKey { keyVersion="
+ "DeviceCheck"
+ "DeviceCheckInternal.DCServerPublicKey"
+ "DeviceCheckKeyFetchLastAttempt"
+ "DeviceCheckKeyFetchURLOverride"
+ "Failed to copy server public key. { status=%d }"
+ "Failed to decode key from storage. { error=%s }"
+ "Failed to decode server response. { error=%s }"
+ "Failed to delete server public key. { status=%d }"
+ "Failed to encode key for storage. { error=%s }"
+ "Failed to fetch TwoBit UAF asset. { error=%s }"
+ "Failed to read the stored server public key. { error=%s }"
+ "Failed to refresh the server public key. { error=%s }"
+ "Failed to store server public key. { status=%d }"
+ "Fetched asset. { assetInfo=%s }"
+ "Fetched server public key. { key={ %s } }"
+ "Fetching server public key. { url=%s }"
+ "Ignoring malformed key fetch URL override. { url=%s }"
+ "Key fetch request failed. { error=%s }"
+ "Key fetch response was not an HTTP response."
+ "Key fetch returned an error status. { statusCode=%ld }"
+ "Key fetch returned an unexpected content type. { contentType=%s }"
+ "Keychain returned a server public key item that is not data."
+ "No key fetch endpoint available, the configurations asset could not be fetched."
+ "No key fetch endpoint available, the configurations asset has no Production URL."
+ "No server public key is stored."
+ "Production"
+ "QA"
+ "Refreshed the server public key. { keyVersion=%s }"
+ "Retrieved server public key. { key={ %s } }"
+ "Skipping refresh, a fetch was attempted recently. { elapsed=%lds, floor=%lds }"
+ "Skipping refresh, the stored key is current. { keyAge=%lds, interval=%lds }"
+ "Stored record has an unrecognized version. { version=%ld }"
+ "Stored server public key. { keyVersion=%s, fetchedAt=%s }"
+ "URLs"
+ "aai"
+ "application/json"
+ "com.apple.devicecheck.server-public-key"
+ "extensionAttestation"
+ "https"
+ "init()"
+ "keyRotation"
+ "mac"
+ "modernization"
+ "{ qaURL=%@, productionURL=%@ }"
```
