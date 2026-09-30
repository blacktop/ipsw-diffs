## batterytrapd

> `/usr/libexec/batterytrapd`

```diff

-8.0.0.0.0
-  __TEXT.__text: 0x16a4
-  __TEXT.__auth_stubs: 0x340
+8.80.1.0.0
+  __TEXT.__text: 0x16dc
+  __TEXT.__auth_stubs: 0x350
   __TEXT.__objc_stubs: 0x500
   __TEXT.__objc_methlist: 0x188
   __TEXT.__const: 0x28
-  __TEXT.__oslogstring: 0x395
-  __TEXT.__cstring: 0x1ef
+  __TEXT.__oslogstring: 0x41f
+  __TEXT.__cstring: 0x211
   __TEXT.__objc_methname: 0x356
   __TEXT.__objc_classname: 0x24
   __TEXT.__objc_methtype: 0xba
   __TEXT.__gcc_except_tab: 0x14
   __TEXT.__unwind_info: 0xe8
-  __DATA_CONST.__auth_got: 0x1b0
+  __DATA_CONST.__auth_got: 0x1b8
   __DATA_CONST.__got: 0x88
   __DATA_CONST.__const: 0x88
   __DATA_CONST.__cfstring: 0x220

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  Functions: 55
-  Symbols:   78
-  CStrings:  120
+  Functions: 53
+  Symbols:   79
+  CStrings:  122
 
Symbols:
+ __os_log_impl
CStrings:
+ "Received XPC launch event com.apple.notifyd.matching SignificantTimeChangeNotification for batterytrapd"
+ "SignificantTimeChangeNotification"
+ "com.apple.notifyd.matching notification from com.apple.system.timezone/SignificantTimeChangeNotification"
- "com.apple.notifyd.matching notification from com.apple.system.timezone"

```
