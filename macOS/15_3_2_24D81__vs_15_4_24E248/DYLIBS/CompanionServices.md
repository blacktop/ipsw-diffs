## CompanionServices

> `/System/Library/PrivateFrameworks/CompanionServices.framework/Versions/A/CompanionServices`

```diff

-156.30.6.0.0
-  __TEXT.__text: 0x8e94
-  __TEXT.__auth_stubs: 0x2b0
-  __TEXT.__objc_methlist: 0xc30
-  __TEXT.__const: 0x132
-  __TEXT.__cstring: 0xe8c
-  __TEXT.__oslogstring: 0x1b3
+156.40.75.0.0
+  __TEXT.__text: 0xb2f0
+  __TEXT.__auth_stubs: 0x4b0
+  __TEXT.__objc_methlist: 0xf04
+  __TEXT.__const: 0x552
+  __TEXT.__cstring: 0x102c
+  __TEXT.__oslogstring: 0x1ef
   __TEXT.__gcc_except_tab: 0x10c
   __TEXT.__dlopen_cstrs: 0x63
-  __TEXT.__constg_swiftt: 0x28
-  __TEXT.__swift5_typeref: 0x6
-  __TEXT.__swift5_fieldmd: 0x10
-  __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x398
+  __TEXT.__swift5_typeref: 0xfa
+  __TEXT.__constg_swiftt: 0xbc
+  __TEXT.__swift5_reflstr: 0x44
+  __TEXT.__swift5_fieldmd: 0xb0
+  __TEXT.__swift5_proto: 0x44
+  __TEXT.__swift5_types: 0x14
+  __TEXT.__unwind_info: 0x488
+  __TEXT.__eh_frame: 0x80
   __TEXT.__objc_classname: 0x364
-  __TEXT.__objc_methname: 0x1d64
-  __TEXT.__objc_methtype: 0x4e9
-  __TEXT.__objc_stubs: 0xb20
-  __DATA_CONST.__got: 0x180
-  __DATA_CONST.__const: 0x2a0
+  __TEXT.__objc_methname: 0x1e0d
+  __TEXT.__objc_methtype: 0x510
+  __TEXT.__objc_stubs: 0xba0
+  __DATA_CONST.__got: 0x1a8
+  __DATA_CONST.__const: 0x2d8
   __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x688
+  __DATA_CONST.__objc_selrefs: 0x778
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x98
-  __AUTH_CONST.__auth_got: 0x168
-  __AUTH_CONST.__const: 0x290
+  __AUTH_CONST.__auth_got: 0x268
+  __AUTH_CONST.__const: 0x440
   __AUTH_CONST.__cfstring: 0xd80
-  __AUTH_CONST.__objc_const: 0x2550
+  __AUTH_CONST.__objc_const: 0x2100
   __AUTH.__objc_data: 0x780
-  __DATA.__objc_ivar: 0xe0
-  __DATA.__data: 0x3c0
-  __DATA.__bss: 0xf8
+  __AUTH.__data: 0x98
+  __DATA.__objc_ivar: 0xe4
+  __DATA.__data: 0x478
+  __DATA.__bss: 0x980
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
+  - /System/Library/PrivateFrameworks/AppIntentsServices.framework/Versions/A/AppIntentsServices
   - /System/Library/PrivateFrameworks/AuthKit.framework/Versions/A/AuthKit
   - /System/Library/PrivateFrameworks/BaseBoard.framework/Versions/A/BaseBoard
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreUtils.framework/Versions/A/CoreUtils
   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
+  - /System/Library/PrivateFrameworks/UserManagement.framework/Versions/A/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
+  - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 277109B4-C197-3927-A128-501E5812042E
-  Functions: 329
-  Symbols:   939
-  CStrings:  719
+  UUID: C9363ECC-F0CC-3308-BDE6-E5701583EBAA
+  Functions: 430
+  Symbols:   1008
+  CStrings:  737
 
Symbols:
+ +[CPSMetrics _sendEvent:withPayloadBuilder:].cold.1
+ -[CPSAppSignInRequest needsShield]
+ -[CPSAuthenticationSession authenticationSessionPresentShieldWithStyle:device:]
+ -[CPSStorePurchaseRequest deviceName]
+ -[CPSStorePurchaseRequest setDeviceName:]
+ ClientSessionLog.cold.1
+ GCC_except_table24
+ GCC_except_table28
+ OBJC_IVAR_$_CPSStorePurchaseRequest._deviceName
+ _OBJC_CLASS_$_UMUserPersona
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ __38-[CPSAuthenticationSession _activated]_block_invoke.19
+ __38-[CPSAuthenticationSession _activated]_block_invoke.19.cold.1
+ ___chkstk_darwin
+ ___swift_destroy_boxed_opaque_existential_1
+ ___swift_instantiateConcreteTypeFromMangledName
+ ___swift_memcpy0_1
+ ___swift_memcpy1_1
+ ___swift_noop_void_return
+ ___swift_project_boxed_opaque_existential_1
+ __swift_FORCE_LOAD_$_swiftCoreAudio
+ __swift_FORCE_LOAD_$_swiftCoreAudio_$_CompanionServices
+ __swift_FORCE_LOAD_$_swiftCoreLocation
+ __swift_FORCE_LOAD_$_swiftCoreLocation_$_CompanionServices
+ __swift_FORCE_LOAD_$_swiftIntents
+ __swift_FORCE_LOAD_$_swiftIntents_$_CompanionServices
+ __swift_FORCE_LOAD_$_swiftOSLog
+ __swift_FORCE_LOAD_$_swiftOSLog_$_CompanionServices
+ _associated conformance 17CompanionServices21ContinueOnRequestTypeO10CodingKeys33_502F6D36DB28526754E6B9097E07CEDBLLOSHAASQ
+ _associated conformance 17CompanionServices21ContinueOnRequestTypeO10CodingKeys33_502F6D36DB28526754E6B9097E07CEDBLLOs0G3KeyAAs23CustomStringConvertible
+ _associated conformance 17CompanionServices21ContinueOnRequestTypeO10CodingKeys33_502F6D36DB28526754E6B9097E07CEDBLLOs0G3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 17CompanionServices21ContinueOnRequestTypeO16EntityCodingKeys33_502F6D36DB28526754E6B9097E07CEDBLLOSHAASQ
+ _associated conformance 17CompanionServices21ContinueOnRequestTypeO16EntityCodingKeys33_502F6D36DB28526754E6B9097E07CEDBLLOs0H3KeyAAs23CustomStringConvertible
+ _associated conformance 17CompanionServices21ContinueOnRequestTypeO16EntityCodingKeys33_502F6D36DB28526754E6B9097E07CEDBLLOs0H3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 17CompanionServices21ContinueOnRequestTypeO21OpensIntentCodingKeys33_502F6D36DB28526754E6B9097E07CEDBLLOSHAASQ
+ _associated conformance 17CompanionServices21ContinueOnRequestTypeO21OpensIntentCodingKeys33_502F6D36DB28526754E6B9097E07CEDBLLOs0I3KeyAAs23CustomStringConvertible
+ _associated conformance 17CompanionServices21ContinueOnRequestTypeO21OpensIntentCodingKeys33_502F6D36DB28526754E6B9097E07CEDBLLOs0I3KeyAAs28CustomDebugStringConvertible
+ _memcpy
+ _objc_msgSend$currentPersona
+ _objc_msgSend$userPersonaNickName
+ _objc_msgSend$userPersonaType
+ _objc_msgSend$userPersonaUniqueString
+ _swift_allocError
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRetain
+ _swift_getEnumCaseMultiPayload
+ _swift_getSingletonMetadata
+ _swift_getTypeByMangledNameInContext2
+ _swift_getWitnessTable
+ _swift_initEnumMetadataMultiPayload
+ _swift_release
+ _swift_retain
+ _swift_storeEnumTagMultiPayload
+ _swift_willThrow
+ _symbolic SS10identifier_SS4typeSS16bundleIdentifiert
+ _symbolic _____ 17CompanionServices21ContinueOnRequestTypeO
+ _symbolic _____ 17CompanionServices21ContinueOnRequestTypeO10CodingKeys33_502F6D36DB28526754E6B9097E07CEDBLLO
+ _symbolic _____ 17CompanionServices21ContinueOnRequestTypeO16EntityCodingKeys33_502F6D36DB28526754E6B9097E07CEDBLLO
+ _symbolic _____ 17CompanionServices21ContinueOnRequestTypeO21OpensIntentCodingKeys33_502F6D36DB28526754E6B9097E07CEDBLLO
+ _symbolic _____ 18AppIntentsServices0A19IntentSpecificationV
+ _symbolic _____y_____G s22KeyedDecodingContainerV 17CompanionServices21ContinueOnRequestTypeO10CodingKeys33_502F6D36DB28526754E6B9097E07CEDBLLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 17CompanionServices21ContinueOnRequestTypeO16EntityCodingKeys33_502F6D36DB28526754E6B9097E07CEDBLLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 17CompanionServices21ContinueOnRequestTypeO21OpensIntentCodingKeys33_502F6D36DB28526754E6B9097E07CEDBLLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 17CompanionServices21ContinueOnRequestTypeO10CodingKeys33_502F6D36DB28526754E6B9097E07CEDBLLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 17CompanionServices21ContinueOnRequestTypeO16EntityCodingKeys33_502F6D36DB28526754E6B9097E07CEDBLLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 17CompanionServices21ContinueOnRequestTypeO21OpensIntentCodingKeys33_502F6D36DB28526754E6B9097E07CEDBLLO
+ _symbolic ypXmT______t s13DecodingErrorO7ContextV
+ cps_daemon_log.cold.1
+ cps_service_connection_log.cold.1
+ cps_service_listener_log.cold.1
+ cps_service_log.cold.1
+ cps_session_log.cold.1
+ cps_signpost_log.cold.1
- -[CPSAuthenticationSession _sessionFailedWithError:].cold.1
- GCC_except_table23
- GCC_except_table27
- __38-[CPSAuthenticationSession _activated]_block_invoke.17
- __38-[CPSAuthenticationSession _activated]_block_invoke.17.cold.1
- __38-[CPSAuthenticationSession _activated]_block_invoke.18.cold.1
CStrings:
+ "-[CPSAuthenticationSession authenticationSessionPresentShieldWithStyle:device:]"
+ "/System/AppleInternal/Library/Frameworks/AppleMediaServices.framework/AppleMediaServices"
+ "/System/AppleInternal/Library/Frameworks/AuthenticationServices.framework/AuthenticationServices"
+ "/System/AppleInternal/Library/Frameworks/PassKitCore.framework/PassKitCore"
+ "Invalid number of keys found, expected one."
+ "T@\"NSString\",&,N,V_deviceName"
+ "activePersona: <ty:%lu, nm:%@, id:%@>"
+ "activePersona: nil"
+ "appleIDAuthorization != ((void*)0)"
+ "authenticationSessionPresentShieldWithStyle:device:"
+ "bundleIdentifier"
+ "currentPersona"
+ "data != ((void*)0)"
+ "needsShield"
+ "password != ((void*)0)"
+ "passwordCredential != ((void*)0)"
+ "user != ((void*)0)"
+ "userPersonaNickName"
+ "userPersonaType"
+ "userPersonaUniqueString"
+ "v32@0:8q16@\"CPSDevice\"24"
+ "v32@0:8q16@24"
- "appleIDAuthorization != ((void *)0)"
- "data != ((void *)0)"
- "password != ((void *)0)"
- "passwordCredential != ((void *)0)"
- "user != ((void *)0)"

```
