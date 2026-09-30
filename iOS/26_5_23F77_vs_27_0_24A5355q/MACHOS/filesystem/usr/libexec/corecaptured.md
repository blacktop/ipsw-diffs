## corecaptured

> `/usr/libexec/corecaptured`

```diff

-1330.5.0.0.0
-  __TEXT.__text: 0x25c sha256:44a80c38f9c67063dabfa5c66ff44641936cd48649cdbaf6bf7d7cd88ae2132b
-  __TEXT.__auth_stubs: 0xc0 sha256:6da9e6d49f959b62af4f950e1705253b5e9ff3e280e7a3ba2d256c710e9bca41
-  __TEXT.__cstring: 0x3d sha256:a3027051f5fde592549b444efa750806f5f7ef0500829c01bbc242888a5ccd3d
-  __TEXT.__oslogstring: 0xe sha256:6f16db08a55b483e9f01f65f0c52ddda38e09dbaf4a2871a55602b7814f0fcf4
-  __TEXT.__unwind_info: 0x60 sha256:cdc70d558b49a1ccaa0a644b262add2b8d20901347a4d4c146a948d4f1e598c0
-  __DATA_CONST.__auth_got: 0x60 sha256:75443b2d7eb304af704e135ce779b1582e40b4e112f49dba1aedc8490c781a2a
-  __DATA_CONST.__got: 0x20 sha256:b326b40f269ff6947f06040b870b6b366b39ef6ca69954dbbdaf1ca1a9635a0d
+1355.39.0.0.0
+  __TEXT.__text: 0x114 sha256:6069bdfdf8f43c08500833d23b1e14e32810a0f3b98060580aedd9b93cc0e4b0
+  __TEXT.__auth_stubs: 0x50 sha256:83f3889bd9c58f1912d0e9c6e7f09ca8a93629f0d7517c03e6a073a38a706b57
+  __TEXT.__cstring: 0x1c sha256:832f02672f293fb152dd06e8b79e5954c21e26931e5e3d69b7f5cb35724b7fb1
+  __TEXT.__unwind_info: 0x60 sha256:4ebc2600bcd695969dd064ac7758b071f2840251c50988dca795f1292ec0cef2
+  __DATA_CONST.__auth_got: 0x28 sha256:2b562e0c5d98e3f426fec6485d45f8f78ef02f706019712f97d8b7deac86b17e
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
~ sub_1000006c8 -> sub_100000628 : sha256 d73e5f42271d748651c8b534326177708dd7435c099554af327304e378cb41fc -> 23ec383fa49a16aa391ae0ab422066c0807c870026c1b1b29b221cb1f4755029
~ sub_100000758 -> sub_1000006b8 : 460 -> 132
CStrings:
- "%b %d %H:%M:%S"
- "%s "
- "SIGBUS DEATH\n"

```
