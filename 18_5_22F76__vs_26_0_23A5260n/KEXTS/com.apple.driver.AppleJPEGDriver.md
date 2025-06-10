## com.apple.driver.AppleJPEGDriver

> `com.apple.driver.AppleJPEGDriver`

```diff

-7.6.8.0.0
-  __TEXT.__cstring: 0x26fd
-  __TEXT.__os_log: 0x8506
-  __TEXT.__const: 0x34b4
-  __TEXT_EXEC.__text: 0x2914c
+7.7.1.0.0
+  __TEXT.__cstring: 0x2750
+  __TEXT.__os_log: 0x89a4
+  __TEXT.__const: 0x34d4
+  __TEXT_EXEC.__text: 0x29eac
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x2108
+  __DATA.__data: 0x2208
   __DATA.__common: 0x358
   __DATA.__bss: 0x1
-  __DATA_CONST.__auth_got: 0x350
+  __DATA_CONST.__auth_got: 0x340
   __DATA_CONST.__got: 0x98
   __DATA_CONST.__mod_init_func: 0xa8
   __DATA_CONST.__mod_term_func: 0xa8
   __DATA_CONST.__const: 0x4578
-  __DATA_CONST.__kalloc_type: 0xbc0
-  UUID: 1D62F748-4FCB-3461-87BB-387C3CFC88AE
-  Functions: 1590
+  __DATA_CONST.__kalloc_type: 0xb40
+  UUID: 1095EEF4-3593-3A62-932A-532B1FAF0288
+  Functions: 1596
   Symbols:   0
-  CStrings:  465
+  CStrings:  490
 
CStrings:
+ "1111111"
+ "1122211111111122121122222222212222222222222222222222222222222222222222222222222222222221111222221122222222222222212222222122222222222222"
+ "1221111111111111221122222222122222"
+ "AppleJPEGDriver: %s : codec %d, RegisterMemoryMap %p, Device Memory Count = %u\n"
+ "AppleJPEGDriver: %s : createInterruptEventSource failed!\n"
+ "AppleJPEGDriver: %s(): Core Analyzer start() failed with %d!\n"
+ "AppleJPEGDriver: %s(): DART registerMapper() failed with %d!\n"
+ "AppleJPEGDriver: %s(): Device Memory Count is 0!\n"
+ "AppleJPEGDriver: %s(): ERROR: start function failed for codec num %u [provider = %p this = %p]\n"
+ "AppleJPEGDriver: %s(): Enter enableDeviceClockWrapper(en = %u, idx = %u)\n"
+ "AppleJPEGDriver: %s(): Error! Call failed (enable = %u, index = %u) with %d\n"
+ "AppleJPEGDriver: %s(): Failed to alloc mpQueueLock!\n"
+ "AppleJPEGDriver: %s(): Failed to initialize mCodecHal[%u]!\n"
+ "AppleJPEGDriver: %s(): Forcing clock speed to %u\n"
+ "AppleJPEGDriver: %s(): HW version read from register 0x%x does not match EDT value 0x%x\n"
+ "AppleJPEGDriver: %s(): IOService start() method failed!\n"
+ "AppleJPEGDriver: %s(): Invalid codec number %u >= %u!\n"
+ "AppleJPEGDriver: %s(): NULL JPEG register memory map!\n"
+ "AppleJPEGDriver: %s(): NULL JPEG request object (from queue %u)!\n"
+ "AppleJPEGDriver: %s(): NULL mCodecHal[%u]!\n"
+ "AppleJPEGDriver: %s(): NULL mCommandGate!\n"
+ "AppleJPEGDriver: %s(): NULL mCommandQueueManager!\n"
+ "AppleJPEGDriver: %s(): NULL mCoreAnalyzer!\n"
+ "AppleJPEGDriver: %s(): NULL mIOSurfaceRoot!\n"
+ "AppleJPEGDriver: %s(): NULL mJpegDart!\n"
+ "AppleJPEGDriver: %s(): NULL mJpegPM!\n"
+ "AppleJPEGDriver: %s(): NULL mRequestHandler!\n"
+ "AppleJPEGDriver: %s(): NULL mWorkLoop!\n"
+ "AppleJPEGDriver: %s(): NULL power provider!\n"
+ "AppleJPEGDriver: %s(): Power manager registerPU() failed with %d!\n"
+ "AppleJPEGDriver: %s(): Skipping call to enableDeviceClockLowLevel(en = %u, idx = %u)\n"
+ "AppleJPEGDriver: %s(): Successfully added codec num %u [%p]\n"
+ "AppleJPEGDriver: %s(): enableDeviceClock(en = %u, idx = %u) returned %d\n"
+ "AppleJPEGDriver: %s(): enablePsdService(en = %u) returned %d\n"
+ "AppleJPEGDriver: %s(): getNodeIndex() failed with %d!\n"
+ "AppleJPEGDriver: %s(): queue[%d] is empty\n"
+ "QueueManager"
+ "com.apple.applejpegdriver.ajpegtestapp"
+ "deQueue"
+ "enableDeviceClockLowLevel"
+ "fullSpeedRequestExist"
+ "init"
+ "start"
+ "turnOnJPEGHW_gated"
- "111111"
- "11222111111111221211222222221222222222222222222222222222222222222222222222222222222222111122222112222222222222212222222122222222222222"
- "122111111111111122112222222122222"
- "AppleJPEGDriver: %s : codec %d, RegisterMemoryMap %p\n"
- "AppleJPEGDriver: ** %s : HW version read from register 0x%x does not match EDT value 0x%x"
- "AppleJPEGDriver: ** %s : PU initialized fail (codec %d) with code %d"
- "AppleJPEGDriver: ** %s : mCommandQueueManager alloc fail"
- "AppleJPEGDriver: ** %s : mCoreAnalyzer alloc fail"
- "AppleJPEGDriver: ** %s : mCoreAnalyzer start fail 0x%x"
- "AppleJPEGDriver: ** %s : mJpegDart %p initialized fail with code %d"
- "AppleJPEGDriver: ** %s : mJpegDart alloc fail"
- "AppleJPEGDriver: ** %s : mJpegPM alloc fail"
- "AppleJPEGDriver: ** %s : mRequestHandler alloc fail"
- "AppleJPEGDriver: ** %s [%p] ERROR: start(%p) function fail\n"
- "AppleJPEGDriver: - %s : queue is empty\n"
- "AppleJPEGDriver: - %s [%p] : added codec num %d, returns %d"
- "ajpeg_setup_t *QueueManager::deQueue(uint32_t)"
- "jpeg"
- "jpeg%d"

```
