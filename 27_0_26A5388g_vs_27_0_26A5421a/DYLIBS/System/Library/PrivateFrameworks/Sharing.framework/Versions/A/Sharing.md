## Sharing

> `/System/Library/PrivateFrameworks/Sharing.framework/Versions/A/Sharing`

```diff

-2126.10.4.0.0
-  __TEXT.__text: 0x337c00
-  __TEXT.__objc_methlist: 0x12b04
-  __TEXT.__cstring: 0x2c6b8
-  __TEXT.__const: 0x2057c
-  __TEXT.__gcc_except_tab: 0x340c
-  __TEXT.__oslogstring: 0xc6d3
+2130.10.2.1.5
+  __TEXT.__text: 0x33e594
+  __TEXT.__objc_methlist: 0x12c14
+  __TEXT.__cstring: 0x2c7c8
+  __TEXT.__const: 0x20f9c
+  __TEXT.__gcc_except_tab: 0x353c
+  __TEXT.__oslogstring: 0xc983
   __TEXT.__dlopen_cstrs: 0x5f2
   __TEXT.__ustring: 0x18
-  __TEXT.__swift5_typeref: 0x8497
-  __TEXT.__constg_swiftt: 0x6d88
-  __TEXT.__swift5_reflstr: 0x3b0a
-  __TEXT.__swift5_fieldmd: 0x69a8
-  __TEXT.__swift5_builtin: 0x1cc
-  __TEXT.__swift5_assocty: 0xf50
-  __TEXT.__swift5_capture: 0x287c
+  __TEXT.__swift5_typeref: 0x864f
+  __TEXT.__constg_swiftt: 0x6f4c
+  __TEXT.__swift5_reflstr: 0x3bda
+  __TEXT.__swift5_fieldmd: 0x6b88
+  __TEXT.__swift5_builtin: 0x1e0
+  __TEXT.__swift5_assocty: 0xfa0
+  __TEXT.__swift5_capture: 0x28f4
   __TEXT.__swift5_protos: 0x24
-  __TEXT.__swift5_proto: 0x1b38
-  __TEXT.__swift5_types: 0x8e0
-  __TEXT.__swift_as_entry: 0x3f4
-  __TEXT.__swift_as_ret: 0x3f4
-  __TEXT.__swift_as_cont: 0xa30
-  __TEXT.__swift5_mpenum: 0xa8
-  __TEXT.__unwind_info: 0xd208
-  __TEXT.__eh_frame: 0xe544
+  __TEXT.__swift5_proto: 0x1bdc
+  __TEXT.__swift5_types: 0x910
+  __TEXT.__swift_as_entry: 0x3fc
+  __TEXT.__swift_as_ret: 0x3fc
+  __TEXT.__swift_as_cont: 0xa50
+  __TEXT.__swift5_mpenum: 0xb8
+  __TEXT.__unwind_info: 0xd448
+  __TEXT.__eh_frame: 0xe82c
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x2d20
-  __DATA_CONST.__objc_classlist: 0x848
+  __DATA_CONST.__objc_classlist: 0x858
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x360
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8648
+  __DATA_CONST.__objc_selrefs: 0x8688
   __DATA_CONST.__objc_protorefs: 0x1d8
   __DATA_CONST.__objc_classrefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x508
   __DATA_CONST.__objc_arraydata: 0x2f0
-  __DATA_CONST.__got: 0x1260
-  __AUTH_CONST.__const: 0x1ae88
-  __AUTH_CONST.__cfstring: 0x11520
-  __AUTH_CONST.__objc_const: 0x34ec0
+  __DATA_CONST.__got: 0x1270
+  __AUTH_CONST.__const: 0x1b5d8
+  __AUTH_CONST.__cfstring: 0x115e0
+  __AUTH_CONST.__objc_const: 0x350d0
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x498
   __AUTH_CONST.__objc_dictobj: 0x398
   __AUTH_CONST.__objc_arrayobj: 0xa8
-  __AUTH_CONST.__auth_got: 0x28d8
-  __AUTH.__objc_data: 0x5ce0
-  __AUTH.__data: 0x3a30
-  __DATA.__objc_ivar: 0x1fb8
-  __DATA.__data: 0xb650
-  __DATA.__bss: 0x36d90
+  __AUTH_CONST.__auth_got: 0x28e0
+  __AUTH.__objc_data: 0x5e08
+  __AUTH.__data: 0x3b10
+  __DATA.__objc_ivar: 0x1fc0
+  __DATA.__data: 0xb7a0
+  __DATA.__bss: 0x38210
   __DATA.__common: 0x160
   __DATA_DIRTY.__objc_data: 0x1120
   __DATA_DIRTY.__data: 0x540

   - /System/Library/Frameworks/IOBluetooth.framework/Versions/A/IOBluetooth
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/ImageIO.framework/Versions/A/ImageIO
+  - /System/Library/Frameworks/LocalAuthentication.framework/Versions/A/LocalAuthentication
   - /System/Library/Frameworks/Network.framework/Versions/A/Network
   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /System/Library/Frameworks/SystemConfiguration.framework/Versions/A/SystemConfiguration

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 21097
-  Symbols:   20987
-  CStrings:  7363
+  Functions: 21295
+  Symbols:   21097
+  CStrings:  7383
 
Symbols:
+ +[SFAllowAccessTapEvent eventName]
+ +[SFCollaborationUtilities addItemAllowedForCollaborationItem:completionHandler:]
+ +[SFCollaborationUtilities fetchExistingShareForFileOrFolderURL:completionHandler:]
+ -[SFAllowAccessTapEvent .cxx_destruct]
+ -[SFAllowAccessTapEvent eventPayload]
+ -[SFAllowAccessTapEvent hostAppBundleID]
+ -[SFAllowAccessTapEvent setHostAppBundleID:]
+ -[SFAllowAccessTapEvent submitEvent]
+ -[SFAuthenticationManager _enableForType:withIDSDeviceID:passcodeRef:sessionID:]
+ -[SFAuthenticationManager _releasePairingContextForSessionID:]
+ -[SFAuthenticationManager pairingLAContexts]
+ -[SFCollaborationPerformer _isCurrentUserCoOwnerOfShare:]
+ -[SFShareSheetService fetchExistingShareForFileOrFolderURL:completionHandler:]
+ -[SFShareSheetSessionManager fetchExistingShareForFileOrFolderURL:completionHandler:]
+ GCC_except_table127
+ GCC_except_table133
+ GCC_except_table137
+ GCC_except_table139
+ GCC_except_table192
+ GCC_except_table198
+ GCC_except_table205
+ GCC_except_table206
+ OBJC_IVAR_$_SFAllowAccessTapEvent._hostAppBundleID
+ OBJC_IVAR_$_SFAuthenticationManager._pairingLAContexts
+ _OBJC_CLASS_$_LAContext
+ _OBJC_CLASS_$_SFAllowAccessTapEvent
+ _OBJC_CLASS_$__TtCO7Sharing20SFAirDropInvocations17ReportBoopOutcome
+ _OBJC_METACLASS_$_SFAllowAccessTapEvent
+ _OBJC_METACLASS_$__TtCO7Sharing20SFAirDropInvocations17ReportBoopOutcome
+ __80-[SFAuthenticationManager _enableForType:withIDSDeviceID:passcodeRef:sessionID:]_block_invoke
+ __80-[SFAuthenticationManager _enableForType:withIDSDeviceID:passcodeRef:sessionID:]_block_invoke_2
+ __80-[SFCollaborationPerformer _checkTransportAndProceedWithAddParticipantsAllowed:]_block_invoke_3
+ __81+[SFCollaborationUtilities addItemAllowedForCollaborationItem:completionHandler:]_block_invoke
+ __CLASS_METHODS__TtCO7Sharing20SFAirDropInvocations17ReportBoopOutcome
+ __CLASS_PROPERTIES__TtCO7Sharing20SFAirDropInvocations17ReportBoopOutcome
+ __DATA__TtCO7Sharing20SFAirDropInvocations17ReportBoopOutcome
+ __INSTANCE_METHODS__TtCO7Sharing20SFAirDropInvocations17ReportBoopOutcome
+ __METACLASS_DATA__TtCO7Sharing20SFAirDropInvocations17ReportBoopOutcome
+ __OBJC_$_CLASS_METHODS_SFAllowAccessTapEvent
+ __OBJC_$_CLASS_PROP_LIST_SFAllowAccessTapEvent
+ __OBJC_$_INSTANCE_METHODS_SFAllowAccessTapEvent
+ __OBJC_$_INSTANCE_VARIABLES_SFAllowAccessTapEvent
+ __OBJC_$_PROP_LIST_SFAllowAccessTapEvent
+ __OBJC_CLASS_PROTOCOLS_$_SFAllowAccessTapEvent
+ __OBJC_CLASS_RO_$_SFAllowAccessTapEvent
+ __OBJC_METACLASS_RO_$_SFAllowAccessTapEvent
+ ___57-[SFCollaborationPerformer _isCurrentUserCoOwnerOfShare:]_block_invoke
+ ___80-[SFAuthenticationManager _enableForType:withIDSDeviceID:passcodeRef:sessionID:]_block_invoke
+ ___80-[SFAuthenticationManager _enableForType:withIDSDeviceID:passcodeRef:sessionID:]_block_invoke_2
+ ___80-[SFCollaborationPerformer _checkTransportAndProceedWithAddParticipantsAllowed:]_block_invoke_3
+ ___81+[SFCollaborationUtilities addItemAllowedForCollaborationItem:completionHandler:]_block_invoke
+ ___83+[SFCollaborationUtilities fetchExistingShareForFileOrFolderURL:completionHandler:]_block_invoke
+ ___block_descriptor_40_e8_32bs_e39_v32?0"NSURL"8"CKShare"16"NSError"24l
+ ___block_descriptor_40_e8_32r_e14_v20?0B8B12B16l
+ ___block_descriptor_40_e8_32r_e27_v16?0"RTIDocumentTraits"8l
+ ___block_descriptor_49_e8_32w_e29_v24?0"CKShare"8"NSError"16l
+ ___flagsForRTISession_block_invoke
+ ___getCKPhotosSharedCollectionsShareTypeSymbolLoc_block_invoke
+ ___infoForRTISession_block_invoke
+ __swift__destructor.431Tm
+ __swift_closure_destructor.1319Tm
+ __swift_closure_destructor.451Tm
+ __swift_closure_destructor.472Tm
+ __swift_closure_destructor.484Tm
+ __swift_closure_destructor.558Tm
+ __swift_closure_destructor.908Tm
+ _associated conformance 7Sharing20SFAirDropInvocationsO17ReportBoopOutcomeCAA22SFXPCInvocableProtocolAA10ParametersAaFP_SE
+ _associated conformance 7Sharing20SFAirDropInvocationsO17ReportBoopOutcomeCAA22SFXPCInvocableProtocolAA10ParametersAaFP_Se
+ _associated conformance 7Sharing20SFAirDropInvocationsO17ReportBoopOutcomeCAA22SFXPCInvocableProtocolAA8ResponseAaFP_SE
+ _associated conformance 7Sharing20SFAirDropInvocationsO17ReportBoopOutcomeCAA22SFXPCInvocableProtocolAA8ResponseAaFP_Se
+ _associated conformance 7Sharing6SFBoopO11CancelStageOSHAASQ
+ _associated conformance 7Sharing6SFBoopO11FailureCodeOSHAASQ
+ _associated conformance 7Sharing6SFBoopO13OutcomeReportV10CodingKeys33_0B461A7249AF7F550805D115321262CALLOSHAASQ
+ _associated conformance 7Sharing6SFBoopO13OutcomeReportV10CodingKeys33_0B461A7249AF7F550805D115321262CALLOs0E3KeyAAs23CustomStringConvertible
+ _associated conformance 7Sharing6SFBoopO13OutcomeReportV10CodingKeys33_0B461A7249AF7F550805D115321262CALLOs0E3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 7Sharing6SFBoopO7OutcomeO10CodingKeys33_0B461A7249AF7F550805D115321262CALLOSHAASQ
+ _associated conformance 7Sharing6SFBoopO7OutcomeO10CodingKeys33_0B461A7249AF7F550805D115321262CALLOs0D3KeyAAs23CustomStringConvertible
+ _associated conformance 7Sharing6SFBoopO7OutcomeO10CodingKeys33_0B461A7249AF7F550805D115321262CALLOs0D3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 7Sharing6SFBoopO7OutcomeO16FailedCodingKeys33_0B461A7249AF7F550805D115321262CALLOSHAASQ
+ _associated conformance 7Sharing6SFBoopO7OutcomeO16FailedCodingKeys33_0B461A7249AF7F550805D115321262CALLOs0E3KeyAAs23CustomStringConvertible
+ _associated conformance 7Sharing6SFBoopO7OutcomeO16FailedCodingKeys33_0B461A7249AF7F550805D115321262CALLOs0E3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 7Sharing6SFBoopO7OutcomeO19CancelledCodingKeys33_0B461A7249AF7F550805D115321262CALLOSHAASQ
+ _associated conformance 7Sharing6SFBoopO7OutcomeO19CancelledCodingKeys33_0B461A7249AF7F550805D115321262CALLOs0E3KeyAAs23CustomStringConvertible
+ _associated conformance 7Sharing6SFBoopO7OutcomeO19CancelledCodingKeys33_0B461A7249AF7F550805D115321262CALLOs0E3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 7Sharing6SFBoopO7OutcomeO19CompletedCodingKeys33_0B461A7249AF7F550805D115321262CALLOs0E3KeyAAs23CustomStringConvertible
+ _associated conformance 7Sharing6SFBoopO7OutcomeO19CompletedCodingKeys33_0B461A7249AF7F550805D115321262CALLOs0E3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 7Sharing6SFBoopO7OutcomeO20BannerOnlyCodingKeys33_0B461A7249AF7F550805D115321262CALLOs0F3KeyAAs23CustomStringConvertible
+ _associated conformance 7Sharing6SFBoopO7OutcomeO20BannerOnlyCodingKeys33_0B461A7249AF7F550805D115321262CALLOs0F3KeyAAs28CustomDebugStringConvertible
+ _getCKShareTypeKey
+ _objc_msgSend$_enableForType:withIDSDeviceID:passcodeRef:sessionID:
+ _objc_msgSend$_isCurrentUserCoOwnerOfShare:
+ _objc_msgSend$_releasePairingContextForSessionID:
+ _objc_msgSend$documentTraitsSafeAccess:
+ _objc_msgSend$externalizedContext
+ _objc_msgSend$fetchExistingShareForFileOrFolderURL:completionHandler:
+ _objc_msgSend$pairingLAContexts
+ _objc_msgSend$setCredential:type:error:
+ _objc_msgSend$setHostAppBundleID:
+ _symbolic _____ 7Sharing20SFAirDropInvocationsO17ReportBoopOutcomeC
+ _symbolic _____ 7Sharing6SFBoopO
+ _symbolic _____ 7Sharing6SFBoopO11CancelStageO
+ _symbolic _____ 7Sharing6SFBoopO11FailureCodeO
+ _symbolic _____ 7Sharing6SFBoopO13OutcomeReportV
+ _symbolic _____ 7Sharing6SFBoopO13OutcomeReportV10CodingKeys33_0B461A7249AF7F550805D115321262CALLO
+ _symbolic _____ 7Sharing6SFBoopO7OutcomeO
+ _symbolic _____ 7Sharing6SFBoopO7OutcomeO10CodingKeys33_0B461A7249AF7F550805D115321262CALLO
+ _symbolic _____ 7Sharing6SFBoopO7OutcomeO16FailedCodingKeys33_0B461A7249AF7F550805D115321262CALLO
+ _symbolic _____ 7Sharing6SFBoopO7OutcomeO19CancelledCodingKeys33_0B461A7249AF7F550805D115321262CALLO
+ _symbolic _____ 7Sharing6SFBoopO7OutcomeO19CompletedCodingKeys33_0B461A7249AF7F550805D115321262CALLO
+ _symbolic _____ 7Sharing6SFBoopO7OutcomeO20BannerOnlyCodingKeys33_0B461A7249AF7F550805D115321262CALLO
+ _symbolic _____4code_t 7Sharing6SFBoopO11FailureCodeO
+ _symbolic _____5stage_t 7Sharing6SFBoopO11CancelStageO
+ _symbolic _____ySSSo11NSExtensionCG s18_DictionaryStorageC
+ _symbolic _____y_____G s22KeyedDecodingContainerV 7Sharing6SFBoopO13OutcomeReportV10CodingKeys33_0B461A7249AF7F550805D115321262CALLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 7Sharing6SFBoopO7OutcomeO10CodingKeys33_0B461A7249AF7F550805D115321262CALLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 7Sharing6SFBoopO7OutcomeO16FailedCodingKeys33_0B461A7249AF7F550805D115321262CALLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 7Sharing6SFBoopO7OutcomeO19CancelledCodingKeys33_0B461A7249AF7F550805D115321262CALLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 7Sharing6SFBoopO7OutcomeO19CompletedCodingKeys33_0B461A7249AF7F550805D115321262CALLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 7Sharing6SFBoopO7OutcomeO20BannerOnlyCodingKeys33_0B461A7249AF7F550805D115321262CALLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 7Sharing6SFBoopO13OutcomeReportV10CodingKeys33_0B461A7249AF7F550805D115321262CALLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 7Sharing6SFBoopO7OutcomeO10CodingKeys33_0B461A7249AF7F550805D115321262CALLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 7Sharing6SFBoopO7OutcomeO16FailedCodingKeys33_0B461A7249AF7F550805D115321262CALLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 7Sharing6SFBoopO7OutcomeO19CancelledCodingKeys33_0B461A7249AF7F550805D115321262CALLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 7Sharing6SFBoopO7OutcomeO19CompletedCodingKeys33_0B461A7249AF7F550805D115321262CALLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 7Sharing6SFBoopO7OutcomeO20BannerOnlyCodingKeys33_0B461A7249AF7F550805D115321262CALLO
+ getCKPhotosSharedCollectionsShareTypeSymbolLoc.ptr
+ getCKShareTypeKey
- GCC_except_table132
- GCC_except_table136
- GCC_except_table138
- GCC_except_table191
- GCC_except_table196
- __69-[SFAuthenticationManager enableForType:withIDSDeviceID:passcodeRef:]_block_invoke
- __69-[SFAuthenticationManager enableForType:withIDSDeviceID:passcodeRef:]_block_invoke_2
- ___69-[SFAuthenticationManager enableForType:withIDSDeviceID:passcodeRef:]_block_invoke
- ___69-[SFAuthenticationManager enableForType:withIDSDeviceID:passcodeRef:]_block_invoke_2
- __swift__destructor.362Tm
- __swift_closure_destructor.382Tm
- __swift_closure_destructor.403Tm
- __swift_closure_destructor.415Tm
- __swift_closure_destructor.489Tm
- __swift_closure_destructor.839Tm
- _objc_msgSend$documentTraits
- _symbolic _____ySSSaySo11NSExtensionCGG s18_DictionaryStorageC
CStrings:
+ "%@ Fetching existing share for URL %@"
+ "CKPhotosSharedCollectionsShareType"
+ "Current user is a co-owner of the existing URL share, skipping transport warning alert"
+ "Current user is a co-owner of the loaded share, skipping transport warning alert"
+ "Current user is a co-owner of the share, skipping transport warning alert"
+ "Failed to externalize passcode as ACM context, falling back to raw passcode: %{public}@"
+ "Failed to load existing share for URL: %@"
+ "File is (or was) shared publicly but options changed, updating options (isPrivateShare: %d, publicPermission: %ld)"
+ "Mac16,10"
+ "Mac16,11"
+ "Mac16,2"
+ "Mac16,3"
+ "MacMini2024"
+ "NSString *getCKPhotosSharedCollectionsShareType(void)"
+ "Share is (or was) shared publicly but options changed, updating options (isPrivateShare: %d, publicPermission: %ld)"
+ "Sharing/SFShareSheetService/fetchExistingShareForFileOrFolderURL:completionHandler:"
+ "Successfully set warning flag (flagType: %ld) for existing URL share"
+ "Warning already shown for existing URL share (flagType: %ld), skipping alert"
+ "afterReceiveOnly"
+ "afterShare"
+ "com.apple.sharing.allowAccessTap"
+ "dismissed"
+ "v16@?0@\"RTIDocumentTraits\"8"
+ "v24@?0@\"CKShare\"8@\"NSError\"16"
- "Failed to get value for key: OSVersion"
- "File is shared publicly but options changed, updating options"
- "MockA2DPActivity"
- "Share is existing public share but options changed, updating options"
```
