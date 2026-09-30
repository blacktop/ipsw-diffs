## FedStatsPluginCore

> `/System/Library/PrivateFrameworks/FedStatsPluginCore.framework/FedStatsPluginCore`

```diff

-38.0.0.0.0
-  __TEXT.__text: 0x106b0
+40.0.0.0.0
+  __TEXT.__text: 0x10248
   __TEXT.__auth_stubs: 0x440
   __TEXT.__objc_methlist: 0xc54
   __TEXT.__const: 0xb0
-  __TEXT.__cstring: 0x2083
+  __TEXT.__cstring: 0x2008
   __TEXT.__gcc_except_tab: 0x84
-  __TEXT.__oslogstring: 0x1277
-  __TEXT.__unwind_info: 0x330
+  __TEXT.__oslogstring: 0x1214
+  __TEXT.__unwind_info: 0x320
   __TEXT.__objc_classname: 0x3ef
-  __TEXT.__objc_methname: 0x2695
+  __TEXT.__objc_methname: 0x2611
   __TEXT.__objc_methtype: 0x385
-  __TEXT.__objc_stubs: 0x2200
+  __TEXT.__objc_stubs: 0x2140
   __DATA_CONST.__got: 0x298
   __DATA_CONST.__const: 0x168
   __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9e0
+  __DATA_CONST.__objc_selrefs: 0x9b0
   __DATA_CONST.__objc_superrefs: 0xa0
   __DATA_CONST.__objc_arraydata: 0x118
   __AUTH_CONST.__auth_got: 0x230
   __AUTH_CONST.__const: 0x200
-  __AUTH_CONST.__cfstring: 0x26c0
+  __AUTH_CONST.__cfstring: 0x2680
   __AUTH_CONST.__objc_const: 0x1f68
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0x28

   - /System/Library/PrivateFrameworks/Trial.framework/Trial
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 319
-  Symbols:   1419
-  CStrings:  930
+  Functions: 313
+  Symbols:   1401
+  CStrings:  919
 
Symbols:
- +[FedStatsPluginCoreConsentCheckHelper checkRSAEligibilityForCondition:].cold.2
- +[FedStatsPluginCoreConsentCheckHelper checkRSAEligibilityForCondition:].cold.3
- +[FedStatsPluginCoreConsentCheckHelper checkRSAEligibilityForCondition:].cold.4
- _objc_msgSend$configuration
- _objc_msgSend$eventClass
- _objc_msgSend$initWithJSONDictionary:error:
- _objc_msgSend$isAppleIntelligenceEligible
- _objc_msgSend$isAppleIntelligenceToggledOn
- _objc_msgSend$isOnboarded3rdParty
CStrings:
+ "This feature is turned off. No consent could be given."
- "Error converting the event: %@"
- "Error evaluating Biome query \"%@\": %@"
- "Error getting %@ stream to check RSA eligibility: %@"
- "Error getting Biome DB instance"
- "RegionalSafetyAnalysis.Eligibility"
- "SELECT * FROM 'RegionalSafetyAnalysis.Eligibility' ORDER BY eventTimestamp DESC LIMIT 1"
- "configuration"
- "eventClass"
- "initWithJSONDictionary:error:"
- "isAppleIntelligenceEligible"
- "isAppleIntelligenceToggledOn"
- "isOnboarded3rdParty"

```
