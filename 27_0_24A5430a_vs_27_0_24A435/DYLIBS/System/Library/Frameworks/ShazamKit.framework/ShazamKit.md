## ShazamKit

> `/System/Library/Frameworks/ShazamKit.framework/ShazamKit`

```diff

 427.0.48.0.0
-  __TEXT.__text: 0xa172c
-  __TEXT.__objc_methlist: 0x5170
-  __TEXT.__const: 0x222b7
-  __TEXT.__cstring: 0x3a9b
-  __TEXT.__gcc_except_tab: 0x38a0
-  __TEXT.__oslogstring: 0x1431
-  __TEXT.__constg_swiftt: 0x7bc
-  __TEXT.__swift5_typeref: 0xfd4
-  __TEXT.__swift5_builtin: 0xb4
-  __TEXT.__swift5_reflstr: 0x4c2
-  __TEXT.__swift5_fieldmd: 0x66c
-  __TEXT.__swift5_assocty: 0x230
-  __TEXT.__swift5_proto: 0x184
-  __TEXT.__swift5_types: 0x94
-  __TEXT.__swift_as_entry: 0xb4
-  __TEXT.__swift_as_ret: 0xc8
-  __TEXT.__swift_as_cont: 0x164
-  __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__swift5_protos: 0x14
+  __TEXT.__text: 0xa68cc
+  __TEXT.__objc_methlist: 0x5200
+  __TEXT.__const: 0x22a97
+  __TEXT.__cstring: 0x3c4d
+  __TEXT.__gcc_except_tab: 0x38a4
+  __TEXT.__oslogstring: 0x1471
+  __TEXT.__constg_swiftt: 0xa6c
+  __TEXT.__swift5_typeref: 0x10ac
+  __TEXT.__swift5_builtin: 0xdc
+  __TEXT.__swift5_reflstr: 0x5ee
+  __TEXT.__swift5_fieldmd: 0x89c
+  __TEXT.__swift5_assocty: 0x248
+  __TEXT.__swift5_proto: 0x1e4
+  __TEXT.__swift5_types: 0xd8
+  __TEXT.__swift_as_entry: 0xbc
+  __TEXT.__swift_as_ret: 0xd4
+  __TEXT.__swift_as_cont: 0x184
+  __TEXT.__swift5_mpenum: 0x20
+  __TEXT.__swift5_protos: 0x18
   __TEXT.__swift5_capture: 0x324
-  __TEXT.__unwind_info: 0x34e8
-  __TEXT.__eh_frame: 0x24c0
+  __TEXT.__unwind_info: 0x36c8
+  __TEXT.__eh_frame: 0x2b68
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x900
-  __DATA_CONST.__objc_classlist: 0x370
+  __DATA_CONST.__const: 0x910
+  __DATA_CONST.__objc_classlist: 0x3a0
   __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x150
+  __DATA_CONST.__objc_protolist: 0x158
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x20
-  __DATA_CONST.__objc_selrefs: 0x2518
+  __DATA_CONST.__objc_selrefs: 0x2558
   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_superrefs: 0x258
-  __DATA_CONST.__got: 0x868
-  __AUTH_CONST.__const: 0x2160
-  __AUTH_CONST.__cfstring: 0x27a0
-  __AUTH_CONST.__objc_const: 0x9f08
+  __DATA_CONST.__got: 0x8b0
+  __AUTH_CONST.__const: 0x27a8
+  __AUTH_CONST.__cfstring: 0x2820
+  __AUTH_CONST.__objc_const: 0xa398
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_intobj: 0x120
-  __AUTH_CONST.__auth_got: 0x1330
-  __AUTH.__objc_data: 0x50
-  __AUTH.__data: 0x298
-  __DATA.__objc_ivar: 0x4e4
-  __DATA.__data: 0x1b2480
+  __AUTH_CONST.__auth_got: 0x1418
+  __AUTH.__objc_data: 0xa0
+  __AUTH.__data: 0x338
+  __DATA.__objc_ivar: 0x4ec
+  __DATA.__data: 0x1b2530
   __DATA.__common: 0x1d8
   __DATA_DIRTY.__objc_data: 0x2288
-  __DATA_DIRTY.__data: 0x7e8
+  __DATA_DIRTY.__data: 0xa78
   __DATA_DIRTY.__bss: 0x160
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /System/Library/PrivateFrameworks/CollectionsInternal.framework/CollectionsInternal
   - /System/Library/PrivateFrameworks/MusicKitInternal.framework/MusicKitInternal
   - /System/Library/PrivateFrameworks/ShazamCore.framework/ShazamCore
+  - /System/Library/PrivateFrameworks/Tightbeam.framework/Tightbeam
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3651
-  Symbols:   6149
-  CStrings:  575
+  Functions: 3816
+  Symbols:   6238
+  CStrings:  587
 
Symbols:
+ +[SHAmbientSession activateSessionWithContext:completionHandler:]
+ +[SHAmbientSession deactivateSessionWithContext:completionHandler:]
+ +[SHAmbientSession serverConnection]
+ +[SHAmbientSession setMusicDetectedState:completionHandler:]
+ -[SHCatalogConfiguration enableInstant]
+ -[SHCatalogConfiguration setEnableInstant:]
+ -[SHRecordRequest enableInstant]
+ -[SHRecordRequest initWithRequestID:notifications:deadline:storeSignatureOnNoMatch:enableLiveActivity:enableInstant:invocationSource:preferredInputAudioRoute:]
+ -[SHShazamKitServiceConnection setAmbientSessionActiveState:forContext:completionHandler:]
+ -[SHShazamKitServiceConnection setMusicDetected:completionHandler:]
+ _OBJC_CLASS_$_SHAmbientSession
+ _OBJC_IVAR_$_SHCatalogConfiguration._enableInstant
+ _OBJC_IVAR_$_SHRecordRequest._enableInstant
+ _OBJC_METACLASS_$_SHAmbientSession
+ _SHAmbientSessionContextLiveActivity
+ _SHAmbientSessionContextSmartStack
+ __DATA__TtC9ShazamKit16SHAmbientSession
+ __DATA__TtC9ShazamKit16SHExclaveService
+ __DATA__TtC9ShazamKit22ShazamSignatureService
+ __DATA__TtCC9ShazamKit22ShazamSignatureService6Server
+ __DATA__TtCC9ShazamKit22ShazamSignatureService7Service
+ __IVARS__TtC9ShazamKit16SHAmbientSession
+ __IVARS__TtC9ShazamKit16SHExclaveService
+ __IVARS__TtCC9ShazamKit22ShazamSignatureService6Server
+ __IVARS__TtCC9ShazamKit22ShazamSignatureService7Service
+ __METACLASS_DATA__TtC9ShazamKit16SHAmbientSession
+ __METACLASS_DATA__TtC9ShazamKit16SHExclaveService
+ __METACLASS_DATA__TtC9ShazamKit22ShazamSignatureService
+ __METACLASS_DATA__TtCC9ShazamKit22ShazamSignatureService6Server
+ __METACLASS_DATA__TtCC9ShazamKit22ShazamSignatureService7Service
+ __OBJC_$_CLASS_METHODS_SHAmbientSession
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SHAmbientSessionService
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SHAmbientSessionService
+ __OBJC_$_PROTOCOL_REFS_SHAmbientSessionService
+ __OBJC_CLASS_RO_$_SHAmbientSession
+ __OBJC_LABEL_PROTOCOL_$_SHAmbientSessionService
+ __OBJC_METACLASS_RO_$_SHAmbientSession
+ __OBJC_PROTOCOL_$_SHAmbientSessionService
+ ___36+[SHAmbientSession serverConnection]_block_invoke
+ ___67-[SHShazamKitServiceConnection setMusicDetected:completionHandler:]_block_invoke
+ ___90-[SHShazamKitServiceConnection setAmbientSessionActiveState:forContext:completionHandler:]_block_invoke
+ ___swift_memcpy0_1
+ ___swift_memcpy25_8
+ _associated conformance 9ShazamKit10SampleRateOSHAASQ
+ _associated conformance 9ShazamKit16SHAmbientSessionC7ContextOSHAASQ
+ _associated conformance 9ShazamKit16SHExclaveServiceC16InvocationSourceOSHAASQ
+ _associated conformance 9ShazamKit24SignatureGenerationErrorOSHAASQ
+ _associated conformance 9ShazamKit25SignatureInvocationSourceOSHAASQ
+ _get_enum_tag_for_layout_string 9ShazamKit16SignaturePayloadO
+ _mach_continuous_time
+ _objc_msgSend$activateSessionWithContext:completionHandler:
+ _objc_msgSend$deactivateSessionWithContext:completionHandler:
+ _objc_msgSend$enableInstant
+ _objc_msgSend$initWithHostTime:sampleTime:atRate:
+ _objc_msgSend$initWithRequestID:notifications:deadline:storeSignatureOnNoMatch:enableLiveActivity:enableInstant:invocationSource:preferredInputAudioRoute:
+ _objc_msgSend$setAmbientSessionActiveState:forContext:completionHandler:
+ _objc_msgSend$setEnableInstant:
+ _objc_msgSend$setMusicDetected:completionHandler:
+ _objc_msgSend$setMusicDetectedState:completionHandler:
+ _swift_deallocPartialClassInstance
+ _swift_defaultActor_deallocate
+ _swift_defaultActor_destroy
+ _symbolic $s9ShazamKit0A23SignatureServiceHandlerP
+ _symbolic BD
+ _symbolic Say_____G s5UInt8V
+ _symbolic _____ 9ShazamKit0A16SignatureServiceC
+ _symbolic _____ 9ShazamKit0A16SignatureServiceC0D0C
+ _symbolic _____ 9ShazamKit0A16SignatureServiceC6ServerC
+ _symbolic _____ 9ShazamKit10SampleRateO
+ _symbolic _____ 9ShazamKit16SHAmbientSessionC
+ _symbolic _____ 9ShazamKit16SHAmbientSessionC7ContextO
+ _symbolic _____ 9ShazamKit16SHExclaveServiceC
+ _symbolic _____ 9ShazamKit16SHExclaveServiceC16InvocationSourceO
+ _symbolic _____ 9ShazamKit16SignaturePayloadO
+ _symbolic _____ 9ShazamKit16SignatureRequestV
+ _symbolic _____ 9ShazamKit24SignatureGenerationErrorO
+ _symbolic _____ 9ShazamKit25SignatureInvocationSourceO
+ _symbolic _____ 9ShazamKit7SecondsV
+ _symbolic _____ 9ShazamKit9AudioDataV
+ _symbolic _____ 9ShazamKit9AudioTimeV
+ _symbolic _____ 9ShazamKit9SignatureV
+ _symbolic _____ 9Tightbeam16ClientConnectionC
+ _symbolic _____ 9Tightbeam17ServiceConnectionC
+ _symbolic _____ So10tb_error_ta
+ _symbolic _____ s6UInt64V
+ _type_layout_string 9ShazamKit16SignaturePayloadO
+ _type_layout_string 9ShazamKit16SignatureRequestV
+ _type_layout_string 9ShazamKit7SecondsV
+ _type_layout_string 9ShazamKit9AudioDataV
+ _type_layout_string 9ShazamKit9AudioTimeV
+ _type_layout_string 9ShazamKit9SignatureV
- -[SHRecordRequest initWithRequestID:notifications:deadline:storeSignatureOnNoMatch:enableLiveActivity:invocationSource:preferredInputAudioRoute:]
- _objc_msgSend$initWithRequestID:notifications:deadline:storeSignatureOnNoMatch:enableLiveActivity:invocationSource:preferredInputAudioRoute:
CStrings:
+ "Encrypted data is not currently supported"
+ "Invalid key value while decoding result type for signature"
+ "Received exclave signature byte array with count %ld"
+ "SHAmbientSessionContextLiveActivity"
+ "SHAmbientSessionContextSmartStack"
+ "SHCatalogConfigurationEnableInstantKey"
+ "ShazamKit/SHExclaveService.swift"
+ "ShazamKit/ShazamKit_swift.swift"
+ "com.apple.shazamd.service"
+ "enableInstant"
+ "illegal variant selector: "
+ "invalid rawValue for SignatureGenerationError: "
```
