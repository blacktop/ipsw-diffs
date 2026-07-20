## timed

> `/usr/libexec/timed`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-340.0.11.0.0
-  __TEXT.__text: 0x17f6c
-  __TEXT.__auth_stubs: 0xb40
+340.0.12.0.0
+  __TEXT.__text: 0x18094
+  __TEXT.__auth_stubs: 0xb30
   __TEXT.__objc_stubs: 0x2760
   __TEXT.__objc_methlist: 0xd6c
   __TEXT.__const: 0x290
   __TEXT.__objc_methname: 0x25ef
-  __TEXT.__cstring: 0x20c9
+  __TEXT.__cstring: 0x20dc
   __TEXT.__objc_classname: 0x111
   __TEXT.__objc_methtype: 0x554
   __TEXT.__oslogstring: 0x2c7e
   __TEXT.__gcc_except_tab: 0x98
-  __TEXT.__unwind_info: 0x5d8
+  __TEXT.__unwind_info: 0x5d0
   __DATA_CONST.__const: 0xf68
   __DATA_CONST.__cfstring: 0x2b00
   __DATA_CONST.__objc_classlist: 0x50

   __DATA_CONST.__linkguard: 0x15
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA_CONST.__auth_got: 0x5b0
+  __DATA_CONST.__auth_got: 0x5a8
   __DATA_CONST.__got: 0x1c8
   __DATA.__objc_const: 0x1da0
   __DATA.__objc_selrefs: 0xb68

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  Functions: 645
-  Symbols:   248
+  Functions: 648
+  Symbols:   247
   CStrings:  1294
 
Symbols:
- _memcpy
CStrings:
+ "-[TMBackgroundNtpSource _fetchTime]"
+ "340.0.12"
+ "best_index > -1 && best_index < NTP_DESIRED_NUM_SERVERS"
- "-[TMBackgroundNtpSource _fetchTime]_block_invoke"
- "340.0.11"
- "machResult > kMachStart"
```
