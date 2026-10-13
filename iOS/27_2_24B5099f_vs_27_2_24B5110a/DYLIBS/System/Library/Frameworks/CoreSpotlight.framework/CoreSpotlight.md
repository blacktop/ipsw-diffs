## CoreSpotlight

> `/System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-2465.1.7.0.0
-  __TEXT.__text: 0x1792f4
+2465.1.9.0.0
+  __TEXT.__text: 0x1795bc
   __TEXT.__objc_methlist: 0x147d8
   __TEXT.__const: 0xf08
   __TEXT.__cstring: 0x2bedd
   __TEXT.__gcc_except_tab: 0x9718
-  __TEXT.__oslogstring: 0xbf0c
+  __TEXT.__oslogstring: 0xbfee
   __TEXT.__ustring: 0x218e
   __TEXT.__dlopen_cstrs: 0x4c4
   __TEXT.__constg_swiftt: 0x1bc

   __TEXT.__swift_as_cont: 0xc
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x7290
+  __TEXT.__unwind_info: 0x7298
   __TEXT.__eh_frame: 0x210
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa618
+  __DATA_CONST.__objc_selrefs: 0xa620
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x748
   __DATA_CONST.__objc_arraydata: 0x11290
-  __DATA_CONST.__got: 0xe70
+  __DATA_CONST.__got: 0xe78
   __AUTH_CONST.__const: 0x2430
   __AUTH_CONST.__cfstring: 0x2e140
-  __AUTH_CONST.__objc_const: 0x20100
+  __AUTH_CONST.__objc_const: 0x20120
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x3ae0
   __AUTH_CONST.__objc_dictobj: 0xaf78

   __AUTH.__data: 0x3a0
   __AUTH.__thread_vars: 0x60
   __AUTH.__thread_bss: 0x28
-  __DATA.__objc_ivar: 0x1468
+  __DATA.__objc_ivar: 0x146c
   __DATA.__data: 0x1c60
   __DATA_DIRTY.__objc_data: 0x1388
   __DATA_DIRTY.__data: 0x20

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 8955
-  Symbols:   14690
-  CStrings:  8104
+  Functions: 8959
+  Symbols:   14692
+  CStrings:  8107
 
Symbols:
+ _NSURLFileSizeKey
+ _OBJC_IVAR_$_CSFileProviderDomainMonitor._savedRemovedCount
CStrings:
+ "At the %lu removed FP domain ceiling; not tracking further removals"
+ "Discarding saved FP domain list: %llu bytes exceeds the %llu byte budget"
+ "Saved FP domain list holds %lu entries; tracking the first %lu and ignoring the rest"
```
