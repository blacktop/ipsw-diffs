## CoreHaptics

> `/System/Library/Frameworks/CoreHaptics.framework/CoreHaptics`

```diff

-272.0.0.0.0
-  __TEXT.__text: 0x55338
-  __TEXT.__auth_stubs: 0xcf0
+272.202.0.0.0
+  __TEXT.__text: 0x55304
+  __TEXT.__auth_stubs: 0xce0
   __TEXT.__objc_methlist: 0x23fc
   __TEXT.__const: 0x568
-  __TEXT.__gcc_except_tab: 0x99ac
+  __TEXT.__gcc_except_tab: 0x99b8
   __TEXT.__cstring: 0x68d4
   __TEXT.__oslogstring: 0x8ac9
   __TEXT.__unwind_info: 0x1cc0

   __TEXT.__objc_methname: 0x4f7d
   __TEXT.__objc_methtype: 0x1c31
   __TEXT.__objc_stubs: 0x4360
-  __DATA_CONST.__got: 0x248
+  __DATA_CONST.__got: 0x240
   __DATA_CONST.__const: 0xa60
   __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x60

   __DATA_CONST.__objc_selrefs: 0x1490
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x98
-  __AUTH_CONST.__auth_got: 0x690
+  __AUTH_CONST.__auth_got: 0x688
   __AUTH_CONST.__const: 0x5a8
   __AUTH_CONST.__cfstring: 0x2b60
   __AUTH_CONST.__objc_const: 0x44c0

   __DATA_DIRTY.__objc_data: 0x820
   __DATA_DIRTY.__data: 0x78
   __DATA_DIRTY.__common: 0x30
-  __DATA_DIRTY.__bss: 0xb8
+  __DATA_DIRTY.__bss: 0xb0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F2AA773E-AB75-3614-A793-7BE067F7AE44
-  Functions: 1040
-  Symbols:   4181
+  UUID: C52249AC-410E-3B40-A97A-35C707D185F9
+  Functions: 1039
+  Symbols:   4177
   CStrings:  2868
 
Symbols:
- __ZGVZN13AudioResource22getTotalAllocationLockEvE6sMutex
- __ZN13AudioResource22getTotalAllocationLockEv.cold.1
- ___cxa_atexit
Functions:
~ __ZN13AudioResource22getTotalAllocationLockEv : 56 -> 12
~ __ZN13AudioResource23incrementAllocatedBytesEy : 572 -> 568
- __ZN13AudioResource22getTotalAllocationLockEv.cold.1
~ __ZN13AudioResource23decrementAllocatedBytesEy : 344 -> 340
~ -[AVHapticPlayerChannel invalidated] : 76 -> 132
~ -[AVHapticSequence invalidated] : 112 -> 160

```
