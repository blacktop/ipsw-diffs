## libSystemDetermination.dylib

> `/System/Library/Frameworks/CoreTelephony.framework/Support/libSystemDetermination.dylib`

```diff

-13110.4.0.0.0
-  __TEXT.__text: 0x5c2c8
-  __TEXT.__auth_stubs: 0x1130
+13113.1.0.0.0
+  __TEXT.__text: 0x5c168
+  __TEXT.__auth_stubs: 0x1140
   __TEXT.__const: 0x2a07
-  __TEXT.__gcc_except_tab: 0x49f4
+  __TEXT.__gcc_except_tab: 0x49dc
   __TEXT.__cstring: 0x2814
-  __TEXT.__oslogstring: 0x7fe7
-  __TEXT.__unwind_info: 0x1c98
+  __TEXT.__oslogstring: 0x7fb1
+  __TEXT.__unwind_info: 0x1c90
   __DATA_CONST.__got: 0x258
   __DATA_CONST.__const: 0xd98
-  __AUTH_CONST.__auth_got: 0x8a0
-  __AUTH_CONST.__const: 0x3090
+  __AUTH_CONST.__auth_got: 0x8a8
+  __AUTH_CONST.__const: 0x3098
   __AUTH_CONST.__cfstring: 0x800
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__bss: 0x60

   - /usr/lib/libTelephonyCapabilities.dylib
   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: ECDFEAF2-953E-38DF-AB24-E8641611DA4D
-  Functions: 1291
-  Symbols:   3103
-  CStrings:  1300
+  UUID: 0332E91D-46CD-33A4-B7DA-F4774D069150
+  Functions: 1290
+  Symbols:   3100
+  CStrings:  1298
 
Symbols:
+ GCC_except_table105
+ GCC_except_table136
+ GCC_except_table147
+ GCC_except_table155
+ GCC_except_table326
+ GCC_except_table329
+ GCC_except_table337
+ GCC_except_table344
+ GCC_except_table347
+ GCC_except_table352
+ GCC_except_table357
+ GCC_except_table360
+ GCC_except_table361
+ GCC_except_table364
+ GCC_except_table367
+ GCC_except_table376
+ GCC_except_table382
+ GCC_except_table385
+ GCC_except_table396
+ GCC_except_table399
+ GCC_except_table400
+ GCC_except_table405
+ GCC_except_table412
+ GCC_except_table415
+ GCC_except_table418
+ GCC_except_table423
+ GCC_except_table426
+ GCC_except_table430
+ GCC_except_table436
+ GCC_except_table444
+ GCC_except_table449
+ GCC_except_table454
+ GCC_except_table457
+ GCC_except_table84
+ GCC_except_table98
+ __ZN26SystemDeterminationManager40handleLazuliRegistrationStateChange_syncERK13PersonalityIDRKN2sd21ImsRegistrationStatusE
+ __ZThn56_N26SystemDeterminationManager40handleLazuliRegistrationStateChange_syncERK13PersonalityIDRKN2sd21ImsRegistrationStatusE
+ _xpc_dictionary_get_count
- GCC_except_table116
- GCC_except_table119
- GCC_except_table135
- GCC_except_table154
- GCC_except_table328
- GCC_except_table331
- GCC_except_table339
- GCC_except_table346
- GCC_except_table351
- GCC_except_table354
- GCC_except_table359
- GCC_except_table362
- GCC_except_table363
- GCC_except_table366
- GCC_except_table369
- GCC_except_table378
- GCC_except_table384
- GCC_except_table387
- GCC_except_table398
- GCC_except_table401
- GCC_except_table404
- GCC_except_table411
- GCC_except_table414
- GCC_except_table419
- GCC_except_table420
- GCC_except_table425
- GCC_except_table428
- GCC_except_table434
- GCC_except_table438
- GCC_except_table448
- GCC_except_table451
- GCC_except_table456
- GCC_except_table459
- GCC_except_table97
- __ZN26SystemDeterminationManager32handleRCSPushEnabledChanged_syncEbb
- __ZNSt3__16__treeINS_12__value_typeI13PersonalityIDN26SystemDeterminationManager12RCSRegMetricEEENS_19__map_value_compareIS2_S5_NS_4lessIS2_EELb1EEENS_9allocatorIS5_EEE12__find_equalIS2_EERPNS_16__tree_node_baseIPvEERPNS_15__tree_end_nodeISH_EERKT_
- __ZNSt3__16__treeINS_12__value_typeI13PersonalityIDN26SystemDeterminationManager12RCSRegMetricEEENS_19__map_value_compareIS2_S5_NS_4lessIS2_EELb1EEENS_9allocatorIS5_EEE16__insert_node_atEPNS_15__tree_end_nodeIPNS_16__tree_node_baseIPvEEEERSH_SH_
- __ZThn48_N26SystemDeterminationManager32handleRCSPushEnabledChanged_syncEbb
CStrings:
+ "#I LazuliInfoReady: Push enabled: %s"
+ "#I Submitting RCSServiceDuration metric (provisioning: old=%u, new=%u, registration: old=%u, new=%u, transient: %u, duration: %llu, reason: %s, isPush: %u, isPR: %u)"
+ "#N Received push for %{public}s with no delegate to handle it"
- "#I LazuliInfoReady: Push is supported and enabled in config: %s"
- "#I RCSPush disabled by IDSBag"
- "#I RCSPush disabled by Trial Experiment"
- "#I RCSPush enabled"
- "#I Submitting RCSServiceDuration metric (provisioning: old=%u, new=%u, registration: old %u, new=%u, transient: %u, duration: %llu, reason: %s, isPush: %u, isPR: %u)"

```
