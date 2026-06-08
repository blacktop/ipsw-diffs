## AppleHIDTransportSupport

> `/System/Library/PrivateFrameworks/AppleHIDTransportSupport.framework/AppleHIDTransportSupport`

```diff

-9140.6.0.0.0
-  __TEXT.__text: 0x43d4
-  __TEXT.__auth_stubs: 0x4e0
-  __TEXT.__objc_methlist: 0x534
-  __TEXT.__const: 0x80
-  __TEXT.__cstring: 0x410
-  __TEXT.__gcc_except_tab: 0x18
-  __TEXT.__unwind_info: 0x178
-  __TEXT.__objc_classname: 0x3f
-  __TEXT.__objc_methname: 0x9a1
-  __TEXT.__objc_methtype: 0x1ba
-  __TEXT.__objc_stubs: 0x7a0
-  __DATA_CONST.__got: 0xc0
-  __DATA_CONST.__const: 0x98
+10100.34.0.0.0
+  __TEXT.__text: 0x623c
+  __TEXT.__objc_methlist: 0x72c
+  __TEXT.__const: 0x88
+  __TEXT.__cstring: 0x4da
+  __TEXT.__gcc_except_tab: 0x1e0
+  __TEXT.__oslogstring: 0x178
+  __TEXT.__unwind_info: 0x210
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x110
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x340
+  __DATA_CONST.__objc_selrefs: 0x490
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x280
+  __DATA_CONST.__got: 0xd8
   __AUTH_CONST.__const: 0x20
-  __AUTH_CONST.__cfstring: 0x560
-  __AUTH_CONST.__objc_const: 0x6a0
-  __DATA.__objc_ivar: 0x4c
+  __AUTH_CONST.__cfstring: 0x680
+  __AUTH_CONST.__objc_const: 0x8f0
+  __AUTH_CONST.__auth_got: 0x388
+  __DATA.__objc_ivar: 0x7c
   __DATA_DIRTY.__objc_data: 0x190
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libIOReport.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 81163F98-33F5-3DB5-90CE-8CB5928F831F
-  Functions: 116
-  Symbols:   463
-  CStrings:  274
+  UUID: 7B49B815-2319-3575-892B-B1697FE0DC3C
+  Functions: 171
+  Symbols:   664
+  CStrings:  125
 
Symbols:
+ -[AHTDevice .cxx_destruct]
+ -[AHTDevice cfMachPort]
+ -[AHTDevice cfRunLoopSource]
+ -[AHTDevice cleanupDispatchQueuePolling]
+ -[AHTDevice cleanupMachPort]
+ -[AHTDevice cleanupRunLoopPolling]
+ -[AHTDevice createMachPort]
+ -[AHTDevice dealloc]
+ -[AHTDevice dispatchQueue]
+ -[AHTDevice dispatchSource]
+ -[AHTDevice getPollingData:kernResult:]
+ -[AHTDevice handleMachNotification]
+ -[AHTDevice machPort]
+ -[AHTDevice parsePollingData:]
+ -[AHTDevice parsePollingEntryFromBytes:totalLength:offset:]
+ -[AHTDevice pollData:]
+ -[AHTDevice pollData:].cold.1
+ -[AHTDevice pollData:].cold.2
+ -[AHTDevice pollData:].cold.3
+ -[AHTDevice pollDataOnce:]
+ -[AHTDevice pollDataOnce]
+ -[AHTDevice pollData]
+ -[AHTDevice pollingBuffer]
+ -[AHTDevice pollingEnabled]
+ -[AHTDevice pollingFifoName]
+ -[AHTDevice pollingParsedAction]
+ -[AHTDevice pollingRawAction]
+ -[AHTDevice pollingScheduled]
+ -[AHTDevice runLoop]
+ -[AHTDevice setCfMachPort:]
+ -[AHTDevice setCfRunLoopSource:]
+ -[AHTDevice setDispatchQueue:]
+ -[AHTDevice setDispatchSource:]
+ -[AHTDevice setMachPort:]
+ -[AHTDevice setPollingBuffer:]
+ -[AHTDevice setPollingEnabled:]
+ -[AHTDevice setPollingFifoName:]
+ -[AHTDevice setPollingParsedAction:]
+ -[AHTDevice setPollingRawAction:]
+ -[AHTDevice setPollingScheduled:]
+ -[AHTDevice setRunLoop:]
+ -[AHTDevice startPollingCommon:error:]
+ -[AHTDevice startWithPolling:queue:error:]
+ -[AHTDevice startWithPolling:runLoop:error:]
+ -[AHTDevice stopPolling:]
+ GCC_except_table17
+ GCC_except_table23
+ GCC_except_table35
+ GCC_except_table39
+ _CFMachPortCreateRunLoopSource
+ _CFMachPortCreateWithPort
+ _CFMachPortInvalidate
+ _CFRunLoopAddSource
+ _CFRunLoopGetCurrent
+ _CFRunLoopPerformBlock
+ _CFRunLoopRemoveSource
+ _CFRunLoopWakeUp
+ _IOPMAssertionCreateWithName
+ _IOPMAssertionRelease
+ _MachPortCallbackForRunLoop
+ _OBJC_IVAR_$_AHTDevice._cfMachPort
+ _OBJC_IVAR_$_AHTDevice._cfRunLoopSource
+ _OBJC_IVAR_$_AHTDevice._dispatchQueue
+ _OBJC_IVAR_$_AHTDevice._dispatchSource
+ _OBJC_IVAR_$_AHTDevice._machPort
+ _OBJC_IVAR_$_AHTDevice._pollingBuffer
+ _OBJC_IVAR_$_AHTDevice._pollingEnabled
+ _OBJC_IVAR_$_AHTDevice._pollingFifoName
+ _OBJC_IVAR_$_AHTDevice._pollingParsedAction
+ _OBJC_IVAR_$_AHTDevice._pollingRawAction
+ _OBJC_IVAR_$_AHTDevice._pollingScheduled
+ _OBJC_IVAR_$_AHTDevice._runLoop
+ __OBJC_$_INSTANCE_VARIABLES_AHTDevice
+ __OBJC_$_PROP_LIST_AHTDevice
+ ___25-[AHTDevice stopPolling:]_block_invoke
+ ___35-[AHTDevice handleMachNotification]_block_invoke
+ ___35-[AHTDevice handleMachNotification]_block_invoke_2
+ ___42-[AHTDevice startWithPolling:queue:error:]_block_invoke
+ ___42-[AHTDevice startWithPolling:queue:error:]_block_invoke_2
+ ___42-[AHTDevice startWithPolling:queue:error:]_block_invoke_3
+ ___44-[AHTDevice startWithPolling:runLoop:error:]_block_invoke
+ ___block_descriptor_40_e8_32w_e5_v8?0lw32l8
+ ___block_descriptor_44_e8_32w_e5_v8?0lw32l8
+ ___block_descriptor_64_e8_32s40r48r56w_e5_v8?0lw56l8r40l8r48l8s32l8
+ __os_log_default
+ __os_log_error_impl
+ __os_log_impl
+ _dispatch_async
+ _dispatch_resume
+ _dispatch_semaphore_create
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
+ _dispatch_source_cancel
+ _dispatch_source_set_cancel_handler
+ _dispatch_time
+ _kCFRunLoopCommonModes
+ _kCFRunLoopDefaultMode
+ _mach_port_set_attributes
+ _objc_claimAutoreleasedReturnValue
+ _objc_copyWeak
+ _objc_destroyWeak
+ _objc_initWeak
+ _objc_loadWeakRetained
+ _objc_msgSend$cleanupDispatchQueuePolling
+ _objc_msgSend$cleanupMachPort
+ _objc_msgSend$cleanupRunLoopPolling
+ _objc_msgSend$createMachPort
+ _objc_msgSend$dataWithBytesNoCopy:length:freeWhenDone:
+ _objc_msgSend$dispatchQueue
+ _objc_msgSend$dispatchSource
+ _objc_msgSend$getCFRunLoop
+ _objc_msgSend$getPollingData:kernResult:
+ _objc_msgSend$handleMachNotification
+ _objc_msgSend$initWithLength:
+ _objc_msgSend$ioErrorWithDomain:code:error:
+ _objc_msgSend$open
+ _objc_msgSend$parsePollingData:
+ _objc_msgSend$parsePollingEntryFromBytes:totalLength:offset:
+ _objc_msgSend$pollData
+ _objc_msgSend$pollData:
+ _objc_msgSend$pollDataOnce:
+ _objc_msgSend$pollingBuffer
+ _objc_msgSend$pollingEnabled
+ _objc_msgSend$pollingFifoName
+ _objc_msgSend$pollingParsedAction
+ _objc_msgSend$pollingRawAction
+ _objc_msgSend$pollingScheduled
+ _objc_msgSend$runLoop
+ _objc_msgSend$setDispatchQueue:
+ _objc_msgSend$setDispatchSource:
+ _objc_msgSend$setPollingBuffer:
+ _objc_msgSend$setPollingEnabled:
+ _objc_msgSend$setPollingFifoName:
+ _objc_msgSend$setPollingScheduled:
+ _objc_msgSend$setRunLoop:
+ _objc_msgSend$startPollingCommon:error:
+ _objc_msgSend$stopPolling:
+ _objc_retain
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x8
+ _os_log_type_enabled
+ _strlen
CStrings:
+ "AHTDevice.pollData"
+ "AHTDevice: Received kAHTDeviceNotificationTypePollingReady notification"
+ "AHTDevice: Received unknown notification type: %u"
+ "AHTDevice: beginDrainFifo failed: 0x%x"
+ "AHTDevice: endDrainFifo failed: 0x%x"
+ "AHTDevice: initial pollData failed with 0x%x, disabling polling"
+ "AHTDevice: pollDataOnce called but polling is not enabled"
+ "AIDFirmwareUpdateService"
+ "AIDHIDSupport"
+ "Failed to create power assertion for polling data: 0x%x"
+ "PreventUserIdleSystemSleep"
+ "fail to create dispatch source"
+ "initial pollData failed"
+ "initial pollData timed out"
+ "polling is not started"
+ "queue is invalid"
- ".cxx_destruct"
- "@\"AHTDevice\""
- "@\"AHTInterface\""
- "@\"NSString\""
- "@16@0:8"
- "@20@0:8C16"
- "@20@0:8I16"
- "@24@0:8@16"
- "@24@0:8Q16"
- "@28@0:8@16I24"
- "@40@0:8@16@?24^@32"
- "AHTBootLoader"
- "AHTCommon"
- "AHTInterface"
- "AHTLoader"
- "AppleFirmwareUpdateKext"
- "B"
- "B16@0:8"
- "B20@0:8B16"
- "B24@0:8^@16"
- "B24@0:8^q16"
- "B24@0:8q16"
- "B28@0:8C16@20"
- "B28@0:8I16^@20"
- "B28@0:8i16^@20"
- "B32@0:8@16^@24"
- "B32@0:8Q16^@24"
- "B32@0:8^@16^@24"
- "B32@0:8^I16^@24"
- "B44@0:8@16B24Q28^@36"
- "B48@0:8@16@24@32^@40"
- "B48@0:8@16@24Q32^@40"
- "B48@0:8@16^@24Q32^@40"
- "C"
- "C16@0:8"
- "I"
- "I16@0:8"
- "Q16@0:8"
- "Q24@0:8Q16"
- "T@\"AHTDevice\",R,N,V_device"
- "T@\"AHTInterface\",R,N,V_interface"
- "T@\"NSString\",C,N,V_name"
- "T@\"NSString\",R,N,V_name"
- "T@\"NSString\",R,N,V_personality"
- "T@\"NSString\",R,N,V_type"
- "TB,R,N,V_needsRestoreUpdate"
- "TB,R,N,V_supportsMemoryDump"
- "TC,R,N,V_interfaceID"
- "TI,N,V_connect"
- "TI,N,V_machPort"
- "TI,N,V_service"
- "TI,R,N,V_connect"
- "TI,R,N,V_imageTag"
- "TI,R,N,V_loadingGroup"
- "TI,R,N,V_service"
- "UTF8String"
- "_connect"
- "_device"
- "_imageTag"
- "_interface"
- "_interfaceID"
- "_loadingGroup"
- "_machPort"
- "_name"
- "_needsRestoreUpdate"
- "_personality"
- "_service"
- "_supportsMemoryDump"
- "_type"
- "addObject:"
- "allBootloaders"
- "allDevices"
- "allInterfaces"
- "appendBytes:length:"
- "appendData:"
- "arrayWithObjects:count:"
- "bootloaderPropertiesForImageTag:"
- "bytes"
- "cStringUsingEncoding:"
- "captureMemoryDump"
- "clearMemoryDumps:"
- "close"
- "connect"
- "countByEnumeratingWithState:objects:count:"
- "createMachPort:"
- "dataUsingEncoding:"
- "dataWithBytes:length:"
- "dataWithCapacity:"
- "dataWithLength:"
- "dealloc"
- "description"
- "destroyMachPort"
- "device"
- "deviceWithParentRegistryId:"
- "dictionaryWithObjects:forKeys:count:"
- "dispatchSourceForNotification:action:error:"
- "errorFromAfuKextResult:error:"
- "errorFromKernel:error:"
- "errorWithDomain:code:userInfo:"
- "frameworkToDriverOptions:"
- "fullDescription"
- "getBootLoader"
- "getInterface:"
- "getInterfaceWithName:"
- "getInterfaces"
- "getMemoryDumpLevel:error:"
- "getMemoryDumps:error:"
- "getPower:"
- "getProperty:property:options:error:"
- "getRegistryProperties"
- "getReport:withData:"
- "imageTag"
- "init"
- "initWithCapacity:"
- "initWithData:encoding:"
- "initWithParent:service:"
- "initWithService:"
- "intValue"
- "interface"
- "interfaceID"
- "isEqualToNumber:"
- "isEqualToString:"
- "isOpen"
- "length"
- "loadImage:payloadOnly:options:error:"
- "loadingGroup"
- "machPort"
- "mutableBytes"
- "name"
- "needsRestoreUpdate"
- "numberWithLongLong:"
- "numberWithUnsignedInt:"
- "numberWithUnsignedInteger:"
- "objectForKeyedSubscript:"
- "open"
- "open:"
- "overrideFDR:fdrClass:fdrSubclass:error:"
- "overrideNextLoadOptions:error:"
- "overridePersonality:error:"
- "overrideProperties:error:"
- "personality"
- "registryID"
- "registryPropertiesForService:"
- "reloadProperties:error:"
- "reporterResults"
- "reset"
- "service"
- "setConnect:"
- "setEnable:"
- "setMachPort:"
- "setMemoryDumpLevel:error:"
- "setName:"
- "setObject:forKeyedSubscript:"
- "setPower:"
- "setReport:withData:"
- "setService:"
- "sortDescriptorWithKey:ascending:comparator:"
- "sortUsingDescriptors:"
- "stringByAppendingFormat:"
- "stringByAppendingString:"
- "stringByPaddingToLength:withString:startingAtIndex:"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "supportsMemoryDump"
- "type"
- "unsignedIntValue"
- "updateProperty:property:options:error:"
- "v16@0:8"
- "v20@0:8I16"
- "v24@0:8@16"
- "withDevice:service:"
- "withName:"
- "withParent:service:"
- "withService:"

```
