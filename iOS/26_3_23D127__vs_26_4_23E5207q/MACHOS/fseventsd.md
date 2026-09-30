## fseventsd

> `/usr/libexec/fseventsd`

```diff

-1407.80.2.0.0
-  __TEXT.__text: 0x18a64
+1413.100.5.0.1
+  __TEXT.__text: 0x17638
   __TEXT.__auth_stubs: 0xdd0
-  __TEXT.__cstring: 0xe9b
-  __TEXT.__const: 0x148
-  __TEXT.__oslogstring: 0x3156
+  __TEXT.__cstring: 0xee0
+  __TEXT.__const: 0x158
+  __TEXT.__oslogstring: 0x31a7
   __TEXT.__unwind_info: 0x380
   __DATA_CONST.__auth_got: 0x6e8
   __DATA_CONST.__got: 0xb0
   __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__const: 0x318
-  __DATA_CONST.__cfstring: 0x4a0
+  __DATA_CONST.__cfstring: 0x4c0
   __DATA.__data: 0x232
   __DATA.__bss: 0x468
   __DATA.__common: 0x2248

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 0DCDA4AE-626E-399B-95D2-338704C145A9
-  Functions: 393
+  UUID: 0DB556EC-617C-3677-895A-4193B7935E1B
+  Functions: 402
   Symbols:   247
-  CStrings:  502
+  CStrings:  506
 
CStrings:
+ "\t\tnum_events[%llu] allocated_bytes[%llu] user_time[%.2f] system_time[%.2f] peak_cpu_usage[%d]\n"
+ "%s: dev(%d) not available or no log files on disk"
+ "could not open [%s]<<%s>> (%s)\n"
+ "implementation_purge_events_for_device_up_to_event_id"
+ "log dir [%s]%s does not match path %s.  bailing out."
+ "peak_cpu_usage"
+ "scan_old: bailing out because device mounted @ [%s]%s has dls %p and dls->fci %p"
- "\t\tnum_events[%llu] allocated_bytes[%llu] user_time[%.2f] system_time[%.2f]\n"
- "could not open <<%s>> (%s)\n"
- "log dir %s does not match path %s.  bailing out."
- "scan_old: bailing out because device mounted @ %s has dls %p and dls->fci %p"

```
