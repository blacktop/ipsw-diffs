## DAAPKit

> `/System/Library/PrivateFrameworks/DAAPKit.framework/DAAPKit`

```diff

-4025.500.37.0.0
-  __TEXT.__text: 0x2428
-  __TEXT.__auth_stubs: 0x1e0
+4026.100.61.0.0
+  __TEXT.__text: 0x2308
   __TEXT.__objc_methlist: 0x2d8
   __TEXT.__const: 0x8
-  __TEXT.__cstring: 0x3e2
+  __TEXT.__cstring: 0x3e9
   __TEXT.__unwind_info: 0x120
-  __TEXT.__objc_classname: 0x4d
-  __TEXT.__objc_methname: 0x895
-  __TEXT.__objc_methtype: 0x1a0
-  __TEXT.__objc_stubs: 0x840
-  __DATA_CONST.__got: 0x60
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x168
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x2c8
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0xf8
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__cfstring: 0x420
   __AUTH_CONST.__objc_const: 0x520
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x38
   __DATA_DIRTY.__objc_data: 0x140
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7BF18F1D-F17C-3F48-A8BD-3113D0AEB3C0
+  UUID: DA7CAE6F-EA7A-3846-9FE2-11DB56E0AF7F
   Functions: 73
-  Symbols:   307
-  CStrings:  221
+  Symbols:   310
+  CStrings:  68
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retain_x1
+ _objc_retain_x21
- _objc_retainAutoreleasedReturnValue
CStrings:
- ".cxx_destruct"
- "@\"<DKDAAPParserDelegate>\""
- "@\"NSError\""
- "@\"NSInputStream\""
- "@\"NSMutableArray\""
- "@\"NSMutableData\""
- "@\"NSOutputStream\""
- "@16@0:8"
- "@20@0:8I16"
- "@24@0:8@16"
- "B"
- "B16@0:8"
- "B20@0:8I16"
- "DKDAAPParser"
- "DKDAAPParserContainer"
- "DKDAAPWriter"
- "DKDAAPWriterContainer"
- "I"
- "I16@0:8"
- "Q"
- "Q16@0:8"
- "T@\"<DKDAAPParserDelegate>\",W,N,V_delegate"
- "T@\"NSError\",R,N,V_error"
- "T@\"NSInputStream\",R,N,V_inputStream"
- "T@\"NSMutableArray\",R,N,V_containerStack"
- "T@\"NSMutableData\",&,N,V_childData"
- "T@\"NSOutputStream\",R,N,V_outputStream"
- "TB,N,GisCanceled,V_canceled"
- "TI,N,V_code"
- "TI,N,V_length"
- "TI,N,V_remaining"
- "TI,R,N,V_code"
- "TQ,R,N,V_state"
- "Tq,R,N,V_state"
- "_callDelegateDidCancel"
- "_callDelegateDidEndContainerCode:"
- "_callDelegateDidFailWithError:"
- "_callDelegateDidFinish"
- "_callDelegateDidParseDataCode:bytes:contentLength:"
- "_callDelegateDidStart"
- "_callDelegateDidStartContainerCode:contentLength:"
- "_callDelegateShouldParseCode:"
- "_callDelegateShouldParseCodeAsContainer:"
- "_canceled"
- "_childData"
- "_code"
- "_containerStack"
- "_delegate"
- "_error"
- "_inputStream"
- "_length"
- "_outputStream"
- "_performWriteWithBuffer:"
- "_remaining"
- "_state"
- "_verifyExpectedEOF"
- "_writeDataToOutputStream:"
- "addObject:"
- "appendBytes:length:"
- "appendData:"
- "array"
- "bytes"
- "cStringUsingEncoding:"
- "cancel"
- "canceled"
- "childData"
- "close"
- "code"
- "containerStack"
- "count"
- "currentHandler"
- "dataWithCapacity:"
- "delegate"
- "dictionaryWithObject:forKey:"
- "dictionaryWithObjects:forKeys:count:"
- "endContainerWithCode:"
- "error"
- "errorWithDomain:code:userInfo:"
- "firstObject"
- "formattedOutputData"
- "handleFailureInMethod:object:file:lineNumber:description:"
- "init"
- "initWithCode:"
- "initWithData:"
- "initWithStream:"
- "inputStreamWithData:"
- "insertObject:atIndex:"
- "isCanceled"
- "lastObject"
- "length"
- "open"
- "outputStream"
- "parse"
- "parser:didEndContainerCode:"
- "parser:didFailWithError:"
- "parser:didFinishWithState:"
- "parser:didParseDataCode:bytes:contentLength:"
- "parser:didStartContainerCode:contentLength:"
- "parser:shouldParseCode:"
- "parser:shouldParseCodeAsContainer:"
- "parserDidCancel:"
- "parserDidStart:"
- "q"
- "q16@0:8"
- "read:maxLength:"
- "remaining"
- "removeLastObject"
- "removeObjectAtIndex:"
- "setCanceled:"
- "setChildData:"
- "setCode:"
- "setDelegate:"
- "setLength:"
- "setObject:forKeyedSubscript:"
- "setRemaining:"
- "startContainerWithCode:"
- "state"
- "streamError"
- "stringWithFormat:"
- "subdataWithRange:"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8I16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8C16I20"
- "v24@0:8I16I20"
- "v24@0:8S16I20"
- "v24@0:8c16I20"
- "v24@0:8i16I20"
- "v24@0:8s16I20"
- "v28@0:8@16I24"
- "v28@0:8Q16I24"
- "v28@0:8q16I24"
- "v28@0:8r*16I24"
- "v32@0:8*16I24I28"
- "v32@0:8I16*20I28"
- "write:maxLength:"
- "writeBytes:ofLength:withCode:"
- "writeCString:withCode:"
- "writeContainerData:"
- "writeData:withCode:"
- "writeSInt16:withCode:"
- "writeSInt32:withCode:"
- "writeSInt64:withCode:"
- "writeSInt8:withCode:"
- "writeString:withCode:"
- "writeUInt16:withCode:"
- "writeUInt32:withCode:"
- "writeUInt64:withCode:"
- "writeUInt8:withCode:"

```
