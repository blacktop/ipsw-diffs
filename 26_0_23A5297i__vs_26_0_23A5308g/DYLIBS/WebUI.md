## WebUI

> `/System/Library/PrivateFrameworks/WebUI.framework/WebUI`

```diff

-622.1.19.10.4
-  __TEXT.__text: 0x12eb4
-  __TEXT.__auth_stubs: 0x610
-  __TEXT.__objc_methlist: 0x11dc
+622.1.21.10.3
+  __TEXT.__text: 0x127d4
+  __TEXT.__auth_stubs: 0x5e0
+  __TEXT.__objc_methlist: 0x1140
   __TEXT.__const: 0x40
   __TEXT.__gcc_except_tab: 0x608
-  __TEXT.__cstring: 0x143b
-  __TEXT.__oslogstring: 0x5b4
+  __TEXT.__cstring: 0x1426
+  __TEXT.__oslogstring: 0x46c
   __TEXT.__ustring: 0x774
-  __TEXT.__unwind_info: 0x538
-  __TEXT.__objc_classname: 0x244
-  __TEXT.__objc_methname: 0x6800
-  __TEXT.__objc_methtype: 0x110b
-  __TEXT.__objc_stubs: 0x3c60
-  __DATA_CONST.__got: 0x418
+  __TEXT.__unwind_info: 0x530
+  __TEXT.__objc_classname: 0x1ec
+  __TEXT.__objc_methname: 0x64d7
+  __TEXT.__objc_methtype: 0xf63
+  __TEXT.__objc_stubs: 0x3b20
+  __DATA_CONST.__got: 0x3e8
   __DATA_CONST.__const: 0xcf8
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x48
+  __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1510
+  __DATA_CONST.__objc_selrefs: 0x1498
   __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x318
-  __AUTH_CONST.__const: 0x200
+  __AUTH_CONST.__auth_got: 0x300
+  __AUTH_CONST.__const: 0x1e0
   __AUTH_CONST.__cfstring: 0xdc0
-  __AUTH_CONST.__objc_const: 0x19c8
+  __AUTH_CONST.__objc_const: 0x1920
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_arrayobj: 0x60
-  __DATA.__objc_ivar: 0xfc
-  __DATA.__data: 0x370
+  __DATA.__objc_ivar: 0xf4
+  __DATA.__data: 0x2b0
   __DATA.__bss: 0x88
   __DATA_DIRTY.__objc_data: 0x460
-  __DATA_DIRTY.__bss: 0x50
+  __DATA_DIRTY.__bss: 0x40
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AuthenticationServices.framework/AuthenticationServices
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DA89F0B5-5A45-30F9-95D9-E270792FD8C1
-  Functions: 394
-  Symbols:   1876
-  CStrings:  1243
+  UUID: 41A1C184-F3D5-39F4-A6ED-34A1EDB319AF
+  Functions: 380
+  Symbols:   1814
+  CStrings:  1214
 
Symbols:
+ -[WBUFormAutoFillPrompt showAutoFillPromptForUsernameInWebView:url:title:message:suggestedUsername:password:isGeneratedPassword:completionHandler:].cold.1
+ -[WBUFormDataController webView:frame:willNavigateFromForm:inContext:bySubmitting:submissionHandler:]
+ -[WBUFormDataController webView:frame:willNavigateFromForm:inContext:bySubmitting:submissionHandler:].cold.1
+ -[WBUFormDataController webView:frame:willNavigateFromForm:inContext:bySubmitting:submissionHandler:].cold.2
+ ___block_literal_global.627
+ ___block_literal_global.648
+ _objc_msgSend$isBeingPresented
+ _objc_msgSend$presentingViewController
- -[WBUFormDataController _autoFillCorrectionManager]
- -[WBUFormDataController _processCorrectionsForFormWithDomain:formMetadata:uniqueIDsOfControlsThatWereAutoFilled:]
- -[WBUFormDataController _processCorrectionsForFormWithDomain:formMetadata:uniqueIDsOfControlsThatWereAutoFilled:].cold.1
- -[WBUFormDataController _processCorrectionsForFormWithDomain:formMetadata:uniqueIDsOfControlsThatWereAutoFilled:].cold.2
- -[WBUFormDataController _processCorrectionsForFormWithDomain:formMetadata:uniqueIDsOfControlsThatWereAutoFilled:].cold.3
- -[WBUFormDataController autoFillCorrectionManagerShouldProcessFeedback:]
- -[WBUFormDataController feedbackProcessorForAutoFillCorrectionManager:]
- -[WBUFormDataController formAutoFillCorrectionManagerForFormFieldClassificationCorrector:]
- -[WBUFormDataController formFieldClassificationCorrector:bestAddressBookLabelForControlValue:]
- -[WBUFormDataController formFieldClassificationCorrector:hasAddressBookDataForAddressBookLabel:]
- -[WBUFormDataController webView:frame:willNavigateFromForm:inContext:bySubmitting:processMetadataCorrections:uniqueIDsOfControlsThatWereAutoFilled:submissionHandler:]
- -[WBUFormDataController webView:frame:willNavigateFromForm:inContext:bySubmitting:processMetadataCorrections:uniqueIDsOfControlsThatWereAutoFilled:submissionHandler:].cold.1
- -[WBUFormDataController webView:frame:willNavigateFromForm:inContext:bySubmitting:processMetadataCorrections:uniqueIDsOfControlsThatWereAutoFilled:submissionHandler:].cold.2
- -[WBUFormDataController webView:frame:willNavigateFromForm:inContext:bySubmitting:processMetadataCorrections:uniqueIDsOfControlsThatWereAutoFilled:submissionHandler:].cold.3
- _DiagnosticLogSubmissionEnabled
- _OBJC_CLASS_$_WBSFormAutoFillCorrectionManager
- _OBJC_CLASS_$_WBSFormAutoFillCorrectionsSQLiteStore
- _OBJC_CLASS_$_WBSFormAutoFillParsecDomainPolicyProvider
- _OBJC_CLASS_$_WBSFormAutoFillParsecFeedbackProcessor
- _OBJC_CLASS_$_WBSFormFieldClassificationCorrector
- _OBJC_IVAR_$_WBUFormDataController._autoFillCorrectionManager
- _OBJC_IVAR_$_WBUFormDataController._autoFillFeedbackProcessor
- _OUTLINED_FUNCTION_1
- _WBSFormAnnotationContactIDKey
- _WBSSharedParsecGlobalFeedbackDispatcher
- _WBS_LOG_CHANNEL_PREFIXCrowdsourcedAutoFill
- _WBS_LOG_CHANNEL_PREFIXCrowdsourcedAutoFill.cold.1
- _WBS_LOG_CHANNEL_PREFIXCrowdsourcedAutoFill.log
- _WBS_LOG_CHANNEL_PREFIXCrowdsourcedAutoFill.onceToken
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_WBSFormAutoFillCorrectionManagerDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_WBSFormFieldClassificationCorrectorDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_WBSFormAutoFillCorrectionManagerDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_WBSFormFieldClassificationCorrectorDelegate
- __OBJC_$_PROTOCOL_REFS_WBSFormAutoFillCorrectionManagerDelegate
- __OBJC_$_PROTOCOL_REFS_WBSFormFieldClassificationCorrectorDelegate
- __OBJC_LABEL_PROTOCOL_$_WBSFormAutoFillCorrectionManagerDelegate
- __OBJC_LABEL_PROTOCOL_$_WBSFormFieldClassificationCorrectorDelegate
- __OBJC_PROTOCOL_$_WBSFormAutoFillCorrectionManagerDelegate
- __OBJC_PROTOCOL_$_WBSFormFieldClassificationCorrectorDelegate
- ___WBS_LOG_CHANNEL_PREFIXCrowdsourcedAutoFill_block_invoke
- ___block_literal_global.13
- ___block_literal_global.649
- ___block_literal_global.670
- _objc_msgSend$_autoFillCorrectionManager
- _objc_msgSend$_processCorrectionsForFormWithDomain:formMetadata:uniqueIDsOfControlsThatWereAutoFilled:
- _objc_msgSend$addressBookHasDataForLabel:
- _objc_msgSend$bestAddressBookLabelForFormMetadata:formControlValue:
- _objc_msgSend$fieldName
- _objc_msgSend$formMetadata
- _objc_msgSend$initWithCorrectionsStore:
- _objc_msgSend$initWithDomain:formMetadata:formValues:uniqueIDsOfControlsThatWereAutoFilled:
- _objc_msgSend$initWithFeedbackAllowList:
- _objc_msgSend$initWithGlobalFeedbackDispatcher:domainPolicyProvider:autoFillVersion:
- _objc_msgSend$processCorrections
- _objc_msgSend$standardStore
- _objc_opt_new
CStrings:
+ "B60@0:8@16@24@32@40B48@?52"
+ "Failed to present prompt for username."
+ "Form was submitted"
+ "Not handling form submission for AutoFill due to absence of form metadata"
+ "isBeingPresented"
+ "presentingViewController"
+ "webView:frame:willNavigateFromForm:inContext:bySubmitting:submissionHandler:"
- "@\"<WBSFormAutoFillFeedbackProcessor>\"24@0:8@\"WBSFormAutoFillCorrectionManager\"16"
- "@\"NSString\"32@0:8@\"WBSFormFieldClassificationCorrector\"16@\"NSString\"24"
- "@\"WBSFormAutoFillCorrectionManager\""
- "@\"WBSFormAutoFillCorrectionManager\"24@0:8@\"WBSFormFieldClassificationCorrector\"16"
- "@\"WBSFormAutoFillParsecFeedbackProcessor\""
- "B24@0:8@\"WBSFormAutoFillCorrectionManager\"16"
- "B32@0:8@\"WBSFormFieldClassificationCorrector\"16@\"NSString\"24"
- "B72@0:8@16@24@32@40B48B52@56@?64"
- "CrowdsourcedAutoFill"
- "Form was submitted; will consider whether to process AutoFill corrections"
- "Not processing AutoFill corrections since a contact card other than the Me card was used for AutoFill"
- "Not processing AutoFill corrections since no form controls were supplied"
- "Not requesting AutoFill correction processing due to absence of form metadata"
- "Processing AutoFill corrections for %lu controls"
- "WBSFormAutoFillCorrectionManagerDelegate"
- "WBSFormFieldClassificationCorrectorDelegate"
- "Will not process AutoFill corrections since correction processing was not requested"
- "_autoFillCorrectionManager"
- "_autoFillFeedbackProcessor"
- "_processCorrectionsForFormWithDomain:formMetadata:uniqueIDsOfControlsThatWereAutoFilled:"
- "addressBookHasDataForLabel:"
- "autoFillCorrectionManagerShouldProcessFeedback:"
- "bestAddressBookLabelForFormMetadata:formControlValue:"
- "feedbackProcessorForAutoFillCorrectionManager:"
- "fieldName"
- "formAutoFillCorrectionManagerForFormFieldClassificationCorrector:"
- "formFieldClassificationCorrector:bestAddressBookLabelForControlValue:"
- "formFieldClassificationCorrector:hasAddressBookDataForAddressBookLabel:"
- "formMetadata"
- "initWithCorrectionsStore:"
- "initWithDomain:formMetadata:formValues:uniqueIDsOfControlsThatWereAutoFilled:"
- "initWithFeedbackAllowList:"
- "initWithGlobalFeedbackDispatcher:domainPolicyProvider:autoFillVersion:"
- "processCorrections"
- "standardStore"
- "webView:frame:willNavigateFromForm:inContext:bySubmitting:processMetadataCorrections:uniqueIDsOfControlsThatWereAutoFilled:submissionHandler:"

```
