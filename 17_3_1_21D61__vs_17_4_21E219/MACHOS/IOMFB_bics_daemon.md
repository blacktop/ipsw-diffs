## IOMFB_bics_daemon

> `/usr/libexec/IOMFB_bics_daemon`

```diff

-336.3.6.0.0
-  __TEXT.__text: 0x7e64
-  __TEXT.__auth_stubs: 0x7f0
-  __TEXT.__cstring: 0x1f86
-  __TEXT.__gcc_except_tab: 0x90
-  __TEXT.__const: 0x1e8
-  __TEXT.__unwind_info: 0x220
-  __DATA_CONST.__auth_got: 0x400
-  __DATA_CONST.__got: 0x58
+337.5.36.0.0
+  __TEXT.__text: 0x847c
+  __TEXT.__auth_stubs: 0x8b0
+  __TEXT.__cstring: 0x2083
+  __TEXT.__gcc_except_tab: 0xa0
+  __TEXT.__const: 0x2b48
+  __TEXT.__unwind_info: 0x248
+  __TEXT.__eh_frame: 0x38
+  __DATA_CONST.__auth_got: 0x460
+  __DATA_CONST.__got: 0x68
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x3e0
+  __DATA_CONST.__const: 0x420
   __DATA_CONST.__cfstring: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__data: 0xa0

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/AggregateDictionary.framework/AggregateDictionary
+  - /System/Library/PrivateFrameworks/AppleEmbeddedDisplayServices.framework/AppleEmbeddedDisplayServices
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/IOMobileFramebuffer.framework/IOMobileFramebuffer
   - /usr/lib/libMobileGestalt.dylib

   - /usr/lib/libamsupport.dylib
   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 4E278C94-0434-395F-B445-BC66EF7B6692
-  Functions: 145
-  Symbols:   146
-  CStrings:  357
+  UUID: E333A5F1-7F9D-38B3-B0A4-A39F912DF6A8
+  Functions: 157
+  Symbols:   160
+  CStrings:  377
 
Symbols:
+ _BIMUpdaterActivate
+ _BIMUpdaterCancel
+ _BIMUpdaterCreate
+ _BIMUpdaterRead
+ _BIMUpdaterWrite
+ __NSConcreteStackBlock
+ __ZSt9terminatev
+ ___cxa_begin_catch
+ __dispatch_main_q
+ _dispatch_semaphore_create
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
+ _xpc_dictionary_set_double
+ _xpc_dictionary_set_int64
CStrings:
+ ">> BICAB read failed"
+ ">> UA Boost read failed"
+ "BICAB saved"
+ "IOMFB: BIM read version:%u header:%u timestamp:%llu crc:%u"
+ "LTHSaveDispPerfBoostEnable"
+ "Max BIM delta above threshold or below 0"
+ "UA Boost factor not valid"
+ "UA Boost saved"
+ "Unable to connect to BIM storage"
+ "Unable to write BIM to storage"
+ "blue_max"
+ "blue_median"
+ "blue_min"
+ "boost"
+ "com.apple.iomfb.bicab"
+ "com.apple.iomfb.bics-data-health"
+ "com.apple.iomfb.uaboost"
+ "green_max"
+ "green_median"
+ "green_min"
+ "max_bim_delta"
+ "red_max"
+ "red_median"
+ "red_min"
+ "request_disp_perf_boost( %d ) -> %d\n"
+ "uaboost"
+ "v8@?0"
- "AppleEmbeddedTouchEEPROMDriver"
- "BIM region: %llu incorrect size %08zx expected - %08lx read"
- "Can't create Embedded Touch EEPROM Driver dictionary"
- "Can't find EEPROM Driver service"
- "Can't open EEPROM Driver service"
- "Unable to connect to EEPROM"
- "Unable to write BIM to display EEPROM"

```
