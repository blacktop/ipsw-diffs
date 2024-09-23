## AppleIDSSOAuthentication

> `/System/Library/PrivateFrameworks/AppleIDSSOAuthentication.framework/AppleIDSSOAuthentication`

```diff

-104.0.0.0.0
-  __TEXT.__text: 0x2cdd8
-  __TEXT.__auth_stubs: 0x530
-  __TEXT.__objc_methlist: 0x540
-  __TEXT.__const: 0xe20
-  __TEXT.__cstring: 0x334
-  __TEXT.__oslogstring: 0xbc3
-  __TEXT.__gcc_except_tab: 0x254
-  __TEXT.__unwind_info: 0x248
-  __TEXT.__objc_classname: 0xed
-  __TEXT.__objc_methname: 0x15da
-  __TEXT.__objc_methtype: 0x3ea
-  __TEXT.__objc_stubs: 0x1000
-  __DATA_CONST.__got: 0x120
-  __DATA_CONST.__const: 0x568
-  __DATA_CONST.__objc_classlist: 0x28
-  __DATA_CONST.__objc_catlist: 0x18
+104.100.1.0.0
+  __TEXT.__text: 0x2ff7c
+  __TEXT.__auth_stubs: 0x540
+  __TEXT.__objc_methlist: 0x5f0
+  __TEXT.__const: 0xd10
+  __TEXT.__cstring: 0x78c
+  __TEXT.__oslogstring: 0xc56
+  __TEXT.__gcc_except_tab: 0x274
+  __TEXT.__unwind_info: 0x278
+  __TEXT.__objc_classname: 0x108
+  __TEXT.__objc_methname: 0x1957
+  __TEXT.__objc_methtype: 0x44a
+  __TEXT.__objc_stubs: 0x1280
+  __DATA_CONST.__got: 0x170
+  __DATA_CONST.__const: 0x600
+  __DATA_CONST.__objc_classlist: 0x30
+  __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x540
+  __DATA_CONST.__objc_selrefs: 0x5e0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x2a8
-  __AUTH_CONST.__const: 0x4410
-  __AUTH_CONST.__cfstring: 0x400
-  __AUTH_CONST.__objc_const: 0xe18
-  __DATA.__objc_ivar: 0x58
+  __AUTH_CONST.__auth_got: 0x2b0
+  __AUTH_CONST.__const: 0x4af0
+  __AUTH_CONST.__cfstring: 0x660
+  __AUTH_CONST.__objc_const: 0xf08
+  __AUTH_CONST.__objc_intobj: 0x18
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0x5c
   __DATA.__data: 0x280
-  __DATA.__bss: 0x40
+  __DATA.__bss: 0x50
   __DATA.__common: 0x61
   __DATA_DIRTY.__objc_data: 0x190
   __DATA_DIRTY.__bss: 0x40

   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 173
-  Symbols:   357
-  CStrings:  401
+  Functions: 188
+  Symbols:   405
+  CStrings:  451
 
Symbols:
+ _kAIDASignInStartTelemetryEventNameFaceTime
+ _kAIDASignInStartTelemetryEventNameGameCenter
+ _kAIDASignInTelemetryEventNameGameCenter
+ _AKAuthenticationDSIDKey
+ _kAIDASignInFinishTelemetryEventNameiCloud
+ _kAIDASignInStartTelemetryEventNameUnknown
+ _kAAFFlowIdString
+ _AKAuthenticationAlternateDSIDKey
+ _kAIDASignInTelemetryEventNameiCloud
+ _OBJC_CLASS_$_AIDAAnalyticsReporterRTC
+ _kAIDASignInTelemetryEventNameMessages
+ _kAIDASignInTelemetryEventNameFaceTime
+ _kAIDASignInStartTelemetryEventNameStore
+ _OBJC_CLASS_$_AKAccountManager
+ _kAIDARTCClientType
+ _OBJC_CLASS_$_AAFAnalyticsTransportRTC
+ _OBJC_CLASS_$_NSBundle
+ _OBJC_METACLASS_$_AIDAAnalyticsReporterRTC
+ _kAIDASignInFinishTelemetryEventNameStore
+ _kAIDASignInFinishTelemetryEventNameFaceTime
+ _kAAFDeviceSessionIdString
+ _kAIDASignInTelemetryEventNameStore
+ _kAIDASignInFinishTelemetryEventNameGameCenter
+ _objc_retain_x6
+ _kAIDASignInFinishTelemetryEventNameUnknown
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _kAIDASignInStartTelemetryEventNameiCloud
+ _kAIDASignInTelemetryEventNameUnknown
+ _kAAFDidSucceed
+ _kAIDASignInStartTelemetryEventNameMessages
+ _kAIDARTCClientName
+ _kAIDASignInFinishTelemetryEventNameMessages
+ _AKAuthenticationTelemetryFlowID
+ __AKLogSystem
- _objc_retain_x27
CStrings:
+ "@40@0:8@16@24@32"
+ "com.apple.appleidauthentication.sign-in-service.start.Store"
+ "com.apple.appleidauthentication.sign-in-service.GameCenter"
+ "aida_updateTelemetryIdsWithAuthenticationResults:accountManager:"
+ "v28@0:8B16@20"
+ "com.apple.appleidauthentication.sign-in-service.finish.GameCenter"
+ "com.apple.appleidauthentication.sign-in-service.finish.iCloud"
+ "Error getting account from auth results during sign-in for telemetry, not updating analytics event with nil account"
+ "aida_analyticsDurationEventForAIDAServiceType:accountManager:authenticationResults:"
+ "authKitAccountWithAltDSID:error:"
+ "finishEventNameForService:"
+ "authKitAccountWithDSID:"
+ "sharedTelemetryReporter"
+ "accountForAuthenticationResults:accountManager:"
+ "com.apple.appleidauthentication.sign-in-service.FaceTime"
+ "com.apple.appleidauthentication.sign-in-service.start.GameCenter"
+ "startEventNameForService:"
+ "com.apple.appleidauthentication.sign-in-service.finish.Messages"
+ "com.apple.aaa.dnu"
+ "_reporter"
+ "com.apple.appleidauthentication.sign-in-service.finish.Unknown"
+ "com.apple.appleidauthentication.sign-in-service.start.Messages"
+ "\x13"
+ "@\"AAFAnalyticsTransportRTC\""
+ "analyticsTransportRTCWithClientType:clientBundleId:clientName:"
+ "eventNameForService:"
+ "com.apple.appleidauthentication.sign-in-service.Unknown"
+ "i"
+ "aida_analyticsFinishEventForAIDAServiceType:accountManager:authenticationResults:success:error:"
+ "com.apple.appleidauthentication.sign-in-service.finish.Store"
+ "com.apple.appleidauthentication.sign-in-service.iCloud"
+ "initWithEventName:eventCategory:initData:"
+ "com.apple.appleidauthentication.sign-in-service.Store"
+ "com.apple.appleidauthentication.sign-in-service.start.Unknown"
+ "com.apple.appleidauthentication.sign-in-service.start.FaceTime"
+ "aida_analyticsEventWithEventName:accountManager:authenticationResults:"
+ "aida_updateEventWithSuccess:error:"
+ "v32@0:8@16@24"
+ "com.apple.appleidauthentication.sign-in-service.start.iCloud"
+ "mainBundle"
+ "@52@0:8@16@24@32B40@44"
+ "aida_analyticsEventWithEventName:"
+ "AIDAAnalyticsReporterRTC"
+ "sharedInstance"
+ "com.apple.appleidauthentication.sign-in-service.Messages"
+ "populateUnderlyingErrorsStartingWithRootError:"
+ "aida_analyticsStartEventForAIDAServiceType:accountManager:authenticationResults:"
+ "telemetryDeviceSessionIDForAccount:"
+ "Error fetching IdMS account:%!@(MISSING)"
+ "com.apple.appleidauthentication.sign-in-service.finish.FaceTime"

```
