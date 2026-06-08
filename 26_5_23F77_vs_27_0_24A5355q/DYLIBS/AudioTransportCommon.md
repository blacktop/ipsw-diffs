## AudioTransportCommon

> `/System/Library/PrivateFrameworks/AudioTransportCommon.framework/AudioTransportCommon`

```diff

-440.2.0.0.0
-  __TEXT.__text: 0x2930
-  __TEXT.__auth_stubs: 0x250
+500.2.0.0.0
+  __TEXT.__text: 0x2740
   __TEXT.__objc_methlist: 0x30c
   __TEXT.__const: 0xb0
-  __TEXT.__cstring: 0x39c
+  __TEXT.__cstring: 0x3a2
   __TEXT.__oslogstring: 0x8d
   __TEXT.__unwind_info: 0xf8
-  __TEXT.__objc_classname: 0x40
-  __TEXT.__objc_methname: 0x9c0
-  __TEXT.__objc_methtype: 0x24a
-  __TEXT.__objc_stubs: 0x700
-  __DATA_CONST.__got: 0x60
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x50
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x8

   __DATA_CONST.__objc_selrefs: 0x2a0
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_arraydata: 0x30
-  __AUTH_CONST.__auth_got: 0x130
+  __DATA_CONST.__got: 0x60
   __AUTH_CONST.__cfstring: 0x360
   __AUTH_CONST.__objc_const: 0x6e0
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x18
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x6c
   __DATA.__data: 0x60

   - /System/Library/PrivateFrameworks/IOKitten.framework/IOKitten
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 90716A8A-988C-37F8-BA12-C65FAEDA5B2B
-  Functions: 79
-  Symbols:   325
-  CStrings:  237
+  UUID: E39DB506-B455-3B48-AC4A-76183259B051
+  Functions: 76
+  Symbols:   322
+  CStrings:  70
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x2
+ _objc_retain_x22
+ _objc_retain_x25
+ _objc_retain_x26
- _OUTLINED_FUNCTION_4
- _OUTLINED_FUNCTION_5
- _OUTLINED_FUNCTION_6
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x20
CStrings:
- ".cxx_destruct"
- "@\"ATCIOA2StreamFormat\""
- "@\"IOKConnection\""
- "@\"IOKNotificationPort\""
- "@\"IOKService\""
- "@\"NSArray\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_dispatch_source>\""
- "@\"NSString\""
- "@16@0:8"
- "@24@0:8@16"
- "@24@0:8^{AudioStreamBasicDescription=dIIIIIIII}16"
- "@24@0:8^{_NSZone=}16"
- "@36@0:8d16I24I28B32"
- "@52@0:8@16@24Q32B40@44"
- "ATCIOA2Device"
- "ATCIOA2Stream"
- "ATCIOA2StreamFormat"
- "B"
- "B16@0:8"
- "B24@0:8@16"
- "B24@0:8^@16"
- "B32@0:8^{IOAudio2Notification=IIIIQQ}16^@24"
- "B32@0:8d16^@24"
- "I"
- "I16@0:8"
- "I20@0:8I16"
- "NSCopying"
- "Q"
- "Q16@0:8"
- "T@\"ATCIOA2StreamFormat\",R,C,N,V_currentFormat"
- "T@\"NSArray\",C,N,V_availableSampleRates"
- "T@\"NSArray\",C,N,V_inputStreams"
- "T@\"NSArray\",C,N,V_outputStreams"
- "T@\"NSArray\",R,C,N,V_availableFormats"
- "T@\"NSString\",R,C,N,V_name"
- "T@\"NSString\",R,C,N,V_uid"
- "TB,R,N,GisInput,V_input"
- "TI,N,V_bitsPerChannel"
- "TI,N,V_bytesPerFrame"
- "TI,N,V_bytesPerPacket"
- "TI,N,V_channelsPerFrame"
- "TI,N,V_formatFlags"
- "TI,N,V_formatID"
- "TI,N,V_framesPerPacket"
- "TI,R,N"
- "TI,R,N,V_startingChannel"
- "Td,N,V_sampleRate"
- "Td,R,N"
- "UTF8String"
- "^{IOAudio2EngineStatus=QQQQQ}"
- "_availableFormats"
- "_availableSampleRates"
- "_bitsPerChannel"
- "_buildInputStreams"
- "_buildOutputStreams"
- "_bytesPerFrame"
- "_bytesPerPacket"
- "_channelsPerFrame"
- "_connection"
- "_currentFormat"
- "_engineStatus"
- "_formatFlags"
- "_formatID"
- "_framesPerPacket"
- "_index"
- "_input"
- "_inputStreams"
- "_name"
- "_notificationPort"
- "_notificationSource"
- "_outputStreams"
- "_physicalID"
- "_queue"
- "_sampleRate"
- "_service"
- "_startingChannel"
- "_uid"
- "addObject:"
- "addObjectsFromArray:"
- "aeaStreamFormatWithDictionary:"
- "aeaStreamFormatsWithRangedDictionary:"
- "allKeys"
- "array"
- "arrayWithArray:"
- "audioStreamBasicDescription"
- "availableFormats"
- "availableSampleRates"
- "bitsPerChannel"
- "bytesPerFrame"
- "bytesPerPacket"
- "callMethodWithSelector:scalarInputs:scalarInputCount:structInput:structInputSize:scalarOutputs:scalarOutputCount:structOutput:structOutputSize:error:"
- "changeToSampleRate:error:"
- "channelsPerFrame"
- "clockDomain"
- "connectToServiceOfType:"
- "containsObject:"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "currentFormat"
- "d"
- "d16@0:8"
- "dealloc"
- "description"
- "doubleValue"
- "firstObject"
- "formatFlags"
- "formatID"
- "framesPerPacket"
- "framesToBytes:"
- "handleNotification:"
- "hash"
- "init"
- "initOnDispatchQueue:"
- "initWithAudioStreamBasicDescription:"
- "initWithIOAudio2Dictionary:"
- "initWithSampleRate:numChannels:commonPCMFormat:isInterleaved:"
- "initWithService:"
- "initWithService:connection:index:input:description:"
- "input"
- "inputLatency"
- "inputSafetyOffset"
- "inputStreams"
- "ioBufferSize"
- "iokitMatchingDictionary"
- "isEqual:"
- "isInput"
- "longLongValue"
- "machPort"
- "mapMemory64OfType:withOptions:atAddress:ofSize:error:"
- "name"
- "numberWithDouble:"
- "objectForKeyedSubscript:"
- "outputLatency"
- "outputSafetyOffset"
- "outputStreams"
- "performConfiigChangeForNotification:error:"
- "properties"
- "propertyForKey:"
- "removeObjectsInArray:"
- "sampleRate"
- "serviceMatching:"
- "setAvailableSampleRates:"
- "setBitsPerChannel:"
- "setBytesPerFrame:"
- "setBytesPerPacket:"
- "setChannelsPerFrame:"
- "setFormatFlags:"
- "setFormatID:"
- "setFramesPerPacket:"
- "setInputStreams:"
- "setNotificationPort:ofType:withReference:error:"
- "setOutputStreams:"
- "setSampleRate:"
- "startIOError:"
- "startingChannel"
- "stopIOError:"
- "stringWithFormat:"
- "uid"
- "unsignedIntValue"
- "v16@0:8"
- "v20@0:8I16"
- "v24@0:8@16"
- "v24@0:8^{IOAudio2Notification=IIIIQQ}16"
- "v24@0:8d16"
- "{AudioStreamBasicDescription=dIIIIIIII}16@0:8"

```
