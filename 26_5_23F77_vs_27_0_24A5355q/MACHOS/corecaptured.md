## corecaptured

> `/usr/libexec/corecaptured`

```diff

-1330.5.0.0.0
-  __TEXT.__text: 0x25c
-  __TEXT.__auth_stubs: 0xc0
-  __TEXT.__cstring: 0x3d
-  __TEXT.__oslogstring: 0xe
+1355.39.0.0.0
+  __TEXT.__text: 0x114
+  __TEXT.__auth_stubs: 0x50
+  __TEXT.__cstring: 0x1c
   __TEXT.__unwind_info: 0x60
-  __DATA_CONST.__auth_got: 0x60
-  __DATA_CONST.__got: 0x20
+  __DATA_CONST.__auth_got: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/CoreCaptureDaemon.framework/CoreCaptureDaemon
   - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: F2A1ABF0-CCF0-3C7F-AE7E-8945542C3CB9
+  UUID: A6E0CD7A-6D73-3D38-8667-A2E1F36DCDF2
   Functions: 2
-  Symbols:   18
-  CStrings:  5
+  Symbols:   7
+  CStrings:  1
 
Symbols:
- ___stack_chk_fail
- ___stack_chk_guard
- __os_log_default
- __os_log_impl
- _coreCaptureOsLog
- _dprintf
- _glog_fd
- _localtime_r
- _os_log_type_enabled
- _strftime
- _time
Functions:
~ sub_100000758 -> sub_1000006b8 : 460 -> 132
CStrings:
- "%b %d %H:%M:%S"
- "%s "
- "SIGBUS DEATH\n"

```
