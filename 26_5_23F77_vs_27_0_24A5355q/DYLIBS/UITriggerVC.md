## UITriggerVC

> `/System/Library/PrivateFrameworks/UITriggerVC.framework/UITriggerVC`

```diff

-1114.4.50.0.0
-  __TEXT.__text: 0x6f18
-  __TEXT.__auth_stubs: 0x2e0
+1115.0.87.0.0
+  __TEXT.__text: 0x6e54
   __TEXT.__objc_methlist: 0xfc0
   __TEXT.__const: 0x58
-  __TEXT.__cstring: 0x30d
-  __TEXT.__unwind_info: 0x298
-  __TEXT.__objc_classname: 0x15f
-  __TEXT.__objc_methname: 0x239e
-  __TEXT.__objc_methtype: 0x1360
-  __TEXT.__objc_stubs: 0xde0
-  __DATA_CONST.__got: 0xa8
+  __TEXT.__cstring: 0x315
+  __TEXT.__unwind_info: 0x220
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x68
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x970
   __DATA_CONST.__objc_superrefs: 0x48
-  __AUTH_CONST.__auth_got: 0x178
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x520
   __AUTH_CONST.__objc_const: 0x12f8
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x2d0
   __DATA.__objc_ivar: 0x74
   __DATA.__data: 0x2a0

   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AABC6547-770F-3EBE-BB9C-79409A5662DF
+  UUID: 57E2CB3A-1BDB-312E-B186-BEF7650048D5
   Functions: 200
-  Symbols:   745
-  CStrings:  604
+  Symbols:   747
+  CStrings:  85
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x1
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x23
+ _objc_retain_x3
+ _objc_retain_x6
+ _objc_retain_x8
- _objc_release_x28
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x22
- _objc_retain_x24
- _objc_retain_x26
Functions:
~ -[CSLUIPBUIPluginTriggerResponse hasErrorString] : 24 -> 28
~ -[CSLUIPBUIPluginTriggerResponse description] : 176 -> 164
~ _CSLUIPBUIPluginTriggerResponseReadFrom : 700 -> 696
~ -[CSLUIPBUIPluginTriggerResponse copyTo:] : 48 -> 60
~ -[CSLUIPBUIPluginTriggerResponse copyWithZone:] : 116 -> 132
~ -[CSLUIPBUIPluginTriggerResponse isEqual:] : 152 -> 168
~ -[CSLUIPBUIPluginTriggerResponse hash] : 72 -> 80
~ -[CSLUIPBUIPluginTriggerResponse mergeFrom:] : 40 -> 52
~ -[CSLUIPBUIPluginTriggerResponse success] : 16 -> 20
~ -[CSLUIPBUIPluginTriggerResponse setSuccess:] : 16 -> 20
~ -[CSLUIPBUIPluginTriggerResponse errorString] : 16 -> 20
~ -[CSLUIPBUIPluginTriggerResponse setErrorString:] : 80 -> 20
~ -[CSLUIPBProperty hasName] : 24 -> 28
~ -[CSLUIPBProperty hasValue] : 24 -> 28
~ -[CSLUIPBProperty description] : 176 -> 164
~ _CSLUIPBPropertyReadFrom : 576 -> 568
~ -[CSLUIPBProperty writeTo:] : 124 -> 136
~ -[CSLUIPBProperty copyTo:] : 116 -> 128
~ -[CSLUIPBProperty copyWithZone:] : 132 -> 148
~ -[CSLUIPBProperty isEqual:] : 160 -> 176
~ -[CSLUIPBProperty hash] : 72 -> 80
~ -[CSLUIPBProperty mergeFrom:] : 148 -> 156
~ -[CSLUIPBProperty name] : 16 -> 20
~ -[CSLUIPBProperty setName:] : 80 -> 20
~ -[CSLUIPBProperty value] : 16 -> 20
~ -[CSLUIPBProperty setValue:] : 80 -> 20
~ -[CSLUIPBSize description] : 176 -> 164
~ -[CSLUIPBSize dictionaryRepresentation] : 200 -> 196
~ _CSLUIPBSizeReadFrom : 768 -> 760
~ -[CSLUIPBSize copyTo:] : 36 -> 52
~ -[CSLUIPBSize copyWithZone:] : 84 -> 100
~ -[CSLUIPBSize isEqual:] : 136 -> 152
~ -[CSLUIPBSize hash] : 268 -> 260
~ -[CSLUIPBSize mergeFrom:] : 36 -> 52
~ -[CSLUIPBSize width] : 16 -> 20
~ -[CSLUIPBSize setWidth:] : 16 -> 20
~ -[CSLUIPBSize height] : 16 -> 20
~ -[CSLUIPBSize setHeight:] : 16 -> 20
~ -[CSLUIPBPropertyValue hasStringValue] : 24 -> 28
~ -[CSLUIPBPropertyValue hasNumberValue] : 24 -> 28
~ -[CSLUIPBPropertyValue hasUUIDValue] : 24 -> 28
~ -[CSLUIPBPropertyValue hasDataValue] : 24 -> 28
~ -[CSLUIPBPropertyValue hasSizeValue] : 24 -> 28
~ -[CSLUIPBPropertyValue hasDictionaryKey] : 24 -> 28
~ -[CSLUIPBPropertyValue clearArrayValues] : 16 -> 20
~ -[CSLUIPBPropertyValue addArrayValues:] : 120 -> 132
~ -[CSLUIPBPropertyValue arrayValuesCount] : 16 -> 20
~ -[CSLUIPBPropertyValue arrayValuesAtIndex:] : 16 -> 20
~ -[CSLUIPBPropertyValue description] : 176 -> 164
~ -[CSLUIPBPropertyValue dictionaryRepresentation] : 668 -> 680
~ _CSLUIPBPropertyValueReadFrom : 876 -> 852
~ -[CSLUIPBPropertyValue writeTo:] : 436 -> 468
~ -[CSLUIPBPropertyValue copyTo:] : 312 -> 332
~ -[CSLUIPBPropertyValue copyWithZone:] : 500 -> 556
~ -[CSLUIPBPropertyValue isEqual:] : 320 -> 376
~ -[CSLUIPBPropertyValue hash] : 188 -> 216
~ -[CSLUIPBPropertyValue mergeFrom:] : 476 -> 520
~ -[CSLUIPBPropertyValue stringValue] : 16 -> 20
~ -[CSLUIPBPropertyValue setStringValue:] : 80 -> 20
~ -[CSLUIPBPropertyValue numberValue] : 16 -> 20
~ -[CSLUIPBPropertyValue setNumberValue:] : 80 -> 20
~ -[CSLUIPBPropertyValue uUIDValue] : 16 -> 20
~ -[CSLUIPBPropertyValue setUUIDValue:] : 80 -> 20
~ -[CSLUIPBPropertyValue dataValue] : 16 -> 20
~ -[CSLUIPBPropertyValue setDataValue:] : 80 -> 20
~ -[CSLUIPBPropertyValue sizeValue] : 16 -> 20
~ -[CSLUIPBPropertyValue setSizeValue:] : 80 -> 20
~ -[CSLUIPBPropertyValue dictionaryKey] : 16 -> 20
~ -[CSLUIPBPropertyValue setDictionaryKey:] : 80 -> 20
~ -[CSLUIPBPropertyValue arrayValues] : 16 -> 20
~ -[CSLUIPBPropertyValue setArrayValues:] : 80 -> 20
~ -[CSLUIPBUIPluginListRequest description] : 176 -> 164
~ _CSLUIPBUIPluginListRequestReadFrom : 372 -> 368
~ -[UITriggerTableViewController viewDidLoad] : 412 -> 404
~ -[UITriggerTableViewController dealloc] : 240 -> 216
~ -[UITriggerTableViewController viewWillLayoutSubviews] : 220 -> 208
~ -[UITriggerTableViewController numberOfSectionsInTableView:] : 84 -> 80
~ -[UITriggerTableViewController tableView:numberOfRowsInSection:] : 168 -> 152
~ -[UITriggerTableViewController tableView:cellForRowAtIndexPath:] : 380 -> 348
~ -[UITriggerTableViewController tableView:titleForHeaderInSection:] : 116 -> 108
~ -[UITriggerTableViewController sectionStringForIndexPath:] : 148 -> 140
~ -[UITriggerTableViewController tailStringForIndexPath:] : 208 -> 192
~ -[UITriggerTableViewController tableView:didSelectRowAtIndexPath:] : 360 -> 352
~ -[UITriggerTableViewController _extractSections:] : 780 -> 752
~ -[UITriggerTableViewController idsUIProvidersResponse:] : 284 -> 264
~ -[UITriggerTableViewController idsRequestUITriggerResponse:] : 344 -> 324
~ -[UITriggerTableViewController sendProtobufRequest:type:priority:expectsResponse:errorHandler:withTimeout:] : 664 -> 636
~ -[UITriggerTableViewController requestPluginList] : 116 -> 112
~ -[UITriggerTableViewController triggerUIProvider:] : 148 -> 144
~ -[UITriggerTableViewController idsService] : 16 -> 20
~ -[UITriggerTableViewController setIdsService:] : 80 -> 20
~ -[UITriggerTableViewController loading] : 16 -> 20
~ -[UITriggerTableViewController setLoading:] : 16 -> 20
~ -[UITriggerTableViewController sectionList] : 16 -> 20
~ -[UITriggerTableViewController setSectionList:] : 80 -> 20
~ -[UITriggerTableViewController sectionContents] : 16 -> 20
~ -[UITriggerTableViewController setSectionContents:] : 80 -> 20
~ -[CSLUIPBNumber setInt32Value:] : 36 -> 44
~ -[CSLUIPBNumber setHasInt32Value:] : 40 -> 44
~ -[CSLUIPBNumber hasInt32Value] : 20 -> 24
~ -[CSLUIPBNumber setFloatValue:] : 36 -> 44
~ -[CSLUIPBNumber setHasFloatValue:] : 40 -> 44
~ -[CSLUIPBNumber hasFloatValue] : 20 -> 24
~ -[CSLUIPBNumber setDoubleValue:] : 36 -> 44
~ -[CSLUIPBNumber setHasDoubleValue:] : 28 -> 32
~ -[CSLUIPBNumber hasDoubleValue] : 20 -> 24
~ -[CSLUIPBNumber setBoolValue:] : 36 -> 44
~ -[CSLUIPBNumber setHasBoolValue:] : 40 -> 44
~ -[CSLUIPBNumber hasBoolValue] : 20 -> 24
~ -[CSLUIPBNumber setInt64Value:] : 36 -> 44
~ -[CSLUIPBNumber setHasInt64Value:] : 40 -> 44
~ -[CSLUIPBNumber hasInt64Value] : 20 -> 24
~ -[CSLUIPBNumber description] : 176 -> 164
~ _CSLUIPBNumberReadFrom : 1576 -> 1612
~ -[CSLUIPBNumber writeTo:] : 256 -> 280
~ -[CSLUIPBNumber copyTo:] : 280 -> 304
~ -[CSLUIPBNumber copyWithZone:] : 260 -> 304
~ -[CSLUIPBNumber isEqual:] : 316 -> 364
~ -[CSLUIPBNumber mergeFrom:] : 280 -> 304
~ -[CSLUIPBNumber int32Value] : 16 -> 20
~ -[CSLUIPBNumber floatValue] : 16 -> 20
~ -[CSLUIPBNumber doubleValue] : 16 -> 20
~ -[CSLUIPBNumber boolValue] : 16 -> 20
~ -[CSLUIPBNumber int64Value] : 16 -> 20
~ -[CSLUIPBUIPluginTriggerRequest hasName] : 24 -> 28
~ -[CSLUIPBUIPluginTriggerRequest clearDictionarys] : 16 -> 20
~ -[CSLUIPBUIPluginTriggerRequest addDictionary:] : 120 -> 132
~ -[CSLUIPBUIPluginTriggerRequest dictionarysCount] : 16 -> 20
~ -[CSLUIPBUIPluginTriggerRequest dictionaryAtIndex:] : 16 -> 20
~ -[CSLUIPBUIPluginTriggerRequest setReason:] : 36 -> 44
~ -[CSLUIPBUIPluginTriggerRequest setHasReason:] : 28 -> 32
~ -[CSLUIPBUIPluginTriggerRequest hasReason] : 20 -> 24
~ -[CSLUIPBUIPluginTriggerRequest description] : 176 -> 164
~ -[CSLUIPBUIPluginTriggerRequest dictionaryRepresentation] : 520 -> 528
~ _CSLUIPBUIPluginTriggerRequestReadFrom : 828 -> 848
~ -[CSLUIPBUIPluginTriggerRequest writeTo:] : 344 -> 364
~ -[CSLUIPBUIPluginTriggerRequest copyTo:] : 236 -> 248
~ -[CSLUIPBUIPluginTriggerRequest copyWithZone:] : 392 -> 420
~ -[CSLUIPBUIPluginTriggerRequest isEqual:] : 220 -> 252
~ -[CSLUIPBUIPluginTriggerRequest hash] : 124 -> 140
~ -[CSLUIPBUIPluginTriggerRequest mergeFrom:] : 340 -> 364
~ -[CSLUIPBUIPluginTriggerRequest name] : 16 -> 20
~ -[CSLUIPBUIPluginTriggerRequest setName:] : 80 -> 20
~ -[CSLUIPBUIPluginTriggerRequest dictionarys] : 16 -> 20
~ -[CSLUIPBUIPluginTriggerRequest setDictionarys:] : 80 -> 20
~ -[CSLUIPBUIPluginTriggerRequest reason] : 16 -> 20
~ -[CSLUIPBUIPluginListResponse clearNames] : 16 -> 20
~ -[CSLUIPBUIPluginListResponse addName:] : 120 -> 132
~ -[CSLUIPBUIPluginListResponse namesCount] : 16 -> 20
~ -[CSLUIPBUIPluginListResponse nameAtIndex:] : 16 -> 20
~ -[CSLUIPBUIPluginListResponse clearUsages] : 16 -> 20
~ -[CSLUIPBUIPluginListResponse addUsage:] : 120 -> 132
~ -[CSLUIPBUIPluginListResponse usagesCount] : 16 -> 20
~ -[CSLUIPBUIPluginListResponse usageAtIndex:] : 16 -> 20
~ -[CSLUIPBUIPluginListResponse description] : 176 -> 164
~ -[CSLUIPBUIPluginListResponse dictionaryRepresentation] : 140 -> 144
~ _CSLUIPBUIPluginListResponseReadFrom : 488 -> 476
~ -[CSLUIPBUIPluginListResponse writeTo:] : 432 -> 448
~ -[CSLUIPBUIPluginListResponse copyTo:] : 260 -> 252
~ -[CSLUIPBUIPluginListResponse copyWithZone:] : 488 -> 504
~ -[CSLUIPBUIPluginListResponse isEqual:] : 160 -> 176
~ -[CSLUIPBUIPluginListResponse hash] : 72 -> 80
~ -[CSLUIPBUIPluginListResponse mergeFrom:] : 424 -> 440
~ -[CSLUIPBUIPluginListResponse names] : 16 -> 20
~ -[CSLUIPBUIPluginListResponse setNames:] : 80 -> 20
~ -[CSLUIPBUIPluginListResponse usages] : 16 -> 20
~ -[CSLUIPBUIPluginListResponse setUsages:] : 80 -> 20
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"CSLUIPBNumber\""
- "@\"CSLUIPBPropertyValue\""
- "@\"CSLUIPBSize\""
- "@\"IDSService\""
- "@\"NSArray\"24@0:8@\"UITableView\"16"
- "@\"NSArray\"32@0:8@\"UITableView\"16@\"NSIndexPath\"24"
- "@\"NSData\""
- "@\"NSIndexPath\"24@0:8@\"UITableView\"16"
- "@\"NSIndexPath\"32@0:8@\"UITableView\"16@\"NSIndexPath\"24"
- "@\"NSIndexPath\"40@0:8@\"UITableView\"16@\"NSIndexPath\"24@\"NSIndexPath\"32"
- "@\"NSMutableArray\""
- "@\"NSMutableDictionary\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSString\"32@0:8@\"UITableView\"16@\"NSIndexPath\"24"
- "@\"NSString\"32@0:8@\"UITableView\"16q24"
- "@\"UIContextMenuConfiguration\"48@0:8@\"UITableView\"16@\"NSIndexPath\"24{CGPoint=dd}32"
- "@\"UISwipeActionsConfiguration\"32@0:8@\"UITableView\"16@\"NSIndexPath\"24"
- "@\"UITableViewCell\"32@0:8@\"UITableView\"16@\"NSIndexPath\"24"
- "@\"UITargetedPreview\"32@0:8@\"UITableView\"16@\"UIContextMenuConfiguration\"24"
- "@\"UIView\"24@0:8@\"UIScrollView\"16"
- "@\"UIView\"32@0:8@\"UITableView\"16q24"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8Q16"
- "@24@0:8^{_NSZone=}16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16q24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@48@0:8@16@24{CGPoint=dd}32"
- "@56@0:8@16S24q28B36@?40d48"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@\"UIScrollView\"16"
- "B24@0:8@16"
- "B32@0:8@\"UITableView\"16@\"NSIndexPath\"24"
- "B32@0:8@\"UITableView\"16@\"UITableViewFocusUpdateContext\"24"
- "B32@0:8@16@24"
- "B40@0:8@\"UITableView\"16@\"NSIndexPath\"24@\"<UISpringLoadedInteractionContext>\"32"
- "B40@0:8@16@24@32"
- "B48@0:8@\"UITableView\"16:24@\"NSIndexPath\"32@40"
- "B48@0:8@16:24@32@40"
- "CSLUIPBNumber"
- "CSLUIPBProperty"
- "CSLUIPBPropertyValue"
- "CSLUIPBSize"
- "CSLUIPBUIPluginListRequest"
- "CSLUIPBUIPluginListResponse"
- "CSLUIPBUIPluginTriggerRequest"
- "CSLUIPBUIPluginTriggerResponse"
- "CSLUIUITriggerIDSProtocolResponse"
- "IDSServiceDelegate"
- "NSCopying"
- "NSObject"
- "Q16@0:8"
- "T#,R"
- "T@\"CSLUIPBNumber\",&,N,V_numberValue"
- "T@\"CSLUIPBPropertyValue\",&,N,V_dictionaryKey"
- "T@\"CSLUIPBPropertyValue\",&,N,V_value"
- "T@\"CSLUIPBSize\",&,N,V_sizeValue"
- "T@\"IDSService\",&,N,V_idsService"
- "T@\"NSData\",&,N,V_dataValue"
- "T@\"NSData\",&,N,V_uUIDValue"
- "T@\"NSMutableArray\",&,N,V_arrayValues"
- "T@\"NSMutableArray\",&,N,V_dictionarys"
- "T@\"NSMutableArray\",&,N,V_names"
- "T@\"NSMutableArray\",&,N,V_sectionList"
- "T@\"NSMutableArray\",&,N,V_usages"
- "T@\"NSMutableDictionary\",&,N,V_sectionContents"
- "T@\"NSString\",&,N,V_errorString"
- "T@\"NSString\",&,N,V_name"
- "T@\"NSString\",&,N,V_stringValue"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TB,N"
- "TB,N,V_boolValue"
- "TB,N,V_loading"
- "TB,N,V_success"
- "TB,R,N"
- "TQ,R"
- "Td,N,V_doubleValue"
- "Tf,N,V_floatValue"
- "Tf,N,V_height"
- "Tf,N,V_width"
- "Ti,N,V_int32Value"
- "Ti,N,V_reason"
- "Tq,N,V_int64Value"
- "UIScrollViewDelegate"
- "UITableViewDataSource"
- "UITableViewDelegate"
- "UITriggerTableViewController"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_arrayValues"
- "_boolValue"
- "_dataValue"
- "_dictionaryKey"
- "_dictionarys"
- "_doubleValue"
- "_errorString"
- "_extractSections:"
- "_floatValue"
- "_has"
- "_height"
- "_idsService"
- "_int32Value"
- "_int64Value"
- "_loading"
- "_name"
- "_names"
- "_numberValue"
- "_reason"
- "_sectionContents"
- "_sectionList"
- "_setError"
- "_sizeValue"
- "_stringValue"
- "_success"
- "_uUIDValue"
- "_usages"
- "_value"
- "_width"
- "accounts"
- "actionWithTitle:style:handler:"
- "addAction:"
- "addArrayValues:"
- "addDelegate:queue:"
- "addDictionary:"
- "addName:"
- "addObject:"
- "addUsage:"
- "alertControllerWithTitle:message:preferredStyle:"
- "allocWithZone:"
- "anyObject"
- "arrayValuesAtIndex:"
- "arrayValuesCount"
- "autorelease"
- "bounds"
- "class"
- "clearArrayValues"
- "clearDictionarys"
- "clearNames"
- "clearUsages"
- "compare:options:"
- "componentsSeparatedByString:"
- "conformsToProtocol:"
- "copyTo:"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "d"
- "d16@0:8"
- "d32@0:8@\"UITableView\"16@\"NSIndexPath\"24"
- "d32@0:8@\"UITableView\"16q24"
- "d32@0:8@16@24"
- "d32@0:8@16q24"
- "data"
- "dataSource"
- "dealloc"
- "debugDescription"
- "delegate"
- "dequeueReusableCellWithIdentifier:"
- "description"
- "deselectRowAtIndexPath:animated:"
- "dictionaryAtIndex:"
- "dictionaryRepresentation"
- "dictionaryWithObjects:forKeys:count:"
- "dictionarys"
- "dictionarysCount"
- "didReceiveMemoryWarning"
- "f"
- "f16@0:8"
- "getBytes:range:"
- "hasBoolValue"
- "hasDataValue"
- "hasDictionaryKey"
- "hasDoubleValue"
- "hasError"
- "hasErrorString"
- "hasFloatValue"
- "hasInt32Value"
- "hasInt64Value"
- "hasName"
- "hasNumberValue"
- "hasPrefix:"
- "hasReason"
- "hasSizeValue"
- "hasStringValue"
- "hasUUIDValue"
- "hasValue"
- "hash"
- "i"
- "i16@0:8"
- "idsRequestUITriggerResponse:"
- "idsService"
- "idsUIProvidersResponse:"
- "indexPathForPreferredFocusedViewInTableView:"
- "init"
- "initWithCapacity:"
- "initWithData:"
- "initWithFrame:style:"
- "initWithProtobufData:type:isResponse:"
- "initWithService:"
- "initWithStyle:reuseIdentifier:"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "length"
- "loading"
- "mainScreen"
- "mergeFrom:"
- "nameAtIndex:"
- "names"
- "namesCount"
- "numberOfSectionsInTableView:"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithFloat:"
- "numberWithInt:"
- "numberWithLongLong:"
- "objectAtIndex:"
- "objectAtIndexedSubscript:"
- "objectForKeyedSubscript:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "position"
- "presentViewController:animated:completion:"
- "q"
- "q16@0:8"
- "q24@0:8@\"UITableView\"16"
- "q24@0:8@16"
- "q32@0:8@\"UITableView\"16@\"NSIndexPath\"24"
- "q32@0:8@\"UITableView\"16q24"
- "q32@0:8@16@24"
- "q32@0:8@16q24"
- "q40@0:8@\"UITableView\"16@\"NSString\"24q32"
- "q40@0:8@16@24q32"
- "readFrom:"
- "release"
- "reloadData"
- "removeAllObjects"
- "requestPluginList"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "row"
- "scrollViewDidChangeAdjustedContentInset:"
- "scrollViewDidEndDecelerating:"
- "scrollViewDidEndDragging:willDecelerate:"
- "scrollViewDidEndScrollingAnimation:"
- "scrollViewDidEndZooming:withView:atScale:"
- "scrollViewDidScroll:"
- "scrollViewDidScrollToTop:"
- "scrollViewDidZoom:"
- "scrollViewShouldScrollToTop:"
- "scrollViewWillBeginDecelerating:"
- "scrollViewWillBeginDragging:"
- "scrollViewWillBeginZooming:withView:"
- "scrollViewWillEndDragging:withVelocity:targetContentOffset:"
- "section"
- "sectionContents"
- "sectionIndexTitlesForTableView:"
- "sectionList"
- "sectionStringForIndexPath:"
- "self"
- "sendProtobuf:fromAccount:toDestinations:priority:options:identifier:error:"
- "sendProtobufRequest:type:priority:expectsResponse:errorHandler:withTimeout:"
- "service:account:didReceiveLocalNetworkHandshake:fromID:context:"
- "service:account:identifier:didSendWithSuccess:error:"
- "service:account:identifier:didSendWithSuccess:error:context:"
- "service:account:identifier:fromID:hasBeenDeliveredWithContext:"
- "service:account:identifier:hasBeenDeliveredWithContext:"
- "service:account:identifier:sentBytes:totalBytes:"
- "service:account:incomingData:fromID:context:"
- "service:account:incomingMessage:fromID:context:"
- "service:account:incomingOpportunisticData:withIdentifier:fromID:context:"
- "service:account:incomingPendingMessageOfType:fromID:context:"
- "service:account:incomingResourceAtURL:fromID:context:"
- "service:account:incomingResourceAtURL:metadata:fromID:context:"
- "service:account:incomingUnhandledProtobuf:fromID:context:"
- "service:account:inviteDroppedForSessionID:fromID:context:error:"
- "service:account:inviteReceivedForSession:fromID:"
- "service:account:inviteReceivedForSession:fromID:withContext:"
- "service:account:inviteReceivedForSession:fromID:withOptions:"
- "service:account:pendingResourceWithMetadata:fromID:acknowledgementBlock:context:"
- "service:account:receivedGroupSessionParticipantDataUpdate:"
- "service:account:receivedGroupSessionParticipantUpdate:"
- "service:account:receivedGroupSessionParticipantUpdate:context:"
- "service:activeAccountsChanged:"
- "service:connectedDevicesChanged:"
- "service:devicesChanged:"
- "service:didCancelMessageWithSuccess:error:identifier:"
- "service:didSendOpportunisticDataWithIdentifier:toIDs:"
- "service:didSwitchActivePairedDevice:acknowledgementBlock:"
- "service:linkedDevicesChanged:"
- "service:nearbyDevicesChanged:"
- "serviceAllowedTrafficClassifiersDidReset:"
- "serviceSpaceDidBecomeAvailable:"
- "setArrayValues:"
- "setBoolValue:"
- "setDataSource:"
- "setDataValue:"
- "setDelegate:"
- "setDictionaryKey:"
- "setDictionarys:"
- "setDoubleValue:"
- "setErrorString:"
- "setFloatValue:"
- "setFrame:"
- "setHasBoolValue:"
- "setHasDoubleValue:"
- "setHasFloatValue:"
- "setHasInt32Value:"
- "setHasInt64Value:"
- "setHasReason:"
- "setHeight:"
- "setIdsService:"
- "setInt32Value:"
- "setInt64Value:"
- "setLoading:"
- "setName:"
- "setNames:"
- "setNumberValue:"
- "setObject:forKey:"
- "setPosition:"
- "setProtobufAction:forIncomingResponsesOfType:"
- "setReason:"
- "setSectionContents:"
- "setSectionList:"
- "setSizeValue:"
- "setStringValue:"
- "setSuccess:"
- "setTableView:"
- "setText:"
- "setUUIDValue:"
- "setUsages:"
- "setValue:"
- "setView:"
- "setWidth:"
- "setWithObject:"
- "sharedApplication"
- "sortedArrayUsingComparator:"
- "statusBarFrame"
- "stringWithFormat:"
- "substringFromIndex:"
- "superclass"
- "tableView"
- "tableView:accessoryButtonTappedForRowWithIndexPath:"
- "tableView:accessoryTypeForRowWithIndexPath:"
- "tableView:canEditRowAtIndexPath:"
- "tableView:canFocusRowAtIndexPath:"
- "tableView:canMoveRowAtIndexPath:"
- "tableView:canPerformAction:forRowAtIndexPath:withSender:"
- "tableView:canPerformPrimaryActionForRowAtIndexPath:"
- "tableView:cellForRowAtIndexPath:"
- "tableView:commitEditingStyle:forRowAtIndexPath:"
- "tableView:contextMenuConfigurationForRowAtIndexPath:point:"
- "tableView:didBeginMultipleSelectionInteractionAtIndexPath:"
- "tableView:didDeselectRowAtIndexPath:"
- "tableView:didEndDisplayingCell:forRowAtIndexPath:"
- "tableView:didEndDisplayingFooterView:forSection:"
- "tableView:didEndDisplayingHeaderView:forSection:"
- "tableView:didEndEditingRowAtIndexPath:"
- "tableView:didHighlightRowAtIndexPath:"
- "tableView:didSelectRowAtIndexPath:"
- "tableView:didUnhighlightRowAtIndexPath:"
- "tableView:didUpdateFocusInContext:withAnimationCoordinator:"
- "tableView:editActionsForRowAtIndexPath:"
- "tableView:editingStyleForRowAtIndexPath:"
- "tableView:estimatedHeightForFooterInSection:"
- "tableView:estimatedHeightForHeaderInSection:"
- "tableView:estimatedHeightForRowAtIndexPath:"
- "tableView:heightForFooterInSection:"
- "tableView:heightForHeaderInSection:"
- "tableView:heightForRowAtIndexPath:"
- "tableView:indentationLevelForRowAtIndexPath:"
- "tableView:leadingSwipeActionsConfigurationForRowAtIndexPath:"
- "tableView:moveRowAtIndexPath:toIndexPath:"
- "tableView:numberOfRowsInSection:"
- "tableView:performAction:forRowAtIndexPath:withSender:"
- "tableView:performPrimaryActionForRowAtIndexPath:"
- "tableView:previewForDismissingContextMenuWithConfiguration:"
- "tableView:previewForHighlightingContextMenuWithConfiguration:"
- "tableView:sectionForSectionIndexTitle:atIndex:"
- "tableView:selectionFollowsFocusForRowAtIndexPath:"
- "tableView:shouldBeginMultipleSelectionInteractionAtIndexPath:"
- "tableView:shouldHighlightRowAtIndexPath:"
- "tableView:shouldIndentWhileEditingRowAtIndexPath:"
- "tableView:shouldShowMenuForRowAtIndexPath:"
- "tableView:shouldSpringLoadRowAtIndexPath:withContext:"
- "tableView:shouldUpdateFocusInContext:"
- "tableView:targetIndexPathForMoveFromRowAtIndexPath:toProposedIndexPath:"
- "tableView:titleForDeleteConfirmationButtonForRowAtIndexPath:"
- "tableView:titleForFooterInSection:"
- "tableView:titleForHeaderInSection:"
- "tableView:trailingSwipeActionsConfigurationForRowAtIndexPath:"
- "tableView:viewForFooterInSection:"
- "tableView:viewForHeaderInSection:"
- "tableView:willBeginEditingRowAtIndexPath:"
- "tableView:willDeselectRowAtIndexPath:"
- "tableView:willDisplayCell:forRowAtIndexPath:"
- "tableView:willDisplayContextMenuWithConfiguration:animator:"
- "tableView:willDisplayFooterView:forSection:"
- "tableView:willDisplayHeaderView:forSection:"
- "tableView:willEndContextMenuInteractionWithConfiguration:animator:"
- "tableView:willPerformPreviewActionForMenuWithConfiguration:animator:"
- "tableView:willSelectRowAtIndexPath:"
- "tableViewDidEndMultipleSelectionInteraction:"
- "tailStringForIndexPath:"
- "textLabel"
- "triggerUIProvider:"
- "uUIDValue"
- "usageAtIndex:"
- "usages"
- "usagesCount"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8f16"
- "v20@0:8i16"
- "v24@0:8@\"IDSProtobuf\"16"
- "v24@0:8@\"IDSService\"16"
- "v24@0:8@\"UIScrollView\"16"
- "v24@0:8@\"UITableView\"16"
- "v24@0:8@16"
- "v24@0:8d16"
- "v24@0:8q16"
- "v28@0:8@\"UIScrollView\"16B24"
- "v28@0:8@16B24"
- "v32@0:8@\"IDSService\"16@\"NSArray\"24"
- "v32@0:8@\"IDSService\"16@\"NSSet\"24"
- "v32@0:8@\"UIScrollView\"16@\"UIView\"24"
- "v32@0:8@\"UITableView\"16@\"NSIndexPath\"24"
- "v32@0:8@16@24"
- "v40@0:8@\"IDSService\"16@\"IDSAccount\"24@\"IDSGroupSessionParticipantUpdate\"32"
- "v40@0:8@\"IDSService\"16@\"IDSDevice\"24@?<v@?>32"
- "v40@0:8@\"IDSService\"16@\"NSString\"24@\"NSArray\"32"
- "v40@0:8@\"UIScrollView\"16@\"UIView\"24d32"
- "v40@0:8@\"UITableView\"16@\"NSIndexPath\"24@\"NSIndexPath\"32"
- "v40@0:8@\"UITableView\"16@\"UIContextMenuConfiguration\"24@\"<UIContextMenuInteractionAnimating>\"32"
- "v40@0:8@\"UITableView\"16@\"UIContextMenuConfiguration\"24@\"<UIContextMenuInteractionCommitAnimating>\"32"
- "v40@0:8@\"UITableView\"16@\"UITableViewCell\"24@\"NSIndexPath\"32"
- "v40@0:8@\"UITableView\"16@\"UITableViewFocusUpdateContext\"24@\"UIFocusAnimationCoordinator\"32"
- "v40@0:8@\"UITableView\"16@\"UIView\"24q32"
- "v40@0:8@\"UITableView\"16q24@\"NSIndexPath\"32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24@?32"
- "v40@0:8@16@24d32"
- "v40@0:8@16@24q32"
- "v40@0:8@16q24@32"
- "v44@0:8@\"IDSService\"16B24@\"NSError\"28@\"NSString\"36"
- "v44@0:8@16B24@28@36"
- "v48@0:8@\"IDSService\"16@\"IDSAccount\"24@\"IDSGroupSessionParticipantUpdate\"32@\"IDSMessageContext\"40"
- "v48@0:8@\"IDSService\"16@\"IDSAccount\"24@\"IDSSession\"32@\"NSString\"40"
- "v48@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSString\"32@40"
- "v48@0:8@\"UIScrollView\"16{CGPoint=dd}24N^{CGPoint=dd}40"
- "v48@0:8@\"UITableView\"16:24@\"NSIndexPath\"32@40"
- "v48@0:8@16:24@32@40"
- "v48@0:8@16@24@32@40"
- "v48@0:8@16{CGPoint=dd}24N^{CGPoint=dd}40"
- "v52@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSString\"32B40@\"NSError\"44"
- "v52@0:8@\"IDSService\"16@\"IDSAccount\"24B32@\"NSString\"36@\"NSData\"44"
- "v52@0:8@16@24@32B40@44"
- "v52@0:8@16@24B32@36@44"
- "v56@0:8@\"IDSService\"16@\"IDSAccount\"24@\"IDSProtobuf\"32@\"NSString\"40@\"IDSMessageContext\"48"
- "v56@0:8@\"IDSService\"16@\"IDSAccount\"24@\"IDSSession\"32@\"NSString\"40@\"NSData\"48"
- "v56@0:8@\"IDSService\"16@\"IDSAccount\"24@\"IDSSession\"32@\"NSString\"40@\"NSDictionary\"48"
- "v56@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSData\"32@\"NSString\"40@\"IDSMessageContext\"48"
- "v56@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSDictionary\"32@\"NSString\"40@\"IDSMessageContext\"48"
- "v56@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSString\"32@\"NSString\"40@48"
- "v56@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSString\"32q40q48"
- "v56@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSURL\"32@\"NSString\"40@\"IDSMessageContext\"48"
- "v56@0:8@\"IDSService\"16@\"IDSAccount\"24q32@\"NSString\"40@\"IDSMessageContext\"48"
- "v56@0:8@16@24@32@40@48"
- "v56@0:8@16@24@32q40q48"
- "v56@0:8@16@24q32@40@48"
- "v60@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSString\"32B40@\"NSError\"44@\"IDSMessageContext\"52"
- "v60@0:8@16@24@32B40@44@52"
- "v64@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSData\"32@\"NSString\"40@\"NSString\"48@\"IDSMessageContext\"56"
- "v64@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSDictionary\"32@\"NSString\"40@?<v@?B>48@\"IDSMessageContext\"56"
- "v64@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSString\"32@\"NSString\"40@\"NSData\"48@\"NSError\"56"
- "v64@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSURL\"32@\"NSDictionary\"40@\"NSString\"48@\"IDSMessageContext\"56"
- "v64@0:8@16@24@32@40@48@56"
- "v64@0:8@16@24@32@40@?48@56"
- "viewDidLoad"
- "viewForZoomingInScrollView:"
- "viewWillLayoutSubviews"
- "writeTo:"
- "zone"
- "{?=\"doubleValue\"b1\"int64Value\"b1\"floatValue\"b1\"int32Value\"b1\"boolValue\"b1}"
- "{?=\"reason\"b1}"

```
