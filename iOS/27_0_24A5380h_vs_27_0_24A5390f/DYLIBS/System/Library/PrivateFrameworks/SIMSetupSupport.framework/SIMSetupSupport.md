## SIMSetupSupport

> `/System/Library/PrivateFrameworks/SIMSetupSupport.framework/SIMSetupSupport`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__DATA.__data`

```diff

-964.0.0.0.0
-  __TEXT.__text: 0xe0d58
-  __TEXT.__objc_methlist: 0xc284
-  __TEXT.__const: 0x1f0
+968.0.0.0.0
+  __TEXT.__text: 0xe1ce4
+  __TEXT.__objc_methlist: 0xc354
+  __TEXT.__const: 0x1f8
   __TEXT.__gcc_except_tab: 0x20e8
-  __TEXT.__cstring: 0x172cc
-  __TEXT.__oslogstring: 0x8a8d
+  __TEXT.__cstring: 0x17485
+  __TEXT.__oslogstring: 0x8acb
   __TEXT.__dlopen_cstrs: 0x2be
   __TEXT.__ustring: 0xa
-  __TEXT.__unwind_info: 0x2f40
+  __TEXT.__unwind_info: 0x2f78
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x20e8
-  __DATA_CONST.__objc_classlist: 0x568
+  __DATA_CONST.__const: 0x2128
+  __DATA_CONST.__objc_classlist: 0x570
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5d98
+  __DATA_CONST.__objc_selrefs: 0x5de8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x508
+  __DATA_CONST.__objc_superrefs: 0x510
   __DATA_CONST.__objc_arraydata: 0x228
-  __DATA_CONST.__got: 0xbe0
+  __DATA_CONST.__got: 0xbe8
   __AUTH_CONST.__const: 0xba0
-  __AUTH_CONST.__cfstring: 0xa8c0
-  __AUTH_CONST.__objc_const: 0x4d458
+  __AUTH_CONST.__cfstring: 0xab40
+  __AUTH_CONST.__objc_const: 0x4da98
   __AUTH_CONST.__objc_intobj: 0x7e0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x35c0
-  __DATA.__objc_ivar: 0x12dc
+  __AUTH.__objc_data: 0x3570
+  __DATA.__objc_ivar: 0x12f8
   __DATA.__data: 0xc70
   __DATA.__bss: 0x178
-  __DATA_DIRTY.__objc_data: 0x50
+  __DATA_DIRTY.__objc_data: 0xf0
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/BridgePreferences.framework/BridgePreferences
   - /System/Library/PrivateFrameworks/CellularPlanManager.framework/CellularPlanManager
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CorePhoneNumbers.framework/CorePhoneNumbers
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4843
-  Symbols:   9889
-  CStrings:  3085
+  Functions: 4861
+  Symbols:   9935
+  CStrings:  3108
 
