## CoreCDPInternal

> `/System/Library/PrivateFrameworks/CoreCDPInternal.framework/CoreCDPInternal`

```diff

-404.0.0.0.0
-  __TEXT.__text: 0x90b5c
+406.0.0.0.0
+  __TEXT.__text: 0x91dec
   __TEXT.__auth_stubs: 0x1100
-  __TEXT.__objc_methlist: 0x54e4
+  __TEXT.__objc_methlist: 0x5514
   __TEXT.__const: 0x8c4
-  __TEXT.__oslogstring: 0x14036
-  __TEXT.__cstring: 0x8c9e
+  __TEXT.__oslogstring: 0x14066
+  __TEXT.__cstring: 0xcd6e
   __TEXT.__gcc_except_tab: 0xc78
   __TEXT.__dlopen_cstrs: 0xb0
   __TEXT.__swift5_typeref: 0x341

   __TEXT.__swift5_capture: 0x1b8
   __TEXT.__swift_as_entry: 0x5c
   __TEXT.__swift_as_ret: 0x60
-  __TEXT.__unwind_info: 0x1d40
+  __TEXT.__unwind_info: 0x1d48
   __TEXT.__eh_frame: 0x8d0
   __TEXT.__objc_classname: 0xcbd
-  __TEXT.__objc_methname: 0xf1be
+  __TEXT.__objc_methname: 0xf24d
   __TEXT.__objc_methtype: 0x2987
-  __TEXT.__objc_stubs: 0xc3e0
-  __DATA_CONST.__got: 0x1030
-  __DATA_CONST.__const: 0x2650
+  __TEXT.__objc_stubs: 0xc480
+  __DATA_CONST.__got: 0x1068
+  __DATA_CONST.__const: 0x2630
   __DATA_CONST.__objc_classlist: 0x288
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x170
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3738
+  __DATA_CONST.__objc_selrefs: 0x3760
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x168
   __DATA_CONST.__objc_arraydata: 0x90
   __AUTH_CONST.__auth_got: 0x890
-  __AUTH_CONST.__const: 0xb60
-  __AUTH_CONST.__cfstring: 0x5bc0
+  __AUTH_CONST.__const: 0xba0
+  __AUTH_CONST.__cfstring: 0x8220
   __AUTH_CONST.__objc_const: 0xfc90
   __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__objc_arrayobj: 0x60

   __AUTH.__data: 0x58
   __DATA.__objc_ivar: 0x3b0
   __DATA.__data: 0x1198
-  __DATA.__bss: 0x8c0
+  __DATA.__bss: 0x8f0
   __DATA_DIRTY.__objc_data: 0xa38
   __DATA_DIRTY.__data: 0x78
   __DATA_DIRTY.__bss: 0x138

   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: C6592813-04A2-325D-AF0F-82EEB6AC0078
-  Functions: 3097
-  Symbols:   10019
-  CStrings:  5636
+  UUID: 73656D29-CC01-396D-A658-24ECB97DC889
+  Functions: 3107
+  Symbols:   10050
+  CStrings:  6256
 
Symbols:
+ +[CDPDAnalyticsTransport getAllowedElementIdentifiers]
+ +[CDPDAnalyticsTransport getAllowedElementIdentifiers].cold.1
+ +[CDPDAnalyticsTransport getAllowedHandlerKey]
+ +[CDPDAnalyticsTransport getAllowedHandlerKey].cold.1
+ +[CDPDAnalyticsTransport getAllowedHookName]
+ +[CDPDAnalyticsTransport getAllowedHookName].cold.1
+ +[CDPDFollowUpController analyticsEventWithEventName:context:identifier:]
+ +[CDPDFollowUpController analyticsEventWithEventName:context:identifier:].cold.1
+ GCC_except_table54
+ _OBJC_CLASS_$_AAAFollowUpAnalyticsInfo
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.1906
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.1906.cold.1
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.1907
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.1907.cold.1
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.1970
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.1970.cold.1
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.1970.cold.2
+ ___44+[CDPDAnalyticsTransport getAllowedHookName]_block_invoke
+ ___46+[CDPDAnalyticsTransport getAllowedHandlerKey]_block_invoke
+ ___54+[CDPDAnalyticsTransport getAllowedElementIdentifiers]_block_invoke
+ ___81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke.1971
+ ___81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke_2.1973
+ ___81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke_2.1973.cold.1
+ ___block_literal_global.1043
+ ___block_literal_global.1072
+ ___block_literal_global.1875
+ ___block_literal_global.1887
+ ___block_literal_global.1903
+ ___block_literal_global.1975
+ ___block_literal_global.47
+ ___block_literal_global.487
+ ___block_literal_global.804
+ ___block_literal_global.815
+ ___block_literal_global.916
+ ___block_literal_global.963
+ _getAllowedElementIdentifiers.approvedElementIdentifiers
+ _getAllowedElementIdentifiers.onceToken
+ _getAllowedHandlerKey.approvedHandlerKeys
+ _getAllowedHandlerKey.onceToken
+ _getAllowedHookName.approvedHookNames
+ _getAllowedHookName.onceToken
+ _kAAFClearFollowupEvent
+ _kAAFPendingCFUTypes
+ _kAAFPostFollowupEvent
+ _kAKElementIdentifier
+ _kAKProcessHandlerKey
+ _kAKProcessHook
+ _objc_msgSend$analyticsEventWithEventName:context:identifier:
+ _objc_msgSend$analyticsEventWithName:eventCategory:followupAnalyticsData:altDSID:
+ _objc_msgSend$getAllowedElementIdentifiers
+ _objc_msgSend$getAllowedHandlerKey
+ _objc_msgSend$getAllowedHookName
+ _objc_msgSend$setCfuType:
- +[CDPDAnalyticsTransport getAllowedEscapeOffer].cold.1
- GCC_except_table48
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.1045
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.1045.cold.1
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.1045.cold.2
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.981
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.981.cold.1
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.982
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.982.cold.1
- ___81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke.1046
- ___81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke_2.1048
- ___81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke_2.1048.cold.1
- ___block_literal_global.1050
- ___block_literal_global.490
- ___block_literal_global.50
- ___block_literal_global.789
- ___block_literal_global.800
- ___block_literal_global.802
- ___block_literal_global.903
- ___block_literal_global.950
- ___block_literal_global.962
- ___block_literal_global.978
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_CoreCDPInternal
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_CoreCDPInternal
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_CoreCDPInternal
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_CoreCDPInternal
- _kAAAPendingCFUTypes
- _objc_msgSend$analyticsEventWithFollowUpContext:eventName:category:
CStrings:
+ "CDP was requested to process a non-allowed CFU: %@"
+ "Complete"
+ "account:navigateToSignIn"
+ "account:signout"
+ "action:hideMyEmailUpdateCache"
+ "action:matterhornUpsell"
+ "ak:auth"
+ "ams:paymentVerification"
+ "analyticsEventWithEventName:context:identifier:"
+ "analyticsEventWithName:eventCategory:followupAnalyticsData:altDSID:"
+ "beneficiary:contactName"
+ "cancel"
+ "cdp:repair"
+ "cdp:upgrade"
+ "code:generate"
+ "com.apple.remoteUI.activateElement"
+ "com.apple.remoteUI.loadURL"
+ "com.apple.remoteUI.processHandler"
+ "com.apple.remoteUI.processHook"
+ "com.apple.remoteUI.renderUI"
+ "com.apple.remoteUI.reportError"
+ "com.apple.remoteui.iforgot_account_inactive"
+ "com.apple.remoteui.iforgot_account_locked"
+ "com.apple.remoteui.iforgot_account_not-eligible"
+ "com.apple.remoteui.iforgot_appleid_locked"
+ "com.apple.remoteui.iforgot_appleid_settings_dismiss"
+ "com.apple.remoteui.iforgot_dismiss"
+ "com.apple.remoteui.iforgot_email_add"
+ "com.apple.remoteui.iforgot_embargo_cancel"
+ "com.apple.remoteui.iforgot_embargo_cancel_choice_1"
+ "com.apple.remoteui.iforgot_embargo_cancel_page"
+ "com.apple.remoteui.iforgot_embargo_cancel_teardown"
+ "com.apple.remoteui.iforgot_embargo_inprogress"
+ "com.apple.remoteui.iforgot_embargo_inprogress_alert"
+ "com.apple.remoteui.iforgot_embargo_inprogress_button_1"
+ "com.apple.remoteui.iforgot_embargo_inprogress_choice_1"
+ "com.apple.remoteui.iforgot_embargo_inprogress_choice_2"
+ "com.apple.remoteui.iforgot_embargo_inprogress_multiChoice_1"
+ "com.apple.remoteui.iforgot_embargo_inprogress_multiChoice_2"
+ "com.apple.remoteui.iforgot_embargo_inprogress_page"
+ "com.apple.remoteui.iforgot_embargo_recovery_startover"
+ "com.apple.remoteui.iforgot_embargo_verification_startover"
+ "com.apple.remoteui.iforgot_embargo_verify_existingphone_account"
+ "com.apple.remoteui.iforgot_embargo_verify_existingphone_account_send"
+ "com.apple.remoteui.iforgot_embargo_verify_existingphone_trusted"
+ "com.apple.remoteui.iforgot_embargo_verify_existingphone_trusted_send"
+ "com.apple.remoteui.iforgot_embargo_verify_newphone"
+ "com.apple.remoteui.iforgot_embargo_verify_newphone_send"
+ "com.apple.remoteui.iforgot_embargo_verify_newphone_smscode"
+ "com.apple.remoteui.iforgot_embargo_verify_phoneoptions"
+ "com.apple.remoteui.iforgot_embargo_verify_recoverycode"
+ "com.apple.remoteui.iforgot_embargo_verify_recoverycode_send"
+ "com.apple.remoteui.iforgot_embargo_verify_recoveryphone"
+ "com.apple.remoteui.iforgot_embargo_verify_trustedphone"
+ "com.apple.remoteui.iforgot_embargo_verify_verificationcode"
+ "com.apple.remoteui.iforgot_embargo_verify_verificationcode_alert"
+ "com.apple.remoteui.iforgot_embargo_verify_verificationcode_alert_1"
+ "com.apple.remoteui.iforgot_embargo_verify_verificationcode_button_1"
+ "com.apple.remoteui.iforgot_embargo_verify_verificationcode_footer_1"
+ "com.apple.remoteui.iforgot_embargo_verify_verificationcode_page"
+ "com.apple.remoteui.iforgot_embargo_verify_verificationcode_pinView_1"
+ "com.apple.remoteui.iforgot_embargo_verify_verificationcode_send"
+ "com.apple.remoteui.iforgot_embargo_verify_verificationcode_send_page"
+ "com.apple.remoteui.iforgot_embargo_verify_verificationcode_send_pinView_1"
+ "com.apple.remoteui.iforgot_iforgot_password_reset"
+ "com.apple.remoteui.iforgot_iforgot_password_verify_appleid"
+ "com.apple.remoteui.iforgot_password_authenticationmethod"
+ "com.apple.remoteui.iforgot_password_authenticationmethod_alert_1"
+ "com.apple.remoteui.iforgot_password_authenticationmethod_button_1"
+ "com.apple.remoteui.iforgot_password_authenticationmethod_linkRow_1"
+ "com.apple.remoteui.iforgot_password_authenticationmethod_page"
+ "com.apple.remoteui.iforgot_password_resend_securitycode"
+ "com.apple.remoteui.iforgot_password_reset"
+ "com.apple.remoteui.iforgot_password_reset_alert"
+ "com.apple.remoteui.iforgot_password_reset_buttonBarItem_1"
+ "com.apple.remoteui.iforgot_password_reset_choice_1"
+ "com.apple.remoteui.iforgot_password_reset_editableTextRow_1"
+ "com.apple.remoteui.iforgot_password_reset_editableTextRow_2"
+ "com.apple.remoteui.iforgot_password_reset_footer_1"
+ "com.apple.remoteui.iforgot_password_reset_header_1"
+ "com.apple.remoteui.iforgot_password_reset_multiChoice_1"
+ "com.apple.remoteui.iforgot_password_reset_navigationBar_1"
+ "com.apple.remoteui.iforgot_password_reset_options"
+ "com.apple.remoteui.iforgot_password_reset_page"
+ "com.apple.remoteui.iforgot_password_reset_signout"
+ "com.apple.remoteui.iforgot_password_reset_tokens"
+ "com.apple.remoteui.iforgot_password_unlock"
+ "com.apple.remoteui.iforgot_password_unlock_alert"
+ "com.apple.remoteui.iforgot_password_unlock_choice_1"
+ "com.apple.remoteui.iforgot_password_unlock_forgot"
+ "com.apple.remoteui.iforgot_password_unlock_multiChoice_1"
+ "com.apple.remoteui.iforgot_password_unlock_page"
+ "com.apple.remoteui.iforgot_password_verify_appleid"
+ "com.apple.remoteui.iforgot_password_verify_appleid_buttonBarItem_1"
+ "com.apple.remoteui.iforgot_password_verify_appleid_editableTextRow_1"
+ "com.apple.remoteui.iforgot_password_verify_appleid_multiChoice_1"
+ "com.apple.remoteui.iforgot_password_verify_appleid_page"
+ "com.apple.remoteui.iforgot_password_verify_appleid_subHeader_1"
+ "com.apple.remoteui.iforgot_password_verify_biometric_ratchet"
+ "com.apple.remoteui.iforgot_password_verify_biometric_ratchet_alert_1"
+ "com.apple.remoteui.iforgot_password_verify_birthday"
+ "com.apple.remoteui.iforgot_password_verify_birthday_alert_1"
+ "com.apple.remoteui.iforgot_password_verify_birthday_linkBarItem_1"
+ "com.apple.remoteui.iforgot_password_verify_birthday_multiChoice_1"
+ "com.apple.remoteui.iforgot_password_verify_birthday_page"
+ "com.apple.remoteui.iforgot_password_verify_confirm_account"
+ "com.apple.remoteui.iforgot_password_verify_confirm_account_multiChoice_1"
+ "com.apple.remoteui.iforgot_password_verify_confirm_account_page"
+ "com.apple.remoteui.iforgot_password_verify_critical_account_edit_block"
+ "com.apple.remoteui.iforgot_password_verify_critical_account_edit_block_alert_1"
+ "com.apple.remoteui.iforgot_password_verify_critical_account_edit_block_multiChoice_1"
+ "com.apple.remoteui.iforgot_password_verify_critical_account_edit_block_page"
+ "com.apple.remoteui.iforgot_password_verify_custodianApproval_cantuse"
+ "com.apple.remoteui.iforgot_password_verify_device"
+ "com.apple.remoteui.iforgot_password_verify_devicenotification"
+ "com.apple.remoteui.iforgot_password_verify_devicenotification_alert"
+ "com.apple.remoteui.iforgot_password_verify_devicenotification_button_1"
+ "com.apple.remoteui.iforgot_password_verify_devicenotification_cancelButton_1"
+ "com.apple.remoteui.iforgot_password_verify_devicenotification_donthaveaccess"
+ "com.apple.remoteui.iforgot_password_verify_devicenotification_htmlHeader_1"
+ "com.apple.remoteui.iforgot_password_verify_devicenotification_multiChoice_1"
+ "com.apple.remoteui.iforgot_password_verify_devicenotification_multiChoice_2"
+ "com.apple.remoteui.iforgot_password_verify_devicenotification_navigationBar_1"
+ "com.apple.remoteui.iforgot_password_verify_devicenotification_page"
+ "com.apple.remoteui.iforgot_password_verify_email"
+ "com.apple.remoteui.iforgot_password_verify_email_didntgetcode"
+ "com.apple.remoteui.iforgot_password_verify_email_resend"
+ "com.apple.remoteui.iforgot_password_verify_email_send"
+ "com.apple.remoteui.iforgot_password_verify_icloudsecuritycode"
+ "com.apple.remoteui.iforgot_password_verify_icloudsecuritycode_alert_1"
+ "com.apple.remoteui.iforgot_password_verify_icloudsecuritycode_button_1"
+ "com.apple.remoteui.iforgot_password_verify_icloudsecuritycode_cancelButton_1"
+ "com.apple.remoteui.iforgot_password_verify_icloudsecuritycode_footer_1"
+ "com.apple.remoteui.iforgot_password_verify_icloudsecuritycode_navigationBar_1"
+ "com.apple.remoteui.iforgot_password_verify_icloudsecuritycode_page"
+ "com.apple.remoteui.iforgot_password_verify_mk"
+ "com.apple.remoteui.iforgot_password_verify_mk_navigationBar_1"
+ "com.apple.remoteui.iforgot_password_verify_mk_page"
+ "com.apple.remoteui.iforgot_password_verify_mk_spinnerView_1"
+ "com.apple.remoteui.iforgot_password_verify_passcode"
+ "com.apple.remoteui.iforgot_password_verify_passcode_alert"
+ "com.apple.remoteui.iforgot_password_verify_passcode_button_1"
+ "com.apple.remoteui.iforgot_password_verify_passcode_footer_1"
+ "com.apple.remoteui.iforgot_password_verify_passcode_forgot"
+ "com.apple.remoteui.iforgot_password_verify_passcode_page"
+ "com.apple.remoteui.iforgot_password_verify_passcode_pinView_1"
+ "com.apple.remoteui.iforgot_password_verify_password"
+ "com.apple.remoteui.iforgot_password_verify_password_alert_1"
+ "com.apple.remoteui.iforgot_password_verify_password_forgot"
+ "com.apple.remoteui.iforgot_password_verify_password_multiChoice_1"
+ "com.apple.remoteui.iforgot_password_verify_password_page"
+ "com.apple.remoteui.iforgot_password_verify_payment"
+ "com.apple.remoteui.iforgot_password_verify_payment_card"
+ "com.apple.remoteui.iforgot_password_verify_payment_none"
+ "com.apple.remoteui.iforgot_password_verify_phone"
+ "com.apple.remoteui.iforgot_password_verify_phone_alert_1"
+ "com.apple.remoteui.iforgot_password_verify_phone_buttonBarItem_1"
+ "com.apple.remoteui.iforgot_password_verify_phone_dismiss"
+ "com.apple.remoteui.iforgot_password_verify_phone_editableTextRow_1"
+ "com.apple.remoteui.iforgot_password_verify_phone_multiChoice_1"
+ "com.apple.remoteui.iforgot_password_verify_phone_page"
+ "com.apple.remoteui.iforgot_password_verify_phone_subHeader_1"
+ "com.apple.remoteui.iforgot_password_verify_phone_unenrollment"
+ "com.apple.remoteui.iforgot_password_verify_questions"
+ "com.apple.remoteui.iforgot_password_verify_questions_alert_1"
+ "com.apple.remoteui.iforgot_password_verify_questions_cancelButton_1"
+ "com.apple.remoteui.iforgot_password_verify_questions_linkBarItem_1"
+ "com.apple.remoteui.iforgot_password_verify_questions_page"
+ "com.apple.remoteui.iforgot_password_verify_recoverykey"
+ "com.apple.remoteui.iforgot_password_verify_resetmethod"
+ "com.apple.remoteui.iforgot_password_verify_securityKey"
+ "com.apple.remoteui.iforgot_password_verify_securityKey_page"
+ "com.apple.remoteui.iforgot_password_verify_securitycode"
+ "com.apple.remoteui.iforgot_password_verify_smscode"
+ "com.apple.remoteui.iforgot_password_verify_smscode_alert"
+ "com.apple.remoteui.iforgot_password_verify_smscode_alert_1"
+ "com.apple.remoteui.iforgot_password_verify_smscode_cancelButton_1"
+ "com.apple.remoteui.iforgot_password_verify_smscode_cantuse"
+ "com.apple.remoteui.iforgot_password_verify_smscode_htmlHeader_1"
+ "com.apple.remoteui.iforgot_password_verify_smscode_linkRow_1"
+ "com.apple.remoteui.iforgot_password_verify_smscode_multiChoice_1"
+ "com.apple.remoteui.iforgot_password_verify_smscode_multiChoice_2"
+ "com.apple.remoteui.iforgot_password_verify_smscode_navigationBar_1"
+ "com.apple.remoteui.iforgot_password_verify_smscode_page"
+ "com.apple.remoteui.iforgot_password_verify_smscode_send"
+ "com.apple.remoteui.iforgot_password_verify_smscode_send_alert"
+ "com.apple.remoteui.iforgot_password_verify_smscode_send_button_1"
+ "com.apple.remoteui.iforgot_password_verify_smscode_send_button_2"
+ "com.apple.remoteui.iforgot_password_verify_smscode_send_button_3"
+ "com.apple.remoteui.iforgot_password_verify_smscode_send_cancelButton_1"
+ "com.apple.remoteui.iforgot_password_verify_smscode_send_footer_1"
+ "com.apple.remoteui.iforgot_password_verify_smscode_send_htmlHeader_1"
+ "com.apple.remoteui.iforgot_password_verify_smscode_send_navigationBar_1"
+ "com.apple.remoteui.iforgot_password_verify_smscode_send_page"
+ "com.apple.remoteui.iforgot_password_verify_smscode_send_pinView_1"
+ "com.apple.remoteui.iforgot_password_verify_start_custodianApproval"
+ "com.apple.remoteui.iforgot_password_verify_start_custodianApproval_multiChoice_1"
+ "com.apple.remoteui.iforgot_password_verify_start_custodianApproval_multiChoice_2"
+ "com.apple.remoteui.iforgot_password_verify_start_custodianApproval_navigationBar_1"
+ "com.apple.remoteui.iforgot_password_verify_start_custodianApproval_page"
+ "com.apple.remoteui.iforgot_password_verify_start_custodianApproval_subHeader_1"
+ "com.apple.remoteui.iforgot_phone_add"
+ "com.apple.remoteui.iforgot_questions_reset"
+ "com.apple.remoteui.iforgot_questions_reset_confirmation"
+ "com.apple.remoteui.iforgot_questions_reset_options"
+ "com.apple.remoteui.iforgot_questions_verify_device"
+ "com.apple.remoteui.iforgot_questions_verify_device_code"
+ "com.apple.remoteui.iforgot_questions_verify_email"
+ "com.apple.remoteui.iforgot_questions_verify_questions"
+ "com.apple.remoteui.iforgot_questions_verify_questions_alert_1"
+ "com.apple.remoteui.iforgot_questions_verify_questions_button_1"
+ "com.apple.remoteui.iforgot_questions_verify_questions_page"
+ "com.apple.remoteui.iforgot_recovery"
+ "com.apple.remoteui.iforgot_recovery_alert_1"
+ "com.apple.remoteui.iforgot_recovery_button_1"
+ "com.apple.remoteui.iforgot_recovery_embargo"
+ "com.apple.remoteui.iforgot_recovery_embargo_alert_1"
+ "com.apple.remoteui.iforgot_recovery_embargo_choice_1"
+ "com.apple.remoteui.iforgot_recovery_embargo_page"
+ "com.apple.remoteui.iforgot_recovery_multiChoice_1"
+ "com.apple.remoteui.iforgot_recovery_page"
+ "com.apple.remoteui.iforgot_recovery_start"
+ "com.apple.remoteui.iforgot_recovery_verify_creditcard"
+ "com.apple.remoteui.iforgot_recovery_verify_creditcard_cantprovide"
+ "com.apple.remoteui.iforgot_recovery_verify_email"
+ "com.apple.remoteui.iforgot_recovery_verify_email_alert"
+ "com.apple.remoteui.iforgot_recovery_verify_email_button_1"
+ "com.apple.remoteui.iforgot_recovery_verify_email_cancelButton_1"
+ "com.apple.remoteui.iforgot_recovery_verify_email_didntgetcode"
+ "com.apple.remoteui.iforgot_recovery_verify_email_multiChoice_1"
+ "com.apple.remoteui.iforgot_recovery_verify_email_page"
+ "com.apple.remoteui.iforgot_recovery_verify_email_resend"
+ "com.apple.remoteui.iforgot_recovery_verify_email_send"
+ "com.apple.remoteui.iforgot_recovery_verify_email_send_page"
+ "com.apple.remoteui.iforgot_recovery_verify_email_send_pinView_1"
+ "com.apple.remoteui.iforgot_recovery_verify_newphone"
+ "com.apple.remoteui.iforgot_recovery_verify_newphone_alert_1"
+ "com.apple.remoteui.iforgot_recovery_verify_newphone_button_1"
+ "com.apple.remoteui.iforgot_recovery_verify_newphone_multiChoice_1"
+ "com.apple.remoteui.iforgot_recovery_verify_newphone_page"
+ "com.apple.remoteui.iforgot_recovery_verify_newphone_pinView_1"
+ "com.apple.remoteui.iforgot_recovery_verify_newphone_send"
+ "com.apple.remoteui.iforgot_recovery_verify_newphone_send_alert"
+ "com.apple.remoteui.iforgot_recovery_verify_newphone_send_button_2"
+ "com.apple.remoteui.iforgot_recovery_verify_newphone_send_footer_1"
+ "com.apple.remoteui.iforgot_recovery_verify_newphone_send_page"
+ "com.apple.remoteui.iforgot_recovery_verify_newphone_send_pinView_1"
+ "com.apple.remoteui.iforgot_recovery_verify_newphone_smscode"
+ "com.apple.remoteui.iforgot_recovery_verify_newphone_smscode_alert_1"
+ "com.apple.remoteui.iforgot_recovery_verify_newphone_smscode_multiChoice_1"
+ "com.apple.remoteui.iforgot_recovery_verify_newphone_smscode_page"
+ "com.apple.remoteui.iforgot_recovery_verify_same_securityKey_verified"
+ "com.apple.remoteui.iforgot_recovery_verify_securityKey"
+ "com.apple.remoteui.iforgot_recovery_verify_securityKey_page"
+ "com.apple.remoteui.iforgot_recovery_verify_smscode"
+ "com.apple.remoteui.iforgot_recovery_verify_smscode_alert_1"
+ "com.apple.remoteui.iforgot_recovery_verify_smscode_cantuse"
+ "com.apple.remoteui.iforgot_recovery_verify_smscode_multiChoice_1"
+ "com.apple.remoteui.iforgot_recovery_verify_smscode_page"
+ "com.apple.remoteui.iforgot_recovery_verify_smscode_send"
+ "com.apple.remoteui.iforgot_recovery_verify_smscode_send_alert"
+ "com.apple.remoteui.iforgot_recovery_verify_smscode_send_button_1"
+ "com.apple.remoteui.iforgot_recovery_verify_smscode_send_footer_1"
+ "com.apple.remoteui.iforgot_recovery_verify_smscode_send_page"
+ "com.apple.remoteui.iforgot_recovery_verify_smscode_send_pinView_1"
+ "com.apple.remoteui.iforgot_request_password_reset"
+ "com.apple.remoteui.iforgot_request_questions_reset"
+ "com.apple.remoteui.iforgot_request_validate_custodianApprovalCode"
+ "com.apple.remoteui.iforgot_request_validate_custodian_startSession"
+ "com.apple.remoteui.iforgot_request_validate_custodian_startSession_htmlHeader_1"
+ "com.apple.remoteui.iforgot_request_validate_custodian_startSession_linkRow_1"
+ "com.apple.remoteui.iforgot_request_validate_custodian_startSession_linkRow_2"
+ "com.apple.remoteui.iforgot_request_validate_custodian_startSession_multiChoice_1"
+ "com.apple.remoteui.iforgot_request_validate_custodian_startSession_multiChoice_2"
+ "com.apple.remoteui.iforgot_request_validate_custodian_startSession_navigationBar_1"
+ "com.apple.remoteui.iforgot_request_validate_custodian_startSession_page"
+ "com.apple.remoteui.iforgot_request_validate_icloudsecuritycode"
+ "com.apple.remoteui.iforgot_request_validate_mk"
+ "com.apple.remoteui.iforgot_request_validate_securityKey"
+ "com.apple.remoteui.iforgot_session_timeout"
+ "com.apple.remoteui.iforgot_submit_account_reactivation"
+ "com.apple.remoteui.iforgot_unenrollment"
+ "com.apple.remoteui.iforgot_unenrollment_reset"
+ "com.apple.remoteui.iforgot_unenrollment_reset_signout"
+ "com.apple.remoteui.iforgot_unenrollment_verify_birthday"
+ "com.apple.remoteui.iforgot_unenrollment_verify_questions"
+ "com.apple.remoteui.iforgot_verify_smscode"
+ "com.apple.remoteui.iforgot_verify_smscode_send"
+ "continue"
+ "custodian:add"
+ "custodian:startApproval"
+ "custodian:startSession"
+ "custodian:verify"
+ "database:revoke"
+ "delete"
+ "edp:recoverytoken"
+ "emails:update"
+ "getAllowedElementIdentifiers"
+ "getAllowedHandlerKey"
+ "getAllowedHookName"
+ "icsc:verify"
+ "inheritance:show"
+ "mk-validation"
+ "open"
+ "passcode:validate"
+ "read"
+ "recovery:print"
+ "recoveryOptions:show"
+ "rk:disable"
+ "rk:enable"
+ "rk:regenerate"
+ "rk:verify"
+ "setCfuType:"
+ "start-icsc"
+ "teardown"
- "analyticsEventWithFollowUpContext:eventName:category:"
- "pendingCFUTypes"

```
