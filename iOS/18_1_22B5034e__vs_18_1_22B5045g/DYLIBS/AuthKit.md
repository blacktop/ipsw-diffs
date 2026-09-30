## AuthKit

> `/System/Library/PrivateFrameworks/AuthKit.framework/AuthKit`

```diff

-491.1.0.0.0
-  __TEXT.__text: 0xc5a1c
+493.100.2.0.0
+  __TEXT.__text: 0xc8118
   __TEXT.__auth_stubs: 0xd70
-  __TEXT.__objc_methlist: 0xad50
+  __TEXT.__objc_methlist: 0xafc8
   __TEXT.__const: 0x2121
-  __TEXT.__cstring: 0xcf5b
-  __TEXT.__oslogstring: 0xff2c
-  __TEXT.__gcc_except_tab: 0x514c
+  __TEXT.__cstring: 0xd111
+  __TEXT.__oslogstring: 0x10009
+  __TEXT.__gcc_except_tab: 0x5174
   __TEXT.__ustring: 0x1b8
   __TEXT.__dlopen_cstrs: 0x10e
-  __TEXT.__unwind_info: 0x3888
-  __TEXT.__objc_classname: 0x17a6
-  __TEXT.__objc_methname: 0x1df8a
-  __TEXT.__objc_methtype: 0x3d8c
-  __TEXT.__objc_stubs: 0xd280
-  __DATA_CONST.__got: 0x920
-  __DATA_CONST.__const: 0x4f78
-  __DATA_CONST.__objc_classlist: 0x520
+  __TEXT.__unwind_info: 0x3930
+  __TEXT.__objc_classname: 0x1862
+  __TEXT.__objc_methname: 0x1e6c8
+  __TEXT.__objc_methtype: 0x3ed1
+  __TEXT.__objc_stubs: 0xd640
+  __DATA_CONST.__got: 0x950
+  __DATA_CONST.__const: 0x5018
+  __DATA_CONST.__objc_classlist: 0x550
   __DATA_CONST.__objc_catlist: 0x80
-  __DATA_CONST.__objc_protolist: 0x1c0
+  __DATA_CONST.__objc_protolist: 0x1c8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x61b0
+  __DATA_CONST.__objc_selrefs: 0x62e0
   __DATA_CONST.__objc_protorefs: 0xd8
-  __DATA_CONST.__objc_superrefs: 0x340
+  __DATA_CONST.__objc_superrefs: 0x360
   __DATA_CONST.__objc_arraydata: 0x138
   __AUTH_CONST.__auth_got: 0x6c8
   __AUTH_CONST.__auth_ptr: 0x18
   __AUTH_CONST.__const: 0x1050
-  __AUTH_CONST.__cfstring: 0xd860
-  __AUTH_CONST.__objc_const: 0x224c0
+  __AUTH_CONST.__cfstring: 0xd9c0
+  __AUTH_CONST.__objc_const: 0x22de8
   __AUTH_CONST.__objc_intobj: 0x240
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x168
-  __AUTH.__objc_data: 0x1748
-  __DATA.__objc_ivar: 0xe5c
-  __DATA.__data: 0x1540
+  __AUTH.__objc_data: 0x1928
+  __DATA.__objc_ivar: 0xe8c
+  __DATA.__data: 0x15a0
   __DATA.__bss: 0x620
   __DATA_DIRTY.__objc_data: 0x1bf8
   __DATA_DIRTY.__bss: 0x238

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5502
-  Symbols:   7463
-  CStrings:  8628
+  Functions: 5568
+  Symbols:   7543
+  CStrings:  8722
 
Symbols:
+ _OBJC_CLASS_$_AKAccountRecoveryModel
+ _OBJC_CLASS_$_AKForgotPasswordController
+ _OBJC_CLASS_$_AKAccountRecoveryResponse
+ _OBJC_METACLASS_$_AKAccountRecoveryModel
+ _OBJC_CLASS_$_AKAppleIDRecoveryController
+ _OBJC_METACLASS_$_AKAccountRecoveryStepVerifyAppleID
+ _OBJC_METACLASS_$_AKForgotPasswordController
+ _OBJC_METACLASS_$_AKChangePasswordController
+ _OBJC_CLASS_$_AKChangePasswordController
+ _OBJC_CLASS_$_AKAccountRecoveryStepVerifyAppleID
+ _OBJC_METACLASS_$_AKAccountRecoveryResponse
+ _OBJC_METACLASS_$_AKAppleIDRecoveryController
CStrings:
+ "@\"NSHTTPURLResponse\""
+ "_supportedRecoverySteps"
+ "_verifyAppleIDWithModel:completion:"
+ "setForgotPasswordController:"
+ "AKChangePasswordController"
+ "supportedRecoverySteps"
+ "@\"AKAppleIDAuthenticationCommandLineContext\""
+ "Finished recovery flow for - %!@(MISSING)"
+ "signXMLRequest:"
+ "AKForgotPasswordController"
+ "ruiElementsAttributesWithName:data:error:"
+ "setCliUtilities:"
+ "beginAccountRecoveryWithModel:completion:"
+ "_tearDownConnection"
+ "_beginVerifyAppleIDWithResponse:model:completion:"
+ "updateConfiguration:fromXMLAttributes:response:"
+ "_promptForUsernameWithModel:"
+ "initWithContext:configuration:utilities:"
+ "T@\"AKForgotPasswordController\",&,N,V_forgotPasswordController"
+ "initWithData:httpResponse:"
+ "T@\"NSString\",C,N,V_recoveryKey"
+ "AKAccountRecoveryStepVerifyAppleID"
+ "recoveryKey"
+ "_processResponse:model:withCompletion:"
+ "SignInSecurityRedesign"
+ "_logResponse:"
+ "T@\"NSArray\",&,N,V_supportedRecoverySteps"
+ "Finished account recovery step: %!@(MISSING)"
+ "\x11\x1b"
+ "_beginAccountRecoveryWithModel:completion:"
+ "multiChoice"
+ "_cliUtilities"
+ "_nativeTakeoverEndpointsWithCompletionHandler:"
+ "Begin account recovery step: %!@(MISSING)"
+ "_nextStepForResponse:"
+ "isSignInSecurityRedesignEnabled"
+ "Verifying user entered Apple ID"
+ "_recoveryKey"
+ "Enter your email address or phone number: "
+ "T@\"AKAppleIDAuthenticationCommandLineContext\",&,N,V_context"
+ "shouldProcessURL:completion:"
+ "_presentServerUIWithConfiguration:completion:"
+ "B24@0:8@\"AKAccountRecoveryResponse\"16"
+ "signXMLRequest:withPostbackDictionary:"
+ "<%!@(MISSING): %!p(MISSING) { UUID: %!@(MISSING) - FlowID: %!@(MISSING) - SessionID: %!@(MISSING) }>"
+ "_forgotPasswordController"
+ "_localSecret"
+ "No matching recovery step found"
+ "_isURLString:"
+ "initWithString:"
+ "_configuration"
+ "Feature SignInSecurityRedesign enabled - %!@(MISSING)"
+ "T@\"NSHTTPURLResponse\",R,N,V_httpResponse"
+ "requestConfiguration is nil"
+ "T@\"NSData\",R,N,V_data"
+ "httpResponse"
+ "Begin change password flow"
+ "processResponse:model:withCompletion:"
+ "_allowAuthenticationBeforeFirstUnlock"
+ "children"
+ "forgotPasswordController"
+ "T@\"NSString\",C,N,V_localSecret"
+ "AKAccountRecoveryModel"
+ "setConfiguration:"
+ "@\"AKChangePasswordController\""
+ "_httpResponse"
+ "AKAccountRecoveryStep"
+ "navigationBar"
+ "Begin iForgot password flow"
+ "Tearing down connection to akd..."
+ "_matchURLProcessingSet:url:"
+ "allowAuthenticationBeforeFirstUnlock"
+ "@\"AKServerRequestConfiguration\""
+ "TB,R,N,GisSignInSecurityRedesignEnabled"
+ "AKAppleIDRecoveryController"
+ "forgot password"
+ "_processNextStep:response:model:completion:"
+ "changePasswordController"
+ "T@\"AKChangePasswordController\",&,N,V_changePasswordController"
+ "T@\"AKServerRequestConfiguration\",&,N,V_configuration"
+ "_findMatchingElementWithName:inElement:"
+ "canProcessResponse:"
+ "T@\"AKCommandLineUtilities\",&,N,V_cliUtilities"
+ "AKAccountRecoveryResponse"
+ "_changePasswordController"
+ "<%!@(MISSING): %!p(MISSING) {\n\theaderFields: %!@(MISSING), \n\tdata: %!@(MISSING), \n}>"
+ "setRecoveryKey:"
+ "v44@?0B8@\"NSData\"12@\"NSHTTPURLResponse\"20@\"NSDictionary\"28@\"NSError\"36"
+ "_cachedSignInSecurityRedesignEnabled"
+ "@\"AKForgotPasswordController\""
+ "v40@0:8@\"AKAccountRecoveryResponse\"16@\"AKAccountRecoveryModel\"24@?<v@?B@\"NSData\"@\"NSHTTPURLResponse\"@\"NSDictionary\"@\"NSError\">32"
+ "setSupportedRecoverySteps:"
+ "setAllowAuthenticationBeforeFirstUnlock:"
+ "cliUtilities"
+ "TB,N,V_allowAuthenticationBeforeFirstUnlock"
+ "setLocalSecret:"
+ "Found matching recovery step: %!@(MISSING)"
+ "localSecret"
+ "setChangePasswordController:"
+ "Failed AppleID verify step with unexpected data"
- "osAttestationURL"
- "<%!@(MISSING): %!p(MISSING) { UUID: %!@(MISSING) }>"
- "circleURL"
- "_presentServerUISecondFactorWithConfiguration:completion:"
- "\x11\x17"
- "AKAnisetteProvisioningControllerXPCLock"
- "storeModernRecoveryURL"
- "fetchFollowUps"

```
