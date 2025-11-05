## GeoServicesCore

> `/System/Library/PrivateFrameworks/GeoServicesCore.framework/Versions/A/GeoServicesCore`

```diff

-1986.23.11.14.2
-  __TEXT.__text: 0x2cbc
+1986.24.9.12.31
+  __TEXT.__text: 0x2ca4
   __TEXT.__auth_stubs: 0x440
   __TEXT.__objc_methlist: 0xa8
   __TEXT.__const: 0xa8
   __TEXT.__cstring: 0x324
-  __TEXT.__gcc_except_tab: 0x138
-  __TEXT.__oslogstring: 0x110
-  __TEXT.__unwind_info: 0x178
+  __TEXT.__gcc_except_tab: 0x134
+  __TEXT.__oslogstring: 0x10d
+  __TEXT.__unwind_info: 0x180
   __TEXT.__objc_classname: 0x41
   __TEXT.__objc_methname: 0x269
   __TEXT.__objc_methtype: 0x163

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1789CAEC-0A6D-36DA-A4B7-6320DDD03C0E
+  UUID: A4FA16B2-D7EE-3511-97FC-28F9AE867285
   Functions: 94
   Symbols:   265
   CStrings:  137
Functions:
~ -[geo_state_capture_handle _capturePlistState:] : 1516 -> 1524
~ __GEORegisterPListStateCaptureAtFrequency : 520 -> 516
~ _geo_isolate_sync : 208 -> 204
~ _geo_isolate_sync_data : 208 -> 204
~ ___geo_isolate_async_block_invoke : 172 -> 160
~ _geo_reentrant_isolate_sync : 208 -> 204
~ _geo_reentrant_isolate_sync_data : 208 -> 204
CStrings:
+ "Assertion failed: handle != ((void*)0)"
+ "Assertion failed: legacyHandle != ((void*)0)"
+ "Assertion failed: self != ((void*)0)"
- "Assertion failed: handle != ((void *)0)"
- "Assertion failed: legacyHandle != ((void *)0)"
- "Assertion failed: self != ((void *)0)"

```
