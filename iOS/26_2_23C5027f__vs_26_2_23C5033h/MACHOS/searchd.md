## searchd

> `/System/Library/PrivateFrameworks/Search.framework/searchd`

```diff

-2400.16.0.0.0
-  __TEXT.__text: 0x61dd8
+2400.17.1.0.0
+  __TEXT.__text: 0x61dd4
   __TEXT.__auth_stubs: 0x1870
   __TEXT.__objc_stubs: 0xa7a0
   __TEXT.__objc_methlist: 0x2af4
-  __TEXT.__const: 0x220
+  __TEXT.__const: 0x230
   __TEXT.__cstring: 0x50ea
   __TEXT.__oslogstring: 0x35a3
   __TEXT.__objc_methname: 0xaea1
   __TEXT.__objc_classname: 0x46b
-  __TEXT.__objc_methtype: 0x1815
+  __TEXT.__objc_methtype: 0x1818
   __TEXT.__gcc_except_tab: 0x5428
   __TEXT.__unwind_info: 0xea8
   __DATA_CONST.__auth_got: 0xc50

   - /System/Library/PrivateFrameworks/SpotlightRecommendation.framework/SpotlightRecommendation
   - /System/Library/PrivateFrameworks/SpotlightResources.framework/SpotlightResources
   - /System/Library/PrivateFrameworks/SpotlightServices.framework/SpotlightServices
+  - /System/Library/PrivateFrameworks/SpotlightUIServices.framework/SpotlightUIServices
   - /System/Library/PrivateFrameworks/SuggestionsSpotlightMetrics.framework/SuggestionsSpotlightMetrics
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 066A20DB-6476-3895-8E69-BAE1D66C8782
+  UUID: 4A9D7E59-4D3C-382E-B8BA-5DFDF60027E0
   Functions: 1218
   Symbols:   968
   CStrings:  3934
Symbols:
+ _OBJC_CLASS_$_SPUISDataDetectorResultGenerator
+ _OBJC_CLASS_$_SPUISDateFormatManager
+ _OBJC_CLASS_$_SPUISSuggestionResultBuilder
- _OBJC_CLASS_$_SSDataDetectorResultGenerator
- _OBJC_CLASS_$_SSDateFormatManager
- _OBJC_CLASS_$_SSSuggestionResultBuilder
Functions:
~ sub_10006246c -> sub_1000624dc : 96 -> 92
CStrings:
+ "@\"SPUISDataDetectorResultGenerator\""
- "@\"SSDataDetectorResultGenerator\""

```
