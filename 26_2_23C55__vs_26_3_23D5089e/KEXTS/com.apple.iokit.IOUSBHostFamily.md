## com.apple.iokit.IOUSBHostFamily

> `com.apple.iokit.IOUSBHostFamily`

```diff

-1493.60.8.0.1
-  __TEXT.__cstring: 0x9e1d
-  __TEXT.__os_log: 0x826b
-  __TEXT.__const: 0xb50
-  __TEXT_EXEC.__text: 0x9dcc8
+1504.80.35.0.1
+  __TEXT.__cstring: 0x9ffd
+  __TEXT.__os_log: 0x8486
+  __TEXT.__const: 0xb60
+  __TEXT_EXEC.__text: 0x9fd4c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x1f0
   __DATA.__common: 0x910
   __DATA.__bss: 0x10
-  __DATA_CONST.__auth_got: 0x690
-  __DATA_CONST.__got: 0x1f0
+  __DATA_CONST.__auth_got: 0x6a8
+  __DATA_CONST.__got: 0x1f8
   __DATA_CONST.__mod_init_func: 0xe0
   __DATA_CONST.__mod_term_func: 0xd8
-  __DATA_CONST.__const: 0xc218
+  __DATA_CONST.__const: 0xc248
   __DATA_CONST.__kalloc_type: 0x1b00
   __DATA_CONST.__kalloc_var: 0x280
-  UUID: 15379F6D-CE7E-3C81-96AC-5432B465A4EA
-  Functions: 1902
+  UUID: A996918D-8E1D-378A-B41D-6560D8EE9ED4
+  Functions: 1910
   Symbols:   0
-  CStrings:  1593
+  CStrings:  1615
 
CStrings:
+ "%s@%s: %s::%s: %s completed with 0x%08x\n"
+ "%s@%s: %s::%s: %s completed with 0x%08x (%d attempts)\n"
+ "%s@%s: %s::%s: %s: %llu completed with %d\n"
+ "%s@%s: %s::%s: offset 0x%08x invalid (memory length 0x%08llx)\n"
+ "%s@%s: %s::%s: offset 0x%08x mask 0x%08x read 0x%08x\n"
+ "%s@%s: %s::%s: offset 0x%08x mask 0x%08x read 0x%08x wrote 0x%08x\n"
+ "%s@%s: %s::%s: unexpected _clockReferenceCount %u\n"
+ "%s@%s: %s::%s: unexpected _mapperReferenceCount %u\n"
+ "%s@%s: %s::%s: unsupported link speed %llu\n"
+ "121111121222121211222222212222222222222222222222222222222222222222222222222221221111122221112112222222222111221121111111111111"
+ "UsbTransportState"
+ "applyTunablesData"
+ "disableClock"
+ "disableMapper"
+ "enableClock"
+ "enableMapper"
+ "setActive"
+ "usb-repeater"
- "%s@%s: %s::%s: %s: %d completed with 0x%08x\n"
- "%s@%s: %s::%s: invalid device speed (port status 0x%08x\n"
- "12111112122212121122222221222222222222222222222222222222222222222222222222222122111112222111211222222222211122111111111111111"

```
