## HIDAnalytics

> `/System/Library/PrivateFrameworks/HIDAnalytics.framework/HIDAnalytics`

```diff

-2238.120.5.0.0
-  __TEXT.__text: 0x24c4
-  __TEXT.__auth_stubs: 0x3a0
+2353.0.0.0.1
+  __TEXT.__text: 0x2358
   __TEXT.__objc_methlist: 0x3f4
   __TEXT.__const: 0x58
-  __TEXT.__cstring: 0xc8
+  __TEXT.__cstring: 0xd3
   __TEXT.__gcc_except_tab: 0x3c
   __TEXT.__oslogstring: 0xb2
   __TEXT.__unwind_info: 0x160
-  __TEXT.__objc_classname: 0xac
-  __TEXT.__objc_methname: 0x636
-  __TEXT.__objc_methtype: 0x30a
-  __TEXT.__objc_stubs: 0x640
-  __DATA_CONST.__got: 0x98
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x110
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x250
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x1e0
+  __DATA_CONST.__got: 0x98
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x180
   __AUTH_CONST.__objc_const: 0xb20
   __AUTH_CONST.__objc_intobj: 0x60
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x44
   __DATA.__data: 0xc0
   __DATA_DIRTY.__objc_data: 0x190

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AE398F42-8FE7-348A-9958-8B4889C89AA4
+  UUID: CB67AE74-C08C-3D3A-8034-69D23D39391D
   Functions: 73
-  Symbols:   355
-  CStrings:  181
+  Symbols:   357
+  CStrings:  36
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x25
+ _objc_retain_x8
- _objc_release_x28
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x24
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"HIDAnalyticsHistogramEventField\""
- "@\"NSDictionary\""
- "@\"NSMutableDictionary\""
- "@\"NSMutableSet\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_dispatch_source>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@40@0:8@16^{_HIDAnalyticsHistogramSegmentConfig=CCCQ}24q32"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "C"
- "HIDAnalyticsEvent"
- "HIDAnalyticsEventField"
- "HIDAnalyticsEventFieldProtocol"
- "HIDAnalyticsHistogramEvent"
- "HIDAnalyticsHistogramEventField"
- "HIDAnalyticsReporter"
- "NSObject"
- "Q16@0:8"
- "T#,R"
- "T@\"NSDictionary\",&,V_desc"
- "T@\"NSString\",&,V_name"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,V_fieldName"
- "T@,W"
- "TB,V_isLogged"
- "TQ,R"
- "Vv16@0:8"
- "^{_HIDAnalyticsHistogramSegment=C^{_HIDAnalyticsHistogramBucket}}"
- "^{_NSZone=}16@0:8"
- "_desc"
- "_events"
- "_field"
- "_fieldName"
- "_fields"
- "_isLogged"
- "_isUpdated"
- "_lock"
- "_name"
- "_queue"
- "_segmentCount"
- "_segments"
- "_timer"
- "activate"
- "addField:"
- "addHistogramFieldWithSegments:segments:count:"
- "addObject:"
- "autorelease"
- "cancel"
- "class"
- "conformsToProtocol:"
- "containsObject:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createBucketData:fieldvalue:fieldDescription:"
- "createBuckets:count:"
- "dataWithJSONObject:options:error:"
- "dealloc"
- "debugDescription"
- "desc"
- "description"
- "dictionaryWithObjects:forKeys:count:"
- "dispatchAnalyticsForEvent:"
- "enumerateKeysAndObjectsUsingBlock:"
- "enumerateObjectsUsingBlock:"
- "fieldName"
- "hash"
- "init"
- "initWithAttributes:description:"
- "initWithAttributes:segments:count:"
- "initWithData:encoding:"
- "initWithName:"
- "initWithSet:"
- "integerValue"
- "isEqual:"
- "isKindOfClass:"
- "isLogged"
- "isMemberOfClass:"
- "isProxy"
- "logAnalyticsEvent:"
- "logAnalyticsEvent:eventDescription:eventValue:"
- "name"
- "numberWithUnsignedChar:"
- "numberWithUnsignedInteger:"
- "numberWithUnsignedLongLong:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "registerEvent:"
- "release"
- "removeAllObjects"
- "removeObject:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "setDesc:"
- "setIntegerValue:"
- "setIntegerValue:forField:"
- "setIsLogged:"
- "setName:"
- "setObject:forKeyedSubscript:"
- "setStringValue:"
- "setStringValue:forField:"
- "setValue:"
- "start"
- "stop"
- "stringValue"
- "stringWithFormat:"
- "stringWithString:"
- "superclass"
- "unregisterEvent:"
- "unsignedIntValue"
- "unsignedIntegerValue"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@16"
- "v24@0:8Q16"
- "v32@0:8@16@24"
- "v32@0:8Q16@24"
- "v32@0:8^{_HIDAnalyticsHistogramSegmentConfig=CCCQ}16q24"
- "v40@0:8@16@24@32"
- "v40@0:8@16^{_HIDAnalyticsHistogramSegmentConfig=CCCQ}24q32"
- "value"
- "zone"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"

```
