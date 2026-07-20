## usbsmartcardreaderd

> `/System/Library/CryptoTokenKit/usbsmartcardreaderd.slotd/Contents/MacOS/usbsmartcardreaderd`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_doubleobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`

```diff

-878.0.8.0.0
-  __TEXT.__text: 0x19580
-  __TEXT.__auth_stubs: 0x4e0
-  __TEXT.__objc_stubs: 0x3400
-  __TEXT.__objc_methlist: 0x17a4
-  __TEXT.__const: 0x2c0
-  __TEXT.__objc_classname: 0x20a
-  __TEXT.__objc_methtype: 0x8f0
-  __TEXT.__objc_methname: 0x25c5
-  __TEXT.__oslogstring: 0x1cd6
-  __TEXT.__cstring: 0x1692
-  __TEXT.__gcc_except_tab: 0x260
-  __TEXT.__unwind_info: 0x670
-  __DATA_CONST.__const: 0x858
-  __DATA_CONST.__cfstring: 0x22c0
-  __DATA_CONST.__objc_classlist: 0xe8
+878.0.9.0.0
+  __TEXT.__text: 0x19fd0
+  __TEXT.__auth_stubs: 0x500
+  __TEXT.__objc_stubs: 0x3960
+  __TEXT.__objc_methlist: 0x1afc
+  __TEXT.__const: 0x2b8
+  __TEXT.__objc_classname: 0x30a
+  __TEXT.__objc_methtype: 0xb52
+  __TEXT.__objc_methname: 0x2c5d
+  __TEXT.__oslogstring: 0x1caf
+  __TEXT.__cstring: 0x17a1
+  __TEXT.__gcc_except_tab: 0x2d4
+  __TEXT.__unwind_info: 0x6c0
+  __DATA_CONST.__const: 0x8f8
+  __DATA_CONST.__cfstring: 0x2320
+  __DATA_CONST.__objc_classlist: 0x130
   __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x28
+  __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0xc0
+  __DATA_CONST.__objc_superrefs: 0xd0
   __DATA_CONST.__objc_intobj: 0x408
   __DATA_CONST.__objc_doubleobj: 0x30
   __DATA_CONST.__objc_arraydata: 0xe0
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x120
-  __DATA_CONST.__auth_got: 0x280
-  __DATA_CONST.__got: 0x170
-  __DATA.__objc_const: 0x27c8
-  __DATA.__objc_selrefs: 0xea8
-  __DATA.__objc_ivar: 0xe4
-  __DATA.__objc_data: 0x910
-  __DATA.__data: 0x1f0
-  __DATA.__bss: 0xf0
+  __DATA_CONST.__auth_got: 0x290
+  __DATA_CONST.__got: 0x188
+  __DATA.__objc_const: 0x3410
+  __DATA.__objc_selrefs: 0x1000
+  __DATA.__objc_ivar: 0x144
+  __DATA.__objc_data: 0xbe0
+  __DATA.__data: 0x370
+  __DATA.__bss: 0x120
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CryptoTokenKit.framework/Versions/A/CryptoTokenKit
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 720
-  Symbols:   126
-  CStrings:  1206
+  Functions: 780
+  Symbols:   130
+  CStrings:  1332
 
