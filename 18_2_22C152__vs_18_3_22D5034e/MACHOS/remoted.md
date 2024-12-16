## remoted

> `/usr/libexec/remoted`

```diff

-172.0.0.0.0
-  __TEXT.__text: 0x3e110
-  __TEXT.__auth_stubs: 0x17f0
-  __TEXT.__objc_stubs: 0x2200
-  __TEXT.__objc_methlist: 0x1358
+172.80.4.0.0
+  __TEXT.__text: 0x4091c
+  __TEXT.__auth_stubs: 0x1810
+  __TEXT.__objc_stubs: 0x2220
+  __TEXT.__objc_methlist: 0x1370
   __TEXT.__const: 0x21a
-  __TEXT.__oslogstring: 0x81b2
-  __TEXT.__cstring: 0x1ec8
-  __TEXT.__objc_methname: 0x229d
+  __TEXT.__oslogstring: 0x81a4
+  __TEXT.__cstring: 0x1ec3
+  __TEXT.__objc_methname: 0x22a4
   __TEXT.__objc_classname: 0x27b
   __TEXT.__objc_methtype: 0x6e6
-  __TEXT.__gcc_except_tab: 0x12c8
-  __TEXT.__unwind_info: 0xdc8
-  __DATA_CONST.__auth_got: 0xc08
-  __DATA_CONST.__got: 0x210
-  __DATA_CONST.__const: 0x1298
+  __TEXT.__gcc_except_tab: 0x16c0
+  __TEXT.__unwind_info: 0xe00
+  __DATA_CONST.__auth_got: 0xc18
+  __DATA_CONST.__got: 0x218
+  __DATA_CONST.__const: 0x12d8
   __DATA_CONST.__cfstring: 0xca0
   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arrayobj: 0x90
   __DATA_CONST.__objc_intobj: 0x90
   __DATA.__objc_const: 0x2420
-  __DATA.__objc_selrefs: 0x8b8
+  __DATA.__objc_selrefs: 0x8c0
   __DATA.__objc_ivar: 0x200
   __DATA.__objc_data: 0x730
   __DATA.__data: 0x670
-  __DATA.__bss: 0x392
+  __DATA.__bss: 0x39a
   __DATA.__common: 0x38
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1347
-  Symbols:   485
-  CStrings:  1720
+  Functions: 1284
+  Symbols:   488
+  CStrings:  1723
 
Symbols:
+ _NSOSStatusErrorDomain
+ _getpid
+ _open
+ _vdprintf
- _SecTrustGetTrustResult
CStrings:
+ "%{public}@> %s TLS."
+ "%{public}@> Authenticated."
+ "%{public}@> Failed to authenticate."
+ "/dev/console"
+ "Declined"
+ "Requested"
+ "domain"
+ "remoted[%d]: %s\n"
- " by default for darwinOS"
- " by default for non-darwinOS"
- "%{public}@> Declined TLS."
- "%{public}@> Requested TLS."
- "Failed to read trust result with status: %d"

```
