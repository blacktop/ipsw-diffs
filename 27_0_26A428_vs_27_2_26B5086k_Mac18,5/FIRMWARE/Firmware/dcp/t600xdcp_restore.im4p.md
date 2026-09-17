## t600xdcp_restore.im4p

> `Firmware/dcp/t600xdcp_restore.im4p`

### Sections with Same Size but Changed Content

- `__TEXT.__chain_starts`
- `__DATA._rtk_patchbay`
- `__DATA.__mod_init_func`
- `__DATA._rtk_data_uuid`
- `__DATA._rtk_mtab`
- `__DATA.__constructor`

```diff

-  __TEXT.__text: 0x32340c
-  __TEXT.__const: 0x3cbd68
+  __TEXT.__text: 0x322dc0
+  __TEXT.__const: 0x3cbd98
   __TEXT.__chain_starts: 0x30
-  __TEXT.__cstring: 0x37e5e
+  __TEXT.__cstring: 0x37f24
   __TEXT.__padding1: 0x1
   __TEXT.__padding2: 0x1
   __TEXT.__lcxx_override: 0x24
   __TEXT.__init_offsets: 0x0
-  __DATA.__const: 0x37e48
-  __DATA.__data: 0x129688
+  __DATA.__const: 0x37e70
+  __DATA.__data: 0x129690
   __DATA._rtk_patchbay: 0x75a
   __DATA._rtk_tunables: 0x1e8
   __DATA._rtk_boot: 0x9000

   __DATA._rtk_exc_stack: 0x1000
   __DATA._afk_sys_drv: 0xe40
   __DATA.__mod_init_func: 0x88
-  __DATA._afk_sys_objt: 0xbb0
+  __DATA._afk_sys_objt: 0xbc0
   __DATA._rtk_heap: 0x30000
   __DATA._rtk_threads: 0x0
   __DATA.__zerofill: 0x325b0

   __DATA.__constructor: 0x8
   __DATA.__gxf_data: 0x10
   __OS_LOG.__string: 0x227f9
-  Functions: 7316
+  Functions: 7318
   Symbols:   0
-  CStrings:  8668
+  CStrings:  8672
 
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
