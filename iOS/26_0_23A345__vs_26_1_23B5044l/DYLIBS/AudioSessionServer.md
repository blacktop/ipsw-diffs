## AudioSessionServer

> `/System/Library/PrivateFrameworks/AudioSessionServer.framework/AudioSessionServer`

```diff

-398.110.32.0.0
-  __TEXT.__text: 0x72ba8
-  __TEXT.__auth_stubs: 0x1120
+398.205.1.30.0
+  __TEXT.__text: 0x72da4
+  __TEXT.__auth_stubs: 0x1130
   __TEXT.__objc_methlist: 0xc28
-  __TEXT.__gcc_except_tab: 0xacec
+  __TEXT.__gcc_except_tab: 0xad20
   __TEXT.__const: 0xc30
-  __TEXT.__cstring: 0x5067
-  __TEXT.__oslogstring: 0x4e7a
+  __TEXT.__cstring: 0x507b
+  __TEXT.__oslogstring: 0x4ea8
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0x2d80
+  __TEXT.__unwind_info: 0x2d88
   __TEXT.__objc_classname: 0x178
   __TEXT.__objc_methname: 0x1d66
   __TEXT.__objc_methtype: 0x254f
   __TEXT.__objc_stubs: 0xf80
-  __DATA_CONST.__got: 0x4c8
+  __DATA_CONST.__got: 0x4d0
   __DATA_CONST.__const: 0x5e0
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x7a8
   __DATA_CONST.__objc_superrefs: 0x30
-  __AUTH_CONST.__auth_got: 0x8a0
+  __AUTH_CONST.__auth_got: 0x8a8
   __AUTH_CONST.__const: 0x10d0
   __AUTH_CONST.__cfstring: 0xf20
   __AUTH_CONST.__objc_const: 0xd10

   __AUTH.__data: 0x10
   __DATA.__objc_ivar: 0x68
   __DATA.__data: 0x2a8
-  __DATA.__bss: 0x38
+  __DATA.__bss: 0x58
   __DATA.__common: 0x1
   __DATA_DIRTY.__objc_data: 0x1e0
   __DATA_DIRTY.__data: 0x30

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 45B8B162-FDA1-3D56-9F61-C60C5FFD400A
-  Functions: 1668
-  Symbols:   5773
-  CStrings:  1587
+  UUID: 6D2EC42A-F6AA-3040-B0FE-51A6CD4B51A1
+  Functions: 1669
+  Symbols:   5786
+  CStrings:  1590
 
Symbols:
+ -[AVAudioSessionServerPriv(ServerProtocol) allowEnhanceDialogue:].cold.1
+ -[AVAudioSessionServerPriv(ServerProtocol) allowEnhanceDialogue:].cold.2
+ _CFPropertyListIsValid
+ __ZGVZN4avasL29EnhanceDialogueBriocheEnabledEvE29enhanceDialogueBriocheEnabled
+ __ZN4avasL29EnhanceDialogueBriocheEnabledEv
+ __ZZN4avasL29EnhanceDialogueBriocheEnabledEvE29enhanceDialogueBriocheEnabled
+ _kMXSessionProperty_AllowEnhancedDialogue
- GCC_except_table167
- GCC_except_table171
Functions:
~ __ZZNK4avas6server20LegacySessionManager33FindSessionAndVerifyOwnershipPrivINS0_17SessionCollection25SessionPresentingIteratorEEET_S5_S5_jRKNS0_15ProcessIdentityERKNSt3__18optionalINS1_24EntitlementExceptionTypeEEEENKUlRKS5_E_clINS9_4pairIjNS9_10shared_ptrINS0_18ISessionPresentingEEEEEEEDaSG_ : 480 -> 492
~ __ZN4avas6server20HandleMXNotificationEP26opaqueCMNotificationCenterPKvPK10__CFStringS4_S4_ : 500 -> 676
~ __ZN12_GLOBAL__N_135HandleCategoryOrModeChangedCallbackEjP8NSStringP12NSDictionary : 3160 -> 2956
~ __ZN4avas6server10forbid_acq16GetPropertyLocalEjRK13audit_token_tP8NSString : 2192 -> 2200
~ __ZN4avas6server10forbid_acq16SetPropertyLocalEjRK13audit_token_tP8NSStringPU25objcproto14NSSecureCoding11objc_object : 2676 -> 2684
~ __ZN4avas6server28HandleMXNotificationCallbackEP26opaqueCMNotificationCenterPKvPK10__CFStringS4_S4_ : 3108 -> 3264
+ __ZN4avasL29EnhanceDialogueBriocheEnabledEv
~ -[AVAudioSessionServerPriv(ServerProtocol) allowEnhanceDialogue:] : 876 -> 1084
~ __ZZNK4avas6server20LegacySessionManager33FindSessionAndVerifyOwnershipPrivINSt3__120__map_const_iteratorINS3_21__tree_const_iteratorINS3_12__value_typeIjNS3_10shared_ptrINS0_16AudioSessionInfoEEEEEPNS3_11__tree_nodeISA_PvEElEEEEEET_SH_SH_jRKNS0_15ProcessIdentityERKNS3_8optionalINS1_24EntitlementExceptionTypeEEEENKUlRKSH_E_clINS3_4pairIKjS9_EEEEDaSR_ : 480 -> 492
CStrings:
+ "%25s:%-5d Invalid notification payload for %@"
+ "Brioche"
+ "FitnessPlus"

```
