## malloc_history

> `/usr/bin/malloc_history`

```diff

-64566.82.1.0.0
-  __TEXT.__text: 0xb958
-  __TEXT.__auth_stubs: 0x9f0
-  __TEXT.__objc_stubs: 0x1160
+64570.34.1.0.0
+  __TEXT.__text: 0xbe6c
+  __TEXT.__auth_stubs: 0xa10
+  __TEXT.__objc_stubs: 0x12a0
   __TEXT.__const: 0xd8
-  __TEXT.__gcc_except_tab: 0x5d4
-  __TEXT.__cstring: 0x2d07
+  __TEXT.__gcc_except_tab: 0x638
+  __TEXT.__cstring: 0x2dd3
   __TEXT.__oslogstring: 0x8f5
   __TEXT.__objc_classname: 0x17
-  __TEXT.__objc_methname: 0xb53
-  __TEXT.__unwind_info: 0x208
-  __DATA_CONST.__auth_got: 0x508
-  __DATA_CONST.__got: 0x180
+  __TEXT.__objc_methname: 0xc02
+  __TEXT.__unwind_info: 0x200
+  __DATA_CONST.__auth_got: 0x518
+  __DATA_CONST.__got: 0x188
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x550
-  __DATA_CONST.__cfstring: 0x7a0
+  __DATA_CONST.__cfstring: 0x8a0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_classrefs: 0x18
   __DATA_CONST.__objc_intobj: 0x18
   __DATA.__objc_const: 0x90
-  __DATA.__objc_selrefs: 0x458
+  __DATA.__objc_selrefs: 0x4a8
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x8
   __DATA.__crash_info: 0x40

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxcselect.dylib
-  UUID: 476C6B62-4A57-31C0-BD8A-30B1E9514986
+  UUID: A399113B-497E-38C2-B0FD-22144550F356
   Functions: 143
-  Symbols:   220
-  CStrings:  512
+  Symbols:   223
+  CStrings:  535
 
Symbols:
+ _OBJC_CLASS_$_NSDateFormatter
+ _msl_payload_get_allocation_timestamp
+ _objc_enumerationMutation
CStrings:
+ ": "
+ "Date/Time:"
+ "Launch Time:"
+ "Stack logging was dynamically enabled in target process, after it was launched,\nso no backtraces are available for earlier allocations.\nStack logging was enabled for %.1f seconds, which is %.1f%% of the process's total lifetime of %.1f seconds.\n\n"
+ "Target process:  %@ [%u] (%@)\n"
+ "core file"
+ "corpse"
+ "countByEnumeratingWithState:objects:count:"
+ "date"
+ "dateFromString:"
+ "launchTime"
+ "live task"
+ "nodeForAddress:"
+ "objectAtIndex:"
+ "setDateFormat:"
+ "taskIsCorpse"
+ "timeIntervalSinceDate:"
+ "timestampForNode:"
+ "void printCallTree(__strong id<VMUCommonGraphInterface>, CSSymbolicatorRef, HighWaterMarkInfo *, VMUCallTreeOptions, VMUObjectContentLevel, BOOL, BOOL, NSHashTable *__strong, __strong id<VMUStackLogReader>, NSTimeInterval)"
+ "yyyy-MM-dd HH:mm:ss.SSS Z"
- "--"
- "-al"
- "Stack logging was dynamically enabled in target process, after it was launched,\nso no backtraces are available for earlier allocations.\n"
- "Target process:  %@ [%u]\n"
- "void printCallTree(__strong id<VMUCommonGraphInterface>, CSSymbolicatorRef, HighWaterMarkInfo *, VMUCallTreeOptions, VMUObjectContentLevel, BOOL, BOOL, NSHashTable *__strong, __strong id<VMUStackLogReader>)"

```
