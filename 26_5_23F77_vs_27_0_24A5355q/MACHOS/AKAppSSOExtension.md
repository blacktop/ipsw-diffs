## AKAppSSOExtension

> `/System/Library/PrivateFrameworks/AuthKitUI.framework/PlugIns/AKAppSSOExtension.appex/AKAppSSOExtension`

```diff

-525.575.8.0.0
-  __TEXT.__text: 0xc198
-  __TEXT.__auth_stubs: 0x2a0
-  __TEXT.__objc_stubs: 0x1200
-  __TEXT.__objc_methlist: 0x53c
-  __TEXT.__const: 0x58
-  __TEXT.__cstring: 0x41cb
-  __TEXT.__objc_classname: 0xc9
-  __TEXT.__objc_methname: 0x1586
-  __TEXT.__objc_methtype: 0x2c1
-  __TEXT.__gcc_except_tab: 0x49c
+550.0.0.0.0
+  __TEXT.__text: 0x110b8
+  __TEXT.__auth_stubs: 0x2e0
+  __TEXT.__objc_stubs: 0x17c0
+  __TEXT.__objc_methlist: 0x5cc
+  __TEXT.__const: 0x60
+  __TEXT.__cstring: 0x4475
+  __TEXT.__objc_methname: 0x1b5d
+  __TEXT.__oslogstring: 0xe18
+  __TEXT.__objc_classname: 0xe9
+  __TEXT.__objc_methtype: 0x303
+  __TEXT.__gcc_except_tab: 0x408
   __TEXT.__dlopen_cstrs: 0x21
-  __TEXT.__oslogstring: 0x8f2
-  __TEXT.__unwind_info: 0x150
-  __DATA_CONST.__auth_got: 0x160
-  __DATA_CONST.__got: 0x160
-  __DATA_CONST.__const: 0x540
-  __DATA_CONST.__cfstring: 0x2460
-  __DATA_CONST.__objc_classlist: 0x20
+  __TEXT.__unwind_info: 0x1a0
+  __DATA_CONST.__const: 0x6e0
+  __DATA_CONST.__cfstring: 0x2660
+  __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__objc_intobj: 0x198
-  __DATA_CONST.__objc_arraydata: 0xee0
-  __DATA_CONST.__objc_dictobj: 0xb90
-  __DATA_CONST.__objc_arrayobj: 0x258
-  __DATA.__objc_const: 0x748
-  __DATA.__objc_selrefs: 0x6d0
+  __DATA_CONST.__objc_intobj: 0x1b0
+  __DATA_CONST.__objc_arraydata: 0x1018
+  __DATA_CONST.__objc_dictobj: 0xc30
+  __DATA_CONST.__objc_arrayobj: 0x288
+  __DATA_CONST.__auth_got: 0x180
+  __DATA_CONST.__got: 0x1b8
+  __DATA.__objc_const: 0x7d8
+  __DATA.__objc_selrefs: 0x850
   __DATA.__objc_ivar: 0x4
-  __DATA.__objc_data: 0x140
+  __DATA.__objc_data: 0x190
   __DATA.__data: 0x130
   __DATA.__bss: 0x58
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/AAAFoundation.framework/AAAFoundation
   - /System/Library/PrivateFrameworks/AppSSO.framework/AppSSO
+  - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount
   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
   - /System/Library/PrivateFrameworks/AuthKitUI.framework/AuthKitUI
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/URLFormatting.framework/URLFormatting
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3D5A6883-4681-3485-99D4-F521C22113DA
-  Functions: 106
-  Symbols:   173
-  CStrings:  901
+  UUID: DBC2D7E5-F352-3F06-A63B-55A337C86932
+  Functions: 132
+  Symbols:   193
+  CStrings:  1012
 
Symbols:
+ _AKTestLDUID
+ _AKTestSDID
+ _AKTestStableID
+ _AKTestTokenCreationTime
+ _AKTestTokenCreationTimeStampString
+ _AKTestTrustedDeviceId
+ _AKURLBagKeyAsyncPrimaryAppInfoFetchDisabled
+ _AKURLBagNTOAppBundleID
+ _OBJC_CLASS_$_AACustodianController
+ _OBJC_CLASS_$_AAOBTrustedContactListModel
+ _OBJC_CLASS_$_AKProxCustodianRecoveryController
+ _OBJC_CLASS_$_AKSiwACallerInfo
+ _OBJC_CLASS_$_AKSiwAContextInfo
+ _OBJC_CLASS_$_AKSiwADiagnostics
+ _OBJC_CLASS_$_NSCharacterSet
+ _OBJC_METACLASS_$_AKProxCustodianRecoveryController
+ _SOAuthorizationOptionInitiatingAction
+ _SOAuthorizationOptionUserActionInitiated
+ __AKLogNto
+ __dispatch_main_q
+ _dispatch_async
+ _objc_opt_respondsToSelector
+ _objc_unsafeClaimAutoreleasedReturnValue
- _AKTestCriticalStaleContinuationKey
- _AKTestCriticalStaleHBToken
- _AKTestCriticalStalePasswordResetKey
CStrings:
+ "."
+ ".store.apple.com"
+ "/"
+ "00006021-001C10842190C3EE"
+ "00006021-001C10842190C3EE_FC761BB2-009F-47A1-8B1F-AF70A5FE4860"
+ "00006021-001C10842190C3EE_FC761BB2-009F-47A1-8B1F-AF70A5FE4860_1716922707348"
+ "1697054087000.000000"
+ "1729287965219"
+ "@40@0:8@16@24@32"
+ "AKProxCustodianRecoveryController"
+ "Custodian Instruction native take over is on."
+ "Custodian instruction cancelled by user."
+ "Custodian instruction failed with error: %@"
+ "Custodian instruction native take over"
+ "Custodian instruction native take over feature not enabled"
+ "Custodian instruction native take over feature not enabled... legacy path"
+ "Custodian instruction response: %@"
+ "FC761BB2-009F-47A1-8B1F-AF70A5FE4860"
+ "Failed to determine SSO request type: %@"
+ "Failed to fetch nativeTakeoverBundleIDs value from URL bag with error: %@"
+ "Failed to read killswitch from URL bag (error: %@), defaulting to async path."
+ "Fetching app bundle ID for hostName: %@, path: %@"
+ "Found Apple domain bundle ID for subdomain '%@': %@"
+ "Found bundle ID: %@ for hostName: %@ and path: %@"
+ "Hostname is nil, unable to extract bundleID."
+ "No bundle ID configured for Apple subdomain '%@'"
+ "No bundle ID mapping found for hostName: %@ and path: %@"
+ "Primary app info fetch returned non-fatal error, continuing authorization: %@"
+ "SSO Request type: custodian instruction native take over"
+ "Unable to find bundle ID for app: %@"
+ "Unable to find bundle ID for hostName: %@ and path: %@, falling back to default icon"
+ "Value for nativeTakeoverBundleIDs is not dictionary. Skipping custom NTO sheet."
+ "_beginAsyncAuthorizationWithRequest:requestParams:authController:"
+ "_configureProxiedClientBundleIDForContext:path:hostName:"
+ "_extractBundleIDFromConfig:hostName:path:"
+ "_fetchPrimaryApplicationInformationForContext: called with nil requestParameters"
+ "_fetchPrimaryApplicationInformationForContext:requestParameters:completion:"
+ "_handlePasswordReset:request:resetError:response:"
+ "_handlePasswordResetResponse:error:completion:"
+ "_handleRequestType:forRequest:"
+ "_performCustodianInstructionNativeTakeOverWithRequest:"
+ "_proxiedClientAppName"
+ "_proxiedClientBundleID"
+ "_proxiedClientServiceID"
+ "appSSORequestTypeForURL:completion:"
+ "apple.com"
+ "backoffServerInfoConfigOption6"
+ "boolValue"
+ "c12af1946b6e2b21a85896741332124:1697054087000"
+ "callerTeamIdentifier"
+ "canRepairCustodianV2"
+ "characterSetWithCharactersInString:"
+ "com.apple.gs.idms.hb:AAAABLwIAAAAAFiTawwRCmdzLmlkbXMuaGK9AEr1O7ISMGE6QcJKA0fCfvkIIQ7DtQLwTv+kNocsKs3dNKRf7mx806XNTvitHW5RCVRXc0/o0kkyS2x+/NoLMX5cr7AT4fY19m1DhpSYT3rS1KmKDNUd2gAnnp70Ehz3wv4MLmdwlkHNO/LKSbQMLISBNaRXfZBGETUqaNVvj5XT6FQNTzcXdREGGzXzNYfbx/uLVxpzFHUwee1T0tA91onStnNC:1731374674:1697054087000"
+ "configurationValueForKey:fromCache:completion:"
+ "custodianConfigWithInterceptURL:"
+ "custodianInstructionInterceptUrl"
+ "custodianInstructionUrlDisplay"
+ "custodianSetupGracePeriodInSeconds"
+ "displayTrustedContactFlowWithModel:completion:"
+ "fetchPrimaryApplicationInformationForWebServiceWithInfo:completion:"
+ "firstObject"
+ "iCloud domain detected but path is empty, cannot extract app name"
+ "initWithListType:"
+ "initWithOriginURL:redirectURI:clientID:responseMode:proxiedBundleID:proxiedAppName:proxiedServiceID:"
+ "initiatorOrigin"
+ "isCallerManaged"
+ "isCustomNTOSheetEnabled"
+ "isFeatureEnabled:"
+ "localizedCallerDisplayName"
+ "logCaller:"
+ "logContext:"
+ "logResponseWithOrigin:redirectURI:responseMode:hasToken:hasGrantCode:"
+ "maxRepairCountV2"
+ "ownerSetupGracePeriodInSeconds"
+ "path"
+ "presentCustodianInstructionForRequest:completion:"
+ "recoverycode.apple"
+ "setBundleID:"
+ "setCallerBundleID:"
+ "setDisplayName:"
+ "setEntitlementCheckDisabled:"
+ "setFrameID:"
+ "setHasBrowserEntitlement:"
+ "setInitiatingAction:"
+ "setIsManaged:"
+ "setRedirectURI:"
+ "setResponseMode:"
+ "setResponseType:"
+ "setScope:"
+ "setTeamID:"
+ "setUrlParamOrigin:"
+ "setUserActionInitiated:"
+ "setWebKitOrigin:"
+ "stringByTrimmingCharactersInSet:"
+ "testPRKToken"
+ "testPRKToken:1697054087000"
+ "v16@?0@\"NSError\"8"
+ "v24@?0@8@\"NSError\"16"
+ "v24@?0Q8@\"NSError\"16"
+ "v32@0:8Q16@24"
+ "v40@0:8@16@24@32"
+ "v40@0:8@16@24@?32"
- "TEST PRK"
- "com.apple.gs.idms.hb:testHBToken:1731374674:1699724538000"
- "com.apple.gs.idms.hb:testStaleHBToken:1731374674:1699724372000"
- "testCKToken:1699724538000"
- "testPRKToken:1699724538000"
- "testStaleCKToken:1699724372000"
- "testStalePRKToken:1699724372000"

```
