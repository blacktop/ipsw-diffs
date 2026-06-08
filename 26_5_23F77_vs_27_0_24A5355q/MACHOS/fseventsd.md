## fseventsd

> `/usr/libexec/fseventsd`

```diff

-1413.100.6.0.0
-  __TEXT.__text: 0x17638
+1430.0.0.0.0
+  __TEXT.__text: 0x16d4c
   __TEXT.__auth_stubs: 0xdd0
   __TEXT.__cstring: 0xee0
-  __TEXT.__const: 0x158
-  __TEXT.__oslogstring: 0x31a7
-  __TEXT.__unwind_info: 0x380
+  __TEXT.__const: 0x168
+  __TEXT.__oslogstring: 0x326a
+  __TEXT.__unwind_info: 0x360
+  __DATA_CONST.__const: 0x318
+  __DATA_CONST.__cfstring: 0x4c0
   __DATA_CONST.__auth_got: 0x6e8
   __DATA_CONST.__got: 0xb0
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x318
-  __DATA_CONST.__cfstring: 0x4c0
   __DATA.__data: 0x232
   __DATA.__bss: 0x468
   __DATA.__common: 0x2248

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 6B35C9AA-9EBF-3C07-BB9E-CFB680E1069C
-  Functions: 402
+  UUID: 45BFB51F-3742-386F-A8EA-7F39263C07A2
+  Functions: 392
   Symbols:   247
-  CStrings:  506
+  CStrings:  508
 
CStrings:
+ "%s: new checksum mis-match: file 0x%.8x, calculated 0x%.8x in index %d"
+ "get_last_event_id: new checksum mis-match: file 0x%.8x, calculated 0x%.8x in file %s"
+ "get_last_event_id: old checksum mis-match: file 0x%.8x, calculated 0x%.8x in file %s"
+ "process_disk_event_buf: magic is wrong (0x%.8x != (0x%.8x <OR> 0x%.8x <OR> 0x%.8x)) - buflen(%d) index(%d) dev(%d)"
+ "process_disk_event_buf: old checksum mis-match: file 0x%.8x, calculated 0x%.8x"
- "get_last_event_id: checksum mis-match: file 0x%.8x, calculated 0x%.8x in file %s"
- "process_disk_event_buf: checksum mis-match: file 0x%.8x, calculated 0x%.8x"
- "process_disk_event_buf: magic is wrong (0x%.8x != (0x%.8x <OR> 0x%.8x <OR> 0x%.8x))"

```
