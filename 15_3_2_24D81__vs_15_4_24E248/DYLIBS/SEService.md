## SEService

> `/System/Library/PrivateFrameworks/SEService.framework/Versions/A/SEService`

```diff

-53.2.0.0.0
-  __TEXT.__text: 0x8cda8
-  __TEXT.__auth_stubs: 0x13d0
-  __TEXT.__objc_methlist: 0x23a0
-  __TEXT.__const: 0x7840
-  __TEXT.__gcc_except_tab: 0x182c
-  __TEXT.__cstring: 0x4ea1
-  __TEXT.__oslogstring: 0xda2
-  __TEXT.__swift5_typeref: 0x1cc8
-  __TEXT.__swift5_reflstr: 0x911
-  __TEXT.__swift5_assocty: 0xd8
-  __TEXT.__constg_swiftt: 0x13d0
-  __TEXT.__swift5_fieldmd: 0x1544
-  __TEXT.__swift5_proto: 0x6c0
-  __TEXT.__swift5_types: 0x1f4
+54.21.1.0.0
+  __TEXT.__text: 0x90560
+  __TEXT.__auth_stubs: 0x14e0
+  __TEXT.__objc_methlist: 0x2ca8
+  __TEXT.__const: 0x7b30
+  __TEXT.__gcc_except_tab: 0x1888
+  __TEXT.__cstring: 0x4c81
+  __TEXT.__oslogstring: 0x1032
+  __TEXT.__swift5_typeref: 0x1dfe
+  __TEXT.__swift5_reflstr: 0x9d1
+  __TEXT.__swift5_assocty: 0x138
+  __TEXT.__constg_swiftt: 0x14f8
+  __TEXT.__swift5_fieldmd: 0x1604
+  __TEXT.__swift5_proto: 0x6dc
+  __TEXT.__swift5_types: 0x20c
   __TEXT.__swift5_builtin: 0x8c
-  __TEXT.__swift5_mpenum: 0x38
-  __TEXT.__swift5_capture: 0x2e8
+  __TEXT.__swift5_mpenum: 0x30
+  __TEXT.__swift5_capture: 0x3d0
+  __TEXT.__swift_as_entry: 0xa8
+  __TEXT.__swift_as_ret: 0x80
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x29c0
-  __TEXT.__eh_frame: 0x3070
+  __TEXT.__unwind_info: 0x29b0
+  __TEXT.__eh_frame: 0x31e0
   __TEXT.__objc_classname: 0x50d
-  __TEXT.__objc_methname: 0x6e16
-  __TEXT.__objc_methtype: 0x2535
-  __TEXT.__objc_stubs: 0x3720
-  __DATA_CONST.__got: 0x470
-  __DATA_CONST.__const: 0x558
-  __DATA_CONST.__objc_classlist: 0x1e8
+  __TEXT.__objc_methname: 0x6ff2
+  __TEXT.__objc_methtype: 0x25ca
+  __TEXT.__objc_stubs: 0x3780
+  __DATA_CONST.__got: 0x478
+  __DATA_CONST.__const: 0x4e0
+  __DATA_CONST.__objc_classlist: 0x200
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1478
+  __DATA_CONST.__objc_selrefs: 0x1558
   __DATA_CONST.__objc_protorefs: 0x78
   __DATA_CONST.__objc_superrefs: 0xc8
   __DATA_CONST.__objc_arraydata: 0xb8
-  __AUTH_CONST.__auth_got: 0x9f8
-  __AUTH_CONST.__const: 0x4218
-  __AUTH_CONST.__cfstring: 0x30a0
-  __AUTH_CONST.__objc_const: 0x6cd0
+  __AUTH_CONST.__auth_got: 0xa80
+  __AUTH_CONST.__const: 0x4628
+  __AUTH_CONST.__cfstring: 0x3000
+  __AUTH_CONST.__objc_const: 0x6090
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH.__objc_data: 0x18d0
-  __AUTH.__data: 0x538
-  __DATA.__objc_ivar: 0x324
-  __DATA.__data: 0x22a8
-  __DATA.__bss: 0xd830
-  __DATA.__common: 0x80
+  __AUTH.__objc_data: 0x1988
+  __AUTH.__data: 0x668
+  __DATA.__objc_ivar: 0x330
+  __DATA.__data: 0x2430
+  __DATA.__bss: 0xdbc0
+  __DATA.__common: 0x88
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CryptoTokenKit.framework/Versions/A/CryptoTokenKit
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 85B85F7B-3A93-3AF4-B9F4-25C783196F66
-  Functions: 3403
-  Symbols:   3512
-  CStrings:  2441
+  UUID: B01E1B40-8469-3D38-9BBE-BCC6DA963D9C
+  Functions: 3494
+  Symbols:   3613
+  CStrings:  2458
 
Symbols:
+ +[SEFidoKeyService shared].cold.1
+ +[SESClient sharedClient].cold.1
+ +[SESPrivacyKeyManager sharedManager].cold.1
+ +[SESSessionManager sharedInstance].cold.1
+ +[SESSessionManagerCallbackInterface interface].cold.1
+ +[SESSessionManagerInterface interface].cold.1
+ -[SEEndPoint keyRole]
+ -[SEEndPoint setKeyRole:]
+ -[SEEndPoint setShareInitiatorCertificateChainData:]
+ -[SEEndPoint shareInitiatorCertificateChainData]
+ -[SEEndPointConfiguration auth1SignallingBitmap]
+ -[SEEndPointConfiguration setAuth1SignallingBitmap:]
+ GCC_except_table101
+ GCC_except_table104
+ GCC_except_table106
+ GCC_except_table108
+ GCC_except_table110
+ GCC_except_table112
+ GCC_except_table114
+ GCC_except_table116
+ GCC_except_table118
+ GCC_except_table120
+ GCC_except_table122
+ GCC_except_table124
+ GCC_except_table126
+ GCC_except_table128
+ GCC_except_table130
+ GCC_except_table134
+ GCC_except_table29
+ GCC_except_table35
+ GCC_except_table49
+ GCC_except_table62
+ GCC_except_table72
+ GCC_except_table77
+ GCC_except_table78
+ GCC_except_table81
+ GCC_except_table85
+ GCC_except_table87
+ GCC_except_table89
+ GCC_except_table92
+ GCC_except_table95
+ GCC_except_table99
+ OBJC_IVAR_$_SEEndPoint._keyRole
+ OBJC_IVAR_$_SEEndPoint._shareInitiatorCertificateChainData
+ OBJC_IVAR_$_SEEndPointConfiguration._auth1SignallingBitmap
+ SESClientSetMachServiceName.cold.1
+ _OBJC_$_PROP_LIST_SESSession.561
+ _OBJC_CLASS_$__TtC9SEService15SESOnceOnlyTask
+ _OBJC_CLASS_$__TtC9SEService22SESOnceOnlyTaskManager
+ _OBJC_METACLASS_$__TtC9SEService15SESOnceOnlyTask
+ _OBJC_METACLASS_$__TtC9SEService22SESOnceOnlyTaskManager
+ _OUTLINED_FUNCTION_0
+ _PROTOCOLS__TtC9SEService10SESnapshot.24
+ _PROTOCOLS__TtC9SEService11MemoryUsage.22
+ _PROTOCOLS__TtC9SEService16AppletMemoryInfo.16
+ _SESDesignatedKeyCopyAccessControlForBioBoundCredentials
+ _SESEndPointIsSharingEnabled
+ _SESExternalProviderCredentialPresent
+ __23-[SEEndPoint dumpState]_block_invoke.1195
+ __26-[SESAssertion invalidate]_block_invoke.475
+ __28-[SESSessionManager connect]_block_invoke.532
+ __29-[SESClient connectToService]_block_invoke.480
+ __29-[SESDCKAssertion invalidate]_block_invoke.478
+ __30-[SESDCKSession setActiveKey:]_block_invoke.476
+ __30-[SESSession endRemoteSession]_block_invoke.481
+ __31-[SESACWGSession setActiveKey:]_block_invoke.476
+ __59-[SESRKESession isPassiveEntryAvailable:isAvailable:error:]_block_invoke.476
+ __62-[SESSessionManager startRKESessionWithOptions:startCallback:]_block_invoke.486
+ __63-[SESSessionManager startACWGSessionWithOptions:startCallback:]_block_invoke.488
+ __72-[SESSessionManager startDigitalCarKeySessionWithOptions:startCallback:]_block_invoke.479
+ __72-[SESSessionManager startDigitalCarKeySessionWithOptions:startCallback:]_block_invoke.483
+ __73-[SESSessionManager startDCKAssertionForKeyIdentifier:withOptions:error:]_block_invoke.543
+ __88+[SESSessionManager pauseRangingForReaderIdentifier:durationInSec:withAppletIdentifier:]_block_invoke.540
+ __91-[SESSessionManager startAssertionForKeyIdentifier:withAppletIdentifier:withOptions:error:]_block_invoke.546
+ __DATA__TtC9SEService15SESOnceOnlyTask
+ __DATA__TtC9SEService22SESOnceOnlyTaskManager
+ __DATA__TtC9SEService23SESNotifyEventPublisher
+ __INSTANCE_METHODS__TtC9SEService15SESOnceOnlyTask
+ __INSTANCE_METHODS__TtC9SEService22SESOnceOnlyTaskManager
+ __IVARS__TtC9SEService15SESOnceOnlyTask
+ __IVARS__TtC9SEService22SESOnceOnlyTaskManager
+ __IVARS__TtC9SEService23SESNotifyEventPublisher
+ __METACLASS_DATA__TtC9SEService15SESOnceOnlyTask
+ __METACLASS_DATA__TtC9SEService22SESOnceOnlyTaskManager
+ __METACLASS_DATA__TtC9SEService23SESNotifyEventPublisher
+ __SESEndPointUpdateWithBlock_block_invoke.493
+ ___SESEndPointIsSharingEnabled_block_invoke
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ ___swift_project_boxed_opaque_existential_0Tm
+ __block_literal_global.477
+ __block_literal_global.480
+ __block_literal_global.482
+ __block_literal_global.558
+ __swiftEmptySetSingleton
+ _associated conformance 9SEService23SESNotifyEventPublisherC12NotificationOSHAASQ
+ _associated conformance 9SEService23SESNotifyEventPublisherC5StateVs10SetAlgebraAASQ
+ _associated conformance 9SEService23SESNotifyEventPublisherC5StateVs10SetAlgebraAAs25ExpressibleByArrayLiteral
+ _associated conformance 9SEService23SESNotifyEventPublisherC5StateVs9OptionSetAASY
+ _associated conformance 9SEService23SESNotifyEventPublisherC5StateVs9OptionSetAAs0G7Algebra
+ _dispatch_group_create
+ _dispatch_group_enter
+ _dispatch_group_leave
+ _notify_cancel
+ _notify_get_state
+ _notify_is_valid_token
+ _notify_register_check
+ _notify_set_state
+ _objc_msgSend$boolForKey:
+ _objc_msgSend$getSESEndpointTSMDictionary:reply:
+ _objc_msgSend$isSharingEnabledForManufacturer:brand:uuid:reply:
+ _objc_msgSend$keyRole
+ _objc_msgSend$listEndPointsWithProxy:mandatoryReconciliation:reply:
+ _objc_msgSend$setAuth1SignallingBitmap:
+ _objc_msgSend$shareInitiatorCertificateChainData
+ _symbolic IeyB_
+ _symbolic SDySSypGIegr_
+ _symbolic Say_____G 10Foundation4DataV
+ _symbolic Say_____G 9SEService17JPKIInternalTypesO16DigitalSignatureC
+ _symbolic Say_____G___________t 10Foundation4DataV 9SEService17JPKIInternalTypesO15CertificateTypeO AF26UserAuthenticationInternalO
+ _symbolic ScCyyt_____G s5NeverO
+ _symbolic SccySay_____G______pG 9SEService11ReservationC s5ErrorP
+ _symbolic Sccy_____Sg______pG 9SEService11ReservationC s5ErrorP
+ _symbolic Sccy___________pG 9SEService11ReservationC s5ErrorP
+ _symbolic Sccy___________pG 9SEService16DeviceCapabilityC s5ErrorP
+ _symbolic Sccy___________pG 9SEService16ReservationStateC s5ErrorP
+ _symbolic Sccyyt______pG s5ErrorP
+ _symbolic Shy_____G 9SEService15SESOnceOnlyTaskC
+ _symbolic So17OS_dispatch_groupC
+ _symbolic _____ 9SEService15SESOnceOnlyTaskC
+ _symbolic _____ 9SEService22SESOnceOnlyTaskManagerC
+ _symbolic _____ 9SEService23SESNotifyEventPublisherC
+ _symbolic _____ 9SEService23SESNotifyEventPublisherC0C0V
+ _symbolic _____ 9SEService23SESNotifyEventPublisherC12NotificationO
+ _symbolic _____ 9SEService23SESNotifyEventPublisherC5StateV
+ _symbolic _____ s5Int32V
+ _symbolic _____ s6UInt64V
+ _symbolic _____y_____G s11_SetStorageC 9SEService15SESOnceOnlyTaskC
+ _symbolic yyc
+ block_copy_helper.101
+ block_copy_helper.30
+ block_copy_helper.35
+ block_copy_helper.43
+ block_copy_helper.48
+ block_copy_helper.55
+ block_copy_helper.62
+ block_copy_helper.67
+ block_copy_helper.71
+ block_copy_helper.79
+ block_copy_helper.84
+ block_copy_helper.92
+ block_descriptor.103
+ block_descriptor.32
+ block_descriptor.37
+ block_descriptor.45
+ block_descriptor.50
+ block_descriptor.57
+ block_descriptor.64
+ block_descriptor.69
+ block_descriptor.73
+ block_descriptor.81
+ block_descriptor.86
+ block_descriptor.94
+ block_destroy_helper.102
+ block_destroy_helper.31
+ block_destroy_helper.36
+ block_destroy_helper.44
+ block_destroy_helper.49
+ block_destroy_helper.56
+ block_destroy_helper.63
+ block_destroy_helper.68
+ block_destroy_helper.72
+ block_destroy_helper.80
+ block_destroy_helper.85
+ block_destroy_helper.93
+ getEndpointQueue.cold.1
- GCC_except_table100
- GCC_except_table102
- GCC_except_table105
- GCC_except_table107
- GCC_except_table109
- GCC_except_table111
- GCC_except_table113
- GCC_except_table115
- GCC_except_table117
- GCC_except_table119
- GCC_except_table121
- GCC_except_table123
- GCC_except_table125
- GCC_except_table127
- GCC_except_table129
- GCC_except_table133
- GCC_except_table40
- GCC_except_table45
- GCC_except_table58
- GCC_except_table60
- GCC_except_table76
- GCC_except_table79
- GCC_except_table83
- GCC_except_table86
- GCC_except_table88
- GCC_except_table90
- GCC_except_table93
- GCC_except_table96
- _OBJC_$_PROP_LIST_SESSession.552
- _PROTOCOLS__TtC9SEService10SESnapshot.22
- _PROTOCOLS__TtC9SEService11MemoryUsage.18
- _PROTOCOLS__TtC9SEService16AppletMemoryInfo.12
- _SESEndpointGetSupportedLyonVersions
- __23-[SEEndPoint dumpState]_block_invoke.1175
- __26-[SESAssertion invalidate]_block_invoke.466
- __28-[SESSessionManager connect]_block_invoke.523
- __29-[SESClient connectToService]_block_invoke.471
- __29-[SESDCKAssertion invalidate]_block_invoke.469
- __30-[SESDCKSession setActiveKey:]_block_invoke.467
- __30-[SESSession endRemoteSession]_block_invoke.472
- __31-[SESACWGSession setActiveKey:]_block_invoke.467
- __59-[SESRKESession isPassiveEntryAvailable:isAvailable:error:]_block_invoke.467
- __62-[SESSessionManager startRKESessionWithOptions:startCallback:]_block_invoke.477
- __63-[SESSessionManager startACWGSessionWithOptions:startCallback:]_block_invoke.479
- __72-[SESSessionManager startDigitalCarKeySessionWithOptions:startCallback:]_block_invoke.470
- __72-[SESSessionManager startDigitalCarKeySessionWithOptions:startCallback:]_block_invoke.474
- __73-[SESSessionManager startDCKAssertionForKeyIdentifier:withOptions:error:]_block_invoke.534
- __88+[SESSessionManager pauseRangingForReaderIdentifier:durationInSec:withAppletIdentifier:]_block_invoke.531
- __91-[SESSessionManager startAssertionForKeyIdentifier:withAppletIdentifier:withOptions:error:]_block_invoke.537
- __SESEndPointUpdateWithBlock_block_invoke.484
- ___SESEndPointList_block_invoke
- ___SESEndPointTSMDictionary_block_invoke_2
- ___block_descriptor_32_e20_B16?0"SEEndPoint"8l
- ___block_descriptor_32_e34_B16?0"SESEndPointContainerInfo"8l
- __block_literal_global.468
- __block_literal_global.471
- __block_literal_global.473
- __block_literal_global.549
- __block_literal_global.765
- __block_literal_global.771
- _objc_msgSend$appletAID
- _objc_msgSend$arrayWithCapacity:
- _objc_msgSend$isSuspended
- _objc_msgSend$listEndPointsWithProxy:reply:
- _symbolic ________________t 10Foundation4DataV 9SEService17JPKIInternalTypesO15CertificateTypeO AF26UserAuthenticationInternalO
- block_copy_helper.39
- block_copy_helper.56
- block_copy_helper.69
- block_copy_helper.80
- block_copy_helper.89
- block_descriptor.30
- block_descriptor.33
- block_descriptor.41
- block_descriptor.44
- block_descriptor.53
- block_descriptor.58
- block_descriptor.61
- block_descriptor.63
- block_descriptor.71
- block_descriptor.74
- block_descriptor.82
- block_descriptor.91
- block_destroy_helper.40
- block_destroy_helper.57
- block_destroy_helper.70
- block_destroy_helper.81
- block_destroy_helper.90
CStrings:
+ "\tkeyRole : 0x%04X,\n"
+ "\tshareInitiatorCertificateChainData : %@\n"
+ "Attempted to insert duplicate task with identifier %s"
+ "Error sending request %s"
+ "Got state %llu for %s"
+ "One-time task %s already ran"
+ "Posted %s"
+ "SESOnceOnlyTask("
+ "SEService.SESOnceOnlyTask"
+ "Successfully deregistered task with identifier %s"
+ "Successfully run all one-time tasks"
+ "Successfully run one-time task %s"
+ "T@\"NSData\",C,V_shareInitiatorCertificateChainData"
+ "T@\"NSNumber\",C,V_keyRole"
+ "TS,V_auth1SignallingBitmap"
+ "Unable to deregister task with identifier %s"
+ "Unable to get state for %s with status %d"
+ "Unable to post %s with status %d"
+ "Unable to register %s"
+ "Unable to register for %s with status %d"
+ "Unable to set state for %s with status %d"
+ "Unexpected status %d while canceling token for %s"
+ "Vv32@0:8@\"<SEProxyInterface>\"16@?<v@?@\"NSDictionary\"@\"NSError\">24"
+ "Vv36@0:8@\"<SEProxyInterface>\"16B24@?<v@?@\"NSArray\"@\"NSError\">28"
+ "Vv36@0:8@16B24@?28"
+ "_TtC9SEService15SESOnceOnlyTask"
+ "_TtC9SEService22SESOnceOnlyTaskManager"
+ "_TtC9SEService23SESNotifyEventPublisher"
+ "_auth1SignallingBitmap"
+ "_keyRole"
+ "_shareInitiatorCertificateChainData"
+ "auth1SignallingBitmap"
+ "boolForKey:"
+ "com.apple.seserviced.secure-element-credential-presence"
+ "getSESEndpointTSMDictionary:reply:"
+ "initWithIdentifier:task:"
+ "isSharingEnabledForManufacturer:brand:uuid:reply:"
+ "keyRole"
+ "listEndPointsWithProxy:mandatoryReconciliation:reply:"
+ "removeObjectForKey:"
+ "secPresenceNotificationToken"
+ "setAuth1SignallingBitmap:"
+ "setKeyRole:"
+ "setShareInitiatorCertificateChainData:"
+ "setValue:forKey:"
+ "shareInitiatorCertificateChainData"
+ "task"
+ "tasks"
+ "vienna.credential.present"
- "B16@?0@\"SESEndPointContainerInfo\"8"
- "Can't construct Array with count < 0"
- "Error sending request "
- "Failed to list containers"
- "Failed to list endpoints"
- "Insufficient space allocated to copy string contents"
- "PTKeys"
- "Swift/Array.swift"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "appletAid"
- "arrayWithCapacity:"
- "carOemProprietaryData"
- "ephemeralPK"
- "invalid Collection: less than 'count' elements in collection"
- "keyId"
- "listEndPointsWithProxy:reply:"
- "ptaContainers"
- "receiverPKID"
- "terminationAttestation"

```
