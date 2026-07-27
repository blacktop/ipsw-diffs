## Diagnostics Reporter

> `/System/Library/CoreServices/Diagnostics Reporter.app/Contents/MacOS/Diagnostics Reporter`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_entry`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA_CONST.__const`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-934.160.3.0.0
-  __TEXT.__text: 0x183cc
-  __TEXT.__auth_stubs: 0x1020
+934.160.4.0.0
+  __TEXT.__text: 0x18498
+  __TEXT.__auth_stubs: 0x1030
   __TEXT.__objc_stubs: 0x740
   __TEXT.__objc_methlist: 0x518
-  __TEXT.__cstring: 0x6d5
+  __TEXT.__cstring: 0x725
   __TEXT.__const: 0x1024
   __TEXT.__constg_swiftt: 0x604
   __TEXT.__swift5_typeref: 0x9a6

   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__unwind_info: 0x538
   __TEXT.__eh_frame: 0x328
-  __DATA_CONST.__auth_got: 0x818
+  __DATA_CONST.__auth_got: 0x820
   __DATA_CONST.__got: 0x278
   __DATA_CONST.__auth_ptr: 0x360
   __DATA_CONST.__const: 0xb70

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 474
-  Symbols:   457
-  CStrings:  307
+  Functions: 475
+  Symbols:   458
+  CStrings:  310
 
Symbols:
+ __os_feature_enabled_impl
CStrings:
+ "OSAnalytics"
+ "com.apple.DiagnosticsReporter"
+ "forceSeedFeedbackPrompting"
```
