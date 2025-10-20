## AuthKit

> `/System/Library/PrivateFrameworks/AuthKit.framework/AuthKit`

```diff

-525.126.5.1.0
-  __TEXT.__text: 0x176c74
+525.127.1.0.0
+  __TEXT.__text: 0x178b94
   __TEXT.__auth_stubs: 0xbc0
-  __TEXT.__objc_methlist: 0xda2c
+  __TEXT.__objc_methlist: 0xdac4
   __TEXT.__const: 0x69c8
-  __TEXT.__cstring: 0xf208
-  __TEXT.__oslogstring: 0x1189f
-  __TEXT.__gcc_except_tab: 0x9ab8
+  __TEXT.__cstring: 0xf57f
+  __TEXT.__oslogstring: 0x118e3
+  __TEXT.__gcc_except_tab: 0x9ae8
   __TEXT.__dlopen_cstrs: 0x305
-  __TEXT.__ustring: 0x1b8
-  __TEXT.__unwind_info: 0x4008
+  __TEXT.__ustring: 0x300
+  __TEXT.__unwind_info: 0x4050
   __TEXT.__objc_classname: 0x1c33
-  __TEXT.__objc_methname: 0x21ee3
+  __TEXT.__objc_methname: 0x220ca
   __TEXT.__objc_methtype: 0x4655
-  __TEXT.__objc_stubs: 0xf620
+  __TEXT.__objc_stubs: 0xf760
   __DATA_CONST.__got: 0xa38
-  __DATA_CONST.__const: 0xa018
+  __DATA_CONST.__const: 0xa048
   __DATA_CONST.__objc_classlist: 0x628
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x208
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6f08
+  __DATA_CONST.__objc_selrefs: 0x6f68
   __DATA_CONST.__objc_protorefs: 0xe0
   __DATA_CONST.__objc_superrefs: 0x3e0
-  __DATA_CONST.__objc_arraydata: 0x2c8
+  __DATA_CONST.__objc_arraydata: 0x2e8
   __AUTH_CONST.__auth_got: 0x5f0
   __AUTH_CONST.__const: 0x1320
-  __AUTH_CONST.__cfstring: 0xf820
-  __AUTH_CONST.__objc_const: 0x25240
-  __AUTH_CONST.__objc_intobj: 0x2d0
+  __AUTH_CONST.__cfstring: 0xfc80
+  __AUTH_CONST.__objc_const: 0x25270
+  __AUTH_CONST.__objc_intobj: 0x2e8
   __AUTH_CONST.__objc_arrayobj: 0x78
-  __AUTH_CONST.__objc_dictobj: 0x3e8
+  __AUTH_CONST.__objc_dictobj: 0x410
   __AUTH.__objc_data: 0x28a0
-  __DATA.__objc_ivar: 0xfc8
+  __DATA.__objc_ivar: 0xfcc
   __DATA.__data: 0x1900
-  __DATA.__bss: 0x6c8
+  __DATA.__bss: 0x6e0
   __DATA_DIRTY.__objc_data: 0x14f0
   __DATA_DIRTY.__bss: 0x2a0
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 38453A32-C120-3DA1-96CD-796906018EF2
-  Functions: 5306
-  Symbols:   20165
-  CStrings:  11655
+  UUID: 96E286F0-321F-31A7-BBE8-FA02393C8423
+  Functions: 5327
+  Symbols:   20229
+  CStrings:  11741
 
Symbols:
+ -[AKAccountRecoveryStepChangePassword _findConfirmRowIDForNewPasswordRowID:editableTextRows:]
+ -[AKAccountRecoveryStepChangePassword _getPasswordFieldMappingFromResponse:editableTextRows:]
+ -[AKAccountRecoveryStepChangePassword _isAuthenticationFailureForData:]
+ -[AKAccountRecoveryStepChangePassword _isConfirmationField:]
+ -[AKAccountRecoveryStepChangePassword _isIncorrectCurrentPasswordErrorForData:]
+ -[AKAccountRecoveryStepChangePassword _tryClientInfoMappingFromResponse:editableTextRows:]
+ -[AKAccountRecoveryStepChangePassword _tryPositionalMappingFromEditableTextRows:]
+ -[AKAccountRecoveryStepSMSVerificationCode _isSMSVerificationErrorForData:]
+ -[AKAccountRecoveryStepSMSVerificationCode _isValidSMSCodeFormat:]
+ -[AKAccountRecoveryStepSMSVerificationCode _verifySMSCodeWithData:model:response:completion:]
+ -[AKAppleIDAuthenticationCommandLineContext currentPassword]
+ -[AKAppleIDAuthenticationCommandLineContext setCurrentPassword:]
+ -[AKDevice healUCRTWithUsername:passwordPET:]
+ GCC_except_table139
+ GCC_except_table144
+ _AKBAAExclusionProcessBagConfigKey
+ _AKBAAExclusionVIPsBagConfigKey
+ _AKBAAOnlyAllowedProcessBagConfigKey
+ _AKBAAOnlyAllowedVIPsBagConfigKey
+ _AKUserInfoADPBlockModeUnenrollContextKey
+ _OBJC_IVAR_$_AKAppleIDAuthenticationCommandLineContext._currentPassword
+ _SMAEReissueUCRTWithError
+ ___73-[AKAppleIDSession _generateAppleIDHeadersForSessionTask:withCompletion:]_block_invoke.70
+ ___73-[AKAppleIDSession _generateAppleIDHeadersForSessionTask:withCompletion:]_block_invoke.71
+ ___73-[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:]_block_invoke.85
+ ___73-[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:]_block_invoke.86
+ ___83-[AKAppleIDSession URLSession:task:getAppleIDHeadersForResponse:completionHandler:]_block_invoke.62
+ ___83-[AKAppleIDSession URLSession:task:getAppleIDHeadersForResponse:completionHandler:]_block_invoke.63
+ ___91-[AKAppleIDSession _handleAnisetteReprovisionWithRequestURL:anisetteController:completion:]_block_invoke.92
+ ___92-[AKAppleIDSession URLSession:task:getAppleIDRequestOrHeadersForResponse:completionHandler:]_block_invoke.58
+ ___92-[AKAppleIDSession URLSession:task:getAppleIDRequestOrHeadersForResponse:completionHandler:]_block_invoke.59
+ ___93-[AKAccountRecoveryStepSMSVerificationCode _verifySMSCodeWithData:model:response:completion:]_block_invoke
+ ___block_literal_global.100
+ ___block_literal_global.88
+ ___getMAEReissueUCRTWithErrorSymbolLoc_block_invoke
+ ___getkMAOptionsActivationLockPETSymbolLoc_block_invoke
+ ___getkMAOptionsActivationLockUsernameSymbolLoc_block_invoke
+ _getMAEReissueUCRTWithErrorSymbolLoc
+ _getMAEReissueUCRTWithErrorSymbolLoc.ptr
+ _getkMAOptionsActivationLockPET
+ _getkMAOptionsActivationLockPETSymbolLoc
+ _getkMAOptionsActivationLockPETSymbolLoc.ptr
+ _getkMAOptionsActivationLockUsername
+ _getkMAOptionsActivationLockUsernameSymbolLoc
+ _getkMAOptionsActivationLockUsernameSymbolLoc.ptr
+ _objc_msgSend$_findConfirmRowIDForNewPasswordRowID:editableTextRows:
+ _objc_msgSend$_getPasswordFieldMappingFromResponse:editableTextRows:
+ _objc_msgSend$_isAuthenticationFailureForData:
+ _objc_msgSend$_isConfirmationField:
+ _objc_msgSend$_isIncorrectCurrentPasswordErrorForData:
+ _objc_msgSend$_isSMSVerificationErrorForData:
+ _objc_msgSend$_isValidSMSCodeFormat:
+ _objc_msgSend$_tryClientInfoMappingFromResponse:editableTextRows:
+ _objc_msgSend$_tryPositionalMappingFromEditableTextRows:
+ _objc_msgSend$_verifySMSCodeWithData:model:response:completion:
+ _objc_msgSend$currentPassword
- -[AKAccountRecoveryStepSMSVerificationCode _verifySMSCodeWithData:model:completion:]
- GCC_except_table135
- GCC_except_table140
- ___73-[AKAppleIDSession _generateAppleIDHeadersForSessionTask:withCompletion:]_block_invoke.68
- ___73-[AKAppleIDSession _generateAppleIDHeadersForSessionTask:withCompletion:]_block_invoke.69
- ___73-[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:]_block_invoke.80
- ___73-[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:]_block_invoke.83
- ___83-[AKAppleIDSession URLSession:task:getAppleIDHeadersForResponse:completionHandler:]_block_invoke.60
- ___83-[AKAppleIDSession URLSession:task:getAppleIDHeadersForResponse:completionHandler:]_block_invoke.61
- ___84-[AKAccountRecoveryStepSMSVerificationCode _verifySMSCodeWithData:model:completion:]_block_invoke
- ___91-[AKAppleIDSession _handleAnisetteReprovisionWithRequestURL:anisetteController:completion:]_block_invoke.90
- ___92-[AKAppleIDSession URLSession:task:getAppleIDRequestOrHeadersForResponse:completionHandler:]_block_invoke.56
- ___92-[AKAppleIDSession URLSession:task:getAppleIDRequestOrHeadersForResponse:completionHandler:]_block_invoke.57
- ___block_literal_global.86
- ___block_literal_global.98
- _objc_msgSend$_verifySMSCodeWithData:model:completion:
CStrings:
+ "\x05' "
+ "Authentication failed. Please check your credentials and try again."
+ "Confirm"
+ "Error during reissue of UCRT. Error: %@"
+ "Invalid code format. Please enter a 6-digit verification code"
+ "L' "
+ "MAEReissueUCRTWithError"
+ "Missing required elements (pinViews: %lu, serverInfo: %lu)"
+ "Password change failed: insufficient password fields in server response"
+ "Password change failed: unsupported server UI format"
+ "Password change request failed: %@"
+ "Retype"
+ "SMS verification failed: %@"
+ "SMS verification failed: invalid request configuration"
+ "SMS verification failed: unexpected server response format"
+ "SMS verification failed: unsupported server response format"
+ "T@\"NSString\",C,N,V_currentPassword"
+ "UCRT was successfully reissued - %@"
+ "Unsupported pinView format '%@'"
+ "^[0-9]{6}$"
+ "_currentPassword"
+ "_findConfirmRowIDForNewPasswordRowID:editableTextRows:"
+ "_getPasswordFieldMappingFromResponse:editableTextRows:"
+ "_isAuthenticationFailureForData:"
+ "_isConfirmationField:"
+ "_isIncorrectCurrentPasswordErrorForData:"
+ "_isSMSVerificationErrorForData:"
+ "_isValidSMSCodeFormat:"
+ "_tryClientInfoMappingFromResponse:editableTextRows:"
+ "_tryPositionalMappingFromEditableTextRows:"
+ "_verifySMSCodeWithData:model:response:completion:"
+ "authentication failed"
+ "baa-exclusion-process"
+ "baa-exclusion-vip"
+ "baa-only-allowed-process"
+ "baa-only-allowed-vip"
+ "confirm"
+ "confirmRowId"
+ "current password"
+ "currentPassword"
+ "failed"
+ "healUCRTWithUsername:passwordPET:"
+ "incorrect"
+ "invalid"
+ "kMAOptionsActivationLockPET"
+ "kMAOptionsActivationLockUsername"
+ "newPassword.confirmedPassword"
+ "newPassword.password"
+ "newPasswordRowId"
+ "nil"
+ "placeholder"
+ "setCurrentPassword:"
+ "two-factor authentication"
+ "unEnrollContext"
+ "unable to verify"
+ "verification"
+ "verification failed"
+ "wrong"
- "Failed change password step with unexpected data"
- "Failed sms verification step with unexpected data"
- "Failed to change password. Error - %@"
- "Password changed successfully."
- "_verifySMSCodeWithData:model:completion:"
- "adpUserInfo"

```
