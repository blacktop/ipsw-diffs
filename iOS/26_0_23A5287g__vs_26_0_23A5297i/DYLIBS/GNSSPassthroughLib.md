## GNSSPassthroughLib

> `/System/Library/Extensions/AppleSPU.kext/PlugIns/GNSSPassthroughLib.plugin/GNSSPassthroughLib`

```diff

-1046.0.3.0.0
-  __TEXT.__text: 0x15bc
-  __TEXT.__auth_stubs: 0x2e0
+1046.0.5.0.0
+  __TEXT.__text: 0x1908
+  __TEXT.__auth_stubs: 0x3a0
   __TEXT.__const: 0x80
   __TEXT.__gcc_except_tab: 0xac
-  __TEXT.__cstring: 0x72
-  __TEXT.__oslogstring: 0xa5
-  __TEXT.__unwind_info: 0x158
-  __DATA_CONST.__got: 0x30
-  __AUTH_CONST.__auth_got: 0x178
-  __AUTH.__data: 0x78
+  __TEXT.__cstring: 0x124
+  __TEXT.__oslogstring: 0xc1
+  __TEXT.__unwind_info: 0x168
+  __DATA_CONST.__got: 0x48
+  __DATA_CONST.__const: 0x20
+  __AUTH_CONST.__auth_got: 0x1d8
+  __AUTH_CONST.__cfstring: 0x80
+  __AUTH.__data: 0x80
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: D1BDE361-139C-3659-8A08-3F9D229F1A8F
-  Functions: 59
-  Symbols:   91
-  CStrings:  12
+  UUID: 0C596EE8-B88E-3EE6-AB91-3A5BC0DCD02E
+  Functions: 63
+  Symbols:   109
+  CStrings:  23
 
Symbols:
+ _CFDataGetBytes
+ _CFDataGetLength
+ _CFDictionaryAddValue
+ _CFDictionaryCreateMutable
+ _CFNumberCreate
+ _CFPropertyListCreateData
+ _IODataQueueDataAvailable
+ __NSConcreteStackBlock
+ __ZN15GNSSPassthrough11PendingDataEv
+ __ZN15GNSSPassthrough24_setupSysdiagnoseHandlerEv
+ ___CFConstantStringClassReference
+ _dispatch_get_global_queue
+ _kCFTypeDictionaryKeyCallBacks
+ _kCFTypeDictionaryValueCallBacks
+ _mach_continuous_time
+ _malloc_type_calloc
+ _os_state_add_handler
+ _os_state_remove_handler
Functions:
~ __ZN15GNSSPassthrough12_dequeueDataEv : 124 -> 144
~ __ZN15GNSSPassthroughC2EPK13__CFAllocator : 272 -> 280
~ __ZN15GNSSPassthroughD2Ev : 140 -> 152
~ __ZN15GNSSPassthrough5StartEPK14__CFDictionaryj : 292 -> 300
+ __ZN15GNSSPassthrough4StopEv
+ __ZN15GNSSPassthrough11PendingDataEv
~ __ZN15GNSSPassthrough14_dequeueEventsEv : 116 -> 136
+ sub_248e4792c
CStrings:
+ "DequeueTime"
+ "Error adding state handler."
+ "EventTime"
+ "GNSSPassthrough Client State"
+ "^{os_state_data_s=I(?=b32I){os_state_data_decoder_s=[64c][64c]}[64c][0C]}16@?0^{os_state_hints_s=I*II}8"
+ "eventCount"
+ "packetCount"

```
