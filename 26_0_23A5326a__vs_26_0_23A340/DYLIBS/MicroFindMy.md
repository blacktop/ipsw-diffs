## MicroFindMy

> `/System/Library/PrivateFrameworks/MicroFindMy.framework/MicroFindMy`

```diff

 8.30.6.9.16
-  __TEXT.__text: 0x0
-  __TEXT.__const: 0x2
-  __DATA_CONST.__const: 0x38
+  __TEXT.__text: 0x13abc
+  __TEXT.__auth_stubs: 0xae0
+  __TEXT.__const: 0xe3c
+  __TEXT.__constg_swiftt: 0x414
+  __TEXT.__swift5_typeref: 0x31d
+  __TEXT.__swift5_reflstr: 0x4de
+  __TEXT.__swift5_fieldmd: 0x564
+  __TEXT.__swift5_builtin: 0x14
+  __TEXT.__swift5_types: 0x60
+  __TEXT.__swift5_proto: 0xac
+  __TEXT.__cstring: 0xb88
+  __TEXT.__oslogstring: 0x41
+  __TEXT.__swift5_assocty: 0x60
+  __TEXT.__swift5_protos: 0x4
+  __TEXT.__unwind_info: 0x510
+  __TEXT.__eh_frame: 0xd10
+  __TEXT.__objc_methname: 0x1f
+  __DATA_CONST.__got: 0x120
+  __DATA_CONST.__const: 0x70
+  __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_selrefs: 0x8
+  __AUTH_CONST.__auth_got: 0x570
+  __AUTH_CONST.__const: 0xa30
+  __AUTH_CONST.__cfstring: 0x20
+  __AUTH_CONST.__objc_const: 0x220
+  __AUTH.__data: 0x288
+  __DATA.__data: 0x1d8
+  __DATA.__bss: 0x1508
+  __DATA.__common: 0x18
+  __DATA_DIRTY.__data: 0x60
+  __DATA_DIRTY.__bss: 0x80
+  - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
+  - /System/Library/PrivateFrameworks/FindMyBase.framework/FindMyBase
+  - /System/Library/PrivateFrameworks/Tightbeam.framework/Tightbeam
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: B551EF85-3456-31AE-AC9B-580414D89AB8
-  Functions: 0
-  Symbols:   15
-  CStrings:  0
+  UUID: 04C35540-8CF2-3781-8BBA-E6FF01D36230
+  Functions: 392
+  Symbols:   288
+  CStrings:  65
 
Symbols:
+ <redacted>
+ _CFAbsoluteTimeGetCurrent
+ _CFDictionaryCreateMutableCopy
+ _CFDictionarySetValue
+ _CFRelease
+ _CFRunLoopAddSource
+ _CFRunLoopAddTimer
+ _CFRunLoopGetCurrent
+ _CFRunLoopRemoveSource
+ _CFRunLoopRemoveTimer
+ _CFRunLoopRun
+ _CFRunLoopStop
+ _CFRunLoopTimerCreate
+ _CFRunLoopTimerInvalidate
+ _CFStringCreateWithCString
+ _DeviceMatched
+ _IOIteratorNext
+ _IONotificationPortCreate
+ _IONotificationPortDestroy
+ _IONotificationPortGetRunLoopSource
+ _IOObjectRelease
+ _IOServiceAddMatchingNotification
+ _IOServiceMatching
+ _MatchTimeout
+ _MobileGestalt_get_current_device
+ _MobileGestalt_get_deviceSupportsAOP2
+ _MobileGestalt_get_deviceSupportsUltraLowPowerNetworking
+ _OBJC_CLASS_$_NSString
+ _OBJC_CLASS_$__TtCs12_SwiftObject
+ _OBJC_METACLASS_$__TtCs12_SwiftObject
+ __DATA__TtC11MicroFindMy18MicroFindMyService
+ __DATA__TtCC11MicroFindMy18MicroFindMyService6Server
+ __DATA__TtCC11MicroFindMy18MicroFindMyService7Service
+ __IVARS__TtCC11MicroFindMy18MicroFindMyService6Server
+ __IVARS__TtCC11MicroFindMy18MicroFindMyService7Service
+ __METACLASS_DATA__TtC11MicroFindMy18MicroFindMyService
+ __METACLASS_DATA__TtCC11MicroFindMy18MicroFindMyService6Server
+ __METACLASS_DATA__TtCC11MicroFindMy18MicroFindMyService7Service
+ ___CFConstantStringClassReference
+ ___chkstk_darwin
+ ___stack_chk_fail
+ ___stack_chk_guard
+ ___swift_allocate_boxed_opaque_existential_1
+ ___swift_allocate_value_buffer
+ ___swift_destroy_boxed_opaque_existential_0Tm
+ ___swift_destroy_boxed_opaque_existential_1
+ ___swift_instantiateConcreteTypeFromMangledName
+ ___swift_instantiateConcreteTypeFromMangledNameAbstract
+ ___swift_memcpy16_8
+ ___swift_memcpy1_1
+ ___swift_memcpy32_8
+ ___swift_memcpy48_8
+ ___swift_memcpy5_4
+ ___swift_memcpy65_8
+ ___swift_memcpy8_8
+ ___swift_noop_void_return
+ ___swift_project_boxed_opaque_existential_1
+ ___swift_project_value_buffer
+ __objc_empty_cache
+ __os_log_impl
+ __swiftEmptyArrayStorage
+ __swiftEmptyDictionarySingleton
+ __swiftImmortalRefCount
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_NonModularSPI
+ __swift_FORCE_LOAD_$_swiftDispatch_$_NonModularSPI
+ __swift_FORCE_LOAD_$_swiftFoundation_$_NonModularSPI
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_NonModularSPI
+ __swift_FORCE_LOAD_$_swiftXPC_$_NonModularSPI
+ __swift_FORCE_LOAD_$_swift_Builtin_float_$_NonModularSPI
+ __swift_FORCE_LOAD_$_swiftos_$_NonModularSPI
+ __swift_stdlib_malloc_size
+ _associated conformance 11MicroFindMy0abC5ErrorOSHAASQ
+ _associated conformance 11MicroFindMy0abC7ServiceC6ServerC9Tightbeam0D8ProtocolAaF013MessageDecodeG0
+ _associated conformance 11MicroFindMy0abC9InterfaceV13ConfigurationV10CodingKeys33_610EC37B058510B80BBCC364A615A474LLOSHAASQ
+ _associated conformance 11MicroFindMy0abC9InterfaceV13ConfigurationV10CodingKeys33_610EC37B058510B80BBCC364A615A474LLOs0F3KeyAAs23CustomStringConvertible
+ _associated conformance 11MicroFindMy0abC9InterfaceV13ConfigurationV10CodingKeys33_610EC37B058510B80BBCC364A615A474LLOs0F3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 11MicroFindMy0abC9InterfaceV21EndpointConfigurationV10CodingKeys33_610EC37B058510B80BBCC364A615A474LLOSHAASQ
+ _associated conformance 11MicroFindMy0abC9InterfaceV21EndpointConfigurationV10CodingKeys33_610EC37B058510B80BBCC364A615A474LLOs0G3KeyAAs23CustomStringConvertible
+ _associated conformance 11MicroFindMy0abC9InterfaceV21EndpointConfigurationV10CodingKeys33_610EC37B058510B80BBCC364A615A474LLOs0G3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 11MicroFindMy0abC9InterfaceV5ErrorOSHAASQ
+ _associated conformance 11MicroFindMy10IdentifierV10CodingKeys33_E23FC74206C441AA90A967B08908BE69LLOSHAASQ
+ _associated conformance 11MicroFindMy10IdentifierV10CodingKeys33_E23FC74206C441AA90A967B08908BE69LLOs0E3KeyAAs23CustomStringConvertible
+ _associated conformance 11MicroFindMy10IdentifierV10CodingKeys33_E23FC74206C441AA90A967B08908BE69LLOs0E3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 11MicroFindMy16CapabilityBitSetVs06OptionF0AASY
+ _associated conformance 11MicroFindMy16CapabilityBitSetVs06OptionF0AAs0F7Algebra
+ _associated conformance 11MicroFindMy16CapabilityBitSetVs0F7AlgebraAASQ
+ _associated conformance 11MicroFindMy16CapabilityBitSetVs0F7AlgebraAAs25ExpressibleByArrayLiteral
+ _associated conformance 11MicroFindMy8LocationV10CodingKeys33_5217B12A387836664591FE2B9FE9548CLLOSHAASQ
+ _associated conformance 11MicroFindMy8LocationV10CodingKeys33_5217B12A387836664591FE2B9FE9548CLLOs0E3KeyAAs23CustomStringConvertible
+ _associated conformance 11MicroFindMy8LocationV10CodingKeys33_5217B12A387836664591FE2B9FE9548CLLOs0E3KeyAAs28CustomDebugStringConvertible
+ _bzero
+ _free
+ _get_enum_tag_for_layout_string 10Foundation4DataV15_RepresentationO
+ _kCFAllocatorDefault
+ _kCFRunLoopDefaultMode
+ _kIOMainPortDefault
+ _malloc_size
+ _malloc_type_malloc
+ _memcmp
+ _memcpy
+ _memmove
+ _objc_allocWithZone
+ _objc_msgSend
+ _objc_opt_self
+ _objc_release_x20
+ _objc_release_x22
+ _objc_release_x26
+ _objc_release_x8
+ _objc_retainAutoreleasedReturnValue
+ _os_log_type_enabled
+ _pthread_mutex_lock
+ _pthread_mutex_unlock
+ _rpc_afk_interface_find
+ _rpc_afk_interface_find_with_timeout
+ _rpc_get_server_by_name
+ _rpc_get_servers
+ _rpc_is_match
+ _rpc_lock
+ _rpc_malloc
+ _rpc_release_server
+ _rpc_release_server_array
+ _rpc_static_connection_head.0
+ _rpctools_find_interface
+ _snprintf
+ _strcmp
+ _strdup
+ _swift_allocBox
+ _swift_allocError
+ _swift_allocObject
+ _swift_arrayInitWithCopy
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRelease_n
+ _swift_bridgeObjectRetain
+ _swift_bridgeObjectRetain_n
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_deallocClassInstance
+ _swift_deletedMethodError
+ _swift_dynamicCast
+ _swift_errorRelease
+ _swift_errorRetain
+ _swift_getEnumTagSinglePayloadGeneric
+ _swift_getForeignTypeMetadata
+ _swift_getObjectType
+ _swift_getSingletonMetadata
+ _swift_getTypeByMangledNameInContext2
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _swift_getWitnessTable
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_once
+ _swift_release
+ _swift_retain
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_storeEnumTagSinglePayloadGeneric
+ _swift_unknownObjectRelease
+ _swift_unknownObjectRetain
+ _swift_willThrow
+ _swift_willThrowTypedImpl
+ _symbolic $s11MicroFindMy0abC14ServiceHandlerP
+ _symbolic $sSY
+ _symbolic $ss10SetAlgebraP
+ _symbolic $ss25ExpressibleByArrayLiteralP
+ _symbolic $ss9OptionSetP
+ _symbolic SDy__________G 10Foundation4DataV s6UInt64V
+ _symbolic SS
+ _symbolic SaySSG
+ _symbolic Say_____G s4Int8V
+ _symbolic Say_____G s5UInt8V
+ _symbolic Sb
+ _symbolic Sd
+ _symbolic Si
+ _symbolic _____ 10Foundation3URLV
+ _symbolic _____ 10Foundation4DataV
+ _symbolic _____ 11MicroFindMy0abC5ErrorO
+ _symbolic _____ 11MicroFindMy0abC7ServiceC
+ _symbolic _____ 11MicroFindMy0abC7ServiceC0D0C
+ _symbolic _____ 11MicroFindMy0abC7ServiceC6ServerC
+ _symbolic _____ 11MicroFindMy0abC8LocationV
+ _symbolic _____ 11MicroFindMy0abC9InterfaceV
+ _symbolic _____ 11MicroFindMy0abC9InterfaceV13ConfigurationV
+ _symbolic _____ 11MicroFindMy0abC9InterfaceV13ConfigurationV10CodingKeys33_610EC37B058510B80BBCC364A615A474LLO
+ _symbolic _____ 11MicroFindMy0abC9InterfaceV21EndpointConfigurationV
+ _symbolic _____ 11MicroFindMy0abC9InterfaceV21EndpointConfigurationV10CodingKeys33_610EC37B058510B80BBCC364A615A474LLO
+ _symbolic _____ 11MicroFindMy0abC9InterfaceV5ErrorO
+ _symbolic _____ 11MicroFindMy10IdentifierV
+ _symbolic _____ 11MicroFindMy10IdentifierV10CodingKeys33_E23FC74206C441AA90A967B08908BE69LLO
+ _symbolic _____ 11MicroFindMy16CapabilityBitSetV
+ _symbolic _____ 11MicroFindMy17EncryptedLocationV
+ _symbolic _____ 11MicroFindMy21EndpointConfigurationV
+ _symbolic _____ 11MicroFindMy24EncryptedLocationCatalogV
+ _symbolic _____ 11MicroFindMy28EncryptedLocatonCatalogEntryV
+ _symbolic _____ 11MicroFindMy8LocationV
+ _symbolic _____ 11MicroFindMy8LocationV10CodingKeys33_5217B12A387836664591FE2B9FE9548CLLO
+ _symbolic _____ 11MicroFindMy9AnalyticsV
+ _symbolic _____ 13NonModularSPI12rpc_server_tV
+ _symbolic _____ 13NonModularSPI5ErrorO
+ _symbolic _____ 9Tightbeam16ClientConnectionC
+ _symbolic _____ So10tb_error_ta
+ _symbolic _____ s13OpaquePointerV
+ _symbolic _____ s5UInt8V
+ _symbolic _____ s6UInt32V
+ _symbolic _____ s6UInt64V
+ _symbolic _____4code_t s5Int32V
+ _symbolic _____Sg 10Foundation3URLV
+ _symbolic _____Sg 11MicroFindMy0abC7ServiceC0D0C
+ _symbolic _____Sg 11MicroFindMy0abC9InterfaceV21EndpointConfigurationV
+ _symbolic _____Sg 11MicroFindMy21EndpointConfigurationV
+ _symbolic _____Sg 13NonModularSPI12rpc_server_tV
+ _symbolic _____Sg 9Tightbeam0A7EncoderV
+ _symbolic ______p 11MicroFindMy0abC14ServiceHandlerP
+ _symbolic ______p s5ErrorP
+ _symbolic _____ySSG s23_ContiguousArrayStorageC
+ _symbolic _____y_____G 9Tightbeam17ServiceConnectionC 11MicroFindMy0defB0C6ServerC
+ _symbolic _____y_____G s22KeyedDecodingContainerV 11MicroFindMy0deF9InterfaceV13ConfigurationV10CodingKeys33_610EC37B058510B80BBCC364A615A474LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 11MicroFindMy0deF9InterfaceV21EndpointConfigurationV10CodingKeys33_610EC37B058510B80BBCC364A615A474LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 11MicroFindMy10IdentifierV10CodingKeys33_E23FC74206C441AA90A967B08908BE69LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 11MicroFindMy8LocationV10CodingKeys33_5217B12A387836664591FE2B9FE9548CLLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 11MicroFindMy0deF9InterfaceV13ConfigurationV10CodingKeys33_610EC37B058510B80BBCC364A615A474LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 11MicroFindMy0deF9InterfaceV21EndpointConfigurationV10CodingKeys33_610EC37B058510B80BBCC364A615A474LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 11MicroFindMy10IdentifierV10CodingKeys33_E23FC74206C441AA90A967B08908BE69LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 11MicroFindMy8LocationV10CodingKeys33_5217B12A387836664591FE2B9FE9548CLLO
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 11MicroFindMy28EncryptedLocatonCatalogEntryV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC s4Int8V
+ _symbolic _____y_____G s23_ContiguousArrayStorageC s5UInt8V
+ _symbolic _____y__________G s18_DictionaryStorageC 10Foundation4DataV s6UInt64V
+ _symbolic _____yypG s23_ContiguousArrayStorageC
+ _symbolic ypSg
+ _type_layout_string 11MicroFindMy0abC8LocationV
+ _type_layout_string 11MicroFindMy0abC9InterfaceV
+ _type_layout_string 11MicroFindMy0abC9InterfaceV13ConfigurationV
+ _type_layout_string 11MicroFindMy10IdentifierV
+ _type_layout_string 11MicroFindMy16CapabilityBitSetV
+ _type_layout_string 11MicroFindMy17EncryptedLocationV
+ _type_layout_string 11MicroFindMy21EndpointConfigurationV
+ _type_layout_string 11MicroFindMy24EncryptedLocationCatalogV
+ _type_layout_string 11MicroFindMy28EncryptedLocatonCatalogEntryV
+ _type_layout_string 11MicroFindMy8LocationV
+ _type_layout_string 11MicroFindMy9AnalyticsV
+ _type_layout_string 13NonModularSPI12rpc_server_tV
CStrings:
+ "%s-%s-%s"
+ ": incorrect fixed-sized array length, expected 16, got "
+ ": incorrect fixed-sized array length, expected 32, got "
+ ": incorrect fixed-sized array length, expected 57, got "
+ "AFKEndpointInterface"
+ "AFKEndpointInterfaceUserClient"
+ "AOP2 not supported on this platform."
+ "Fatal error"
+ "Foundation/arm64e-apple-ios.private.swiftinterface"
+ "IONameMatch"
+ "IOServiceFirstMatch"
+ "Invalid key value while decoding result type for encryptedLocation"
+ "Invalid key value while decoding result type for encryptedLocationCatalog"
+ "Invalid key value while decoding result type for generatePushPayload"
+ "Invalid key value while decoding result type for setConfiguration"
+ "Invalid key value while decoding result type for setEndpointConfiguration"
+ "Invalid key value while decoding result type for setIdentifier"
+ "Invalid key value while decoding result type for setLocation"
+ "Invalid key value while decoding result type for setPublicKey"
+ "Invalid key value while decoding result type for setPushToken"
+ "Invalid key value while decoding result type for simulateReceivePush"
+ "MicroFindMy/MicroFindMy_swift.swift"
+ "Missing `com.apple.afk.user` entitlement"
+ "RootDomainUserClient"
+ "_TtC11MicroFindMy18MicroFindMyService"
+ "_TtCC11MicroFindMy18MicroFindMyService6Server"
+ "_TtCC11MicroFindMy18MicroFindMyService7Service"
+ "`com.apple.security.iokit-user-client-class` is missing `AFKEndpointInterfaceUserClient`"
+ "`com.apple.security.iokit-user-client-class` is missing `RootDomainUserClient`"
+ "activeDurationInSeconds"
+ "capabilities: %s"
+ "com.apple.afk.user"
+ "com.apple.aop2.MicroFindMy"
+ "com.apple.aop2.MicroFindMy.ap.client"
+ "com.apple.findmy.framework.MicroFindMy"
+ "com.apple.security.iokit-user-client-class"
+ "connectedWatches"
+ "connection"
+ "distanceThresholdInMeters"
+ "encryptedLocation threw an unexpected error type"
+ "encryptedLocation(keyIdentifier:)"
+ "encryptedLocationCatalog threw an unexpected error type"
+ "fwd"
+ "generatePushPayload threw an unexpected error type"
+ "handler"
+ "horizontalAccuracy"
+ "illegal variant selector: "
+ "initWithBytes:length:encoding:"
+ "input of String.init(cString:encoding:) must be null-terminated"
+ "input of String.init(utf8String:) must be null-terminated"
+ "invalid rawValue for CapabilityBitSet: unexpected bits in value, "
+ "invalid rawValue for MicroFindMyService.Selector "
+ "microFindMyLocation: "
+ "minimumTimeBetweenPublishInSeconds"
+ "rev"
+ "setConfiguration threw an unexpected error type"
+ "setEndpointConfiguration threw an unexpected error type"
+ "setIdentifier threw an unexpected error type"
+ "setLocation threw an unexpected error type"
+ "setPublicKey threw an unexpected error type"
+ "setPushToken threw an unexpected error type"
+ "simulateReceivePush threw an unexpected error type"
+ "timeThresholdInSeconds"
+ "useTestInstances"

```
