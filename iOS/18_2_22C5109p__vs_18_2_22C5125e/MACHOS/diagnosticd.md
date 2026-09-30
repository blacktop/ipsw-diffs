## diagnosticd

> `/usr/libexec/diagnosticd`

```diff

-1612.60.25.0.0
-  __TEXT.__text: 0x7c34
+1612.60.26.0.0
+  __TEXT.__text: 0x7cf0
   __TEXT.__auth_stubs: 0xf10
   __TEXT.__objc_stubs: 0x460
   __TEXT.__objc_methlist: 0x50
   __TEXT.__const: 0x458
-  __TEXT.__cstring: 0x177c
+  __TEXT.__cstring: 0x17e5
   __TEXT.__objc_methname: 0x33c
   __TEXT.__objc_classname: 0x11
   __TEXT.__objc_methtype: 0x50

   __DATA_CONST.__auth_got: 0x790
   __DATA_CONST.__got: 0x138
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x7f8
+  __DATA_CONST.__const: 0x800
   __DATA_CONST.__cfstring: 0x940
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/libz.1.dylib
   Functions: 91
   Symbols:   289
-  CStrings:  256
+  CStrings:  258
 
CStrings:
+ "TB_ASSERT: (oslogdarwin_streamprefsbatch__encode(&msg, prefs) == TB_ERROR_SUCCESS) && \"failed to encode type: OSLogDarwin.StreamPrefsBatch\""
+ "TB_FATAL: invalid value: unexpected case value, %!l(MISSING)lx"
+ "TB_FATAL: invalid value: unexpected case value, %!l(MISSING)lx (%!s(MISSING):%!d(MISSING))\n"
- "TB_ASSERT: (oslogdarwin_configerror__decode(message, &result->value.failure) == TB_ERROR_SUCCESS) && \"failed to decode type: OSLogDarwin.ConfigError\""

```
