## libEmbeddedSystemAUs.dylib

> `/System/Library/Frameworks/AudioToolbox.framework/libEmbeddedSystemAUs.dylib`

```diff

-1638.208.0.0.0
-  __TEXT.__text: 0xd1888
+1638.209.1.0.0
+  __TEXT.__text: 0xd19b0
   __TEXT.__realtime: 0x38084
   __TEXT.__const: 0xb344
   __TEXT.__dlopen_cstrs: 0x36d
-  __TEXT.__gcc_except_tab: 0x794c
+  __TEXT.__gcc_except_tab: 0x7958
   __TEXT.__cstring: 0xa313
-  __TEXT.__oslogstring: 0xc28c
+  __TEXT.__oslogstring: 0xc2cc
   __TEXT.__unwind_info: 0x4f00
   __TEXT.__eh_frame: 0x108
   __TEXT.__auth_stubs: 0x0

   - /usr/lib/libobjc.A.dylib
   Functions: 4083
   Symbols:   6299
-  CStrings:  1992
+  CStrings:  1993
 
Functions:
~ ____ZN20AudioCapturerManager10InitializeEv_block_invoke : 1820 -> 1804
~ __ZZN10AURemoteIO5StartEvENK3$_0clE8TapPointRK27AudioStreamBasicDescriptionPKcb : 1908 -> 2220
CStrings:
+ "%25s:%-5d AURemoteIO::Start: cannot capture %s; bus is disabled"
```
