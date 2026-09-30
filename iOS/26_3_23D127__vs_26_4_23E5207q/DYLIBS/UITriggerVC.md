## UITriggerVC

> `/System/Library/PrivateFrameworks/UITriggerVC.framework/UITriggerVC`

```diff

-1114.2.10.0.0
-  __TEXT.__text: 0x690c
-  __TEXT.__auth_stubs: 0x300
+1114.4.41.0.0
+  __TEXT.__text: 0x6f18
+  __TEXT.__auth_stubs: 0x2e0
   __TEXT.__objc_methlist: 0xfc0
   __TEXT.__const: 0x58
   __TEXT.__cstring: 0x30d
-  __TEXT.__unwind_info: 0x220
+  __TEXT.__unwind_info: 0x298
   __TEXT.__objc_classname: 0x15f
   __TEXT.__objc_methname: 0x239e
   __TEXT.__objc_methtype: 0x1360

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x970
   __DATA_CONST.__objc_superrefs: 0x48
-  __AUTH_CONST.__auth_got: 0x188
+  __AUTH_CONST.__auth_got: 0x178
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x520
   __AUTH_CONST.__objc_const: 0x12f8

   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F0688057-B4F8-3DB3-8C2C-2050B9B1D7EA
+  UUID: F57C8E74-D605-39C4-BBA7-86C5DC88AD2B
   Functions: 200
-  Symbols:   747
+  Symbols:   745
   CStrings:  604
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x22
+ _objc_retain_x24
+ _objc_retain_x26
- _objc_claimAutoreleasedReturnValue
- _objc_release_x1
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x6
- _objc_retain_x8
Functions:
~ -[CSLUIPBUIPluginTriggerResponse description] : 164 -> 176
~ -[CSLUIPBUIPluginTriggerResponse dictionaryRepresentation] : 168 -> 176
~ _CSLUIPBUIPluginTriggerResponseReadFrom : 696 -> 700
~ -[CSLUIPBUIPluginTriggerResponse writeTo:] : 116 -> 124
~ -[CSLUIPBUIPluginTriggerResponse setErrorString:] : 20 -> 80
~ -[CSLUIPBProperty description] : 164 -> 176
~ -[CSLUIPBProperty dictionaryRepresentation] : 156 -> 164
~ _CSLUIPBPropertyReadFrom : 568 -> 576
~ -[CSLUIPBProperty writeTo:] : 128 -> 124
~ -[CSLUIPBProperty copyTo:] : 120 -> 116
~ -[CSLUIPBProperty mergeFrom:] : 144 -> 148
~ -[CSLUIPBProperty setName:] : 20 -> 80
~ -[CSLUIPBProperty setValue:] : 20 -> 80
~ -[CSLUIPBSize description] : 164 -> 176
~ -[CSLUIPBSize dictionaryRepresentation] : 188 -> 200
~ _CSLUIPBSizeReadFrom : 760 -> 768
~ -[CSLUIPBSize writeTo:] : 124 -> 132
~ -[CSLUIPBPropertyValue addArrayValues:] : 128 -> 120
~ -[CSLUIPBPropertyValue description] : 164 -> 176
~ -[CSLUIPBPropertyValue dictionaryRepresentation] : 648 -> 668
~ _CSLUIPBPropertyValueReadFrom : 852 -> 876
~ -[CSLUIPBPropertyValue copyTo:] : 308 -> 312
~ -[CSLUIPBPropertyValue setStringValue:] : 20 -> 80
~ -[CSLUIPBPropertyValue setNumberValue:] : 20 -> 80
~ -[CSLUIPBPropertyValue setUUIDValue:] : 20 -> 80
~ -[CSLUIPBPropertyValue setDataValue:] : 20 -> 80
~ -[CSLUIPBPropertyValue setSizeValue:] : 20 -> 80
~ -[CSLUIPBPropertyValue setDictionaryKey:] : 20 -> 80
~ -[CSLUIPBPropertyValue setArrayValues:] : 20 -> 80
~ -[CSLUIPBUIPluginListRequest description] : 164 -> 176
~ -[UITriggerTableViewController viewDidLoad] : 400 -> 412
~ -[UITriggerTableViewController dealloc] : 216 -> 240
~ -[UITriggerTableViewController viewWillLayoutSubviews] : 208 -> 220
~ -[UITriggerTableViewController numberOfSectionsInTableView:] : 80 -> 84
~ -[UITriggerTableViewController tableView:numberOfRowsInSection:] : 152 -> 168
~ -[UITriggerTableViewController tableView:cellForRowAtIndexPath:] : 348 -> 380
~ -[UITriggerTableViewController tableView:titleForHeaderInSection:] : 108 -> 116
~ -[UITriggerTableViewController sectionStringForIndexPath:] : 140 -> 148
~ -[UITriggerTableViewController tailStringForIndexPath:] : 192 -> 208
~ -[UITriggerTableViewController tableView:didSelectRowAtIndexPath:] : 352 -> 360
~ -[UITriggerTableViewController _extractSections:] : 748 -> 780
~ -[UITriggerTableViewController idsUIProvidersResponse:] : 264 -> 284
~ -[UITriggerTableViewController idsRequestUITriggerResponse:] : 324 -> 344
~ -[UITriggerTableViewController sendProtobufRequest:type:priority:expectsResponse:errorHandler:withTimeout:] : 640 -> 664
~ -[UITriggerTableViewController requestPluginList] : 112 -> 116
~ -[UITriggerTableViewController triggerUIProvider:] : 144 -> 148
~ -[UITriggerTableViewController setIdsService:] : 20 -> 80
~ -[UITriggerTableViewController setSectionList:] : 20 -> 80
~ -[UITriggerTableViewController setSectionContents:] : 20 -> 80
~ -[CSLUIPBNumber description] : 164 -> 176
~ -[CSLUIPBNumber dictionaryRepresentation] : 420 -> 444
~ _CSLUIPBNumberReadFrom : 1568 -> 1576
~ -[CSLUIPBNumber copyTo:] : 260 -> 280
~ -[CSLUIPBNumber mergeFrom:] : 260 -> 280
~ -[CSLUIPBUIPluginTriggerRequest addDictionary:] : 128 -> 120
~ -[CSLUIPBUIPluginTriggerRequest description] : 164 -> 176
~ -[CSLUIPBUIPluginTriggerRequest dictionaryRepresentation] : 508 -> 520
~ _CSLUIPBUIPluginTriggerRequestReadFrom : 824 -> 828
~ -[CSLUIPBUIPluginTriggerRequest copyTo:] : 232 -> 236
~ -[CSLUIPBUIPluginTriggerRequest setName:] : 20 -> 80
~ -[CSLUIPBUIPluginTriggerRequest setDictionarys:] : 20 -> 80
~ -[CSLUIPBUIPluginListResponse addName:] : 128 -> 120
~ -[CSLUIPBUIPluginListResponse addUsage:] : 128 -> 120
~ -[CSLUIPBUIPluginListResponse description] : 164 -> 176
~ -[CSLUIPBUIPluginListResponse dictionaryRepresentation] : 136 -> 140
~ _CSLUIPBUIPluginListResponseReadFrom : 480 -> 488
~ -[CSLUIPBUIPluginListResponse copyTo:] : 252 -> 260
~ -[CSLUIPBUIPluginListResponse setNames:] : 20 -> 80
~ -[CSLUIPBUIPluginListResponse setUsages:] : 20 -> 80

```
