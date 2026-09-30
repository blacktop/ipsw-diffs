## GLTools

> `/System/Library/PrivateFrameworks/GLTools.framework/GLTools`

```diff

 310.8.0.0.0
-  __TEXT.__text: 0x37ec
-  __TEXT.__auth_stubs: 0x290
+  __TEXT.__text: 0x3748
+  __TEXT.__auth_stubs: 0x280
   __TEXT.__objc_methlist: 0x190
   __TEXT.__gcc_except_tab: 0x11c
-  __TEXT.__cstring: 0x586
+  __TEXT.__cstring: 0x2f8
   __TEXT.__const: 0x60
   __TEXT.__unwind_info: 0x180
   __TEXT.__objc_classname: 0x2a

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1d0
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x158
+  __AUTH_CONST.__auth_got: 0x150
   __AUTH_CONST.__const: 0x1a8
   __AUTH_CONST.__cfstring: 0x40
   __AUTH_CONST.__objc_const: 0x400

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 919DDD12-7151-30AD-8258-D7D93688957C
+  UUID: 60DD62BA-7259-3CC1-A098-23F0272BC308
   Functions: 75
-  Symbols:   307
-  CStrings:  134
+  Symbols:   306
+  CStrings:  132
 
Symbols:
+ __ZNSt3__110unique_ptrIN8GPUTools8VMBufferENS_14default_deleteIS2_EEED1B9nqe210106Ev
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIyNS0_IN8GPUTools8Playback2GL11ContextInfoENS_14default_deleteIS6_EEEEEEPvEENS_22__hash_node_destructorINS_9allocatorISC_EEEEED1B9nqe210106Ev
+ __ZSt28__throw_bad_array_new_lengthB9nqe210106v
- __ZNSt3__110unique_ptrIN8GPUTools8VMBufferENS_14default_deleteIS2_EEED1B9foe210106Ev
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIyNS0_IN8GPUTools8Playback2GL11ContextInfoENS_14default_deleteIS6_EEEEEEPvEENS_22__hash_node_destructorINS_9allocatorISC_EEEEED1B9foe210106Ev
- __ZNSt3__132__internal_log_hardening_failureEPKc
- __ZSt28__throw_bad_array_new_lengthB9foe210106v
Functions:
~ -[DYGLFunctionPlayer deleteCurrentContext] : 568 -> 472
~ -[DYGLFunctionPlayer executePlatformFunction] : 1800 -> 1732
CStrings:
- "/AppleInternal/Library/BuildRoots/4~CJlkugAuTpBdib00ZFkVRbbQ89UkmxxXFd_jJwU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__hash_table:1892: libc++ Hardening assertion __p != end() failed: unordered container::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/4~CJlkugAuTpBdib00ZFkVRbbQ89UkmxxXFd_jJwU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1565: libc++ Hardening assertion !empty() failed: deque::back called on an empty deque\n"

```
