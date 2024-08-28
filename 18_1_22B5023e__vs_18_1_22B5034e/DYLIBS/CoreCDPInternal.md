## CoreCDPInternal

> `/System/Library/PrivateFrameworks/CoreCDPInternal.framework/CoreCDPInternal`

```diff

-383.0.0.0.0
-  __TEXT.__text: 0x795ec
+383.2.0.0.0
+  __TEXT.__text: 0x7a7d0
   __TEXT.__auth_stubs: 0x10c0
-  __TEXT.__objc_methlist: 0x3ee8
+  __TEXT.__objc_methlist: 0x3f50
   __TEXT.__const: 0x534
-  __TEXT.__oslogstring: 0x10f2e
-  __TEXT.__cstring: 0x5dbc
+  __TEXT.__oslogstring: 0x1127e
+  __TEXT.__cstring: 0x5ebc
   __TEXT.__gcc_except_tab: 0x800
   __TEXT.__dlopen_cstrs: 0xb0
   __TEXT.__swift5_typeref: 0x2e2

   __TEXT.__swift5_proto: 0x28
   __TEXT.__swift5_types: 0x14
   __TEXT.__swift5_capture: 0x1b8
-  __TEXT.__unwind_info: 0x1910
+  __TEXT.__unwind_info: 0x1928
   __TEXT.__eh_frame: 0x890
   __TEXT.__objc_classname: 0xbe3
-  __TEXT.__objc_methname: 0xd4f6
-  __TEXT.__objc_methtype: 0x2445
-  __TEXT.__objc_stubs: 0xade0
-  __DATA_CONST.__got: 0xee8
-  __DATA_CONST.__const: 0x1e10
+  __TEXT.__objc_methname: 0xd682
+  __TEXT.__objc_methtype: 0x248a
+  __TEXT.__objc_stubs: 0xaf40
+  __DATA_CONST.__got: 0xef8
+  __DATA_CONST.__const: 0x1e28
   __DATA_CONST.__objc_classlist: 0x268
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x158
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3098
+  __DATA_CONST.__objc_selrefs: 0x30f0
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x158
-  __DATA_CONST.__objc_arraydata: 0x68
+  __DATA_CONST.__objc_arraydata: 0x70
   __AUTH_CONST.__auth_got: 0x870
   __AUTH_CONST.__auth_ptr: 0x178
   __AUTH_CONST.__const: 0x898
-  __AUTH_CONST.__cfstring: 0x4100
-  __AUTH_CONST.__objc_const: 0x107f8
+  __AUTH_CONST.__cfstring: 0x41e0
+  __AUTH_CONST.__objc_const: 0x10818
   __AUTH_CONST.__objc_intobj: 0x150
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0x1088

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 2630
-  Symbols:   3396
-  CStrings:  4203
+  Functions: 2650
+  Symbols:   3424
+  CStrings:  4237
 
Symbols:
+ _kADPStateHealingActionContinue
+ _kADPStateHealingItemIdentifier
+ _FLNotificationOptionBannerAlert
+ _kADPDeepLinkUrl
+ _CDP_FOLLOWUP_ADP_STATE_HEALING
CStrings:
+ "\"Account not eligible, cannot fetch walrus matched status: %!@(MISSING)\""
+ "ADP_STATE_HEALING_CFU_TITLE"
+ "\"Found CFU with uniqueIdentifier %!@(MISSING)\""
+ "\"No eligible primary account found, cannot fetch walrus matched status: %!@(MISSING)\""
+ "combinedWalrusStatusWithContext:error:"
+ "ADP_STATE_HEALING_CFU_TEXT"
+ "\"Walrus state mismatch NOT detected. Checking if there is a pending ADPStateHealing CFU posted...\""
+ "\"Pending ADPStateHealing CFU found. Dismissing...\""
+ "pendingFollowUpItems:"
+ "_adpStateHealingFollowUpAction"
+ "ADP_STATE_HEALING_NOTIFICATION_TEXT"
+ "_followUpForADPStateHealingWithContext:"
+ "prefs:root=APPLE_ACCOUNT&path=ICLOUD_SERVICE/ICLOUD_ADP_SPECIFIER_NAME"
+ "_combinedWalrusStatusWithOptions:context:error:"
+ "com.apple.CDPFollowUpIdentifier.adpStateHealing"
+ "_combinedWalrusStatusForPrimaryAccountWithError:"
+ "contextForADPStateHealing"
+ "_combinedWalrusStatusWithContext:error:"
+ "Vv32@0:8@\"CDPContext\"16@?<v@?@\"CDPCombinedWalrusStatus\"@\"NSError\">24"
+ "combinedWalrusStatusWithContext:completion:"
+ "\"Walrus state mismatch detected\""
+ "\"Walrus octagon state error: %!@(MISSING)\""
+ "\"Walrus state: %!@(MISSING)\""
+ "hasPendingFollowUpWithUniqueIdentifier:"
+ "\"Dropped keys successfully, this error means success for mismatched state\""
+ "CONTINUE"
+ "mismatchDetected"
+ "\"Failed to fetch any pending CFUs, error: %!{(MISSING)public}@\""
+ "\"No Pending ADPStateHealing CFU found. Continuing to Return combined walrus status\""
+ "\"Walrus stingray state error: %!@(MISSING)\""
+ "\"Walrus combined status %!@(MISSING) status fetched successfully.\""
+ "com.apple.cdp.adpStateHealing.continue"
+ "\"Did Clear Pending ADPStateHealing CFU? %!d(MISSING) with error: %!@(MISSING)\""
+ "\"Failed to fetch walrus combined status with error code: %!z(MISSING)d, error: %!@(MISSING)\""

```
