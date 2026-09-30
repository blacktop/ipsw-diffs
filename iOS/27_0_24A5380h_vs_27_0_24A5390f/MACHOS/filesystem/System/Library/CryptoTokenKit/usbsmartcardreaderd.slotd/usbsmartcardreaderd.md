## usbsmartcardreaderd

> `/System/Library/CryptoTokenKit/usbsmartcardreaderd.slotd/usbsmartcardreaderd`

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
-  __TEXT.__text: 0x16c74
-  __TEXT.__auth_stubs: 0x650
-  __TEXT.__objc_stubs: 0x3100
-  __TEXT.__objc_methlist: 0x1734
-  __TEXT.__const: 0x2a8
-  __TEXT.__objc_classname: 0x1fc
-  __TEXT.__objc_methtype: 0x891
-  __TEXT.__objc_methname: 0x236e
-  __TEXT.__oslogstring: 0x1a90
-  __TEXT.__cstring: 0x15db
-  __TEXT.__gcc_except_tab: 0x278
-  __TEXT.__unwind_info: 0x630
-  __DATA_CONST.__const: 0x808
-  __DATA_CONST.__cfstring: 0x2140
-  __DATA_CONST.__objc_classlist: 0xe0
+878.0.9.0.0
+  __TEXT.__text: 0x176c0
+  __TEXT.__auth_stubs: 0x670
+  __TEXT.__objc_stubs: 0x3660
+  __TEXT.__objc_methlist: 0x1a94
+  __TEXT.__const: 0x2a0
+  __TEXT.__objc_classname: 0x2fc
+  __TEXT.__objc_methtype: 0xaf3
+  __TEXT.__objc_methname: 0x2a06
+  __TEXT.__oslogstring: 0x1a69
+  __TEXT.__cstring: 0x16ea
+  __TEXT.__gcc_except_tab: 0x2e8
+  __TEXT.__unwind_info: 0x680
+  __DATA_CONST.__const: 0x898
+  __DATA_CONST.__cfstring: 0x21a0
+  __DATA_CONST.__objc_classlist: 0x128
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
-  __DATA_CONST.__auth_got: 0x338
-  __DATA_CONST.__got: 0x150
-  __DATA.__objc_const: 0x2700
-  __DATA.__objc_selrefs: 0xde8
-  __DATA.__objc_ivar: 0xe4
-  __DATA.__objc_data: 0x8c0
-  __DATA.__data: 0x1f0
-  __DATA.__bss: 0xd0
+  __DATA_CONST.__auth_got: 0x348
+  __DATA_CONST.__got: 0x168
+  __DATA.__objc_const: 0x3348
+  __DATA.__objc_selrefs: 0xf40
+  __DATA.__objc_ivar: 0x144
+  __DATA.__objc_data: 0xb90
+  __DATA.__data: 0x370
+  __DATA.__bss: 0x100
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CryptoTokenKit.framework/CryptoTokenKit
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/IOUSBHost.framework/IOUSBHost
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 680
-  Symbols:   146
-  CStrings:  1155
+  Functions: 740
+  Symbols:   150
+  CStrings:  1281
 
Symbols:
+ _NSLocalizedDescriptionKey
+ ___kCFBooleanFalse
+ _objc_opt_respondsToSelector
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x25
+ _objc_setProperty_nonatomic_copy
- _memcpy
- _objc_retain_x6
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
