## libsystem_trace.dylib

> `/usr/lib/system/libsystem_trace.dylib`

```diff

-1861.120.4.0.0
-  __TEXT.__text: 0x1abb4
-  __TEXT.__auth_stubs: 0x1140
+1952.0.0.0.0
+  __TEXT.__text: 0x1b718
   __TEXT.__delay_stubs: 0x180
   __TEXT.__delay_helper: 0xa4
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0xf4
-  __TEXT.__const: 0x2b5
-  __TEXT.__cstring: 0x1bf5
+  __TEXT.__const: 0x2b0
+  __TEXT.__cstring: 0x1c4a
   __TEXT.__gcc_except_tab: 0x64
   __TEXT.__oslogstring: 0x137
-  __TEXT.__unwind_info: 0x4f8
-  __TEXT.__objc_classname: 0x70
-  __TEXT.__objc_methname: 0x38d
-  __TEXT.__objc_methtype: 0xc5
-  __TEXT.__objc_stubs: 0x500
-  __DATA_CONST.__got: 0xe8
-  __DATA_CONST.__const: 0x528
+  __TEXT.__unwind_info: 0x528
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x588
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_nlclslist: 0x10
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x168
   __DATA_CONST.__objc_superrefs: 0x30
-  __AUTH_CONST.__auth_got: 0x8e0
-  __AUTH_CONST.__const: 0x358
+  __DATA_CONST.__got: 0xe8
+  __AUTH_CONST.__const: 0x3d0
   __AUTH_CONST.__objc_const: 0x5c8
+  __AUTH_CONST.__auth_got: 0x900
   __AUTH.__objc_data: 0x140
   __AUTH.__data: 0x168
   __DATA.__objc_ivar: 0x34
   __DATA.__data: 0xe4
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x1d8
+  __DATA.__bss: 0x200
   __DATA_DIRTY.__objc_data: 0xf0
   __DATA_DIRTY.__data: 0x368
-  __DATA_DIRTY.__bss: 0x2c8
+  __DATA_DIRTY.__bss: 0x2f0
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/system/libcompiler_rt.dylib
   - /usr/lib/system/libcorecrypto.dylib

   - /usr/lib/system/libsystem_notify.dylib
   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
+  - /usr/lib/system/libsystem_sandbox.dylib
   - /usr/lib/system/libsystem_symptoms.dylib
   - /usr/lib/system/libunwind.dylib
   - /usr/lib/system/libxpc.dylib
-  UUID: 838E2D5F-14C5-32E1-804E-D2784FA231C6
-  Functions: 368
-  Symbols:   1085
-  CStrings:  487
+  UUID: A80ACB5E-BF29-3BB7-8A5A-08E986A291F4
+  Functions: 380
+  Symbols:   1120
+  CStrings:  419
 
Symbols:
+ ____os_trace_personas_in_oslog_enabled_block_invoke
+ ____os_trace_should_embed_persona_block_invoke
+ ___block_descriptor_tmp.176
+ ___block_descriptor_tmp.271
+ ___block_descriptor_tmp.3.126
+ ___block_descriptor_tmp.3.506
+ ___block_descriptor_tmp.307
+ ___block_descriptor_tmp.317
+ ___block_descriptor_tmp.36
+ ___block_descriptor_tmp.44
+ ___block_descriptor_tmp.492
+ ___block_descriptor_tmp.527
+ ___block_descriptor_tmp.74.370
+ ___block_literal_global.127
+ ___block_literal_global.174
+ ___block_literal_global.268
+ ___block_literal_global.305
+ ___block_literal_global.38
+ ___block_literal_global.382
+ ___block_literal_global.454
+ ___block_literal_global.46
+ ___block_literal_global.5
+ ___block_literal_global.505
+ ___block_literal_global.522
+ ___os_trace_safe_ascii_strcspn_block_invoke.272
+ __os_activity_stream_entry_encode_persona
+ __os_feature_enabled_impl
+ __os_log_dynamic_impl_4XOJIT
+ __os_log_fmt_builtin_multichar
+ __os_trace_personas_in_oslog_enabled
+ __os_trace_personas_in_oslog_enabled.enabled
+ __os_trace_personas_in_oslog_enabled.once
+ __os_trace_set_intprefsdir_path
+ __os_trace_set_prefsdir_path
+ __os_trace_set_sysprefsdir_path
+ __os_trace_should_embed_persona
+ __os_trace_should_embed_persona.once
+ __os_trace_should_embed_persona.should_embed
+ __os_trace_unsafe_ascii_once
+ __os_trace_unsafe_ascii_tbl
+ _kpersona_pidinfo
+ _objc_retain_x1
+ _os_log_fmt_flatten
+ _sandbox_check
+ _voucher_get_current_persona
- ___block_descriptor_tmp.167
- ___block_descriptor_tmp.293
- ___block_descriptor_tmp.3.490
- ___block_descriptor_tmp.303
- ___block_descriptor_tmp.35.305
- ___block_descriptor_tmp.477
- ___block_descriptor_tmp.511
- ___block_descriptor_tmp.74.357
- ___block_literal_global.101
- ___block_literal_global.165
- ___block_literal_global.291
- ___block_literal_global.369
- ___block_literal_global.37
- ___block_literal_global.439
- ___block_literal_global.489
- ___block_literal_global.506
- _objc_retain_x19
CStrings:
+ "INBOX"
+ "Libtrace"
+ "launch_persona_id"
+ "multichar"
+ "persona_id"
+ "personas_in_oslog"
+ "syscall-unix"
- "C"
- "OSLogCoder"
- "OS__os_metric"
- "OS_os_activity"
- "OS_os_log"
- "OS_os_metric_dimensions"
- "OS_os_metric_group"
- "OS_os_metric_label"
- "Q"
- "S"
- "[128c]"
- "^{?=b4b4C[0C]}"
- "^{os_trace_blob_s=(?=*^v**)IIISB}"
- "_fastCStringContents:"
- "_fmt_cmd"
- "_initBlob"
- "_initialized"
- "_mask"
- "_maskbuf"
- "_maxsz"
- "_ob"
- "_ob_mask"
- "_ob_priv"
- "_ob_pub"
- "_offset"
- "_privacy_level"
- "_truncated"
- "_written"
- "appendBytes:length:"
- "charValue"
- "dealloc"
- "doubleValue"
- "encodeWithOSLogCoder:options:maxLength:"
- "floatValue"
- "getBytes:maxLength:usedLength:encoding:options:range:remainingRange:"
- "initWithBytes:length:"
- "initWithBytes:length:encoding:"
- "initWithChar:"
- "initWithDouble:"
- "initWithFormat:arguments:"
- "initWithInt:"
- "initWithLong:"
- "initWithLongLong:"
- "initWithShort:"
- "initWithUnsignedChar:"
- "initWithUnsignedInt:"
- "initWithUnsignedLongLong:"
- "initWithUnsignedShort:"
- "intValue"
- "isKindOfClass:"
- "isNSCFConstantString__"
- "isNSDate__"
- "isNSNumber__"
- "isNSString__"
- "isProxy"
- "length"
- "lengthOfBytesUsingEncoding:"
- "longLongValue"
- "longValue"
- "objCType"
- "retainCount"
- "setPublic"
- "setTruncated"
- "shortValue"
- "string"
- "timeIntervalSince1970"
- "unsignedCharValue"
- "unsignedIntValue"
- "unsignedLongLongValue"
- "unsignedLongValue"
- "unsignedShortValue"
- "v16@0:8"
- "v32@0:8r^v16Q24"
- "{os_trace_blob_s=\"\"(?=\"ob_b\"*\"ob_v\"^v\"ob_s\"*\"ob_c\"*)\"ob_len\"I\"ob_size\"I\"ob_maxsize\"I\"ob_flags\"S\"ob_binary\"B}"

```
