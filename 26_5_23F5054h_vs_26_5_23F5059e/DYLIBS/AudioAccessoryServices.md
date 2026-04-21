## AudioAccessoryServices

> `/System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices`

```diff

-35.11.0.0.0
-  __TEXT.__text: 0x4a100
+35.12.0.0.0
+  __TEXT.__text: 0x4a314
   __TEXT.__auth_stubs: 0x8a0
-  __TEXT.__objc_methlist: 0x5a24
+  __TEXT.__objc_methlist: 0x5a3c
   __TEXT.__const: 0x2e0
-  __TEXT.__gcc_except_tab: 0x16d0
-  __TEXT.__cstring: 0xd6da
-  __TEXT.__unwind_info: 0x1630
+  __TEXT.__gcc_except_tab: 0x16f8
+  __TEXT.__cstring: 0xd7b6
+  __TEXT.__unwind_info: 0x1640
   __TEXT.__objc_classname: 0x705
   __TEXT.__objc_methname: 0xc672
   __TEXT.__objc_methtype: 0x167c

   - /System/Library/PrivateFrameworks/Sharing.framework/Sharing
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 98B6C65A-0BC2-3E31-B902-86392C961A0B
-  Functions: 2484
-  Symbols:   7418
-  CStrings:  4436
+  UUID: 3461FBFB-2114-3708-B892-856ADE34AC36
+  Functions: 2489
+  Symbols:   7429
+  CStrings:  4441
 
Symbols:
+ -[AASystemStateMonitor _reset]
+ -[AASystemStateMonitor _reset].cold.1
+ -[AASystemStateMonitor aaServicesRequireReset]
+ -[AASystemStateMonitor aaServicesRequireReset].cold.1
+ GCC_except_table21
+ ___30-[AASystemStateMonitor _reset]_block_invoke
+ ___block_literal_global.143
+ ___block_literal_global.163
- ___block_literal_global.140
- ___block_literal_global.157
CStrings:
+ "-[AASystemStateMonitor _reset]"
+ "-[AASystemStateMonitor aaServicesRequireReset]"
+ "AASystemStateMonitor reset required, as messages might have been dropped"
+ "AASystemStateMonitor: Reset complete"
+ "AASystemStateMonitor: Resetting"

```
