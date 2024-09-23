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
+ _AKAuthenticationTelemetryFlowID
+ _OBJC_CLASS_$_AIDAAnalyticsReporterRTC
+ _kAIDASignInTelemetryEventNameStore
+ _AKAuthenticationAlternateDSIDKey
+ _kAAFDidSucceed
+ _kAAFDeviceSessionIdString
+ _kAIDASignInFinishTelemetryEventNameiCloud
+ _kAIDASignInTelemetryEventNameUnknown
+ _kAIDASignInTelemetryEventNameFaceTime
+ _OBJC_CLASS_$_AKAccountManager
+ _kAIDASignInStartTelemetryEventNameGameCenter
+ _OBJC_METACLASS_$_AIDAAnalyticsReporterRTC
+ _kAIDASignInStartTelemetryEventNameiCloud
+ _kAIDASignInStartTelemetryEventNameUnknown
+ _kAIDARTCClientType
+ _kAIDASignInFinishTelemetryEventNameFaceTime
+ _OBJC_CLASS_$_AAFAnalyticsTransportRTC
+ _kAIDASignInStartTelemetryEventNameMessages
+ _kAIDASignInFinishTelemetryEventNameMessages
+ _kAIDASignInFinishTelemetryEventNameStore
+ _AKAuthenticationDSIDKey
+ _kAIDASignInStartTelemetryEventNameFaceTime
+ _kAIDASignInTelemetryEventNameMessages
+ _kAIDARTCClientName
+ _kAIDASignInTelemetryEventNameiCloud
+ _kAIDASignInStartTelemetryEventNameStore
+ _OBJC_CLASS_$_NSBundle
+ _kAIDASignInTelemetryEventNameGameCenter
+ _kAIDASignInFinishTelemetryEventNameUnknown
+ __AKLogSystem
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _kAIDASignInFinishTelemetryEventNameGameCenter
+ _kAAFFlowIdString
+ _objc_retain_x6
- _objc_retain_x27
CStrings:
+ "v28@0:8B16@20"
+ "com.apple.appleidauthentication.sign-in-service.start.Unknown"
+ "aida_updateEventWithSuccess:error:"
+ "com.apple.appleidauthentication.sign-in-service.start.Messages"
+ "@\"AAFAnalyticsTransportRTC\""
+ "aida_updateTelemetryIdsWithAuthenticationResults:accountManager:"
+ "com.apple.appleidauthentication.sign-in-service.FaceTime"
+ "Error fetching IdMS account:%!@(MISSING)"
+ "initWithEventName:eventCategory:initData:"
+ "aida_analyticsStartEventForAIDAServiceType:accountManager:authenticationResults:"
+ "eventNameForService:"
+ "com.apple.appleidauthentication.sign-in-service.Store"
+ "populateUnderlyingErrorsStartingWithRootError:"
+ "sharedTelemetryReporter"
+ "com.apple.appleidauthentication.sign-in-service.finish.iCloud"
+ "com.apple.appleidauthentication.sign-in-service.start.FaceTime"
+ "aida_analyticsEventWithEventName:accountManager:authenticationResults:"
+ "@40@0:8@16@24@32"
+ "com.apple.appleidauthentication.sign-in-service.GameCenter"
+ "sharedInstance"
+ "telemetryDeviceSessionIDForAccount:"
+ "com.apple.appleidauthentication.sign-in-service.finish.Store"
+ "com.apple.appleidauthentication.sign-in-service.Unknown"
+ "com.apple.appleidauthentication.sign-in-service.finish.Unknown"
+ "AIDAAnalyticsReporterRTC"
+ "aida_analyticsEventWithEventName:"
+ "finishEventNameForService:"
+ "@52@0:8@16@24@32B40@44"
+ "com.apple.appleidauthentication.sign-in-service.Messages"
+ "com.apple.appleidauthentication.sign-in-service.finish.FaceTime"
+ "\x13"
+ "_reporter"
+ "authKitAccountWithAltDSID:error:"
+ "mainBundle"
+ "Error getting account from auth results during sign-in for telemetry, not updating analytics event with nil account"
+ "i"
+ "aida_analyticsDurationEventForAIDAServiceType:accountManager:authenticationResults:"
+ "aida_analyticsFinishEventForAIDAServiceType:accountManager:authenticationResults:success:error:"
+ "com.apple.appleidauthentication.sign-in-service.start.iCloud"
+ "com.apple.appleidauthentication.sign-in-service.start.GameCenter"
+ "com.apple.aaa.dnu"
+ "com.apple.appleidauthentication.sign-in-service.iCloud"
+ "authKitAccountWithDSID:"
+ "com.apple.appleidauthentication.sign-in-service.finish.Messages"
+ "com.apple.appleidauthentication.sign-in-service.start.Store"
+ "v32@0:8@16@24"
+ "accountForAuthenticationResults:accountManager:"
+ "analyticsTransportRTCWithClientType:clientBundleId:clientName:"
+ "startEventNameForService:"
+ "com.apple.appleidauthentication.sign-in-service.finish.GameCenter"

```
