## PerfPowerServicesReader

> `/System/Library/PrivateFrameworks/PerfPowerServicesReader.framework/PerfPowerServicesReader`

```diff

-3486.40.98.0.0
-  __TEXT.__text: 0x150e3c
+3486.40.112.0.0
+  __TEXT.__text: 0x151140
   __TEXT.__init_offsets: 0xdc
-  __TEXT.__objc_methlist: 0x1399c
+  __TEXT.__objc_methlist: 0x139ac
   __TEXT.__const: 0x5fe2
   __TEXT.__cstring: 0xe156
-  __TEXT.__gcc_except_tab: 0x4adc
-  __TEXT.__oslogstring: 0xda1
-  __TEXT.__unwind_info: 0x5498
+  __TEXT.__gcc_except_tab: 0x4b10
+  __TEXT.__oslogstring: 0xe59
+  __TEXT.__unwind_info: 0x54a8
   __TEXT.__eh_frame: 0xa0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x368
-  __DATA_CONST.__objc_selrefs: 0x60b0
+  __DATA_CONST.__objc_selrefs: 0x60c0
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x508
   __DATA_CONST.__objc_arraydata: 0x110

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 8165
-  Symbols:   12066
-  CStrings:  2361
+  Functions: 8166
+  Symbols:   12067
+  CStrings:  2363
 
Symbols:
+ -[PPSTimestampConverter monotonicRangeForStartEpoch:endEpoch:startMonotonic:endMonotonic:]
Functions:
~ -[PPSSQLiteTimeSeriesIngester parseDataForRequest:outError:] : 2840 -> 2944
~ +[PPSTimestampConverterRegistry converterForFilepath:] : 180 -> 224
~ +[PPSPredicateUtilities predicateForStartTimestamp:endTimestamp:withKeyPath:] : 268 -> 384
+ -[PPSTimestampConverter monotonicRangeForStartEpoch:endEpoch:startMonotonic:endMonotonic:]
CStrings:
+ "Epoch range [%.6f, %.6f] has no monotonic preimage in %{public}@ (%zu system-offset entries)."
+ "Inverted timestamp range for key-path %{public}@: [%.6f, %.6f]. Query will match no rows."
```
