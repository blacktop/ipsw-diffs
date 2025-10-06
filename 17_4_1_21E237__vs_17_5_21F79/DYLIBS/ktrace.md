## ktrace

> `/System/Library/PrivateFrameworks/ktrace.framework/ktrace`

```diff

-599.100.6.0.0
-  __TEXT.__text: 0xc8e5c
+599.120.3.0.0
+  __TEXT.__text: 0xc8f04
   __TEXT.__auth_stubs: 0x3050
   __TEXT.__objc_methlist: 0x160
   __TEXT.__const: 0x3201

   __TEXT.__eh_frame: 0x284c
   __TEXT.__objc_classname: 0x9b
   __TEXT.__objc_methname: 0xc4f
-  __TEXT.__objc_methtype: 0xfc1
+  __TEXT.__objc_methtype: 0xfea
   __TEXT.__objc_stubs: 0x7e0
   __DATA_CONST.__got: 0x3f0
   __DATA_CONST.__const: 0x1bb0

   - /usr/lib/swift/libswiftSystem.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 0584ED50-3FA1-38A5-846C-4727D50CCEFD
-  Functions: 4987
-  Symbols:   6610
+  UUID: 4C12A8E3-8D2B-3F47-B891-1EB09A5CC25C
+  Functions: 4989
+  Symbols:   6614
   CStrings:  1717
 
Symbols:
+ __session_handle_stackshot.cold.2
+ _ktrace_stackshot.cold.2
CStrings:
+ "v24@0:8^{ktrace_session=ii*B{ktrace_callback_list=ii^{ktrace_callback}}{ktrace_callback_list=ii^{ktrace_callback}}@?@?@?^{ktrace_session}@?{ktrace_callback_list=ii^{ktrace_callback}}{ktrace_callback_list=ii^{ktrace_callback}}@@IiIABABABABQQ@@@@@@b1b1b1b1b1b1b1b1b1b1@^^{?}^{?}iiiiiiiii^{kthmap}^{ktrace_uuid_map}^{KtraceSymbolicator}^{ktrace_chunk}QQ^{ktrace_machine}^{ktrace_cpus}{kteventnames=^{__CFDictionary}^{__CFDictionary}^{__CFArray}^{__CFArray}b1b1b1}^{vnode_path_map}^{thread_cputime_map}^{kpdecode_cursor}{mach_timebase_info=II}{kttimesync=QQ{mach_timebase_info=II}{timespec=qq}{timezone=ii}b1b1b1b1}QQQQQ{bt_params=dQQ}^{__CFSet}i^{__CFSet}iB^{__CFSet}^{ktrace_client}^v^{ktrace_file}^{ktrace_stream}^{ktrace_stream}^v^{ktrace_time_ringbuffer}^{ktrace_file}i@?@?@?@?**iQ{ktrace_event_matching=I[4Q]}{ktrace_event_matching=I[4Q]}i@{os_unfair_lock_s=I}b1b1b1}16"
- "v24@0:8^{ktrace_session=ii*B{ktrace_callback_list=ii^{ktrace_callback}}{ktrace_callback_list=ii^{ktrace_callback}}@?@?@?^{ktrace_session}@?@?{ktrace_callback_list=ii^{ktrace_callback}}@@IiIABABABABQQ@@@@@@b1b1b1b1b1b1b1b1b1b1@^^{?}^{?}iiiiiiiii^{kthmap}^{ktrace_uuid_map}^{KtraceSymbolicator}^{ktrace_chunk}QQ^{ktrace_machine}^{ktrace_cpus}{kteventnames=^{__CFDictionary}^{__CFDictionary}^{__CFArray}^{__CFArray}b1b1b1}^{vnode_path_map}^{thread_cputime_map}^{kpdecode_cursor}{mach_timebase_info=II}{kttimesync=QQ{mach_timebase_info=II}{timespec=qq}{timezone=ii}b1b1b1b1}QQQQQ{bt_params=dQQ}^{__CFSet}i^{__CFSet}iB^{__CFSet}^{ktrace_client}^v^{ktrace_file}^{ktrace_stream}^{ktrace_stream}^v^{ktrace_time_ringbuffer}^{ktrace_file}i@?@?@?@?**iQ{ktrace_event_matching=I[4Q]}{ktrace_event_matching=I[4Q]}i@{os_unfair_lock_s=I}b1b1b1}16"

```
