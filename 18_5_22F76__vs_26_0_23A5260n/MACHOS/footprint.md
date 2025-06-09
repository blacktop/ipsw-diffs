## footprint

> `/usr/bin/footprint`

```diff

-281.100.5.0.0
-  __TEXT.__text: 0x19db4
-  __TEXT.__auth_stubs: 0xc30
-  __TEXT.__objc_stubs: 0x2260
-  __TEXT.__objc_methlist: 0x117c
+301.0.0.0.0
+  __TEXT.__text: 0x1ac8c
+  __TEXT.__auth_stubs: 0xc50
+  __TEXT.__objc_stubs: 0x22a0
+  __TEXT.__objc_methlist: 0x115c
+  __TEXT.__cstring: 0x330a
+  __TEXT.__objc_classname: 0x206
+  __TEXT.__objc_methtype: 0x7ab
   __TEXT.__const: 0xe8
-  __TEXT.__gcc_except_tab: 0x3c8
-  __TEXT.__cstring: 0x2fee
-  __TEXT.__objc_methname: 0x22f1
-  __TEXT.__objc_classname: 0x1fa
-  __TEXT.__objc_methtype: 0x79e
+  __TEXT.__gcc_except_tab: 0x3d4
+  __TEXT.__objc_methname: 0x231a
   __TEXT.__ustring: 0xd0
   __TEXT.__oslogstring: 0x21
   __TEXT.__unwind_info: 0x480
-  __DATA_CONST.__auth_got: 0x628
-  __DATA_CONST.__got: 0x218
-  __DATA_CONST.__const: 0x16e0
-  __DATA_CONST.__cfstring: 0x20c0
-  __DATA_CONST.__objc_classlist: 0xb8
+  __DATA_CONST.__auth_got: 0x638
+  __DATA_CONST.__got: 0x228
+  __DATA_CONST.__const: 0x1768
+  __DATA_CONST.__cfstring: 0x2200
+  __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0xa0
-  __DATA_CONST.__objc_arraydata: 0x8
-  __DATA_CONST.__objc_arrayobj: 0x18
+  __DATA_CONST.__objc_arraydata: 0x28
+  __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x2dc8
-  __DATA.__objc_selrefs: 0x9c0
-  __DATA.__objc_ivar: 0x280
-  __DATA.__objc_data: 0x730
-  __DATA.__data: 0x248
+  __DATA.__objc_const: 0x2e98
+  __DATA.__objc_selrefs: 0x9d0
+  __DATA.__objc_ivar: 0x28c
+  __DATA.__objc_data: 0x780
+  __DATA.__data: 0x250
   __DATA.__bss: 0x4140
   __DATA.__common: 0x38
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  UUID: 6C6AEFF4-D202-3E10-AC75-523E70D6733C
-  Functions: 408
-  Symbols:   272
-  CStrings:  1390
+  UUID: BCA25BFC-DD48-3090-98DA-090AB5578B80
+  Functions: 410
+  Symbols:   276
+  CStrings:  1430
 
Symbols:
+ _IOAccelMemoryInfoErrorDomain
+ _host_statistics64
+ _memcmp
+ _strerror
+ _vm_page_size
- _proc_pid_rusage
CStrings:
+ "\n    Additional per-process auxiliary data:\n"
+ "        dirty                 whether a process has outstanding XPC transactions\n"
+ "        jetsam priority\u00a0      relative order of process force exit under memory pressure\n"
+ "    --drainDeferredReclaim    drain deferred reclaim buffers before measuring (default varies by platform)\n    --noDrainDeferredReclaim  don't drain deferred reclaim buffers\n"
+ "    --ioaccel                 print IOAccelMemory region descriptions, implies -v\n"
+ "    --layout (v|h)            layout style for text formatter v:vertical h:horizontal (default: v)\n"
+ "    --perfdata <file.pdj>     write perfdata(1) output to a file\n"
+ "    --sort <column>           change the column used for sorting (default: %s)\n"
+ "    -w, --wide                show wide output with all columns and full paths (implies --swapped --wired)\n    --swapped                 show swapped/compressed column\n    --wired                   show wired column\n    --vmObjectDirty           interpret dirty memory as viewed by VM objects in the kernel\n    --unmapped                search all processes for unmapped memory owned by the target processes\n    --sample <interval>       repeatedly gather footprint at the given sampling interval in seconds\n                              (can be fractional — e.g. 0.5)\n    --sample-duration <secs>  how long to sample in seconds (default: 0 / unlimited)\n    --noCategories            print only total footprint and auxiliary data\n"
+ "\"dispositions\":"
+ "%s%s:%*s\n"
+ "---------------------------------------"
+ "@\"FPSystemMem\""
+ "@32@0:8Q16^@24"
+ "Error while collecting swapusage values: %s (%d)\n"
+ "Error while collecting sys_footprint values: %s\n"
+ "FPSystemMem"
+ "Gather memory information about a process or set of processes\nUsage: footprint [args] [proc/pid/memgraph [proc/pid/memgraph [...]]]\n    -a, --all                 target all processes\n    -j, --json <file>         print json output to a file\n    -h, --help                print this output\n    -p, --proc <name>         target a process by name\n    -p, --pid <pid>           target a process by process ID\n    -x, --exclude <name/pid>  exclude a process\n    -s, --skip                skip processes that are idle-exit clean\n    --minFootprint <MiB>      skip processes with footprint less than the provided minimum\n    --forkCorpse              analyze a forked corpse of the target process (not compatible with --all)\n    -v                        print all regions and vmmap-like output of address space layout\n                              (default output is a summary)\n    -f, --format <fmt>        <fmt> is one of 'bytes', 'formatted', or 'pages' (default: formatted)\n"
+ "System auxiliary data:\n"
+ "TQ,R,N,V_bootCarveoutSize"
+ "VM_KERN_COUNT_EXCLAVES_CARVEOUT"
+ "VM_KERN_MEMORY_EXCLAVES_SHARED"
+ "VM_KERN_MEMORY_KALLOC_SHARED"
+ "[5Q]"
+ "_bootCarveoutSize"
+ "_drainDeferredReclaim"
+ "_sysData"
+ "b!"
+ "bootCarveoutSize"
+ "boot_carveout"
+ "drainDeferredReclaim"
+ "gatherData:error:"
+ "neural_nofootprint_total"
+ "neural_peak"
+ "noDrainDeferredReclaim"
+ "sysMemData"
+ "sys_aux_data"
+ "sys_footprint"
+ "sys_unwired"
+ "sys_wired"
+ "v16@?0r^{FPRangeListNode=QQQQQQQ^{FPRangeListNode}}8"
+ "vm.reclaim.drain_pid"
+ "vm.swapusage"
- "    --ioaccel                             print IOAccelMemory region descriptions, implies -v\n"
- "    --layout (v|h)                        layout style for text formatter v:vertical h:horizontal (default: v)\n"
- "    --perfdata <file.pdj>                 print perfdata(1) output to a file\n"
- "    --sort <column>                       change the column used for sorting (default: %s)\n"
- "    -w, --wide                            show wide output with all columns and full paths (implies --swapped --wired)\n    --swapped                             show swapped/compressed column\n    --wired                               show wired column\n    --vmObjectDirty                       interpret dirty memory as viewed by VM objects in the kernel\n    --unmapped                            search all processes for unmapped memory owned by the target processes\n    --sample <interval>                   repeatedly gather footprint at the given sampling interval in seconds (can be fractional — e.g. 0.5)\n    --sample-duration <duration>          how long to sample in seconds (default and 0 is unlimited)\n    --noCategories                        exclude categories\n"
- "@\"NSArray\"16@0:8"
- "Gather memory information about a process or set of processes\nUsage: footprint [args] [proc/pid/memgraph [proc/pid/memgraph [...]]]\n    -a, --all                             target all processes\n    -j, --json <file>                     print json output to a file\n    -h, --help                            print this output\n    -p, --proc, --pid [proc/pid]          target pid or process (or interpret for -p)\n    -x, --exclude [proc/pid]              exclude pid or process\n    -s, --skip                            skip processes that are idle-exit clean\n    --minFootprint <MiB>                  skip processes with footprint less than the provided minimum\n    --forkCorpse                          analyze a forked corpse of the target process (not compatible with --all)\n    -v                                    print all regions and vmmap-like output of address space layout (default output is a summary)\n    -f, --format (bytes|formatted|pages)  change size formatting preference (default: formatted)\n"
- "R!"
- "T@\"NSArray\",R,N"
- "T@\"NSArray\",R,N,V_memoryRegions"
- "[4Q]"
- "_gatherPhysFootprint"
- "_rangeList"

```
