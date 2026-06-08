## AFKUser

> `/System/Library/PrivateFrameworks/AFKUser.framework/AFKUser`

```diff

-634.120.2.0.0
-  __TEXT.__text: 0x6794
-  __TEXT.__auth_stubs: 0x560
+736.0.0.502.1
+  __TEXT.__text: 0x67f0
   __TEXT.__objc_methlist: 0x3f0
   __TEXT.__const: 0x90
-  __TEXT.__gcc_except_tab: 0x938
-  __TEXT.__oslogstring: 0x8c8
-  __TEXT.__cstring: 0x1e2
+  __TEXT.__gcc_except_tab: 0x92c
+  __TEXT.__oslogstring: 0x8cc
+  __TEXT.__cstring: 0x25d
   __TEXT.__unwind_info: 0x368
-  __TEXT.__objc_classname: 0x7a
-  __TEXT.__objc_methname: 0x910
-  __TEXT.__objc_methtype: 0x387
-  __TEXT.__objc_stubs: 0x620
-  __DATA_CONST.__got: 0x78
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x1d8
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x260
+  __DATA_CONST.__objc_selrefs: 0x268
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x2c8
+  __DATA_CONST.__got: 0x88
   __AUTH_CONST.__const: 0x20
-  __AUTH_CONST.__cfstring: 0x1e0
+  __AUTH_CONST.__cfstring: 0x200
   __AUTH_CONST.__objc_const: 0x790
+  __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x18
+  __AUTH_CONST.__auth_got: 0x348
   __DATA.__objc_ivar: 0x7c
   __DATA.__data: 0x10
   __DATA.__bss: 0x10

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3893A4B3-5AD1-340D-AA43-E8CB87A3D6FB
-  Functions: 156
-  Symbols:   646
-  CStrings:  260
+  UUID: A510C137-E504-304C-9A84-C984BAC370F3
+  Functions: 160
+  Symbols:   670
+  CStrings:  102
 
Symbols:
+ _CFRunLoopAddSource
+ _CFRunLoopGetCurrent
+ _CFRunLoopRemoveSource
+ _CFRunLoopRun
+ _CFRunLoopStop
+ _IOConnectMapMemory64
+ _IOIteratorNext
+ _IONotificationPortGetRunLoopSource
+ _IOServiceAddMatchingNotification
+ _IOServiceMatching
+ _OBJC_CLASS_$_NSString
+ __ZL13matchCallbackPvj
+ __ZN18afkshmem_mapping_sD2Ev
+ __ZdlPvSt19__type_descriptor_t
+ __ZnwmSt19__type_descriptor_t
+ ___assert_rtn
+ _afkshmem_create_mapping
+ _afkshmem_create_mapping.cold.1
+ _afkshmem_destroy_mapping
+ _afkshmem_get_address
+ _afkshmem_get_size
+ _kCFRunLoopDefaultMode
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$stringWithCString:encoding:
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x21
+ _objc_retain_x3
+ _objc_retain_x8
+ _strlcpy
- GCC_except_table53
- GCC_except_table54
- GCC_except_table76
- _OUTLINED_FUNCTION_9
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x24
CStrings:
+ "AFKSharedMemory.mm"
+ "AFKSharedMemoryRegionBase"
+ "IONameMatch"
+ "IOServiceFirstMatch"
+ "afkshmem_create_mapping"
+ "assertion failure: \"size >= sizeof(*command)\" -> %llu"
+ "assertion failure: \"size >= sizeof(*descMsg)\" -> %llu"
+ "assertion failure: \"size >= sizeof(*queue)\" -> %llu"
+ "assertion failure: \"size >= sizeof(*response)\" -> %llu"
+ "name && handle"
- "*"
- "*16@0:8"
- ".cxx_destruct"
- "@"
- "@\"AFKMemoryDescriptorManager\""
- "@\"NSMutableDictionary\""
- "@\"NSObject<OS_dispatch_mach>\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_dispatch_source>\""
- "@\"NSSet\""
- "@16@0:8"
- "@20@0:8I16"
- "@24@0:8^@16"
- "@28@0:8I16@20"
- "@32@0:8@16Q24"
- "@36@0:8@16Q24B32"
- "@40@0:8@16@24^@32"
- "@40@0:8@16Q24Q32"
- "@?"
- "AFKBufferMemoryDescriptor"
- "AFKMemoryDescriptor"
- "AFKMemoryDescriptorManager"
- "AFKUserSystemService"
- "B16@0:8"
- "B20@0:8I16"
- "B24@0:8@16"
- "B40@0:8@16@24^@32"
- "I"
- "I16@0:8"
- "Q"
- "Q16@0:8"
- "T*,R,N,V_buffer"
- "T@\"AFKMemoryDescriptorManager\",R,N,V_manager"
- "TI,R,N,V_connect"
- "TQ,N"
- "TQ,R,N,V_capacity"
- "TQ,R,N,V_regID"
- "TQ,R,N,V_token"
- "^v32@0:8Q16Q24"
- "^{IONotificationPort=}"
- "^{_IODataQueueMemory=III[1{_IODataQueueEntry=I[4C]}]}"
- "_asyncPort"
- "_buffer"
- "_cachedLength"
- "_cancel"
- "_capacity"
- "_commandHandler"
- "_commandHandlerWithReturn"
- "_connect"
- "_dataQueue"
- "_dataQueueMachChannel"
- "_dataQueuePort"
- "_dataQueueSize"
- "_descriptorHandler"
- "_descriptorManagers"
- "_eventHandler"
- "_manager"
- "_properties"
- "_queue"
- "_regID"
- "_reportHandler"
- "_responseHandler"
- "_service"
- "_source"
- "_state"
- "_token"
- "activate"
- "activate:"
- "addObject:"
- "appendBytes:length:"
- "appendBytes:withSize:"
- "assertPower:"
- "assertion failure: \"size >= sizeof(command)\" -> %llu"
- "assertion failure: \"size >= sizeof(descMsg)\" -> %llu"
- "assertion failure: \"size >= sizeof(queue)\" -> %llu"
- "assertion failure: \"size >= sizeof(response)\" -> %llu"
- "assumeControl"
- "assumeControlWithOffset:andSize:"
- "buffer"
- "bytes"
- "cancel"
- "capacity"
- "compleOOBBuffer:"
- "connect"
- "copyMatchedServiceProperties:key:error:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "dealloc"
- "dequeueDataMessage:"
- "dictionaryWithObjects:forKeys:count:"
- "enqueueCommand:inputBuffer:inputBufferSize:outputPayloadSize:context:options:"
- "enqueueCommand:timestamp:inputBuffer:inputBufferSize:outputPayloadSize:context:options:"
- "enqueueCommandSync:timestamp:inputBuffer:inputBufferSize:responseTimestamp:outputBuffer:inOutBufferSize:options:"
- "enqueueDescriptor:packetType:timestamp:options:"
- "enqueueReport:inputBuffer:inputBufferSize:options:"
- "enqueueReport:timestamp:inputBuffer:inputBufferSize:options:"
- "enqueueResponseForContext:status:outputBuffer:outputBufferSize:options:"
- "enqueueResponseForContext:status:timestamp:outputBuffer:outputBufferSize:options:"
- "enumerateObjectsUsingBlock:"
- "errorWithDomain:code:userInfo:"
- "getBytesNoCopy:withSize:"
- "handleCommand:size:"
- "handleDescriptor:size:"
- "handleEnqueue"
- "handleQueue:size:"
- "handleReport:size:"
- "handleResponse:size:"
- "hasState:"
- "i16@0:8"
- "i20@0:8B16"
- "i24@0:8Q16"
- "i32@0:8Q16Q24"
- "i32@0:8r^v16Q24"
- "i36@0:8B16Q20Q28"
- "i40@0:8@16I24Q28I36"
- "i40@0:8I16r^v20Q28I36"
- "i40@0:8^v16Q24Q32"
- "i40@0:8r^v16Q24Q32"
- "i48@0:8I16Q20r^v28Q36I44"
- "i48@0:8^v16i24^v28Q36I44"
- "i56@0:8I16r^v20Q28Q36^v44I52"
- "i56@0:8^v16i24Q28^v36Q44I52"
- "i64@0:8I16Q20r^v28Q36Q44^v52I60"
- "i72@0:8I16Q20r^v28Q36^Q44^v52^Q60I68"
- "init"
- "initWithCapacity:"
- "initWithManager:capacity:buffer:"
- "initWithManager:capacity:token:"
- "initWithService:"
- "isEqual:"
- "length"
- "manager"
- "mapDescriptor"
- "me"
- "mutableCopy"
- "objectAtIndexedSubscript:"
- "objectForKeyedSubscript:"
- "readBytes:size:fromOffset:"
- "regID"
- "registry:"
- "releaseControl:"
- "releaseControl:withOffset:andSize:"
- "setCommandHandler:"
- "setCommandHandlerWithReturn:"
- "setDescriptorHandler:"
- "setDescriptorManagers:"
- "setDispatchQueue:"
- "setEventHandler:"
- "setLength:"
- "setMatchedServiceProperties:proprties:error:"
- "setObject:atIndexedSubscript:"
- "setObject:forKeyedSubscript:"
- "setReportHandler:"
- "setResponseHandler:"
- "startSession:"
- "token"
- "v16@0:8"
- "v20@0:8I16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8Q16"
- "v24@0:8^{_IODataQueueMemory=III[1{_IODataQueueEntry=I[4C]}]}16"
- "v28@0:8*16I24"
- "withManager:capacity:"
- "withManager:capacity:token:"
- "withService:"
- "withService:properties:"
- "writeBytes:size:toOffset:"

```
