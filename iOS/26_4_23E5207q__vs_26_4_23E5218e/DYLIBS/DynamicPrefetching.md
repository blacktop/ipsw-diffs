## DynamicPrefetching

> `/System/Library/PrivateFrameworks/DynamicPrefetching.framework/DynamicPrefetching`

```diff

-3.3.1.1.0
-  __TEXT.__text: 0x12c08
-  __TEXT.__auth_stubs: 0x6b0
-  __TEXT.__const: 0x1b8
-  __TEXT.__gcc_except_tab: 0xb94
-  __TEXT.__cstring: 0x3b8
-  __TEXT.__oslogstring: 0x14f9
-  __TEXT.__unwind_info: 0x5a8
-  __TEXT.__objc_methname: 0x15b
-  __TEXT.__objc_stubs: 0x200
-  __DATA_CONST.__got: 0x78
+3.4.0.0.0
+  __TEXT.__text: 0x12ec0
+  __TEXT.__auth_stubs: 0x710
+  __TEXT.__const: 0x390
+  __TEXT.__gcc_except_tab: 0xb48
+  __TEXT.__cstring: 0x3e6
+  __TEXT.__oslogstring: 0x17b5
+  __TEXT.__unwind_info: 0x5a0
+  __TEXT.__objc_methname: 0x1a6
+  __TEXT.__objc_stubs: 0x2a0
+  __DATA_CONST.__got: 0x80
   __DATA_CONST.__const: 0x1d0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x80
-  __AUTH_CONST.__auth_got: 0x368
+  __DATA_CONST.__objc_selrefs: 0xa8
+  __AUTH_CONST.__auth_got: 0x398
   __AUTH_CONST.__const: 0xe8
-  __AUTH_CONST.__cfstring: 0x180
-  __DATA.__data: 0x20
-  __DATA.__bss: 0x189
+  __AUTH_CONST.__cfstring: 0x1a0
+  __DATA.__data: 0x28
+  __DATA.__bss: 0x168
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
   - /System/Library/PrivateFrameworks/Trial.framework/Trial
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6481E8D1-B46A-3C95-AB7D-2C7AD1E8FC97
+  UUID: 4BDE195A-4637-3276-B11A-AC22183E1BDA
   Functions: 346
-  Symbols:   1012
-  CStrings:  163
+  Symbols:   1024
+  CStrings:  180
 
Symbols:
+ GCC_except_table14
+ GCC_except_table28
+ GCC_except_table62
+ GCC_except_table67
+ GCC_except_table68
+ GCC_except_table76
+ GCC_except_table77
+ GCC_except_table94
+ _OBJC_CLASS_$_BSBuildVersion
+ __ZN11Prefetching21kLastSeenBuildVersionE
+ __ZN11Prefetching2V113profile_dirty25deserialize_profile_dirtyENSt3__14spanIKhLm18446744073709551615EEE.cold.3
+ __ZN11Prefetching2V119telemetry_payload_tC1EPK8NSStringNS0_8ScenarioE
+ __ZN11Prefetching2V119telemetry_payload_tC1ERKNS0_7ProfileE
+ __ZN11Prefetching2V119telemetry_payload_tC2EPK8NSStringNS0_8ScenarioE
+ __ZN11Prefetching2V119telemetry_payload_tC2ERKNS0_7ProfileE
+ __ZN11Prefetching2V123emit_powerlog_telemetryEPK22PPSTelemetryIdentifierRKNS0_19telemetry_payload_tE
+ __ZN11Prefetching2V123emit_powerlog_telemetryEPK22PPSTelemetryIdentifierRKNS0_19telemetry_payload_tE.cold.1
+ __ZN11Prefetching2V17Profile19delete_all_profilesEv
+ __ZN11Prefetching2V17Profile19delete_all_profilesEv.cold.1
+ __ZN11Prefetching2V17get_logEv
+ __ZN11Prefetching2V17get_logEv.cold.1
+ __ZN11Prefetching2V1L15bucketize_valueEyNSt3__14spanIKyLm18446744073709551615EEE
+ __ZN11Prefetching2V1L24PREFETCHING_SIZE_BUCKETSE
+ __ZN11Prefetching2V1L29PREFETCHING_ITERATION_BUCKETSE
+ __ZN12_GLOBAL__N_113fast_defaultsE
+ __ZN12_GLOBAL__N_119incompatible_kernelE.0
+ __ZN12_GLOBAL__N_127check_build_version_updatedEPv
+ __ZN12_GLOBAL__N_127check_build_version_updatedEPv.cold.1
+ __ZN12_GLOBAL__N_127check_build_version_updatedEPv.cold.2
+ __ZN12_GLOBAL__N_127check_build_version_updatedEPv.cold.3
+ __ZN12_GLOBAL__N_127check_build_version_updatedEPv.cold.4
+ __ZN12_GLOBAL__N_127check_build_version_updatedEPv.cold.5
+ __ZNK11Prefetching2V15Types9file_path19get_prefetchabilityEv.cold.1
+ __ZNSt3__14__fs10filesystem12__remove_allERKNS1_4pathEPNS_10error_codeE
+ ____ZN12_GLOBAL__N_14initEv_block_invoke.23
+ ____ZN12_GLOBAL__N_14initEv_block_invoke.23.cold.1
+ ___block_literal_global.16
+ ___block_literal_global.25
+ _dispatch_async_f
+ _memchr
+ _objc_alloc_init
+ _objc_msgSend$fromString:
+ _objc_msgSend$isSameAs:
+ _objc_msgSend$setObject:forKey:
+ _objc_msgSend$stringForKey:
+ _objc_msgSend$stringRepresentation
+ _objc_release_x28
+ _objc_retain_x22
- GCC_except_table109
- GCC_except_table12
- GCC_except_table22
- GCC_except_table27
- GCC_except_table29
- GCC_except_table46
- GCC_except_table47
- GCC_except_table50
- GCC_except_table61
- GCC_except_table63
- GCC_except_table82
- GCC_except_table83
- GCC_except_table91
- GCC_except_table92
- __ZGVZN12_GLOBAL__N_132check_update_prefetching_defaultEvE8defaults
- __ZN11Prefetching2V112_GLOBAL__N_17get_logEv
- __ZN11Prefetching2V112_GLOBAL__N_17get_logEv.cold.1
- __ZN12_GLOBAL__N_119incompatible_kernelE
- __ZN12_GLOBAL__N_119telemetry_payload_tC1ERKN11Prefetching2V17ProfileE
- __ZN12_GLOBAL__N_123emit_powerlog_telemetryERKNS_19telemetry_payload_tE
- __ZN12_GLOBAL__N_123emit_powerlog_telemetryERKNS_19telemetry_payload_tE.cold.1
- __ZN12_GLOBAL__N_123emit_powerlog_telemetryERKNS_19telemetry_payload_tE.cold.2
- __ZN12_GLOBAL__N_17get_logEv
- __ZN12_GLOBAL__N_17get_logEv.cold.1
- __ZNKSt3__111__copy_implclB9fqn210106IPN11Prefetching2V112file_regionsES5_S5_EENS_4pairIT_T1_EES7_T0_S8_
- __ZNSt3__116__variant_detail12__assignmentINS0_8__traitsIJNS_9monostateEN11Prefetching2V113profile_cleanENS5_13profile_dirtyEEEEE12__assign_altB9fqn210106ILm2ES7_RS7_EEvRNS0_5__altIXT_ET0_EEOT1_
- __ZNSt3__135__uninitialized_allocator_copy_implB9fqn210106INS_9allocatorIN11Prefetching2V112file_regionsEEEPS4_S6_S6_EET2_RT_T0_T1_S7_
- __ZNSt3__16vectorI9radvisoryNS_9allocatorIS1_EEEC2B9fqn210106ERKS4_
- __ZNSt3__16vectorIN11Prefetching2V112file_regionsENS_9allocatorIS3_EEE11__vallocateB9fqn210106Em
- __ZNSt3__16vectorIN11Prefetching2V112file_regionsENS_9allocatorIS3_EEE16__init_with_sizeB9fqn210106IPS3_S8_EEvT_T0_m
- __ZNSt3__16vectorIN11Prefetching2V112file_regionsENS_9allocatorIS3_EEE18__assign_with_sizeB9fqn210106IPS3_S8_EEvT_T0_l
- __ZZN12_GLOBAL__N_132check_update_prefetching_defaultEvE8defaults
- __ZZNSt3__116__variant_detail12__assignmentINS0_8__traitsIJNS_9monostateEN11Prefetching2V113profile_cleanENS5_13profile_dirtyEEEEE12__assign_altB9fqn210106ILm2ES7_RS7_EEvRNS0_5__altIXT_ET0_EEOT1_ENKUt_clENS_17integral_constantIbLb0EEE
- ____ZN12_GLOBAL__N_14initEv_block_invoke.34
- ____ZN12_GLOBAL__N_14initEv_block_invoke.34.cold.1
- ___block_literal_global.27
- ___block_literal_global.36
CStrings:
+ ".."
+ "Profile: Error setting permissions on \"%s\" (%s)."
+ "Profile::delete_all_profiles: Could not delete prefetching directory due to %s"
+ "Profile::delete_all_profiles: Successfully deleted all prefetching profiles"
+ "check_build_version_updated: BSBuildVersion not present"
+ "check_build_version_updated: Could not create defaults object for %@."
+ "check_build_version_updated: Could not delete all prefetching profiles"
+ "check_build_version_updated: Could not get the current OS version"
+ "check_build_version_updated: Detected update from version %@ to %@, successfully deleted old profiles"
+ "emit_powerlog_telemetry: Sent telemetry to PPS: %@:%@, %@:%llu, %@:%llu, %@:%llu"
+ "end_scenario_internal: scenario %llu not supported (only Launch is implemented)"
+ "fromString:"
+ "isSameAs:"
+ "prefetching_last_seen_build_version_string"
+ "profile_dirty: bundle_id is null in FlatBuffer."
+ "setObject:forKey:"
+ "start_scenario: scenario %llu not supported (only Launch is implemented)"
+ "stringForKey:"
+ "stringRepresentation"
- "emit_powerlog_telemetry: Sent telemetry to PPS!"
- "end_scenario_internal: called with an invalid scenario"
- "start_scenario: called with an invalid scenario"

```
