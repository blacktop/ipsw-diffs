## rans.t8152.release.im4p

> `Firmware/rans.t8152.release.im4p`

### Sections with Same Size but Changed Content

- `__TEXT.__chain_starts`
- `__DATA._rtk_power`
- `__DATA._rtk_patchbay`
- `__DATA._rtk_mtab`

```diff

   __TEXT.text_first: 0x45a0
-  __TEXT.__text: 0x20dfbc
+  __TEXT.__text: 0x210880
   __TEXT.shared: 0xee40
   __TEXT.read: 0x7214
-  __TEXT.__const: 0x6300
-  __TEXT.__cstring: 0x271b7
+  __TEXT.__const: 0x63c0
+  __TEXT.__cstring: 0x277dc
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x1c
   __DATA._rtk_boot: 0x4000

   __DATA._rtk_patchbay: 0x4b9
   __DATA._rtk_tunables: 0xa10
   __DATA._rtk_mtab: 0x330
-  __DATA.__data: 0x8528
-  __DATA.__const: 0x1cc0
+  __DATA.__data: 0x8530
+  __DATA.__const: 0x1cc8
   __DATA.__gxf_data: 0x10
-  __DATA.core_globals: 0x179
+  __DATA.core_globals: 0x17b
   __DATA._rtk_init_stack: 0x1000
   __DATA._rtk_irq_stack: 0x1000
   __DATA._rtk_exc_stack: 0x1000

   __DATA._rtk_heap: 0x0
   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
-  __DATA.__zerofill: 0x3f3318
-  Functions: 2157
+  __DATA.__zerofill: 0x3f33f8
+  Functions: 2169
   Symbols:   0
-  CStrings:  4225
+  CStrings:  4258
 
CStrings:
+ " DebugData_DumpData -> %ums"
+ "3975.40.11"
+ "3975.40.11~177"
+ "AppleStorageFirmware-3975.40.11~177"
+ "BDB_DEFAULT"
+ "BDB_DYNAMIC"
+ "BG.todo = 0x%llx"
+ "DebugData ASI dropped: size=%u asiLbas=%u maxLbas=%u"
+ "DebugData ASI included: size=%u lbas=%u"
+ "DebugData GET special failed segIdx=%d err=%u"
+ "DebugData TunnelGet sizeOnly: outputLen=%u (compLbas=%u)"
+ "DebugData TunnelGet: Buf_Get(%u) failed"
+ "DebugData TunnelGet: ReadHiddenLbas failed (totalLbas=%u)"
+ "DebugData TunnelGet: buffer too small (have=%u need=%u)"
+ "DebugData TunnelGet: no data available"
+ "DebugData TunnelGet: not init, returning INVALID_PARAM"
+ "DebugData TunnelGet: success outputLen=%u (compLbas=%u)"
+ "DebugData TunnelTrigger: invalid event %u payload=0x%llx"
+ "DebugData TunnelTrigger: not init, returning INVALID_PARAM"
+ "DebugData TunnelTrigger: success event=%u payload=%llx"
+ "DebugData TunnelTrim: not init, returning INVALID_PARAM"
+ "DebugData TunnelTrim: success"
+ "DebugData compressed: orig=%u comp=%u totalInflatedLbas=%u asi=%s"
+ "DebugData dump skipped: event=%u"
+ "DebugData dump skipped: shutdown in progress (event=%u)"
+ "DebugData request event=%u payload=%llu, init %u"
+ "DebugData request skipped: data pending consumption (event=%u payload=%llu)"
+ "DebugData request skipped: shutdown in progress (event=%u payload=%llu)"
+ "DebugData submit %s msp=%u vdie=%u dramIdx=%u"
+ "DebugData write OOB: nLbas=%u"
+ "DebugData write aborted (not writable / in shutdown)"
+ "DebugData_Init2: recovered compLbas=%u"
+ "EAN b=0x%llx f=0x%x sz=0x%x dBS=0x%x dBB=0x%x | BGtd=0x%llx UPtd=0x%x"
+ "ErrInj: forced deflate failure"
+ "Sanitize Failed"
+ "debug_data.c"
+ "deflate failed: src=%u, status %d avail_in=%u avail_out=%u"
+ "deflate output overwrite input: src=%u failed, avail_in=%u avail_out=%u"
+ "deflate(FINISH) failed: status %d avail_out=%u"
+ "deflate: deflateInit2 failed, status %d"
+ "deflateEnd failed: status %d"
+ "dump still pending after 100ms, abort tunnel"
+ "invalid event id %u"
+ "msp=%u dies=%u headerLba=%u numBdbLbas=%u"
+ "out of range lbaOffset=%u nLbas=%u max=%u"
+ "override devFused %u"
+ "sanitize cmd drop - not init"
+ "{ 'trace_id': 'BG_TODO_NEW', 'tp_func': %d, 'timestamp': %llu, 'initialTodoLo': %u, 'initialTodoHi': %u, 'endTodoLo': %u, 'endTodoHi': %u }\n"
- "3975.0.39"
- "3975.0.39~473"
- "Abort Pad: Flow %u , Band: %u"
- "AppleStorageFirmware-3975.0.39~473"
- "BG.todo = 0x%x"
- "EAN b=0x%llx f=0x%x sz=0x%x dBS=0x%x dBB=0x%x | BGtd=0x%x UPtd=0x%x"
- "FADUMP: deflate failed. status %d, Sec left to store: %d"
- "FADUMP: deflateEnd failed. status %d"
- "FADUMP: deflateInit2 failed. status %d"
- "Sanitize already in progress, phase=%d"
- "Sanitize drop - device in shutdown"
- "mark invalid band %u S %u"
- "mark valid band %u M %u"
- "override TT devFused %u"
- "{ 'trace_id': 'BG_TODO_NEW', 'tp_func': %d, 'timestamp': %llu, 'initialTodo': %u, 'endTodo': %u }\n"
```
