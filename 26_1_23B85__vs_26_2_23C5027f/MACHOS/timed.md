## timed

> `/usr/libexec/timed`

```diff

-334.0.16.0.0
-  __TEXT.__text: 0x1800c
-  __TEXT.__auth_stubs: 0xba0
+334.0.16.1.0
+  __TEXT.__text: 0x1810c
+  __TEXT.__auth_stubs: 0xb90
   __TEXT.__objc_stubs: 0x2560
   __TEXT.__objc_methlist: 0xd6c
   __TEXT.__const: 0x278
   __TEXT.__objc_methname: 0x2397
-  __TEXT.__cstring: 0x1fce
+  __TEXT.__cstring: 0x1fe3
   __TEXT.__objc_classname: 0x11d
   __TEXT.__objc_methtype: 0x53e
   __TEXT.__oslogstring: 0x2ae2
-  __TEXT.__gcc_except_tab: 0xe8
-  __TEXT.__unwind_info: 0x5f0
-  __DATA_CONST.__auth_got: 0x5e0
+  __TEXT.__gcc_except_tab: 0xdc
+  __TEXT.__unwind_info: 0x5e8
+  __DATA_CONST.__auth_got: 0x5d8
   __DATA_CONST.__got: 0x1b0
   __DATA_CONST.__const: 0xdd0
   __DATA_CONST.__cfstring: 0x2a40

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  UUID: 0B4DD206-73E6-38F7-ACB5-1366C6BFCEA1
-  Functions: 570
-  Symbols:   254
+  UUID: 3593D10D-0490-3E79-B26A-78BD45D390B1
+  Functions: 574
+  Symbols:   253
   CStrings:  1627
 
Symbols:
- _memcpy
CStrings:
+ "-[TMBackgroundNtpSource _fetchTime]"
+ "334.0.16.1"
+ "best_index > -1 && best_index < NTP_DESIRED_NUM_SERVERS"
- "-[TMBackgroundNtpSource _fetchTime]_block_invoke"
- "334.0.16"
- "machResult > kMachStart"

```
