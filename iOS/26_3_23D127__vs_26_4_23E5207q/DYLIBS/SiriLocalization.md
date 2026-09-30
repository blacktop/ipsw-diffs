## SiriLocalization

> `/System/Library/PrivateFrameworks/SiriLocalization.framework/SiriLocalization`

```diff

-3515.3.1.0.0
-  __TEXT.__text: 0x13c8
-  __TEXT.__auth_stubs: 0x210
-  __TEXT.__objc_methlist: 0x114
+3520.84.5.1.6
+  __TEXT.__text: 0x142c
+  __TEXT.__auth_stubs: 0x1d0
+  __TEXT.__objc_methlist: 0xfc
   __TEXT.__const: 0x48
-  __TEXT.__cstring: 0x216
+  __TEXT.__cstring: 0x20b
   __TEXT.__oslogstring: 0x62
-  __TEXT.__unwind_info: 0xa8
+  __TEXT.__unwind_info: 0xa0
   __TEXT.__objc_classname: 0x46
   __TEXT.__objc_methname: 0x2a2
   __TEXT.__objc_methtype: 0x63

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x118
-  __AUTH_CONST.__auth_got: 0x110
+  __AUTH_CONST.__auth_got: 0xf0
   __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__cfstring: 0x5e0
   __AUTH_CONST.__objc_const: 0x280

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B7A5AC46-2B4B-37CA-BF59-3AADE4DEE782
-  Functions: 25
-  Symbols:   171
-  CStrings:  151
+  UUID: EC2B8B7B-C10D-3F18-8BCD-56C914AB026B
+  Functions: 24
+  Symbols:   164
+  CStrings:  149
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
- +[SFFeatureFlags isLassoEnabled]
- __OBJC_$_CLASS_METHODS_SFFeatureFlags
- __os_feature_enabled_impl
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x2
- _objc_retain_x22
Functions:
~ +[SLPreferences allSupportedLocales] : 84 -> 100
~ ___36+[SLPreferences allSupportedLocales]_block_invoke : 132 -> 144
~ +[SLPreferences builtInLocales] : 84 -> 100
~ ___31+[SLPreferences builtInLocales]_block_invoke : 700 -> 724
~ +[SLPreferences internalLocales] : 868 -> 876
~ ___34-[NSLocale(SWAI) isMontaraEnabled]_block_invoke : 124 -> 128
~ +[SLPreferences(Internal) builtIniOSLanguages] : 540 -> 544
~ +[SLPreferences(Internal) builtInVisionLanguages] : 124 -> 128
~ +[SLPreferences(Internal) builtInHorsemanLanguages] : 512 -> 516
~ +[SLPreferences(Internal) builtInZeusLanguages] : 512 -> 516
~ +[SLPreferences(Internal) builtInMultiUserLanguages] : 744 -> 748
~ +[SLPreferences(Internal) configValueForKey:] : 196 -> 216
CStrings:
- "Siri"
- "lasso"

```
