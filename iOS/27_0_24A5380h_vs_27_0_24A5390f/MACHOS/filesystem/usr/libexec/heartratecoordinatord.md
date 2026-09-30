## heartratecoordinatord

> `/usr/libexec/heartratecoordinatord`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__objc_classname`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-40.0.0.0.0
-  __TEXT.__text: 0x26e50
+41.1.0.0.0
+  __TEXT.__text: 0x26e6c
   __TEXT.__auth_stubs: 0x7d0
-  __TEXT.__objc_stubs: 0x4000
+  __TEXT.__objc_stubs: 0x3fe0
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x1a0c
-  __TEXT.__const: 0x369
-  __TEXT.__oslogstring: 0x3a6f
-  __TEXT.__cstring: 0x21b2
-  __TEXT.__gcc_except_tab: 0x4374
-  __TEXT.__objc_methname: 0x51ab
+  __TEXT.__objc_methlist: 0x19f4
+  __TEXT.__const: 0x375
+  __TEXT.__oslogstring: 0x3ae8
+  __TEXT.__cstring: 0x2191
+  __TEXT.__gcc_except_tab: 0x439c
+  __TEXT.__objc_methname: 0x5119
   __TEXT.__objc_classname: 0x38b
-  __TEXT.__objc_methtype: 0x1c3e
-  __TEXT.__unwind_info: 0x1248
+  __TEXT.__objc_methtype: 0x1c3b
+  __TEXT.__unwind_info: 0x1238
   __DATA_CONST.__const: 0xce0
-  __DATA_CONST.__cfstring: 0x2080
+  __DATA_CONST.__cfstring: 0x2020
   __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_superrefs: 0x88
   __DATA_CONST.__objc_intobj: 0x168
   __DATA_CONST.__objc_arraydata: 0x570
-  __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0xf0
+  __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__auth_got: 0x3f8
-  __DATA_CONST.__got: 0x228
-  __DATA.__objc_const: 0x2c48
-  __DATA.__objc_selrefs: 0x11f8
-  __DATA.__objc_ivar: 0x28c
+  __DATA_CONST.__got: 0x238
+  __DATA.__objc_const: 0x2c18
+  __DATA.__objc_selrefs: 0x11f0
+  __DATA.__objc_ivar: 0x288
   __DATA.__objc_data: 0x640
   __DATA.__data: 0x600
   __DATA.__bss: 0xa8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 922
+  Functions: 919
   Symbols:   209
-  CStrings:  1603
+  CStrings:  1600
 
CStrings:
+ "@48@0:8@16@24@32@40"
+ "firstObject"
+ "hr_count"
+ "initWithDelegate:remoteObjectProxy:onQueue:recentHighConfidenceHRBuffer:"
+ "most recent high confidence HR requested by %{public}@, returning bpm: %{sensitive}f timestamp: %{sensitive}@"
+ "most recent high confidence HR requested by %{public}@, returning nil"
+ "recent high confidence HRs requested by %{public}@, returning %lu samples, oldest: %.0fs, latest: %.0fs"
- "@56@0:8@16@24@32@40@48"
- "HR with bpm: %{sensitive}f"
- "T@\"HRCHeartRateData\",&,V_mostRecentHighConfidenceHeartRate"
- "initWithDelegate:remoteObjectProxy:onQueue:mostRecentHighConfidenceHR:recentHighConfidenceHRBuffer:"
- "most recent high confidence HR requested by %{public}@, returning %@"
- "mostRecentHighConfidenceHeartRate"
- "nil"
- "none"
- "recent high confidence HRs requested by %{public}@, returning %lu samples, latest: %{public}@"
- "setMostRecentHighConfidenceHeartRate:"
```