Symbols:
+ _NSLocalizedDescriptionKey
+ ___kCFBooleanFalse
+ _objc_opt_respondsToSelector
+ _objc_retainAutoreleasedReturnValue
+ _objc_setProperty_nonatomic_copy
- _memcpy
CStrings:
+ "!"
+ "1"
+ "@\"<CCIDBulkPipe>\""
+ "@\"<CCIDBulkPipe>\"16@0:8"
+ "@\"<CCIDControlEndpoint>\""
+ "@\"<CCIDControlEndpoint>\"16@0:8"
+ "@\"<CCIDInterface>\""
+ "@\"<CCIDSequenceSource>\""
+ "@\"<CCIDSlotTransmitting>\""
+ "@\"<Transmitter>\""
+ "@\"CCIDDescriptorView\"16@0:8"
+ "@\"CCIDMessageView\""
+ "@\"CCIDMessageView\"40@0:8@\"CCIDMessageView\"16Q24@?<v@?>32"
+ "@\"CCIDMessageView\"64@0:8@\"CCIDMessageView\"16Q24@\"NSNumber\"32@\"NSNumber\"40@\"NSNumber\"48@?<v@?>56"
+ "@\"NSArray\"20@0:8C16"
+ "@\"NSNumber\""
+ "@\"NSNumber\"16@0:8"
+ "@16@?0@?<@@?>8"
+ "@32@0:8@16Q24"
+ "@40@0:8@16@24@?32"
+ "@44@0:8@16@24C32@36"
+ "@44@0:8@16@24C32@?36"
+ "@52@0:8@16@24@32C40@44"
+ "@64@0:8@16@24@32@40@48@56"
+ "@?16@0:8"
+ "@?<v@?>16@0:8"
+ "@?<v@?C>16@0:8"
+ "AB"
+ "ABORT drain deadline (%.1fs) expired without a matching SlotStatus terminator (seq=%u)"
+ "ABORT drain saw a frame for slot %u while aborting slot %u"
+ "B32@0:8C16C20^@24"
+ "B64@0:8@16@24@32C40C44Q48^@56"
+ "C44@0:8@16C24@28@36"
+ "CCIDAbortSequence"
+ "CCIDControlEndpoint"
+ "CCIDInterface"
+ "CCIDInterruptParser"
+ "CCIDOutboundFrame"
+ "CCIDParametersCodec"
+ "CCIDReceiveLoop"
+ "CCIDReceiveOutcome"
+ "CCIDReceiveParameters"
+ "CCIDSequenceSource"
+ "CCIDSlotControlEndpoint"
+ "CCIDSlotInterface"
+ "CCIDSlotTransmitter"
+ "CCIDSlotTransmitting"
+ "Communication error"
+ "Failed to decode APDU: %{private}@"
+ "Maximum response length exceeded (%lu)!"
+ "Received message with wrong slot number: %@"
+ "Received message with wrong slot sequence number: %@"
+ "T@\"<CCIDBulkPipe>\",R"
+ "T@\"<CCIDControlEndpoint>\",R"
+ "T@\"<CCIDInterface>\",R,V_interface"
+ "T@\"CCIDMessageView\",&,N,V_message"
+ "T@\"NSNumber\",&,N,V_timeout"
+ "T@\"NSString\",R,N"
+ "T@?,C,N"
+ "T@?,C,N,V_analyticsFailureHandler"
+ "T@?,C,N,V_timeExtensionHandler"
+ "TB,N,V_timeExtensionRequested"
+ "TC,N,V_duplicateMessage"
+ "TC,N,V_sequence"
+ "TC,N,V_slot"
+ "TQ,N,V_maxPayload"
+ "TQ,N,V_receiveSize"
+ "Td,N,V_elapsed"
+ "Td,N,V_maxWaitingTime"
+ "Td,N,V_maxWaitingTimeWithExtensions"
+ "The reader vid:%{public}@ pid:%{public}@ does not support suggested protocol"
+ "Tq,N,V_kind"
+ "_analyticsFailureHandler"
+ "_bulkInPipe"
+ "_bulkOutPipe"
+ "_controlEndpoint"
+ "_duplicateMessage"
+ "_elapsed"
+ "_kind"
+ "_maxWaitingTime"
+ "_maxWaitingTimeWithExtensions"
+ "_message"
+ "_productId"
+ "_receiveSize"
+ "_sequenceNumber"
+ "_sequenceSource"
+ "_serialize"
+ "_slot"
+ "_terminated"
+ "_timeExtensionHandler"
+ "_timeExtensionRequested"
+ "_timeout"
+ "_vendorId"
+ "abortSequence: drain saw short/partial reply (%lu bytes); discarding"
+ "abortSequence: slot %d did not complete cleanly: %{public}@"
+ "analyticsFailureHandler"
+ "bulkInPipe"
+ "bulkOutPipe"
+ "clockFrequencies:"
+ "com.apple.CryptoTokenKit.ccid.abort"
+ "controlEndpoint"
+ "copy"
+ "d"
+ "d16@0:8"
+ "dataRates:"
+ "dictionary"
+ "duplicateMessage"
+ "elapsed"
+ "enumerateKeysAndObjectsUsingBlock:"
+ "errorMessage"
+ "incrementSequenceNumber"
+ "initWithInterface:"
+ "initWithInterface:sequenceSource:slot:serialize:"
+ "initWithInterface:slotName:slotNumber:engine:"
+ "initWithInterface:transmitter:slotName:slotNumber:engine:"
+ "initWithProductId:vendorId:CCIDDescriptor:bulkInPipe:bulkOutPipe:controlEndpoint:"
+ "kind"
+ "maxWaitingTime"
+ "maxWaitingTimeWithExtensions"
+ "message"
+ "numberWithUnsignedInteger:"
+ "protocolDataFromPayload:"
+ "q"
+ "rateQuery:count:"
+ "receiveFromPipe:parameters:onTimeExtension:"
+ "receiveSize"
+ "reportFailure:"
+ "runWithControlEndpoint:pipeOut:pipeIn:slot:sequence:maxMessageLength:error:"
+ "sendAbortRequestForSlot:sequence:error:"
+ "sendAnalyticsFailureType:"
+ "sequenceNumber"
+ "setAnalyticsFailureHandler:"
+ "setDuplicateMessage:"
+ "setElapsed:"
+ "setKind:"
+ "setMaxPayload:"
+ "setMaxWaitingTime:"
+ "setMaxWaitingTimeWithExtensions:"
+ "setMessage:"
+ "setParametersRequest:"
+ "setReceiveSize:"
+ "setSequence:"
+ "setSlot:"
+ "setTimeExtensionHandler:"
+ "setTimeExtensionRequested:"
+ "setTimeout:"
+ "slot"
+ "slotNotificationsFromBuffer:slotCount:"
+ "stampMessage:slot:sequence:sequenceSource:"
+ "timeExtensionHandler"
+ "timeExtensionRequested"
+ "timeout"
+ "unsignedIntegerValue"
+ "v12@?0C8"
+ "v24@0:8@?<v@?>16"
+ "v24@0:8@?<v@?C>16"
+ "v24@0:8Q16"
+ "v24@0:8d16"
+ "v24@0:8q16"
+ "v32@?0@\"NSNumber\"8@\"NSNumber\"16^B24"
- "@\"Device\""
- "@\"IOUSBHostPipe\""
- "@\"NSObject<Transmitter>\""
- "@32@0:8@16C24C28"
- "@36@0:8@16@24C32"
- "@48@0:8C16C20C24C28@32@40"
- "@52@0:8@16@24C32@36@44"
- "APDUResponse"
- "APDUWithCLA:INS:P1:P2:dataField:Le:"
- "Commnication error"
- "Failed to decode APDU: %{public}@"
- "Invalid length: %lu"
- "Maximum responde length exceeded (%lu)!"
- "SW1"
- "SW2"
- "T@\"Device\",R,W,V_device"
- "The reader %{public}@ %{public}@ dose not support suggested protocol"
- "_device"
- "_messageSequenceNumber"
- "_pipeIn"
- "_pipeOut"
- "abort:"
- "abortSequence: drain receive returned 0 bytes (timeout); checking deadline"
- "abortSequence: drain saw short/partial reply (%lu bytes, below CCID header); discarding and continuing"
- "dataField length should be between 1 and 65535"
- "device"
- "initWithDevice:slotName:slotNumber:"
- "initWithDevice:slotName:slotNumber:pipeIn:pipeOut:"
- "le should be between 0 and 65536"
- "messageSequenceNumber"
- "mutableBytes"
- "responseWithData:"
- "responseWithDataField:SW1:SW2:"
- "{ SW1: 0x%.2x SW2: 0x%.2x dataLen: %lu }"
```
