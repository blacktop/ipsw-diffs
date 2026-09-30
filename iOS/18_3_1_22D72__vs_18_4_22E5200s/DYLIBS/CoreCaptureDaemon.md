## CoreCaptureDaemon

> `/System/Library/PrivateFrameworks/CoreCaptureDaemon.framework/CoreCaptureDaemon`

```diff

-1215.5.0.0.0
-  __TEXT.__text: 0x37370
-  __TEXT.__auth_stubs: 0xf30
-  __TEXT.__const: 0x4f0
-  __TEXT.__gcc_except_tab: 0xa0
-  __TEXT.__oslogstring: 0x5c3f
-  __TEXT.__cstring: 0x6eda
-  __TEXT.__unwind_info: 0x588
+1255.30.0.0.0
+  __TEXT.__text: 0x38e50
+  __TEXT.__auth_stubs: 0xf50
+  __TEXT.__const: 0x4e8
+  __TEXT.__gcc_except_tab: 0xcc
+  __TEXT.__oslogstring: 0x5fd4
+  __TEXT.__cstring: 0x72a3
+  __TEXT.__unwind_info: 0x598
   __TEXT.__objc_classname: 0x1
   __TEXT.__objc_methname: 0x9f
   __TEXT.__objc_stubs: 0x100
   __DATA_CONST.__got: 0x138
-  __DATA_CONST.__const: 0x1f0
+  __DATA_CONST.__const: 0x210
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x40
-  __AUTH_CONST.__auth_got: 0x7a8
-  __AUTH_CONST.__const: 0xff8
-  __AUTH_CONST.__cfstring: 0x940
-  __DATA.__bss: 0x11b
-  __DATA.__common: 0x24
+  __AUTH_CONST.__auth_got: 0x7b8
+  __AUTH_CONST.__const: 0x1018
+  __AUTH_CONST.__cfstring: 0x960
+  __DATA.__data: 0x1
+  __DATA.__common: 0x4c
+  __DATA.__bss: 0x11a
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 469
-  Symbols:   840
-  CStrings:  1047
+  Functions: 470
+  Symbols:   851
+  CStrings:  1080
 
Symbols:
+ __ZN18CCLogPipeInterface18dumpToDiskCompleteEP11CCTimestamp
+ __ZN8CCDaemon11fIsCCDaemonE
+ __ZN8CCDaemon11fWorkingDirE
+ __ZN8CCDaemon23initCCDaemonWithOptionsEPKcS1_b
+ __ZN8CCDaemon7ccstartEPKcS1_b
+ __ZN8CCDaemon8fSaveDirE
+ __gQueuePrivateServNotify
+ _clock
+ _fflush
+ _fwrite
+ _startCalled
- __ZN8CCDaemon4initEv
- __ZN8CCDaemon7ccstartEv
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
- "S"

```
