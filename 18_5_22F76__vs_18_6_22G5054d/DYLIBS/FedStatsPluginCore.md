## FedStatsPluginCore

> `/System/Library/PrivateFrameworks/FedStatsPluginCore.framework/FedStatsPluginCore`

```diff

-40.0.0.0.0
-  __TEXT.__text: 0x10248
+46.0.0.0.0
+  __TEXT.__text: 0x10324
   __TEXT.__auth_stubs: 0x440
-  __TEXT.__objc_methlist: 0xc54
+  __TEXT.__objc_methlist: 0xc3c
   __TEXT.__const: 0xb0
-  __TEXT.__cstring: 0x2008
+  __TEXT.__cstring: 0x2014
   __TEXT.__gcc_except_tab: 0x84
-  __TEXT.__oslogstring: 0x1214
+  __TEXT.__oslogstring: 0x11c1
   __TEXT.__unwind_info: 0x320
   __TEXT.__objc_classname: 0x3ef
-  __TEXT.__objc_methname: 0x2611
-  __TEXT.__objc_methtype: 0x385
-  __TEXT.__objc_stubs: 0x2140
+  __TEXT.__objc_methname: 0x25f3
+  __TEXT.__objc_methtype: 0x37a
+  __TEXT.__objc_stubs: 0x2100
   __DATA_CONST.__got: 0x298
   __DATA_CONST.__const: 0x168
   __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9b0
+  __DATA_CONST.__objc_selrefs: 0x9a0
   __DATA_CONST.__objc_superrefs: 0xa0
   __DATA_CONST.__objc_arraydata: 0x118
   __AUTH_CONST.__auth_got: 0x230
   __AUTH_CONST.__const: 0x200
-  __AUTH_CONST.__cfstring: 0x2680
+  __AUTH_CONST.__cfstring: 0x2660
   __AUTH_CONST.__objc_const: 0x1f68
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0x28

   - /System/Library/PrivateFrameworks/Trial.framework/Trial
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EF63A5B2-297D-3425-A266-7D030CFAFD04
-  Functions: 313
-  Symbols:   1401
-  CStrings:  1222
+  UUID: 3943ABAC-C92B-33E1-8FFB-39EC9BAD27D9
+  Functions: 310
+  Symbols:   1391
+  CStrings:  1217
 
Symbols:
+ +[FedStatsPluginCoreConsentCheckHelper checkChinaAIEligibility]
+ +[FedStatsPluginCoreConsentCheckHelper checkChinaAIEligibility].cold.1
+ -[FedStatsPluginRecipe checkDeviceOSVersionFilterWithError:]
+ -[FedStatsPluginRecipe checkDeviceOSVersionFilterWithError:].cold.1
+ _objc_msgSend$checkChinaAIEligibility
+ _objc_msgSend$checkDeviceOSVersionFilter:
+ _objc_msgSend$checkDeviceOSVersionFilterWithError:
- +[FedStatsPluginCoreConsentCheck checkConsentConfigurationItem:].cold.8
- +[FedStatsPluginCoreConsentCheck checkConsentConfigurationItem:].cold.9
- +[FedStatsPluginCoreConsentCheckHelper checkMCN]
- +[FedStatsPluginCoreConsentCheckHelper checkRSAEligibilityForApple]
- +[FedStatsPluginCoreConsentCheckHelper checkRSAEligibilityForCondition:]
- +[FedStatsPluginCoreConsentCheckHelper checkRSAEligibilityForCondition:].cold.1
- +[FedStatsPluginCoreConsentCheckHelper checkRSAEligibilityForThirdParty]
- _OUTLINED_FUNCTION_7
- _objc_msgSend$checkMCN
- _objc_msgSend$checkRSAEligibilityForApple
- _objc_msgSend$checkRSAEligibilityForCondition:
- _objc_msgSend$checkRSAEligibilityForThirdParty
- _objc_msgSend$uppercaseString
CStrings:
+ "Cannot load recipe."
+ "Checking device filter %@."
+ "Device is not China AI eligible."
+ "Regional safety consent for China AI is required for this use-case but not given"
+ "The plugin should not run for %@ as device filter: %@."
+ "checkChinaAIEligibility"
+ "checkDeviceOSVersionFilter:"
+ "checkDeviceOSVersionFilterWithError:"
+ "deviceOSVersionFilter"
+ "needsCNAI"
- "B20@0:8B16"
- "CN"
- "Mainland CN consent is required for this use-case but not given"
- "Regional safety consent for 3rd party is required for this use-case but not given"
- "Regional safety consent for Apple is required for this use-case but not given"
- "This feature is turned off. No consent could be given."
- "checkMCN"
- "checkRSAEligibilityForApple"
- "checkRSAEligibilityForCondition:"
- "checkRSAEligibilityForThirdParty"
- "needsMCN"
- "needsRSAFirst"
- "needsRSAThird"
- "uppercaseString"

```
