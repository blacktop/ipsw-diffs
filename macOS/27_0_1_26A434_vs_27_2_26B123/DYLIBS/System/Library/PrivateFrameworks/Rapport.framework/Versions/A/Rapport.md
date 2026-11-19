## Rapport

> `/System/Library/PrivateFrameworks/Rapport.framework/Versions/A/Rapport`

```diff

-751.100.1.0.0
-  __TEXT.__text: 0xe0f28
-  __TEXT.__objc_methlist: 0x9ee8
-  __TEXT.__cstring: 0x13c2c
-  __TEXT.__const: 0x3f68
-  __TEXT.__gcc_except_tab: 0x149c
-  __TEXT.__oslogstring: 0x242d
-  __TEXT.__swift5_typeref: 0xbd5
-  __TEXT.__swift5_capture: 0x890
-  __TEXT.__swift5_fieldmd: 0xb28
-  __TEXT.__constg_swiftt: 0xd94
-  __TEXT.__swift5_reflstr: 0x91c
+751.200.83.0.0
+  __TEXT.__text: 0xe9cd0
+  __TEXT.__objc_methlist: 0xa1a0
+  __TEXT.__cstring: 0x1471c
+  __TEXT.__const: 0x41a8
+  __TEXT.__gcc_except_tab: 0x1508
+  __TEXT.__oslogstring: 0x26bd
+  __TEXT.__swift5_typeref: 0xc4f
+  __TEXT.__swift5_capture: 0x958
+  __TEXT.__swift5_fieldmd: 0xb34
+  __TEXT.__constg_swiftt: 0xdbc
+  __TEXT.__swift5_reflstr: 0x93c
   __TEXT.__swift5_proto: 0x144
   __TEXT.__swift5_types: 0xb0
   __TEXT.__swift_as_entry: 0x14

   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x2e60
+  __TEXT.__unwind_info: 0x2f58
   __TEXT.__eh_frame: 0x960
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x12f8
-  __DATA_CONST.__objc_classlist: 0x2c8
+  __DATA_CONST.__const: 0x1300
+  __DATA_CONST.__objc_classlist: 0x2d8
   __DATA_CONST.__objc_catlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x160
+  __DATA_CONST.__objc_protolist: 0x170
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4460
-  __DATA_CONST.__objc_protorefs: 0xf0
-  __DATA_CONST.__objc_superrefs: 0x1f0
+  __DATA_CONST.__objc_selrefs: 0x45d8
+  __DATA_CONST.__objc_protorefs: 0x100
+  __DATA_CONST.__objc_superrefs: 0x1f8
   __DATA_CONST.__objc_arraydata: 0xb0
-  __DATA_CONST.__got: 0x4d0
-  __AUTH_CONST.__const: 0x3cd8
-  __AUTH_CONST.__cfstring: 0x6080
-  __AUTH_CONST.__objc_const: 0x11278
-  __AUTH_CONST.__objc_intobj: 0x240
+  __DATA_CONST.__got: 0x4e8
+  __AUTH_CONST.__const: 0x3f90
+  __AUTH_CONST.__cfstring: 0x6040
+  __AUTH_CONST.__objc_const: 0x11658
+  __AUTH_CONST.__objc_intobj: 0x270
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH_CONST.__auth_got: 0xf80
+  __AUTH_CONST.__auth_got: 0xfc8
   __AUTH_CONST.__auth_ptr: 0x2c0
-  __AUTH.__objc_data: 0x1280
-  __AUTH.__data: 0x520
-  __DATA.__objc_ivar: 0x10ec
-  __DATA.__data: 0x2128
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0x111c
+  __DATA.__data: 0x738
   __DATA.__bss: 0x2e30
   __DATA.__common: 0x68
-  __DATA_DIRTY.__objc_data: 0x1318
-  __DATA_DIRTY.__data: 0x5f8
-  __DATA_DIRTY.__bss: 0xd8
+  __DATA_DIRTY.__objc_data: 0x2618
+  __DATA_DIRTY.__data: 0x2650
+  __DATA_DIRTY.__bss: 0xe8
   __DATA_DIRTY.__common: 0x28
   - /System/Library/Frameworks/CFNetwork.framework/Versions/A/CFNetwork
   - /System/Library/Frameworks/CoreBluetooth.framework/Versions/A/CoreBluetooth

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5775
-  Symbols:   8296
-  CStrings:  2976
+  Functions: 5887
+  Symbols:   8456
+  CStrings:  3051
 
Symbols:
+ +[RPNWTXTUtils statusFlagsForEndpoint:]
+ +[RPNWTXTUtils statusFlagsForTXTRecord:]
+ +[RPNWTXTUtils updateStatusFlags:onEndpoint:operation:]
+ +[RPNWTXTUtils updateStatusFlags:onTXTRecord:operation:]
+ -[RPAccessPolicyClient .cxx_destruct]
+ -[RPAccessPolicyClient _activateWithPolicy:forService:completion:]
+ -[RPAccessPolicyClient _invalidate]
+ -[RPAccessPolicyClient _invalidated]
+ -[RPAccessPolicyClient _updateState:]
+ -[RPAccessPolicyClient _xpcActivate:completion:]
+ -[RPAccessPolicyClient _xpcInterrupted]
+ -[RPAccessPolicyClient _xpcInvalidated]
+ -[RPAccessPolicyClient _xpcSetup]
+ -[RPAccessPolicyClient accessPermittedHandler]
+ -[RPAccessPolicyClient accessPolicyUpdatedDevices:]
+ -[RPAccessPolicyClient accessRevokedHandler]
+ -[RPAccessPolicyClient activateWithPolicy:forService:completion:]
+ -[RPAccessPolicyClient devices]
+ -[RPAccessPolicyClient dispatchQueue]
+ -[RPAccessPolicyClient init]
+ -[RPAccessPolicyClient invalidate]
+ -[RPAccessPolicyClient invalidationHandler]
+ -[RPAccessPolicyClient policy]
+ -[RPAccessPolicyClient serviceName]
+ -[RPAccessPolicyClient setAccessPermittedHandler:]
+ -[RPAccessPolicyClient setAccessRevokedHandler:]
+ -[RPAccessPolicyClient setDevices:]
+ -[RPAccessPolicyClient setDispatchQueue:]
+ -[RPAccessPolicyClient setInvalidationHandler:]
+ -[RPAccessPolicyClient setState:]
+ -[RPAccessPolicyClient setXpcConnection:]
+ -[RPAccessPolicyClient state]
+ -[RPAccessPolicyClient xpcConnection]
+ -[RPClient endpointContextForService:trustCircles:completion:]
+ -[RPClient endpointContextForService:trustCircles:parameters:completion:]
+ -[RPClient updateEndpointAttributes:forService:usingContext:completion:]
+ -[RPCompanionLinkDevice updateMultiUserDeviceWithPeer:]
+ -[RPConnection _identityDaemonGetPairingIdentityFromHomeWithAccessory:completion:]
+ -[RPConnection _multiUserDeviceWithIdentifier:]
+ -[RPConnection _requestIDIsHighVolume:messageIsChatty:]
+ -[RPConnection multiUserDevices]
+ -[RPConnection setMultiUserDevices:]
+ -[RPConnection verifyIdentityProof:accountAltDSID:]
+ -[RPConnection verifyMUHomeKitIdentityProof:identifier:accountAltDSID:completion:]
+ -[RPSiriSession _triggerInfoRequest]
+ -[RPSiriSession setTriggerDurationMs:]
+ -[RPSiriSession setTriggeredPhrase:]
+ -[RPSiriSession setTwoShotFeedbackDelaySec:]
+ -[RPSiriSession triggerDurationMs]
+ -[RPSiriSession triggeredPhrase]
+ -[RPSiriSession twoShotFeedbackDelaySec]
+ GCC_except_table14
+ GCC_except_table281
+ GCC_except_table300
+ GCC_except_table75
+ GCC_except_table77
+ GCC_except_table79
+ GCC_except_table98
+ OBJC_IVAR_$_RPAccessPolicyClient._accessPermittedHandler
+ OBJC_IVAR_$_RPAccessPolicyClient._accessRevokedHandler
+ OBJC_IVAR_$_RPAccessPolicyClient._devices
+ OBJC_IVAR_$_RPAccessPolicyClient._dispatchQueue
+ OBJC_IVAR_$_RPAccessPolicyClient._invalidationHandler
+ OBJC_IVAR_$_RPAccessPolicyClient._policy
+ OBJC_IVAR_$_RPAccessPolicyClient._serviceName
+ OBJC_IVAR_$_RPAccessPolicyClient._state
+ OBJC_IVAR_$_RPAccessPolicyClient._xpcConnection
+ OBJC_IVAR_$_RPConnection._multiUserDevices
+ OBJC_IVAR_$_RPSiriSession._triggerDurationMs
+ OBJC_IVAR_$_RPSiriSession._triggeredPhrase
+ OBJC_IVAR_$_RPSiriSession._twoShotFeedbackDelaySec
+ _OBJC_CLASS_$_NSScanner
+ _OBJC_CLASS_$_RPAccessPolicyClient
+ _OBJC_CLASS_$_RPNWTXTUtils
+ _OBJC_METACLASS_$_RPAccessPolicyClient
+ _OBJC_METACLASS_$_RPNWTXTUtils
+ _RPOptionMultiUserDeviceID
+ __33-[RPAccessPolicyClient _xpcSetup]_block_invoke
+ __48-[RPAccessPolicyClient _xpcActivate:completion:]_block_invoke
+ __72-[RPClient updateEndpointAttributes:forService:usingContext:completion:]_block_invoke_3
+ __OBJC_$_CLASS_METHODS_RPNWTXTUtils
+ __OBJC_$_INSTANCE_METHODS_RPAccessPolicyClient
+ __OBJC_$_INSTANCE_VARIABLES_RPAccessPolicyClient
+ __OBJC_$_PROP_LIST_RPAccessPolicyClient
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_RPAccessPolicyXPCClientInterface
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_RPAccessPolicyXPCServerInterface
+ __OBJC_$_PROTOCOL_METHOD_TYPES_RPAccessPolicyXPCClientInterface
+ __OBJC_$_PROTOCOL_METHOD_TYPES_RPAccessPolicyXPCServerInterface
+ __OBJC_CLASS_PROTOCOLS_$_RPAccessPolicyClient
+ __OBJC_CLASS_RO_$_RPAccessPolicyClient
+ __OBJC_CLASS_RO_$_RPNWTXTUtils
+ __OBJC_LABEL_PROTOCOL_$_RPAccessPolicyXPCClientInterface
+ __OBJC_LABEL_PROTOCOL_$_RPAccessPolicyXPCServerInterface
+ __OBJC_METACLASS_RO_$_RPAccessPolicyClient
+ __OBJC_METACLASS_RO_$_RPNWTXTUtils
+ __OBJC_PROTOCOL_$_RPAccessPolicyXPCClientInterface
+ __OBJC_PROTOCOL_$_RPAccessPolicyXPCServerInterface
+ __OBJC_PROTOCOL_REFERENCE_$_RPAccessPolicyXPCClientInterface
+ __OBJC_PROTOCOL_REFERENCE_$_RPAccessPolicyXPCServerInterface
+ ___33-[RPAccessPolicyClient _xpcSetup]_block_invoke
+ ___34-[RPAccessPolicyClient invalidate]_block_invoke
+ ___40+[RPNWTXTUtils statusFlagsForTXTRecord:]_block_invoke
+ ___48-[RPAccessPolicyClient _xpcActivate:completion:]_block_invoke
+ ___62-[RPClient endpointContextForService:trustCircles:completion:]_block_invoke
+ ___62-[RPClient endpointContextForService:trustCircles:completion:]_block_invoke_2
+ ___65-[RPAccessPolicyClient activateWithPolicy:forService:completion:]_block_invoke
+ ___72-[RPClient updateEndpointAttributes:forService:usingContext:completion:]_block_invoke
+ ___72-[RPClient updateEndpointAttributes:forService:usingContext:completion:]_block_invoke_2
+ ___72-[RPClient updateEndpointAttributes:forService:usingContext:completion:]_block_invoke_3
+ ___73-[RPClient endpointContextForService:trustCircles:parameters:completion:]_block_invoke
+ ___73-[RPClient endpointContextForService:trustCircles:parameters:completion:]_block_invoke_2
+ ___82-[RPConnection verifyMUHomeKitIdentityProof:identifier:accountAltDSID:completion:]_block_invoke
+ ___82-[RPConnection verifyMUHomeKitIdentityProof:identifier:accountAltDSID:completion:]_block_invoke_2
+ ___block_descriptor_40_e8_32r_e19_B36?0r*8i16r*20Q28l
+ ___block_descriptor_49_e8_32s40bs_e27_v24?0"NSSet"8"NSError"16l
+ ___block_descriptor_56_e8_32s40s48bs_e45_v24?0"NSObject<OS_xpc_object>"8"NSError"16l
+ ___block_descriptor_64_e8_32s40s48bs_e5_v8?0l
+ ___block_descriptor_65_e8_32s40s48bs56r_e25_v20?0B8"CUPairedPeer"12l
+ ___block_descriptor_72_e8_32s40s48s56bs_e5_v8?0l
+ ___block_descriptor_88_e8_32s40s48s56s64s72bs80r_e23_v20?0B8"RPIdentity"12l
+ ___copy_helper_block_e8_32s40s48s56s64s72b80r
+ ___destroy_helper_block_e8_32s40s48s56s64s72s80r
+ __swift_closure_destructor.142Tm
+ __swift_closure_destructor.154Tm
+ __swift_closure_destructor.186Tm
+ __swift_closure_destructor.253Tm
+ __xpc_type_dictionary
+ _gLogCategory_RPAccessPolicyClient
+ _nw_endpoint_copy_dictionary
+ _nw_endpoint_copy_txt_record
+ _nw_endpoint_create_from_dictionary
+ _nw_endpoint_set_txt_record
+ _nw_parameters_copy_dictionary
+ _nw_txt_record_access_key
+ _nw_txt_record_create_dictionary
+ _nw_txt_record_set_key
+ _objc_msgSend$_activateWithPolicy:forService:completion:
+ _objc_msgSend$_identityDaemonGetPairingIdentityFromHomeWithAccessory:completion:
+ _objc_msgSend$_multiUserDeviceWithIdentifier:
+ _objc_msgSend$_requestIDIsHighVolume:messageIsChatty:
+ _objc_msgSend$_triggerInfoRequest
+ _objc_msgSend$_updateState:
+ _objc_msgSend$_xpcActivate:completion:
+ _objc_msgSend$_xpcInterrupted
+ _objc_msgSend$_xpcInvalidated
+ _objc_msgSend$_xpcSetup
+ _objc_msgSend$accessPolicyClientActivate:serviceName:completion:
+ _objc_msgSend$cStringUsingEncoding:
+ _objc_msgSend$endpointContextForService:trustCircles:completion:
+ _objc_msgSend$endpointContextForService:trustCircles:encodedParameters:completion:
+ _objc_msgSend$identityResolved
+ _objc_msgSend$identityVerified
+ _objc_msgSend$initWithArray:
+ _objc_msgSend$intersectSet:
+ _objc_msgSend$isEqualToSet:
+ _objc_msgSend$minusSet:
+ _objc_msgSend$resolveIdentityforSignature:data:flags:accountaltDSID:
+ _objc_msgSend$scanUnsignedLongLong:
+ _objc_msgSend$setDevices:
+ _objc_msgSend$setXPCType:forSelector:argumentIndex:ofReply:
+ _objc_msgSend$statusFlagsForTXTRecord:
+ _objc_msgSend$stringValue
+ _objc_msgSend$updateEncodedEndpoint:forService:usingContext:completion:
+ _objc_msgSend$updateStatusFlags:onTXTRecord:operation:
+ _sepBackedIdentityEnabled.enabled
+ _swift_deletedMethodError
+ _symbolic So10RPIdentityC
+ _symbolic So10RPIdentityCSgIeghg_
+ _symbolic So16CUPairingSessionCSgXw
+ _symbolic So16CUPairingSessionCSgXwz_Xx
+ _symbolic yySo10RPIdentityCSgYbccSg
- -[RPConnection _requestIDLogLevel:chatty:]
- GCC_except_table290
- GCC_except_table76
- GCC_except_table78
- GCC_except_table97
- OBJC_IVAR_$_RPConnection._identityVerified
- __swift_closure_destructor.143Tm
- __swift_closure_destructor.175Tm
- __swift_closure_destructor.242Tm
- __swift_closure_destructor.250Tm
- _objc_msgSend$_requestIDLogLevel:chatty:
CStrings:
+ "### Failed to obtain local account for multi-user HK verify\n"
+ "### Specifying the trust flags using RPOptionStatusFlags for registering message '%@' is required."
+ "-[RPAccessPolicyClient _activateWithPolicy:forService:completion:]"
+ "-[RPAccessPolicyClient _invalidate]"
+ "-[RPAccessPolicyClient _invalidated]"
+ "-[RPAccessPolicyClient _updateState:]"
+ "-[RPAccessPolicyClient _xpcActivate:completion:]"
+ "-[RPAccessPolicyClient _xpcActivate:completion:]_block_invoke"
+ "-[RPAccessPolicyClient _xpcInterrupted]"
+ "-[RPAccessPolicyClient _xpcInvalidated]"
+ "-[RPAccessPolicyClient _xpcSetup]"
+ "-[RPAccessPolicyClient accessPolicyUpdatedDevices:]"
+ "-[RPAccessPolicyClient setDevices:]"
+ "-[RPClient endpointContextForService:trustCircles:completion:]"
+ "-[RPClient endpointContextForService:trustCircles:parameters:completion:]"
+ "-[RPClient endpointContextForService:trustCircles:parameters:completion:]_block_invoke"
+ "-[RPClient updateEndpointAttributes:forService:usingContext:completion:]"
+ "-[RPClient updateEndpointAttributes:forService:usingContext:completion:]_block_invoke"
+ "-[RPClient updateEndpointAttributes:forService:usingContext:completion:]_block_invoke_3"
+ "-[RPConnection verifyMUHomeKitIdentityProof:identifier:accountAltDSID:completion:]"
+ "Access permitted for %@ for %@"
+ "Access permitted for %~@ for %@"
+ "Access revoked for %@ for %@"
+ "Access revoked for %~@ for %@"
+ "Activating with policy %u for %@"
+ "Activation complete for %@ (%lu existing devices)"
+ "Activation failed for %@: %{error}"
+ "B36@?0r*8i16r*20Q28"
+ "Capture"
+ "Cockpit"
+ "Devices changed (%lu -> %lu) for %@: %lu added, %lu removed, %lu unchanged"
+ "Error updating state to %u: %{error}"
+ "Failed to decode endpoint"
+ "Failed to encode endpoint"
+ "Failed to encode parameters"
+ "Failed to encode parameters %@ for %@: %{error}"
+ "Failed to resolve client HomeKit pairing identity for %s: %@"
+ "Failed to update attributes of endpoint %@ for %@: %{error}"
+ "Identity daemon not available"
+ "Ignoring device update (%lu devices) for %@ from daemon in state %u"
+ "Invalid policy %u"
+ "Invalid service name '%@'"
+ "Invalid state transition %u -> %u"
+ "Invalidating"
+ "MusicHandoffScan"
+ "No change in devices: "
+ "No context provided"
+ "No endpoint provided"
+ "PairVerify activate client"
+ "PairVerify activate client: session no longer current, ignoring"
+ "PairVerify client identity resolution result nil, will use default"
+ "PairVerify client identity resolution: session no longer current, ignoring"
+ "PairVerify client ignoring resolved identity %@, handler already set"
+ "PairVerify client will use resolved identity %@"
+ "PairVerify prepare client: AT %{public}s, CF %{public}s, FL %{public}s, PWT %{public}s"
+ "PairVerify will resolve client identity before activation"
+ "RPAccessPolicyClient"
+ "Reactivation complete for %@ (%lu existing devices)"
+ "Reactivation failed for %@: %{error}"
+ "Received device update (%lu devices) for %@ from daemon"
+ "Requesting endpoint context for %@ with %#ll{flags}\n"
+ "Requesting endpoint context for %@ with %@ and %#ll{flags}\n"
+ "Resolving client HomeKit pairing identity for %s"
+ "SEPBackedIdentity"
+ "SpeakerGroupSetup"
+ "SpeakerGroupSetupDemoApp"
+ "Starting in invalid state %u"
+ "StatusFlags"
+ "Successfully resolved client HomeKit pairing identity for %s to %@"
+ "Successfully updated attributes of endpoint %@ for %@: %@"
+ "Unable to activate for %@ with XPC error %{error}"
+ "Unable to activate for %@: %{error}"
+ "Unable to activate: %{error}"
+ "Unable to reactivate for %@ with XPC error %{error}"
+ "Unable to reactivate for %@: %{error}"
+ "Unable to resolve client HomeKit pairing identity for %s"
+ "Unable to setup XPC in state %u"
+ "Unexpected state %u"
+ "Updating endpoint %@ for %@ with context (%lu bytes)\n"
+ "Updating state: %u -> %u"
+ "XPC connection interrupted"
+ "_vtDurMs"
+ "_vtPhrase"
+ "_vtTwoShotSec"
+ "com.apple.rapport.AccessPolicy"
+ "iCrowd"
+ "missingFlag.MultiUser"
+ "multiUserDevID"
+ "tutool"
+ "v24@?0@\"NSObject<OS_xpc_object>\"8@\"NSError\"16"
+ "v24@?0@\"NSSet\"8@\"NSError\"16"
- "### Specifying the trust flags using RPOptionStatusFlags for registering message '%@' is required. Please file a radar in 'Rapport | All' to get more information."
- "FaceTimeAgent"
- "GeneralKnowledgeAgent"
- "HomeKitAgent"
- "HomepodSystemAgent"
- "IMSHPApp"
- "IMSTVApp"
- "MediaAgent"
- "PairVerify start client: AT %{public}s, CF %{public}s, FL %{public}s, PWT %{public}s"
- "PhotosAgent"
- "ScreenSaverAgent"
- "SearchAgent"
- "SystemAgent"
- "idacd"
- "idactool"
- "imsutil"
```
