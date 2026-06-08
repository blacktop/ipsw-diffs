## CommunicationsFilter

> `/System/Library/PrivateFrameworks/CommunicationsFilter.framework/CommunicationsFilter`

```diff

-181.600.11.0.0
-  __TEXT.__text: 0x35d4
-  __TEXT.__auth_stubs: 0x460
+194.100.2.0.0
+  __TEXT.__text: 0x3440
   __TEXT.__objc_methlist: 0x414
   __TEXT.__const: 0xa6
   __TEXT.__cstring: 0x220
-  __TEXT.__gcc_except_tab: 0x214
+  __TEXT.__gcc_except_tab: 0x1fc
   __TEXT.__oslogstring: 0x3d7
   __TEXT.__constg_swiftt: 0x28
   __TEXT.__swift5_typeref: 0x6
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x1f0
-  __TEXT.__objc_classname: 0xcc
-  __TEXT.__objc_methname: 0x87a
-  __TEXT.__objc_methtype: 0x2ac
-  __TEXT.__objc_stubs: 0x880
-  __DATA_CONST.__got: 0x90
+  __TEXT.__unwind_info: 0x208
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x150
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x308
   __DATA_CONST.__objc_superrefs: 0x30
-  __AUTH_CONST.__auth_got: 0x240
+  __DATA_CONST.__got: 0x90
   __AUTH_CONST.__const: 0xb8
   __AUTH_CONST.__cfstring: 0x120
   __AUTH_CONST.__objc_const: 0x828
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x4c
   __DATA.__data: 0x160
   __DATA_DIRTY.__objc_data: 0x1e0

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  UUID: 1BFBE860-B19F-336B-A663-3CF4DAEFA4C5
+  UUID: 105AC292-FE8C-3EFF-B1E0-DC763D73F087
   Functions: 100
-  Symbols:   465
-  CStrings:  236
+  Symbols:   467
+  CStrings:  56
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x2
+ _objc_retain_x24
+ _objc_retain_x3
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x20
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"<CMFXPCServiceProtocol>\""
- "@\"CMFNotificationObserver\""
- "@\"CommunicationFilterItem\""
- "@\"CommunicationsFilterBlockListCache\""
- "@\"NSDictionary\"24@0:8@\"NSObject<OS_xpc_object>\"16"
- "@\"NSMutableArray\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_xpc_object>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8^{_NSZone=}16"
- "@24@0:8^{__CFPhoneNumber=}16"
- "@32@0:8:16@24"
- "@32@0:8@16q24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@?32"
- "@?"
- "@?16@0:8"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "CMFNotificationObserver"
- "CMFXPCService"
- "CMFXPCServiceProtocol"
- "CommunicationFilterItem"
- "CommunicationFilterItemCache"
- "CommunicationsFilterBlockList"
- "CommunicationsFilterBlockListCache"
- "NSCopying"
- "NSObject"
- "Q16@0:8"
- "T#,R"
- "T@\"CMFNotificationObserver\",R,N,V_blockListUpdateObserver"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_queue"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,N,V_name"
- "T@\"NSString\",R,N"
- "T@\"NSString\",R,N,V_emailAddress"
- "T@?,R,C,N,V_callback"
- "TQ,R"
- "T^{__CFPhoneNumber=},R,N,V_phoneNumber"
- "Ti,N,V_token"
- "Tq,N,V_isInList"
- "UTF8String"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "^{__CFPhoneNumber=}"
- "^{__CFPhoneNumber=}16@0:8"
- "__mainThreadPostNotificationName:object:"
- "_acceptItemType:"
- "_acceptVersion:"
- "_appearsToBeEmail"
- "_appearsToBePhoneNumber"
- "_blockListChanged"
- "_blockListUpdateObserver"
- "_cache"
- "_callback"
- "_connect"
- "_connection"
- "_dictionaryRepresentationWithRedaction"
- "_disconnect"
- "_disconnected"
- "_emailAddress"
- "_filterItem"
- "_isInList"
- "_listIsEmpty"
- "_name"
- "_notifyEmptyListToken"
- "_phoneNumber"
- "_queue"
- "_recentItems"
- "_recentObjectsTested"
- "_retries"
- "_sendXPCRequest:completionBlock:"
- "_token"
- "_xpcService"
- "addItemForAllServices:"
- "addObject:"
- "allKeys"
- "allocWithZone:"
- "areItemsInList:"
- "autorelease"
- "blockListUpdateObserver"
- "boolValue"
- "cachedResponseForItem:"
- "callback"
- "caseInsensitiveCompare:"
- "class"
- "conformsToProtocol:"
- "copy"
- "copyAllItems"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "dealloc"
- "debugDescription"
- "defaultCenter"
- "description"
- "dictionary"
- "dictionaryRepresentation"
- "dictionaryWithCapacity:"
- "dictionaryWithDictionary:"
- "emailAddress"
- "errorWithDomain:code:userInfo:"
- "hash"
- "i"
- "i16@0:8"
- "init"
- "initWithCapacity:"
- "initWithDictionaryRepresentation:"
- "initWithEmailAddress:"
- "initWithFilterItem:isInList:"
- "initWithName:queue:callback:"
- "initWithPhoneNumber:"
- "initWithXPCService:"
- "insertObject:atIndex:"
- "intValue"
- "isEmailAddress"
- "isEqual:"
- "isInList"
- "isItemInList:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isPhoneNumber"
- "isProxy"
- "lowercaseString"
- "matchesFilterItem:"
- "matchesItem:"
- "name"
- "numberWithBool:"
- "numberWithInt:"
- "numberWithUnsignedInt:"
- "objectForKey:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "phoneNumber"
- "q"
- "q16@0:8"
- "q24@0:8@16"
- "queue"
- "release"
- "removeAllObjects"
- "removeItemForAllServices:"
- "removeItemFromCache:"
- "removeLastObject"
- "removeObject:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "sendSynchronousXPCRequest:"
- "setIsInList:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setResponse:forItem:"
- "setToken:"
- "sharedInstance"
- "stringWithUTF8String:"
- "superclass"
- "syncListEmptyState"
- "token"
- "unformattedID"
- "unsignedIntegerValue"
- "v16@0:8"
- "v20@0:8i16"
- "v24@0:8@16"
- "v24@0:8q16"
- "v28@0:8B16@20"
- "v32@0:8@16@?24"
- "zone"

```
