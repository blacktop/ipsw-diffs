## com.apple.ifdreader

> `/System/Library/CryptoTokenKit/com.apple.ifdreader.slotd/Contents/MacOS/com.apple.ifdreader`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_got`

```diff

-878.0.8.0.0
-  __TEXT.__text: 0xf428
+878.0.9.0.0
+  __TEXT.__text: 0x10b58
   __TEXT.__auth_stubs: 0x400
-  __TEXT.__objc_stubs: 0x2bc0
-  __TEXT.__objc_methlist: 0x1558
-  __TEXT.__objc_methname: 0x22a9
-  __TEXT.__objc_classname: 0x1d2
-  __TEXT.__cstring: 0xfd0
-  __TEXT.__objc_methtype: 0xa71
-  __TEXT.__const: 0x78
-  __TEXT.__oslogstring: 0xcc4
+  __TEXT.__objc_stubs: 0x2fa0
+  __TEXT.__objc_methlist: 0x17e8
+  __TEXT.__objc_methname: 0x288d
+  __TEXT.__objc_classname: 0x277
+  __TEXT.__cstring: 0x112f
+  __TEXT.__objc_methtype: 0xbc3
+  __TEXT.__const: 0x88
+  __TEXT.__oslogstring: 0xfce
   __TEXT.__gcc_except_tab: 0x134
-  __TEXT.__unwind_info: 0x550
-  __DATA_CONST.__const: 0x980
-  __DATA_CONST.__cfstring: 0x16c0
-  __DATA_CONST.__objc_classlist: 0xb8
+  __TEXT.__unwind_info: 0x5a8
+  __DATA_CONST.__const: 0x9a0
+  __DATA_CONST.__cfstring: 0x17c0
+  __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x20
+  __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x88
+  __DATA_CONST.__objc_superrefs: 0x90
   __DATA_CONST.__objc_intobj: 0x3d8
   __DATA_CONST.__objc_arraydata: 0xc0
   __DATA_CONST.__objc_arrayobj: 0x120
+  __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__auth_got: 0x210
-  __DATA_CONST.__got: 0x170
-  __DATA.__objc_const: 0x2058
-  __DATA.__objc_selrefs: 0xd88
-  __DATA.__objc_ivar: 0x94
-  __DATA.__objc_data: 0x730
-  __DATA.__data: 0x190
-  __DATA.__bss: 0x100
+  __DATA_CONST.__got: 0x190
+  __DATA.__objc_const: 0x2980
+  __DATA.__objc_selrefs: 0xee8
+  __DATA.__objc_ivar: 0xdc
+  __DATA.__objc_data: 0x9b0
+  __DATA.__data: 0x1f0
+  __DATA.__bss: 0x110
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CryptoTokenKit.framework/Versions/A/CryptoTokenKit
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 576
-  Symbols:   117
-  CStrings:  939
+  Functions: 631
+  Symbols:   119
+  CStrings:  1067
 
