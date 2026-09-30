## watchpresenced

> `/usr/libexec/watchpresenced`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-29.0.0.0.0
-  __TEXT.__text: 0x627c
+30.0.0.0.0
+  __TEXT.__text: 0x6558
   __TEXT.__auth_stubs: 0x440
-  __TEXT.__objc_stubs: 0x1300
-  __TEXT.__objc_methlist: 0xa14
+  __TEXT.__objc_stubs: 0x1320
+  __TEXT.__objc_methlist: 0xa24
   __TEXT.__const: 0x98
   __TEXT.__cstring: 0x411
-  __TEXT.__objc_methname: 0x192c
+  __TEXT.__objc_methname: 0x194c
   __TEXT.__objc_classname: 0x108
   __TEXT.__objc_methtype: 0x641
-  __TEXT.__oslogstring: 0x7e1
-  __TEXT.__gcc_except_tab: 0x1b4
-  __TEXT.__unwind_info: 0x2e0
-  __DATA_CONST.__const: 0x438
+  __TEXT.__oslogstring: 0x859
+  __TEXT.__gcc_except_tab: 0x228
+  __TEXT.__unwind_info: 0x300
+  __DATA_CONST.__const: 0x410
   __DATA_CONST.__cfstring: 0x500
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x38

   __DATA_CONST.__auth_got: 0x238
   __DATA_CONST.__got: 0x178
   __DATA.__objc_const: 0x1dc8
-  __DATA.__objc_selrefs: 0x6c8
+  __DATA.__objc_selrefs: 0x6d0
   __DATA.__objc_ivar: 0xd0
   __DATA.__objc_data: 0x280
   __DATA.__data: 0x2c0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 176
+  Functions: 181
   Symbols:   124
-  CStrings:  490
+  CStrings:  493
 
Symbols:
+ _objc_release_x27
- _objc_release_x28
CStrings:
+ "Cannot run discovery mode: watch or CBCentralManager unavailable"
+ "Sharing was interrupted, re-arming on wrist detection..."
+ "Unsupported RSSI window size %d, falling back to 8"
+ "_wristMonitoringWasInterrupted:"
- "SFClient invalidation completed, releasing reference"
```
