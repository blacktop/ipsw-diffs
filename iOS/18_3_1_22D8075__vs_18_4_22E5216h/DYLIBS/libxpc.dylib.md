## libxpc.dylib

> `/usr/lib/system/libxpc.dylib`

```diff

-2866.80.6.0.0
-  __TEXT.__text: 0x3a894
-  __TEXT.__auth_stubs: 0x10e0
-  __TEXT.__objc_methlist: 0x224
-  __TEXT.__const: 0x630
-  __TEXT.__cstring: 0x7103
-  __TEXT.__oslogstring: 0x1709
+2894.100.80.0.0
+  __TEXT.__text: 0x3a5e4
+  __TEXT.__auth_stubs: 0x10f0
+  __TEXT.__objc_methlist: 0x32c
+  __TEXT.__const: 0x620
+  __TEXT.__cstring: 0x732c
+  __TEXT.__oslogstring: 0x1759
   __TEXT.__dof_libxpc: 0xa5d
-  __TEXT.__unwind_info: 0x10d8
+  __TEXT.__unwind_info: 0x10a0
   __TEXT.__objc_classname: 0x217
   __TEXT.__objc_methname: 0x1e2
   __TEXT.__objc_methtype: 0xb5
   __TEXT.__objc_stubs: 0x100
-  __DATA_CONST.__got: 0xf8
-  __DATA_CONST.__const: 0x1af0
+  __DATA_CONST.__got: 0xf0
+  __DATA_CONST.__const: 0x1b00
   __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_nlclslist: 0xe0
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x88
+  __DATA_CONST.__objc_selrefs: 0x100
   __DATA_CONST.__objc_superrefs: 0x50
-  __AUTH_CONST.__auth_got: 0x878
-  __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x19f8
-  __AUTH_CONST.__objc_const: 0x2390
+  __AUTH_CONST.__auth_got: 0x880
+  __AUTH_CONST.__auth_ptr: 0x10
+  __AUTH_CONST.__const: 0x1a08
+  __AUTH_CONST.__objc_const: 0x21a0
   __DATA.__data: 0xb40
   __DATA.__crash_info: 0x40
   __DATA.__common: 0x8
-  __DATA.__bss: 0x70
+  __DATA.__bss: 0x78
   __DATA_DIRTY.__objc_data: 0xaa0
   __DATA_DIRTY.__common: 0x8
   __DATA_DIRTY.__bss: 0x120

   - /usr/lib/system/libsystem_sandbox.dylib
   - /usr/lib/system/libsystem_trace.dylib
   - /usr/lib/system/libunwind.dylib
-  Functions: 1693
-  Symbols:   2261
-  CStrings:  1192
+  Functions: 1713
+  Symbols:   2409
+  CStrings:  1216
 
Symbols:
+ ___assert_rtn
+ _launch_urgent_log_submission_completed
+ _xpc_add_bundle_with_lwcr
+ _xpc_connection_bs_seal_listener
+ _xpc_service_instance_set_use_sec_transition_shims
CStrings:
+ "!(consume_suspend_cnt && ready_only)"
+ "!(ready_only && (self->_type == XC_TYPE_PEER))"
+ "!ready_only"
+ "Couldn't retrieve XPCService dictionary from service bundle. Cause: %s"
+ "Entitlements element not allowed"
+ "Sealing is only possible for listeners."
+ "UTC Time element not allowed"
+ "Unknown DER entitlements encoding"
+ "Unknown UTC Time encoding"
+ "Unknown numeric string encoding"
+ "[%p] %{public}s connection: mach=%{bool}d listener=%{bool}d peer=%{bool}d name=%{public}s"
+ "[%p] %{public}s connection: name=%{public}s publishToken=%{public}llu"
+ "[%p] Sealing failed to init recv right."
+ "[%p] Sealing failed to make send right."
+ "_xpc_connection_activate_if_needed"
+ "_xpc_connection_init"
+ "activated"
+ "activating"
+ "connection.c"
+ "der_decode_entitlements"
+ "der_decode_numeric_string"
+ "der_decode_utc_time"
+ "init-ready"
+ "lwcr"
+ "numeric string element not allowed"
+ "pid-version"
+ "readying"
+ "readying error"
+ "xpc_connection_bs_seal_listener"
- "1"
- "Configuration error: Couldn't retrieve XPCService dictionary from service bundle."
- "[%p] activating connection: mach=%{bool}d listener=%{bool}d peer=%{bool}d name=%{public}s"
- "[%p] activating connection: name=%{public}s publishToken=%{public}llu"
- "])"

```
