## t604xdcp_restore.im4p

> `Firmware/dcp/t604xdcp_restore.im4p`

### Sections with Same Size but Changed Content

- `__TEXT.__chain_starts`
- `__DATA.__data`
- `__DATA._rtk_patchbay`
- `__DATA.__mod_init_func`
- `__DATA._rtk_data_uuid`
- `__DATA._rtk_mtab`
- `__DATA.__constructor`

```diff

-  __TEXT.__text: 0x307dfc
-  __TEXT.__const: 0x3b3b18
+  __TEXT.__text: 0x307798
+  __TEXT.__const: 0x3b3bc0
   __TEXT.__chain_starts: 0x34
-  __TEXT.__cstring: 0x39f64
+  __TEXT.__cstring: 0x3a02a
   __TEXT.__lcxx_override: 0x24
   __TEXT.__init_offsets: 0x0
-  __DATA.__const: 0x3af78
+  __DATA.__const: 0x3af88
   __DATA.__data: 0x11f4c0
   __DATA._rtk_patchbay: 0x75a
   __DATA._rtk_tunables: 0x6a0

   __DATA._rtk_exc_stack: 0x1000
   __DATA._afk_sys_drv: 0xc00
   __DATA.__mod_init_func: 0x88
-  __DATA._afk_sys_objt: 0xbf0
+  __DATA._afk_sys_objt: 0xc00
   __DATA._rtk_heap: 0x30000
   __DATA._rtk_threads: 0x0
   __DATA.__zerofill: 0x5c628

   __DATA.__constructor: 0x8
   __DATA.__gxf_data: 0x10
   __OS_LOG.__string: 0x24180
-  Functions: 7431
+  Functions: 7433
   Symbols:   0
-  CStrings:  9017
+  CStrings:  9021
 
CStrings:
+ "%s: sampled sink DSC caps: maxSlicesPerLine=%u version=0x%x sliceCapabilityMask=0x%x\n"
+ "%s: vi is null\n"
+ "A491_callback__"
+ "A492_callback__"
+ "A494_callback__"
+ "A500_callback__"
+ "DCPI2CBase"
+ "M3 diags cmd type %u timed out after %u ms with no response, returning busy"
+ "Skip notifying hotplug to AP since it's already notified\n"
+ "Trigger mode set for display wake\n"
+ "get_sink_max_dsc_slices"
- "%s: connected sink advertises %u max DSC slices per line"
- "%s: no vi for DSC caps"
- "A441_callback__"
- "A442_callback__"
- "A444_callback__"
- "A450_callback__"
- "getPlatformExtDisplayLimits"
```
