## ansf.t8142.release.im4p

> `Firmware/ansf.t8142.release.im4p`

### Sections with Same Size but Changed Content

- `__DATA._rtk_patchbay`
- `__DATA._rtk_mtab`
- `__DATA.__data`
- `__DATA.__const`

```diff

   __TEXT.text_first: 0x45a0
-  __TEXT.__text: 0x1f6b8c
-  __TEXT.shared: 0xe6fc
+  __TEXT.__text: 0x1f6f90
+  __TEXT.shared: 0xe848
   __TEXT.read: 0x70cc
-  __TEXT.__const: 0x5cf8
-  __TEXT.__cstring: 0x263c1
+  __TEXT.__const: 0x5ef8
+  __TEXT.__cstring: 0x263c6
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x1c
   __DATA._rtk_boot: 0x4000

   __DATA.__data: 0x7990
   __DATA.__const: 0x2680
   __DATA.__gxf_data: 0x10
-  __DATA.core_globals: 0x166
+  __DATA.core_globals: 0x168
   __DATA._rtk_init_stack: 0x1000
   __DATA._rtk_irq_stack: 0x1000
   __DATA._rtk_exc_stack: 0x1000

   __DATA._rtk_heap: 0x0
   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
-  __DATA.__zerofill: 0x3a1b00
-  Functions: 2056
+  __DATA.__zerofill: 0x3a1b30
+  Functions: 2057
   Symbols:   0
-  CStrings:  4112
+  CStrings:  4111
 
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
