## tmutil

> `/usr/bin/tmutil`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__cstring`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_ivar`

```diff

-2612.1.0.0.0
-  __TEXT.__text: 0x23c20
+2614.1.0.0.0
+  __TEXT.__text: 0x23c9c
   __TEXT.__auth_stubs: 0x1070
-  __TEXT.__objc_stubs: 0x3500
-  __TEXT.__objc_methlist: 0xc54
+  __TEXT.__objc_stubs: 0x3540
+  __TEXT.__objc_methlist: 0xc64
   __TEXT.__const: 0x6a0
   __TEXT.__cstring: 0x33d5
-  __TEXT.__objc_methname: 0x3445
+  __TEXT.__objc_methname: 0x34da
   __TEXT.__objc_classname: 0x21b
-  __TEXT.__objc_methtype: 0x4a9
+  __TEXT.__objc_methtype: 0x49d
   __TEXT.__gcc_except_tab: 0x360
   __TEXT.__constg_swiftt: 0x270
   __TEXT.__swift5_typeref: 0x3bf
   __TEXT.__swift5_builtin: 0x78
-  __TEXT.__swift5_reflstr: 0x25c
-  __TEXT.__swift5_fieldmd: 0x24c
+  __TEXT.__swift5_reflstr: 0x27c
+  __TEXT.__swift5_fieldmd: 0x258
   __TEXT.__swift5_capture: 0x5c
   __TEXT.__swift5_assocty: 0x68
   __TEXT.__swift5_proto: 0x20

   __DATA_CONST.__auth_got: 0x848
   __DATA_CONST.__got: 0x4c0
   __DATA_CONST.__auth_ptr: 0x1b0
-  __DATA.__objc_const: 0x16c0
-  __DATA.__objc_selrefs: 0xf88
+  __DATA.__objc_const: 0x16f0
+  __DATA.__objc_selrefs: 0xf98
   __DATA.__objc_ivar: 0xc4
-  __DATA.__objc_data: 0x648
-  __DATA.__data: 0x670
+  __DATA.__objc_data: 0x650
+  __DATA.__data: 0x680
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/swift/libswift_DarwinFoundation2.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 619
+  Functions: 620
   Symbols:   499
-  CStrings:  1133
+  CStrings:  1136
 
CStrings:
+ "       %s %s [-@acdefghlmnstuETUX] [-D depth] [-I name] path1 path2\n"
+ "       %s %s [-@acdefghlmnstuETX] [-D depth] [-I name] snapshot_path\n"
+ "@88@0:8Q16@24@32@40B48B52B56B60B64@68@76B84"
+ "@acdefghilmnrstuzD:EI:RTUVX"
+ "TB,N,R,VtolerateCopierTimestampRounding"
+ "Usage: %s %s [-@acdefghlmnstuETX] [-D depth] [-I name]\n"
+ "initWithFlags:depth:ignoredXattrPrefixes:ignoredPathComponents:verbose:ignoreRoots:respectExclusions:respectVolumeUUIDs:printDifferences:includedDisks:plistStream:tolerateCopierTimestampRounding:"
+ "setToleratesCopierTimestampRounding:"
+ "tolerateCopierTimestampRounding"
- "       %s %s [-@acdefghlmnstuEUX] [-D depth] [-I name] path1 path2\n"
- "       %s %s [-@acdefghlmnstuEX] [-D depth] [-I name] snapshot_path\n"
- "@84@0:8Q16@24@32@40B48B52B56B60B64@68@76"
- "@acdefghilmnrstuzD:EI:RUVX"
- "Usage: %s %s [-@acdefghlmnstuEX] [-D depth] [-I name]\n"
- "initWithFlags:depth:ignoredXattrPrefixes:ignoredPathComponents:verbose:ignoreRoots:respectExclusions:respectVolumeUUIDs:printDifferences:includedDisks:plistStream:"
```
