## libswiftDistributed.dylib

> `/usr/lib/swift/libswiftDistributed.dylib`

```diff

-6.0.3.1.6
-  __TEXT.__text: 0xb144
-  __TEXT.__auth_stubs: 0x6f0
-  __TEXT.__cstring: 0xbda
+6.1.0.109.3
+  __TEXT.__text: 0xc2d4
+  __TEXT.__auth_stubs: 0x7a0
+  __TEXT.__cstring: 0xe24
   __TEXT.__swift5_typeref: 0x44a
   __TEXT.__swift5_capture: 0x50
-  __TEXT.__const: 0x86e
+  __TEXT.__const: 0x878
   __TEXT.__swift5_reflstr: 0x1c7
   __TEXT.__swift5_assocty: 0x80
   __TEXT.__swift5_fieldmd: 0x280

   __TEXT.__swift5_protos: 0x1c
   __TEXT.__swift5_proto: 0x54
   __TEXT.__swift5_types: 0x40
-  __TEXT.__unwind_info: 0x4a0
-  __TEXT.__eh_frame: 0x830
-  __DATA_CONST.__got: 0xa8
+  __TEXT.__swift_as_entry: 0x4c
+  __TEXT.__swift_as_ret: 0x3c
+  __TEXT.__oslogstring: 0xd
+  __TEXT.__unwind_info: 0x4a8
+  __TEXT.__eh_frame: 0x858
+  __DATA_CONST.__got: 0xc0
   __DATA_CONST.__const: 0x48
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __AUTH_CONST.__auth_got: 0x378
+  __AUTH_CONST.__auth_got: 0x3d0
   __AUTH_CONST.__auth_ptr: 0x150
   __AUTH_CONST.__const: 0x5e8
   __AUTH_CONST.__objc_const: 0x310
   __DATA.__data: 0x168
-  __DATA.__bss: 0x9c0
+  __DATA.__bss: 0x9e8
   __DATA_DIRTY.__data: 0x3b8
   __DATA_DIRTY.__bss: 0x80
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 340
-  Symbols:   720
-  CStrings:  68
+  Functions: 354
+  Symbols:   742
+  CStrings:  87
 
Symbols:
+ _$s6Darwin6stderrSpySo7__sFILEVGvg
+ _$sSpMa
+ _$sSvN
+ ___progname
+ __os_log_impl
+ _dispatch_once_f
+ _fputs
+ _mach_task_self_
+ _os_log_create
+ _os_log_type_enabled
+ _strcmp
+ _swift_distributed_log_info
+ _swift_distributed_use_guarded_alloc
+ _vm_allocate
+ _vm_deallocate
+ _vm_protect
CStrings:
+ " @ "
+ " greater than page size, we'll leak some memory when we free\n"
+ " subs="
+ "%{public}.*s"
+ "Distributed"
+ "WARNING: big allocation "
+ "argumentType="
+ "com.apple.swift.distributed"
+ "doAllocateReturnTypeBuffer: R="
+ "doDestroyReturnTypeBuffer: R="
+ "doDestroyReturnTypeBuffer: allocate("
+ "doDestroyReturnTypeBuffer: deinitialize("
+ "executeDistributedTarget: append "
+ "executeDistributedTarget: subs.count="
+ "executeDistributedTarget: target="
+ "non-power-of-two alignment "
+ "remoteappintentsd"
+ "vm_allocate failed with error "
+ "vm_deallocate failed with error "
+ "vm_protect failed with error "
- "Index out of range"

```
