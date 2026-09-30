## SpotlightServices

> `/System/Library/PrivateFrameworks/SpotlightServices.framework/SpotlightServices`

```diff

-2400.8.1.0.0
-  __TEXT.__text: 0x156c50
+2400.11.100.0.0
+  __TEXT.__text: 0x157f64
   __TEXT.__auth_stubs: 0x1ce0
-  __TEXT.__objc_methlist: 0xf0a8
+  __TEXT.__objc_methlist: 0xf170
   __TEXT.__const: 0x2a20
-  __TEXT.__cstring: 0x3105f
+  __TEXT.__cstring: 0x3116f
   __TEXT.__gcc_except_tab: 0x4d04
   __TEXT.__oslogstring: 0x9c7b
   __TEXT.__ustring: 0x8c2

   __TEXT.__swift5_proto: 0xc
   __TEXT.__swift5_types: 0x18
   __TEXT.__swift5_capture: 0x94
-  __TEXT.__unwind_info: 0x33d8
-  __TEXT.__objc_classname: 0x1520
-  __TEXT.__objc_methname: 0x2ba57
-  __TEXT.__objc_methtype: 0x3111
-  __TEXT.__objc_stubs: 0x1cf00
-  __DATA_CONST.__got: 0x20a0
+  __TEXT.__unwind_info: 0x3420
+  __TEXT.__objc_classname: 0x1521
+  __TEXT.__objc_methname: 0x2bd20
+  __TEXT.__objc_methtype: 0x314a
+  __TEXT.__objc_stubs: 0x1d160
+  __DATA_CONST.__got: 0x20a8
   __DATA_CONST.__const: 0xfce8
   __DATA_CONST.__objc_classlist: 0x6c8
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8f18
+  __DATA_CONST.__objc_selrefs: 0x8fa0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x560
   __DATA_CONST.__objc_arraydata: 0x1248
   __AUTH_CONST.__auth_got: 0xe80
-  __AUTH_CONST.__const: 0x28b0
-  __AUTH_CONST.__cfstring: 0x2b440
-  __AUTH_CONST.__objc_const: 0x187d8
-  __AUTH_CONST.__objc_intobj: 0x32b8
+  __AUTH_CONST.__const: 0x28d0
+  __AUTH_CONST.__cfstring: 0x2b680
+  __AUTH_CONST.__objc_const: 0x188d8
+  __AUTH_CONST.__objc_intobj: 0x32d0
   __AUTH_CONST.__objc_doubleobj: 0x2a0
   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__objc_arrayobj: 0x828
   __AUTH_CONST.__objc_dictobj: 0x258
   __AUTH.__objc_data: 0x2228
   __AUTH.__data: 0x118
-  __DATA.__objc_ivar: 0x1544
-  __DATA.__data: 0x1238
+  __DATA.__objc_ivar: 0x1558
+  __DATA.__data: 0x1240
   __DATA.__bss: 0xc68
   __DATA.__common: 0x28
   __DATA_DIRTY.__objc_data: 0x23f0
   __DATA_DIRTY.__data: 0x298
-  __DATA_DIRTY.__bss: 0x4c80
+  __DATA_DIRTY.__bss: 0x4cb0
   __DATA_DIRTY.__common: 0x30
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 37FCFD65-7689-3EB3-A851-0E8CBF701FF2
-  Functions: 6419
-  Symbols:   22225
-  CStrings:  19554
+  UUID: A595F764-E65D-36DE-B25B-C5FA6C4F8520
+  Functions: 6439
+  Symbols:   22293
+  CStrings:  19618
 
Symbols:
+ +[SPSearchEntity spotlightQueryFormattedString:]
+ +[SSBrowseSectionBuilder _sectionResultForResults:style:sectionTitle:sectionIdentifier:]
+ +[SSFilterResult supportsSecureCoding]
+ +[SSFilterUtilities hiddenFilterBundleIDs]
+ +[SSFilterUtilities hiddenFilterBundleIDs].cold.1
+ -[PRSQueryRankingConfiguration dateSortedL1]
+ -[PRSQueryRankingConfiguration setDateSortedL1:]
+ -[SPKQuery feedbackListener]
+ -[SPKQuery sendEndLocalSearchFeedback]
+ -[SPKQuery sendStartLocalSearchFeedback]
+ -[SPKQuery setFeedbackListener:]
+ -[SPKQuery setStartLocalSearchFeedback:]
+ -[SPKQuery startLocalSearchFeedback]
+ -[SPSearchQueryContext dateSortedL1]
+ -[SPSearchQueryContext setDateSortedL1:]
+ -[SSContactResultBuilder highlightedMatchedText]
+ -[SSFilterResult encodeWithCoder:]
+ -[SSFilterResult initWithCoder:]
+ -[SSMailResultBuilder bundleIdentifierForAppIconBadgeImage]
+ -[SSResultBuilder lastUsedDate]
+ -[SSResultBuilder setLastUsedDate:]
+ -[SSToolResultBuilder buildBadgingImageWithThumbnail:]
+ -[SSToolResultBuilder buildSecondaryCommand]
+ -[SSToolResultBuilder setToolIconData:]
+ -[SSToolResultBuilder toolIconData]
+ GCC_except_table78
+ _MDItemShortcutsToolIconData
+ _OBJC_IVAR_$_PRSQueryRankingConfiguration._dateSortedL1
+ _OBJC_IVAR_$_SPKQuery._feedbackListener
+ _OBJC_IVAR_$_SPKQuery._startLocalSearchFeedback
+ _OBJC_IVAR_$_SPSearchQueryContext._dateSortedL1
+ _OBJC_IVAR_$_SSResultBuilder._lastUsedDate
+ _OBJC_IVAR_$_SSToolResultBuilder._toolIconData
+ ___42+[SSFilterUtilities hiddenFilterBundleIDs]_block_invoke
+ ___block_literal_global.169
+ ___block_literal_global.171
+ ___block_literal_global.506
+ ___block_literal_global.569
+ _hiddenFilterBundleIDs.hiddenFilterBundleIDs
+ _hiddenFilterBundleIDs.onceToken
+ _objc_msgSend$_sectionResultForResults:style:sectionTitle:sectionIdentifier:
+ _objc_msgSend$didEndSearch:
+ _objc_msgSend$didStartSearch:
+ _objc_msgSend$feedbackListener
+ _objc_msgSend$hiddenFilterBundleIDs
+ _objc_msgSend$highlightedMatchedText
+ _objc_msgSend$initWithEntityQueryCommand:triggerEvent:searchType:indexType:queryId:originatingApp:
+ _objc_msgSend$initWithInput:triggerEvent:indexType:
+ _objc_msgSend$initWithStartSearch:
+ _objc_msgSend$isParsecQuery
+ _objc_msgSend$sendEndLocalSearchFeedback
+ _objc_msgSend$sendStartLocalSearchFeedback
+ _objc_msgSend$setImageData:
+ _objc_msgSend$setSpotlightBrowsingSearchScope:
+ _objc_msgSend$setStartLocalSearchFeedback:
+ _objc_msgSend$setToolIconData:
+ _objc_msgSend$spotlightQueryFormattedString:
+ _objc_msgSend$startLocalSearchFeedback
+ _objc_msgSend$thumbnailType
+ _objc_msgSend$toolIconData
- +[SSAppBrowseSectionBuilder sectionBundleIdentifier]
- +[SSBrowseSectionBuilder _sectionResultForResults:style:withSectionTitle:]
- +[SSBrowseSectionBuilder sectionBundleIdentifier]
- +[SSFilesBrowseSectionBuilder sectionBundleIdentifier]
- -[SSFileResultBuilder lastUsedDate]
- -[SSFileResultBuilder setLastUsedDate:]
- GCC_except_table77
- _OBJC_IVAR_$_SSFileResultBuilder._lastUsedDate
- ___block_literal_global.168
- ___block_literal_global.553
- _objc_msgSend$_sectionResultForResults:style:withSectionTitle:
CStrings:
+ "(redacted)"
+ "@\"<SFFeedbackListener>\""
+ "@\"SFStartLocalSearchFeedback\""
+ "@44@0:8@16i24@28@36"
+ "T@\"<SFFeedbackListener>\",W,N,V_feedbackListener"
+ "T@\"NSData\",&,V_toolIconData"
+ "T@\"NSDate\",&,N"
+ "T@\"SFStartLocalSearchFeedback\",&,V_startLocalSearchFeedback"
+ "TB,V_dateSortedL1"
+ "_dateSortedL1"
+ "_feedbackListener"
+ "_sectionResultForResults:style:sectionTitle:sectionIdentifier:"
+ "_startLocalSearchFeedback"
+ "_toolIconData"
+ "com.apple.SpotlightService"
+ "com.apple.spotlight.zkw.apps"
+ "dateSortedL1"
+ "hiddenFilterBundleIDs"
+ "highlightedMatchedText"
+ "initWithEntityQueryCommand:triggerEvent:searchType:indexType:queryId:originatingApp:"
+ "initWithInput:triggerEvent:indexType:"
+ "initWithStartSearch:"
+ "sendEndLocalSearchFeedback"
+ "sendStartLocalSearchFeedback"
+ "setDateSortedL1:"
+ "setFeedbackListener:"
+ "setImageData:"
+ "setSpotlightBrowsingSearchScope:"
+ "setStartLocalSearchFeedback:"
+ "setToolIconData:"
+ "skipExecution"
+ "spotlightQueryFormattedString:"
+ "startLocalSearchFeedback"
+ "toolIconData"
+ "visited %@"
- "@36@0:8@16i24@28"
- "_sectionResultForResults:style:withSectionTitle:"

```
