## afcd

> `/usr/libexec/afcd`

```diff

-282.0.0.0.0
-  __TEXT.__text: 0xc98
-  __TEXT.__auth_stubs: 0x480
-  __TEXT.__const: 0x38
-  __TEXT.__cstring: 0x67b
-  __TEXT.__unwind_info: 0x70
-  __DATA_CONST.__auth_got: 0x240
-  __DATA_CONST.__got: 0x80
+283.0.0.0.1
+  __TEXT.__text: 0x1eb0
+  __TEXT.__auth_stubs: 0x4c0
+  __TEXT.__const: 0x70
+  __TEXT.__cstring: 0x158
+  __TEXT.__oslogstring: 0x56b
+  __TEXT.__unwind_info: 0xc8
+  __DATA_CONST.__auth_got: 0x260
+  __DATA_CONST.__got: 0x88
   __DATA_CONST.__const: 0x60
   __DATA.__data: 0x40
   __DATA.__bss: 0x28

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libafc.dylib
   - /usr/lib/liblockdown.dylib
-  UUID: C9C8F769-9F9E-3059-9B58-B0DEF8256846
-  Functions: 6
-  Symbols:   90
-  CStrings:  60
+  UUID: 8A5630E4-5E17-3D12-B93A-C14B7DC1CA10
+  Functions: 44
+  Symbols:   95
+  CStrings:  62
 
Symbols:
+ ___AFCInitializeActivationMonitor
+ ___gAFCOSLog
+ __os_log_debug_impl
+ __os_log_error_impl
+ __os_log_impl
+ _os_log_type_enabled
- _AFCLog
CStrings:
+ "Initializing activation monitor"
+ "failed to initialize activation monitor"

```
