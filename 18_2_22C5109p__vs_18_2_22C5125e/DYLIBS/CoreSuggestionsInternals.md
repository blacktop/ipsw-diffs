## CoreSuggestionsInternals

> `/System/Library/PrivateFrameworks/CoreSuggestionsInternals.framework/CoreSuggestionsInternals`

```diff

-1271.0.6.0.0
-  __TEXT.__text: 0x260d98
+1271.3.0.2.0
+  __TEXT.__text: 0x2610c8
   __TEXT.__auth_stubs: 0x25d0
-  __TEXT.__objc_methlist: 0x14274
+  __TEXT.__objc_methlist: 0x1429c
   __TEXT.__const: 0x747a
-  __TEXT.__gcc_except_tab: 0xb2ec
-  __TEXT.__cstring: 0x30892
-  __TEXT.__oslogstring: 0x21d03
+  __TEXT.__gcc_except_tab: 0xb2fc
+  __TEXT.__cstring: 0x3081f
+  __TEXT.__oslogstring: 0x21e57
   __TEXT.__dlopen_cstrs: 0x336
   __TEXT.__ustring: 0xc4
-  __TEXT.__unwind_info: 0x81e0
+  __TEXT.__unwind_info: 0x81b0
   __TEXT.__objc_classname: 0x29d0
-  __TEXT.__objc_methname: 0x3b458
-  __TEXT.__objc_methtype: 0x708e
-  __TEXT.__objc_stubs: 0x2a960
+  __TEXT.__objc_methname: 0x3b503
+  __TEXT.__objc_methtype: 0x7092
+  __TEXT.__objc_stubs: 0x2aa20
   __DATA_CONST.__got: 0x2150
-  __DATA_CONST.__const: 0xb5a0
+  __DATA_CONST.__const: 0xb530
   __DATA_CONST.__objc_classlist: 0xb18
   __DATA_CONST.__objc_catlist: 0x120
   __DATA_CONST.__objc_protolist: 0x208
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xce70
+  __DATA_CONST.__objc_selrefs: 0xcea0
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x758
   __DATA_CONST.__objc_arraydata: 0x37c8
   __AUTH_CONST.__auth_got: 0x1300
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x4a08
-  __AUTH_CONST.__cfstring: 0x25800
-  __AUTH_CONST.__objc_const: 0x21950
+  __AUTH_CONST.__const: 0x49e8
+  __AUTH_CONST.__cfstring: 0x25840
+  __AUTH_CONST.__objc_const: 0x219a0
   __AUTH_CONST.__objc_intobj: 0x1068
   __AUTH_CONST.__objc_doubleobj: 0x80
   __AUTH_CONST.__objc_arrayobj: 0xe58
   __AUTH_CONST.__objc_dictobj: 0x348
-  __AUTH.__objc_data: 0x26e8
+  __AUTH.__objc_data: 0x2468
   __AUTH.__data: 0x200
-  __DATA.__objc_ivar: 0x146c
+  __DATA.__objc_ivar: 0x1474
   __DATA.__data: 0x1a60
-  __DATA.__bss: 0x7a8
+  __DATA.__bss: 0x738
   __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_data: 0x4808
+  __DATA_DIRTY.__objc_data: 0x4a88
   __DATA_DIRTY.__data: 0x388
-  __DATA_DIRTY.__bss: 0x99a0
+  __DATA_DIRTY.__bss: 0x9a10
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/libz.1.dylib
   Functions: 9963
   Symbols:   12726
-  CStrings:  18101
+  CStrings:  18111
 
Symbols:
+ _ACPropertyKeyEnabledDataclasses
- _DUInformationExtractorErrorDomain
CStrings:
+ "@\"PSUSummarizationPipeline\""
+ "SGDSuggestManager: consumeMessagesContentWithContext %!@(MISSING): %!{(MISSING)sensitive}@ -- rejected for time interval <= -1h"
+ "SGDocumentUnderstandingConsumer: consumeMessagesContentWithContext %!@(MISSING): %!{(MISSING)sensitive}@ -- rejected for date > 1h"
+ "SGExtractionDissector %!l(MISSING)u items extracted by regex pipeline for [SGPipelineEntity (%!{(MISSING)public}@)]"
+ "SGExtractionDissector: Create Enrichments from the SGOutput created using LLM extracted events"
+ "SGExtractionDissector: Not dissecting based on shouldProcessTextMessage"
+ "TB,R,GisTapBack,V_tapBack"
+ "_adjustLocalDateToUTC:"
+ "_areAllOutputTemplatesSchemaOrg:"
+ "_dateForUTCDate:withTimeZone:"
+ "_dateWithoutTimezoneFromString:"
+ "_persistRealtimeExtractions"
+ "_summarizationPipeline"
+ "_tapBack"
+ "accountsWithAccountTypeIdentifiers:preloadedProperties:error:"
+ "containsDateTextMessage:"
+ "deleteItemsWithIdentifiers:bundleId:"
+ "eventExtractionFromMail:"
+ "initWithContactStore:"
+ "isTapBack"
+ "messageType"
+ "outputFromLLMDissectionOfMailMessage:"
+ "persistRealtimeExtractions"
+ "processItem:receivedDate:positionInReceivedItems:"
+ "schemaorg"
+ "tapBack"
+ "tpbck"
- "B56@0:8@16@24@32@40^@48"
- "CatchUp"
- "FoundInEventReverseTemplateMLEnsemble"
- "PrecomputeSmartReplies"
- "PrecomputeSmartRepliesMail"
- "SGExtractionDissector: Create Enrichments from the SGOutput"
- "Using persistent store for realtime harvesting of mail (isTextMessage = %!{(MISSING)BOOL}d)"
- "_accessSummarizationPipelineForBundleId:block:"
- "_dateFromString:"
- "_keepRealtimeAsLost"
- "accountsWithAccountTypeIdentifiers:error:"
- "eventExtractionFromMail:error:"
- "handleDeletionOfItemsWithIdentifiers:bundleIdentifier:"
- "keepRealtimeAsLost"
- "llmDissectionOfMailMessage:entity:context:eventClassification:error:"
- "sharedPipelineWithContactStore:incomingBundleId:"
- "v16@?0@\"PSUSummarizationPipeline\"8"

```
