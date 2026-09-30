## adc-boreas-v6x.im4p

> `Firmware/isp_bni/adc-boreas-v6x.im4p`

### Sections with Same Size but Changed Content

- `__TEXT._rtk_patchbay`
- `__TEXT.__eh_frame`
- `__DATA.__data`
- `__DATA._rtk_power`
- `__DATA.__data_copy`
- `__DATA._fwinfo`
- `__DATA._rtk_mtab`
- `__DATA.__chain_starts`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0xb3ca60
-  __TEXT.__const: 0x91e608
-  __TEXT.__cstring: 0xccaf9
+  __TEXT.__text: 0xb3e260
+  __TEXT.__const: 0x920408
+  __TEXT.__cstring: 0xccaf0
   __TEXT._rtk_patchbay: 0x24a
   __TEXT.__constructor: 0x0
   __TEXT.__init_offsets: 0x0
   __TEXT.__eh_frame: 0x1bc
-  __DATA.__const: 0x89320
+  __DATA.__const: 0x89550
   __DATA._rtk_heap: 0x1000
   __DATA._copy_begin: 0x0
   __DATA.__data: 0x11cb10

   __DATA.__chain_starts: 0x38
   __DATA.__mod_init_func: 0xd8
   __DATA._rtk_threads: 0x0
-  __DATA.__zerofill: 0x603e00
-  Functions: 14945
+  __DATA.__zerofill: 0x5ffe00
+  Functions: 14949
   Symbols:   0
-  CStrings:  22247
+  CStrings:  22249
 
CStrings:
+ "%s: %s: Using AST golden AF dynamic cal.\n"
+ "%s: ch %zu bMultiChannelsStop %s\n"
+ "ISR_IRQ"
+ "[DSI] %s %s frameID=%d\n"
- "CPDEProc::ISR_IRQ %zu: \n"
- "LCMOT: [%s] UNFILTERED_ACCEL_VALID flag not set? No unfiltered acceleration data populated\n"
```
