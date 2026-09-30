## KDKs

- `KDK_15.0_24A5264n.kdk/System/Library/Kernels/kernel.release.t6031`
- `KDK_15.0_24A5279h.kdk/System/Library/Kernels/kernel.release.t6031`

#### turnstile

```diff

 struct turnstile* sle_next;	
 }
  ts_free_elm;	
-struct mpsc_queue_chain ts_deallocate_link;	
 }
  ;	
 struct priority_queue_sched_max ts_inheritor_queue;	

```
#### recount_processor

```diff

 struct recount_processor {
 struct recount_snap rpr_snap;	
 struct recount_track rpr_active;	
-struct recount_snap rpr_interrupt_snap;	
-uint64_t rpr_interrupt_time_mach;	
+uint64_t rpr_interrupt_duration_mach;	
+uint64_t rpr_last_interrupt_enter_time_mach;	
+uint64_t rpr_last_interrupt_leave_time_mach;	
 uint64_t rpr_idle_time_mach;	
 uint64_t rpr_state_last_abs_time;	
 uint8_t rpr_cpu_kind_index;	

```
#### machine_thread

```diff

 struct perfcontrol_state perfctrl_state;	
 uint64_t aprr_shadow_mask_el0_value;	
 uint64_t jitbox_ctl_el0;	
-vm_offset_t pcpu_data_base;	
+union {
+long pcpu_data_base_and_cpu_number;	
+const uint16_t cpu_number;	
+}
+ ;	
 struct cpu_data* CpuDatap;	
 unsigned int preemption_count;	
 uint16_t exception_trace_code;	

```
#### recount_thread

```diff

 struct recount_thread {
 struct recount_track* rth_lifetime;	
-uint64_t rth_interrupt_time_mach;	
+uint64_t rth_interrupt_duration_mach;	
 recount_level_t rth_current_level;	
 }

```
#### cpu_data

```diff

 struct cpu_data {
-short cpu_number;	
+unsigned short cpu_number;	
 cpu_flags_t cpu_flags;	
 int cpu_type;	
 int cpu_subtype;	
 int cpu_threadtype;	
 void* __ptrauth(DA, true, 0xe94d) istackptr;	
 vm_offset_t intstack_top;	
+void* __ptrauth(DA, true, 0x467) excepstackptr;	
 vm_offset_t excepstack_top;	
 thread_t cpu_active_thread;	
 vm_offset_t cpu_active_stack;	

```
#### smr_hash_iterator

```diff

 struct smr_hash_iterator {
+struct smr_hash* smrh;	
 struct smrq_slist_head* hd_next;	
 struct smrq_slist_head* hd_last;	
 __smrq_slink_t* prev;	

```
#### _image4_dlxk_interface

```diff

 _image4_environment_flash_dlxk_t dlxk_environment_flash;	
 _image4_coprocessor_resolve_from_manifest_dlxk_t dlxk_coprocessor_resolve_from_manifest;	
 _image4_coprocessor_bootpc_dlxk_t dlxk_coprocessor_bootpc;	
+_image4_coprocessor_vma2_dlxk_t dlxk_coprocessor_vma2;	
+_image4_coprocessor_vma3_dlxk_t dlxk_coprocessor_vma3;	
+_image4_trust_set_result_buffer_dlxk_t dlxk_trust_set_result_buffer;	
 }

```
#### _image4_trust_storage

```diff

 struct _image4_trust_storage {
-uint8_t __opaque[1920];	
+uint8_t __opaque[2048];	
 }

```
#### _select

```diff

 struct _select {
-u_int32_t* ibits;	
-u_int32_t* obits;	
+u_int32_t* __ptrauth(DA, true, 0x5353) ibits;	
+u_int32_t* __ptrauth(DA, true, 0x52bc) obits;	
 uint nbytes;	
 }

```
#### xbpf_d

```diff

 uint8_t bd_exthdr;	
 uint8_t bd_trunc;	
 uint8_t bd_pkthdrv2;	
-uint8_t bd_pad;	
+uint8_t bd_batch_write;	
+uint8_t bd_divert_in;	
+uint8_t bd_padding;	
 uint64_t bd_rcount;	
 uint64_t bd_dcount;	
 uint64_t bd_fcount;	

```
#### __kern_channel_ring

```diff

 lck_grp_t* ckr_qlock_group;	
 lck_grp_t* ckr_slock_group;	
 char ckr_name[64];	
+uint64_t ckr_rx_dequeue_ts;	
+uint64_t ckr_rx_enqueue_ts;	
 }

```
#### netif_stats

```diff

 struct netif_stats {
-uint64_t _arr[135];	
+uint64_t _arr[136];	
 }

```
#### nx_flowswitch

```diff

 uint64_t fsw_reap_last;	
 uint64_t fsw_drain_channel_chk_last;	
 uint64_t fsw_drain_netif_chk_last;	
+uint64_t fsw_rx_stall_chk_last;	
 lck_mtx_t fsw_linger_lock;	
 struct flow_entry_linger_head fsw_linger_head;	
 uint32_t fsw_linger_cnt;	

```
#### fsw_stats

