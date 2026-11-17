## adc-boreas-v6x.im4p

> `Firmware/isp_bni/adc-boreas-v6x.im4p`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT._rtk_patchbay`
- `__TEXT.__eh_frame`
- `__DATA.__data`
- `__DATA._rtk_power`
- `__DATA.__data_copy`
- `__DATA._rtk_mtab`
- `__DATA.__chain_starts`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0xb3c30c
+  __TEXT.__text: 0xb3d358
   __TEXT.__const: 0x91f918
-  __TEXT.__cstring: 0xce1be
+  __TEXT.__cstring: 0xce416
   __TEXT._rtk_patchbay: 0x24a
   __TEXT.__constructor: 0x0
   __TEXT.__init_offsets: 0x0
   __TEXT.__eh_frame: 0x1bc
-  __DATA.__const: 0x87258
+  __DATA.__const: 0x87288
   __DATA._rtk_heap: 0x1000
   __DATA._copy_begin: 0x0
   __DATA.__data: 0x11cf30

   __DATA.__mod_init_func: 0xb0
   __DATA._rtk_threads: 0x0
   __DATA.__zerofill: 0x602300
-  Functions: 14943
+  Functions: 14949
   Symbols:   0
-  CStrings:  22352
+  CStrings:  22370
 
CStrings:
+ "%s%s \n"
+ "%s: SECURITY_STATE 0x%x: sec 0x%x op 0x%x err 0x%x\n"
+ "%s[%zu]%-*s%#08llX \n"
+ "===== SENSOR_DIAG ch %zu BEGIN %s =====\n"
+ "===== SENSOR_DIAG ch %zu END =====\n"
+ "ACL ERROR bridge%zu ch%u write 0x%02x:0x%04x (%s)"
+ "AclCheckWrite"
+ "BTR: "
+ "EnqueueWrite"
+ "FRAMEDONE_STALL"
+ "I2C write At: "
+ "IGNORE cmd %zu, as other ch is active! %x"
+ "NO_FIRST_RVSYNC"
+ "SENSOR_DIAG %s: frame counter (0x%04x):\n"
+ "SENSOR_DIAG ch %zu %s %llu us after stream start, fc %d\n"
+ "SENSOR_DIAG ch %zu --- %s registers ---\n"
+ "SENSOR_DIAG ch %zu --- DPRX lane status ---\n"
+ "SENSOR_DIAG ch %zu pwr cnt/st sns %u/%d foc %u/%d stb %u/%d hwk %u/%d efs %u/%d fpd %u/%d\n"
+ "rails missing %zu %zu - %p %p\n"
- "IGNORE cmd, as other ch is active!"
```
