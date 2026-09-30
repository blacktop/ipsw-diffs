## SiriAppIntentsRuntime

> `/System/Library/PrivateFrameworks/SiriAppIntentsRuntime.framework/SiriAppIntentsRuntime`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_mpenum`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA_DIRTY.__data`

```diff

-3600.82.15.0.0
-  __TEXT.__text: 0x7c728
-  __TEXT.__objc_methlist: 0x3e8
-  __TEXT.__const: 0x2798
-  __TEXT.__cstring: 0x1431
-  __TEXT.__constg_swiftt: 0xc9c
-  __TEXT.__swift5_typeref: 0x12f3
+3600.82.20.0.0
+  __TEXT.__text: 0x815b4
+  __TEXT.__objc_methlist: 0x404
+  __TEXT.__const: 0x2808
+  __TEXT.__cstring: 0x14b1
+  __TEXT.__constg_swiftt: 0xca4
+  __TEXT.__swift5_typeref: 0x1385
   __TEXT.__swift5_reflstr: 0xcf6
   __TEXT.__swift5_fieldmd: 0x940
-  __TEXT.__oslogstring: 0x32dd
+  __TEXT.__oslogstring: 0x348d
   __TEXT.__swift5_builtin: 0x3c
   __TEXT.__swift5_types: 0xb4
-  __TEXT.__swift_as_entry: 0x1c0
-  __TEXT.__swift_as_ret: 0x170
-  __TEXT.__swift_as_cont: 0x2cc
+  __TEXT.__swift_as_entry: 0x1cc
+  __TEXT.__swift_as_ret: 0x17c
+  __TEXT.__swift_as_cont: 0x2ec
   __TEXT.__swift5_proto: 0x104
-  __TEXT.__swift5_capture: 0x1758
+  __TEXT.__swift5_capture: 0x1880
   __TEXT.__swift5_assocty: 0x98
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x1a10
-  __TEXT.__eh_frame: 0x4670
+  __TEXT.__unwind_info: 0x1ac0
+  __TEXT.__eh_frame: 0x4818
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x438
+  __DATA_CONST.__objc_selrefs: 0x440
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x4378
-  __AUTH_CONST.__objc_const: 0xcc8
-  __AUTH_CONST.__auth_got: 0x1888
+  __AUTH_CONST.__const: 0x4648
+  __AUTH_CONST.__objc_const: 0xcd0
+  __AUTH_CONST.__auth_got: 0x18e8
   __AUTH.__objc_data: 0xa0
   __AUTH.__data: 0x570
-  __DATA.__data: 0x7e8
+  __DATA.__data: 0x828
   __DATA.__bss: 0x1400
   __DATA.__common: 0x88
-  __DATA_DIRTY.__objc_data: 0x9c0
+  __DATA_DIRTY.__objc_data: 0x9d8
   __DATA_DIRTY.__data: 0xd28
   __DATA_DIRTY.__bss: 0xb80
   __DATA_DIRTY.__common: 0x110

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2792
-  Symbols:   214
-  CStrings:  330
+  Functions: 2905
+  Symbols:   216
+  CStrings:  337
 
Symbols:
+ _swift_projectBox
+ _swift_release_x1
CStrings:
+ "Failed to fetch raw inference event data batch: %@"
+ "Fetched raw inference event data batch: %ld success, %ld errors"
+ "Fetching raw inference event data batch for %ld plannerIDs"
+ "TimeInterval.from: kind=clampedAnomalousTimestamp machContinuousTime=%llu"
+ "fetchEventsBatch(plannerIDs:windowStart:windowEnd:)"
+ "fetchRawInferenceEventDataBatch(plannerIDs:plannerTimestamps:with:)"
+ "kind=summary TokenGenerationStreamHandler.fetchEventsBatch plannerIDsRequested=%ld matched=%ld bucketsReturned=%ld"
+ "kind=summary fetchRawInferenceEventDataBatch requested=%ld payloads=%ld errors=%ld windowSeconds=%ld"
+ "kind=summary fetchRawInferenceEventDataBatch status=noValidInputs requested=%ld errors=%ld"
+ "plannerID is not a valid UUID"
- "TokenGenerationStreamHandler.fetchEvents: kind=summary plannerID=%s matched=%ld"
- "TokenGenerationStreamHandler.fetchEvents: kind=summary status=failed plannerID=%s error=%s"
- "fetchEvents(plannerID:requestTimestamp:)"
```
