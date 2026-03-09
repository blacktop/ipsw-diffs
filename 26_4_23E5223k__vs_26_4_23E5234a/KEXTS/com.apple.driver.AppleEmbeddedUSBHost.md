## com.apple.driver.AppleEmbeddedUSBHost

> `com.apple.driver.AppleEmbeddedUSBHost`

```diff

 682.100.15.0.0
-  __TEXT.__cstring: 0x9f6
+  __TEXT.__cstring: 0xcdf
+  __TEXT.__os_log: 0x421
   __TEXT.__const: 0x48
-  __TEXT.__os_log: 0x25c
-  __TEXT_EXEC.__text: 0x4e74
+  __TEXT_EXEC.__text: 0x6a74
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
-  __DATA.__common: 0x1b0
-  __DATA_CONST.__auth_got: 0x128
-  __DATA_CONST.__got: 0xd0
-  __DATA_CONST.__mod_init_func: 0x38
-  __DATA_CONST.__mod_term_func: 0x38
-  __DATA_CONST.__const: 0x3f30
-  __DATA_CONST.__kalloc_type: 0x240
-  UUID: D963E1B8-B740-3687-BFDE-04816E5279D9
-  Functions: 196
+  __DATA.__common: 0x1d8
+  __DATA_CONST.__auth_got: 0x170
+  __DATA_CONST.__got: 0xe0
+  __DATA_CONST.__mod_init_func: 0x40
+  __DATA_CONST.__mod_term_func: 0x40
+  __DATA_CONST.__const: 0x4558
+  __DATA_CONST.__kalloc_type: 0x280
+  UUID: F3C3BB17-EF86-3D83-AAC5-1EFA86DB446D
+  Functions: 224
   Symbols:   0
-  CStrings:  83
+  CStrings:  120
 
CStrings:
+ "%s: %s::%s: %d\n"
+ "%s: %s::%s: address 0x%02x, value 0x%02x returned %s\n"
+ "%s: %s::%s: applying offset 0x%02x mask 0x%02x value 0x%02x\n"
+ "%s: %s::%s: failed offset 0x%08x\n"
+ "%s: %s::%s: failed to build dictionary for %s\n"
+ "%s: %s::%s: failed to find AppleUSBHostPort for %s\n"
+ "%s: %s::%s: port powered off\n"
+ "%s: %s::%s: port powering on\n"
+ "%s: %s::%s: skipping offset 0x%02x mask 0x%02x value 0x%02x (already set)\n"
+ "12111112122212121112112"
+ "AAPL,phandle"
+ "AppleUSBHostPort"
+ "AppleUSBHubIICDevice"
+ "AppleUSBHubIICDeviceResetFunction"
+ "AppleUSBHubIICDeviceTunables"
+ "AppleUSBHubIICDeviceVendor"
+ "Genesys Logic"
+ "VIA Labs"
+ "copyPortForPhandle"
+ "function-reset"
+ "hubReset"
+ "powerStateDidChangeTo"
+ "powerStateWillChangeTo"
+ "site.AppleUSBHubIICDevice"
+ "tunable-gl"
+ "tunable-vl"
+ "tunable-vlf0"
+ "usb-port"

```
