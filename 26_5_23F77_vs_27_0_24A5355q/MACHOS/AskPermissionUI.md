## AskPermissionUI

> `/Applications/AskPermissionUI.app/AskPermissionUI`

```diff

-129.5.3.0.0
-  __TEXT.__text: 0xd3d0
-  __TEXT.__auth_stubs: 0x4f0
-  __TEXT.__objc_stubs: 0x1f20
-  __TEXT.__objc_methlist: 0x1044
-  __TEXT.__const: 0xc0
-  __TEXT.__objc_classname: 0x1e4
-  __TEXT.__objc_methname: 0x3453
-  __TEXT.__objc_methtype: 0x1288
-  __TEXT.__gcc_except_tab: 0x124
-  __TEXT.__cstring: 0x9dd
-  __TEXT.__oslogstring: 0xbcc
-  __TEXT.__dlopen_cstrs: 0x47
-  __TEXT.__unwind_info: 0x2a8
-  __DATA_CONST.__auth_got: 0x288
-  __DATA_CONST.__got: 0x1e8
-  __DATA_CONST.__const: 0x330
-  __DATA_CONST.__cfstring: 0x1380
-  __DATA_CONST.__objc_classlist: 0x68
+130.0.18.0.0
+  __TEXT.__text: 0xdd48
+  __TEXT.__auth_stubs: 0x500
+  __TEXT.__objc_stubs: 0x2400
+  __TEXT.__objc_methlist: 0x13c8
+  __TEXT.__const: 0xb0
+  __TEXT.__cstring: 0xa41
+  __TEXT.__oslogstring: 0xe08
+  __TEXT.__objc_classname: 0x25d
+  __TEXT.__objc_methname: 0x400f
+  __TEXT.__objc_methtype: 0x18d0
+  __TEXT.__gcc_except_tab: 0x168
+  __TEXT.__unwind_info: 0x2e8
+  __DATA_CONST.__const: 0x3b8
+  __DATA_CONST.__cfstring: 0x1440
+  __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x48
+  __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x40
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_superrefs: 0x48
   __DATA_CONST.__objc_intobj: 0x18
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x2020
-  __DATA.__objc_selrefs: 0xc60
-  __DATA.__objc_ivar: 0x144
-  __DATA.__objc_data: 0x410
-  __DATA.__data: 0x360
+  __DATA_CONST.__auth_got: 0x290
+  __DATA_CONST.__got: 0x238
+  __DATA.__objc_const: 0x2570
+  __DATA.__objc_selrefs: 0xea8
+  __DATA.__objc_ivar: 0x164
+  __DATA.__objc_data: 0x500
+  __DATA.__data: 0x420
   __DATA.__bss: 0x28
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/Frameworks/StoreKit.framework/StoreKit
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/Frameworks/WebKit.framework/WebKit
   - /System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices
   - /System/Library/PrivateFrameworks/AskPermission.framework/AskPermission
   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
-  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
+  - /System/Library/PrivateFrameworks/AuthKitUI.framework/AuthKitUI
   - /System/Library/PrivateFrameworks/SpringBoardUIServices.framework/SpringBoardUIServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FDEFD1A7-51F9-3FED-9D49-1A5C4F608404
-  Functions: 217
-  Symbols:   157
-  CStrings:  1065
+  UUID: 1C579C40-165B-323C-9E55-6060B5D98577
+  Functions: 257
+  Symbols:   167
+  CStrings:  1211
 
Symbols:
+ _AMSBuyParamPropertyAppAdamId
+ _AMSBuyParamPropertyBundleId
+ _ConnectionServiceName
+ _OBJC_CLASS_$_AKAppleIDAuthenticationInAppContext
+ _OBJC_CLASS_$_NSThread
+ _OBJC_CLASS_$_NSUUID
+ _OBJC_CLASS_$_NSXPCConnection
+ _OBJC_CLASS_$_NSXPCInterface
+ _OBJC_CLASS_$_SKStoreProductViewController
+ _OBJC_CLASS_$_UIWindowSceneGeometryPreferencesIOS
+ _SKStoreProductParameterITunesItemIdentifier
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x1
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_setProperty_nonatomic_copy
+ _os_transaction_create
- _OBJC_CLASS_$_UIApplication
- _OBJC_CLASS_$_UIWindow
- __Block_object_dispose
- __sl_dlopen
- _abort_report_np
- _dlerror
- _dlsym
- _free
- _objc_autorelease
- _objc_getClass
CStrings:
+ "%{public}@: Completing authentication. Error: %{public}@"
+ "%{public}@: Configured with context. authenticationType: %{public}ld"
+ "%{public}@: Daemon connection lost, cancelling authentication"
+ "%{public}@: Error requesting geometry update. Error: %{public}@"
+ "%{public}@: Home button pressed, cancelling authentication"
+ "%{public}@: Remote view controller proxy error. Error: %{public}@"
+ "%{public}@: XPC error sending authentication result. Error: %{public}@"
+ "%{public}@: contextWillBeginPresentingSecondaryUI"
+ "%{public}@: presentingViewController is nil, falling back to base context"
+ "@\"NSObject<OS_os_transaction>\""
+ "@\"NSUUID\""
+ "@\"NSUUID\"16@0:8"
+ "@\"NSXPCConnection\""
+ "@\"RUIStyle\"16@0:8"
+ "@212@0:8@16@24@32@40@48B56B60@64@72@80@88@96@104B112@116@124@132@140@148@156@164@172@180@188@196q204"
+ "AKAppleIDAuthenticationInAppContextDelegate"
+ "AuthKitContextDelegate"
+ "Authentication dismissed by user"
+ "AuthenticationRemoteViewController"
+ "ConnectionProtocol"
+ "Daemon connection lost"
+ "T@\"AuthKitContextDelegate\",R,N"
+ "T@\"NSObject<OS_os_transaction>\",&,N,V_transaction"
+ "T@\"NSString\",&,N,V_requesterAltDSID"
+ "T@\"NSString\",C,N,V_username"
+ "T@\"NSUUID\",R,N"
+ "T@\"NSUUID\",R,N,V_uuid"
+ "T@\"NSXPCConnection\",&,N,V_daemonConnection"
+ "TB,N,V_authenticationStarted"
+ "TB,N,V_completed"
+ "Tq,N,V_authenticationType"
+ "UUID"
+ "UUIDString"
+ "User cancelled"
+ "UserAuthenticatorUI"
+ "_acquireProcessAssertion"
+ "_authenticationStarted"
+ "_authenticationType"
+ "_completeWithUser:error:"
+ "_completed"
+ "_configureAuthenticationContext:withTitle:"
+ "_createAuthenticationContext"
+ "_daemonConnection"
+ "_dismiss"
+ "_releaseProcessAssertion"
+ "_requesterAltDSID"
+ "_transaction"
+ "_uuid"
+ "addExceptionRequestWithUUID:type:bundleIdentifier:adamID:distributorID:ageRatingValue:withCompletion:"
+ "addExceptionRequestWithUUID:type:bundleIdentifier:withCompletion:"
+ "addExceptionRequestWithUUID:type:title:message:bundleIdentifier:adamID:distributorID:ageRatingValue:preApprove:postApprove:preDecline:postDecline:responseBundleIdentifier:metadata:withCompletion:"
+ "addRequestWithURL:account:completion:"
+ "ams_sanitizedForSecureCoding"
+ "authenticationStarted"
+ "authenticationType"
+ "checkDownloadQueueWithContentType:completion:"
+ "clearExceptionRequestsWithCompletion:"
+ "com.apple.AskPermissionUI.Authentication"
+ "completeAuthenticationWithUserDictionary:error:completion:"
+ "completed"
+ "contextDidDismissLoginAlertController:"
+ "contextDidEndPresentingSecondaryUI:"
+ "contextDidPresentLoginAlertController:"
+ "contextWillBeginPresentingSecondaryUI:"
+ "contextWillBeginPresentingSecondaryUI:completion:"
+ "contextWillDismissLoginAlertController:"
+ "count"
+ "daemonConnection"
+ "didReceiveStorePushNotificationWithPayload:"
+ "getCachedRequestsWithCompletion:"
+ "getExceptionRequestWithDistributorIdentifier:completionHandler:"
+ "getExceptionRequestWithUniqueIdentifier:completionHandler:"
+ "getExceptionRequestsWithBundleIdentifier:completionHandler:"
+ "getExceptionRequestsWithCompletion:"
+ "getMatchingRequestsWithIdentifier:completion:"
+ "getRequestWithIdentifier:completion:"
+ "getRequestWithItemIdentifier:completion:"
+ "initWithApproverDSID:createdDate:modifiedDate:requestIdentifier:uniqueIdentifier:canSendViaMessages:isException:itemBundleID:itemDescription:itemIdentifier:itemTitle:localizations:offerName:mocked:previewURL:productType:productTypeName:productURL:requesterName:requesterDSID:requesterAltDSID:requestInfo:requestString:requestSummary:priceSummary:status:"
+ "initWithMachServiceName:options:"
+ "initWithUUIDString:"
+ "interfaceOrientation"
+ "interfaceWithProtocol:"
+ "invalidate"
+ "isMainThread"
+ "localApproveExceptionWithUniqueIdentifier:completionHandler:"
+ "localApproveRequestWithItemIdentifier:completion:"
+ "parentSalableForRequestInfo:fromParentSalables:"
+ "presentApprovalSheetWithRequestIdentifier:completion:"
+ "presentProductPageWithTitle:body:approve:decline:itemIdentifier:previewURL:offerName:requestString:requestSummary:priceSummary:isException:"
+ "presentingViewController"
+ "remoteObjectProxyWithErrorHandler:"
+ "remoteUIStyle"
+ "requestGeometryUpdateWithPreferences:errorHandler:"
+ "requesterAltDSID"
+ "resetAccountWithType:"
+ "restartAPNSConnection"
+ "resume"
+ "setAuthenticationStarted:"
+ "setCompleted:"
+ "setDaemonConnection:"
+ "setForceInlinePresentation:"
+ "setInterfaceOrientations:"
+ "setInvalidationHandler:"
+ "setNavigationBarHidden:"
+ "setPresentingViewController:"
+ "setRemoteObjectInterface:"
+ "setRequesterAltDSID:"
+ "setTitle:"
+ "setTransaction:"
+ "sharedDelegate"
+ "signAdditionalHeadersWithRequest:withCompletion:"
+ "start"
+ "transaction"
+ "updateExceptionRequestWithUniqueIdentifier:action:completionHandler:"
+ "uuid"
+ "v100@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@\"NSString\"48@\"NSString\"56@\"NSString\"64@\"NSString\"72@\"NSString\"80@\"NSString\"88B96"
+ "v100@0:8@16@24@32@40@48@56@64@72@80@88B96"
+ "v136@0:8@\"NSUUID\"16q24@\"NSString\"32@\"NSString\"40@\"NSString\"48@\"NSNumber\"56@\"NSString\"64@\"NSNumber\"72@\"NSString\"80@\"NSString\"88@\"NSString\"96@\"NSString\"104@\"NSString\"112@\"APAskToAgeRestrictionMetadata\"120@?<v@?B@\"NSError\">128"
+ "v136@0:8@16q24@32@40@48@56@64@72@80@88@96@104@112@120@?128"
+ "v24@0:8@\"AKAppleIDAuthenticationInAppContext\"16"
+ "v24@0:8@\"NSDictionary\"16"
+ "v24@0:8@\"UINavigationController\"16"
+ "v24@0:8@\"UIViewController\"16"
+ "v24@0:8@?16"
+ "v24@0:8@?<v@?@\"NSArray\">16"
+ "v24@0:8@?<v@?@\"NSError\">16"
+ "v24@?0@\"User\"8@\"NSError\"16"
+ "v32@0:8@\"AKAppleIDAuthenticationInAppContext\"16@?<v@?>24"
+ "v32@0:8@\"NSMutableURLRequest\"16@?<v@?@\"NSMutableURLRequest\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSArray\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSArray\"@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSDictionary\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSDictionary\"@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?B@\"NSError\">24"
+ "v32@0:8q16@?24"
+ "v32@0:8q16@?<v@?@\"NSError\">24"
+ "v40@0:8@\"NSDictionary\"16@\"NSError\"24@?<v@?>32"
+ "v40@0:8@\"NSString\"16q24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"NSURL\"16@\"ACAccount\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"WKWebView\"16@\"WKFormInfo\"24@?<v@?>32"
+ "v48@0:8@\"NSUUID\"16q24@\"NSString\"32@?<v@?B@\"NSUUID\"@\"NSError\">40"
+ "v48@0:8@16q24@32@?40"
+ "v72@0:8@\"NSUUID\"16q24@\"NSString\"32@\"NSNumber\"40@\"NSString\"48@\"NSNumber\"56@?<v@?B@\"NSUUID\"@\"NSError\">64"
+ "v72@0:8@16q24@32@40@48@56@?64"
+ "webView:willSubmitForm:submissionHandler:"
+ "willPresentModalNavigationController:"
+ "willShowViewController:"
+ "windowScene"
- "%s"
- "@204@0:8@16@24@32@40@48B56B60@64@72@80@88@96@104B112@116@124@132@140@148@156@164@172@180@188q196"
- "SKStoreProductParameterITunesItemIdentifier"
- "SKStoreProductViewController"
- "Unable to find class %s"
- "_applicationKeyWindow"
- "_setRotatableViewOrientation:duration:force:"
- "initWithApproverDSID:createdDate:modifiedDate:requestIdentifier:uniqueIdentifier:canSendViaMessages:isException:itemBundleID:itemDescription:itemIdentifier:itemTitle:localizations:offerName:mocked:previewURL:productType:productTypeName:productURL:requesterName:requesterDSID:requestInfo:requestString:requestSummary:priceSummary:status:"
- "sharedApplication"
- "softlink:r:path:/System/Library/Frameworks/StoreKit.framework/StoreKit"
- "statusBarOrientation"

```
