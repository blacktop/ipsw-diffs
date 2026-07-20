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
-  __TEXT.__text: 0x17734
-  __TEXT.__auth_stubs: 0xbb0
+340.0.12.0.0
+  __TEXT.__text: 0x17858
+  __TEXT.__auth_stubs: 0xba0
   __TEXT.__objc_stubs: 0x26e0
   __TEXT.__objc_methlist: 0xd6c
   __TEXT.__const: 0x280
   __TEXT.__objc_methname: 0x255c
-  __TEXT.__cstring: 0x20d4
+  __TEXT.__cstring: 0x20e7
   __TEXT.__objc_classname: 0x111
   __TEXT.__objc_methtype: 0x554
   __TEXT.__oslogstring: 0x2c6c
   __TEXT.__gcc_except_tab: 0x98
-  __TEXT.__unwind_info: 0x600
+  __TEXT.__unwind_info: 0x5f8
   __DATA_CONST.__const: 0xe68
   __DATA_CONST.__cfstring: 0x2b60
   __DATA_CONST.__objc_classlist: 0x50

   __DATA_CONST.__linkguard: 0x15
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA_CONST.__auth_got: 0x5e8
+  __DATA_CONST.__auth_got: 0x5e0
   __DATA_CONST.__got: 0x1d8
   __DATA.__objc_const: 0x1da0
   __DATA.__objc_selrefs: 0xb48

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  Functions: 618
-  Symbols:   257
+  Functions: 622
+  Symbols:   256
   CStrings:  1289
 
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
