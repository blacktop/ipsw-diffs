## CoreCaptureDaemon

> `/System/Library/PrivateFrameworks/CoreCaptureDaemon.framework/CoreCaptureDaemon`

```diff

-1325.18.0.0.0
-  __TEXT.__text: 0x47380
+1330.3.0.0.0
+  __TEXT.__text: 0x47134
   __TEXT.__auth_stubs: 0x1260
   __TEXT.__const: 0x518
   __TEXT.__gcc_except_tab: 0x2cc
-  __TEXT.__oslogstring: 0x7c39
-  __TEXT.__cstring: 0x930f
-  __TEXT.__unwind_info: 0x680
+  __TEXT.__oslogstring: 0x7ad7
+  __TEXT.__cstring: 0x91c1
+  __TEXT.__unwind_info: 0x688
   __TEXT.__objc_classname: 0x1
   __TEXT.__objc_methname: 0x131
   __TEXT.__objc_stubs: 0x1c0
   __DATA_CONST.__got: 0x168
-  __DATA_CONST.__const: 0x368
+  __DATA_CONST.__const: 0x388
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x70
   __AUTH_CONST.__auth_got: 0x940

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 4B82F087-B611-33FE-84E8-6FA57E591BA1
-  Functions: 530
-  Symbols:   1159
-  CStrings:  1467
+  UUID: C67C9425-3ACE-3E29-A24A-C106430F317E
+  Functions: 532
+  Symbols:   1163
+  CStrings:  1463
 
Symbols:
+ GCC_except_table272
+ GCC_except_table339
+ GCC_except_table340
+ GCC_except_table385
+ GCC_except_table396
+ GCC_except_table401
+ GCC_except_table402
+ GCC_except_table462
+ GCC_except_table527
+ __ZN15CCPipeInterface25cancelNotificationSourcesEv
+ __ZN8CCLogTap12processEventEP18CCLogPipeInterface
+ __ZN9CCDataTap12processEventEP19CCDataPipeInterface
+ ____ZN15CCPipeInterface25cancelNotificationSourcesEv_block_invoke
+ ____ZN15CCPipeInterface25cancelNotificationSourcesEv_block_invoke_2
+ ___block_descriptor_tmp.14
+ ___block_descriptor_tmp.1878
+ ___block_descriptor_tmp.2030
+ ___block_descriptor_tmp.2303
+ ___block_descriptor_tmp.24
+ ___block_descriptor_tmp.2422
+ ___block_literal_global.1154
+ ___block_literal_global.1300
+ ___block_literal_global.2244
+ ___block_literal_global.842
+ _mach_port_mod_refs
- GCC_except_table270
- GCC_except_table337
- GCC_except_table338
- GCC_except_table383
- GCC_except_table394
- GCC_except_table395
- GCC_except_table400
- GCC_except_table460
- GCC_except_table525
- __ZN8CCLogTap12processEventEv
- __ZN9CCDataTap12processEventEv
- __ZZ12isSeedAndiOSE10bootArgSet
- ____ZN15CCPipeInterface13freeResourcesEv_block_invoke
- ___block_descriptor_tmp.1884
- ___block_descriptor_tmp.2036
- ___block_descriptor_tmp.23
- ___block_descriptor_tmp.2309
- ___block_descriptor_tmp.2428
- ___block_literal_global.1160
- ___block_literal_global.1306
- ___block_literal_global.2250
- ___block_literal_global.836
CStrings:
+ "CCDataTap::%s invalid dataPipeInterface\n"
+ "CCDataTap::%s:%d cast failed\n"
+ "CCLogTap::%s invalid logPipeInterface\n"
+ "IOReturn CCLogTap::processEvent(CCLogPipeInterface *)"
- "%s dynamic cast to CCLogPipeInterface failed\n"
- "IOReturn CCLogTap::processEvent()"
- "_dataTapInterestCallback_dext called when CCDaemon::getInstance().isShutdownPending() == true, ignoring\n"
- "_dataTapInterestCallback_kext called when CCDaemon::getInstance().isShutdownPending() == true, ignoring\n"
- "_logTapInterestCallback_dext called when CCDaemon::getInstance().isShutdownPending() == true, ignoring\n"
- "_logTapInterestCallback_kext called when CCDaemon::getInstance().isShutdownPending() == true, ignoring\n"

```
