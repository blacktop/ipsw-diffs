## NetworkUplinkClock

> `/System/Library/Audio/Plug-Ins/HAL/NetworkUplinkClock.driver/NetworkUplinkClock`

```diff

-1075.0.0.0.0
-  __TEXT.__text: 0x9af4
-  __TEXT.__auth_stubs: 0x5a0
+1158.0.0.0.0
+  __TEXT.__text: 0x9398
+  __TEXT.__auth_stubs: 0x590
   __TEXT.__const: 0x1f1
-  __TEXT.__gcc_except_tab: 0x820
+  __TEXT.__gcc_except_tab: 0x738
   __TEXT.__oslogstring: 0x6bf
-  __TEXT.__cstring: 0x69c
-  __TEXT.__unwind_info: 0x3d8
-  __DATA_CONST.__auth_got: 0x2d8
-  __DATA_CONST.__got: 0x70
-  __DATA_CONST.__const: 0x320
+  __TEXT.__cstring: 0x67c
+  __TEXT.__unwind_info: 0x390
+  __DATA_CONST.__const: 0x2e0
   __DATA_CONST.__cfstring: 0x4e0
+  __DATA_CONST.__auth_got: 0x2d0
+  __DATA_CONST.__got: 0x70
   __DATA.__data: 0x148
-  __DATA.__bss: 0x41
+  __DATA.__bss: 0x31
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony
   - /System/Library/PrivateFrameworks/AppleSauce.framework/AppleSauce

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libWirelessAudioIPC.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 93B680DC-3609-3C68-8FE7-4BF56457EF5A
-  Functions: 125
-  Symbols:   112
-  CStrings:  202
+  UUID: 9BCB1D7D-2984-3252-B90A-DB985DBF5193
+  Functions: 122
+  Symbols:   111
+  CStrings:  201
 
Symbols:
- _os_parse_boot_arg_int
CStrings:
+ "TimeSource %{multichar}x"
+ "changing time source %{multichar}x -> %{multichar}x (running %u)"
+ "failed %{multichar}x"
+ "object %u, selector %{multichar}x, scope %{multichar}x, element %u"
+ "op %{multichar}x"
+ "result %{multichar}x"
+ "result %{multichar}x, changed %zu"
+ "result %{multichar}x, dataSize %u"
+ "result %{multichar}x, isSettable %{BOOL}d"
+ "result %{multichar}x, sampleTime %lf, hostTime %llu, seed %llu"
+ "success %{multichar}x"
+ "unsupported time source %{multichar}x"
- "TimeSource %{waipc:4cc}u"
- "changing time source %{waipc:4cc}u -> %{waipc:4cc}u (running %u)"
- "dale-ignore-time-sync-interrupt"
- "failed %{waipc:4cc}u"
- "object %u, selector %{waipc:4cc}u, scope %{waipc:4cc}u, element %u"
- "op %{waipc:4cc}u"
- "result %{waipc:4cc}u"
- "result %{waipc:4cc}u, changed %zu"
- "result %{waipc:4cc}u, dataSize %u"
- "result %{waipc:4cc}u, isSettable %{BOOL}d"
- "result %{waipc:4cc}u, sampleTime %lf, hostTime %llu, seed %llu"
- "success %{waipc:4cc}u"
- "unsupported time source %{waipc:4cc}u"

```
