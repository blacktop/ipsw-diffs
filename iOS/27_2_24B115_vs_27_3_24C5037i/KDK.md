## KDKs

- `KDK_27.2_26B123.kdk/System/Library/Kernels/kernel.release.t8152`
- `KDK_27.3_26C5035r.kdk/System/Library/Kernels/kernel.release.t8152`

#### __block_literal_263

```diff

 void* __isa;	
 int __flags;	
 int __reserved;	
- tb_error_t (xnuupcalls_xnuupcalls_readdir__result_s);* __FuncPtr;	
+ tb_error_t (xnuupcalls_xnuupcalls_sync__result_s);* __FuncPtr;	
 struct __block_descriptor_withcopydispose* __descriptor;	
 struct {
 void* __isa;	
 void* __forwarding;	
 int __flags;	
 int __size;	
-xnuupcalls_xnuupcalls_readdir__completion_s cmp;	
+xnuupcalls_xnuupcalls_sync__completion_s cmp;	
 }
 * cmp;	
 }

```
#### __block_literal_286

```diff

 void* __isa;	
 int __flags;	
 int __reserved;	
- tb_error_t (uint64_t);* __FuncPtr;	
+ tb_error_t (xnuupcalls_xnuupcalls_notification_signal__result_s);* __FuncPtr;	
 struct __block_descriptor_withcopydispose* __descriptor;	
 struct {
 void* __isa;	
 void* __forwarding;	
 int __flags;	
 int __size;	
-xnuupcalls_xnuupcalls_exfil_newchannel__completion_s cmp;	
+xnuupcalls_xnuupcalls_notification_signal__completion_s cmp;	
 }
 * cmp;	
 }

```
#### __bounds_safety::wide_ptr.indexable.305

```c
struct __bounds_safety::wide_ptr.indexable.305 {
  struct necp_client_signable *ptr;
  struct necp_client_signable *ub;
}

```
#### necp_fd_data

```diff

 int update_count;	
 int flags;	
 size_t client_count;	
+u_int64_t platform_binary_cached_uniqueid;	
+int platform_binary_cached_idversion;	
+_Bool platform_binary;	
 unsigned int background;	
 unsigned int request_in_process_flow_divert;	
 int proc_pid;	

```
#### launch_constraint_data

```diff

 struct launch_constraint_data {
 cs_launch_type_t launch_type;	
+_Bool is_exec;	
+_Bool caller_is_platform_binary;	
+_Bool caller_is_xpc_launcher;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.143

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.143 {
-struct netif_qset* ptr;	
-struct netif_qset* ub;	
-struct netif_qset* lb;	
+struct flow_route* ptr;	
+struct flow_route* ub;	
+struct flow_route* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.152

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.152 {
-struct skmem_arena* ptr;	
-struct skmem_arena* ub;	
-struct skmem_arena* lb;	
+struct netif_llink* ptr;	
+struct netif_llink* ub;	
+struct netif_llink* lb;	
 }

```
#### __block_literal_201

```diff

 void* __isa;	
 int __flags;	
 int __reserved;	
- void (size_t, const stackshot_stackshotentry_s*);* __FuncPtr;	
+ void (size_t, const stackshottypes_textlayout_s*);* __FuncPtr;	
 struct __block_descriptor* __descriptor;	
 }
 * block;	
-const stackshot_stackshotentry_v_s* val;	
+const stackshottypes_textlayout_v_s* val;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.116

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.116 {
-struct __user_channel_ring* ptr;	
-struct __user_channel_ring* ub;	
-struct __user_channel_ring* lb;	
+struct ifnet* ptr;	
+struct ifnet* ub;	
+struct ifnet* lb;	
 }

```
#### __block_literal_292

```c
struct __block_literal_292 {
  void *__isa;
  int   __flags;
  int   __reserved;
  tb_error_t(xnuupcalls_xnuupcalls_conclave_crash_info__result_s);
  *__FuncPtr;
  struct __block_descriptor_withcopydispose *__descriptor;
  struct {
    void                                                   *__isa;
    void                                                   *__forwarding;
    int                                                     __flags;
    int                                                     __size;
    xnuupcalls_xnuupcalls_conclave_crash_info__completion_s cmp;
  } *cmp;
}

```
#### key_offload_delete

```c
struct key_offload_delete {
  struct {
    struct key_offload_delete  *tqe_next;
    struct key_offload_delete **tqe_prev;
  } kod_link;
  struct ifnet *kod_ifp;
  uint64_t      kod_handle;
  _Bool         kod_policy;
  _Bool         kod_issuing;
  const void   *kod_owner;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.231

```c
struct __bounds_safety::wide_ptr.bidi_indexable.231 {
  struct if_cellular_status_v1 *ptr;
  struct if_cellular_status_v1 *ub;
  struct if_cellular_status_v1 *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.150

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.150 {
-struct __kern_quantum* ptr;	
-struct __kern_quantum* ub;	
-struct __kern_quantum* lb;	
+struct __kern_slot_desc* ptr;	
+struct __kern_slot_desc* ub;	
+struct __kern_slot_desc* lb;	
 }

```
#### __block_literal_279

```diff

 void* __isa;	
 int __flags;	
 int __reserved;	
- tb_error_t (xnuupcalls_xnuupcalls_mapper_activate__result_s);* __FuncPtr;	
+ tb_error_t (xnuupcalls_xnuupcalls_async_notification_signal__result_s);* __FuncPtr;	
 struct __block_descriptor_withcopydispose* __descriptor;	
 struct {
 void* __isa;	
 void* __forwarding;	
 int __flags;	
 int __size;	
-xnuupcalls_xnuupcalls_mapper_activate__completion_s cmp;	
+xnuupcalls_xnuupcalls_async_notification_signal__completion_s cmp;	
 }
 * cmp;	
 }

```
#### cpc_event_info

```c
struct cpc_event_info {
  const char *cev_name;
  uint16_t    cev_selector;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.226

```c
struct __bounds_safety::wide_ptr.bidi_indexable.226 {
  struct _necp_arena_info_list *ptr;
  struct _necp_arena_info_list *ub;
  struct _necp_arena_info_list *lb;
}

```
#### __bounds_safety::wide_ptr.indexable.93

```c
struct __bounds_safety::wide_ptr.indexable.93 {
  void *ptr;
  void *ub;
}

```
#### __bounds_safety::wide_ptr.indexable.202

```c
struct __bounds_safety::wide_ptr.indexable.202 {
  struct __kern_channel_ring *ptr;
  struct __kern_channel_ring *ub;
}

```
#### __block_literal_196

```diff

 int __flags;	
 int __reserved;	
  tb_error_t (tb_message_t);* __FuncPtr;	
-struct __block_descriptor_withcopydispose* __descriptor;	
-struct {
-void* __isa;	
-int __flags;	
-int __reserved;	
- void (size_t, const stackshottypes_address_s);* __FuncPtr;	
 struct __block_descriptor* __descriptor;	
-}
-* block;	
-const address_v_s* val;	
+uint8_t* out;	
+size_t srccnt;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.136

```c
struct __bounds_safety::wide_ptr.bidi_indexable.136 {
  struct sockaddr *ptr;
  struct sockaddr *ub;
  struct sockaddr *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.157

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.157 {
-struct netif_queue* ptr;	
-struct netif_queue* ub;	
-struct netif_queue* lb;	
+struct pktq* ptr;	
+struct pktq* ub;	
+struct pktq* lb;	
 }

```
#### IODataQueueDispatchSource_IVars

```diff

