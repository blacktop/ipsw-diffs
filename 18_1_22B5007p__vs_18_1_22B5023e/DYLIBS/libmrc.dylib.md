## libmrc.dylib

> `/usr/lib/libmrc.dylib`

```diff

-2559.0.31.0.0
-  __TEXT.__text: 0x61cc
-  __TEXT.__auth_stubs: 0x580
+2559.40.2.0.0
+  __TEXT.__text: 0x62f4
+  __TEXT.__auth_stubs: 0x570
   __TEXT.__objc_methlist: 0x44
-  __TEXT.__const: 0x40
-  __TEXT.__cstring: 0x695
-  __TEXT.__oslogstring: 0x1b9
+  __TEXT.__const: 0x50
+  __TEXT.__cstring: 0x6a6
+  __TEXT.__oslogstring: 0x2d5
   __TEXT.__unwind_info: 0x278
   __TEXT.__objc_classname: 0x150
   __TEXT.__objc_methname: 0x15b
   __TEXT.__objc_methtype: 0xb5
   __DATA_CONST.__got: 0x78
-  __DATA_CONST.__const: 0x448
+  __DATA_CONST.__const: 0x420
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x2c0
-  __AUTH_CONST.__const: 0x4f0
+  __AUTH_CONST.__auth_got: 0x2b8
+  __AUTH_CONST.__const: 0x518
   __AUTH_CONST.__objc_const: 0x1040
-  __AUTH.__objc_data: 0x410
   __DATA.__objc_classrefs: 0x8
   __DATA.__objc_superrefs: 0x8
   __DATA.__data: 0x540
-  __DATA.__bss: 0x70
+  __DATA.__bss: 0x38
+  __DATA_DIRTY.__objc_data: 0x410
+  __DATA_DIRTY.__bss: 0x38
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 180
-  Symbols:   292
-  CStrings:  177
+  Symbols:   291
+  CStrings:  182
 
Symbols:
+ _mrc_dns_service_registration_set_reports_connection_errors
+ _xpc_dictionary_get_dictionary
+ _xpc_dictionary_get_uint64
- _mrc_cached_local_records_inquiry_set_handler
- _xpc_array_append_value
- _xpc_array_get_dictionary
- _xpc_string_create_with_format
CStrings:
+ "Current DNS service registration didn't require error reporting, ignoring -- registration: %!@(MISSING), notification: %!{(MISSING)private}s"
+ "OS_mrc_session"
+ "Unrecognized notification ID: %!l(MISSING)lu"
+ "[S%!l(MISSING)lu] %!{(MISSING)public}s start reply -- error: %!{(MISSING)mdns:err}ld"
+ "[S%!l(MISSING)lu] %!{(MISSING)public}s stop reply -- error: %!{(MISSING)mdns:err}ld"
+ "[S%!l(MISSING)lu] Abnormal %!{(MISSING)public}s start reply: %!{(MISSING)public}s"
+ "[S%!l(MISSING)lu] Abnormal %!{(MISSING)public}s stop reply: %!{(MISSING)public}s"
+ "[S%!l(MISSING)lu] Notification for %!{(MISSING)public}s is missing body: %!{(MISSING)private}s"
+ "[S%!l(MISSING)lu] Notification for %!{(MISSING)public}s was unhandled: %!{(MISSING)private}s"
+ "body"
+ "connection_error"
+ "mrc_session"
+ "reports_connection_errors"
- "%!s(MISSING) %!s(MISSING)"
- "OS_mrc_enabler"
- "[E%!l(MISSING)lu] %!{(MISSING)public}s start reply -- error: %!{(MISSING)mdns:err}ld"
- "[E%!l(MISSING)lu] %!{(MISSING)public}s stop reply -- error: %!{(MISSING)mdns:err}ld"
- "[E%!l(MISSING)lu] Abnormal %!{(MISSING)public}s start reply: %!{(MISSING)public}s"
- "[E%!l(MISSING)lu] Abnormal %!{(MISSING)public}s stop reply: %!{(MISSING)public}s"
- "_device-info._tcp.local."
- "mrc_enabler"

```
