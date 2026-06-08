## RevealCore

> `/System/Library/PrivateFrameworks/RevealCore.framework/RevealCore`

```diff

-56.0.0.0.0
-  __TEXT.__text: 0x2fb0
-  __TEXT.__auth_stubs: 0x280
+59.0.0.0.0
+  __TEXT.__text: 0x2dcc
   __TEXT.__objc_methlist: 0x5f0
   __TEXT.__const: 0x48
-  __TEXT.__cstring: 0x28d
-  __TEXT.__unwind_info: 0x118
-  __TEXT.__objc_classname: 0x68
-  __TEXT.__objc_methname: 0x1164
-  __TEXT.__objc_methtype: 0x294
-  __TEXT.__objc_stubs: 0x720
-  __DATA_CONST.__got: 0x88
+  __TEXT.__cstring: 0x297
+  __TEXT.__unwind_info: 0x100
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x38
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x20

   __DATA_CONST.__objc_selrefs: 0x460
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_arraydata: 0x68
-  __AUTH_CONST.__auth_got: 0x148
+  __DATA_CONST.__got: 0x88
   __AUTH_CONST.__cfstring: 0x600
   __AUTH_CONST.__objc_const: 0xc58
   __AUTH_CONST.__objc_arrayobj: 0x18
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x9c
   __DATA.__data: 0x180
   __DATA_DIRTY.__objc_data: 0x140

   - /System/Library/PrivateFrameworks/DataDetectorsCore.framework/DataDetectorsCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B9896DB2-111B-30B2-BD36-E38E6BC17D2F
+  UUID: 3BFDABCD-14B4-3854-B731-FBA911C6A2A8
   Functions: 95
-  Symbols:   410
-  CStrings:  361
+  Symbols:   416
+  CStrings:  97
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x24
+ _objc_retain_x26
+ _objc_retain_x3
- _objc_retainAutoreleasedReturnValue
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"DDScannerResult\""
- "@\"NSArray\""
- "@\"NSDate\""
- "@\"NSNumber\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSTimeZone\""
- "@\"NSURL\""
- "@\"RVQuery\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@32@0:8@16#24"
- "@40@0:8:16@24@32"
- "@40@0:8@16{_NSRange=QQ}24"
- "@48@0:8@16@24{_NSRange=QQ}32"
- "@48@0:8@16Q24@32^B40"
- "@48@0:8@16{_NSRange=QQ}24@?40"
- "@48@0:8q16@24{_NSRange=QQ}32"
- "@56@0:8@16@24@32q40@?48"
- "@?"
- "@?16@0:8"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "NSCoding"
- "NSObject"
- "NSSecureCoding"
- "Q16@0:8"
- "RVDocumentContext"
- "RVItem"
- "RVQuery"
- "RVQueryProtocol"
- "RVSelection"
- "T#,R"
- "T@\"DDScannerResult\",R,N,V_ddResult"
- "T@\"NSArray\",C,N"
- "T@\"NSDate\",C,N,VcontentReferenceDate"
- "T@\"NSNumber\",C,N,VgroupCategory"
- "T@\"NSString\",&,N,V_leadingText"
- "T@\"NSString\",&,N,V_originalSelectedText"
- "T@\"NSString\",&,N,V_trailingText"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,N,VauthorContactUUID"
- "T@\"NSString\",C,N,VauthorEmailAddress"
- "T@\"NSString\",C,N,VauthorName"
- "T@\"NSString\",C,N,VcontentSubject"
- "T@\"NSString\",C,N,VcoreSpotlightUniqueIdentifier"
- "T@\"NSString\",C,N,VgroupTranscript"
- "T@\"NSString\",C,N,VselectedText"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,N"
- "T@\"NSString\",R,N,V_clientIdentifier"
- "T@\"NSString\",R,N,V_contactPropertyValue"
- "T@\"NSString\",R,N,V_identifier"
- "T@\"NSString\",R,N,V_text"
- "T@\"NSString\",R,N,V_title"
- "T@\"NSString\",R,N,V_userAgent"
- "T@\"NSTimeZone\",C,N,VcontentReferenceTimeZone"
- "T@\"NSURL\",C,N,VdocumentURL"
- "T@\"NSURL\",R,N"
- "T@\"NSURL\",R,N,V_url"
- "T@\"RVQuery\",R,N,V_query"
- "T@,&,N,V_clientHints"
- "T@?,C,N,V_lookupContextFetchingBlock"
- "T@?,C,N,V_reportAnIssueBlock"
- "T@?,C,N,V_reportAnIssueExtendedBlock"
- "T@?,C,N,V_reportAnIssueMetadataFetchingBlock"
- "T@?,C,N,V_textQueryProvider"
- "T@?,R,N,V_queryProvider"
- "TB,R"
- "TQ,R"
- "Tq,R,N"
- "Tq,R,N,V_contactPropertyType"
- "Tq,R,N,V_normalizedType"
- "Tq,R,N,V_queryID"
- "Tq,R,N,V_selectionType"
- "Tq,R,N,V_type"
- "T{_NSRange=QQ},R,N,V_highlightRange"
- "URLWithString:"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_clientHints"
- "_clientIdentifier"
- "_contactPropertyType"
- "_contactPropertyValue"
- "_ddResult"
- "_highlightRange"
- "_identifier"
- "_leadingText"
- "_lookupContextFetchingBlock"
- "_normalized"
- "_normalizedType"
- "_originalSelectedText"
- "_query"
- "_queryID"
- "_queryProvider"
- "_reportAnIssueBlock"
- "_reportAnIssueExtendedBlock"
- "_reportAnIssueMetadataFetchingBlock"
- "_selectionType"
- "_text"
- "_textQueryProvider"
- "_title"
- "_trailingText"
- "_type"
- "_url"
- "_userAgent"
- "absoluteString"
- "arrayWithObjects:count:"
- "autorelease"
- "characterAtIndex:"
- "characterIsMember:"
- "class"
- "clientHints"
- "conformsToProtocol:"
- "containsObject:"
- "containsString:"
- "copy"
- "coreResult"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "debugDescription"
- "decodeIntegerForKey:"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "description"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "enumerateTagsInRange:unit:scheme:options:usingBlock:"
- "firstObject"
- "getCharacters:"
- "getClientHintKey:ofType:"
- "hash"
- "init"
- "initWithCharacters:length:"
- "initWithClientIdentifier:rangeInContext:"
- "initWithCoder:"
- "initWithContactProperty:value:rangeInContext:"
- "initWithDDResult:"
- "initWithDDResult:text:range:"
- "initWithScannerType:passiveIntent:"
- "initWithSearchQuery:rangeInContext:"
- "initWithTagSchemes:"
- "initWithText:clickedIndex:selectionRanges:shouldUpdateSelection:"
- "initWithText:selectedRange:"
- "initWithText:selectedRange:customURLParser:"
- "initWithTitle:clientIdentifier:userAgent:queryID:queryProvider:"
- "initWithURL:rangeInContext:"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "length"
- "lookupContextFetchingBlock"
- "lowercaseString"
- "maxContextLength"
- "normalizedURL"
- "objectForKeyedSubscript:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "q"
- "q16@0:8"
- "query"
- "queryProvider"
- "range"
- "rangeValue"
- "release"
- "reportAnIssueBlock"
- "reportAnIssueExtendedBlock"
- "reportAnIssueMetadataFetchingBlock"
- "respondsToSelector:"
- "resultsFromCoreResults:"
- "retain"
- "retainCount"
- "revealRangeAtIndex:selectedRanges:shouldUpdateSelection:"
- "scanString:range:configuration:"
- "scheme"
- "searchRangeForString:aroundLocation:"
- "selectionType"
- "self"
- "setAuthorContactUUID:"
- "setAuthorEmailAddress:"
- "setAuthorName:"
- "setClientHints:"
- "setContentReferenceDate:"
- "setContentReferenceTimeZone:"
- "setContentSubject:"
- "setCoreSpotlightUniqueIdentifier:"
- "setDocumentURL:"
- "setExistingDDResultsList:"
- "setGroupAllResults:"
- "setGroupCategory:"
- "setGroupTranscript:"
- "setLeadingText:"
- "setLookupContextFetchingBlock:"
- "setNameAndEmailWithRawSenderField:"
- "setOriginalSelectedText:"
- "setReportAnIssueBlock:"
- "setReportAnIssueExtendedBlock:"
- "setReportAnIssueMetadataFetchingBlock:"
- "setSelectedText:"
- "setString:"
- "setTextQueryProvider:"
- "setTrailingText:"
- "setWithArray:"
- "setWithObjects:"
- "stringByReplacingOccurrencesOfString:withString:"
- "stringWithCharacters:length:"
- "substringWithRange:"
- "superclass"
- "supportsSecureCoding"
- "textQueryProvider"
- "textSearchContext"
- "urlificationRange"
- "v16@0:8"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "whitespaceCharacterSet"
- "zone"
- "{_NSRange=\"location\"Q\"length\"Q}"
- "{_NSRange=QQ}16@0:8"
- "{_NSRange=QQ}32@0:8@16Q24"
- "{_NSRange=QQ}40@0:8Q16@24^B32"

```
