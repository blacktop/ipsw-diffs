## MetalTools

> `/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`

```diff

-372.11.0.0.0
-  __TEXT.__text: 0x132e0c
+372.12.0.0.0
+  __TEXT.__text: 0x1332a4
   __TEXT.__auth_stubs: 0xd40
-  __TEXT.__objc_methlist: 0x1972c
+  __TEXT.__objc_methlist: 0x197c4
   __TEXT.__gcc_except_tab: 0x2e6c
   __TEXT.__cstring: 0x33a46
   __TEXT.__const: 0x480
   __TEXT.__oslogstring: 0x282e
-  __TEXT.__unwind_info: 0x52f8
+  __TEXT.__unwind_info: 0x5320
   __TEXT.__objc_classname: 0x257a
-  __TEXT.__objc_methname: 0x1f1a3
-  __TEXT.__objc_methtype: 0x1831b
-  __TEXT.__objc_stubs: 0x17120
+  __TEXT.__objc_methname: 0x1f270
+  __TEXT.__objc_methtype: 0x1832c
+  __TEXT.__objc_stubs: 0x171a0
   __DATA_CONST.__got: 0xb48
   __DATA_CONST.__const: 0x1b80
   __DATA_CONST.__objc_classlist: 0x758
   __DATA_CONST.__objc_protolist: 0x4d0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x64e0
+  __DATA_CONST.__objc_selrefs: 0x6500
   __DATA_CONST.__objc_protorefs: 0xa0
-  __DATA_CONST.__objc_superrefs: 0x660
+  __DATA_CONST.__objc_superrefs: 0x668
   __AUTH_CONST.__auth_got: 0x6b0
   __AUTH_CONST.__const: 0x1d0
   __AUTH_CONST.__cfstring: 0xe9e0
-  __AUTH_CONST.__objc_const: 0x471b8
+  __AUTH_CONST.__objc_const: 0x471d8
   __AUTH.__thread_vars: 0x18
   __AUTH.__thread_bss: 0x1
-  __DATA.__objc_ivar: 0x1034
+  __DATA.__objc_ivar: 0x1038
   __DATA.__data: 0x39d0
   __DATA.__bss: 0x80
   __DATA_DIRTY.__objc_data: 0x4970

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5DA1EE10-3A04-305A-8C6D-5BA9061FCEEB
-  Functions: 7868
-  Symbols:   24925
-  CStrings:  11248
+  UUID: 465541FB-0162-31B6-B7FB-89A989EA261A
+  Functions: 7881
+  Symbols:   24956
+  CStrings:  11254
 
Symbols:
+ -[MTL4GPUDebugBinaryFunction dealloc]
+ -[MTLDebugTensor _initInternalBuffers]
+ -[MTLDebugTensor initWithBaseObject:parent:]
+ -[MTLDebugTensor internalMTLBuffer]
+ -[MTLGPUDebugTensor _initInternalBuffers]
+ -[MTLGPUDebugTensor initWithBaseObject:parent:]
+ -[MTLGPUDebugTensor internalMTLBuffer]
+ -[MTLToolsTensor _initInternalBuffers]
+ -[MTLToolsTensor initWithBaseObject:buffer:initializeInternalBuffers:]
+ -[MTLToolsTensor initWithBaseObject:parent:]
+ -[MTLToolsTensor initWithBaseObject:parent:initializeInternalBuffers:]
+ -[MTLToolsTensor initWithBaseObject:parentTensor:initializeInternalBuffers:]
+ -[MTLToolsTensor internalMTLBuffer]
+ OBJC_IVAR_$_MTLToolsTensor._internalMTLBuffer
+ _objc_msgSend$_initInternalBuffers
+ _objc_msgSend$initWithBaseObject:buffer:initializeInternalBuffers:
+ _objc_msgSend$initWithBaseObject:parent:initializeInternalBuffers:
+ _objc_msgSend$initWithBaseObject:parentTensor:initializeInternalBuffers:
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CJIiugC6-of4-fSfXu_Ptjy6sDpGE361J7VsWkk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__hash_table:1892: libc++ Hardening assertion __p != end() failed: unordered container::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIiugC6-of4-fSfXu_Ptjy6sDpGE361J7VsWkk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIiugC6-of4-fSfXu_Ptjy6sDpGE361J7VsWkk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIiugC6-of4-fSfXu_Ptjy6sDpGE361J7VsWkk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIiugC6-of4-fSfXu_Ptjy6sDpGE361J7VsWkk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/array:271: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
+ "@36@0:8@16@24B32"
+ "_initInternalBuffers"
+ "_internalMTLBuffer"
+ "initWithBaseObject:buffer:initializeInternalBuffers:"
+ "initWithBaseObject:parent:initializeInternalBuffers:"
+ "initWithBaseObject:parentTensor:initializeInternalBuffers:"
- "/AppleInternal/Library/BuildRoots/4~CH9OugA5KweCiALo_XM9Uwm9f0p93kUZzJStKO0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__hash_table:1892: libc++ Hardening assertion __p != end() failed: unordered container::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/4~CH9OugA5KweCiALo_XM9Uwm9f0p93kUZzJStKO0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CH9OugA5KweCiALo_XM9Uwm9f0p93kUZzJStKO0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CH9OugA5KweCiALo_XM9Uwm9f0p93kUZzJStKO0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CH9OugA5KweCiALo_XM9Uwm9f0p93kUZzJStKO0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/array:271: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"

```
