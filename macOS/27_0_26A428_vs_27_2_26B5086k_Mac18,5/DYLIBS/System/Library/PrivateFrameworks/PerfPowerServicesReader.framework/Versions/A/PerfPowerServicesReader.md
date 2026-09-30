## PerfPowerServicesReader

> `/System/Library/PrivateFrameworks/PerfPowerServicesReader.framework/Versions/A/PerfPowerServicesReader`

```diff

-3486.1.2.0.0
-  __TEXT.__text: 0x158044
+3486.40.92.0.0
+  __TEXT.__text: 0x15826c
   __TEXT.__init_offsets: 0xdc
-  __TEXT.__objc_methlist: 0x13994
-  __TEXT.__const: 0x5fda
-  __TEXT.__cstring: 0xe092
+  __TEXT.__objc_methlist: 0x1399c
+  __TEXT.__const: 0x5fea
+  __TEXT.__cstring: 0xe156
   __TEXT.__gcc_except_tab: 0x4b10
   __TEXT.__oslogstring: 0xda1
-  __TEXT.__unwind_info: 0x54f8
+  __TEXT.__unwind_info: 0x5500
   __TEXT.__eh_frame: 0xa0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x368
-  __DATA_CONST.__objc_selrefs: 0x60a8
+  __DATA_CONST.__objc_selrefs: 0x60b0
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x508
   __DATA_CONST.__objc_arraydata: 0x110
   __DATA_CONST.__got: 0x758
   __AUTH_CONST.__const: 0x36f0
-  __AUTH_CONST.__cfstring: 0x10b80
+  __AUTH_CONST.__cfstring: 0x10be0
   __AUTH_CONST.__objc_const: 0x179e0
   __AUTH_CONST.__weak_auth_got: 0xb0
   __AUTH_CONST.__objc_intobj: 0x1e0

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 8204
-  Symbols:   13428
-  CStrings:  2358
+  Functions: 8205
+  Symbols:   13429
+  CStrings:  2361
 
Symbols:
+ -[PPSTimeSeriesRequest initWithDistinctMetrics:predicate:timeFilter:]
Functions:
+ -[PPSTimeSeriesRequest initWithDistinctMetrics:predicate:timeFilter:]
~ -[PPSRequestValidator validateDataRequest:filepath:withError:] : 2180 -> 2668
~ -[PPSSQLiteTimeSeriesIngester parseDataForRequest:outError:] : 2972 -> 2984
CStrings:
+ "Distinct requests cannot select the timestampEnd metric."
+ "Distinct requests cannot select variable-length array metric '%@'."
+ "Distinct requests cannot use limitCount, offsetCount, or readDirection."
```
