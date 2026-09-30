## peakpowermanagerd

> `/usr/libexec/peakpowermanagerd`

```diff

-931.120.2.0.0
-  __TEXT.__text: 0xd2d8
-  __TEXT.__auth_stubs: 0x490
-  __TEXT.__objc_stubs: 0x1ec0
+1035.0.7.0.0
+  __TEXT.__text: 0xfd38
+  __TEXT.__auth_stubs: 0x680
+  __TEXT.__objc_stubs: 0x2140
   __TEXT.__objc_methlist: 0x10ac
-  __TEXT.__objc_methname: 0x28c5
-  __TEXT.__cstring: 0x768
-  __TEXT.__objc_classname: 0x5b
+  __TEXT.__objc_methname: 0x2a53
+  __TEXT.__cstring: 0x7e6
+  __TEXT.__objc_classname: 0x5c
   __TEXT.__objc_methtype: 0x2e7
-  __TEXT.__const: 0x30
-  __TEXT.__oslogstring: 0x4e1
-  __TEXT.__unwind_info: 0x278
-  __DATA_CONST.__auth_got: 0x250
-  __DATA_CONST.__got: 0x90
-  __DATA_CONST.__const: 0x68
-  __DATA_CONST.__cfstring: 0x9e0
+  __TEXT.__const: 0x58
+  __TEXT.__gcc_except_tab: 0x9c
+  __TEXT.__oslogstring: 0x909
+  __TEXT.__unwind_info: 0x2c0
+  __DATA_CONST.__auth_got: 0x350
+  __DATA_CONST.__got: 0xa0
+  __DATA_CONST.__const: 0xb8
+  __DATA_CONST.__cfstring: 0xa80
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA.__objc_const: 0x13f0
-  __DATA.__objc_selrefs: 0xb18
+  __DATA.__objc_selrefs: 0xbb8
   __DATA.__objc_ivar: 0x114
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x60
-  __DATA.__bss: 0x18
+  __DATA.__bss: 0x20
+  __DATA.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
+  - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 64E95F51-A18B-3AF1-AE2D-B914C33FBC5F
-  Functions: 402
-  Symbols:   101
-  CStrings:  711
+  UUID: 9109576A-2E19-36F6-AAE7-A911ED07368E
+  Functions: 434
+  Symbols:   135
+  CStrings:  759
 
Symbols:
+ _CFBooleanGetTypeID
+ _CFBooleanGetValue
+ _IOConnectCallMethod
+ _IOConnectMapMemory
+ _IOConnectSetNotificationPort
+ _IODataQueueAllocateNotificationPort
+ _IODataQueueDataAvailable
+ _IODataQueueDequeue
+ _IODataQueuePeek
+ _IOObjectRelease
+ _OBJC_CLASS_$_NSData
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_NSDateFormatter
+ _OBJC_CLASS_$_NSPropertyListSerialization
+ _PPSCreateTelemetryIdentifier
+ _PPSSendTelemetry
+ __Block_object_dispose
+ __Unwind_Resume
+ ___objc_personality_v0
+ __dispatch_source_type_mach_recv
+ __dispatch_source_type_timer
+ _dispatch_get_global_queue
+ _dispatch_resume
+ _dispatch_source_cancel
+ _dispatch_source_create
+ _dispatch_source_set_cancel_handler
+ _dispatch_source_set_event_handler
+ _dispatch_source_set_timer
+ _dispatch_time
+ _mach_error_string
+ _mach_msg
+ _mach_port_mod_refs
+ _objc_enumerationMutation
+ _objc_opt_isKindOfClass
+ _objc_release_x27
+ _objc_release_x28
+ _objc_retain_x19
+ _objc_retain_x22
+ _objc_retain_x23
- OBJC_IVAR_$_PBDataReader._bytes
- OBJC_IVAR_$_PBDataReader._error
- OBJC_IVAR_$_PBDataReader._length
- OBJC_IVAR_$_PBDataReader._pos
- _objc_retain_x20
CStrings:
+ "CPMS"
+ "CaptureTimestamp"
+ "Failed to create dispatch source for mach port\n"
+ "Failed to create stream ID to be sent to PPS\n"
+ "Failed to deserialize data read from shared memory\n"
+ "Failed to map the deserialized data to a dictionary %@ \n"
+ "Failed to receive IOSharedDataQueue enqueue mach msg return code: %d error string: %s\n"
+ "Malloc failure, unable to allocate memory for data buffer\n"
+ "TelemetrySharedQueueAllocStatus"
+ "There is no valid entry present in the shared queue\n"
+ "_setError"
+ "category"
+ "com.apple.peakpowermanagerd.telemetryqueue"
+ "countByEnumeratingWithState:objects:count:"
+ "data"
+ "dataWithBytesNoCopy:length:freeWhenDone:"
+ "dateWithTimeIntervalSince1970:"
+ "getBytes:length:"
+ "getBytes:range:"
+ "hasError"
+ "length"
+ "mutableCopy"
+ "numberWithInt:"
+ "objectForKeyedSubscript:"
+ "peakpowermanagerd could not allocate mach notification port\n"
+ "peakpowermanagerd failed to destroy mach port status code : %d\n"
+ "peakpowermanagerd failed to send mach port deallocated notification to kext\n"
+ "peakpowermanagerd failed to send timer notification to kext for data donation\n"
+ "peakpowermanagerd is not able to set notification port code %lu, return status %d\n"
+ "peakpowermanagerd is unable to dequeue from the shared buffer\n"
+ "peakpowermanagerd is unable to find CPMS kext service\n"
+ "peakpowermanagerd is unable to map shared memory(IODataQueueMemory) %u\n"
+ "peakpowermanagerd is unable to open connection to CPMS kext\n"
+ "peakpowermanagerd shared memory queue is NULL\n"
+ "position"
+ "propertyListWithData:options:format:error:"
+ "removeObjectForKey:"
+ "setDateFormat:"
+ "setObject:forKeyedSubscript:"
+ "setPosition:"
+ "stringFromDate:"
+ "unsignedLongLongValue"
+ "yyyy-MM-dd HH:mm:ss"

```
