## corespeechd

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd`

```diff

-3401.17.1.0.0
-  __TEXT.__text: 0x1720e8
-  __TEXT.__auth_stubs: 0x1750
-  __TEXT.__objc_stubs: 0x1e3a0
-  __TEXT.__objc_methlist: 0x16ef8
+3401.22.1.0.0
+  __TEXT.__text: 0x17212c
+  __TEXT.__auth_stubs: 0x1770
+  __TEXT.__objc_stubs: 0x1e3c0
+  __TEXT.__objc_methlist: 0x16f20
   __TEXT.__const: 0x338
   __TEXT.__gcc_except_tab: 0x38f8
   __TEXT.__cstring: 0x2a57f
-  __TEXT.__objc_methname: 0x3e27b
-  __TEXT.__oslogstring: 0x21841
+  __TEXT.__objc_methname: 0x3e347
+  __TEXT.__oslogstring: 0x217f9
   __TEXT.__objc_classname: 0x35c7
-  __TEXT.__objc_methtype: 0x86db
+  __TEXT.__objc_methtype: 0x8741
   __TEXT.__dlopen_cstrs: 0x2c5
-  __TEXT.__unwind_info: 0x5630
-  __DATA_CONST.__auth_got: 0xbc0
+  __TEXT.__unwind_info: 0x5628
+  __DATA_CONST.__auth_got: 0xbd0
   __DATA_CONST.__got: 0x1398
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x5cd8

   __DATA_CONST.__objc_arrayobj: 0x150
   __DATA_CONST.__objc_dictobj: 0x320
   __DATA_CONST.__objc_floatobj: 0x4b0
-  __DATA.__objc_const: 0x2c500
-  __DATA.__objc_selrefs: 0xb610
-  __DATA.__objc_ivar: 0x1f20
+  __DATA.__objc_const: 0x2c530
+  __DATA.__objc_selrefs: 0xb628
+  __DATA.__objc_ivar: 0x1f24
   __DATA.__objc_data: 0x5fa0
   __DATA.__data: 0x3ba0
   __DATA.__bss: 0x808

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 9636
-  Symbols:   1017
-  CStrings:  15691
+  Functions: 9639
+  Symbols:   1019
+  CStrings:  15698
 
Symbols:
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
CStrings:
+ "forceCancelSecondPassTrigger"
+ "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
+ "_secondpassTriggerCancellationLock"
+ "%!s(MISSING) Requested cancelling 2nd pass trigger"
+ "setSecondpassTriggerCancellationLock:"
+ "{os_unfair_lock_s=I}16@0:8"
+ "_cancelSecondPassTrigger"
+ "TB,N,V_cancelSecondPassTrigger"
+ "cancelSecondPassTrigger"
+ "secondpassTriggerCancellationLock"
+ "setCancelSecondPassTrigger:"
+ "v20@0:8{os_unfair_lock_s=I}16"
+ "T{os_unfair_lock_s=I},N,V_secondpassTriggerCancellationLock"
- "setIsSecondPassCancelled:"
- "TB,N,V_isSecondPassCancelled"
- "%!s(MISSING) Requested cancelling 2nd pass"
- "_isSecondPassCancelled"
- "isSecondPassCancelled"
- "%!s(MISSING) Second Pass request is marked for cancellation before second pass completion"

```
