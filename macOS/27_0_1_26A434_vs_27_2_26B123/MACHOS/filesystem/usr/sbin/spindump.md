## spindump

> `/usr/sbin/spindump`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-448.0.0.0.0
-  __TEXT.__text: 0x10e08c
-  __TEXT.__auth_stubs: 0x1580
+453.1.0.0.0
+  __TEXT.__text: 0x10e9ac
+  __TEXT.__auth_stubs: 0x15b0
   __TEXT.__objc_stubs: 0x4bc0
   __TEXT.__objc_methlist: 0xce0
   __TEXT.__const: 0x2e0
-  __TEXT.__oslogstring: 0x356f6
-  __TEXT.__cstring: 0x1bbf3
+  __TEXT.__oslogstring: 0x35abf
+  __TEXT.__cstring: 0x1bd12
   __TEXT.__objc_classname: 0x143
   __TEXT.__objc_methtype: 0x596
   __TEXT.__gcc_except_tab: 0x47cc
   __TEXT.__objc_methname: 0x4a11
-  __TEXT.__unwind_info: 0x2620
-  __DATA_CONST.__const: 0x2190
-  __DATA_CONST.__cfstring: 0xdb80
+  __TEXT.__unwind_info: 0x2648
+  __DATA_CONST.__const: 0x21b0
+  __DATA_CONST.__cfstring: 0xdc20
   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__objc_intobj: 0xf0
   __DATA_CONST.__objc_arraydata: 0x48
   __DATA_CONST.__objc_arrayobj: 0x48
-  __DATA_CONST.__auth_got: 0xad0
+  __DATA_CONST.__auth_got: 0xae8
   __DATA_CONST.__got: 0x348
   __DATA_CONST.__auth_ptr: 0x50
   __DATA.__objc_const: 0x2580

   - /usr/lib/libsystemstats.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 2769
-  Symbols:   458
-  CStrings:  5195
+  Functions: 2779
+  Symbols:   462
+  CStrings:  5208
 
Symbols:
+ _ktrace_config_create_current
+ _ktrace_config_destroy
+ _ktrace_config_get_owner_kind
+ _ktrace_config_kdebug_get_state
+ _tailspin_dump_output_with_options
- _tailspin_currently_running
CStrings:
+ "BundleIdOverride=%{public, signpost.description:attribute}@ %{public, signpost.description:begin_time}llu cid=%{public,name=cid}llu pid=%{public,name=pid}u conditionsPreventingSubmission=%{public,name=conditionsPreventingSubmission}#llx otherConditions=%{public,name=otherConditions}#llx hidEventCountSinceLastSignpost=%{signpost.telemetry:number1,public}llu userActionCountSinceLastSignpost=%{signpost.telemetry:number2,public}llu enableTelemetry=YES "
+ "Unable to format: tailspin check: ktrace is not available"
+ "Unable to format: tailspin check: tailspin is running"
+ "Unable to format: tailspin check: trace is not background mode"
+ "Unable to format: tailspin check: trace is not enabled"
+ "Unable to format: tailspin check: unable to check kdebug config: %d (%s)"
+ "hid_event_count_since_last_signpost"
+ "tailspin check: ktrace is not available"
+ "tailspin check: tailspin is running"
+ "tailspin check: trace is not background mode"
+ "tailspin check: trace is not enabled"
+ "tailspin check: unable to check kdebug config: %d (%s)"
+ "user_action_count_since_last_signpost"
```
