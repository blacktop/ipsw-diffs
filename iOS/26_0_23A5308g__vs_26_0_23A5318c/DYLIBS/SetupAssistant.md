## SetupAssistant

> `/System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant`

```diff

-5373.100.0.0.0
-  __TEXT.__text: 0x456c8
+5374.103.0.0.0
+  __TEXT.__text: 0x459ec
   __TEXT.__auth_stubs: 0xd80
-  __TEXT.__objc_methlist: 0x4134
+  __TEXT.__objc_methlist: 0x4164
   __TEXT.__const: 0x138
-  __TEXT.__gcc_except_tab: 0x10b8
-  __TEXT.__oslogstring: 0x593a
-  __TEXT.__cstring: 0x3035
+  __TEXT.__gcc_except_tab: 0x112c
+  __TEXT.__oslogstring: 0x5982
+  __TEXT.__cstring: 0x306c
   __TEXT.__dlopen_cstrs: 0x138b
   __TEXT.__ustring: 0x12
-  __TEXT.__unwind_info: 0x1310
+  __TEXT.__unwind_info: 0x1340
   __TEXT.__objc_classname: 0x8ca
-  __TEXT.__objc_methname: 0xb1a7
+  __TEXT.__objc_methname: 0xb28a
   __TEXT.__objc_methtype: 0x1254
   __TEXT.__objc_stubs: 0x8900
   __DATA_CONST.__got: 0x520

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2c00
+  __DATA_CONST.__objc_selrefs: 0x2c20
   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_superrefs: 0x150
   __DATA_CONST.__objc_arraydata: 0x178
   __AUTH_CONST.__auth_got: 0x6d0
   __AUTH_CONST.__const: 0xaa0
-  __AUTH_CONST.__cfstring: 0x36c0
-  __AUTH_CONST.__objc_const: 0x61b0
+  __AUTH_CONST.__cfstring: 0x3700
+  __AUTH_CONST.__objc_const: 0x61f0
   __AUTH_CONST.__objc_intobj: 0x270
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH.__objc_data: 0x550
-  __DATA.__objc_ivar: 0x3c4
+  __DATA.__objc_ivar: 0x3cc
   __DATA.__data: 0xa90
   __DATA.__bss: 0x608
   __DATA_DIRTY.__objc_data: 0xeb0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CA3F603B-70D7-3EFC-8A7A-0973C9698FA9
-  Functions: 1774
-  Symbols:   6499
-  CStrings:  3646
+  UUID: 188F6144-2FD0-3676-8061-6D813F1E709F
+  Functions: 1778
+  Symbols:   6514
+  CStrings:  3657
 
Symbols:
+ -[BFFSettingsManager _stashedIsIntelligenceEnabled]
+ -[BFFSettingsManager _stashedNotificationOnboardingDefaults]
+ -[BFFSettingsManager applySafeHavenStashWithIsIntelligenceEnabledBlock:notificationOnboardingDefaultsBlock:]
+ -[BFFSettingsManager stashIsIntelligenceEnabled:]
+ -[BFFSettingsManager stashNotificationOnboardingDefaults:]
+ GCC_except_table112
+ GCC_except_table45
+ GCC_except_table64
+ GCC_except_table69
+ GCC_except_table75
+ _OBJC_IVAR_$_BFFSettingsManager._stashedIntelligenceState
+ _OBJC_IVAR_$_BFFSettingsManager._stashedNotificationOnboardingDefaults
- -[BFFSettingsManager applySafeHavenStash]
- GCC_except_table108
- GCC_except_table41
- GCC_except_table56
- GCC_except_table65
- GCC_except_table67
CStrings:
+ " No _stashedIntelligenceState"
+ "No _stashedNotificationOnboardingDefaults"
+ "_stashedIntelligenceState"
+ "_stashedIsIntelligenceEnabled"
+ "_stashedNotificationOnboardingDefaults"
+ "applySafeHavenStashWithIsIntelligenceEnabledBlock:notificationOnboardingDefaultsBlock:"
+ "intelligenceStateKey"
+ "notificationOnboardingDefaultsKey"
+ "stashIsIntelligenceEnabled:"
+ "stashNotificationOnboardingDefaults:"
- "applySafeHavenStash"

```
