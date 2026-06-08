## RapportUI

> `/System/Library/PrivateFrameworks/RapportUI.framework/RapportUI`

```diff

-716.600.13.0.0
-  __TEXT.__text: 0x328c
-  __TEXT.__auth_stubs: 0x360
+740.100.2.0.0
+  __TEXT.__text: 0x2ba4
   __TEXT.__objc_methlist: 0xa14
   __TEXT.__const: 0x198
-  __TEXT.__cstring: 0x270
-  __TEXT.__unwind_info: 0x240
-  __TEXT.__objc_classname: 0xd5
-  __TEXT.__objc_methname: 0x14db
-  __TEXT.__objc_methtype: 0x2a7
-  __TEXT.__objc_stubs: 0x740
-  __DATA_CONST.__got: 0x88
+  __TEXT.__cstring: 0x27d
+  __TEXT.__unwind_info: 0x148
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x90
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x6b8
   __DATA_CONST.__objc_superrefs: 0x30
-  __AUTH_CONST.__auth_got: 0x1b8
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0x1e0
   __AUTH_CONST.__objc_const: 0x12b8
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x1e0
   __DATA.__objc_ivar: 0xc8
   __DATA.__data: 0x200

   - /System/Library/PrivateFrameworks/Rapport.framework/Rapport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2530D2F2-2700-3B1B-BCE4-1E3C5976F770
+  UUID: 6AC81C50-AEB9-3A6C-80B5-DA1A491E6CB1
   Functions: 160
-  Symbols:   581
-  CStrings:  412
+  Symbols:   576
+  CStrings:  42
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
- _objc_release_x2
- _objc_release_x25
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
- _objc_retain_x20
- _objc_retain_x21
- _objc_retain_x22
- _objc_retain_x23
Functions:
~ -[RPPairingManagerUIController init] : 100 -> 92
~ -[RPPairingManagerUIController setDispatchQueue:] : 64 -> 12
~ -[RPPairingManagerUIController setPresentingViewController:] : 64 -> 12
~ -[RPPairingUIController init] : 100 -> 92
~ -[RPPairingUIController setPresentingViewController:] : 64 -> 12
~ -[RPPairingUIController setDispatchQueue:] : 64 -> 12
~ -[RPPINEntryView awakeFromNib] : 584 -> 640
~ -[RPPINEntryView setDisabled:] : 16 -> 20
~ -[RPPINEntryView text] : 80 -> 84
~ -[RPPINEntryView touchesBegan:withEvent:] : 92 -> 96
~ -[RPPINEntryView _updateFields] : 828 -> 832
~ -[RPPINEntryView deleteBackward] : 184 -> 196
~ -[RPPINEntryView insertText:] : 480 -> 500
~ -[RPPINEntryView hasText] : 44 -> 48
~ -[RPPINEntryView keyboardType] : 32 -> 36
~ -[RPPINEntryView alphaNumeric] : 16 -> 20
~ -[RPPINEntryView setAlphaNumeric:] : 16 -> 20
~ -[RPPINEntryView disabled] : 16 -> 20
~ -[RPPINEntryView labels] : 16 -> 20
~ -[RPPINEntryView setLabels:] : 80 -> 20
~ -[RPPINEntryView label1] : 16 -> 20
~ -[RPPINEntryView setLabel1:] : 80 -> 20
~ -[RPPINEntryView label2] : 16 -> 20
~ -[RPPINEntryView setLabel2:] : 80 -> 20
~ -[RPPINEntryView label3] : 16 -> 20
~ -[RPPINEntryView setLabel3:] : 80 -> 20
~ -[RPPINEntryView label4] : 16 -> 20
~ -[RPPINEntryView setLabel4:] : 80 -> 20
~ -[RPPINEntryView label5] : 16 -> 20
~ -[RPPINEntryView setLabel5:] : 80 -> 20
~ -[RPPINEntryView label6] : 16 -> 20
~ -[RPPINEntryView setLabel6:] : 80 -> 20
~ -[RPPINEntryView label7] : 16 -> 20
~ -[RPPINEntryView setLabel7:] : 80 -> 20
~ -[RPPINEntryView label8] : 16 -> 20
~ -[RPPINEntryView setLabel8:] : 80 -> 20
~ -[RPPINEntryView textChangedHandler] : 16 -> 20
~ -[RPPINEntryView wells] : 16 -> 20
~ -[RPPINEntryView setWells:] : 80 -> 20
~ -[RPPINEntryView well1] : 16 -> 20
~ -[RPPINEntryView setWell1:] : 80 -> 20
~ -[RPPINEntryView well2] : 16 -> 20
~ -[RPPINEntryView setWell2:] : 80 -> 20
~ -[RPPINEntryView well3] : 16 -> 20
~ -[RPPINEntryView setWell3:] : 80 -> 20
~ -[RPPINEntryView well4] : 16 -> 20
~ -[RPPINEntryView setWell4:] : 80 -> 20
~ -[RPPINEntryView well5] : 16 -> 20
~ -[RPPINEntryView setWell5:] : 80 -> 20
~ -[RPPINEntryView well6] : 16 -> 20
~ -[RPPINEntryView setWell6:] : 80 -> 20
~ -[RPPINEntryView well7] : 16 -> 20
~ -[RPPINEntryView setWell7:] : 80 -> 20
~ -[RPPINEntryView well8] : 16 -> 20
~ -[RPPINEntryView setWell8:] : 80 -> 20
~ -[RPPINEntryView wellFocusColor] : 16 -> 20
~ -[RPPINEntryView setWellFocusColor:] : 80 -> 20
~ +[RPPairingPromptViewController instantiateViewController] : 168 -> 156
~ -[RPPairingPromptViewController viewWillAppear:] : 216 -> 220
~ ___48-[RPPairingPromptViewController viewWillAppear:]_block_invoke : 156 -> 148
~ -[RPPairingPromptViewController viewDidDisappear:] : 216 -> 232
~ -[RPPairingPromptViewController handlePINEntered:] : 232 -> 244
~ -[RPPairingPromptViewController updateWithFlags:throttleSeconds:] : 488 -> 508
~ -[RPPairingPromptViewController _retryTimer] : 284 -> 304
~ -[RPPairingPromptViewController dismissHandler] : 16 -> 20
~ -[RPPairingPromptViewController tryPasswordHandler] : 16 -> 20
~ -[RPPairingPromptViewController cancelButton] : 16 -> 20
~ -[RPPairingPromptViewController setCancelButton:] : 80 -> 20
~ -[RPPairingPromptViewController titleLabel] : 16 -> 20
~ -[RPPairingPromptViewController setTitleLabel:] : 80 -> 20
~ -[RPPairingPromptViewController subTitleLabel] : 16 -> 20
~ -[RPPairingPromptViewController setSubTitleLabel:] : 80 -> 20
~ -[RPPairingPromptViewController pinEntryView] : 16 -> 20
~ -[RPPairingPromptViewController setPinEntryView:] : 80 -> 20
~ -[RPPairingPromptViewController progressSpinner] : 16 -> 20
~ -[RPPairingPromptViewController setProgressSpinner:] : 80 -> 20
~ -[RPPairingPromptViewController progressLabel] : 16 -> 20
~ -[RPPairingPromptViewController setProgressLabel:] : 80 -> 20
~ +[RPPairingShowViewController instantiateViewController] : 168 -> 156
~ -[RPPairingShowViewController viewDidDisappear:] : 132 -> 128
~ -[RPPairingShowViewController _updatePasswordUI] : 612 -> 620
~ -[RPPairingShowViewController dismissHandler] : 16 -> 20
~ -[RPPairingShowViewController password] : 16 -> 20
~ -[RPPairingShowViewController cancelButton] : 16 -> 20
~ -[RPPairingShowViewController setCancelButton:] : 80 -> 20
~ -[RPPairingShowViewController titleLabel] : 16 -> 20
~ -[RPPairingShowViewController setTitleLabel:] : 80 -> 20
~ -[RPPairingShowViewController subTitleLabel] : 16 -> 20
~ -[RPPairingShowViewController setSubTitleLabel:] : 80 -> 20
~ -[RPPairingShowViewController verificationCodeLabel] : 16 -> 20
~ -[RPPairingShowViewController setVerificationCodeLabel:] : 80 -> 20
~ _RPUILocalizedString : 148 -> 132
~ ___RPUILocalizedString_block_invoke : 76 -> 72
~ _RPUILocalizedStringF : 68 -> 64
~ _RPUILocalizedStringV : 152 -> 136
~ -[UIView(RPUIViewExtensions) borderColor] : 84 -> 80
~ -[UIView(RPUIViewExtensions) setBorderColor:] : 112 -> 108
~ -[UIView(RPUIViewExtensions) borderWidth] : 76 -> 72
~ -[UIView(RPUIViewExtensions) setBorderWidth:] : 200 -> 188
~ -[UIView(RPUIViewExtensions) shadowUIColor] : 84 -> 80
~ -[UIView(RPUIViewExtensions) setShadowUIColor:] : 112 -> 108
~ _RPImageForDeviceModel : 564 -> 528
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"NSArray\""
- "@\"NSMutableString\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_dispatch_source>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"RPPINEntryView\""
- "@\"UIActivityIndicatorView\""
- "@\"UIButton\""
- "@\"UIColor\""
- "@\"UIConversationContext\"16@0:8"
- "@\"UILabel\""
- "@\"UITextInputPasswordRules\"16@0:8"
- "@\"UIView\""
- "@\"UIViewController\""
- "@16@0:8"
- "@24@0:8:16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "@?"
- "@?16@0:8"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "CGColor"
- "NSObject"
- "Q"
- "Q16@0:8"
- "RPHighlightButton"
- "RPPINEntryView"
- "RPPairingPromptViewController"
- "RPPairingShowViewController"
- "RPUIViewExtensions"
- "T#,R"
- "T@\"NSArray\",&,N,V_labels"
- "T@\"NSArray\",&,N,V_wells"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_dispatchQueue"
- "T@\"NSString\",?,C,N"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,N"
- "T@\"NSString\",C,N,V_password"
- "T@\"NSString\",C,N,V_serviceType"
- "T@\"NSString\",R,C"
- "T@\"RPPINEntryView\",&,N,V_pinEntryView"
- "T@\"UIActivityIndicatorView\",&,N,V_progressSpinner"
- "T@\"UIButton\",&,N,V_cancelButton"
- "T@\"UIColor\",&,N"
- "T@\"UIColor\",&,N,V_wellFocusColor"
- "T@\"UIConversationContext\",?,&,N"
- "T@\"UILabel\",&,N,V_label1"
- "T@\"UILabel\",&,N,V_label2"
- "T@\"UILabel\",&,N,V_label3"
- "T@\"UILabel\",&,N,V_label4"
- "T@\"UILabel\",&,N,V_label5"
- "T@\"UILabel\",&,N,V_label6"
- "T@\"UILabel\",&,N,V_label7"
- "T@\"UILabel\",&,N,V_label8"
- "T@\"UILabel\",&,N,V_progressLabel"
- "T@\"UILabel\",&,N,V_subTitleLabel"
- "T@\"UILabel\",&,N,V_titleLabel"
- "T@\"UILabel\",&,N,V_verificationCodeLabel"
- "T@\"UITextInputPasswordRules\",?,C,N"
- "T@\"UIView\",&,N,V_well1"
- "T@\"UIView\",&,N,V_well2"
- "T@\"UIView\",&,N,V_well3"
- "T@\"UIView\",&,N,V_well4"
- "T@\"UIView\",&,N,V_well5"
- "T@\"UIView\",&,N,V_well6"
- "T@\"UIView\",&,N,V_well7"
- "T@\"UIView\",&,N,V_well8"
- "T@\"UIViewController\",&,N,V_presentingViewController"
- "T@?,C,N,V_dismissHandler"
- "T@?,C,N,V_invalidationHandler"
- "T@?,C,N,V_retryHandler"
- "T@?,C,N,V_textChangedHandler"
- "T@?,C,N,V_tryPINHandler"
- "T@?,C,N,V_tryPasswordHandler"
- "TB,?,N"
- "TB,?,N,GisSecureTextEntry"
- "TB,N,V_allowManualIP"
- "TB,N,V_alphaNumeric"
- "TB,N,V_disabled"
- "TB,N,V_runInProcess"
- "TB,R,N"
- "TQ,?"
- "TQ,R"
- "Td,N"
- "Tq,?"
- "Tq,?,N"
- "UIKeyInput"
- "UITextInputTraits"
- "UTF8String"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_allowManualIP"
- "_alphaNumeric"
- "_cancelButton"
- "_cleanup"
- "_disabled"
- "_dismissHandler"
- "_dispatchQueue"
- "_invalidationHandler"
- "_label1"
- "_label2"
- "_label3"
- "_label4"
- "_label5"
- "_label6"
- "_label7"
- "_label8"
- "_labels"
- "_password"
- "_pinEntryView"
- "_presentingViewController"
- "_progressLabel"
- "_progressSpinner"
- "_retryDeadlineTicks"
- "_retryHandler"
- "_retryTimer"
- "_runInProcess"
- "_serviceType"
- "_subTitleLabel"
- "_text"
- "_textChangedHandler"
- "_titleLabel"
- "_tryPINHandler"
- "_tryPasswordHandler"
- "_updateFields"
- "_updatePasswordUI"
- "_verificationCodeLabel"
- "_well1"
- "_well2"
- "_well3"
- "_well4"
- "_well5"
- "_well6"
- "_well7"
- "_well8"
- "_wellFocusColor"
- "_wells"
- "activate"
- "addObject:"
- "allowManualIP"
- "allowedWritingToolsResultOptions"
- "allowsNumberPadPopover"
- "alphaNumeric"
- "appendFormat:"
- "autocapitalizationType"
- "autocorrectionType"
- "autorelease"
- "awakeFromNib"
- "becomeFirstResponder"
- "blackColor"
- "borderColor"
- "borderWidth"
- "bundleWithIdentifier:"
- "bundleWithURL:"
- "canBecomeFirstResponder"
- "cancelButton"
- "characterAtIndex:"
- "class"
- "colorWithCGColor:"
- "colorWithWhite:alpha:"
- "conformsToProtocol:"
- "conversationContext"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "d16@0:8"
- "debugDescription"
- "deleteBackward"
- "deleteCharactersInRange:"
- "description"
- "disabled"
- "dismissHandler"
- "dismissViewControllerAnimated:completion:"
- "dispatchQueue"
- "enablesReturnKeyAutomatically"
- "floatValue"
- "grayColor"
- "handleCancelButton:"
- "handlePINEntered:"
- "hasText"
- "hash"
- "imageWithContentsOfFile:"
- "init"
- "initWithFormat:"
- "initWithFormat:arguments:"
- "inlinePredictionType"
- "insertText:"
- "instantiateViewController"
- "instantiateViewControllerWithIdentifier:"
- "invalidate"
- "invalidationHandler"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isSecureTextEntry"
- "keyboardAppearance"
- "keyboardType"
- "label1"
- "label2"
- "label3"
- "label4"
- "label5"
- "label6"
- "label7"
- "label8"
- "labels"
- "layer"
- "length"
- "localizedStringForKey:value:table:"
- "mainScreen"
- "mathExpressionCompletionType"
- "mutableCopy"
- "navigationController"
- "numberWithDouble:"
- "objectForKeyedSubscript:"
- "pairingError:"
- "password"
- "passwordRules"
- "pathForResource:ofType:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "pinEntryView"
- "presentingViewController"
- "progressLabel"
- "progressSpinner"
- "promptWithFlags:throttleSeconds:"
- "q16@0:8"
- "rangeOfComposedCharacterSequenceAtIndex:"
- "release"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "retryHandler"
- "returnKeyType"
- "runInProcess"
- "scale"
- "secureTextEntry"
- "self"
- "serviceType"
- "setAllowManualIP:"
- "setAllowedWritingToolsResultOptions:"
- "setAllowsNumberPadPopover:"
- "setAlpha:"
- "setAlphaNumeric:"
- "setAutocapitalizationType:"
- "setAutocorrectionType:"
- "setBorderColor:"
- "setBorderWidth:"
- "setCancelButton:"
- "setConversationContext:"
- "setDisabled:"
- "setDismissHandler:"
- "setDispatchQueue:"
- "setEnablesReturnKeyAutomatically:"
- "setHidden:"
- "setHighlighted:"
- "setInlinePredictionType:"
- "setInvalidationHandler:"
- "setKeyboardAppearance:"
- "setKeyboardType:"
- "setLabel1:"
- "setLabel2:"
- "setLabel3:"
- "setLabel4:"
- "setLabel5:"
- "setLabel6:"
- "setLabel7:"
- "setLabel8:"
- "setLabels:"
- "setMathExpressionCompletionType:"
- "setPassword:"
- "setPasswordRules:"
- "setPinEntryView:"
- "setPresentingViewController:"
- "setProgressLabel:"
- "setProgressSpinner:"
- "setRetryHandler:"
- "setReturnKeyType:"
- "setRunInProcess:"
- "setSecureTextEntry:"
- "setServiceType:"
- "setShadowColor:"
- "setShadowUIColor:"
- "setSmartDashesType:"
- "setSmartInsertDeleteType:"
- "setSmartQuotesType:"
- "setSpellCheckingType:"
- "setSubTitleLabel:"
- "setText:"
- "setTextChangedHandler:"
- "setTextColor:"
- "setTextContentType:"
- "setTitleLabel:"
- "setTryPINHandler:"
- "setTryPasswordHandler:"
- "setVerificationCodeLabel:"
- "setWell1:"
- "setWell2:"
- "setWell3:"
- "setWell4:"
- "setWell5:"
- "setWell6:"
- "setWell7:"
- "setWell8:"
- "setWellFocusColor:"
- "setWells:"
- "setWritingToolsBehavior:"
- "shadowColor"
- "shadowUIColor"
- "smartDashesType"
- "smartInsertDeleteType"
- "smartQuotesType"
- "spellCheckingType"
- "startAnimating"
- "stopAnimating"
- "storyboardWithName:bundle:"
- "subTitleLabel"
- "substringWithRange:"
- "superclass"
- "systemGrayColor"
- "systemRedColor"
- "text"
- "textChangedHandler"
- "textContentType"
- "titleLabel"
- "touchesBegan:withEvent:"
- "tryPINHandler"
- "tryPasswordHandler"
- "updateWithFlags:throttleSeconds:"
- "uppercaseString"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@\"UIConversationContext\"16"
- "v24@0:8@\"UITextInputPasswordRules\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8I16i20"
- "v24@0:8Q16"
- "v24@0:8d16"
- "v24@0:8q16"
- "v32@0:8@16@24"
- "verificationCodeLabel"
- "view"
- "viewDidDisappear:"
- "viewWillAppear:"
- "well1"
- "well2"
- "well3"
- "well4"
- "well5"
- "well6"
- "well7"
- "well8"
- "wellFocusColor"
- "wells"
- "writingToolsBehavior"
- "zone"

```
