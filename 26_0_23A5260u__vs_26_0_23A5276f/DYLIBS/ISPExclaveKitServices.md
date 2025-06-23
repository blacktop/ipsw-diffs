## ISPExclaveKitServices

> `/System/Library/PrivateFrameworks/ISPExclaveKitServices.framework/ISPExclaveKitServices`

```diff

-4.12.4.0.0
-  __TEXT.__text: 0x1c868
+4.15.7.0.0
+  __TEXT.__text: 0x1d704
   __TEXT.__auth_stubs: 0x580
-  __TEXT.__const: 0x128
-  __TEXT.__gcc_except_tab: 0x4a8
-  __TEXT.__oslogstring: 0x1da7
-  __TEXT.__cstring: 0x342d
-  __TEXT.__unwind_info: 0x540
+  __TEXT.__const: 0x118
+  __TEXT.__gcc_except_tab: 0x4c0
+  __TEXT.__oslogstring: 0x1d98
+  __TEXT.__cstring: 0x34ab
+  __TEXT.__unwind_info: 0x558
   __DATA_CONST.__got: 0x30
-  __DATA_CONST.__const: 0xaa8
+  __DATA_CONST.__const: 0xad0
   __AUTH_CONST.__auth_got: 0x2c8
   __AUTH_CONST.__const: 0x20
-  __AUTH_CONST.__cfstring: 0x200
-  __DATA.__data: 0x105ba3
+  __AUTH_CONST.__cfstring: 0x220
+  __DATA.__data: 0x105bdb
   __DATA.__common: 0x9
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/PrivateFrameworks/Tightbeam.framework/Tightbeam
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: AFA67C07-7718-3AB9-80F8-BB1F05FBDFEF
-  Functions: 611
-  Symbols:   1406
-  CStrings:  370
+  UUID: 3AC6B14C-97F5-31B8-98E1-0A1B5CF4AAF9
+  Functions: 616
+  Symbols:   1417
+  CStrings:  372
 
Symbols:
+ GCC_except_table20
+ GCC_except_table22
+ __ZN18ISPExclaveKitTimer10updateInfoEPKcj
+ __ZN18ISPExclaveKitTimer8getCmdIdEv
+ ____Z20commandTimerCallbackP18ISPExclaveKitTimer_block_invoke
+ ___block_descriptor_tmp.198
+ ___block_descriptor_tmp.205
+ ___block_descriptor_tmp.559
+ ___block_descriptor_tmp.560
+ _ispexclavekitdebugmodule_ekdebug_channelcommandtimeout
- __ZN18ISPExclaveKitTimer10updateNoteEPKc
- ___block_descriptor_tmp.31
- ___block_descriptor_tmp.38
- ___block_descriptor_tmp.516
- ___block_descriptor_tmp.517
CStrings:
+ "%s:%d - command timeout triggered, interval=%llu ms, timer command: %s, command Id: 0x%x\n"
+ "T8160"
+ "v24@?0{ispexclavekitdebugmodule_ekdebug_channelcommandtimeout__result_s=C(?={exclavesispshared_exclavesisperror_s=Q})}8"
- "%s:%d - command timeout triggered, interval=%llu ms, timer command: %s\n"
- "%s:%d - crash ek for channel %d\n"

```
