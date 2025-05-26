## timed

> `/usr/libexec/timed`

```diff

-326.0.0.0.0
-  __TEXT.__text: 0x183d0
-  __TEXT.__auth_stubs: 0xb60
-  __TEXT.__objc_stubs: 0x2560
+327.0.3.1.0
+  __TEXT.__text: 0x185d4
+  __TEXT.__auth_stubs: 0xb70
+  __TEXT.__objc_stubs: 0x25a0
   __TEXT.__objc_methlist: 0xb7c
-  __TEXT.__const: 0x1a8
-  __TEXT.__cstring: 0x1fea
-  __TEXT.__oslogstring: 0x2886
-  __TEXT.__objc_methname: 0x2323
+  __TEXT.__const: 0x1a0
+  __TEXT.__cstring: 0x1ff0
+  __TEXT.__oslogstring: 0x2952
+  __TEXT.__objc_methname: 0x2357
   __TEXT.__objc_classname: 0x124
   __TEXT.__objc_methtype: 0x504
   __TEXT.__gcc_except_tab: 0xa0
   __TEXT.__ustring: 0x2c
   __TEXT.__unwind_info: 0x53c
-  __DATA_CONST.__auth_got: 0x5c0
+  __DATA_CONST.__auth_got: 0x5c8
   __DATA_CONST.__got: 0x110
   __DATA_CONST.__const: 0xdb0
   __DATA_CONST.__cfstring: 0x2b80

   __DATA_CONST.__objc_catlist: 0x0
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_classrefs: 0x128
+  __DATA_CONST.__objc_superrefs: 0x48
   __DATA_CONST.__objc_doubleobj: 0x40
   __DATA_CONST.__objc_intobj: 0x570
   __DATA_CONST.__linkguard: 0x15
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA.__objc_const: 0x23e0
-  __DATA.__objc_selrefs: 0xa20
-  __DATA.__objc_classrefs: 0x128
-  __DATA.__objc_superrefs: 0x48
+  __DATA.__objc_selrefs: 0xa30
   __DATA.__objc_ivar: 0x178
   __DATA.__objc_data: 0x320
-  __DATA.__data: 0x308
+  __DATA.__data: 0x310
   __DATA.__bss: 0x140
   __DATA.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
   Functions: 546
-  Symbols:   256
-  CStrings:  1286
+  Symbols:   257
+  CStrings:  1293
 
Symbols:
+ _clock_gettime_nsec_np
CStrings:
+ "327.0.3.1"
+ "CLOCK_MONOTONIC_RAW has stepped backward since last NTP fetch"
+ "Failed to read cache: %@"
+ "T@\"NSString\",?,R,C"
+ "Throttling power management triggered NTP fetch attempt lastFetch: %f currentTime: %f"
+ "fileURLWithPath:"
+ "initWithContentsOfURL:error:"
+ "soft reset due to rtc rollback"
+ "userInfo"
- "326"
- "initWithContentsOfFile:"

```
