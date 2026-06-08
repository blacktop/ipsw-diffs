## AGXGPURawCounterBundle

> `/System/Library/Extensions/AGXGPURawCounterBundle.bundle/AGXGPURawCounterBundle`

```diff

-351.1.0.0.0
-  __TEXT.__text: 0x226c
-  __TEXT.__auth_stubs: 0x140
+360.27.0.0.0
+  __TEXT.__text: 0x2df0
   __TEXT.__objc_methlist: 0x1d0
   __TEXT.__const: 0x8
-  __TEXT.__cstring: 0x363
+  __TEXT.__gcc_except_tab: 0x54
+  __TEXT.__cstring: 0x3ac
   __TEXT.__oslogstring: 0x4d
-  __TEXT.__unwind_info: 0xa8
-  __TEXT.__objc_classname: 0x49
-  __TEXT.__objc_methname: 0x717
-  __TEXT.__objc_methtype: 0x190
-  __TEXT.__objc_stubs: 0x5c0
-  __DATA_CONST.__got: 0x90
+  __TEXT.__unwind_info: 0xc8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x60
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x218
+  __DATA_CONST.__objc_selrefs: 0x258
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0xa8
-  __AUTH_CONST.__cfstring: 0x460
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__cfstring: 0x4c0
   __AUTH_CONST.__objc_const: 0x340
+  __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_dictobj: 0x50
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x28
   __DATA.__bss: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E58CF1E1-BA40-3D67-A55C-E9DC843CB6B9
-  Functions: 36
-  Symbols:   198
-  CStrings:  183
+  UUID: 43CED09A-9756-3E2E-8B2E-8B2A67DB7C62
+  Functions: 38
+  Symbols:   222
+  CStrings:  82
 
Symbols:
+ GCC_except_table18
+ _OBJC_CLASS_$_GPURawCounterSelect
+ _OBJC_CLASS_$_NSArray
+ __Unwind_Resume
+ __ZNSt3__16vectorIPKcNS_9allocatorIS2_EEE20__throw_length_errorB9fqn220100Ev
+ __ZNSt3__16vectorIPKcNS_9allocatorIS2_EEE24__emplace_back_slow_pathIJS2_EEEPS2_DpOT_
+ __ZSt28__throw_bad_array_new_lengthB9fqn220100v
+ __ZdlPv
+ __ZnwmSt19__type_descriptor_t
+ ___gxx_personality_v0
+ _abort
+ _memcpy
+ _objc_msgSend$containsObject:
+ _objc_msgSend$dictionaryWithCapacity:
+ _objc_msgSend$indexOfObjectIdenticalTo:
+ _objc_msgSend$initWithArray:copyItems:
+ _objc_msgSend$initWithName:description:valueType:subEventList:
+ _objc_msgSend$mutableCopy
+ _objc_msgSend$selectWithName:options:
+ _objc_msgSend$subarrayWithRange:
+ _objc_release_x20
CStrings:
+ "EventSelect"
+ "SupportOption_DisablePowerOff"
+ "SupportOption_RDEReadThreshold"
- "@\"NSArray\""
- "@\"NSMutableArray\""
- "@\"NSMutableData\""
- "@16@0:8"
- "@20@0:8I16"
- "@32@0:8@16@24"
- "@32@0:8@16^{Source=^^?}24"
- "AGXGPURawCounterSource"
- "AGXGPURawCounterSourceGroup"
- "B16@0:8"
- "B20@0:8B16"
- "B24@0:8@16"
- "B28@0:8I16@?20"
- "B32@0:8@16^Q24"
- "B52@0:8I16^*20^I28^I36^I44"
- "B68@0:8*16Q24^Q32*40Q48^Q56B64"
- "B84@0:8*16Q24^Q32Q40*48Q56Q64^Q72B80"
- "B88@0:8I16*20Q28^Q36Q44*52Q60Q68^Q76B84"
- "I"
- "I16@0:8"
- "I24@0:8I16I20"
- "PollPostProcessBuffer"
- "Q16@0:8"
- "T@\"NSMutableData\",R,V_dstBuffer"
- "TI,V_srcBufferPrevOffset"
- "TI,V_srcBufferPrevSize"
- "UTF8String"
- "^{AGXGPURawCounter=^^?}"
- "^{Source=^^?}"
- "_counterList"
- "_dstBuffer"
- "_impl"
- "_pollPostProcessBufferList"
- "_selectedCounterList"
- "_selectedTriggerList"
- "_srcBufferPrevOffset"
- "_srcBufferPrevSize"
- "_triggerList"
- "addObject:"
- "addObjectsFromArray:"
- "array"
- "arrayWithArray:"
- "arrayWithCapacity:"
- "availableCounters"
- "availableTriggers"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "dealloc"
- "dictionary"
- "drainRingBufferAtIndex:dataSize:"
- "dstBuffer"
- "flushRingBuffers"
- "hasPrefix:"
- "init"
- "initWithAcceleratorPort:"
- "initWithCapacity:"
- "initWithLength:"
- "initWithName:description:options:"
- "initWithName:description:valueType:"
- "initWithObjectsAndKeys:"
- "initWithSourceGroup:impl:"
- "initWithSourceGroup:name:"
- "isEnabled"
- "isEqualToString:"
- "length"
- "mutableBytes"
- "name"
- "numberWithUnsignedInt:"
- "numberWithUnsignedInteger:"
- "objectAtIndexedSubscript:"
- "objectForKeyedSubscript:"
- "options"
- "pollCountersAtBufferIndex:withBlock:"
- "postProcessRawDataWithRingBufferIndex:source:sourceSize:sourceRead:sourceWrite:output:outputSize:outputRead:outputWrite:isLast:"
- "postProcessRawDataWithRingBufferSource:sourceSize:sourceRead:sourceWrite:output:outputSize:outputRead:outputWrite:isLast:"
- "postProcessRawDataWithSource:sourceSize:sourceRead:output:outputSize:outputWritten:isLast:"
- "removeAllObjects"
- "requestCounter:"
- "requestCounters:firstErrorIndex:"
- "requestTriggers:firstErrorIndex:"
- "reset"
- "resetRawDataPostProcessor"
- "ringBufferInfoAtIndex:base:size:dataOffset:dataSize:"
- "ringBufferNum"
- "sampleMarker"
- "selectedCounters"
- "selectedTriggers"
- "setEnabled:"
- "setObject:atIndexedSubscript:"
- "setObject:forKeyedSubscript:"
- "setOptions:"
- "setSrcBufferPrevOffset:"
- "setSrcBufferPrevSize:"
- "srcBufferPrevOffset"
- "srcBufferPrevSize"
- "startSampling"
- "stopSampling"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "subDivideCounterList:withOptions:"
- "unsignedIntValue"
- "unsignedLongLongValue"
- "unsignedLongValue"
- "v16@0:8"
- "v20@0:8I16"
- "v24@0:8@16"

```
