## libsysdiagnose.dylib

> `/usr/lib/libsysdiagnose.dylib`

```diff

-1270.80.1.0.0
-  __TEXT.__text: 0x2d00
-  __TEXT.__auth_stubs: 0x4c0
+1295.100.44.0.0
+  __TEXT.__text: 0x2edc
+  __TEXT.__auth_stubs: 0x4e0
   __TEXT.__objc_methlist: 0xe0
-  __TEXT.__const: 0x18
+  __TEXT.__const: 0x20
   __TEXT.__gcc_except_tab: 0x60
   __TEXT.__cstring: 0x519
-  __TEXT.__oslogstring: 0x18c
-  __TEXT.__unwind_info: 0xdc
+  __TEXT.__oslogstring: 0x1d4
+  __TEXT.__unwind_info: 0xe4
   __TEXT.__objc_classname: 0xf
   __TEXT.__objc_methname: 0x715
   __TEXT.__objc_methtype: 0xd9

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x48
   __DATA_CONST.__objc_selrefs: 0x220
+  __DATA_CONST.__objc_classrefs: 0x80
   __AUTH_CONST.__cfstring: 0x460
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_const: 0x0
-  __AUTH_CONST.__auth_got: 0x270
-  __DATA.__objc_classrefs: 0x80
+  __AUTH_CONST.__auth_got: 0x280
+  __DATA.__data: 0x8
   __DATA_DIRTY.__const: 0x60
   __DATA_DIRTY.__objc_const: 0x48
   __DATA_DIRTY.__objc_data: 0x50

   - /System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A1E954E1-702C-3A6B-899A-066E31BB21EF
-  Functions: 33
-  Symbols:   270
-  CStrings:  186
+  UUID: 8741E450-DB46-3BED-BEF6-C11725913283
+  Functions: 34
+  Symbols:   274
+  CStrings:  188
 
Symbols:
+ ___83+[Libsysdiagnose sendSysdiagnoseRequest:withMetrics:withError:withProgressHandler:]_block_invoke.cold.1
+ ___block_descriptor_72_e8_32bs40r48r56r64r_e33_v16?0"NSObject<OS_xpc_object>"8lr40l8r48l8s32l8r56l8r64l8
+ __os_log_error_impl
+ _dispatch_time
- ___block_descriptor_56_e8_32bs40r48r_e33_v16?0"NSObject<OS_xpc_object>"8lr40l8s32l8r48l8
CStrings:
+ "More than 100 progress reported"
+ "Timed out waiting for progress updates."

```
