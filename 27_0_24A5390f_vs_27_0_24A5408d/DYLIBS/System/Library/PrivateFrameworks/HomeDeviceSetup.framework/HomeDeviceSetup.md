## HomeDeviceSetup

> `/System/Library/PrivateFrameworks/HomeDeviceSetup.framework/HomeDeviceSetup`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`

```diff

-405.0.7.0.0
-  __TEXT.__text: 0x72750
-  __TEXT.__objc_methlist: 0x3444
+405.0.11.0.0
+  __TEXT.__text: 0x729fc
+  __TEXT.__objc_methlist: 0x345c
   __TEXT.__const: 0x478
-  __TEXT.__cstring: 0x1aa54
+  __TEXT.__cstring: 0x1aae4
   __TEXT.__oslogstring: 0x81d
   __TEXT.__gcc_except_tab: 0x294
   __TEXT.__constg_swiftt: 0xe0

   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift_as_ret: 0x24
   __TEXT.__swift_as_cont: 0x28
-  __TEXT.__unwind_info: 0x1868
+  __TEXT.__unwind_info: 0x1870
   __TEXT.__eh_frame: 0x468
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2da0
+  __DATA_CONST.__objc_selrefs: 0x2db0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x70
   __DATA_CONST.__objc_arraydata: 0x230
   __DATA_CONST.__got: 0x410
   __AUTH_CONST.__const: 0xc38
-  __AUTH_CONST.__cfstring: 0x5580
-  __AUTH_CONST.__objc_const: 0x7878
+  __AUTH_CONST.__cfstring: 0x55a0
+  __AUTH_CONST.__objc_const: 0x78b8
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x3c0
   __AUTH_CONST.__objc_intobj: 0x1e0
   __AUTH_CONST.__auth_got: 0x848
   __AUTH.__objc_data: 0x778
   __AUTH.__data: 0x328
-  __DATA.__objc_ivar: 0xa48
+  __DATA.__objc_ivar: 0xa50
   __DATA.__data: 0xb70
   __DATA.__common: 0x40
   __DATA.__bss: 0x7d0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3076
-  Symbols:   4370
-  CStrings:  3118
+  Functions: 3080
+  Symbols:   4377
+  CStrings:  3122
 
Symbols:
+ -[HDSSetupSession _armTRAuthenticationTimeout]
+ -[HDSSetupSession _runTRAuthenticationTimeout]
+ GCC_except_table372
+ GCC_except_table424
+ _OBJC_IVAR_$_HDSSetupSession._trAuthTimedOut
+ _OBJC_IVAR_$_HDSSetupSession._trAuthTimeoutTimer
+ ___46-[HDSSetupSession _armTRAuthenticationTimeout]_block_invoke
+ _objc_msgSend$_armTRAuthenticationTimeout
+ _objc_msgSend$_runTRAuthenticationTimeout
- GCC_except_table369
- GCC_except_table421
CStrings:
+ "### TRAuthentication timed out after %d seconds (stage %@)\n"
+ "-[HDSSetupSession _runTRAuthenticationTimeout]"
+ "TRAuth timed out after %d secs"
+ "TRAuthTimeout"
```
