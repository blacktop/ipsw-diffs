## TimeSync

> `/System/Library/PrivateFrameworks/TimeSync.framework/Versions/A/TimeSync`

```diff

-1501.7.0.0.0
-  __TEXT.__text: 0x5cc14
-  __TEXT.__objc_methlist: 0x6e9c
-  __TEXT.__const: 0x2a8
-  __TEXT.__oslogstring: 0x490e
-  __TEXT.__cstring: 0x8645
-  __TEXT.__gcc_except_tab: 0xf34
+1510.9.0.0.0
+  __TEXT.__text: 0x5cf54
+  __TEXT.__objc_methlist: 0x6e4c
+  __TEXT.__const: 0x2b8
+  __TEXT.__oslogstring: 0x49d9
+  __TEXT.__cstring: 0x8611
+  __TEXT.__gcc_except_tab: 0xfac
   __TEXT.__unwind_info: 0x1b30
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x28f8
+  __DATA_CONST.__objc_selrefs: 0x28e0
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x3a8
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__got: 0x418
-  __AUTH_CONST.__const: 0x1030
+  __AUTH_CONST.__const: 0x1090
   __AUTH_CONST.__cfstring: 0x56e0
   __AUTH_CONST.__objc_const: 0xdea8
   __AUTH_CONST.__objc_arrayobj: 0x30

   __AUTH_CONST.__auth_ptr: 0x0
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x964
-  __DATA.__data: 0x788
+  __DATA.__data: 0x1
   __DATA.__bss: 0x98
   __DATA_DIRTY.__objc_data: 0x2300
+  __DATA_DIRTY.__data: 0x780
   __DATA_DIRTY.__bss: 0x130
   __DATA_DIRTY.__common: 0x4
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2968
-  Symbols:   5645
-  CStrings:  1256
+  Functions: 2964
+  Symbols:   5638
+  CStrings:  1259
 
Symbols:
+ GCC_except_table40
+ GCC_except_table74
+ GCC_except_table80
+ ___block_descriptor_48_e8_32s40r_e16_v16?0"NSUUID"8l
+ ___block_descriptor_48_e8_32s40r_e20_v20?0B8"NSError"12l
+ ___block_descriptor_48_e8_32s40r_e20_v20?0S8"NSError"12l
+ ___block_descriptor_48_e8_32s40r_e20_v20?0i8"NSError"12l
+ ___block_descriptor_48_e8_32s40r_e28_v24?0"NSUUID"8"NSError"16l
+ ___block_descriptor_56_e8_32r40r_e20_v20?0i8"NSError"12l
- -[TSgPTPManager dockReplayTimestamps:]
- -[TSgPTPManager startReplayTimestamps:]
- -[TSgPTPManager stopReplayTimestamps:]
- -[_TSF_TSDgPTPManager dockReplayTimestamps:]
- -[_TSF_TSDgPTPManager startReplayTimestamps:]
- -[_TSF_TSDgPTPManager stopReplayTimestamps:]
- GCC_except_table78
- __36-[TSSyncEntity daemonClientRefresh:]_block_invoke_2
- ___36-[TSSyncEntity daemonClientRefresh:]_block_invoke_2
- ___block_descriptor_40_e8_32r_e20_v20?0i8"NSError"12l
- ___block_descriptor_40_e8_32s_e20_v20?0S8"NSError"12l
- ___block_descriptor_40_e8_32s_e20_v20?0i8"NSError"12l
- ___block_descriptor_40_e8_32s_e28_v24?0"NSUUID"8"NSError"16l
- _objc_msgSend$dockReplayTimestamps:
- _objc_msgSend$startReplayTimestamps:
- _objc_msgSend$stopReplayTimestamps:
CStrings:
+ "%@: %s error during call. UUID is nil."
+ "%@: %s failed to create sync entity (registered: %d, queriedSyncState: %d)."
+ "%@: %s failed to query sync entity type."
+ "%@: Failed to create sync entity for UUID: %@\n"
- "-[TSSyncEntity daemonClientRefresh:]_block_invoke_2"
```
