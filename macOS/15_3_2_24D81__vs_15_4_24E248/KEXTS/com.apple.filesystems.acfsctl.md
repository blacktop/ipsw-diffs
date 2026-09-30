## com.apple.filesystems.acfsctl

> `com.apple.filesystems.acfsctl`

```diff

-780.80.2.0.1
+782.100.7.0.0
   __TEXT.__cstring: 0x256
-  __TEXT_EXEC.__text: 0xadc
+  __TEXT_EXEC.__text: 0xb00
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x170
   __DATA.__common: 0x10
   __DATA_CONST.__auth_got: 0x180
   __DATA_CONST.__got: 0x28
-  UUID: 1420B6BF-F187-3558-BC7B-E598F6786192
-  Functions: 7
-  Symbols:   69
+  UUID: 196ED9DA-24A5-3750-B14C-7FC8A6622D91
+  Functions: 14
+  Symbols:   77
   CStrings:  16
 
Symbols:
+ _OUTLINED_FUNCTION_0
+ cvfsctl_ioctl.cold.1
+ cvfsctl_ioctl.cold.2
+ cvfsctl_ioctl.cold.3
+ cvfsctl_ioctl.cold.4
+ cvfsctl_ioctl.cold.5
+ cvfsctl_rdwrt.cold.1
+ cvfsctl_strategy.cold.1
Functions:
~ _cvfsctl_strategy : 128 -> 92
~ _cvfsctl_ioctl : 2168 -> 1988
~ _cvfsctl_rdwrt : 88 -> 60
CStrings:
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/XsanFS/snfs/client/fsctl/nomad/fsctl.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/XsanFS/snfs/client/fsctl/nomad/fsctl.c"

```
