## Rapport

> `/System/Library/PrivateFrameworks/Rapport.framework/Rapport`

```diff

-716.200.31.0.0
-  __TEXT.__text: 0x966c8
-  __TEXT.__auth_stubs: 0x1bb0
-  __TEXT.__objc_methlist: 0x8df4
-  __TEXT.__const: 0x34b8
-  __TEXT.__cstring: 0x14d94
+716.200.62.0.0
+  __TEXT.__text: 0x9ad5c
+  __TEXT.__auth_stubs: 0x1cd0
+  __TEXT.__objc_methlist: 0x8eb4
+  __TEXT.__const: 0x3828
+  __TEXT.__cstring: 0x150b4
   __TEXT.__gcc_except_tab: 0x171c
-  __TEXT.__oslogstring: 0x69d
-  __TEXT.__swift5_typeref: 0x663
-  __TEXT.__swift5_fieldmd: 0x608
-  __TEXT.__constg_swiftt: 0x5a4
-  __TEXT.__swift5_reflstr: 0x28b
-  __TEXT.__swift5_proto: 0xf0
-  __TEXT.__swift5_types: 0x80
-  __TEXT.__swift5_capture: 0x94
+  __TEXT.__oslogstring: 0x6cd
+  __TEXT.__swift5_typeref: 0x779
+  __TEXT.__swift5_capture: 0xd0
+  __TEXT.__swift5_fieldmd: 0x7f4
+  __TEXT.__constg_swiftt: 0x6f0
+  __TEXT.__swift5_reflstr: 0x35c
+  __TEXT.__swift5_proto: 0x128
+  __TEXT.__swift5_types: 0x98
+  __TEXT.__swift_as_entry: 0x4
+  __TEXT.__swift_as_ret: 0x4
   __TEXT.__swift5_assocty: 0x40
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x2430
-  __TEXT.__eh_frame: 0x598
-  __TEXT.__objc_classname: 0xa7c
-  __TEXT.__objc_methname: 0x10c7f
-  __TEXT.__objc_methtype: 0x2bf6
-  __TEXT.__objc_stubs: 0x8f20
-  __DATA_CONST.__got: 0x3a0
+  __TEXT.__unwind_info: 0x2578
+  __TEXT.__eh_frame: 0x7b0
+  __TEXT.__objc_classname: 0xa8c
+  __TEXT.__objc_methname: 0x10d79
+  __TEXT.__objc_methtype: 0x2bff
+  __TEXT.__objc_stubs: 0x8f60
+  __DATA_CONST.__got: 0x3e8
   __DATA_CONST.__const: 0x2708
-  __DATA_CONST.__objc_classlist: 0x288
+  __DATA_CONST.__objc_classlist: 0x298
   __DATA_CONST.__objc_catlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x128
+  __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3a28
-  __DATA_CONST.__objc_protorefs: 0xc8
+  __DATA_CONST.__objc_selrefs: 0x3a90
+  __DATA_CONST.__objc_protorefs: 0xd8
   __DATA_CONST.__objc_superrefs: 0x1d8
   __DATA_CONST.__objc_arraydata: 0xb0
-  __AUTH_CONST.__auth_got: 0xde8
-  __AUTH_CONST.__const: 0xfd0
-  __AUTH_CONST.__cfstring: 0x5180
-  __AUTH_CONST.__objc_const: 0x10530
+  __AUTH_CONST.__auth_got: 0xe78
+  __AUTH_CONST.__const: 0x11e0
+  __AUTH_CONST.__cfstring: 0x51a0
+  __AUTH_CONST.__objc_const: 0x107c0
   __AUTH_CONST.__objc_intobj: 0x2b8
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH.__objc_data: 0x5e8
-  __AUTH.__data: 0x7d8
-  __DATA.__objc_ivar: 0x1124
-  __DATA.__data: 0x1cb8
-  __DATA.__bss: 0x2290
-  __DATA.__common: 0x48
+  __AUTH.__objc_data: 0x7a0
+  __AUTH.__data: 0x8c8
+  __DATA.__objc_ivar: 0x1128
+  __DATA.__data: 0x1db8
+  __DATA.__bss: 0x2ab0
+  __DATA.__common: 0x68
   __DATA_DIRTY.__objc_data: 0x14a0
-  __DATA_DIRTY.__data: 0x198
+  __DATA_DIRTY.__data: 0x1a0
   __DATA_DIRTY.__bss: 0x14
+  - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CryptoKit.framework/CryptoKit
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 280CA79D-79C2-34FD-B6EA-C3B7F90B2F89
-  Functions: 4371
-  Symbols:   12033
-  CStrings:  7017
+  UUID: 94307BB8-CB33-3B69-83D4-8CF48574906E
+  Functions: 4473
+  Symbols:   12106
+  CStrings:  7061
 
Symbols:
+ +[RPNWFramer setupDaemonFramer:token:receiveHandler:closeHandler:]
+ +[RPNWFramer startConnection:token:]
+ +[RPNWFramer startConnection:token:].cold.1
+ +[RPNWFramer writeControlOnFramer:type:error:token:]
+ +[RPNWFramer writeControlOnFramer:type:error:token:].cold.1
+ +[RPNWFramer writeErrorOnFramer:token:error:]
+ -[RPEndpoint setTxtRecord:]
+ -[RPEndpoint txtRecord]
+ _OBJC_CLASS_$_NSLock
+ _OBJC_CLASS_$__TtC7Rapport16RPPairingPINInfo
+ _OBJC_CLASS_$__TtC7Rapport31RPPairingBonjourResolveResponse
+ _OBJC_IVAR_$_RPEndpoint._txtRecord
+ _OBJC_METACLASS_$__TtC7Rapport16RPPairingPINInfo
+ _OBJC_METACLASS_$__TtC7Rapport31RPPairingBonjourResolveResponse
+ __DATA__TtC7Rapport16RPPairingPINInfo
+ __DATA__TtC7Rapport31RPPairingBonjourResolveResponse
+ __INSTANCE_METHODS__TtC7Rapport16RPPairingPINInfo
+ __INSTANCE_METHODS__TtC7Rapport31RPPairingBonjourResolveResponse
+ __IVARS__TtC7Rapport12RPThreadSafe
+ __IVARS__TtC7Rapport16RPPairingPINInfo
+ __IVARS__TtC7Rapport31RPPairingBonjourResolveResponse
+ __METACLASS_DATA__TtC7Rapport16RPPairingPINInfo
+ __METACLASS_DATA__TtC7Rapport31RPPairingBonjourResolveResponse
+ __OBJC_$_PROTOCOL_REFS_OS_sec_identity
+ __OBJC_LABEL_PROTOCOL_$_OS_sec_identity
+ __OBJC_PROTOCOL_$_OS_sec_identity
+ __PROPERTIES__TtC7Rapport16RPPairingPINInfo
+ __PROPERTIES__TtC7Rapport31RPPairingBonjourResolveResponse
+ ___52+[RPNWFramer writeControlOnFramer:type:error:token:]_block_invoke
+ ___52+[RPNWFramer writeControlOnFramer:type:error:token:]_block_invoke.cold.1
+ ___52+[RPNWFramer writeControlOnFramer:type:error:token:]_block_invoke.cold.2
+ ___66+[RPNWFramer setupDaemonFramer:token:receiveHandler:closeHandler:]_block_invoke
+ ___66+[RPNWFramer setupDaemonFramer:token:receiveHandler:closeHandler:]_block_invoke.cold.1
+ ___66+[RPNWFramer setupDaemonFramer:token:receiveHandler:closeHandler:]_block_invoke.cold.2
+ ___66+[RPNWFramer setupDaemonFramer:token:receiveHandler:closeHandler:]_block_invoke.cold.3
+ ___66+[RPNWFramer setupDaemonFramer:token:receiveHandler:closeHandler:]_block_invoke.cold.4
+ ___66+[RPNWFramer setupDaemonFramer:token:receiveHandler:closeHandler:]_block_invoke.cold.5
+ ___66+[RPNWFramer setupDaemonFramer:token:receiveHandler:closeHandler:]_block_invoke_2
+ ___66+[RPNWFramer setupDaemonFramer:token:receiveHandler:closeHandler:]_block_invoke_3
+ ___66+[RPNWFramer setupDaemonFramer:token:receiveHandler:closeHandler:]_block_invoke_3.cold.1
+ ___66+[RPNWFramer setupDaemonFramer:token:receiveHandler:closeHandler:]_block_invoke_3.cold.2
+ ___66+[RPNWFramer setupDaemonFramer:token:receiveHandler:closeHandler:]_block_invoke_4
+ ___66+[RPNWFramer setupDaemonFramer:token:receiveHandler:closeHandler:]_block_invoke_4.cold.1
+ ___66+[RPNWFramer setupDaemonFramer:token:receiveHandler:closeHandler:]_block_invoke_5
+ ___66+[RPNWFramer setupDaemonFramer:token:receiveHandler:closeHandler:]_block_invoke_5.cold.1
+ ___block_descriptor_69_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_88_e8_32s40s48bs56bs64r72r80r_e32_Q16?0"NSObject<OS_nw_framer>"8lr64l8r72l8r80l8s48l8s32l8s56l8s40l8
+ ___block_literal_global.204
+ ___block_literal_global.34
+ ___block_literal_global.51
+ ___block_literal_global.63
+ ___block_literal_global.66
+ ___nwrapport_copy_protocol_definition_block_invoke.57
+ ___nwrapport_copy_protocol_definition_block_invoke.57.cold.1
+ ___nwrapport_copy_protocol_definition_block_invoke.60.cold.1
+ ___nwrapport_copy_protocol_definition_block_invoke.64
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ ___swift_destroy_boxed_opaque_existential_1Tm
+ ___swift_memcpy112_8
+ ___swift_project_boxed_opaque_existential_1Tm
+ ___unnamed_22
+ _associated conformance 7Rapport26RPPairingTemporaryIdentityV10CodingKeys33_4096031F76CFA760152ED9A42AB523CELLOSHAASQ
+ _associated conformance 7Rapport26RPPairingTemporaryIdentityV10CodingKeys33_4096031F76CFA760152ED9A42AB523CELLOs0E3KeyAAs23CustomStringConvertible
+ _associated conformance 7Rapport26RPPairingTemporaryIdentityV10CodingKeys33_4096031F76CFA760152ED9A42AB523CELLOs0E3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 7Rapport31RPPairingBonjourResolveResponseC10CodingKeys33_4096031F76CFA760152ED9A42AB523CELLOSHAASQ
+ _associated conformance 7Rapport31RPPairingBonjourResolveResponseC10CodingKeys33_4096031F76CFA760152ED9A42AB523CELLOs0F3KeyAAs23CustomStringConvertible
+ _associated conformance 7Rapport31RPPairingBonjourResolveResponseC10CodingKeys33_4096031F76CFA760152ED9A42AB523CELLOs0F3KeyAAs28CustomDebugStringConvertible
+ _flat unique So15OS_sec_identity_p
+ _objc_msgSend$appendFormat:
+ _objc_msgSend$txtRecord
+ _objc_msgSend$writeControlOnFramer:type:error:token:
+ _swift_arrayDestroy
+ _swift_continuation_await
+ _swift_continuation_init
+ _swift_continuation_throwingResume
+ _swift_continuation_throwingResumeWithError
+ _swift_deallocPartialClassInstance
+ _swift_task_switch
+ _symbolic SSSg
+ _symbolic Say_____GIego_ 7Rapport23SPAKE2PlusConfigurationV
+ _symbolic SbIeyBy_
+ _symbolic SccySaySo10RPIdentityCG______pG s5ErrorP
+ _symbolic So6NSLockC
+ _symbolic _____ 10Foundation4UUIDV
+ _symbolic _____ 7Rapport12RPThreadSafeC
+ _symbolic _____ 7Rapport16RPPairingPINInfoC
+ _symbolic _____ 7Rapport26RPPairingTemporaryIdentityV
+ _symbolic _____ 7Rapport26RPPairingTemporaryIdentityV10CodingKeys33_4096031F76CFA760152ED9A42AB523CELLO
+ _symbolic _____ 7Rapport31RPPairingBonjourResolveResponseC
+ _symbolic _____ 7Rapport31RPPairingBonjourResolveResponseC10CodingKeys33_4096031F76CFA760152ED9A42AB523CELLO
+ _symbolic _____XMT 7Network12NWParametersC
+ _symbolic ______p s5ErrorP
+ _symbolic ______pSgIeyBy_ So15OS_sec_identityP
+ _symbolic _____y_____G s22KeyedDecodingContainerV 7Rapport26RPPairingTemporaryIdentityV10CodingKeys33_4096031F76CFA760152ED9A42AB523CELLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 7Rapport31RPPairingBonjourResolveResponseC10CodingKeys33_4096031F76CFA760152ED9A42AB523CELLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 7Rapport26RPPairingTemporaryIdentityV10CodingKeys33_4096031F76CFA760152ED9A42AB523CELLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 7Rapport31RPPairingBonjourResolveResponseC10CodingKeys33_4096031F76CFA760152ED9A42AB523CELLO
- +[RPNWFramer setupDaemonFramer:receiveHandler:closeHandler:]
- +[RPNWFramer startConnection:]
- +[RPNWFramer startConnection:].cold.1
- +[RPNWFramer writeControlOnFramer:type:error:]
- +[RPNWFramer writeErrorOnFramer:error:]
- +[RPNWFramer writeErrorOnFramer:error:].cold.1
- ___46+[RPNWFramer writeControlOnFramer:type:error:]_block_invoke
- ___46+[RPNWFramer writeControlOnFramer:type:error:]_block_invoke.cold.1
- ___46+[RPNWFramer writeControlOnFramer:type:error:]_block_invoke.cold.2
- ___60+[RPNWFramer setupDaemonFramer:receiveHandler:closeHandler:]_block_invoke
- ___60+[RPNWFramer setupDaemonFramer:receiveHandler:closeHandler:]_block_invoke.cold.1
- ___60+[RPNWFramer setupDaemonFramer:receiveHandler:closeHandler:]_block_invoke.cold.2
- ___60+[RPNWFramer setupDaemonFramer:receiveHandler:closeHandler:]_block_invoke.cold.3
- ___60+[RPNWFramer setupDaemonFramer:receiveHandler:closeHandler:]_block_invoke.cold.4
- ___60+[RPNWFramer setupDaemonFramer:receiveHandler:closeHandler:]_block_invoke.cold.5
- ___60+[RPNWFramer setupDaemonFramer:receiveHandler:closeHandler:]_block_invoke_2
- ___60+[RPNWFramer setupDaemonFramer:receiveHandler:closeHandler:]_block_invoke_3
- ___60+[RPNWFramer setupDaemonFramer:receiveHandler:closeHandler:]_block_invoke_3.cold.1
- ___60+[RPNWFramer setupDaemonFramer:receiveHandler:closeHandler:]_block_invoke_3.cold.2
- ___60+[RPNWFramer setupDaemonFramer:receiveHandler:closeHandler:]_block_invoke_4
- ___60+[RPNWFramer setupDaemonFramer:receiveHandler:closeHandler:]_block_invoke_4.cold.1
- ___60+[RPNWFramer setupDaemonFramer:receiveHandler:closeHandler:]_block_invoke_5
- ___60+[RPNWFramer setupDaemonFramer:receiveHandler:closeHandler:]_block_invoke_5.cold.1
- ___block_descriptor_61_e8_32s_e5_v8?0ls32l8
- ___block_descriptor_80_e8_32s40bs48bs56r64r72r_e32_Q16?0"NSObject<OS_nw_framer>"8lr56l8r64l8r72l8s40l8s48l8s32l8
- ___block_literal_global.203
- ___block_literal_global.30
- ___block_literal_global.47
- ___block_literal_global.55
- ___block_literal_global.62
- ___nwrapport_copy_protocol_definition_block_invoke.53
- ___nwrapport_copy_protocol_definition_block_invoke.53.cold.1
- ___nwrapport_copy_protocol_definition_block_invoke.56
- ___nwrapport_copy_protocol_definition_block_invoke.56.cold.1
- _objc_msgSend$writeControlOnFramer:type:error:
CStrings:
+ "%@ Framer is not set, failed to to write CTRL message %s, error=%d (%s) on framer"
+ "%@ Invalid message type, closing connection"
+ "%@ Received CLOSE message"
+ "%@ Sending error (%d) to client app connection\n"
+ "%@ Starting connection by writing magic value (RPNW_CONTROL_HANDSHAKE)\n"
+ "%@ Wrote CTRL message %s on framer=%@\n"
+ "%@ Wrote CTRL message %s, error=%d (%s) on framer=%@\n"
+ "%@: using ratcheted irk: %{private}@"
+ "%p"
+ "+[RPNWFramer setupDaemonFramer:token:receiveHandler:closeHandler:]_block_invoke"
+ "+[RPNWFramer setupDaemonFramer:token:receiveHandler:closeHandler:]_block_invoke_3"
+ "+[RPNWFramer setupDaemonFramer:token:receiveHandler:closeHandler:]_block_invoke_4"
+ "+[RPNWFramer setupDaemonFramer:token:receiveHandler:closeHandler:]_block_invoke_5"
+ "+[RPNWFramer startConnection:token:]"
+ "+[RPNWFramer writeControlOnFramer:type:error:token:]"
+ "+[RPNWFramer writeControlOnFramer:type:error:token:]_block_invoke"
+ "+[RPNWFramer writeErrorOnFramer:token:error:]"
+ "B40@0:8@16i24C28@32"
+ "OS_sec_identity"
+ "Rapport.RPPairingBonjourResolveResponse"
+ "Rapport.RPPairingPINInfo"
+ "T@\"NSData\",N,R"
+ "T@\"NSDictionary\",&,N,V_txtRecord"
+ "T@\"NSString\",N,R"
+ "T@\"NSUUID\",N,R"
+ "Unable to retrieve ratcheted IRK"
+ "_TtC7Rapport16RPPairingPINInfo"
+ "_TtC7Rapport31RPPairingBonjourResolveResponse"
+ "_applicationServicePrePairing._tcp"
+ "_txtRecord"
+ "_value"
+ "appendFormat:"
+ "application-service-pairing-client"
+ "application-service-pairing-context"
+ "bonjourServiceID"
+ "client_identity"
+ "contactImageData"
+ "familyName"
+ "givenName"
+ "initWithServerPublicKey:bonjourServiceID:"
+ "lock"
+ "pake"
+ "pin"
+ "serverPublicKey"
+ "server_identity"
+ "setTxtRecord:"
+ "setupDaemonFramer:token:receiveHandler:closeHandler:"
+ "startConnection:token:"
+ "txtRecord"
+ "unlock"
+ "v36@0:8@16@24C32"
+ "v48@0:8@16@24@?32@?40"
+ "writeControlOnFramer:type:error:token:"
+ "writeErrorOnFramer:token:error:"
- "+[RPNWFramer setupDaemonFramer:receiveHandler:closeHandler:]_block_invoke"
- "+[RPNWFramer setupDaemonFramer:receiveHandler:closeHandler:]_block_invoke_3"
- "+[RPNWFramer setupDaemonFramer:receiveHandler:closeHandler:]_block_invoke_4"
- "+[RPNWFramer setupDaemonFramer:receiveHandler:closeHandler:]_block_invoke_5"
- "+[RPNWFramer startConnection:]"
- "+[RPNWFramer writeControlOnFramer:type:error:]_block_invoke"
- "+[RPNWFramer writeErrorOnFramer:error:]"
- "B32@0:8@16i24C28"
- "Creating connection by writing magic value\n"
- "Invalid message type, closing connection"
- "Received CLOSE message"
- "Sending error (%d) to client app connection\n"
- "Wrote CTRL message %s on framer=%@\n"
- "Wrote CTRL message %s, error=%d (%s) on framer=%@\n"
- "setupDaemonFramer:receiveHandler:closeHandler:"
- "startConnection:"
- "v28@0:8@16C24"
- "v40@0:8@16@?24@?32"
- "writeControlOnFramer:type:error:"
- "writeErrorOnFramer:error:"

```
