## apsd

> `/System/Library/PrivateFrameworks/ApplePushService.framework/apsd`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_protos`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1168.200.41.0.0
-  __TEXT.__text: 0x11b2e8
+1168.200.51.0.0
+  __TEXT.__text: 0x11b70c
   __TEXT.__auth_stubs: 0x35f0
-  __TEXT.__objc_stubs: 0x10ee0
+  __TEXT.__objc_stubs: 0x10f80
   __TEXT.__init_offsets: 0xc
-  __TEXT.__objc_methlist: 0xb990
-  __TEXT.__objc_methname: 0x1bdc5
+  __TEXT.__objc_methlist: 0xb9e0
+  __TEXT.__objc_methname: 0x1bef5
   __TEXT.__objc_classname: 0x13ef
   __TEXT.__objc_methtype: 0x56e9
-  __TEXT.__cstring: 0xfe43
+  __TEXT.__cstring: 0xfe83
   __TEXT.__const: 0x12503
-  __TEXT.__oslogstring: 0x14525
-  __TEXT.__gcc_except_tab: 0x2680
+  __TEXT.__oslogstring: 0x145e5
+  __TEXT.__gcc_except_tab: 0x2698
   __TEXT.__dlopen_cstrs: 0x15e
   __TEXT.__constg_swiftt: 0x1540
   __TEXT.__swift5_typeref: 0xb26

   __TEXT.__swift_as_cont: 0x50
   __TEXT.__swift5_assocty: 0x78
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x5ff0
+  __TEXT.__unwind_info: 0x6010
   __TEXT.__eh_frame: 0x700
-  __DATA_CONST.__const: 0xa380
-  __DATA_CONST.__cfstring: 0x85c0
+  __DATA_CONST.__const: 0xa3a0
+  __DATA_CONST.__cfstring: 0x8600
   __DATA_CONST.__objc_classlist: 0x430
   __DATA_CONST.__objc_protolist: 0x2b8
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__auth_got: 0x1b10
   __DATA_CONST.__got: 0x970
   __DATA_CONST.__auth_ptr: 0x200
-  __DATA.__objc_const: 0x1d1b0
-  __DATA.__objc_selrefs: 0x5730
-  __DATA.__objc_ivar: 0xbc8
+  __DATA.__objc_const: 0x1d210
+  __DATA.__objc_selrefs: 0x5760
+  __DATA.__objc_ivar: 0xbd0
   __DATA.__objc_data: 0x38f8
   __DATA.__data: 0x4968
   __DATA.__common: 0x1d8

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 7003
+  Functions: 7012
   Symbols:   1220
-  CStrings:  8696
+  CStrings:  8712
 
CStrings:
+ "%@ not resending deferred daemonAlive, no longer nearby"
+ "%@ previous daemonAlive failed with retry later, resending in %f seconds"
+ "%@ previous daemonAlive failed with retry later, retry already scheduled"
+ "IDSFoundation"
+ "IDSSendErrorDomain"
+ "TB,N,V_mainQueue_daemonAliveRetryScheduled"
+ "Td,N,V_retryLaterDelay"
+ "_isRetryLaterError:"
+ "_mainQueue_daemonAliveRetryScheduled"
+ "_resendDaemonAliveMessageAfterFailureWithError:"
+ "_retryLaterDelay"
+ "com.apple.ids.idssenderrordomain"
+ "mainQueue_daemonAliveRetryScheduled"
+ "retryLaterDelay"
+ "setMainQueue_daemonAliveRetryScheduled:"
+ "setRetryLaterDelay:"
```
