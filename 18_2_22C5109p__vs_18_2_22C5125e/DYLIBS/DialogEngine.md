## DialogEngine

> `/System/Library/PrivateFrameworks/DialogEngine.framework/DialogEngine`

```diff

-3402.29.1.0.0
-  __TEXT.__text: 0x4fb88c
-  __TEXT.__auth_stubs: 0x2050
+3402.34.1.0.0
+  __TEXT.__text: 0x4fc9a4
+  __TEXT.__auth_stubs: 0x2080
   __TEXT.__init_offsets: 0x24
-  __TEXT.__objc_methlist: 0x317c
-  __TEXT.__gcc_except_tab: 0x3b880
-  __TEXT.__const: 0x1b503
-  __TEXT.__cstring: 0x64bcf
+  __TEXT.__objc_methlist: 0x31ac
+  __TEXT.__gcc_except_tab: 0x3b954
+  __TEXT.__const: 0x1b5ab
+  __TEXT.__cstring: 0x64f06
   __TEXT.__ustring: 0xaa
   __TEXT.__oslogstring: 0x27c
-  __TEXT.__unwind_info: 0x14120
+  __TEXT.__unwind_info: 0x141e0
   __TEXT.__objc_classname: 0x4a4
-  __TEXT.__objc_methname: 0x66fc
+  __TEXT.__objc_methname: 0x680c
   __TEXT.__objc_methtype: 0x6374
-  __TEXT.__objc_stubs: 0x3e80
+  __TEXT.__objc_stubs: 0x3ec0
   __DATA_CONST.__got: 0x570
-  __DATA_CONST.__const: 0x30c0
+  __DATA_CONST.__const: 0x30e0
   __DATA_CONST.__objc_classlist: 0x280
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x17a8
+  __DATA_CONST.__objc_selrefs: 0x17c8
   __DATA_CONST.__objc_superrefs: 0x160
   __DATA_CONST.__objc_arraydata: 0x188
-  __AUTH_CONST.__auth_got: 0x1040
+  __AUTH_CONST.__auth_got: 0x1058
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x124c8
+  __AUTH_CONST.__const: 0x12610
   __AUTH_CONST.__cfstring: 0x1ae0
-  __AUTH_CONST.__objc_const: 0x5f80
+  __AUTH_CONST.__objc_const: 0x5fe0
   __AUTH_CONST.__objc_arrayobj: 0x1f8
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x50

   __AUTH.__data: 0x888
   __AUTH.__thread_vars: 0x18
   __AUTH.__thread_bss: 0x8
-  __DATA.__objc_ivar: 0x390
-  __DATA.__data: 0x4f0
+  __DATA.__objc_ivar: 0x398
+  __DATA.__data: 0x4d0
   __DATA.__bss: 0x3128
   __DATA.__common: 0x1288
   __DATA_DIRTY.__objc_data: 0xa0

   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libxml2.2.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 15587
-  Symbols:   17912
-  CStrings:  28016
+  Functions: 15617
+  Symbols:   17951
+  CStrings:  28037
 
Symbols:
+ __ZN4siri12dialogengine12ICUTitleCaseERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_
+ __ZN4siri12dialogengine27ConditionReferenceCollector20CollectConditionNameERKNS0_4NodeE
+ __ZN4siri12dialogengine27ConditionReferenceCollector5VisitERKNS0_4TextE
+ __ZN4siri12dialogengine27ConditionReferenceCollector5VisitERKNS0_5GroupE
+ __ZN4siri12dialogengine27ConditionReferenceCollector5VisitERKNS0_6DialogE
+ __ZN4siri12dialogengine29AddValidationEntriesToJsonDocERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERKNS1_6vectorINS0_15ValidationEntryENS5_ISB_EEEERN9rapidjson12PrettyWriterINSG_19GenericStringBufferINSG_4UTF8IcEENSG_12CrtAllocatorEEESK_SK_SL_Lj0EEE
+ __ZN4siri12dialogengine4File16AddValidationNitERKNS0_15ValidationEntryE
+ __ZN4siri12dialogengine4File16AddValidationNitERKNSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEPKNS0_14LineNumberBaseE
+ __ZN4siri12dialogengine7Context16AddValidationNitERKNSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEPKNS0_14LineNumberBaseE
+ __ZNK4siri12dialogengine11GroupRandom46ShouldDoValidationCheckForFewerThanTwoChildrenEv
+ __ZNK4siri12dialogengine13GroupFallback46ShouldDoValidationCheckForFewerThanTwoChildrenEv
+ __ZNK4siri12dialogengine27ConditionReferenceCollector17GetConditionNamesEv
+ __ZNK4siri12dialogengine4File17GetValidationNitsEv
+ __ZNK4siri12dialogengine4File24CheckForUnusedConditionsERNS0_7ContextE
+ __ZTIN4siri12dialogengine13GroupFallbackE
+ __ZTIN4siri12dialogengine27ConditionReferenceCollectorE
+ __ZTSN4siri12dialogengine13GroupFallbackE
+ __ZTSN4siri12dialogengine27ConditionReferenceCollectorE
+ __ZTVN4siri12dialogengine13GroupFallbackE
+ __ZTVN4siri12dialogengine27ConditionReferenceCollectorE
+ _ucasemap_close
+ _ucasemap_open
+ _ucasemap_utf8ToTitle
+ _xmlTextReaderMoveToElement
- __ZN4siri12dialogengine11GroupRandomC1Ev
- __ZN4siri12dialogengine11GroupRandomC2Ev
- _xmlTextReaderMoveToAttributeNo
CStrings:
+ "\x1f"
+ "' is not used; Consider removing it"
+ "3402.34.1"
+ "<dialog> element has equal <full> and <supporting> content; Consider replacing the child elements with their shared content"
+ "<random> group contains fewer than two items; Consider replacing it with <first>"
+ "> element has equal <speak> and <print> content; Consider replacing the child elements with their shared content"
+ "A ConditionEntry had type SUB_CONDITION but casting it to ConditionSubCondition failed"
+ "CAT Request (Dialog Engine 3402.34.1)"
+ "Cannot log validation nit (no file loaded): "
+ "Clearing the DtdPaths cache"
+ "Clearing the GradingAllowListPaths cache"
+ "Clearing the SchemaPaths cache"
+ "Condition with name '"
+ "Dialog ID: '%!s(MISSING)'\nFull print: '%!s(MISSING)'\nFull speak: '%!s(MISSING)'\nSupporting print: '%!s(MISSING)'\nSupporting speak: '%!s(MISSING)'\nUnfiltered full print: '%!s(MISSING)'\nUnfiltered full speak: '%!s(MISSING)'\nUnfiltered supporting print: '%!s(MISSING)'\nUnfiltered supporting speak: '%!s(MISSING)'\nspokenOnly: %!s(MISSING)\nprintOnly:  %!s(MISSING)\nisApprovedForGrading: %!s(MISSING)\nRedacted full print: '%!s(MISSING)'\nRedacted full speak: '%!s(MISSING)'\nRedacted supporting print: '%!s(MISSING)'\nRedacted supporting speak: '%!s(MISSING)'\nUnfiltered redacted full print: '%!s(MISSING)'\nUnfiltered redacted full speak: '%!s(MISSING)'\n"
+ "Failed to capitalize string: %!s(MISSING)."
+ "T@\"NSString\",&,N,V_unfilteredRedactedFullPrint"
+ "T@\"NSString\",&,N,V_unfilteredRedactedFullSpeak"
+ "Validation Nit: "
+ "_unfilteredRedactedFullPrint"
+ "_unfilteredRedactedFullSpeak"
+ "handleAssetUpdate(): Dialog assets were updated; Begin clearing caches"
+ "handleAssetUpdate(): Done clearing caches"
+ "setUnfilteredRedactedFullPrint:"
+ "setUnfilteredRedactedFullSpeak:"
+ "unfilteredRedactedFullPrint"
+ "unfilteredRedactedFullSpeak"
- "\x1d"
- "3402.29.1"
- "CAT Request (Dialog Engine 3402.29.1)"
- "Dialog ID: '%!s(MISSING)'\nFull print: '%!s(MISSING)'\nFull speak: '%!s(MISSING)'\nSupporting print: '%!s(MISSING)'\nSupporting speak: '%!s(MISSING)'\nUnfiltered Full print: '%!s(MISSING)'\nUnfiltered Full speak: '%!s(MISSING)'\nUnfiltered Supporting print: '%!s(MISSING)'\nUnfiltered Supporting speak: '%!s(MISSING)'\nspokenOnly: %!s(MISSING)\nprintOnly:  %!s(MISSING)\nisApprovedForGrading: %!s(MISSING)\nRedacted full print: '%!s(MISSING)'\nRedacted full speak: '%!s(MISSING)'\nRedacted supporting print: '%!s(MISSING)'\nRedacted supporting speak: '%!s(MISSING)'\n"
- "Dialog assets updated"

```
