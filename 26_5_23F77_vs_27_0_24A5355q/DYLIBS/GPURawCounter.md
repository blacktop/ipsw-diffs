## GPURawCounter

> `/System/Library/PrivateFrameworks/GPURawCounter.framework/GPURawCounter`

```diff

-34.0.0.0.0
-  __TEXT.__text: 0x10ac
-  __TEXT.__auth_stubs: 0x1e0
-  __TEXT.__objc_methlist: 0x714
+35.0.0.0.0
+  __TEXT.__text: 0x1168
+  __TEXT.__objc_methlist: 0x734
   __TEXT.__const: 0x8
-  __TEXT.__cstring: 0x1ae
-  __TEXT.__unwind_info: 0x118
-  __TEXT.__objc_classname: 0xef
-  __TEXT.__objc_methname: 0xac2
-  __TEXT.__objc_methtype: 0x3f3
-  __TEXT.__objc_stubs: 0x360
-  __DATA_CONST.__got: 0x68
+  __TEXT.__cstring: 0x1af
+  __TEXT.__unwind_info: 0x120
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x40
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x288
+  __DATA_CONST.__objc_selrefs: 0x2a0
   __DATA_CONST.__objc_superrefs: 0x30
-  __AUTH_CONST.__auth_got: 0xf8
+  __DATA_CONST.__got: 0x68
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0x180
-  __AUTH_CONST.__objc_const: 0xc00
-  __DATA.__objc_ivar: 0x4c
+  __AUTH_CONST.__objc_const: 0xc48
+  __AUTH_CONST.__auth_got: 0x0
+  __DATA.__objc_ivar: 0x50
   __DATA.__data: 0x1e0
   __DATA.__bss: 0x18
   __DATA_DIRTY.__objc_data: 0x1e0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D2D55612-10E7-3FB5-91B4-F4206EA03790
-  Functions: 76
-  Symbols:   324
-  CStrings:  203
+  UUID: 3EEB0469-B9C8-3CE8-8A7E-ACE1636A914B
+  Functions: 78
+  Symbols:   330
+  CStrings:  30
 
Symbols:
+ -[_GPURawCounter initWithName:description:valueType:subEventList:]
+ -[_GPURawCounter subEventList]
+ OBJC_IVAR_$__GPURawCounter._subEventList
+ _objc_msgSend$initWithArray:
CStrings:
- "#16@0:8"
- "@\"<GPURawCounterSourceGroup>\""
- "@\"<GPURawCounterSourceGroup>\"16@0:8"
- "@\"NSArray\""
- "@\"NSArray\"16@0:8"
- "@\"NSDictionary\""
- "@\"NSDictionary\"16@0:8"
- "@\"NSDictionary\"32@0:8@\"NSArray\"16@\"NSDictionary\"24"
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@20@0:8I16"
- "@24@0:8:16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@40@0:8@16@24Q32"
- "B16@0:8"
- "B20@0:8B16"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8^@16"
- "B28@0:8B16^@20"
- "B28@0:8I16@?20"
- "B28@0:8I16@?<v@?^QQQ>20"
- "B32@0:8@\"NSArray\"16^Q24"
- "B32@0:8@16^Q24"
- "B36@0:8I16@?20^@28"
- "B36@0:8I16@?<v@?^QQQ>20^@28"
- "B40@0:8@\"NSArray\"16^Q24^@32"
- "B40@0:8@16^Q24^@32"
- "B52@0:8I16^*20^I28^I36^I44"
- "B60@0:8I16^*20^I28^I36^I44^@52"
- "B68@0:8*16Q24^Q32*40Q48^Q56B64"
- "B76@0:8*16Q24^Q32*40Q48^Q56B64^@68"
- "B84@0:8*16Q24^Q32Q40*48Q56Q64^Q72B80"
- "B88@0:8I16*20Q28^Q36Q44*52Q60Q68^Q76B84"
- "B92@0:8*16Q24^Q32Q40*48Q56Q64^Q72B80^@84"
- "B96@0:8I16*20Q28^Q36Q44*52Q60Q68^Q76B84^@88"
- "GPURawCounter"
- "GPURawCounterSelect"
- "GPURawCounterSource"
- "GPURawCounterSourceGroup"
- "GPURawCounterSourceTrigger"
- "GPURawCounterSourceTriggerSelect"
- "I"
- "I16@0:8"
- "I24@0:8I16I20"
- "I32@0:8I16I20^@24"
- "NSObject"
- "Q"
- "Q16@0:8"
- "T#,R"
- "T@\"<GPURawCounterSourceGroup>\",R"
- "T@\"<GPURawCounterSourceGroup>\",R,V_sourceGroup"
- "T@\"NSArray\",R"
- "T@\"NSArray\",R,V_sourceList"
- "T@\"NSDictionary\",C"
- "T@\"NSDictionary\",C,V_options"
- "T@\"NSDictionary\",R,C"
- "T@\"NSDictionary\",R,C,V_features"
- "T@\"NSDictionary\",R,C,V_options"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,V_description"
- "T@\"NSString\",R,C,V_name"
- "T@\"NSString\",R,V_name"
- "TI,R"
- "TI,R,V_acceleratorPort"
- "TQ,R"
- "TQ,R,V_counterValueType"
- "UTF8String"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_GPURawCounter"
- "_GPURawCounterSource"
- "_GPURawCounterSourceGroup"
- "_GPURawCounterSourceTrigger"
- "_acceleratorPort"
- "_counterValueType"
- "_description"
- "_features"
- "_name"
- "_options"
- "_sourceGroup"
- "_sourceList"
- "acceleratorPort"
- "addObject:"
- "autorelease"
- "availableCounters"
- "availableTriggers"
- "bundleWithPath:"
- "class"
- "classNamed:"
- "conformsToProtocol:"
- "copy"
- "counterValueType"
- "dealloc"
- "debugDescription"
- "description"
- "dictionaryWithObjects:forKeys:count:"
- "doesNotRecognizeSelector:"
- "drainRingBufferAtIndex:dataSize:"
- "drainRingBufferAtIndex:dataSize:error:"
- "errorWithDomain:code:userInfo:"
- "features"
- "flushRingBuffers"
- "hash"
- "init"
- "initWithAcceleratorPort:"
- "initWithAcceleratorPort:error:"
- "initWithName:description:options:"
- "initWithName:description:valueType:"
- "initWithName:options:"
- "initWithSourceGroup:name:"
- "isEnabled"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isSubclassOfClass:"
- "name"
- "options"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "pollCountersAtBufferIndex:withBlock:"
- "pollCountersAtBufferIndex:withBlock:error:"
- "postProcessRawDataWithRingBufferIndex:source:sourceSize:sourceRead:sourceWrite:output:outputSize:outputRead:outputWrite:isLast:"
- "postProcessRawDataWithRingBufferIndex:source:sourceSize:sourceRead:sourceWrite:output:outputSize:outputRead:outputWrite:isLast:error:"
- "postProcessRawDataWithRingBufferSource:sourceSize:sourceRead:sourceWrite:output:outputSize:outputRead:outputWrite:isLast:"
- "postProcessRawDataWithRingBufferSource:sourceSize:sourceRead:sourceWrite:output:outputSize:outputRead:outputWrite:isLast:error:"
- "postProcessRawDataWithSource:sourceSize:sourceRead:output:outputSize:outputWritten:isLast:"
- "postProcessRawDataWithSource:sourceSize:sourceRead:output:outputSize:outputWritten:isLast:error:"
- "release"
- "requestCounters:firstErrorIndex:"
- "requestCounters:firstErrorIndex:error:"
- "requestTriggers:firstErrorIndex:"
- "requestTriggers:firstErrorIndex:error:"
- "resetRawDataPostProcessor"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "ringBufferInfoAtIndex:base:size:dataOffset:dataSize:"
- "ringBufferInfoAtIndex:base:size:dataOffset:dataSize:error:"
- "ringBufferNum"
- "sampleMarker"
- "selectWithName:options:"
- "selectedCounters"
- "selectedTriggers"
- "self"
- "setEnabled:"
- "setEnabled:error:"
- "setOptions:"
- "sourceGroup"
- "sourceList"
- "startSampling"
- "startSamplingWithError:"
- "stopSampling"
- "stopSamplingWithError:"
- "stringByAppendingPathComponent:"
- "stringByAppendingString:"
- "stringWithFormat:"
- "subDivideCounterList:withOptions:"
- "superclass"
- "v16@0:8"
- "v24@0:8@\"NSDictionary\"16"
- "v24@0:8@16"
- "zone"

```
