## com.apple.driver.AppleHIDTransportFIFO

> `com.apple.driver.AppleHIDTransportFIFO`

```diff

-8150.1.0.0.0
-  __TEXT.__cstring: 0x2de1
+9100.28.0.0.0
   __TEXT.__const: 0x8
-  __TEXT_EXEC.__text: 0x18190
+  __TEXT.__cstring: 0x2ab9
+  __TEXT_EXEC.__text: 0x16020
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
-  __DATA.__common: 0xd8
+  __DATA.__common: 0x60
   __DATA.__bss: 0x1
-  __DATA_CONST.__auth_got: 0x218
-  __DATA_CONST.__got: 0x138
-  __DATA_CONST.__mod_init_func: 0x28
-  __DATA_CONST.__mod_term_func: 0x28
-  __DATA_CONST.__const: 0x2088
-  __DATA_CONST.__kalloc_type: 0x400
-  UUID: F07E08EC-4017-3328-A43C-C030DF43E8DD
-  Functions: 454
+  __DATA_CONST.__auth_got: 0x1d0
+  __DATA_CONST.__got: 0xb8
+  __DATA_CONST.__mod_init_func: 0x10
+  __DATA_CONST.__mod_term_func: 0x10
+  __DATA_CONST.__const: 0x10a8
+  __DATA_CONST.__kalloc_type: 0x2c0
+  UUID: 7BA34B9A-05C7-31BF-B4AF-26A368E1A3AD
+  Functions: 328
   Symbols:   0
-  CStrings:  330
+  CStrings:  288
 
CStrings:
+ "12111112122212121111111211212111111112121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212122212121121222222222222222222222222222222222222222222222222222222222222212111"
+ "[0x%llx][%llx][%s::%s]: ERROR!! Coudn't allocate stat arrays"
+ "[0x%llx][%llx][%s::%s]: ERROR!! Creating stat array for memory FIFO %d failed"
+ "[0x%llx][%llx][%s::%s]: ERROR!! maxDRAMUsageInLastDay is nullptr"
+ "[0x%llx][%llx][%s::%s]: ERROR!! totalDRAMCapacity is nullptr"
+ "_dramUsageStat"
+ "_maxDRAMUsageInLastDayArray && _totalDRAMCapacityArray"
+ "drainSharedMemoryFifos"
+ "drainSharedMemoryFifosFromThread_block_invoke"
+ "maxDRAMUsageInLastDay"
+ "maxDRAMUsageInLastDay && totalDRAMCapacity"
+ "maxDRAMUsageInLastDayCopy && totalDRAMCapacityCopy"
+ "memoryFifoCount && fifoIds && maxDRAMUsageInLastDayArray && totalDRAMCapacityArray"
+ "provideAndResetDRAMUsageData"
+ "threadLaunched"
+ "totalDRAMCapacity"
- "!_booted"
- "!payload"
- "/Library/Caches/com.apple.xbs/Sources/AppleInputDeviceSupport_kexts/AppleHIDTransport/FIFO/AHTRTBuddyFirmwareService.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleInputDeviceSupport_kexts/AppleHIDTransport/FIFO/AppleHIDTransportBootloaderRTBuddy.cpp"
- "1211111212221212111111111"
- "12111112122212121111111211212111111112121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212122212121121222222222222222222222222222222222222222222222222222222222222212"
- "121111121222121211111121111111111221121111211112"
- "121221"
- "AHTRTBuddyFirmwareService"
- "AHTSCMMessage"
- "AppleDAPF"
- "AppleHIDTransportBootloaderRTBuddy"
- "Build"
- "RTP"
- "RTPM8ALL"
- "Role"
- "Run In Restore"
- "Version"
- "[0x%llx][%llx][%s::%s]: %s = %s"
- "[0x%llx][%llx][%s::%s]: ERROR!! Ignoring unknown image type '%s'"
- "[0x%llx][%llx][%s::%s]: Finished waiting for AppleDAPF"
- "[0x%llx][%llx][%s::%s]: Firmware for %s\n"
- "[0x%llx][%llx][%s::%s]: Found firmware service for %s\n"
- "[0x%llx][%llx][%s::%s]: Found image binary %s (%u bytes)"
- "[0x%llx][%llx][%s::%s]: Loading image with options: 0x%08X"
- "[0x%llx][%llx][%s::%s]: Nothing to do during restore"
- "[0x%llx][%llx][%s::%s]: Skipping image loading since it was already loaded during pre-fdr update"
- "[0x%llx][%llx][%s::%s]: Waiting for AppleDAPF..."
- "_device"
- "_firmware"
- "_firmwareService"
- "_slaveNub"
- "checkNewImage"
- "configString"
- "createFirmware"
- "dapf-parent"
- "dapfParentPhandle"
- "description"
- "firmware"
- "handleLoadImage"
- "hid-merge-personality"
- "initWithData"
- "loadFirmware"
- "matching"
- "no-firmware-service"
- "parentMatching"
- "payload"
- "phandleData"
- "pre-loaded"
- "providerString"
- "role"
- "service"
- "site.AHTRTBuddyFirmwareService"
- "site.AHTSCMMessage"
- "site.AppleHIDTransportBootloaderRTBuddy"
- "site.Header"
- "start"
- "waitForAppleDAPF"

```
