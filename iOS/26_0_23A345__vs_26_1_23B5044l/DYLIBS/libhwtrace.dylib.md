## libhwtrace.dylib

> `/usr/lib/libhwtrace.dylib`

```diff

-133.0.25.0.0
-  __TEXT.__text: 0x21f5fc
-  __TEXT.__auth_stubs: 0x16a0
-  __TEXT.__const: 0x1ae530
-  __TEXT.__cstring: 0x19d8b
+133.40.6.0.0
+  __TEXT.__text: 0x21899c
+  __TEXT.__auth_stubs: 0x16b0
+  __TEXT.__const: 0x1ae5c0
+  __TEXT.__cstring: 0x19d12
   __TEXT.__oslogstring: 0x6a5
   __TEXT.__gcc_except_tab: 0x308
-  __TEXT.__unwind_info: 0x2b90
+  __TEXT.__unwind_info: 0x2b78
   __TEXT.__eh_frame: 0x98
   __TEXT.__objc_methname: 0xa9
   __TEXT.__objc_stubs: 0x120
   __DATA_CONST.__got: 0xa0
-  __DATA_CONST.__const: 0x48b38
+  __DATA_CONST.__const: 0x48af0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x48
-  __AUTH_CONST.__auth_got: 0xb60
-  __AUTH_CONST.__const: 0x6618
-  __AUTH_CONST.__cfstring: 0x320
+  __AUTH_CONST.__auth_got: 0xb68
+  __AUTH_CONST.__const: 0x65f8
+  __AUTH_CONST.__cfstring: 0x300
   __AUTH.__data: 0x18
   __DATA.__data: 0x68
   __DATA.__bss: 0xaa0

   - /usr/lib/libncurses.5.4.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 1026ADCD-FD8D-37A6-AF70-5D5A741AB9B1
-  Functions: 4313
-  Symbols:   574
-  CStrings:  5716
+  UUID: 6A6E1AEA-A248-31D4-9C3E-91BB8823CDFA
+  Functions: 4308
+  Symbols:   575
+  CStrings:  5706
 
Symbols:
+ _dyld_image_content_for_section
CStrings:
+ "\n         +--------------------------------------------------------------------+\n         | Support for PIO-based configuration of cputrace on XNU is          |\n         | deprecated in favor of a safer, more performant, and feature-rich  |\n         | replacement through a driver. PIO support has now been removed.    |\n         | Please pass -driver=1 or --CPUTrace:driver=1 to migrate now.       |\n         | Reach out on Slack to share feedback or ask questions. See:        |\n         | 'at' dot 'apple.com/ariadne-cputrace' for migration help, some     |\n         | required bootargs have changed and SIP no longer must be disabled. |\n         +--------------------------------------------------------------------+\n    "
+ " This explains why tracing is restricted."
+ ", kern.csw="
+ "... Detected that amfi_unrestrict_task_for_pid=1 is not present in boot-args."
+ "Address tracing requires a driver"
+ "Error verifyPortMatchesTarget(pid_t, task_read_t)"
+ "libhwtrace @ tag libhwtrace-133.40.6"
+ "libhwtrace @ tag libhwtrace-133.40.6\n"
- "\n         +--------------------------------------------------------------------+\n         | Support for PIO-based configuration of cputrace on XNU is          |\n         | deprecated in favor of a safer, more performant, and feature-rich  |\n         | replacement through a driver. PIO support will be removed in an    |\n         | upcoming SU: pass -driver=1 or --CPUTrace:driver=1 to migrate now. |\n         | Reach out on Slack to share feedback or ask questions. See:        |\n         | 'at' dot 'apple.com/ariadne-cputrace' for migration help, some     |\n         | required bootargs have changed and SIP no longer must be disabled. |\n         +--------------------------------------------------------------------+\n    "
- " (requires H16G+)"
- ") failed, "
- "... Detected that amfi_unrestrict_task_for_pid=1 is not present in boot-args, so tracing policy is not relaxed."
- ": write failed"
- "AppleHWAccess::write_32("
- "Could not find cpm-impl-reg"
- "HID_PROD_TRC_CORE_CFG_EL1"
- "PROD_TRACE_EN_GL2"
- "PROD_TRC_CORE_CFG_EL2"
- "PROD_TRC_CTL_EL2"
- "cpm-impl-reg"
- "libhwtrace @ tag libhwtrace-133.0.25"
- "libhwtrace @ tag libhwtrace-133.0.25\n"
- "msr("
- "resetTraceState"
- "write_32("

```
