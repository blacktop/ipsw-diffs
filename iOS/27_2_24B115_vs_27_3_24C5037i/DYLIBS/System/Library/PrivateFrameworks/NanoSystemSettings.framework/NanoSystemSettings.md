## NanoSystemSettings

> `/System/Library/PrivateFrameworks/NanoSystemSettings.framework/NanoSystemSettings`

```diff

-383.0.0.0.0
-  __TEXT.__text: 0x36c3c
-  __TEXT.__objc_methlist: 0x3fec
-  __TEXT.__cstring: 0x1523
-  __TEXT.__const: 0x4d2
-  __TEXT.__gcc_except_tab: 0x6cc
-  __TEXT.__oslogstring: 0x722
-  __TEXT.__swift5_typeref: 0x146
-  __TEXT.__swift5_reflstr: 0x64
+386.0.0.0.0
+  __TEXT.__text: 0x3b3a0
+  __TEXT.__objc_methlist: 0x4424
+  __TEXT.__cstring: 0x1661
+  __TEXT.__const: 0x528
+  __TEXT.__gcc_except_tab: 0x74c
+  __TEXT.__oslogstring: 0x792
+  __TEXT.__swift5_typeref: 0x14b
+  __TEXT.__swift5_reflstr: 0x82
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__constg_swiftt: 0xf8
-  __TEXT.__swift5_fieldmd: 0x6c
+  __TEXT.__swift5_fieldmd: 0x84
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__swift5_proto: 0x34
+  __TEXT.__swift5_proto: 0x38
   __TEXT.__swift5_types: 0x10
-  __TEXT.__unwind_info: 0x10b8
+  __TEXT.__unwind_info: 0x1230
   __TEXT.__eh_frame: 0x1f0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x940
-  __DATA_CONST.__objc_classlist: 0x218
+  __DATA_CONST.__const: 0x968
+  __DATA_CONST.__objc_classlist: 0x240
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1450
+  __DATA_CONST.__objc_selrefs: 0x1518
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x208
-  __DATA_CONST.__got: 0x298
-  __AUTH_CONST.__const: 0x230
-  __AUTH_CONST.__cfstring: 0x1fa0
-  __AUTH_CONST.__objc_const: 0x64d8
-  __AUTH_CONST.__auth_got: 0x5c8
-  __AUTH.__objc_data: 0xd60
-  __DATA.__objc_ivar: 0x30c
-  __DATA.__data: 0x2e8
+  __DATA_CONST.__objc_superrefs: 0x230
+  __DATA_CONST.__got: 0x2b8
+  __AUTH_CONST.__const: 0x260
+  __AUTH_CONST.__cfstring: 0x2020
+  __AUTH_CONST.__objc_const: 0x6bf8
+  __AUTH_CONST.__auth_got: 0x610
+  __AUTH.__objc_data: 0xef0
+  __DATA.__objc_ivar: 0x338
+  __DATA.__data: 0x308
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x7d0
   __DATA_DIRTY.__data: 0xc8

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1594
-  Symbols:   2519
-  CStrings:  336
+  Functions: 1711
+  Symbols:   2669
+  CStrings:  349
 
Symbols:
+ -[NSSCancelSecurePairingMsg .cxx_destruct]
+ -[NSSCancelSecurePairingMsg copyTo:]
+ -[NSSCancelSecurePairingMsg copyWithZone:]
+ -[NSSCancelSecurePairingMsg description]
+ -[NSSCancelSecurePairingMsg dictionaryRepresentation]
+ -[NSSCancelSecurePairingMsg hasRequestIdentifier]
+ -[NSSCancelSecurePairingMsg hash]
+ -[NSSCancelSecurePairingMsg isEqual:]
+ -[NSSCancelSecurePairingMsg mergeFrom:]
+ -[NSSCancelSecurePairingMsg readFrom:]
+ -[NSSCancelSecurePairingMsg requestIdentifier]
+ -[NSSCancelSecurePairingMsg setRequestIdentifier:]
+ -[NSSCancelSecurePairingMsg writeTo:]
+ -[NSSManager awaitSecurePairingAlertStatus:]
+ -[NSSManager cancelSecurePairing:]
+ -[NSSManager securePairingDidFinish:]
+ -[NSSManager startSecurePairing:]
+ -[NSSRequestSecurePairingFromGizmoMsg copyTo:]
+ -[NSSRequestSecurePairingFromGizmoMsg copyWithZone:]
+ -[NSSRequestSecurePairingFromGizmoMsg description]
+ -[NSSRequestSecurePairingFromGizmoMsg dictionaryRepresentation]
+ -[NSSRequestSecurePairingFromGizmoMsg entryPoint]
+ -[NSSRequestSecurePairingFromGizmoMsg hasEntryPoint]
+ -[NSSRequestSecurePairingFromGizmoMsg hash]
+ -[NSSRequestSecurePairingFromGizmoMsg isEqual:]
+ -[NSSRequestSecurePairingFromGizmoMsg mergeFrom:]
+ -[NSSRequestSecurePairingFromGizmoMsg readFrom:]
+ -[NSSRequestSecurePairingFromGizmoMsg setEntryPoint:]
+ -[NSSRequestSecurePairingFromGizmoMsg setHasEntryPoint:]
+ -[NSSRequestSecurePairingFromGizmoMsg writeTo:]
+ -[NSSSecurePairingAlertStatusMsg .cxx_destruct]
+ -[NSSSecurePairingAlertStatusMsg copyTo:]
+ -[NSSSecurePairingAlertStatusMsg copyWithZone:]
+ -[NSSSecurePairingAlertStatusMsg description]
+ -[NSSSecurePairingAlertStatusMsg dictionaryRepresentation]
+ -[NSSSecurePairingAlertStatusMsg hasRequestIdentifier]
+ -[NSSSecurePairingAlertStatusMsg hasStatus]
+ -[NSSSecurePairingAlertStatusMsg hash]
+ -[NSSSecurePairingAlertStatusMsg isEqual:]
+ -[NSSSecurePairingAlertStatusMsg mergeFrom:]
+ -[NSSSecurePairingAlertStatusMsg readFrom:]
+ -[NSSSecurePairingAlertStatusMsg requestIdentifier]
+ -[NSSSecurePairingAlertStatusMsg setHasStatus:]
+ -[NSSSecurePairingAlertStatusMsg setRequestIdentifier:]
+ -[NSSSecurePairingAlertStatusMsg setStatus:]
+ -[NSSSecurePairingAlertStatusMsg status]
+ -[NSSSecurePairingAlertStatusMsg writeTo:]
+ -[NSSStartSecurePairingMsg copyTo:]
+ -[NSSStartSecurePairingMsg copyWithZone:]
+ -[NSSStartSecurePairingMsg description]
+ -[NSSStartSecurePairingMsg dictionaryRepresentation]
+ -[NSSStartSecurePairingMsg expireAt]
+ -[NSSStartSecurePairingMsg hasExpireAt]
+ -[NSSStartSecurePairingMsg hash]
+ -[NSSStartSecurePairingMsg isEqual:]
+ -[NSSStartSecurePairingMsg mergeFrom:]
+ -[NSSStartSecurePairingMsg readFrom:]
+ -[NSSStartSecurePairingMsg setExpireAt:]
+ -[NSSStartSecurePairingMsg setHasExpireAt:]
+ -[NSSStartSecurePairingMsg writeTo:]
+ -[NSSStartSecurePairingRespMsg .cxx_destruct]
+ -[NSSStartSecurePairingRespMsg copyTo:]
+ -[NSSStartSecurePairingRespMsg copyWithZone:]
+ -[NSSStartSecurePairingRespMsg description]
+ -[NSSStartSecurePairingRespMsg dictionaryRepresentation]
+ -[NSSStartSecurePairingRespMsg error]
+ -[NSSStartSecurePairingRespMsg hasError]
+ -[NSSStartSecurePairingRespMsg hasSuccess]
+ -[NSSStartSecurePairingRespMsg hash]
+ -[NSSStartSecurePairingRespMsg isEqual:]
+ -[NSSStartSecurePairingRespMsg mergeFrom:]
+ -[NSSStartSecurePairingRespMsg readFrom:]
+ -[NSSStartSecurePairingRespMsg setError:]
+ -[NSSStartSecurePairingRespMsg setHasSuccess:]
+ -[NSSStartSecurePairingRespMsg setSuccess:]
+ -[NSSStartSecurePairingRespMsg success]
+ -[NSSStartSecurePairingRespMsg writeTo:]
+ GCC_except_table227
+ GCC_except_table234
+ GCC_except_table241
+ GCC_except_table248
+ _NSSCancelSecurePairingMsgReadFrom
+ _NSSRequestSecurePairingFromGizmoMsgReadFrom
+ _NSSSecurePairingAlertStatusMsgReadFrom
+ _NSSStartSecurePairingMsgReadFrom
+ _NSSStartSecurePairingRespMsgReadFrom
+ _OBJC_CLASS_$_NSSCancelSecurePairingMsg
+ _OBJC_CLASS_$_NSSRequestSecurePairingFromGizmoMsg
+ _OBJC_CLASS_$_NSSSecurePairingAlertStatusMsg
+ _OBJC_CLASS_$_NSSStartSecurePairingMsg
+ _OBJC_CLASS_$_NSSStartSecurePairingRespMsg
+ _OBJC_IVAR_$_NSSCancelSecurePairingMsg._requestIdentifier
+ _OBJC_IVAR_$_NSSRequestSecurePairingFromGizmoMsg._entryPoint
+ _OBJC_IVAR_$_NSSRequestSecurePairingFromGizmoMsg._has
+ _OBJC_IVAR_$_NSSSecurePairingAlertStatusMsg._has
+ _OBJC_IVAR_$_NSSSecurePairingAlertStatusMsg._requestIdentifier
+ _OBJC_IVAR_$_NSSSecurePairingAlertStatusMsg._status
+ _OBJC_IVAR_$_NSSStartSecurePairingMsg._expireAt
+ _OBJC_IVAR_$_NSSStartSecurePairingMsg._has
+ _OBJC_IVAR_$_NSSStartSecurePairingRespMsg._error
+ _OBJC_IVAR_$_NSSStartSecurePairingRespMsg._has
+ _OBJC_IVAR_$_NSSStartSecurePairingRespMsg._success
+ _OBJC_METACLASS_$_NSSCancelSecurePairingMsg
+ _OBJC_METACLASS_$_NSSRequestSecurePairingFromGizmoMsg
+ _OBJC_METACLASS_$_NSSSecurePairingAlertStatusMsg
+ _OBJC_METACLASS_$_NSSStartSecurePairingMsg
+ _OBJC_METACLASS_$_NSSStartSecurePairingRespMsg
+ _PBDataWriterWriteDoubleField
+ __OBJC_$_INSTANCE_METHODS_NSSCancelSecurePairingMsg
+ __OBJC_$_INSTANCE_METHODS_NSSRequestSecurePairingFromGizmoMsg
+ __OBJC_$_INSTANCE_METHODS_NSSSecurePairingAlertStatusMsg
+ __OBJC_$_INSTANCE_METHODS_NSSStartSecurePairingMsg
+ __OBJC_$_INSTANCE_METHODS_NSSStartSecurePairingRespMsg
+ __OBJC_$_INSTANCE_VARIABLES_NSSCancelSecurePairingMsg
+ __OBJC_$_INSTANCE_VARIABLES_NSSRequestSecurePairingFromGizmoMsg
+ __OBJC_$_INSTANCE_VARIABLES_NSSSecurePairingAlertStatusMsg
+ __OBJC_$_INSTANCE_VARIABLES_NSSStartSecurePairingMsg
+ __OBJC_$_INSTANCE_VARIABLES_NSSStartSecurePairingRespMsg
+ __OBJC_$_PROP_LIST_NSSCancelSecurePairingMsg
+ __OBJC_$_PROP_LIST_NSSRequestSecurePairingFromGizmoMsg
+ __OBJC_$_PROP_LIST_NSSSecurePairingAlertStatusMsg
+ __OBJC_$_PROP_LIST_NSSStartSecurePairingMsg
+ __OBJC_$_PROP_LIST_NSSStartSecurePairingRespMsg
+ __OBJC_CLASS_PROTOCOLS_$_NSSCancelSecurePairingMsg
+ __OBJC_CLASS_PROTOCOLS_$_NSSRequestSecurePairingFromGizmoMsg
+ __OBJC_CLASS_PROTOCOLS_$_NSSSecurePairingAlertStatusMsg
+ __OBJC_CLASS_PROTOCOLS_$_NSSStartSecurePairingMsg
+ __OBJC_CLASS_PROTOCOLS_$_NSSStartSecurePairingRespMsg
+ __OBJC_CLASS_RO_$_NSSCancelSecurePairingMsg
+ __OBJC_CLASS_RO_$_NSSRequestSecurePairingFromGizmoMsg
+ __OBJC_CLASS_RO_$_NSSSecurePairingAlertStatusMsg
+ __OBJC_CLASS_RO_$_NSSStartSecurePairingMsg
+ __OBJC_CLASS_RO_$_NSSStartSecurePairingRespMsg
+ __OBJC_METACLASS_RO_$_NSSCancelSecurePairingMsg
+ __OBJC_METACLASS_RO_$_NSSRequestSecurePairingFromGizmoMsg
+ __OBJC_METACLASS_RO_$_NSSSecurePairingAlertStatusMsg
+ __OBJC_METACLASS_RO_$_NSSStartSecurePairingMsg
+ __OBJC_METACLASS_RO_$_NSSStartSecurePairingRespMsg
+ ___33-[NSSManager startSecurePairing:]_block_invoke
+ ___33-[NSSManager startSecurePairing:]_block_invoke_2
+ ___34-[NSSManager cancelSecurePairing:]_block_invoke
+ ___34-[NSSManager cancelSecurePairing:]_block_invoke_2
+ ___37-[NSSManager securePairingDidFinish:]_block_invoke
+ ___37-[NSSManager securePairingDidFinish:]_block_invoke_2
+ ___44-[NSSManager awaitSecurePairingAlertStatus:]_block_invoke
+ ___44-[NSSManager awaitSecurePairingAlertStatus:]_block_invoke_2
+ ___block_descriptor_48_e8_32bs40w_e20_v24?0q8"NSError"16lw40l8s32l8
+ ___swift_allocate_boxed_opaque_existential_0
+ ___unnamed_7
+ _swift_allocBox
+ _symbolic _____Sg 16GenerativeModels0aB12AvailabilityV6PolicyV
- ___unnamed_5
CStrings:
+ "%s: status: (%ld), error: (%@)"
+ "-[NSSManager awaitSecurePairingAlertStatus:]_block_invoke_2"
+ "-[NSSManager cancelSecurePairing:]_block_invoke_2"
+ "-[NSSManager securePairingDidFinish:]_block_invoke_2"
+ "-[NSSManager startSecurePairing:]_block_invoke_2"
+ "Overriding availability from %ld to .unavailable for China policy legacy compatibility"
+ "entryPoint"
+ "expireAt"
+ "isChinaPolicy"
+ "rawAvailability"
+ "requestIdentifier"
+ "status"
+ "v24@?0q8@\"NSError\"16"
```
