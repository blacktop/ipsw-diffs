## SESShared

> `/System/Library/PrivateFrameworks/SESShared.framework/SESShared`

```diff

-65.3.1.0.0
-  __TEXT.__text: 0xea1c
-  __TEXT.__auth_stubs: 0x7d0
-  __TEXT.__objc_methlist: 0x7bc
-  __TEXT.__const: 0xc38
-  __TEXT.__cstring: 0x1750
-  __TEXT.__gcc_except_tab: 0x8c
-  __TEXT.__oslogstring: 0x625
-  __TEXT.__swift5_typeref: 0x4a
+70.31.1.0.0
+  __TEXT.__text: 0xf254
+  __TEXT.__objc_methlist: 0x930
+  __TEXT.__const: 0xc20
+  __TEXT.__cstring: 0x1c5a
+  __TEXT.__gcc_except_tab: 0xa8
+  __TEXT.__oslogstring: 0x796
+  __TEXT.__swift5_typeref: 0x40
   __TEXT.__swift5_fieldmd: 0x48
   __TEXT.__constg_swiftt: 0x64
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_proto: 0x8
   __TEXT.__swift5_reflstr: 0xf
-  __TEXT.__swift5_capture: 0x40
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x378
-  __TEXT.__eh_frame: 0xb8
-  __TEXT.__objc_classname: 0xf9
-  __TEXT.__objc_methname: 0x11df
-  __TEXT.__objc_methtype: 0x3f7
-  __TEXT.__objc_stubs: 0xcc0
-  __DATA_CONST.__got: 0x170
-  __DATA_CONST.__const: 0x8f0
-  __DATA_CONST.__objc_classlist: 0x50
+  __TEXT.__unwind_info: 0x3d0
+  __TEXT.__eh_frame: 0xb0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0xbc0
+  __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x628
-  __DATA_CONST.__objc_superrefs: 0x30
+  __DATA_CONST.__objc_selrefs: 0x6f0
+  __DATA_CONST.__objc_superrefs: 0x48
   __DATA_CONST.__objc_arraydata: 0x80
-  __AUTH_CONST.__auth_got: 0x3f8
-  __AUTH_CONST.__const: 0x1f8
-  __AUTH_CONST.__cfstring: 0x2460
-  __AUTH_CONST.__objc_const: 0xbb0
+  __DATA_CONST.__got: 0x1a0
+  __AUTH_CONST.__const: 0x230
+  __AUTH_CONST.__cfstring: 0x2a40
+  __AUTH_CONST.__objc_const: 0xf00
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_intobj: 0x30
-  __DATA.__objc_ivar: 0x6c
-  __DATA.__data: 0x38
-  __DATA_DIRTY.__objc_data: 0x320
-  __DATA_DIRTY.__bss: 0x50
+  __AUTH_CONST.__auth_got: 0x4d0
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0x94
+  __DATA.__data: 0x28
+  __DATA.__bss: 0x10
+  __DATA_DIRTY.__objc_data: 0x3c0
+  __DATA_DIRTY.__bss: 0x70
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CryptoKit.framework/CryptoKit
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 7AB48F19-037C-3ADC-A57F-4AEA8C4FAEA0
-  Functions: 290
-  Symbols:   1148
-  CStrings:  968
+  UUID: A70DBAD9-EA9D-3507-8589-CE545D2C24A6
+  Functions: 333
+  Symbols:   1387
+  CStrings:  756
 
Symbols:
+ +[CertificationLogging logRawAPDU:encrypted:]
+ +[CertificationLogging logRawAPDU:encrypted:].cold.1
+ +[NSData(DERItem) ses_dataWithDERItem:]
+ +[NSData(HexString) ses_dataWithHexString:]
+ +[NSData(Integer) ses_withU16BE:]
+ +[NSData(Random) ses_randomData:]
+ +[NSString(AsciiData) ses_stringWithAsciiData:]
+ +[SESDarwinNotificationMonitor kickoff]
+ +[SESDarwinNotificationMonitor registerDelegate:forEvent:]
+ +[SESDarwinNotificationMonitor sharedObject]
+ +[SESDarwinNotificationMonitor sharedObject].cold.1
+ +[SESXPCEventListener kickoff]
+ +[SESXPCEventListener registerOnStream:forEvent:handler:]
+ +[SESXPCEventListener sharedObject]
+ +[SESXPCEventListener sharedObject].cold.1
+ -[NFSecureXPCEventPublisher .cxx_destruct]
+ -[NFSecureXPCEventPublisher available]
+ -[NFSecureXPCEventPublisher connection]
+ -[NFSecureXPCEventPublisher dealloc]
+ -[NFSecureXPCEventPublisher initWithMachPort:queue:]
+ -[NFSecureXPCEventPublisher queue]
+ -[NFSecureXPCEventPublisher sendEvent:]
+ -[NFSecureXPCEventPublisher serviceName]
+ -[NFSecureXPCEventPublisher setAvailable:]
+ -[NFSecureXPCEventPublisher setConnection:]
+ -[NFSecureXPCEventPublisher setQueue:]
+ -[NFSecureXPCEventPublisher setServiceName:]
+ -[NSArray(Functional) ses_allSatisfy:]
+ -[NSArray(Functional) ses_filter:]
+ -[NSArray(Functional) ses_filterMap:]
+ -[NSArray(Functional) ses_find:]
+ -[NSArray(Random) ses_randomElement]
+ -[NSData(Base64) ses_base64]
+ -[NSData(DERItem) ses_DERItem]
+ -[NSData(DERItem) ses_isEqualToDERItem:]
+ -[NSData(HexString) ses_asHexString]
+ -[NSData(Integer) ses_s32BE:]
+ -[NSData(Integer) ses_u16BE:]
+ -[NSData(Integer) ses_u16LE:]
+ -[NSData(Integer) ses_u32BE:]
+ -[NSData(Integer) ses_u32LE:]
+ -[NSData(Integer) ses_u64BE:]
+ -[NSData(Integer) ses_u64LE:]
+ -[NSData(Integer) ses_u8:]
+ -[NSMutableArray(queue) ses_popFirst]
+ -[NSMutableArray(queue) ses_pushLast:]
+ -[NSMutableData(Append) ses_appendU16BE:]
+ -[NSMutableData(Append) ses_appendU16LE:]
+ -[NSMutableData(Append) ses_appendU32BE:]
+ -[NSMutableData(Append) ses_appendU32LE:]
+ -[NSMutableData(Append) ses_appendU64BE:]
+ -[NSMutableData(Append) ses_appendU64LE:]
+ -[NSMutableData(Append) ses_appendU8:]
+ -[NSSet(Functional) ses_allSatisfy:]
+ -[NSSet(Functional) ses_contains:]
+ -[NSSet(Functional) ses_filter:]
+ -[NSSet(Functional) ses_filterMap:]
+ -[NSSet(Functional) ses_find:]
+ -[NSString(AsciiData) ses_asAsciiData]
+ -[NSString(HexString) ses_hexStringAsData]
+ -[SESDarwinNotificationMonitor .cxx_destruct]
+ -[SESDarwinNotificationMonitor _handleEvent:]
+ -[SESDarwinNotificationMonitor initWithQueue:]
+ -[SESXPCEventListener .cxx_destruct]
+ -[SESXPCEventListener _dumpState]
+ -[SESXPCEventListener _handleEvent:payload:]
+ -[SESXPCEventListener init]
+ GCC_except_table1
+ GCC_except_table5
+ GCC_except_table7
+ _CA_AliroAnalyticsReaderKeyType
+ _CA_AliroAnalyticsVerticalType
+ _CA_AvgConnectionDurationPerPeripheral
+ _CA_BiolockCount
+ _CA_BtDisconnectionCount
+ _CA_DSKAnalyticsBtConnectionDuration
+ _CA_DSKAnalyticsBtOutOfOrderMessageCount
+ _CA_DSKAnalyticsBtTimeExtensionInitiatedByDeviceCount
+ _CA_DSKAnalyticsBtTimeExtensionInitiatedByLockCount
+ _CA_DSKAnalyticsDeviceInitatedRangingAttemptsCount
+ _CA_DSKAnalyticsDeviceStatus
+ _CA_DSKAnalyticsDisconnectReason
+ _CA_DSKAnalyticsInfoBrand
+ _CA_DSKAnalyticsInfoFWVersion
+ _CA_DSKAnalyticsInfoManufacturer
+ _CA_DSKAnalyticsInfoProductID
+ _CA_DSKAnalyticsInfoVendorID
+ _CA_DSKAnalyticsIntentFallbackTriggered
+ _CA_DSKAnalyticsKeyType
+ _CA_DSKAnalyticsLockCapability
+ _CA_DSKAnalyticsLockSharingCapability
+ _CA_DSKAnalyticsLockStatus
+ _CA_DSKAnalyticsLockStatusAtConnection
+ _CA_DSKAnalyticsRangingAttemptsCount
+ _CA_DSKAnalyticsRangingDuration
+ _CA_DSKAnalyticsRangingExceptionBitmap
+ _CA_DSKAnalyticsStepUpDuration
+ _CA_DSKAnalyticsTimeSyncProcedure1Count
+ _CA_DSKAnalyticsTransactionMode
+ _CA_DSKAnalyticsUnlockCount
+ _CA_DSKAnalyticsUnlockFromOtherSourceCount
+ _CA_DSKAnalyticsUnlockSource
+ _CA_GeofenceEntryCount
+ _CA_PairingDidReceiveProductPlanIdentifier
+ _CA_PairingPairingDuration
+ _CA_PairingPairingFlow
+ _CA_PairingUsedPendingPairing
+ _CA_PairingVehicleMotionState
+ _CA_PassiveEntryDailyTransactionEventAliro
+ _CA_PassiveEntryDailyTransactionEventAlisha
+ _CA_PassiveEntrySessionEventAliro
+ _CA_PassiveEntrySessionEventAlisha
+ _CA_PendingCarKeyPairingCount
+ _CA_PendingPairingBrand
+ _CA_PendingPairingCreationFailureReason
+ _CA_PendingPairingDeletionReason
+ _CA_PendingPairingEvent
+ _CA_PendingPairingIsCreation
+ _CA_PendingPairingManufacturer
+ _CA_PendingPairingNumMagicPairingAttempts
+ _CA_PendingPairingNumPasswordAttempts
+ _CA_PendingPairingPairingTransportUsed
+ _CA_PendingPairingPendingPairingAge
+ _CA_PendingPairingReceivedUserConsent
+ _CA_PendingPairingSchedulingStrategy
+ _CA_PendingPairingSource
+ _CA_PendingPairingSourceAge
+ _CA_PendingPairingSourceLanguage
+ _CA_PendingPairingState
+ _CA_PendingPairingSupportedTransports
+ _CA_PendingPairingVehicleDetectionMechanism
+ _CA_PeripheralInitiatedResumeRangingCount
+ _CA_PeripheralInitiatedSuspendRangingCount
+ _CA_TrackingUsedPendingPairing
+ _OBJC_CLASS_$_NFSecureXPCEventPublisher
+ _OBJC_CLASS_$_NSPointerArray
+ _OBJC_CLASS_$_NSPropertyListSerialization
+ _OBJC_CLASS_$_SESDarwinNotificationMonitor
+ _OBJC_CLASS_$_SESXPCEventListener
+ _OBJC_IVAR_$_NFSecureXPCEventPublisher._available
+ _OBJC_IVAR_$_NFSecureXPCEventPublisher._connection
+ _OBJC_IVAR_$_NFSecureXPCEventPublisher._queue
+ _OBJC_IVAR_$_NFSecureXPCEventPublisher._serviceName
+ _OBJC_IVAR_$_SESDarwinNotificationMonitor._pendingNotificationIdentifiers
+ _OBJC_IVAR_$_SESDarwinNotificationMonitor._queue
+ _OBJC_IVAR_$_SESDarwinNotificationMonitor._registeredDelegates
+ _OBJC_IVAR_$_SESXPCEventListener.pendingEvents
+ _OBJC_IVAR_$_SESXPCEventListener.queue
+ _OBJC_IVAR_$_SESXPCEventListener.registeredDelegates
+ _OBJC_METACLASS_$_NFSecureXPCEventPublisher
+ _OBJC_METACLASS_$_SESDarwinNotificationMonitor
+ _OBJC_METACLASS_$_SESXPCEventListener
+ _OUTLINED_FUNCTION_11
+ __OBJC_$_CLASS_METHODS_SESDarwinNotificationMonitor
+ __OBJC_$_CLASS_METHODS_SESXPCEventListener
+ __OBJC_$_INSTANCE_METHODS_NFSecureXPCEventPublisher
+ __OBJC_$_INSTANCE_METHODS_SESDarwinNotificationMonitor
+ __OBJC_$_INSTANCE_METHODS_SESXPCEventListener
+ __OBJC_$_INSTANCE_VARIABLES_NFSecureXPCEventPublisher
+ __OBJC_$_INSTANCE_VARIABLES_SESDarwinNotificationMonitor
+ __OBJC_$_INSTANCE_VARIABLES_SESXPCEventListener
+ __OBJC_$_PROP_LIST_NFSecureXPCEventPublisher
+ __OBJC_CLASS_RO_$_NFSecureXPCEventPublisher
+ __OBJC_CLASS_RO_$_SESDarwinNotificationMonitor
+ __OBJC_CLASS_RO_$_SESXPCEventListener
+ __OBJC_METACLASS_RO_$_NFSecureXPCEventPublisher
+ __OBJC_METACLASS_RO_$_SESDarwinNotificationMonitor
+ __OBJC_METACLASS_RO_$_SESXPCEventListener
+ ___27-[SESXPCEventListener init]_block_invoke
+ ___35+[SESXPCEventListener sharedObject]_block_invoke
+ ___44+[SESDarwinNotificationMonitor sharedObject]_block_invoke
+ ___46-[SESDarwinNotificationMonitor initWithQueue:]_block_invoke
+ ___50-[CertificationLogging logEvent:message:peerUUID:]_block_invoke.67
+ ___52-[NFSecureXPCEventPublisher initWithMachPort:queue:]_block_invoke
+ ___57+[SESXPCEventListener registerOnStream:forEvent:handler:]_block_invoke
+ ___57+[SESXPCEventListener registerOnStream:forEvent:handler:]_block_invoke_2
+ ___58+[SESDarwinNotificationMonitor registerDelegate:forEvent:]_block_invoke
+ ___Block_byref_object_copy_
+ ___Block_byref_object_dispose_
+ ____log_object_block_invoke
+ ___block_descriptor_40_e8_32s_e103_^{os_state_data_s=I(?=b32I){os_state_data_decoder_s=[64c][64c]}[64c][0C]}16?0^{os_state_hints_s=I*II}8ls32l8
+ ___block_descriptor_48_e8_32s40s_e33_v16?0"NSObject<OS_xpc_object>"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40w_e33_v16?0"NSObject<OS_xpc_object>"8lw40l8s32l8
+ ___block_descriptor_72_e8_32s40s48s56s64r_e5_v8?0ls32l8s40l8s48l8s56l8r64l8
+ ___block_literal_global.32
+ ___strlcpy_chk
+ __log_object
+ __log_object.cold.1
+ __log_object.log
+ __log_object.once
+ __xpc_error_connection_interrupted
+ __xpc_error_connection_invalid
+ __xpc_error_key_description
+ __xpc_type_dictionary
+ __xpc_type_error
+ _malloc_type_calloc
+ _objc_claimAutoreleasedReturnValue
+ _objc_copyWeak
+ _objc_destroyWeak
+ _objc_initWeak
+ _objc_loadWeakRetained
+ _objc_msgSend$_dumpState
+ _objc_msgSend$_handleEvent:
+ _objc_msgSend$_handleEvent:payload:
+ _objc_msgSend$addPointer:
+ _objc_msgSend$allKeys
+ _objc_msgSend$allObjects
+ _objc_msgSend$available
+ _objc_msgSend$connection
+ _objc_msgSend$dataWithPropertyList:format:options:error:
+ _objc_msgSend$initWithQueue:
+ _objc_msgSend$keyEnumerator
+ _objc_msgSend$onDarwinNotification:
+ _objc_msgSend$onEvent:eventPayload:
+ _objc_msgSend$serviceName
+ _objc_msgSend$ses_DERItem
+ _objc_msgSend$ses_asAsciiData
+ _objc_msgSend$ses_asHexString
+ _objc_msgSend$ses_base64
+ _objc_msgSend$ses_dataWithDERItem:
+ _objc_msgSend$ses_dataWithHexString:
+ _objc_msgSend$ses_hexStringAsData
+ _objc_msgSend$setAvailable:
+ _objc_msgSend$weakObjectsPointerArray
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x5
+ _objc_retain_x8
+ _os_state_add_handler
+ _swift_release_x1
+ _swift_release_x20
+ _swift_release_x23
+ _xpc_connection_activate
+ _xpc_connection_cancel
+ _xpc_connection_create_mach_service
+ _xpc_connection_send_notification
+ _xpc_connection_set_event_handler
+ _xpc_dictionary_create_empty
+ _xpc_dictionary_get_value
+ _xpc_equal
+ _xpc_get_type
+ _xpc_string_get_string_ptr
+ _xpc_type_get_name
- +[NSData(DERItem) dataWithDERItem:]
- +[NSData(HexString) dataWithHexString:]
- +[NSData(Integer) withU16BE:]
- +[NSData(Random) randomData:]
- +[NSString(AsciiData) stringWithAsciiData:]
- -[NSArray(Functional) allSatisfy:]
- -[NSArray(Functional) filter:]
- -[NSArray(Functional) filterMap:]
- -[NSArray(Functional) find:]
- -[NSArray(Random) randomElement]
- -[NSData(Base64) base64]
- -[NSData(DERItem) DERItem]
- -[NSData(DERItem) isEqualToDERItem:]
- -[NSData(HexString) asHexString]
- -[NSData(Integer) s32BE:]
- -[NSData(Integer) u16BE:]
- -[NSData(Integer) u16LE:]
- -[NSData(Integer) u32BE:]
- -[NSData(Integer) u32LE:]
- -[NSData(Integer) u64BE:]
- -[NSData(Integer) u64LE:]
- -[NSData(Integer) u8:]
- -[NSMutableArray(queue) popFirst]
- -[NSMutableArray(queue) pushLast:]
- -[NSMutableData(Append) appendU16BE:]
- -[NSMutableData(Append) appendU16LE:]
- -[NSMutableData(Append) appendU32BE:]
- -[NSMutableData(Append) appendU32LE:]
- -[NSMutableData(Append) appendU64BE:]
- -[NSMutableData(Append) appendU64LE:]
- -[NSMutableData(Append) appendU8:]
- -[NSSet(Functional) allSatisfy:]
- -[NSSet(Functional) contains:]
- -[NSSet(Functional) filter:]
- -[NSSet(Functional) filterMap:]
- -[NSSet(Functional) find:]
- -[NSString(AsciiData) asAsciiData]
- -[NSString(HexString) hexStringAsData]
- ___50-[CertificationLogging logEvent:message:peerUUID:]_block_invoke.61
- ___swift_destroy_boxed_opaque_existential_1
- ___swift_instantiateConcreteTypeFromMangledNameAbstractV2
- ___swift_project_boxed_opaque_existential_1
- _objc_msgSend$DERItem
- _objc_msgSend$asHexString
- _objc_msgSend$base64
- _objc_msgSend$dataWithDERItem:
- _objc_msgSend$dataWithHexString:
- _objc_retain_x27
- _swift_deallocObject
- _swift_getTypeByMangledNameInContextInMetadataState2
- _symbolic _____ySWG s5SliceV
CStrings:
+ "%s"
+ "BuildOPPreTrackRequest"
+ "IgnoreExtractedPairingData"
+ "IgnoreMagicPairingPostProvisioningCooldown"
+ "Invalid event type: %s"
+ "MagicPairingBluetooth"
+ "MagicPairingNFC"
+ "Notification %@ received"
+ "PairingDataExtractionBlockedLanguages"
+ "RSSIPairing"
+ "Received event on stream %@ have %lu delegates"
+ "Registered client for stream %@ and returning %u pending events"
+ "Registered delegate for event %{public}@, pending %{public}d"
+ "SendDeviceDiscriminator"
+ "Service interrupted: %@"
+ "Service not available: %@"
+ "Service unavailable: %@"
+ "Too many notifications received, dropping event %@"
+ "Unexpected typed: %s"
+ "^{os_state_data_s=I(?=b32I){os_state_data_decoder_s=[64c][64c]}[64c][0C]}16@?0^{os_state_hints_s=I*II}8"
+ "alarm"
+ "avgConnectionDurationPerPeripheral"
+ "biolockCount"
+ "btDisconnectionCount"
+ "com.apple.kml.pendingPairingEvent"
+ "com.apple.notifyd.matching"
+ "com.apple.seserviced.connection.alisha"
+ "com.apple.seserviced.connection.lyon"
+ "com.apple.seserviced.dsk.daily.alisha"
+ "com.apple.seserviced.dsk.daily.lyon"
+ "com.apple.seserviced.sesdarwinnotification"
+ "com.apple.seserviced.sesxpclistener"
+ "creationFailureReason"
+ "dck_encrypted"
+ "deletionReason"
+ "encrypted_payload"
+ "geofenceEntryCount"
+ "infoBrand"
+ "infoManufacturer"
+ "isCreation"
+ "numMagicPairingAttempts"
+ "numPasswordAttempts"
+ "pairingDuration"
+ "pairingFlow"
+ "pairingTransportUsed"
+ "pendingCarKeyPairingCount"
+ "pendingEvents"
+ "pendingPairingAge"
+ "pendingState"
+ "peripheralInitiatedResumeRangingCount"
+ "peripheralInitiatedSuspendRangingCount"
+ "readerKeyType"
+ "receivedUserConsent"
+ "registeredStreams"
+ "schedulingStrategy"
+ "seserviced.sesxpclistener.state"
+ "source"
+ "sourceAge"
+ "sourceLanguage"
+ "supportedTransports"
+ "usedPendingPairing"
+ "vehicleDetectionMechanism"
+ "vehicleMotionState"
+ "verticalType"
- ".cxx_destruct"
- "@\"NSArray\""
- "@\"NSData\""
- "@\"NSDictionary\""
- "@\"NSMapTable\""
- "@\"NSMutableSet\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_os_log>\""
- "@\"NSString\""
- "@\"NSURL\""
- "@\"SESConfig\""
- "@16@0:8"
- "@20@0:8I16"
- "@20@0:8S16"
- "@24@0:8@16"
- "@24@0:8@?16"
- "@24@0:8I16C20"
- "@24@0:8I16I20"
- "@24@0:8I16S20"
- "@24@0:8Q16"
- "@24@0:8^@16"
- "@24@0:8r^{?=*Q}16"
- "@28@0:8@16f24"
- "@28@0:8I16@20"
- "@32@0:8@16@24"
- "@32@0:8@16^@24"
- "@36@0:8@16f24@28"
- "@36@0:8r^*16r*24B32"
- "@40@0:8@16#24@32"
- "@40@0:8@16@24@32"
- "@40@0:8@16@24^@32"
- "@40@0:8@16Q24^@32"
- "@44@0:8@16@24B32^@36"
- "@48@0:8@16@24@32^@40"
- "@56@0:8@16@24@32@40^@48"
- "@56@0:8Q16@24@32@40^@48"
- "@64@0:8@16@24@32@40@48^@56"
- "@72@0:8@16@24@32@40@48@56^@64"
- "Append"
- "AsciiData"
- "B16@0:8"
- "B24@0:8@16"
- "B24@0:8@?16"
- "B24@0:8r*16"
- "B24@0:8r^{?=*Q}16"
- "B32@0:8@16@24"
- "B32@0:8@16^@24"
- "B32@0:8r^v16Q24"
- "B48@0:8@16@24@32^@40"
- "B64@0:8@16@24@32@40@48^@56"
- "B80@0:8@16@24@32@40@48@56@64^@72"
- "Base64"
- "C16@0:8"
- "C24@0:8Q16"
- "CALogger"
- "CertificationLogging"
- "Comparison"
- "DERItem"
- "Data"
- "Digest"
- "Functional"
- "HexString"
- "I"
- "I16@0:8"
- "I24@0:8Q16"
- "I24@0:8d16"
- "Integer"
- "KmlRoutingInformation"
- "Q"
- "Q16@0:8"
- "Q24@0:8Q16"
- "Random"
- "S16@0:8"
- "S24@0:8Q16"
- "SESAlarm"
- "SESBootUUID"
- "SESConfig"
- "SESConfigAliro"
- "SESConfigDCK"
- "SESConfigUtilities"
- "SESTLV"
- "T@\"NSArray\",R,N"
- "T@\"NSData\",R,N"
- "T@\"NSData\",R,N,V_readerIdentifier"
- "T@\"NSString\",&,N,V_bootUUID"
- "T@\"NSString\",R,N,V_brand"
- "T@\"NSString\",R,N,V_manufacturer"
- "T@\"NSString\",R,N,V_regionString"
- "T@\"NSString\",R,V_cachedFileName"
- "TI,R,N"
- "TLVWithData:"
- "TLVWithTag:children:"
- "TLVWithTag:fromData:"
- "TLVWithTag:unsignedChar:"
- "TLVWithTag:unsignedLongValue:"
- "TLVWithTag:unsignedShort:"
- "TLVWithTag:value:"
- "TLVsWithData:"
- "URLByAppendingPathComponent:"
- "UTF8String"
- "UUIDString"
- "_bootUUID"
- "_brand"
- "_cache"
- "_cachedComponent"
- "_cachedFileName"
- "_children"
- "_config"
- "_handleAlarmFired:"
- "_intToData:"
- "_log"
- "_manufacturer"
- "_mgDeviceClass"
- "_mgProductVersion"
- "_minOSKey"
- "_parseTLVs:end:simple:"
- "_path"
- "_productVersion"
- "_readerIdentifier"
- "_regionString"
- "_tag"
- "_value"
- "_vehicleBrand"
- "_vehicleUUID"
- "addObject:"
- "allSatisfy:"
- "appendBytes:length:"
- "appendData:"
- "appendFormat:"
- "appendU16BE:"
- "appendU16LE:"
- "appendU32BE:"
- "appendU32LE:"
- "appendU64BE:"
- "appendU64LE:"
- "appendU8:"
- "array"
- "arrayValueForSetting:manufacturer:brand:uuid:error:"
- "asAsciiData"
- "asData"
- "asHexString"
- "base64"
- "base64EncodedStringWithOptions:"
- "bleLogCharacteristics:peerUUID:"
- "bleLogMessageReceived:peerUUID:"
- "bleLogMessageSent:peerUUID:"
- "bleLogRSSI:peerUUID:"
- "bleLogVehicleConnected:"
- "bleLogVehicleDisconnected:"
- "boolForKey:"
- "boolValue"
- "boolValueForSetting:manufacturer:brand:uuid:error:"
- "bootUUID"
- "bucketRawTrackingRequestDuration:"
- "bytes"
- "cachedFileName"
- "characterAtIndex:"
- "childWithTag:"
- "children"
- "childrenWithTag:"
- "clearAlarm:"
- "code"
- "componentsSeparatedByString:"
- "contains:"
- "containsObject:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "data"
- "dataUsingEncoding:"
- "dataWithBytes:length:"
- "dataWithBytesNoCopy:length:freeWhenDone:"
- "dataWithCapacity:"
- "dataWithDERItem:"
- "dataWithHexString:"
- "dataWithJSONObject:options:error:"
- "dataWithLength:"
- "dataWithTLVs:"
- "date"
- "dckLogTrackingReceipt:"
- "defaultManager"
- "deregisterAlarm:"
- "description"
- "dictValueForSetting:manufacturer:brand:uuid:error:"
- "dictionaryWithContentsOfURL:error:"
- "dictionaryWithObjects:forKeys:count:"
- "enumerateKeysAndObjectsUsingBlock:"
- "errorWithDomain:code:userInfo:"
- "evaluateCondition:operator:value:brand:uuid:deviceClass:productVersion:error:"
- "evaluateOperator:valueFromDevice:valueFromConfig:error:"
- "f"
- "f32@0:8@16^@24"
- "fileURLWithPath:"
- "filter:"
- "filterMap:"
- "find:"
- "firstObject"
- "floatValue"
- "getBootUUID"
- "getCertificate:manufacturer:environment:region:prodSE:keyID:error:"
- "getConfigForManufacturer:component:error:"
- "getConfiguration:"
- "getContentsOfAssetFile:component:error:"
- "getEncryptionCertificateFor:environment:region:error:"
- "getExternalCACertificateFor:environment:prodSE:error:"
- "getInstance"
- "getReaderInformation"
- "getResolvedSettingsFrom:brand:uuid:deviceClass:productVersion:error:"
- "getRootCertificateFor:keyID:error:"
- "getRoutingInformation"
- "getSettingForKey:error:"
- "getSettingsFor:brand:uuid:error:"
- "getSignatureCertificateFor:environment:region:keyID:error:"
- "getUUIDBytes:"
- "getVersion:error:"
- "hexStringAsData"
- "i24@0:8Q16"
- "init"
- "initAtPath:deviceClass:productVersion:"
- "initWithBytes:length:"
- "initWithData:encoding:"
- "initWithDeviceClass:productVersion:"
- "initWithDeviceClass:productVersion:path:"
- "initWithFormat:arguments:"
- "initWithInformation:readerIdentifier:"
- "initWithReaderInformation:"
- "initWithSuiteName:"
- "initWithUUIDBytes:"
- "initWithUUIDString:"
- "intValueForSetting:manufacturer:brand:uuid:error:"
- "isAlarmSet:"
- "isConfigurationApplicable:brand:uuid:deviceClass:productVersion:error:"
- "isDCKConfigurationAvailableFor:error:"
- "isEqual:"
- "isEqualToDERItem:"
- "isEqualToData:"
- "isEqualToString:"
- "isFirstLaunchAfterBootForKey:"
- "isReadableFileAtPath:"
- "isValidJSONObject:"
- "kickoff"
- "lastObject"
- "length"
- "logEncryptedAPDU:decrypted:"
- "mutableBytes"
- "mutableCopy"
- "numberWithBool:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "onAlarm:"
- "path"
- "pendingAlarms"
- "popFirst"
- "postCAEventFor:eventInput:"
- "pushLast:"
- "queue"
- "randomData:"
- "randomElement"
- "readContentsOfPlist:component:isProfile:error:"
- "readerIdentifier"
- "regionString"
- "registerAlarm:handler:"
- "registered"
- "removeObject:"
- "removeObjectAtIndex:"
- "removeObjectForKey:"
- "s32BE:"
- "ses_contains:"
- "ses_isAllZero"
- "ses_isEqualToBytes:length:"
- "ses_isEqualToHexCString:"
- "ses_map:"
- "ses_sha1"
- "ses_sha256"
- "ses_sha384"
- "ses_toData"
- "ses_withData:"
- "ses_withUUIDString:"
- "setAlarm:secondsFromNow:shouldWake:"
- "setBootUUID:"
- "setFirstLaunchAfterBootDoneForKey:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "sharedObject"
- "simpleTLVsWithData:"
- "simpleTLVsWithTag:fromData:"
- "stringWithAsciiData:"
- "stringWithCapacity:"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "strongToWeakObjectsMapTable"
- "tag"
- "timeIntervalSince1970"
- "u16BE:"
- "u16LE:"
- "u32BE:"
- "u32LE:"
- "u64BE:"
- "u64LE:"
- "u8:"
- "v16@0:8"
- "v20@0:8C16"
- "v20@0:8I16"
- "v20@0:8S16"
- "v24@0:8@16"
- "v24@0:8Q16"
- "v32@0:8@16@24"
- "v36@0:8@16d24B32"
- "validateKey:expectedClass:dictionary:"
- "value"
- "valueAsString"
- "valueAsUnsignedChar"
- "valueAsUnsignedLong"
- "valueAsUnsignedLongLong"
- "valueAsUnsignedShort"
- "valueForKey:"
- "withU16BE:"
- "{?=*Q}16@0:8"

```
