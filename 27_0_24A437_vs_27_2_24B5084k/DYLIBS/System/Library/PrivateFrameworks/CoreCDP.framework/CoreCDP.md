## CoreCDP

> `/System/Library/PrivateFrameworks/CoreCDP.framework/CoreCDP`

```diff

-447.0.0.0.0
-  __TEXT.__text: 0x4e618
-  __TEXT.__objc_methlist: 0x3a74
-  __TEXT.__const: 0x147c
+448.125.5.1.0
+  __TEXT.__text: 0x4e8f8
+  __TEXT.__objc_methlist: 0x3aac
+  __TEXT.__const: 0x14d4
   __TEXT.__gcc_except_tab: 0x1114
   __TEXT.__oslogstring: 0x91ef
-  __TEXT.__cstring: 0x65c2
+  __TEXT.__cstring: 0x66aa
   __TEXT.__dlopen_cstrs: 0xca
   __TEXT.__ustring: 0x28
-  __TEXT.__unwind_info: 0x2028
+  __TEXT.__unwind_info: 0x2038
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2fd0
+  __DATA_CONST.__const: 0x2fe8
   __DATA_CONST.__objc_classlist: 0x1a8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x21b8
+  __DATA_CONST.__objc_selrefs: 0x21d8
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0xe8
   __DATA_CONST.__objc_arraydata: 0x90
   __DATA_CONST.__got: 0x4f0
   __AUTH_CONST.__const: 0x610
-  __AUTH_CONST.__cfstring: 0x3e80
-  __AUTH_CONST.__objc_const: 0x8838
+  __AUTH_CONST.__cfstring: 0x3f40
+  __AUTH_CONST.__objc_const: 0x8868
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x878
   __DATA.__objc_ivar: 0x300
-  __DATA.__data: 0x1178
+  __DATA.__data: 0x11a0
   __DATA.__common: 0x20
   __DATA_DIRTY.__objc_data: 0x1090
   __DATA_DIRTY.__data: 0x8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2401
-  Symbols:   4527
-  CStrings:  1639
+  Functions: 2404
+  Symbols:   4546
+  CStrings:  1647
 
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
