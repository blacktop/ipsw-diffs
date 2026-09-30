## sandboxd

> `/usr/libexec/sandboxd`

```diff

-2401.81.2.0.0
-  __TEXT.__text: 0x2a2c4
-  __TEXT.__auth_stubs: 0xef0
+2401.101.1.0.0
+  __TEXT.__text: 0x2b0e8
+  __TEXT.__auth_stubs: 0xf00
   __TEXT.__objc_stubs: 0x2480
-  __TEXT.__objc_methlist: 0xe10
+  __TEXT.__objc_methlist: 0xfc4
   __TEXT.__const: 0x7d40
-  __TEXT.__cstring: 0x13ac0
-  __TEXT.__oslogstring: 0x1c37
+  __TEXT.__cstring: 0x13d2f
+  __TEXT.__oslogstring: 0x1c81
   __TEXT.__objc_classname: 0x1b8
   __TEXT.__objc_methname: 0x28fc
   __TEXT.__objc_methtype: 0x664
-  __TEXT.__gcc_except_tab: 0x264
+  __TEXT.__gcc_except_tab: 0x2ac
   __TEXT.__dof_sandboxd: 0x2f5
   __TEXT.__unwind_info: 0x7d0
-  __DATA_CONST.__auth_got: 0x788
-  __DATA_CONST.__got: 0x268
-  __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x1fd8
-  __DATA_CONST.__cfstring: 0x7ae0
+  __DATA_CONST.__auth_got: 0x790
+  __DATA_CONST.__got: 0x250
+  __DATA_CONST.__auth_ptr: 0x30
+  __DATA_CONST.__const: 0x2088
+  __DATA_CONST.__cfstring: 0x7ba0
   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x80
-  __DATA_CONST.__objc_intobj: 0xde0
+  __DATA_CONST.__objc_intobj: 0xe10
   __DATA_CONST.__objc_arraydata: 0x1258
   __DATA_CONST.__objc_arrayobj: 0xae0
-  __DATA.__objc_const: 0x2368
-  __DATA.__objc_selrefs: 0xab8
+  __DATA.__objc_const: 0x2050
+  __DATA.__objc_selrefs: 0xb38
   __DATA.__objc_ivar: 0x158
   __DATA.__objc_data: 0x5f0
-  __DATA.__data: 0x9220
+  __DATA.__data: 0x9300
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x1f8
+  __DATA.__bss: 0x208
   __DATA.__common: 0x38
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsandbox.1.dylib
-  UUID: C1AB60CD-F0AA-30C3-8EFC-EB6F5D6908A4
-  Functions: 742
-  Symbols:   326
-  CStrings:  5535
+  UUID: 1D37867C-5F72-382C-915F-A12A9B270A69
+  Functions: 751
+  Symbols:   327
+  CStrings:  5564
 
Symbols:
+ _TCCAccessRequestIndirect
+ _os_parse_boot_arg_int
- __os_feature_enabled_impl
CStrings:
+ "APFSIOC_FILE_PADDING"
+ "MEMORYSTATUS_CMD_GET_KILL_COUNTS"
+ "MEMORYSTATUS_CMD_GET_PRIORITY_LIST_V2"
+ "SIOCGIFCONGESTEDLINK"
+ "SIOCGLINKHEURISTICS"
+ "SIOCGPOINTOPOINTMDNS"
+ "SIOCSIFCONGESTEDLINK"
+ "SIOCSPOINTOPOINTMDNS"
+ "SYS_oslog_coproc"
+ "SYS_oslog_coproc_reg"
+ "_request_tcc_approval_for_automation_target"
+ "checking %{public}s, prompting %{public}sallowed"
+ "com.apple.Sandbox.UnprivilegedContainerCreation"
+ "com.apple.sandbox.TCCService"
+ "containerId"
+ "kTCCServiceAppleEvents"
+ "kTCCServiceMediaLibrary-telemetry-"
+ "kTCCServiceSystemPolicyAppData-telemetry-container-creation"
+ "mach_vm_deferred_reclamation_buffer_allocate"
+ "mach_vm_deferred_reclamation_buffer_flush"
+ "mach_vm_deferred_reclamation_buffer_resize"
+ "mach_vm_deferred_reclamation_buffer_update_reclaimable_bytes"
+ "no target for %{public}s"
+ "path-is-translated"
+ "process-team-id"
+ "responsible-signing-id"
+ "responsible-team-id"
+ "sb_role_account_protections"
+ "strcmp(category, \"kTCCServiceAppleEvents\") == 0"
+ "target-pid-version"
+ "thread_raise_exception"
- "SIOCSETOT"
- "get_backtrack_address"
- "kTCCServiceMediaLibrary-telemetry"
- "kTCCServiceMediaLibrary-telemetry-music-garageband"
- "kTCCServiceMediaLibrary-telemetry-music-logic"
- "pop_backtrack_address"
- "protectRootAndRoleAccountHomeDirectories"
- "s->backtrack_count > 0"

```
