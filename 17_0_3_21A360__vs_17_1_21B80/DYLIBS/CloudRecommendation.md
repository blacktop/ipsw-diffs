## CloudRecommendation

> `/System/Library/PrivateFrameworks/CloudRecommendation.framework/CloudRecommendation`

```diff

-301.21.0.6.0
-  __TEXT.__text: 0x19fac
+301.21.1.1.0
+  __TEXT.__text: 0x1a2d8
   __TEXT.__auth_stubs: 0xc50
-  __TEXT.__objc_methlist: 0xe90
+  __TEXT.__objc_methlist: 0xf08
   __TEXT.__const: 0x630
   __TEXT.__cstring: 0x12df
   __TEXT.__oslogstring: 0x12b6

   __TEXT.__swift5_proto: 0x34
   __TEXT.__swift5_types: 0x20
   __TEXT.__swift5_capture: 0xc0
-  __TEXT.__unwind_info: 0x5b8
+  __TEXT.__unwind_info: 0x5c4
   __TEXT.__objc_classname: 0x1f0
-  __TEXT.__objc_methname: 0x1d1f
+  __TEXT.__objc_methname: 0x1e2e
   __TEXT.__objc_methtype: 0x326
-  __TEXT.__objc_stubs: 0xf60
+  __TEXT.__objc_stubs: 0xfa0
   __DATA_CONST.__got: 0xe8
   __DATA_CONST.__const: 0x270
   __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x2338
-  __DATA_CONST.__objc_selrefs: 0x648
+  __DATA_CONST.__objc_selrefs: 0x6a8
   __AUTH_CONST.__cfstring: 0xde0
   __AUTH_CONST.__objc_const: 0xa20
   __AUTH_CONST.__const: 0x598

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: D60EDC0C-FF85-3835-B2AA-76B3ABE498BC
-  Functions: 698
-  Symbols:   1750
-  CStrings:  810
+  UUID: 42339E68-8FA4-3A69-8E08-A07466E8A7D5
+  Functions: 708
+  Symbols:   1772
+  CStrings:  822
 
Symbols:
+ -[CERecommendationStringTemplate actionTitleTemplateForKey:]
+ -[CERecommendationStringTemplate messageTemplateForKey:]
+ -[CERecommendationStringTemplate setActionTitleTemplates:]
+ -[CERecommendationStringTemplate setMessageTemplates:]
+ -[CERecommendationStringTemplate setSubTitleTemplates:]
+ -[CERecommendationStringTemplate setTitleTemplates:]
+ -[CERecommendationStringTemplate subTitleTemplateForKey:]
+ -[CERecommendationStringTemplate titleTemplateForKey:]
+ -[CERuleConfiguration setThresholds:]
+ -[CERuleConfiguration thresholdForKey:]
+ -[CERuleset sortRecommendationRulesUsingComparator:]
+ _objc_msgSend$copyWithZone:
+ _objc_msgSend$sortedArrayUsingComparator:
+ _objc_msgSend$valueForKey:
- -[CERuleset setRecommendationRules:]
- _objc_msgSend$setRecommendationRules:
CStrings:
+ "T@\"NSArray\",R,N,V_recommendationRules"
+ "T@\"NSDictionary\",&,N,V_actionTitleTemplates"
+ "T@\"NSDictionary\",&,N,V_messageTemplates"
+ "T@\"NSDictionary\",&,N,V_subTitleTemplates"
+ "T@\"NSDictionary\",&,N,V_thresholds"
+ "T@\"NSDictionary\",&,N,V_titleTemplates"
+ "actionTitleTemplateForKey:"
+ "messageTemplateForKey:"
+ "setActionTitleTemplates:"
+ "setMessageTemplates:"
+ "setSubTitleTemplates:"
+ "setThresholds:"
+ "setTitleTemplates:"
+ "sortRecommendationRulesUsingComparator:"
+ "sortedArrayUsingComparator:"
+ "subTitleTemplateForKey:"
+ "thresholdForKey:"
+ "titleTemplateForKey:"
+ "valueForKey:"
- "T@\"NSArray\",&,N,V_recommendationRules"
- "T@\"NSDictionary\",R,N,V_actionTitleTemplates"
- "T@\"NSDictionary\",R,N,V_messageTemplates"
- "T@\"NSDictionary\",R,N,V_subTitleTemplates"
- "T@\"NSDictionary\",R,N,V_thresholds"
- "T@\"NSDictionary\",R,N,V_titleTemplates"
- "setRecommendationRules:"

```
