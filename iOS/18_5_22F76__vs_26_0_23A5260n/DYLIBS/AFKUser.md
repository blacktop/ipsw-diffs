## AFKUser

> `/System/Library/PrivateFrameworks/AFKUser.framework/AFKUser`

```diff

-531.120.3.0.0
-  __TEXT.__text: 0x4d78
-  __TEXT.__auth_stubs: 0x440
-  __TEXT.__objc_methlist: 0x378
-  __TEXT.__const: 0x78
-  __TEXT.__gcc_except_tab: 0x7e0
-  __TEXT.__oslogstring: 0x6b3
-  __TEXT.__cstring: 0xe9
-  __TEXT.__unwind_info: 0x308
-  __TEXT.__objc_classname: 0x65
-  __TEXT.__objc_methname: 0x7c1
-  __TEXT.__objc_methtype: 0x34c
-  __TEXT.__objc_stubs: 0x400
-  __DATA_CONST.__got: 0x50
-  __DATA_CONST.__const: 0xc0
-  __DATA_CONST.__objc_classlist: 0x20
+634.0.3.0.0
+  __TEXT.__text: 0x6870
+  __TEXT.__auth_stubs: 0x5a0
+  __TEXT.__objc_methlist: 0x3f0
+  __TEXT.__const: 0x90
+  __TEXT.__gcc_except_tab: 0x954
+  __TEXT.__oslogstring: 0x8c8
+  __TEXT.__cstring: 0x1e2
+  __TEXT.__unwind_info: 0x360
+  __TEXT.__objc_classname: 0x7a
+  __TEXT.__objc_methname: 0x910
+  __TEXT.__objc_methtype: 0x387
+  __TEXT.__objc_stubs: 0x620
+  __DATA_CONST.__got: 0x78
+  __DATA_CONST.__const: 0x1d8
+  __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1f0
-  __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x230
+  __DATA_CONST.__objc_selrefs: 0x260
+  __DATA_CONST.__objc_superrefs: 0x28
+  __AUTH_CONST.__auth_got: 0x2e8
   __AUTH_CONST.__const: 0x20
-  __AUTH_CONST.__cfstring: 0x100
-  __AUTH_CONST.__objc_const: 0x6a0
-  __DATA.__objc_ivar: 0x74
+  __AUTH_CONST.__cfstring: 0x1e0
+  __AUTH_CONST.__objc_const: 0x790
+  __AUTH_CONST.__objc_intobj: 0x18
+  __DATA.__objc_ivar: 0x7c
   __DATA.__data: 0x10
   __DATA.__bss: 0x10
-  __DATA_DIRTY.__objc_data: 0x140
+  __DATA_DIRTY.__objc_data: 0x190
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4B7CB610-B0CF-3858-96DC-643DF0053C39
-  Functions: 119
-  Symbols:   513
-  CStrings:  209
+  UUID: 89ADA5C1-3DBB-3E1E-9541-0A036E9B4DE2
+  Functions: 155
+  Symbols:   645
+  CStrings:  260
 
Symbols:
+ +[AFKUserSystemService withService:]
+ -[AFKEndpointInterface hasState:]
+ -[AFKEndpointInterface initWithService:].cold.1
+ -[AFKEndpointInterface initWithService:].cold.2
+ -[AFKEndpointInterface initWithService:].cold.3
+ -[AFKUserSystemService copyMatchedServiceProperties:key:error:]
+ -[AFKUserSystemService copyMatchedServiceProperties:key:error:].cold.1
+ -[AFKUserSystemService copyMatchedServiceProperties:key:error:].cold.2
+ -[AFKUserSystemService dealloc]
+ -[AFKUserSystemService initWithService:]
+ -[AFKUserSystemService initWithService:].cold.1
+ -[AFKUserSystemService initWithService:].cold.2
+ -[AFKUserSystemService regID]
+ -[AFKUserSystemService registry:]
+ -[AFKUserSystemService registry:].cold.1
+ -[AFKUserSystemService setMatchedServiceProperties:proprties:error:]
+ -[AFKUserSystemService setMatchedServiceProperties:proprties:error:].cold.1
+ -[AFKUserSystemService setMatchedServiceProperties:proprties:error:].cold.2
+ GCC_except_table21
+ GCC_except_table3
+ GCC_except_table31
+ GCC_except_table35
+ GCC_except_table37
+ GCC_except_table53
+ GCC_except_table54
+ GCC_except_table76
+ _CFRelease
+ _IOCFSerialize
+ _IOCFUnserializeBinary
+ _IOCFUnserializeWithSize
+ _OBJC_CLASS_$_AFKUserSystemService
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OBJC_CLASS_$_NSDictionary
+ _OBJC_CLASS_$_NSMutableArray
+ _OBJC_CLASS_$_NSMutableData
+ _OBJC_IVAR_$_AFKUserSystemService._regID
+ _OBJC_IVAR_$_AFKUserSystemService._service
+ _OBJC_METACLASS_$_AFKUserSystemService
+ _OUTLINED_FUNCTION_10
+ __OBJC_$_CLASS_METHODS_AFKUserSystemService
+ __OBJC_$_INSTANCE_METHODS_AFKUserSystemService
+ __OBJC_$_INSTANCE_VARIABLES_AFKUserSystemService
+ __OBJC_$_PROP_LIST_AFKUserSystemService
+ __OBJC_CLASS_RO_$_AFKUserSystemService
+ __OBJC_METACLASS_RO_$_AFKUserSystemService
+ ___33-[AFKUserSystemService registry:]_block_invoke
+ ___33-[AFKUserSystemService registry:]_block_invoke.10
+ ___33-[AFKUserSystemService registry:]_block_invoke_2
+ ___33-[AFKUserSystemService registry:]_block_invoke_2.20
+ ___33-[AFKUserSystemService registry:]_block_invoke_3
+ ___63-[AFKUserSystemService copyMatchedServiceProperties:key:error:]_block_invoke
+ ___63-[AFKUserSystemService copyMatchedServiceProperties:key:error:]_block_invoke.cold.1
+ ___63-[AFKUserSystemService copyMatchedServiceProperties:key:error:]_block_invoke.cold.2
+ ___68-[AFKUserSystemService setMatchedServiceProperties:proprties:error:]_block_invoke
+ ___68-[AFKUserSystemService setMatchedServiceProperties:proprties:error:]_block_invoke.cold.1
+ ___block_descriptor_48_e8_32r40r_e15_v32?08Q16^B24lr32l8r40l8
+ ___block_descriptor_48_e8_32s40r_e15_v32?08Q16^B24lr40l8s32l8
+ ___block_descriptor_48_e8_32s40r_e47_v52?0"AFKEndpointInterface"8^v16i24Q28^v36Q44lr40l8s32l8
+ ___block_descriptor_48_e8_32s40s_e15_v32?08Q16^B24ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e47_v52?0"AFKEndpointInterface"8^v16i24Q28^v36Q44ls32l8s40l8
+ ___block_descriptor_56_e8_32s40r48r_e44_v44?0"AFKEndpointInterface"8I16Q20r^v28Q36ls32l8r40l8r48l8
+ ___block_descriptor_64_e8_32s40s48r_e47_v52?0"AFKEndpointInterface"8^v16i24Q28^v36Q44ls32l8r48l8s40l8
+ ___objc_personality_v0
+ __os_log_debug_impl
+ _dispatch_queue_create
+ _dispatch_semaphore_create
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
+ _dispatch_time
+ _kCFAllocatorDefault
+ _mach_continuous_time
+ _objc_alloc_init
+ _objc_autorelease
+ _objc_msgSend$addObject:
+ _objc_msgSend$appendBytes:length:
+ _objc_msgSend$bytes
+ _objc_msgSend$cancel
+ _objc_msgSend$dictionaryWithObjects:forKeys:count:
+ _objc_msgSend$enumerateObjectsUsingBlock:
+ _objc_msgSend$hasState:
+ _objc_msgSend$initWithCapacity:
+ _objc_msgSend$objectAtIndexedSubscript:
+ _objc_msgSend$objectForKeyedSubscript:
+ _objc_msgSend$setDispatchQueue:
+ _objc_msgSend$setObject:atIndexedSubscript:
+ _objc_msgSend$setObject:forKeyedSubscript:
+ _objc_msgSend$setReportHandler:
+ _objc_msgSend$setResponseHandler:
+ _objc_msgSend$withService:
+ _objc_msgSend$withService:properties:
+ _objc_release_x25
+ _objc_release_x26
+ _objc_release_x27
+ _objc_release_x28
+ _objc_release_x9
+ _objc_retainAutorelease
+ _objc_retain_x1
+ _objc_retain_x21
+ _objc_retain_x27
- GCC_except_table29
- GCC_except_table34
- GCC_except_table36
- GCC_except_table49
- GCC_except_table50
- GCC_except_table72
CStrings:
+ "0x%llx: Could not encode value for setting property %@\n"
+ "0x%llx: IOCFUnserializeBinary failed:%@"
+ "0x%llx: IOCFUnserializeWithSize:%@"
+ "0x%llx: IOObjectRetain:0x%x"
+ "0x%llx: IORegistryEntryGetRegistryEntryID:0x%x"
+ "0x%llx: Timed out waiting for response from setMatchedServiceProperties %@"
+ "0x%llx: Timeout waiting for getProperty: %@"
+ "0x%llx: getPropertyFromMatchedService:0x%x"
+ "0x%llx: packetType:0x%x timestamp:%lld inputBuffer:%p inputBufferSize:%zu"
+ "0x%llx: service==IO_OBJECT_NULL"
+ "0x%llx: setPropertyOnMatchedService:0x%x"
+ "@24@0:8^@16"
+ "@40@0:8@16@24^@32"
+ "AFKRootService"
+ "AFKUser"
+ "AFKUserSystemService"
+ "B20@0:8I16"
+ "B40@0:8@16@24^@32"
+ "addObject:"
+ "afkregistry"
+ "appendBytes:length:"
+ "assertion failure: \"[self hasState:(kAFKDispatchStateActiveStart)]\" -> %llu"
+ "assertion failure: \"state & kAFKDispatchStateActiveStart\" -> %llu"
+ "bytes"
+ "children"
+ "class"
+ "copyMatchedServiceProperties"
+ "copyMatchedServiceProperties:key:error:"
+ "dictionaryWithObjects:forKeys:count:"
+ "enumerateObjectsUsingBlock:"
+ "hasState:"
+ "i"
+ "id"
+ "initWithCapacity:"
+ "objectAtIndexedSubscript:"
+ "objectForKeyedSubscript:"
+ "properties"
+ "registry:"
+ "service-matching"
+ "setMatchedServiceProperties"
+ "setMatchedServiceProperties:proprties:error:"
+ "setObject:atIndexedSubscript:"
+ "setObject:forKeyedSubscript:"
+ "v32@?0@8Q16^B24"
+ "v44@?0@\"AFKEndpointInterface\"8I16Q20r^v28Q36"
+ "v52@?0@\"AFKEndpointInterface\"8^v16i24Q28^v36Q44"
- "assertion failure: \"_state == kAFKDispatchStateActive\" -> %llu"
- "assertion failure: \"state & kAFKDispatchStateActive\" -> %llu"

```
