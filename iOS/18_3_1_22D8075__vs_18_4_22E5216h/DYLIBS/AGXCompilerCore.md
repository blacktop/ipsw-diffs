## AGXCompilerCore

> `/System/Library/PrivateFrameworks/AGXCompilerCore.framework/AGXCompilerCore`

```diff

-324.6.0.0.0
-  __TEXT.__text: 0x1d083c
-  __TEXT.__auth_stubs: 0x22b0
-  __TEXT.__const: 0x481b8
-  __TEXT.__cstring: 0x15650
-  __TEXT.__oslogstring: 0x343
-  __TEXT.__unwind_info: 0x34b8
+325.30.0.0.0
+  __TEXT.__text: 0x1cc230
+  __TEXT.__auth_stubs: 0x22a0
+  __TEXT.__const: 0x482c8
+  __TEXT.__cstring: 0x15782
+  __TEXT.__oslogstring: 0x40f
+  __TEXT.__unwind_info: 0x3240
   __TEXT.__objc_methname: 0xa2
   __TEXT.__objc_stubs: 0x100
   __DATA_CONST.__got: 0x108
   __DATA_CONST.__const: 0x62b0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x40
-  __AUTH_CONST.__auth_got: 0x1160
+  __AUTH_CONST.__auth_got: 0x1158
   __AUTH_CONST.__const: 0x6d0d0
-  __AUTH_CONST.__cfstring: 0xe0
+  __AUTH_CONST.__cfstring: 0xc0
   __AUTH.__data: 0x70
   __DATA.__data: 0x8
-  __DATA.__bss: 0x3260
+  __DATA.__bss: 0x3288
   __DATA_DIRTY.__bss: 0xf38
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libllvm-flatbuffers.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5953
-  Symbols:   6579
-  CStrings:  3812
+  Functions: 5749
+  Symbols:   6600
+  CStrings:  3828
 
Symbols:
+ _AIRNTGetPreferredAIRArch
+ _CFStringGetCStringPtr
- _CFStringCreateWithBytes
- __ZNSt3__115system_categoryEv
CStrings:
+ "%s bitcode_url is NULL for bundle '%s', filename '%s', extension '%s' and subdirectory '%s'"
+ "%s bundle not found"
+ "%s file_name is empty"
+ "%s filename is NULL"
+ "%s path was not initialized to %s"
+ "%s posix_path is NULL"
+ "%s subdirectory is NULL"
+ "+aggressive-ipr-alloc-in-complex-cfg"
+ ".i64"
+ "AGC_ENABLE_ATOMIC_SMASHING_FOR_RELEASE_ATOMICS"
+ "after optimizeReleaseAtomicsByDisableSmashing"
+ "air.atomic"
+ "air.atomic.fence"
+ "auto AGCLLVMObject::readBitcode(AGCLLVMCtx &, llvm::LLVMContext &, llvm::StringRef, bool)::(anonymous class)::operator()() const"
+ "cmpxchg"
+ "global bindings unsupported prior to Apple6 GPU family"
+ "i64"
+ "xchg"
- " type does not match between vertex and fragment function"
- "Bitcode URL for '%s' is NULL."

```
