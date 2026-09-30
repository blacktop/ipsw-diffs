## PosterUIFoundation

> `/System/Library/PrivateFrameworks/PosterUIFoundation.framework/PosterUIFoundation`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_floatobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-347.102.0.0.0
-  __TEXT.__text: 0x94324
-  __TEXT.__objc_methlist: 0xab8c
-  __TEXT.__const: 0xdc4
-  __TEXT.__oslogstring: 0x3961
-  __TEXT.__cstring: 0x66a3
+350.1.100.0.0
+  __TEXT.__text: 0x93db0
+  __TEXT.__objc_methlist: 0xab64
+  __TEXT.__const: 0xdb4
+  __TEXT.__oslogstring: 0x38a1
+  __TEXT.__cstring: 0x6663
   __TEXT.__gcc_except_tab: 0x1674
   __TEXT.__dlopen_cstrs: 0x216
   __TEXT.__swift5_typeref: 0x7f2

   __TEXT.__swift5_proto: 0x28
   __TEXT.__swift5_types: 0x2c
   __TEXT.__swift5_capture: 0x30
-  __TEXT.__unwind_info: 0x29f0
+  __TEXT.__unwind_info: 0x29d0
   __TEXT.__eh_frame: 0x40
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0xe0
   __DATA_CONST.__objc_protolist: 0x1c0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x58e8
+  __DATA_CONST.__objc_selrefs: 0x58c8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x410
   __DATA_CONST.__objc_arraydata: 0x18e0
-  __DATA_CONST.__got: 0xf98
+  __DATA_CONST.__got: 0xf90
   __AUTH_CONST.__const: 0x10c0
   __AUTH_CONST.__cfstring: 0x7f20
-  __AUTH_CONST.__objc_const: 0x1efc0
+  __AUTH_CONST.__objc_const: 0x1ef80
   __AUTH_CONST.__objc_dictobj: 0xcf8
   __AUTH_CONST.__objc_intobj: 0xdb0
   __AUTH_CONST.__objc_doubleobj: 0x2b0
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH_CONST.__auth_got: 0x1098
+  __AUTH_CONST.__auth_got: 0x1090
   __AUTH.__objc_data: 0x2410
   __AUTH.__data: 0x1a0
-  __DATA.__objc_ivar: 0xbe4
+  __DATA.__objc_ivar: 0xbdc
   __DATA.__data: 0x17a8
   __DATA.__bss: 0x8c0
   __DATA.__common: 0x18

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4142
-  Symbols:   9650
-  CStrings:  1493
+  Functions: 4136
+  Symbols:   9640
+  CStrings:  1489
 
Symbols:
- -[PUIPosterSnapshotter _lock_retryStartupLater]
- -[PUIPosterSnapshotter consecutiveStartupFailuresForTesting]
- -[PUIPosterSnapshotter setConsecutiveStartupFailuresForTesting:]
- _OBJC_IVAR_$_PUIPosterSnapshotter._lock_consecutiveStartupFailures
- _OBJC_IVAR_$_PUIPosterSnapshotter._lock_waitingForRetry
- ___47-[PUIPosterSnapshotter _lock_retryStartupLater]_block_invoke
- _exp2
- _kPFErrorDomain
- _objc_msgSend$_lock_retryStartupLater
- _objc_msgSend$domain
CStrings:
+ "(%{public}@) Booted extension process is invalid (no error) — treating as a boot failure"
+ "(%{public}@) couldn't get assertions; invalidating so the request can be retried on a fresh process"
+ "Snapshotter state error: shouldn't call %s while waiting for extension"
+ "\xb1"
- "(%{public}@) Booted extension process is invalid (no error) — treating as a startup failure"
- "(%{public}@) Exceeded %lu consecutive mid-snapshot interruptions, giving up"
- "(%{public}@) Exceeded %lu consecutive startup failures, giving up"
- "(%{public}@) Retrying startup in %.1f seconds (attempt %lu/%lu)"
- "(%{public}@) couldn't get assertions, deferring snapshot"
- "-[PUIPosterSnapshotter setConsecutiveStartupFailuresForTesting:]"
- "Snapshotter state error: shouldn't call %s while waiting: for retry? %d; for extension? %d"
- "\xc1"
```
