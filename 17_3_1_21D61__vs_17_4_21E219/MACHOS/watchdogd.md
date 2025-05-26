## watchdogd

> `/usr/libexec/watchdogd`

```diff

-250.0.0.0.0
-  __TEXT.__text: 0x8098
-  __TEXT.__auth_stubs: 0xc80
+254.100.5.0.0
+  __TEXT.__text: 0x81f8
+  __TEXT.__auth_stubs: 0xc70
   __TEXT.__objc_stubs: 0x620
-  __TEXT.__cstring: 0x34f8
+  __TEXT.__cstring: 0x3661
   __TEXT.__const: 0x48
   __TEXT.__objc_classname: 0x1
   __TEXT.__oslogstring: 0x76
   __TEXT.__gcc_except_tab: 0x44
   __TEXT.__objc_methname: 0x406
-  __TEXT.__unwind_info: 0x1c0
-  __DATA_CONST.__auth_got: 0x650
+  __TEXT.__unwind_info: 0x1c8
+  __DATA_CONST.__auth_got: 0x648
   __DATA_CONST.__got: 0x80
   __DATA_CONST.__auth_ptr: 0x30
-  __DATA_CONST.__const: 0x490
+  __DATA_CONST.__const: 0x4f0
   __DATA_CONST.__cfstring: 0x700
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_classrefs: 0xa8
   __DATA_CONST.__objc_intobj: 0x318
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA.__objc_selrefs: 0x188
-  __DATA.__objc_classrefs: 0xa8
   __DATA.__data: 0x8508
   __DATA.__bss: 0x660
   __DATA.__common: 0x68

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 188
-  Symbols:   246
-  CStrings:  449
+  Functions: 191
+  Symbols:   245
+  CStrings:  453
 
Symbols:
- _strdup
CStrings:
+ "%s boot-arg specified for daemon %s which cannot be found in services list"
+ "%s boot-arg specified with empty daemon name"
+ "detected boot-arg (%s) to capture ddt on timeout with value: %s"
+ "monitoring for %s configured to capture ddt on timeout (per %s boot-arg)"
+ "v16@?0^{watchdog_service=BB****iBBBBBi(?={ephemeral_service_data=*B^{watchdog_service}{?=^{watchdog_service}}}{controller_service_data={?=^{watchdog_service}}})I{watchdog_service_state=QQQQQQQBBii{watchdog_service_state_round=IiBB[1024c]Q[5[32c]]QB[400c]}}}8"
+ "wdt_capture_ddt_on_timeout"
- "%s boot-arg specifies panic on first timeout configuration for daemon not found in services list: %s"
- "%s boot-arg specifies panic on first timeout configuration for empty daemon name"

```
