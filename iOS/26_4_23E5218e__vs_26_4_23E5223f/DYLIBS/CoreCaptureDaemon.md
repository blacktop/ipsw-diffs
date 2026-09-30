## CoreCaptureDaemon

> `/System/Library/PrivateFrameworks/CoreCaptureDaemon.framework/CoreCaptureDaemon`

```diff

-1325.17.0.0.0
-  __TEXT.__text: 0x45a7c
-  __TEXT.__auth_stubs: 0x11f0
+1325.18.0.0.0
+  __TEXT.__text: 0x472e8
+  __TEXT.__auth_stubs: 0x1250
   __TEXT.__const: 0x518
-  __TEXT.__gcc_except_tab: 0x2d8
-  __TEXT.__oslogstring: 0x78f8
-  __TEXT.__cstring: 0x8f69
-  __TEXT.__unwind_info: 0x670
+  __TEXT.__gcc_except_tab: 0x2cc
+  __TEXT.__oslogstring: 0x7c39
+  __TEXT.__cstring: 0x930f
+  __TEXT.__unwind_info: 0x680
   __TEXT.__objc_classname: 0x1
-  __TEXT.__objc_methname: 0x11b
-  __TEXT.__objc_stubs: 0x1a0
+  __TEXT.__objc_methname: 0x131
+  __TEXT.__objc_stubs: 0x1c0
   __DATA_CONST.__got: 0x168
   __DATA_CONST.__const: 0x368
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x68
-  __AUTH_CONST.__auth_got: 0x908
-  __AUTH_CONST.__const: 0x1108
-  __AUTH_CONST.__cfstring: 0xb60
+  __DATA_CONST.__objc_selrefs: 0x70
+  __AUTH_CONST.__auth_got: 0x938
+  __AUTH_CONST.__const: 0x1168
+  __AUTH_CONST.__cfstring: 0xc40
   __DATA.__data: 0x1
   __DATA.__common: 0x3c
-  __DATA.__bss: 0x178
+  __DATA.__bss: 0x188
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/PrivateFrameworks/CacheDelete.framework/CacheDelete
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 9C4CB9EB-34EF-3A1D-B4AB-69FC699A6FAF
-  Functions: 522
-  Symbols:   1135
-  CStrings:  1421
+  UUID: 5E8077DE-09F1-3764-A081-896321310886
+  Functions: 530
+  Symbols:   1158
+  CStrings:  1467
 
Symbols:
+ GCC_except_table152
+ GCC_except_table208
+ GCC_except_table223
+ GCC_except_table270
+ GCC_except_table337
+ GCC_except_table338
+ GCC_except_table383
+ GCC_except_table394
+ GCC_except_table395
+ GCC_except_table397
+ GCC_except_table399
+ GCC_except_table400
+ GCC_except_table460
+ GCC_except_table525
+ GCC_except_table70
+ GCC_except_table73
+ _CCCacheDeleteDisablePurgeNotification
+ _CCCacheDeleteEnablePurgeNotification
+ _CFArrayCreate
+ _CFArrayCreateCopy
+ _CacheDeleteEnumerateRemovedFilesInDirectories
+ _CacheDeleteInitPurgeMarker
+ _CacheDeleteRegisterPurgeNotification
+ __ZL19processRemovedFilesPK9__CFArray
+ __ZL20monitoredDirectories
+ __ZL28purgeNotificationInitialized
+ __ZN8CCDaemon23enablePurgeNotificationEv
+ __ZN8CCDaemon24disablePurgeNotificationEv
+ __ZNSt3__15dequeI14StackshotEntryNS_9allocatorIS1_EEED2B9nqe210106Ev
+ __ZNSt3__19allocatorIP14StackshotEntryE17allocate_at_leastB9nqe210106Em
+ __ZSt28__throw_bad_array_new_lengthB9nqe210106v
+ ___CCCacheDeleteDisablePurgeNotification_block_invoke
+ ___CCCacheDeleteEnablePurgeNotification_block_invoke
+ ___CCCacheDeleteEnablePurgeNotification_block_invoke.15
+ ___CCCacheDeleteEnablePurgeNotification_block_invoke_2
+ ___block_descriptor_32_e20_v16?0^{__CFArray=}8l
+ ___block_descriptor_tmp.168
+ ___block_descriptor_tmp.1884
+ ___block_descriptor_tmp.2036
+ ___block_descriptor_tmp.2309
+ ___block_descriptor_tmp.2428
+ ___block_descriptor_tmp.28
+ ___block_descriptor_tmp.401
+ ___block_descriptor_tmp.48
+ ___block_descriptor_tmp.57
+ ___block_descriptor_tmp.841
+ ___block_literal_global.1160
+ ___block_literal_global.13
+ ___block_literal_global.1306
+ ___block_literal_global.151
+ ___block_literal_global.156
+ ___block_literal_global.17
+ ___block_literal_global.20
+ ___block_literal_global.2250
+ ___block_literal_global.26
+ ___block_literal_global.836
+ _ffsctl
+ _objc_msgSend$unsignedLongLongValue
- GCC_except_table150
- GCC_except_table206
- GCC_except_table221
- GCC_except_table268
- GCC_except_table328
- GCC_except_table329
- GCC_except_table374
- GCC_except_table385
- GCC_except_table386
- GCC_except_table388
- GCC_except_table390
- GCC_except_table391
- GCC_except_table452
- GCC_except_table517
- GCC_except_table69
- GCC_except_table72
- __ZNSt3__132__internal_log_hardening_failureEPKc
- __ZNSt3__15dequeI14StackshotEntryNS_9allocatorIS1_EEED2B9foe210106Ev
- __ZNSt3__19allocatorIP14StackshotEntryE17allocate_at_leastB9foe210106Em
- __ZSt28__throw_bad_array_new_lengthB9foe210106v
- ____ZN5CCTap13freeResourcesEv_block_invoke
- ___block_descriptor_tmp.160
- ___block_descriptor_tmp.1806
- ___block_descriptor_tmp.1867
- ___block_descriptor_tmp.1960
- ___block_descriptor_tmp.2234
- ___block_descriptor_tmp.2353
- ___block_descriptor_tmp.29
- ___block_descriptor_tmp.393
- ___block_descriptor_tmp.44
- ___block_descriptor_tmp.53
- ___block_descriptor_tmp.819
- ___block_literal_global.1232
- ___block_literal_global.148
- ___block_literal_global.153
- ___block_literal_global.1865
- ___block_literal_global.2174
- ___block_literal_global.27
- ___block_literal_global.814
CStrings:
+ "/private/var"
+ "CCCacheDelete: cannot create monitored directories\n"
+ "CCCacheDelete: cannot register for purge notifications ret=0x%x\n"
+ "CCCacheDelete: file purged: %s (inode: %llu)\n"
+ "CCCacheDelete: framework not available on this platform\n"
+ "CCCacheDelete: no directories provided\n"
+ "CCCacheDelete: purge history lost, rescan needed\n"
+ "CCCacheDelete: purge history processing complete\n"
+ "CCCacheDelete: purge notification already enabled\n"
+ "CCCacheDelete: purge notification disabled\n"
+ "CCCacheDelete: purge notification enabled\n"
+ "CCDaemon::enablePurgeNotification failed to create CFString for other save location\n"
+ "CCDaemon::enablePurgeNotification failed to create CFString for save location\n"
+ "CCDaemon::enablePurgeNotification failed to get save location\n"
+ "Failed to get fCaptureDirPath for purgeable marking\n"
+ "Failed to mark %s as purgeable %d (%s) (flags 0x%llx)\n"
+ "Reason"
+ "com.apple.corecaptured.purge"
+ "fileID"
+ "historyDone"
+ "path"
+ "rescan"
+ "unsignedLongLongValue"
+ "v16@?0^{__CFArray=}8"

```
