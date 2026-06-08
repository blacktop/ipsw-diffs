## HomeServices

> `/System/Library/PrivateFrameworks/HomeServices.framework/HomeServices`

```diff

-422.6.2.0.0
-  __TEXT.__text: 0x78980
-  __TEXT.__auth_stubs: 0x1c10
+471.0.0.0.2
+  __TEXT.__text: 0x8edd0
   __TEXT.__objc_methlist: 0x154
-  __TEXT.__const: 0x5858
-  __TEXT.__constg_swiftt: 0xfcc
-  __TEXT.__swift5_typeref: 0x10d1
-  __TEXT.__swift5_fieldmd: 0x14bc
-  __TEXT.__cstring: 0x190b
-  __TEXT.__swift5_proto: 0x4d8
-  __TEXT.__swift5_types: 0x194
-  __TEXT.__swift5_reflstr: 0xc46
-  __TEXT.__swift5_assocty: 0x258
-  __TEXT.__oslogstring: 0x2301
-  __TEXT.__swift_as_entry: 0x60
-  __TEXT.__swift_as_ret: 0x74
-  __TEXT.__swift5_protos: 0x8
-  __TEXT.__swift5_capture: 0x10
-  __TEXT.__unwind_info: 0x1600
-  __TEXT.__eh_frame: 0x2768
-  __TEXT.__objc_classname: 0x251
-  __TEXT.__objc_methname: 0x7d3
-  __TEXT.__objc_methtype: 0x117
-  __TEXT.__objc_stubs: 0x7c0
-  __DATA_CONST.__got: 0x4a0
-  __DATA_CONST.__const: 0xe0
-  __DATA_CONST.__objc_classlist: 0x60
+  __TEXT.__const: 0x61d0
+  __TEXT.__constg_swiftt: 0x13c8
+  __TEXT.__swift5_typeref: 0x12c3
+  __TEXT.__swift5_fieldmd: 0x16d8
+  __TEXT.__cstring: 0x1b8b
+  __TEXT.__swift5_proto: 0x534
+  __TEXT.__swift5_types: 0x1d8
+  __TEXT.__swift5_reflstr: 0xde6
+  __TEXT.__swift5_assocty: 0x288
+  __TEXT.__oslogstring: 0x25c1
+  __TEXT.__swift_as_entry: 0xb0
+  __TEXT.__swift_as_ret: 0xe4
+  __TEXT.__swift_as_cont: 0x1e4
+  __TEXT.__swift5_protos: 0xc
+  __TEXT.__swift5_capture: 0x48
+  __TEXT.__swift5_builtin: 0x14
+  __TEXT.__swift5_mpenum: 0x8
+  __TEXT.__unwind_info: 0x1b90
+  __TEXT.__eh_frame: 0x3d70
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0xf0
+  __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2b8
+  __DATA_CONST.__objc_selrefs: 0x2c0
   __DATA_CONST.__objc_protorefs: 0x10
-  __AUTH_CONST.__auth_got: 0xe10
-  __AUTH_CONST.__const: 0x4110
-  __AUTH_CONST.__objc_const: 0xcb8
-  __AUTH.__data: 0x490
-  __DATA.__data: 0x998
-  __DATA.__bss: 0x6860
-  __DATA.__common: 0x138
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__const: 0x4718
+  __AUTH_CONST.__objc_const: 0x1058
+  __AUTH_CONST.__auth_got: 0x1040
+  __AUTH.__data: 0x838
+  __DATA.__data: 0xb20
+  __DATA.__bss: 0x6fe0
+  __DATA.__common: 0x188
   __DATA_DIRTY.__objc_data: 0x140
-  __DATA_DIRTY.__data: 0x1550
-  __DATA_DIRTY.__bss: 0x2d00
+  __DATA_DIRTY.__data: 0x1578
+  __DATA_DIRTY.__bss: 0x3100
   __DATA_DIRTY.__common: 0x158
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/CryptoKit.framework/CryptoKit
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/MapKit.framework/MapKit
+  - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount
+  - /System/Library/PrivateFrameworks/DeviceIdentity.framework/DeviceIdentity
   - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
   - /System/Library/PrivateFrameworks/FeedbackLogger.framework/FeedbackLogger
   - /System/Library/PrivateFrameworks/InternalSwiftProtobuf.framework/InternalSwiftProtobuf

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftMapKit.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: D1CE025B-7183-3147-B028-D906B4102413
-  Functions: 1811
-  Symbols:   843
-  CStrings:  457
+  UUID: 7B2FDF8D-DCE9-3929-B77E-580831816051
+  Functions: 2121
+  Symbols:   1025
+  CStrings:  348
 
Symbols:
+ _CFPreferencesGetAppBooleanValue
+ _DeviceIdentityIssueClientCertificateWithCompletion
+ _DeviceIdentityUCRTAttestationSupported
+ _SecAccessControlCreateWithFlags
+ _SecCertificateCopyData
+ _SecItemAdd
+ _SecItemCopyMatching
+ _SecItemDelete
+ _SecItemUpdate
+ _SecKeyCreateSignature
+ __DATA__TtC12HomeServices15KeychainManager
+ __DATA__TtC12HomeServices16AccessKeyManager
+ __DATA__TtC12HomeServices16ManagedBaaValues
+ __DATA__TtC12HomeServices23AccessKeyRequestBuilder
+ __IVARS__TtC12HomeServices15KeychainManager
+ __IVARS__TtC12HomeServices16AccessKeyManager
+ __IVARS__TtC12HomeServices16ManagedBaaValues
+ __IVARS__TtC12HomeServices23AccessKeyRequestBuilder
+ __METACLASS_DATA__TtC12HomeServices15KeychainManager
+ __METACLASS_DATA__TtC12HomeServices16AccessKeyManager
+ __METACLASS_DATA__TtC12HomeServices16ManagedBaaValues
+ __METACLASS_DATA__TtC12HomeServices23AccessKeyRequestBuilder
+ ___swift__destructor
+ ___swift_async_cont_functlets
+ ___swift_closure_destructor
+ ___swift_memcpy112_8
+ ___swift_memcpy6_4
+ ___swift_memcpy8_8
+ ___swift_project_boxed_opaque_existential_0Tm
+ ___unnamed_5
+ __swift_FORCE_LOAD_$_swiftCoreAudio
+ __swift_FORCE_LOAD_$_swiftCoreAudio_$_HomeServices
+ __swift_implicitisolationactor_to_executor_cast
+ _associated conformance 12HomeServices11Attestation33_DC542D6C2C0D9768D03762C8AF6A1619LLV10CodingKeysOSHAASQ
+ _associated conformance 12HomeServices11Attestation33_DC542D6C2C0D9768D03762C8AF6A1619LLV10CodingKeysOs0M3KeyAAs23CustomStringConvertible
+ _associated conformance 12HomeServices11Attestation33_DC542D6C2C0D9768D03762C8AF6A1619LLV10CodingKeysOs0M3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 12HomeServices12AccessKeyDtoV10CodingKeys33_F1A7FAB852757D072E2120138F56AC28LLOSHAASQ
+ _associated conformance 12HomeServices12AccessKeyDtoV10CodingKeys33_F1A7FAB852757D072E2120138F56AC28LLOs0fD0AAs23CustomStringConvertible
+ _associated conformance 12HomeServices12AccessKeyDtoV10CodingKeys33_F1A7FAB852757D072E2120138F56AC28LLOs0fD0AAs28CustomDebugStringConvertible
+ _associated conformance 12HomeServices23AccessKeyRequestBuilderCAA0eF0AA11ResponseDtoAaDP_Se
+ _get_enum_tag_for_layout_string 12HomeServices15BAASigningErrorO
+ _kMAOptionsBAAAccessControls
+ _kMAOptionsBAAKeychainAccessGroup
+ _kMAOptionsBAAKeychainLabel
+ _kMAOptionsBAANetworkTimeoutInterval
+ _kMAOptionsBAAOIDSToInclude
+ _kMAOptionsBAAOIDUCRTDeviceIdentifiers
+ _kMAOptionsBAASCRTAttestation
+ _kMAOptionsBAAValidity
+ _kSecAttrAccessGroup
+ _kSecAttrAccessibleAfterFirstUnlockThisDeviceOnly
+ _kSecAttrAccount
+ _kSecClass
+ _kSecClassGenericPassword
+ _kSecKeyAlgorithmECDSASignatureMessageX962SHA256
+ _kSecMatchLimit
+ _kSecMatchLimitAll
+ _kSecReturnAttributes
+ _kSecReturnData
+ _kSecValueData
+ _objc_msgSend$compressedDataUsingAlgorithm:error:
+ _objc_retain_x21
+ _objc_retain_x25
+ _objc_retain_x27
+ _swift_continuation_await
+ _swift_continuation_init
+ _swift_cvw_enumFn_getEnumTag
+ _swift_deallocBox
+ _swift_defaultActor_deallocate
+ _swift_defaultActor_destroy
+ _swift_defaultActor_initialize
+ _swift_getAssociatedConformanceWitness
+ _swift_getAssociatedTypeWitness
+ _swift_getForeignTypeMetadata
+ _swift_getTupleTypeMetadata2
+ _swift_projectBox
+ _swift_release_x1
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x23
+ _swift_release_x24
+ _swift_release_x25
+ _swift_release_x26
+ _swift_release_x27
+ _swift_release_x28
+ _swift_release_x8
+ _swift_retain_n
+ _swift_retain_x1
+ _swift_retain_x19
+ _swift_retain_x2
+ _swift_retain_x20
+ _swift_retain_x21
+ _swift_retain_x22
+ _swift_retain_x23
+ _swift_retain_x24
+ _swift_retain_x25
+ _swift_task_create
+ _symbolic $s12HomeServices26GuidanceBaseRequestBuilderP
+ _symbolic BD
+ _symbolic SS3key______5valuet 12HomeServices12AccessKeyDtoV
+ _symbolic SS______t 12HomeServices12AccessKeyDtoV
+ _symbolic SaySDySSypGG
+ _symbolic ScA_pSg
+ _symbolic ScCy___________pG 12HomeServices16ManagedBaaValuesC s5ErrorP
+ _symbolic ScPSg
+ _symbolic Scgyyt______pG s5ErrorP
+ _symbolic Se_p
+ _symbolic So12NSURLSessionCSg
+ _symbolic _____ 12HomeServices11Attestation33_DC542D6C2C0D9768D03762C8AF6A1619LLV
+ _symbolic _____ 12HomeServices11Attestation33_DC542D6C2C0D9768D03762C8AF6A1619LLV10CodingKeysO
+ _symbolic _____ 12HomeServices12AccessKeyDtoV
+ _symbolic _____ 12HomeServices12AccessKeyDtoV10CodingKeys33_F1A7FAB852757D072E2120138F56AC28LLO
+ _symbolic _____ 12HomeServices15BAASigningErrorO
+ _symbolic _____ 12HomeServices15KeychainManagerC
+ _symbolic _____ 12HomeServices16AccessKeyManagerC
+ _symbolic _____ 12HomeServices16ManagedBaaValuesC
+ _symbolic _____ 12HomeServices20KeychainManagerErrorO
+ _symbolic _____ 12HomeServices21AccessKeyManagerErrorO
+ _symbolic _____ 12HomeServices23AccessKeyRequestBuilderC
+ _symbolic _____ So9SecKeyRefa
+ _symbolic _____Sg 10Foundation4UUIDV
+ _symbolic _____Sg4code_t s5Int32V
+ _symbolic ______p3sub_t s5ErrorP
+ _symbolic ______pSg15underlyingError_t s5ErrorP
+ _symbolic _____ySDySSypGG s23_ContiguousArrayStorageC
+ _symbolic _____ySS3key______5valuetG s23_ContiguousArrayStorageC 12HomeServices12AccessKeyDtoV
+ _symbolic _____ySS_____G s18_DictionaryStorageC 12HomeServices12AccessKeyDtoV
+ _symbolic _____ySS______tG s23_ContiguousArrayStorageC 12HomeServices12AccessKeyDtoV
+ _symbolic _____y_____G s22KeyedDecodingContainerV 12HomeServices11Attestation33_DC542D6C2C0D9768D03762C8AF6A1619LLV10CodingKeysO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 12HomeServices12AccessKeyDtoV10CodingKeys33_F1A7FAB852757D072E2120138F56AC28LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 12HomeServices11Attestation33_DC542D6C2C0D9768D03762C8AF6A1619LLV10CodingKeysO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 12HomeServices12AccessKeyDtoV10CodingKeys33_F1A7FAB852757D072E2120138F56AC28LLO
+ _symbolic _____y_____GSg s9UnmanagedV So10CFErrorRefa
+ _symbolic _____yc 10Foundation4DateV
+ _symbolic yp
+ _type_layout_string 12HomeServices11Attestation33_DC542D6C2C0D9768D03762C8AF6A1619LLV
+ _type_layout_string 12HomeServices12AccessKeyDtoV
+ _type_layout_string 12HomeServices15BAASigningErrorO
+ _type_layout_string 12HomeServices21AccessKeyManagerErrorO
- ___swift_memcpy96_8
- ___swift_project_boxed_opaque_existential_1Tm
- ___unnamed_6
- __swift_FORCE_LOAD_$_swiftMapKit
- __swift_FORCE_LOAD_$_swiftMapKit_$_HomeServices
- _swift_unknownObjectRelease_n
- _symbolic _____Sg 10Foundation8URLErrorV
- _symbolic ______pSg 10Foundation15ContiguousBytesP
- _symbolic ______ypt s11AnyHashableV
CStrings:
+ "==== Fetching request ===="
+ "==== Fetching request complete ===="
+ "Access key request: BAA disabled Using HMAC."
+ "Attempted to delete an access key that does not exist"
+ "Auth configuration missing. Defaulting to HMAC."
+ "Auth failed."
+ "Auth mode override detected: %s"
+ "Cleaning up failed access key."
+ "Current Device is type is unsupported for this API."
+ "Duplicate values for key: '"
+ "Environment : %s"
+ "Error cleaning up access key: %@"
+ "Error decoding value from keychain: %@"
+ "Error while encoding Cert Chain for BAA. %@"
+ "Error while generating BAA key and certificate %@"
+ "Fatal error"
+ "Swift/NativeDictionary.swift"
+ "Unable to Create Signature: %@"
+ "Unable to Issue Client Certificate. underlying error: %@"
+ "Unable to compute API Path for access key generation"
+ "Unable to create URL with required query parameters."
+ "Unable to create access Control object for BAA %@"
+ "Unable to create access control: "
+ "Unable to create hash of the request body."
+ "Unable to create signature: "
+ "Unable to encode uri as parameter"
+ "Unable to encode wildcard as parameter"
+ "Unable to issue client certificate: "
+ "Unable to remove invalid access key: %@"
+ "Unable to sign request."
+ "User enabled BAA Auth to include Device identifiers"
+ "X-Apple-BaaCertChain"
+ "X-Apple-BaaPayloadHash"
+ "X-Apple-BaaSignatureAndTimestamp"
+ "authDeviceIdentifiersEnabled"
+ "certs"
+ "com.apple.wpc.energyservices.keychain"
+ "com.apple.wpc.utilityservices.baaCertificates-"
+ "com.apple.wpc.utilityservices.baacertgeneration"
+ "energyService.authMode"
+ "fetch(session:providedBuiltRequest:)"
+ "generateBAAKeyAndCertificate()"
- "#16@0:8"
- "$__lazy_storage_$_bitCodeByCharacter"
- "$__lazy_storage_$_characterByBitCode"
- "%s env used for Internal calculation"
- "==== EK Fetching request ===="
- "==== EK Fetching request complete ===="
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "Config Environment : %s"
- "Connected Server Environment : %s"
- "EK Request Failed"
- "HMACAuthInfo"
- "Internal build variant detected. Evaluating Server URL value for Environment information."
- "JSONObjectWithData:options:error:"
- "MKGeoJSONObject"
- "NSObject"
- "Q16@0:8"
- "T#,R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TQ,R"
- "URL %s"
- "URLProtocol:didFailWithError:"
- "URLProtocol:didLoadData:"
- "URLProtocol:didReceiveResponse:cacheStoragePolicy:"
- "URLProtocolDidFinishLoading:"
- "URLsForDirectory:inDomains:"
- "Unable to retrieve server Base URL. Returning default value"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_TtC12HomeServices11TimeService"
- "_TtC12HomeServices12StreamReader"
- "_TtC12HomeServices13HMACConstants"
- "_TtC12HomeServices15GridBaseRequest"
- "_TtC12HomeServices17GridLookupRequest"
- "_TtC12HomeServices19AppleAccountManager"
- "_TtC12HomeServices20EnergyWindowsRequest"
- "_TtC12HomeServices22AutoBugCaptureReporter"
- "_TtC12HomeServices25GridGuidanceSignalRequest"
- "_TtC12HomeServices29GuidanceHistoryRequestBuilder"
- "_TtC12HomeServices30GuidanceForecastRequestBuilder"
- "_TtC12HomeServices7Geohash"
- "aa_personID"
- "aa_primaryAppleAccount"
- "accountStore"
- "allHeaderFields"
- "appendData:"
- "atEof"
- "autorelease"
- "boolValue"
- "buffer"
- "canInitWithRequest:"
- "canonicalRequestForRequest:"
- "characterSetWithBitmapRepresentation:"
- "chunkSize"
- "class"
- "client"
- "closeFile"
- "conformsToProtocol:"
- "coordinate"
- "copy"
- "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
- "currentCalendar"
- "dataWithJSONObject:options:error:"
- "dateFromString:"
- "dealloc"
- "debugDescription"
- "defaultManager"
- "delimData"
- "description"
- "encoding"
- "ephemeralSessionConfiguration"
- "fetch(session:builtRequest:)"
- "fileExistsAtPath:"
- "fileExistsAtPath:isDirectory:"
- "fileHandle"
- "fileHandleForReadingAtPath:"
- "geoJSONObjectsWithData:error:"
- "geometry"
- "gridID"
- "hash"
- "init"
- "initWithCapacity:"
- "initWithLatitude:longitude:"
- "initWithPolygon:"
- "initWithRequest:cachedResponse:client:"
- "initWithURL:statusCode:HTTPVersion:headerFields:"
- "interval"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "lastReportedDate"
- "length"
- "objCType"
- "path"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "pointForMapPoint:"
- "polygons"
- "processInfo"
- "processName"
- "properties"
- "rangeOfData:options:range:"
- "ratePlan"
- "readDataOfLength:"
- "registerClass:"
- "release"
- "removeCharactersInString:"
- "removeItemAtPath:error:"
- "replaceBytesInRange:withBytes:length:"
- "reporter"
- "request"
- "requestId"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "sessionWithConfiguration:"
- "setCalendar:"
- "setDateFormat:"
- "setFormatOptions:"
- "setLength:"
- "setLocale:"
- "setProtocolClasses:"
- "setTimeZone:"
- "sharedSession"
- "signatureWithDomain:type:subType:subtypeContext:detectedProcess:triggerThresholdValues:"
- "snapshotWithSignature:duration:event:payload:reply:"
- "startLoading"
- "statusCode"
- "stopLoading"
- "stringFromDate:"
- "subdataWithRange:"
- "superclass"
- "type"
- "v16@0:8"
- "v16@?0@\"NSDictionary\"8"
- "v8@?0"
- "zone"

```
