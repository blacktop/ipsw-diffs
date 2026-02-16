## com.apple.iokit.IOThunderboltFamily

> `com.apple.iokit.IOThunderboltFamily`

```diff

-6800.80.15.0.0
-  __TEXT.__cstring: 0x49c58
-  __TEXT.__os_log: 0x3acfc
+6805.100.14.0.0
+  __TEXT.__cstring: 0x49e4a
+  __TEXT.__os_log: 0x3aee7
   __TEXT.__const: 0xb60
-  __TEXT_EXEC.__text: 0x1e461c
+  __TEXT_EXEC.__text: 0x1c3e4c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xb22
   __DATA.__common: 0x15b0

   __DATA_CONST.__const: 0x23e18
   __DATA_CONST.__kalloc_type: 0x22c0
   __DATA_CONST.__kalloc_var: 0xbe0
-  UUID: 54BC51EF-4EF7-34E6-B64B-6D5E8A9A03F4
-  Functions: 5585
+  UUID: 78136EFA-913D-3912-AF25-A9A1549D0787
+  Functions: 5586
   Symbols:   0
-  CStrings:  6101
+  CStrings:  6107
 
CStrings:
+ "%lldus Error: IOThunderboltSwitchDelegateACIO(%x@%llx)::initWithController Error writing to VSEC register: fACIOVSECRegOffset: 0x%08x, fACIOVSECRegValue: 0x%08x, VSEC Length: %d, offset greater than VSEC Length\n"
+ "%lldus Error: IOThunderboltSwitchDelegateACIO(%x@%llx)::initWithController Unable to find VSEC block with id: 0x%x\n"
+ "%lldus IOThunderboltSwitchDelegateACIO(%x@%llx)::initWithController Writing to VSEC register: fACIOVSECRegOffset: 0x%08x, fACIOVSECRegValue: 0x%08x, status: 0x%x\n"
+ "12111122122222222211222"
+ "21:10:40"
+ "Feb  5 2026"
+ "acio_vsec_reg_write"
- "\"dfp\\n\" @%s:%d"
- "121111221222222222112"
- "20:48:08"
- "Jan 26 2026"

```
