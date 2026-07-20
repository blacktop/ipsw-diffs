## managedeventsd

> `/usr/libexec/managedeventsd`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-111.0.0.0.0
-  __TEXT.__text: 0x23648
-  __TEXT.__auth_stubs: 0xcb0
-  __TEXT.__objc_stubs: 0xec0
-  __TEXT.__objc_methlist: 0x6b4
-  __TEXT.__const: 0x860
-  __TEXT.__objc_methname: 0x188b
-  __TEXT.__cstring: 0x1212
+113.0.2.0.0
+  __TEXT.__text: 0x23a70
+  __TEXT.__auth_stubs: 0xce0
+  __TEXT.__objc_stubs: 0xfa0
+  __TEXT.__objc_methlist: 0x6d4
+  __TEXT.__const: 0x870
+  __TEXT.__objc_methname: 0x192b
+  __TEXT.__cstring: 0x1142
   __TEXT.__objc_classname: 0x195
   __TEXT.__objc_methtype: 0x22ce
-  __TEXT.__oslogstring: 0xe42
-  __TEXT.__gcc_except_tab: 0xf80
+  __TEXT.__oslogstring: 0xeb2
+  __TEXT.__gcc_except_tab: 0x1004
   __TEXT.__swift5_entry: 0x8
   __TEXT.__swift5_typeref: 0x163
   __TEXT.__swift5_fieldmd: 0xb8

   __TEXT.__swift5_proto: 0x10
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_assocty: 0x18
-  __TEXT.__unwind_info: 0xb10
+  __TEXT.__unwind_info: 0xb40
   __TEXT.__eh_frame: 0x48
-  __DATA_CONST.__const: 0xc70
-  __DATA_CONST.__cfstring: 0x800
+  __DATA_CONST.__const: 0xce0
+  __DATA_CONST.__cfstring: 0x760
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA_CONST.__auth_got: 0x668
+  __DATA_CONST.__auth_got: 0x680
   __DATA_CONST.__got: 0x160
   __DATA_CONST.__auth_ptr: 0xa0
-  __DATA.__objc_const: 0x1b70
-  __DATA.__objc_selrefs: 0x4d8
+  __DATA.__objc_const: 0x1b78
+  __DATA.__objc_selrefs: 0x508
   __DATA.__objc_ivar: 0x94
   __DATA.__objc_data: 0x360
   __DATA.__data: 0x418

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/system/libxpc.dylib
-  Functions: 642
-  Symbols:   293
-  CStrings:  506
+  Functions: 649
+  Symbols:   296
+  CStrings:  511
 
Symbols:
+ __os_log_debug_impl
+ _audit_token_to_euid
+ _audit_token_to_pidversion
+ _strstr
- _es_mute_process_options
CStrings:
+ ".app/Contents/MacOS/"
+ "Broadcast login-item index invalidation to %lu agent(s)"
+ "Login-item invalidation to agent (UID %u) failed: %{public}@"
+ "_handleESMessage:"
+ "com.apple.campo"
+ "enumerateKeysAndObjectsUsingBlock:"
+ "initWithBytes:length:encoding:"
+ "invalidateAgentLoginItemIndex"
+ "invalidateLoginItemIndex"
+ "unsignedIntValue"
+ "v32@?0@\"NSNumber\"8@\"NSXPCConnection\"16^B24"
- "Allowlist muting of a core allowed process"
- "Allowlist muting of allowed internal process"
- "Allowlist muting of an allowed accessibility process"
- "Allowlist muting of an allowed internal process"
- "Allowlist muting of an allowed process"
- "Allowlist muting of an allowed utility process"
```
