## CoreCDP

> `/System/Library/PrivateFrameworks/CoreCDP.framework/Versions/A/CoreCDP`

```diff

-447.0.0.0.0
-  __TEXT.__text: 0x51d18
-  __TEXT.__objc_methlist: 0x3a84
-  __TEXT.__const: 0x1484
+448.125.5.1.0
+  __TEXT.__text: 0x52004
+  __TEXT.__objc_methlist: 0x3abc
+  __TEXT.__const: 0x14dc
   __TEXT.__gcc_except_tab: 0x1114
   __TEXT.__oslogstring: 0x91f1
-  __TEXT.__cstring: 0x655d
+  __TEXT.__cstring: 0x6645
   __TEXT.__dlopen_cstrs: 0x12e
   __TEXT.__ustring: 0x28
-  __TEXT.__unwind_info: 0x20a0
+  __TEXT.__unwind_info: 0x20b0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1ea0
+  __DATA_CONST.__const: 0x1eb8
   __DATA_CONST.__objc_classlist: 0x1a8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x21c0
+  __DATA_CONST.__objc_selrefs: 0x21e0
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0xe8
   __DATA_CONST.__objc_arraydata: 0x168
   __DATA_CONST.__got: 0x4f8
   __AUTH_CONST.__const: 0x1930
-  __AUTH_CONST.__cfstring: 0x3f40
-  __AUTH_CONST.__objc_const: 0x8838
+  __AUTH_CONST.__cfstring: 0x4000
+  __AUTH_CONST.__objc_const: 0x8868
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH_CONST.__auth_got: 0x778
   __DATA.__objc_ivar: 0x300
-  __DATA.__data: 0x1178
+  __DATA.__data: 0x11a0
   __DATA.__common: 0x20
   __DATA_DIRTY.__objc_data: 0x1090
   __DATA_DIRTY.__data: 0x8

   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2435
-  Symbols:   4702
-  CStrings:  1637
+  Functions: 2438
+  Symbols:   4721
+  CStrings:  1645
 
Symbols:
+ +[CDPUtilities isDBRHealingEnabled]
+ +[CDPUtilities isDBRInlineSignInHealEnabled]
+ +[CDPUtilities isEntitlementEnforcementEnabled]
+ -[AAFAnalyticsEvent(CDP) populateDBRDetectionDetailWithRemainingAttempts:detectionError:]
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_AAFAnalyticsEvent_$_CDP
+ ___der_key_state_abs_last_mesa_auth
+ ___der_key_state_abs_last_mesa_unlock
+ ___der_key_state_abs_last_passcode_auth
+ ___der_key_state_abs_last_passcode_unlock
+ ___der_key_state_abs_lock_time
+ _der_key_state_abs_last_mesa_auth
+ _der_key_state_abs_last_mesa_unlock
+ _der_key_state_abs_last_passcode_auth
+ _der_key_state_abs_last_passcode_unlock
+ _der_key_state_abs_lock_time
+ _kCDPAnalyticsPDPRecordGenerationAheadEvent
+ _kCDPAnalyticsPDPRecordGenerationCheckSkippedEvent
+ _kCDPAnalyticsPDPWrappingKeyRepairEvent
+ _objc_msgSend$isDBRHealingEnabled
CStrings:
+ "DBRHealing"
+ "DBRHealingEnabled"
+ "DBRInlineSignInHeal"
+ "DBRInlineSignInHealEnabled"
+ "EnforceCDPDEntitlements"
+ "com.apple.corecdp.pdpRecordGenerationAhead"
+ "com.apple.corecdp.pdpRecordGenerationCheckSkipped"
+ "com.apple.corecdp.pdpWrappingKeyRepair"
```
