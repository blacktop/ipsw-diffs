## AggregateDictionary

> `/System/Library/PrivateFrameworks/AggregateDictionary.framework/AggregateDictionary`

```diff

 443.0.0.0.0
   __TEXT.__text: 0x444
-  __TEXT.__auth_stubs: 0x60
   __TEXT.__objc_methlist: 0x34
   __TEXT.__const: 0x10
   __TEXT.__cstring: 0x6
   __TEXT.__oslogstring: 0x5a
-  __TEXT.__unwind_info: 0x88
-  __TEXT.__objc_classname: 0x1d
-  __TEXT.__objc_methname: 0x59
-  __TEXT.__objc_methtype: 0x13
-  __TEXT.__objc_stubs: 0x40
-  __DATA_CONST.__got: 0x10
+  __TEXT.__unwind_info: 0x80
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x20
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x38
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__objc_const: 0x40
+  __AUTH_CONST.__auth_got: 0x0
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5884508B-A90C-3DCA-8634-E200C78C887B
+  UUID: 14FDA3E5-460A-3D40-9F69-BD16FB4E9F98
   Functions: 22
   Symbols:   68
-  CStrings:  9
+  CStrings:  2
 
Functions:
~ _ADClientBatchKeys -> _ADClientSignificantTimeChanged.cold.1 : 44 -> 4
~ _ADClientSetValueForScalarKey -> _OUTLINED_FUNCTION_0 : 44 -> 20
~ _ADClientSignificantTimeChanged.cold.1 -> _ADClientSetValueForScalarKey : 4 -> 44
~ +[NSDate(AggregateDictionaryAdditions) daysSince1970] -> _ADClientPushValueForDistributionKey : 60 -> 44
~ +[NSDate(AggregateDictionaryAdditions) dateForDaysSince1970:] -> _ADDaysSince1970 : 28 -> 60
~ -[NSDate(AggregateDictionaryAdditions) daysSince1970] -> +[NSDate(AggregateDictionaryAdditions) dateForDaysSince1970:] : 40 -> 28
~ _ADClientIsEnabled -> -[NSDate(AggregateDictionaryAdditions) daysSince1970] : 52 -> 40
~ _ADClientSignificantTimeChanged -> _ADClientCheckpoint : 44 -> 52
~ _ADMonotonicTimeGetCurrent -> _ADClientSetValueForDistributionKey : 4 -> 44
~ _ADPushTimeIntervalForDistributionKeySinceStartTime -> _ADMonotonicTimeGetCurrent : 160 -> 4
~ _ADPushTimeIntervalForDistributionKeyTimingBlock -> _ADPushTimeIntervalForDistributionKeySinceStartTime : 76 -> 160
~ _OUTLINED_FUNCTION_0 -> _ADPushTimeIntervalForDistributionKeyTimingBlock : 20 -> 76
CStrings:
- "@20@0:8i16"
- "AggregateDictionaryAdditions"
- "dateForDaysSince1970:"
- "dateWithTimeIntervalSince1970:"
- "daysSince1970"
- "i16@0:8"
- "timeIntervalSince1970"

```
