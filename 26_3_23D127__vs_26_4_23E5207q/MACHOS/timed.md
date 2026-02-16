## timed

> `/usr/libexec/timed`

```diff

-334.0.16.1.0
-  __TEXT.__text: 0x18120
-  __TEXT.__auth_stubs: 0xb90
+334.0.16.3.0
+  __TEXT.__text: 0x176d8
+  __TEXT.__auth_stubs: 0xba0
   __TEXT.__objc_stubs: 0x2560
   __TEXT.__objc_methlist: 0xd6c
-  __TEXT.__const: 0x278
+  __TEXT.__const: 0x280
   __TEXT.__objc_methname: 0x2397
-  __TEXT.__cstring: 0x1fe3
+  __TEXT.__cstring: 0x1fd0
   __TEXT.__objc_classname: 0x11d
   __TEXT.__objc_methtype: 0x53e
   __TEXT.__oslogstring: 0x2ae2
-  __TEXT.__gcc_except_tab: 0xdc
-  __TEXT.__unwind_info: 0x5e8
-  __DATA_CONST.__auth_got: 0x5d8
+  __TEXT.__gcc_except_tab: 0xe8
+  __TEXT.__unwind_info: 0x610
+  __DATA_CONST.__auth_got: 0x5e0
   __DATA_CONST.__got: 0x1b0
   __DATA_CONST.__const: 0xdd0
   __DATA_CONST.__cfstring: 0x2a40

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  UUID: 49951B64-9F29-3115-8911-C3E2418328EB
-  Functions: 574
-  Symbols:   253
+  UUID: 41CC93F1-898C-3A98-A893-41977E21817F
+  Functions: 602
+  Symbols:   254
   CStrings:  1627
 
Symbols:
+ _memcpy
CStrings:
+ "-[TMBackgroundNtpSource _fetchTime]_block_invoke"
+ "334.0.16.3"
+ "machResult > kMachStart"
- "-[TMBackgroundNtpSource _fetchTime]"
- "334.0.16.1"
- "best_index > -1 && best_index < NTP_DESIRED_NUM_SERVERS"

```
