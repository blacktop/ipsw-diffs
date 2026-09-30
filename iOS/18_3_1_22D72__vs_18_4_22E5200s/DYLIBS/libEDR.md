## libEDR

> `/System/Library/PrivateFrameworks/libEDR.framework/libEDR`

```diff

-63.0.0.0.0
-  __TEXT.__text: 0x10a50
+64.0.0.0.0
+  __TEXT.__text: 0x106c4
   __TEXT.__auth_stubs: 0x890
-  __TEXT.__const: 0x1850
-  __TEXT.__gcc_except_tab: 0x74c
+  __TEXT.__const: 0x1838
+  __TEXT.__gcc_except_tab: 0x7a8
   __TEXT.__oslogstring: 0xe25
-  __TEXT.__cstring: 0x1e00
-  __TEXT.__unwind_info: 0x4f8
+  __TEXT.__cstring: 0x1e2f
+  __TEXT.__unwind_info: 0x4f0
   __TEXT.__objc_classname: 0x1
   __TEXT.__objc_methname: 0xab
   __TEXT.__objc_stubs: 0xe0

   __DATA.__data: 0x4
   __DATA.__bss: 0x9
   __DATA_DIRTY.__data: 0x98
-  __DATA_DIRTY.__bss: 0x21a0
+  __DATA_DIRTY.__bss: 0x2190
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 222
+  Functions: 233
   Symbols:   199
   CStrings:  363
 
Symbols:
+ _mach_port_destruct
- __ZNSt3__120__throw_system_errorEiPKc
CStrings:
+ "EDR - %s: Not using send-once right for message marked as kFlagSyncReq\n"
+ "EDR - %s: fail to create reply port  => %s (%d) \n"
+ "EDR - %s: fail to destroy reply port  => %s (%d) \n"
- "EDR - %s: data size %d exceeds message data size %ud\n"
- "server_remove_client_with_no_send_right"
- "unique_lock::unlock: not locked"

```
