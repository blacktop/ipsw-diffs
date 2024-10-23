## watchdogd

> `/usr/libexec/watchdogd`

```diff

-274.40.4.0.0
-  __TEXT.__text: 0xa5a4
-  __TEXT.__auth_stubs: 0xf30
-  __TEXT.__objc_stubs: 0xa40
+277.60.12.0.0
+  __TEXT.__text: 0xa8cc
+  __TEXT.__auth_stubs: 0xf70
+  __TEXT.__objc_stubs: 0xa80
   __TEXT.__const: 0x88
-  __TEXT.__cstring: 0x4187
+  __TEXT.__cstring: 0x4255
   __TEXT.__oslogstring: 0x280
   __TEXT.__objc_classname: 0x1
   __TEXT.__gcc_except_tab: 0x5c
-  __TEXT.__objc_methname: 0x69f
-  __TEXT.__unwind_info: 0x258
-  __DATA_CONST.__auth_got: 0x7a8
+  __TEXT.__objc_methname: 0x6bf
+  __TEXT.__unwind_info: 0x250
+  __DATA_CONST.__auth_got: 0x7c8
   __DATA_CONST.__got: 0x1c8
   __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__const: 0x760

   __DATA_CONST.__objc_intobj: 0x318
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_selrefs: 0x290
-  __DATA.__data: 0x8d50
+  __DATA.__objc_selrefs: 0x2a0
+  __DATA.__data: 0x95b0
   __DATA.__bss: 0xae0
   __DATA.__common: 0x90
   __INFO_FILTER.__disable: 0x0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 170
-  Symbols:   305
-  CStrings:  573
+  Functions: 171
+  Symbols:   309
+  CStrings:  583
 
Symbols:
+ _TSPDumpOptions_Symbolicate
+ ___kCFBooleanFalse
+ _uuid_clear
+ _uuid_copy
+ _uuid_generate
+ _uuid_unparse
- _TSPDumpOptions_NoSymbolicate
- ___kCFBooleanTrue
CStrings:
+ "-m"
+ "/usr/local/libexec/watchdogtestexclave"
+ "com.apple.watchdogtestexclave"
+ "com.apple.watchdogtestexclave.watchdog"
+ "service %!s(MISSING) incident_id is null"
+ "setIncidentID:"
+ "setValue:forKey:"
+ "v16@?0^{watchdog_service={?=^{watchdog_service}}QBB****iBBBBBi(?={ephemeral_service_data=*B^{watchdog_service}{?=^{watchdog_service}}}{controller_service_data={?=^{watchdog_service}}})I{watchdog_service_state=QQQQQQQ[16C]AiBii{watchdog_service_state_round=IiBB[1024c]Q[5[32c]]QBB[400c]}}}8"
+ "watchdogd detected testing boot-args for daemon (controller: %!d(MISSING)) (ephemeral: %!d(MISSING)) (optin: %!d(MISSING)) (exclave :%!d(MISSING))"
+ "watchdogtestexclave"
+ "wdt_exclave"
+ "wdt_exclave="
- "v16@?0^{watchdog_service={?=^{watchdog_service}}QBB****iBBBBBi(?={ephemeral_service_data=*B^{watchdog_service}{?=^{watchdog_service}}}{controller_service_data={?=^{watchdog_service}}})I{watchdog_service_state=QQQQQQQAiBii{watchdog_service_state_round=IiBB[1024c]Q[5[32c]]QBB[400c]}}}8"
- "watchdogd detected testing boot-args for daemon (controller: %!d(MISSING)) (ephemeral: %!d(MISSING)) (optin: %!d(MISSING))"

```
