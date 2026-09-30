## com.apple.iokit.IOSurface

> `com.apple.iokit.IOSurface`

```diff

-  __TEXT.__cstring: 0x325e
-  __TEXT.__os_log: 0x327d
+  __TEXT.__cstring: 0x32bf
+  __TEXT.__os_log: 0x345e
   __TEXT.__const: 0x40
-  __TEXT_EXEC.__text: 0x3371c
+  __TEXT_EXEC.__text: 0x34350
   __TEXT_EXEC.__auth_stubs: 0x930
   __DATA.__data: 0x178
   __DATA.__common: 0x460

   __DATA_CONST.__auth_got: 0x498
   __DATA_CONST.__got: 0xd0
   Functions: 1330
-  Symbols:   2851
-  CStrings:  625
+  Symbols:   2864
+  CStrings:  637
 
Sections:
~ __DATA.__data : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__mod_term_func : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__kalloc_type : content changed
~ __DATA_CONST.__kalloc_var : content changed
~ __DATA_CONST.__auth_got : content changed
~ __DATA_CONST.__got : content changed
Symbols:
+ __ZZN13IOSurfaceRoot14client_startedEP23IOSurfaceRootUserClientP4taskE21kalloc_type_view_3166
+ __ZZN13IOSurfaceRoot14client_startedEP23IOSurfaceRootUserClientP4taskE21kalloc_type_view_3176
+ __ZZN23IOSurfaceRootUserClient12free_handlesEvE21kalloc_type_view_2708
+ __ZZN23IOSurfaceRootUserClient13alloc_handlesEvE21kalloc_type_view_2679
+ __ZZN23IOSurfaceRootUserClient13alloc_handlesEvE21kalloc_type_view_2698
+ __ZZN23IOSurfaceRootUserClient17flush_memory_poolEjPvjE11_os_log_fmt
+ __ZZN23IOSurfaceRootUserClient17flush_memory_poolEjPvjE11_os_log_fmt_0
+ __ZZN23IOSurfaceRootUserClient17flush_memory_poolEjPvjE11_os_log_fmt_1
+ __ZZN23IOSurfaceRootUserClient17flush_memory_poolEjPvjE11_os_log_fmt_2
+ __ZZN23IOSurfaceRootUserClient17flush_memory_poolEjPvjE11_os_log_fmt_3
+ __ZZN23IOSurfaceRootUserClient18append_transactionEjjybE11_os_log_fmt
+ __ZZN23IOSurfaceRootUserClient23gather_memory_pool_dataEjP11OSSerializeE11_os_log_fmt
+ __ZZN23IOSurfaceRootUserClient23gather_memory_pool_dataEjP11OSSerializeE11_os_log_fmt_0
+ __ZZN23IOSurfaceRootUserClient25ensure_memory_pool_memoryEjPvjE11_os_log_fmt
+ __ZZN23IOSurfaceRootUserClient25ensure_memory_pool_memoryEjPvjE11_os_log_fmt_0
+ __ZZN23IOSurfaceRootUserClient25ensure_memory_pool_memoryEjPvjE11_os_log_fmt_1
+ __ZZN23IOSurfaceRootUserClient25ensure_memory_pool_memoryEjPvjE11_os_log_fmt_2
+ __ZZN23IOSurfaceRootUserClient25ensure_memory_pool_memoryEjPvjE11_os_log_fmt_3
+ __ZZN9IOSurface12setPurgeableEjPjE21kalloc_type_view_3344
+ __ZZN9IOSurface12setPurgeableEjPjE21kalloc_type_view_3522
+ __ZZN9IOSurface12setPurgeableEjPjE21kalloc_type_view_3564
+ __ZZN9IOSurface12setPurgeableEjPjE21kalloc_type_view_3613
+ __ZZN9IOSurface16parse_propertiesEP12OSDictionaryE21kalloc_type_view_1105
+ __ZZN9IOSurface16parse_propertiesEP12OSDictionaryE21kalloc_type_view_2502
+ __ZZN9IOSurface19trace_current_fenceEP7IOFenceE21kalloc_type_view_5663
+ __ZZN9IOSurface22query_transaction_listEP4taskym26IOSurfaceTransactionFilterbPmS3_S3_E21kalloc_type_view_7108
+ __ZZN9IOSurface22query_transaction_listEP4taskym26IOSurfaceTransactionFilterbPmS3_S3_E21kalloc_type_view_7131
+ __ZZN9IOSurface25synchronize_device_cachesEjjbE21kalloc_type_view_3021
+ __ZZN9IOSurface25synchronize_device_cachesEjjbE21kalloc_type_view_3043
- __ZZN13IOSurfaceRoot14client_startedEP23IOSurfaceRootUserClientP4taskE21kalloc_type_view_3169
- __ZZN13IOSurfaceRoot14client_startedEP23IOSurfaceRootUserClientP4taskE21kalloc_type_view_3179
- __ZZN23IOSurfaceRootUserClient12free_handlesEvE21kalloc_type_view_2709
- __ZZN23IOSurfaceRootUserClient13alloc_handlesEvE21kalloc_type_view_2680
- __ZZN23IOSurfaceRootUserClient13alloc_handlesEvE21kalloc_type_view_2699
- __ZZN9IOSurface12setPurgeableEjPjE21kalloc_type_view_3343
- __ZZN9IOSurface12setPurgeableEjPjE21kalloc_type_view_3521
- __ZZN9IOSurface12setPurgeableEjPjE21kalloc_type_view_3563
- __ZZN9IOSurface12setPurgeableEjPjE21kalloc_type_view_3612
- __ZZN9IOSurface16parse_propertiesEP12OSDictionaryE21kalloc_type_view_1104
- __ZZN9IOSurface16parse_propertiesEP12OSDictionaryE21kalloc_type_view_2501
- __ZZN9IOSurface19trace_current_fenceEP7IOFenceE21kalloc_type_view_5661
- __ZZN9IOSurface22query_transaction_listEP4taskym26IOSurfaceTransactionFilterbPmS3_S3_E21kalloc_type_view_7106
- __ZZN9IOSurface22query_transaction_listEP4taskym26IOSurfaceTransactionFilterbPmS3_S3_E21kalloc_type_view_7129
- __ZZN9IOSurface25synchronize_device_cachesEjjbE21kalloc_type_view_3020
- __ZZN9IOSurface25synchronize_device_cachesEjjbE21kalloc_type_view_3042
Functions:
~ __ZN20IOSurfaceSharedEvent19assignAgentMaskSlotEyPj : 548 -> 556
~ __ZN9IOSurface4initEP13IOSurfaceRootP4taskP12OSDictionaryPS_ : 1564 -> 1604
~ __ZN9IOSurface16parse_propertiesEP12OSDictionary : 14072 -> 14160
~ __ZN9IOSurface8allocateEv : 2848 -> 3140
~ __ZN9IOSurface16reset_propertiesEv : 620 -> 616
~ __ZN9IOSurface9set_valueEPK8OSSymbolPK15OSMetaClassBasePj : 696 -> 704
~ __ZN15IOSurfaceClient9mapInTaskEP4taskjb : 408 -> 444
~ __ZN13IOSurfaceRoot12find_surfaceEjP4taskP23IOSurfaceRootUserClient : 360 -> 432
~ __ZN13IOSurfaceRoot17userClientForTaskEP4task : 268 -> 256
~ __ZN13IOSurfaceRoot17clientTaskStoppedEP4task : 96 -> 132
~ __ZN13IOSurfaceRoot23get_pid_gpu_policy_dictEyP11OSSerialize : 404 -> 456
~ __ZN13IOSurfaceRoot25removeEventNotifierClientEP28IOSurfaceEventNotifierClient : 276 -> 268
~ __ZN23IOSurfaceRootUserClient4initEP13IOSurfaceRootP4taskP12OSDictionary : 796 -> 824
~ __ZN23IOSurfaceRootUserClient4freeEv : 536 -> 576
~ __ZN23IOSurfaceRootUserClient5startEP9IOService : 376 -> 428
~ __ZN23IOSurfaceRootUserClient4stopEP9IOService : 136 -> 240
~ __ZN23IOSurfaceRootUserClient14create_surfaceEPvjP19IOSurfaceLockResultjPj : 1212 -> 1316
~ __ZN23IOSurfaceRootUserClient14lookup_surfaceEjP19IOSurfaceLockResultPj : 340 -> 388
~ __ZN23IOSurfaceRootUserClient24lookup_surface_from_portEjP19IOSurfaceLockResultPj : 440 -> 580
~ __ZN23IOSurfaceRootUserClient24create_port_from_surfaceEjyPj : 136 -> 184
~ __ZN23IOSurfaceRootUserClient24create_surface_fast_pathEP24_IOSurfaceFastCreateArgsP19IOSurfaceLockResultjPj : 992 -> 1040
~ __ZN23IOSurfaceRootUserClient25create_surface_client_memEyyP19IOSurfaceLockResultPj : 988 -> 1036
~ __ZN23IOSurfaceRootUserClient17wait_shared_eventEjyy : 256 -> 304
~ __ZN23IOSurfaceRootUserClient19signal_shared_eventEjy : 200 -> 248
~ __ZN23IOSurfaceRootUserClient19create_shared_eventEyPjPy : 228 -> 276
~ __ZN23IOSurfaceRootUserClient18query_shared_eventEjPyS0_S0_S0_ : 312 -> 360
~ __ZN23IOSurfaceRootUserClient19notify_shared_eventEjyyyy : 504 -> 552
~ __ZN23IOSurfaceRootUserClient29signal_shared_event_operationEjyjy : 292 -> 340
~ __ZN23IOSurfaceRootUserClient18create_memory_poolEPjPyPvj : 392 -> 488
~ __ZN23IOSurfaceRootUserClient25ensure_memory_pool_memoryEjPvj : 416 -> 760
~ __ZN23IOSurfaceRootUserClient17flush_memory_poolEjPvj : 416 -> 760
~ __ZN23IOSurfaceRootUserClient23gather_memory_pool_dataEjP11OSSerialize : 488 -> 684
~ __ZN23IOSurfaceRootUserClient29write_debug_info_with_optionsEP12OSDictionaryj : 1008 -> 1056
~ __ZN23IOSurfaceRootUserClient26log_surface_creation_countEv : 252 -> 300
~ __ZN23IOSurfaceRootUserClient18append_transactionEjjyb : 396 -> 508
~ __ZN23IOSurfaceRootUserClient22query_transaction_listEjym26IOSurfaceTransactionFilterbPmS1_S1_ : 188 -> 240
~ __ZN15IOSurfaceShared4initEP4taskP13IOSurfaceRootb : 200 -> 228
~ __ZN15IOSurfaceShared4freeEv : 340 -> 384
~ __ZNK15IOSurfaceShared13getOwningTaskEv : 12 -> 60
~ __ZN15IOSurfaceShared25map_surface_client_sharedEjPyS0_ : 208 -> 308
~ __ZN15IOSurfaceShared23map_event_client_sharedEjPy : 124 -> 176
~ __ZN19IOSurfaceMemoryPool23returnComponentToBucketE11OSSharedPtrI28IOSurfaceDescriptorComponentE : 380 -> 364
~ __ZN19IOSurfaceMemoryPool4initEy11OSSharedPtrI12OSDictionaryEP4taskS0_I24IOSurfaceMemoryPoolBunchE : 1184 -> 1212
~ __ZN19IOSurfaceMemoryPool14taskCanUsePoolEP4task : 584 -> 628
CStrings:
+ "%s error - copyObjectForPortNameInTask failed\n"
+ "%s error - ensureMemory failed\n"
+ "%s error - flush failed\n"
+ "%s error - invalid args\n"
+ "%s error - invalid memory pool port\n"
+ "%s error - invalid shared event port\n"
+ "%s error - task does not own memory pool\n"
+ "12111112122212121111111111111128112122111"
+ "1211228111111111111121"
+ "128111112"
+ "append_transaction"
+ "ensure_memory_pool_memory"
+ "flush_memory_pool"
+ "gather_memory_pool_data"
- "12111112122212121111111111111121112122111"
- "1211221111111111111121"

```
