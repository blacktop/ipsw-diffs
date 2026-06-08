## ContactsMetrics

> `/System/Library/PrivateFrameworks/ContactsMetrics.framework/ContactsMetrics`

```diff

-21.500.21.0.0
-  __TEXT.__text: 0x11ac
-  __TEXT.__auth_stubs: 0x220
+28.100.2.0.0
+  __TEXT.__text: 0x10dc
   __TEXT.__objc_methlist: 0x3a4
-  __TEXT.__cstring: 0x9c7
+  __TEXT.__cstring: 0x9cb
   __TEXT.__const: 0x10
   __TEXT.__gcc_except_tab: 0x34
   __TEXT.__oslogstring: 0x20
-  __TEXT.__unwind_info: 0xf8
-  __TEXT.__objc_classname: 0xac
-  __TEXT.__objc_methname: 0x63b
-  __TEXT.__objc_methtype: 0x1eb
-  __TEXT.__objc_stubs: 0x3a0
-  __DATA_CONST.__got: 0x70
+  __TEXT.__unwind_info: 0xf0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x3d8
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_catlist: 0x10

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x228
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x120
+  __DATA_CONST.__got: 0x70
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0xea0
   __AUTH_CONST.__objc_const: 0x710
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x10
   __DATA.__data: 0x1e0
   __DATA_DIRTY.__objc_data: 0x190

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BE7A9F5D-DCD5-3002-B882-DDC50F48376E
+  UUID: 2DC6B232-E464-3263-99A4-D30C959E4A17
   Functions: 43
-  Symbols:   363
-  CStrings:  365
+  Symbols:   366
+  CStrings:  238
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x3
- _objc_retainAutoreleasedReturnValue
Functions:
~ -[CNMetricsUIReporter logSearchResultsFetchedforApplication:fromSuggestions:] : 300 -> 292
~ -[CNMetricsUIReporter logSearchResultsSelectedforApplication:fromSuggestions:] : 300 -> 292
~ -[CNMetricsUIReporter logUnknownContactGeminiViewDifferentChannelSelected:] : 252 -> 244
~ +[CNMetricsReporter log] : 84 -> 68
~ +[CNMetricsReporter sendDictionary:forEvent:andLog:] : 124 -> 128
~ -[CNMetricsReporter sendDictionary:forEvent:andLog:] : 360 -> 316
~ ___52-[CNMetricsReporter sendDictionary:forEvent:andLog:]_block_invoke : 56 -> 8
~ -[CNMetricsReporter compoundKeyForEvent:] : 116 -> 108
~ +[CNMetricsReporter logDatabaseResolution:] : 220 -> 216
~ -[CNMetricsReporterSpiedEntry initWithDictionary:event:logged:] : 168 -> 172
~ -[CNMetricsReporterSpiedEntry description] : 184 -> 176
~ -[CNMetricsReporterSpiedEntry copyWithZone:] : 40 -> 4
~ -[CNMetricsReporterSpiedEntry initWithCoder:] : 268 -> 256
~ -[CNMetricsReporterSpiedEntry encodeWithCoder:] : 136 -> 128
~ -[CNMetricsReporterSpy events] : 108 -> 104
~ -[CNMetricsReporterSpy clearEvents] : 112 -> 108
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"NSMutableArray\""
- "@\"NSMutableDictionary\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8^{_NSZone=}16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@36@0:8@16@24B32"
- "@40@0:8:16@24@32"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "CNMetricsReporter"
- "CNMetricsReporterSpiedEntry"
- "CNMetricsReporterSpy"
- "CNMetricsReporterStub"
- "CNMetricsUIReporter"
- "ContactsMetrics"
- "NSCoding"
- "NSCopying"
- "NSObject"
- "NSSecureCoding"
- "Q16@0:8"
- "T#,R"
- "T@\"<CNMetricsReporter>\",&,D"
- "T@\"<CNMetricsReporter>\",R"
- "T@\"NSArray\",R"
- "T@\"NSMutableDictionary\",R,C,V_dictionary"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,V_event"
- "TB,R"
- "TB,R,GisLogged,V_logged"
- "TQ,R"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_dictionary"
- "_entries"
- "_event"
- "_logged"
- "addObject:"
- "appendName:boolValue:"
- "appendName:object:"
- "autorelease"
- "build"
- "class"
- "clearEvents"
- "compoundKeyForEvent:"
- "conformsToProtocol:"
- "copy"
- "copyWithZone:"
- "debugDescription"
- "decodeBoolForKey:"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "description"
- "descriptionBuilderWithObject:"
- "dictionaryWithObjects:forKeys:count:"
- "emptyDictionaryForAction:andApplication:"
- "encodeBool:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "eventKeyPrefix"
- "events"
- "hash"
- "init"
- "initWithCoder:"
- "initWithDictionary:"
- "initWithDictionary:event:logged:"
- "isEqual:"
- "isKindOfClass:"
- "isLogged"
- "isMemberOfClass:"
- "isProxy"
- "log"
- "logActionDictionary:"
- "logContactShownforApplication:"
- "logDatabaseResolution:"
- "logSearchActionWithDictionary:"
- "logSearchResultsFetchedforApplication:fromSuggestions:"
- "logSearchResultsSelectedforApplication:fromSuggestions:"
- "logSearchUsageforApplication:"
- "logSimpleEvent:forApplication:andLog:"
- "logUnknownContactGeminiViewDifferentChannelSelected:"
- "metricsReporter"
- "numberWithBool:"
- "objectHash:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "release"
- "removeAllObjects"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "sendDictionary:forEvent:"
- "sendDictionary:forEvent:andLog:"
- "setMetricsReporter:"
- "setValue:forKey:"
- "setWithObjects:"
- "stringByAppendingString:"
- "superclass"
- "supportsSecureCoding"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@16"
- "v28@0:8@16B24"
- "v32@0:8@16@24"
- "v36@0:8@\"NSMutableDictionary\"16@\"NSString\"24B32"
- "v36@0:8@\"NSString\"16@\"NSString\"24B32"
- "v36@0:8@16@24B32"
- "valueForKey:onCacheMiss:"
- "zone"

```
