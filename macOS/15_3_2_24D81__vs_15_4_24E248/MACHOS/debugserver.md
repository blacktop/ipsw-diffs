## debugserver

> `/usr/libexec/rosetta/debugserver`

```diff

-342.0.0.0.0
-  __TEXT.__text: 0x3e564
-  __TEXT.__auth_stubs: 0x1030
+349.0.0.0.0
+  __TEXT.__text: 0x3e800
+  __TEXT.__auth_stubs: 0x1040
   __TEXT.__objc_stubs: 0xc0
   __TEXT.__init_offsets: 0xc
-  __TEXT.__gcc_except_tab: 0x60c
-  __TEXT.__const: 0x168
-  __TEXT.__cstring: 0xc400
-  __TEXT.__objc_classname: 0x1
+  __TEXT.__const: 0x188
+  __TEXT.__gcc_except_tab: 0x5e4
+  __TEXT.__cstring: 0xc98c
   __TEXT.__objc_methname: 0x60
-  __TEXT.__unwind_info: 0x890
-  __DATA_CONST.__auth_got: 0x828
-  __DATA_CONST.__got: 0xe0
+  __TEXT.__unwind_info: 0x860
+  __DATA_CONST.__auth_got: 0x830
+  __DATA_CONST.__got: 0xf0
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x5a08
+  __DATA_CONST.__const: 0x5af8
   __DATA_CONST.__cfstring: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x30
-  __DATA.__data: 0x12e4
-  __DATA.__bss: 0x400eb8
+  __DATA.__crash_info: 0x40
+  __DATA.__data: 0x12dc
+  __DATA.__bss: 0x400e78
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/Security.framework/Versions/A/Security

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8ACD43F1-A9A1-382C-8644-0BF61A52ABC2
-  Functions: 609
-  Symbols:   323
-  CStrings:  1776
+  UUID: F77975FF-D030-34BD-B0AA-1B13F314F798
+  Functions: 597
+  Symbols:   326
+  CStrings:  1850
 
Symbols:
+ _CFPropertyListCreateData
+ __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEElsEb
+ __ZNSt3__114basic_iostreamIcNS_11char_traitsIcEEED2Ev
+ __ZTTNSt3__118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE
+ __ZTVNSt3__118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE
+ _sysctlnametomib
+ _thread_abort_safely
- _CFPropertyListCreateXMLData
- _asl_new
- _asl_set
- _asl_vlog
CStrings:
+ " "
+ "%s - Failed to attach to pid %d, AttachForDebug() unable to ptrace(PT_ATTACHEXC)"
+ "%s - process %d is already being debugged by pid %d"
+ "/AppleInternal/Library/BuildRoots/28f4b4c9-00e0-11f0-8e4b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Rosetta/src/debugserver/RNBRemote.cpp"
+ "::mach_msg ( msg->{bits = %#x, size = %u remote_port = %#x, local_port = %#x, reserved = 0x%x, id = 0x%x}, option = %#x, send_size = %u, rcv_size = %u, rcv_name = %#x, timeout = %u, notify = %#x)"
+ "::mach_msg ( msg->{bits = %#x, size = %u remote_port = %#x, local_port = %#x, reserved = 0x%x, id = 0x%x}, option = %#x, send_size = 0, rcv_size = %llu, rcv_name = %#x, timeout = %u, notify = %#x)"
+ "DNBArchImplARM64::GetHardwareWatchpointHit() slot: %u %s"
+ "DNBArchImplARM64::GetHardwareWatchpointHit() slot: %u (addr = 0x%llx, WCR = 0x%llx)"
+ "DNBArchImplARM64::GetHardwareWatchpointHit() slot: %u matched BAS"
+ "DNBArchImplARM64::GetHardwareWatchpointHit() slot: %u matched MASK ignoring %u low bits"
+ "DNBArchMachARM64::EnableHardwareWatchpoint() using %zu hardware watchpoints"
+ "DNBArchMachARM64::ReenableHardwareWatchpoint_helper( %u ) - WVR%u = 0x%8.8llx  WCR%u = 0x%8.8llx"
+ "DNBArchMachARM64::SetBASWatchpoint() SetDBGState() => 0x%8.8x."
+ "DNBArchMachARM64::SetBASWatchpoint() adding watchpoint on address 0x%llx with control register value 0x%x"
+ "DNBArchMachARM64::SetBASWatchpoint() set hardware register %d to BAS watchpoint aligned start address 0x%llx, watch region start offset %lld, number of bytes %zu"
+ "DNBArchMachARM64::SetBASWatchpoint(): All hardware resources (%u) are in use."
+ "DNBArchMachARM64::SetMASKWatchpoint() SetDBGState() => 0x%8.8x."
+ "DNBArchMachARM64::SetMASKWatchpoint() adding watchpoint on address 0x%llx with control register value 0x%llx"
+ "DNBArchMachARM64::SetMASKWatchpoint() set hardware register %d to MASK watchpoint aligned start address 0x%llx, aligned size %zu"
+ "DNBArchMachARM64::SetMASKWatchpoint(): All hardware resources (%u) are in use."
+ "DNBArchMachARM64::ThreadWillResume() DisableHardwareWatchpoint(%d) called"
+ "DNBArchMachARM64::ThreadWillResume() failed to enable single step"
+ "DNBArchMachARM64::ThreadWillResume() succeeded to enable single step"
+ "E01"
+ "E04"
+ "E89"
+ "E96"
+ "ESR watchpoint fields parsed: iss = 0x%x, wpt = %u, wptv = %d, wpf = %d, fnp = %d, vncr = %d, fnv = %d, cm = %d, wnr = %d, dfsc = 0x%x"
+ "Failed to attach to pid %d, LaunchForDebug() unable to ptrace(PT_ATTACHEXC)"
+ "Interrupted by packet thread shutdown while waiting for %s to appear.\n"
+ "Interrupted by packet while waiting for '%s' to appear.\n"
+ "LC_AOT_METADATA command is wrong size"
+ "LC_BUILD_VERSION command is wrong size"
+ "LC_CODE_SIGNATURE command is wrong size"
+ "LC_MAIN command is wrong size"
+ "LC_SOURCE_VERSION command is wrong size"
+ "LC_UUID command is wrong size"
+ "LC_VERSION_MIN_MACOSX command is wrong size"
+ "Mach-O has too many segments"
+ "Mach-O header sizeofcmds is incorrect"
+ "MachProcess::RefineWatchpointStopInfo mach exception addr 0x%llx but FAR register has value 0x%llx"
+ "MachProcess::RefineWatchpointStopInfo mach exception addr 0x%llx moved in to nearest watchpoint, 0x%llx-0x%llx"
+ "QEnableErrorStrings"
+ "Tell debugserver it can append descriptive error messages in replies."
+ "Watchpoint Valid field true, finding startaddr of watchpoint %d"
+ "[LaunchAttach] (%d) MachProcess::AttachForDebug pid %d is already being debugged by pid %d"
+ "attached to process, but could not pause execution; attach failed"
+ "com.apple.security.get-task-allow"
+ "description:"
+ "ds"
+ "es"
+ "executable is inconsistent about dynamic linking"
+ "failed to get the task for process %i: %s"
+ "failed to get the task for process %i: this likely means the process cannot be debugged, either because it's a system process or because the process is missing the %s entitlement."
+ "gsbase"
+ "integer overflow in aot metadata load command fragment list"
+ "integer overflow in aot metadata load x86 image path"
+ "integer overflow in section boundaries"
+ "invalid LC_MAIN entry point"
+ "invalid LC_SEGMENT_64 command size"
+ "invalid LC_UNIXTHREAD architecture"
+ "invalid Mach-O magic"
+ "invalid cpu type/subtype"
+ "invalid entry point"
+ "invalid segment permissions"
+ "invalid state size"
+ "is BAS watchpoint"
+ "is MASK watchpoint"
+ "load commands are mapped by multiple segments"
+ "load commands too large"
+ "malformed LC_UNIXTHREAD command"
+ "malformed load command"
+ "me_watch_addr"
+ "me_watch_addr:"
+ "multiple LC_LOAD_SIGNATURE commands"
+ "multiple LC_UUID commands"
+ "multiple __LINKEDIT segments"
+ "multiple load commands specify entry points"
+ "no segment mapping load commands"
+ "no such process"
+ "out-of-bounds Mach-O header"
+ "out-of-bounds load command"
+ "overlapping Mach-O segments"
+ "ptrsize:4;"
+ "qEcho+;native-signals+;"
+ "qXfer:features:read+;PacketSize="
+ "reason:watchpoint;"
+ "report_load_commands"
+ "segment partially maps load commands"
+ "sizeof(msg.thread_get_state_response.state) >= state_size"
+ "ss"
+ "st0"
+ "st1"
+ "st2"
+ "st3"
+ "st4"
+ "st5"
+ "st6"
+ "st7"
+ "sysctl.proc_cputype"
+ "thread_get_state signed regs \n   fp=%16.16llx\n   lr=%16.16llx\n   sp=%16.16llx\n   pc=%16.16llx"
+ "unsupported Mach-O filetype"
+ "watch_addr:"
+ "watchpoint"
+ "wp_esr_cm:"
+ "wp_esr_dfsc:"
+ "wp_esr_fnp:"
+ "wp_esr_fnv:"
+ "wp_esr_iss:"
+ "wp_esr_vncr:"
+ "wp_esr_wnr:"
+ "wp_esr_wpf:"
+ "wp_esr_wpt:"
+ "wp_esr_wptv:"
+ "wp_hw_idx:"
+ "xros"
+ "xrossimulator"
- "%s - process %d is already being debugged"
- "*"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/Rosetta/src/debugserver/RNBRemote.cpp"
- "1"
- "::mach_msg ( msg->{bits = %#x, size = %u reply_port = %#x, local_port = %#x, reserved = 0x%x, id = 0x%x}, option = %#x, send_size = %u, rcv_size = %u, rcv_name = %#x, timeout = %u, notify = %#x)"
- "::mach_msg ( msg->{bits = %#x, size = %u reply_port = %#x, local_port = %#x, reserved = 0x%x, id = 0x%x}, option = %#x, send_size = 0, rcv_size = %llu, rcv_name = %#x, timeout = %u, notify = %#x)"
- "::thread_get_state (0x%4.4x, %u, &gpr, %u) => 0x%8.8x\n\trax = %16.16llx rbx = %16.16llx rcx = %16.16llx rdx = %16.16llx\n\trdi = %16.16llx rsi = %16.16llx rbp = %16.16llx rsp = %16.16llx\n\t r8 = %16.16llx  r9 = %16.16llx r10 = %16.16llx r11 = %16.16llx\n\tr12 = %16.16llx r13 = %16.16llx r14 = %16.16llx r15 = %16.16llx\n\trip = %16.16llx\n\tflg = %16.16llx  cs = %16.16llx  fs = %16.16llx  gs = %16.16llx"
- "::thread_set_state (0x%4.4x, %u, &gpr, %u) => 0x%8.8x\n\trax = %16.16llx rbx = %16.16llx rcx = %16.16llx rdx = %16.16llx\n\trdi = %16.16llx rsi = %16.16llx rbp = %16.16llx rsp = %16.16llx\n\t r8 = %16.16llx  r9 = %16.16llx r10 = %16.16llx r11 = %16.16llx\n\tr12 = %16.16llx r13 = %16.16llx r14 = %16.16llx r15 = %16.16llx\n\trip = %16.16llx\n\tflg = %16.16llx  cs = %16.16llx  fs = %16.16llx  gs = %16.16llx"
- "BVR%-2u/BCR%-2u = { 0x%8.8llx, 0x%8.8llx } WVR%-2u/WCR%-2u = { 0x%8.8llx, 0x%8.8llx }"
- "DNBArchImplX86_64::DisableHardwareWatchpoint( %u ) - WVR%u = 0x%8.8llx  WCR%u = 0x%8.8llx"
- "DNBArchImplX86_64::EnableHardwareWatchpoint() SetDBGState() => 0x%8.8x."
- "DNBArchImplX86_64::EnableHardwareWatchpoint() adding watchpoint on address 0x%llx with control register value 0x%x"
- "DNBArchImplX86_64::EnableHardwareWatchpoint(): All hardware resources (%u) are in use."
- "DNBArchImplX86_64::EnableHardwareWatchpoint(addr = 0x%8.8llx, size = %zu) needs two hardware watchpoints slots to monitor"
- "DNBArchImplX86_64::EnableHardwareWatchpoint(addr = 0x%llx, size = %llu, read = %u, write = %u)"
- "DNBArchImplX86_64::GetHardwareWatchpointHit() GetDBGState() => 0x%8.8x."
- "DNBArchImplX86_64::GetHardwareWatchpointHit() addr = 0x%llx"
- "DNBArchImplX86_64::GetHardwareWatchpointHit() slot: %u (addr = 0x%llx; byte_mask = 0x%x)"
- "DNBArchImplX86_64::SetDBGState failed to set debug control register state: 0x%8.8x."
- "DNBArchMachARM64::EnableHardwareWatchpoint( %u ) - WVR%u = 0x%8.8llx  WCR%u = 0x%8.8llx"
- "DNBArchMachARM64::EnableHardwareWatchpoint() SetDBGState() => 0x%8.8x."
- "DNBArchMachARM64::EnableHardwareWatchpoint() adding watchpoint on address 0x%llx with control register value 0x%x"
- "DNBArchMachARM64::EnableHardwareWatchpoint(): All hardware resources (%u) are in use."
- "DNBArchMachARM64::EnableHardwareWatchpoint(addr = 0x%8.8llx, size = %zu) needs two hardware watchpoints slots to monitor"
- "DNBArchMachARM::NotifyException It is a linked watchpoint; rewritten to index %d addr 0x%llx"
- "DNBArchMachARM::NotifyException watchpoint %d was hit on address 0x%llx"
- "DNBArchMachARM::ThreadWillResume() DisableHardwareWatchpoint(%d) called"
- "DNBArchMachARM::ThreadWillResume() failed to enable single step"
- "DNBArchMachARM::ThreadWillResume() succeeded to enable single step"
- "E"
- "E96;"
- "ERROR: Could not identify the number of HW watchpoints supported "
- "Sender"
- "[LaunchAttach] (%d) MachProcess::AttachForDebug pid %d is already being debugged"
- "com.apple.rosetta.debugserver-%s"
- "debugserver will use ASL for internal logging."
- "failed to get the task for process %i"
- "failed to get the task for process %i (%s)"
- "image_count"
- "image_list_address"
- "minsize:"
- "no such process."
- "qXfer:features:read+;PacketSize=%x;qEcho+;native-signals+"

```
