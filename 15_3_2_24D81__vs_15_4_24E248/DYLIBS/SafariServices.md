## SafariServices

> `/System/iOSSupport/System/Library/Frameworks/SafariServices.framework/Versions/A/SafariServices`

```diff

-620.2.4.11.6
-  __TEXT.__text: 0x182b8
+621.1.15.11.10
+  __TEXT.__text: 0x17f34
   __TEXT.__auth_stubs: 0x990
-  __TEXT.__objc_methlist: 0x1bf4
+  __TEXT.__objc_methlist: 0x2cac
   __TEXT.__gcc_except_tab: 0xd1c
-  __TEXT.__const: 0x14d6
-  __TEXT.__cstring: 0xdee
+  __TEXT.__const: 0x14f6
+  __TEXT.__cstring: 0xd8e
   __TEXT.__oslogstring: 0x6cf
   __TEXT.__dlopen_cstrs: 0x43
   __TEXT.__constg_swiftt: 0x50
   __TEXT.__swift5_typeref: 0x6
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0xb30
-  __TEXT.__objc_classname: 0x6de
-  __TEXT.__objc_methname: 0x9d73
-  __TEXT.__objc_methtype: 0x38a7
-  __TEXT.__objc_stubs: 0x53e0
-  __DATA_CONST.__got: 0x510
-  __DATA_CONST.__const: 0x720
+  __TEXT.__unwind_info: 0xb58
+  __TEXT.__objc_classname: 0x6df
+  __TEXT.__objc_methname: 0x9be0
+  __TEXT.__objc_methtype: 0x384c
+  __TEXT.__objc_stubs: 0x5340
+  __DATA_CONST.__got: 0x528
+  __DATA_CONST.__const: 0x718
   __DATA_CONST.__objc_classlist: 0x118
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1c20
+  __DATA_CONST.__objc_selrefs: 0x20f0
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0xe8
   __DATA_CONST.__objc_arraydata: 0x20
   __AUTH_CONST.__auth_got: 0x4e0
-  __AUTH_CONST.__const: 0x448
-  __AUTH_CONST.__cfstring: 0x1040
-  __AUTH_CONST.__objc_const: 0x61a0
+  __AUTH_CONST.__const: 0x450
+  __AUTH_CONST.__cfstring: 0xfa0
+  __AUTH_CONST.__objc_const: 0x4140
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x30

   - /System/Library/PrivateFrameworks/TextInput.framework/Versions/A/TextInput
   - /System/Library/PrivateFrameworks/UIKitServices.framework/Versions/A/UIKitServices
   - /System/iOSSupport/System/Library/Frameworks/AuthenticationServices.framework/Versions/A/AuthenticationServices
+  - /System/iOSSupport/System/Library/Frameworks/ExtensionKit.framework/Versions/A/ExtensionKit
   - /System/iOSSupport/System/Library/Frameworks/JavaScriptCore.framework/Versions/A/JavaScriptCore
   - /System/iOSSupport/System/Library/Frameworks/MediaPlayer.framework/Versions/A/MediaPlayer
   - /System/iOSSupport/System/Library/Frameworks/UIKit.framework/Versions/A/UIKit

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: D5A0F256-A37B-32C9-B232-FBA3A5EDA0C0
-  Functions: 730
-  Symbols:   2579
-  CStrings:  2043
+  UUID: CE85489B-9971-3BA0-874D-9300F3703BE6
+  Functions: 743
+  Symbols:   2592
+  CStrings:  2026
 
Symbols:
+ +[NSBundle(SafariServicesExtras) _sf_safariServicesBundle].cold.1
+ +[NSUserDefaults(MobileSafariExtras) safari_sfAppDefaults].cold.1
+ +[SFLargeGladeButton _accentColorNames].cold.1
+ +[SFSafariViewControllerDataStore defaultDataStore].cold.1
+ -[SFSafariLaunchPlaceholderView initWithAppName:destinationURL:forAuthentication:dismissalHandler:openHandler:].cold.2
+ -[SFSafariViewController _addLaunchPlaceholderView].cold.1
+ -[SFSafariViewController initWithURL:entersReaderIfAvailable:].cold.1
+ -[_SFFormMetadataController autoFillFormInFrame:withValues:fillSynchronously:setAutoFilled:focusFieldAfterFilling:fieldToFocus:fieldsToObscure:fillAllCharactersAtOnce:submitForm:]
+ -[_SFReaderController didCollectReaderAvailabilityResultForTesting:]
+ -[_SFReaderController setTestController:]
+ -[_SFReaderController testController]
+ -[_SFWebProcessPlugInAutoFillPageController autoFillFormAsynchronouslyInFrame:withValues:setAutoFilled:focusFieldAfterFilling:fieldToFocus:fieldsToObscure:fillAllCharactersAtOnce:submitForm:]
+ -[_SFWebProcessPlugInAutoFillPageController setPageTestType:]
+ .compoundliteral
+ OBJC_IVAR_$__SFReaderController._testController
+ WBS_LOG_CHANNEL_PREFIXAutoFill.cold.1
+ WBS_LOG_CHANNEL_PREFIXContentBlockers.cold.1
+ WBS_LOG_CHANNEL_PREFIXExtensions.cold.1
+ WBS_LOG_CHANNEL_PREFIXOther.cold.1
+ WBS_LOG_CHANNEL_PREFIXReaderExtraction.cold.1
+ WBS_LOG_CHANNEL_PREFIXReadingList.cold.1
+ WBS_LOG_CHANNEL_PREFIXViewService.cold.1
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _SFShowTabBarDefaultsKey
+ _SuppressSearchSuggestionsDefaultsKey
+ __SFOpenLinksInBackgroundDefaultsKey
+ __ZN12SafariShared28ReaderAvailabilityController46checkReaderAvailabilityIfNeededAndUpdateResultEP32WBSReaderAvailabilityCheckResult
+ _objc_msgSend$autoFillFormInFrame:withValues:fillSynchronously:setAutoFilled:focusFieldAfterFilling:fieldToFocus:fieldsToObscure:fillAllCharactersAtOnce:submitForm:
+ _objc_msgSend$didCollectReaderAvailabilityResultForTesting:
+ _objc_msgSend$safari_safariServicesInjectedBundleURL
- -[SFSafariViewController _handleURLExternallyIfApplicableBypassingVisibilityCheck:].cold.1
- -[SFSafariViewController _handleURLExternallyIfApplicableBypassingVisibilityCheck:].cold.2
- -[_SFFormMetadataController _assistedNodeMetadataWithPasswordField:passwordFieldMetadata:formMetadata:inFrame:]
- -[_SFFormMetadataController autoFillFormInFrame:withValues:fillSynchronously:setAutoFilled:focusFieldAfterFilling:fieldToFocus:]
- -[_SFFormMetadataController autoFillFormInFrame:withValues:fillSynchronously:setAutoFilled:selectFieldAfterFilling:]
- -[_SFFormMetadataController creditCardFieldFocused:inFrame:]
- -[_SFFormMetadataController passwordFieldFocused:inFrame:textFieldMetadata:formMetadata:isPasswordFieldForUserCredentials:]
- -[_SFFormMetadataController shouldIncludeNonEmptyFields]
- -[_SFFormMetadataController usernameFieldFocused:fieldMetadata:inForm:inFrame:]
- -[_SFWebProcessPlugInAutoFillPageController autoFillFormAsynchronouslyInFrame:withValues:setAutoFilled:focusFieldAfterFilling:fieldToFocus:]
- -[_SFWebProcessPlugInAutoFillPageController autoFillFormAsynchronouslyInFrame:withValues:setAutoFilled:focusFieldAfterFilling:fieldToFocus:fieldsToObscure:submitForm:]
- -[_SFWebProcessPlugInAutoFillPageController autoFillFormAsynchronouslyInFrame:withValues:setAutoFilled:focusFieldAfterFilling:fieldToFocus:submitForm:]
- -[_SFWebProcessPlugInAutoFillPageController autoFillFormAsynchronouslyInFrame:withValues:setAutoFilled:selectFieldAfterFilling:]
- -[_SFWebProcessPlugInAutoFillPageController autoFillFormSynchronouslyInFrame:withValues:]
- GCC_except_table39
- OBJC_IVAR_$__SFFormMetadataController._assistedNodeMetadata
- __swift_FORCE_LOAD_$_swiftFileProvider
- __swift_FORCE_LOAD_$_swiftFileProvider_$_SafariServices
- _objc_msgSend$URLByAppendingPathComponent:isDirectory:
- _objc_msgSend$_assistedNodeMetadataWithPasswordField:passwordFieldMetadata:formMetadata:inFrame:
- _objc_msgSend$autoFillFormAsynchronouslyInFrame:withValues:setAutoFilled:focusFieldAfterFilling:fieldToFocus:fieldsToObscure:submitForm:
- _objc_msgSend$autoFillFormAsynchronouslyInFrame:withValues:setAutoFilled:focusFieldAfterFilling:fieldToFocus:submitForm:
- _objc_msgSend$autoFillFormInFrame:withValues:fillSynchronously:setAutoFilled:focusFieldAfterFilling:fieldToFocus:
- _objc_msgSend$autoFillFormInFrame:withValues:fillSynchronously:setAutoFilled:focusFieldAfterFilling:fieldToFocus:fieldsToObscure:submitForm:
- _objc_msgSend$autoFillFormSynchronouslyInFrame:withValues:
- _objc_msgSend$builtInPlugInsURL
CStrings:
+ "@\"<_SFReaderTestController>\""
+ "T@\"<_SFReaderTestController>\",W,N,V_testController"
+ "_testController"
+ "_webView:decidePolicyForScreenCaptureUnmutingForOrigin:initiatedByFrame:decisionHandler:"
+ "autoFillFormAsynchronouslyInFrame:withValues:setAutoFilled:focusFieldAfterFilling:fieldToFocus:fieldsToObscure:fillAllCharactersAtOnce:submitForm:"
+ "autoFillFormInFrame:withValues:fillSynchronously:setAutoFilled:focusFieldAfterFilling:fieldToFocus:fieldsToObscure:fillAllCharactersAtOnce:submitForm:"
+ "didCollectReaderAvailabilityResultForTesting:"
+ "safari_safariServicesInjectedBundleURL"
+ "setPageTestType:"
+ "setTestController:"
+ "testController"
+ "v44@0:8@\"WKWebView\"16@\"WKBackForwardListItem\"24B32@?<v@?B>36"
+ "v44@0:8@16@24B32@?36"
+ "v48@0:8@\"WKWebView\"16@\"WKOpenPanelParameters\"24@\"WKFrameInfo\"32@?<v@?@\"NSArray\">40"
+ "v48@0:8@\"WKWebView\"16@\"WKSecurityOrigin\"24@\"WKFrameInfo\"32@?<v@?B>40"
+ "v64@0:8@\"SFFormAutoFillFrameHandle\"16@\"NSDictionary\"24B32B36@\"NSString\"40@\"NSArray\"48B56B60"
+ "v64@0:8@16@24B32B36@40@48B56B60"
+ "v68@0:8@16@24B32B36B40@44@52B60B64"
+ "webView:runOpenPanelWithParameters:initiatedByFrame:completionHandler:"
+ "webView:shouldGoToBackForwardListItem:willUseInstantBack:completionHandler:"
- "SafariServices.wkbundle"
- "URLByAppendingPathComponent:isDirectory:"
- "_assistedNodeMetadata"
- "_assistedNodeMetadataWithPasswordField:passwordFieldMetadata:formMetadata:inFrame:"
- "autoFillButtonType"
- "autoFillFormAsynchronouslyInFrame:withValues:setAutoFilled:focusFieldAfterFilling:fieldToFocus:"
- "autoFillFormAsynchronouslyInFrame:withValues:setAutoFilled:focusFieldAfterFilling:fieldToFocus:fieldsToObscure:submitForm:"
- "autoFillFormAsynchronouslyInFrame:withValues:setAutoFilled:focusFieldAfterFilling:fieldToFocus:submitForm:"
- "autoFillFormAsynchronouslyInFrame:withValues:setAutoFilled:selectFieldAfterFilling:"
- "autoFillFormInFrame:withValues:fillSynchronously:setAutoFilled:focusFieldAfterFilling:fieldToFocus:"
- "autoFillFormInFrame:withValues:fillSynchronously:setAutoFilled:focusFieldAfterFilling:fieldToFocus:fieldsToObscure:submitForm:"
- "autoFillFormInFrame:withValues:fillSynchronously:setAutoFilled:selectFieldAfterFilling:"
- "autoFillFormSynchronouslyInFrame:withValues:"
- "builtInPlugInsURL"
- "creditCardFieldFocused:inFrame:"
- "lastAutoFillButtonType"
- "passwordField"
- "passwordFieldFocused:inFrame:textFieldMetadata:formMetadata:isPasswordFieldForUserCredentials:"
- "shouldIncludeNonEmptyFields"
- "usernameField"
- "usernameFieldFocused:fieldMetadata:inForm:inFrame:"
- "v32@0:8@\"SFFormAutoFillFrameHandle\"16@\"NSDictionary\"24"
- "v44@0:8@\"SFFormAutoFillFrameHandle\"16@\"NSDictionary\"24B32@\"NSString\"36"
- "v44@0:8@16@24B32@36"
- "v48@0:8@\"SFFormAutoFillFrameHandle\"16@\"NSDictionary\"24B32B36@\"NSString\"40"
- "v48@0:8@16@24B32B36@40"
- "v52@0:8@\"SFFormAutoFillFrameHandle\"16@\"NSDictionary\"24B32B36@\"NSString\"40B48"
- "v52@0:8@16@24@32@40B48"
- "v52@0:8@16@24B32B36@40B48"
- "v52@0:8@16@24B32B36B40@44"
- "v60@0:8@\"SFFormAutoFillFrameHandle\"16@\"NSDictionary\"24B32B36@\"NSString\"40@\"NSArray\"48B56"
- "v60@0:8@16@24B32B36@40@48B56"

```
