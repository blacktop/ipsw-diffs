## logd

> `/usr/libexec/logd`

```diff

-1612.60.25.0.0
-  __TEXT.__text: 0x22e90
+1612.60.26.0.0
+  __TEXT.__text: 0x22fc0
   __TEXT.__auth_stubs: 0x1850
   __TEXT.__objc_stubs: 0x5e0
   __TEXT.__objc_methlist: 0x2c
   __TEXT.__const: 0x3c4
-  __TEXT.__cstring: 0x3696
+  __TEXT.__cstring: 0x36f3
   __TEXT.__objc_methname: 0x3e2
   __TEXT.__objc_classname: 0x14
   __TEXT.__objc_methtype: 0x10
-  __TEXT.__unwind_info: 0x628
+  __TEXT.__unwind_info: 0x620
   __DATA_CONST.__auth_got: 0xc30
   __DATA_CONST.__got: 0x160
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x1d38
+  __DATA_CONST.__const: 0x1d40
   __DATA_CONST.__cfstring: 0x480
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_nlclslist: 0x8

   - /usr/lib/libz.1.dylib
   Functions: 471
   Symbols:   439
-  CStrings:  507
+  CStrings:  509
 
CStrings:
+ "TB_ASSERT: (oslogdarwin_prefsbatch__encode(&msg, prefs) == TB_ERROR_SUCCESS) && \"failed to encode type: OSLogDarwin.PrefsBatch\""
+ "TB_FATAL: invalid value: unexpected case value, %!l(MISSING)lx"
+ "TB_FATAL: invalid value: unexpected case value, %!l(MISSING)lx (%!s(MISSING):%!d(MISSING))\n"
- "TB_ASSERT: (oslogdarwin_configerror__decode(message, &result->value.failure) == TB_ERROR_SUCCESS) && \"failed to decode type: OSLogDarwin.ConfigError\""

```
