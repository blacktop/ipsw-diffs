## ansf.t8140_largemem.release.im4p

> `Firmware/ansf.t8140_largemem.release.im4p`

### Sections with Same Size but Changed Content

- `__DATA._rtk_patchbay`
- `__DATA._rtk_mtab`
- `__DATA.__data`
- `__DATA.__const`

```diff

   __TEXT.text_first: 0x45a0
-  __TEXT.__text: 0x1e6168
-  __TEXT.shared: 0xdef0
+  __TEXT.__text: 0x1e64e0
+  __TEXT.shared: 0xe03c
   __TEXT.read: 0x70e0
-  __TEXT.__const: 0x5918
-  __TEXT.__cstring: 0x25040
+  __TEXT.__const: 0x5b18
+  __TEXT.__cstring: 0x25045
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x1c
   __DATA._rtk_boot: 0x8000

   __DATA.__data: 0x7010
   __DATA.__const: 0x2450
   __DATA.__gxf_data: 0x10
-  __DATA.core_globals: 0x162
+  __DATA.core_globals: 0x164
   __DATA._rtk_init_stack: 0x1000
   __DATA._rtk_irq_stack: 0x1000
   __DATA._rtk_exc_stack: 0x1000

   __DATA._rtk_heap: 0x0
   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
-  __DATA.__zerofill: 0x356558
-  Functions: 1980
+  __DATA.__zerofill: 0x356588
+  Functions: 1981
   Symbols:   0
-  CStrings:  3963
+  CStrings:  3962
 
CStrings:
+ "241.40.4"
+ "241.40.4~161"
+ "AppleStorageFirmwareASP3-241.40.4~161"
+ "Sanitize Failed"
+ "Sweep stuck detected - aborting - channel %d, die %d, plane %d"
+ "Sweep was aborted - rejecting continuation command"
+ "sanitize cmd drop - not init"
- "241.0.12"
- "241.0.12~642"
- "Abort Pad: Flow %u , Band: %u"
- "AppleStorageFirmwareASP3-241.0.12~642"
- "Sanitize already in progress, phase=%d"
- "Sanitize drop - device in shutdown"
- "mark invalid band %u S %u"
- "mark valid band %u M %u"
```
