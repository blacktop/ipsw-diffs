## IdentityLookupUI

> `/System/Library/Frameworks/IdentityLookupUI.framework/IdentityLookupUI`

```diff

-1367.600.1.0.0
-  __TEXT.__text: 0x3e34
-  __TEXT.__auth_stubs: 0x2d0
+139.100.27.2.9
+  __TEXT.__text: 0x3700
   __TEXT.__objc_methlist: 0x5bc
   __TEXT.__const: 0x78
-  __TEXT.__gcc_except_tab: 0x6c
-  __TEXT.__cstring: 0x444
+  __TEXT.__gcc_except_tab: 0x30
+  __TEXT.__cstring: 0x44c
   __TEXT.__oslogstring: 0x473
-  __TEXT.__unwind_info: 0x1d8
-  __TEXT.__objc_classname: 0x1ec
-  __TEXT.__objc_methname: 0x13c4
-  __TEXT.__objc_methtype: 0x480
-  __TEXT.__objc_stubs: 0xdc0
-  __DATA_CONST.__got: 0xb8
+  __TEXT.__unwind_info: 0x180
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x250
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x4a0
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x178
+  __DATA_CONST.__got: 0xb8
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0x2e0
   __AUTH_CONST.__objc_const: 0xaf8
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x1e0
   __DATA.__objc_ivar: 0x54
   __DATA.__data: 0x240

   - /usr/lib/libBASupport.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6F9960DE-1FA3-389B-BE8D-BB0DCBD4CFF2
-  Functions: 122
-  Symbols:   557
-  CStrings:  343
+  UUID: C2D588AF-4AB6-3484-9620-61F5888C25FB
+  Functions: 117
+  Symbols:   554
+  CStrings:  83
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x24
+ _objc_retain_x25
+ _objc_retain_x3
+ _objc_retain_x8
- GCC_except_table15
- _OUTLINED_FUNCTION_2
- _OUTLINED_FUNCTION_3
- _objc_retainAutoreleasedReturnValue
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"<ILClassificationExtensionShellViewControllerDelegate>\""
- "@\"<ILClassificationUIExtensionHostContextDelegate>\""
- "@\"<ILClassificationUIExtensionHostViewControllerDelegate>\""
- "@\"<NSCopying>\""
- "@\"ILClassificationExtensionShellViewController\""
- "@\"ILClassificationReportingController\""
- "@\"ILClassificationRequest\""
- "@\"ILClassificationResponse\""
- "@\"ILClassificationUIExtensionHostContext\""
- "@\"NSExtension\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"UIBarButtonItem\""
- "@\"UINavigationController\""
- "@\"UIViewController\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8@?16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@?"
- "@?16@0:8"
- "Attributes"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "ILClassificationExtensionShellViewController"
- "ILClassificationExtensionShellViewControllerDelegate"
- "ILClassificationReportingController"
- "ILClassificationUIExtensionContext"
- "ILClassificationUIExtensionHostContext"
- "ILClassificationUIExtensionHostContextDelegate"
- "ILClassificationUIExtensionHostProtocol"
- "ILClassificationUIExtensionVendorProtocol"
- "ILClassificationUIExtensionViewController"
- "MFMessageComposeViewControllerDelegate"
- "NSObject"
- "Q16@0:8"
- "SMSReportDestination"
- "T#,R"
- "T@\"<ILClassificationExtensionShellViewControllerDelegate>\",W,N,V_delegate"
- "T@\"<ILClassificationUIExtensionHostContextDelegate>\",W,N,V_delegate"
- "T@\"<ILClassificationUIExtensionHostViewControllerDelegate>\",W,N,V_delegate"
- "T@\"<NSCopying>\",&,N,V_extensionRequestIdentifier"
- "T@\"ILClassificationExtensionShellViewController\",&,N,V_shellViewController"
- "T@\"ILClassificationReportingController\",R,N,V_reportingController"
- "T@\"ILClassificationRequest\",R,N,V_classificationRequest"
- "T@\"ILClassificationResponse\",&,N,V_classificationResponse"
- "T@\"ILClassificationUIExtensionContext\",R,D,N"
- "T@\"ILClassificationUIExtensionHostContext\",&,N,V_extensionHostContext"
- "T@\"NSExtension\",&,N,V_extension"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_delegateQueue"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_queue"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,N,V_isoCountryCode"
- "T@\"NSString\",C,N,V_sender"
- "T@\"NSString\",R,C"
- "T@\"UIBarButtonItem\",&,N,V_doneButton"
- "T@\"UINavigationController\",&,N,V_navigationController"
- "T@\"UIViewController\",&,N,V_extensionViewController"
- "T@\"UIViewController\",R,W,N,V_hostViewController"
- "T@?,C,N,V_completion"
- "TB,N,GisReadyForClassificationResponse,V_readyForClassificationResponse"
- "TB,N,V_enableFinishOption"
- "TQ,R"
- "URLWithString:"
- "Vv16@0:8"
- "Vv20@0:8B16"
- "Vv24@0:8@\"ILClassificationRequest\"16"
- "Vv24@0:8@16"
- "Vv32@0:8@\"ILClassificationRequest\"16@?<v@?@\"ILClassificationResponse\"@\"NSError\">24"
- "Vv32@0:8@16@?24"
- "^{_NSZone=}16@0:8"
- "_auxiliaryConnection"
- "_classificationRequest"
- "_classificationResponse"
- "_completion"
- "_delegate"
- "_delegateQueue"
- "_doneButton"
- "_enableFinishOption"
- "_extension"
- "_extensionAuxiliaryHostProtocol"
- "_extensionAuxiliaryVendorProtocol"
- "_extensionContextForUUID:"
- "_extensionHostContext"
- "_extensionRequestIdentifier"
- "_extensionViewController"
- "_hostViewController"
- "_isoCountryCode"
- "_navigationController"
- "_plugIn"
- "_principalObject"
- "_queue"
- "_readyForClassificationResponse"
- "_reportingController"
- "_sender"
- "_shellViewController"
- "action"
- "actionWithTitle:style:handler:"
- "activateExtensionWithCompletion:"
- "activateWithCompletion:"
- "addAction:"
- "addChildViewController:"
- "addSubview:"
- "alertControllerWithTitle:message:preferredStyle:"
- "arrayWithObjects:count:"
- "attributes"
- "autorelease"
- "blockNumber:withCountryCode:"
- "bundleForClass:"
- "cancelExtensionRequestWithIdentifier:"
- "class"
- "classificationRequest"
- "classificationResponse"
- "classificationResponseForRequest:"
- "classificationResponseForRequest:completion:"
- "completion"
- "conformsToProtocol:"
- "context:didBecomeReadyForClassificationResponse:"
- "controller:didCompleteClassificationRequest:withResponse:"
- "debugDescription"
- "defaultWorkspace"
- "delegate"
- "delegateQueue"
- "description"
- "dictionaryWithObjects:forKeys:count:"
- "didCompleteClassificationRequestWithResponse:"
- "didMoveToParentViewController:"
- "dismissViewControllerAnimated:completion:"
- "displayExtensionViewController:forExtension:"
- "doneButton"
- "enableFinishOption"
- "errorWithDomain:code:userInfo:"
- "extension"
- "extensionContext"
- "extensionHostContext"
- "extensionRequestIdentifier"
- "extensionViewController"
- "finish"
- "frame"
- "hash"
- "hostViewController"
- "identifier"
- "il_classificationUIExtensionHostInterface"
- "il_classificationUIExtensionVendorInterface"
- "init"
- "initUnactivatedVCWithRequest:sender:isoCountryCode:"
- "initWithBarButtonSystemItem:target:action:"
- "initWithClassificationAction:"
- "initWithClassificationRequest:sender:isoCountryCode:"
- "initWithExtensionIdentifier:jsonDictionary:"
- "initWithHostViewController:"
- "initWithNibName:bundle:"
- "initWithRootViewController:"
- "instantiateViewControllerWithInputItems:connectionHandler:"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isReadyForClassificationResponse"
- "isoCountryCode"
- "launchSettings"
- "length"
- "localizedContainingName"
- "localizedStringForKey:value:table:"
- "logErrorWithMessage:"
- "messageComposeViewController:didFinishWithResult:"
- "navigationController"
- "navigationItem"
- "networkReportDestination"
- "objectForKeyedSubscript:"
- "openSensitiveURL:withOptions:error:"
- "performClassificationReportRequest:completion:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "phoneNumberWithDigits:countryCode:"
- "prepareForClassificationRequest:"
- "presentBlockAlertWithCompletion:"
- "presentViewController:animated:completion:"
- "presentedViewController"
- "queue"
- "readyForClassificationResponse"
- "release"
- "remoteObjectProxyWithErrorHandler:"
- "reportResponse:forExtension:withCompletion:"
- "reportResponseViaNetwork:forExtension:withCompletion:"
- "reportResponseViaSMS:forExtension:withCompletion:"
- "reportingController"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "sender"
- "setBackgroundColor:"
- "setBlockIncomingCommunication:forPhoneNumber:"
- "setBody:"
- "setClassificationResponse:"
- "setCompletion:"
- "setDelegate:"
- "setDelegate:queue:"
- "setDelegateQueue:"
- "setDoneButton:"
- "setEnableFinishOption:"
- "setEnabled:"
- "setExtension:"
- "setExtensionHostContext:"
- "setExtensionRequestIdentifier:"
- "setExtensionViewController:"
- "setFrame:"
- "setIsoCountryCode:"
- "setLeftBarButtonItem:"
- "setMessageComposeDelegate:"
- "setNavigationController:"
- "setReadyForClassificationResponse:"
- "setRecipients:"
- "setRequestInterruptionBlock:"
- "setRightBarButtonItem:"
- "setSender:"
- "setShellViewController:"
- "setTitle:"
- "sharedInstance"
- "sharedPrivacyManager"
- "shellViewController"
- "stringWithFormat:"
- "superclass"
- "userDidCancel"
- "userDidCancelForExtensionShellViewController:"
- "userDidFinish"
- "userDidFinishForExtensionShellViewController:"
- "userInfo"
- "userString"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"ILClassificationExtensionShellViewController\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v28@0:8@\"ILClassificationUIExtensionHostContext\"16B24"
- "v28@0:8@16B24"
- "v32@0:8@\"MFMessageComposeViewController\"16q24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8@16q24"
- "v40@0:8@16@24@?32"
- "view"
- "viewController"
- "viewDidDisappear:"
- "viewDidLoad"
- "whiteColor"
- "zone"

```
