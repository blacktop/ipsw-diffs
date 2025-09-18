## AppleAccountUI

> `/System/Library/PrivateFrameworks/AppleAccountUI.framework/AppleAccountUI`

```diff

-494.4.9.0.0
-  __TEXT.__text: 0xb5510
+494.4.12.0.0
+  __TEXT.__text: 0xb7600
   __TEXT.__auth_stubs: 0x1bf0
-  __TEXT.__objc_methlist: 0x6f64
+  __TEXT.__objc_methlist: 0x705c
   __TEXT.__const: 0x1144
   __TEXT.__gcc_except_tab: 0xe78
-  __TEXT.__cstring: 0x4717
-  __TEXT.__oslogstring: 0x90b3
+  __TEXT.__cstring: 0x4a97
+  __TEXT.__oslogstring: 0x92d6
   __TEXT.__dlopen_cstrs: 0x387
   __TEXT.__ustring: 0x4
   __TEXT.__swift5_typeref: 0x16be

   __TEXT.__swift5_proto: 0x70
   __TEXT.__swift5_types: 0x8c
   __TEXT.__swift5_builtin: 0x50
-  __TEXT.__unwind_info: 0x2d7c
+  __TEXT.__unwind_info: 0x2dc4
   __TEXT.__eh_frame: 0x53c
-  __TEXT.__objc_classname: 0x1aa2
-  __TEXT.__objc_methname: 0x1622d
-  __TEXT.__objc_methtype: 0x42ef
-  __TEXT.__objc_stubs: 0x107e0
+  __TEXT.__objc_classname: 0x1ab3
+  __TEXT.__objc_methname: 0x165ab
+  __TEXT.__objc_methtype: 0x432b
+  __TEXT.__objc_stubs: 0x10a60
   __DATA_CONST.__got: 0x8c8
-  __DATA_CONST.__const: 0x23f8
-  __DATA_CONST.__objc_classlist: 0x548
+  __DATA_CONST.__const: 0x2498
+  __DATA_CONST.__objc_classlist: 0x550
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0x208
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x286d8
-  __DATA_CONST.__objc_selrefs: 0x50b8
+  __DATA_CONST.__objc_const: 0x28760
+  __DATA_CONST.__objc_selrefs: 0x5168
   __DATA_CONST.__objc_arraydata: 0xb8
-  __AUTH_CONST.__objc_const: 0x3a60
-  __AUTH_CONST.__cfstring: 0x3ce0
+  __AUTH_CONST.__objc_const: 0x3af0
+  __AUTH_CONST.__cfstring: 0x3f80
   __AUTH_CONST.__const: 0x1a68
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__auth_got: 0xe08
-  __AUTH.__objc_data: 0x3678
+  __AUTH.__objc_data: 0x36c8
   __AUTH.__data: 0x220
   __DATA.__objc_protorefs: 0x28
-  __DATA.__objc_classrefs: 0xb60
-  __DATA.__objc_superrefs: 0x398
-  __DATA.__objc_ivar: 0x994
+  __DATA.__objc_classrefs: 0xb88
+  __DATA.__objc_superrefs: 0x3a0
+  __DATA.__objc_ivar: 0x9a4
   __DATA.__data: 0x1f68
   __DATA.__bss: 0x11f0
   __DATA.__common: 0x280

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 6AE377B2-ADB0-3701-82A2-7FE9AC6ACF21
-  Functions: 4309
-  Symbols:   12533
-  CStrings:  6019
+  UUID: A8016E81-FF78-36CF-8BF7-64C4F4BF6FCC
+  Functions: 4366
+  Symbols:   12686
+  CStrings:  6100
 
Symbols:
+ +[AAUIDTOHelper _shouldAllowOpForRatchetState:]
+ -[AAUIAccountRecoveryViewController _displayCustodianAddNotAllowedAlert]
+ -[AAUIAccountRecoveryViewController _displayRatchetGenericErrorAlert]
+ -[AAUICDPStingrayRemoteUIController attachBiometricRatchetHandler:]
+ -[AAUICDPStingrayRemoteUIController attachDTOBiometryHandler:]
+ -[AAUIDTOHelper .cxx_destruct]
+ -[AAUIDTOHelper _makeOpNotAllowedAlertForAddCustodian:]
+ -[AAUIDTOHelper _makeOpNotAllowedAlertForAddCustodian:].cold.1
+ -[AAUIDTOHelper initWithDTOController:]
+ -[AAUIDTOHelper isDTOGatingEnabled]
+ -[AAUIDTOHelper makeCustodianAddOpNotAllowedAlert]
+ -[AAUIDTOHelper makeCustodianDeleteOpNotAllowedAlert]
+ -[AAUIDTOHelper makeGenericRatchetFailedAlert]
+ -[AAUIDTOHelper makeRatchetContextWithPresentationContext:DTOContextType:]
+ -[AAUIDTOHelper shouldAllowOpForContext:completion:]
+ -[AAUIDTOHelper shouldGateUsingRatchetForAltDSID:completion:]
+ -[AAUIMyCustodianActionHandler _displayCustodianDeleteNotAllowedAlert]
+ -[AAUIMyCustodianActionHandler _displayRatchetGenericErrorAlert]
+ -[AAUIRecoveryFactorController _displayCustodianAddNotAllowedAlert]
+ -[AAUIRecoveryFactorController _displayRatchetGenericErrorAlert]
+ -[AAUIRecoveryFactorController startAddingRecoveryContact].cold.1
+ GCC_except_table26
+ GCC_except_table27
+ GCC_except_table29
+ _OBJC_CLASS_$_AAUIDTOHelper
+ _OBJC_CLASS_$_AKBiometricRatchetController
+ _OBJC_CLASS_$_AKBiometricRatchetHook
+ _OBJC_CLASS_$_AKBiometricRatchetUIContext
+ _OBJC_CLASS_$_AKDTOBiometryHook
+ _OBJC_IVAR_$_AAUIAccountRecoveryViewController._dtoHelper
+ _OBJC_IVAR_$_AAUIDTOHelper._controller
+ _OBJC_IVAR_$_AAUIMyCustodianActionHandler._dtoHelper
+ _OBJC_IVAR_$_AAUIRecoveryFactorController._dtoHelper
+ _OBJC_METACLASS_$_AAUIDTOHelper
+ __OBJC_$_CLASS_METHODS_AAUIDTOHelper
+ __OBJC_$_INSTANCE_METHODS_AAUIDTOHelper
+ __OBJC_$_INSTANCE_VARIABLES_AAUIDTOHelper
+ __OBJC_CLASS_RO_$_AAUIDTOHelper
+ __OBJC_METACLASS_RO_$_AAUIDTOHelper
+ ___50-[AAUIMyCustodianActionHandler _doCustodianRemove]_block_invoke.33
+ ___52-[AAUIDTOHelper shouldAllowOpForContext:completion:]_block_invoke
+ ___52-[AAUIDTOHelper shouldAllowOpForContext:completion:]_block_invoke.cold.1
+ ___54-[AAUIAccountRecoveryViewController _showAddCustodian]_block_invoke
+ ___54-[AAUIAccountRecoveryViewController _showAddCustodian]_block_invoke.84
+ ___54-[AAUIAccountRecoveryViewController _showAddCustodian]_block_invoke.84.cold.1
+ ___54-[AAUIAccountRecoveryViewController _showAddCustodian]_block_invoke.85
+ ___54-[AAUIAccountRecoveryViewController _showAddCustodian]_block_invoke.86
+ ___54-[AAUIAccountRecoveryViewController _showAddCustodian]_block_invoke.86.cold.1
+ ___54-[AAUIAccountRecoveryViewController _showAddCustodian]_block_invoke.cold.1
+ ___54-[AAUIAccountRecoveryViewController _showAddCustodian]_block_invoke.cold.2
+ ___54-[AAUIAccountRecoveryViewController _showAddCustodian]_block_invoke_2
+ ___54-[AAUIAccountRecoveryViewController _showAddCustodian]_block_invoke_2.cold.1
+ ___58-[AAUIRecoveryFactorController startAddingRecoveryContact]_block_invoke
+ ___58-[AAUIRecoveryFactorController startAddingRecoveryContact]_block_invoke.23
+ ___58-[AAUIRecoveryFactorController startAddingRecoveryContact]_block_invoke.23.cold.1
+ ___58-[AAUIRecoveryFactorController startAddingRecoveryContact]_block_invoke.24
+ ___58-[AAUIRecoveryFactorController startAddingRecoveryContact]_block_invoke.27
+ ___58-[AAUIRecoveryFactorController startAddingRecoveryContact]_block_invoke.27.cold.1
+ ___58-[AAUIRecoveryFactorController startAddingRecoveryContact]_block_invoke.cold.1
+ ___58-[AAUIRecoveryFactorController startAddingRecoveryContact]_block_invoke.cold.2
+ ___58-[AAUIRecoveryFactorController startAddingRecoveryContact]_block_invoke_2
+ ___58-[AAUIRecoveryFactorController startAddingRecoveryContact]_block_invoke_2.cold.1
+ ___60-[AAUIAccountRecoveryViewController _fetchRecoveryKeyUpdate]_block_invoke.56
+ ___62-[AAUIMyCustodianActionHandler doDestructiveAction:specifier:]_block_invoke
+ ___62-[AAUIMyCustodianActionHandler doDestructiveAction:specifier:]_block_invoke.24
+ ___62-[AAUIMyCustodianActionHandler doDestructiveAction:specifier:]_block_invoke.24.cold.1
+ ___62-[AAUIMyCustodianActionHandler doDestructiveAction:specifier:]_block_invoke.25
+ ___62-[AAUIMyCustodianActionHandler doDestructiveAction:specifier:]_block_invoke.28
+ ___62-[AAUIMyCustodianActionHandler doDestructiveAction:specifier:]_block_invoke.28.cold.1
+ ___62-[AAUIMyCustodianActionHandler doDestructiveAction:specifier:]_block_invoke.cold.1
+ ___62-[AAUIMyCustodianActionHandler doDestructiveAction:specifier:]_block_invoke.cold.2
+ ___62-[AAUIMyCustodianActionHandler doDestructiveAction:specifier:]_block_invoke_2
+ ___62-[AAUIMyCustodianActionHandler doDestructiveAction:specifier:]_block_invoke_2.cold.1
+ ___63-[AAUIAccountRecoveryViewController _fetchAllCustodianContacts]_block_invoke.54
+ ___69-[AAUIAccountRecoveryViewController _syncTrustedContactsFromCloudKit]_block_invoke.44
+ ___74-[AAUIMyCustodianActionHandler _checkRecoveryContactAndRecoveryKeyStatus:]_block_invoke.41
+ ___79-[AAUIAccountRecoveryViewController _syncAccountRecoveryFactorsWithCompletion:]_block_invoke.57
+ ___79-[AAUIAccountRecoveryViewController _syncAccountRecoveryFactorsWithCompletion:]_block_invoke.57.cold.1
+ ___block_descriptor_40_e8_32bs_e46_v24?0"AKBiometricRatchetResult"8"NSError"16ls32l8
+ ___block_descriptor_64_e8_32s40s48s56s_e20_v20?0B8"NSError"12ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_e8_32s40s48s56s_e8_v12?0B8ls32l8s40l8s48l8s56l8
+ ___block_literal_global.45
+ _objc_msgSend$_displayCustodianAddNotAllowedAlert
+ _objc_msgSend$_displayCustodianDeleteNotAllowedAlert
+ _objc_msgSend$_makeOpNotAllowedAlertForAddCustodian:
+ _objc_msgSend$_shouldAllowOpForRatchetState:
+ _objc_msgSend$ak_isLAUserCancelError
+ _objc_msgSend$alertWithTitle:message:buttonTitle:
+ _objc_msgSend$armWithContext:completion:
+ _objc_msgSend$initWithDTOController:
+ _objc_msgSend$initWithReason:calloutReason:deeplinkURL:presentationContext:fallbackToNoAuth:useShortExpiration:beginRatchetTitle:beginRatchetBody:showsLocationWarning:countdownText:findMyErrorTitle:findMyErrorMessage:metaContext:
+ _objc_msgSend$isCriticalEditAllowedForAltDSID:completion:
+ _objc_msgSend$isDTOEnabled
+ _objc_msgSend$isDTOGatingEnabled
+ _objc_msgSend$makeCustodianAddOpNotAllowedAlert
+ _objc_msgSend$makeCustodianDeleteOpNotAllowedAlert
+ _objc_msgSend$makeGenericRatchetFailedAlert
+ _objc_msgSend$makeRatchetContextWithPresentationContext:DTOContextType:
+ _objc_msgSend$ratchetState
+ _objc_msgSend$rawState
+ _objc_msgSend$shouldAllowOpForContext:completion:
+ _objc_msgSend$shouldGateUsingRatchetForAltDSID:completion:
- GCC_except_table19
- ___50-[AAUIMyCustodianActionHandler _doCustodianRemove]_block_invoke.25
- ___60-[AAUIAccountRecoveryViewController _fetchRecoveryKeyUpdate]_block_invoke.54
- ___63-[AAUIAccountRecoveryViewController _fetchAllCustodianContacts]_block_invoke.52
- ___69-[AAUIAccountRecoveryViewController _syncTrustedContactsFromCloudKit]_block_invoke.42
- ___74-[AAUIMyCustodianActionHandler _checkRecoveryContactAndRecoveryKeyStatus:]_block_invoke.35
- ___79-[AAUIAccountRecoveryViewController _syncAccountRecoveryFactorsWithCompletion:]_block_invoke.55
- ___79-[AAUIAccountRecoveryViewController _syncAccountRecoveryFactorsWithCompletion:]_block_invoke.55.cold.1
- ___block_literal_global.38
CStrings:
+ "\x05\x11"
+ "\f\x11"
+ "@\"AAUIDTOHelper\""
+ "@\"AKBiometricRatchetController\""
+ "@20@0:8B16"
+ "AAUIDTOHelper"
+ "BIOMETRIC_RATCHET_BEGIN_RATCHET_BODY"
+ "BIOMETRIC_RATCHET_BEGIN_RATCHET_TITLE"
+ "BIOMETRIC_RATCHET_BEGIN_RATCHET_TITLE_ADD_RC"
+ "BIOMETRIC_RATCHET_BEGIN_RATCHET_TITLE_DELETE_RC"
+ "BIOMETRIC_RATCHET_CALLOUT_REASON"
+ "BIOMETRIC_RATCHET_CALLOUT_REASON_ADD"
+ "BIOMETRIC_RATCHET_CALLOUT_REASON_DELETE"
+ "BIOMETRIC_RATCHET_COUNTDOWN_TEXT"
+ "BIOMETRIC_RATCHET_COUNTDOWN_TEXT_ADD_RC"
+ "BIOMETRIC_RATCHET_COUNTDOWN_TEXT_DELETE_RC"
+ "BIOMETRIC_RATCHET_FALLBACK_TEXT"
+ "Calling armed ratchet error: %@"
+ "DTO disabled, proceeding with usual flow without auth"
+ "DTO enabled, IdMS says RC add is allowed, proceeding to ratchet auth"
+ "DTO enabled, IdMS says RC delete is allowed, proceeding to ratchet auth"
+ "IdMS says RC add is allowed on this device, proceeding to check if DTO is enabled"
+ "IdMS says RC add is not allowed on weak device, proceeding to show error alert"
+ "IdMS says RC delete is allowed on this device, proceeding to check if DTO is enabled"
+ "Localizable-DTO"
+ "RATCHET_RC_ADD_NOT_ALLOWED_ALERT_TITLE"
+ "RATCHET_RC_ADD_NOT_ALLOWED_MESSAGE"
+ "RATCHET_RC_DELETE_NOT_ALLOWED_ALERT_TITLE"
+ "RATCHET_RC_DELETE_NOT_ALLOWED_MESSAGE"
+ "RATCHET_RC_EDIT_GENERIC_RATCHET_FAILURE_ALERT_BUTTON"
+ "RATCHET_RC_EDIT_GENERIC_RATCHET_FAILURE_ALERT_DESCRIPTION"
+ "RATCHET_RC_EDIT_NOT_ALLOWED_ALERT_BUTTON"
+ "RATCHET_RC_EDIT_NOT_ALLOWED_ALERT_TITLE"
+ "Ratchet auth returned with success: %d, error: %@,"
+ "_controller"
+ "_displayCustodianAddNotAllowedAlert"
+ "_displayCustodianDeleteNotAllowedAlert"
+ "_displayRatchetGenericErrorAlert"
+ "_dtoHelper"
+ "_makeOpNotAllowedAlertForAddCustodian:"
+ "_shouldAllowOpForRatchetState:"
+ "ak_isLAUserCancelError"
+ "armWithContext:completion:"
+ "attachBiometricRatchetHandler:"
+ "attachDTOBiometryHandler:"
+ "initWithDTOController:"
+ "initWithReason:calloutReason:deeplinkURL:presentationContext:fallbackToNoAuth:useShortExpiration:beginRatchetTitle:beginRatchetBody:showsLocationWarning:countdownText:findMyErrorTitle:findMyErrorMessage:metaContext:"
+ "isCriticalEditAllowedForAltDSID:completion:"
+ "isDTOEnabled"
+ "isDTOGatingEnabled"
+ "makeCustodianAddOpNotAllowedAlert"
+ "makeCustodianDeleteOpNotAllowedAlert"
+ "makeGenericRatchetFailedAlert"
+ "makeRatchetContextWithPresentationContext:DTOContextType:"
+ "prefs:root=APPLE_ACCOUNT&aaaction=accountRecovery"
+ "r"
+ "ratchetState"
+ "rawState"
+ "shouldAllowOpForContext:completion:"
+ "shouldGateUsingRatchetForAltDSID:completion:"
+ "title: %@, message: %@"
+ "v24@?0@\"AKBiometricRatchetResult\"8@\"NSError\"16"
- "\v\x11"
- "b"

```
