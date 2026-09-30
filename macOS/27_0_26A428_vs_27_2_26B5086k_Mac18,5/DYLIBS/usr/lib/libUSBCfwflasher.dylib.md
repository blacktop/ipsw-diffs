## libUSBCfwflasher.dylib

> `/usr/lib/libUSBCfwflasher.dylib`

```diff

-37.0.0.0.0
-  __TEXT.__text: 0x24d98
+40.0.0.0.0
+  __TEXT.__text: 0x24dc4
   __TEXT.__init_offsets: 0x18
   __TEXT.__objc_methlist: 0x4fc
-  __TEXT.__cstring: 0x90e6
-  __TEXT.__const: 0x1680
+  __TEXT.__cstring: 0x8efa
   __TEXT.__gcc_except_tab: 0x6e0
-  __TEXT.__oslogstring: 0x26d1
-  __TEXT.__unwind_info: 0xa18
+  __TEXT.__const: 0x1670
+  __TEXT.__oslogstring: 0x270f
+  __TEXT.__unwind_info: 0xa20
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__got: 0x108
   __AUTH_CONST.__const: 0x238
-  __AUTH_CONST.__cfstring: 0x3160
+  __AUTH_CONST.__cfstring: 0x3020
   __AUTH_CONST.__objc_const: 0x720
   __AUTH_CONST.__weak_auth_got: 0x20
   __AUTH_CONST.__objc_intobj: 0x30

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 480
-  Symbols:   1075
-  CStrings:  1221
+  Functions: 482
+  Symbols:   1076
+  CStrings:  1213
 
Symbols:
+ GCC_except_table259
+ __ZNSt3__16vectorI20bypass_config_desc_tNS_9allocatorIS1_EEE16__destroy_vectorclB9nqe220106Ev
+ __ZNSt3__16vectorI20bypass_config_desc_tNS_9allocatorIS1_EEE5clearB9nqe220106Ev
- GCC_except_table16
- GCC_except_table248
CStrings:
+ "3679.40.26b70"
+ "AstrisArmProbeServer-3679.40.26~70 (FizzBSeed tools)"
+ "PongoSWD"
+ "{%s} probe advertised csv_maxbuf=%u > client max %u; clamping"
- "3679.0.30b209"
- "AstrisArmProbeServer-3679.0.30~209 (Fizz tools)"
- "Attempting to un-bork firmware... status = 0x%X"
- "Command set required to update this HW is not available.  Update process is forced to abort."
- "Failed to write \"MAGIC\" data or send memory modify command. status=0x%02x"
- "Firmware appears to be within the range known to have a broken update path.  Attempting to fix"
- "MEMm response: %02X %02X %02X %02X"
- "Memory modify failed and out of retries.  Aborting as retries were exhausted"
- "Modifying memory..."
- "Retrying memory modify command as it looks like it didn't execute..."
- "Should think SFWu now usable"
- "useBorkedSFWWorkarounds: %s"
```
