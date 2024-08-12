## CoreCDPInternal

> `/System/Library/PrivateFrameworks/CoreCDPInternal.framework/CoreCDPInternal`

```diff

-382.0.0.0.0
-  __TEXT.__text: 0x79080
-  __TEXT.__auth_stubs: 0x10d0
-  __TEXT.__objc_methlist: 0x3eb8
+383.2.0.0.0
+  __TEXT.__text: 0x7a7d0
+  __TEXT.__auth_stubs: 0x10c0
+  __TEXT.__objc_methlist: 0x3f50
   __TEXT.__const: 0x534
-  __TEXT.__oslogstring: 0x10fae
-  __TEXT.__cstring: 0x5d0c
-  __TEXT.__gcc_except_tab: 0x7d0
+  __TEXT.__oslogstring: 0x1127e
+  __TEXT.__cstring: 0x5ebc
+  __TEXT.__gcc_except_tab: 0x800
   __TEXT.__dlopen_cstrs: 0xb0
   __TEXT.__swift5_typeref: 0x2e2
   __TEXT.__swift5_fieldmd: 0x64

   __TEXT.__swift5_proto: 0x28
   __TEXT.__swift5_types: 0x14
   __TEXT.__swift5_capture: 0x1b8
-  __TEXT.__unwind_info: 0x18d8
+  __TEXT.__unwind_info: 0x1928
   __TEXT.__eh_frame: 0x890
   __TEXT.__objc_classname: 0xbe3
-  __TEXT.__objc_methname: 0xd460
-  __TEXT.__objc_methtype: 0x2434
-  __TEXT.__objc_stubs: 0xad40
-  __DATA_CONST.__got: 0xee8
-  __DATA_CONST.__const: 0x1df0
+  __TEXT.__objc_methname: 0xd682
+  __TEXT.__objc_methtype: 0x248a
+  __TEXT.__objc_stubs: 0xaf40
+  __DATA_CONST.__got: 0xef8
+  __DATA_CONST.__const: 0x1e28
   __DATA_CONST.__objc_classlist: 0x268
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x158
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3068
+  __DATA_CONST.__objc_selrefs: 0x30f0
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x158
-  __DATA_CONST.__objc_arraydata: 0x68
-  __AUTH_CONST.__auth_got: 0x878
+  __DATA_CONST.__objc_arraydata: 0x70
+  __AUTH_CONST.__auth_got: 0x870
   __AUTH_CONST.__auth_ptr: 0x178
-  __AUTH_CONST.__const: 0x8b8
-  __AUTH_CONST.__cfstring: 0x4100
-  __AUTH_CONST.__objc_const: 0x107b8
+  __AUTH_CONST.__const: 0x898
+  __AUTH_CONST.__cfstring: 0x41e0
+  __AUTH_CONST.__objc_const: 0x10818
   __AUTH_CONST.__objc_intobj: 0x150
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0x1088
   __AUTH.__data: 0x88
-  __DATA.__objc_ivar: 0x388
+  __DATA.__objc_ivar: 0x38c
   __DATA.__data: 0x1190
   __DATA.__bss: 0x530
   __DATA.__common: 0x18

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 2620
-  Symbols:   3387
-  CStrings:  4192
+  Functions: 2650
+  Symbols:   3424
+  CStrings:  4237
 
Symbols:
+ _CDP_FOLLOWUP_ADP_STATE_HEALING
+ _FLNotificationOptionBannerAlert
+ _kADPDeepLinkUrl
+ _kADPStateHealingActionContinue
+ _kADPStateHealingItemIdentifier
- _dlopen
CStrings:
+ "\"%!@(MISSING): Do not override CDPContextType=%!l(MISSING)d\""
+ "\"Account not eligible, cannot fetch walrus matched status: %!@(MISSING)\""
+ "\"Did Clear Pending ADPStateHealing CFU? %!d(MISSING) with error: %!@(MISSING)\""
+ "\"Dropped keys successfully, this error means success for mismatched state\""
+ "\"Failed to fetch any pending CFUs, error: %!{(MISSING)public}@\""
+ "\"Failed to fetch walrus combined status with error code: %!z(MISSING)d, error: %!@(MISSING)\""
+ "\"Found CFU with uniqueIdentifier %!@(MISSING)\""
+ "\"No Pending ADPStateHealing CFU found. Continuing to Return combined walrus status\""
+ "\"No eligible primary account found, cannot fetch walrus matched status: %!@(MISSING)\""
+ "\"Pending ADPStateHealing CFU found. Dismissing...\""
+ "\"Walrus combined status %!@(MISSING) status fetched successfully.\""
+ "\"Walrus octagon state error: %!@(MISSING)\""
+ "\"Walrus state mismatch NOT detected. Checking if there is a pending ADPStateHealing CFU posted...\""
+ "\"Walrus state mismatch detected\""
+ "\"Walrus state: %!@(MISSING)\""
+ "\"Walrus stingray state error: %!@(MISSING)\""
+ "/AppleInternal/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication"
+ "/System/Library/PrivateFrameworks/LocalAuthentication.framework/LocalAuthentication"
+ "@\"LAEnvironment\""
+ "ADP_STATE_HEALING_CFU_TEXT"
+ "ADP_STATE_HEALING_CFU_TITLE"
+ "ADP_STATE_HEALING_NOTIFICATION_TEXT"
+ "CONTINUE"
+ "LAEnvironment"
+ "T@\"LAEnvironment\",&,N,V_currentUser"
+ "Vv32@0:8@\"CDPContext\"16@?<v@?@\"CDPCombinedWalrusStatus\"@\"NSError\">24"
+ "_adpStateHealingFollowUpAction"
+ "_combinedWalrusStatusForPrimaryAccountWithError:"
+ "_combinedWalrusStatusWithContext:error:"
+ "_combinedWalrusStatusWithOptions:context:error:"
+ "_currentUser"
+ "_followUpForADPStateHealingWithContext:"
+ "_isBiometricAuthEnrolledWithLAEnvironment:"
+ "biometry"
+ "com.apple.CDPFollowUpIdentifier.adpStateHealing"
+ "com.apple.cdp.adpStateHealing.continue"
+ "combinedWalrusStatusWithContext:completion:"
+ "combinedWalrusStatusWithContext:error:"
+ "contextForADPStateHealing"
+ "currentUser"
+ "hasPendingFollowUpWithUniqueIdentifier:"
+ "isEnrolled"
+ "isSubsetOfContextTypeSignIn:"
+ "mismatchDetected"
+ "pendingFollowUpItems:"
+ "prefs:root=APPLE_ACCOUNT&path=ICLOUD_SERVICE/ICLOUD_ADP_SPECIFIER_NAME"
+ "setCurrentUser:"
+ "state"
- "\"Default to older behaviour until we are confident about correctness of this Keychain feature\""
- "\"Detected internal build...Enabling privacy compliant Keychain flow\""
- "canEvaluatePolicy:error:"

```
