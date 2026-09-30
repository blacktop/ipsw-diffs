## abmlite

> `/usr/bin/abmlite`

```diff

-1183.0.0.0.0
-  __TEXT.__text: 0x18ddc
+1209.0.0.0.0
+  __TEXT.__text: 0x18e24
   __TEXT.__auth_stubs: 0x770
   __TEXT.__objc_stubs: 0x560
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x14
-  __TEXT.__gcc_except_tab: 0x1b20
+  __TEXT.__gcc_except_tab: 0x1b18
   __TEXT.__cstring: 0x9a1
   __TEXT.__const: 0x390
   __TEXT.__oslogstring: 0xc6

   - /System/Library/PrivateFrameworks/BasebandTraceHelper.framework/BasebandTraceHelper
   - /System/Library/PrivateFrameworks/LoggingSupport.framework/LoggingSupport
   - /usr/lib/libSystem.B.dylib
+  - /usr/lib/libTelephonyBasebandDynamic.dylib
   - /usr/lib/libTelephonyCapabilities.dylib
   - /usr/lib/libTelephonyDebugDynamic.dylib
   - /usr/lib/libTelephonyUtilDynamic.dylib

   - /usr/lib/libedit.3.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 136
-  Symbols:   326
+  Symbols:   328
   CStrings:  151
 
Symbols:
+ _TelephonyBasebandWatchdogStartWithStackshot
+ _TelephonyBasebandWatchdogStop

```
