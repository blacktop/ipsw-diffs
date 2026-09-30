## libRPAC.dylib

> `/usr/lib/libRPAC.dylib`

```diff

-83.0.0.0.0
-  __TEXT.__text: 0x8e2fc
-  __TEXT.__auth_stubs: 0x7b0
+84.0.0.0.0
+  __TEXT.__text: 0x8e1ac
+  __TEXT.__auth_stubs: 0x790
   __TEXT.__objc_stubs: 0x1a0
   __TEXT.__init_offsets: 0x4
-  __TEXT.__cstring: 0x4aaa
+  __TEXT.__cstring: 0x4a0f
   __TEXT.__gcc_except_tab: 0x44
   __TEXT.__const: 0x1d60
   __TEXT.__objc_methname: 0x13b
   __TEXT.__oslogstring: 0x1d
   __TEXT.__objc_classname: 0x1
-  __TEXT.__unwind_info: 0x250
-  __DATA_CONST.__auth_got: 0x3f0
+  __TEXT.__unwind_info: 0x288
+  __DATA_CONST.__auth_got: 0x3e0
   __DATA_CONST.__got: 0x80
   __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__const: 0x3b8

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__objc_arrayobj: 0x30
+  __AUTH_CONST.__interpose: 0x90
   __DATA.__objc_selrefs: 0x88
   __DATA.__data: 0x7c8
-  __DATA.__interpose: 0x90
   __DATA.__common: 0x800e8
   __DATA.__bss: 0x580630
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F59A1452-7680-372D-9845-B7A10BD4E11C
-  Functions: 191
-  Symbols:   542
-  CStrings:  563
+  UUID: C2FEA880-24AE-3CE4-A9F2-085EFA251870
+  Functions: 194
+  Symbols:   547
+  CStrings:  558
 
Symbols:
+ _Z22initializePrimitiveMapv.cold.1
+ __ZSt28__throw_bad_array_new_lengthB8ne190102v
+ createPrimitiveEntry.cold.1
+ culledOsLogFault.cold.2
+ findPrimitiveInfoNoAssert.cold.1
+ getNumCPU.cold.1
+ isAppleInternal.cold.1
+ shouldFlag.cold.3
+ suppressionCheck.cold.1
+ swizzleAPIsForHangDetection.cold.1
+ ticks_to_ns.cold.2
- __ZSt28__throw_bad_array_new_lengthB8ne180100v
- _wordexp
- _wordfree
- initializeSwizzlers.cold.1
- initializeSwizzlers.cold.2
- initializeSwizzlers.cold.3
CStrings:
- "Swizzlers.m"
- "getAppleInternalReplacementImplementationInstanceMethod"
- "getReplacementImplementationClassMethod"
- "getReplacementImplementationInstanceMethod"
- "qos"

```
