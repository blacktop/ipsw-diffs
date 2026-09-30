## libRPAC.dylib

> `/usr/lib/libRPAC.dylib`

```diff

 83.0.0.0.0
-  __TEXT.__text: 0x924f8
+  __TEXT.__text: 0x9245c
   __TEXT.__auth_stubs: 0xad0
   __TEXT.__objc_stubs: 0x1a0
   __TEXT.__init_offsets: 0x4
-  __TEXT.__cstring: 0x522b
+  __TEXT.__cstring: 0x5190
   __TEXT.__gcc_except_tab: 0x5c
   __TEXT.__const: 0x1d58
   __TEXT.__objc_methname: 0x13b
   __TEXT.__oslogstring: 0x1d
   __TEXT.__objc_classname: 0x1
-  __TEXT.__unwind_info: 0x2e8
+  __TEXT.__unwind_info: 0x320
   __DATA_CONST.__auth_got: 0x580
   __DATA_CONST.__got: 0x148
   __DATA_CONST.__auth_ptr: 0x10

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__objc_arrayobj: 0x30
+  __AUTH_CONST.__interpose: 0x230
   __DATA.__objc_selrefs: 0x88
   __DATA.__data: 0x7c8
-  __DATA.__interpose: 0x230
   __DATA.__common: 0x800e8
   __DATA.__bss: 0x5809e0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 273
-  Symbols:   724
-  CStrings:  640
+  Functions: 277
+  Symbols:   732
+  CStrings:  635
 
Symbols:
+ _Z22initializePrimitiveMapv.cold.1
+ _ZL13getTableIndexl.cold.1
+ __ZSt28__throw_bad_array_new_lengthB8ne190102v
+ _objc_release_x25
+ _objc_retain_x25
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
- _objc_release_x26
- _objc_retain_x26
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
