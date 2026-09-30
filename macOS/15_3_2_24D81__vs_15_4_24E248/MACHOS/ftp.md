## ftp

> `/System/Library/Filesystems/NetFSPlugins/ftp.bundle/Contents/MacOS/ftp`

```diff

-19.0.0.0.0
-  __TEXT.__text: 0x17bc
+20.0.0.0.0
+  __TEXT.__text: 0x17ac
   __TEXT.__auth_stubs: 0x3f0
   __TEXT.__cstring: 0x52c
-  __TEXT.__unwind_info: 0x98
+  __TEXT.__unwind_info: 0xa0
   __DATA_CONST.__auth_got: 0x1f8
   __DATA_CONST.__got: 0x38
   __DATA_CONST.__cfstring: 0x340

   - /System/Library/Frameworks/SystemConfiguration.framework/Versions/A/SystemConfiguration
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  UUID: D942776B-601F-3942-A1D0-EECB4AC2D09D
+  UUID: 911C66BB-2345-3B85-B551-0AF3323021C2
   Functions: 15
   Symbols:   86
   CStrings:  106
Functions:
~ _FTP_CreateSessionRef : 296 -> 284
~ _FTP_OpenSession : 512 -> 516
~ _FTP_Mount : 2028 -> 2024
~ _FTP_CloseSession : 228 -> 224

```
