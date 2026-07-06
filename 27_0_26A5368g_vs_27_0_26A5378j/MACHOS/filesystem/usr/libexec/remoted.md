## remoted

> `/usr/libexec/remoted`

```diff

-  __TEXT.__text: 0x40d1c
-  __TEXT.__auth_stubs: 0x17b0
+  __TEXT.__text: 0x40fd8
+  __TEXT.__auth_stubs: 0x1800
   __TEXT.__objc_stubs: 0x2700
   __TEXT.__objc_methlist: 0x1828
-  __TEXT.__const: 0x202
+  __TEXT.__const: 0x222
   __TEXT.__oslogstring: 0x8976
-  __TEXT.__cstring: 0x2428
+  __TEXT.__cstring: 0x245d
   __TEXT.__objc_methname: 0x2976
   __TEXT.__objc_classname: 0x3c3
   __TEXT.__objc_methtype: 0x9e3
   __TEXT.__gcc_except_tab: 0x1054
-  __TEXT.__unwind_info: 0xe48
+  __TEXT.__unwind_info: 0xe58
   __DATA_CONST.__const: 0x14e0
   __DATA_CONST.__cfstring: 0xea0
   __DATA_CONST.__objc_classlist: 0xf8

   __DATA_CONST.__objc_arrayobj: 0x90
   __DATA_CONST.__objc_intobj: 0xa8
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA_CONST.__auth_got: 0xbe8
-  __DATA_CONST.__got: 0x248
+  __DATA_CONST.__auth_got: 0xc10
+  __DATA_CONST.__got: 0x260
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0x2e38
   __DATA.__objc_selrefs: 0xab0
   __DATA.__objc_ivar: 0x244
   __DATA.__objc_data: 0x9b0
   __DATA.__data: 0x8f0
-  __DATA.__bss: 0x3e8
+  __DATA.__bss: 0x3f0
   __DATA.__common: 0x38
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1448
-  Symbols:   479
-  CStrings:  2045
+  Functions: 1453
+  Symbols:   489
+  CStrings:  2051
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_selrefs : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
+ _ftruncate
+ _kCFAbsoluteTimeIntervalSince1970
+ _mmap
+ _sntp_datestamp_from_double
+ _sntp_header_mmap
+ _sntp_shortstamp_hton
+ _sntp_timestamp_to_shortstamp
+ _umask
+ _warn
+ _write
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.K1XCVP/Sources/RemoteServiceDiscovery_executables/remoted/modules/identity.m"
+ "/var/sntpd/state.bin"
+ "close"
+ "ftruncate"
+ "mmap"
+ "open"
+ "write"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.t2TEXn/Sources/RemoteServiceDiscovery_executables/remoted/modules/identity.m"

```