```diff

 struct fsw_stats {
-uint64_t _arr[118];	
+uint64_t _arr[119];	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.81

```diff

 struct __firebloom::wide_ptr.bidi_indexable.81 {
-struct event* ptr;	
-struct event* ub;	
-struct event* lb;	
+struct kern_event_msg* ptr;	
+struct kern_event_msg* ub;	
+struct kern_event_msg* lb;	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.77

```diff

 struct __firebloom::wide_ptr.bidi_indexable.77 {
-struct icmp6_hdr* ptr;	
-struct icmp6_hdr* ub;	
-struct icmp6_hdr* lb;	
+struct ether_header* ptr;	
+struct ether_header* ub;	
+struct ether_header* lb;	
 }

```
#### rtstat_64

```c
struct rtstat_64 {
  uint64_t rts_badredirect;
  uint64_t rts_dynamic;
  uint64_t rts_newgateway;
  uint64_t rts_unreach;
  uint64_t rts_wildcard;
  uint64_t rts_badrtgwroute;
}

```
#### __firebloom::wide_ptr.bidi_indexable.84

```diff

 struct __firebloom::wide_ptr.bidi_indexable.84 {
-struct xtcpcb_n* ptr;	
-struct xtcpcb_n* ub;	
-struct xtcpcb_n* lb;	
+struct if_msghdr2* ptr;	
+struct if_msghdr2* ub;	
+struct if_msghdr2* lb;	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.86

```diff

 struct __firebloom::wide_ptr.bidi_indexable.86 {
-struct udphdr* ptr;	
-struct udphdr* ub;	
-struct udphdr* lb;	
+struct ifma_msghdr2* ptr;	
+struct ifma_msghdr2* ub;	
+struct ifma_msghdr2* lb;	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.78

```diff

 struct __firebloom::wide_ptr.bidi_indexable.78 {
-struct sockaddr* ptr;	
-struct sockaddr* ub;	
-struct sockaddr* lb;	
+struct in6_ifaddr* ptr;	
+struct in6_ifaddr* ub;	
+struct in6_ifaddr* lb;	
 }

```
#### __firebloom::wide_ptr.indexable.58

```diff

 struct __firebloom::wide_ptr.indexable.58 {
-void* ptr;	
-void* ub;	
+uint8_t* ptr;	
+uint8_t* ub;	
 }

```
#### walkarg

```diff

 int w_tmemsize;	
 int w_op;	
 int w_arg;	
-caddr_t w_tmem;	
+__firebloom::sized_by::w_tmemsize w_tmem;	
 struct sysctl_req* w_req;	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.76

```diff

 struct __firebloom::wide_ptr.bidi_indexable.76 {
-struct kalloc_heap* ptr;	
-struct kalloc_heap* ub;	
-struct kalloc_heap* lb;	
+struct ifaddr* ptr;	
+struct ifaddr* ub;	
+struct ifaddr* lb;	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.89

```diff

 struct __firebloom::wide_ptr.bidi_indexable.89 {
-struct m_tag* ptr;	
-struct m_tag* ub;	
-struct m_tag* lb;	
+struct protosw* ptr;	
+struct protosw* ub;	
+struct protosw* lb;	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.73

```diff

 struct __firebloom::wide_ptr.bidi_indexable.73 {
-const uint8_t* ptr;	
-const uint8_t* ub;	
-const uint8_t* lb;	
+nstat_flow_data* ptr;	
+nstat_flow_data* ub;	
+nstat_flow_data* lb;	
 }

```
#### __firebloom::wide_ptr.indexable.120

```diff

 struct __firebloom::wide_ptr.indexable.120 {
-struct fileglob** ptr;	
-struct fileglob** ub;	
+uint8_t* ptr;	
+uint8_t* ub;	
 }

```
#### __firebloom::wide_ptr.indexable.83

```c
struct __firebloom::wide_ptr.indexable .83 {
  const void *ptr;
  const void *ub;
}

```
#### __firebloom::wide_ptr.bidi_indexable.126

```diff

 struct __firebloom::wide_ptr.bidi_indexable.126 {
-struct socket* ptr;	
-struct socket* ub;	
-struct socket* lb;	
+struct kern_nexus* ptr;	
+struct kern_nexus* ub;	
+struct kern_nexus* lb;	
 }

```
#### necp_kernel_socket_policy

```diff

 u_int32_t cond_bound_interface_flags;	
 u_int32_t cond_bound_interface_eflags;	
 u_int32_t cond_bound_interface_xflags;	
+u_int8_t cond_local_networks_flags;	
 necp_kernel_policy_result result;	
 necp_kernel_policy_result_parameter result_parameter;	
 }

```
#### necp_kernel_ip_output_policy

```diff

 u_int32_t cond_bound_interface_flags;	
 u_int32_t cond_bound_interface_eflags;	
 u_int32_t cond_bound_interface_xflags;	
+u_int8_t cond_local_networks_flags;	
 necp_kernel_policy_result result;	
 necp_kernel_policy_result_parameter result_parameter;	
 }

```
#### necp_client_update

```diff

  chain;	
 uuid_t client_id;	
 size_t update_length;	
-__firebloom::counted_by::update_length update;	
+__firebloom::sized_by::update_length update;	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.121

```diff

 struct __firebloom::wide_ptr.bidi_indexable.121 {
-struct inpcb* ptr;	
-struct inpcb* ub;	
-struct inpcb* lb;	
+struct ip_moptions_dbg* ptr;	
+struct ip_moptions_dbg* ub;	
+struct ip_moptions_dbg* lb;	
 }

```
#### mptses

```diff

 sae_associd_t mpte_associd;	
 sae_connid_t mpte_connid_last;	
 uint64_t mpte_time_target;	
-thread_call_t mpte_time_thread;	
-thread_call_t mpte_stop_urgency;	
+struct thread_call* mpte_time_thread;	
+struct thread_call* mpte_stop_urgency;	
 uint32_t mpte_last_cellicon_set;	
 uint32_t mpte_cellicon_increments;	
 union {

```
#### __firebloom::wide_ptr.indexable.102

```c
struct __firebloom::wide_ptr.indexable .102 {
  char *ptr;
  char *ub;
}

```
#### __firebloom::wide_ptr.indexable.105

```c
struct __firebloom::wide_ptr.indexable .105 {
  void *ptr;
  void *ub;
}

```
#### __firebloom::wide_ptr.indexable.104

```c
struct __firebloom::wide_ptr.indexable .104 {
  struct icmp6_nodeinfo *ptr;
  struct icmp6_nodeinfo *ub;
}

```
#### __firebloom::wide_ptr.indexable.24

```c
struct __firebloom::wide_ptr.indexable .24 {
  char *ptr;
  char *ub;
}

```
#### __firebloom::wide_ptr.indexable.53

```c
struct __firebloom::wide_ptr.indexable .53 {
  uint8_t *ptr;
  uint8_t *ub;
}

```
#### __firebloom::wide_ptr.indexable.96

```c
struct __firebloom::wide_ptr.indexable .96 {
  char *ptr;
  char *ub;
}

```
#### __firebloom::wide_ptr.indexable.95

```c
struct __firebloom::wide_ptr.indexable .95 {
  void *ptr;
  void *ub;
}

```
#### __firebloom::wide_ptr.indexable.129

```c
struct __firebloom::wide_ptr.indexable .129 {
  void *ptr;
  void *ub;
}

```
#### __firebloom::wide_ptr.indexable.80

```diff

 struct __firebloom::wide_ptr.indexable.80 {
-const void* ptr;	
-const void* ub;	
+void* ptr;	
+void* ub;	
 }

```
#### __firebloom::wide_ptr.indexable.119

```c
struct __firebloom::wide_ptr.indexable .119 {
  struct fileglob **ptr;
  struct fileglob **ub;
}

```
#### sk_tag_spec

```diff

 struct sk_tag_spec {
-kern_allocation_name_t* skt_var;	
+kern_allocation_name** skt_var;	
 const char* skt_name;	
 }

```
#### skmem_bufctl_audit

```diff

 struct skmem_bufctl* sle_next;	
 }
  bc_link;	
-void* bc_addr;	
+__firebloom::sized_by::bc_lim bc_addr;	
 void* bc_addrm;	
 struct skmem_slab* bc_slab;	
+uint32_t bc_lim;	
 uint32_t bc_flags;	
 uint32_t bc_idx;	
 volatile uint32_t bc_usecnt;	

```
#### __firebloom::wide_ptr.indexable.57

```diff

 struct __firebloom::wide_ptr.indexable.57 {
-char* ptr;	
-char* ub;	
+void* ptr;	
+void* ub;	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.153

```diff

 struct __firebloom::wide_ptr.bidi_indexable.153 {
-struct nx_llink_info_req* ptr;	
-struct nx_llink_info_req* ub;	
-struct nx_llink_info_req* lb;	
+const struct __kern_packet** ptr;	
+const struct __kern_packet** ub;	
+const struct __kern_packet** lb;	
 }

```
#### __firebloom::wide_ptr.indexable.3

```c
struct __firebloom::wide_ptr.indexable .3 {
  volatile struct ip6_hdr *ptr;
  volatile struct ip6_hdr *ub;
}

```
#### __firebloom::wide_ptr.indexable.22

```c
struct __firebloom::wide_ptr.indexable .22 {
  void *ptr;
  void *ub;
}

```
#### IOPMAOTAnalytics

```c
struct IOPMAOTAnalytics {
  uint32_t possibleCount;
  uint32_t confirmedPossibleCount;
  uint32_t rejectedPossibleCount;
  uint32_t expiredPossibleCount;
}

```
#### _ca_event_aot_analytics

```c
struct _ca_event_aot_analytics {
  unsigned long long possible_count;
  unsigned long long confirmed_possible_count;
  unsigned long long rejected_possible_count;
  unsigned long long expired_possible_count;
}

```
