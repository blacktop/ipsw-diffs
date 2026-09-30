## rans.t604x.release.im4p

> `Firmware/rans.t604x.release.im4p`

### Sections with Same Size but Changed Content

- `__DATA._rtk_patchbay`
- `__DATA._rtk_mtab`
- `__DATA.__data`
- `__DATA.__const`

```diff

   __TEXT.text_first: 0x45a0
-  __TEXT.__text: 0x2015ec
-  __TEXT.shared: 0xe9ac
+  __TEXT.__text: 0x2019dc
+  __TEXT.shared: 0xeb00
   __TEXT.read: 0x7728
-  __TEXT.__const: 0x66e8
-  __TEXT.__cstring: 0x263c0
+  __TEXT.__const: 0x68e8
+  __TEXT.__cstring: 0x263c5
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x1c
   __DATA._rtk_boot: 0x4000

   __DATA.__data: 0x7908
   __DATA.__const: 0x3700
   __DATA.__gxf_data: 0x10
-  __DATA.core_globals: 0x167
+  __DATA.core_globals: 0x169
   __DATA._rtk_init_stack: 0x1000
   __DATA._rtk_irq_stack: 0x1000
   __DATA._rtk_exc_stack: 0x1000

   __DATA._rtk_heap: 0x0
   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
-  __DATA.__zerofill: 0x594db8
-  Functions: 2188
+  __DATA.__zerofill: 0x594de8
+  Functions: 2189
   Symbols:   0
-  CStrings:  4098
+  CStrings:  4097
 
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
