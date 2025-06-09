## AMSAccountAuthenticationPlugin

> `/System/Library/Accounts/Authentication/AMSAccountAuthenticationPlugin.bundle/AMSAccountAuthenticationPlugin`

```diff

-8.5.11.0.0
-  __TEXT.__text: 0x8a58
-  __TEXT.__auth_stubs: 0x4b0
-  __TEXT.__objc_stubs: 0x1fe0
-  __TEXT.__objc_methlist: 0x5cc
+9.0.54.2.1
+  __TEXT.__text: 0x7c4c
+  __TEXT.__auth_stubs: 0x4a0
+  __TEXT.__objc_stubs: 0x1d20
+  __TEXT.__objc_methlist: 0x5a4
   __TEXT.__const: 0xca
-  __TEXT.__cstring: 0x9d2
+  __TEXT.__cstring: 0x942
   __TEXT.__objc_classname: 0x9c
-  __TEXT.__objc_methname: 0x210e
-  __TEXT.__objc_methtype: 0x896
-  __TEXT.__oslogstring: 0x172d
+  __TEXT.__objc_methname: 0x1ed3
+  __TEXT.__objc_methtype: 0x884
+  __TEXT.__oslogstring: 0x1465
   __TEXT.__gcc_except_tab: 0x3c
   __TEXT.__dlopen_cstrs: 0x58
-  __TEXT.__unwind_info: 0x1a8
-  __DATA_CONST.__auth_got: 0x268
-  __DATA_CONST.__got: 0x1a8
-  __DATA_CONST.__const: 0x528
-  __DATA_CONST.__cfstring: 0x940
+  __TEXT.__unwind_info: 0x190
+  __DATA_CONST.__auth_got: 0x260
+  __DATA_CONST.__got: 0x178
+  __DATA_CONST.__const: 0x4a0
+  __DATA_CONST.__cfstring: 0x920
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA.__objc_const: 0x808
-  __DATA.__objc_selrefs: 0x9b8
+  __DATA.__objc_selrefs: 0x908
   __DATA.__objc_ivar: 0x24
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x180

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
-  - /usr/lib/swift/libswiftCoreMIDI.dylib
-  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 2D725CF4-9FB8-3EA8-B976-EFA27FD386F2
-  Functions: 102
-  Symbols:   165
-  CStrings:  652
+  UUID: 4CDAC0AA-B4D7-3C5D-8E58-2E5E7D563AAA
+  Functions: 93
+  Symbols:   156
+  CStrings:  619
 
Symbols:
+ _OBJC_CLASS_$_AMSAccountPostSignInService
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftOSLog
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- _OBJC_CLASS_$_AMSAccountCachedServerData
- _OBJC_CLASS_$_AMSAccountDeviceInfoTask
- _OBJC_CLASS_$_AMSBinaryPromise
- _OBJC_CLASS_$_AMSDeviceAccountPrivacyAcknowledgementTask
- _OBJC_CLASS_$_AMSEngagement
- _OBJC_CLASS_$_AMSMutablePromise
- _OBJC_CLASS_$_AMSSignOutTask
- __swift_FORCE_LOAD_$_swiftCoreMIDI
- __swift_FORCE_LOAD_$_swiftCryptoTokenKit
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd
- _objc_retainAutoreleaseReturnValue
CStrings:
+ "%{public}@: [%{public}@] Processing Account"
+ "performPostSignInTasksInDaemonForAccount:credentialSource:"
- "%{public}@: [%{public}@] Account save failed with error %{public}@"
- "%{public}@: [%{public}@] Auth completed without prompt, no data sync for authenticatedAccount = %{public}@"
- "%{public}@: [%{public}@] Device doesn't meet requirments for device account info gdpr evaluation authenticatedAccount = %{public}@"
- "%{public}@: [%{public}@] Evaluating device account gdpr requirements for authenticatedAccount = %{public}@"
- "%{public}@: [%{public}@] Failed to sign out of account that has failed to meet GDPR requirements for this device. Signout error: %{public}@"
- "%{public}@: [%{public}@] Loud auth completed, will sync data for authenticatedAccount = %{public}@"
- "%{public}@: [%{public}@] Successfully authenticated the account but required GDPR acknowledgment missing"
- "@\"AMSBinaryPromise\"16@?0@\"ACAccount\"8"
- "@40@0:8@16@24@?32"
- "Authentication cancelled due to missing gdpr requirement"
- "_handleBundleGDPRRequirementsForAuthenticatedAccount:task:gdprFailureAction:"
- "_processAccountDeviceRequirementsForAutheniticatedAccount:accountStore:bag:"
- "_shouldUpdateBundleOwnerStatusForAccount:"
- "_startDataSyncForAccount:"
- "accountAuthSyncForAccountID:"
- "ams_isBundleOwner"
- "ams_saveAccount:withOptions:"
- "arrayWithObjects:count:"
- "deviceIsBundle"
- "didFetchBundleOwnerStatus"
- "fetchMetricsIdentifiers"
- "finishWithError:"
- "finishWithPromise:"
- "finishWithResult:"
- "initWithAccount:accountStore:bag:"
- "initWithAccounts:"
- "initWithoutBag"
- "isDirty"
- "performPrivacyAcknowledgement"
- "promiseWithSuccess"
- "setDidFetchBundleOwnerStatus:"
- "sharedAccountsConfig"
- "sharedInstance"
- "v24@?0@\"AMSAccountDeviceInfoResult\"8@\"NSError\"16"

```
