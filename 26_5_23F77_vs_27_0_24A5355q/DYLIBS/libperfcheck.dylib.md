## libperfcheck.dylib

> `/usr/lib/libperfcheck.dylib`

```diff

 46.0.0.0.0
-  __TEXT.__text: 0xa32c
-  __TEXT.__auth_stubs: 0x830
+  __TEXT.__text: 0xa2ec
   __TEXT.__const: 0x90
   __TEXT.__cstring: 0x1091
-  __TEXT.__gcc_except_tab: 0x7c
-  __TEXT.__unwind_info: 0x200
-  __TEXT.__objc_classname: 0x1
-  __TEXT.__objc_methname: 0x4ac
-  __TEXT.__objc_stubs: 0x7a0
-  __DATA_CONST.__got: 0xd0
+  __TEXT.__gcc_except_tab: 0x80
+  __TEXT.__unwind_info: 0x208
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_methname: 0x0
   __DATA_CONST.__const: 0x198
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1f0
   __DATA_CONST.__objc_arraydata: 0x28
-  __AUTH_CONST.__auth_got: 0x428
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x520
   __AUTH_CONST.__objc_arrayobj: 0x18
+  __AUTH_CONST.__auth_got: 0x440
   __DATA.__data: 0x2c0
   __DATA.__bss: 0x18
   __DATA_DIRTY.__data: 0x8

   - /System/Library/PrivateFrameworks/perfdata.framework/perfdata
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AA2019A0-6B99-3CA1-8C4F-C4E580010AF6
+  UUID: 710C2E6B-AA68-311D-805C-A2AFCB2DA53D
   Functions: 132
-  Symbols:   419
-  CStrings:  295
+  Symbols:   422
+  CStrings:  233
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x8
+ _objc_retain_x9
+ _objc_storeStrong
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x10
- _objc_retain_x26
CStrings:
- "JSONObjectWithData:options:error:"
- "UTF8String"
- "addObject:"
- "allKeys"
- "allObjects"
- "appendFormat:"
- "appendString:"
- "arrayByAddingObjectsFromArray:"
- "arrayWithCapacity:"
- "boolValue"
- "code"
- "compare:"
- "compare:options:range:"
- "componentsJoinedByString:"
- "componentsSeparatedByString:"
- "containerWithJSONDictionary:error:"
- "containsObject:"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "countForObject:"
- "dataWithBytesNoCopy:length:freeWhenDone:"
- "dataWithContentsOfFile:options:error:"
- "dataWithPropertyList:format:options:error:"
- "description"
- "dictionary"
- "dictionaryWithCapacity:"
- "doubleValue"
- "enumerateKeysAndObjectsUsingBlock:"
- "enumerateMeasurementsWithError:usingBlock:"
- "getBytes:length:"
- "hasPrefix:"
- "intersectSet:"
- "isComparableTo:"
- "isComparableTo:ignoringVariables:"
- "isEqualToString:"
- "largerBetter"
- "length"
- "localizedStandardCompare:"
- "mean"
- "metric"
- "metricFilterIgnoringVariables:"
- "name"
- "numberWithBool:"
- "numberWithDouble:"
- "objectAtIndexedSubscript:"
- "objectForKeyedSubscript:"
- "propertyListWithData:options:format:error:"
- "removeObject:"
- "setByAddingObjectsFromArray:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setWithArray:"
- "sortedArrayUsingSelector:"
- "string"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "testDescription"
- "unionSet:"
- "unitString"
- "value"
- "variables"

```
