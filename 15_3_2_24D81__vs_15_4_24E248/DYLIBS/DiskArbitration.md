## DiskArbitration

> `/System/Library/Frameworks/DiskArbitration.framework/Versions/A/DiskArbitration`

```diff

-490.81.1.0.0
-  __TEXT.__text: 0x6e3c
-  __TEXT.__auth_stubs: 0x7d0
+490.100.20.0.1
+  __TEXT.__text: 0x6bf4
+  __TEXT.__auth_stubs: 0x7c0
   __TEXT.__cstring: 0x7ed
-  __TEXT.__const: 0x98
+  __TEXT.__const: 0x90
   __TEXT.__oslogstring: 0x89
   __TEXT.__unwind_info: 0x240
-  __DATA_CONST.__got: 0x98
+  __DATA_CONST.__got: 0x88
   __DATA_CONST.__const: 0x320
-  __AUTH_CONST.__auth_got: 0x3e8
+  __AUTH_CONST.__auth_got: 0x3e0
   __AUTH_CONST.__const: 0xc0
   __AUTH_CONST.__cfstring: 0x9c0
   __DATA.__data: 0x68

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /usr/lib/libSystem.B.dylib
-  UUID: 5B54B140-0055-302C-94FE-06522FB8A1E8
-  Functions: 164
-  Symbols:   399
+  UUID: 3DEF7AF6-B023-3BAB-9D5C-D0267DC469CD
+  Functions: 163
+  Symbols:   397
   CStrings:  216
 
Symbols:
- __DAServerDiskSetEncoding
- _strrchr
Functions:
~ _DAAddCallbackToSession : 204 -> 200
~ __DAServerSessionRegisterCallback : 388 -> 392
~ __DAServerSessionCopyCallbackQueue : 444 -> 448
~ _DAGetCallbackFromSession : 124 -> 128
~ _DADiskCopyWholeDisk : 260 -> 276
~ _DADiskCopyIOMedia : 104 -> 96
~ ___DASessionDeallocate : 404 -> 396
~ __DASessionScheduleWithRunLoop : 316 -> 324
~ _DADiskRenameCommon : 356 -> 352
~ _DADiskSetFSKitAdditionsCommon : 156 -> 188
~ __DADiskSetEncoding : 140 -> 12
~ __DAVolumeGetDevicePathForLifsMount : 212 -> 216
~ _DARemoveCallbackFromSessionWithKey : 216 -> 204
~ _DARemoveCallbackFromSession : 448 -> 432
~ __DASessionRecreate : 756 -> 744
- __DAServerDiskSetEncoding
~ __DAServerSessionQueueResponse : 368 -> 380
~ __DAServerSessionSetKeepAlive : 292 -> 296
~ DASessionCreate.cold.1 : 44 -> 128
~ DASessionCreate.cold.2 : 128 -> 44

```
