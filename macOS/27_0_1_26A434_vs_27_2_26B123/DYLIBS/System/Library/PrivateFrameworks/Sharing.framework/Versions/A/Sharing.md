## Sharing

> `/System/Library/PrivateFrameworks/Sharing.framework/Versions/A/Sharing`

```diff

-2130.10.2.1.5
-  __TEXT.__text: 0x33eef0
-  __TEXT.__objc_methlist: 0x12c34
-  __TEXT.__cstring: 0x2c868
-  __TEXT.__const: 0x20f9c
-  __TEXT.__gcc_except_tab: 0x353c
-  __TEXT.__oslogstring: 0xc983
+2131.21.31.1.3
+  __TEXT.__text: 0x3516f4
+  __TEXT.__objc_methlist: 0x12ebc
+  __TEXT.__cstring: 0x2cf48
+  __TEXT.__const: 0x21f8c
+  __TEXT.__gcc_except_tab: 0x35b0
+  __TEXT.__oslogstring: 0xcff3
   __TEXT.__dlopen_cstrs: 0x5f2
   __TEXT.__ustring: 0x18
-  __TEXT.__swift5_typeref: 0x864f
-  __TEXT.__constg_swiftt: 0x6f4c
-  __TEXT.__swift5_reflstr: 0x3bda
-  __TEXT.__swift5_fieldmd: 0x6b88
+  __TEXT.__swift5_typeref: 0x8a0f
+  __TEXT.__constg_swiftt: 0x726c
+  __TEXT.__swift5_reflstr: 0x420a
+  __TEXT.__swift5_fieldmd: 0x7068
   __TEXT.__swift5_builtin: 0x1e0
-  __TEXT.__swift5_assocty: 0xfa0
-  __TEXT.__swift5_capture: 0x28f4
-  __TEXT.__swift5_protos: 0x24
-  __TEXT.__swift5_proto: 0x1bdc
-  __TEXT.__swift5_types: 0x910
-  __TEXT.__swift_as_entry: 0x3fc
-  __TEXT.__swift_as_ret: 0x3fc
-  __TEXT.__swift_as_cont: 0xa50
+  __TEXT.__swift5_assocty: 0x1130
+  __TEXT.__swift5_capture: 0x29e4
+  __TEXT.__swift5_protos: 0x28
+  __TEXT.__swift5_proto: 0x1cc8
+  __TEXT.__swift5_types: 0x954
+  __TEXT.__swift_as_entry: 0x40c
+  __TEXT.__swift_as_ret: 0x40c
+  __TEXT.__swift_as_cont: 0xa88
   __TEXT.__swift5_mpenum: 0xb8
-  __TEXT.__unwind_info: 0xd458
-  __TEXT.__eh_frame: 0xe82c
+  __TEXT.__unwind_info: 0xda00
+  __TEXT.__eh_frame: 0xeb74
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2d20
-  __DATA_CONST.__objc_classlist: 0x858
+  __DATA_CONST.__const: 0x2ee8
+  __DATA_CONST.__objc_classlist: 0x878
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x360
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x86a0
+  __DATA_CONST.__objc_selrefs: 0x87b0
   __DATA_CONST.__objc_protorefs: 0x1d8
   __DATA_CONST.__objc_classrefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x508
   __DATA_CONST.__objc_arraydata: 0x2f0
-  __DATA_CONST.__got: 0x1270
-  __AUTH_CONST.__const: 0x1b638
-  __AUTH_CONST.__cfstring: 0x11800
-  __AUTH_CONST.__objc_const: 0x35100
+  __DATA_CONST.__got: 0x12b8
+  __AUTH_CONST.__const: 0x1c4e8
+  __AUTH_CONST.__cfstring: 0x11900
+  __AUTH_CONST.__objc_const: 0x35a38
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x498
   __AUTH_CONST.__objc_dictobj: 0x398
   __AUTH_CONST.__objc_arrayobj: 0xa8
-  __AUTH_CONST.__auth_got: 0x28e0
-  __AUTH_CONST.__auth_ptr: 0x1078
-  __AUTH.__objc_data: 0x5e08
-  __AUTH.__data: 0x3b10
-  __DATA.__objc_ivar: 0x1fc0
-  __DATA.__data: 0xb7a0
-  __DATA.__bss: 0x38240
+  __AUTH_CONST.__auth_got: 0x2970
+  __AUTH_CONST.__auth_ptr: 0x1118
+  __AUTH.__objc_data: 0x2ba8
+  __AUTH.__data: 0x3098
+  __DATA.__objc_ivar: 0x1ff4
+  __DATA.__data: 0xba20
+  __DATA.__bss: 0x39ad0
   __DATA.__common: 0x160
-  __DATA_DIRTY.__objc_data: 0x1120
-  __DATA_DIRTY.__data: 0x540
+  __DATA_DIRTY.__objc_data: 0x45a0
+  __DATA_DIRTY.__data: 0x1388
   __DATA_DIRTY.__bss: 0x428
   __DATA_DIRTY.__common: 0x60
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 21305
-  Symbols:   21113
-  CStrings:  7400
+  Functions: 21939
+  Symbols:   21329
+  CStrings:  7490
 
Symbols:
+ +[SFCollaborationRouteEvent eventName]
+ +[SFCollaborationRouteEvent routeCodeForActivityType:]
+ -[NSURL(Sharing) sf_hasSchemeIn:]
+ -[SFAutoUnlockManager _enableAutoUnlockWithDevice:passcode:passcodeRef:]
+ -[SFAutoUnlockManager _releasePairingContextForDevice:]
+ -[SFAutoUnlockManager enableAutoUnlockWithDevice:passcodeRef:]
+ -[SFAutoUnlockManager pairingLAContexts]
+ -[SFAutoUnlockNotificationModel authToken]
+ -[SFAutoUnlockNotificationModel setAuthToken:]
+ -[SFCollaborationPerformer _failIfMetadataLoadFailed]
+ -[SFCollaborationPerformer _isOptionsLoadInFlightForItem:]
+ -[SFCollaborationPerformer _performAfterOptionsCheck]
+ -[SFCollaborationPerformer _stopWaitingForOptionsLoad]
+ -[SFCollaborationPerformer _submitRouteEventIfNeededWithOutcome:error:]
+ -[SFCollaborationPerformer _suppressRouteEvent]
+ -[SFCollaborationPerformer dealloc]
+ -[SFCollaborationPerformer didReportRouteEvent]
+ -[SFCollaborationPerformer isWaitingForOptionsLoad]
+ -[SFCollaborationPerformer observable:didChange:]
+ -[SFCollaborationPerformer performStartTicks]
+ -[SFCollaborationPerformer reportCreationFailureWithError:]
+ -[SFCollaborationPerformer routeItemType]
+ -[SFCollaborationPerformer setDidReportRouteEvent:]
+ -[SFCollaborationPerformer setIsWaitingForOptionsLoad:]
+ -[SFCollaborationPerformer setPerformStartTicks:]
+ -[SFCollaborationPerformer setRouteItemType:]
+ -[SFCollaborationRouteEvent .cxx_destruct]
+ -[SFCollaborationRouteEvent activityType]
+ -[SFCollaborationRouteEvent errorCode]
+ -[SFCollaborationRouteEvent errorDomain]
+ -[SFCollaborationRouteEvent eventPayload]
+ -[SFCollaborationRouteEvent hostAppBundleID]
+ -[SFCollaborationRouteEvent itemType]
+ -[SFCollaborationRouteEvent outcome]
+ -[SFCollaborationRouteEvent setActivityType:]
+ -[SFCollaborationRouteEvent setErrorCode:]
+ -[SFCollaborationRouteEvent setErrorDomain:]
+ -[SFCollaborationRouteEvent setHostAppBundleID:]
+ -[SFCollaborationRouteEvent setItemType:]
+ -[SFCollaborationRouteEvent setOutcome:]
+ -[SFCollaborationRouteEvent setWaitMs:]
+ -[SFCollaborationRouteEvent submitEvent]
+ -[SFCollaborationRouteEvent waitMs]
+ GCC_except_table100
+ GCC_except_table128
+ GCC_except_table129
+ GCC_except_table135
+ GCC_except_table141
+ GCC_except_table158
+ GCC_except_table160
+ GCC_except_table194
+ GCC_except_table199
+ GCC_except_table200
+ GCC_except_table207
+ GCC_except_table208
+ GCC_except_table78
+ GCC_except_table90
+ OBJC_IVAR_$_SFAutoUnlockManager._pairingLAContexts
+ OBJC_IVAR_$_SFAutoUnlockNotificationModel._authToken
+ OBJC_IVAR_$_SFCollaborationPerformer._didReportRouteEvent
+ OBJC_IVAR_$_SFCollaborationPerformer._isWaitingForOptionsLoad
+ OBJC_IVAR_$_SFCollaborationPerformer._performStartTicks
+ OBJC_IVAR_$_SFCollaborationPerformer._routeItemType
+ OBJC_IVAR_$_SFCollaborationRouteEvent._activityType
+ OBJC_IVAR_$_SFCollaborationRouteEvent._errorCode
+ OBJC_IVAR_$_SFCollaborationRouteEvent._errorDomain
+ OBJC_IVAR_$_SFCollaborationRouteEvent._hostAppBundleID
+ OBJC_IVAR_$_SFCollaborationRouteEvent._itemType
+ OBJC_IVAR_$_SFCollaborationRouteEvent._outcome
+ OBJC_IVAR_$_SFCollaborationRouteEvent._waitMs
+ SFShouldPrintSensitiveData
+ SFShouldPrintSensitiveData.onceToken
+ SFShouldPrintSensitiveData.sensitive
+ SFStringForSensitiveData
+ _OBJC_CLASS_$_SFAirDropInvocationsFetchTTRInactivityNudgeOptOut
+ _OBJC_CLASS_$_SFAirDropInvocationsSetTTRInactivityNudgeOptOut
+ _OBJC_CLASS_$_SFCollaborationRouteEvent
+ _OBJC_METACLASS_$_SFAirDropInvocationsFetchTTRInactivityNudgeOptOut
+ _OBJC_METACLASS_$_SFAirDropInvocationsSetTTRInactivityNudgeOptOut
+ _OBJC_METACLASS_$_SFCollaborationRouteEvent
+ _SFIsDeviceHomeAccessory
+ _SFShouldPrintSensitiveData
+ _SFStringForSensitiveData
+ _SFStringsForSensitiveData
+ __72-[SFAutoUnlockManager _enableAutoUnlockWithDevice:passcode:passcodeRef:]_block_invoke
+ __CLASS_METHODS_SFAirDropInvocationsFetchTTRInactivityNudgeOptOut
+ __CLASS_METHODS_SFAirDropInvocationsSetTTRInactivityNudgeOptOut
+ __CLASS_PROPERTIES_SFAirDropInvocationsFetchTTRInactivityNudgeOptOut
+ __CLASS_PROPERTIES_SFAirDropInvocationsSetTTRInactivityNudgeOptOut
+ __DATA_SFAirDropInvocationsFetchTTRInactivityNudgeOptOut
+ __DATA_SFAirDropInvocationsSetTTRInactivityNudgeOptOut
+ __DATA__TtC7Sharing19SFAccessReportStore
+ __INSTANCE_METHODS_SFAirDropInvocationsFetchTTRInactivityNudgeOptOut
+ __INSTANCE_METHODS_SFAirDropInvocationsSetTTRInactivityNudgeOptOut
+ __IVARS__TtC7Sharing19SFAccessReportStore
+ __METACLASS_DATA_SFAirDropInvocationsFetchTTRInactivityNudgeOptOut
+ __METACLASS_DATA_SFAirDropInvocationsSetTTRInactivityNudgeOptOut
+ __METACLASS_DATA__TtC7Sharing19SFAccessReportStore
+ __OBJC_$_CLASS_METHODS_SFCollaborationRouteEvent
+ __OBJC_$_CLASS_PROP_LIST_SFCollaborationRouteEvent
+ __OBJC_$_INSTANCE_METHODS_SFCollaborationRouteEvent
+ __OBJC_$_INSTANCE_VARIABLES_SFCollaborationRouteEvent
+ __OBJC_$_PROP_LIST_SFCollaborationRouteEvent
+ __OBJC_CLASS_PROTOCOLS_$_SFCollaborationPerformer
+ __OBJC_CLASS_PROTOCOLS_$_SFCollaborationRouteEvent
+ __OBJC_CLASS_RO_$_SFCollaborationRouteEvent
+ __OBJC_METACLASS_RO_$_SFCollaborationRouteEvent
+ ___53-[SFCollaborationPerformer _performAfterOptionsCheck]_block_invoke
+ ___53-[SFCollaborationPerformer _performAfterOptionsCheck]_block_invoke_2
+ ___54-[SFCollaborationPerformer _stopWaitingForOptionsLoad]_block_invoke
+ ___72-[SFAutoUnlockManager _enableAutoUnlockWithDevice:passcode:passcodeRef:]_block_invoke
+ ___72-[SFAutoUnlockManager _enableAutoUnlockWithDevice:passcode:passcodeRef:]_block_invoke_2
+ ___72-[SFAutoUnlockManager _enableAutoUnlockWithDevice:passcode:passcodeRef:]_block_invoke_3
+ ___SFShouldPrintSensitiveData_block_invoke
+ ___block_descriptor_40_e8_32s_e39_B32?0"_SWCollaborationOption"8Q16^B24l
+ __swift__destructor.521Tm
+ __swift_closure_destructor.1400Tm
+ __swift_closure_destructor.445Tm
+ __swift_closure_destructor.448Tm
+ __swift_closure_destructor.466Tm
+ __swift_closure_destructor.478Tm
+ __swift_closure_destructor.644Tm
+ __swift_closure_destructor.989Tm
+ __xpc_type_array
+ _associated conformance 7Sharing14SFAccessReportV10CodingKeys33_3BDD3C3E45FF7210A0FA925F88A08251LLOSHAASQ
+ _associated conformance 7Sharing14SFAccessReportV10CodingKeys33_3BDD3C3E45FF7210A0FA925F88A08251LLOs0D3KeyAAs23CustomStringConvertible
+ _associated conformance 7Sharing14SFAccessReportV10CodingKeys33_3BDD3C3E45FF7210A0FA925F88A08251LLOs0D3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 7Sharing14SFAccessReportVSHAASQ
+ _associated conformance 7Sharing14SFAccessReportVSLAASQ
+ _associated conformance 7Sharing15TapToRadarDraftV0bcD5ErrorO10Foundation09LocalizedF0AAs0F0
+ _associated conformance 7Sharing15TapToRadarDraftV0bcD5ErrorOSHAASQ
+ _associated conformance 7Sharing15TapToRadarDraftV11DeviceClassOSHAASQ
+ _associated conformance 7Sharing15TapToRadarDraftV14ClassificationOSHAASQ
+ _associated conformance 7Sharing15TapToRadarDraftV15AutoDiagnosticsOSHAASQ
+ _associated conformance 7Sharing15TapToRadarDraftV15ReproducibilityOSHAASQ
+ _associated conformance 7Sharing15TapToRadarDraftV22RemoteDeviceSelectionsVSHAASQ
+ _associated conformance 7Sharing15TapToRadarDraftV22RemoteDeviceSelectionsVs10SetAlgebraAASQ
+ _associated conformance 7Sharing15TapToRadarDraftV22RemoteDeviceSelectionsVs10SetAlgebraAAs25ExpressibleByArrayLiteral
+ _associated conformance 7Sharing15TapToRadarDraftV22RemoteDeviceSelectionsVs9OptionSetAASY
+ _associated conformance 7Sharing15TapToRadarDraftV22RemoteDeviceSelectionsVs9OptionSetAAs0J7Algebra
+ _associated conformance 7Sharing15TapToRadarDraftV9ComponentVSHAASQ
+ _associated conformance 7Sharing19SFClientAccessLevelV10CapabilityOSHAASQ
+ _associated conformance 7Sharing19SFClientAccessLevelV10CapabilityOs12CaseIterableAA8AllCasessAFP_Sl
+ _associated conformance 7Sharing20SFAirDropInvocationsO27SetTTRInactivityNudgeOptOutCAA22SFXPCInvocableProtocolAA10ParametersAaFP_SE
+ _associated conformance 7Sharing20SFAirDropInvocationsO27SetTTRInactivityNudgeOptOutCAA22SFXPCInvocableProtocolAA10ParametersAaFP_Se
+ _associated conformance 7Sharing20SFAirDropInvocationsO27SetTTRInactivityNudgeOptOutCAA22SFXPCInvocableProtocolAA8ResponseAaFP_SE
+ _associated conformance 7Sharing20SFAirDropInvocationsO27SetTTRInactivityNudgeOptOutCAA22SFXPCInvocableProtocolAA8ResponseAaFP_Se
+ _associated conformance 7Sharing20SFAirDropInvocationsO29FetchTTRInactivityNudgeOptOutCAA22SFXPCInvocableProtocolAA10ParametersAaFP_SE
+ _associated conformance 7Sharing20SFAirDropInvocationsO29FetchTTRInactivityNudgeOptOutCAA22SFXPCInvocableProtocolAA10ParametersAaFP_Se
+ _associated conformance 7Sharing20SFAirDropInvocationsO29FetchTTRInactivityNudgeOptOutCAA22SFXPCInvocableProtocolAA8ResponseAaFP_SE
+ _associated conformance 7Sharing20SFAirDropInvocationsO29FetchTTRInactivityNudgeOptOutCAA22SFXPCInvocableProtocolAA8ResponseAaFP_Se
+ _associated conformance 7Sharing9URLSchemeVSHAASQ
+ _associated conformance 7Sharing9URLSchemeVs26ExpressibleByStringLiteralAA0eF4TypesADP_s01_cd7BuiltineF0
+ _associated conformance 7Sharing9URLSchemeVs26ExpressibleByStringLiteralAAs0cd23ExtendedGraphemeClusterF0
+ _associated conformance 7Sharing9URLSchemeVs33ExpressibleByUnicodeScalarLiteralAA0efG4TypesADP_s01_cd7BuiltinefG0
+ _associated conformance 7Sharing9URLSchemeVs43ExpressibleByExtendedGraphemeClusterLiteralAA0efgH4TypesADP_s01_cd7BuiltinefgH0
+ _associated conformance 7Sharing9URLSchemeVs43ExpressibleByExtendedGraphemeClusterLiteralAAs0cd13UnicodeScalarH0
+ _generic environment 7Sharing21URLParameterEncodableRzl
+ _objc_msgSend$_enableAutoUnlockWithDevice:passcode:passcodeRef:
+ _objc_msgSend$_failIfMetadataLoadFailed
+ _objc_msgSend$_isOptionsLoadInFlightForItem:
+ _objc_msgSend$_performAfterOptionsCheck
+ _objc_msgSend$_releasePairingContextForDevice:
+ _objc_msgSend$_stopWaitingForOptionsLoad
+ _objc_msgSend$_submitRouteEventIfNeededWithOutcome:error:
+ _objc_msgSend$_suppressRouteEvent
+ _objc_msgSend$authToken
+ _objc_msgSend$enableAutoUnlockWithDevice:passcodeRef:clientProxy:
+ _objc_msgSend$indexOfObjectPassingTest:
+ _objc_msgSend$inheritedParticipants
+ _objc_msgSend$isAnyoneWithLinkSharingAvailable
+ _objc_msgSend$isCurrentUser
+ _objc_msgSend$isReadOnly
+ _objc_msgSend$isWaitingForOptionsLoad
+ _objc_msgSend$itemType
+ _objc_msgSend$outcome
+ _objc_msgSend$routeCodeForActivityType:
+ _objc_msgSend$setAuthToken:
+ _objc_msgSend$setDoesRelativeDateFormatting:
+ _objc_msgSend$setIsWaitingForOptionsLoad:
+ _objc_msgSend$setItemType:
+ _objc_msgSend$setOutcome:
+ _objc_msgSend$setWaitMs:
+ _objc_msgSend$waitMs
+ _os_variant_has_internal_content
+ _swift_getAtKeyPath
+ _symbolic $s7Sharing21URLParameterEncodableP
+ _symbolic $ss26ExpressibleByStringLiteralP
+ _symbolic $ss33ExpressibleByUnicodeScalarLiteralP
+ _symbolic $ss43ExpressibleByExtendedGraphemeClusterLiteralP
+ _symbolic SDySSShy_____GG 7Sharing14SFAccessReportV
+ _symbolic SaySiG
+ _symbolic Say_____G 7Sharing15TapToRadarDraftV11DeviceClassO
+ _symbolic Say_____G 7Sharing19SFClientAccessLevelV10CapabilityO
+ _symbolic Shy_____G 7Sharing14SFAccessReportV
+ _symbolic _____ 7Sharing12URLParameterV
+ _symbolic _____ 7Sharing14SFAccessReportV
+ _symbolic _____ 7Sharing14SFAccessReportV10CodingKeys33_3BDD3C3E45FF7210A0FA925F88A08251LLO
+ _symbolic _____ 7Sharing15TapToRadarDraftV
+ _symbolic _____ 7Sharing15TapToRadarDraftV0bcD5ErrorO
+ _symbolic _____ 7Sharing15TapToRadarDraftV11DeviceClassO
+ _symbolic _____ 7Sharing15TapToRadarDraftV14ClassificationO
+ _symbolic _____ 7Sharing15TapToRadarDraftV15AutoDiagnosticsO
+ _symbolic _____ 7Sharing15TapToRadarDraftV15ReproducibilityO
+ _symbolic _____ 7Sharing15TapToRadarDraftV22RemoteDeviceSelectionsV
+ _symbolic _____ 7Sharing15TapToRadarDraftV9ComponentV
+ _symbolic _____ 7Sharing19SFAccessReportStoreC
+ _symbolic _____ 7Sharing19SFClientAccessLevelV10CapabilityO
+ _symbolic _____ 7Sharing20SFAirDropInvocationsO27SetTTRInactivityNudgeOptOutC
+ _symbolic _____ 7Sharing20SFAirDropInvocationsO29FetchTTRInactivityNudgeOptOutC
+ _symbolic _____ 7Sharing9SFAirDropO17SenderDiagnosticsO
+ _symbolic _____ 7Sharing9URLSchemeV
+ _symbolic _____Sg 10Foundation12URLQueryItemV
+ _symbolic _____Sg 7Sharing15TapToRadarDraftV14ClassificationO
+ _symbolic _____Sg 7Sharing15TapToRadarDraftV15ReproducibilityO
+ _symbolic _____Sg 7Sharing15TapToRadarDraftV9ComponentV
+ _symbolic _____ySSSgG 7Sharing12URLParameterV
+ _symbolic _____ySSShy_____GG s18_DictionaryStorageC 7Sharing14SFAccessReportV
+ _symbolic _____ySaySSGG 7Sharing12URLParameterV
+ _symbolic _____ySaySiGG 7Sharing12URLParameterV
+ _symbolic _____ySay_____GG 7Sharing12URLParameterV 10Foundation3URLV
+ _symbolic _____ySay_____GG 7Sharing12URLParameterV AA15TapToRadarDraftV11DeviceClassO
+ _symbolic _____ySbG 7Sharing12URLParameterV
+ _symbolic _____ySdG 7Sharing13SFUserDefaultC
+ _symbolic _____ySdG 7Sharing18AirDropUserDefaultC
+ _symbolic _____ySdSg_____G 7Combine19CurrentValueSubjectC s5NeverO
+ _symbolic _____y_____G 7Sharing12URLParameterV AA15TapToRadarDraftV15AutoDiagnosticsO
+ _symbolic _____y_____G 7Sharing12URLParameterV AA15TapToRadarDraftV22RemoteDeviceSelectionsV
+ _symbolic _____y_____G s11_SetStorageC 7Sharing14SFAccessReportV
+ _symbolic _____y_____G s22KeyedDecodingContainerV 7Sharing14SFAccessReportV10CodingKeys33_3BDD3C3E45FF7210A0FA925F88A08251LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 7Sharing14SFAccessReportV10CodingKeys33_3BDD3C3E45FF7210A0FA925F88A08251LLO
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 10Foundation12URLQueryItemV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 7Sharing19SFClientAccessLevelV10CapabilityO
+ _symbolic _____y_____G s23_ContiguousArrayStorageC s4Int8V
+ _symbolic _____y_____SgG 7Sharing12URLParameterV 10Foundation4DateV
+ _symbolic _____y_____SgG 7Sharing12URLParameterV AA15TapToRadarDraftV14ClassificationO
+ _symbolic _____y_____SgG 7Sharing12URLParameterV AA15TapToRadarDraftV15ReproducibilityO
+ _type_layout_string 7Sharing14SFAccessReportV
+ _type_layout_string 7Sharing15TapToRadarDraftV22RemoteDeviceSelectionsV
+ _type_layout_string 7Sharing15TapToRadarDraftV9ComponentV
+ _type_layout_string 7Sharing9URLSchemeV
+ _xpc_type_get_name
+ keypath_set.117Tm
- GCC_except_table126
- GCC_except_table133
- GCC_except_table137
- GCC_except_table153
- GCC_except_table155
- GCC_except_table192
- GCC_except_table197
- GCC_except_table198
- GCC_except_table205
- GCC_except_table206
- GCC_except_table48
- __59-[SFAutoUnlockManager enableAutoUnlockWithDevice:passcode:]_block_invoke
- ___59-[SFAutoUnlockManager enableAutoUnlockWithDevice:passcode:]_block_invoke
- ___59-[SFAutoUnlockManager enableAutoUnlockWithDevice:passcode:]_block_invoke_2
- ___59-[SFAutoUnlockManager enableAutoUnlockWithDevice:passcode:]_block_invoke_3
- ___63-[SFCollaborationPerformer _performWithAddParticipantsAllowed:]_block_invoke
- ___63-[SFCollaborationPerformer _performWithAddParticipantsAllowed:]_block_invoke_2
- ___unnamed_68
- __swift__destructor.431Tm
- __swift_closure_destructor.1319Tm
- __swift_closure_destructor.451Tm
- __swift_closure_destructor.472Tm
- __swift_closure_destructor.484Tm
- __swift_closure_destructor.558Tm
- __swift_closure_destructor.908Tm
- _objc_msgSend$enableAutoUnlockWithDevice:passcode:clientProxy:
- keypath_set.105Tm
CStrings:
+ " - pinPairingRequired "
+ "### Ignoring CLI mode / forced PIN from unauthenticated PreAuth on non-internal build\n"
+ "%@: cannot set allowsAccessRequests:%s, share options have not loaded"
+ "%@: cannot set isPublicCollaboration:%s, share options have not loaded"
+ "%{public}@ advertisement request for %{public}@ succeeded"
+ "%{public}@ dispatching advertisement request for %{public}@ failed (%@)"
+ "%{public}@ dispatching request to advertise %{public}@"
+ "%~@"
+ "(null)"
+ "-1"
+ "Access report store was already empty"
+ "AccessReports.plist"
+ "Add item not allowed, collaboration is public"
+ "AirDropTTRInactivityNudgeOptOut"
+ "Always"
+ "AudioAccessory11,1"
+ "B32@?0@\"_SWCollaborationOption\"8Q16^B24"
+ "B525"
+ "B525ish"
+ "CallbackIdentifier"
+ "Cleared the access report store"
+ "Collaboration Performer for item %@ resuming after options loaded"
+ "Collaboration Performer for item %@ resuming without options after loading finished"
+ "Collaboration Performer for item %@ waiting for options to load before performing"
+ "CollaborationContactHandles"
+ "CollaborationGroupChatID"
+ "ComponentVersion"
+ "Crash/Hang/Data Loss"
+ "Enhancement"
+ "ExtensionIdentifiers"
+ "Failed to clear the access report store {error: %@}"
+ "Failed to launch Tap-to-Radar"
+ "Failed to persist the access report store {error: %@}"
+ "Failed to read the access report store -- starting empty {error: %@}"
+ "Feature (New)"
+ "Handing off to Manage Share, not reporting a collaboration route"
+ "HomeAccessory"
+ "HomeKitPrimaryResident"
+ "I Didn't Try"
+ "IncludeDevicePrefixInTitle"
+ "Loaded the access report store {entitlements: %ld}"
+ "Mac17,5"
+ "MacBookNeo"
+ "MusicHandoffScan"
+ "No Sharing container -- this report will be filed again after a restart"
+ "No access report store yet -- starting empty"
+ "Not Applicable"
+ "Options group:%@ has no options left after removing anyone-with-link"
+ "Other Bug"
+ "Performance"
+ "Power"
+ "QUICHTTPPerf server is internal-only; refusing to start listener on a customer build"
+ "QUICHTTPPerf server is not available on this build"
+ "Rarely"
+ "RemoteAttachments"
+ "Removing anyone-with-link option from options group:%@"
+ "Report collaboration route: %{public}@"
+ "Security"
+ "Serious Bug"
+ "Sometimes"
+ "Tap-to-Radar isn't supported on this platform"
+ "Task"
+ "UI/Usability"
+ "Unable"
+ "Unable to construct URL from query items"
+ "Vision"
+ "WarpShockwaveEffectDuration_connectionHint"
+ "WarpShockwaveEffectDuration_shockwave"
+ "WarpShockwaveEffectTransitionSpeed"
+ "[%{public}@] Did send payload to %{public}@ for activity identifier %@. Handled: %{public}@"
+ "[%{public}@] Dispatching payload request to %{public}@ for %{public}@"
+ "[%{public}@] Found device %{public}@. Handled:%{public}@"
+ "[%{public}@] Lost device %{public}@. Handled:%{public}@"
+ "[%{public}@] Received advertisement %{public}@. Handled:%{public}@"
+ "[%{public}@] Received payload request from %{public}@ for %{public}@"
+ "[%{public}@] Received payload request from %{public}@ for %{public}@. Handled: %{public}@"
+ "all"
+ "allowRestrictedBoop"
+ "canShowShareOptions:no, the share options are read-only"
+ "com.apple.private.airdrop.client"
+ "com.apple.private.airdrop.internal"
+ "com.apple.private.airdrop.settings"
+ "com.apple.private.sharing.account-state"
+ "com.apple.private.sharing.continuity-streams"
+ "com.apple.private.sharing.hotspot"
+ "com.apple.sharing.collaborationRoute"
+ "continuityStreams"
+ "createSFNodeKindsFromXPCArray: expected an XPC array, got %{public}s"
+ "createSFNodeKindsFromXPCArray: skipping unknown kind %ld at array index %ld"
+ "full-log-archive"
+ "getSFNodeKindForIndex: index %ld out of range (count %ld)"
+ "iPhone18Pro"
+ "iPhoneDuo"
+ "itemType"
+ "kern.osversion"
+ "log-archive-only"
+ "outcome"
+ "privateLoggingEnabled"
+ "proximityHandoffInteractions"
+ "route"
+ "skips-local-sysdiagnose-only"
+ "sysdiagnose-only"
+ "waitMs"
+ "yyyy.MM.dd_HH-mm-ss"
- "%@ advertisement request for %@ succeeded"
- "%@ dispatching advertisement request for %@ failed (%@)"
- "%@ dispatching request to advertise %@"
- "Created UUID: %s from %ld"
- "Signature for %s: %ld"
- "V63"
- "V64"
- "[%@] Did send payload to %@ for activity identifier %@. Handled: %@"
- "[%@] Dispatching payload request to %@ for %@"
- "[%@] Found device %@. Handled:%@"
- "[%@] Lost device %@. Handled:%@"
- "[%@] Received advertisement %@. Handled:%@"
- "[%@] Received payload request from %@ for %@"
- "[%@] Received payload request from %@ for %@. Handled: %@"
```