Symbols:
+ _NSLocalizedDescriptionKey
+ _OBJC_CLASS_$_NSConstantDoubleNumber
+ _OBJC_CLASS_$_NSDate
+ ___kCFBooleanFalse
- _NSInvalidArgumentException
- _OBJC_CLASS_$_NSException
CStrings:
+ ""
+ " (with time extensions)"
+ "!"
+ "1"
+ "@\"<CCIDBulkPipe>\""
+ "@\"<CCIDBulkPipe>\"16@0:8"
+ "@\"<CCIDControlEndpoint>\""
+ "@\"<CCIDControlEndpoint>\"16@0:8"
+ "@\"CCIDDescriptorView\""
+ "@\"CCIDDescriptorView\"16@0:8"
+ "@\"CCIDMessageView\""
+ "@\"NSNumber\"16@0:8"
+ "@32@0:8@16Q24"
+ "@40@0:8@16@24@?32"
+ "@64@0:8@16@24@32@40@48@56"
+ "ABORT drain deadline (%.1fs) expired without a matching SlotStatus terminator (seq=%u)"
+ "ABORT drain saw a frame for slot %u while aborting slot %u"
+ "B64@0:8@16@24@32C40C44Q48^@56"
+ "C44@0:8@16C24@28@36"
+ "CCIDAbortSequence"
+ "CCIDInterface"
+ "CCIDInterruptParser"
+ "CCIDOutboundFrame"
+ "CCIDParametersCodec"
+ "CCIDReceiveLoop"
+ "CCIDReceiveOutcome"
+ "CCIDReceiveParameters"
+ "CCIDSlotInterface"
+ "Communication error"
+ "Duplicate message detected (%u, %u, %u)!"
+ "Long operation in progress: %.1f seconds elapsed"
+ "Maximum response length exceeded (%lu)!"
+ "RDR_to_PC_HardwareError: short frame (%lu bytes)"
+ "RDR_to_PC_HardwareError: slot=%u bSeq=%u bHardwareErrorCode=0x%02x"
+ "Reached 'Receive message' timeout: %.3f%@"
+ "Received message with wrong slot number: %@"
+ "Received message with wrong slot sequence number: %@"
+ "T@\"<CCIDBulkPipe>\",R"
+ "T@\"<CCIDControlEndpoint>\",R"
+ "T@\"CCIDMessageView\",&,N,V_message"
+ "T@\"NSNumber\",&,N,V_timeout"
+ "T@\"NSNumber\",R"
+ "T@\"NSString\",R,N"
+ "TB,N,V_timeExtensionRequested"
+ "TC,N,V_duplicateMessage"
+ "TC,N,V_sequence"
+ "TC,N,V_slot"
+ "TQ,N,V_maxPayload"
+ "TQ,N,V_receiveSize"
+ "Td,N,V_elapsed"
+ "Td,N,V_maxWaitingTime"
+ "Td,N,V_maxWaitingTimeWithExtensions"
+ "Time extension received"
+ "Tq,N,V_kind"
+ "Unhandled interrupt-IN message type 0x%02x"
+ "_CCIDDescriptor"
+ "_bulkInPipe"
+ "_bulkOutPipe"
+ "_controlEndpoint"
+ "_duplicateMessage"
+ "_elapsed"
+ "_kind"
+ "_maxPayload"
+ "_maxWaitingTime"
+ "_maxWaitingTimeWithExtensions"
+ "_message"
+ "_productId"
+ "_receiveSize"
+ "_sequence"
+ "_timeExtensionRequested"
+ "_timeout"
+ "_vendorId"
+ "abortSequence: drain deadline (%.1fs) expired without matching SlotStatus terminator (seq=%u)"
+ "abortSequence: drain saw frame for slot %u while aborting slot %u; bailing"
+ "abortSequence: drain saw short/partial reply (%lu bytes); discarding"
+ "abortSequence: drained matching SlotStatus terminator (seq=%u)"
+ "abortSequence: step 1 control transfer failed (continuing to step 2): %{public}@"
+ "abortSequence: step 2 bulk-OUT short send (%lu of %lu bytes; continuing to step 3)"
+ "bulkInPipe"
+ "bulkOutPipe"
+ "com.apple.CryptoTokenKit.ccid.abort"
+ "controlEndpoint"
+ "d"
+ "d16@0:8"
+ "data"
+ "date"
+ "dateWithTimeIntervalSinceNow:"
+ "duplicateMessage"
+ "elapsed"
+ "errorMessage"
+ "incrementSequenceNumber"
+ "initWithProductId:vendorId:CCIDDescriptor:bulkInPipe:bulkOutPipe:controlEndpoint:"
+ "kind"
+ "maxPayload"
+ "maxWaitingTime"
+ "maxWaitingTimeWithExtensions"
+ "message"
+ "numberWithInt:"
+ "numberWithUnsignedInteger:"
+ "productId"
+ "protocolDataFromPayload:"
+ "q"
+ "receiveFromPipe:parameters:onTimeExtension:"
+ "receiveSize"
+ "runWithControlEndpoint:pipeOut:pipeIn:slot:sequence:maxMessageLength:error:"
+ "sendAbortRequestForSlot:sequence:error:"
+ "sequence"
+ "sequenceNumber"
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
+ "setTimeExtensionRequested:"
+ "setTimeout:"
+ "slotNotificationsFromBuffer:slotCount:"
+ "stampMessage:slot:sequence:sequenceSource:"
+ "timeExtensionRequested"
+ "timeIntervalSinceDate:"
+ "timeIntervalSinceNow"
+ "timeout"
+ "v20@0:8B16"
+ "v24@0:8d16"
+ "v24@0:8q16"
+ "vendorId"
- "Invalid length: %lu"
- "raise:format:"
```
