## ExclavesStats

> `/System/Library/PrivateFrameworks/ExclavesStats.framework/ExclavesStats`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_selrefs`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH.__data`

```diff

-10848.0.13.0.0
-  __TEXT.__text: 0x13db4
+10848.0.14.0.0
+  __TEXT.__text: 0x13ecc
   __TEXT.__const: 0x892
-  __TEXT.__cstring: 0x6c3
+  __TEXT.__cstring: 0x703
   __TEXT.__swift5_typeref: 0x252
   __TEXT.__constg_swiftt: 0x254
   __TEXT.__swift5_fieldmd: 0x25c

   __TEXT.__unwind_info: 0x388
   __TEXT.__eh_frame: 0x6f8
   __TEXT.__objc_stubs: 0xa0
-  __TEXT.__auth_stubs: 0x850
+  __TEXT.__auth_stubs: 0x870
   __TEXT.__objc_classname: 0xbb
   __TEXT.__objc_methname: 0x7d
   __TEXT.__objc_methtype: 0x1

   __DATA_CONST.__got: 0x1c8
   __AUTH_CONST.__const: 0x4a0
   __AUTH_CONST.__objc_const: 0x288
-  __AUTH_CONST.__auth_got: 0x430
+  __AUTH_CONST.__auth_got: 0x440
   __AUTH.__data: 0x2c0
   __DATA.__data: 0x220
   __DATA.__common: 0x20
   __DATA.__bss: 0x920
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/perfdata.framework/perfdata
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   Functions: 329
-  Symbols:   954
-  CStrings:  71
+  Symbols:   956
+  CStrings:  72
 
Symbols:
+ _MGGetBoolAnswer
+ _MGIsQuestionValid
Functions:
~ _$s13ExclavesStats0aB8SyscallsC17exclavesAvailableSbvgZ : 28 -> 308
CStrings:
+ "ExclaveCapability"
+ "PerfUtils.ExclavesStatsServer.exclaves_stats"
- "exclaves.stats"
```
