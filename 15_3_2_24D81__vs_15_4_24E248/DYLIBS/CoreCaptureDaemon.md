## CoreCaptureDaemon

> `/System/Library/PrivateFrameworks/CoreCaptureDaemon.framework/Versions/A/CoreCaptureDaemon`

```diff

-1210.3.0.0.0
-  __TEXT.__text: 0x39590
-  __TEXT.__auth_stubs: 0x1040
-  __TEXT.__const: 0x518
-  __TEXT.__gcc_except_tab: 0xec
-  __TEXT.__oslogstring: 0x60d3
-  __TEXT.__cstring: 0x73e1
-  __TEXT.__unwind_info: 0x598
+1250.24.0.0.0
+  __TEXT.__text: 0x3bc4c
+  __TEXT.__auth_stubs: 0x1070
+  __TEXT.__const: 0x516
+  __TEXT.__gcc_except_tab: 0x118
+  __TEXT.__oslogstring: 0x680b
+  __TEXT.__cstring: 0x7b0e
+  __TEXT.__unwind_info: 0x5b0
   __TEXT.__objc_classname: 0x1
   __TEXT.__objc_methname: 0x9f
   __TEXT.__objc_stubs: 0x100
   __DATA_CONST.__got: 0x150
-  __DATA_CONST.__const: 0x208
+  __DATA_CONST.__const: 0x228
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x40
-  __AUTH_CONST.__auth_got: 0x830
+  __AUTH_CONST.__auth_got: 0x848
   __AUTH_CONST.__const: 0x10d0
-  __AUTH_CONST.__cfstring: 0x940
+  __AUTH_CONST.__cfstring: 0x960
+  __DATA.__data: 0x1
+  __DATA.__common: 0x4c
   __DATA.__bss: 0x11b
-  __DATA.__common: 0x24
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 2FE9C67F-042C-39EF-B812-F37FF7F95235
-  Functions: 489
-  Symbols:   931
-  CStrings:  1168
+  UUID: 593EDFBC-2FD9-3B5A-91B4-3BAA89757871
+  Functions: 490
+  Symbols:   945
+  CStrings:  1219
 
Symbols:
+ GCC_except_table191
+ GCC_except_table205
+ GCC_except_table275
+ GCC_except_table351
+ GCC_except_table423
+ GCC_except_table485
+ GCC_except_table55
+ GCC_except_table56
+ GCC_except_table61
+ GCC_except_table64
+ __ZL14getCCSessionidPKcmS0_mP11CCTimestampS0_
+ __ZL40fillCaptureDescriptionStringFromMetaDataPcS_m11CCTimestampPKc
+ __ZN18CCLogPipeInterface18dumpToDiskCompleteEP11CCTimestamp
+ __ZN8CCDaemon11fIsCCDaemonE
+ __ZN8CCDaemon11fWorkingDirE
+ __ZN8CCDaemon23initCCDaemonWithOptionsEPKcS1_b
+ __ZN8CCDaemon7ccstartEPKcS1_b
+ __ZN8CCDaemon8fSaveDirE
+ ____ZN5CCTap13freeResourcesEv_block_invoke
+ ____ZN8CCDaemon23initCCDaemonWithOptionsEPKcS1_b_block_invoke
+ __block_descriptor_tmp.1067
+ __block_descriptor_tmp.11
+ __block_descriptor_tmp.1418
+ __block_descriptor_tmp.1622
+ __block_descriptor_tmp.1725
+ __block_descriptor_tmp.1955
+ __block_descriptor_tmp.36
+ __block_descriptor_tmp.513
+ __block_descriptor_tmp.710
+ __block_literal_global.1620
+ __block_literal_global.1916
+ __gQueuePrivateServNotify
+ _clock
+ _fflush
+ _fwrite
+ _startCalled
- GCC_except_table190
- GCC_except_table203
- GCC_except_table273
- GCC_except_table349
- GCC_except_table420
- GCC_except_table482
- GCC_except_table54
- GCC_except_table63
- __ZL40fillCaptureDescriptionStringFromMetaDataPcS_mR13CCLogMetadataPKcmS3_m
- __ZN8CCDaemon4initEv
- __ZN8CCDaemon7ccstartEv
- ____ZN8CCDaemon4initEv_block_invoke
- __block_descriptor_tmp.1018
- __block_descriptor_tmp.1372
- __block_descriptor_tmp.1652
- __block_descriptor_tmp.1881
- __block_descriptor_tmp.27
- __block_descriptor_tmp.471
- __block_descriptor_tmp.665
- __block_descriptor_tmp.9
- __block_literal_global.1431
- __block_literal_global.1842
CStrings:
+ "%s dynamic cast to CCLogPipeInterface failed\n"
+ "%s:%d processEvent entry:%u Owner:%s Name:%s"
+ "CCDaemon::init CoreCaptureStart was already called\n"
+ "CCDaemon::init failed to create come.apple.corecaptured.service_notify\n"
+ "CCDaemon::init invalid arguments passed for non-daemon case\n"
+ "CCDaemon::non daemon cleanup is in progress\n"
+ "CCFIle::copyFile: Unable to stat source path errno %d, reason %s\n"
+ "CCFile::captureLogRun copying files took %f seconds\n"
+ "CCFile::copyFile Failed to open source file:%s errno %d, reason %s\n"
+ "CCFile::copyFile Unable to stat dest path errno = %d, reason %s\n"
+ "CCFile::copyFile written bytes 0 \n"
+ "CCFile::initWithTap Failed to create log directory  %s\n"
+ "CCFile::initWithTap Failed to get log directory \n"
+ "CCFile::initWithTap create with cstring failed\n"
+ "CCFile::initWithTap fLogDirPath is invalid\n"
+ "CCFile::initWithTap memory allocation failed\n"
+ "CCFile::writeDataFiles memory allocation failed\n"
+ "CCProfileMonitor 10 seconds since CCProfileMonitor initted, calling profileCallback(1) to check for installed profiles\n"
+ "CCProfileMonitor got com.apple.ManagedConfiguration.profileListChanged update, calling profileCallback(%d)\n"
+ "CCProfileMonitor::applyProfile fProfileLoaded is not set, not applying owner:%s, pipe:%s\n"
+ "CCProfileMonitor::profileCallback exiting states shutDownPending %d fProfileLoaded %d fProfileRemoveApplied %d\n"
+ "CCProfileMonitor::profileCallback fKeyCount=0 fProfileLoaded:%d Removed\n"
+ "CCProfileMonitor::profileCallback fProfileLoaded is true, exiting\n"
+ "CCProfileMonitor::profileCallback failed to get fMutex, exiting \n"
+ "CCProfileMonitor::profileCallback setting removeProfile, exiting\n"
+ "CCProfileMonitor::profileCallback starting states shutDownPending %d fProfileLoaded %d fProfileRemoveApplied %d\n"
+ "CCProfileMonitor::profileCallback:%d removePending token:%d fProfileLoaded:%d fProfileRemoveApplied:%d, setting removeProfile, exiting\n"
+ "CCProfileMonitor::setStreamEventHandler calling profileCallback(1)\n"
+ "CCProfileMonitor::setStreamEventHandler event received matching kXPCManagedPrefsName, no action from this handler\n"
+ "CCProfileMonitor::setStreamEventHandler eventType unhandled:%@"
+ "CompressionDisabled"
+ "Notification to dump to disk failed for entry:%u"
+ "come.apple.corecaptured.service_notify"
+ "fopen failed errno = %d, reason : %s\n"
+ "getting CC session id failed for entry:%u"
+ "gzflush error code = %d\n"
+ "gzflush failed errno = %d, errnum = %d, reason : %s, %s\n"
+ "gzopen failed errno = %d, reason : %s\n"
- "%s\n"
- "%s:%d MADHU processEvent entry:%u Owner:%s Name:%s"
- "."
- ".."
- "CCFIle::copyFile: Unable to stat source path\n"
- "CCFile::copyFile Failed to open source file:%s\n"
- "CCFile::copyFile Unable to stat dest path\n"
- "CCFile::initWithTap Failed to create  %s\n"
- "CCProfileMonitor::profileCallback Removed\n"
- "CCProfileMonitor::profileCallback fProfileLoaded is true\n"
- "CCProfileMonitor::profileCallback fProfileLoaded:%d Removed\n"
- "CCProfileMonitor::profileCallback:%d removePending token:%d fProfileLoaded:%d fProfileRemoveApplied:%d\n"
- "S"

```
