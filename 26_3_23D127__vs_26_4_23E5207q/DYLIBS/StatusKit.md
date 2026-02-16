## StatusKit

> `/System/Library/PrivateFrameworks/StatusKit.framework/StatusKit`

```diff

-116.400.11.0.0
-  __TEXT.__text: 0x19de4
-  __TEXT.__auth_stubs: 0x500
-  __TEXT.__objc_methlist: 0x1a18
-  __TEXT.__const: 0xa8
-  __TEXT.__gcc_except_tab: 0xbe0
-  __TEXT.__oslogstring: 0x3f4a
-  __TEXT.__cstring: 0xffa
-  __TEXT.__unwind_info: 0x840
-  __TEXT.__objc_classname: 0x3c2
-  __TEXT.__objc_methname: 0x3f4d
-  __TEXT.__objc_methtype: 0xc1d
-  __TEXT.__objc_stubs: 0x1f80
-  __DATA_CONST.__got: 0x140
-  __DATA_CONST.__const: 0x748
-  __DATA_CONST.__objc_classlist: 0xb8
+116.500.122.2.1
+  __TEXT.__text: 0x20c70
+  __TEXT.__auth_stubs: 0x640
+  __TEXT.__objc_methlist: 0x1ff8
+  __TEXT.__const: 0x1a2
+  __TEXT.__gcc_except_tab: 0xec0
+  __TEXT.__oslogstring: 0x4aef
+  __TEXT.__cstring: 0x17d4
+  __TEXT.__swift5_typeref: 0x30
+  __TEXT.__constg_swiftt: 0x7c
+  __TEXT.__swift5_reflstr: 0x22
+  __TEXT.__swift5_fieldmd: 0x50
+  __TEXT.__swift5_proto: 0x8
+  __TEXT.__swift5_types: 0x8
+  __TEXT.__unwind_info: 0xb08
+  __TEXT.__objc_classname: 0x483
+  __TEXT.__objc_methname: 0x4ed3
+  __TEXT.__objc_methtype: 0x1019
+  __TEXT.__objc_stubs: 0x26c0
+  __DATA_CONST.__got: 0x198
+  __DATA_CONST.__const: 0x8c8
+  __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x68
+  __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xbb8
+  __DATA_CONST.__objc_selrefs: 0xe60
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0xb8
-  __DATA_CONST.__objc_arraydata: 0x68
-  __AUTH_CONST.__auth_got: 0x290
-  __AUTH_CONST.__const: 0x320
-  __AUTH_CONST.__cfstring: 0xc00
-  __AUTH_CONST.__objc_const: 0x2790
-  __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x15c
-  __DATA.__data: 0x4e0
-  __DATA_DIRTY.__objc_data: 0x6e0
-  __DATA_DIRTY.__bss: 0x110
+  __DATA_CONST.__objc_superrefs: 0xd8
+  __DATA_CONST.__objc_arraydata: 0xb0
+  __AUTH_CONST.__auth_got: 0x330
+  __AUTH_CONST.__const: 0x340
+  __AUTH_CONST.__cfstring: 0x1000
+  __AUTH_CONST.__objc_const: 0x3168
+  __AUTH_CONST.__objc_dictobj: 0x28
+  __AUTH.__objc_data: 0x208
+  __AUTH.__data: 0xb8
+  __DATA.__objc_ivar: 0x1c4
+  __DATA.__data: 0x558
+  __DATA.__common: 0x8
+  __DATA.__bss: 0x120
+  __DATA_DIRTY.__objc_data: 0x780
+  __DATA_DIRTY.__bss: 0x120
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/IDS.framework/IDS
   - /System/Library/PrivateFrameworks/IDSFoundation.framework/IDSFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 905F4F7A-A4C5-3D11-8432-C0D633F7E3CE
-  Functions: 709
-  Symbols:   2368
-  CStrings:  1133
+  - /usr/lib/swift/libswiftCompression.dylib
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  UUID: 2070005F-C358-3559-B137-6570323B3BC5
+  Functions: 896
+  Symbols:   2992
+  CStrings:  1427
 
Symbols:
+ +[SKFeatureFlagProvider logger]
+ +[SKFeatureFlagProvider logger].cold.1
+ +[SKPresence clientIdentifierPrefixByCodeSigningIdentifier]
+ +[SKPresence clientIdentifierPrefixForServiceIdentifier:]
+ +[SKPresence clientIdentifierPrefixForServiceIdentifier:].cold.1
+ +[SKPresence clientIdentifierPrefixForServiceIdentifier:].cold.2
+ +[SKPresence clientPrefixedPresenceIdentifierForPresenceIdentifier:serviceIdentifier:]
+ +[SKPresenceChannel logger]
+ +[SKPresenceChannel logger].cold.1
+ +[SKPresenceChannel supportsSecureCoding]
+ +[SKPresenceServerRoutablePayload logger]
+ +[SKPresenceServerRoutablePayload logger].cold.1
+ +[SKPresenceServerRoutablePayload supportsSecureCoding]
+ +[SKPresenceValidationToken supportsSecureCoding]
+ +[SKStatusSubscriptionValidationTokenResult supportsSecureCoding]
+ -[NSString(StatusKitAgent) clientIdentifierPrefixFromPresenceIdentifier]
+ -[SKFeatureFlagProvider isFeatureEnabled:]
+ -[SKFeatureFlagProvider isFeatureEnabled:].cold.1
+ -[SKPresence activeChannel]
+ -[SKPresence assertPresenceOnChannel:withPresencePayload:persistentPayload:serverRoutablePayload:assertionOptions:completion:]
+ -[SKPresence assertPresenceOnChannel:withPresencePayload:persistentPayload:serverRoutablePayload:assertionOptions:completion:].cold.1
+ -[SKPresence assertPresenceWithPresencePayload:persistentPayload:assertionOptions:completion:]
+ -[SKPresence assertPresenceWithPresencePayload:persistentPayload:serverRoutablePayload:assertionOptions:completion:]
+ -[SKPresence createChannelWithCompletion:]
+ -[SKPresence devicesChangedForPresenceIdentifier:presentDevices:persistentDevices:completion:]
+ -[SKPresence donateTrustedHandle:completion:]
+ -[SKPresence donateTrustedHandles:completion:]
+ -[SKPresence featureFlagProvider]
+ -[SKPresence initWithPresenceIdentifier:options:listenerEndpoint:featureFlagProvider:]
+ -[SKPresence initWithPresenceIdentifier:options:listenerEndpoint:featureFlagProvider:].cold.1
+ -[SKPresence initWithPresenceIdentifier:options:listenerEndpoint:featureFlagProvider:].cold.2
+ -[SKPresence isActive]
+ -[SKPresence lastDaemonReconnectionTime]
+ -[SKPresence listenerEndpoint]
+ -[SKPresence persistentDevices]
+ -[SKPresence persistentPayload]
+ -[SKPresence presencePayload]
+ -[SKPresence retainTransientSubscriptionAssertionOnChannel:completion:]
+ -[SKPresence retainTransientSubscriptionAssertionOnChannel:completion:].cold.1
+ -[SKPresence rollToChannel:completion:]
+ -[SKPresence rollToChannel:completion:].cold.1
+ -[SKPresence setActiveChannel:]
+ -[SKPresence setFeatureFlagProvider:]
+ -[SKPresence setFilterOverride:completion:]
+ -[SKPresence setLastDaemonReconnectionTime:]
+ -[SKPresence setListenerEndpoint:]
+ -[SKPresence setPersistentPayload:]
+ -[SKPresence setPersistentPayload:completion:]
+ -[SKPresence setPersistentPayloadOnChannel:payload:completion:]
+ -[SKPresence setPresencePayload:]
+ -[SKPresence validateToken:completion:]
+ -[SKPresence validationToken]
+ -[SKPresenceChannel .cxx_destruct]
+ -[SKPresenceChannel cachedDateCreated]
+ -[SKPresenceChannel copyWithZone:]
+ -[SKPresenceChannel data]
+ -[SKPresenceChannel dateCreated]
+ -[SKPresenceChannel dateCreated].cold.1
+ -[SKPresenceChannel dateCreated].cold.2
+ -[SKPresenceChannel dateCreated].cold.3
+ -[SKPresenceChannel description]
+ -[SKPresenceChannel encodeWithCoder:]
+ -[SKPresenceChannel hash]
+ -[SKPresenceChannel initWithCoder:]
+ -[SKPresenceChannel initWithData:]
+ -[SKPresenceChannel isEqual:]
+ -[SKPresenceChannel setCachedDateCreated:]
+ -[SKPresenceDaemonConnection initWithPresenceDaemonDelegate:connectionDelegate:listenerEndpoint:]
+ -[SKPresenceDaemonConnection listenerEndpoint]
+ -[SKPresenceDaemonConnection setListenerEndpoint:]
+ -[SKPresencePayload initWithData:priority:]
+ -[SKPresencePayload initWithData:priority:ttlSeconds:]
+ -[SKPresencePayload priority]
+ -[SKPresencePayload ttlSeconds]
+ -[SKPresencePayload(DictionaryPayloads) initWithDictionary:priority:]
+ -[SKPresencePayload(DictionaryPayloads) initWithDictionary:priority:ttlSeconds:]
+ -[SKPresencePayload(DictionaryPayloads) initWithDictionary:priority:ttlSeconds:].cold.1
+ -[SKPresenceServerRoutablePayload .cxx_destruct]
+ -[SKPresenceServerRoutablePayload description]
+ -[SKPresenceServerRoutablePayload encodeWithCoder:]
+ -[SKPresenceServerRoutablePayload hash]
+ -[SKPresenceServerRoutablePayload initWithCoder:]
+ -[SKPresenceServerRoutablePayload initWithData:routingUUID:payloadKeyData:]
+ -[SKPresenceServerRoutablePayload isEqual:]
+ -[SKPresenceServerRoutablePayload payloadData]
+ -[SKPresenceServerRoutablePayload payloadKeyData]
+ -[SKPresenceServerRoutablePayload routingUUID]
+ -[SKPresenceValidationToken .cxx_destruct]
+ -[SKPresenceValidationToken channelIdentifierToken]
+ -[SKPresenceValidationToken copyWithZone:]
+ -[SKPresenceValidationToken description]
+ -[SKPresenceValidationToken encodeWithCoder:]
+ -[SKPresenceValidationToken hash]
+ -[SKPresenceValidationToken initWithChannelIdentifierToken:serverTime:]
+ -[SKPresenceValidationToken initWithChannelIdentifierToken:serverTime:version:]
+ -[SKPresenceValidationToken initWithCoder:]
+ -[SKPresenceValidationToken isEqual:]
+ -[SKPresenceValidationToken isEqualToPresenceValidationToken:]
+ -[SKPresenceValidationToken serverTime]
+ -[SKPresenceValidationToken version]
+ -[SKPresentDevice initWithHandle:deviceIdentifier:deviceTokenURI:payload:assertionTime:serverOriginatedTime:selfHandle:selfDevice:isPresent:sequenceNumber:]
+ -[SKPresentDevice initWithHandle:deviceIdentifier:deviceTokenURI:payload:assertionTime:serverOriginatedTime:selfHandle:selfDevice:isPresent:sequenceNumber:].cold.1
+ -[SKPresentDevice initWithHandle:deviceIdentifier:deviceTokenURI:payload:assertionTime:serverOriginatedTime:selfHandle:selfDevice:isPresent:sequenceNumber:].cold.2
+ -[SKPresentDevice initWithHandle:deviceIdentifier:deviceTokenURI:payload:assertionTime:serverOriginatedTime:selfHandle:selfDevice:isPresent:sequenceNumber:].cold.3
+ -[SKPresentDevice isPresent]
+ -[SKPresentDevice sequenceNumber]
+ -[SKPresentDevice serverOriginatedTime]
+ -[SKPresentDevice setSequenceNumber:]
+ -[SKStatusPublishingDaemonConnection initWithPublishingDaemonDelegate:connectionDelegate:listenerEndpoint:]
+ -[SKStatusPublishingDaemonConnection listenerEndpoint]
+ -[SKStatusPublishingDaemonConnection setListenerEndpoint:]
+ -[SKStatusPublishingService initWithStatusTypeIdentifier:listenerEndpoint:]
+ -[SKStatusPublishingService listenerEndpoint]
+ -[SKStatusPublishingService setListenerEndpoint:]
+ -[SKStatusSubscriptionDaemonConnection initWithSubscriptionDaemonDelegate:connectionDelegate:listenerEndpoint:]
+ -[SKStatusSubscriptionDaemonConnection listenerEndpoint]
+ -[SKStatusSubscriptionDaemonConnection setListenerEndpoint:]
+ -[SKStatusSubscriptionService initWithStatusTypeIdentifier:listenerEndpoint:]
+ -[SKStatusSubscriptionService listenerEndpoint]
+ -[SKStatusSubscriptionService setListenerEndpoint:]
+ -[SKStatusSubscriptionValidationTokenResult encodeWithCoder:]
+ -[SKStatusSubscriptionValidationTokenResult initInvalidWithUnmatchedField:isExpectedFailure:]
+ -[SKStatusSubscriptionValidationTokenResult initUnknown]
+ -[SKStatusSubscriptionValidationTokenResult initValid]
+ -[SKStatusSubscriptionValidationTokenResult initWithCoder:]
+ -[SKStatusSubscriptionValidationTokenResult isExpectedFailure]
+ -[SKStatusSubscriptionValidationTokenResult unmatchedField]
+ -[SKStatusSubscriptionValidationTokenResult validity]
+ GCC_except_table10
+ GCC_except_table112
+ GCC_except_table117
+ GCC_except_table118
+ GCC_except_table123
+ GCC_except_table126
+ GCC_except_table15
+ GCC_except_table175
+ GCC_except_table18
+ GCC_except_table182
+ GCC_except_table2
+ GCC_except_table21
+ GCC_except_table24
+ GCC_except_table27
+ GCC_except_table28
+ GCC_except_table31
+ GCC_except_table33
+ GCC_except_table34
+ GCC_except_table37
+ GCC_except_table41
+ GCC_except_table44
+ GCC_except_table49
+ GCC_except_table53
+ GCC_except_table61
+ GCC_except_table65
+ GCC_except_table69
+ GCC_except_table72
+ GCC_except_table75
+ GCC_except_table78
+ GCC_except_table8
+ GCC_except_table81
+ GCC_except_table99
+ _$s10Foundation4UUIDV2eeoiySbAC_ACtFZ
+ _$s10Foundation4UUIDV36_unconditionallyBridgeFromObjectiveCyACSo6NSUUIDCSgFZ
+ _$s10Foundation4UUIDVACs23CustomStringConvertibleAAWL
+ _$s10Foundation4UUIDVACs23CustomStringConvertibleAAWl
+ _$s10Foundation4UUIDVMa
+ _$s10Foundation4UUIDVMn
+ _$s10Foundation4UUIDVs23CustomStringConvertibleAAMc
+ _$s9StatusKit14SKDeviceCircleO11descriptionSSvg
+ _$s9StatusKit14SKDeviceCircleO11descriptionSSvpMV
+ _$s9StatusKit14SKDeviceCircleO2eeoiySbAC_ACtFZ
+ _$s9StatusKit14SKDeviceCircleO2eeoiySbAC_ACtFZTf4nnd_n
+ _$s9StatusKit14SKDeviceCircleO4homeyAC10Foundation4UUIDVcACmFWC
+ _$s9StatusKit14SKDeviceCircleO6familyyA2CmFWC
+ _$s9StatusKit14SKDeviceCircleO8personalyA2CmFWC
+ _$s9StatusKit14SKDeviceCircleOMF
+ _$s9StatusKit14SKDeviceCircleOMa
+ _$s9StatusKit14SKDeviceCircleOMaTm
+ _$s9StatusKit14SKDeviceCircleOMf
+ _$s9StatusKit14SKDeviceCircleOMl
+ _$s9StatusKit14SKDeviceCircleOMn
+ _$s9StatusKit14SKDeviceCircleOMr
+ _$s9StatusKit14SKDeviceCircleON
+ _$s9StatusKit14SKDeviceCircleOSQAAMc
+ _$s9StatusKit14SKDeviceCircleOSQAAMcMK
+ _$s9StatusKit14SKDeviceCircleOSQAASQ2eeoiySbx_xtFZTW
+ _$s9StatusKit14SKDeviceCircleOWOc
+ _$s9StatusKit14SKDeviceCircleOWOh
+ _$s9StatusKit14SKDeviceCircleOWV
+ _$s9StatusKit14SKDeviceCircleO_ACtMR
+ _$s9StatusKit14SKDeviceCircleO_ACtMd
+ _$s9StatusKit14SKDeviceCircleOs23CustomStringConvertibleAAMc
+ _$s9StatusKit14SKDeviceCircleOs23CustomStringConvertibleAAMcMK
+ _$s9StatusKit14SKDeviceCircleOs23CustomStringConvertibleAAsADP11descriptionSSvgTW
+ _$s9StatusKit14SKDeviceCircleOwet
+ _$s9StatusKit14SKDeviceCircleOwst
+ _$s9StatusKit14SKDeviceCircleOwup
+ _$s9StatusKit18SKDeviceCircleObjCC04homeD04uuidACXD10Foundation4UUIDV_tFZ
+ _$s9StatusKit18SKDeviceCircleObjCC04homeD04uuidACXD10Foundation4UUIDV_tFZTo
+ _$s9StatusKit18SKDeviceCircleObjCC06deviceD0AA0cD0Ovg
+ _$s9StatusKit18SKDeviceCircleObjCC06deviceD0AA0cD0OvpMV
+ _$s9StatusKit18SKDeviceCircleObjCC06deviceD0AA0cD0OvpWvd
+ _$s9StatusKit18SKDeviceCircleObjCC06deviceD0AcA0cD0O_tcfC
+ _$s9StatusKit18SKDeviceCircleObjCC06deviceD0AcA0cD0O_tcfCTj
+ _$s9StatusKit18SKDeviceCircleObjCC06deviceD0AcA0cD0O_tcfCTq
+ _$s9StatusKit18SKDeviceCircleObjCC06deviceD0AcA0cD0O_tcfc
+ _$s9StatusKit18SKDeviceCircleObjCC06familyD0ACXDyFZ
+ _$s9StatusKit18SKDeviceCircleObjCC06familyD0ACXDyFZTo
+ _$s9StatusKit18SKDeviceCircleObjCC08personalD0ACXDyFZ
+ _$s9StatusKit18SKDeviceCircleObjCC08personalD0ACXDyFZTm
+ _$s9StatusKit18SKDeviceCircleObjCC08personalD0ACXDyFZTo
+ _$s9StatusKit18SKDeviceCircleObjCC08personalD0ACXDyFZToTm
+ _$s9StatusKit18SKDeviceCircleObjCC11descriptionSSvg
+ _$s9StatusKit18SKDeviceCircleObjCC11descriptionSSvgTo
+ _$s9StatusKit18SKDeviceCircleObjCC7isEqualySbypSgF
+ _$s9StatusKit18SKDeviceCircleObjCC7isEqualySbypSgFTo
+ _$s9StatusKit18SKDeviceCircleObjCCACycfC
+ _$s9StatusKit18SKDeviceCircleObjCCACycfc
+ _$s9StatusKit18SKDeviceCircleObjCCACycfcTo
+ _$s9StatusKit18SKDeviceCircleObjCCMF
+ _$s9StatusKit18SKDeviceCircleObjCCMU
+ _$s9StatusKit18SKDeviceCircleObjCCMa
+ _$s9StatusKit18SKDeviceCircleObjCCMf
+ _$s9StatusKit18SKDeviceCircleObjCCMl
+ _$s9StatusKit18SKDeviceCircleObjCCMn
+ _$s9StatusKit18SKDeviceCircleObjCCMo
+ _$s9StatusKit18SKDeviceCircleObjCCMr
+ _$s9StatusKit18SKDeviceCircleObjCCMu
+ _$s9StatusKit18SKDeviceCircleObjCCN
+ _$s9StatusKit18SKDeviceCircleObjCCfD
+ _$s9StatusKit18SKDeviceCircleObjCCfETo
+ _$s9StatusKitMXM
+ _$sBOWV
+ _$sSQ2eeoiySbx_xtFZTq
+ _$sSQMp
+ _$sSS10FoundationE19_bridgeToObjectiveCSo8NSStringCyF
+ _$sSS6appendyySSF
+ _$ss018_bridgeAnyObjectToB0yypyXlSgF
+ _$ss23CustomStringConvertibleMp
+ _$ss23CustomStringConvertibleP11descriptionSSvgTj
+ _$ss23CustomStringConvertibleP11descriptionSSvgTq
+ _$sypN
+ _$sypSgMR
+ _$sypSgMd
+ _$sypSgWOc
+ _$sypSgWOhTm
+ _CFErrorCopyDescription
+ _CFRelease
+ _NSDebugDescriptionErrorKey
+ _OBJC_CLASS_$_NSConstantDictionary
+ _OBJC_CLASS_$_NSDictionary
+ _OBJC_CLASS_$_NSError
+ _OBJC_CLASS_$_NSJSONSerialization
+ _OBJC_CLASS_$_SKDeviceCircleObjC
+ _OBJC_CLASS_$_SKFeatureFlagProvider
+ _OBJC_CLASS_$_SKPresenceChannel
+ _OBJC_CLASS_$_SKPresenceServerRoutablePayload
+ _OBJC_CLASS_$_SKPresenceValidationToken
+ _OBJC_CLASS_$_SKStatusSubscriptionValidationTokenResult
+ _OBJC_IVAR_$_SKPresence._activeChannel
+ _OBJC_IVAR_$_SKPresence._featureFlagProvider
+ _OBJC_IVAR_$_SKPresence._lastDaemonReconnectionTime
+ _OBJC_IVAR_$_SKPresence._listenerEndpoint
+ _OBJC_IVAR_$_SKPresence._persistentPayload
+ _OBJC_IVAR_$_SKPresence._presencePayload
+ _OBJC_IVAR_$_SKPresenceChannel._cachedDateCreated
+ _OBJC_IVAR_$_SKPresenceChannel._data
+ _OBJC_IVAR_$_SKPresenceDaemonConnection._listenerEndpoint
+ _OBJC_IVAR_$_SKPresencePayload._priority
+ _OBJC_IVAR_$_SKPresencePayload._ttlSeconds
+ _OBJC_IVAR_$_SKPresenceServerRoutablePayload._payloadData
+ _OBJC_IVAR_$_SKPresenceServerRoutablePayload._payloadKeyData
+ _OBJC_IVAR_$_SKPresenceServerRoutablePayload._routingUUID
+ _OBJC_IVAR_$_SKPresenceValidationToken._channelIdentifierToken
+ _OBJC_IVAR_$_SKPresenceValidationToken._serverTime
+ _OBJC_IVAR_$_SKPresenceValidationToken._version
+ _OBJC_IVAR_$_SKPresentDevice._isPresent
+ _OBJC_IVAR_$_SKPresentDevice._sequenceNumber
+ _OBJC_IVAR_$_SKPresentDevice._serverOriginatedTime
+ _OBJC_IVAR_$_SKStatusPublishingDaemonConnection._listenerEndpoint
+ _OBJC_IVAR_$_SKStatusPublishingService._listenerEndpoint
+ _OBJC_IVAR_$_SKStatusSubscriptionDaemonConnection._listenerEndpoint
+ _OBJC_IVAR_$_SKStatusSubscriptionService._listenerEndpoint
+ _OBJC_IVAR_$_SKStatusSubscriptionValidationTokenResult._isExpectedFailure
+ _OBJC_IVAR_$_SKStatusSubscriptionValidationTokenResult._unmatchedField
+ _OBJC_IVAR_$_SKStatusSubscriptionValidationTokenResult._validity
+ _OBJC_METACLASS_$_SKDeviceCircleObjC
+ _OBJC_METACLASS_$_SKFeatureFlagProvider
+ _OBJC_METACLASS_$_SKPresenceChannel
+ _OBJC_METACLASS_$_SKPresenceServerRoutablePayload
+ _OBJC_METACLASS_$_SKPresenceValidationToken
+ _OBJC_METACLASS_$_SKStatusSubscriptionValidationTokenResult
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ _SKHelperSHA256StringForData
+ _SecTaskCopySigningIdentifier
+ _SecTaskCreateFromSelf
+ __CLASS_METHODS_SKDeviceCircleObjC
+ __DATA_SKDeviceCircleObjC
+ __INSTANCE_METHODS_SKDeviceCircleObjC
+ __IVARS_SKDeviceCircleObjC
+ __METACLASS_DATA_SKDeviceCircleObjC
+ __OBJC_$_CLASS_METHODS_SKFeatureFlagProvider
+ __OBJC_$_CLASS_METHODS_SKPresenceChannel
+ __OBJC_$_CLASS_METHODS_SKPresenceServerRoutablePayload
+ __OBJC_$_CLASS_METHODS_SKPresenceValidationToken
+ __OBJC_$_CLASS_METHODS_SKStatusSubscriptionValidationTokenResult
+ __OBJC_$_CLASS_PROP_LIST_SKPresenceChannel
+ __OBJC_$_CLASS_PROP_LIST_SKPresenceServerRoutablePayload
+ __OBJC_$_CLASS_PROP_LIST_SKPresenceValidationToken
+ __OBJC_$_CLASS_PROP_LIST_SKStatusSubscriptionValidationTokenResult
+ __OBJC_$_INSTANCE_METHODS_SKFeatureFlagProvider
+ __OBJC_$_INSTANCE_METHODS_SKPresenceChannel
+ __OBJC_$_INSTANCE_METHODS_SKPresenceServerRoutablePayload
+ __OBJC_$_INSTANCE_METHODS_SKPresenceValidationToken
+ __OBJC_$_INSTANCE_METHODS_SKStatusSubscriptionValidationTokenResult
+ __OBJC_$_INSTANCE_VARIABLES_SKPresenceChannel
+ __OBJC_$_INSTANCE_VARIABLES_SKPresenceServerRoutablePayload
+ __OBJC_$_INSTANCE_VARIABLES_SKPresenceValidationToken
+ __OBJC_$_INSTANCE_VARIABLES_SKStatusSubscriptionValidationTokenResult
+ __OBJC_$_PROP_LIST_SKPresenceChannel
+ __OBJC_$_PROP_LIST_SKPresenceServerRoutablePayload
+ __OBJC_$_PROP_LIST_SKPresenceValidationToken
+ __OBJC_$_PROP_LIST_SKStatusSubscriptionValidationTokenResult
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SKFeatureFlagProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SKFeatureFlagProviding
+ __OBJC_CLASS_PROTOCOLS_$_SKFeatureFlagProvider
+ __OBJC_CLASS_PROTOCOLS_$_SKPresenceChannel
+ __OBJC_CLASS_PROTOCOLS_$_SKPresenceServerRoutablePayload
+ __OBJC_CLASS_PROTOCOLS_$_SKPresenceValidationToken
+ __OBJC_CLASS_PROTOCOLS_$_SKStatusSubscriptionValidationTokenResult
+ __OBJC_CLASS_RO_$_SKFeatureFlagProvider
+ __OBJC_CLASS_RO_$_SKPresenceChannel
+ __OBJC_CLASS_RO_$_SKPresenceServerRoutablePayload
+ __OBJC_CLASS_RO_$_SKPresenceValidationToken
+ __OBJC_CLASS_RO_$_SKStatusSubscriptionValidationTokenResult
+ __OBJC_LABEL_PROTOCOL_$_SKFeatureFlagProviding
+ __OBJC_METACLASS_RO_$_SKFeatureFlagProvider
+ __OBJC_METACLASS_RO_$_SKPresenceChannel
+ __OBJC_METACLASS_RO_$_SKPresenceServerRoutablePayload
+ __OBJC_METACLASS_RO_$_SKPresenceValidationToken
+ __OBJC_METACLASS_RO_$_SKStatusSubscriptionValidationTokenResult
+ __OBJC_PROTOCOL_$_SKFeatureFlagProviding
+ __PROPERTIES_SKDeviceCircleObjC
+ ___123-[SKStatusSubscriptionService validatePersonalStatusSubscriptionMatchesSubscriptionValidationTokens:fromSender:completion:]_block_invoke.22
+ ___123-[SKStatusSubscriptionService validatePersonalStatusSubscriptionMatchesSubscriptionValidationTokens:fromSender:completion:]_block_invoke.22.cold.1
+ ___123-[SKStatusSubscriptionService validatePersonalStatusSubscriptionMatchesSubscriptionValidationTokens:fromSender:completion:]_block_invoke.22.cold.2
+ ___123-[SKStatusSubscriptionService validatePersonalStatusSubscriptionMatchesSubscriptionValidationTokens:fromSender:completion:]_block_invoke.22.cold.3
+ ___123-[SKStatusSubscriptionService validatePersonalStatusSubscriptionMatchesSubscriptionValidationTokens:fromSender:completion:]_block_invoke.22.cold.4
+ ___124-[SKStatusSubscriptionService allStatusSubscriptionsWithPersistentSubscriptionAssertionForApplicationIdentifier:completion:]_block_invoke.18
+ ___124-[SKStatusSubscriptionService allStatusSubscriptionsWithPersistentSubscriptionAssertionForApplicationIdentifier:completion:]_block_invoke.18.cold.1
+ ___126-[SKPresence assertPresenceOnChannel:withPresencePayload:persistentPayload:serverRoutablePayload:assertionOptions:completion:]_block_invoke
+ ___126-[SKPresence assertPresenceOnChannel:withPresencePayload:persistentPayload:serverRoutablePayload:assertionOptions:completion:]_block_invoke.108
+ ___126-[SKPresence assertPresenceOnChannel:withPresencePayload:persistentPayload:serverRoutablePayload:assertionOptions:completion:]_block_invoke.108.cold.1
+ ___126-[SKPresence assertPresenceOnChannel:withPresencePayload:persistentPayload:serverRoutablePayload:assertionOptions:completion:]_block_invoke.cold.1
+ ___27+[SKPresenceChannel logger]_block_invoke
+ ___28-[SKPresence invitedHandles]_block_invoke.118
+ ___28-[SKPresence presentDevices]_block_invoke.116
+ ___29-[SKPresence validationToken]_block_invoke
+ ___29-[SKPresence validationToken]_block_invoke.130
+ ___29-[SKPresence validationToken]_block_invoke.cold.1
+ ___31+[SKFeatureFlagProvider logger]_block_invoke
+ ___31-[SKPresence persistentDevices]_block_invoke
+ ___31-[SKPresence persistentDevices]_block_invoke.134
+ ___31-[SKPresence persistentDevices]_block_invoke.cold.1
+ ___38-[SKPresence fetchPresenceCapability:]_block_invoke.136
+ ___39-[SKPresence rollToChannel:completion:]_block_invoke
+ ___39-[SKPresence rollToChannel:completion:]_block_invoke.144
+ ___39-[SKPresence rollToChannel:completion:]_block_invoke.144.cold.1
+ ___39-[SKPresence rollToChannel:completion:]_block_invoke.cold.1
+ ___39-[SKPresence validateToken:completion:]_block_invoke
+ ___39-[SKPresence validateToken:completion:]_block_invoke.132
+ ___39-[SKPresence validateToken:completion:]_block_invoke.132.cold.1
+ ___39-[SKPresence validateToken:completion:]_block_invoke.cold.1
+ ___40-[SKPresence rollChannelWithCompletion:]_block_invoke.129
+ ___40-[SKPresence rollChannelWithCompletion:]_block_invoke.129.cold.1
+ ___41+[SKPresenceServerRoutablePayload logger]_block_invoke
+ ___42-[SKPresence _attemptReconnectingToDaemon]_block_invoke_5
+ ___42-[SKPresence createChannelWithCompletion:]_block_invoke
+ ___42-[SKPresence createChannelWithCompletion:]_block_invoke.139
+ ___42-[SKPresence createChannelWithCompletion:]_block_invoke.139.cold.1
+ ___42-[SKPresence createChannelWithCompletion:]_block_invoke.cold.1
+ ___43-[SKPresence setFilterOverride:completion:]_block_invoke
+ ___43-[SKPresence setFilterOverride:completion:]_block_invoke.110
+ ___43-[SKPresence setFilterOverride:completion:]_block_invoke.110.cold.1
+ ___43-[SKPresence setFilterOverride:completion:]_block_invoke.cold.1
+ ___43-[SKPresenceDaemonConnection xpcConnection]_block_invoke.9
+ ___44-[SKPresence releasePresenceWithCompletion:]_block_invoke.109
+ ___44-[SKPresence releasePresenceWithCompletion:]_block_invoke.109.cold.1
+ ___46-[SKPresence donateTrustedHandles:completion:]_block_invoke
+ ___46-[SKPresence donateTrustedHandles:completion:]_block_invoke.128
+ ___46-[SKPresence donateTrustedHandles:completion:]_block_invoke.128.cold.1
+ ___46-[SKPresence donateTrustedHandles:completion:]_block_invoke.cold.1
+ ___46-[SKPresence removeInvitedHandles:completion:]_block_invoke.127
+ ___46-[SKPresence removeInvitedHandles:completion:]_block_invoke.127.cold.1
+ ___48-[SKPresence _isHandleInvited:fromSenderHandle:]_block_invoke.119
+ ___51-[SKStatusPublishingDaemonConnection xpcConnection]_block_invoke.9
+ ___53-[SKStatusSubscriptionDaemonConnection xpcConnection]_block_invoke.9
+ ___54-[SKPresence _registerForDelegateCallbacksIfNecessary]_block_invoke.145
+ ___54-[SKPresence _registerForDelegateCallbacksIfNecessary]_block_invoke.145.cold.1
+ ___57-[SKPresence _inviteHandles:fromSenderHandle:completion:]_block_invoke.126
+ ___57-[SKPresence _inviteHandles:fromSenderHandle:completion:]_block_invoke.126.cold.1
+ ___57-[SKStatusSubscriptionService personalStatusSubscription]_block_invoke.11
+ ___57-[SKStatusSubscriptionService personalStatusSubscription]_block_invoke.11.cold.1
+ ___58-[SKPresence initialCloudKitImportReceivedWithCompletion:]_block_invoke.164
+ ___59-[SKPresence _isHandleInvited:fromSenderHandle:completion:]_block_invoke.121
+ ___59-[SKStatusSubscriptionService statusSubscriptionForHandle:]_block_invoke.7
+ ___59-[SKStatusSubscriptionService statusSubscriptionForHandle:]_block_invoke.7.cold.1
+ ___61-[SKPresence hasInitialCloudKitImportOccurredWithCompletion:]_block_invoke.91
+ ___61-[SKPresence hasInitialCloudKitImportOccurredWithCompletion:]_block_invoke.91.cold.1
+ ___63-[SKPresence setPersistentPayloadOnChannel:payload:completion:]_block_invoke
+ ___63-[SKPresence setPersistentPayloadOnChannel:payload:completion:]_block_invoke.135
+ ___63-[SKPresence setPersistentPayloadOnChannel:payload:completion:]_block_invoke.135.cold.1
+ ___63-[SKPresence setPersistentPayloadOnChannel:payload:completion:]_block_invoke.cold.1
+ ___66-[SKPresence releaseTransientSubscriptionAssertionWithCompletion:]_block_invoke.115
+ ___66-[SKPresence releaseTransientSubscriptionAssertionWithCompletion:]_block_invoke.115.cold.1
+ ___67-[SKPresence _fetchHandleInvitability:fromSenderHandle:completion:]_block_invoke.123
+ ___68-[SKPresence invitedHandlesChangedForPresenceIdentifier:completion:]_block_invoke.159
+ ___70-[SKStatusSubscriptionService statusSubscriptionForHandle:completion:]_block_invoke.10
+ ___70-[SKStatusSubscriptionService statusSubscriptionForHandle:completion:]_block_invoke.10.cold.1
+ ___71-[SKPresence retainTransientSubscriptionAssertionOnChannel:completion:]_block_invoke
+ ___71-[SKPresence retainTransientSubscriptionAssertionOnChannel:completion:]_block_invoke.114
+ ___71-[SKPresence retainTransientSubscriptionAssertionOnChannel:completion:]_block_invoke.114.cold.1
+ ___71-[SKPresence retainTransientSubscriptionAssertionOnChannel:completion:]_block_invoke.cold.1
+ ___71-[SKStatusSubscriptionService _registerForDelegateCallbacksIfNecessary]_block_invoke.25
+ ___71-[SKStatusSubscriptionService _registerForDelegateCallbacksIfNecessary]_block_invoke.25.cold.1
+ ___72-[SKStatusSubscriptionService personalStatusSubscriptionWithCompletion:]_block_invoke.12
+ ___72-[SKStatusSubscriptionService personalStatusSubscriptionWithCompletion:]_block_invoke.12.cold.1
+ ___73-[SKStatusSubscriptionService allStatusSubscriptionsWithActiveAssertions]_block_invoke.13
+ ___73-[SKStatusSubscriptionService allStatusSubscriptionsWithActiveAssertions]_block_invoke.13.cold.1
+ ___73-[SKStatusSubscriptionService allStatusSubscriptionsWithActiveAssertions]_block_invoke.13.cold.2
+ ___73-[SKStatusSubscriptionService subscriptionInvitationReceived:completion:]_block_invoke.40
+ ___75-[SKStatusSubscriptionService subscriptionReceivedStatusUpdate:completion:]_block_invoke.37
+ ___75-[SKStatusSubscriptionService subscriptionValidationTokensForHandle:error:]_block_invoke.19
+ ___75-[SKStatusSubscriptionService subscriptionValidationTokensForHandle:error:]_block_invoke.19.cold.1
+ ___75-[SKStatusSubscriptionService subscriptionValidationTokensForHandle:error:]_block_invoke.19.cold.2
+ ___76-[SKStatusSubscriptionService allStatusSubscriptionsWithActiveSubscriptions]_block_invoke.16
+ ___76-[SKStatusSubscriptionService allStatusSubscriptionsWithActiveSubscriptions]_block_invoke.16.cold.1
+ ___76-[SKStatusSubscriptionService allStatusSubscriptionsWithActiveSubscriptions]_block_invoke.16.cold.2
+ ___80-[SKStatusSubscriptionService subscriptionValidationTokensForHandle:completion:]_block_invoke.21
+ ___80-[SKStatusSubscriptionService subscriptionValidationTokensForHandle:completion:]_block_invoke.21.cold.1
+ ___80-[SKStatusSubscriptionService subscriptionValidationTokensForHandle:completion:]_block_invoke.21.cold.2
+ ___83-[SKStatusSubscriptionService subscriptionStateChangedForSubscriptions:completion:]_block_invoke.33
+ ___84-[SKStatusSubscriptionService _allStatusSubscriptionsIncludingPersonalSubscription:]_block_invoke.17
+ ___84-[SKStatusSubscriptionService _allStatusSubscriptionsIncludingPersonalSubscription:]_block_invoke.17.cold.1
+ ___84-[SKStatusSubscriptionService _allStatusSubscriptionsIncludingPersonalSubscription:]_block_invoke.17.cold.2
+ ___94-[SKPresence devicesChangedForPresenceIdentifier:presentDevices:persistentDevices:completion:]_block_invoke
+ ___94-[SKPresence devicesChangedForPresenceIdentifier:presentDevices:persistentDevices:completion:]_block_invoke.156
+ ___94-[SKPresence devicesChangedForPresenceIdentifier:presentDevices:persistentDevices:completion:]_block_invoke.cold.1
+ ___94-[SKPresence devicesChangedForPresenceIdentifier:presentDevices:persistentDevices:completion:]_block_invoke.cold.2
+ ___block_descriptor_48_e8_32bs40w_e20_v24?0q8"NSError"16lw40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e39_v24?0"SKPresenceChannel"8"NSError"16ls40l8s32l8
+ ___block_descriptor_48_e8_32s40r_e47_v24?0"SKPresenceValidationToken"8"NSError"16ls32l8r40l8
+ ___block_descriptor_48_e8_32s40w_e5_v8?0ls32l8w40l8
+ ___block_descriptor_56_e8_32s40s48s_e30_v16?0"<SKPresenceDelegate>"8ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48bs56w_e63_v24?0"SKStatusSubscriptionValidationTokenResult"8"NSError"16lw56l8s32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e17_v16?0"NSError"8ls56l8s32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56bs64w_e17_v16?0"NSError"8ls56l8s32l8s40l8w64l8s48l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72bs80w_e17_v16?0"NSError"8ls32l8w80l8s40l8s48l8s56l8s64l8s72l8
+ ___block_literal_global.167
+ ___block_literal_global.169
+ ___block_literal_global.171
+ ___block_literal_global.175
+ ___chkstk_darwin
+ ___swift_instantiateConcreteTypeFromMangledNameV2
+ ___swift_reflection_version
+ __swift_FORCE_LOAD_$_swiftCompression
+ __swift_FORCE_LOAD_$_swiftCompression_$_StatusKit
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_StatusKit
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftDispatch_$_StatusKit
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation_$_StatusKit
+ __swift_FORCE_LOAD_$_swiftOSLog
+ __swift_FORCE_LOAD_$_swiftOSLog_$_StatusKit
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_StatusKit
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftXPC_$_StatusKit
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_Builtin_float_$_StatusKit
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftos_$_StatusKit
+ __swift_stdlib_reportUnimplementedInitializer
+ _kCFAllocatorDefault
+ _objc_allocWithZone
+ _objc_msgSend$JSONObjectWithData:options:error:
+ _objc_msgSend$activeChannel
+ _objc_msgSend$appendString:
+ _objc_msgSend$assertPresenceForIdentifier:onChannel:withPresencePayload:persistentPayload:serverRoutablePayload:assertionOptions:completion:
+ _objc_msgSend$assertPresenceOnChannel:withPresencePayload:persistentPayload:serverRoutablePayload:assertionOptions:completion:
+ _objc_msgSend$assertPresenceWithPresencePayload:persistentPayload:assertionOptions:completion:
+ _objc_msgSend$assertPresenceWithPresencePayload:persistentPayload:serverRoutablePayload:assertionOptions:completion:
+ _objc_msgSend$boolValue
+ _objc_msgSend$channelIdentifierToken
+ _objc_msgSend$clientIdentifierPrefixByCodeSigningIdentifier
+ _objc_msgSend$clientIdentifierPrefixForServiceIdentifier:
+ _objc_msgSend$clientPrefixedPresenceIdentifierForPresenceIdentifier:serviceIdentifier:
+ _objc_msgSend$createChannelWithCompletion:
+ _objc_msgSend$data
+ _objc_msgSend$dateByAddingTimeInterval:
+ _objc_msgSend$dateWithTimeIntervalSinceReferenceDate:
+ _objc_msgSend$decodeDoubleForKey:
+ _objc_msgSend$decodeIntegerForKey:
+ _objc_msgSend$dictionaryWithObjects:forKeys:count:
+ _objc_msgSend$donateTrustedHandles:completion:
+ _objc_msgSend$donateTrustedHandles:presenceIdentifier:completion:
+ _objc_msgSend$doubleValue
+ _objc_msgSend$encodeDouble:forKey:
+ _objc_msgSend$encodeInteger:forKey:
+ _objc_msgSend$errorWithDomain:code:userInfo:
+ _objc_msgSend$featureFlagProvider
+ _objc_msgSend$hasSuffix:
+ _objc_msgSend$initWithChannelIdentifierToken:serverTime:version:
+ _objc_msgSend$initWithData:priority:
+ _objc_msgSend$initWithData:priority:ttlSeconds:
+ _objc_msgSend$initWithData:routingUUID:payloadKeyData:
+ _objc_msgSend$initWithDictionary:priority:
+ _objc_msgSend$initWithDictionary:priority:ttlSeconds:
+ _objc_msgSend$initWithListenerEndpoint:
+ _objc_msgSend$initWithPresenceDaemonDelegate:connectionDelegate:listenerEndpoint:
+ _objc_msgSend$initWithPresenceIdentifier:options:listenerEndpoint:featureFlagProvider:
+ _objc_msgSend$initWithPublishingDaemonDelegate:connectionDelegate:listenerEndpoint:
+ _objc_msgSend$initWithStatusTypeIdentifier:listenerEndpoint:
+ _objc_msgSend$initWithSubscriptionDaemonDelegate:connectionDelegate:listenerEndpoint:
+ _objc_msgSend$isActive
+ _objc_msgSend$isEqualToDate:
+ _objc_msgSend$isEqualToPresenceValidationToken:
+ _objc_msgSend$isFeatureEnabled:
+ _objc_msgSend$isPresent
+ _objc_msgSend$mutableCopy
+ _objc_msgSend$now
+ _objc_msgSend$objectForKeyedSubscript:
+ _objc_msgSend$payloadKeyData
+ _objc_msgSend$persistentDevicesForPresenceIdentifier:onChannel:completion:
+ _objc_msgSend$persistentPayload
+ _objc_msgSend$presence:persistentDevicesChanged:
+ _objc_msgSend$presence:presentDevicesChanged:
+ _objc_msgSend$presenceAssertionOptions
+ _objc_msgSend$presentDevicesForPresenceIdentifier:onChannel:completion:
+ _objc_msgSend$retainTransientSubscriptionAssertionForPresenceIdentifier:onChannel:completion:
+ _objc_msgSend$retainTransientSubscriptionAssertionOnChannel:completion:
+ _objc_msgSend$rollChannelFromChannel:toChannel:completion:
+ _objc_msgSend$routingUUID
+ _objc_msgSend$serverOriginatedTime
+ _objc_msgSend$serverTime
+ _objc_msgSend$setActiveChannel:
+ _objc_msgSend$setFilterOverride:onChannel:presenceIdentifier:completion:
+ _objc_msgSend$setPersistentPayload:
+ _objc_msgSend$setPersistentPayload:onChannel:presenceIdentifier:completion:
+ _objc_msgSend$setPersistentPayloadOnChannel:payload:completion:
+ _objc_msgSend$setPresencePayload:
+ _objc_msgSend$timeIntervalSinceDate:
+ _objc_msgSend$ttlSeconds
+ _objc_msgSend$validateToken:presenceIdentifier:completion:
+ _objc_msgSend$validationTokenForPresenceIdentifier:completion:
+ _objc_msgSend$validity
+ _objc_msgSend$version
+ _os_variant_allows_internal_security_policies
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRetain
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initEnumMetadataSinglePayloadWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_cvw_singlePayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_cvw_singlePayloadEnumGeneric_getEnumTag
+ _swift_dynamicCast
+ _swift_getEnumTagSinglePayloadGeneric
+ _swift_getObjCClassMetadata
+ _swift_getObjectType
+ _swift_getSingletonMetadata
+ _swift_getTypeByMangledNameInContext2
+ _swift_getWitnessTable
+ _swift_lookUpClassMethod
+ _swift_storeEnumTagSinglePayloadGeneric
+ _swift_unknownObjectRelease
+ _swift_unknownObjectRetain
+ _swift_updateClassMetadata2
+ _symbolic So8NSObjectC
+ _symbolic _____ 10Foundation4UUIDV
+ _symbolic _____ 9StatusKit14SKDeviceCircleO
+ _symbolic _____ 9StatusKit18SKDeviceCircleObjCC
+ _symbolic ______AAt 9StatusKit14SKDeviceCircleO
+ _symbolic ypSg
- +[SKPresence clientID]
- +[SKPresence clientPrefixedPresenceIdentifierForPresenceIdentifier:]
- -[NSString(StatusKitAgent) clientIDFromPresenceIdentifier]
- -[SKPresence initWithPresenceIdentifier:options:].cold.1
- -[SKPresence initWithPresenceIdentifier:options:].cold.2
- -[SKPresence payload]
- -[SKPresence presentHandlesChangedForPresenceIdentifier:completion:]
- -[SKPresence setPayload:]
- -[SKPresenceDaemonConnection setXPCConnection:]
- -[SKPresenceDaemonConnection setXpcConnection:]
- -[SKPresencePayload(DictionaryPayloads) initWithDictionary:].cold.1
- -[SKPresentDevice initWithHandle:deviceIdentifier:deviceTokenURI:payload:assertionTime:selfHandle:selfDevice:]
- -[SKPresentDevice initWithHandle:deviceIdentifier:deviceTokenURI:payload:assertionTime:selfHandle:selfDevice:].cold.1
- -[SKPresentDevice initWithHandle:deviceIdentifier:deviceTokenURI:payload:assertionTime:selfHandle:selfDevice:].cold.2
- -[SKPresentDevice initWithHandle:deviceIdentifier:deviceTokenURI:payload:assertionTime:selfHandle:selfDevice:].cold.3
- -[SKStatusPublishingDaemonConnection setXPCConnection:]
- -[SKStatusPublishingDaemonConnection setXpcConnection:]
- -[SKStatusSubscriptionDaemonConnection setXPCConnection:]
- -[SKStatusSubscriptionDaemonConnection setXpcConnection:]
- GCC_except_table1
- GCC_except_table12
- GCC_except_table14
- GCC_except_table16
- GCC_except_table17
- GCC_except_table19
- GCC_except_table20
- GCC_except_table22
- GCC_except_table23
- GCC_except_table25
- GCC_except_table26
- GCC_except_table29
- GCC_except_table32
- GCC_except_table35
- GCC_except_table38
- GCC_except_table4
- GCC_except_table43
- GCC_except_table46
- GCC_except_table52
- GCC_except_table55
- GCC_except_table59
- GCC_except_table67
- GCC_except_table80
- GCC_except_table9
- GCC_except_table90
- GCC_except_table93
- _OBJC_CLASS_$_NSConstantArray
- _OBJC_IVAR_$_SKPresence._payload
- _ValidateClientIsInAllowlistForServiceName
- _ValidateClientIsInAllowlistForServiceName.cold.1
- _ValidateClientIsInAllowlistForServiceName.cold.2
- _ValidateClientIsInAllowlistForServiceName.cold.3
- _ValidateClientIsInAllowlistForServiceName.presenceClients
- _ValidateClientIsInAllowlistForServiceName.presenceClientsToken
- _ValidateClientIsInAllowlistForServiceName.statusClients
- _ValidateClientIsInAllowlistForServiceName.statusClientsToken
- ___123-[SKStatusSubscriptionService validatePersonalStatusSubscriptionMatchesSubscriptionValidationTokens:fromSender:completion:]_block_invoke.19
- ___123-[SKStatusSubscriptionService validatePersonalStatusSubscriptionMatchesSubscriptionValidationTokens:fromSender:completion:]_block_invoke.19.cold.1
- ___123-[SKStatusSubscriptionService validatePersonalStatusSubscriptionMatchesSubscriptionValidationTokens:fromSender:completion:]_block_invoke.19.cold.2
- ___123-[SKStatusSubscriptionService validatePersonalStatusSubscriptionMatchesSubscriptionValidationTokens:fromSender:completion:]_block_invoke.19.cold.3
- ___123-[SKStatusSubscriptionService validatePersonalStatusSubscriptionMatchesSubscriptionValidationTokens:fromSender:completion:]_block_invoke.19.cold.4
- ___124-[SKStatusSubscriptionService allStatusSubscriptionsWithPersistentSubscriptionAssertionForApplicationIdentifier:completion:]_block_invoke.15
- ___124-[SKStatusSubscriptionService allStatusSubscriptionsWithPersistentSubscriptionAssertionForApplicationIdentifier:completion:]_block_invoke.15.cold.1
- ___28-[SKPresence invitedHandles]_block_invoke.45
- ___28-[SKPresence presentDevices]_block_invoke.43
- ___38-[SKPresence fetchPresenceCapability:]_block_invoke.56
- ___40-[SKPresence rollChannelWithCompletion:]_block_invoke.55
- ___40-[SKPresence rollChannelWithCompletion:]_block_invoke.55.cold.1
- ___43-[SKPresenceDaemonConnection xpcConnection]_block_invoke.7
- ___44-[SKPresence releasePresenceWithCompletion:]_block_invoke.40
- ___44-[SKPresence releasePresenceWithCompletion:]_block_invoke.40.cold.1
- ___46-[SKPresence removeInvitedHandles:completion:]_block_invoke.54
- ___46-[SKPresence removeInvitedHandles:completion:]_block_invoke.54.cold.1
- ___48-[SKPresence _isHandleInvited:fromSenderHandle:]_block_invoke.46
- ___51-[SKStatusPublishingDaemonConnection xpcConnection]_block_invoke.7
- ___53-[SKStatusSubscriptionDaemonConnection xpcConnection]_block_invoke.7
- ___54-[SKPresence _registerForDelegateCallbacksIfNecessary]_block_invoke.59
- ___54-[SKPresence _registerForDelegateCallbacksIfNecessary]_block_invoke.59.cold.1
- ___57-[SKPresence _inviteHandles:fromSenderHandle:completion:]_block_invoke.53
- ___57-[SKPresence _inviteHandles:fromSenderHandle:completion:]_block_invoke.53.cold.1
- ___57-[SKStatusSubscriptionService personalStatusSubscription]_block_invoke.8
- ___57-[SKStatusSubscriptionService personalStatusSubscription]_block_invoke.8.cold.1
- ___58-[SKPresence initialCloudKitImportReceivedWithCompletion:]_block_invoke.74
- ___59-[SKPresence _isHandleInvited:fromSenderHandle:completion:]_block_invoke.48
- ___59-[SKStatusSubscriptionService statusSubscriptionForHandle:]_block_invoke.4
- ___59-[SKStatusSubscriptionService statusSubscriptionForHandle:]_block_invoke.4.cold.1
- ___61-[SKPresence hasInitialCloudKitImportOccurredWithCompletion:]_block_invoke.30
- ___61-[SKPresence hasInitialCloudKitImportOccurredWithCompletion:]_block_invoke.30.cold.1
- ___65-[SKPresence retainTransientSubscriptionAssertionWithCompletion:]_block_invoke
- ___65-[SKPresence retainTransientSubscriptionAssertionWithCompletion:]_block_invoke.41
- ___65-[SKPresence retainTransientSubscriptionAssertionWithCompletion:]_block_invoke.41.cold.1
- ___65-[SKPresence retainTransientSubscriptionAssertionWithCompletion:]_block_invoke.cold.1
- ___66-[SKPresence releaseTransientSubscriptionAssertionWithCompletion:]_block_invoke.42
- ___66-[SKPresence releaseTransientSubscriptionAssertionWithCompletion:]_block_invoke.42.cold.1
- ___67-[SKPresence _fetchHandleInvitability:fromSenderHandle:completion:]_block_invoke.50
- ___68-[SKPresence invitedHandlesChangedForPresenceIdentifier:completion:]_block_invoke.69
- ___68-[SKPresence presentHandlesChangedForPresenceIdentifier:completion:]_block_invoke
- ___68-[SKPresence presentHandlesChangedForPresenceIdentifier:completion:]_block_invoke.66
- ___68-[SKPresence presentHandlesChangedForPresenceIdentifier:completion:]_block_invoke.cold.1
- ___70-[SKStatusSubscriptionService statusSubscriptionForHandle:completion:]_block_invoke.7
- ___70-[SKStatusSubscriptionService statusSubscriptionForHandle:completion:]_block_invoke.7.cold.1
- ___71-[SKStatusSubscriptionService _registerForDelegateCallbacksIfNecessary]_block_invoke.22
- ___71-[SKStatusSubscriptionService _registerForDelegateCallbacksIfNecessary]_block_invoke.22.cold.1
- ___72-[SKStatusSubscriptionService personalStatusSubscriptionWithCompletion:]_block_invoke.9
- ___72-[SKStatusSubscriptionService personalStatusSubscriptionWithCompletion:]_block_invoke.9.cold.1
- ___73-[SKStatusSubscriptionService allStatusSubscriptionsWithActiveAssertions]_block_invoke.10
- ___73-[SKStatusSubscriptionService allStatusSubscriptionsWithActiveAssertions]_block_invoke.10.cold.1
- ___73-[SKStatusSubscriptionService allStatusSubscriptionsWithActiveAssertions]_block_invoke.10.cold.2
- ___73-[SKStatusSubscriptionService subscriptionInvitationReceived:completion:]_block_invoke.37
- ___75-[SKStatusSubscriptionService subscriptionReceivedStatusUpdate:completion:]_block_invoke.34
- ___75-[SKStatusSubscriptionService subscriptionValidationTokensForHandle:error:]_block_invoke.16
- ___75-[SKStatusSubscriptionService subscriptionValidationTokensForHandle:error:]_block_invoke.16.cold.1
- ___75-[SKStatusSubscriptionService subscriptionValidationTokensForHandle:error:]_block_invoke.16.cold.2
- ___76-[SKPresence assertPresenceWithPresencePayload:assertionOptions:completion:]_block_invoke
- ___76-[SKPresence assertPresenceWithPresencePayload:assertionOptions:completion:]_block_invoke.39
- ___76-[SKPresence assertPresenceWithPresencePayload:assertionOptions:completion:]_block_invoke.39.cold.1
- ___76-[SKPresence assertPresenceWithPresencePayload:assertionOptions:completion:]_block_invoke.cold.1
- ___76-[SKStatusSubscriptionService allStatusSubscriptionsWithActiveSubscriptions]_block_invoke.13
- ___76-[SKStatusSubscriptionService allStatusSubscriptionsWithActiveSubscriptions]_block_invoke.13.cold.1
- ___76-[SKStatusSubscriptionService allStatusSubscriptionsWithActiveSubscriptions]_block_invoke.13.cold.2
- ___80-[SKStatusSubscriptionService subscriptionValidationTokensForHandle:completion:]_block_invoke.18
- ___80-[SKStatusSubscriptionService subscriptionValidationTokensForHandle:completion:]_block_invoke.18.cold.1
- ___80-[SKStatusSubscriptionService subscriptionValidationTokensForHandle:completion:]_block_invoke.18.cold.2
- ___83-[SKStatusSubscriptionService subscriptionStateChangedForSubscriptions:completion:]_block_invoke.30
- ___84-[SKStatusSubscriptionService _allStatusSubscriptionsIncludingPersonalSubscription:]_block_invoke.14
- ___84-[SKStatusSubscriptionService _allStatusSubscriptionsIncludingPersonalSubscription:]_block_invoke.14.cold.1
- ___84-[SKStatusSubscriptionService _allStatusSubscriptionsIncludingPersonalSubscription:]_block_invoke.14.cold.2
- ___ValidateClientIsInAllowlistForServiceName_block_invoke
- ___ValidateClientIsInAllowlistForServiceName_block_invoke_2
- ___block_descriptor_64_e8_32s40s48bs56w_e20_v24?0q8"NSError"16lw56l8s32l8s40l8s48l8
- ___block_descriptor_72_e8_32s40s48s56bs64w_e17_v16?0"NSError"8ls32l8w64l8s40l8s48l8s56l8
- ___block_literal_global.23
- ___block_literal_global.58
- ___block_literal_global.76
- ___block_literal_global.78
- ___block_literal_global.80
- ___block_literal_global.84
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$assertPresenceForIdentifier:withPresencePayload:assertionOptions:completion:
- _objc_msgSend$clientID
- _objc_msgSend$clientPrefixedPresenceIdentifierForPresenceIdentifier:
- _objc_msgSend$containsObject:
- _objc_msgSend$initWithPresenceDaemonDelegate:connectionDelegate:
- _objc_msgSend$initWithPublishingDaemonDelegate:connectionDelegate:
- _objc_msgSend$initWithSubscriptionDaemonDelegate:connectionDelegate:
- _objc_msgSend$payload
- _objc_msgSend$presentDevicesForPresenceIdentifier:completion:
- _objc_msgSend$retainTransientSubscriptionAssertionForPresenceIdentifier:completion:
- _objc_msgSend$retainTransientSubscriptionAssertionWithCompletion:
- _objc_msgSend$setPayload:
- _objc_msgSend$setXpcConnection:
- _objc_msgSend$stringWithUTF8String:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x8
- _xpc_copy_entitlement_for_self
- _xpc_string_get_string_ptr
CStrings:
+ ","
+ "-[SKPresence initWithPresenceIdentifier:options:listenerEndpoint:featureFlagProvider:]"
+ "-[SKPresenceDaemonConnection xpcConnection]"
+ "-[SKPresentDevice initWithHandle:deviceIdentifier:deviceTokenURI:payload:assertionTime:serverOriginatedTime:selfHandle:selfDevice:isPresent:sequenceNumber:]"
+ "-[SKStatusPublishingDaemonConnection xpcConnection]"
+ "-[SKStatusSubscriptionDaemonConnection xpcConnection]"
+ ".prototype"
+ "<%@: %p; channelIdentifierToken = \"%@\"; serverTime = \"%@\"; version = %lu>"
+ "<%@: %p; data = %lu bytes, dateCreated = %@>"
+ "<%@: %p; handle = \"%@\"; deviceIdentifier = \"%@\"; deviceTokenURI = \"%@\"; assertionTime = \"%@\"; serverOriginatedTime = \"%@\"; selfDevice = \"%d\"; selfHandle = \"%d\"; isPresent = \"%d\"; payload = \"%@\">"
+ "<%@: %p; payloadData = \"%@\" payloadKeyData = %@ routingUUID = %@>;"
+ "<%@: %p; payloadData = \"%@\" priority = %ld ttlSeconds = %f>;"
+ "<%@: %p; payloadDictionary = \"%@\" priority = %ld ttlSeconds = %f>;"
+ "<SKDeviceCircle "
+ "@\"<SKFeatureFlagProviding>\""
+ "@\"NSUUID\""
+ "@\"NSXPCListenerEndpoint\""
+ "@\"SKPresenceChannel\""
+ "@28@0:8q16B24"
+ "@32@0:8@16q24"
+ "@40@0:8@16@24q32"
+ "@40@0:8@16q24d32"
+ "@48@0:8@16@24@32@40"
+ "@84@0:8@16@24@32@40@48@56B64B68B72Q76"
+ "Appended prototype suffix to chosen client identifier: %@"
+ "Asserting presence for %@ with presence payload %@ and persistent payload %@ { on channel: %@ }"
+ "Attempted to assert on channel %@ that is not equivalent to active channel: %@. Please use the rollToChannel API to change channels."
+ "Attempted to assert on channel that is not equivalent to active channel"
+ "Attempted to check unknown feature flag: %ld"
+ "Attempted to retain subscription on channel %@ that is not equivalent to active channel: %@. Please use the rollToChannel API to change channels."
+ "Attempted to retain subscription on channel that is not equivalent to active channel"
+ "Attempted to roll channels when there was no active channel. Please use the createChannel API to create one, then assert/subscribe/set a persistent payload on it."
+ "B24@0:8q16"
+ "Clearing connection handlers and invalidating XPC connection"
+ "CloudKitVoucher"
+ "Creating channel for %@"
+ "Delegate does not implement presence:persistentDevicesChanged:, not informing delegate: %@"
+ "Delegate does not implement presentDevicesChangedForPresence: or presence:presentDevicesChanged:, not informing delegate: %@"
+ "Devices changed on presence: %@"
+ "Donating handles completed with error: %@"
+ "Donating handles completed."
+ "Error creating channel. Error: %{public}@"
+ "Error retrieving SecTask for self"
+ "Error retrieving code-signing identifier: %@"
+ "Error rolling channel. Error: %{public}@"
+ "Error setting filter override. Error: %{public}@"
+ "Error setting persistent payload. Error: %{public}@"
+ "Error when unpacking data as JSON: %@"
+ "Extracted date field was nil or empty"
+ "FastSyncSecurityCheck"
+ "ForceClientDefinitions"
+ "Informing delegate of persistent devices update with devices. Delegate: %@"
+ "Informing delegate of present devices update with devices. Delegate: %@"
+ "InitializeCloudKitSchema"
+ "JSONObjectWithData:options:error:"
+ "Last connection was %f seconds ago, backing off for %f seconds"
+ "LocalStatusKit"
+ "Object was not a valid JSON dictionary: %@"
+ "PresenceNonWakingPush"
+ "PresenceTester"
+ "Q"
+ "Received request to donate handles: %@ from presenceIdentifier: %{public}@"
+ "Retaining transient subscription assertion for presenceIdentifier %@ { on channel: %@ }"
+ "Retrieved code signing identifier: %@"
+ "Retrieved persistent devices. Presence: %{public}@ Handles: %@"
+ "Retrieved persistent devices. Presence: %{public}@ Handles: %@ Error: %@"
+ "Retrieved validation token. Presence: %{public}@ Token: %@"
+ "Retrieved validation token. Presence: %{public}@ Token: %@ Error: %@"
+ "Retrieving persistent devices. Presence: %{public}@"
+ "Retrieving validation token. Presence: %{public}@"
+ "Reve"
+ "Rolling channel for %@ from %@ to %@"
+ "SKDeviceCircleObjC"
+ "SKFeatureFlagProvider"
+ "SKFeatureFlagProviding"
+ "SKPresenceChannel"
+ "SKPresenceChannelData"
+ "SKPresenceDaemonConnection.m"
+ "SKPresenceServerRoutablePayload"
+ "SKPresenceValidationToken"
+ "SKPresenceValidationTokenChannelIdentifierToken"
+ "SKPresenceValidationTokenServerTime"
+ "SKPresenceValidationTokenVersion"
+ "SKStatusPublishingDaemonConnection.m"
+ "SKStatusSubscriptionDaemonConnection.m"
+ "SKStatusSubscriptionValidationTokenResult"
+ "SKUpdatePriorityDefault"
+ "Setting filter override for presenceIdentifier: %{public}@"
+ "Setting persistent payload for %@ with payload %@"
+ "StatusKit.SKDeviceCircleObjC"
+ "StatusNonWakingPush"
+ "Streams"
+ "Successfully created channel for presence identifier %@: %@"
+ "Successfully rolled channel for presence identifier %@"
+ "Successfully set filter override for presence identifier: %{public}@"
+ "Successfully set persistent payload for presence identifier %@ to payload %@"
+ "T@\"<SKFeatureFlagProviding>\",&,N,V_featureFlagProvider"
+ "T@\"NSData\",R,C,N,V_payloadData"
+ "T@\"NSData\",R,C,N,V_payloadKeyData"
+ "T@\"NSData\",R,N,V_data"
+ "T@\"NSDate\",&,N,V_cachedDateCreated"
+ "T@\"NSDate\",&,N,V_lastDaemonReconnectionTime"
+ "T@\"NSDate\",R,N"
+ "T@\"NSDate\",R,N,V_serverOriginatedTime"
+ "T@\"NSDate\",R,N,V_serverTime"
+ "T@\"NSString\",N,R"
+ "T@\"NSString\",R,N,V_channelIdentifierToken"
+ "T@\"NSUUID\",R,C,N,V_routingUUID"
+ "T@\"NSXPCConnection\",R,N,V_xpcConnection"
+ "T@\"NSXPCListenerEndpoint\",&,N,V_listenerEndpoint"
+ "T@\"SKPresenceChannel\",&,N,V_activeChannel"
+ "T@\"SKPresencePayload\",&,N,V_persistentPayload"
+ "T@\"SKPresencePayload\",&,N,V_presencePayload"
+ "T@\"SKPresenceValidationToken\",R,N"
+ "TB,R,N,V_isExpectedFailure"
+ "TB,R,N,V_isPresent"
+ "TQ,N,V_sequenceNumber"
+ "Td,R,N,V_ttlSeconds"
+ "Tq,R,N,V_unmatchedField"
+ "Tq,R,N,V_validity"
+ "Tq,R,N,V_version"
+ "Validating token completed with error: %@"
+ "Validating token completed with validity: %ld"
+ "Validating token with presence identifier: %@, token: %@"
+ "XPC Error creating channel. Error: %{public}@"
+ "XPC Error donating handles. Presence: %{public}@ handles:%@ Error: %{public}@"
+ "XPC Error retrieving persistent devices. Presence: %{public}@ Error: %{public}@"
+ "XPC Error retrieving validation tkoen. Presence: %{public}@ Error: %{public}@"
+ "XPC Error setting filter override. Error: %{public}@"
+ "XPC Error setting persistent payload. Error: %{public}@"
+ "XPC error validating token. Error: %{public}@"
+ "_activeChannel"
+ "_cachedDateCreated"
+ "_channelIdentifierToken"
+ "_data"
+ "_featureFlagProvider"
+ "_isExpectedFailure"
+ "_isPresent"
+ "_lastDaemonReconnectionTime"
+ "_listenerEndpoint"
+ "_payloadKeyData"
+ "_persistentPayload"
+ "_routingUUID"
+ "_sequenceNumber"
+ "_serverOriginatedTime"
+ "_serverTime"
+ "_ttlSeconds"
+ "_unmatchedField"
+ "_validity"
+ "_version"
+ "activeChannel"
+ "appendString:"
+ "assertPresenceForIdentifier:onChannel:withPresencePayload:persistentPayload:serverRoutablePayload:assertionOptions:completion:"
+ "assertPresenceOnChannel:withPresencePayload:persistentPayload:serverRoutablePayload:assertionOptions:completion:"
+ "assertPresenceWithPresencePayload:persistentPayload:assertionOptions:completion:"
+ "assertPresenceWithPresencePayload:persistentPayload:serverRoutablePayload:assertionOptions:completion:"
+ "boolValue"
+ "cachedDateCreated"
+ "calling _registerForDelegateCallbacksIfNecessary for presenceIdentifier %{public}@"
+ "calling daemon setFilterOverride for presenceIdentifier %{public}@"
+ "cd"
+ "channelIdentifierToken"
+ "clientIdentifierPrefixByCodeSigningIdentifier"
+ "clientIdentifierPrefixForServiceIdentifier:"
+ "clientIdentifierPrefixFromPresenceIdentifier"
+ "clientPrefixedPresenceIdentifierForPresenceIdentifier:serviceIdentifier:"
+ "com.apple.PresenceTester"
+ "com.apple.SharePlay.GroupSessionService"
+ "com.apple.StatusKitMultiDeviceTests.xctrunner"
+ "com.apple.Streams"
+ "com.apple.homecommsd"
+ "com.apple.homed"
+ "com.apple.identityservicesd"
+ "com.apple.internal.Reve"
+ "com.apple.mDNSResponder"
+ "com.apple.mediaremoted"
+ "com.apple.statustool"
+ "createChannelWithCompletion:"
+ "d"
+ "d16@0:8"
+ "data"
+ "dateByAddingTimeInterval:"
+ "dateWithTimeIntervalSinceReferenceDate:"
+ "decodeDoubleForKey:"
+ "decodeIntegerForKey:"
+ "deviceCircle"
+ "devicesChangedForPresenceIdentifier:presentDevices:persistentDevices:completion:"
+ "dictionaryWithObjects:forKeys:count:"
+ "donateTrustedHandle:completion:"
+ "donateTrustedHandles:completion:"
+ "donateTrustedHandles:presenceIdentifier:completion:"
+ "doubleValue"
+ "encodeDouble:forKey:"
+ "encodeInteger:forKey:"
+ "errorWithDomain:code:userInfo:"
+ "familyCircle"
+ "featureFlagProvider"
+ "hasSuffix:"
+ "homeCircleWithUUID:"
+ "init()"
+ "initInvalidWithUnmatchedField:isExpectedFailure:"
+ "initUnknown"
+ "initValid"
+ "initWithChannelIdentifierToken:serverTime:"
+ "initWithChannelIdentifierToken:serverTime:version:"
+ "initWithData:priority:"
+ "initWithData:priority:ttlSeconds:"
+ "initWithData:routingUUID:payloadKeyData:"
+ "initWithDictionary:priority:"
+ "initWithDictionary:priority:ttlSeconds:"
+ "initWithHandle:deviceIdentifier:deviceTokenURI:payload:assertionTime:serverOriginatedTime:selfHandle:selfDevice:isPresent:sequenceNumber:"
+ "initWithListenerEndpoint:"
+ "initWithPresenceDaemonDelegate:connectionDelegate:listenerEndpoint:"
+ "initWithPresenceIdentifier:options:listenerEndpoint:featureFlagProvider:"
+ "initWithPublishingDaemonDelegate:connectionDelegate:listenerEndpoint:"
+ "initWithStatusTypeIdentifier:listenerEndpoint:"
+ "initWithSubscriptionDaemonDelegate:connectionDelegate:listenerEndpoint:"
+ "isActive"
+ "isEqualToDate:"
+ "isEqualToPresenceValidationToken:"
+ "isExpectedFailure"
+ "isFeatureEnabled:"
+ "isPresent"
+ "lastDaemonReconnectionTime"
+ "listenerEndpoint"
+ "mutableCopy"
+ "none"
+ "now"
+ "objectForKeyedSubscript:"
+ "os_variant_allows_internal_security_policies(STATUS_KIT_LOG_SUBSYSTEM)"
+ "payloadKey"
+ "payloadKeyData"
+ "persistentDevices"
+ "persistentDevicesForPresenceIdentifier:onChannel:completion:"
+ "persistentPayload"
+ "personalCircle"
+ "presence:persistentDevicesChanged:"
+ "presence:presentDevicesChanged:"
+ "presentDevicesForPresenceIdentifier:onChannel:completion:"
+ "retainTransientSubscriptionAssertionForPresenceIdentifier:onChannel:completion:"
+ "retainTransientSubscriptionAssertionOnChannel:completion:"
+ "rollChannelFromChannel:toChannel:completion:"
+ "rollToChannel:completion:"
+ "routingUUID"
+ "sequenceNumber"
+ "serverOriginatedTime"
+ "serverTime"
+ "setActiveChannel:"
+ "setCachedDateCreated:"
+ "setFeatureFlagProvider:"
+ "setFilterOverride:completion:"
+ "setFilterOverride:onChannel:presenceIdentifier:completion:"
+ "setLastDaemonReconnectionTime:"
+ "setListenerEndpoint:"
+ "setPersistentPayload:"
+ "setPersistentPayload:completion:"
+ "setPersistentPayload:onChannel:presenceIdentifier:completion:"
+ "setPersistentPayloadOnChannel:payload:completion:"
+ "setPresencePayload:"
+ "setSequenceNumber:"
+ "timeIntervalSinceDate:"
+ "ttlSeconds"
+ "unmatchedField"
+ "v24@0:8@?<v@?@\"SKPresenceChannel\"@\"NSError\">16"
+ "v24@0:8Q16"
+ "v24@?0@\"SKPresenceChannel\"8@\"NSError\"16"
+ "v24@?0@\"SKPresenceValidationToken\"8@\"NSError\"16"
+ "v24@?0@\"SKStatusSubscriptionValidationTokenResult\"8@\"NSError\"16"
+ "v28@0:8i16@?20"
+ "v32@0:8@\"NSString\"16@?<v@?@\"SKPresenceValidationToken\"@\"NSError\">24"
+ "v40@0:8@\"NSString\"16@\"SKPresenceChannel\"24@?<v@?@\"NSArray\"@\"NSError\">32"
+ "v40@0:8@\"NSString\"16@\"SKPresenceChannel\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"SKPresenceChannel\"16@\"SKPresenceChannel\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"SKPresenceValidationToken\"16@\"NSString\"24@?<v@?q@\"NSError\">32"
+ "v44@0:8i16@\"SKPresenceChannel\"20@\"NSString\"28@?<v@?@\"NSError\">36"
+ "v44@0:8i16@20@28@?36"
+ "v48@0:8@\"NSString\"16@\"NSArray\"24@\"NSArray\"32@?<v@?>40"
+ "v48@0:8@\"SKPresencePayload\"16@\"SKPresenceChannel\"24@\"NSString\"32@?<v@?@\"NSError\">40"
+ "v48@0:8@\"SKSubscriptionValidationTokens\"16@\"SKHandle\"24@\"NSString\"32@?<v@?@\"SKStatusSubscriptionValidationTokenResult\"@\"NSError\">40"
+ "v64@0:8@16@24@32@40@48@?56"
+ "v72@0:8@\"NSString\"16@\"SKPresenceChannel\"24@\"SKPresencePayload\"32@\"SKPresencePayload\"40@\"SKPresenceServerRoutablePayload\"48@\"SKPresenceAssertionOptions\"56@?<v@?@\"NSError\">64"
+ "v72@0:8@16@24@32@40@48@56@?64"
+ "validateToken:completion:"
+ "validateToken:presenceIdentifier:completion:"
+ "validationToken"
+ "validationTokenForPresenceIdentifier:completion:"
+ "validity"
+ "version"
- "'"
- "-[SKPresence initWithPresenceIdentifier:options:]"
- "-[SKPresentDevice initWithHandle:deviceIdentifier:deviceTokenURI:payload:assertionTime:selfHandle:selfDevice:]"
- "<%@: %p; handle = \"%@\"; deviceIdentifier = \"%@\"; deviceTokenURI = \"%@\"; assertionTime = \"%@\"; selfDevice = \"%d\"; selfHandle = \"%d\"; payload = \"%@\">"
- "@64@0:8@16@24@32@40@48B56B60"
- "Asserting presence for %@ with payload %@"
- "Delegate does not implement presentDevicesChangedForPresence:, not informing delegate: %@"
- "MediaTransport"
- "Present devices changed on presence: %@"
- "Retaining transient subscription assertion for presenceIdentifier %@"
- "T@\"NSXPCConnection\",&,N,V_xpcConnection"
- "T@\"SKPresencePayload\",&,N,V_payload"
- "Unknown service name %@ when checking allowlist"
- "XPC Connection Interruption Handled"
- "XPC Connection Invalidation Handled"
- "_payload"
- "ancli"
- "assertPresenceForIdentifier:withPresencePayload:assertionOptions:completion:"
- "clientID"
- "clientIDFromPresenceIdentifier"
- "clientPrefixedPresenceIdentifierForPresenceIdentifier:"
- "com.apple.StatusKit.presence.clientID"
- "com.apple.availability"
- "com.apple.focus.status"
- "com.apple.offgrid.status"
- "containsObject:"
- "initWithHandle:deviceIdentifier:deviceTokenURI:payload:assertionTime:selfHandle:selfDevice:"
- "presentDevicesForPresenceIdentifier:completion:"
- "presentHandlesChangedForPresenceIdentifier:completion:"
- "retainTransientSubscriptionAssertionForPresenceIdentifier:completion:"
- "safari"
- "setPayload:"
- "setXPCConnection:"
- "setXpcConnection:"
- "stringWithUTF8String:"
- "v48@0:8@\"NSString\"16@\"SKPresencePayload\"24@\"SKPresenceAssertionOptions\"32@?<v@?@\"NSError\">40"
- "v48@0:8@\"SKSubscriptionValidationTokens\"16@\"SKHandle\"24@\"NSString\"32@?<v@?q@\"NSError\">40"

```
