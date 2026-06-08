## com.apple.driver.AppleHIDTransportFIFO

> `com.apple.driver.AppleHIDTransportFIFO`

```diff

-9140.6.0.0.0
+10100.34.0.0.0
   __TEXT.__const: 0x8
-  __TEXT.__cstring: 0x2b37
-  __TEXT_EXEC.__text: 0x135c0
+  __TEXT.__cstring: 0x2be6
+  __TEXT_EXEC.__text: 0x13674
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x60
   __DATA.__bss: 0x1
-  __DATA_CONST.__auth_got: 0x1e0
-  __DATA_CONST.__got: 0xb8
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
-  __DATA_CONST.__const: 0x10a8
+  __DATA_CONST.__const: 0x10f8
   __DATA_CONST.__kalloc_type: 0x2c0
-  UUID: 2EC831B3-013C-37E9-99AB-462A51159E9C
-  Functions: 324
+  __DATA_CONST.__auth_got: 0x1f0
+  __DATA_CONST.__got: 0xb8
+  UUID: 8BDE21FE-C193-3B3F-A0E1-1258D32FC69A
+  Functions: 328
   Symbols:   0
-  CStrings:  288
+  CStrings:  289
 
CStrings:
+ "\"[%s::%s] Invalid message read from the FIFO ID %d, interface ID %u, report ID 0x%02X, transfer ID 0x%02X: invalid checksum (read: 0x%08X, calculated: 0x%08X)\" @%s:%d"
+ "\"[%s::%s] Invalid message read from the FIFO ID %d, interface ID %u: header size too large\" @%s:%d"
+ "\"[%s::%s] Invalid message read from the FIFO ID %d, interface ID %u: message exceeds capacity %llu bytes\" @%s:%d"
+ "\"[%s::%s] Invalid message read from the FIFO ID %d, interface ID %u: read beyond message boundary\" @%s:%d"
+ "121111121222121211111211122112111112111121"
+ "Off Without Reset"
+ "ret == kIOReturnSuccess"
- "\"[%s::%s] Invalid message read from the FIFO ID %d: header size too large\" @%s:%d"
- "\"[%s::%s] Invalid message read from the FIFO ID %d: invalid checksum\" @%s:%d"
- "\"[%s::%s] Invalid message read from the FIFO ID %d: message exceeds capacity %llu bytes\" @%s:%d"
- "\"[%s::%s] Invalid message read from the FIFO ID %d: read beyond message boundary\" @%s:%d"
- "12111112122212121111121112211211112111121"
- "ret == 0"

```
