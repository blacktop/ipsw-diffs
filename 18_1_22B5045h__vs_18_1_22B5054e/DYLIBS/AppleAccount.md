## AppleAccount

> `/System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount`

```diff

-1007.100.1.1.0
-  __TEXT.__text: 0xbfba4
+1007.100.5.0.0
+  __TEXT.__text: 0xc30e4
   __TEXT.__auth_stubs: 0xaa0
-  __TEXT.__objc_methlist: 0x9054
-  __TEXT.__const: 0x1b00
-  __TEXT.__cstring: 0xbd6e
-  __TEXT.__oslogstring: 0xdb18
-  __TEXT.__gcc_except_tab: 0x21a0
+  __TEXT.__objc_methlist: 0x90c4
+  __TEXT.__const: 0x19f0
+  __TEXT.__cstring: 0xbe98
+  __TEXT.__oslogstring: 0xdbb0
+  __TEXT.__gcc_except_tab: 0x21c8
   __TEXT.__dlopen_cstrs: 0x2d9
-  __TEXT.__unwind_info: 0x2520
-  __TEXT.__objc_classname: 0x1c59
-  __TEXT.__objc_methname: 0x1371f
+  __TEXT.__unwind_info: 0x2538
+  __TEXT.__objc_classname: 0x1c57
+  __TEXT.__objc_methname: 0x1386f
   __TEXT.__objc_methtype: 0x2a62
-  __TEXT.__objc_stubs: 0xaf40
-  __DATA_CONST.__got: 0xc00
-  __DATA_CONST.__const: 0x31b8
+  __TEXT.__objc_stubs: 0xafc0
+  __DATA_CONST.__got: 0xc08
+  __DATA_CONST.__const: 0x3260
   __DATA_CONST.__objc_classlist: 0x740
   __DATA_CONST.__objc_catlist: 0x98
   __DATA_CONST.__objc_protolist: 0x150
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4508
+  __DATA_CONST.__objc_selrefs: 0x4538
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x520
   __DATA_CONST.__objc_arraydata: 0xc0
   __AUTH_CONST.__auth_got: 0x560
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x4f00
-  __AUTH_CONST.__cfstring: 0xb200
-  __AUTH_CONST.__objc_const: 0x21400
+  __AUTH_CONST.__const: 0x55c0
+  __AUTH_CONST.__cfstring: 0xb2a0
+  __AUTH_CONST.__objc_const: 0x21a60
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH.__objc_data: 0x140
-  __DATA.__objc_ivar: 0xb08
+  __DATA.__objc_ivar: 0xb10
   __DATA.__data: 0x12a0
   __DATA.__bss: 0x358
   __DATA.__common: 0x69

   - /System/Library/Frameworks/MobileCoreServices.framework/MobileCoreServices
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/AAAFoundation.framework/AAAFoundation
+  - /System/Library/PrivateFrameworks/AAAFoundationSwift.framework/AAAFoundationSwift
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/AppleIDSSOAuthentication.framework/AppleIDSSOAuthentication
   - /System/Library/PrivateFrameworks/ApplePushService.framework/ApplePushService

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3905
-  Symbols:   5489
-  CStrings:  6541
+  Functions: 3942
+  Symbols:   5507
+  CStrings:  6559
 
Symbols:
+ _kInheritanceCleanupStaleRecordsEventName
+ _kAAAnalyticsEventCustodianRecovery
+ _OBJC_CLASS_$_AAFExponentialRetryScheduler
CStrings:
+ "CustodianRecoveryRequestContext with ownerAppleID: %!@(MISSING) \nsessionID: %!@(MISSING) \nrecoveryCode: %!@(MISSING) \ncustodianUUID: %!@(MISSING) \nrecoveryToken: %!@(MISSING) \ncliMode: %!i(MISSING) \ndataOnly: %!@(MISSING), recordBuildVersion: %!@(MISSING), flowID: %!@(MISSING), altDSID: %!@(MISSING)"
+ "_retryingGenerateCustodianRecoveryCodeWithContext:completion:"
+ "isLCDeletionChangeCKStatusToDeclinedEnabled"
+ "com.apple.appleaccount.CustodianRecovery"
+ "_telemetryFlowID"
+ "Scheduling validate recovery code through retry scheduler"
+ "T@\"NSString\",C,N,V_telemetryFlowID"
+ "com.apple.appleaccount.inheritance.cleanupStaleRecords"
+ "appleaccount-legacycontact-onboarding"
+ "accessibilityIdentifier"
+ "v24@?0@8@\"NSError\"16"
+ "v16@?0@?<v@?@@\"NSError\">8"
+ "scheduleTask:shouldRetry:completionHandler:"
+ "Cannot call daemon to generate custodian recovery code as custodian controller is deallocated"
+ "LCDeletionChangeCKStatusToDeclined"
+ "initWithMaxRetries:"
+ "appleaccount-recoverycontact-onboarding"
+ "setAccessibilityIdentifier:"
+ "_retryingValidateCustodianRecoveryCodeWithContext:completion:"
- "\x16"
- "CustodianRecoveryRequestContext with ownerAppleID: %!@(MISSING) \nsessionID: %!@(MISSING) \nrecoveryCode: %!@(MISSING) \ncustodianUUID: %!@(MISSING) \nrecoveryToken: %!@(MISSING) \ncliMode: %!i(MISSING) \ndataOnly: %!@(MISSING), recordBuildVersion: %!@(MISSING)"

```