 class IOMemoryDescriptor* memory;	
 class OSAction* dataAvailableAction;	
 class OSAction* dataServicedAction;	
+IORWLock* lock;	
 uint64_t options;	
 uint32_t queueByteCount;	
 }

```
#### __block_literal_354

```c
struct __block_literal_354 {
  void *__isa;
  int   __flags;
  int   __reserved;
  tb_error_t();
  *__FuncPtr;
  struct __block_descriptor *__descriptor;
  uint64_t                   count;
  tb_message_t               msg;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.167

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.167 {
-struct nx_llink_info* ptr;	
-struct nx_llink_info* ub;	
-struct nx_llink_info* lb;	
+struct {
+struct netif_qset* slh_first;	
+}
+* ptr;	
+struct {
+struct netif_qset* slh_first;	
+}
+* ub;	
+struct {
+struct netif_qset* slh_first;	
+}
+* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.123

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.123 {
-struct mbuf* ptr;	
-struct mbuf* ub;	
-struct mbuf* lb;	
+struct nx_flowswitch* ptr;	
+struct nx_flowswitch* ub;	
+struct nx_flowswitch* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.119

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.119 {
-uint8_t* ptr;	
-uint8_t* ub;	
-uint8_t* lb;	
+struct sk_stats_flow* ptr;	
+struct sk_stats_flow* ub;	
+struct sk_stats_flow* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.221

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.221 {
-struct necp_client_update* ptr;	
-struct necp_client_update* ub;	
-struct necp_client_update* lb;	
+nstat_msg_src_added* ptr;	
+nstat_msg_src_added* ub;	
+nstat_msg_src_added* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.195

```c
struct __bounds_safety::wide_ptr.bidi_indexable.195 {
  nstat_msg_src_update *ptr;
  nstat_msg_src_update *ub;
  nstat_msg_src_update *lb;
}

```
#### __block_literal_277

```diff

 void* __isa;	
 int __flags;	
 int __reserved;	
- tb_error_t (xnuupcalls_xnuupcalls_unlock_wl__result_s);* __FuncPtr;	
+ tb_error_t (xnuupcalls_xnuupcalls_lock_wl__result_s);* __FuncPtr;	
 struct __block_descriptor_withcopydispose* __descriptor;	
 struct {
 void* __isa;	
 void* __forwarding;	
 int __flags;	
 int __size;	
-xnuupcalls_xnuupcalls_unlock_wl__completion_s cmp;	
+xnuupcalls_xnuupcalls_lock_wl__completion_s cmp;	
 }
 * cmp;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.201

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.201 {
-struct if_proto** ptr;	
-struct if_proto** ub;	
-struct if_proto** lb;	
+struct nstat_sysinfo_lim_stats* ptr;	
+struct nstat_sysinfo_lim_stats* ub;	
+struct nstat_sysinfo_lim_stats* lb;	
 }

```
#### __bounds_safety::wide_ptr.indexable.196

```c
struct __bounds_safety::wide_ptr.indexable.196 {
  struct nstat_msg_src_update *ptr;
  struct nstat_msg_src_update *ub;
}

```
#### __block_literal_216

```c
struct __block_literal_216 {
  void *__isa;
  int   __flags;
  int   __reserved;
  tb_error_t(tb_message_t);
  *__FuncPtr;
  struct __block_descriptor_withcopydispose *__descriptor;
  struct {
    void *__isa;
    int   __flags;
    int   __reserved;
    void(size_t, const sharedmemorybase_physicaladdress_s);
    *__FuncPtr;
    struct __block_descriptor *__descriptor;
  }                         *block;
  const physicaladdress_v_s *val;
}

```
#### nx_netif

```diff

 void* nif_intf_adv_prov_ctx;	
 struct netif_qset_extensions nif_qset_extensions;	
 struct netif_rx_flow_steering nif_rx_flow_steering;	
-struct netif_ipsec_offload nif_ipsec_offload;	
+struct netif_ipsec_offload* nif_ipsec_offload;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.185

```c
struct __bounds_safety::wide_ptr.bidi_indexable.185 {
  struct necp_kernel_ip_output_policy **ptr;
  struct necp_kernel_ip_output_policy **ub;
  struct necp_kernel_ip_output_policy **lb;
}

```
#### __block_literal_352

```c
struct __block_literal_352 {
  void *__isa;
  int   __flags;
  int   __reserved;
  tb_error_t();
  *__FuncPtr;
  struct __block_descriptor *__descriptor;
  uint64_t                   count;
  tb_message_t               msg;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.161

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.161 {
-struct {
-struct kern_nexus_domain_provider* stqh_first;	
-struct kern_nexus_domain_provider** stqh_last;	
-}
-* ptr;	
-struct {
-struct kern_nexus_domain_provider* stqh_first;	
-struct kern_nexus_domain_provider** stqh_last;	
-}
-* ub;	
-struct {
-struct kern_nexus_domain_provider* stqh_first;	
-struct kern_nexus_domain_provider** stqh_last;	
-}
-* lb;	
+struct kern_nexus_provider* ptr;	
+struct kern_nexus_provider* ub;	
+struct kern_nexus_provider* lb;	
 }

```
#### __bounds_safety::wide_ptr.indexable.151

```diff

 struct __bounds_safety::wide_ptr.indexable.151 {
-uint8_t* ptr;	
-uint8_t* ub;	
+char* ptr;	
+char* ub;	
 }

```
#### vm_fault_offset_ctx

```c
struct vm_fault_offset_ctx {
  _Bool vfo_pager_retry;
  _Bool vfo_asked_pager;
  _Bool vfo_fault_requires_copy_on_read;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.138

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.138 {
-struct flow_entry_linger_head* ptr;	
-struct flow_entry_linger_head* ub;	
-struct flow_entry_linger_head* lb;	
+struct __kern_packet** ptr;	
+struct __kern_packet** ub;	
+struct __kern_packet** lb;	
 }

```
#### __block_literal_202

```c
struct __block_literal_202 {
  void *__isa;
  int   __flags;
  int   __reserved;
  tb_error_t(tb_message_t);
  *__FuncPtr;
  struct __block_descriptor_withcopydispose *__descriptor;
  struct {
    void *__isa;
    int   __flags;
    int   __reserved;
    void(size_t, const stackshot_stackshotentry_s *);
    *__FuncPtr;
    struct __block_descriptor *__descriptor;
  }                                  *block;
  const stackshot_stackshotentry_v_s *val;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.218

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.218 {
-struct ifaddr* ptr;	
-struct ifaddr* ub;	
-struct ifaddr* lb;	
+struct necp_client_result_netagent* ptr;	
+struct necp_client_result_netagent* ub;	
+struct necp_client_result_netagent* lb;	
 }

```
#### os_log_metadata_entry

```c
struct os_log_metadata_entry {
  struct {
    struct os_log_metadata_entry  *tqe_next;
    struct os_log_metadata_entry **tqe_prev;
  } ome_link;
  uint16_t ome_size;
  uint8_t *ome_record;
}

```
#### __bounds_safety::wide_ptr.indexable.59

```c
struct __bounds_safety::wide_ptr.indexable.59 {
  uint8_t *ptr;
  uint8_t *ub;
}

```
#### __bounds_safety::wide_ptr.indexable.76

```diff

 struct __bounds_safety::wide_ptr.indexable.76 {
-void* ptr;	
-void* ub;	
+uint8_t* ptr;	
+uint8_t* ub;	
 }

```
#### __block_literal_287

```diff

 void* __forwarding;	
 int __flags;	
 int __size;	
-xnuupcalls_xnuupcalls_exfil_data__completion_s cmp;	
+xnuupcalls_xnuupcalls_exfil_newchannel__completion_s cmp;	
 }
 * cmp;	
 }

```
#### __block_literal_304

```c
struct __block_literal_304 {
  void *__isa;
  int   __flags;
  int   __reserved;
  tb_error_t(tb_message_t);
  *__FuncPtr;
  struct __block_descriptor_withcopydispose *__descriptor;
  struct {
    void *__isa;
    int   __flags;
    int   __reserved;
    void(size_t, const statsdelegate_statvalue__opt_s *);
    *__FuncPtr;
    struct __block_descriptor *__descriptor;
  }                                     *block;
  const statsdelegate_statvalue_opt_v_s *val;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.200

```c
struct __bounds_safety::wide_ptr.bidi_indexable.200 {
  struct necp_tcp_stats *ptr;
  struct necp_tcp_stats *ub;
  struct necp_tcp_stats *lb;
}

```
#### __bounds_safety::wide_ptr.indexable.149

```c
struct __bounds_safety::wide_ptr.indexable.149 {
  char *ptr;
  char *ub;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.285

```c
struct __bounds_safety::wide_ptr.bidi_indexable.285 {
  struct eventhandler_entry *ptr;
  struct eventhandler_entry *ub;
  struct eventhandler_entry *lb;
}

```
#### exclaveindicatorcontroller_cpstate_s

```c
struct exclaveindicatorcontroller_cpstate_s {
  uint64_t usage;
  uint64_t max;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.183

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.183 {
-struct ucred* ptr;	
-struct ucred* ub;	
-struct ucred* lb;	
+struct if_wifi_status_v1* ptr;	
+struct if_wifi_status_v1* ub;	
+struct if_wifi_status_v1* lb;	
 }

```
#### __block_literal_343

```c
struct __block_literal_343 {
  void *__isa;
  int   __flags;
  int   __reserved;
  tb_error_t();
  *__FuncPtr;
  struct __block_descriptor *__descriptor;
  uint64_t                   count;
  tb_message_t               msg;
}

```
#### __block_literal_197

```c
struct __block_literal_197 {
  void *__isa;
  int   __flags;
  int   __reserved;
  tb_error_t(tb_message_t);
  *__FuncPtr;
  struct __block_descriptor_withcopydispose *__descriptor;
  struct {
    void *__isa;
    int   __flags;
    int   __reserved;
    void(size_t, const stackshottypes_address_s);
    *__FuncPtr;
    struct __block_descriptor *__descriptor;
  }                 *block;
  const address_v_s *val;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.209

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.209 {
-struct {
-struct ns_token* lh_first;	
-}
-* ptr;	
-struct {
-struct ns_token* lh_first;	
-}
-* ub;	
-struct {
-struct ns_token* lh_first;	
-}
-* lb;	
+struct necp_domain_filter_list* ptr;	
+struct necp_domain_filter_list* ub;	
+struct necp_domain_filter_list* lb;	
 }

```
#### _ca_event_exclave_indicator_controller_dispwake_metrics_v1

```c
struct _ca_event_exclave_indicator_controller_dispwake_metrics_v1 {
  unsigned long long display_wake_allowance_ms;
  unsigned long long num_display_power_policies_triggered;
  unsigned long long num_default_display_changed_policies_triggered;
  unsigned long long max_display_power_used_ms;
  unsigned long long max_default_display_changed_used_ms;
  unsigned long long display_power_bucket_0_100_ms;
  unsigned long long display_power_bucket_101_200_ms;
  unsigned long long display_power_bucket_201_300_ms;
  unsigned long long display_power_bucket_301_400_ms;
  unsigned long long display_power_bucket_401_500_ms;
  unsigned long long display_power_bucket_501_600_ms;
  unsigned long long display_power_bucket_601_700_ms;
  unsigned long long display_power_bucket_701_800_ms;
  unsigned long long display_power_bucket_801_900_ms;
  unsigned long long display_power_bucket_901_1000_ms;
  unsigned long long display_power_bucket_1001_1500_ms;
  unsigned long long display_power_bucket_1501_2000_ms;
  unsigned long long display_power_bucket_2001_2500_ms;
  unsigned long long display_power_bucket_2501_3000_ms;
  unsigned long long display_power_bucket_3001_3500_ms;
  unsigned long long display_power_bucket_3501_4000_ms;
  unsigned long long display_power_bucket_4000_plus_ms;
  unsigned long long default_display_changed_bucket_0_100_ms;
  unsigned long long default_display_changed_bucket_101_200_ms;
  unsigned long long default_display_changed_bucket_201_300_ms;
  unsigned long long default_display_changed_bucket_301_400_ms;
  unsigned long long default_display_changed_bucket_401_500_ms;
  unsigned long long default_display_changed_bucket_501_600_ms;
  unsigned long long default_display_changed_bucket_601_700_ms;
  unsigned long long default_display_changed_bucket_701_800_ms;
  unsigned long long default_display_changed_bucket_801_900_ms;
  unsigned long long default_display_changed_bucket_901_1000_ms;
  unsigned long long default_display_changed_bucket_1001_1500_ms;
  unsigned long long default_display_changed_bucket_1501_2000_ms;
  unsigned long long default_display_changed_bucket_2001_2500_ms;
  unsigned long long default_display_changed_bucket_2501_3000_ms;
  unsigned long long default_display_changed_bucket_3001_3500_ms;
  unsigned long long default_display_changed_bucket_3501_4000_ms;
  unsigned long long default_display_changed_bucket_4000_plus_ms;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.137

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.137 {
-struct protosw* ptr;	
-struct protosw* ub;	
-struct protosw* lb;	
+struct cmsghdr* ptr;	
+struct cmsghdr* ub;	
+struct cmsghdr* lb;	
 }

```
#### __bounds_safety::wide_ptr.indexable.102

```c
struct __bounds_safety::wide_ptr.indexable.102 {
  char *ptr;
  char *ub;
}

```
#### __block_literal_253

```diff

 void* __forwarding;	
 int __flags;	
 int __size;	
-xnuupcalls_xnuupcalls_free_ext__completion_s cmp;	
+xnuupcalls_xnuupcalls_free__completion_s cmp;	
 }
 * cmp;	
 }

```
#### __block_literal_259

```diff

 void* __isa;	
 int __flags;	
 int __reserved;	
- tb_error_t (xnuupcalls_xnuupcalls_read__result_s);* __FuncPtr;	
+ tb_error_t (xnuupcalls_xnuupcalls_create__result_s);* __FuncPtr;	
 struct __block_descriptor_withcopydispose* __descriptor;	
 struct {
 void* __isa;	
 void* __forwarding;	
 int __flags;	
 int __size;	
-xnuupcalls_xnuupcalls_read__completion_s cmp;	
+xnuupcalls_xnuupcalls_create__completion_s cmp;	
 }
 * cmp;	
 }

```
#### __block_literal_285

```diff

 void* __isa;	
 int __flags;	
 int __reserved;	
- tb_error_t (xnuupcalls_xnuupcalls_notification_signal__result_s);* __FuncPtr;	
+ tb_error_t (xnuupcalls_xnuupcalls_ane_workend__result_s);* __FuncPtr;	
 struct __block_descriptor_withcopydispose* __descriptor;	
 struct {
 void* __isa;	
 void* __forwarding;	
 int __flags;	
 int __size;	
-xnuupcalls_xnuupcalls_notification_signal__completion_s cmp;	
+xnuupcalls_xnuupcalls_ane_workend__completion_s cmp;	
 }
 * cmp;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.86

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.86 {
-const struct __kern_packet** ptr;	
-const struct __kern_packet** ub;	
-const struct __kern_packet** lb;	
+struct nx_port_info* ptr;	
+struct nx_port_info* ub;	
+struct nx_port_info* lb;	
 }

```
#### __block_literal_280

```diff

 void* __isa;	
 int __flags;	
 int __reserved;	
- tb_error_t (xnuupcalls_xnuupcalls_mapper_deactivate__result_s);* __FuncPtr;	
+ tb_error_t (xnuupcalls_xnuupcalls_mapper_activate__result_s);* __FuncPtr;	
 struct __block_descriptor_withcopydispose* __descriptor;	
 struct {
 void* __isa;	
 void* __forwarding;	
 int __flags;	
 int __size;	
-xnuupcalls_xnuupcalls_mapper_deactivate__completion_s cmp;	
+xnuupcalls_xnuupcalls_mapper_activate__completion_s cmp;	
 }
 * cmp;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.164

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.164 {
-struct nx_llink_info_req* ptr;	
-struct nx_llink_info_req* ub;	
-struct nx_llink_info_req* lb;	
+struct kalloc_heap* ptr;	
+struct kalloc_heap* ub;	
+struct kalloc_heap* lb;	
 }

```
#### __bounds_safety::wide_ptr.indexable.175

```c
struct __bounds_safety::wide_ptr.indexable.175 {
  const u_int8_t *ptr;
  const u_int8_t *ub;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.177

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.177 {
-struct nxprov_params* ptr;	
-struct nxprov_params* ub;	
-struct nxprov_params* lb;	
+necp_application_id_t* ptr;	
+necp_application_id_t* ub;	
+necp_application_id_t* lb;	
 }

```
#### __block_literal_268

```diff

 void* __isa;	
 int __flags;	
 int __reserved;	
- tb_error_t (xnuupcalls_xnuupcalls_irq_enable__result_s);* __FuncPtr;	
+ tb_error_t (xnuupcalls_xnuupcalls_irq_remove__result_s);* __FuncPtr;	
 struct __block_descriptor_withcopydispose* __descriptor;	
 struct {
 void* __isa;	
 void* __forwarding;	
 int __flags;	
 int __size;	
-xnuupcalls_xnuupcalls_irq_enable__completion_s cmp;	
+xnuupcalls_xnuupcalls_irq_remove__completion_s cmp;	
 }
 * cmp;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.129

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.129 {
-struct icmp6_hdr* ptr;	
-struct icmp6_hdr* ub;	
-struct icmp6_hdr* lb;	
+struct rtentry* ptr;	
+struct rtentry* ub;	
+struct rtentry* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.206

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.206 {
-struct necp_domain_filter_list* ptr;	
-struct necp_domain_filter_list* ub;	
-struct necp_domain_filter_list* lb;	
+struct necp_stat_counts* ptr;	
+struct necp_stat_counts* ub;	
+struct necp_stat_counts* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.142

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.142 {
-struct mbuf* ptr;	
-struct mbuf* ub;	
-struct mbuf* lb;	
+struct netif_qset* ptr;	
+struct netif_qset* ub;	
+struct netif_qset* lb;	
 }

```
#### netagent_registration

```diff

 u_int8_t allow_multiple_registrations;	
 u_int8_t __pad_bytes[2];	
 struct netagent_token_list_s token_list;	
+struct netagent_tls_psk_derivation_context* tls_psk_derivation_context_outbound;	
+struct netagent_tls_psk_derivation_context_list_s tls_psk_derivation_context_inbound_list;	
 struct netagent_client_list_s pending_triggers_list;	
 size_t netagent_alloc_size;	
 __bounds_safety::sized_by::netagent_alloc_size netagent;	

```
#### __bounds_safety::wide_ptr.bidi_indexable.214

```c
struct __bounds_safety::wide_ptr.bidi_indexable.214 {
  struct necp_domain_trie *ptr;
  struct necp_domain_trie *ub;
  struct necp_domain_trie *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.158

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.158 {
-struct pktq* ptr;	
-struct pktq* ub;	
-struct pktq* lb;	
+const struct in6_addr* ptr;	
+const struct in6_addr* ub;	
+const struct in6_addr* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.168

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.168 {
-struct {
-struct netif_qset* slh_first;	
-}
-* ptr;	
-struct {
-struct netif_qset* slh_first;	
-}
-* ub;	
-struct {
-struct netif_qset* slh_first;	
-}
-* lb;	
+struct nx_qset_info* ptr;	
+struct nx_qset_info* ub;	
+struct nx_qset_info* lb;	
 }

```
#### __block_literal_288

```diff

 void* __forwarding;	
 int __flags;	
 int __size;	
-xnuupcalls_xnuupcalls_exfil_closechannel__completion_s cmp;	
+xnuupcalls_xnuupcalls_exfil_data__completion_s cmp;	
 }
 * cmp;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.163

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.163 {
-struct sastat* ptr;	
-struct sastat* ub;	
-struct sastat* lb;	
+struct nx_llink_info_req* ptr;	
+struct nx_llink_info_req* ub;	
+struct nx_llink_info_req* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.125

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.125 {
-struct nx_flowswitch* ptr;	
-struct nx_flowswitch* ub;	
-struct nx_flowswitch* lb;	
+struct __kern_packet* ptr;	
+struct __kern_packet* ub;	
+struct __kern_packet* lb;	
 }

```
#### __block_literal_254

```diff

 void* __isa;	
 int __flags;	
 int __reserved;	
- tb_error_t (uint64_t);* __FuncPtr;	
+ tb_error_t ();* __FuncPtr;	
 struct __block_descriptor_withcopydispose* __descriptor;	
 struct {
 void* __isa;	
 void* __forwarding;	
 int __flags;	
 int __size;	
-xnuupcalls_xnuupcalls_helloupcall__completion_s cmp;	
+xnuupcalls_xnuupcalls_free_ext__completion_s cmp;	
 }
 * cmp;	
 }

```
#### if_fake

```diff

 unsigned int iff_max_mtu;	
 uint32_t iff_fcs;	
 uint32_t iff_trailer_length;	
+struct feth_ipsec_state iff_ipsec;	
 fake_nx iff_nx;	
 struct netif_stats* iff_nifs;	
 uint32_t iff_nifs_ref;	

```
#### necp_policy_result_ip_tunnel

```diff

 struct necp_policy_result_ip_tunnel {
 u_int32_t secondary_result;	
 char interface_name[24];	
+u_int32_t result_flags;	
 }

```
#### __block_literal_271

```diff

 void* __isa;	
 int __flags;	
 int __reserved;	
- tb_error_t (xnuupcalls_xnuupcalls_timer_remove__result_s);* __FuncPtr;	
+ tb_error_t (xnuupcalls_xnuupcalls_timer_register__result_s);* __FuncPtr;	
 struct __block_descriptor_withcopydispose* __descriptor;	
 struct {
 void* __isa;	
 void* __forwarding;	
 int __flags;	
 int __size;	
-xnuupcalls_xnuupcalls_timer_remove__completion_s cmp;	
+xnuupcalls_xnuupcalls_timer_register__completion_s cmp;	
 }
 * cmp;	
 }

```
#### necp_client

```diff

 necp_policy_id skip_policy_id;	
 necp_kernel_policy_result policy_result;	
 necp_kernel_policy_routing_result_parameter policy_result_parameter;	
+u_int32_t policy_result_flags;	
 u_int32_t flow_divert_control_unit;	
 u_int32_t filter_control_unit;	
 u_int8_t ip_protocol;	

```
#### __bounds_safety::wide_ptr.bidi_indexable.76

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.76 {
-struct __kern_buflet* ptr;	
-struct __kern_buflet* ub;	
-struct __kern_buflet* lb;	
+struct netif_list_flowtable* ptr;	
+struct netif_list_flowtable* ub;	
+struct netif_list_flowtable* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.160

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.160 {
-struct kern_nexus_domain_provider* ptr;	
-struct kern_nexus_domain_provider* ub;	
-struct kern_nexus_domain_provider* lb;	
+struct {
+struct kern_nexus_domain_provider* stqh_first;	
+struct kern_nexus_domain_provider** stqh_last;	
+}
+* ptr;	
+struct {
+struct kern_nexus_domain_provider* stqh_first;	
+struct kern_nexus_domain_provider** stqh_last;	
+}
+* ub;	
+struct {
+struct kern_nexus_domain_provider* stqh_first;	
+struct kern_nexus_domain_provider** stqh_last;	
+}
+* lb;	
 }

```
#### os_log_metadata_list

```c
struct os_log_metadata_list {
  struct {
    struct os_log_metadata_entry  *tqh_first;
    struct os_log_metadata_entry **tqh_last;
  } oml_entries;
  uint32_t oml_count;
  uint32_t oml_bytes;
  uint32_t oml_max_count;
  _Bool    oml_incomplete;
  _Bool(const void *, const void *);
  *oml_same;
}

```
#### __block_literal_266

```diff

 void* __isa;	
 int __flags;	
 int __reserved;	
- tb_error_t (xnuupcalls_xnuupcalls_irq_register__result_s);* __FuncPtr;	
+ tb_error_t (xnuupcalls_xnuupcalls_sealstate__result_s);* __FuncPtr;	
 struct __block_descriptor_withcopydispose* __descriptor;	
 struct {
 void* __isa;	
 void* __forwarding;	
 int __flags;	
 int __size;	
-xnuupcalls_xnuupcalls_irq_register__completion_s cmp;	
+xnuupcalls_xnuupcalls_sealstate__completion_s cmp;	
 }
 * cmp;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.134

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.134 {
-struct sockaddr* ptr;	
-struct sockaddr* ub;	
-struct sockaddr* lb;	
+struct ipsec_tag_container* ptr;	
+struct ipsec_tag_container* ub;	
+struct ipsec_tag_container* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.212

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.212 {
-struct necp_domain_trie_list* ptr;	
-struct necp_domain_trie_list* ub;	
-struct necp_domain_trie_list* lb;	
+struct skmem_cache* ptr;	
+struct skmem_cache* ub;	
+struct skmem_cache* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.199

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.199 {
-struct nstat_sysinfo_lim_stats* ptr;	
-struct nstat_sysinfo_lim_stats* ub;	
-struct nstat_sysinfo_lim_stats* lb;	
+ctrace_t* ptr;	
+ctrace_t* ub;	
+ctrace_t* lb;	
 }

```
#### __bounds_safety::wide_ptr.indexable.129

```c
struct __bounds_safety::wide_ptr.indexable.129 {
  char *ptr;
  char *ub;
}

```
#### __block_literal_275

```diff

 void* __isa;	
 int __flags;	
 int __reserved;	
- tb_error_t (xnuupcalls_xnuupcalls_timer_cancel_timeout__result_s);* __FuncPtr;	
+ tb_error_t (xnuupcalls_xnuupcalls_timer_set_timeout__result_s);* __FuncPtr;	
 struct __block_descriptor_withcopydispose* __descriptor;	
 struct {
 void* __isa;	
 void* __forwarding;	
 int __flags;	
 int __size;	
-xnuupcalls_xnuupcalls_timer_cancel_timeout__completion_s cmp;	
+xnuupcalls_xnuupcalls_timer_set_timeout__completion_s cmp;	
 }
 * cmp;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.144

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.144 {
-struct nx_pktq* ptr;	
-struct nx_pktq* ub;	
-struct nx_pktq* lb;	
+struct flow_route_bucket* ptr;	
+struct flow_route_bucket* ub;	
+struct flow_route_bucket* lb;	
 }

```
#### kern_nexus_capab_ipsec_offload

```diff

 uint32_t io_ops_version;	
 struct ipsec_offload_ops* io_ops;	
 void* io_prov_ctx;	
+ void (void*);* io_release;	
+const void* io_kern_ctx;	
+const  errno_t (void*);* io_flush;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.198

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.198 {
-struct necp_tcp_stats* ptr;	
-struct necp_tcp_stats* ub;	
-struct necp_tcp_stats* lb;	
+struct ifmultiaddr_dbg* ptr;	
+struct ifmultiaddr_dbg* ub;	
+struct ifmultiaddr_dbg* lb;	
 }

```
#### __bounds_safety::wide_ptr.indexable.214

```c
struct __bounds_safety::wide_ptr.indexable.214 {
  struct nstat_msg_add_src *ptr;
  struct nstat_msg_add_src *ub;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.172

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.172 {
-struct tseg_qent* ptr;	
-struct tseg_qent* ub;	
-struct tseg_qent* lb;	
+symptoms_advisory_t* ptr;	
+symptoms_advisory_t* ub;	
+symptoms_advisory_t* lb;	
 }

```
#### __block_literal_200

```diff

 void* __isa;	
 int __flags;	
 int __reserved;	
- void (size_t, const stackshottypes_textlayout_s*);* __FuncPtr;	
+ void (size_t, const stackshottypes_addressspace_s*);* __FuncPtr;	
 struct __block_descriptor* __descriptor;	
 }
 * block;	
-const stackshottypes_textlayout_v_s* val;	
+const stackshottypes_addressspace_v_s* val;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.93

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.93 {
-struct kern_channel* ptr;	
-struct kern_channel* ub;	
-struct kern_channel* lb;	
+struct counted_mbufq* ptr;	
+struct counted_mbufq* ub;	
+struct counted_mbufq* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.188

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.188 {
-struct sockaddr_dl* ptr;	
-struct sockaddr_dl* ub;	
-struct sockaddr_dl* lb;	
+struct bridge_delayed_call* ptr;	
+struct bridge_delayed_call* ub;	
+struct bridge_delayed_call* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.190

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.190 {
-nstat_msg_src_details* ptr;	
-nstat_msg_src_details* ub;	
-nstat_msg_src_details* lb;	
+struct sockaddr_dl* ptr;	
+struct sockaddr_dl* ub;	
+struct sockaddr_dl* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.176

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.176 {
-struct proc* ptr;	
-struct proc* ub;	
-struct proc* lb;	
+struct nxprov_params* ptr;	
+struct nxprov_params* ub;	
+struct nxprov_params* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.103

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.103 {
-struct ip6_ext* ptr;	
-struct ip6_ext* ub;	
-struct ip6_ext* lb;	
+struct sockbuf* ptr;	
+struct sockbuf* ub;	
+struct sockbuf* lb;	
 }

```
#### netagent_tls_psk_derivation_context_add

```c
struct netagent_tls_psk_derivation_context_add {
  u_int64_t key_id;
  u_int8_t  direction;
  u_int8_t  __pad[7];
  u_int8_t  root_key[64];
}

```
#### __block_literal_265

```diff

 void* __isa;	
 int __flags;	
 int __reserved;	
- tb_error_t (xnuupcalls_xnuupcalls_sealstate__result_s);* __FuncPtr;	
+ tb_error_t (xnuupcalls_xnuupcalls_getsize__result_s);* __FuncPtr;	
 struct __block_descriptor_withcopydispose* __descriptor;	
 struct {
 void* __isa;	
 void* __forwarding;	
 int __flags;	
 int __size;	
-xnuupcalls_xnuupcalls_sealstate__completion_s cmp;	
+xnuupcalls_xnuupcalls_getsize__completion_s cmp;	
 }
 * cmp;	
 }

```
#### netagent_tls_psk_derivation_context_list_s

```c
struct netagent_tls_psk_derivation_context_list_s {
  struct netagent_tls_psk_derivation_context  *tqh_first;
  struct netagent_tls_psk_derivation_context **tqh_last;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.165

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.165 {
-struct kalloc_heap* ptr;	
-struct kalloc_heap* ub;	
-struct kalloc_heap* lb;	
+struct {
+struct netif_llink* stqh_first;	
+struct netif_llink** stqh_last;	
+}
+* ptr;	
+struct {
+struct netif_llink* stqh_first;	
+struct netif_llink** stqh_last;	
+}
+* ub;	
+struct {
+struct netif_llink* stqh_first;	
+struct netif_llink** stqh_last;	
+}
+* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.279

```c
struct __bounds_safety::wide_ptr.bidi_indexable.279 {
  nstat_udp_descriptor *ptr;
  nstat_udp_descriptor *ub;
  nstat_udp_descriptor *lb;
}

```
#### firehose_subsystem_record_s

```c
struct firehose_subsystem_record_s {
  uint16_t fsr_size;
  uint16_t fsr_sid;
  uint8_t  fsr_subsystem_size;
  uint8_t  fsr_category_size;
  uint16_t fsr_reserved;
  char     fsr_names[0];
}

```
#### __bounds_safety::wide_ptr.indexable.166

```c
struct __bounds_safety::wide_ptr.indexable.166 {
  void *ptr;
  void *ub;
}

```
#### os_log_metadata_writer

```c
struct os_log_metadata_writer {
  uint8_t *omw_buffer;
  size_t   omw_capacity;
  size_t   omw_used;
  size_t   omw_needed;
  uint32_t omw_count;
  _Bool    omw_full;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.141

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.141 {
-const struct sadb_lifetime* ptr;	
-const struct sadb_lifetime* ub;	
-const struct sadb_lifetime* lb;	
+struct nx_pktq* ptr;	
+struct nx_pktq* ub;	
+struct nx_pktq* lb;	
 }

```
#### __bounds_safety::wide_ptr.indexable.124

```c
struct __bounds_safety::wide_ptr.indexable.124 {
  uint8_t *ptr;
  uint8_t *ub;
}

```
#### firehose_uuid_record_s

```c
struct firehose_uuid_record_s {
  uint16_t fur_size;
  uint16_t fur_path_size;
  uint8_t  fur_kind;
  uint8_t  fur_reserved[3];
  uint8_t  fur_uuid[16];
  uint64_t fur_address;
  uint64_t fur_load_size;
  char     fur_path[0];
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.290

```c
struct __bounds_safety::wide_ptr.bidi_indexable.290 {
  struct nd_ifinfo *ptr;
  struct nd_ifinfo *ub;
  struct nd_ifinfo *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.145

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.145 {
-struct cmsghdr* ptr;	
-struct cmsghdr* ub;	
-struct cmsghdr* lb;	
+struct ifclassq* ptr;	
+struct ifclassq* ub;	
+struct ifclassq* lb;	
 }

```
#### vm_pageout_stat

```diff

 uint64_t balance_deficit_reactivate_throttled;	
 uint64_t balance_deficit_upl_commit;	
 unsigned int pages_grabbed;	
+unsigned int pages_grabbed_kern;	
+unsigned int pages_grabbed_upl;	
+unsigned int pages_grabbed_iopl;	
 unsigned int pages_freed;	
 unsigned int pages_compressed;	
 unsigned int pages_decompressed;	
 unsigned int pages_grabbed_by_compressor;	
 unsigned int failed_compressions;	
 unsigned int pageins;	
+unsigned int pageins_used;	
+unsigned int pageins_shared_cache_requested;	
+unsigned int pageins_shared_cache_used;	
+unsigned int pagein_faults;	
+unsigned int pagein_cow_faults;	
 unsigned int pageouts;	
 unsigned int zero_fills;	
 unsigned int cow_faults;	
+unsigned int cache_hits;	
+unsigned int pmap_fast_faults;	
+unsigned int pmap_force_fast_faults;	
+unsigned int pmap_spurious_fast_faults;	
+unsigned int page_wires;	
+unsigned int page_unwires;	
+unsigned int kill_pages_freed;	
+unsigned int kill_footprint_pages;	
 unsigned int pages_evicted;	
 unsigned int pages_purged;	
 unsigned int considered;	

 unsigned int freed_cleaned;	
 unsigned int freed_internal;	
 unsigned int freed_external;	
+unsigned int freed_speculative_sharedcache;	
+unsigned int freed_external_sharedcache;	
+unsigned int freed_external_executable;	
+unsigned int freed_external_sharedcache_executable;	
 unsigned long inactive_clean;	
 unsigned long inactive_absent;	
 unsigned long inactive_not_alive;	

 uint64_t inactive_referenced_anonymous;	
 uint64_t inactive_referenced_external;	
 uint64_t inactive_reactivated_xpmapped;	
+unsigned int background_promoted;	
 unsigned int inactive_nolock;	
 unsigned int inactive_busy;	
 unsigned int inactive_used;	

```
#### __bounds_safety::wide_ptr.bidi_indexable.232

```c
struct __bounds_safety::wide_ptr.bidi_indexable.232 {
  struct necp_drop_dest_entry *ptr;
  struct necp_drop_dest_entry *ub;
  struct necp_drop_dest_entry *lb;
}

```
#### __block_literal_283

```diff

 void* __isa;	
 int __flags;	
 int __reserved;	
- tb_error_t (xnuupcalls_xnuupcalls_ane_workbegin__result_s);* __FuncPtr;	
+ tb_error_t (xnuupcalls_xnuupcalls_ane_worksubmit__result_s);* __FuncPtr;	
 struct __block_descriptor_withcopydispose* __descriptor;	
 struct {
 void* __isa;	
 void* __forwarding;	
 int __flags;	
 int __size;	
-xnuupcalls_xnuupcalls_ane_workbegin__completion_s cmp;	
+xnuupcalls_xnuupcalls_ane_worksubmit__completion_s cmp;	
 }
 * cmp;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.96

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.96 {
-struct flow_ip_addr* ptr;	
-struct flow_ip_addr* ub;	
-struct flow_ip_addr* lb;	
+struct {
+struct kern_channel* stqh_first;	
+struct kern_channel** stqh_last;	
+}
+* ptr;	
+struct {
+struct kern_channel* stqh_first;	
+struct kern_channel** stqh_last;	
+}
+* ub;	
+struct {
+struct kern_channel* stqh_first;	
+struct kern_channel** stqh_last;	
+}
+* lb;	
 }

```
#### __bounds_safety::wide_ptr.indexable.88

```c
struct __bounds_safety::wide_ptr.indexable.88 {
  uint8_t *ptr;
  uint8_t *ub;
}

```
#### __block_literal_256

```diff

 void* __isa;	
 int __flags;	
 int __reserved;	
- tb_error_t (xnuupcalls_xnuupcalls_open__result_s);* __FuncPtr;	
+ tb_error_t (xnuupcalls_xnuupcalls_root__result_s);* __FuncPtr;	
 struct __block_descriptor_withcopydispose* __descriptor;	
 struct {
 void* __isa;	
 void* __forwarding;	
 int __flags;	
 int __size;	
-xnuupcalls_xnuupcalls_open__completion_s cmp;	
+xnuupcalls_xnuupcalls_root__completion_s cmp;	
 }
 * cmp;	
 }

```
#### __block_literal_264

```diff

 void* __isa;	
 int __flags;	
 int __reserved;	
- tb_error_t (xnuupcalls_xnuupcalls_getsize__result_s);* __FuncPtr;	
+ tb_error_t (xnuupcalls_xnuupcalls_readdir__result_s);* __FuncPtr;	
 struct __block_descriptor_withcopydispose* __descriptor;	
 struct {
 void* __isa;	
 void* __forwarding;	
 int __flags;	
 int __size;	
-xnuupcalls_xnuupcalls_getsize__completion_s cmp;	
+xnuupcalls_xnuupcalls_readdir__completion_s cmp;	
 }
 * cmp;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.192

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.192 {
-nstat_msg_src_extended_item_hdr* ptr;	
-nstat_msg_src_extended_item_hdr* ub;	
-nstat_msg_src_extended_item_hdr* lb;	
+struct __kern_netif_intf_advisory* ptr;	
+struct __kern_netif_intf_advisory* ub;	
+struct __kern_netif_intf_advisory* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.220

```c
struct __bounds_safety::wide_ptr.bidi_indexable.220 {
  struct ifaddr *ptr;
  struct ifaddr *ub;
  struct ifaddr *lb;
}

```
#### __block_literal_371

```c
struct __block_literal_371 {
  void *__isa;
  int   __flags;
  int   __reserved;
  tb_error_t();
  *__FuncPtr;
  struct __block_descriptor *__descriptor;
  uint64_t                   count;
  tb_message_t               msg;
}

```
#### __bounds_safety::wide_ptr.indexable.77

```diff

 struct __bounds_safety::wide_ptr.indexable.77 {
-char* ptr;	
-char* ub;	
+const bitmap_t* ptr;	
+const bitmap_t* ub;	
 }

```
#### feth_ipsec_obj

```c
struct feth_ipsec_obj {
  uint64_t      fio_handle;
  struct ifnet *fio_ifp;
  _Bool         fio_is_policy;
  uint32_t      fio_spi;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.151

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.151 {
-struct __kern_slot_desc* ptr;	
-struct __kern_slot_desc* ub;	
-struct __kern_slot_desc* lb;	
+struct {
+struct kern_channel* stqh_first;	
+struct kern_channel** stqh_last;	
+}
+* ptr;	
+struct {
+struct kern_channel* stqh_first;	
+struct kern_channel** stqh_last;	
+}
+* ub;	
+struct {
+struct kern_channel* stqh_first;	
+struct kern_channel** stqh_last;	
+}
+* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.159

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.159 {
-struct rtentry* ptr;	
-struct rtentry* ub;	
-struct rtentry* lb;	
+struct kern_nexus_domain_provider* ptr;	
+struct kern_nexus_domain_provider* ub;	
+struct kern_nexus_domain_provider* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.193

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.193 {
-struct __kern_netif_intf_advisory* ptr;	
-struct __kern_netif_intf_advisory* ub;	
-struct __kern_netif_intf_advisory* lb;	
+struct flow_mgr* ptr;	
+struct flow_mgr* ub;	
+struct flow_mgr* lb;	
 }

```
#### __bounds_safety::wide_ptr.indexable.111

```c
struct __bounds_safety::wide_ptr.indexable.111 {
  void *ptr;
  void *ub;
}

```
#### __block_literal_255

```diff

 void* __isa;	
 int __flags;	
 int __reserved;	
- tb_error_t (xnuupcalls_xnuupcalls_root__result_s);* __FuncPtr;	
+ tb_error_t (uint64_t);* __FuncPtr;	
 struct __block_descriptor_withcopydispose* __descriptor;	
 struct {
 void* __isa;	
 void* __forwarding;	
 int __flags;	
 int __size;	
-xnuupcalls_xnuupcalls_root__completion_s cmp;	
+xnuupcalls_xnuupcalls_helloupcall__completion_s cmp;	
 }
 * cmp;	
 }

```
#### firehose_metadata_request_s

```c
struct firehose_metadata_request_s {
  uint32_t fmr_version;
  uint64_t fmr_buffer;
  uint32_t fmr_size;
  uint32_t fmr_flags;
  uint32_t fmr_count;
}

```
#### __block_literal_251

```diff

 void* __forwarding;	
 int __flags;	
 int __size;	
-xnuupcalls_xnuupcalls_alloc_ext__completion_s cmp;	
+xnuupcalls_xnuupcalls_alloc__completion_s cmp;	
 }
 * cmp;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.181

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.181 {
-struct if_wifi_status_v1* ptr;	
-struct if_wifi_status_v1* ub;	
-struct if_wifi_status_v1* lb;	
+struct kern_nexus_provider* ptr;	
+struct kern_nexus_provider* ub;	
+struct kern_nexus_provider* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.182

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.182 {
-struct kern_nexus_provider* ptr;	
-struct kern_nexus_provider* ub;	
-struct kern_nexus_provider* lb;	
+struct ucred* ptr;	
+struct ucred* ub;	
+struct ucred* lb;	
 }

```
#### __block_literal_269

```diff

 void* __isa;	
 int __flags;	
 int __reserved;	
- tb_error_t (xnuupcalls_xnuupcalls_irq_disable__result_s);* __FuncPtr;	
+ tb_error_t (xnuupcalls_xnuupcalls_irq_enable__result_s);* __FuncPtr;	
 struct __block_descriptor_withcopydispose* __descriptor;	
 struct {
 void* __isa;	
 void* __forwarding;	
 int __flags;	
 int __size;	
-xnuupcalls_xnuupcalls_irq_disable__completion_s cmp;	
+xnuupcalls_xnuupcalls_irq_enable__completion_s cmp;	
 }
 * cmp;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.207

```c
struct __bounds_safety::wide_ptr.bidi_indexable.207 {
  struct sk_stats_flow *ptr;
  struct sk_stats_flow *ub;
  struct sk_stats_flow *lb;
}

```
#### netif_ipsec_offload

```diff

 struct netif_ipsec_offload {
+struct {
+struct netif_ipsec_offload* le_next;	
+struct netif_ipsec_offload** le_prev;	
+}
+ io_link;	
+struct ifnet* io_ifp;	
 ipsec_offload_ops_t io_ops;	
 void* io_prov_ctx;	
+ void (void*);* io_release;	
+uint32_t io_refcnt;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.166

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.166 {
-struct {
-struct netif_llink* stqh_first;	
-struct netif_llink** stqh_last;	
-}
-* ptr;	
-struct {
-struct netif_llink* stqh_first;	
-struct netif_llink** stqh_last;	
-}
-* ub;	
-struct {
-struct netif_llink* stqh_first;	
-struct netif_llink** stqh_last;	
-}
-* lb;	
+struct nx_llink_info* ptr;	
+struct nx_llink_info* ub;	
+struct nx_llink_info* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.171

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.171 {
-struct netif_qstats_info* ptr;	
-struct netif_qstats_info* ub;	
-struct netif_qstats_info* lb;	
+struct sockaddr* ptr;	
+struct sockaddr* ub;	
+struct sockaddr* lb;	
 }

```
#### cpc_event_list

```c
struct cpc_event_list {
  unsigned int          cel_event_count;
  struct cpc_event_info cel_events[0];
}

```
#### __bounds_safety::wide_ptr.indexable.153

```c
struct __bounds_safety::wide_ptr.indexable.153 {
  uint8_t *ptr;
  uint8_t *ub;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.77

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.77 {
-struct netif_stats* ptr;	
-struct netif_stats* ub;	
-struct netif_stats* lb;	
+struct __kern_buflet* ptr;	
+struct __kern_buflet* ub;	
+struct __kern_buflet* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.170

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.170 {
-symptoms_advisory_t* ptr;	
-symptoms_advisory_t* ub;	
-symptoms_advisory_t* lb;	
+struct netif_qstats_info* ptr;	
+struct netif_qstats_info* ub;	
+struct netif_qstats_info* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.208

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.208 {
-struct nstat_msg_hdr* ptr;	
-struct nstat_msg_hdr* ub;	
-struct nstat_msg_hdr* lb;	
+struct necp_domain_filter* ptr;	
+struct necp_domain_filter* ub;	
+struct necp_domain_filter* lb;	
 }

```
#### __block_literal_272

```diff

 void* __isa;	
 int __flags;	
 int __reserved;	
- tb_error_t (xnuupcalls_xnuupcalls_timer_enable__result_s);* __FuncPtr;	
+ tb_error_t (xnuupcalls_xnuupcalls_timer_remove__result_s);* __FuncPtr;	
 struct __block_descriptor_withcopydispose* __descriptor;	
 struct {
 void* __isa;	
 void* __forwarding;	
 int __flags;	
 int __size;	
-xnuupcalls_xnuupcalls_timer_enable__completion_s cmp;	
+xnuupcalls_xnuupcalls_timer_remove__completion_s cmp;	
 }
 * cmp;	
 }

```
#### __block_literal_282

```diff

 void* __isa;	
 int __flags;	
 int __reserved;	
- tb_error_t (xnuupcalls_xnuupcalls_ane_worksubmit__result_s);* __FuncPtr;	
+ tb_error_t (xnuupcalls_xnuupcalls_ane_setpowerstate__result_s);* __FuncPtr;	
 struct __block_descriptor_withcopydispose* __descriptor;	
 struct {
 void* __isa;	
 void* __forwarding;	
 int __flags;	
 int __size;	
-xnuupcalls_xnuupcalls_ane_worksubmit__completion_s cmp;	
+xnuupcalls_xnuupcalls_ane_setpowerstate__completion_s cmp;	
 }
 * cmp;	
 }

```
#### __bounds_safety::wide_ptr.indexable.135

```c
struct __bounds_safety::wide_ptr.indexable.135 {
  struct flow_divert_group **ptr;
  struct flow_divert_group **ub;
}

```
#### __bounds_safety::wide_ptr.indexable.85

```diff

 struct __bounds_safety::wide_ptr.indexable.85 {
-void* ptr;	
-void* ub;	
+uint8_t* ptr;	
+uint8_t* ub;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.189

```c
struct __bounds_safety::wide_ptr.bidi_indexable.189 {
  struct necp_policy_condition_addr_range *ptr;
  struct necp_policy_condition_addr_range *ub;
  struct necp_policy_condition_addr_range *lb;
}

```
#### __bounds_safety::wide_ptr.indexable.185

```c
struct __bounds_safety::wide_ptr.indexable.185 {
  struct nstat_sysinfo_keyval *ptr;
  struct nstat_sysinfo_keyval *ub;
}

```
#### __bounds_safety::wide_ptr.indexable.148

```c
struct __bounds_safety::wide_ptr.indexable.148 {
  void *ptr;
  void *ub;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.241

```c
struct __bounds_safety::wide_ptr.bidi_indexable.241 {
  nstat_connection_descriptor *ptr;
  nstat_connection_descriptor *ub;
  nstat_connection_descriptor *lb;
}

```
#### __block_literal_250

```diff

 void* __isa;	
 int __flags;	
 int __reserved;	
- tb_error_t (xnuupcalls_pagelist_s);* __FuncPtr;	
-struct __block_descriptor_withcopydispose* __descriptor;	
-struct {
-void* __isa;	
-void* __forwarding;	
-int __flags;	
-int __size;	
-xnuupcalls_xnuupcalls_alloc__completion_s cmp;	
-}
-* cmp;	
+ tb_message_t (tb_service_connection_t, tb_message_t);* __FuncPtr;	
+struct __block_descriptor* __descriptor;	
+const xnuupcalls_xnuupcalls__server_s* server;	
 }

```
#### __block_literal_274

```diff

 void* __isa;	
 int __flags;	
 int __reserved;	
- tb_error_t (xnuupcalls_xnuupcalls_timer_set_timeout__result_s);* __FuncPtr;	
+ tb_error_t (xnuupcalls_xnuupcalls_timer_disable__result_s);* __FuncPtr;	
 struct __block_descriptor_withcopydispose* __descriptor;	
 struct {
 void* __isa;	
 void* __forwarding;	
 int __flags;	
 int __size;	
-xnuupcalls_xnuupcalls_timer_set_timeout__completion_s cmp;	
+xnuupcalls_xnuupcalls_timer_disable__completion_s cmp;	
 }
 * cmp;	
 }

```
#### __block_literal_261

```diff

 void* __isa;	
 int __flags;	
 int __reserved;	
- tb_error_t (xnuupcalls_xnuupcalls_remove__result_s);* __FuncPtr;	
+ tb_error_t (xnuupcalls_xnuupcalls_write__result_s);* __FuncPtr;	
 struct __block_descriptor_withcopydispose* __descriptor;	
 struct {
 void* __isa;	
 void* __forwarding;	
 int __flags;	
 int __size;	
-xnuupcalls_xnuupcalls_remove__completion_s cmp;	
+xnuupcalls_xnuupcalls_write__completion_s cmp;	
 }
 * cmp;	
 }

```
#### __block_literal_348

```c
struct __block_literal_348 {
  void *__isa;
  int   __flags;
  int   __reserved;
  tb_error_t();
  *__FuncPtr;
  struct __block_descriptor *__descriptor;
  uint64_t                   count;
  tb_message_t               msg;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.215

```c
struct __bounds_safety::wide_ptr.bidi_indexable.215 {
  struct necp_domain_trie_list *ptr;
  struct necp_domain_trie_list *ub;
  struct necp_domain_trie_list *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.297

```c
struct __bounds_safety::wide_ptr.bidi_indexable.297 {
  struct ifaddrhead *ptr;
  struct ifaddrhead *ub;
  struct ifaddrhead *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.224

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.224 {
-struct _necp_arena_info_list* ptr;	
-struct _necp_arena_info_list* ub;	
-struct _necp_arena_info_list* lb;	
+struct llc* ptr;	
+struct llc* ub;	
+struct llc* lb;	
 }

```
#### netagent_tls_psk_derivation_context

```c
struct netagent_tls_psk_derivation_context {
  struct {
    struct netagent_tls_psk_derivation_context  *tqe_next;
    struct netagent_tls_psk_derivation_context **tqe_prev;
  } tls_psk_derivation_context_chain;
  u_int64_t         key_id;
  struct cchmac_ctx hmac_ctx[34];
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.278

```c
struct __bounds_safety::wide_ptr.bidi_indexable.278 {
  struct necp_udp_stats *ptr;
  struct necp_udp_stats *ub;
  struct necp_udp_stats *lb;
}

```
#### vm_pageout_vminfo

```diff

 unsigned long vm_pageout_freed_speculative;	
 unsigned long vm_pageout_freed_external;	
 unsigned long vm_pageout_freed_internal;	
+unsigned long vm_pageout_freed_speculative_sharedcache;	
+unsigned long vm_pageout_freed_external_sharedcache;	
+unsigned long vm_pageout_freed_external_executable;	
+unsigned long vm_pageout_freed_external_sharedcache_executable;	
 unsigned long vm_pageout_inactive_clean;	
 unsigned long vm_pageout_inactive_absent;	
 unsigned long vm_pageout_inactive_not_alive;	

```
#### __bounds_safety::wide_ptr.indexable.86

```diff

 struct __bounds_safety::wide_ptr.indexable.86 {
-uint8_t* ptr;	
-uint8_t* ub;	
+void* ptr;	
+void* ub;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.155

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.155 {
-struct ifaddrhead* ptr;	
-struct ifaddrhead* ub;	
-struct ifaddrhead* lb;	
+struct netif_qstats* ptr;	
+struct netif_qstats* ub;	
+struct netif_qstats* lb;	
 }

```
#### __block_literal_289

```diff

 void* __isa;	
 int __flags;	
 int __reserved;	
- tb_error_t (xnuupcalls_xnuupcalls_conclave_suspend__result_s);* __FuncPtr;	
+ tb_error_t (uint64_t);* __FuncPtr;	
 struct __block_descriptor_withcopydispose* __descriptor;	
 struct {
 void* __isa;	
 void* __forwarding;	
 int __flags;	
 int __size;	
-xnuupcalls_xnuupcalls_conclave_suspend__completion_s cmp;	
+xnuupcalls_xnuupcalls_exfil_closechannel__completion_s cmp;	
 }
 * cmp;	
 }

```
#### __block_literal_199

```diff

 void* __isa;	
 int __flags;	
 int __reserved;	
- void (size_t, const stackshottypes_addressspace_s*);* __FuncPtr;	
+ void (size_t, const stackshottypes_ipcstackentry_s*);* __FuncPtr;	
 struct __block_descriptor* __descriptor;	
 }
 * block;	
-const stackshottypes_addressspace_v_s* val;	
+const stackshottypes_ipcstackentry_v_s* val;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.146

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.146 {
-struct ifclassq* ptr;	
-struct ifclassq* ub;	
-struct ifclassq* lb;	
+const struct flow_key* ptr;	
+const struct flow_key* ub;	
+const struct flow_key* lb;	
 }

```
#### __block_literal_369

```c
struct __block_literal_369 {
  void *__isa;
  int   __flags;
  int   __reserved;
  tb_error_t();
  *__FuncPtr;
  struct __block_descriptor *__descriptor;
  uint64_t                   count;
  tb_message_t               msg;
}

```
#### __bounds_safety::wide_ptr.indexable.108

```c
struct __bounds_safety::wide_ptr.indexable.108 {
  void *ptr;
  void *ub;
}

```
#### __block_literal_252

```diff

 void* __isa;	
 int __flags;	
 int __reserved;	
- tb_error_t ();* __FuncPtr;	
+ tb_error_t (xnuupcalls_pagelist_s);* __FuncPtr;	
 struct __block_descriptor_withcopydispose* __descriptor;	
 struct {
 void* __isa;	
 void* __forwarding;	
 int __flags;	
 int __size;	
-xnuupcalls_xnuupcalls_free__completion_s cmp;	
+xnuupcalls_xnuupcalls_alloc_ext__completion_s cmp;	
 }
 * cmp;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.131

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.131 {
-struct user32_timeval* ptr;	
-struct user32_timeval* ub;	
-struct user32_timeval* lb;	
+struct icmp6_hdr* ptr;	
+struct icmp6_hdr* ub;	
+struct icmp6_hdr* lb;	
 }

```
#### exclaves_chillpill_state

```c
struct exclaves_chillpill_state {
  uint64_t version;
  uint64_t usage;
  uint64_t max;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.223

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.223 {
-struct necp_client_observer_update* ptr;	
-struct necp_client_observer_update* ub;	
-struct necp_client_observer_update* lb;	
+struct necp_client_update* ptr;	
+struct necp_client_update* ub;	
+struct necp_client_update* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.153

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.153 {
-struct netif_llink* ptr;	
-struct netif_llink* ub;	
-struct netif_llink* lb;	
+struct sk_stats_flow_adv* ptr;	
+struct sk_stats_flow_adv* ub;	
+struct sk_stats_flow_adv* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.204

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.204 {
-struct necp_stat_counts* ptr;	
-struct necp_stat_counts* ub;	
-struct necp_stat_counts* lb;	
+struct tcp_info* ptr;	
+struct tcp_info* ub;	
+struct tcp_info* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.213

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.213 {
-nstat_msg_add_all_srcs* ptr;	
-nstat_msg_add_all_srcs* ub;	
-nstat_msg_add_all_srcs* lb;	
+struct net_bloom_filter* ptr;	
+struct net_bloom_filter* ub;	
+struct net_bloom_filter* lb;	
 }

```
#### __bounds_safety::wide_ptr.indexable.89

```c
struct __bounds_safety::wide_ptr.indexable.89 {
  char *ptr;
  char *ub;
}

```
#### __block_literal_267

```diff

 void* __isa;	
 int __flags;	
 int __reserved;	
- tb_error_t (xnuupcalls_xnuupcalls_irq_remove__result_s);* __FuncPtr;	
+ tb_error_t (xnuupcalls_xnuupcalls_irq_register__result_s);* __FuncPtr;	
 struct __block_descriptor_withcopydispose* __descriptor;	
 struct {
 void* __isa;	
 void* __forwarding;	
 int __flags;	
 int __size;	
-xnuupcalls_xnuupcalls_irq_remove__completion_s cmp;	
+xnuupcalls_xnuupcalls_irq_register__completion_s cmp;	
 }
 * cmp;	
 }

```
#### __block_literal_360

```c
struct __block_literal_360 {
  void *__isa;
  int   __flags;
  int   __reserved;
  tb_error_t();
  *__FuncPtr;
  struct __block_descriptor *__descriptor;
  uint64_t                   count;
  tb_message_t               msg;
}

```
#### __bounds_safety::wide_ptr.indexable.171

```c
struct __bounds_safety::wide_ptr.indexable.171 {
  struct nstat_msg_src_description *ptr;
  struct nstat_msg_src_description *ub;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.269

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.269 {
-nstat_tcp_descriptor* ptr;	
-nstat_tcp_descriptor* ub;	
-nstat_tcp_descriptor* lb;	
+struct traffic_stats* ptr;	
+struct traffic_stats* ub;	
+struct traffic_stats* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.178

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.178 {
-nstat_ifnet_desc_cellular_status* ptr;	
-nstat_ifnet_desc_cellular_status* ub;	
-nstat_ifnet_desc_cellular_status* lb;	
+struct tcp_timer_entry* ptr;	
+struct tcp_timer_entry* ub;	
+struct tcp_timer_entry* lb;	
 }

```
#### netagent_tls_psk_derivation_context_remove

```c
struct netagent_tls_psk_derivation_context_remove {
  u_int64_t key_id;
  u_int8_t  direction;
  u_int8_t  __pad[7];
}

```
#### __block_literal_341

```c
struct __block_literal_341 {
  void *__isa;
  int   __flags;
  int   __reserved;
  tb_error_t();
  *__FuncPtr;
  struct __block_descriptor *__descriptor;
  uint64_t                   count;
  tb_message_t               msg;
}

```
#### __block_literal_291

```diff

 void* __isa;	
 int __flags;	
 int __reserved;	
- tb_error_t (xnuupcalls_xnuupcalls_conclave_crash_info__result_s);* __FuncPtr;	
+ tb_error_t (xnuupcalls_xnuupcalls_conclave_stop__result_s);* __FuncPtr;	
 struct __block_descriptor_withcopydispose* __descriptor;	
 struct {
 void* __isa;	
 void* __forwarding;	
 int __flags;	
 int __size;	
-xnuupcalls_xnuupcalls_conclave_crash_info__completion_s cmp;	
+xnuupcalls_xnuupcalls_conclave_stop__completion_s cmp;	
 }
 * cmp;	
 }

```
#### __bounds_safety::wide_ptr.indexable.87

```diff

 struct __bounds_safety::wide_ptr.indexable.87 {
-char* ptr;	
-char* ub;	
+void* ptr;	
+void* ub;	
 }

```
#### __block_literal_257

```diff

 void* __isa;	
 int __flags;	
 int __reserved;	
- tb_error_t (xnuupcalls_xnuupcalls_close__result_s);* __FuncPtr;	
+ tb_error_t (xnuupcalls_xnuupcalls_open__result_s);* __FuncPtr;	
 struct __block_descriptor_withcopydispose* __descriptor;	
 struct {
 void* __isa;	
 void* __forwarding;	
 int __flags;	
 int __size;	
-xnuupcalls_xnuupcalls_close__completion_s cmp;	
+xnuupcalls_xnuupcalls_open__completion_s cmp;	
 }
 * cmp;	
 }

```
#### __bounds_safety::wide_ptr.indexable.107

```c
struct __bounds_safety::wide_ptr.indexable.107 {
  struct icmp6_nodeinfo *ptr;
  struct icmp6_nodeinfo *ub;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.277

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.277 {
-nstat_udp_descriptor* ptr;	
-nstat_udp_descriptor* ub;	
-nstat_udp_descriptor* lb;	
+nstat_interface_counts* ptr;	
+nstat_interface_counts* ub;	
+nstat_interface_counts* lb;	
 }

```
#### __block_literal_195

```diff

 int __flags;	
 int __reserved;	
  tb_error_t (tb_message_t);* __FuncPtr;	
+struct __block_descriptor_withcopydispose* __descriptor;	
+struct {
+void* __isa;	
+int __flags;	
+int __reserved;	
+ void (size_t, const uint8_t);* __FuncPtr;	
 struct __block_descriptor* __descriptor;	
-uint8_t* out;	
-size_t srccnt;	
+}
+* block;	
+const u8_v_s* val;	
 }

```
#### __block_literal_273

```diff

 void* __isa;	
 int __flags;	
 int __reserved;	
- tb_error_t (xnuupcalls_xnuupcalls_timer_disable__result_s);* __FuncPtr;	
+ tb_error_t (xnuupcalls_xnuupcalls_timer_enable__result_s);* __FuncPtr;	
 struct __block_descriptor_withcopydispose* __descriptor;	
 struct {
 void* __isa;	
 void* __forwarding;	
 int __flags;	
 int __size;	
-xnuupcalls_xnuupcalls_timer_disable__completion_s cmp;	
+xnuupcalls_xnuupcalls_timer_enable__completion_s cmp;	
 }
 * cmp;	
 }

```
#### __block_literal_260

```diff

 void* __isa;	
 int __flags;	
 int __reserved;	
- tb_error_t (xnuupcalls_xnuupcalls_write__result_s);* __FuncPtr;	
+ tb_error_t (xnuupcalls_xnuupcalls_read__result_s);* __FuncPtr;	
 struct __block_descriptor_withcopydispose* __descriptor;	
 struct {
 void* __isa;	
 void* __forwarding;	
 int __flags;	
 int __size;	
-xnuupcalls_xnuupcalls_write__completion_s cmp;	
+xnuupcalls_xnuupcalls_read__completion_s cmp;	
 }
 * cmp;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.128

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.128 {
-struct m_tag* ptr;	
-struct m_tag* ub;	
-struct m_tag* lb;	
+struct user64_timeval* ptr;	
+struct user64_timeval* ub;	
+struct user64_timeval* lb;	
 }

```
#### __bounds_safety::wide_ptr.indexable.114

```c
struct __bounds_safety::wide_ptr.indexable.114 {
  char *ptr;
  char *ub;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.266

```c
struct __bounds_safety::wide_ptr.bidi_indexable.266 {
  const struct sk_stats_flow *ptr;
  const struct sk_stats_flow *ub;
  const struct sk_stats_flow *lb;
}

```
#### __block_literal_262

```diff

 void* __isa;	
 int __flags;	
 int __reserved;	
- tb_error_t (xnuupcalls_xnuupcalls_sync__result_s);* __FuncPtr;	
+ tb_error_t (xnuupcalls_xnuupcalls_remove__result_s);* __FuncPtr;	
 struct __block_descriptor_withcopydispose* __descriptor;	
 struct {
 void* __isa;	
 void* __forwarding;	
 int __flags;	
 int __size;	
-xnuupcalls_xnuupcalls_sync__completion_s cmp;	
+xnuupcalls_xnuupcalls_remove__completion_s cmp;	
 }
 * cmp;	
 }

```
#### feth_ipsec_state

```c
struct feth_ipsec_state {
  errno_t(void *);
  *fis_flush;
  void *fis_kern_ctx;
  _Bool fis_disabled;
  _Bool fis_torn_down;
}

```
#### __block_literal_258

```diff

 void* __isa;	
 int __flags;	
 int __reserved;	
- tb_error_t (xnuupcalls_xnuupcalls_create__result_s);* __FuncPtr;	
+ tb_error_t (xnuupcalls_xnuupcalls_close__result_s);* __FuncPtr;	
 struct __block_descriptor_withcopydispose* __descriptor;	
 struct {
 void* __isa;	
 void* __forwarding;	
 int __flags;	
 int __size;	
-xnuupcalls_xnuupcalls_create__completion_s cmp;	
+xnuupcalls_xnuupcalls_close__completion_s cmp;	
 }
 * cmp;	
 }

```
#### __block_literal_284

```diff

 void* __isa;	
 int __flags;	
 int __reserved;	
- tb_error_t (xnuupcalls_xnuupcalls_ane_workend__result_s);* __FuncPtr;	
+ tb_error_t (xnuupcalls_xnuupcalls_ane_workbegin__result_s);* __FuncPtr;	
 struct __block_descriptor_withcopydispose* __descriptor;	
 struct {
 void* __isa;	
 void* __forwarding;	
 int __flags;	
 int __size;	
-xnuupcalls_xnuupcalls_ane_workend__completion_s cmp;	
+xnuupcalls_xnuupcalls_ane_workbegin__completion_s cmp;	
 }
 * cmp;	
 }

```
#### __block_literal_194

```diff

 void* __isa;	
 int __flags;	
 int __reserved;	
- void (size_t, const uint8_t);* __FuncPtr;	
+ void (size_t, const stackshottypes_textsegment_s*);* __FuncPtr;	
 struct __block_descriptor* __descriptor;	
 }
 * block;	
-const u8_v_s* val;	
+const stackshottypes_textsegment_v_s* val;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.149

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.149 {
-struct in_ifaddr* ptr;	
-struct in_ifaddr* ub;	
-struct in_ifaddr* lb;	
+struct __kern_quantum* ptr;	
+struct __kern_quantum* ub;	
+struct __kern_quantum* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.156

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.156 {
-struct netif_qstats* ptr;	
-struct netif_qstats* ub;	
-struct netif_qstats* lb;	
+struct netif_queue* ptr;	
+struct netif_queue* ub;	
+struct netif_queue* lb;	
 }

```
#### __bounds_safety::wide_ptr.indexable.65

```diff

 struct __bounds_safety::wide_ptr.indexable.65 {
-void* ptr;	
-void* ub;	
+char* ptr;	
+char* ub;	
 }

```
#### necp_policy_result_socket_scoped

```c
struct necp_policy_result_socket_scoped {
  char      interface_name[24];
  u_int32_t result_flags;
}

```
#### __block_literal_270

```diff

 void* __isa;	
 int __flags;	
 int __reserved;	
- tb_error_t (xnuupcalls_xnuupcalls_timer_register__result_s);* __FuncPtr;	
+ tb_error_t (xnuupcalls_xnuupcalls_irq_disable__result_s);* __FuncPtr;	
 struct __block_descriptor_withcopydispose* __descriptor;	
 struct {
 void* __isa;	
 void* __forwarding;	
 int __flags;	
 int __size;	
-xnuupcalls_xnuupcalls_timer_register__completion_s cmp;	
+xnuupcalls_xnuupcalls_irq_disable__completion_s cmp;	
 }
 * cmp;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.271

```c
struct __bounds_safety::wide_ptr.bidi_indexable.271 {
  nstat_tcp_descriptor *ptr;
  nstat_tcp_descriptor *ub;
  nstat_tcp_descriptor *lb;
}

```
#### __block_literal_281

```diff

 void* __isa;	
 int __flags;	
 int __reserved;	
- tb_error_t (xnuupcalls_xnuupcalls_ane_setpowerstate__result_s);* __FuncPtr;	
+ tb_error_t (xnuupcalls_xnuupcalls_mapper_deactivate__result_s);* __FuncPtr;	
 struct __block_descriptor_withcopydispose* __descriptor;	
 struct {
 void* __isa;	
 void* __forwarding;	
 int __flags;	
 int __size;	
-xnuupcalls_xnuupcalls_ane_setpowerstate__completion_s cmp;	
+xnuupcalls_xnuupcalls_mapper_deactivate__completion_s cmp;	
 }
 * cmp;	
 }

```
#### __bounds_safety::wide_ptr.indexable.186

```c
struct __bounds_safety::wide_ptr.indexable.186 {
  struct nstat_msg_sysinfo_counts *ptr;
  struct nstat_msg_sysinfo_counts *ub;
}

```
#### __bounds_safety::wide_ptr.indexable.136

```c
struct __bounds_safety::wide_ptr.indexable.136 {
  void *ptr;
  void *ub;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.242

```c
struct __bounds_safety::wide_ptr.bidi_indexable.242 {
  struct nstat_counts *ptr;
  struct nstat_counts *ub;
  struct nstat_counts *lb;
}

```
#### __bounds_safety::wide_ptr.indexable.94

```c
struct __bounds_safety::wide_ptr.indexable.94 {
  struct ip *ptr;
  struct ip *ub;
}

```
#### __block_literal_278

```diff

 void* __isa;	
 int __flags;	
 int __reserved;	
- tb_error_t (xnuupcalls_xnuupcalls_async_notification_signal__result_s);* __FuncPtr;	
+ tb_error_t (xnuupcalls_xnuupcalls_unlock_wl__result_s);* __FuncPtr;	
 struct __block_descriptor_withcopydispose* __descriptor;	
 struct {
 void* __isa;	
 void* __forwarding;	
 int __flags;	
 int __size;	
-xnuupcalls_xnuupcalls_async_notification_signal__completion_s cmp;	
+xnuupcalls_xnuupcalls_unlock_wl__completion_s cmp;	
 }
 * cmp;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.140

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.140 {
-struct __kern_packet** ptr;	
-struct __kern_packet** ub;	
-struct __kern_packet** lb;	
+struct mbuf* ptr;	
+struct mbuf* ub;	
+struct mbuf* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.162

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.162 {
-struct sadb_sastat* ptr;	
-struct sadb_sastat* ub;	
-struct sadb_sastat* lb;	
+struct sadb_session_id* ptr;	
+struct sadb_session_id* ub;	
+struct sadb_session_id* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.127

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.127 {
-struct __kern_packet* ptr;	
-struct __kern_packet* ub;	
-struct __kern_packet* lb;	
+struct timeval* ptr;	
+struct timeval* ub;	
+struct timeval* lb;	
 }

```
#### __block_literal_366

```c
struct __block_literal_366 {
  void *__isa;
  int   __flags;
  int   __reserved;
  tb_error_t();
  *__FuncPtr;
  struct __block_descriptor *__descriptor;
  uint64_t                   count;
  tb_message_t               msg;
}

```
#### __block_literal_290

```diff

 void* __isa;	
 int __flags;	
 int __reserved;	
- tb_error_t (xnuupcalls_xnuupcalls_conclave_stop__result_s);* __FuncPtr;	
+ tb_error_t (xnuupcalls_xnuupcalls_conclave_suspend__result_s);* __FuncPtr;	
 struct __block_descriptor_withcopydispose* __descriptor;	
 struct {
 void* __isa;	
 void* __forwarding;	
 int __flags;	
 int __size;	
-xnuupcalls_xnuupcalls_conclave_stop__completion_s cmp;	
+xnuupcalls_xnuupcalls_conclave_suspend__completion_s cmp;	
 }
 * cmp;	
 }

```
#### thread

```diff

  ;	
 int32_t user_stop_count;	
 int32_t legacy_user_stop_count;	
+_Bool th_vm_faults_disabled;	
+_Bool recover;	
 natural_t ith_assertions;	
 circle_queue_head_t ith_messages;	
 mach_port_t ith_kernel_reply_port;	
-_Bool th_vm_faults_disabled;	
-_Bool recover;	
+uint64_t t_page_free_count;	
 queue_chain_t threads;	
 queue_chain_t task_threads;	
 struct thread_ro* t_tro;	

```
#### __bounds_safety::wide_ptr.indexable.251

```c
struct __bounds_safety::wide_ptr.indexable.251 {
  struct necp_client_add_flow *ptr;
  struct necp_client_add_flow *ub;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.169

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.169 {
-struct nx_qset_info* ptr;	
-struct nx_qset_info* ub;	
-struct nx_qset_info* lb;	
+struct __kern_slot_desc* ptr;	
+struct __kern_slot_desc* ub;	
+struct __kern_slot_desc* lb;	
 }

```
#### cfil_sign_parameters

```diff

 struct cfil_sign_parameters {
 struct cfil_crypto_state* csp_state;	
 struct cfil_crypto_data* csp_data;	
-struct __bounds_safety::wide_ptr.indexable.65 csp_signature;	
+struct __bounds_safety::wide_ptr.indexable.67 csp_signature;	
 uint32_t* csp_signature_size;	
 }

```
#### __bounds_safety::wide_ptr.indexable.193

```c
struct __bounds_safety::wide_ptr.indexable.193 {
  struct nstat_msg_src_details *ptr;
  struct nstat_msg_src_details *ub;
}

```
#### __block_literal_276

```diff

 void* __isa;	
 int __flags;	
 int __reserved;	
- tb_error_t (xnuupcalls_xnuupcalls_lock_wl__result_s);* __FuncPtr;	
+ tb_error_t (xnuupcalls_xnuupcalls_timer_cancel_timeout__result_s);* __FuncPtr;	
 struct __block_descriptor_withcopydispose* __descriptor;	
 struct {
 void* __isa;	
 void* __forwarding;	
 int __flags;	
 int __size;	
-xnuupcalls_xnuupcalls_lock_wl__completion_s cmp;	
+xnuupcalls_xnuupcalls_timer_cancel_timeout__completion_s cmp;	
 }
 * cmp;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.205

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.205 {
-struct sk_stats_flow* ptr;	
-struct sk_stats_flow* ub;	
-struct sk_stats_flow* lb;	
+struct aop_quic_info* ptr;	
+struct aop_quic_info* ub;	
+struct aop_quic_info* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.225

```c
struct __bounds_safety::wide_ptr.bidi_indexable.225 {
  struct necp_client_observer_update *ptr;
  struct necp_client_observer_update *ub;
  struct necp_client_observer_update *lb;
}

```
