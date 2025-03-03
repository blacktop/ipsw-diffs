## diagnosticd

> `/usr/libexec/diagnosticd`

```diff

-1612.80.7.0.0
-  __TEXT.__text: 0x7cf0
-  __TEXT.__auth_stubs: 0xf10
+1643.100.44.0.0
+  __TEXT.__text: 0x7c94
+  __TEXT.__auth_stubs: 0xf40
   __TEXT.__objc_stubs: 0x460
   __TEXT.__objc_methlist: 0x50
   __TEXT.__const: 0x458
-  __TEXT.__cstring: 0x17e5
+  __TEXT.__cstring: 0x17e9
   __TEXT.__objc_methname: 0x33c
   __TEXT.__objc_classname: 0x11
   __TEXT.__objc_methtype: 0x50
   __TEXT.__unwind_info: 0x1a8
-  __DATA_CONST.__auth_got: 0x790
-  __DATA_CONST.__got: 0x138
-  __DATA_CONST.__auth_ptr: 0x8
+  __DATA_CONST.__auth_got: 0x7a8
+  __DATA_CONST.__got: 0x128
+  __DATA_CONST.__auth_ptr: 0x18
   __DATA_CONST.__const: 0x800
   __DATA_CONST.__cfstring: 0x940
   __DATA_CONST.__objc_classlist: 0x8

   __DATA.__objc_selrefs: 0x138
   __DATA.__objc_ivar: 0x8
   __DATA.__objc_data: 0x50
+  __DATA.__os_assumes_log: 0x8
   __DATA.__data: 0x1a4
   __DATA.__crash_info: 0x40
-  __DATA.__os_assumes_log: 0x8
   __DATA.__bss: 0x1d0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
   Functions: 91
-  Symbols:   289
+  Symbols:   292
   CStrings:  258
 
Symbols:
+ _tb_message_precheck_decoding
+ _tb_message_precheck_encoding
+ _tb_message_raw_decode_u32
+ _tb_message_raw_decode_u64
+ _tb_message_raw_encode_bool
+ _tb_message_raw_encode_u32
+ _tb_message_raw_encode_u64
+ _tb_message_raw_encode_u8
- _tb_message_decode_u32
- _tb_message_encode_bool
- _tb_message_encode_u32
- _tb_message_encode_u64
- _tb_message_encode_u8
CStrings:
+ "TB_ASSERT: (oslogdarwin_streamprefsbatch__raw_encode(&msg, prefs) == TB_ERROR_SUCCESS) && \"failed to encode type: OSLogDarwin.StreamPrefsBatch\""
- "TB_ASSERT: (oslogdarwin_streamprefsbatch__encode(&msg, prefs) == TB_ERROR_SUCCESS) && \"failed to encode type: OSLogDarwin.StreamPrefsBatch\""

```
