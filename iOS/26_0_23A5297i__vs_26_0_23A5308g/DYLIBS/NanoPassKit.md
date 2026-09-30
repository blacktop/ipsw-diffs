## NanoPassKit

> `/System/Library/PrivateFrameworks/NanoPassKit.framework/NanoPassKit`

```diff

-1269.0.0.0.0
-  __TEXT.__text: 0x24ff68
+1274.1.0.0.0
+  __TEXT.__text: 0x2555f8
   __TEXT.__auth_stubs: 0x1e80
-  __TEXT.__objc_methlist: 0x25478
-  __TEXT.__cstring: 0x17848
+  __TEXT.__objc_methlist: 0x25ab0
+  __TEXT.__cstring: 0x17c28
   __TEXT.__const: 0xd34
-  __TEXT.__oslogstring: 0x2c117
-  __TEXT.__gcc_except_tab: 0x6dbc
+  __TEXT.__oslogstring: 0x2c7d7
+  __TEXT.__gcc_except_tab: 0x6e10
   __TEXT.__dlopen_cstrs: 0x260
   __TEXT.__ustring: 0x160
   __TEXT.__constg_swiftt: 0x294

   __TEXT.__swift5_assocty: 0xc0
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_builtin: 0x3c
-  __TEXT.__unwind_info: 0x8d50
+  __TEXT.__unwind_info: 0x8ed0
   __TEXT.__eh_frame: 0x378
-  __TEXT.__objc_classname: 0x6a73
-  __TEXT.__objc_methname: 0x3f742
-  __TEXT.__objc_methtype: 0x9f79
-  __TEXT.__objc_stubs: 0x21f40
-  __DATA_CONST.__got: 0x1e40
-  __DATA_CONST.__const: 0x6ae0
-  __DATA_CONST.__objc_classlist: 0x11d0
+  __TEXT.__objc_classname: 0x6b98
+  __TEXT.__objc_methname: 0x3f977
+  __TEXT.__objc_methtype: 0xa08b
+  __TEXT.__objc_stubs: 0x22040
+  __DATA_CONST.__got: 0x1e78
+  __DATA_CONST.__const: 0x6b08
+  __DATA_CONST.__objc_classlist: 0x1200
   __DATA_CONST.__objc_catlist: 0x100
   __DATA_CONST.__objc_protolist: 0x278
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc908
+  __DATA_CONST.__objc_selrefs: 0xc970
   __DATA_CONST.__objc_protorefs: 0xa0
-  __DATA_CONST.__objc_superrefs: 0x1100
+  __DATA_CONST.__objc_superrefs: 0x1130
   __DATA_CONST.__objc_arraydata: 0x98
   __AUTH_CONST.__auth_got: 0xf50
-  __AUTH_CONST.__const: 0x1670
-  __AUTH_CONST.__cfstring: 0xe920
-  __AUTH_CONST.__objc_const: 0x452a0
+  __AUTH_CONST.__const: 0x1750
+  __AUTH_CONST.__cfstring: 0xe9a0
+  __AUTH_CONST.__objc_const: 0x45b38
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_intobj: 0x228
   __AUTH_CONST.__objc_doubleobj: 0x70
   __AUTH_CONST.__objc_dictobj: 0xc8
-  __AUTH.__objc_data: 0xb200
+  __AUTH.__objc_data: 0xb3e0
   __AUTH.__data: 0x1d0
-  __DATA.__objc_ivar: 0x1c1c
+  __DATA.__objc_ivar: 0x1c50
   __DATA.__data: 0x1f48
   __DATA.__bss: 0x1200
   __DATA_DIRTY.__objc_data: 0xf0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: AACA1545-E901-397A-BDDA-C35226EFF8D8
-  Functions: 14337
-  Symbols:   42110
-  CStrings:  16949
+  UUID: 626B8D4D-2063-39A9-BCFF-98A2B84254E5
+  Functions: 14485
+  Symbols:   42477
+  CStrings:  17018
 
Symbols:
+ +[NPKAudioPlayer _playSoundsWithIdentifier:].cold.1
+ +[NPKIDVRemoteDeviceProtoDeletePIIHashDataRequest configuredPartitionsIdentifiersType]
+ +[NPKIDVRemoteDeviceProtoRetrievePIIHashDataRequest configuredPartitionsIdentifiersType]
+ +[NPKIDVRemoteDeviceProtoStorePIIHashDataRequest configuredPartitionsIdentifiersType]
+ -[NPKButtonListener _handlerQueue_buttonHandler]
+ -[NPKIDVRemoteDeviceConnectionCoordinator deletePIIHashDataForCredentialIdentifier:withConfiguredPartitions:completion:]
+ -[NPKIDVRemoteDeviceConnectionCoordinator deletePIIHashDataResponse:]
+ -[NPKIDVRemoteDeviceConnectionCoordinator retrievePIIHashDataForCredentialIdentifier:withConfiguredPartitions:completion:]
+ -[NPKIDVRemoteDeviceConnectionCoordinator retrievePIIHashDataResponse:]
+ -[NPKIDVRemoteDeviceConnectionCoordinator storePIIHashDataForCredentialIdentifier:data:withConfiguredPartitions:completion:]
+ -[NPKIDVRemoteDeviceConnectionCoordinator storePIIHashDataResponse:]
+ -[NPKIDVRemoteDeviceProtoDeletePIIHashDataRequest .cxx_destruct]
+ -[NPKIDVRemoteDeviceProtoDeletePIIHashDataRequest addConfiguredPartitionsIdentifiers:]
+ -[NPKIDVRemoteDeviceProtoDeletePIIHashDataRequest clearConfiguredPartitionsIdentifiers]
+ -[NPKIDVRemoteDeviceProtoDeletePIIHashDataRequest configuredPartitionsIdentifiersAtIndex:]
+ -[NPKIDVRemoteDeviceProtoDeletePIIHashDataRequest configuredPartitionsIdentifiersCount]
+ -[NPKIDVRemoteDeviceProtoDeletePIIHashDataRequest configuredPartitionsIdentifiers]
+ -[NPKIDVRemoteDeviceProtoDeletePIIHashDataRequest copyTo:]
+ -[NPKIDVRemoteDeviceProtoDeletePIIHashDataRequest copyWithZone:]
+ -[NPKIDVRemoteDeviceProtoDeletePIIHashDataRequest credentialIdentifier]
+ -[NPKIDVRemoteDeviceProtoDeletePIIHashDataRequest description]
+ -[NPKIDVRemoteDeviceProtoDeletePIIHashDataRequest dictionaryRepresentation]
+ -[NPKIDVRemoteDeviceProtoDeletePIIHashDataRequest hash]
+ -[NPKIDVRemoteDeviceProtoDeletePIIHashDataRequest isEqual:]
+ -[NPKIDVRemoteDeviceProtoDeletePIIHashDataRequest mergeFrom:]
+ -[NPKIDVRemoteDeviceProtoDeletePIIHashDataRequest readFrom:]
+ -[NPKIDVRemoteDeviceProtoDeletePIIHashDataRequest setConfiguredPartitionsIdentifiers:]
+ -[NPKIDVRemoteDeviceProtoDeletePIIHashDataRequest setCredentialIdentifier:]
+ -[NPKIDVRemoteDeviceProtoDeletePIIHashDataRequest writeTo:]
+ -[NPKIDVRemoteDeviceProtoDeletePIIHashDataRequest writeTo:].cold.1
+ -[NPKIDVRemoteDeviceProtoDeletePIIHashDataResponse .cxx_destruct]
+ -[NPKIDVRemoteDeviceProtoDeletePIIHashDataResponse copyTo:]
+ -[NPKIDVRemoteDeviceProtoDeletePIIHashDataResponse copyWithZone:]
+ -[NPKIDVRemoteDeviceProtoDeletePIIHashDataResponse credentialIdentifier]
+ -[NPKIDVRemoteDeviceProtoDeletePIIHashDataResponse description]
+ -[NPKIDVRemoteDeviceProtoDeletePIIHashDataResponse dictionaryRepresentation]
+ -[NPKIDVRemoteDeviceProtoDeletePIIHashDataResponse errorData]
+ -[NPKIDVRemoteDeviceProtoDeletePIIHashDataResponse hasErrorData]
+ -[NPKIDVRemoteDeviceProtoDeletePIIHashDataResponse hash]
+ -[NPKIDVRemoteDeviceProtoDeletePIIHashDataResponse isEqual:]
+ -[NPKIDVRemoteDeviceProtoDeletePIIHashDataResponse mergeFrom:]
+ -[NPKIDVRemoteDeviceProtoDeletePIIHashDataResponse readFrom:]
+ -[NPKIDVRemoteDeviceProtoDeletePIIHashDataResponse setCredentialIdentifier:]
+ -[NPKIDVRemoteDeviceProtoDeletePIIHashDataResponse setErrorData:]
+ -[NPKIDVRemoteDeviceProtoDeletePIIHashDataResponse writeTo:]
+ -[NPKIDVRemoteDeviceProtoDeletePIIHashDataResponse writeTo:].cold.1
+ -[NPKIDVRemoteDeviceProtoRetrievePIIHashDataRequest .cxx_destruct]
+ -[NPKIDVRemoteDeviceProtoRetrievePIIHashDataRequest addConfiguredPartitionsIdentifiers:]
+ -[NPKIDVRemoteDeviceProtoRetrievePIIHashDataRequest clearConfiguredPartitionsIdentifiers]
+ -[NPKIDVRemoteDeviceProtoRetrievePIIHashDataRequest configuredPartitionsIdentifiersAtIndex:]
+ -[NPKIDVRemoteDeviceProtoRetrievePIIHashDataRequest configuredPartitionsIdentifiersCount]
+ -[NPKIDVRemoteDeviceProtoRetrievePIIHashDataRequest configuredPartitionsIdentifiers]
+ -[NPKIDVRemoteDeviceProtoRetrievePIIHashDataRequest copyTo:]
+ -[NPKIDVRemoteDeviceProtoRetrievePIIHashDataRequest copyWithZone:]
+ -[NPKIDVRemoteDeviceProtoRetrievePIIHashDataRequest credentialIdentifier]
+ -[NPKIDVRemoteDeviceProtoRetrievePIIHashDataRequest description]
+ -[NPKIDVRemoteDeviceProtoRetrievePIIHashDataRequest dictionaryRepresentation]
+ -[NPKIDVRemoteDeviceProtoRetrievePIIHashDataRequest hash]
+ -[NPKIDVRemoteDeviceProtoRetrievePIIHashDataRequest isEqual:]
+ -[NPKIDVRemoteDeviceProtoRetrievePIIHashDataRequest mergeFrom:]
+ -[NPKIDVRemoteDeviceProtoRetrievePIIHashDataRequest readFrom:]
+ -[NPKIDVRemoteDeviceProtoRetrievePIIHashDataRequest setConfiguredPartitionsIdentifiers:]
+ -[NPKIDVRemoteDeviceProtoRetrievePIIHashDataRequest setCredentialIdentifier:]
+ -[NPKIDVRemoteDeviceProtoRetrievePIIHashDataRequest writeTo:]
+ -[NPKIDVRemoteDeviceProtoRetrievePIIHashDataRequest writeTo:].cold.1
+ -[NPKIDVRemoteDeviceProtoRetrievePIIHashDataResponse .cxx_destruct]
+ -[NPKIDVRemoteDeviceProtoRetrievePIIHashDataResponse copyTo:]
+ -[NPKIDVRemoteDeviceProtoRetrievePIIHashDataResponse copyWithZone:]
+ -[NPKIDVRemoteDeviceProtoRetrievePIIHashDataResponse credentialIdentifier]
+ -[NPKIDVRemoteDeviceProtoRetrievePIIHashDataResponse description]
+ -[NPKIDVRemoteDeviceProtoRetrievePIIHashDataResponse dictionaryRepresentation]
+ -[NPKIDVRemoteDeviceProtoRetrievePIIHashDataResponse errorData]
+ -[NPKIDVRemoteDeviceProtoRetrievePIIHashDataResponse hasErrorData]
+ -[NPKIDVRemoteDeviceProtoRetrievePIIHashDataResponse hasPiiHashData]
+ -[NPKIDVRemoteDeviceProtoRetrievePIIHashDataResponse hash]
+ -[NPKIDVRemoteDeviceProtoRetrievePIIHashDataResponse isEqual:]
+ -[NPKIDVRemoteDeviceProtoRetrievePIIHashDataResponse mergeFrom:]
+ -[NPKIDVRemoteDeviceProtoRetrievePIIHashDataResponse piiHashData]
+ -[NPKIDVRemoteDeviceProtoRetrievePIIHashDataResponse readFrom:]
+ -[NPKIDVRemoteDeviceProtoRetrievePIIHashDataResponse setCredentialIdentifier:]
+ -[NPKIDVRemoteDeviceProtoRetrievePIIHashDataResponse setErrorData:]
+ -[NPKIDVRemoteDeviceProtoRetrievePIIHashDataResponse setPiiHashData:]
+ -[NPKIDVRemoteDeviceProtoRetrievePIIHashDataResponse writeTo:]
+ -[NPKIDVRemoteDeviceProtoRetrievePIIHashDataResponse writeTo:].cold.1
+ -[NPKIDVRemoteDeviceProtoStorePIIHashDataRequest .cxx_destruct]
+ -[NPKIDVRemoteDeviceProtoStorePIIHashDataRequest addConfiguredPartitionsIdentifiers:]
+ -[NPKIDVRemoteDeviceProtoStorePIIHashDataRequest clearConfiguredPartitionsIdentifiers]
+ -[NPKIDVRemoteDeviceProtoStorePIIHashDataRequest configuredPartitionsIdentifiersAtIndex:]
+ -[NPKIDVRemoteDeviceProtoStorePIIHashDataRequest configuredPartitionsIdentifiersCount]
+ -[NPKIDVRemoteDeviceProtoStorePIIHashDataRequest configuredPartitionsIdentifiers]
+ -[NPKIDVRemoteDeviceProtoStorePIIHashDataRequest copyTo:]
+ -[NPKIDVRemoteDeviceProtoStorePIIHashDataRequest copyWithZone:]
+ -[NPKIDVRemoteDeviceProtoStorePIIHashDataRequest credentialIdentifier]
+ -[NPKIDVRemoteDeviceProtoStorePIIHashDataRequest description]
+ -[NPKIDVRemoteDeviceProtoStorePIIHashDataRequest dictionaryRepresentation]
+ -[NPKIDVRemoteDeviceProtoStorePIIHashDataRequest hash]
+ -[NPKIDVRemoteDeviceProtoStorePIIHashDataRequest isEqual:]
+ -[NPKIDVRemoteDeviceProtoStorePIIHashDataRequest mergeFrom:]
+ -[NPKIDVRemoteDeviceProtoStorePIIHashDataRequest piiHashData]
+ -[NPKIDVRemoteDeviceProtoStorePIIHashDataRequest readFrom:]
+ -[NPKIDVRemoteDeviceProtoStorePIIHashDataRequest setConfiguredPartitionsIdentifiers:]
+ -[NPKIDVRemoteDeviceProtoStorePIIHashDataRequest setCredentialIdentifier:]
+ -[NPKIDVRemoteDeviceProtoStorePIIHashDataRequest setPiiHashData:]
+ -[NPKIDVRemoteDeviceProtoStorePIIHashDataRequest writeTo:]
+ -[NPKIDVRemoteDeviceProtoStorePIIHashDataRequest writeTo:].cold.1
+ -[NPKIDVRemoteDeviceProtoStorePIIHashDataRequest writeTo:].cold.2
+ -[NPKIDVRemoteDeviceProtoStorePIIHashDataResponse .cxx_destruct]
+ -[NPKIDVRemoteDeviceProtoStorePIIHashDataResponse copyTo:]
+ -[NPKIDVRemoteDeviceProtoStorePIIHashDataResponse copyWithZone:]
+ -[NPKIDVRemoteDeviceProtoStorePIIHashDataResponse credentialIdentifier]
+ -[NPKIDVRemoteDeviceProtoStorePIIHashDataResponse description]
+ -[NPKIDVRemoteDeviceProtoStorePIIHashDataResponse dictionaryRepresentation]
+ -[NPKIDVRemoteDeviceProtoStorePIIHashDataResponse errorData]
+ -[NPKIDVRemoteDeviceProtoStorePIIHashDataResponse hasErrorData]
+ -[NPKIDVRemoteDeviceProtoStorePIIHashDataResponse hash]
+ -[NPKIDVRemoteDeviceProtoStorePIIHashDataResponse isEqual:]
+ -[NPKIDVRemoteDeviceProtoStorePIIHashDataResponse mergeFrom:]
+ -[NPKIDVRemoteDeviceProtoStorePIIHashDataResponse readFrom:]
+ -[NPKIDVRemoteDeviceProtoStorePIIHashDataResponse setCredentialIdentifier:]
+ -[NPKIDVRemoteDeviceProtoStorePIIHashDataResponse setErrorData:]
+ -[NPKIDVRemoteDeviceProtoStorePIIHashDataResponse writeTo:]
+ -[NPKIDVRemoteDeviceProtoStorePIIHashDataResponse writeTo:].cold.1
+ -[NPKIDVRemoteDeviceSession deletePIIHashDataForCredentialIdentifier:completion:]
+ -[NPKIDVRemoteDeviceSession retrievePIIHashDataForCredentialIdentifier:completion:]
+ -[NPKIDVRemoteDeviceSession storePIIHashDataForCredentialIdentifier:data:completion:]
+ -[NPKIDVRemoteDeviceSessionServer deletePIIHashDataForCredentialIdentifier:completion:]
+ -[NPKIDVRemoteDeviceSessionServer retrievePIIHashDataForCredentialIdentifier:completion:]
+ -[NPKIDVRemoteDeviceSessionServer storePIIHashDataForCredentialIdentifier:data:completion:]
+ -[NPKPaymentWebServiceCompanionTargetDevice deviceSupportedRadioTechnologiesWithCompletion:]
+ -[NPKPaymentWebServiceCompanionTargetDevice(Capabilities) _isSimultaneousSinglePollingAndGymKitSupported]
+ GCC_except_table198
+ GCC_except_table230
+ GCC_except_table796
+ GCC_except_table802
+ GCC_except_table804
+ GCC_except_table813
+ GCC_except_table819
+ GCC_except_table826
+ GCC_except_table831
+ GCC_except_table836
+ GCC_except_table841
+ GCC_except_table846
+ GCC_except_table852
+ GCC_except_table860
+ GCC_except_table871
+ GCC_except_table897
+ _AudioServicesPlaySystemSoundWithOptions
+ _NPKIDVRemoteDeviceProtoDeletePIIHashDataRequestReadFrom
+ _NPKIDVRemoteDeviceProtoDeletePIIHashDataResponseReadFrom
+ _NPKIDVRemoteDeviceProtoRetrievePIIHashDataRequestReadFrom
+ _NPKIDVRemoteDeviceProtoRetrievePIIHashDataResponseReadFrom
+ _NPKIDVRemoteDeviceProtoStorePIIHashDataRequestReadFrom
+ _NPKIDVRemoteDeviceProtoStorePIIHashDataResponseReadFrom
+ _NPKIsWatchOfferSupportedForCompanionPaymentPass
+ _NPKNeedsLiveActivity
+ _OBJC_CLASS_$_NPKIDVRemoteDeviceProtoDeletePIIHashDataRequest
+ _OBJC_CLASS_$_NPKIDVRemoteDeviceProtoDeletePIIHashDataResponse
+ _OBJC_CLASS_$_NPKIDVRemoteDeviceProtoRetrievePIIHashDataRequest
+ _OBJC_CLASS_$_NPKIDVRemoteDeviceProtoRetrievePIIHashDataResponse
+ _OBJC_CLASS_$_NPKIDVRemoteDeviceProtoStorePIIHashDataRequest
+ _OBJC_CLASS_$_NPKIDVRemoteDeviceProtoStorePIIHashDataResponse
+ _OBJC_IVAR_$_NPKIDVRemoteDeviceProtoDeletePIIHashDataRequest._configuredPartitionsIdentifiers
+ _OBJC_IVAR_$_NPKIDVRemoteDeviceProtoDeletePIIHashDataRequest._credentialIdentifier
+ _OBJC_IVAR_$_NPKIDVRemoteDeviceProtoDeletePIIHashDataResponse._credentialIdentifier
+ _OBJC_IVAR_$_NPKIDVRemoteDeviceProtoDeletePIIHashDataResponse._errorData
+ _OBJC_IVAR_$_NPKIDVRemoteDeviceProtoRetrievePIIHashDataRequest._configuredPartitionsIdentifiers
+ _OBJC_IVAR_$_NPKIDVRemoteDeviceProtoRetrievePIIHashDataRequest._credentialIdentifier
+ _OBJC_IVAR_$_NPKIDVRemoteDeviceProtoRetrievePIIHashDataResponse._credentialIdentifier
+ _OBJC_IVAR_$_NPKIDVRemoteDeviceProtoRetrievePIIHashDataResponse._errorData
+ _OBJC_IVAR_$_NPKIDVRemoteDeviceProtoRetrievePIIHashDataResponse._piiHashData
+ _OBJC_IVAR_$_NPKIDVRemoteDeviceProtoStorePIIHashDataRequest._configuredPartitionsIdentifiers
+ _OBJC_IVAR_$_NPKIDVRemoteDeviceProtoStorePIIHashDataRequest._credentialIdentifier
+ _OBJC_IVAR_$_NPKIDVRemoteDeviceProtoStorePIIHashDataRequest._piiHashData
+ _OBJC_IVAR_$_NPKIDVRemoteDeviceProtoStorePIIHashDataResponse._credentialIdentifier
+ _OBJC_IVAR_$_NPKIDVRemoteDeviceProtoStorePIIHashDataResponse._errorData
+ _OBJC_METACLASS_$_NPKIDVRemoteDeviceProtoDeletePIIHashDataRequest
+ _OBJC_METACLASS_$_NPKIDVRemoteDeviceProtoDeletePIIHashDataResponse
+ _OBJC_METACLASS_$_NPKIDVRemoteDeviceProtoRetrievePIIHashDataRequest
+ _OBJC_METACLASS_$_NPKIDVRemoteDeviceProtoRetrievePIIHashDataResponse
+ _OBJC_METACLASS_$_NPKIDVRemoteDeviceProtoStorePIIHashDataRequest
+ _OBJC_METACLASS_$_NPKIDVRemoteDeviceProtoStorePIIHashDataResponse
+ __OBJC_$_CLASS_METHODS_NPKIDVRemoteDeviceProtoDeletePIIHashDataRequest
+ __OBJC_$_CLASS_METHODS_NPKIDVRemoteDeviceProtoRetrievePIIHashDataRequest
+ __OBJC_$_CLASS_METHODS_NPKIDVRemoteDeviceProtoStorePIIHashDataRequest
+ __OBJC_$_INSTANCE_METHODS_NPKIDVRemoteDeviceProtoDeletePIIHashDataRequest
+ __OBJC_$_INSTANCE_METHODS_NPKIDVRemoteDeviceProtoDeletePIIHashDataResponse
+ __OBJC_$_INSTANCE_METHODS_NPKIDVRemoteDeviceProtoRetrievePIIHashDataRequest
+ __OBJC_$_INSTANCE_METHODS_NPKIDVRemoteDeviceProtoRetrievePIIHashDataResponse
+ __OBJC_$_INSTANCE_METHODS_NPKIDVRemoteDeviceProtoStorePIIHashDataRequest
+ __OBJC_$_INSTANCE_METHODS_NPKIDVRemoteDeviceProtoStorePIIHashDataResponse
+ __OBJC_$_INSTANCE_VARIABLES_NPKIDVRemoteDeviceProtoDeletePIIHashDataRequest
+ __OBJC_$_INSTANCE_VARIABLES_NPKIDVRemoteDeviceProtoDeletePIIHashDataResponse
+ __OBJC_$_INSTANCE_VARIABLES_NPKIDVRemoteDeviceProtoRetrievePIIHashDataRequest
+ __OBJC_$_INSTANCE_VARIABLES_NPKIDVRemoteDeviceProtoRetrievePIIHashDataResponse
+ __OBJC_$_INSTANCE_VARIABLES_NPKIDVRemoteDeviceProtoStorePIIHashDataRequest
+ __OBJC_$_INSTANCE_VARIABLES_NPKIDVRemoteDeviceProtoStorePIIHashDataResponse
+ __OBJC_$_PROP_LIST_NPKIDVRemoteDeviceProtoDeletePIIHashDataRequest
+ __OBJC_$_PROP_LIST_NPKIDVRemoteDeviceProtoDeletePIIHashDataResponse
+ __OBJC_$_PROP_LIST_NPKIDVRemoteDeviceProtoRetrievePIIHashDataRequest
+ __OBJC_$_PROP_LIST_NPKIDVRemoteDeviceProtoRetrievePIIHashDataResponse
+ __OBJC_$_PROP_LIST_NPKIDVRemoteDeviceProtoStorePIIHashDataRequest
+ __OBJC_$_PROP_LIST_NPKIDVRemoteDeviceProtoStorePIIHashDataResponse
+ __OBJC_CLASS_PROTOCOLS_$_NPKIDVRemoteDeviceProtoDeletePIIHashDataRequest
+ __OBJC_CLASS_PROTOCOLS_$_NPKIDVRemoteDeviceProtoDeletePIIHashDataResponse
+ __OBJC_CLASS_PROTOCOLS_$_NPKIDVRemoteDeviceProtoRetrievePIIHashDataRequest
+ __OBJC_CLASS_PROTOCOLS_$_NPKIDVRemoteDeviceProtoRetrievePIIHashDataResponse
+ __OBJC_CLASS_PROTOCOLS_$_NPKIDVRemoteDeviceProtoStorePIIHashDataRequest
+ __OBJC_CLASS_PROTOCOLS_$_NPKIDVRemoteDeviceProtoStorePIIHashDataResponse
+ __OBJC_CLASS_RO_$_NPKIDVRemoteDeviceProtoDeletePIIHashDataRequest
+ __OBJC_CLASS_RO_$_NPKIDVRemoteDeviceProtoDeletePIIHashDataResponse
+ __OBJC_CLASS_RO_$_NPKIDVRemoteDeviceProtoRetrievePIIHashDataRequest
+ __OBJC_CLASS_RO_$_NPKIDVRemoteDeviceProtoRetrievePIIHashDataResponse
+ __OBJC_CLASS_RO_$_NPKIDVRemoteDeviceProtoStorePIIHashDataRequest
+ __OBJC_CLASS_RO_$_NPKIDVRemoteDeviceProtoStorePIIHashDataResponse
+ __OBJC_METACLASS_RO_$_NPKIDVRemoteDeviceProtoDeletePIIHashDataRequest
+ __OBJC_METACLASS_RO_$_NPKIDVRemoteDeviceProtoDeletePIIHashDataResponse
+ __OBJC_METACLASS_RO_$_NPKIDVRemoteDeviceProtoRetrievePIIHashDataRequest
+ __OBJC_METACLASS_RO_$_NPKIDVRemoteDeviceProtoRetrievePIIHashDataResponse
+ __OBJC_METACLASS_RO_$_NPKIDVRemoteDeviceProtoStorePIIHashDataRequest
+ __OBJC_METACLASS_RO_$_NPKIDVRemoteDeviceProtoStorePIIHashDataResponse
+ ___110-[NPKIDVRemoteDeviceConnectionCoordinator _sendRequest:withType:priority:queueIdentifier:requestItem:timeout:]_block_invoke.215
+ ___120-[NPKIDVRemoteDeviceConnectionCoordinator deletePIIHashDataForCredentialIdentifier:withConfiguredPartitions:completion:]_block_invoke
+ ___122-[NPKIDVRemoteDeviceConnectionCoordinator retrievePIIHashDataForCredentialIdentifier:withConfiguredPartitions:completion:]_block_invoke
+ ___124-[NPKIDVRemoteDeviceConnectionCoordinator storePIIHashDataForCredentialIdentifier:data:withConfiguredPartitions:completion:]_block_invoke
+ ___77-[NPKIDVRemoteDeviceConnectionCoordinator establishPrearmTrustV2:completion:]_block_invoke.163
+ ___80-[NPKAssertionController _releaseAssertionFromOwnerObject:withDelay:completion:]_block_invoke_2
+ ___81-[NPKIDVRemoteDeviceSession deletePIIHashDataForCredentialIdentifier:completion:]_block_invoke
+ ___81-[NPKIDVRemoteDeviceSession deletePIIHashDataForCredentialIdentifier:completion:]_block_invoke.106
+ ___83-[NPKIDVRemoteDeviceSession retrievePIIHashDataForCredentialIdentifier:completion:]_block_invoke
+ ___83-[NPKIDVRemoteDeviceSession retrievePIIHashDataForCredentialIdentifier:completion:]_block_invoke.105
+ ___85-[NPKIDVRemoteDeviceSession storePIIHashDataForCredentialIdentifier:data:completion:]_block_invoke
+ ___85-[NPKIDVRemoteDeviceSession storePIIHashDataForCredentialIdentifier:data:completion:]_block_invoke.104
+ ___block_descriptor_56_e8_32s40s48bs_e30_v24?0"NSString"8"NSError"16ls32l8s48l8s40l8
+ ___block_descriptor_64_e8_32s40bs48r56w_e5_v8?0lw56l8s32l8r48l8s40l8
+ ___block_literal_global.21
+ _kAudioServicesPlaySystemSoundOptionFlagsKey
+ _objc_msgSend$_handlerQueue_buttonHandler
+ _objc_msgSend$_isSimultaneousSinglePollingAndGymKitSupported
+ _objc_msgSend$deletePIIHashDataForCredentialIdentifier:completion:
+ _objc_msgSend$deletePIIHashDataForCredentialIdentifier:withConfiguredPartitions:completion:
+ _objc_msgSend$dictionaryWithObjectsAndKeys:
+ _objc_msgSend$expressModeSettingsCoordinator:didEncounterConflictWhenEnablingExpressForPass:conflictingExpressPasses:completion:
+ _objc_msgSend$flight
+ _objc_msgSend$paymentSessionSource:receivedButtonEventAtDate:authIntentSource:delegated:
+ _objc_msgSend$piiHashData
+ _objc_msgSend$retrievePIIHashDataForCredentialIdentifier:completion:
+ _objc_msgSend$retrievePIIHashDataForCredentialIdentifier:withConfiguredPartitions:completion:
+ _objc_msgSend$setPiiHashData:
+ _objc_msgSend$storePIIHashDataForCredentialIdentifier:data:completion:
+ _objc_msgSend$storePIIHashDataForCredentialIdentifier:data:withConfiguredPartitions:completion:
- +[NPKAudioPlayer _playSoundsWithFallbackHapticIfNecessaryForSoundIdentifier:]
- +[NPKAudioPlayer _playSoundsWithFallbackHapticIfNecessaryForSoundIdentifier:].cold.1
- -[NPKButtonListener _queue_notifyButtonEventFromSource:]
- -[NPKButtonListener registerObserver:]
- -[NPKButtonListener unregisterObserver:]
- GCC_except_table150
- GCC_except_table192
- GCC_except_table227
- GCC_except_table229
- GCC_except_table795
- GCC_except_table801
- GCC_except_table803
- GCC_except_table812
- GCC_except_table818
- GCC_except_table825
- GCC_except_table830
- GCC_except_table835
- GCC_except_table840
- GCC_except_table845
- GCC_except_table851
- GCC_except_table859
- GCC_except_table870
- GCC_except_table896
- _AudioServicesPlaySystemSoundWithCompletion
- _OBJC_IVAR_$_NPKButtonListener._observers
- ___110-[NPKIDVRemoteDeviceConnectionCoordinator _sendRequest:withType:priority:queueIdentifier:requestItem:timeout:]_block_invoke.194
- ___56-[NPKButtonListener _queue_notifyButtonEventFromSource:]_block_invoke
- ___77-[NPKIDVRemoteDeviceConnectionCoordinator establishPrearmTrustV2:completion:]_block_invoke.157
- ___block_descriptor_48_e8_32s_e37_v16?0"<NPKButtonListenerObserver>"8ls32l8
- ___block_literal_global.25
- _objc_msgSend$_playSoundsWithFallbackHapticIfNecessaryForSoundIdentifier:
- _objc_msgSend$_queue_notifyButtonEventFromSource:
- _objc_msgSend$buttonListener:didReceiveButtonEventFromSource:
- _objc_msgSend$expressModeSettingsCoordinator:didEncounterConflictWhenEnablingExpressForPass:conflictingExpressPasses:conflictsWithGymKit:completion:
- _objc_msgSend$hasImmediateAutomaticSelectionCriterion
- _objc_msgSend$paymentSessionSource:receivedDelegatedButtonEventAtDate:authIntentSource:
CStrings:
+ "-[NPKIDVRemoteDeviceConnectionCoordinator deletePIIHashDataResponse:]"
+ "-[NPKIDVRemoteDeviceConnectionCoordinator retrievePIIHashDataResponse:]"
+ "-[NPKIDVRemoteDeviceConnectionCoordinator storePIIHashDataResponse:]"
+ "-[NPKIDVRemoteDeviceProtoDeletePIIHashDataRequest writeTo:]"
+ "-[NPKIDVRemoteDeviceProtoDeletePIIHashDataResponse writeTo:]"
+ "-[NPKIDVRemoteDeviceProtoRetrievePIIHashDataRequest writeTo:]"
+ "-[NPKIDVRemoteDeviceProtoRetrievePIIHashDataResponse writeTo:]"
+ "-[NPKIDVRemoteDeviceProtoStorePIIHashDataRequest writeTo:]"
+ "-[NPKIDVRemoteDeviceProtoStorePIIHashDataResponse writeTo:]"
+ "Error: Attempted to create assertion for %@ with reason: %@, but received nil."
+ "Error: NPKIDVRemoteDeviceService: Error deleting PII hash for credential with error:%@"
+ "Error: NPKIDVRemoteDeviceService: Error retrieving PII hash for credential with error:%@"
+ "Error: NPKIDVRemoteDeviceService: Error storing PII hash for credential with error:%@"
+ "Error: NPKIDVRemoteDeviceService: Error while retrieving PII Hash with error:%@"
+ "Error: NPKIDVRemoteDeviceService: Error while storing PII Hash with error:%@"
+ "Error: NPKIDVRemoteDeviceService: Failed to delete PII hash in partition with error:%@"
+ "Error: NPKIDVRemoteDeviceService: Failed to retrieve PII hash for credential with error:%@"
+ "Error: NPKIDVRemoteDeviceService: Failed to store PII hash for credential with error:%@"
+ "NPKIDVRemoteDeviceProtoDeletePIIHashDataRequest"
+ "NPKIDVRemoteDeviceProtoDeletePIIHashDataRequest.m"
+ "NPKIDVRemoteDeviceProtoDeletePIIHashDataResponse"
+ "NPKIDVRemoteDeviceProtoDeletePIIHashDataResponse.m"
+ "NPKIDVRemoteDeviceProtoRetrievePIIHashDataRequest"
+ "NPKIDVRemoteDeviceProtoRetrievePIIHashDataRequest.m"
+ "NPKIDVRemoteDeviceProtoRetrievePIIHashDataResponse"
+ "NPKIDVRemoteDeviceProtoRetrievePIIHashDataResponse.m"
+ "NPKIDVRemoteDeviceProtoStorePIIHashDataRequest"
+ "NPKIDVRemoteDeviceProtoStorePIIHashDataRequest.m"
+ "NPKIDVRemoteDeviceProtoStorePIIHashDataResponse"
+ "NPKIDVRemoteDeviceProtoStorePIIHashDataResponse.m"
+ "Notice: NPKIDVRemoteDeviceService: Finish deleting PII hash for credential with identifier%@"
+ "Notice: NPKIDVRemoteDeviceService: Finish retrieving PII hash for credential with identifier%@"
+ "Notice: NPKIDVRemoteDeviceService: Finish storing PII hash for credential with identifier%@"
+ "Notice: NPKIDVRemoteDeviceService: Requested delete PII hash for Credential:%@"
+ "Notice: NPKIDVRemoteDeviceService: Requested retrieve PII hash for Credential:%@"
+ "Notice: NPKIDVRemoteDeviceService: Requested store PII hash for Credential:%@"
+ "Notice: NPKIDVRemoteDeviceService: Session - requested to delete PII Hash for credential with identifier:%@"
+ "Notice: NPKIDVRemoteDeviceService: Session - requested to retrieve PII Hash for credential with identifier:%@"
+ "Notice: NPKIDVRemoteDeviceService: Session - requested to store PII Hash for credential with identifier:%@"
+ "Notice: Pass does not support Watch offer. %@"
+ "Notice: Target device - device supported radio technologies with completion: %@"
+ "Notice: Target device - returning device supported radio technologies: %lu"
+ "T@\"NSData\",&,N,V_piiHashData"
+ "T@\"NSString\",&,N,V_piiHashData"
+ "_handlerQueue_buttonHandler"
+ "_isSimultaneousSinglePollingAndGymKitSupported"
+ "_piiHashData"
+ "canSaveFPANCardWithDescriptor:credential:completion:"
+ "deletePIIHashDataForCredentialIdentifier"
+ "deletePIIHashDataForCredentialIdentifier:completion:"
+ "deletePIIHashDataForCredentialIdentifier:withConfiguredPartitions:completion:"
+ "deletePIIHashDataResponse:"
+ "dictionaryWithObjectsAndKeys:"
+ "expressModeSettingsCoordinator:didEncounterConflictWhenEnablingExpressForPass:conflictingExpressPasses:completion:"
+ "flight"
+ "hasPiiHashData"
+ "nil != self->_piiHashData"
+ "paymentSessionSource:receivedButtonEventAtDate:authIntentSource:delegated:"
+ "piiHashData"
+ "retrievePIIHashDataForCredentialIdentifier"
+ "retrievePIIHashDataForCredentialIdentifier:completion:"
+ "retrievePIIHashDataForCredentialIdentifier:withConfiguredPartitions:completion:"
+ "retrievePIIHashDataResponse:"
+ "setPiiHashData:"
+ "storePIIHashDataForCredentialIdentifier"
+ "storePIIHashDataForCredentialIdentifier:data:completion:"
+ "storePIIHashDataForCredentialIdentifier:data:withConfiguredPartitions:completion:"
+ "storePIIHashDataResponse:"
+ "v40@0:8@\"NSString\"16@\"NSData\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"NSString\"16@\"NSSet\"24@?<v@?@\"NSString\"@\"NSError\">32"
+ "v40@0:8@\"PKAutoFillCardDescriptor\"16@\"PKAutoFillCardCredential\"24@?<v@?@\"PKFPANCardCanSaveResult\">32"
+ "v48@0:8@\"NSString\"16@\"NSData\"24@\"NSSet\"32@?<v@?@\"NSError\">40"
- "Notice: Audio player playing sound %u; should fall back to haptic: %@"
- "_playSoundsWithFallbackHapticIfNecessaryForSoundIdentifier:"
- "_queue_notifyButtonEventFromSource:"
- "buttonListener:didReceiveButtonEventFromSource:"
- "expressModeSettingsCoordinator:didEncounterConflictWhenEnablingExpressForPass:conflictingExpressPasses:conflictsWithGymKit:completion:"
- "hasImmediateAutomaticSelectionCriterion"
- "paymentSessionSource:receivedDelegatedButtonEventAtDate:authIntentSource:"
- "v16@?0@\"<NPKButtonListenerObserver>\"8"

```
