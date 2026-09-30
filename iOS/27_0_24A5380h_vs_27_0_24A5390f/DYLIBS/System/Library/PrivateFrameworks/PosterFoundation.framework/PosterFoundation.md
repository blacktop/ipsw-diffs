## PosterFoundation

> `/System/Library/PrivateFrameworks/PosterFoundation.framework/PosterFoundation`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_proto`
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
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-347.102.0.0.0
-  __TEXT.__text: 0x5e1e0
-  __TEXT.__objc_methlist: 0x3aa0
-  __TEXT.__const: 0x558
-  __TEXT.__cstring: 0x4969
-  __TEXT.__oslogstring: 0x47d1
+350.1.100.0.0
+  __TEXT.__text: 0x5e500
+  __TEXT.__objc_methlist: 0x3ab8
+  __TEXT.__const: 0x568
+  __TEXT.__cstring: 0x49b9
+  __TEXT.__oslogstring: 0x4911
   __TEXT.__gcc_except_tab: 0xe28
   __TEXT.__swift5_typeref: 0x44d
   __TEXT.__swift5_capture: 0x2b8

   __TEXT.__swift_as_cont: 0x44
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_proto: 0x4
-  __TEXT.__unwind_info: 0x18d8
+  __TEXT.__unwind_info: 0x18e0
   __TEXT.__eh_frame: 0x838
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2270
+  __DATA_CONST.__objc_selrefs: 0x2280
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x190
   __DATA_CONST.__objc_arraydata: 0x250
   __DATA_CONST.__got: 0x608
   __AUTH_CONST.__const: 0x14c0
-  __AUTH_CONST.__cfstring: 0x4480
-  __AUTH_CONST.__objc_const: 0x9390
+  __AUTH_CONST.__cfstring: 0x44c0
+  __AUTH_CONST.__objc_const: 0x93e0
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0xd68
+  __AUTH_CONST.__auth_got: 0xd70
   __AUTH.__objc_data: 0x628
   __AUTH.__data: 0x98
-  __DATA.__objc_ivar: 0x310
+  __DATA.__objc_ivar: 0x318
   __DATA.__data: 0xd60
   __DATA.__bss: 0xd0
   __DATA.__common: 0x30

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2175
-  Symbols:   3909
-  CStrings:  1014
+  Functions: 2178
+  Symbols:   3916
+  CStrings:  1018
 
Symbols:
+ -[PFPosterExtensionInstanceProvider initWithDefaultInstanceIdentifier:maxNumberOfInstancesPerExtension:]
+ -[PFPosterExtensionInstanceProvider maxNumberOfInstancesPerExtension]
+ GCC_except_table68
+ _OBJC_IVAR_$_PFPosterExtensionInstanceProvider._lock_releasedInstances
+ _OBJC_IVAR_$_PFPosterExtensionInstanceProvider._maxNumberOfInstancesPerExtension
+ _PFDispatchTimeAfterSeconds
+ ___104-[PFPosterExtensionInstanceProvider initWithDefaultInstanceIdentifier:maxNumberOfInstancesPerExtension:]_block_invoke
+ _dispatch_time
+ _objc_msgSend$initWithDefaultInstanceIdentifier:maxNumberOfInstancesPerExtension:
- GCC_except_table67
- ___71-[PFPosterExtensionInstanceProvider initWithDefaultInstanceIdentifier:]_block_invoke
CStrings:
+ "(%p) BACKSTOP HIT: extension '%{public}@' already has %lu live instances (max %lu); refusing to create another for reason '%{public}@' — an upstream gate over-admitted (accounting bug). rdar://181536204"
+ "(%p) relinquish of UNKNOWN instance '%{public}@'/%{public}@ for reason '%{public}@' — never vended by this provider"
+ "(%p) relinquish of already-released instance '%{public}@'/%{public}@ for reason '%{public}@' — no-op"
+ "exceeds max number of instances for extension"
+ "maxNumberOfInstancesPerExtension"
- "(%p) attempted to relinquish unknown or mismatched instance '%{public}@'/%{public}@ for reason '%{public}@'"
```
