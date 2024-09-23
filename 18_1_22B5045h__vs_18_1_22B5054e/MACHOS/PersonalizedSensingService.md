## PersonalizedSensingService

> `/System/Library/PrivateFrameworks/PersonalizedSensing.framework/XPCServices/PersonalizedSensingService.xpc/PersonalizedSensingService`

```diff

-202.0.6.0.0
-  __TEXT.__text: 0x67ed8
-  __TEXT.__auth_stubs: 0x8b0
-  __TEXT.__objc_stubs: 0xab00
-  __TEXT.__objc_methlist: 0x6a14
+202.0.7.0.0
+  __TEXT.__text: 0x68634
+  __TEXT.__auth_stubs: 0x8c0
+  __TEXT.__objc_stubs: 0xab40
+  __TEXT.__objc_methlist: 0x6a54
   __TEXT.__objc_classname: 0x825
   __TEXT.__objc_methtype: 0xfa1
-  __TEXT.__cstring: 0xb56b
-  __TEXT.__objc_methname: 0x117f7
-  __TEXT.__const: 0x470
+  __TEXT.__cstring: 0xb56f
+  __TEXT.__objc_methname: 0x11870
+  __TEXT.__const: 0x498
   __TEXT.__gcc_except_tab: 0xbd0
-  __TEXT.__oslogstring: 0x6b39
+  __TEXT.__oslogstring: 0x6c4f
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x1158
-  __DATA_CONST.__auth_got: 0x470
+  __TEXT.__unwind_info: 0x1160
+  __DATA_CONST.__auth_got: 0x478
   __DATA_CONST.__got: 0x528
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x2e58

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x220
   __DATA_CONST.__objc_intobj: 0xc00
-  __DATA_CONST.__objc_arraydata: 0x8b0
-  __DATA_CONST.__objc_arrayobj: 0xa38
+  __DATA_CONST.__objc_arraydata: 0x908
+  __DATA_CONST.__objc_arrayobj: 0xa50
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_floatobj: 0x1b0
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0xbc50
-  __DATA.__objc_selrefs: 0x36b0
-  __DATA.__objc_ivar: 0x910
+  __DATA.__objc_const: 0xbcb0
+  __DATA.__objc_selrefs: 0x36c0
+  __DATA.__objc_ivar: 0x918
   __DATA.__objc_data: 0x1c70
   __DATA.__data: 0x4c0
   __DATA.__bss: 0x40

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libperfcheck.dylib
-  Functions: 2463
-  Symbols:   18709
-  CStrings:  5502
+  Functions: 2472
+  Symbols:   18762
+  CStrings:  5512
 
Symbols:
+ __block_literal_global.1489
+ +[MOBundleContentExtractor insignificantPlaceTypes]
+ __OBJC_$_CLASS_METHODS_MOBundleContentExtractor
+ -[MOBundleContentExtractor _updateContextGoodnessScoreFromBundle:forBundleContent:].cold.1
+ -[MOTemplateBasedContextBuilder insignificantPlaceTypes]
+ OBJC_IVAR_$_MOTemplateBasedContextBuilder._insignificantPlaceTypes
+ __105-[MOTemplateBasedContextBuilder _generateContextStringsBasedOnNewTemplateFromBundleContents:WithHandler:]_block_invoke.104
+ __139-[MOBundleContentExtractor _extractContentsFromBundleStartDate:endDate:daysPerFetch:significantLocationEnabled:partialResults:withHandler:]_block_invoke.1369
+ -[MOBundleContentExtractor _extractPersonsFromBundle:].cold.2
+ -[MOTemplateBasedContextBuilder _getMostRecentTemplateVersion]
+ OBJC_IVAR_$_MOBundleContentExtractor._insignificantPlaceTypes
+ __98-[MOTemplateBasedContextBuilder _generateContextStringsFromTemplateWithBundleContent:withHandler:]_block_invoke.83
+ -[MOBundleContentExtractor _updateContextGoodnessScoreFromBundle:forBundleContent:].cold.3
+ _objc_msgSend$_getMostRecentTemplateVersion
+ -[MOBundleContentExtractor _updateContextGoodnessScoreFromBundle:forBundleContent:].cold.2
+ -[MOBundleContentExtractor insignificantPlaceTypes]
+ _objc_msgSend$insignificantPlaceTypes
+ __105-[MOTemplateBasedContextBuilder _generateContextStringsBasedOnNewTemplateFromBundleContents:WithHandler:]_block_invoke.109
+ _arc4random_uniform
- __block_literal_global.1482
- __105-[MOTemplateBasedContextBuilder _generateContextStringsBasedOnNewTemplateFromBundleContents:WithHandler:]_block_invoke.101
- __105-[MOTemplateBasedContextBuilder _generateContextStringsBasedOnNewTemplateFromBundleContents:WithHandler:]_block_invoke.96
- __98-[MOTemplateBasedContextBuilder _generateContextStringsFromTemplateWithBundleContent:withHandler:]_block_invoke.76
- __139-[MOBundleContentExtractor _extractContentsFromBundleStartDate:endDate:daysPerFetch:significantLocationEnabled:partialResults:withHandler:]_block_invoke.1366
CStrings:
+ "\n"
+ "Extracted the following persons : %!{(MISSING)private}@ , from the bundle suggestionID : %!{(MISSING)private}@ "
+ "Randomly selected person %!{(MISSING)private}@ from persons"
+ "T@\"NSArray\",R,N,V_insignificantPlaceTypes"
+ "_getMostRecentTemplateVersion"
+ "templateVersion.json"
+ " contextGoodnessScore=%!f(MISSING), photoTrait=%!l(MISSING)u, placeType=%!l(MISSING)u"
+ "most recent template version: %!f(MISSING)"
+ "most recent template version from file: %!f(MISSING)"
+ " BundleGoodnessScore=%!f(MISSING)"
+ " Current bundle:%!{(MISSING)private}@. Content:%!{(MISSING)private}@ "
+ "insignificantPlaceTypes"
+ "_insignificantPlaceTypes"
- "Extracted the following persons : %!@(MISSING) , from the bundle suggestionID : %!@(MISSING) "
- "\t"
- "Template_Version"

```
