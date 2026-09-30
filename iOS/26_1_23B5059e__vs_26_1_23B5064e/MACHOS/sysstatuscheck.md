## sysstatuscheck

> `/usr/libexec/sysstatuscheck`

```diff

-207.0.0.0.0
-  __TEXT.__text: 0xc2d8
+210.0.0.0.0
+  __TEXT.__text: 0xc324
   __TEXT.__auth_stubs: 0x4f0
   __TEXT.__init_offsets: 0x4
   __TEXT.__gcc_except_tab: 0x538
-  __TEXT.__cstring: 0x8d6
+  __TEXT.__cstring: 0x8e7
   __TEXT.__const: 0x498
   __TEXT.__unwind_info: 0x518
   __DATA_CONST.__auth_got: 0x280

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: A2D8E96C-0038-359C-8A21-23BD4A0E4DFB
+  UUID: 89A4CEB7-8BBE-3DA4-A40B-9756C6CD4D38
   Functions: 248
   Symbols:   129
   CStrings:  66
Functions:
~ sub_100001b94 : 232 -> 244
~ sub_100001c7c -> sub_100001c88 : 1036 -> 1100
CStrings:
+ "com.apple.driver.AppleH[0-9]+CameraInterface.NonPersistent.*"
+ "pressure: raw level %u -> corrected %u, excluded bytes %llu of which collectable %llu, diag %llu, mte tags %llu, kext site %llu, kext named %llu\n"
- "com.apple.driver.AppleH[0-9]+CameraInterface.NonPersistent"
- "pressure: raw level %u -> corrected %u, excluded bytes %llu of which collectable %llu, diag %llu, kext site %llu, kext named %llu\n"

```
