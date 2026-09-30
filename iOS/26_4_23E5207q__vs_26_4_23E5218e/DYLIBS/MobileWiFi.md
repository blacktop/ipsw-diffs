## MobileWiFi

> `/System/Library/PrivateFrameworks/MobileWiFi.framework/MobileWiFi`

```diff

-1995.27.1.0.0
-  __TEXT.__text: 0x2e7ec
+1995.26.4.0.0
+  __TEXT.__text: 0x2e830
   __TEXT.__auth_stubs: 0xdc0
   __TEXT.__objc_methlist: 0x74
   __TEXT.__cstring: 0x44e5
-  __TEXT.__const: 0x6a0
+  __TEXT.__const: 0x6b0
   __TEXT.__oslogstring: 0x91f
   __TEXT.__gcc_except_tab: 0x124
   __TEXT.__dlopen_cstrs: 0xe9
-  __TEXT.__unwind_info: 0xac0
+  __TEXT.__unwind_info: 0xab8
   __TEXT.__objc_classname: 0x3f
   __TEXT.__objc_methname: 0x10d4
   __TEXT.__objc_methtype: 0xea

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FD70DE37-86DD-3643-9EA2-9F46E6AFDC07
+  UUID: 67FB6BC2-2600-3133-8E3E-020D22472167
   Functions: 1159
   Symbols:   2716
   CStrings:  1801
Functions:
~ _WiFiNetworkCopyPreparedEAPProfile : 364 -> 432
~ _WiFiNetworkCopyPassword -> _WiFiNetworkCopyPasswordWithTimeout : 244 -> 408
~ _WiFiNetworkCopyHashedWPAPassword -> _WiFiNetworkCopyPassword : 60 -> 244
~ _WiFiNetworkCopyPasswordWithTimeout -> _WiFiNetworkCopyHashedWPAPassword : 408 -> 60

```
