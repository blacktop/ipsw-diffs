## APFS

> `/System/Library/PrivateFrameworks/APFS.framework/APFS`

```diff

-2632.0.15.0.1
-  __TEXT.__text: 0x4fd54
-  __TEXT.__auth_stubs: 0xb40
+2632.0.36.0.1
+  __TEXT.__text: 0x4fee8
+  __TEXT.__auth_stubs: 0xb60
   __TEXT.__const: 0x8410
-  __TEXT.__cstring: 0xddcd
-  __TEXT.__oslogstring: 0xac7
+  __TEXT.__cstring: 0xdde2
+  __TEXT.__oslogstring: 0xb0e
   __TEXT.__gcc_except_tab: 0x18
   __TEXT.__unwind_info: 0x918
   __DATA_CONST.__got: 0x78
   __DATA_CONST.__const: 0x4e8
-  __AUTH_CONST.__auth_got: 0x5a8
+  __AUTH_CONST.__auth_got: 0x5b8
   __AUTH_CONST.__const: 0x380
   __AUTH_CONST.__cfstring: 0x1160
   __DATA.__data: 0x98

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libutil.dylib
-  UUID: B4A39A41-1334-361F-8923-A0F130F2B172
+  UUID: FC2EB705-8667-3428-98D1-F8E9025A0886
   Functions: 807
-  Symbols:   1758
-  CStrings:  1441
+  Symbols:   1760
+  CStrings:  1443
 
Symbols:
+ _IOServiceWaitQuiet
+ _ccdigest_parallel
Functions:
~ _authapfs_digest : 472 -> 568
~ _APFSVolumeDelete : 8 -> 52
~ __APFSVolumeOperation : 204 -> 444
~ _APFSSetupMetadataRollingMediaKey : 428 -> 436
~ _APFSVolumeTranscribePFK : 44 -> 52
~ _APFSVolumeMigrateMediaKey : 44 -> 52
CStrings:
+ "%s:%d: timed out waiting for container quiet after op %d on volume %s\n"
+ "2632.0.36.0.1"
+ "_APFSVolumeOperation"
- "2632.0.15.0.1"

```