Symbols:
+ -[SSQuickSwitchSecondaryEnrollmentFlow _buildQSMetricPayload]
+ -[SSQuickSwitchSecondaryEnrollmentFlow flowCompleted:]
+ -[TSDeviceInfoViewController _continueTapped]
+ -[TSDeviceInfoViewController detailTextForSharingIdentitySupported:nalPresent:]
+ -[TSDeviceInfoViewController didConfirmSetup]
+ -[TSDeviceInfoViewController orderedInfoKeys]
+ -[TSESIMSetupConfirmationViewController .cxx_destruct]
+ -[TSESIMSetupConfirmationViewController _continueButtonTapped]
+ -[TSESIMSetupConfirmationViewController delegate]
+ -[TSESIMSetupConfirmationViewController init]
+ -[TSESIMSetupConfirmationViewController setDelegate:]
+ -[TSESIMSetupConfirmationViewController viewDidLoad]
+ -[TSESIMSetupConfirmationViewController(TSSetupFlowItem) prepare:]
+ -[TSIdentityShareFlow viewControllerDidComplete:]
+ -[TSPRXIdentityShareViewController setShareDeviceInfoInPurpleBuddy:]
+ -[TSPRXIdentityShareViewController shareDeviceInfoInPurpleBuddy]
+ _AnalyticsSendEventLazy
+ _CTPlanTransferStatusQSReverseProvisioningSkipped
+ _OBJC_CLASS_$_TSESIMSetupConfirmationViewController
+ _OBJC_IVAR_$_SSQuickSwitchSecondaryEnrollmentFlow._metricUserChoice
+ _OBJC_IVAR_$_TSDeviceInfoViewController._continueButton
+ _OBJC_IVAR_$_TSDeviceInfoViewController._deviceInfo
+ _OBJC_IVAR_$_TSDeviceInfoViewController._didConfirmSetup
+ _OBJC_IVAR_$_TSDeviceInfoViewController._showCarrierConfirmContinue
+ _OBJC_IVAR_$_TSESIMSetupConfirmationViewController._continueButton
+ _OBJC_IVAR_$_TSESIMSetupConfirmationViewController._delegate
+ _OBJC_IVAR_$_TSPRXIdentityShareViewController._shareDeviceInfoInPurpleBuddy
+ _OBJC_METACLASS_$_TSESIMSetupConfirmationViewController
+ _TSUserInfoNalKey
+ _TSUserInfoShareDeviceInfoInSetupKey
+ __OBJC_$_INSTANCE_METHODS_TSESIMSetupConfirmationViewController(TSSetupFlowItem)
+ __OBJC_$_INSTANCE_VARIABLES_TSESIMSetupConfirmationViewController
+ __OBJC_$_PROP_LIST_TSESIMSetupConfirmationViewController
+ __OBJC_CLASS_PROTOCOLS_$_TSESIMSetupConfirmationViewController
+ __OBJC_CLASS_RO_$_TSESIMSetupConfirmationViewController
+ __OBJC_METACLASS_RO_$_TSESIMSetupConfirmationViewController
+ ___54-[SSQuickSwitchSecondaryEnrollmentFlow flowCompleted:]_block_invoke
+ ___block_descriptor_40_e8_32s_e19_"NSDictionary"8?0ls32l8
+ _objc_msgSend$_buildQSMetricPayload
+ _objc_msgSend$bundleIdentifier
+ _objc_msgSend$detailTextForSharingIdentitySupported:nalPresent:
+ _objc_msgSend$didConfirmSetup
+ _objc_msgSend$getActivateForEsimSetupInBuddy:
+ _objc_msgSend$orderedInfoKeys
+ _objc_msgSend$retrieveDeviceIdentifier:clientBundleIdentifier:error:
+ _objc_msgSend$setShareDeviceInfoInPurpleBuddy:
+ _objc_msgSend$shareDeviceInfoInPurpleBuddy
- _OBJC_IVAR_$_TSDeviceInfoViewController._sortedInfo
CStrings:
+ "@\"NSDictionary\"8@?0"
+ "CTPlanTransferStatusQSReverseProvisioningSkipped"
+ "ESIM_IN_STORE_SIGNUP_NAL_BUTTON"
+ "ESIM_IN_STORE_SIGNUP_NAL_DETAIL"
+ "ESIM_SETUP_CONFIRM_DETAIL"
+ "ESIM_SETUP_CONFIRM_TITLE"
+ "NETWORK_ACCESS_IDENTIFIER_TITLE"
+ "NalKey"
+ "ShareDeviceInfoInSetupKey"
+ "[E]Failed to query activateForEsimSetupInBuddy: %@ @%s"
+ "[I] Updating plan info: CTPlanTransferStatusQSReverseProvisioningSkipped. Current VC: %@ @%s"
+ "cancelled"
+ "com.apple.Telephony.quickSwitchEnrollmentFlow"
+ "cross_platform"
+ "in_buddy"
+ "number_qs_already_enrolled"
+ "number_qs_capable_sims"
+ "other"
+ "proximity"
+ "quickswitch"
+ "scan"
+ "transfer"
+ "unknown"
+ "user_choice"
- "[I] Updating plan info: CTPlanTransferStatusTimeoutInstallOngoing. Current VC: %@ @%s"
```
