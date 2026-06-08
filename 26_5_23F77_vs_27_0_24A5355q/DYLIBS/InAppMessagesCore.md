## InAppMessagesCore

> `/System/Library/PrivateFrameworks/InAppMessagesCore.framework/InAppMessagesCore`

```diff

 4024.100.3.1.0
-  __TEXT.__text: 0x3a44
-  __TEXT.__auth_stubs: 0x2a0
+  __TEXT.__text: 0x37a4
   __TEXT.__objc_methlist: 0x72c
   __TEXT.__const: 0x68
-  __TEXT.__cstring: 0x45f
-  __TEXT.__gcc_except_tab: 0x60
+  __TEXT.__cstring: 0x470
+  __TEXT.__gcc_except_tab: 0x50
   __TEXT.__oslogstring: 0x33
-  __TEXT.__unwind_info: 0x1a8
-  __TEXT.__objc_classname: 0x11e
-  __TEXT.__objc_methname: 0x14f4
-  __TEXT.__objc_methtype: 0x29c
-  __TEXT.__objc_stubs: 0x1360
-  __DATA_CONST.__got: 0xe0
+  __TEXT.__unwind_info: 0x198
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x130
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_catlist: 0x30

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x668
   __DATA_CONST.__objc_superrefs: 0x60
-  __AUTH_CONST.__auth_got: 0x160
+  __DATA_CONST.__got: 0xe0
   __AUTH_CONST.__const: 0xc0
   __AUTH_CONST.__cfstring: 0x760
   __AUTH_CONST.__objc_const: 0x13d0
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x90
   __DATA.__data: 0x120

   - /System/Library/PrivateFrameworks/iTunesCloud.framework/iTunesCloud
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AD698065-280E-3A87-BF56-F5E0C6F7D919
+  UUID: 971D6555-96C5-379E-82AD-1EBB1CFC46FF
   Functions: 120
-  Symbols:   660
-  CStrings:  475
+  Symbols:   665
+  CStrings:  129
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x8
Functions:
~ _IAMLogCategoryDefault : 84 -> 68
~ -[ICIAMMetricEvent(Metrics) reportableDictionary] : 288 -> 268
~ -[ICIAMMetricEvent(Metrics) reportableDictionaryForClickEventWithMessageIdentifier:andTargetIdentifier:] : 248 -> 240
~ -[NSArray(Utilities) iam_map:] : 240 -> 228
~ ___30-[NSArray(Utilities) iam_map:]_block_invoke : 144 -> 132
~ -[NSArray(Utilities) iam_compactMap:] : 240 -> 228
~ ___37-[NSArray(Utilities) iam_compactMap:]_block_invoke : 108 -> 104
~ -[NSArray(Utilities) iam_dictionaryFromArrayOfICIIAMParameters] : 420 -> 408
~ -[ICInAppMessageMetadataEntry(Utilities) numberOfDisplays] : 68 -> 64
~ -[ICInAppMessageMetadataEntry(Utilities) setNumberOfDisplays:] : 104 -> 100
~ -[ICInAppMessageMetadataEntry(Utilities) didCancelUserNotification] : 68 -> 64
~ -[ICInAppMessageMetadataEntry(Utilities) setDidCancelUserNotification:] : 104 -> 100
~ -[IAMImpression initWithMessageEntry:targetIdentifier:] : 148 -> 152
~ -[IAMImpression messageIdentifier] : 88 -> 80
~ -[IAMImpression messageType] : 64 -> 60
~ _IAMLogCategoryDefault_Oversize : 84 -> 68
~ -[IAMImpression(Metrics) reportableMetricsEventDictionary] : 1112 -> 1020
~ ___48-[NSDictionary(IAMSubset) isSubsetOfDictionary:]_block_invoke : 360 -> 348
~ -[IAMDecomposedKey constructCompoundPredicateIfNeeded] : 144 -> 140
~ ___54-[IAMDecomposedKey constructCompoundPredicateIfNeeded]_block_invoke : 304 -> 244
~ -[IAMDecomposedKey setRuleDestructuredIdentifiers:] : 64 -> 12
~ -[IAMEvent matchesWithKey:] : 92 -> 88
~ -[IAMValueEvent initWithName:value:] : 164 -> 168
~ -[IAMFigaroEvent name] : 100 -> 92
~ -[IAMFigaroEvent matchesWithKey:] : 412 -> 372
~ -[IAMFigaroEvent decomposeKey:] : 820 -> 776
~ -[IAMFigaroEvent serializeFigaroEventProperties:withPrefix:] : 376 -> 384
~ ___60-[IAMFigaroEvent serializeFigaroEventProperties:withPrefix:]_block_invoke : 404 -> 384
~ -[IAMApplicationDidBecomeActiveEvent initWithName:] : 124 -> 120
~ -[IAMApplicationDidBecomeActiveEvent initWithName:type:] : 124 -> 120
~ -[IAMContent initWithTitle:subtitle:body:images:actions:contentParameters:identifier:] : 292 -> 308
~ -[IAMContent initWithICMessageContent:] : 420 -> 380
~ -[IAMMessage initWithIdentifier:messageGroupIdentifier:contentPages:requiresCloseButton:] : 200 -> 208
~ -[IAMMessage initWithICInAppMessageEntry:] : 256 -> 236
~ -[ICIAMMessageContent(Metrics) dictionaryRepresentationWithReportableMetricsEvents] : 692 -> 660
~ -[IAMAction initWithIdentifier:displayText:url:requiresDelegate:actionParameters:] : 228 -> 244
~ -[IAMAction initWithICAction:] : 304 -> 280
~ -[IAMTempTestMessages initWithDisplayType:] : 1832 -> 1772
~ -[IAMTempTestMessages setMessageEntry:] : 64 -> 12
~ -[IAMImage initWithIdentifier:url:] : 152 -> 156
~ -[IAMImage initWithIdentifier:url:width:height:] : 172 -> 176
~ -[IAMImage initWithICImage:] : 228 -> 216
~ -[ICIAMMessageAction(Metrics) dictionaryRepresentationWithReportableMetricsEvents] : 180 -> 168
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"<NSCopying>\""
- "@\"ICInAppMessageEntry\""
- "@\"NSArray\""
- "@\"NSCompoundPredicate\""
- "@\"NSDate\""
- "@\"NSDictionary\""
- "@\"NSDictionary\"16@0:8"
- "@\"NSMutableArray\""
- "@\"NSMutableDictionary\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSURL\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8@?16"
- "@24@0:8^{_NSZone=}16"
- "@24@0:8q16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16q24"
- "@32@0:8d16q24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24I32I36"
- "@44@0:8@16@24@32B40"
- "@52@0:8@16@24@32B40@44"
- "@72@0:8@16@24@32@40@48@56@64"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"NSString\"16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "I"
- "I16@0:8"
- "IAMAction"
- "IAMApplicationDidBecomeActiveEvent"
- "IAMContent"
- "IAMCountableEvent"
- "IAMDecomposedKey"
- "IAMEvent"
- "IAMEventProtocol"
- "IAMFigaroEvent"
- "IAMImage"
- "IAMImpression"
- "IAMMessage"
- "IAMPresentationPolicy"
- "IAMSubset"
- "IAMTempTestMessages"
- "IAMValueEvent"
- "Metrics"
- "NSCopying"
- "NSObject"
- "Q16@0:8"
- "T#,R"
- "T@\"<NSCopying>\",C,N,Vvalue"
- "T@\"ICInAppMessageEntry\",&,N,V_messageEntry"
- "T@\"ICInAppMessageEntry\",C,N,V_messageEntry"
- "T@\"NSArray\",R,C,N,V_actions"
- "T@\"NSArray\",R,C,N,V_images"
- "T@\"NSArray\",R,N,V_contentPages"
- "T@\"NSDate\",C,N,V_displayEndTime"
- "T@\"NSDate\",C,N,V_displayStartTime"
- "T@\"NSDictionary\",?,R,C,N"
- "T@\"NSDictionary\",C,N,V_payload"
- "T@\"NSDictionary\",R,N,V_actionParameters"
- "T@\"NSDictionary\",R,N,V_contentParameters"
- "T@\"NSMutableDictionary\",&,N,V_ruleDestructuredIdentifiers"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",?,R,C,N"
- "T@\"NSString\",C,N,V_name"
- "T@\"NSString\",C,N,V_targetIdentifier"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,N"
- "T@\"NSString\",R,C,N,V_body"
- "T@\"NSString\",R,C,N,V_displayText"
- "T@\"NSString\",R,C,N,V_identifier"
- "T@\"NSString\",R,C,N,V_messageGroupIdentifier"
- "T@\"NSString\",R,C,N,V_subtitle"
- "T@\"NSString\",R,C,N,V_title"
- "T@\"NSString\",R,N"
- "T@\"NSString\",R,N,V_identifier"
- "T@\"NSURL\",R,C,N,V_url"
- "T@,?,R,C,N"
- "TB,N"
- "TB,R,N,V_requiresCloseButton"
- "TB,R,N,V_requiresDelegate"
- "TI,R,N,V_height"
- "TI,R,N,V_width"
- "TQ,N"
- "TQ,R"
- "Td,R,N,V_minimumIntervalBetweenPresentations"
- "Ti,R,N"
- "Tq,N,V_type"
- "Tq,R,N"
- "Tq,R,N,V_policyGroup"
- "URLByStandardizingPath"
- "URLForResource:withExtension:"
- "URLWithString:"
- "Utilities"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_actionParameters"
- "_actions"
- "_body"
- "_contentPages"
- "_contentParameters"
- "_displayEndTime"
- "_displayStartTime"
- "_displayText"
- "_height"
- "_identifier"
- "_images"
- "_messageEntry"
- "_messageGroupIdentifier"
- "_minimumIntervalBetweenPresentations"
- "_name"
- "_payload"
- "_policyGroup"
- "_requiresCloseButton"
- "_requiresDelegate"
- "_ruleDestructuredIdentifiers"
- "_subtitle"
- "_targetIdentifier"
- "_title"
- "_type"
- "_url"
- "_width"
- "absoluteString"
- "actionDetailsCount"
- "actionParameters"
- "actions"
- "addObject:"
- "addPredicateCondition:"
- "allKeys"
- "allocWithZone:"
- "applicationMessage"
- "arrayWithCapacity:"
- "arrayWithObjects:"
- "arrayWithObjects:count:"
- "autorelease"
- "body"
- "boolValue"
- "bundleIdentifier"
- "class"
- "componentsSeparatedByString:"
- "compoundPredicate"
- "compoundPredicateNeedsInitialization"
- "conformsToProtocol:"
- "constructCompoundPredicateIfNeeded"
- "containsString:"
- "contentPages"
- "contentParameters"
- "copy"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "d16@0:8"
- "debugDescription"
- "decomposeKey:"
- "description"
- "dictionaryRepresentation"
- "dictionaryRepresentationWithReportableMetricsEvents"
- "dictionaryWithObjects:forKeys:count:"
- "didCancelUserNotification"
- "displayEndTime"
- "displayStartTime"
- "displayText"
- "enumerateKeysAndObjectsUsingBlock:"
- "enumerateObjectsUsingBlock:"
- "evaluateWithObject:"
- "hasCardClickEvent"
- "hasClickEvent"
- "hasCloseClickEvent"
- "hasImpression"
- "hasImpressionEvent"
- "hasPageEvent"
- "hasPredicates"
- "hasPrefix:"
- "hasSuffix:"
- "hash"
- "height"
- "i16@0:8"
- "iam_compactMap:"
- "iam_dictionaryFromArrayOfICIIAMParameters"
- "iam_map:"
- "identifier"
- "images"
- "impression"
- "impressionEvent"
- "init"
- "initWithApplicationMessage:bundleIdentifier:"
- "initWithCapacity:"
- "initWithDisplayType:"
- "initWithFigaroEventProperties:"
- "initWithICAction:"
- "initWithICImage:"
- "initWithICInAppMessageEntry:"
- "initWithICMessageContent:"
- "initWithIdentifier:displayText:url:requiresDelegate:actionParameters:"
- "initWithIdentifier:messageGroupIdentifier:contentPages:requiresCloseButton:"
- "initWithIdentifier:url:"
- "initWithIdentifier:url:width:height:"
- "initWithMessageEntry:targetIdentifier:"
- "initWithMinimumIntervalBetweenPresentations:forPresentationPolicyGroup:"
- "initWithName:"
- "initWithName:type:"
- "initWithName:value:"
- "initWithTitle:subtitle:body:images:actions:contentParameters:identifier:"
- "initWithType:subpredicates:"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isNSDictionary__"
- "isNSNumber__"
- "isNSString__"
- "isProxy"
- "isSubsetOfDictionary:"
- "isSubsetOfSet:"
- "key"
- "length"
- "mainBundle"
- "matchesWithKey:"
- "messageActionsCount"
- "messageEntry"
- "messageGroupIdentifier"
- "messageIdentifier"
- "messageType"
- "metadataValueForKey:"
- "minimumIntervalBetweenPresentations"
- "mutableCopy"
- "null"
- "numberOfDisplays"
- "numberWithBool:"
- "numberWithInt:"
- "numberWithLongLong:"
- "numberWithUnsignedInteger:"
- "objectAtIndexedSubscript:"
- "objectForKeyedSubscript:"
- "pageDetailsCount"
- "payload"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "policyGroup"
- "predicateWithFormat:"
- "predicatesMatchFigaroEventProperties:"
- "presentationPolicyGroupForGlobalPresentationPolicyGroup:"
- "q"
- "q16@0:8"
- "q20@0:8i16"
- "raise:format:"
- "rawPredicateConditions"
- "release"
- "reportableDictionary"
- "reportableDictionaryForClickEventWithMessageIdentifier:andTargetIdentifier:"
- "reportableMetricsEventDictionary"
- "requiresCloseButton"
- "requiresDelegate"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "ruleDestructuredIdentifiers"
- "self"
- "serializeFigaroEventProperties:withPrefix:"
- "setActionDetails:"
- "setActionType:"
- "setBody:"
- "setCardClickEvent:"
- "setClickEvent:"
- "setCloseClickEvent:"
- "setComparisonType:"
- "setContentPages:"
- "setDataType:"
- "setDidCancelUserNotification:"
- "setDisplayEndTime:"
- "setDisplayStartTime:"
- "setDisplayText:"
- "setIdentifier:"
- "setImpression:"
- "setKey:"
- "setMaximumDisplays:"
- "setMessageActions:"
- "setMessageEntry:"
- "setMessageType:"
- "setMetadataValue:forKey:"
- "setName:"
- "setNumberOfDisplays:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setPageDetails:"
- "setPageEvent:"
- "setPageId:"
- "setPageType:"
- "setPayload:"
- "setRequiresDelegate:"
- "setRule:"
- "setRuleDestructuredIdentifiers:"
- "setSubtitle:"
- "setTargetId:"
- "setTargetIdentifier:"
- "setTargetType:"
- "setTargets:"
- "setTitle:"
- "setTriggerCondition:"
- "setTriggerValue:"
- "setType:"
- "setURL:"
- "setValue:"
- "setWebArchiveURL:"
- "setWithArray:"
- "source"
- "stringByAppendingString:"
- "stringValue"
- "stringWithFormat:"
- "substringWithRange:"
- "subtitle"
- "superclass"
- "targetIdentifier"
- "timeIntervalSince1970"
- "title"
- "type"
- "uRL"
- "unsignedIntegerValue"
- "url"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@16"
- "v24@0:8Q16"
- "v24@0:8q16"
- "value"
- "width"
- "zone"

```
