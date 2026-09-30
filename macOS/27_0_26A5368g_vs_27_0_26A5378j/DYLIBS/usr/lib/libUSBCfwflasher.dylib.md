## libUSBCfwflasher.dylib

> `/usr/lib/libUSBCfwflasher.dylib`

```diff

-  __TEXT.__text: 0x24dbc
+  __TEXT.__text: 0x24ec0
   __TEXT.__init_offsets: 0x18
   __TEXT.__objc_methlist: 0x4fc
-  __TEXT.__cstring: 0x8eae
+  __TEXT.__cstring: 0x8eb0
   __TEXT.__gcc_except_tab: 0x6e0
-  __TEXT.__const: 0x1660
-  __TEXT.__oslogstring: 0x26ae
-  __TEXT.__unwind_info: 0x868
+  __TEXT.__const: 0x1670
+  __TEXT.__oslogstring: 0x26d1
+  __TEXT.__unwind_info: 0x870
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __AUTH_CONST.__objc_const: 0x720
   __AUTH_CONST.__weak_auth_got: 0x20
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH_CONST.__auth_got: 0x5f8
+  __AUTH_CONST.__auth_got: 0x618
   __AUTH.__objc_data: 0x190
   __DATA.__objc_ivar: 0x6c
-  __DATA.__data: 0x410
+  __DATA.__data: 0x420
   __DATA.__bss: 0x768
   __DATA.__common: 0xac
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 479
-  Symbols:   1109
-  CStrings:  1812
+  Functions: 480
+  Symbols:   1114
+  CStrings:  1815
 
Sections:
~ __TEXT.__init_offsets : content changed
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__weak_got : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH.__objc_data : content changed
Symbols:
+ GCC_except_table248
+ GCC_except_table588
+ __os_signpost_emit_with_name_impl
+ _astris_get_process_info
+ _os_signpost_enabled
+ _os_signpost_id_generate
+ _uuid_generate
- GCC_except_table582
Functions:
~ _astris_boosters_init_with_paths : 1088 -> 1104
~ __ZNSt3__16vectorI11prod_desc_tNS_9allocatorIS1_EEE22__base_destruct_at_endB9nqe220106EPS1_ : 96 -> 84
~ __ZNSt3__15dequeI19astris_os_log_src_tNS_9allocatorIS1_EEE19__add_back_capacityEv : 448 -> 436
~ __ZN5exc_t9exc_throwEiPKcyS1_jS1_S1_S1_z : 1328 -> 1324
~ __ZN5exc_t9exc_checkEPKcyS1_jS1_S1_S1_z : 1408 -> 1396
~ __ZN14exc_instance_t7est_logERK17exc_thread_root_t : 496 -> 492
~ __ZN23AstrisAsyncController_t17collect_responsesEP8AXconn_s : 732 -> 924
~ __ZNSt3__15dequeI18outstanding_acmd_sNS_9allocatorIS1_EEE19__add_back_capacityEv : 448 -> 436
~ __ZNSt3__16vectorI16async_snapshot_sNS_9allocatorIS1_EEE22__base_destruct_at_endB9nqe220106EPS1_ : 96 -> 84
~ __astris_os_log_level_for_category : 120 -> 128
~ __ZL20axlog_setup_base_dirP11axlog_ctx_sPcPS1_ : 556 -> 528
~ _AXassert_cause_name : 88 -> 80
~ _AXstrerror : 68 -> 64
+ _astris_get_process_info
~ _AXconn_create : 1104 -> 1128
~ _reset_connect_state : 352 -> 356
~ _astris_err_from_cs_type : 388 -> 372
CStrings:
+ "%s (%d)"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.zYknpc/Sources/AstrisArmProbeServer/api/booster_api/astris_boostermanager.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.zYknpc/Sources/AstrisArmProbeServer/api/booster_api/astris_boostermanager_soc.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.zYknpc/Sources/AstrisArmProbeServer/api/concurrency/astris_attitude.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.zYknpc/Sources/AstrisArmProbeServer/api/misc/astris_user_default.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.zYknpc/Sources/AstrisArmProbeServer/api/probe_comms/astris_connect.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.zYknpc/Sources/AstrisArmProbeServer/api/probe_comms/astris_transact.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.zYknpc/Sources/AstrisArmProbeServer/api/socs/astris_explore_override.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.zYknpc/Sources/AstrisArmProbeServer/api/socs/astris_soc.cpp"
+ "3679.0.15b11"
+ "AstrisArmProbeServer-3679.0.15~11 (FizzSeed tools)"
+ "collect_responses"
+ "outstanding=%zu"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BcwAh0/Sources/AstrisArmProbeServer/api/booster_api/astris_boostermanager.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BcwAh0/Sources/AstrisArmProbeServer/api/booster_api/astris_boostermanager_soc.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BcwAh0/Sources/AstrisArmProbeServer/api/concurrency/astris_attitude.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BcwAh0/Sources/AstrisArmProbeServer/api/misc/astris_user_default.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BcwAh0/Sources/AstrisArmProbeServer/api/probe_comms/astris_connect.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BcwAh0/Sources/AstrisArmProbeServer/api/probe_comms/astris_transact.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BcwAh0/Sources/AstrisArmProbeServer/api/socs/astris_explore_override.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BcwAh0/Sources/AstrisArmProbeServer/api/socs/astris_soc.cpp"
- "3678.0.0.0.2b69"
- "AstrisArmProbeServer-3678.0.0.0.2~69 (FizzSeed tools)"

```
