## AppIntentsLiveEntityService

> `/System/Library/PrivateFrameworks/AppIntentsLiveEntitySupport.framework/XPCServices/AppIntentsLiveEntityService.xpc/AppIntentsLiveEntityService`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_mpenum`
- `__DATA.__objc_selrefs`

```diff

-301.2.7.2.0
-  __TEXT.__text: 0x45438
-  __TEXT.__auth_stubs: 0x16d0
+301.2.12.2.0
+  __TEXT.__text: 0x4caa0
+  __TEXT.__auth_stubs: 0x17e0
   __TEXT.__objc_stubs: 0x420
-  __TEXT.__const: 0x1a98
+  __TEXT.__const: 0x1ea8
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__oslogstring: 0x14c3
-  __TEXT.__swift5_typeref: 0x9cc
-  __TEXT.__cstring: 0x1089
-  __TEXT.__constg_swiftt: 0x4e0
+  __TEXT.__oslogstring: 0x1673
+  __TEXT.__swift5_typeref: 0xab2
+  __TEXT.__cstring: 0x10d9
+  __TEXT.__constg_swiftt: 0x5ac
   __TEXT.__swift5_builtin: 0x28
-  __TEXT.__swift5_reflstr: 0x2b9
-  __TEXT.__swift5_fieldmd: 0x380
-  __TEXT.__swift5_types: 0x4c
-  __TEXT.__swift_as_entry: 0x190
-  __TEXT.__swift_as_ret: 0x1e4
-  __TEXT.__swift_as_cont: 0x2d0
-  __TEXT.__objc_classname: 0x1bf
-  __TEXT.__objc_methname: 0x40a
+  __TEXT.__swift5_reflstr: 0x309
+  __TEXT.__swift5_fieldmd: 0x3e8
+  __TEXT.__swift5_types: 0x54
+  __TEXT.__swift_as_entry: 0x1d4
+  __TEXT.__swift_as_ret: 0x230
+  __TEXT.__swift_as_cont: 0x3d0
+  __TEXT.__objc_classname: 0x23f
+  __TEXT.__objc_methname: 0x42a
   __TEXT.__objc_methtype: 0x3d
-  __TEXT.__swift5_capture: 0x1224
+  __TEXT.__swift5_capture: 0x13d0
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__swift5_proto: 0x80
-  __TEXT.__swift5_assocty: 0xa8
-  __TEXT.__swift5_acfuncs: 0x104
-  __TEXT.__unwind_info: 0x14d8
-  __TEXT.__eh_frame: 0x4388
-  __DATA_CONST.__const: 0x30c0
-  __DATA_CONST.__objc_classlist: 0x40
+  __TEXT.__swift5_proto: 0xa0
+  __TEXT.__swift5_assocty: 0xe0
+  __TEXT.__swift5_acfuncs: 0x12c
+  __TEXT.__unwind_info: 0x1808
+  __TEXT.__eh_frame: 0x4d80
+  __DATA_CONST.__const: 0x34f8
+  __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0xb70
-  __DATA_CONST.__got: 0x380
-  __DATA_CONST.__auth_ptr: 0x390
-  __DATA.__objc_const: 0x688
+  __DATA_CONST.__auth_got: 0xbf8
+  __DATA_CONST.__got: 0x3e0
+  __DATA_CONST.__auth_ptr: 0x3e8
+  __DATA.__objc_const: 0x830
   __DATA.__objc_selrefs: 0x108
-  __DATA.__objc_data: 0xf0
-  __DATA.__data: 0xdb8
-  __DATA.__common: 0x60
+  __DATA.__objc_data: 0x140
+  __DATA.__data: 0x1028
+  __DATA.__common: 0x70
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AppIntentsLiveEntitySupport.framework/AppIntentsLiveEntitySupport
   - /System/Library/PrivateFrameworks/LinkMetadata.framework/LinkMetadata

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1847
-  Symbols:   216
-  CStrings:  201
+  Functions: 2084
+  Symbols:   223
+  CStrings:  214
 
Symbols:
+ _os_transaction_create
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
+ _swift_weakDestroy
+ _swift_weakInit
+ _swift_weakLoadStrong
+ _xpc_transaction_exit_clean
CStrings:
+ "%s::acquire failed: %@"
+ "%s::acquire rejected: caller has no live entity entitlement"
+ "%s::acquire(warming: %{public}ld feature(s)) completed"
+ "KeepAliveHold reached its maximum duration, releasing"
+ "Missing live entity entitlement"
+ "Service: arming idle exit timeout for %{public}s"
+ "Service: endActivity() called without a matching beginActivity()"
+ "Service: no client activity for %{public}s, exiting"
+ "_TtC27AppIntentsLiveEntityService13KeepAliveHold"
+ "_TtC27AppIntentsLiveEntityService14KeepAliveActor"
+ "com.apple.appintents.LiveEntityService.activity"
+ "expiry"
+ "hold"
```
