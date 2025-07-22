## com.apple.driver.AppleEmbeddedUSBHost

> `com.apple.driver.AppleEmbeddedUSBHost`

```diff

-679.0.2.0.0
-  __TEXT.__cstring: 0x5b3
+679.0.3.0.0
+  __TEXT.__cstring: 0x697
   __TEXT.__const: 0x40
-  __TEXT_EXEC.__text: 0x2738
+  __TEXT.__os_log: 0xa3
+  __TEXT_EXEC.__text: 0x30c4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
-  __DATA.__common: 0x138
-  __DATA_CONST.__auth_got: 0xe0
-  __DATA_CONST.__got: 0x90
-  __DATA_CONST.__mod_init_func: 0x20
-  __DATA_CONST.__mod_term_func: 0x20
-  __DATA_CONST.__const: 0x2ba0
-  __DATA_CONST.__kalloc_type: 0x180
-  UUID: 9183BF67-22C8-3A45-B3CB-E957F5665CF4
-  Functions: 125
+  __DATA.__common: 0x160
+  __DATA_CONST.__auth_got: 0xf0
+  __DATA_CONST.__got: 0xa0
+  __DATA_CONST.__mod_init_func: 0x28
+  __DATA_CONST.__mod_term_func: 0x28
+  __DATA_CONST.__const: 0x3280
+  __DATA_CONST.__kalloc_type: 0x1c0
+  UUID: 05BD4DE3-6F73-3907-8A6E-EE0CFB37E27E
+  Functions: 144
   Symbols:   0
-  CStrings:  40
+  CStrings:  49
 
CStrings:
+ "%s@%s: %s::%s: register 0x%04x failed with 0x%08x\n"
+ "%s@%s: %s::%s: register 0x%04x value 0x%02x -> 0x%02x\n"
+ "%s@%s: %s::%s: register 0x%04x value 0x%02x already set\n"
+ "AppleUSB20Hub_32789"
+ "site.AppleUSB20Hub_32789"
+ "writeVendorRegister"

```
