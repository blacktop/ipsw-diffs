## AuthKitUI

> `/System/Library/PrivateFrameworks/AuthKitUI.framework/AuthKitUI`

```diff

-560.125.6.0.0
-  __TEXT.__text: 0xe9da0
-  __TEXT.__objc_methlist: 0x8b7c
-  __TEXT.__const: 0x20d4
-  __TEXT.__gcc_except_tab: 0x11f8
-  __TEXT.__cstring: 0x592d
+560.250.3.0.0
+  __TEXT.__text: 0xf78bc
+  __TEXT.__objc_methlist: 0x8dbc
+  __TEXT.__const: 0x27a4
+  __TEXT.__gcc_except_tab: 0x123c
+  __TEXT.__cstring: 0x5b5d
   __TEXT.__dlopen_cstrs: 0x179
-  __TEXT.__oslogstring: 0x5d29
+  __TEXT.__oslogstring: 0x6029
   __TEXT.__ustring: 0x2c
-  __TEXT.__swift5_typeref: 0x13c6
-  __TEXT.__constg_swiftt: 0x7ac
-  __TEXT.__swift5_reflstr: 0x2ea
-  __TEXT.__swift5_assocty: 0x288
-  __TEXT.__swift5_fieldmd: 0x4d8
-  __TEXT.__swift5_builtin: 0x8c
-  __TEXT.__swift5_protos: 0x1c
-  __TEXT.__swift5_proto: 0x150
-  __TEXT.__swift5_types: 0x88
-  __TEXT.__swift5_capture: 0x29c
-  __TEXT.__swift_as_entry: 0x68
-  __TEXT.__swift_as_ret: 0x68
-  __TEXT.__swift_as_cont: 0xd4
-  __TEXT.__unwind_info: 0x3c50
-  __TEXT.__eh_frame: 0x1398
+  __TEXT.__constg_swiftt: 0x98c
+  __TEXT.__swift5_typeref: 0x1686
+  __TEXT.__swift5_reflstr: 0x54a
+  __TEXT.__swift5_fieldmd: 0x6cc
+  __TEXT.__swift5_builtin: 0xb4
+  __TEXT.__swift5_assocty: 0x330
+  __TEXT.__swift5_capture: 0x3a8
+  __TEXT.__swift5_proto: 0x198
+  __TEXT.__swift5_types: 0xb0
+  __TEXT.__swift5_protos: 0x20
+  __TEXT.__swift_as_entry: 0x6c
+  __TEXT.__swift_as_ret: 0x78
+  __TEXT.__swift_as_cont: 0xc8
+  __TEXT.__unwind_info: 0x4078
+  __TEXT.__eh_frame: 0x15c8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3078
-  __DATA_CONST.__objc_classlist: 0x418
+  __DATA_CONST.__const: 0x30e0
+  __DATA_CONST.__objc_classlist: 0x428
   __DATA_CONST.__objc_catlist: 0x60
-  __DATA_CONST.__objc_protolist: 0x2a8
+  __DATA_CONST.__objc_protolist: 0x2b8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6178
-  __DATA_CONST.__objc_protorefs: 0x70
-  __DATA_CONST.__objc_superrefs: 0x2c8
+  __DATA_CONST.__objc_selrefs: 0x63b8
+  __DATA_CONST.__objc_protorefs: 0x78
+  __DATA_CONST.__objc_superrefs: 0x2d0
   __DATA_CONST.__objc_arraydata: 0x2b8
-  __DATA_CONST.__got: 0xf68
-  __AUTH_CONST.__const: 0x10b0
-  __AUTH_CONST.__cfstring: 0x51a0
-  __AUTH_CONST.__objc_const: 0x1a150
+  __DATA_CONST.__got: 0x1088
+  __AUTH_CONST.__const: 0x15f0
+  __AUTH_CONST.__cfstring: 0x5280
+  __AUTH_CONST.__objc_const: 0x1a800
+  __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH_CONST.__objc_intobj: 0x2a0
   __AUTH_CONST.__objc_arrayobj: 0x90
-  __AUTH_CONST.__auth_got: 0xee8
-  __AUTH.__objc_data: 0x25b0
-  __AUTH.__data: 0x5b0
-  __DATA.__objc_ivar: 0x774
-  __DATA.__data: 0x24d0
+  __AUTH_CONST.__auth_got: 0xfd8
+  __AUTH.__objc_data: 0x2750
+  __AUTH.__data: 0x690
+  __DATA.__objc_ivar: 0x7ac
+  __DATA.__data: 0x2708
   __DATA.__common: 0x70
   __DATA_DIRTY.__objc_data: 0x438
   __DATA_DIRTY.__data: 0x28

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3798
-  Symbols:   6035
-  CStrings:  1339
+  Functions: 4108
+  Symbols:   6195
+  CStrings:  1363
 
Symbols:
+ +[AKDTOBiometryHook new]
+ -[AKApprovalFlowRemoteUICoordinator _requestTapToRadarForPage:objectModel:]
+ -[AKApprovalFlowRemoteUICoordinator _tapToRadarButtonForPage:objectModel:]
+ -[AKApprovalFlowRemoteUICoordinator _updateStateWithFinalResponse:error:completion:]
+ -[AKApprovalFlowRemoteUICoordinator analyticsReporter]
+ -[AKApprovalFlowRemoteUICoordinator approvalCodeType]
+ -[AKApprovalFlowRemoteUICoordinator approvalCode]
+ -[AKApprovalFlowRemoteUICoordinator didLoadURL:error:]
+ -[AKApprovalFlowRemoteUICoordinator initWithAnalyticsReporter:eventHandler:authenticationController:accountManager:device:tapToRadarWrapper:]
+ -[AKApprovalFlowRemoteUICoordinator init]
+ -[AKApprovalFlowRemoteUICoordinator odiAssessmentSender]
+ -[AKApprovalFlowRemoteUICoordinator processedElementWithError:forElement:]
+ -[AKApprovalFlowRemoteUICoordinator remoteUIController:willPresentObjectModel:modally:]
+ -[AKApprovalFlowRemoteUICoordinator setApprovalCode:]
+ -[AKApprovalFlowRemoteUICoordinator setApprovalCodeType:]
+ -[AKApprovalFlowRemoteUICoordinator setOdiAssessmentSender:]
+ -[AKApprovalFlowRemoteUICoordinator setTelemetryFlowID:]
+ -[AKApprovalFlowRemoteUICoordinator telemetryFlowID]
+ -[AKApprovalFlowRemoteUICoordinator willActivateElement:]
+ -[AKApprovalFlowRemoteUICoordinator willDisplayUI:]
+ -[AKApprovalFlowRemoteUICoordinator willLoadURL:]
+ -[AKApprovalFlowRemoteUICoordinator willProcessHook:]
+ -[AKAuthorizationNavigationController _sizesFormSheetFromPane]
+ -[AKAuthorizationNavigationController preferredContentSize]
+ -[AKAuthorizationSubPaneConfirmButton _passcodePolicy]
+ -[AKBasicLoginViewController _setCredentialFieldsEnabled:]
+ -[AKBasicLoginViewController restoreFirstResponder]
+ -[AKDTOBiometryHook _report:]
+ -[AKDTOBiometryHook initWithTelemetryFlowID:analyticsReporter:]
+ -[AKDTOBiometryHook init]
+ _AKApprovalCodeHeaderFieldForCodeType
+ _AKAuthenticationSMSCodeHeaderField
+ _AKBiometryAllowedTimeSinceDeviceUnlockKey
+ _AKRiskingSignalActiveCallTypeKey
+ _AKRiskingSignalCallerContactRecencyKey
+ _AKRiskingSignalsDirectiveKey
+ _AKSecrecyFeatureServerDrivenApprovalFlowSMS
+ _AKTTRComponentID
+ _AKTTRComponentName
+ _AKTTRComponentVersion
+ _AKTemporaryCollectRiskingSignalsHeaderKey
+ _AKTemporaryRiskingSignalsHeaderKey
+ _OBJC_CLASS_$_AAFAnalyticsReporter
+ _OBJC_CLASS_$_AAFTapToRadarHelper
+ _OBJC_CLASS_$_AAFTapToRadarRequest
+ _OBJC_CLASS_$_AKODIAssessmentHook
+ _OBJC_CLASS_$_AKTapToRadarWrapper
+ _OBJC_CLASS_$_OS_dispatch_queue
+ _OBJC_CLASS_$_RUIBarButtonItem
+ _OBJC_CLASS_$_TUCall
+ _OBJC_CLASS_$_TUCallCenter
+ _OBJC_IVAR_$_AKApprovalFlowRemoteUICoordinator._accountManager
+ _OBJC_IVAR_$_AKApprovalFlowRemoteUICoordinator._analyticsReporter
+ _OBJC_IVAR_$_AKApprovalFlowRemoteUICoordinator._approvalCode
+ _OBJC_IVAR_$_AKApprovalFlowRemoteUICoordinator._approvalCodeType
+ _OBJC_IVAR_$_AKApprovalFlowRemoteUICoordinator._authenticationController
+ _OBJC_IVAR_$_AKApprovalFlowRemoteUICoordinator._device
+ _OBJC_IVAR_$_AKApprovalFlowRemoteUICoordinator._eventHandler
+ _OBJC_IVAR_$_AKApprovalFlowRemoteUICoordinator._odiAssessmentSender
+ _OBJC_IVAR_$_AKApprovalFlowRemoteUICoordinator._riskingSignalsHook
+ _OBJC_IVAR_$_AKApprovalFlowRemoteUICoordinator._tapToRadarButtons
+ _OBJC_IVAR_$_AKApprovalFlowRemoteUICoordinator._tapToRadarWrapper
+ _OBJC_IVAR_$_AKApprovalFlowRemoteUICoordinator._telemetryFlowID
+ _OBJC_IVAR_$_AKDTOBiometryHook._analyticsReporter
+ _OBJC_IVAR_$_AKDTOBiometryHook._telemetryFlowID
+ _OBJC_METACLASS_$_AKODIAssessmentHook
+ _OBJC_METACLASS_$_AKTapToRadarWrapper
+ __DATA_AKODIAssessmentHook
+ __DATA_AKTapToRadarWrapper
+ __INSTANCE_METHODS_AKODIAssessmentHook
+ __INSTANCE_METHODS_AKTapToRadarWrapper
+ __IVARS_AKODIAssessmentHook
+ __METACLASS_DATA_AKODIAssessmentHook
+ __METACLASS_DATA_AKTapToRadarWrapper
+ __OBJC_$_CLASS_METHODS_AKDTOBiometryHook
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AKODIAssessmentSending
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AKTapToRadarWrapping
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AKODIAssessmentSending
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AKTapToRadarWrapping
+ __OBJC_$_PROTOCOL_REFS_AKODIAssessmentSending
+ __OBJC_$_PROTOCOL_REFS_AKTapToRadarWrapping
+ __OBJC_LABEL_PROTOCOL_$_AKODIAssessmentSending
+ __OBJC_LABEL_PROTOCOL_$_AKTapToRadarWrapping
+ __OBJC_PROTOCOL_$_AKODIAssessmentSending
+ __OBJC_PROTOCOL_$_AKTapToRadarWrapping
+ __PROPERTIES_AKODIAssessmentHook
+ __PROTOCOLS_AKODIAssessmentHook
+ __PROTOCOLS_AKTapToRadarWrapper
+ ___74-[AKApprovalFlowRemoteUICoordinator _tapToRadarButtonForPage:objectModel:]_block_invoke
+ ___84-[AKApprovalFlowRemoteUICoordinator _updateStateWithFinalResponse:error:completion:]_block_invoke
+ ___84-[AKApprovalFlowRemoteUICoordinator _updateStateWithFinalResponse:error:completion:]_block_invoke_2
+ ___89-[AKApprovalFlowRemoteUICoordinator handleShouldLoadRequest:redirectResponse:completion:]_block_invoke
+ ___block_descriptor_48_e8_32bs40w_e42_v32?0"NSHTTPURLResponse"816"NSError"24lw40l8s32l8
+ ___block_descriptor_56_e8_32w40w48w_e5_v8?0lw32l8w40l8w48l8
+ ___swift_closure_destructor.19Tm
+ ___swift_memcpy24_8
+ ___swift_memcpy4_4
+ __swiftEmptySetSingleton
+ __swift_implicitisolationactor_to_executor_cast
+ _associated conformance 9AuthKitUI14ActiveCallTypeOSHAASQ
+ _associated conformance 9AuthKitUI14ActiveCallTypeOSLAASQ
+ _associated conformance 9AuthKitUI20SignInDisclosureViewV05SwiftC00G0AA4BodyAdEP_AdE
+ _associated conformance 9AuthKitUI20SignInDisclosureViewV06RemoteC007ElementG0AA05SwiftC00G0
+ _associated conformance 9AuthKitUI20SignInDisclosureViewV06RemoteC007ElementG0AASe
+ _associated conformance 9AuthKitUI20SignInDisclosureViewV06RemoteC007ElementG0AAs12Identifiable
+ _associated conformance 9AuthKitUI20SignInDisclosureViewV10CodingKeys33_87D323745B29C4E34883A8B65EA3BEE8LLOSHAASQ
+ _associated conformance 9AuthKitUI20SignInDisclosureViewV10CodingKeys33_87D323745B29C4E34883A8B65EA3BEE8LLOs0H3KeyAAs23CustomStringConvertible
+ _associated conformance 9AuthKitUI20SignInDisclosureViewV10CodingKeys33_87D323745B29C4E34883A8B65EA3BEE8LLOs0H3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 9AuthKitUI20SignInDisclosureViewVs12IdentifiableAA2IDsADP_SH
+ _associated conformance So12TUCallStatusVSHSCSQ
+ _flat unique So22AKODIAssessmentSending_p
+ _get_witness_table qd__7SwiftUI4ViewHD2_AaBPAAE4task4name8priority4file4line_QrSSSg_ScPSSSiyyYaYAcntFQOyAA15ModifiedContentVyAA6VStackVyAA012_ConditionalJ0VyAKyAKyAKyAA4TextVAA30_EnvironmentKeyWritingModifierVyAA0M9AlignmentOGGAA16_FixedSizeLayoutVGAA010_FlexFrameU0VGAA05EmptyC0VGGA0_G_Qo_HO
+ _get_witness_table qd__7SwiftUI4ViewHD2_AaBPAAE4task4name8priority4file4line_QrSSSg_ScPSSSiyyYaYAcntFQOyAA15ModifiedContentVyAC013AAAFoundationB0E19invisibleInkOverlay14coveragePolicy17onCoverageChangedQrAL09InvisiblemrP0O_ySbcSgtFQOyAKyAKyAKyAKyAA4TextVAA16_FlexFrameLayoutVGAA14_OpacityEffectVGAA08_PaddingX0VGAA19_BackgroundModifierVyAA06_ShapeC0VyAA16RoundedRectangleVAA5ColorVGGG_Qo_AA05_ClipZ0VyA7_GG_Qo_HO
+ _kAAFDeviceSessionIdString
+ _kAAFDidSucceed
+ _kAKAnalyticsEventCallSignalsRequested
+ _kAKAnalyticsEventCodeDisplayedWithInvisibleInk
+ _kAKAnalyticsEventInvisibleInkRemovedFromCode
+ _kAKAnalyticsEventLocalAuthentication
+ _kAKAnalyticsEventSignInDisclosure
+ _kAKRTCEventCategoryAccountDataAccessRecovery
+ _kAKRUIHookNameAttributeKey
+ _kAKRemoteUIDomainPrefix
+ _kApprovalFlowSMSRemoteUITag
+ _kApprovalFlowSignInDisclosureViewRemoteUITag
+ _swift_arrayInitWithCopy
+ _swift_isUniquelyReferenced_nonNull_bridgeObject
+ _swift_release_n
+ _swift_release_x26
+ _swift_release_x3
+ _swift_retain_x25
+ _swift_retain_x26
+ _swift_retain_x27
+ _swift_retain_x28
+ _symbolic $s9AuthKitUI31ApprovalFlowCodeRequestDelegateP
+ _symbolic Ieg_
+ _symbolic IeyB_
+ _symbolic SS_Sit
+ _symbolic SaySo6TUCallCG
+ _symbolic Say_____G 8Dispatch0A13WorkItemFlagsV
+ _symbolic Say_____G 9AuthKitUI18ActiveCallSnapshotV
+ _symbolic Say_____G So17OS_dispatch_queueC8DispatchE10AttributesV
+ _symbolic SayypG
+ _symbolic ScCySay_____G_____G 9AuthKitUI18ActiveCallSnapshotV s5NeverO
+ _symbolic ScCy__________G 9AuthKitUI20CallerContactRecencyO s5NeverO
+ _symbolic SccySDy_____ypGSg______pG s11AnyHashableV s5ErrorP
+ _symbolic ShySSG
+ _symbolic So12TUCallCenterC
+ _symbolic So19NSMutableURLRequestC
+ _symbolic So20AAFAnalyticsReporterC
+ _symbolic _____ 7SwiftUI13TextAlignmentO
+ _symbolic _____ 9AuthKitUI021ApprovalFlowTelemetryE5IDKeyV
+ _symbolic _____ 9AuthKitUI14ActiveCallTypeO
+ _symbolic _____ 9AuthKitUI17ODIAssessmentHookC
+ _symbolic _____ 9AuthKitUI17TapToRadarWrapperC
+ _symbolic _____ 9AuthKitUI18ActiveCallSnapshotV
+ _symbolic _____ 9AuthKitUI20AnalyticsReporterKeyV
+ _symbolic _____ 9AuthKitUI20SignInDisclosureViewV
+ _symbolic _____ 9AuthKitUI20SignInDisclosureViewV10CodingKeys33_87D323745B29C4E34883A8B65EA3BEE8LLO
+ _symbolic _____ 9AuthKitUI25LocalAuthenticationPromptV
+ _symbolic _____ 9AuthKitUI26ActiveCallReaderFactoryKeyV
+ _symbolic _____ So12TUCallStatusV
+ _symbolic _____ So16os_unfair_lock_sV
+ _symbolic _____ s5Int32V
+ _symbolic _____ s6UInt32V
+ _symbolic _____XDXMT 9AuthKitUI25TelephonyUtilitiesWrapperC
+ _symbolic ______p 9AuthKitUI31ApprovalFlowCodeRequestDelegateP
+ _symbolic ______p So22AKODIAssessmentSendingP
+ _symbolic ______pSg 9AuthKitUI31ApprovalFlowCodeRequestDelegateP
+ _symbolic ______pyYbc 9AuthKitUI33TelephonyUtilitiesWrapperProtocolP
+ _symbolic _____yAAyAAyAAy__________G_____G_____G_____y_____y__________GGG 7SwiftUI15ModifiedContentV AA4TextV AA16_FlexFrameLayoutV AA14_OpacityEffectV AA08_PaddingH0V AA19_BackgroundModifierV AA10_ShapeViewV AA16RoundedRectangleV AA5ColorV
+ _symbolic _____yAAyAAy__________G_____G_____G 7SwiftUI15ModifiedContentV AA4TextV AA16_FlexFrameLayoutV AA14_OpacityEffectV AA08_PaddingH0V
+ _symbolic _____yAAy__________y_____GG_____G 7SwiftUI15ModifiedContentV AA4TextV AA30_EnvironmentKeyWritingModifierV AA0E9AlignmentO AA16_FixedSizeLayoutV
+ _symbolic _____yAAy_____yAAyAAyAAyAAy__________G_____G_____G_____y_____y__________GGG_Qo______yAKGG_____G 7SwiftUI15ModifiedContentV AA4ViewP013AAAFoundationB0E19invisibleInkOverlay14coveragePolicy17onCoverageChangedQrAF09InvisiblehmK0O_ySbcSgtFQO AA4TextV AA16_FlexFrameLayoutV AA14_OpacityEffectV AA08_PaddingS0V AA19_BackgroundModifierV AA06_ShapeE0V AA16RoundedRectangleV AA5ColorV AA05_ClipU0V AA14_TaskModifier2V
+ _symbolic _____yAAy_____y_____yAAyAAyAAy__________y_____GG_____G_____G_____GGAKG_____G 7SwiftUI15ModifiedContentV AA6VStackV AA012_ConditionalD0V AA4TextV AA30_EnvironmentKeyWritingModifierV AA0G9AlignmentO AA16_FixedSizeLayoutV AA010_FlexFrameO0V AA9EmptyViewV AA14_TaskModifier2V
+ _symbolic _____ySSG s11_SetStorageC
+ _symbolic _____ySSSgG 15AAAFoundationUI16AAFTestableStateV
+ _symbolic _____ySS_SitG s23_ContiguousArrayStorageC
+ _symbolic _____yShySSGG 2os21OSAllocatedUnfairLockV
+ _symbolic _____yShySSG_____G s13ManagedBufferCsRi__rlE So16os_unfair_lock_sV
+ _symbolic _____y_____G 7SwiftUI11_ClipEffectV AA16RoundedRectangleV
+ _symbolic _____y_____G s11_SetStorageC So12TUCallStatusV
+ _symbolic _____y_____G s22KeyedDecodingContainerV 9AuthKitUI20SignInDisclosureViewV10CodingKeys33_87D323745B29C4E34883A8B65EA3BEE8LLO
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 9AuthKitUI18ActiveCallSnapshotV
+ _symbolic _____y_____yAAyAAyAAyAAy__________G_____G_____G_____y_____y__________GGG_Qo______yAKGG 7SwiftUI15ModifiedContentV AA4ViewP013AAAFoundationB0E19invisibleInkOverlay14coveragePolicy17onCoverageChangedQrAF09InvisiblehmK0O_ySbcSgtFQO AA4TextV AA16_FlexFrameLayoutV AA14_OpacityEffectV AA08_PaddingS0V AA19_BackgroundModifierV AA06_ShapeE0V AA16RoundedRectangleV AA5ColorV AA05_ClipU0V
+ _symbolic _____y_____y_____yAAyAAyAAyAAy__________G_____G_____G_____y_____y__________GGG_Qo______yAKGG_Qo_ 7SwiftUI4ViewPAAE4task4name8priority4file4line_QrSSSg_ScPSSSiyyYaYAcntFQO AA15ModifiedContentV AC013AAAFoundationB0E19invisibleInkOverlay14coveragePolicy17onCoverageChangedQrAL09InvisiblemrP0O_ySbcSgtFQO AA4TextV AA16_FlexFrameLayoutV AA14_OpacityEffectV AA08_PaddingX0V AA19_BackgroundModifierV AA06_ShapeC0V AA16RoundedRectangleV AA5ColorV AA05_ClipZ0V
+ _symbolic _____y_____y_____yAAyAAyAAy__________y_____GG_____G_____G_____GGAKG 7SwiftUI15ModifiedContentV AA6VStackV AA012_ConditionalD0V AA4TextV AA30_EnvironmentKeyWritingModifierV AA0G9AlignmentO AA16_FixedSizeLayoutV AA010_FlexFrameO0V AA9EmptyViewV
+ _symbolic _____y_____y_____yACyACy__________y_____GG_____G_____G_____GG 7SwiftUI6VStackV AA19_ConditionalContentV AA08ModifiedE0V AA4TextV AA30_EnvironmentKeyWritingModifierV AA0G9AlignmentO AA16_FixedSizeLayoutV AA010_FlexFrameO0V AA9EmptyViewV
+ _symbolic _____y_____y_____y_____yAAyAAyAAy__________y_____GG_____G_____G_____GGAKG_Qo_ 7SwiftUI4ViewPAAE4task4name8priority4file4line_QrSSSg_ScPSSSiyyYaYAcntFQO AA15ModifiedContentV AA6VStackV AA012_ConditionalJ0V AA4TextV AA30_EnvironmentKeyWritingModifierV AA0M9AlignmentO AA16_FixedSizeLayoutV AA010_FlexFrameU0V AA05EmptyC0V
+ _type_layout_string 9AuthKitUI18ActiveCallSnapshotV
+ _type_layout_string So16os_unfair_lock_sV
- -[AKAuthorizationSubPaneConfirmButton _checkIfPasscodeFallbackAllowedWithCompletion:]
- -[AKBasicLoginViewController viewDidLayoutSubviews]
- -[AKBasicLoginViewController viewDidLoad]
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_AKApprovalFlowCodeRequestDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_AKApprovalFlowCodeRequestDelegate
- __OBJC_$_PROTOCOL_REFS_AKApprovalFlowCodeRequestDelegate
- __OBJC_LABEL_PROTOCOL_$_AKApprovalFlowCodeRequestDelegate
- __OBJC_PROTOCOL_$_AKApprovalFlowCodeRequestDelegate
- ___85-[AKAuthorizationSubPaneConfirmButton _checkIfPasscodeFallbackAllowedWithCompletion:]_block_invoke
- ___87-[AKAuthorizationSubPaneConfirmButton _handleBiometricAuthFailureWithError:forContext:]_block_invoke
- ___block_descriptor_40_e8_32bs_e23_v32?0816"NSError"24ls32l8
- _associated conformance 9AuthKitUI20AKCodeDisplayElementV12LoadingStateOSHAASQ
- _flat unique So33AKApprovalFlowCodeRequestDelegate_p
- _get_witness_table qd__7SwiftUI4ViewHD2_AaBPAAE4task4name8priority4file4line_QrSSSg_ScPSSSiyyYaYAcntFQOyAA15ModifiedContentVyAKyAKyAKyAKyAKyAA4TextVAA16_FlexFrameLayoutVGAA14_OpacityEffectVGAA16_OverlayModifierVyAA08ProgressC0VyAA05EmptyC0VAYGSgGGAA08_PaddingN0VGA3_GAA011_BackgroundR0VyAA06_ShapeC0VyAA16RoundedRectangleVAA5ColorVGGG_Qo_HO
- _swift_asyncLet_begin
- _swift_asyncLet_finish
- _swift_asyncLet_get_throwing
- _symbolic SccySS______pG s5ErrorP
- _symbolic _____ 9AuthKitUI20AKCodeDisplayElementV12LoadingStateO
- _symbolic ______p So33AKApprovalFlowCodeRequestDelegateP
- _symbolic ______pSg So33AKApprovalFlowCodeRequestDelegateP
- _symbolic _____yAAyAAyAAyAAyAAyAAy__________G_____G_____y_____y_____AIGSgGG_____GANG_____y_____y__________GGG_____G 7SwiftUI15ModifiedContentV AA4TextV AA16_FlexFrameLayoutV AA14_OpacityEffectV AA16_OverlayModifierV AA12ProgressViewV AA05EmptyN0V AA08_PaddingH0V AA011_BackgroundL0V AA06_ShapeN0V AA16RoundedRectangleV AA5ColorV AA14_TaskModifier2V
- _symbolic _____yAAyAAyAAyAAyAAy__________G_____G_____y_____y_____AIGSgGG_____GANG_____y_____y__________GGG 7SwiftUI15ModifiedContentV AA4TextV AA16_FlexFrameLayoutV AA14_OpacityEffectV AA16_OverlayModifierV AA12ProgressViewV AA05EmptyN0V AA08_PaddingH0V AA011_BackgroundL0V AA06_ShapeN0V AA16RoundedRectangleV AA5ColorV
- _symbolic _____yAAyAAyAAyAAy__________G_____G_____y_____y_____AIGSgGG_____GANG 7SwiftUI15ModifiedContentV AA4TextV AA16_FlexFrameLayoutV AA14_OpacityEffectV AA16_OverlayModifierV AA12ProgressViewV AA05EmptyN0V AA08_PaddingH0V
- _symbolic _____yAAyAAyAAy__________G_____G_____y_____y_____AIGSgGG_____G 7SwiftUI15ModifiedContentV AA4TextV AA16_FlexFrameLayoutV AA14_OpacityEffectV AA16_OverlayModifierV AA12ProgressViewV AA05EmptyN0V AA08_PaddingH0V
- _symbolic _____yAAyAAy__________G_____G_____y_____y_____AIGSgGG 7SwiftUI15ModifiedContentV AA4TextV AA16_FlexFrameLayoutV AA14_OpacityEffectV AA16_OverlayModifierV AA12ProgressViewV AA05EmptyN0V
- _symbolic _____ySSG 15AAAFoundationUI16AAFTestableStateV
- _symbolic _____y_____ABG 7SwiftUI12ProgressViewV AA05EmptyD0V
- _symbolic _____y_____G 15AAAFoundationUI16AAFTestableStateV 07AuthKitB020AKCodeDisplayElementV07LoadingD0O
- _symbolic _____y_____yAAyAAyAAyAAyAAy__________G_____G_____y_____y_____AIGSgGG_____GANG_____y_____y__________GGG_Qo_ 7SwiftUI4ViewPAAE4task4name8priority4file4line_QrSSSg_ScPSSSiyyYaYAcntFQO AA15ModifiedContentV AA4TextV AA16_FlexFrameLayoutV AA14_OpacityEffectV AA16_OverlayModifierV AA08ProgressC0V AA05EmptyC0V AA08_PaddingN0V AA011_BackgroundR0V AA06_ShapeC0V AA16RoundedRectangleV AA5ColorV
- _symbolic _____y_____y_____ACGSgG 7SwiftUI16_OverlayModifierV AA12ProgressViewV AA05EmptyF0V
CStrings:
+ "AKBasicLoginViewController - Entering busy state"
+ "AKBasicLoginViewController - Leaving busy state"
+ "AKBasicLoginViewController - Restoring first responder - %@ field became first responder: %@"
+ "AKBasicLoginViewController - Sign in pressed - keyboard dismissed: %@, submitting to password handler: %@"
+ "AKBasicLoginViewController - Sign in pressed with no submit path - staying idle"
+ "AKCodeDisplayElement: Drawing a code (length=%ld)"
+ "AKCodeDisplayElement: No delegate to ask for a sign in approval flow code"
+ "AKCodeDisplayElement: Registering for codes of type=%s"
+ "Account Breach Prevention: Issue During Approval Flow"
+ "ApprovalFlowRemoteUICoordinator: Final response is not actionable, skipping the state update"
+ "ApprovalFlowRemoteUICoordinator: No final response to hand to akd"
+ "AuthKitUI.LocalAuthenticationHook"
+ "AuthKitUI.ODIAssessmentHook"
+ "AuthKitUI.RiskingSignalsHook"
+ "Decoded tag '%s' as sms"
+ "Feedback from the sign-in approval flow.\n\nPage: %@\nSource: %@\n\nWhat happened:\n"
+ "No server-provided UI left to dismiss. Skipping, so the dismiss cannot forward to the host's own presentation."
+ "ODIAssessmentHook is asking akd to send the ODI assessment"
+ "RiskingSignalsHook attaching %{public}ld signal(s) to the postback"
+ "RiskingSignalsHook ignored %{public}ld unrecognized signal name(s)"
+ "RiskingSignalsHook stamping %{public}ld signal(s) on the request"
+ "SignInDisclosureView: call state read failed: domain=%{public}s code=%{public}ld"
+ "TelephonyUtilitiesWrapper read %{public}ld live call(s) from %{public}ld local and %{public}ld elsewhere"
+ "Unknown"
+ "Untitled page"
+ "View.task @ AuthKitUI/SignInDisclosureView.swift:"
+ "activeCallText"
+ "com.apple.AuthKit.RiskSignalCollector.recency"
+ "com.apple.AuthKit.TelephonyUtilitiesWrapper"
+ "defaultText"
+ "fetchActiveCalls()"
+ "lookback"
+ "readRecency(for:)"
+ "v32@?0@\"NSHTTPURLResponse\"8@16@\"NSError\"24"
- "AKCodeDisplayElement: Code fetch failed with error: %s"
- "AKCodeDisplayElement: Code successfully fetched and loaded (length=%ld)"
- "AKCodeDisplayElement: No delegate found - cannot fetch code"
- "AKCodeDisplayElement: Showing spinner after delay"
- "AKCodeDisplayElement: Spinner delay task cancelled or failed: %s"
- "AKCodeDisplayElement: Starting code fetch from delegate for type=%s"
- "AKCodeDisplayElement: Task was cancelled after code fetch"
- "AKCodeDisplayElement: Task was cancelled during code fetch"
- "Location based device policy preflight passcode validation returned with error %@"
- "v32@?0@8@16@\"NSError\"24"
```
