## com.apple.driver.AppleEmbeddedUSBHost

> `com.apple.driver.AppleEmbeddedUSBHost`

```diff

-651.100.4.0.0
-  __TEXT.__cstring: 0x5a2
+679.0.1.0.0
+  __TEXT.__cstring: 0x8c0
+  __TEXT.__os_log: 0x1c5
   __TEXT.__const: 0x40
-  __TEXT_EXEC.__text: 0x2578
+  __TEXT_EXEC.__text: 0x45b0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
-  __DATA.__common: 0x138
-  __DATA_CONST.__auth_got: 0xe0
-  __DATA_CONST.__got: 0x90
-  __DATA_CONST.__mod_init_func: 0x20
-  __DATA_CONST.__mod_term_func: 0x20
-  __DATA_CONST.__const: 0x2b80
-  __DATA_CONST.__kalloc_type: 0x180
-  UUID: 25AFEF38-9B4D-3CF2-ADB3-D2921D46E0E6
-  Functions: 119
+  __DATA.__common: 0x160
+  __DATA_CONST.__auth_got: 0x140
+  __DATA_CONST.__got: 0xc8
+  __DATA_CONST.__mod_init_func: 0x28
+  __DATA_CONST.__mod_term_func: 0x28
+  __DATA_CONST.__const: 0x31c8
+  __DATA_CONST.__kalloc_type: 0x1c0
+  UUID: 2A3BA667-DEAE-39EF-8F6F-E43F7D4E1F84
+  Functions: 153
   Symbols:   0
-  CStrings:  40
+  CStrings:  80
 
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
+ "12111112122212121121111111111121222111111111111111111222222222222222222221"
+ "12111112122212121122222221222222222222222222222222222222222222222222222222222122111112222111211222222222211122111111111111111121"
+ "1211111212221212112222222122222222222222222222222222222222222222222222222222212211111222211121122222222221112211111111111111112122"
+ "AAPL,phandle"
+ "AppleUSBHostPort"
+ "AppleUSBHubIICDevice"
+ "AppleUSBHubIICDeviceResetFunction"
+ "AppleUSBHubIICDeviceTunables"
+ "AppleUSBHubIICDeviceVendor"
+ "Genesys Logic"
+ "VIA Labs"
+ "applyTunables"
+ "copyPortForPhandle"
+ "function-reset"
+ "hubReset"
+ "powerStateDidChangeTo"
+ "powerStateWillChangeTo"
+ "readRegister"
+ "site.AppleUSBHubIICDevice"
+ "tunable"
+ "tunable-gl"
+ "tunable-vl"
+ "usb-port"
+ "writeRegister"
- "1211111212221212112111111111121222111111111111111111222222222222222222221"
- "121111121222121211222222212222222222222222222222222222222222222222222222222221221111122221111111112112222222222111221221"
- "12111112122212121122222221222222222222222222222222222222222222222222222222222122111112222111111111211222222222211122122122"

```
