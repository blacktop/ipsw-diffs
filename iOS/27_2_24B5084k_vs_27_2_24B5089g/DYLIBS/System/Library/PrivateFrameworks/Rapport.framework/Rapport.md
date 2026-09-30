## Rapport

> `/System/Library/PrivateFrameworks/Rapport.framework/Rapport`

```diff

-751.200.31.0.0
-  __TEXT.__text: 0xd8a60
-  __TEXT.__objc_methlist: 0x9fe0
-  __TEXT.__cstring: 0x145fc
+751.200.41.0.0
+  __TEXT.__text: 0xdaa1c
+  __TEXT.__objc_methlist: 0xa190
+  __TEXT.__cstring: 0x14dfc
   __TEXT.__const: 0x41b8
-  __TEXT.__gcc_except_tab: 0x14d8
+  __TEXT.__gcc_except_tab: 0x1518
   __TEXT.__oslogstring: 0x26fd
   __TEXT.__swift5_typeref: 0xc4f
   __TEXT.__swift5_capture: 0x950

   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x3b50
+  __TEXT.__unwind_info: 0x3bf0
   __TEXT.__eh_frame: 0x960
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2810
-  __DATA_CONST.__objc_classlist: 0x2d0
+  __DATA_CONST.__const: 0x28b0
+  __DATA_CONST.__objc_classlist: 0x2d8
   __DATA_CONST.__objc_catlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x150
+  __DATA_CONST.__objc_protolist: 0x160
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4558
-  __DATA_CONST.__objc_protorefs: 0xe0
-  __DATA_CONST.__objc_superrefs: 0x1f0
+  __DATA_CONST.__objc_selrefs: 0x4600
+  __DATA_CONST.__objc_protorefs: 0xf0
+  __DATA_CONST.__objc_superrefs: 0x1f8
   __DATA_CONST.__objc_arraydata: 0xb0
-  __DATA_CONST.__got: 0x4e0
+  __DATA_CONST.__got: 0x4e8
   __AUTH_CONST.__const: 0x27c0
-  __AUTH_CONST.__cfstring: 0x6100
-  __AUTH_CONST.__objc_const: 0x113e8
+  __AUTH_CONST.__cfstring: 0x6160
+  __AUTH_CONST.__objc_const: 0x11670
   __AUTH_CONST.__objc_intobj: 0x258
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH_CONST.__auth_got: 0x1178
-  __AUTH.__objc_data: 0x1300
+  __AUTH_CONST.__auth_got: 0x1188
+  __AUTH.__objc_data: 0x1350
   __AUTH.__data: 0x538
-  __DATA.__objc_ivar: 0x10f8
-  __DATA.__data: 0x20e8
+  __DATA.__objc_ivar: 0x111c
+  __DATA.__data: 0x2218
   __DATA.__common: 0x68
   __DATA_DIRTY.__objc_data: 0x1318
   __DATA_DIRTY.__data: 0x588

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5785
-  Symbols:   8255
-  CStrings:  3030
+  Functions: 5840
+  Symbols:   8344
+  CStrings:  3081
 
Symbols:
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
+ GCC_except_table10
+ _OBJC_CLASS_$_RPAccessPolicyClient
+ _OBJC_IVAR_$_RPAccessPolicyClient._accessPermittedHandler
+ _OBJC_IVAR_$_RPAccessPolicyClient._accessRevokedHandler
+ _OBJC_IVAR_$_RPAccessPolicyClient._devices
+ _OBJC_IVAR_$_RPAccessPolicyClient._dispatchQueue
+ _OBJC_IVAR_$_RPAccessPolicyClient._invalidationHandler
+ _OBJC_IVAR_$_RPAccessPolicyClient._policy
+ _OBJC_IVAR_$_RPAccessPolicyClient._serviceName
+ _OBJC_IVAR_$_RPAccessPolicyClient._state
+ _OBJC_IVAR_$_RPAccessPolicyClient._xpcConnection
+ _OBJC_METACLASS_$_RPAccessPolicyClient
+ __OBJC_$_INSTANCE_METHODS_RPAccessPolicyClient
+ __OBJC_$_INSTANCE_VARIABLES_RPAccessPolicyClient
+ __OBJC_$_PROP_LIST_RPAccessPolicyClient
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_RPAccessPolicyXPCClientInterface
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_RPAccessPolicyXPCServerInterface
+ __OBJC_$_PROTOCOL_METHOD_TYPES_RPAccessPolicyXPCClientInterface
+ __OBJC_$_PROTOCOL_METHOD_TYPES_RPAccessPolicyXPCServerInterface
+ __OBJC_CLASS_PROTOCOLS_$_RPAccessPolicyClient
+ __OBJC_CLASS_RO_$_RPAccessPolicyClient
+ __OBJC_LABEL_PROTOCOL_$_RPAccessPolicyXPCClientInterface
+ __OBJC_LABEL_PROTOCOL_$_RPAccessPolicyXPCServerInterface
+ __OBJC_METACLASS_RO_$_RPAccessPolicyClient
+ __OBJC_PROTOCOL_$_RPAccessPolicyXPCClientInterface
+ __OBJC_PROTOCOL_$_RPAccessPolicyXPCServerInterface
+ __OBJC_PROTOCOL_REFERENCE_$_RPAccessPolicyXPCClientInterface
+ __OBJC_PROTOCOL_REFERENCE_$_RPAccessPolicyXPCServerInterface
+ ___33-[RPAccessPolicyClient _xpcSetup]_block_invoke
+ ___33-[RPAccessPolicyClient _xpcSetup]_block_invoke_2
+ ___34-[RPAccessPolicyClient invalidate]_block_invoke
+ ___48-[RPAccessPolicyClient _xpcActivate:completion:]_block_invoke
+ ___48-[RPAccessPolicyClient _xpcActivate:completion:]_block_invoke_2
+ ___62-[RPClient endpointContextForService:trustCircles:completion:]_block_invoke_2
+ ___65-[RPAccessPolicyClient activateWithPolicy:forService:completion:]_block_invoke
+ ___72-[RPClient updateEndpointAttributes:forService:usingContext:completion:]_block_invoke_2
+ ___72-[RPClient updateEndpointAttributes:forService:usingContext:completion:]_block_invoke_3
+ ___block_descriptor_49_e8_32s40bs_e27_v24?0"NSSet"8"NSError"16ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e45_v24?0"NSObject<OS_xpc_object>"8"NSError"16ls48l8s32l8s40l8
+ ___block_descriptor_60_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48bs_e5_v8?0ls32l8s48l8s40l8
+ __xpc_type_dictionary
+ _gLogCategory_RPAccessPolicyClient
+ _nw_endpoint_copy_dictionary
+ _nw_endpoint_create_from_dictionary
+ _objc_msgSend$_activateWithPolicy:forService:completion:
+ _objc_msgSend$_updateState:
+ _objc_msgSend$_xpcActivate:completion:
+ _objc_msgSend$_xpcInterrupted
+ _objc_msgSend$_xpcInvalidated
+ _objc_msgSend$_xpcSetup
+ _objc_msgSend$accessPolicyClientActivate:serviceName:completion:
+ _objc_msgSend$endpointContextForService:trustCircles:completion:
+ _objc_msgSend$initWithArray:
+ _objc_msgSend$intersectSet:
+ _objc_msgSend$isEqualToSet:
+ _objc_msgSend$minusSet:
+ _objc_msgSend$setDevices:
+ _objc_msgSend$setXPCType:forSelector:argumentIndex:ofReply:
+ _objc_msgSend$updateEncodedEndpoint:forService:usingContext:completion:
CStrings:
+ "-[RPAccessPolicyClient _activateWithPolicy:forService:completion:]"
+ "-[RPAccessPolicyClient _invalidate]"
+ "-[RPAccessPolicyClient _invalidated]"
+ "-[RPAccessPolicyClient _updateState:]"
+ "-[RPAccessPolicyClient _xpcActivate:completion:]"
+ "-[RPAccessPolicyClient _xpcActivate:completion:]_block_invoke"
+ "-[RPAccessPolicyClient _xpcActivate:completion:]_block_invoke_2"
+ "-[RPAccessPolicyClient _xpcInterrupted]"
+ "-[RPAccessPolicyClient _xpcInvalidated]"
+ "-[RPAccessPolicyClient _xpcSetup]"
+ "-[RPAccessPolicyClient accessPolicyUpdatedDevices:]"
+ "-[RPAccessPolicyClient setDevices:]"
+ "-[RPClient updateEndpointAttributes:forService:usingContext:completion:]_block_invoke"
+ "-[RPClient updateEndpointAttributes:forService:usingContext:completion:]_block_invoke_3"
+ "Access permitted for %@ for %@"
+ "Access revoked for %@ for %@"
+ "Activating with policy %u for %@"
+ "Activation complete for %@ (%lu existing devices)"
+ "Activation failed for %@: %{error}"
+ "Capture"
+ "Cockpit"
+ "Devices changed (%lu -> %lu) for %@: %lu added, %lu removed, %lu unchanged"
+ "Error updating state to %u: %{error}"
+ "Failed to decode endpoint"
+ "Failed to encode endpoint"
+ "Failed to update attributes of endpoint %@ for %@: %{error}"
+ "Ignoring device update (%lu devices) for %@ from daemon in state %u"
+ "Invalid policy %u"
+ "Invalid service name '%@'"
+ "Invalid state transition %u -> %u"
+ "Invalidating"
+ "No change in devices: %@"
+ "No endpoint provided"
+ "RPAccessPolicyClient"
+ "Reactivation complete for %@ (%lu existing devices)"
+ "Reactivation failed for %@: %{error}"
+ "Received device update (%lu devices) for %@ from daemon"
+ "Starting in invalid state %u"
+ "Successfully updated attributes of endpoint %@ for %@: %@"
+ "Unable to activate for %@ with XPC error %{error}"
+ "Unable to activate for %@: %{error}"
+ "Unable to activate: %{error}"
+ "Unable to reactivate for %@ with XPC error %{error}"
+ "Unable to reactivate for %@: %{error}"
+ "Unable to setup XPC in state %u"
+ "Unexpected state %u"
+ "Updating state: %u -> %u"
+ "XPC connection interrupted"
+ "com.apple.rapport.AccessPolicy"
+ "v24@?0@\"NSObject<OS_xpc_object>\"8@\"NSError\"16"
+ "v24@?0@\"NSSet\"8@\"NSError\"16"
```
