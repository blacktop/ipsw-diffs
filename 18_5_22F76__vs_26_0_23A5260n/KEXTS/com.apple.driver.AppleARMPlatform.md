## com.apple.driver.AppleARMPlatform

> `com.apple.driver.AppleARMPlatform`

```diff

-1066.100.11.0.0
-  __TEXT.__const: 0x1778
+1103.0.2.0.0
+  __TEXT.__const: 0x17f8
   __TEXT.__os_log: 0x14f3
-  __TEXT.__cstring: 0xcca7
-  __TEXT_EXEC.__text: 0x551ec
+  __TEXT.__cstring: 0xcf63
+  __TEXT_EXEC.__text: 0x57c20
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x6c8
-  __DATA.__common: 0xca0
+  __DATA.__common: 0xcc8
   __DATA.__bss: 0x69
-  __DATA_CONST.__auth_got: 0x660
+  __DATA_CONST.__auth_got: 0x670
   __DATA_CONST.__got: 0x1e8
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x128
   __DATA_CONST.__mod_term_func: 0x128
-  __DATA_CONST.__const: 0x16390
-  __DATA_CONST.__kalloc_var: 0x140
-  __DATA_CONST.__kalloc_type: 0x1540
-  UUID: 20FE7225-0128-312E-A3B5-018373D802CB
-  Functions: 2130
+  __DATA_CONST.__const: 0x16a70
+  __DATA_CONST.__kalloc_var: 0x370
+  __DATA_CONST.__kalloc_type: 0x1580
+  UUID: 4BA16EC3-BDF9-3006-9716-1EA595FBAB5D
+  Functions: 2158
   Symbols:   0
-  CStrings:  1705
+  CStrings:  1732
 
CStrings:
+ "\"Illegal config in %s EDT entry, no wakeup-data\\n\" @%s:%d"
+ "%s: %d.%06d [%3dus] %c %02X %2dB device: %0llX state %04X (%s)\n"
+ "%s: iicWakeDeviceCount=%u\n"
+ "%s: inputSize=%#x, outputSize=%#x\n"
+ "%s: no reg prop\n"
+ "%s: parent not SPI controller\n"
+ "%s: reg too short\n"
+ "%s: selector=%u\n"
+ "%s: setSPIConfig ret=%08x\n"
+ "%s: super::init failed\n"
+ "%s:iicWakeData #%d- reg=0x%02x, interval=0x%08x, delay=0x%08x\n"
+ "%s[%s]:%s:%u - Error erasing %#x sector - %#x\n"
+ "%s[%s]:%s:%u - Error erasing block @ sector %#x - %#x\n"
+ "%s[%s]:%s:%u - Error programming %#x sector - %#x\n"
+ "%s[%s]:%s:%u - Error transferring data at %#x offset - %#x\n"
+ "%s[%s]:%s:%u - JEDEC ID: %#x\n"
+ "%s[%s]:%s:%u - SPI Flash status busy - error %#x\n"
+ "%s[%s]:%s:%u - SPI Flash status write enable %d - error %#x\n"
+ "%s[%s]:%s:%u - WRSR(%#02x), pre=%#02x, post=%#02x\n"
+ "%s[%s]:%s:%u - _programBytes error, ret=%#x\n"
+ "%s[%s]:%s:%u - cannot be locked\n"
+ "%s[%s]:%s:%u - disabling quad writes\n"
+ "%s[%s]:%s:%u - invalid - length: %#x offset: %#x\n"
+ "%s[%s]:%s:%u - invalid length\n"
+ "%s[%s]:%s:%u - status: %#08x, waiting for mask %#0x to clear\n"
+ "%s[%s]:%s:%u - unaligned - length: %#x offset: %#x\n"
+ "%s[%s]:%s:%u - unknown JEDEC ID: %#x\n"
+ "%s[%s]:%s:%u - writes unsupported\n"
+ "121111121222121211212121211212121"
+ "121111121222121211222112111122111"
+ "121111121222121211222112111122111112"
+ "AppleARMIIC.cpp"
+ "AppleARMSPIDeviceUserClient"
+ "Found nameString: %s\n"
+ "Unable to enablePsdService, result=%08x\n"
+ "com.apple.driver.spi.device.user-access"
+ "disable-quad-writes"
+ "iicLogBuf == nullptr\n"
+ "sMethodExtTransfer"
+ "service-gates"
+ "service-name"
+ "service-reset"
+ "site.AbsoluteTime"
+ "site.AppleARMIICDevice *"
+ "site.AppleARMSPIDeviceUserClient"
+ "site.IICWakeInfo"
+ "site.char"
- "%s: %d.%06d [%3dms] %c %02X %2dB device: %0llX state %04X (%s)\n"
- "%s:%s:%u - Error erasing %#x sector - %#x\n"
- "%s:%s:%u - Error erasing block @ sector %#x - %#x\n"
- "%s:%s:%u - Error programming %#x sector - %#x\n"
- "%s:%s:%u - Error transferring data at %#x offset - %#x\n"
- "%s:%s:%u - SPI Flash status busy - error %#x\n"
- "%s:%s:%u - SPI Flash status write enable %d - error %#x\n"
- "%s:%s:%u - WRSR(%#02x), pre=%#02x, post=%#02x\n"
- "%s:%s:%u - _programBytes error, ret=%#x\n"
- "%s:%s:%u - invalid - length: %#x offset: %#x\n"
- "%s:%s:%u - invalid length\n"
- "%s:%s:%u - status: %#08x, waiting for mask %#0x to clear\n"
- "%s:%s:%u - writes unsupported\n"
- "%s:iicWakeData - reg=0x%02x, interval=0x%08x, delay=0x%08x\n"
- "121111121222121211212121211"
- "121111121222121211222112111121222"
- "121111121222121211222112111121222112"
- "AppleARMSPIFlashController::_identifyNORDevice read JEDEC ID: %#x\n"
- "AppleARMSPIFlashController::_identifyNORDevice unknown JEDEC ID: %#x\n"
- "No wakeup-data!!\n"

```
