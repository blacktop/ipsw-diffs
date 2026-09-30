## ansf.t603x_ASP3.release.im4p

> `Firmware/ansf.t603x_ASP3.release.im4p`

### Sections with Same Size but Changed Content

- `__TEXT.__chain_starts`
- `__DATA._rtk_power`
- `__DATA._rtk_patchbay`
- `__DATA._rtk_mtab`
- `__DATA.__data`
- `__DATA.__const`

```diff

   __TEXT.text_first: 0x45a0
-  __TEXT.__text: 0x208524
-  __TEXT.shared: 0xead4
+  __TEXT.__text: 0x208914
+  __TEXT.shared: 0xec28
   __TEXT.read: 0x7734
-  __TEXT.__const: 0x6c68
-  __TEXT.__cstring: 0x2678d
+  __TEXT.__const: 0x6e68
+  __TEXT.__cstring: 0x26792
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x1c
   __DATA._rtk_boot: 0x4000

   __DATA.__data: 0x83f8
   __DATA.__const: 0x42b0
   __DATA.__gxf_data: 0x10
-  __DATA.core_globals: 0x167
+  __DATA.core_globals: 0x169
   __DATA._rtk_init_stack: 0x1000
   __DATA._rtk_irq_stack: 0x1000
   __DATA._rtk_exc_stack: 0x1000

   __DATA._rtk_heap: 0x0
   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
-  __DATA.__zerofill: 0x5825f8
-  Functions: 2322
+  __DATA.__zerofill: 0x582628
+  Functions: 2323
   Symbols:   0
-  CStrings:  4173
+  CStrings:  4172
 
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
