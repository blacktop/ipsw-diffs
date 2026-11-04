## SetupAssistant

> `/System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant`

```diff

-5411.2.5.0.0
-  __TEXT.__text: 0x437a0
-  __TEXT.__objc_methlist: 0x4204
-  __TEXT.__const: 0x140
+5412.2.3.101.0
+  __TEXT.__text: 0x43a64
+  __TEXT.__objc_methlist: 0x424c
+  __TEXT.__const: 0x138
   __TEXT.__gcc_except_tab: 0xf4c
-  __TEXT.__oslogstring: 0x5a30
-  __TEXT.__cstring: 0x3511
+  __TEXT.__oslogstring: 0x5ac4
+  __TEXT.__cstring: 0x3556
   __TEXT.__dlopen_cstrs: 0x13dd
   __TEXT.__ustring: 0x12
-  __TEXT.__unwind_info: 0x19b8
+  __TEXT.__unwind_info: 0x19c8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1788
+  __DATA_CONST.__const: 0x1780
   __DATA_CONST.__objc_classlist: 0x208
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2ca8
+  __DATA_CONST.__objc_selrefs: 0x2cd8
   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_superrefs: 0x150
   __DATA_CONST.__objc_arraydata: 0x178
   __DATA_CONST.__got: 0x540
   __AUTH_CONST.__const: 0xac0
-  __AUTH_CONST.__cfstring: 0x3b20
-  __AUTH_CONST.__objc_const: 0x6300
+  __AUTH_CONST.__cfstring: 0x3ba0
+  __AUTH_CONST.__objc_const: 0x6350
   __AUTH_CONST.__objc_intobj: 0x270
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x10e0
-  __DATA.__objc_ivar: 0x3d4
+  __DATA.__objc_ivar: 0x3d8
   __DATA.__data: 0xa90
   __DATA_DIRTY.__objc_data: 0x370
   __DATA_DIRTY.__bss: 0x90

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1807
-  Symbols:   3118
-  CStrings:  1139
+  Functions: 1812
+  Symbols:   3124
+  CStrings:  1146
 
Symbols:
+ +[BYDevice isV68ProductType:]
+ +[BYDevice isV68ProductTypeString:]
+ -[BFFSettingsManager setAssistantAppleIntelligenceFallback:]
+ -[BYDevice isV68]
+ -[BuddyFeatureFlags isAdaptiveModalPresentationEnabled]
+ GCC_except_table37
+ GCC_except_table45
+ GCC_except_table60
+ GCC_except_table63
+ GCC_except_table66
+ GCC_except_table72
+ _OBJC_IVAR_$_BFFSettingsManager._stashedAssistantAppleIntelligenceFallback
- GCC_except_table36
- GCC_except_table59
- GCC_except_table65
- GCC_except_table67
- GCC_except_table71
- _BYPrivacySubscriptionBundleIdentifier
CStrings:
+ "27.0"
+ "AdaptiveModalPresentation"
+ "ForceTouchIDSupport"
+ "No first supported OS release for V68 product type (%ld); falling back to %{public}@"
+ "Setting assistant Apple Intelligence fallback to %{public}@..."
+ "assistantAppleIntelligenceFallback"
+ "iPhone19,4"
+ "iPhone99,10"
- "com.apple.onboarding.subscriptionbundle"
```
