## HangTracer

> `/System/Library/PrivateFrameworks/HangTracer.framework/HangTracer`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-421.0.0.0.0
-  __TEXT.__text: 0x174f0
+424.0.0.0.0
+  __TEXT.__text: 0x17524
   __TEXT.__objc_methlist: 0x9fc
   __TEXT.__const: 0x268
   __TEXT.__gcc_except_tab: 0x214
-  __TEXT.__cstring: 0x4534
+  __TEXT.__cstring: 0x45aa
   __TEXT.__oslogstring: 0x2bf4
   __TEXT.__ustring: 0xe0
-  __TEXT.__unwind_info: 0x5c8
+  __TEXT.__unwind_info: 0x5d0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x17b8
+  __DATA_CONST.__const: 0x17f8
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xa58
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__got: 0x1f0
   __AUTH_CONST.__const: 0x540
-  __AUTH_CONST.__cfstring: 0x5b80
+  __AUTH_CONST.__cfstring: 0x5c60
   __AUTH_CONST.__objc_const: 0x1a98
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_doubleobj: 0x10

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libapp_launch_measurement.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 588
-  Symbols:   1501
-  CStrings:  994
+  Functions: 589
+  Symbols:   1510
+  CStrings:  1001
 
Symbols:
+ _HTIsDeviceRestricted
+ _kHTExtendedAttributeHangEnd
+ _kHTExtendedAttributeHangStart
+ _kHTExtendedAttributeSampleEnd
+ _kHTExtendedAttributeSampleStart
+ _kHTLostPerfJSONKeyEndMATU
+ _kHTLostPerfJSONKeyIntervals
+ _kHTLostPerfJSONKeyReason
+ _kHTLostPerfJSONKeyStartMATU
Functions:
~ _HTHangEventCreateWithBundleID : 1360 -> 1368
~ _bundleIDFromPath : 180 -> 216
+ _HTIsDeviceRestricted
CStrings:
+ "end_matu"
+ "hangtracer.hang_end"
+ "hangtracer.hang_start"
+ "hangtracer.sample_end"
+ "hangtracer.sample_start"
+ "intervals"
+ "start_matu"
```
