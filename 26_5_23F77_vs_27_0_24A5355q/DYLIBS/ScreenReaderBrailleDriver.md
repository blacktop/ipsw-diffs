## ScreenReaderBrailleDriver

> `/System/Library/PrivateFrameworks/ScreenReaderBrailleDriver.framework/ScreenReaderBrailleDriver`

```diff

-424.15.0.0.0
-  __TEXT.__text: 0xc754
-  __TEXT.__auth_stubs: 0x5f0
+455.1.1.0.0
+  __TEXT.__text: 0xc1ac
   __TEXT.__objc_methlist: 0x274
-  __TEXT.__const: 0x380
-  __TEXT.__cstring: 0x562
-  __TEXT.__oslogstring: 0x2db
+  __TEXT.__const: 0x34c
   __TEXT.__gcc_except_tab: 0x28
-  __TEXT.__unwind_info: 0x2d0
-  __TEXT.__objc_classname: 0x52
-  __TEXT.__objc_methname: 0x7f5
-  __TEXT.__objc_methtype: 0x26c
-  __TEXT.__objc_stubs: 0x800
-  __DATA_CONST.__got: 0x78
+  __TEXT.__cstring: 0x569
+  __TEXT.__oslogstring: 0x2db
+  __TEXT.__unwind_info: 0x2b0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x98
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x2c8
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x308
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x9a0
   __AUTH_CONST.__objc_const: 0x498
+  __AUTH_CONST.__auth_got: 0x340
   __AUTH.__objc_data: 0x140
   __DATA.__objc_ivar: 0x40
-  __DATA.__data: 0x208
+  __DATA.__data: 0x200
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/ScreenReaderOutput.framework/ScreenReaderOutput
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 58707CE2-FE7F-3424-96CB-32D2A383C642
-  Functions: 204
-  Symbols:   576
-  CStrings:  327
+  UUID: 26FD5824-B14C-3487-97FA-83864BAF727B
+  Functions: 197
+  Symbols:   568
+  CStrings:  178
 
Symbols:
+ GCC_except_table171
+ GCC_except_table81
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x24
+ _objc_retain_x25
+ _objc_retain_x26
+ _objc_retain_x28
+ _objc_retain_x8
- +[SCRDUSBDeviceCallbackManager sharedManager].cold.1
- GCC_except_table5
- GCC_except_table7
- __SCRDEventForKeyID
- __SCRDPapenmeierCreateWriteBuffer
- __SCRDSeikaNotetakerExtractEventsFromBuffer
- __appendBrailleKeyboardEvent
- __appendInteractiveKeyboardEvent
- __createKeyboardPacketFromBuffer
- _kSCRDFreedomScientificFocus14ModelName
- _objc_retainAutoreleasedReturnValue
CStrings:
- ".cxx_destruct"
- "@\"<SCRDFileReaderDelegate>\""
- "@\"NSData\""
- "@\"NSFileHandle\""
- "@\"NSMutableDictionary\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\""
- "@\"NSThread\""
- "@16@0:8"
- "@20@0:8I16"
- "@32@0:8@16@24"
- "B"
- "B16@0:8"
- "B20@0:8B16"
- "B20@0:8C16"
- "B24@0:8C16B20"
- "B36@0:8^v16^Q24C32"
- "B44@0:8^v16Q24C32I36I40"
- "B60@0:8C16*20*28*36^S44*52"
- "B64@0:8C16C20S24S28^v32S40^Q44C52d56"
- "C"
- "C16@0:8"
- "I"
- "Q44@0:8^v16Q24C32I36I40"
- "Q44@0:8^v16Q24C32d36"
- "Q52@0:8^v16Q24C32d36^?44"
- "SCRDFileReader"
- "SCRDKGSPacket"
- "SCRDUSBDevice"
- "SCRDUSBDeviceCallbackManager"
- "T@\"NSData\",&,N,V_data"
- "TC,N,V_command"
- "TC,N,V_subCommand"
- "^^{IOUSBDeviceStruct300}"
- "^^{IOUSBInterfaceStruct220}"
- "^{IONotificationPort=}"
- "^{_SCRDUSBDeviceCompletion=Qi}24@0:8^v16"
- "_command"
- "_completions"
- "_data"
- "_delegate"
- "_device"
- "_fileHandle"
- "_interface"
- "_isConfigured"
- "_isOpen"
- "_notification"
- "_notificationPort"
- "_privateRunLoopMode"
- "_queue"
- "_readHandler:"
- "_readerThread"
- "_subCommand"
- "_threadStartCount"
- "_transferData:withSize:toPipe:withTimeout:withFunction:"
- "abortPipe:"
- "addCompletion:"
- "addObject:"
- "array"
- "bytes"
- "cStringUsingEncoding:"
- "cancel"
- "clearPipe:bothEnds:"
- "close"
- "command"
- "completionWithReference:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "currentThread"
- "data"
- "dealloc"
- "defaultCenter"
- "dictionaryWithObjects:forKeys:count:"
- "fileDescriptor"
- "fileReader:data:length:"
- "floatValue"
- "getInformationForPipe:direction:number:transferType:maxPacketSize:interval:"
- "hasStarted"
- "himsUsesDot7ForCommands"
- "i"
- "i16@0:8"
- "indexesOfObjectsPassingTest:"
- "init"
- "initWithBytes:length:"
- "initWithDelegate:fileHandle:"
- "initWithFormat:"
- "initWithIOObject:"
- "initWithObjectsAndKeys:"
- "initWithTarget:selector:object:"
- "initWithUTF8String:"
- "insertObject:atIndex:"
- "intValue"
- "invalidate"
- "invalidateWithWait:"
- "isCancelled"
- "isConfigured"
- "isEqualToString:"
- "isExecuting"
- "isFinished"
- "isOpen"
- "isValid"
- "length"
- "numberOfConfigurations"
- "numberWithBool:"
- "numberWithInt:"
- "numberWithLong:"
- "numberWithUnsignedChar:"
- "numberWithUnsignedInt:"
- "numberWithUnsignedLong:"
- "numberWithUnsignedShort:"
- "objectForKey:"
- "open"
- "openWithSeize:"
- "pointerValue"
- "postNotificationName:object:"
- "postNotificationName:object:userInfo:"
- "product"
- "readData:withSize:fromBulkPipe:withNoDataTimeout:andCompletionTimeOut:"
- "readData:withSize:fromPipe:"
- "readData:withSize:fromPipe:withTimeout:"
- "registerForDisconnectNotifications:"
- "removeCompletion:"
- "removeObjectForKey:"
- "removeObjectsAtIndexes:"
- "reset"
- "sendControlRequest:type:value:index:data:size:sizeTransferred:pipe:timeout:"
- "setAlternateInterface:"
- "setCommand:"
- "setConfiguration:"
- "setData:"
- "setInterface:"
- "setObject:forKey:"
- "setSubCommand:"
- "sharedInstance"
- "sharedManager"
- "sleepForTimeInterval:"
- "start"
- "subCommand"
- "unsignedIntValue"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8C16"
- "v24@0:8@16"
- "v24@0:8^v16"
- "v24@0:8^{_SCRDUSBDeviceCompletion=Qi}16"
- "valueWithPointer:"
- "vendor"
- "writeData:withSize:toBulkPipe:withNoDataTimeout:andCompletionTimeOut:"
- "writeData:withSize:toPipe:withTimeout:"

```
