## DiskArbitration

> `/System/Library/PrivateFrameworks/DiskArbitration.framework/DiskArbitration`

```diff

-490.120.6.0.1
-  __TEXT.__text: 0x6148
-  __TEXT.__auth_stubs: 0x740
-  __TEXT.__cstring: 0x720
-  __TEXT.__const: 0x80
+535.0.0.0.0
+  __TEXT.__text: 0x68fc
+  __TEXT.__auth_stubs: 0x760
+  __TEXT.__cstring: 0x730
+  __TEXT.__const: 0xa8
   __TEXT.__oslogstring: 0x89
-  __TEXT.__unwind_info: 0x200
+  __TEXT.__unwind_info: 0x210
   __DATA_CONST.__got: 0x88
-  __DATA_CONST.__const: 0x318
-  __AUTH_CONST.__auth_got: 0x3a0
+  __DATA_CONST.__const: 0x320
+  __AUTH_CONST.__auth_got: 0x3b0
   __AUTH_CONST.__const: 0xc0
-  __AUTH_CONST.__cfstring: 0x980
+  __AUTH_CONST.__cfstring: 0x9a0
   __DATA.__data: 0x28
   __DATA.__bss: 0x411
   __DATA_DIRTY.__data: 0x10

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Security.framework/Security
   - /usr/lib/libSystem.B.dylib
-  UUID: 691528AF-7F33-3053-9167-A92FD896A9C3
-  Functions: 151
-  Symbols:   468
-  CStrings:  206
+  - /usr/lib/libbsm.0.dylib
+  UUID: 76F26D36-497E-3865-9C0F-2D7241F65ED3
+  Functions: 158
+  Symbols:   480
+  CStrings:  208
 
Symbols:
+ _DADiskEjectWithBlockAndAuditToken
+ _DADiskMountWithArgumentsAndBlockAndAuditToken
+ _DADiskMountWithBlockAndAuditToken
+ _DADiskRenameWithBlockAndAuditToken
+ _DADiskUnmountWithBlockAndAuditToken
+ __DAServerSessionQueueRequestWithUserToken
+ ___DAQueueRequestWithUserToken
+ _audit_token_to_pid
+ _getuid
+ _kDADiskDescriptionRepairRunningKey
CStrings:
+ "DARepairRunning"

```
