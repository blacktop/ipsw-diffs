## libGPUCompilerImpl.dylib

> `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/libGPUCompilerImpl.dylib`

```diff

-32023.116.0.0.0
-  __TEXT.__text: 0x3a98dc
-  __TEXT.__auth_stubs: 0x48f0
+32023.157.0.0.0
+  __TEXT.__text: 0x3b21bc
+  __TEXT.__auth_stubs: 0x4950
   __TEXT.__init_offsets: 0x48
-  __TEXT.__const: 0x167174
-  __TEXT.__cstring: 0x28c907
-  __TEXT.__unwind_info: 0x5aa4
+  __TEXT.__const: 0x167134
+  __TEXT.__cstring: 0x28ca20
+  __TEXT.__oslogstring: 0x22
+  __TEXT.__unwind_info: 0x5be0
   __DATA_CONST.__got: 0x218
   __DATA_CONST.__const: 0x9bd78
-  __AUTH_CONST.__const: 0x8bc8
-  __AUTH_CONST.__auth_got: 0x2460
-  __AUTH.__const_weak: 0x858
+  __AUTH_CONST.__const: 0x9460
+  __AUTH_CONST.__auth_got: 0x2490
   __AUTH.__got_weak: 0x18
-  __DATA.__got_weak: 0x838
+  __DATA.__got_weak: 0x850
   __DATA.__data: 0x1c
   __DATA.__thread_vars: 0x30
   __DATA.__thread_bss: 0x11
   __DATA.__common: 0x22
-  __DATA.__bss: 0x6e9
+  __DATA.__bss: 0x701
   __DATA_DIRTY.__data: 0x10
   __DATA_DIRTY.__common: 0x608
   __DATA_DIRTY.__bss: 0x1768

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libllvm-flatbuffers.dylib
   - /usr/lib/libllvm-lmdb.dylib
-  UUID: 0FA6A74A-E71A-3C1E-8EA2-9C40EE05F5C1
-  Functions: 9246
-  Symbols:   2766
-  CStrings:  14757
+  UUID: B8FA966B-866B-3E59-8028-91D65C3F2892
+  Functions: 9417
+  Symbols:   2777
+  CStrings:  14768
 
Symbols:
+ __ZN4llvm3air10APITrackerC1EPKc
+ __ZN4llvm3air10APITrackerC2EPKc
+ __ZN4llvm3air10APITrackerD1Ev
+ __ZN4llvm3air10APITrackerD2Ev
+ __ZNK4llvm17ManagedStaticBase21RegisterManagedStaticEPFPvvEPFvS1_E
+ __ZNSt3__119piecewise_constructE
+ __os_signpost_emit_with_name_impl
+ _getrusage
+ _os_log_create
+ _os_release
+ _os_signpost_enabled
+ _os_signpost_id_generate
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1ERKS5_
CStrings:
+ "%s"
+ "%s(MaxRSS = %ld bytes)"
+ "32023.157"
+ "APICall"
+ "PointsOfInterest"
+ "com.apple.metalfe.embedded.internal"
+ "compute or fragment"
+ "expecting '%s' stage in pipeline no. '%d'"
+ "missing '%s' stage in pipeline no. '%d'"
+ "missing unit id for compute pipeline"
+ "missing unit id for tile render pipeline"
+ "unexpecting stages in pipelino no. '%d"
+ "unknown pipeline flags ("
- "32023.116"
- "device-lowering"

```
