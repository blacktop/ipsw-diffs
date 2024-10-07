## InputAnalytics

> `/System/Library/PrivateFrameworks/InputAnalytics.framework/InputAnalytics`

```diff

-64.108.0.0.0
-  __TEXT.__text: 0x1bf58
-  __TEXT.__auth_stubs: 0x7f0
-  __TEXT.__objc_methlist: 0x2228
-  __TEXT.__const: 0x202
-  __TEXT.__gcc_except_tab: 0x68c
-  __TEXT.__oslogstring: 0x25f0
-  __TEXT.__cstring: 0x4202
+64.110.0.0.0
+  __TEXT.__text: 0x1dd18
+  __TEXT.__auth_stubs: 0x830
+  __TEXT.__objc_methlist: 0x22f0
+  __TEXT.__const: 0x282
+  __TEXT.__gcc_except_tab: 0x6a8
+  __TEXT.__oslogstring: 0x28b0
+  __TEXT.__cstring: 0x4282
   __TEXT.__ustring: 0x4
-  __TEXT.__swift5_typeref: 0x82
+  __TEXT.__swift5_typeref: 0x8a
   __TEXT.__swift5_capture: 0x88
   __TEXT.__constg_swiftt: 0x4c
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x870
-  __TEXT.__eh_frame: 0x2f8
+  __TEXT.__unwind_info: 0x8a8
+  __TEXT.__eh_frame: 0x2e8
   __TEXT.__objc_classname: 0x6fe
-  __TEXT.__objc_methname: 0x4af4
-  __TEXT.__objc_methtype: 0x9c8
-  __TEXT.__objc_stubs: 0x2ec0
-  __DATA_CONST.__got: 0x230
-  __DATA_CONST.__const: 0x1060
+  __TEXT.__objc_methname: 0x4c45
+  __TEXT.__objc_methtype: 0x9c1
+  __TEXT.__objc_stubs: 0x2fc0
+  __DATA_CONST.__got: 0x248
+  __DATA_CONST.__const: 0x1030
   __DATA_CONST.__objc_classlist: 0x1b8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1070
+  __DATA_CONST.__objc_selrefs: 0x10d0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x120
   __DATA_CONST.__objc_arraydata: 0xdb0
-  __AUTH_CONST.__auth_got: 0x408
-  __AUTH_CONST.__auth_ptr: 0x20
+  __AUTH_CONST.__auth_got: 0x428
+  __AUTH_CONST.__auth_ptr: 0x28
   __AUTH_CONST.__const: 0x478
-  __AUTH_CONST.__cfstring: 0x5e60
-  __AUTH_CONST.__objc_const: 0x4710
-  __AUTH_CONST.__objc_intobj: 0x30
+  __AUTH_CONST.__cfstring: 0x5f80
+  __AUTH_CONST.__objc_const: 0x4798
+  __AUTH_CONST.__objc_intobj: 0x2e8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x7f0
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x23c
-  __DATA.__data: 0x368
+  __DATA.__objc_ivar: 0x244
+  __DATA.__data: 0x370
   __DATA.__common: 0x8
   __DATA.__bss: 0xe8
   __DATA_DIRTY.__objc_data: 0x960

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 920
-  Symbols:   506
-  CStrings:  1967
+  Functions: 944
+  Symbols:   538
+  CStrings:  2002
 
Symbols:
+ _IADataStoreDaterangeDaysInMonth
+ _IADataStoreDaterangeDaysInWeek
+ _IADataStoreDaterangeMonthEnd
+ _IADataStoreDaterangeMonthStart
+ _IADataStoreDaterangeToday
+ _IADataStoreDaterangeWeek1End
+ _IADataStoreDaterangeWeek1Start
+ _IADataStoreDaterangeWeek2End
+ _IADataStoreDaterangeWeek2Start
+ _IADataStoreDaterangeWeek3End
+ _IADataStoreDaterangeWeek3Start
+ _IADataStoreDaterangeWeek4End
+ _IADataStoreDaterangeWeek4Start
+ _IADataStoreDaterangeYesterday
+ _IADataStoreObjectTypeBoolean
+ _IADataStoreObjectTypeCounter
+ _IADataStoreObjectTypeDaterange
+ _IAPayloadKeySmartRepliesGeneratedContent
+ _IAPayloadKeySmartRepliesOriginalContent
+ _IAPayloadKeySmartRepliesRejectedAll
+ _IAPayloadKeySmartRepliesResultIndices
+ _OBJC_CLASS_$_IADataStoreBoolean
+ _OBJC_CLASS_$_IADataStoreCounter
+ _OBJC_CLASS_$_IADataStoreDaterange
+ _OBJC_CLASS_$_IADataStoreObject
+ _OBJC_CLASS_$_IADefaultsDataStore
+ _OBJC_METACLASS_$_IADataStoreBoolean
+ _OBJC_METACLASS_$_IADataStoreCounter
+ _OBJC_METACLASS_$_IADataStoreDaterange
+ _OBJC_METACLASS_$_IADataStoreObject
+ _OBJC_METACLASS_$_IADefaultsDataStore
+ _swift_bridgeObjectRetain_n
CStrings:
+ "@32@0:8Q16Q24"
+ "@40@0:8@16@24^@32"
+ "Daterange with name %!{(MISSING)private}@ requires endDayNumber (%!l(MISSING)u) >= startDayNumber (%!l(MISSING)u)"
+ "IADefaultsDataStore datastoreName should start with '%!{(MISSING)private}@', got '%!{(MISSING)private}@'"
+ "Missing definitions in channelBasedPayloadKeyAllowList for channel '%!{(MISSING)private}@' payloadKey '%!{(MISSING)private}@'"
+ "Missing definitions in channelBasedPayloadKeyAllowList for channel '%!{(MISSING)private}@' signal '%!{(MISSING)private}@'"
+ "Payload value '%!{(MISSING)private}@' not found in translator for channel '%!{(MISSING)private}@' payloadKey '%!{(MISSING)private}@'. Using default"
+ "Q32@0:8Q16Q24"
+ "T@\"NSDate\",R,N,V_originDate"
+ "T@\"NSDictionary\",&,N,V_signalTranslation"
+ "_appendSignalEnumTo:forSignalAnalyticsObject:"
+ "_originDate"
+ "_signalTranslation"
+ "bitmaskForDayRangeFrom:to:"
+ "bitmaskForLessThanDayN:"
+ "createDataStoreObjectWithName:withType:withError:"
+ "enumTranslation"
+ "enumTranslationDefaultValue"
+ "everUsed"
+ "featureDetailsEnum"
+ "featureEnum"
+ "getObjectWithName:withType:withError:"
+ "mail_messages.txt"
+ "originDate"
+ "periodic24HourEvents"
+ "publishEnumName"
+ "publishFieldName"
+ "setBitfield:"
+ "setOriginDate:"
+ "setSignalTranslation:"
+ "signal '%!{(MISSING)private}@' not found in translator for channel '%!{(MISSING)private}@'. Using default"
+ "signalEnum"
+ "signalTranslation"
+ "timesUsedInDayRangeFrom:to:"
+ "timesUsedInLastNDays:"
+ "uiEnum"
+ "usageFrequency"
+ "usageFrequency [%!{(MISSING)private}@] daily failed"
+ "usageFrequency [%!{(MISSING)private}@] month failed"
+ "usageFrequency [%!{(MISSING)private}@] week failed"
+ "usedInDayRangeFrom:to:"
+ "usedInLastDay"
+ "usedInLastMonth"
+ "usedInLastNDays:"
+ "usedInLastWeek"
+ "v20@0:8i16"
- "B24@0:8^B16"
- "B32@0:8^B16Q24"
- "B32@0:8^Q16Q24"
- "B48@0:8@16@24^@32^@40"
- "createDataStoreObjectWithName:withType:inVar:withError:"
- "everUsed:"
- "getObjectWithName:withType:inVar:withError:"
- "timesUsedInLastNDays:forN:"
- "usedInLastDay:"
- "usedInLastMonth:"
- "usedInLastNDays:forN:"
- "usedInLastWeek:"
- "v32@?0@\"NSString\"8@\"NSDictionary\"16^B24"

```
