## HelpKit

> `/System/Library/PrivateFrameworks/HelpKit.framework/HelpKit`

```diff

-174.3.0.0.0
-  __TEXT.__text: 0x27044
+177.10.0.0.0
+  __TEXT.__text: 0x27b7c
   __TEXT.__auth_stubs: 0x6d0
-  __TEXT.__objc_methlist: 0x2b64
+  __TEXT.__objc_methlist: 0x2bdc
   __TEXT.__const: 0xe0
   __TEXT.__gcc_except_tab: 0x928
-  __TEXT.__cstring: 0x1812
-  __TEXT.__oslogstring: 0x318
+  __TEXT.__cstring: 0x188e
+  __TEXT.__oslogstring: 0x329
   __TEXT.__dlopen_cstrs: 0x10e
   __TEXT.__ustring: 0x82
-  __TEXT.__unwind_info: 0x9d0
+  __TEXT.__unwind_info: 0x9f4
   __TEXT.__objc_classname: 0x5ef
-  __TEXT.__objc_methname: 0x93f8
-  __TEXT.__objc_methtype: 0x1c23
-  __TEXT.__objc_stubs: 0x70a0
+  __TEXT.__objc_methname: 0x9644
+  __TEXT.__objc_methtype: 0x1cca
+  __TEXT.__objc_stubs: 0x7260
   __DATA_CONST.__got: 0x130
-  __DATA_CONST.__const: 0xe18
+  __DATA_CONST.__const: 0xe40
   __DATA_CONST.__objc_classlist: 0x130
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x4c20
-  __DATA_CONST.__objc_selrefs: 0x2200
+  __DATA_CONST.__objc_const: 0x4ca0
+  __DATA_CONST.__objc_selrefs: 0x2270
+  __DATA_CONST.__objc_classrefs: 0x378
+  __DATA_CONST.__objc_superrefs: 0xf0
   __DATA_CONST.__objc_arraydata: 0x80
-  __AUTH_CONST.__cfstring: 0x2940
+  __AUTH_CONST.__cfstring: 0x2a20
   __AUTH_CONST.__const: 0x320
   __AUTH_CONST.__objc_const: 0x1158
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__auth_got: 0x378
   __AUTH.__objc_data: 0xb90
-  __DATA.__objc_classrefs: 0x360
-  __DATA.__objc_superrefs: 0xf0
-  __DATA.__objc_ivar: 0x408
+  __DATA.__objc_ivar: 0x410
   __DATA.__data: 0x8b8
   __DATA.__bss: 0x1b0
   __DATA_DIRTY.__objc_data: 0x50

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1053
-  Symbols:   4149
-  CStrings:  2307
+  Functions: 1066
+  Symbols:   4195
+  CStrings:  2335
 
Symbols:
+ -[HLPHelpTableOfContentViewController logAnalyticsContentViewedWithHelpTopicItem:sourceType:]
+ -[HLPHelpTableOfContentViewController registerTraitChanges]
+ -[HLPHelpTableOfContentViewController searchBlurEffectView]
+ -[HLPHelpTableOfContentViewController setSearchBlurEffectView:]
+ -[HLPHelpTableOfContentViewController setShowTopicViewOnLoad:]
+ -[HLPHelpTableOfContentViewController showTopicViewOnLoad]
+ -[HLPHelpTableOfContentViewController updateSearchBarBlur]
+ -[HLPHelpTopicViewController rangeFromData:byteRangeString:]
+ -[HLPHelpTopicViewController registerTraitChanges]
+ -[HLPHelpTopicViewController setWebViewRequestsDataMap:]
+ -[HLPHelpTopicViewController updateHTMLStringPath:tag:attribute:useScheme:extension:]
+ -[HLPHelpTopicViewController updateURLSchemeTask:URL:MIMEType:data:error:]
+ -[HLPHelpTopicViewController webViewRequestsDataMap]
+ -[HLPHelpTopicViewController webViewWebContentProcessDidTerminate:]
+ -[HLPHelpViewController registerTraitChanges]
+ -[HLPHelpViewController tableOfContentViewControllerToCContentViewed:topicID:topicTitle:source:interfaceStyle:fromTopicID:externalURLString:]
+ GCC_except_table41
+ GCC_except_table51
+ GCC_except_table54
+ _OBJC_CLASS_$_UIBlurEffect
+ _OBJC_CLASS_$_UITraitUserInterfaceStyle
+ _OBJC_CLASS_$_UIVisualEffectView
+ _OBJC_IVAR_$_HLPHelpTableOfContentViewController._searchBlurEffectView
+ _OBJC_IVAR_$_HLPHelpTableOfContentViewController._showTopicViewOnLoad
+ _OBJC_IVAR_$_HLPHelpTopicViewController._webViewRequestsDataMap
+ _OBJC_IVAR_$_HLPHelpViewController._helpBookVersion
+ ___45-[HLPHelpViewController registerTraitChanges]_block_invoke
+ ___50-[HLPHelpTopicViewController registerTraitChanges]_block_invoke
+ ___59-[HLPHelpTableOfContentViewController registerTraitChanges]_block_invoke
+ ___block_descriptor_40_e8_32s_e52_v24?0"<UITraitEnvironment>"8"UITraitCollection"16ls32l8
+ __unnamed_array_storage.286
+ _objc_msgSend$effectWithStyle:
+ _objc_msgSend$initWithEffect:
+ _objc_msgSend$initWithURL:statusCode:HTTPVersion:headerFields:
+ _objc_msgSend$insertSubview:atIndex:
+ _objc_msgSend$logAnalyticsContentViewedWithHelpTopicItem:sourceType:
+ _objc_msgSend$rangeFromData:byteRangeString:
+ _objc_msgSend$registerForTraitChanges:withHandler:
+ _objc_msgSend$registerTraitChanges
+ _objc_msgSend$searchBlurEffectView
+ _objc_msgSend$setShowTopicViewOnLoad:
+ _objc_msgSend$showTopicViewOnLoad
+ _objc_msgSend$subdataWithRange:
+ _objc_msgSend$tableOfContentViewControllerToCContentViewed:topicID:topicTitle:source:interfaceStyle:fromTopicID:externalURLString:
+ _objc_msgSend$updateHTMLStringPath:tag:attribute:useScheme:extension:
+ _objc_msgSend$updateSearchBarBlur
+ _objc_msgSend$updateURLSchemeTask:URL:MIMEType:data:error:
+ _objc_msgSend$webViewRequestsDataMap
- -[HLPHelpTableOfContentViewController initialHelpTopicItem]
- -[HLPHelpTableOfContentViewController setInitialHelpTopicItem:]
- -[HLPHelpTableOfContentViewController traitCollectionDidChange:]
- -[HLPHelpTopicViewController traitCollectionDidChange:]
- -[HLPHelpTopicViewController updateHTMLStringPath:tag:attribute:useScheme:]
- -[HLPHelpViewController traitCollectionDidChange:]
- GCC_except_table34
- GCC_except_table44
- GCC_except_table50
- GCC_except_table53
- _OBJC_IVAR_$_HLPHelpTableOfContentViewController._initialHelpTopicItem
- _OBJC_IVAR_$_HLPHelpViewController._helpbookVersion
- ___block_literal_global.52
- __unnamed_array_storage.289
- _objc_msgSend$initialHelpTopicItem
- _objc_msgSend$setInitialHelpTopicItem:
- _objc_msgSend$updateHTMLStringPath:tag:attribute:useScheme:
CStrings:
+ "\x01\x16*"
+ "%ld"
+ "*"
+ "@\"UIVisualEffectView\""
+ "Content-Length"
+ "Content-Range"
+ "HLPHelpBookDynamicServerLastFailureLoadVersion"
+ "HTTP/1.1"
+ "Loading topic %@"
+ "Range"
+ "T@\"NSMutableDictionary\",&,N,V_webViewRequestsDataMap"
+ "T@\"NSString\",?,R,C"
+ "T@\"UIVisualEffectView\",&,N,V_searchBlurEffectView"
+ "_helpBookVersion"
+ "_searchBlurEffectView"
+ "_webViewRequestsDataMap"
+ "bytes %ld-%ld/%lu"
+ "bytes="
+ "effectWithStyle:"
+ "initWithEffect:"
+ "initWithURL:statusCode:HTTPVersion:headerFields:"
+ "insertSubview:atIndex:"
+ "logAnalyticsContentViewedWithHelpTopicItem:sourceType:"
+ "rangeFromData:byteRangeString:"
+ "registerForTraitChanges:withHandler:"
+ "registerTraitChanges"
+ "searchBlurEffectView"
+ "setSearchBlurEffectView:"
+ "setWebViewRequestsDataMap:"
+ "subdataWithRange:"
+ "tableOfContentViewControllerToCContentViewed:topicID:topicTitle:source:interfaceStyle:fromTopicID:externalURLString:"
+ "updateHTMLStringPath:tag:attribute:useScheme:extension:"
+ "updateSearchBarBlur"
+ "updateURLSchemeTask:URL:MIMEType:data:error:"
+ "v24@?0@\"<UITraitEnvironment>\"8@\"UITraitCollection\"16"
+ "v52@0:8@16@24@32B40@44"
+ "v72@0:8@\"HLPHelpTableOfContentViewController\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40q48@\"NSString\"56@\"NSString\"64"
+ "webViewRequestsDataMap"
+ "{_NSRange=QQ}32@0:8@16@24"
- "\x01\x16)"
- "HLPHelpBookDyanmicServerLastFailureLoadVersion"
- "T@\"HLPHelpTopicItem\",&,N,V_initialHelpTopicItem"
- "_helpbookVersion"
- "_initialHelpTopicItem"
- "initialHelpTopicItem"
- "mov"
- "setInitialHelpTopicItem:"
- "traitCollectionDidChange:"
- "updateHTMLStringPath:tag:attribute:useScheme:"
- "v44@0:8@16@24@32B40"

```
