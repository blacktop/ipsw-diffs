## KDKs

- `KDK_14.5_23F79.kdk/System/Library/Kernels/kernel.release.t6031`
- `KDK_15.0_24A5264n.kdk/System/Library/Kernels/kernel.release.t6031`

#### arm_saved_state64

```diff

 uint32_t cpsr;	
 uint32_t aspsr;	
 uint64_t far;	
-uint32_t esr;	
-uint32_t exception;	
+uint64_t esr;	
 uint64_t jophash;	
 }

```
#### ipc_port

```diff

  ;	
 struct ipc_port* ip_nsrequest;	
 ipc_port_request_table_t __ptrauth(DA, true, 0xb9dc) ip_requests;	
-union {
-struct ipc_kmsg* __ptrauth(DA, true, 0x1a35) ip_premsg;	
 struct turnstile* ip_send_turnstile;	
-}
- ;	
 mach_vm_address_t ip_context;	
 natural_t ip_impcount;	
 mach_port_mscount_t ip_mscount;	

```
#### ipc_mqueue

```diff

 uint32_t imq_context;	
 union {
 struct klist imq_klist;	
-struct knote* imq_inheritor_knote;	
-struct turnstile* imq_inheritor_turnstile;	
-thread_t imq_inheritor_thread_ref;	
-thread_t imq_srp_owner_thread;	
+struct knote* __ptrauth(DA, true, 0xf8f2) imq_inheritor_knote;	
+struct turnstile* __ptrauth(DA, true, 0xf7fc) imq_inheritor_turnstile;	
+thread_t __ptrauth(DA, true, 0x2a72) imq_inheritor_thread_ref;	
+thread_t __ptrauth(DA, true, 0xf4d6) imq_srp_owner_thread;	
 }
  ;	
 }

```
#### thread

```diff

 uint64_t same_pri_latency;	
 uint64_t workq_quantum_deadline;	
 struct thread_group* thread_group;	
-sched_group_t sched_group;	
 processor_t bound_processor;	
 processor_t last_processor;	
 processor_t chosen_processor;	

 task_watch_t* taskwatch;	
 union {
 struct {
+mach_msg_recv_bufs_t recv_bufs;	
+mach_msg_option64_t option;	
+ipc_object_t object;	
 mach_msg_return_t state;	
 mach_port_seqno_t seqno;	
-ipc_object_t object;	
-mach_vm_address_t msg_addr;	
-mach_vm_address_t aux_addr;	
-mach_msg_size_t max_msize;	
-mach_msg_size_t max_asize;	
 mach_msg_size_t msize;	
 mach_msg_size_t asize;	
-mach_msg_option64_t option;	
 mach_port_name_t receiver_name;	
 union {
 struct ipc_kmsg* __ptrauth(DA, true, 0x33ff) kmsg;	

 natural_t ith_assertions;	
 circle_queue_head_t ith_messages;	
 mach_port_t ith_kernel_reply_port;	
+_Bool th_vm_faults_disabled;	
 vm_offset_t recover;	
 queue_chain_t threads;	
 queue_chain_t task_threads;	

```
#### processor

```diff

 perfcontrol_class_t current_perfctl_class;	
 pset_cluster_type_t current_recommended_pset_type;	
 thread_urgency_t current_urgency;	
-int runq_bound_count;	
 struct thread_group* current_thread_group;	
 int starting_pri;	
 int cpu_id;	

 uint64_t kperf_last_sample_time;	
 uint64_t deadline;	
 _Bool first_timeslice;	
-_Bool processor_offlined;	
 _Bool must_idle;	
 _Bool next_idle_short;	
 _Bool running_timers_active;	

 struct ipc_port* processor_self;	
 processor_t processor_list;	
 uint64_t timer_call_ttd;	
-simple_lock_data_t start_state_lock;	
 processor_reason_t last_startup_reason;	
 processor_reason_t last_shutdown_reason;	
 processor_reason_t last_recommend_reason;	
 processor_reason_t last_derecommend_reason;	
+_Bool processor_instartup;	
+_Bool processor_booted;	
 _Bool shutdown_temporary;	
-_Bool shutdown_locked;	
+_Bool processor_online;	
+_Bool processor_inshutdown;	
+processor_offline_state_t processor_offline_state;	
 }

```
#### processor_set

```diff

 int last_chosen;	
 uint64_t load_average;	
 uint64_t pset_load_average[6];	
+uint32_t pset_runnable_depth[6];	
 uint64_t pset_load_last_update;	
 cpumap_t cpu_bitmask;	
 cpumap_t recommended_bitmask;	

 struct rt_queue rt_runq;	
 uint64_t stealable_rt_threads_earliest_deadline;	
 struct sched_clutch_root pset_clutch_root;	
-int pset_runq_bound_count;	
 cpumap_t pending_AST_URGENT_cpu_mask;	
 cpumap_t pending_AST_PREEMPT_cpu_mask;	
 cpumap_t pending_deferred_AST_cpu_mask;	

```
#### pset_node

```diff

 pset_map_t pset_idle_primary_map;	
 pset_map_t pset_non_rt_map;	
 pset_map_t pset_non_rt_primary_map;	
+pset_map_t pset_recommended_map;	
 }

```
#### machine_thread

```diff

 struct machine_thread {
+uint32_t arm_machine_flags;	
 arm_context_t* contextData;	
 arm_saved_state_t* __ptrauth(DA, true, 0x1e91) upcb;	
-arm_neon_saved_state_t* uNeon;	
+arm_neon_saved_state_t* __ptrauth(DA, true, 0x356a) uNeon;	
 arm_saved_state_t* kpcb;	
 union {
 arm_state_hdr_t* umatrix_hdr;	

 uint64_t recover_far;	
 arm_debug_state_t* DebugData;	
 vm_address_t cthread_self;	
-uint32_t recover_esr;	
-uint32_t arm_machine_flags;	
+uint64_t recover_esr;	
 void* __ptrauth(DA, true, 0x6d42) kstackptr;	
 struct perfcontrol_state perfctrl_state;	
 uint64_t aprr_shadow_mask_el0_value;	

 struct cpu_data* CpuDatap;	
 unsigned int preemption_count;	
 uint16_t exception_trace_code;	
-uint8_t vcpu_mode;	
 _Bool vcpu_dirtied_matrix_context;	
 uint64_t rop_pid;	
 uint64_t jop_pid;	

```
#### ipc_kmsg

```diff

 struct ipc_kmsg {
 queue_chain_t ikm_link;	
-union {
-ipc_port_t __ptrauth(DA, true, 0xf51f) ikm_prealloc;	
-void* __ptrauth(DA, true, 0x9c97) ikm_udata;	
-}
- ;	
 ipc_port_t __ptrauth(DA, true, 0xc442) ikm_voucher_port;	
 struct ipc_importance_elem* ikm_importance;	
 queue_chain_t ikm_inheritance;	
-mach_msg_size_t ikm_aux_size;	
+uint16_t ikm_aux_size;	
+ipc_kmsg_keep_alive_t ikm_keep_alive;	
+uint8_t __ikm_padding;	
 uint32_t ikm_ppriority;	
+uint32_t ikm_signature;	
+ipc_object_copyin_flags_t ikm_flags;	
+mach_msg_qos_t ikm_qos_override;	
+mach_msg_type_name_t ikm_voucher_type;	
+ipc_kmsg_type_t ikm_type;	
 union {
+uint32_t ikm_big_data[48];	
 struct {
-uint32_t ikm_sig_partial;	
-uint32_t ikm_sig_full;	
+uint32_t ikm_small_data[42];	
+void* __ptrauth(DA, true, 0x289d) ikm_kdata;	
+void* __ptrauth(DA, true, 0x9c97) ikm_udata;	
+mach_msg_size_t ikm_kdata_size;	
+mach_msg_size_t ikm_udata_size;	
 }
  ;	
-uint64_t ikm_signature;	
 }
  ;	
-ipc_object_copyin_flags_t ikm_flags;	
-mach_msg_qos_t ikm_qos_override;	
-mach_msg_type_name_t ikm_voucher_type;	
-ipc_kmsg_type_t ikm_type;	
-mach_msg_size_t ikm_udata_size;	
 }

```
#### task

```diff

 queue_chain_t tasks;	
 struct task_watchports* watchports;	
 turnstile_inheritor_t returnwait_inheritor;	
-sched_group_t sched_group;	
 queue_head_t threads;	
 struct restartable_ranges* t_rr_ranges;	
 processor_set_t pset_hint;	

 struct ipc_port* __ptrauth(DA, true, 0x4447) itk_settable_self;	
 struct ipc_port* __ptrauth(DA, true, 0x58ef) itk_self;	
 struct exception_action exc_actions[14];	
+struct hardened_exception_action hardened_exception_action;	
 struct ipc_port* __ptrauth(DA, true, 0xbb51) itk_host;	
 struct ipc_port* __ptrauth(DA, true, 0xe868) itk_bootstrap;	
 struct ipc_port* __ptrauth(DA, true, 0xb8b1) itk_debug_control;	

 boolean_t jitbox_enabled;	
 arm64_uexc_region_t uexc;	
 _Bool preserve_x18;	
+_Bool uses_1ghz_timebase;	
 counter_t faults;	
 counter_t pageins;	
 counter_t cow_faults;	

 vm_extmod_statistics_data_t extmod_statistics;	
 struct task_requested_policy requested_policy;	
 struct task_effective_policy effective_policy;	
+struct task_pend_token pended_coalition_changes;	
 uint32_t low_mem_notified_warn;	
 uint32_t low_mem_notified_critical;	
 uint32_t purged_memory_warn;	

 unsigned int task_extra_footprint_limit;	
 unsigned int task_ios13extended_footprint_limit;	
 unsigned int task_region_footprint;	
+unsigned int task_region_info_flags;	
 unsigned int task_has_crossed_thread_limit;	
 unsigned int task_rr_in_flight;	
 coalition_t coalition[2];	

```
#### exception_action

```diff

 thread_state_flavor_t flavor;	
 exception_behavior_t behavior;	
 boolean_t privileged;	
+boolean_t hardened;	
 struct label* label;	
 }

```
#### hardened_exception_action

```c
struct hardened_exception_action {
  struct exception_action ea;
  uint32_t                signed_pc_key;
  exception_mask_t        exception;
}

```
#### kcdata_descriptor

```diff

 mach_vm_address_t kcd_addr_end;	
 struct kcdata_compress_descriptor kcd_comp_d;	
 uint32_t kcd_endalloced;	
+ struct kcdata_descriptor* (struct kcdata_descriptor*, size_t);* kcd_alloc_callback;	
 }

```
#### task_effective_policy

```diff

 uint64_t tep_qos_clamp;	
 uint64_t tep_qos_ceiling;	
 uint64_t tep_adaptive_bg;	
+uint64_t tep_coalition_bg;	
 uint64_t tep_reserved;	
 }

```
#### task_pend_token

```diff

 struct task_pend_token {
+union {
+struct {
 uint32_t tpt_update_sockets;	
 uint32_t tpt_update_timers;	
 uint32_t tpt_update_watchers;	

 uint32_t tpt_update_turnstile;	
 uint32_t tpt_update_tg_app_flag;	
 uint32_t tpt_update_game_mode;	
+uint32_t tpt_update_carplay_mode;	
+}
+ ;	
+uint32_t tpt_value;	
+}
+ ;	
 }

```
#### host

```diff

 struct host {
 lck_mtx_t lock;	
-ipc_port_t __ptrauth(DA, true, 0x9b8d) special[35];	
+ipc_port_t __ptrauth(DA, true, 0x9b8d) special[36];	
 struct exception_action exc_actions[14];	
 }

```
#### stackshot_context

```diff

 struct stackshot_context {
-int pid;	
-uint64_t trace_flags;	
-_Bool include_drivers;	
+struct kdp_snapshot_args sc_args;	
+int sc_calling_cpuid;	
+int sc_main_cpuid;	
+_Bool sc_enable_faulting;	
+uint64_t sc_microsecs;	
+_Bool sc_panic_stackshot;	
+size_t sc_min_kcdata_size;	
+_Bool sc_is_singlethreaded;	
+stackshot_state_t sc_state;	
+kern_return_t sc_retval;	
+uint32_t sc_cpus_working;	
+linked_kcdata_descriptor_t sc_pretask_kcdata;	
+linked_kcdata_descriptor_t sc_posttask_kcdata;	
+kcdata_descriptor_t sc_finalized_kcdata;	
+struct stackshot_buffer sc_buffers[6];	
+size_t sc_num_buffers;	
+struct stackshot_workqueue sc_workqueues[2];	
+struct stackshot_duration_v2 sc_duration;	
+uint32_t sc_bytes_traced;	
+uint32_t sc_bytes_uncompressed;	
 }

```
#### kdp_snapshot_args

```c
struct kdp_snapshot_args {
  int                       pid;
  void                     *buffer;
  struct kcdata_descriptor *descriptor;
  uint32_t                  buffer_size;
  uint64_t                  flags;
  uint64_t                  since_timestamp;
  uint32_t                  pagetable_mask;
}

```
#### linked_kcdata_descriptor

```c
struct linked_kcdata_descriptor {
  struct kcdata_descriptor         kcdata;
  struct linked_kcdata_descriptor *next;
}

```
#### stackshot_buffer

```c
struct stackshot_buffer {
  void                  *ssb_ptr;
  size_t                 ssb_size;
  size_t                 ssb_used;
  struct freelist_entry *ssb_freelist;
  int                    ssb_freelist_lock;
  size_t                 ssb_overhead;
}

```
#### freelist_entry

```c
struct freelist_entry {
  struct freelist_entry *fl_next;
  size_t                 fl_size;
}

```
#### stackshot_workqueue

```c
struct stackshot_workqueue {
  uint32_t                   sswq_num_items;
  uint32_t                   sswq_cur_item;
  size_t                     sswq_capacity;
  _Bool                      sswq_populated;
  struct stackshot_workitem *sswq_items;
}

```
#### stackshot_workitem

```c
struct stackshot_workitem {
  task_t                     sswi_task;
  linked_kcdata_descriptor_t sswi_data;
  int                        sswi_idx;
}

```
#### cpu_data

```diff

 struct cpu_data {
 short cpu_number;	
-unsigned short cpu_flags;	
+cpu_flags_t cpu_flags;	
 int cpu_type;	
 int cpu_subtype;	
 int cpu_threadtype;	

 thread_t cpu_active_thread;	
 vm_offset_t cpu_active_stack;	
 cpu_id_t cpu_id;	
-volatile unsigned int cpu_signal;	
+volatile cpu_signal_t cpu_signal;	
 ast_t cpu_pending_ast;	
 cache_dispatch_t cpu_cache_dispatch;	
 uint64_t cpu_base_timebase;	

```
#### stackshot_cpu_context

```c
struct stackshot_cpu_context {
  _Bool                        scc_can_work;
  _Bool                        scc_did_work;
  linked_kcdata_descriptor_t   scc_kcdata_head;
  linked_kcdata_descriptor_t   scc_kcdata_tail;
  uintptr_t                   *scc_stack_buffer;
  struct stackshot_fault_stats scc_fault_stats;
}

```
#### crashinfo_jit_address_range

```c
struct crashinfo_jit_address_range {
  uint64_t start_address;
  uint64_t end_address;
}

```
#### _kernelrpc_mach_vm_allocate_trap_args

```diff

 user_addr_t addr;	
 char addr_r_[0];	
 char size_l_[0];	
-mach_vm_size_t size;	
+mach_vm_size_ut size;	
 char size_r_[0];	
 char flags_l_[0];	
 int flags;	

```
#### _kernelrpc_mach_vm_deallocate_args

```diff

 mach_port_name_t target;	
 char target_r_[4];	
 char address_l_[0];	
-mach_vm_address_t address;	
+mach_vm_address_ut address;	
 char address_r_[0];	
 char size_l_[0];	
-mach_vm_size_t size;	
+mach_vm_size_ut size;	
 char size_r_[0];	
 }

```
#### _kernelrpc_mach_vm_map_trap_args

```diff

 user_addr_t addr;	
 char addr_r_[0];	
 char size_l_[0];	
-mach_vm_size_t size;	
+mach_vm_size_ut size;	
 char size_r_[0];	
 char mask_l_[0];	
-mach_vm_offset_t mask;	
+mach_vm_offset_ut mask;	
 char mask_r_[0];	
 char flags_l_[0];	
 int flags;	
 char flags_r_[4];	
 char cur_protection_l_[0];	
-vm_prot_t cur_protection;	
+vm_prot_ut cur_protection;	
 char cur_protection_r_[4];	
 }

```
#### _exception_info

```c
struct _exception_info {
  int                        os_reason;
  int                        signal;
  exception_type_t           exception_type;
  mach_exception_data_type_t mx_code;
  mach_exception_data_type_t mx_subcode;
  struct kt_info             kt_info;
}

```
#### kt_info

```c
struct kt_info {
  int      kt_subsys;
  uint32_t kt_error;
}

```
#### coalition

```diff

 uint32_t focal_task_count;	
 uint32_t nonfocal_task_count;	
 uint32_t game_task_count;	
+uint32_t carplay_task_count;	
 uint32_t privileged;	
 uint32_t termrequested;	
 uint32_t terminated;	

```
#### i_resource_coalition

```diff

 uint64_t cpu_time_rqos[7];	
 uint64_t cpu_instructions;	
 uint64_t cpu_cycles;	
+uint64_t ane_mach_time;	
+uint64_t ane_energy_nj;	
+uint64_t gpu_energy_nj;	
+uint64_t gpu_energy_nj_billed_to_me;	
+uint64_t gpu_energy_nj_billed_to_others;	
 struct recount_coalition co_recount;	
 uint64_t task_count;	
 uint64_t dead_task_count;	

```
#### i_jetsam_coalition

```diff

 queue_head_t other;	
 struct thread_group* thread_group;	
 _Bool swap_enabled;	
+struct coalition_requested_policy c_requested_policy;	
+struct coalition_effective_policy c_effective_policy;	
 }

```
#### coalition_requested_policy

```c
struct coalition_requested_policy {
  uint64_t crp_darwinbg;
  uint64_t crp_reserved;
}

```
#### coalition_effective_policy

```c
struct coalition_effective_policy {
  uint64_t cep_darwinbg;
  uint64_t cep_reserved;
}

```
#### coalition_type

```diff

  kern_return_t (coalition_t, task_t);* remove_task;	
  kern_return_t (coalition_t, task_t, int);* set_taskrole;	
  int (coalition_t, task_t);* get_taskrole;	
- void (coalition_t, void*,  void (coalition_t, void*, task_t);*);* iterate_tasks;	
+ task_t (coalition_t, coalition_for_each_task_block_t);* iterate_tasks;	
 }

```
#### coalition_pend_token

```c
struct coalition_pend_token {
  uint32_t cpt_update_timers;
  uint32_t cpt_update_j_coal_tasks;
}

```
#### coalition_resource_usage

```diff

 uint64_t cpu_pinstructions;	
 uint64_t cpu_pcycles;	
 uint64_t conclave_mem;	
+uint64_t ane_mach_time;	
+uint64_t ane_energy_nj;	
+uint64_t phys_footprint;	
+uint64_t gpu_energy_nj;	
+uint64_t gpu_energy_nj_billed_to_me;	
+uint64_t gpu_energy_nj_billed_to_others;	
 }

```
#### __block_literal_3

```diff

 void* __isa;	
 int __flags;	
 int __reserved;	
- void ();* __FuncPtr;	
+ _Bool (task_t);* __FuncPtr;	
 struct __block_descriptor* __descriptor;	
-lck_spin_t* lock;	
 }

```
#### debugger_state

```diff

 va_list* db_panic_args;	
 void* db_panic_data_ptr;	
 unsigned long db_panic_caller;	
+const char* db_panic_initiator;	
 uint32_t db_entry_count;	
 kern_return_t db_op_return;	
 }

```
#### ext_paniclog_handle

```diff

 uint32_t max_len;	
 uint32_t used_len;	
 ext_paniclog_create_options_t options;	
+ext_paniclog_flags_t flags;	
 uint8_t active;	
 }

```
#### vm_compressor_q_lens

```c
struct vm_compressor_q_lens {
  uint32_t qcc_segments_available;
  uint32_t qcc_segment_count;
  uint32_t qcc_age_count;
  uint32_t qcc_early_swappedin_count;
  uint32_t qcc_regular_swappedin_count;
  uint32_t qcc_late_swappedin_count;
  uint32_t qcc_early_swapout_count;
  uint32_t qcc_regular_swapout_count;
  uint32_t qcc_late_swapout_count;
  uint32_t qcc_swapio_count;
  uint32_t qcc_swappedout_count;
  uint32_t qcc_swappedout_sparse_count;
  uint32_t qcc_major_count;
  uint32_t qcc_filling_count;
  uint32_t qcc_empty_count;
  uint32_t qcc_bad_count;
  uint32_t qcc_minor_count;
}

```
#### zone_security_flags

```diff

 uint16_t z_pgz_use_guards;	
 uint16_t z_submap_from_end;	
 uint16_t z_noencrypt;	
-uint16_t z_unused;	
+uint16_t z_tag;	
 zone_id_t z_sig_eq;	
 }

```
#### io_timeout_override_entry

```diff

 struct io_timeout_override_entry* rbe_parent;	
 }
  tree;	
-uintptr_t iovaddr_base;	
+uintptr_t ioaddr_base;	
 unsigned int size;	
 uint32_t read_timeout;	
 uint32_t write_timeout;	

```
#### mk_timer

```diff

 struct mk_timer {
 simple_lock_data_t lock;	
 thread_call_data_t mkt_thread_call;	
-uint32_t is_dead;	
-uint32_t is_armed;	
+_Bool is_dead;	
+_Bool is_armed;	
 int active;	
-ipc_port_t port;	
+ipc_port_t __ptrauth(DA, true, 0x82ca) port;	
+ipc_kmsg_t __ptrauth(DA, true, 0xaec9) prealloc;	
 }

```
#### ml_topology_cluster

```diff

 unsigned int num_cpus;	
 unsigned int first_cpu_id;	
 uint64_t cpu_mask;	
+unsigned int die_id;	
+unsigned int die_cluster_id;	
 vm_offset_t acc_IMPL_regs;	
 uint64_t acc_IMPL_pa;	
 uint64_t acc_IMPL_len;	

```
#### ml_topology_info

```diff

 unsigned int cluster_types;	
 unsigned int cluster_type_num_cpus[3];	
 unsigned int cluster_type_num_clusters[3];	
+unsigned int cluster_power_down;	
 }

```
#### global_powered_cores_state

```c
struct global_powered_cores_state {
  _Bool                       pcs_init_completed;
  cpumap_t                    pcs_managed_cores;
  cpumap_t                    pcs_requested_online_user;
  cpumap_t                    pcs_requested_online_clpc_user;
  cpumap_t                    pcs_requested_online_clpc_system;
  cpumap_t                    pcs_required_online_pmgr;
  cpumap_t                    pcs_required_online_system;
  int32_t                     pcs_powerdown_suspend_count;
  _Bool                       pcs_user_online_core_control;
  _Bool                       pcs_wants_kernel_sleep;
  _Bool                       pcs_in_kernel_sleep;
  struct powered_cores_state  pcs_effective;
  struct powered_cores_state  pcs_requested;
  cpumap_t                    pcs_requested_recommended_clpc;
  cpumap_t                    pcs_requested_recommended_clpc_system;
  cpumap_t                    pcs_requested_recommended_clpc_user;
  _Bool                       pcs_recommended_clpc_failsafe_active;
  _Bool                       pcs_sleep_override_recommended;
  cpumap_t                    pcs_recommended_cores;
  volatile processor_reason_t pcs_in_flight_reason;
  volatile processor_reason_t pcs_previous_reason;
}

```
#### powered_cores_state

```c
struct powered_cores_state {
  cpumap_t pcs_powerdown_recommended_cores;
  cpumap_t pcs_online_cores;
  cpumap_t pcs_tempdown_cores;
}

```
#### _task_ledger_indices

```diff

 int neural_footprint;	
 int neural_nofootprint_compressed;	
 int neural_footprint_compressed;	
+int neural_nofootprint_total;	
 int platform_idle_wakeups;	
 int interrupt_wakeups;	
 int sfi_wait_times[17];	

```
#### task_vm_info

```diff

 uint64_t limit_bytes_remaining;	
 integer_t decompressions;	
 int64_t ledger_swapins;	
+int64_t ledger_tag_neural_nofootprint_total;	
+int64_t ledger_tag_neural_nofootprint_peak;	
 }

```
#### _ca_event_thread_set_state

```c
struct _ca_event_thread_set_state {
  ca_sstr current_proc[17];
}

```
#### rusage_info_v6

```diff

 uint64_t ri_penergy_nj;	
 uint64_t ri_secure_time_in_system;	
 uint64_t ri_secure_ptime_in_system;	
-uint64_t ri_reserved[12];	
+uint64_t ri_neural_footprint;	
+uint64_t ri_lifetime_max_neural_footprint;	
+uint64_t ri_interval_max_neural_footprint;	
+uint64_t ri_reserved[9];	
 }

```
#### catch_mach_exc_subsystem

```diff

 mach_msg_id_t end;	
 unsigned int maxsize;	
 vm_address_t reserved;	
-struct kern_routine_descriptor kroutine[5];	
+struct kern_routine_descriptor kroutine[6];	
 }

```
#### zone_btrecord

```c
struct zone_btrecord {
  uint32_t ref_count;
  uint32_t operation_type;
  uint64_t bt[15];
}

```
#### hash_info_bucket

```c
struct hash_info_bucket {
  natural_t hib_count;
}

```
#### list_xattrs_result

```c
struct list_xattrs_result {
  uint64_t finderInfoOffset;
  uint64_t resourceForkOffset;
  uint64_t resourceForkLength;
  uint64_t numOfXattrs;
  uint64_t dataLength;
  uint64_t namesLength;
  uint64_t rangesLength;
  uint8_t  data[34860];
}

```
#### task_subsystem

```diff

 mach_msg_id_t end;	
 unsigned int maxsize;	
 vm_address_t reserved;	
-struct kern_routine_descriptor kroutine[65];	
+struct kern_routine_descriptor kroutine[66];	
 }

```
#### thread_act_subsystem

```diff

 mach_msg_id_t end;	
 unsigned int maxsize;	
 vm_address_t reserved;	
-struct kern_routine_descriptor kroutine[31];	
+struct kern_routine_descriptor kroutine[32];	
 }

```
#### vm_info_object

```c
struct vm_info_object {
  natural_t                     vio_object;
  natural_t                     vio_size;
  unsigned int                  vio_ref_count;
  unsigned int                  vio_resident_page_count;
  unsigned int                  vio_absent_count;
  natural_t                     vio_copy;
  natural_t                     vio_shadow;
  natural_t                     vio_shadow_offset;
  natural_t                     vio_paging_offset;
  memory_object_copy_strategy_t vio_copy_strategy;
  vm_offset_t                   vio_last_alloc;
  unsigned int                  vio_paging_in_progress;
  boolean_t                     vio_pager_created;
  boolean_t                     vio_pager_initialized;
  boolean_t                     vio_pager_ready;
  boolean_t                     vio_can_persist;
  boolean_t                     vio_internal;
  boolean_t                     vio_temporary;
  boolean_t                     vio_alive;
  boolean_t                     vio_purgable;
  boolean_t                     vio_purgable_volatile;
}

```
#### _ca_event_vm_sanitize_updated_return_code

```c
struct _ca_event_vm_sanitize_updated_return_code {
  ca_sstr            backtrace[340];
  ca_sstr            process_name[33];
  ca_sstr            process_uuid[37];
  unsigned long long method_checker_info;
  unsigned long long arg1;
  unsigned long long arg2;
  unsigned long long arg3;
  unsigned long long arg4;
  unsigned long long future_ret;
  unsigned long long past_ret;
}

```
#### upl

```diff

 int ref_count;	
 int ext_ref_count;	
 int flags;	
+ctid_t map_addr_owner;	
 vm_object_offset_t u_offset;	
 upl_size_t u_size;	
 upl_size_t u_mapped_size;	

```
#### vm_compressor_kdp_state

```c
struct vm_compressor_kdp_state {
  char     *kc_scratch_bufs;
  char     *kc_decompressed_pages;
  addr64_t *kc_decompressed_pages_paddr;
  ppnum_t  *kc_decompressed_pages_ppnum;
  char     *kc_panic_scratch_buf;
  char     *kc_panic_decompressed_page;
  addr64_t  kc_panic_decompressed_page_paddr;
  ppnum_t   kc_panic_decompressed_page_ppnum;
}

```
#### vm_sanitize_caller

```c
struct vm_sanitize_caller {
  vm_sanitize_caller_id_t vm_sanitize_caller_id;
  const char             *vm_sanitize_caller_name;
  vm_sanitize_method_t    vm_sanitize_telemetry_id;
  enum vm_sanitize_subsys_error_codes {
    KDBG_TRIAGE_VM_SANITIZE_PREFIX = 0,
    KDBG_TRIAGE_VM_SANITIZE_SKIP = 0,
    KDBG_TRIAGE_VM_SANITIZE_MACH_MAKE_MEMORY_ENTRY = 1,
    KDBG_TRIAGE_VM_SANITIZE_MACH_MEMORY_ENTRY_PAGE_OP = 2,
    KDBG_TRIAGE_VM_SANITIZE_MACH_MEMORY_ENTRY_RANGE_OP = 3,
    KDBG_TRIAGE_VM_SANITIZE_MACH_MEMORY_ENTRY_MAP_SIZE = 4,
    KDBG_TRIAGE_VM_SANITIZE_MACH_MEMORY_OBJECT_MEMORY_ENTRY = 5,
    KDBG_TRIAGE_VM_SANITIZE_VM_ALLOCATE_FIXED = 6,
    KDBG_TRIAGE_VM_SANITIZE_VM_ALLOCATE_ANYWHERE = 7,
    KDBG_TRIAGE_VM_SANITIZE_VM_DEALLOCATE = 8,
    KDBG_TRIAGE_VM_SANITIZE_MUNMAP = 9,
    KDBG_TRIAGE_VM_SANITIZE_VM_MAP_REMAP = 10,
    KDBG_TRIAGE_VM_SANITIZE_MMAP = 11,
    KDBG_TRIAGE_VM_SANITIZE_MAP_WITH_LINKING_NP = 12,
    KDBG_TRIAGE_VM_SANITIZE_ENTER_MEM_OBJ = 13,
    KDBG_TRIAGE_VM_SANITIZE_ENTER_MEM_OBJ_CTL = 14,
    KDBG_TRIAGE_VM_SANITIZE_MREMAP_ENCRYPTED = 15,
    KDBG_TRIAGE_VM_SANITIZE_VM_WIRE_USER = 16,
    KDBG_TRIAGE_VM_SANITIZE_VM_UNWIRE_USER = 17,
    KDBG_TRIAGE_VM_SANITIZE_VM_MAP_WIRE = 18,
    KDBG_TRIAGE_VM_SANITIZE_VM_MAP_UNWIRE = 19,
    KDBG_TRIAGE_VM_SANITIZE_VSLOCK = 20,
    KDBG_TRIAGE_VM_SANITIZE_VSUNLOCK = 21,
    KDBG_TRIAGE_VM_SANITIZE_VM_MAP_COPY_OVERWRITE = 22,
    KDBG_TRIAGE_VM_SANITIZE_VM_MAP_COPYIN = 23,
    KDBG_TRIAGE_VM_SANITIZE_VM_MAP_READ_USER = 24,
    KDBG_TRIAGE_VM_SANITIZE_VM_MAP_WRITE_USER = 25,
    KDBG_TRIAGE_VM_SANITIZE_MACH_VM_INHERIT = 26,
    KDBG_TRIAGE_VM_SANITIZE_VM_INHERIT = 27,
    KDBG_TRIAGE_VM_SANITIZE_VM32_INHERIT = 28,
    KDBG_TRIAGE_VM_SANITIZE_VM_MAP_INHERIT = 29,
    KDBG_TRIAGE_VM_SANITIZE_MINHERIT = 30,
    KDBG_TRIAGE_VM_SANITIZE_MACH_VM_PROTECT = 31,
    KDBG_TRIAGE_VM_SANITIZE_VM_PROTECT = 32,
    KDBG_TRIAGE_VM_SANITIZE_VM32_PROTECT = 33,
    KDBG_TRIAGE_VM_SANITIZE_VM_MAP_PROTECT = 34,
    KDBG_TRIAGE_VM_SANITIZE_MPROTECT = 35,
    KDBG_TRIAGE_VM_SANITIZE_USERACC = 36,
    KDBG_TRIAGE_VM_SANITIZE_VM_MAP_MSYNC = 37,
    KDBG_TRIAGE_VM_SANITIZE_MSYNC = 38,
    KDBG_TRIAGE_VM_SANITIZE_VM_MAP_MACHINE_ATTRIBUTE = 39,
    KDBG_TRIAGE_VM_SANITIZE_MINCORE = 40,
    KDBG_TRIAGE_VM_SANITIZE_VM_MAP_PAGE_RANGE_INFO = 41,
    KDBG_TRIAGE_VM_SANITIZE_VM_MAP_PAGE_RANGE_QUERY = 42,
    KDBG_TRIAGE_VM_SANITIZE_TEST = 43,
    KDBG_TRIAGE_VM_SANITIZE_MAX = 44
  } vm_sanitize_ktriage_id;
  vm_sanitize_err_compat_addr_size_fn         err_compat_addr_size;
  vm_sanitize_err_compat_cur_and_max_prots_fn err_compat_prot_cur_max;
}

```
#### vm_deferred_reclamation_metadata_s

```diff

 }
  vdrm_async_list;	
 lck_mtx_t vdrm_lock;	
+gate_t vdrm_gate;	
 task_t vdrm_task;	
+pid_t vdrm_pid;	
 vm_map_t vdrm_map;	
+os_refcnt_t vdrm_refcnt;	
 user_addr_t vdrm_reclaim_buffer;	
 mach_vm_size_t vdrm_buffer_size;	
 user_addr_t vdrm_reclaim_indices;	
 uint64_t vdrm_reclaimed_at;	
 size_t vdrm_num_bytes_put_in_buffer;	
 size_t vdrm_num_bytes_reclaimed;	
+uint32_t vdrm_waiters;	
 }

```
#### dsp

```c
struct dsp {
  size_t info_size;
  size_t dst_size;
  void  *info;
  void  *dst;
}

```
#### _image4_dlxk_interface

```diff

 _image4_trust_evaluation_boot_dlxk_t dlxk_trust_evaluation_boot;	
 _image4_cs_trap_resolve_handler_dlxk_t dlxk_cs_trap_resolve_handler;	
 _image4_cs_trap_vector_size_dlxk_t dlxk_cs_trap_vector_size;	
+_image4_trust_evaluation_normalize_dlxk_t dlxk_trust_evaluation_normalize;	
+_image4_environment_identify_dlxk_t dlxk_environment_identify;	
+_image4_environment_get_digest_info_dlxk_t dlxk_environment_get_digest_info;	
+_image4_environment_flash_dlxk_t dlxk_environment_flash;	
+_image4_coprocessor_resolve_from_manifest_dlxk_t dlxk_coprocessor_resolve_from_manifest;	
+_image4_coprocessor_bootpc_dlxk_t dlxk_coprocessor_bootpc;	
 }

```
#### pmap_ledger_data

```diff

 struct pmap_ledger_data {
-uint8_t pld_data[2360];	
+uint8_t pld_data[2408];	
 }

```
#### hv_vm_percpu_t

```c
struct hv_vm_percpu_t {
  uint64_t last_vcpu_gen;
  bitmap_t stale_vmid_bitmap[4];
}

```
#### arm_exception_state64_v2

```c
struct arm_exception_state64_v2 {
  __uint64_t far;
  __uint64_t esr;
}

```
#### ppl_sart_reg_version

```diff

 struct ppl_sart_reg_version {
 uint32_t versionString;	
+uint8_t regionCount;	
 uint32_t regionConfigRegOffset;	
 uint8_t regionConfigRegSize;	
 uint8_t cpuAccessShift;	

```
#### bti_telemetry_tree

```c
struct bti_telemetry_tree {
  struct bti_telemetry_record *sph_root;
}

```
#### bti_telemetry_record

```c
struct bti_telemetry_record {
  struct {
    struct bti_telemetry_record *spe_left;
    struct bti_telemetry_record *spe_right;
  } link;
  uintptr_t faulting_address;
  uint8_t   branch_type;
}

```
#### _ca_event_arm_bti_exceptions

```c
struct _ca_event_arm_bti_exceptions {
  unsigned long long branch_type;
  unsigned long long faulting_offset;
  ca_sstr            faulting_uuid[37];
}

```
#### workqueue

```diff

 uint8_t wq_cooperative_queue_scheduled_count[6];	
 uint16_t wq_cooperative_queue_best_req_qos;	
 uint16_t wq_cooperative_queue_has_limited_max_size;	
+uint16_t wq_exceeded_active_constrained_thread_limit;	
 uint16_t unused;	
 struct workq_threadreq_tailq wq_cooperative_queue[6];	
 }

```
#### radix_node

```diff

 short rn_bit;	
 char rn_bmask;	
 u_char rn_flags;	
+u_char __rn_keylen;	
+u_char __rn_masklen;	
+short pad2;	
 union {
 struct {
 caddr_t rn_Key;	

```
#### radix_mask

```diff

 short rm_bit;	
 char rm_unused;	
 u_char rm_flags;	
+u_char __rm_masklen;	
+u_char pad[3];	
 struct radix_mask* rm_mklist;	
 union {
-caddr_t rm_mask;	
+caddr_t __rm_mask;	
 struct radix_node* rm_leaf;	
 }
  ;	

```
#### nfserr_info

```c
struct nfserr_info {
  const char *nei_name;
  const int   nei_error;
  const int   nei_index;
}

```
#### nfsrvstats

```diff

 uint64_t srvcache_nonidemdonehits;	
 uint64_t srvcache_misses;	
 uint64_t srvvop_writes;	
+struct {
+uint64_t errs_common[30];	
+uint64_t errs_unknown;	
+}
+ nfs_errs;	
 }

```
#### ifnet

```diff

 struct if_data_internal if_data;	
 ifnet_family_t if_family;	
 ifnet_subfamily_t if_subfamily;	
+u_int32_t peer_egress_functional_type;	
 uintptr_t if_family_cookie;	
 volatile dlil_input_func if_input_dlil;	
 volatile dlil_output_func if_output_dlil;	

 thread_call_t if_dt_tcall;	
 struct {
 u_int32_t length;	
-union {
-u_char buffer[8];	
 u_char* ptr;	
-}
- u;	
 }
  if_broadcast;	
 struct pfi_kif* if_pf_kif;	

 u_int32_t subfamily;	
 uint32_t expensive;	
 uint32_t constrained;	
+uint32_t ultra_constrained;	
 }
  if_delegated;	
 uuid_t* if_agentids;	

 struct if_tcp_ecn_stat* if_ipv4_stat;	
 struct if_tcp_ecn_stat* if_ipv6_stat;	
 struct {
-struct ns_token* slh_first;	
+struct ns_token* lh_first;	
 }
  if_netns_tokens;	
 struct if_lim_perf_stat if_lim_stat;	

```
#### ifreq

```diff

 }
  ifru_type;	
 u_int32_t ifru_functional_type;	
+u_int32_t ifru_peer_egress_functional_type;	
 u_int32_t ifru_expensive;	
 u_int32_t ifru_constrained;	
 u_int32_t ifru_2kcl;	

  ifru_radio_details;	
 uint64_t ifru_creation_generation_id;	
 u_int8_t ifru_is_directlink;	
+u_int8_t ifru_is_vpn;	
+uint32_t ifru_delay_wake_pkt_event;	
 }
  ifr_ifru;	
 }

```
#### mmap_args

```diff

 struct mmap_args {
 char addr_l_[0];	
-user_addr_t addr;	
+user_addr_ut addr;	
 char addr_r_[0];	
 char len_l_[0];	
-user_size_t len;	
+user_size_ut len;	
 char len_r_[0];	
 char prot_l_[0];	
 int prot;	

```
#### mremap_encrypted_args

```diff

 struct mremap_encrypted_args {
 char addr_l_[0];	
-user_addr_t addr;	
+user_addr_ut addr;	
 char addr_r_[0];	
 char len_l_[0];	
-user_size_t len;	
+user_size_ut len;	
 char len_r_[0];	
 char cryptid_l_[0];	
 uint32_t cryptid;	

```
#### buf

```diff

 uint32_t b_redundancy_flags;	
 proc_t b_proc;	
 struct bufattr b_attr;	
-uint32_t b_lblksize;	
+off_t b_lblksize;	
 vnode_t b_vnop_vp;	
 }

```
#### verify_buf

```c
struct verify_buf {
  struct {
    struct verify_buf  *tqe_next;
    struct verify_buf **tqe_prev;
  } vb_entry;
  buf_t   vb_cbp;
  void   *vb_callback_arg;
  int32_t vb_whichq;
}

```
#### fsioc_auth_fs

```diff

 struct fsioc_auth_fs {
 vnode_t authvp;	
+uint64_t flags;	
 }

```
#### registered_tags_head

```c
struct registered_tags_head {
  struct registered_fs_tag *lh_first;
}

```
#### registered_fs_tag

```c
struct registered_fs_tag {
  struct {
    struct registered_fs_tag  *le_next;
    struct registered_fs_tag **le_prev;
  } link;
  uint32_t           fstag;
  uint32_t           flags;
  vnode_t            vp;
  dev_t              dev;
  fsioc_graft_info_t graft_info;
}

```
#### bpf_if

```diff

 uint32_t bif_exthdrlen;	
 uint32_t bif_comphdrlen;	
 struct ifnet* bif_ifp;	
-bpf_send_func bif_send;	
-bpf_tap_func bif_tap;	
+ errno_t (struct ifnet*, u_int32_t, struct mbuf*);* bif_send;	
+ errno_t (struct ifnet*, u_int32_t, bpf_tap_mode);* bif_tap;	
 }

```
#### bpf_d

```diff

 struct bpf_d {
 struct bpf_d* bd_next;	
-caddr_t bd_sbuf;	
-caddr_t bd_hbuf;	
-caddr_t bd_fbuf;	
+caddr_t __bidi_indexable bd_sbuf;	
+caddr_t __bidi_indexable bd_hbuf;	
+caddr_t __bidi_indexable bd_fbuf;	
 uint32_t bd_slen;	
 uint32_t bd_hlen;	
 uint32_t bd_scnt;	

 uint32_t bd_write_size_max;	
 uint32_t bd_rtout;	
 struct bpf_if* bd_bif;	
-struct bpf_insn* bd_filter;	
+__firebloom::counted_by::bd_filter_len bd_filter;	
+uint32_t bd_filter_len;	
 uint64_t bd_rcount;	
 uint64_t bd_dcount;	
 uint64_t bd_fcount;	

 int bd_hdrcmplt;	
 u_int bd_direction;	
 int bd_oflags;	
-thread_call_t bd_thread_call;	
+struct thread_call* bd_thread_call;	
 int bd_traffic_class;	
 int bd_flags;	
+int bd_tstamp;	
 int bd_refcnt;	
 void* bd_ref_lr[4];	
 void* bd_unref_lr[4];	

 uuid_t bd_uuid;	
 pid_t bd_pid;	
 uint8_t bd_prev_slen;	
-caddr_t bd_prev_sbuf;	
-caddr_t bd_prev_fbuf;	
+caddr_t __bidi_indexable bd_prev_sbuf;	
+caddr_t __bidi_indexable bd_prev_fbuf;	
 struct bpf_comp_stats bd_bcs;	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.4

```c
struct __firebloom::wide_ptr.bidi_indexable .4 {
  char *ptr;
  char *ub;
  char *lb;
}

```
#### kern_pbufpool

```diff

 struct skmem_region* pp_umd_region;	
 struct skmem_region* pp_ubft_region;	
 struct skmem_region* pp_kbft_region;	
-struct kern_pbufpool_u_bkt* pp_u_hash_table;	
+__firebloom::counted_by::pp_u_hash_table_size pp_u_hash_table;	
 uint64_t pp_u_bufinuse;	
-struct kern_pbufpool_u_bft_bkt* pp_u_bft_hash_table;	
+__firebloom::counted_by::pp_u_bft_hash_table_size pp_u_bft_hash_table;	
 uint64_t pp_u_bftinuse;	
 void* pp_ctx;	
-pbuf_ctx_retain_fn_t pp_ctx_retain;	
-pbuf_ctx_release_fn_t pp_ctx_release;	
+ void (const void*);* pp_ctx_retain;	
+ void (const void*);* pp_ctx_release;	
 nexus_meta_type_t pp_md_type;	
 nexus_meta_subtype_t pp_md_subtype;	
 uint32_t pp_midx_start;	
 uint32_t pp_bidx_start;	
 pbufpool_name_t pp_name;	
-pbuf_seg_ctor_fn_t pp_pbuf_seg_ctor;	
-pbuf_seg_dtor_fn_t pp_pbuf_seg_dtor;	
+ void (const struct kern_pbufpool*, const struct sksegment*, const struct IOMemoryDescriptor*);* pp_pbuf_seg_ctor;	
+ void (const struct kern_pbufpool*, const struct sksegment*, const struct IOMemoryDescriptor*);* pp_pbuf_seg_dtor;	
+uint32_t pp_u_hash_table_size;	
+uint32_t pp_u_bft_hash_table_size;	
 }

```
#### skmem_cache

```diff

 struct skmem_cache {
 uint32_t skm_mode;	
-skmem_ctor_fn_t skm_ctor;	
-skmem_dtor_fn_t skm_dtor;	
-skmem_reclaim_fn_t skm_reclaim;	
+ int (struct skmem_obj_info*, struct skmem_obj_info*, void*, uint32_t);* skm_ctor;	
+ void (void*, void*);* skm_dtor;	
+ void (void*);* skm_reclaim;	
 void* skm_private;	
 lck_mtx_t skm_dp_lock;	
 struct skmem_magtype* skm_magtype;	
 struct skmem_maglist skm_full;	
 struct skmem_maglist skm_empty;	
 lck_mtx_t skm_sl_lock;	
-skmem_slab_alloc_fn_t skm_slab_alloc;	
-skmem_slab_free_fn_t skm_slab_free;	
+ int (struct skmem_cache*, struct skmem_obj_info*, struct skmem_obj_info*, uint32_t);* skm_slab_alloc;	
+ void (struct skmem_cache*, void*);* skm_slab_free;	
 size_t skm_chunksize;	
 size_t skm_objsize;	
 size_t skm_slabsize;	

 size_t skm_hash_limit;	
 size_t skm_hash_shift;	
 size_t skm_hash_mask;	
-struct skmem_bufctl_bkt* skm_hash_table;	
+size_t skm_hash_size;	
+__firebloom::counted_by::skm_hash_size skm_hash_table;	
 struct {
 struct skmem_slab* tqh_first;	
 struct skmem_slab** tqh_last;	

 struct thread* skm_rs_owner;	
 uint32_t skm_rs_busy;	
 uint32_t skm_rs_want;	
-struct skmem_cpu_cache skm_cpu_cache[1];	
+size_t skm_cpu_cache_count;	
+struct skmem_cpu_cache skm_cpu_cache[0];	
 }

```
#### skmem_obj_info

```diff

 struct skmem_obj_info {
-void* oi_addr;	
+__firebloom::sized_by::oi_size oi_addr;	
 struct skmem_bufctl* oi_bc;	
 uint32_t oi_size;	
 obj_idx_t oi_idx_reg;	

```
#### skmem_bufctl

```diff

 struct skmem_bufctl* sle_next;	
 }
  bc_link;	
-void* bc_addr;	
+__firebloom::sized_by::bc_lim bc_addr;	
 void* bc_addrm;	
 struct skmem_slab* bc_slab;	
 uint32_t bc_lim;	

```
#### sksegment

```diff

 }
  sg_node;	
 struct skmem_region* sg_region;	
-IOSKMemoryBufferRef sg_md;	
+struct IOMemoryDescriptor* sg_md;	
 mach_vm_address_t sg_start;	
 mach_vm_address_t sg_end;	
 uint32_t sg_index;	

```
#### skmem_region

```diff

 uint32_t skr_size;	
 IOSKMemoryBufferSpec skr_bufspec;	
 IOSKRegionSpec skr_regspec;	
-IOSKRegionRef skr_reg;	
+struct IOSKRegion* skr_reg;	
 struct zone* skr_zreg;	
 void* skr_private;	
 struct skmem_cache* skr_cache[2];	
-sksegment_ctor_fn_t skr_seg_ctor;	
-sksegment_dtor_fn_t skr_seg_dtor;	
+ void (struct sksegment*, struct IOMemoryDescriptor*, void*);* skr_seg_ctor;	
+ void (struct sksegment*, struct IOMemoryDescriptor*, void*);* skr_seg_dtor;	
 uint32_t skr_seg_objs;	
 uint32_t skr_seg_bmap_len;	
-bitmap_t* skr_seg_bmap;	
+size_t skr_seg_bmap_size;	
+__firebloom::sized_by::skr_seg_bmap_size skr_seg_bmap;	
 uint32_t skr_seg_free_cnt;	
 uint32_t skr_hash_initial;	
 uint32_t skr_hash_limit;	
 uint32_t skr_hash_shift;	
 uint32_t skr_hash_mask;	
-struct sksegment_bkt* skr_hash_table;	
+size_t skr_hash_size;	
+__firebloom::counted_by::skr_hash_size skr_hash_table;	
 struct segfreehead skr_seg_free;	
 struct segtfreehead skr_seg_tfree;	
 uint32_t skr_seg_waiters;	

```
#### skmem_mag

```diff

 }
  mg_link;	
 struct skmem_magtype* mg_magtype;	
-void* mg_round[1];	
+size_t mg_count;	
+void* mg_round[0];	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.14

```c
struct __firebloom::wide_ptr.bidi_indexable .14 {
  struct bpf_hdr_ext *ptr;
  struct bpf_hdr_ext *ub;
  struct bpf_hdr_ext *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.9

```diff

 struct __firebloom::wide_ptr.bidi_indexable.9 {
-struct nwk_wq_entry* ptr;	
-struct nwk_wq_entry* ub;	
-struct nwk_wq_entry* lb;	
+void* ptr;	
+void* ub;	
+void* lb;	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.18

```c
struct __firebloom::wide_ptr.bidi_indexable .18 {
  struct pktap_header *ptr;
  struct pktap_header *ub;
  struct pktap_header *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.19

```c
struct __firebloom::wide_ptr.bidi_indexable .19 {
  struct bpf_hdr *ptr;
  struct bpf_hdr *ub;
  struct bpf_hdr *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.20

```c
struct __firebloom::wide_ptr.bidi_indexable .20 {
  struct bpf_comp_hdr *ptr;
  struct bpf_comp_hdr *ub;
  struct bpf_comp_hdr *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.12

```c
struct __firebloom::wide_ptr.bidi_indexable .12 {
  u_char *ptr;
  u_char *ub;
  u_char *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.58

```c
struct __firebloom::wide_ptr.bidi_indexable .58 {
  u_int *ptr;
  u_int *ub;
  u_int *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.68

```c
struct __firebloom::wide_ptr.bidi_indexable .68 {
  struct bpf_if *ptr;
  struct bpf_if *ub;
  struct bpf_if *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.80

```diff

 struct __firebloom::wide_ptr.bidi_indexable.80 {
-uint8_t* ptr;	
-uint8_t* ub;	
-uint8_t* lb;	
+struct ether_header* ptr;	
+struct ether_header* ub;	
+struct ether_header* lb;	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.85

```diff

 struct __firebloom::wide_ptr.bidi_indexable.85 {
-const struct sockaddr_in6* ptr;	
-const struct sockaddr_in6* ub;	
-const struct sockaddr_in6* lb;	
+struct bpf_insn* ptr;	
+struct bpf_insn* ub;	
+struct bpf_insn* lb;	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.91

```diff

 struct __firebloom::wide_ptr.bidi_indexable.91 {
-struct in6_multi* ptr;	
-struct in6_multi* ub;	
-struct in6_multi* lb;	
+struct bpf_packet* ptr;	
+struct bpf_packet* ub;	
+struct bpf_packet* lb;	
 }

```
#### bpf_packet

```diff

 struct bpf_packet {
 int bpfp_type;	
-void* bpfp_header;	
+__firebloom::sized_by::bpfp_header_length bpfp_header;	
 size_t bpfp_header_length;	
 union {
 struct mbuf* bpfpu_mbuf;	

```
#### __firebloom::wide_ptr.bidi_indexable.99

```c
struct __firebloom::wide_ptr.bidi_indexable .99 {
  const uint32_t *ptr;
  const uint32_t *ub;
  const uint32_t *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.111

```c
struct __firebloom::wide_ptr.bidi_indexable .111 {
  struct xbpf_d *ptr;
  struct xbpf_d *ub;
  struct xbpf_d *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.83

```diff

 struct __firebloom::wide_ptr.bidi_indexable.83 {
-char* ptr;	
-char* ub;	
-char* lb;	
+struct kalloc_heap* ptr;	
+struct kalloc_heap* ub;	
+struct kalloc_heap* lb;	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.79

```c
struct __firebloom::wide_ptr.bidi_indexable .79 {
  struct pktap_v2_hdr *ptr;
  struct pktap_v2_hdr *ub;
  struct pktap_v2_hdr *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.30

```c
struct __firebloom::wide_ptr.bidi_indexable .30 {
  struct mbuf *ptr;
  struct mbuf *ub;
  struct mbuf *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable

```diff

 struct __firebloom::wide_ptr.bidi_indexable {
-struct igmp_ifinfo* ptr;	
-struct igmp_ifinfo* ub;	
-struct igmp_ifinfo* lb;	
+struct bpf_d* ptr;	
+struct bpf_d* ub;	
+struct bpf_d* lb;	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.56

```c
struct __firebloom::wide_ptr.bidi_indexable .56 {
  const void *ptr;
  const void *ub;
  const void *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.100

```c
struct __firebloom::wide_ptr.bidi_indexable .100 {
  struct __kern_buflet *ptr;
  struct __kern_buflet *ub;
  struct __kern_buflet *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.6

```c
struct __firebloom::wide_ptr.bidi_indexable .6 {
  struct bpf_d **ptr;
  struct bpf_d **ub;
  struct bpf_d **lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.21

```c
struct __firebloom::wide_ptr.bidi_indexable .21 {
  struct ifnet *ptr;
  struct ifnet *ub;
  struct ifnet *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.0

```c
struct __firebloom::wide_ptr.bidi_indexable .0 {
  struct bpf_packet *ptr;
  struct bpf_packet *ub;
  struct bpf_packet *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.3

```diff

 struct __firebloom::wide_ptr.bidi_indexable.3 {
-struct nwk_wq_entry** ptr;	
-struct nwk_wq_entry** ub;	
-struct nwk_wq_entry** lb;	
+void* ptr;	
+void* ub;	
+void* lb;	
 }

```
#### __firebloom::wide_ptr.indexable

```diff

 struct __firebloom::wide_ptr.indexable {
-struct igmpv3* ptr;	
-struct igmpv3* ub;	
+u_char* ptr;	
+u_char* ub;	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.28

```c
struct __firebloom::wide_ptr.bidi_indexable .28 {
  struct mbuf *ptr;
  struct mbuf *ub;
  struct mbuf *lb;
}

```
#### __firebloom::wide_ptr.indexable.30

```c
struct __firebloom::wide_ptr.indexable .30 {
  void *ptr;
  void *ub;
}

```
#### bridge_softc

```diff

 struct bridge_softc {
 struct ifnet* sc_ifp;	
-u_int32_t sc_flags;	
+uint32_t sc_flags;	
 struct {
 struct bridge_softc* le_next;	
 struct bridge_softc** le_prev;	
 }
  sc_list;	
 lck_mtx_t sc_mtx;	
-struct _bridge_rtnode_list* sc_rthash;	
+__firebloom::counted_by::sc_rthash_size sc_rthash;	
 struct _bridge_rtnode_list sc_rtlist;	
 uint32_t sc_rthash_key;	
 uint32_t sc_rthash_size;	

 }
  sc_spanlist;	
 struct bstp_state sc_stp;	
-bpf_packet_func sc_bpf_input;	
-bpf_packet_func sc_bpf_output;	
 void* sc_cv;	
 uint32_t sc_brtmax;	
 uint32_t sc_brtcnt;	

```
#### pf_ruleset

```diff

 struct pf_rulequeue queues[2];	
 struct {
 struct pf_rulequeue* ptr;	
-struct pf_rule** ptr_array;	
+__firebloom::counted_by::rsize ptr_array;	
 u_int32_t rcount;	
 u_int32_t rsize;	
 u_int32_t ticket;	

  active;	
 struct {
 struct pf_rulequeue* ptr;	
-struct pf_rule** ptr_array;	
+__firebloom::counted_by::rsize ptr_array;	
 u_int32_t rcount;	
 u_int32_t rsize;	
 u_int32_t ticket;	

```
#### nexus_netif_adapter

```diff

 struct nexus_netif_adapter {
 struct nexus_adapter nifna_up;	
 struct nx_netif* nifna_netif;	
-struct nx_netif_mit* nifna_tx_mit;	
-struct nx_netif_mit* nifna_rx_mit;	
+__firebloom::counted_by::nifna_tx_mit_count nifna_tx_mit;	
+__firebloom::counted_by::nifna_rx_mit_count nifna_rx_mit;	
 union {
 struct netif_filter* nifna_filter;	
 struct netif_flow* nifna_flow;	
 }
  ;	
 uint16_t nifna_gencnt;	
+uint32_t nifna_tx_mit_count;	
+uint32_t nifna_rx_mit_count;	
 }

```
#### nexus_adapter

```diff

 uint32_t na_num_allocator_ring_pairs;	
 uint32_t na_num_event_rings;	
 uint32_t na_num_large_buf_alloc_rings;	
+uint32_t na_rx_rings_cnt;	
+uint32_t na_tx_rings_cnt;	
+uint32_t na_alloc_free_rings_cnt;	
+uint32_t na_event_rings_cnt;	
+uint32_t na_large_buf_alloc_rings_cnt;	
+uint32_t na_slot_ctxs_cnt;	
+uint32_t na_scratch_cnt;	
+uint32_t na_all_rings_cnt;	
 uint64_t na_work_ts;	
-struct __kern_channel_ring* na_tx_rings;	
-struct __kern_channel_ring* na_rx_rings;	
+__firebloom::counted_by::na_tx_rings_cnt na_tx_rings;	
+__firebloom::counted_by::na_rx_rings_cnt na_rx_rings;	
+__firebloom::counted_by::na_all_rings_cnt na_all_rings;	
 struct kern_nexus* na_nx;	
 volatile uint32_t na_refcount;	
 int na_si_users[6];	

 uint32_t na_total_slots;	
 const uint32_t na_flowadv_max;	
 const nexus_stats_type_t na_stats_type;	
-struct __kern_channel_ring* na_alloc_rings;	
-struct __kern_channel_ring* na_free_rings;	
-struct __kern_channel_ring* na_event_rings;	
-struct __kern_channel_ring* na_large_buf_alloc_rings;	
+__firebloom::counted_by::na_alloc_free_rings_cnt na_alloc_rings;	
+__firebloom::counted_by::na_alloc_free_rings_cnt na_free_rings;	
+__firebloom::counted_by::na_event_rings_cnt na_event_rings;	
+__firebloom::counted_by::na_large_buf_alloc_rings_cnt na_large_buf_alloc_rings;	
 uint64_t na_ch_mit_ival;	
 struct kern_nexus_domain_provider* na_nxdom_prov;	
-struct slot_ctx* na_slot_ctxs;	
-kern_packet_t* na_scratch;	
-struct __kern_channel_ring* na_tail;	
+__firebloom::counted_by::na_slot_ctxs_cnt na_slot_ctxs;	
+__firebloom::counted_by::na_scratch_cnt na_scratch;	
+__firebloom::counted_by::0 na_tail;	
 void* na_private;	
 struct ifnet* na_ifp;	
 uint8_t na_kring_svc_lut[10];	
 uint32_t na_next_pipe;	
 uint32_t na_max_pipes;	
-struct nexus_upipe_adapter** na_pipes;	
+__firebloom::counted_by::na_max_pipes na_pipes;	
 char na_name[64];	
 uuid_t na_uuid;	
  int (struct nexus_adapter*, na_activate_mode_t);* na_activate;	

```
#### __kern_channel_ring

```diff

 volatile uint32_t ckr_alloc_ws;	
 struct nexus_adapter* ckr_na;	
 struct kern_pbufpool* ckr_pp;	
-struct __slot_desc* ckr_usds;	
-struct __slot_desc* ckr_ksds;	
+__firebloom::counted_by::ckr_usds_cnt ckr_usds;	
+slot_idx_t ckr_usds_cnt;	
+__firebloom::counted_by::ckr_ksds_cnt ckr_ksds;	
+slot_idx_t ckr_ksds_cnt;	
 struct __slot_desc* ckr_ksds_last;	
 struct skmem_cache* ckr_ksds_cache;	
 uint32_t ckr_ring_id;	
 boolean_t ckr_rate_limited;	
-uint64_t* ckr_scratch;	
+__firebloom::counted_by::ckr_scratch_cnt ckr_scratch;	
+slot_idx_t ckr_scratch_cnt;	
  int (struct __kern_channel_ring*, struct proc*, uint32_t);* ckr_na_sync;	
 volatile  int (struct __kern_channel_ring*, struct proc*, uint32_t);* ckr_na_notify;	
  int (struct kern_channel*, struct __kern_channel_ring*, const slot_idx_t, uint32_t*, uint64_t*, struct proc*);* ckr_prologue;	
  void (struct kern_channel*, struct __kern_channel_ring*, const slot_idx_t, struct proc*);* ckr_finalize;	
 uint64_t ckr_sync_time;	
  int (struct __kern_channel_ring*, struct proc*, uint32_t);* ckr_save_notify;	
-uint32_t* ckr_leases;	
-slot_idx_t ckr_klease;	
-slot_idx_t ckr_lease_idx;	
 kern_packet_svc_class_t ckr_svc;	
 uint32_t ckr_slot_ctxs_set;	
-struct slot_ctx* ckr_slot_ctxs;	
+__firebloom::counted_by::ckr_slot_ctxs_cnt ckr_slot_ctxs;	
+uint32_t ckr_slot_ctxs_cnt;	
 void* ckr_ctx;	
 struct ch_selinfo ckr_si;	
  int (struct __kern_channel_ring*, struct proc*, uint32_t);* ckr_netif_notify;	

 struct nx_netif_mit* ckr_mit;	
 volatile uint32_t ckr_pending_intr;	
 volatile uint32_t ckr_pending_doorbell;	
-struct mbuf** ckr_tx_pool;	
+__firebloom::counted_by::ckr_tx_pool_count ckr_tx_pool;	
+uint32_t ckr_tx_pool_count;	
 struct nx_mbq ckr_rx_queue;	
 struct __kern_channel_ring* ckr_pipe;	
 struct __user_channel_ring* ckr_save_ring;	

```
#### kern_nexus

```diff

 uint32_t nx_refcnt;	
 volatile uint32_t nx_flags;	
 void* nx_ctx;	
-nexus_ctx_release_fn_t nx_ctx_release;	
+ void (const void*);* nx_ctx_release;	
 struct kern_nexus_provider* nx_prov;	
 uint64_t nx_id;	
 uuid_t nx_uuid;	

 struct kern_pbufpool* nx_rx_pp;	
 struct kern_pbufpool* nx_tx_pp;	
 struct kern_nexus_advisory nx_adv;	
-struct nx_port_info* nx_ports;	
-bitmap_t* nx_ports_bmap;	
+__firebloom::counted_by::nx_num_ports nx_ports;	
+__firebloom::sized_by::nx_ports_bmap_size nx_ports_bmap;	
 nexus_port_size_t nx_active_ports;	
 nexus_port_size_t nx_num_ports;	
+size_t nx_ports_bmap_size;	
 }

```
#### nxctl

```diff

 }
  nxctl_link;	
 struct fileproc* nxctl_fp;	
-kauth_cred_t nxctl_cred;	
-void* nxctl_traffic_rule_storage;	
+struct ucred* nxctl_cred;	
+struct nxctl_traffic_rule_storage* nxctl_traffic_rule_storage;	
 }

```
#### nxbind

```diff

 uint64_t nxb_uniqueid;	
 uuid_t nxb_exec_uuid;	
 uint32_t nxb_key_len;	
-void* nxb_key;	
+__firebloom::sized_by::nxb_key_len nxb_key;	
 }

```
#### kern_nexus_domain_provider_init

```diff

 struct kern_nexus_domain_provider_init {
 uint32_t nxdpi_version;	
 uint32_t nxdpi_flags;	
-nxdom_prov_init_fn_t nxdpi_init;	
-nxdom_prov_fini_fn_t nxdpi_fini;	
+ errno_t (struct kern_nexus_domain_provider*);* nxdpi_init;	
+ void (struct kern_nexus_domain_provider*);* nxdpi_fini;	
 }

```
#### nxdom_prov_cb

```diff

 struct nxdom_prov_cb {
  int (struct kern_nexus_domain_provider*);* dp_cb_init;	
  void (struct kern_nexus_domain_provider*);* dp_cb_fini;	
- int (struct kern_nexus_domain_provider*, const uint32_t, const struct nxprov_params*, struct nxprov_params*, struct skmem_region_params*, uint32_t);* dp_cb_params;	
+ int (struct kern_nexus_domain_provider*, const uint32_t, const struct nxprov_params*, struct nxprov_params*, __firebloom::counted_by::28, uint32_t);* dp_cb_params;	
  int (struct kern_nexus_domain_provider*, struct kern_nexus*, struct nexus_adapter*);* dp_cb_mem_new;	
- int (struct kern_nexus_domain_provider*, struct kern_nexus*, struct nx_cfg_req*, int, struct proc*, kauth_cred_t);* dp_cb_config;	
+ int (struct kern_nexus_domain_provider*, struct kern_nexus*, struct nx_cfg_req*, int, struct proc*, struct ucred*);* dp_cb_config;	
  int (struct kern_nexus*);* dp_cb_nx_ctor;	
  void (struct kern_nexus*);* dp_cb_nx_dtor;	
  int (struct kern_nexus*, struct kern_pbufpool**, struct kern_pbufpool**);* dp_cb_nx_mem_info;	

```
#### info_tuple

```diff

 struct info_tuple {
 u_int8_t itpl_proto;	
 union {
-struct sockaddr _itpl_sa;	
 struct __sockaddr_header _itpl_sah;	
 struct sockaddr_in _itpl_sin;	
 struct sockaddr_in6 _itpl_sin6;	
 }
  itpl_localaddr;	
 union {
-struct sockaddr _itpl_sa;	
 struct __sockaddr_header _itpl_sah;	
 struct sockaddr_in _itpl_sin;	
 struct sockaddr_in6 _itpl_sin6;	

```
#### kern_nexus_provider_init

```diff

 struct kern_nexus_provider_init {
 uint32_t nxpi_version;	
 uint32_t nxpi_flags;	
-nxprov_pre_connect_fn_t nxpi_pre_connect;	
-nxprov_connected_fn_t nxpi_connected;	
-nxprov_pre_disconnect_fn_t nxpi_pre_disconnect;	
-nxprov_disconnected_fn_t nxpi_disconnected;	
-nxprov_ring_init_fn_t nxpi_ring_init;	
-nxprov_ring_fini_fn_t nxpi_ring_fini;	
-nxprov_slot_init_fn_t nxpi_slot_init;	
-nxprov_slot_fini_fn_t nxpi_slot_fini;	
-nxprov_sync_tx_fn_t nxpi_sync_tx;	
-nxprov_sync_rx_fn_t nxpi_sync_rx;	
-nxprov_tx_doorbell_fn_t nxpi_tx_doorbell;	
-nxprov_sync_packets_fn_t nxpi_rx_sync_packets;	
-nxprov_sync_packets_fn_t nxpi_tx_sync_packets;	
-nxprov_capab_config_fn_t nxpi_config_capab;	
+ errno_t (struct kern_nexus_provider*, struct proc*, struct kern_nexus*, nexus_port_t, struct kern_channel*, void**);* nxpi_pre_connect;	
+ errno_t (struct kern_nexus_provider*, struct kern_nexus*, struct kern_channel*);* nxpi_connected;	
+ void (struct kern_nexus_provider*, struct kern_nexus*, struct kern_channel*);* nxpi_pre_disconnect;	
+ void (struct kern_nexus_provider*, struct kern_nexus*, struct kern_channel*);* nxpi_disconnected;	
+ errno_t (struct kern_nexus_provider*, struct kern_nexus*, struct kern_channel*, struct __kern_channel_ring*, boolean_t, void**);* nxpi_ring_init;	
+ void (struct kern_nexus_provider*, struct kern_nexus*, struct __kern_channel_ring*);* nxpi_ring_fini;	
+ errno_t (struct kern_nexus_provider*, struct kern_nexus*, struct __kern_channel_ring*, struct __slot_desc*, uint32_t, struct kern_slot_prop**, void**);* nxpi_slot_init;	
+ void (struct kern_nexus_provider*, struct kern_nexus*, struct __kern_channel_ring*, struct __slot_desc*, uint32_t);* nxpi_slot_fini;	
+ errno_t (struct kern_nexus_provider*, struct kern_nexus*, struct __kern_channel_ring*, uint32_t);* nxpi_sync_tx;	
+ errno_t (struct kern_nexus_provider*, struct kern_nexus*, struct __kern_channel_ring*, uint32_t);* nxpi_sync_rx;	
+ errno_t (struct kern_nexus_provider*, struct kern_nexus*, struct __kern_channel_ring*, uint32_t);* nxpi_tx_doorbell;	
+ errno_t (struct kern_nexus_provider*, struct kern_nexus*, struct __kern_channel_ring*, uint64_t*, uint32_t*, uint32_t);* nxpi_rx_sync_packets;	
+ errno_t (struct kern_nexus_provider*, struct kern_nexus*, struct __kern_channel_ring*, uint64_t*, uint32_t*, uint32_t);* nxpi_tx_sync_packets;	
+ errno_t (struct kern_nexus_provider*, struct kern_nexus*, kern_nexus_capab_t, void*, uint32_t*);* nxpi_config_capab;	
 }

```
#### kern_nexus_netif_provider_init

```diff

 struct kern_nexus_netif_provider_init {
 uint32_t nxnpi_version;	
 uint32_t nxnpi_flags;	
-nxprov_pre_connect_fn_t nxnpi_pre_connect;	
-nxprov_connected_fn_t nxnpi_connected;	
-nxprov_pre_disconnect_fn_t nxnpi_pre_disconnect;	
-nxprov_disconnected_fn_t nxnpi_disconnected;	
-nxprov_qset_init_fn_t nxnpi_qset_init;	
-nxprov_qset_fini_fn_t nxnpi_qset_fini;	
-nxprov_queue_init_fn_t nxnpi_queue_init;	
-nxprov_queue_fini_fn_t nxnpi_queue_fini;	
-nxprov_tx_qset_notify_fn_t nxnpi_tx_qset_notify;	
-nxprov_capab_config_fn_t nxnpi_config_capab;	
+ errno_t (struct kern_nexus_provider*, struct proc*, struct kern_nexus*, nexus_port_t, struct kern_channel*, void**);* nxnpi_pre_connect;	
+ errno_t (struct kern_nexus_provider*, struct kern_nexus*, struct kern_channel*);* nxnpi_connected;	
+ void (struct kern_nexus_provider*, struct kern_nexus*, struct kern_channel*);* nxnpi_pre_disconnect;	
+ void (struct kern_nexus_provider*, struct kern_nexus*, struct kern_channel*);* nxnpi_disconnected;	
+ errno_t (struct kern_nexus_provider*, struct kern_nexus*, void*, uint8_t, uint64_t, struct netif_qset*, void**);* nxnpi_qset_init;	
+ void (struct kern_nexus_provider*, struct kern_nexus*, void*);* nxnpi_qset_fini;	
+ errno_t (struct kern_nexus_provider*, struct kern_nexus*, void*, uint8_t, _Bool, struct netif_queue*, void**);* nxnpi_queue_init;	
+ void (struct kern_nexus_provider*, struct kern_nexus*, void*);* nxnpi_queue_fini;	
+ errno_t (struct kern_nexus_provider*, struct kern_nexus*, void*, uint32_t);* nxnpi_tx_qset_notify;	
+ errno_t (struct kern_nexus_provider*, struct kern_nexus*, kern_nexus_capab_t, void*, uint32_t*);* nxnpi_config_capab;	
+ errno_t (struct kern_nexus_provider*, struct kern_nexus*, void*, kern_packet_t*, uint32_t*, uint32_t*);* nxnpi_queue_tx_push;	
 }

```
#### netif_qset

```diff

 uint16_t nqs_flags;	
 uint8_t nqs_num_rx_queues;	
 uint8_t nqs_num_tx_queues;	
+uint8_t nqs_num_queues;	
 struct netif_queue nqs_driver_queues[0];	
 }

```
#### nx_netif

```diff

 struct netif_agent_flow_head nif_agent_flow_list;	
 uint32_t nif_agent_flow_cnt;	
 uint32_t nif_agent_flags;	
-netagent_session_t nif_agent_session;	
+void* nif_agent_session;	
 uuid_t nif_agent_uuid;	
 uint32_t nif_hwassist;	
 uint32_t nif_capabilities;	

  nif_llink_list;	
 uint16_t nif_llink_cnt;	
 uint32_t nif_extended_capabilities;	
-kern_nexus_capab_interface_advisory_config_fn_t nif_intf_adv_config;	
+ errno_t (void*, _Bool);* nif_intf_adv_config;	
 void* nif_intf_adv_prov_ctx;	
 struct netif_qset_extensions nif_qset_extensions;	
 }

```
#### ifnet_interface_advisory_header

```diff

 IF_INTERFACE_ADVISORY_INTERFACE_TYPE_MIN=1,
 IF_INTERFACE_ADVISORY_INTERFACE_TYPE_CELL=2,
 IF_INTERFACE_ADVISORY_INTERFACE_TYPE_MAX=2} interface_type;	
-uint8_t reserved;	
+ifnet_interface_advisory_notification_type_t notification_type;	
 }

```
#### netif_flowtable_ops

```diff

 netif_flow_info_t* nfo_info;	
 netif_flow_insert_t* nfo_insert;	
 netif_flow_remove_t* nfo_remove;	
-netif_flow_table_alloc_t* nfo_table_alloc;	
+ struct netif_flowtable* (struct netif_flowtable_ops*);* nfo_table_alloc;	
 netif_flow_table_free_t* nfo_table_free;	
 }

```
#### kern_nexus_netif_llink_init

```diff

 uint8_t nli_num_qsets;	
 void* nli_ctx;	
 kern_nexus_netif_llink_id_t nli_link_id;	
-struct kern_nexus_netif_llink_qset_init* nli_qsets;	
+__firebloom::counted_by::nli_num_qsets nli_qsets;	
 }

```
#### netif_qset_extensions

```diff

 struct netif_qset_extensions {
-kern_nexus_capab_qsext_notify_steering_info_fn_t qe_notify_steering_info;	
+ errno_t (void*, void*, struct ifnet_traffic_descriptor_common*, _Bool);* qe_notify_steering_info;	
 void* qe_prov_ctx;	
 }

```
#### kern_nexus_advisory

```diff

 struct kern_nexus_advisory {
 struct skmem_region* nxv_reg;	
-void* nxv_adv;	
+__firebloom::sized_by::nxv_adv_size nxv_adv;	
 nexus_advisory_type_t nxv_adv_type;	
 union {
 struct sk_nexusadv* flowswitch_nxv_adv;	
 struct netif_nexus_advisory* netif_nxv_adv;	
 }
  ;	
+uint32_t nxv_adv_size;	
 }

```
#### __user_channel_schema

```diff

 struct __user_channel_schema {
 const uint32_t csm_ver;	
 const volatile uint32_t csm_flags;	
-const char csm_kern_name[256];	
-const uuid_t csm_kern_uuid;	
+char csm_kern_name[256];	
+uuid_t csm_kern_uuid;	
 const uint32_t csm_tx_rings;	
 const uint32_t csm_rx_rings;	
 const uint32_t csm_allocator_ring_pairs;	

```
#### ch_selinfo

```diff

 uint32_t csi_pending;	
 uint64_t csi_eff_interval;	
 uint64_t csi_interval;	
-thread_call_t csi_tcall;	
+struct thread_call* csi_tcall;	
 }

```
#### skmem_arena_mmap_info

```diff

 }
  ami_link;	
 struct skmem_arena* ami_arena;	
-IOSKMapperRef ami_mapref;	
-task_t ami_maptask;	
+struct IOSKMapper* ami_mapref;	
+struct task* ami_maptask;	
 mach_vm_address_t ami_mapaddr;	
 mach_vm_size_t ami_mapsize;	
 boolean_t ami_redirect;	

```
#### skmem_arena

```diff

 skmem_arena_type_t ar_type;	
 uint32_t ar_flags;	
 size_t ar_zsize;	
-IOSKArenaRef ar_ar;	
+struct IOSKArena* ar_ar;	
 struct skmem_region* ar_regions[28];	
 mach_vm_size_t ar_mapsize;	
 uint32_t ar_mapcnt;	

```
#### slot_ctx

```diff

 struct slot_ctx {
-mach_vm_address_t slot_ctx_arg;	
+void* slot_ctx_arg;	
 }

```
#### bridge_iflist

```diff

 uint32_t bif_addrmax;	
 uint32_t bif_addrcnt;	
 uint32_t bif_addrexceeded;	
-interface_filter_t bif_iff_ref;	
+struct ifnet_filter* bif_iff_ref;	
 struct bridge_softc* bif_sc;	
 uint32_t bif_flags;	
 struct in_addr bif_hf_ipsrc;	

```
#### bstp_state

```diff

 struct bstp_port* lh_first;	
 }
  bs_bplist;	
-bstp_state_cb_t bs_state_cb;	
-bstp_rtage_cb_t bs_rtage_cb;	
+ void (struct ifnet*, int);* bs_state_cb;	
+ void (struct ifnet*, int);* bs_rtage_cb;	
 }

```
#### bridge_delayed_call

```diff

 struct bridge_delayed_call {
 struct bridge_softc* bdc_sc;	
-bridge_delayed_func_t bdc_func;	
+ void (struct bridge_softc*);* bdc_func;	
 struct timespec bdc_ts;	
 u_int32_t bdc_flags;	
-thread_call_t bdc_thread_call;	
+struct thread_call* bdc_thread_call;	
 }

```
#### if_clone

```diff

 lck_mtx_t ifc_mutex;	
 u_int32_t ifc_minifs;	
 u_int32_t ifc_maxunit;	
-unsigned char* ifc_units;	
 u_int32_t ifc_bmlen;	
+__firebloom::counted_by::ifc_bmlen ifc_units;	
  int (struct if_clone*, u_int32_t, void*);* ifc_create;	
  int (struct ifnet*);* ifc_destroy;	
 uint8_t ifc_namelen;	

```
#### bridge_control

```diff

 struct bridge_control {
- int (struct bridge_softc*, void*);* bc_func;	
+ int (struct bridge_softc*, __firebloom::sized_by::arg_len, size_t);* bc_func;	
 unsigned int bc_argsize;	
 unsigned int bc_flags;	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.44

```c
struct __firebloom::wide_ptr.bidi_indexable .44 {
  char *ptr;
  char *ub;
  char *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.64

```c
struct __firebloom::wide_ptr.bidi_indexable .64 {
  struct _bridge_rtnode_list *ptr;
  struct _bridge_rtnode_list *ub;
  struct _bridge_rtnode_list *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.10

```c
struct __firebloom::wide_ptr.bidi_indexable .10 {
  void *ptr;
  void *ub;
  void *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.43

```c
struct __firebloom::wide_ptr.bidi_indexable .43 {
  struct ether_header *ptr;
  struct ether_header *ub;
  struct ether_header *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.88

```diff

 struct __firebloom::wide_ptr.bidi_indexable.88 {
-struct in_multi* ptr;	
-struct in_multi* ub;	
-struct in_multi* lb;	
+struct ether_arp* ptr;	
+struct ether_arp* ub;	
+struct ether_arp* lb;	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.57

```c
struct __firebloom::wide_ptr.bidi_indexable .57 {
  uint8_t *ptr;
  uint8_t *ub;
  uint8_t *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.97

```c
struct __firebloom::wide_ptr.bidi_indexable .97 {
  struct ip6_hdr *ptr;
  struct ip6_hdr *ub;
  struct ip6_hdr *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.102

```c
struct __firebloom::wide_ptr.bidi_indexable .102 {
  struct icmp6_hdr *ptr;
  struct icmp6_hdr *ub;
  struct icmp6_hdr *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.104

```c
struct __firebloom::wide_ptr.bidi_indexable .104 {
  struct nd_neighbor_solicit *ptr;
  struct nd_neighbor_solicit *ub;
  struct nd_neighbor_solicit *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.107

```diff

 struct __firebloom::wide_ptr.bidi_indexable.107 {
-struct in_multi* ptr;	
-struct in_multi* ub;	
-struct in_multi* lb;	
+struct nd_opt_hdr* ptr;	
+struct nd_opt_hdr* ub;	
+struct nd_opt_hdr* lb;	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.108

```diff

 struct __firebloom::wide_ptr.bidi_indexable.108 {
-int* ptr;	
-int* ub;	
-int* lb;	
+struct nd_neighbor_advert* ptr;	
+struct nd_neighbor_advert* ub;	
+struct nd_neighbor_advert* lb;	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.117

```c
struct __firebloom::wide_ptr.bidi_indexable .117 {
  struct llc *ptr;
  struct llc *ub;
  struct llc *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.123

```c
struct __firebloom::wide_ptr.bidi_indexable .123 {
  struct tcphdr *ptr;
  struct tcphdr *ub;
  struct tcphdr *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.138

```diff

 struct __firebloom::wide_ptr.bidi_indexable.138 {
-struct igmp_report* ptr;	
-struct igmp_report* ub;	
-struct igmp_report* lb;	
+struct ifreq* ptr;	
+struct ifreq* ub;	
+struct ifreq* lb;	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.139

```diff

 struct __firebloom::wide_ptr.bidi_indexable.139 {
-struct sockaddr_in6* ptr;	
-struct sockaddr_in6* ub;	
-struct sockaddr_in6* lb;	
+struct ifmediareq32* ptr;	
+struct ifmediareq32* ub;	
+struct ifmediareq32* lb;	
 }

```
#### ifmediareq32

```c
struct ifmediareq32 {
  char          ifm_name[16];
  int           ifm_current;
  int           ifm_mask;
  int           ifm_status;
  int           ifm_active;
  int           ifm_count;
  user32_addr_t ifmu_ulist;
}

```
#### __firebloom::wide_ptr.bidi_indexable.145

```diff

 struct __firebloom::wide_ptr.bidi_indexable.145 {
-ctrace_t* ptr;	
-ctrace_t* ub;	
-ctrace_t* lb;	
+struct ifdrv32* ptr;	
+struct ifdrv32* ub;	
+struct ifdrv32* lb;	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.151

```c
struct __firebloom::wide_ptr.bidi_indexable .151 {
  struct ifdrv64 *ptr;
  struct ifdrv64 *ub;
  struct ifdrv64 *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.169

```c
struct __firebloom::wide_ptr.bidi_indexable .169 {
  struct sockaddr *ptr;
  struct sockaddr *ub;
  struct sockaddr *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.95

```diff

 struct __firebloom::wide_ptr.bidi_indexable.95 {
-struct in6_multi** ptr;	
-struct in6_multi** ub;	
-struct in6_multi** lb;	
+struct udphdr* ptr;	
+struct udphdr* ub;	
+struct udphdr* lb;	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.69

```c
struct __firebloom::wide_ptr.bidi_indexable .69 {
  struct bridge_rtnode *ptr;
  struct bridge_rtnode *ub;
  struct bridge_rtnode *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.180

```c
struct __firebloom::wide_ptr.bidi_indexable .180 {
  struct kern_event_msg *ptr;
  struct kern_event_msg *ub;
  struct kern_event_msg *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.181

```c
struct __firebloom::wide_ptr.bidi_indexable .181 {
  struct event *ptr;
  struct event *ub;
  struct event *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.48

```c
struct __firebloom::wide_ptr.bidi_indexable .48 {
  struct bridge_softc *ptr;
  struct bridge_softc *ub;
  struct bridge_softc *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.208

```c
struct __firebloom::wide_ptr.bidi_indexable .208 {
  struct sockaddr_dl *ptr;
  struct sockaddr_dl *ub;
  struct sockaddr_dl *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.82

```diff

 struct __firebloom::wide_ptr.bidi_indexable.82 {
-struct in6_msource* ptr;	
-struct in6_msource* ub;	
-struct in6_msource* lb;	
+struct mac_nat_entry* ptr;	
+struct mac_nat_entry* ub;	
+struct mac_nat_entry* lb;	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.75

```c
struct __firebloom::wide_ptr.bidi_indexable .75 {
  struct bridge_iflist *ptr;
  struct bridge_iflist *ub;
  struct bridge_iflist *lb;
}

```
#### __firebloom::wide_ptr.indexable.94

```c
struct __firebloom::wide_ptr.indexable .94 {
  uint8_t *ptr;
  uint8_t *ub;
}

```
#### __firebloom::wide_ptr.bidi_indexable.67

```c
struct __firebloom::wide_ptr.bidi_indexable .67 {
  struct ifnet *ptr;
  struct ifnet *ub;
  struct ifnet *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.13

```c
struct __firebloom::wide_ptr.bidi_indexable .13 {
  struct mbuf *ptr;
  struct mbuf *ub;
  struct mbuf *lb;
}

```
#### gso_ip_tcp_state

```diff

 struct gso_ip_tcp_state {
  void (struct gso_ip_tcp_state*, struct mbuf*);* update;	
  void (struct gso_ip_tcp_state*, struct mbuf*);* internal;	
-union iphdr hdr;	
+u_int ip_m0_len;	
+__firebloom::counted_by::ip_m0_len hdr;	
 struct tcphdr* tcp;	
 int mac_hlen;	
 int ip_hlen;	

```
#### __firebloom::wide_ptr.bidi_indexable.127

```diff

 struct __firebloom::wide_ptr.bidi_indexable.127 {
-int* ptr;	
-int* ub;	
-int* lb;	
+struct in_ifaddr* ptr;	
+struct in_ifaddr* ub;	
+struct in_ifaddr* lb;	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.132

```diff

 struct __firebloom::wide_ptr.bidi_indexable.132 {
-struct in6_multi* ptr;	
-struct in6_multi* ub;	
-struct in6_multi* lb;	
+struct in6_ifaddr* ptr;	
+struct in6_ifaddr* ub;	
+struct in6_ifaddr* lb;	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.49

```c
struct __firebloom::wide_ptr.bidi_indexable .49 {
  struct kalloc_type_view *ptr;
  struct kalloc_type_view *ub;
  struct kalloc_type_view *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.175

```diff

 struct __firebloom::wide_ptr.bidi_indexable.175 {
-struct mbuf* ptr;	
-struct mbuf* ub;	
-struct mbuf* lb;	
+struct bridge_delayed_call* ptr;	
+struct bridge_delayed_call* ub;	
+struct bridge_delayed_call* lb;	
 }

```
#### ifnet_init_eparams

```diff

 u_int32_t ver;	
 u_int32_t len;	
 u_int32_t flags;	
-const void* uniqueid;	
+__firebloom::sized_by::uniqueid_len uniqueid;	
 u_int32_t uniqueid_len;	
 const char* name;	
 u_int32_t unit;	
 ifnet_family_t family;	
 u_int32_t type;	
 u_int32_t sndq_maxlen;	
-ifnet_output_func output;	
-ifnet_pre_enqueue_func pre_enqueue;	
-ifnet_start_func start;	
-ifnet_ctl_func output_ctl;	
+ errno_t (struct ifnet*, struct mbuf*);* output;	
+ errno_t (struct ifnet*, struct mbuf*);* pre_enqueue;	
+ void (struct ifnet*);* start;	
+ errno_t (struct ifnet*, ifnet_ctl_cmd_t, u_int32_t, void*);* output_ctl;	
 u_int32_t output_sched_model;	
 u_int32_t output_target_qdelay;	
 u_int64_t output_bw;	

 u_int16_t start_delay_qlen;	
 u_int16_t start_delay_timeout;	
 u_int32_t _reserved[3];	
-ifnet_input_poll_func input_poll;	
-ifnet_ctl_func input_ctl;	
+ void (struct ifnet*, u_int32_t, u_int32_t, struct mbuf**, struct mbuf**, u_int32_t*, u_int32_t*);* input_poll;	
+ errno_t (struct ifnet*, ifnet_ctl_cmd_t, u_int32_t, void*);* input_ctl;	
 u_int32_t rcvq_maxlen;	
 u_int32_t __reserved;	
 u_int64_t input_bw;	

 u_int64_t input_lt;	
 u_int64_t input_lt_max;	
 u_int64_t ___reserved[2];	
-ifnet_demux_func demux;	
-ifnet_add_proto_func add_proto;	
-ifnet_del_proto_func del_proto;	
-ifnet_check_multi check_multi;	
-ifnet_framer_func framer;	
+ errno_t (struct ifnet*, struct mbuf*, char*, protocol_family_t*);* demux;	
+ errno_t (struct ifnet*, protocol_family_t, __firebloom::counted_by::demux_count, u_int32_t);* add_proto;	
+ errno_t (struct ifnet*, protocol_family_t);* del_proto;	
+ errno_t (struct ifnet*, const struct sockaddr*);* check_multi;	
+ errno_t (struct ifnet*, struct mbuf**, const struct sockaddr*, const char*, const char*);* framer;	
 void* softc;	
-ifnet_ioctl_func ioctl;	
-ifnet_set_bpf_tap set_bpf_tap;	
-ifnet_detached_func detach;	
-ifnet_event_func event;	
-const void* broadcast_addr;	
+ errno_t (struct ifnet*, unsigned long, void*);* ioctl;	
+ errno_t (struct ifnet*, bpf_tap_mode,  errno_t (struct ifnet*, struct mbuf*);*);* set_bpf_tap;	
+ void (struct ifnet*);* detach;	
+ void (struct ifnet*, const struct kev_msg*);* event;	
+__firebloom::sized_by::broadcast_len broadcast_addr;	
 u_int32_t broadcast_len;	
-ifnet_framer_extended_func framer_extended;	
+ errno_t (struct ifnet*, struct mbuf**, const struct sockaddr*, const char*, const char*, u_int32_t*, u_int32_t*);* framer_extended;	
 ifnet_subfamily_t subfamily;	
 u_int16_t tx_headroom;	
 u_int16_t tx_trailer;	
 u_int32_t rx_mit_ival;	
 u_int32_t ____reserved;	
-ifnet_free_func free;	
+ void (struct ifnet*);* free;	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.146

```diff

 struct __firebloom::wide_ptr.bidi_indexable.146 {
-u_int16_t* ptr;	
-u_int16_t* ub;	
-u_int16_t* lb;	
+const struct bridge_control* ptr;	
+const struct bridge_control* ub;	
+const struct bridge_control* lb;	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.185

```c
struct __firebloom::wide_ptr.bidi_indexable .185 {
  struct kalloc_heap *ptr;
  struct kalloc_heap *ub;
  struct kalloc_heap *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.182

```c
struct __firebloom::wide_ptr.bidi_indexable .182 {
  struct bstp_port *ptr;
  struct bstp_port *ub;
  struct bstp_port *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.189

```c
struct __firebloom::wide_ptr.bidi_indexable .189 {
  struct bstp_state *ptr;
  struct bstp_state *ub;
  struct bstp_state *lb;
}

```
#### iff_filter

```diff

 void* iff_cookie;	
 const char* iff_name;	
 protocol_family_t iff_protocol;	
-iff_input_func iff_input;	
-iff_output_func iff_output;	
-iff_event_func iff_event;	
-iff_ioctl_func iff_ioctl;	
-iff_detached_func iff_detached;	
+ errno_t (void*, struct ifnet*, protocol_family_t, struct mbuf**, char**);* iff_input;	
+ errno_t (void*, struct ifnet*, protocol_family_t, struct mbuf**);* iff_output;	
+ void (void*, struct ifnet*, protocol_family_t, const struct kev_msg*);* iff_event;	
+ errno_t (void*, struct ifnet*, protocol_family_t, unsigned long, void*);* iff_ioctl;	
+ void (void*, struct ifnet*);* iff_detached;	
 }

```
#### ifnet_attach_proto_param

```diff

 struct ifnet_attach_proto_param {
-struct ifnet_demux_desc* demux_array;	
+__firebloom::counted_by::demux_count demux_array;	
 u_int32_t demux_count;	
-proto_media_input input;	
-proto_media_preout pre_output;	
-proto_media_event event;	
-proto_media_ioctl ioctl;	
-proto_media_detached detached;	
-proto_media_resolve_multi resolve;	
-proto_media_send_arp send_arp;	
+ errno_t (struct ifnet*, protocol_family_t, struct mbuf*, char*);* input;	
+ errno_t (struct ifnet*, protocol_family_t, struct mbuf**, const struct sockaddr*, void*, char*, char*);* pre_output;	
+ void (struct ifnet*, protocol_family_t, const struct kev_msg*);* event;	
+ errno_t (struct ifnet*, protocol_family_t, unsigned long, void*);* ioctl;	
+ errno_t (struct ifnet*, protocol_family_t);* detached;	
+ errno_t (struct ifnet*, const struct sockaddr*, struct sockaddr_dl*, size_t);* resolve;	
+ errno_t (struct ifnet*, u_short, const struct sockaddr_dl*, const struct sockaddr*, const struct sockaddr_dl*, const struct sockaddr*);* send_arp;	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.96

```diff

 struct __firebloom::wide_ptr.bidi_indexable.96 {
-struct ip6_hdr* ptr;	
-struct ip6_hdr* ub;	
-struct ip6_hdr* lb;	
+uint16_t* ptr;	
+uint16_t* ub;	
+uint16_t* lb;	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.119

```diff

 struct __firebloom::wide_ptr.bidi_indexable.119 {
-struct ifnet* ptr;	
-struct ifnet* ub;	
-struct ifnet* lb;	
+struct brcsumstats* ptr;	
+struct brcsumstats* ub;	
+struct brcsumstats* lb;	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.22

```c
struct __firebloom::wide_ptr.bidi_indexable .22 {
  unsigned char *ptr;
  unsigned char *ub;
  unsigned char *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.90

```diff

 struct __firebloom::wide_ptr.bidi_indexable.90 {
-struct mbuf* ptr;	
-struct mbuf* ub;	
-struct mbuf* lb;	
+struct ifmediareq32* ptr;	
+struct ifmediareq32* ub;	
+struct ifmediareq32* lb;	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.92

```diff

 struct __firebloom::wide_ptr.bidi_indexable.92 {
-struct igmp* ptr;	
-struct igmp* ub;	
-struct igmp* lb;	
+struct if_descreq* ptr;	
+struct if_descreq* ub;	
+struct if_descreq* lb;	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.94

```diff

 struct __firebloom::wide_ptr.bidi_indexable.94 {
-struct in6_multi_mship* ptr;	
-struct in6_multi_mship* ub;	
-struct in6_multi_mship* lb;	
+struct if_qstatsreq* ptr;	
+struct if_qstatsreq* ub;	
+struct if_qstatsreq* lb;	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.98

```diff

 struct __firebloom::wide_ptr.bidi_indexable.98 {
-struct igmpv3* ptr;	
-struct igmpv3* ub;	
-struct igmpv3* lb;	
+struct if_agentidreq* ptr;	
+struct if_agentidreq* ub;	
+struct if_agentidreq* lb;	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.101

```diff

 struct __firebloom::wide_ptr.bidi_indexable.101 {
-int* ptr;	
-int* ub;	
-int* lb;	
+struct if_nexusreq* ptr;	
+struct if_nexusreq* ub;	
+struct if_nexusreq* lb;	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.110

```c
struct __firebloom::wide_ptr.bidi_indexable .110 {
  struct if_clat46req *ptr;
  struct if_clat46req *ub;
  struct if_clat46req *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.70

```c
struct __firebloom::wide_ptr.bidi_indexable .70 {
  struct ifstat *ptr;
  struct ifstat *ub;
  struct ifstat *lb;
}

```
#### __firebloom::wide_ptr.indexable.56

```c
struct __firebloom::wide_ptr.indexable .56 {
  char *ptr;
  char *ub;
}

```
#### __firebloom::wide_ptr.bidi_indexable.60

```c
struct __firebloom::wide_ptr.bidi_indexable .60 {
  u_int32_t *ptr;
  u_int32_t *ub;
  u_int32_t *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.130

```diff

 struct __firebloom::wide_ptr.bidi_indexable.130 {
-struct sockaddr_storage* ptr;	
-struct sockaddr_storage* ub;	
-struct sockaddr_storage* lb;	
+int* ptr;	
+int* ub;	
+int* lb;	
 }

```
#### __firebloom::wide_ptr.indexable.55

```c
struct __firebloom::wide_ptr.indexable .55 {
  void *ptr;
  void *ub;
}

```
#### __firebloom::wide_ptr.bidi_indexable.47

```c
struct __firebloom::wide_ptr.bidi_indexable .47 {
  const uint8_t *ptr;
  const uint8_t *ub;
  const uint8_t *lb;
}

```
#### eventhandler_entry_ifnet_event

```diff

 struct eventhandler_entry_ifnet_event {
 struct eventhandler_entry ee;	
-ifnet_event_fn eh_func;	
+ void (struct eventhandler_entry_arg, struct ifnet*, struct sockaddr*, intf_event_code_t);* eh_func;	
 }

```
#### __firebloom::wide_ptr.indexable.48

```c
struct __firebloom::wide_ptr.indexable .48 {
  uint8_t *ptr;
  uint8_t *ub;
}

```
#### __firebloom::wide_ptr.bidi_indexable.35

```c
struct __firebloom::wide_ptr.bidi_indexable .35 {
  struct ifnet *ptr;
  struct ifnet *ub;
  struct ifnet *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.41

```c
struct __firebloom::wide_ptr.bidi_indexable .41 {
  struct ifaddr *ptr;
  struct ifaddr *ub;
  struct ifaddr *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.23

```c
struct __firebloom::wide_ptr.bidi_indexable .23 {
  struct kalloc_heap *ptr;
  struct kalloc_heap *ub;
  struct kalloc_heap *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.36

```c
struct __firebloom::wide_ptr.bidi_indexable .36 {
  struct in_ifaddr *ptr;
  struct in_ifaddr *ub;
  struct in_ifaddr *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.42

```c
struct __firebloom::wide_ptr.bidi_indexable .42 {
  struct in6_ifaddr *ptr;
  struct in6_ifaddr *ub;
  struct in6_ifaddr *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.135

```diff

 struct __firebloom::wide_ptr.bidi_indexable.135 {
-struct ip_moptions* ptr;	
-struct ip_moptions* ub;	
-struct ip_moptions* lb;	
+const struct sockaddr_dl* ptr;	
+const struct sockaddr_dl* ub;	
+const struct sockaddr_dl* lb;	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.50

```c
struct __firebloom::wide_ptr.bidi_indexable .50 {
  struct sockaddr *ptr;
  struct sockaddr *ub;
  struct sockaddr *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.59

```c
struct __firebloom::wide_ptr.bidi_indexable .59 {
  struct ifclassq *ptr;
  struct ifclassq *ub;
  struct ifclassq *lb;
}

```
#### pr_usrreqs_old

```diff

  int (struct socket*, struct sockaddr*, struct proc*);* pru_bind;	
  int (struct socket*, struct sockaddr*, struct proc*);* pru_connect;	
  int (struct socket*, struct socket*);* pru_connect2;	
- int (struct socket*, u_long, caddr_t, struct ifnet*, struct proc*);* pru_control;	
+ int (struct socket*, u_long, char*, struct ifnet*, struct proc*);* pru_control;	
  int (struct socket*);* pru_detach;	
  int (struct socket*);* pru_disconnect;	
  int (struct socket*, struct proc*);* pru_listen;	

```
#### pr_usrreqs

```diff

  int (struct socket*, struct sockaddr*, struct proc*);* pru_connect;	
  int (struct socket*, struct socket*);* pru_connect2;	
  int (struct socket*, struct sockaddr*, struct sockaddr*, struct proc*, uint32_t, sae_associd_t, sae_connid_t*, uint32_t, void*, uint32_t, struct uio*, user_ssize_t*);* pru_connectx;	
- int (struct socket*, u_long, caddr_t, struct ifnet*, struct proc*);* pru_control;	
+ int (struct socket*, u_long, __firebloom::sized_by::(((cmd) >> 16) & 8191), struct ifnet*, struct proc*);* pru_control;	
  int (struct socket*);* pru_detach;	
  int (struct socket*);* pru_disconnect;	
  int (struct socket*, sae_associd_t, sae_connid_t);* pru_disconnectx;	

```
#### __firebloom::wide_ptr.bidi_indexable.173

```c
struct __firebloom::wide_ptr.bidi_indexable .173 {
  struct ifmultiaddr_dbg *ptr;
  struct ifmultiaddr_dbg *ub;
  struct ifmultiaddr_dbg *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.174

```c
struct __firebloom::wide_ptr.bidi_indexable .174 {
  ctrace_t *ptr;
  ctrace_t *ub;
  ctrace_t *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.167

```diff

 struct __firebloom::wide_ptr.bidi_indexable.167 {
-struct sockaddr_in* ptr;	
-struct sockaddr_in* ub;	
-struct sockaddr_in* lb;	
+struct rtentry* ptr;	
+struct rtentry* ub;	
+struct rtentry* lb;	
 }

```
#### init_list_entry

```diff

 struct init_list_entry {
 struct init_list_entry* next;	
-net_init_func_ptr func;	
+ void ();* func;	
 }

```
#### flow_mgr

```diff

 size_t fm_flow_hash_count[7];	
 uint16_t fm_flow_hash_masks[7];	
 void* fm_owner_buckets;	
-const size_t fm_owner_buckets_cnt;	
-const size_t fm_owner_bucket_sz;	
-const size_t fm_owner_bucket_tot_sz;	
+size_t fm_owner_buckets_cnt;	
+size_t fm_owner_bucket_sz;	
+size_t fm_owner_bucket_tot_sz;	
 void* fm_route_buckets;	
-const size_t fm_route_buckets_cnt;	
-const size_t fm_route_bucket_sz;	
-const size_t fm_route_bucket_tot_sz;	
+size_t fm_route_buckets_cnt;	
+size_t fm_route_bucket_sz;	
+size_t fm_route_bucket_tot_sz;	
 void* fm_route_id_buckets;	
-const size_t fm_route_id_buckets_cnt;	
-const size_t fm_route_id_bucket_sz;	
-const size_t fm_route_id_bucket_tot_sz;	
+size_t fm_route_id_buckets_cnt;	
+size_t fm_route_id_bucket_sz;	
+size_t fm_route_id_bucket_tot_sz;	
 }

```
#### fsw_stats

```diff

 struct fsw_stats {
-uint64_t _arr[117];	
+uint64_t _arr[118];	
 }

```
#### tcp_stats

```diff

 struct tcp_stats {
-uint64_t _arr[210];	
+uint64_t _arr[213];	
 }

```
#### flow_entry

```diff

 uint8_t fe_transport_protocol;	
 uint16_t fe_rx_frag_count;	
 uint32_t fe_rx_pktq_bytes;	
+lck_mtx_t fe_rx_pktq_lock;	
 struct pktq fe_rx_pktq;	
 struct {
 struct flow_entry* tqe_next;	
 struct flow_entry** tqe_prev;	
 }
  fe_rx_link;	
-flow_action_t fe_rx_process;	
+flow_rx_action_t fe_rx_process;	
+uint64_t fe_rx_worker_tid;	
 uint32_t fe_rx_largest_size;	
 _Bool fe_tx_is_cont_frag;	
 uint32_t fe_tx_frag_id;	

 struct flow_entry** tqe_prev;	
 }
  fe_tx_link;	
-flow_action_t fe_tx_process;	
+flow_tx_action_t fe_tx_process;	
 uuid_t fe_eproc_uuid;	
 flowadv_idx_t fe_adv_idx;	
 kern_packet_svc_class_t fe_svc_class;	

```
#### ether_desc_blk_str

```diff

 u_int32_t n_max_used;	
 u_int32_t n_count;	
 u_int32_t n_used;	
-struct en_desc block_ptr[1];	
+struct en_desc block_ptr[0];	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.40

```c
struct __firebloom::wide_ptr.bidi_indexable .40 {
  char *ptr;
  char *ub;
  char *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.17

```c
struct __firebloom::wide_ptr.bidi_indexable .17 {
  struct ether_header *ptr;
  struct ether_header *ub;
  struct ether_header *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.52

```c
struct __firebloom::wide_ptr.bidi_indexable .52 {
  struct sockaddr_dl *ptr;
  struct sockaddr_dl *ub;
  struct sockaddr_dl *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.5

```c
struct __firebloom::wide_ptr.bidi_indexable .5 {
  struct en_desc *ptr;
  struct en_desc *ub;
  struct en_desc *lb;
}

```
#### __firebloom::wide_ptr.indexable.37

```c
struct __firebloom::wide_ptr.indexable .37 {
  char *ptr;
  char *ub;
}

```
#### ether_vlan_encap_header

```c
struct ether_vlan_encap_header {
  u_int16_t evle_tag;
  u_int16_t evle_proto;
}

```
#### __firebloom::wide_ptr.bidi_indexable.45

```c
struct __firebloom::wide_ptr.bidi_indexable .45 {
  struct mbuf *ptr;
  struct mbuf *ub;
  struct mbuf *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.1

```c
struct __firebloom::wide_ptr.bidi_indexable .1 {
  char *ptr;
  char *ub;
  char *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.33

```c
struct __firebloom::wide_ptr.bidi_indexable .33 {
  struct ether_arp *ptr;
  struct ether_arp *ub;
  struct ether_arp *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.32

```c
struct __firebloom::wide_ptr.bidi_indexable .32 {
  uint8_t *ptr;
  uint8_t *ub;
  uint8_t *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.37

```c
struct __firebloom::wide_ptr.bidi_indexable .37 {
  const struct ether_header *ptr;
  const struct ether_header *ub;
  const struct ether_header *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.38

```c
struct __firebloom::wide_ptr.bidi_indexable .38 {
  struct sockaddr_dl *ptr;
  struct sockaddr_dl *ub;
  struct sockaddr_dl *lb;
}

```
#### __firebloom::wide_ptr.indexable.46

```c
struct __firebloom::wide_ptr.indexable .46 {
  char *ptr;
  char *ub;
}

```
#### __firebloom::wide_ptr.bidi_indexable.34

```c
struct __firebloom::wide_ptr.bidi_indexable .34 {
  const struct sockaddr_in *ptr;
  const struct sockaddr_in *ub;
  const struct sockaddr_in *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.61

```c
struct __firebloom::wide_ptr.bidi_indexable .61 {
  const struct sockaddr_inarp *ptr;
  const struct sockaddr_inarp *ub;
  const struct sockaddr_inarp *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.62

```c
struct __firebloom::wide_ptr.bidi_indexable .62 {
  struct ifaddr *ptr;
  struct ifaddr *ub;
  struct ifaddr *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.11

```c
struct __firebloom::wide_ptr.bidi_indexable .11 {
  struct mbuf *ptr;
  struct mbuf *ub;
  struct mbuf *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.46

```c
struct __firebloom::wide_ptr.bidi_indexable .46 {
  const struct sockaddr_in6 *ptr;
  const struct sockaddr_in6 *ub;
  const struct sockaddr_in6 *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.16

```c
struct __firebloom::wide_ptr.bidi_indexable .16 {
  struct ip6aux *ptr;
  struct ip6aux *ub;
  struct ip6aux *lb;
}

```
#### lo_statics_str

```diff

 struct lo_statics_str {
 int bpf_mode;	
-bpf_packet_func bpf_callback;	
+ errno_t (struct ifnet*, struct mbuf*);* bpf_callback;	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.53

```c
struct __firebloom::wide_ptr.bidi_indexable .53 {
  struct loopback_header *ptr;
  struct loopback_header *ub;
  struct loopback_header *lb;
}

```
#### ifvlan

```diff

 char ifv_name[16];	
 struct ifnet* ifv_ifp;	
 vlan_parent_ref ifv_vlp;	
-struct ifv_linkmib ifv_mib;	
+u_int16_t ifv_mtufudge;	
+u_int16_t ifv_tag;	
 struct multicast_list ifv_multicast;	
 u_int32_t ifv_flags;	
 int32_t ifv_retain_count;	

```
#### multicast_entry

```diff

 struct multicast_entry* sle_next;	
 }
  mc_entries;	
-ifmultiaddr_t mc_ifma;	
+struct ifmultiaddr* mc_ifma;	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.81

```diff

 struct __firebloom::wide_ptr.bidi_indexable.81 {
-struct in_mfilter* ptr;	
-struct in_mfilter* ub;	
-struct in_mfilter* lb;	
+struct event* ptr;	
+struct event* ub;	
+struct event* lb;	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.24

```c
struct __firebloom::wide_ptr.bidi_indexable .24 {
  struct ifnet *ptr;
  struct ifnet *ub;
  struct ifnet *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.78

```diff

 struct __firebloom::wide_ptr.bidi_indexable.78 {
-struct in_msource* ptr;	
-struct in_msource* ub;	
-struct in_msource* lb;	
+struct sockaddr* ptr;	
+struct sockaddr* ub;	
+struct sockaddr* lb;	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.74

```c
struct __firebloom::wide_ptr.bidi_indexable .74 {
  struct mbuf *ptr;
  struct mbuf *ub;
  struct mbuf *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.55

```c
struct __firebloom::wide_ptr.bidi_indexable .55 {
  struct ifreq *ptr;
  struct ifreq *ub;
  struct ifreq *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.54

```c
struct __firebloom::wide_ptr.bidi_indexable .54 {
  struct ifmediareq32 *ptr;
  struct ifmediareq32 *ub;
  struct ifmediareq32 *lb;
}

```
#### if_fake

```diff

 int iff_media_active;	
 uint32_t iff_media_count;	
 int iff_media_list[27];	
-struct mbuf* iff_pending_tx_packet;	
 boolean_t iff_start_busy;	
 unsigned int iff_max_mtu;	
 uint32_t iff_fcs;	

```
#### __firebloom::wide_ptr.bidi_indexable.77

```c
struct __firebloom::wide_ptr.bidi_indexable .77 {
  struct icmp6_hdr *ptr;
  struct icmp6_hdr *ub;
  struct icmp6_hdr *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.124

```diff

 struct __firebloom::wide_ptr.bidi_indexable.124 {
-int* ptr;	
-int* ub;	
-int* lb;	
+struct kern_event_msg* ptr;	
+struct kern_event_msg* ub;	
+struct kern_event_msg* lb;	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.125

```diff

 struct __firebloom::wide_ptr.bidi_indexable.125 {
-struct in6_ifaddr* ptr;	
-struct in6_ifaddr* ub;	
-struct in6_ifaddr* lb;	
+struct event* ptr;	
+struct event* ub;	
+struct event* lb;	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.105

```diff

 struct __firebloom::wide_ptr.bidi_indexable.105 {
-struct ip_moptions* ptr;	
-struct ip_moptions* ub;	
-struct ip_moptions* lb;	
+struct nexus_controller* ptr;	
+struct nexus_controller* ub;	
+struct nexus_controller* lb;	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.15

```c
struct __firebloom::wide_ptr.bidi_indexable .15 {
  struct {
    char                        rd_name[16];
    lck_mtx_t                   rd_lock;
    uint32_t                    rd_ftype;
    struct ifnet               *rd_ifp;
    struct ifnet               *rd_delegate_ifp;
    boolean_t                   rd_detaching;
    boolean_t                   rd_connected;
    boolean_t                   rd_self_ref;
    boolean_t                   rd_delegate_parent_set;
    boolean_t                   rd_delegate_ref;
    boolean_t                   rd_fsw_rx_cb_set;
    boolean_t                   rd_delegate_set;
    boolean_t                   rd_mac_addr_set;
    boolean_t                   rd_detach_notify_set;
    unsigned int                rd_max_mtu;
    uint32_t                    rd_retain_count;
    struct kern_pbufpool       *rd_pp;
    struct __kern_channel_ring *rd_rx_ring[1];
    struct __kern_channel_ring *rd_tx_ring[1];
    redirect_nx                 rd_nx;
    struct netif_stats         *rd_nifs;
    void                       *rd_intf_adv_kern_ctx;
    struct thread_call         *rd_doorbell_tcall;
    boolean_t                   rd_doorbell_tcall_active;
    boolean_t                   rd_waiting_for_tcall;
    _Bool                       rd_intf_adv_enabled;
    errno_t(void *, const struct ifnet_interface_advisory *);
    *rd_intf_adv_notify;
  } *ptr;
  struct {
    char                        rd_name[16];
    lck_mtx_t                   rd_lock;
    uint32_t                    rd_ftype;
    struct ifnet               *rd_ifp;
    struct ifnet               *rd_delegate_ifp;
    boolean_t                   rd_detaching;
    boolean_t                   rd_connected;
    boolean_t                   rd_self_ref;
    boolean_t                   rd_delegate_parent_set;
    boolean_t                   rd_delegate_ref;
    boolean_t                   rd_fsw_rx_cb_set;
    boolean_t                   rd_delegate_set;
    boolean_t                   rd_mac_addr_set;
    boolean_t                   rd_detach_notify_set;
    unsigned int                rd_max_mtu;
    uint32_t                    rd_retain_count;
    struct kern_pbufpool       *rd_pp;
    struct __kern_channel_ring *rd_rx_ring[1];
    struct __kern_channel_ring *rd_tx_ring[1];
    redirect_nx                 rd_nx;
    struct netif_stats         *rd_nifs;
    void                       *rd_intf_adv_kern_ctx;
    struct thread_call         *rd_doorbell_tcall;
    boolean_t                   rd_doorbell_tcall_active;
    boolean_t                   rd_waiting_for_tcall;
    _Bool                       rd_intf_adv_enabled;
    errno_t(void *, const struct ifnet_interface_advisory *);
    *rd_intf_adv_notify;
  } *ub;
  struct {
    char                        rd_name[16];
    lck_mtx_t                   rd_lock;
    uint32_t                    rd_ftype;
    struct ifnet               *rd_ifp;
    struct ifnet               *rd_delegate_ifp;
    boolean_t                   rd_detaching;
    boolean_t                   rd_connected;
    boolean_t                   rd_self_ref;
    boolean_t                   rd_delegate_parent_set;
    boolean_t                   rd_delegate_ref;
    boolean_t                   rd_fsw_rx_cb_set;
    boolean_t                   rd_delegate_set;
    boolean_t                   rd_mac_addr_set;
    boolean_t                   rd_detach_notify_set;
    unsigned int                rd_max_mtu;
    uint32_t                    rd_retain_count;
    struct kern_pbufpool       *rd_pp;
    struct __kern_channel_ring *rd_rx_ring[1];
    struct __kern_channel_ring *rd_tx_ring[1];
    redirect_nx                 rd_nx;
    struct netif_stats         *rd_nifs;
    void                       *rd_intf_adv_kern_ctx;
    struct thread_call         *rd_doorbell_tcall;
    boolean_t                   rd_doorbell_tcall_active;
    boolean_t                   rd_waiting_for_tcall;
    _Bool                       rd_intf_adv_enabled;
    errno_t(void *, const struct ifnet_interface_advisory *);
    *rd_intf_adv_notify;
  } *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.51

```c
struct __firebloom::wide_ptr.bidi_indexable .51 {
  struct __kern_packet *ptr;
  struct __kern_packet *ub;
  struct __kern_packet *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.109

```c
struct __firebloom::wide_ptr.bidi_indexable .109 {
  struct netif_stats *ptr;
  struct netif_stats *ub;
  struct netif_stats *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.116

```c
struct __firebloom::wide_ptr.bidi_indexable .116 {
  struct nexus_netif_adapter *ptr;
  struct nexus_netif_adapter *ub;
  struct nexus_netif_adapter *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.29

```c
struct __firebloom::wide_ptr.bidi_indexable .29 {
  struct ifreq *ptr;
  struct ifreq *ub;
  struct ifreq *lb;
}

```
#### ifbond_s

```diff

 struct os_refcnt ifb_retain_count;	
 char ifb_name[16];	
 struct ifnet* ifb_ifp;	
-bpf_packet_func ifb_bpf_input;	
-bpf_packet_func ifb_bpf_output;	
 int ifb_altmtu;	
 struct port_list ifb_port_list;	
 short ifb_port_count;	
 struct lag_list ifb_lag_list;	
 lacp_key ifb_key;	
 short ifb_max_active;	
-LAG_ref ifb_active_lag;	
+struct LAG_s* ifb_active_lag;	
 struct ifmultiaddr* ifb_ifma_slow_proto;	
-bondport_ref* ifb_distributing_array;	
+__firebloom::counted_by::ifb_distributing_max ifb_distributing_array;	
 int ifb_distributing_count;	
 int ifb_distributing_max;	
 int ifb_last_link_event;	

```
#### bondport_s

```diff

 char po_name[16];	
 struct ifdevmtu po_devmtu;	
 uint32_t po_control_flags;	
-interface_filter_t po_filter;	
 struct {
 struct bondport_s* tqe_next;	
 struct bondport_s** tqe_prev;	
 }
  po_lag_port_list;	
-devtimer_ref po_current_while_timer;	
-devtimer_ref po_periodic_timer;	
-devtimer_ref po_wait_while_timer;	
-devtimer_ref po_transmit_timer;	
+struct devtimer_s* po_current_while_timer;	
+struct devtimer_s* po_periodic_timer;	
+struct devtimer_s* po_wait_while_timer;	
+struct devtimer_s* po_transmit_timer;	
 partner_state po_partner_state;	
 lacp_port_priority po_priority;	
 lacp_actor_partner_state po_actor_state;	

 int32_t po_last_transmit_secs;	
 struct media_info po_media_info;	
 uint64_t po_force_link_event_time;	
-LAG_ref po_lag;	
+struct LAG_s* po_lag;	
 }

```
#### __firebloom::wide_ptr.indexable.86

```c
struct __firebloom::wide_ptr.indexable .86 {
  uint8_t *ptr;
  uint8_t *ub;
}

```
#### __firebloom::wide_ptr.bidi_indexable.103

```c
struct __firebloom::wide_ptr.bidi_indexable .103 {
  struct lacpdu_s *ptr;
  struct lacpdu_s *ub;
  struct lacpdu_s *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.112

```diff

 struct __firebloom::wide_ptr.bidi_indexable.112 {
-struct kalloc_type_view* ptr;	
-struct kalloc_type_view* ub;	
-struct kalloc_type_view* lb;	
+struct la_marker_pdu_s* ptr;	
+struct la_marker_pdu_s* ub;	
+struct la_marker_pdu_s* lb;	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.114

```diff

 struct __firebloom::wide_ptr.bidi_indexable.114 {
-struct kalloc_type_view* ptr;	
-struct kalloc_type_view* ub;	
-struct kalloc_type_view* lb;	
+struct lacp_collector_tlv_s* ptr;	
+struct lacp_collector_tlv_s* ub;	
+struct lacp_collector_tlv_s* lb;	
 }

```
#### __firebloom::wide_ptr.indexable.64

```c
struct __firebloom::wide_ptr.indexable .64 {
  void *ptr;
  void *ub;
}

```
#### __firebloom::wide_ptr.bidi_indexable.118

```c
struct __firebloom::wide_ptr.bidi_indexable .118 {
  struct event *ptr;
  struct event *ub;
  struct event *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.106

```c
struct __firebloom::wide_ptr.bidi_indexable .106 {
  struct partner_state_s *ptr;
  struct partner_state_s *ub;
  struct partner_state_s *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.25

```c
struct __firebloom::wide_ptr.bidi_indexable .25 {
  struct ifnet *ptr;
  struct ifnet *ub;
  struct ifnet *lb;
}

```
#### __firebloom::wide_ptr.indexable.85

```c
struct __firebloom::wide_ptr.indexable .85 {
  const uint8_t *ptr;
  const uint8_t *ub;
}

```
#### __firebloom::wide_ptr.bidi_indexable.71

```c
struct __firebloom::wide_ptr.bidi_indexable .71 {
  struct ifmediareq32 *ptr;
  struct ifmediareq32 *ub;
  struct ifmediareq32 *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.120

```c
struct __firebloom::wide_ptr.bidi_indexable .120 {
  struct if_bond_partner_state *ptr;
  struct if_bond_partner_state *ub;
  struct if_bond_partner_state *lb;
}

```
#### devtimer_s

```diff

 struct devtimer_s {
 void* dt_callout;	
-devtimer_timeout_func dt_timeout_func;	
-devtimer_process_func dt_process_func;	
+ void (void*, void*, void*);* dt_timeout_func;	
+ void (struct devtimer_s*, devtimer_process_func_event);* dt_process_func;	
 void* dt_arg0;	
 void* dt_arg1;	
 void* dt_arg2;	

```
#### ndrv_multiaddr

```diff

 struct ndrv_multiaddr {
 struct ndrv_multiaddr* next;	
-ifmultiaddr_t ifma;	
+struct ifmultiaddr* ifma;	
 struct sockaddr* addr;	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.8

```c
struct __firebloom::wide_ptr.bidi_indexable .8 {
  const char *ptr;
  const char *ub;
  const char *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.66

```c
struct __firebloom::wide_ptr.bidi_indexable .66 {
  uint8_t *ptr;
  uint8_t *ub;
  uint8_t *lb;
}

```
#### __firebloom::wide_ptr.indexable.70

```c
struct __firebloom::wide_ptr.indexable .70 {
  uint8_t *ptr;
  uint8_t *ub;
}

```
#### ndrv_protocol_desc_kernel

```c
struct ndrv_protocol_desc_kernel {
  u_int32_t                            version;
  u_int32_t                            protocol_family;
  u_int32_t                            demux_count;
  __firebloom::counted_by::demux_count demux_array;
}

```
#### route_event

```diff

 }
  rt_addr;	
 uint32_t route_event_code;	
-eventhandler_tag evtag;	
+struct eventhandler_entry* evtag;	
 }

```
#### __firebloom::wide_ptr.indexable.44

```c
struct __firebloom::wide_ptr.indexable .44 {
  char *ptr;
  char *ub;
}

```
#### eventhandler_entry_route_event

```diff

 struct eventhandler_entry_route_event {
 struct eventhandler_entry ee;	
-route_event_fn eh_func;	
+ void (struct eventhandler_entry_arg, struct sockaddr*, int, struct sockaddr*, int);* eh_func;	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.63

```c
struct __firebloom::wide_ptr.bidi_indexable .63 {
  struct domain *ptr;
  struct domain *ub;
  struct domain *lb;
}

```
#### __firebloom::wide_ptr.indexable.26

```c
struct __firebloom::wide_ptr.indexable .26 {
  uint8_t *ptr;
  uint8_t *ub;
}

```
#### __firebloom::wide_ptr.indexable.32

```c
struct __firebloom::wide_ptr.indexable .32 {
  const void *ptr;
  const void *ub;
}

```
#### __firebloom::wide_ptr.bidi_indexable.27

```c
struct __firebloom::wide_ptr.bidi_indexable .27 {
  struct sockaddr *ptr;
  struct sockaddr *ub;
  struct sockaddr *lb;
}

```
#### rt_msghdr_common

```c
struct rt_msghdr_common {
  u_short rtm_msglen;
  u_char  rtm_version;
  u_char  rtm_type;
  u_short rtm_index;
  int     rtm_flags;
  int     rtm_addrs;
  pid_t   rtm_pid;
  int     rtm_seq;
  int     rtm_errno;
  int     rtm_use;
}

```
#### kern_ctl_reg

```diff

 u_int32_t ctl_flags;	
 u_int32_t ctl_sendsize;	
 u_int32_t ctl_recvsize;	
-ctl_connect_func ctl_connect;	
-ctl_disconnect_func ctl_disconnect;	
-ctl_send_func ctl_send;	
-ctl_setopt_func ctl_setopt;	
-ctl_getopt_func ctl_getopt;	
-ctl_rcvd_func ctl_rcvd;	
-ctl_send_list_func ctl_send_list;	
-ctl_bind_func ctl_bind;	
-ctl_setup_func ctl_setup;	
+ errno_t (void*, struct sockaddr_ctl*, void**);* ctl_connect;	
+ errno_t (void*, u_int32_t, void*);* ctl_disconnect;	
+ errno_t (void*, u_int32_t, void*, struct mbuf*, int);* ctl_send;	
+ errno_t (void*, u_int32_t, void*, int, void*, size_t);* ctl_setopt;	
+ errno_t (void*, u_int32_t, void*, int, void*, size_t*);* ctl_getopt;	
+ void (void*, u_int32_t, void*, int);* ctl_rcvd;	
+ errno_t (void*, u_int32_t, void*, struct mbuf*, int);* ctl_send_list;	
+ errno_t (void*, struct sockaddr_ctl*, void**);* ctl_bind;	
+ errno_t (u_int32_t*, void**);* ctl_setup;	
 }

```
#### nstat_provider

```diff

 struct nstat_provider* next;	
 nstat_provider_id_t nstat_provider_id;	
 size_t nstat_descriptor_length;	
- errno_t (const void*, u_int32_t, nstat_provider_cookie_t*);* nstat_lookup;	
- int (nstat_provider_cookie_t);* nstat_gone;	
- errno_t (nstat_provider_cookie_t, struct nstat_counts*, int*);* nstat_counts;	
- errno_t (nstat_control_state*, nstat_msg_add_all_srcs*);* nstat_watcher_add;	
- void (nstat_control_state*);* nstat_watcher_remove;	
- errno_t (nstat_provider_cookie_t, void*, size_t);* nstat_copy_descriptor;	
- void (nstat_provider_cookie_t, boolean_t);* nstat_release;	
- _Bool (nstat_provider_cookie_t, nstat_provider_filter*, u_int64_t);* nstat_reporting_allowed;	
- _Bool (nstat_provider_cookie_t, nstat_provider_cookie_t);* nstat_cookie_equal;	
- size_t (nstat_provider_cookie_t, u_int32_t, void*, size_t);* nstat_copy_extension;	
+ errno_t (__firebloom::sized_by::length, u_int32_t, void**);* nstat_lookup;	
+ int (void*);* nstat_gone;	
+ errno_t (void*, struct nstat_counts*, int*);* nstat_counts;	
+ errno_t (nstat_client*, nstat_msg_add_all_srcs*);* nstat_watcher_add;	
+ void (nstat_client*);* nstat_watcher_remove;	
+ errno_t (void*, __firebloom::sized_by::len, size_t);* nstat_copy_descriptor;	
+ void (void*, boolean_t);* nstat_release;	
+ _Bool (void*, nstat_provider_filter*, u_int64_t);* nstat_reporting_allowed;	
+ _Bool (void*, void*);* nstat_cookie_equal;	
+ size_t (void*, u_int32_t, void*, size_t);* nstat_copy_extension;	
 }

```
#### nstat_client

```c
struct nstat_client {
  struct nstat_client      *ntc_next;
  u_int32_t                 ntc_watching;
  u_int32_t                 ntc_added_src;
  lck_mtx_t                 ntc_user_mtx;
  void                     *ntc_kctl;
  u_int32_t                 ntc_unit;
  nstat_src_ref_t           ntc_next_srcref;
  tailq_head_nstat_src      ntc_src_queue;
  struct mbuf              *ntc_accumulated;
  u_int32_t                 ntc_flags;
  nstat_provider_filter     ntc_provider_filters[11];
  u_int64_t                 ntc_context;
  u_int64_t                 ntc_seq;
  struct nstat_procdetails *ntc_procdetails;
  struct nstat_metrics      ntc_metrics;
}

```
#### nstat_src

```diff

 struct nstat_src {
-tailq_entry_nstat_src ns_control_link;	
-nstat_control_state* ns_control;	
-nstat_src_ref_t srcref;	
-nstat_provider* provider;	
-nstat_provider_cookie_t cookie;	
-uint32_t filter;	
-_Bool ns_reported;	
-uint64_t seq;	
+tailq_entry_nstat_src nts_client_link;	
+nstat_client* nts_client;	
+nstat_src_ref_t nts_srcref;	
+nstat_provider* nts_provider;	
+void* nts_cookie;	
+uint32_t nts_filter;	
+_Bool nts_reported;	
+uint64_t nts_seq;	
 }

```
#### nstat_metrics

```c
struct nstat_metrics {
  uint32_t nstat_src_current;
  uint32_t nstat_src_max;
  uint32_t nstat_first_uint32_count;
  uint32_t nstat_query_request_all;
  uint32_t nstat_query_request_one;
  uint32_t nstat_query_description_all;
  uint32_t nstat_query_description_one;
  uint32_t nstat_query_update_all;
  uint32_t nstat_query_update_one;
  uint32_t nstat_remove_src_found;
  uint32_t nstat_remove_src_missed;
  uint32_t nstat_query_request_nobuf;
  uint32_t nstat_query_request_upgrade;
  uint32_t nstat_query_request_noupgrade;
  uint32_t nstat_query_request_nodesc;
  uint32_t nstat_query_request_yield;
  uint32_t nstat_query_request_limit;
  uint32_t nstat_query_description_nobuf;
  uint32_t nstat_query_description_yield;
  uint32_t nstat_query_description_limit;
  uint32_t nstat_query_update_nobuf;
  uint32_t nstat_query_update_upgrade;
  uint32_t nstat_query_update_noupgrade;
  uint32_t nstat_query_update_nodesc;
  uint32_t nstat_query_update_yield;
  uint32_t nstat_query_update_limit;
  uint32_t nstat_src_add_success;
  uint32_t nstat_src_add_no_buf;
  uint32_t nstat_src_add_no_src_mem;
  uint32_t nstat_src_add_send_err;
  uint32_t nstat_src_add_while_cleanup;
  uint32_t nstat_src_gone_idlecheck;
  uint32_t nstat_last_uint32_count;
  uint32_t nstat_stats_pad;
}

```
#### nstat_global_counts

```c
struct nstat_global_counts {
  uint64_t nstat_global_client_current;
  uint64_t nstat_global_client_max;
  uint64_t nstat_global_client_allocs;
  uint64_t nstat_global_src_current;
  uint64_t nstat_global_src_max;
  uint64_t nstat_global_src_allocs;
  uint64_t nstat_global_src_idlecheck_gone;
  uint64_t nstat_global_tucookie_current;
  uint64_t nstat_global_tucookie_max;
  uint64_t nstat_global_tucookie_allocs;
  uint64_t nstat_global_tucookie_skip_dead;
  uint64_t nstat_global_tucookie_skip_stopusing;
  uint64_t nstat_global_tucookie_alloc_fail;
  uint64_t nstat_global_tu_shad_current;
  uint64_t nstat_global_tu_shad_max;
  uint64_t nstat_global_tu_shad_allocs;
  uint64_t nstat_global_gshad_current;
  uint64_t nstat_global_gshad_max;
  uint64_t nstat_global_gshad_allocs;
  uint64_t nstat_global_procdetails_current;
  uint64_t nstat_global_procdetails_max;
  uint64_t nstat_global_procdetails_allocs;
}

```
#### nstat_tu_shadow

```diff

 tailq_entry_tu_shadow shad_link;	
 userland_stats_request_vals_fn* shad_getvals_fn;	
 userland_stats_request_extension_fn* shad_get_extension_fn;	
-userland_stats_provider_context* shad_provider_context;	
+void** shad_provider_context;	
 u_int64_t shad_properties;	
 u_int64_t shad_start_timestamp;	
 nstat_provider_id_t shad_provider;	

```
#### nstat_generic_shadow

```diff

 struct nstat_generic_shadow {
 tailq_entry_generic_shadow gshad_link;	
-nstat_provider_context gshad_provider_context;	
+void* gshad_provider_context;	
 nstat_provider_request_vals_fn* gshad_getvals_fn;	
 nstat_provider_request_extensions_fn* gshad_getextensions_fn;	
 u_int64_t gshad_properties;	

```
#### nstat_tucookie

```diff

 struct nstat_tucookie {
 struct inpcb* inp;	
-char pname[17];	
+char pname[33];	
 _Bool cached;	
 union {
 struct sockaddr_in v4;	

```
#### inpcb

```diff

 uint64_t inp_fadv_total_time;	
 uint64_t inp_fadv_start_time;	
 uint64_t inp_fadv_cnt;	
-caddr_t inp_saved_ppcb;	
+char* inp_saved_ppcb;	
 struct inpcbpolicy* inp_sp;	
 struct inp_necp_attributes inp_necp_attributes;	
 struct necp_inpcb_result inp_policyresult;	
 uuid_t necp_client_uuid;	
-necp_client_flow_cb necp_cb;	
-uint8_t* inp_resolver_signature;	
+ void (void*, int, uint32_t, uint32_t, _Bool*);* necp_cb;	
 size_t inp_resolver_signature_length;	
-netns_token inp_netns_token;	
-netns_token inp_wildcard_netns_token;	
-u_char* inp_keepalive_data;	
+__firebloom::sized_by::inp_resolver_signature_length inp_resolver_signature;	
+struct ns_token* inp_netns_token;	
+struct ns_token* inp_wildcard_netns_token;	
+__firebloom::sized_by::inp_keepalive_datalen inp_keepalive_data;	
 uint8_t inp_keepalive_datalen;	
 uint8_t inp_keepalive_type;	
 uint16_t inp_keepalive_interval;	

 struct inp_stat* inp_cstat;	
 struct inp_stat* inp_wstat;	
 struct inp_stat* inp_Wstat;	
+struct inp_stat* inp_btstat;	
 uint8_t inp_stat_store[40];	
 uint8_t inp_cstat_store[40];	
 uint8_t inp_wstat_store[40];	
 uint8_t inp_Wstat_store[40];	
+uint8_t inp_btstat_store[40];	
 activity_bitmap_t inp_nw_activity;	
 uint64_t inp_start_timestamp;	
 uint64_t inp_connect_timestamp;	

```
#### inpcbinfo

```diff

 struct inpcbinfo** tqe_prev;	
 }
  ipi_entry;	
-inpcb_timer_func_t ipi_gc;	
-inpcb_timer_func_t ipi_timer;	
+ void (struct inpcbinfo*);* ipi_gc;	
+ void (struct inpcbinfo*);* ipi_timer;	
 struct intimercount ipi_gc_req;	
 struct intimercount ipi_timer_req;	
 lck_rw_t ipi_lock;	

 uint16_t ipi_lastport;	
 uint16_t ipi_lastlow;	
 uint16_t ipi_lasthi;	
-kalloc_type_view_t ipi_zone;	
-struct inpcbhead* ipi_hashbase;	
+struct kalloc_type_view* ipi_zone;	
+__firebloom::counted_by::ipi_hashbase_count ipi_hashbase;	
+size_t ipi_hashbase_count;	
 u_long ipi_hashmask;	
-struct inpcbporthead* ipi_porthashbase;	
+__firebloom::counted_by::ipi_porthashbase_count ipi_porthashbase;	
+size_t ipi_porthashbase_count;	
 u_long ipi_porthashmask;	
 lck_attr_t ipi_lock_attr;	
 lck_grp_t* ipi_lock_grp;	

```
#### ip_moptions

```diff

 u_char imo_multicast_loop;	
 u_short imo_num_memberships;	
 u_short imo_max_memberships;	
-struct in_multi** imo_membership;	
-struct in_mfilter* imo_mfilters;	
+u_short imo_max_filters;	
+__firebloom::counted_by::imo_max_memberships imo_membership;	
+__firebloom::counted_by::imo_max_filters imo_mfilters;	
 u_int32_t imo_multicast_vif;	
 struct in_addr imo_multicast_addr;	
  void (struct ip_moptions*, int);* imo_trace;	

```
#### ip6_moptions

```diff

 u_char im6o_multicast_loop;	
 u_short im6o_num_memberships;	
 u_short im6o_max_memberships;	
-struct in6_multi** im6o_membership;	
-struct in6_mfilter* im6o_mfilters;	
+u_short im6o_max_filters;	
+__firebloom::counted_by::im6o_max_memberships im6o_membership;	
+__firebloom::counted_by::im6o_max_filters im6o_mfilters;	
  void (struct ip6_moptions*, int);* im6o_trace;	
 }

```
#### secpolicy

```diff

 u_int state;	
 u_int policy;	
 struct ipsecrequest* req;	
-ifnet_t ipsec_if;	
-ifnet_t outgoing_if;	
+struct ifnet* ipsec_if;	
+struct ifnet* outgoing_if;	
 char disabled;	
 u_int64_t created;	
 u_int64_t lastused;	

```
#### secpolicyindex

```diff

 u_int8_t prefs;	
 u_int8_t prefd;	
 u_int8_t ul_proto;	
-ifnet_t internal_if;	
+struct ifnet* internal_if;	
 struct secpolicyaddrrange src_range;	
 struct secpolicyaddrrange dst_range;	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.84

```diff

 struct __firebloom::wide_ptr.bidi_indexable.84 {
-struct ifnet* ptr;	
-struct ifnet* ub;	
-struct ifnet* lb;	
+struct xtcpcb_n* ptr;	
+struct xtcpcb_n* ub;	
+struct xtcpcb_n* lb;	
 }

```
#### __firebloom::wide_ptr.indexable.106

```c
struct __firebloom::wide_ptr.indexable .106 {
  char *ptr;
  char *ub;
}

```
#### tcpcb

```diff

 struct tsegqe_head t_segq;	
 uint32_t t_dupacks;	
 int t_state;	
-uint32_t t_timer[9];	
+uint32_t t_timer[10];	
 struct tcptimerentry tentry;	
 struct inpcb* t_inpcb;	
 uint32_t t_flags;	

 u_int32_t ts_recent;	
 u_int32_t ts_recent_age;	
 tcp_seq last_ack_sent;	
-u_int32_t t_bytes_acked;	
+uint32_t t_bytes_acked;	
+uint32_t total_ect_packets_marked;	
+uint32_t total_ect_packets_acked;	
 int t_lastchain;	
 uint16_t t_unacksegs;	
 uint16_t t_unacksegs_ce;	

 uint64_t t_ecn_capable_packets_acked;	
 uint64_t t_ecn_capable_packets_marked;	
 uint64_t t_ecn_capable_packets_lost;	
+uint32_t t_last_ack_tsecr;	
 uint16_t t_prev_ace_flags;	
 uint8_t t_prev_ip_ecn;	
-uint32_t t_rcv_ce_packets;	
-uint32_t t_snd_ce_packets;	
-uint32_t t_delta_ce_packets;	
-uint64_t t_rcv_ect1_bytes;	
-uint64_t t_rcv_ect0_bytes;	
-uint64_t t_rcv_ce_bytes;	
-uint64_t t_snd_ect1_bytes;	
-uint64_t t_snd_ect0_bytes;	
-uint64_t t_snd_ce_bytes;	
+struct accecn t_aecn;	
+struct pacer t_pacer;	
 u_int32_t snd_cwnd_prev;	
 u_int32_t snd_ssthresh_prev;	
 tcp_seq snd_recover_prev;	

 u_int32_t t_badrexmt_time;	
 u_int32_t t_reorderwin;	
 int16_t snd_numholes;	
-tcp_seq sack_newdata;	
 struct sackhole_head snd_holes;	
 tcp_seq snd_fack;	
 int rcv_numsacks;	
 struct sackblk sackblks[6];	
 struct sackhint sackhint;	
-tcp_seq send_highest_sack;	
-int t_new_dupacks;	
 struct mbuf* t_pktlist_head;	
 struct mbuf* t_pktlist_tail;	
 u_int32_t t_pktlist_sentlen;	

 struct tcp_ccstate* t_ccstate;	
 struct tcp_ccstate _t_ccstate;	
 tcp_seq t_tlphighrxt;	
+tcp_seq t_tlphightrxt_persist;	
 u_int32_t t_tlpstart;	
 tcp_seq t_dsack_lseq;	
 tcp_seq t_dsack_rseq;	

 u_int32_t t_rcvoopack;	
 u_int32_t t_pawsdrop;	
 u_int32_t t_sack_recovery_episode;	
+uint32_t t_rack_recovery_episode;	
+uint32_t t_rack_reo_timeout_recovery_episode;	
 u_int32_t t_reordered_pkts;	
 u_int32_t t_dsack_sent;	
 u_int32_t t_dsack_recvd;	

 uint32_t rcv_srtt;	
 uint32_t rcv_rtt_est_ts;	
 uint32_t rcv_rtt_est_seq;	
+struct tcp_seg_sent_head t_segs_sent;	
+struct tcp_seg_sent_tree_head t_segs_sent_tree;	
+struct tcp_seg_acked_head t_segs_acked;	
+struct tcp_seg_pool seg_pool;	
+struct tcp_rack rack;	
+uint32_t bytes_lost;	
+uint32_t bytes_retransmitted;	
+uint32_t bytes_sacked;	
 uuid_t t_fsw_uuid;	
 uuid_t t_flow_uuid;	
 }

```
#### accecn

```c
struct accecn {
  uint32_t t_rcv_ce_packets;
  uint32_t t_snd_ce_packets;
  uint32_t t_delta_ce_packets;
  uint8_t  accecn_processed;
  uint8_t  unused;
  uint64_t t_rcv_ect1_bytes;
  uint64_t t_rcv_ect0_bytes;
  uint64_t t_rcv_ce_bytes;
  uint64_t t_snd_ect1_bytes;
  uint64_t t_snd_ect0_bytes;
  uint64_t t_snd_ce_bytes;
}

```
#### pacer

```c
struct pacer {
  uint64_t rate;
  uint32_t tso_burst_size;
  uint64_t packet_tx_time;
}

```
#### tcp_ccstate

```diff

 struct tcp_ccstate {
 union {
 struct tcp_cubic_state _cubic_state_;	
+struct tcp_prague_state _prague_state_;	
 struct tcp_ledbat_state _ledbat_state_;	
 }
  __u__;	

```
#### tcp_prague_state

```c
struct tcp_prague_state {
  uint16_t               num_cong_events_loss;
  uint16_t               num_cong_events_ce;
  uint32_t               packets_acked;
  uint32_t               packets_marked;
  uint32_t               ce_counter;
  uint32_t               bytes_acked;
  uint32_t               snd_nxt_alpha;
  uint32_t               snd_nxt_cwr;
  uint8_t                ever_saw_ce;
  uint8_t                in_loss;
  uint8_t                reduced_due_to_ce;
  uint8_t                unused;
  uint8_t                pad[3];
  uint64_t               scaled_alpha;
  uint64_t               alpha_ai;
  struct tcp_cubic_state cubic_state;
}

```
#### tcp_seg_sent_head

```c
struct tcp_seg_sent_head {
  struct tcp_seg_sent  *tqh_first;
  struct tcp_seg_sent **tqh_last;
}

```
#### tcp_seg_sent

```c
struct tcp_seg_sent {
  tcp_seq  start_seq;
  tcp_seq  end_seq;
  uint32_t xmit_ts;
  uint8_t  flags;
  uint8_t  pad[3];
  struct {
    struct tcp_seg_sent  *tqe_next;
    struct tcp_seg_sent **tqe_prev;
  } tx_link;
  struct {
    struct tcp_seg_sent *rbe_left;
    struct tcp_seg_sent *rbe_right;
    struct tcp_seg_sent *rbe_parent;
  } seg_link;
  struct {
    struct tcp_seg_sent  *tqe_next;
    struct tcp_seg_sent **tqe_prev;
  } ack_link;
  struct {
    struct tcp_seg_sent  *tqe_next;
    struct tcp_seg_sent **tqe_prev;
  } free_link;
}

```
#### tcp_seg_sent_tree_head

```c
struct tcp_seg_sent_tree_head {
  struct tcp_seg_sent *rbh_root;
}

```
#### tcp_seg_acked_head

```c
struct tcp_seg_acked_head {
  struct tcp_seg_sent  *tqh_first;
  struct tcp_seg_sent **tqh_last;
}

```
#### tcp_seg_pool

```c
struct tcp_seg_pool {
  struct {
    struct tcp_seg_sent  *tqh_first;
    struct tcp_seg_sent **tqh_last;
  } free_segs;
  uint32_t free_segs_count;
  char     pad[4];
}

```
#### tcp_rack

```c
struct tcp_rack {
  uint32_t xmit_ts;
  uint32_t end_seq;
  uint32_t rtt;
  tcp_seq  dsack_round_end;
  uint32_t reo_wnd;
  uint8_t  reo_wnd_multi;
  uint8_t  reo_wnd_persist;
  uint8_t  advanced;
  uint8_t  dsack_round_seen;
  uint8_t  segs_retransmitted;
}

```
#### nstat_interface_counts

```c
struct nstat_interface_counts {
  u_int64_t nstat_rxpackets;
  u_int64_t nstat_rxbytes;
  u_int64_t nstat_txpackets;
  u_int64_t nstat_txbytes;
}

```
#### __firebloom::wide_ptr.bidi_indexable.134

```c
struct __firebloom::wide_ptr.bidi_indexable .134 {
  nstat_connection_descriptor *ptr;
  nstat_connection_descriptor *ub;
  nstat_connection_descriptor *lb;
}

```
#### __firebloom::wide_ptr.indexable.110

```c
struct __firebloom::wide_ptr.indexable .110 {
  uint8_t *ptr;
  uint8_t *ub;
}

```
#### __firebloom::wide_ptr.bidi_indexable.157

```c
struct __firebloom::wide_ptr.bidi_indexable .157 {
  nstat_ifnet_descriptor *ptr;
  nstat_ifnet_descriptor *ub;
  nstat_ifnet_descriptor *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.168

```c
struct __firebloom::wide_ptr.bidi_indexable .168 {
  nstat_msg_sysinfo_counts *ptr;
  nstat_msg_sysinfo_counts *ub;
  nstat_msg_sysinfo_counts *lb;
}

```
#### __firebloom::wide_ptr.indexable.171

```c
struct __firebloom::wide_ptr.indexable .171 {
  struct nstat_sysinfo_keyval *ptr;
  struct nstat_sysinfo_keyval *ub;
}

```
#### __firebloom::wide_ptr.bidi_indexable.177

```c
struct __firebloom::wide_ptr.bidi_indexable .177 {
  nstat_msg_src_extended_item_hdr *ptr;
  nstat_msg_src_extended_item_hdr *ub;
  nstat_msg_src_extended_item_hdr *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.192

```c
struct __firebloom::wide_ptr.bidi_indexable .192 {
  struct nstat_msg_hdr *ptr;
  struct nstat_msg_hdr *ub;
  struct nstat_msg_hdr *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.194

```c
struct __firebloom::wide_ptr.bidi_indexable .194 {
  nstat_msg_add_src_req *ptr;
  nstat_msg_add_src_req *ub;
  nstat_msg_add_src_req *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.197

```c
struct __firebloom::wide_ptr.bidi_indexable .197 {
  nstat_msg_add_all_srcs *ptr;
  nstat_msg_add_all_srcs *ub;
  nstat_msg_add_all_srcs *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.203

```c
struct __firebloom::wide_ptr.bidi_indexable .203 {
  nstat_msg_src_added *ptr;
  nstat_msg_src_added *ub;
  nstat_msg_src_added *lb;
}

```
#### nstat_progress_indicators

```c
struct nstat_progress_indicators {
  u_int32_t np_numflows;
  u_int32_t np_conn_probe_fails;
  u_int32_t np_read_probe_fails;
  u_int32_t np_write_probe_fails;
  u_int32_t np_recentflows;
  u_int32_t np_recentflows_unacked;
  u_int64_t np_recentflows_rxbytes;
  u_int64_t np_recentflows_txbytes;
  u_int64_t np_recentflows_rxooo;
  u_int64_t np_recentflows_rxdup;
  u_int64_t np_recentflows_retx;
  u_int64_t np_reserved1;
  u_int64_t np_reserved2;
  u_int64_t np_reserved3;
  u_int64_t np_reserved4;
}

```
#### __firebloom::wide_ptr.bidi_indexable.121

```diff

 struct __firebloom::wide_ptr.bidi_indexable.121 {
-struct in_ifaddr* ptr;	
-struct in_ifaddr* ub;	
-struct in_ifaddr* lb;	
+struct inpcb* ptr;	
+struct inpcb* ub;	
+struct inpcb* lb;	
 }

```
#### __firebloom::wide_ptr.indexable.196

```c
struct __firebloom::wide_ptr.indexable .196 {
  struct nstat_msg_add_src *ptr;
  struct nstat_msg_add_src *ub;
}

```
#### __firebloom::wide_ptr.indexable.139

```c
struct __firebloom::wide_ptr.indexable .139 {
  struct nstat_msg_src_description *ptr;
  struct nstat_msg_src_description *ub;
}

```
#### __firebloom::wide_ptr.indexable.176

```c
struct __firebloom::wide_ptr.indexable .176 {
  struct nstat_msg_src_update *ptr;
  struct nstat_msg_src_update *ub;
}

```
#### __firebloom::wide_ptr.bidi_indexable.187

```c
struct __firebloom::wide_ptr.bidi_indexable .187 {
  struct nstat_sysinfo_net_api_stats *ptr;
  struct nstat_sysinfo_net_api_stats *ub;
  struct nstat_sysinfo_net_api_stats *lb;
}

```
#### __firebloom::wide_ptr.indexable.172

```c
struct __firebloom::wide_ptr.indexable .172 {
  struct nstat_msg_sysinfo_counts *ptr;
  struct nstat_msg_sysinfo_counts *ub;
}

```
#### __firebloom::wide_ptr.bidi_indexable.126

```diff

 struct __firebloom::wide_ptr.bidi_indexable.126 {
-struct ifqueue* ptr;	
-struct ifqueue* ub;	
-struct ifqueue* lb;	
+struct socket* ptr;	
+struct socket* ub;	
+struct socket* lb;	
 }

```
#### nstat_progress_req

```c
struct nstat_progress_req {
  u_int64_t np_ifindex;
  u_int64_t np_recentflow_maxduration;
  u_int64_t np_filter_flags;
  u_int64_t np_transport_protocol_mask;
}

```
#### __firebloom::wide_ptr.bidi_indexable.190

```c
struct __firebloom::wide_ptr.bidi_indexable .190 {
  nstat_client **ptr;
  nstat_client **ub;
  nstat_client **lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.159

```c
struct __firebloom::wide_ptr.bidi_indexable .159 {
  struct if_link_status *ptr;
  struct if_link_status *ub;
  struct if_link_status *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.163

```c
struct __firebloom::wide_ptr.bidi_indexable .163 {
  nstat_ifnet_desc_link_status *ptr;
  nstat_ifnet_desc_link_status *ub;
  nstat_ifnet_desc_link_status *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.166

```diff

 struct __firebloom::wide_ptr.bidi_indexable.166 {
-struct mbuf* ptr;	
-struct mbuf* ub;	
-struct mbuf* lb;	
+nstat_ifnet_desc_wifi_status* ptr;	
+nstat_ifnet_desc_wifi_status* ub;	
+nstat_ifnet_desc_wifi_status* lb;	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.164

```c
struct __firebloom::wide_ptr.bidi_indexable .164 {
  nstat_ifnet_desc_cellular_status *ptr;
  nstat_ifnet_desc_cellular_status *ub;
  nstat_ifnet_desc_cellular_status *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.165

```c
struct __firebloom::wide_ptr.bidi_indexable .165 {
  struct if_cellular_status_v1 *ptr;
  struct if_cellular_status_v1 *ub;
  struct if_cellular_status_v1 *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.65

```c
struct __firebloom::wide_ptr.bidi_indexable .65 {
  const uint8_t *ptr;
  const uint8_t *ub;
  const uint8_t *lb;
}

```
#### gif_softc

```diff

 struct gif_softc {
-ifnet_t gif_if;	
+struct ifnet* gif_if;	
 struct sockaddr* gif_psrc;	
 struct sockaddr* gif_pdst;	
 protocol_family_t gif_proto;	

 }
  gif_link;	
 bpf_tap_mode tap_mode;	
-bpf_packet_func tap_callback;	
+ errno_t (struct ifnet*, struct mbuf*);* tap_callback;	
 char gif_ifname[16];	
 lck_mtx_t gif_lock;	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.72

```c
struct __firebloom::wide_ptr.bidi_indexable .72 {
  struct in6_aliasreq_64 *ptr;
  struct in6_aliasreq_64 *ub;
  struct in6_aliasreq_64 *lb;
}

```
#### in6_ifreq

```diff

 int ifru_flags6;	
 int ifru_metric;	
 int ifru_intval;	
-caddr_t ifru_data;	
+char* ifru_data;	
 struct in6_addrlifetime ifru_lifetime;	
 struct in6_ifstat ifru_stat;	
 struct icmp6_ifstat ifru_icmp6stat;	

```
#### __firebloom::wide_ptr.indexable.74

```c
struct __firebloom::wide_ptr.indexable .74 {
  uint8_t *ptr;
  uint8_t *ub;
}

```
#### __firebloom::wide_ptr.indexable.78

```c
struct __firebloom::wide_ptr.indexable .78 {
  void *ptr;
  void *ub;
}

```
#### __firebloom::wide_ptr.bidi_indexable.73

```c
struct __firebloom::wide_ptr.bidi_indexable .73 {
  const uint8_t *ptr;
  const uint8_t *ub;
  const uint8_t *lb;
}

```
#### stf_softc

```diff

 struct stf_softc {
-ifnet_t sc_if;	
+struct ifnet* sc_if;	
 u_int32_t sc_protocol_family;	
 union {
 struct route __sc_ro4;	

 lck_mtx_t sc_ro_mtx;	
 const struct encaptab* encap_cookie;	
 bpf_tap_mode tap_mode;	
-bpf_packet_func tap_callback;	
+ errno_t (struct ifnet*, struct mbuf*);* tap_callback;	
 }

```
#### if_ports_used_stats

```diff

 uint64_t ifpu_npi_not_added_no_wakeuuid;	
 uint64_t ifpu_deferred_isakmp_natt_wake_pkt;	
 uint64_t ifpu_spurious_wake_event;	
+uint64_t ifpu_delayed_attributed_wake_event;	
+uint64_t ifpu_delayed_unattributed_wake_event;	
+uint64_t ifpu_delayed_wake_event_undelivered;	
 }

```
#### net_port_info_wake_pkt_event

```c
struct net_port_info_wake_pkt_event {
  uint32_t npi_wp_code;
  uint32_t npi_wp_flags;
  union {
    struct net_port_info_wake_event     _npi_ev_wake_pkt_attributed;
    struct net_port_info_una_wake_event _npi_ev_wake_pkt_unattributed;
  } npi_ev_wake_pkt_;
}

```
#### __firebloom::wide_ptr.bidi_indexable.7

```c
struct __firebloom::wide_ptr.bidi_indexable .7 {
  const char *ptr;
  const char *ub;
  const char *lb;
}

```
#### ifnet_init_params

```diff

 struct ifnet_init_params {
-const void* uniqueid;	
+__firebloom::sized_by::uniqueid_len uniqueid;	
 u_int32_t uniqueid_len;	
 const char* name;	
 u_int32_t unit;	
 ifnet_family_t family;	
 u_int32_t type;	
-ifnet_output_func output;	
-ifnet_demux_func demux;	
-ifnet_add_proto_func add_proto;	
-ifnet_del_proto_func del_proto;	
-ifnet_check_multi check_multi;	
-ifnet_framer_func framer;	
+ errno_t (struct ifnet*, struct mbuf*);* output;	
+ errno_t (struct ifnet*, struct mbuf*, char*, protocol_family_t*);* demux;	
+ errno_t (struct ifnet*, protocol_family_t, __firebloom::counted_by::demux_count, u_int32_t);* add_proto;	
+ errno_t (struct ifnet*, protocol_family_t);* del_proto;	
+ errno_t (struct ifnet*, const struct sockaddr*);* check_multi;	
+ errno_t (struct ifnet*, struct mbuf**, const struct sockaddr*, const char*, const char*);* framer;	
 void* softc;	
-ifnet_ioctl_func ioctl;	
-ifnet_set_bpf_tap set_bpf_tap;	
-ifnet_detached_func detach;	
-ifnet_event_func event;	
-const void* broadcast_addr;	
+ errno_t (struct ifnet*, unsigned long, void*);* ioctl;	
+ errno_t (struct ifnet*, bpf_tap_mode,  errno_t (struct ifnet*, struct mbuf*);*);* set_bpf_tap;	
+ void (struct ifnet*);* detach;	
+ void (struct ifnet*, const struct kev_msg*);* event;	
+__firebloom::sized_by::broadcast_len broadcast_addr;	
 u_int32_t broadcast_len;	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.26

```c
struct __firebloom::wide_ptr.bidi_indexable .26 {
  struct ifclassq *ptr;
  struct ifclassq *ub;
  struct ifclassq *lb;
}

```
#### __firebloom::wide_ptr.indexable.80

```c
struct __firebloom::wide_ptr.indexable .80 {
  const void *ptr;
  const void *ub;
}

```
#### __firebloom::wide_ptr.indexable.45

```c
struct __firebloom::wide_ptr.indexable .45 {
  uint8_t *ptr;
  uint8_t *ub;
}

```
#### __firebloom::wide_ptr.bidi_indexable.76

```c
struct __firebloom::wide_ptr.bidi_indexable .76 {
  struct kalloc_heap *ptr;
  struct kalloc_heap *ub;
  struct kalloc_heap *lb;
}

```
#### ifnet_clone_params

```diff

 struct ifnet_clone_params {
 const char* ifc_name;	
-ifnet_clone_create_func ifc_create;	
-ifnet_clone_destroy_func ifc_destroy;	
+ errno_t (struct if_clone*, u_int32_t, void*);* ifc_create;	
+ errno_t (struct ifnet*);* ifc_destroy;	
 }

```
#### proto_input_entry

```diff

 int hash;	
 int chain;	
 protocol_family_t protocol;	
-proto_input_handler input;	
-proto_input_detached_handler detached;	
-mbuf_t inject_first;	
-mbuf_t inject_last;	
+ void (protocol_family_t, struct mbuf*);* input;	
+ void (protocol_family_t);* detached;	
+struct mbuf* inject_first;	
+struct mbuf* inject_last;	
 struct proto_input_entry* input_next;	
-mbuf_t input_first;	
-mbuf_t input_last;	
+struct mbuf* input_first;	
+struct mbuf* input_last;	
 }

```
#### proto_family_str

```diff

  proto_fam_next;	
 protocol_family_t proto_family;	
 ifnet_family_t if_family;	
-proto_plumb_handler attach_proto;	
-proto_unplumb_handler detach_proto;	
+ errno_t (struct ifnet*, protocol_family_t);* attach_proto;	
+ void (struct ifnet*, protocol_family_t);* detach_proto;	
 }

```
#### net_str_id_entry

```diff

 struct net_str_id_entry* sle_next;	
 }
  nsi_next;	
-u_int32_t nsi_flags;	
-u_int32_t nsi_id;	
-char nsi_string[1];	
+uint32_t nsi_flags;	
+uint32_t nsi_id;	
+uint32_t nsi_length;	
+char nsi_string[-1];	
 }

```
#### utun_pcb

```diff

 struct utun_pcb** tqe_prev;	
 }
  utun_chain;	
-kern_ctl_ref utun_ctlref;	
-ifnet_t utun_ifp;	
+void* utun_ctlref;	
+struct ifnet* utun_ifp;	
 u_int32_t utun_unit;	
 u_int32_t utun_unique_id;	
 u_int32_t utun_flags;	

 uuid_t utun_kpipe_uuid;	
 void* utun_kpipe_rxring;	
 void* utun_kpipe_txring;	
-kern_pbufpool_t utun_kpipe_pp;	
+struct kern_pbufpool* utun_kpipe_pp;	
 u_int32_t utun_kpipe_tx_ring_size;	
 u_int32_t utun_kpipe_rx_ring_size;	
-kern_nexus_t utun_netif_nexus;	
-kern_pbufpool_t utun_netif_pp;	
+struct kern_nexus* utun_netif_nexus;	
+struct kern_pbufpool* utun_netif_pp;	
 void* utun_netif_rxring;	
 void* utun_netif_txring;	
 uint64_t utun_netif_txring_size;	

```
#### __firebloom::wide_ptr.bidi_indexable.87

```diff

 struct __firebloom::wide_ptr.bidi_indexable.87 {
-struct in6_mfilter* ptr;	
-struct in6_mfilter* ub;	
-struct in6_mfilter* lb;	
+struct __kern_buflet* ptr;	
+struct __kern_buflet* ub;	
+struct __kern_buflet* lb;	
 }

```
#### ipsec_pcb

```diff

 struct ipsec_pcb** tqe_prev;	
 }
  ipsec_chain;	
-kern_ctl_ref ipsec_ctlref;	
-ifnet_t ipsec_ifp;	
+void* ipsec_ctlref;	
+struct ifnet* ipsec_ifp;	
 u_int32_t ipsec_unit;	
 u_int32_t ipsec_unique_id;	
 u_int32_t ipsec_external_flags;	

 uuid_t ipsec_kpipe_uuid[4];	
 void* ipsec_kpipe_rxring[4];	
 void* ipsec_kpipe_txring[4];	
-kern_pbufpool_t ipsec_kpipe_pp;	
+struct kern_pbufpool* ipsec_kpipe_pp;	
 u_int32_t ipsec_kpipe_tx_ring_size;	
 u_int32_t ipsec_kpipe_rx_ring_size;	
-kern_nexus_t ipsec_netif_nexus;	
-kern_pbufpool_t ipsec_netif_pp;	
+struct kern_nexus* ipsec_netif_nexus;	
+struct kern_pbufpool* ipsec_netif_pp;	
 void* ipsec_netif_rxring[1];	
 void* ipsec_netif_txring[4];	
 uint64_t ipsec_netif_txring_size;	

```
#### ipsec_detached_channels

```diff

 struct ipsec_detached_channels {
 int count;	
-kern_pbufpool_t pp;	
+struct kern_pbufpool* pp;	
 uuid_t uuids[4];	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.129

```diff

 struct __firebloom::wide_ptr.bidi_indexable.129 {
-struct ip_msource* ptr;	
-struct ip_msource* ub;	
-struct ip_msource* lb;	
+struct ifnet* ptr;	
+struct ifnet* ub;	
+struct ifnet* lb;	
 }

```
#### necp_session_policy

```diff

 _Bool pending_update;	
 necp_policy_id local_id;	
 necp_policy_order order;	
-u_int8_t* result;	
 u_int32_t result_size;	
-u_int8_t* conditions;	
+__firebloom::sized_by::result_size result;	
 u_int32_t conditions_size;	
-u_int8_t* route_rules;	
+__firebloom::sized_by::conditions_size conditions;	
 u_int32_t route_rules_size;	
+__firebloom::sized_by::route_rules_size route_rules;	
 uuid_t applied_app_uuid;	
 uuid_t applied_real_app_uuid;	
-char* applied_account;	
 u_int32_t applied_account_size;	
+__firebloom::sized_by::applied_account_size applied_account;	
 uuid_t applied_result_uuid;	
 u_int32_t applied_route_rules_id;	
 necp_kernel_policy_id kernel_socket_policies[1];	

```
#### necp_kernel_socket_policy

```diff

 pid_t cond_pid;	
 uid_t cond_uid;	
 uid_t cond_real_uid;	
-ifnet_t cond_bound_interface;	
+struct ifnet* cond_bound_interface;	
 struct necp_policy_condition_tc_range cond_traffic_class;	
 u_int16_t cond_protocol;	
 union necp_sockaddr_union cond_local_start;	

```
#### necp_kernel_ip_output_policy

```diff

 u_int64_t condition_mask;	
 u_int64_t condition_negated_mask;	
 necp_kernel_policy_id cond_policy_id;	
-ifnet_t cond_bound_interface;	
+struct ifnet* cond_bound_interface;	
 u_int16_t cond_protocol;	
 union necp_sockaddr_union cond_local_start;	
 union necp_sockaddr_union cond_local_end;	

```
#### __firebloom::wide_ptr.indexable.41

```c
struct __firebloom::wide_ptr.indexable .41 {
  struct necp_kernel_ip_output_policy **ptr;
  struct necp_kernel_ip_output_policy **ub;
}

```
#### necp_route_rule

```diff

 u_int8_t expensive_action;	
 u_int8_t constrained_action;	
 u_int8_t companion_action;	
+u_int8_t vpn_action;	
 u_int exception_if_indices[10];	
 u_int8_t exception_if_actions[10];	
 os_refcnt_t refcount;	

```
#### necp_policy_condition_addr

```diff

 u_int8_t prefix;	
 union {
 struct sockaddr sa;	
-struct __sockaddr_header sah;	
 struct sockaddr_in sin;	
 struct sockaddr_in6 sin6;	
 }

```
#### __firebloom::wide_ptr.indexable.72

```c
struct __firebloom::wide_ptr.indexable .72 {
  void *ptr;
  void *ub;
}

```
#### __firebloom::wide_ptr.bidi_indexable.152

```diff

 struct __firebloom::wide_ptr.bidi_indexable.152 {
-struct kalloc_type_view* ptr;	
-struct kalloc_type_view* ub;	
-struct kalloc_type_view* lb;	
+struct ip6_hdr* ptr;	
+struct ip6_hdr* ub;	
+struct ip6_hdr* lb;	
 }

```
#### necp_policy_condition_addr_range

```diff

 struct necp_policy_condition_addr_range {
 union {
 struct sockaddr sa;	
-struct __sockaddr_header sah;	
 struct sockaddr_in sin;	
 struct sockaddr_in6 sin6;	
 }
  start_address;	
 union {
 struct sockaddr sa;	
-struct __sockaddr_header sah;	
 struct sockaddr_in sin;	
 struct sockaddr_in6 sin6;	
 }

```
#### __firebloom::wide_ptr.indexable.42

```c
struct __firebloom::wide_ptr.indexable .42 {
  u_int8_t *ptr;
  u_int8_t *ub;
}

```
#### __firebloom::wide_ptr.indexable.213

```c
struct __firebloom::wide_ptr.indexable .213 {
  struct __firebloom::wide_ptr.indexable .42 * ptr;
  struct __firebloom::wide_ptr.indexable .42 * ub;
}

```
#### __firebloom::wide_ptr.bidi_indexable.205

```c
struct __firebloom::wide_ptr.bidi_indexable .205 {
  struct net_bloom_filter *ptr;
  struct net_bloom_filter *ub;
  struct net_bloom_filter *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.158

```c
struct __firebloom::wide_ptr.bidi_indexable .158 {
  struct necp_session_policy *ptr;
  struct necp_session_policy *ub;
  struct necp_session_policy *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.201

```c
struct __firebloom::wide_ptr.bidi_indexable .201 {
  struct necp_domain_filter *ptr;
  struct necp_domain_filter *ub;
  struct necp_domain_filter *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.162

```c
struct __firebloom::wide_ptr.bidi_indexable .162 {
  struct kalloc_heap *ptr;
  struct kalloc_heap *ub;
  struct kalloc_heap *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.172

```c
struct __firebloom::wide_ptr.bidi_indexable .172 {
  struct necp_string_id_mapping *ptr;
  struct necp_string_id_mapping *ub;
  struct necp_string_id_mapping *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.154

```c
struct __firebloom::wide_ptr.bidi_indexable .154 {
  struct necp_aggregate_route_rule *ptr;
  struct necp_aggregate_route_rule *ub;
  struct necp_aggregate_route_rule *lb;
}

```
#### substring

```diff

 struct substring {
-char* string;	
 size_t length;	
+__firebloom::sized_by::length string;	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.223

```c
struct __firebloom::wide_ptr.bidi_indexable .223 {
  struct necp_drop_dest_entry *ptr;
  struct necp_drop_dest_entry *ub;
  struct necp_drop_dest_entry *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.156

```diff

 struct __firebloom::wide_ptr.bidi_indexable.156 {
-u_int16_t* ptr;	
-u_int16_t* ub;	
-u_int16_t* lb;	
+struct sockaddr_in6* ptr;	
+struct sockaddr_in6* ub;	
+struct sockaddr_in6* lb;	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.178

```c
struct __firebloom::wide_ptr.bidi_indexable .178 {
  struct necp_kernel_ip_output_policy **ptr;
  struct necp_kernel_ip_output_policy **ub;
  struct necp_kernel_ip_output_policy **lb;
}

```
#### necp_client_flow_registration

```diff

 unsigned int flow_result_read;	
 unsigned int defunct;	
 void* interface_handle;	
-necp_client_flow_cb interface_cb;	
+ void (void*, int, uint32_t, uint32_t, _Bool*);* interface_cb;	
 struct necp_client* client;	
 struct _necp_registration_flow_list flow_list;	
 struct necp_arena_info* stats_arena;	
 void* kstats_kaddr;	
 mach_vm_address_t ustats_uaddr;	
-nstat_userland_context stats_handler_context;	
+void* stats_handler_context;	
 struct flow_stats* nexus_stats;	
 u_int64_t last_interface_details;	
 }

```
#### necp_client

```diff

 struct _necp_client_flow_tree flow_registrations;	
 struct _necp_client_assertion_list assertion_list;	
 size_t assigned_group_members_length;	
-u_int8_t* assigned_group_members;	
+__firebloom::counted_by::assigned_group_members_length assigned_group_members;	
 struct rtentry* current_route;	
 struct necp_client_interface_option interface_options[4];	
-struct necp_client_interface_option* extra_interface_options;	
+struct __firebloom::wide_ptr.indexable extra_interface_options;	
 u_int8_t interface_option_count;	
 struct necp_client_result_netagent failed_trigger_agent;	
 void* agent_handle;	
 uuid_t override_euuid;	
-netns_token port_reservation;	
-nstat_context nstat_context;	
+struct ns_token* port_reservation;	
+void* nstat_context;	
 uuid_t latest_flow_registration_id;	
 uuid_t parent_client_id;	
 struct necp_client* original_parameters_source;	
 size_t parameters_length;	
-u_int8_t* parameters;	
+__firebloom::sized_by::parameters_length parameters;	
 }

```
#### necp_client_flow

```diff

 uuid_t nexus_agent;	
 struct {
 void* socket_handle;	
-necp_client_flow_cb cb;	
+ void (void*, int, uint32_t, uint32_t, _Bool*);* cb;	
 }
  ;	
 }

 union necp_sockaddr_union local_addr;	
 union necp_sockaddr_union remote_addr;	
 size_t assigned_results_length;	
-u_int8_t* assigned_results;	
+__firebloom::counted_by::assigned_results_length assigned_results;	
 }

```
#### necp_client_update

```diff

  chain;	
 uuid_t client_id;	
 size_t update_length;	
-struct necp_client_observer_update* update;	
+__firebloom::counted_by::update_length update;	
 }

```
#### __firebloom::wide_ptr.indexable.115

```c
struct __firebloom::wide_ptr.indexable .115 {
  void *ptr;
  void *ub;
}

```
#### __firebloom::wide_ptr.indexable.108

```c
struct __firebloom::wide_ptr.indexable .108 {
  char *ptr;
  char *ub;
}

```
#### __firebloom::wide_ptr.indexable.76

```c
struct __firebloom::wide_ptr.indexable .76 {
  u_int8_t *ptr;
  u_int8_t *ub;
}

```
#### necp_client_nexus_parameters

```diff

 pid_t pid;	
 pid_t epid;	
 uuid_t euuid;	
-netns_token port_reservation;	
+struct ns_token* port_reservation;	
 union necp_sockaddr_union local_addr;	
 union necp_sockaddr_union remote_addr;	
 u_int8_t ip_protocol;	

```
#### necp_client_group_members

```diff

 struct necp_client_group_members {
 size_t group_members_length;	
-u_int8_t* group_members;	
+__firebloom::sized_by::group_members_length group_members;	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.170

```c
struct __firebloom::wide_ptr.bidi_indexable .170 {
  struct necp_quic_stats *ptr;
  struct necp_quic_stats *ub;
  struct necp_quic_stats *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.137

```diff

 struct __firebloom::wide_ptr.bidi_indexable.137 {
-struct icmp6_hdr* ptr;	
-struct icmp6_hdr* ub;	
-struct icmp6_hdr* lb;	
+uuid_t* ptr;	
+uuid_t* ub;	
+uuid_t* lb;	
 }

```
#### __firebloom::wide_ptr.indexable.216

```c
struct __firebloom::wide_ptr.indexable .216 {
  struct necp_client_add_flow *ptr;
  struct necp_client_add_flow *ub;
}

```
#### __firebloom::wide_ptr.bidi_indexable.245

```c
struct __firebloom::wide_ptr.bidi_indexable .245 {
  nstat_interface_counts *ptr;
  nstat_interface_counts *ub;
  nstat_interface_counts *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.246

```c
struct __firebloom::wide_ptr.bidi_indexable .246 {
  struct necp_udp_stats *ptr;
  struct necp_udp_stats *ub;
  struct necp_udp_stats *lb;
}

```
#### __firebloom::wide_ptr.indexable.263

```c
struct __firebloom::wide_ptr.indexable .263 {
  struct necp_client_signable *ptr;
  struct necp_client_signable *ub;
}

```
#### __firebloom::wide_ptr.bidi_indexable.31

```c
struct __firebloom::wide_ptr.bidi_indexable .31 {
  struct proc *ptr;
  struct proc *ub;
  struct proc *lb;
}

```
#### __firebloom::wide_ptr.indexable.221

```c
struct __firebloom::wide_ptr.indexable .221 {
  struct necp_client_flow_stats *ptr;
  struct necp_client_flow_stats *ub;
}

```
#### __firebloom::wide_ptr.bidi_indexable.155

```diff

 struct __firebloom::wide_ptr.bidi_indexable.155 {
-ctrace_t* ptr;	
-ctrace_t* ub;	
-ctrace_t* lb;	
+necp_application_id_t* ptr;	
+necp_application_id_t* ub;	
+necp_application_id_t* lb;	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.209

```c
struct __firebloom::wide_ptr.bidi_indexable .209 {
  struct nstat_counts *ptr;
  struct nstat_counts *ub;
  struct nstat_counts *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.235

```c
struct __firebloom::wide_ptr.bidi_indexable .235 {
  const struct sk_stats_flow *ptr;
  const struct sk_stats_flow *ub;
  const struct sk_stats_flow *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.236

```c
struct __firebloom::wide_ptr.bidi_indexable .236 {
  nstat_quic_descriptor *ptr;
  nstat_quic_descriptor *ub;
  nstat_quic_descriptor *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.247

```c
struct __firebloom::wide_ptr.bidi_indexable .247 {
  nstat_udp_descriptor *ptr;
  nstat_udp_descriptor *ub;
  nstat_udp_descriptor *lb;
}

```
#### netagent_wrapper

```diff

  list_chain;	
 lck_rw_t agent_lock;	
 u_int32_t control_unit;	
-netagent_event_f event_handler;	
+ errno_t (u_int8_t, __firebloom::counted_by::16UL, pid_t, void*, void*, struct necp_client_agent_parameters*, __firebloom::sized_by::*assigned_results_length*, size_t*);* event_handler;	
 void* event_context;	
 u_int32_t generation;	
 u_int64_t use_count;	

```
#### netagent_token

```diff

 }
  token_chain;	
 u_int32_t token_length;	
-u_int8_t* token_bytes;	
+struct __firebloom::wide_ptr.indexable token_bytes;	
 }

```
#### netagent_session

```diff

 u_int32_t control_unit;	
 lck_mtx_t session_lock;	
 struct netagent_wrapper* wrapper;	
-netagent_event_f event_handler;	
+ errno_t (u_int8_t, __firebloom::counted_by::16UL, pid_t, void*, void*, struct necp_client_agent_parameters*, __firebloom::sized_by::*assigned_results_length*, size_t*);* event_handler;	
 void* event_context;	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.2

```c
struct __firebloom::wide_ptr.bidi_indexable .2 {
  uint8_t *ptr;
  uint8_t *ub;
  uint8_t *lb;
}

```
#### pf_pdesc

```diff

 }
  lookup;	
 u_int64_t tot_len;	
-union {
-struct tcphdr* tcp;	
-struct udphdr* udp;	
-struct icmp* icmp;	
-struct icmp6_hdr* icmp6;	
-struct pf_grev1_hdr* grev1;	
-struct pf_esp_hdr* esp;	
-void* any;	
-}
- hdr;	
+__firebloom::sized_by::hdrmaxlen hdr;	
+size_t hdrlen;	
+size_t hdrmaxlen;	
 struct pf_addr baddr;	
 struct pf_addr bdaddr;	
 struct pf_addr naddr;	

 struct pf_mtag* pf_mtag;	
 u_int16_t* ip_sum;	
 u_int32_t off;	
-u_int32_t hdrlen;	
 u_int32_t p_len;	
 u_int16_t flags;	
 sa_family_t af;	

```
#### eventhandler_entry_in6_clat46_event

```diff

 struct eventhandler_entry_in6_clat46_event {
 struct eventhandler_entry ee;	
-in6_clat46_event_fn eh_func;	
+ void (struct eventhandler_entry_arg, in6_clat46_evhdlr_code_t, pid_t, __firebloom::counted_by::16UL);* eh_func;	
 }

```
#### pf_state

```diff

 u_int8_t allow_opts;	
 u_int8_t timeout;	
 u_int8_t sync_flags;	
-netns_token nstoken;	
+struct ns_token* nstoken;	
 }

```
#### hook_desc

```diff

 struct hook_desc** tqe_prev;	
 }
  hd_list;	
-hook_fn_t hd_fn;	
+ void (void*);* hd_fn;	
 void* hd_arg;	
 }

```
#### pf_app_state

```diff

 struct pf_app_state {
-pf_app_handler handler;	
-pf_app_compare compare_lan_ext;	
-pf_app_compare compare_ext_gwy;	
+ void (struct pf_state*, int, int, struct pf_pdesc*, struct pfi_kif*);* handler;	
+ int (struct pf_app_state*, struct pf_app_state*);* compare_lan_ext;	
+ int (struct pf_app_state*, struct pf_app_state*);* compare_ext_gwy;	
 union {
 struct pf_pptp_state pptp;	
 struct pf_grev1_state grev1;	

```
#### pf_esp_hdr

```diff

 struct pf_esp_hdr {
 u_int32_t spi;	
 u_int32_t seqno;	
-u_int8_t payload[0];	
 }

```
#### __firebloom::wide_ptr.indexable.147

```c
struct __firebloom::wide_ptr.indexable .147 {
  uint8_t *ptr;
  uint8_t *ub;
}

```
#### __firebloom::wide_ptr.indexable.103

```c
struct __firebloom::wide_ptr.indexable .103 {
  void *ptr;
  void *ub;
}

```
#### __firebloom::wide_ptr.bidi_indexable.143

```diff

 struct __firebloom::wide_ptr.bidi_indexable.143 {
-struct igmp_ifinfo* ptr;	
-struct igmp_ifinfo* ub;	
-struct igmp_ifinfo* lb;	
+u_int8_t* ptr;	
+u_int8_t* ub;	
+u_int8_t* lb;	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.150

```diff

 struct __firebloom::wide_ptr.bidi_indexable.150 {
-struct sockaddr_storage* ptr;	
-struct sockaddr_storage* ub;	
-struct sockaddr_storage* lb;	
+struct pf_app_state* ptr;	
+struct pf_app_state* ub;	
+struct pf_app_state* lb;	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.147

```c
struct __firebloom::wide_ptr.bidi_indexable .147 {
  struct pfioc_token *ptr;
  struct pfioc_token *ub;
  struct pfioc_token *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.195

```c
struct __firebloom::wide_ptr.bidi_indexable .195 {
  struct ip *ptr;
  struct ip *ub;
  struct ip *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.191

```c
struct __firebloom::wide_ptr.bidi_indexable .191 {
  struct pf_rulequeue *ptr;
  struct pf_rulequeue *ub;
  struct pf_rulequeue *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.128

```diff

 struct __firebloom::wide_ptr.bidi_indexable.128 {
-struct igmp_grouprec* ptr;	
-struct igmp_grouprec* ub;	
-struct igmp_grouprec* lb;	
+struct pf_src_node* ptr;	
+struct pf_src_node* ub;	
+struct pf_src_node* lb;	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.148

```c
struct __firebloom::wide_ptr.bidi_indexable .148 {
  struct kalloc_heap *ptr;
  struct kalloc_heap *ub;
  struct kalloc_heap *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.160

```diff

 struct __firebloom::wide_ptr.bidi_indexable.160 {
-struct kalloc_heap* ptr;	
-struct kalloc_heap* ub;	
-struct kalloc_heap* lb;	
+struct pf_pooladdr* ptr;	
+struct pf_pooladdr* ub;	
+struct pf_pooladdr* lb;	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.184

```c
struct __firebloom::wide_ptr.bidi_indexable .184 {
  struct pf_anchor *ptr;
  struct pf_anchor *ub;
  struct pf_anchor *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.39

```c
struct __firebloom::wide_ptr.bidi_indexable .39 {
  struct radix_node_head *ptr;
  struct radix_node_head *ub;
  struct radix_node_head *lb;
}

```
#### ipf_filter

```diff

 struct ipf_filter {
 void* cookie;	
 const char* name;	
-ipf_input_func ipf_input;	
-ipf_output_func ipf_output;	
-ipf_detach_func ipf_detach;	
+ errno_t (void*, struct mbuf**, int, u_int8_t);* ipf_input;	
+ errno_t (void*, struct mbuf**, struct ipf_pktopts*);* ipf_output;	
+ void (void*);* ipf_detach;	
 }

```
#### ipf_pktopts

```diff

 struct ipf_pktopts {
 u_int32_t ippo_flags;	
-ifnet_t ippo_mcast_ifnet;	
+struct ifnet* ippo_mcast_ifnet;	
 int ippo_mcast_loop;	
 u_int8_t ippo_mcast_ttl;	
 }

```
#### pktap_softc

```diff

 uint32_t pktp_dlt_raw_count;	
 uint32_t pktp_dlt_pkttap_count;	
 struct ifnet* pktp_ifp;	
-struct pktap_filter pktp_filters[8];	
+struct kern_pktap_filter pktp_filters[8];	
 }

```
#### kern_pktap_filter

```c
struct kern_pktap_filter {
  uint32_t filter_op;
  uint32_t filter_param;
  union {
    uint32_t _filter_if_type;
    char     _filter_if_name[24];
  } param_;
  size_t filter_ifname_len;
  _Bool  filter_ifname_prefix_match;
}

```
#### pktap_filter

```diff

 char _filter_if_name[24];	
 }
  param_;	
-size_t filter_ifname_prefix_len;	
 }

```
#### droptap_list

```c
struct droptap_list {
  struct droptap_softc *lh_first;
}

```
#### droptap_softc

```c
struct droptap_softc {
  struct {
    struct droptap_softc  *le_next;
    struct droptap_softc **le_prev;
  } dtap_link;
  uint32_t      dtap_unit;
  uint32_t      dtap_dlt_pktap_count;
  struct ifnet *dtap_ifp;
}

```
#### droptap_header

```c
struct droptap_header {
  struct pktap_header dth_pktap_hdr;
  uint32_t            dth_dropreason;
  uint8_t             dth_dropfunc_size;
  uint16_t            dth_dropline;
  char                dth_dropfunc[64];
}

```
#### __firebloom::wide_ptr.indexable.35

```c
struct __firebloom::wide_ptr.indexable .35 {
  char *ptr;
  char *ub;
}

```
#### content_filter

```diff

 struct content_filter {
-kern_ctl_ref cf_kcref;	
+void* cf_kcref;	
 u_int32_t cf_kcunit;	
 u_int32_t cf_flags;	
 uint32_t cf_necp_control_unit;	

 struct cfil_entry** tqh_last;	
 }
  cf_sock_entries;	
-cfil_crypto_state_t cf_crypto_state;	
+struct cfil_crypto_state* cf_crypto_state;	
 }

```
#### soflow_db

```diff

 os_refcnt_t soflow_db_ref_count;	
 struct socket* soflow_db_so;	
 uint32_t soflow_db_count;	
-struct soflow_hash_head* soflow_db_hashbase;	
+__firebloom::counted_by::16 soflow_db_hashbase;	
 u_long soflow_db_hashmask;	
 struct soflow_hash_entry* soflow_db_only_entry;	
 uint8_t soflow_db_debug;	

```
#### soflow_hash_entry

```diff

 uint64_t soflow_feat_ctxt_id;	
 void* soflow_feat_ctxt;	
 uuid_t soflow_uuid;	
-nstat_context soflow_nstat_context;	
+void* soflow_nstat_context;	
 }

```
#### cfil_msg_data_event

```diff

 cfil_crypto_signature cfd_signature;	
 uint32_t cfd_signature_length;	
 uint32_t cfd_flags;	
+pid_t cfd_delegated_pid;	
+unsigned int cfd_delegated_audit_token[8];	
 }

```
#### cfil_sign_parameters

```diff

 struct cfil_sign_parameters {
-cfil_crypto_state_t csp_state;	
+struct cfil_crypto_state* csp_state;	
 struct cfil_crypto_data* csp_data;	
-uint8_t* csp_signature;	
+struct __firebloom::wide_ptr.indexable.50 csp_signature;	
 uint32_t* csp_signature_size;	
 }

```
#### __firebloom::wide_ptr.indexable.50

```c
struct __firebloom::wide_ptr.indexable .50 {
  uint8_t *ptr;
  uint8_t *ub;
}

```
#### __firebloom::wide_ptr.bidi_indexable.140

```diff

 struct __firebloom::wide_ptr.bidi_indexable.140 {
-struct ipoption* ptr;	
-struct ipoption* ub;	
-struct ipoption* lb;	
+struct cfil_msg_hdr* ptr;	
+struct cfil_msg_hdr* ub;	
+struct cfil_msg_hdr* lb;	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.115

```diff

 struct __firebloom::wide_ptr.bidi_indexable.115 {
-const struct in_addr* ptr;	
-const struct in_addr* ub;	
-const struct in_addr* lb;	
+struct proc* ptr;	
+struct proc* ub;	
+struct proc* lb;	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.89

```c
struct __firebloom::wide_ptr.bidi_indexable .89 {
  struct m_tag *ptr;
  struct m_tag *ub;
  struct m_tag *lb;
}

```
#### __firebloom::wide_ptr.bidi_indexable.142

```diff

 struct __firebloom::wide_ptr.bidi_indexable.142 {
-struct ifmultiaddr* ptr;	
-struct ifmultiaddr* ub;	
-struct ifmultiaddr* lb;	
+struct cfil_msg_bless_client* ptr;	
+struct cfil_msg_bless_client* ub;	
+struct cfil_msg_bless_client* lb;	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.144

```c
struct __firebloom::wide_ptr.bidi_indexable .144 {
  struct cfil_crypto_state *ptr;
  struct cfil_crypto_state *ub;
  struct cfil_crypto_state *lb;
}

```
#### __firebloom::wide_ptr.indexable.8

```c
struct __firebloom::wide_ptr.indexable .8 {
  const bitmap_t *ptr;
  const bitmap_t *ub;
}

```
#### rvi_client_t

```diff

 struct rvi_client_t** le_prev;	
 }
  _cle;	
-ifnet_t _ifp;	
+struct ifnet* _ifp;	
 uint32_t _unit;	
 uint32_t _vif;	
 uint32_t _raw_count;	

```
#### flowq

```diff

 }
  ;	
 struct {
-struct flowq* sle_next;	
+struct flowq* le_next;	
+struct flowq** le_prev;	
 }
  fq_hashlink;	
 union {

```
#### fq_codel_sched_data

```diff

 struct fq_codel_sched_data {
 struct ifclassq* fqs_ifq;	
-flowq_list_t fqs_flows[256];	
+__firebloom::counted_by::fqs_flows_count fqs_flows;	
+uint32_t fqs_flows_count;	
 uint32_t fqs_pkt_droplimit;	
 uint8_t fqs_throttle;	
 uint8_t fqs_flags;	

 uint32_t fqs_empty_list_cnt;	
 pktsched_bitmap_t fqs_combined_grp_bitmap;	
 classq_pkt_type_t fqs_ptype;	
-thread_call_t fqs_pacemaker_tcall;	
+struct thread_call* fqs_pacemaker_tcall;	
 bitmap_ops_t* fqs_bm_ops;	
 fq_if_group_t* fqs_classq_groups[16];	
 }

```
#### fq_if_bitmap_ops

```diff

 struct fq_if_bitmap_ops {
-fq_if_bitmaps_ffs ffs;	
-fq_if_bitmaps_zeros zeros;	
-fq_if_bitmaps_cpy cpy;	
-fq_if_bitmaps_clr clr;	
-fq_if_bitmaps_move move;	
+ int (fq_grp_tailq_t*, int, fq_if_state, fq_if_group_t**);* ffs;	
+ boolean_t (fq_grp_tailq_t*, int, fq_if_state);* zeros;	
+ void (fq_grp_tailq_t*, int, fq_if_state, fq_if_state);* cpy;	
+ void (fq_grp_tailq_t*, int, fq_if_state);* clr;	
+ void (fq_grp_tailq_t*, int, fq_if_state, fq_if_state);* move;	
 }

```
#### netem

```diff

 uint32_t netem_output_ival_ms;	
 struct heap* netem_heap;	
 netem_model_t netem_model;	
-netem_enqueue_fn_t netem_enqueue;	
+ int (struct netem*, classq_pkt_t*, _Bool*);* netem_enqueue;	
 struct bandwidth netem_bandwidth_model;	
 struct corruption netem_corruption_model;	
 struct duplication netem_duplication_model;	

```
#### _mbuf

```diff

 struct _mbuf {
 struct _mbuf* _m_next;	
 void* _m_pad;	
-uint8_t* _m_data;	
+__firebloom::sized_by::_m_len _m_data;	
 int32_t _m_len;	
 }

```
#### __firebloom::wide_ptr.indexable.40

```c
struct __firebloom::wide_ptr.indexable .40 {
  uint8_t *ptr;
  uint8_t *ub;
}

```
#### tcp_info

```diff

 uint64_t tcpi_ecn_capable_packets_acked;	
 uint64_t tcpi_ecn_capable_packets_marked;	
 uint64_t tcpi_ecn_capable_packets_lost;	
+uint64_t tcpi_received_ce_packets;	
+uint64_t tcpi_received_ect0_bytes;	
+uint64_t tcpi_received_ect1_bytes;	
+uint64_t tcpi_received_ce_bytes;	
+uint64_t tcpi_delivered_ect0_bytes;	
+uint64_t tcpi_delivered_ect1_bytes;	
+uint64_t tcpi_delivered_ce_bytes;	
 uint64_t tcpi_flow_control_total_time;	
 uint64_t tcpi_rcvwnd_limited_total_time;	
 }

```
#### kev_in_collision

```diff

 struct net_event_data link_data;	
 struct in_addr ia_ipaddr;	
 u_char hw_len;	
-u_char hw_addr[0];	
+u_char hw_addr[-1];	
 }

```
#### __firebloom::wide_ptr.indexable.66

```c
struct __firebloom::wide_ptr.indexable .66 {
  char *ptr;
  char *ub;
}

```
#### __firebloom::wide_ptr.indexable.97

```c
struct __firebloom::wide_ptr.indexable .97 {
  char *ptr;
  char *ub;
}

```
#### __firebloom::wide_ptr.indexable.61

```c
struct __firebloom::wide_ptr.indexable .61 {
  const bitmap_t *ptr;
  const bitmap_t *ub;
}

```
#### ipstat

```diff

 u_int32_t ips_necp_policy_drop;	
 u_int32_t ips_rcv_if_weak_match;	
 u_int32_t ips_rcv_if_no_match;	
+u_int32_t ips_input_ipf_drop;	
+u_int32_t ips_input_no_proto;	
+u_int32_t ips_src_addr_not_avail;	
 }

```
#### __firebloom::wide_ptr.indexable.100

```c
struct __firebloom::wide_ptr.indexable .100 {
  char *ptr;
  char *ub;
}

```
#### __firebloom::wide_ptr.bidi_indexable.113

```c
struct __firebloom::wide_ptr.bidi_indexable .113 {
  struct m_tag *ptr;
  struct m_tag *ub;
  struct m_tag *lb;
}

```
#### __firebloom::wide_ptr.indexable.99

```c
struct __firebloom::wide_ptr.indexable .99 {
  u_char *ptr;
  u_char *ub;
}

```
#### __firebloom::wide_ptr.bidi_indexable.131

```diff

 struct __firebloom::wide_ptr.bidi_indexable.131 {
-struct mldv2_record* ptr;	
-struct mldv2_record* ub;	
-struct mldv2_record* lb;	
+struct pf_mtag* ptr;	
+struct pf_mtag* ub;	
+struct pf_mtag* lb;	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.133

```c
struct __firebloom::wide_ptr.bidi_indexable .133 {
  struct in_ifaddr *ptr;
  struct in_ifaddr *ub;
  struct in_ifaddr *lb;
}

```
#### secasvar

```diff

 u_int32_t spi;	
 u_int32_t flags;	
 u_int16_t flags2;	
-struct sadb_key* key_auth;	
-struct sadb_key* key_enc;	
-caddr_t iv;	
-u_int ivlen;	
-void* sched_auth;	
-void* sched_enc;	
+__firebloom::sized_by::key_auth_len key_auth;	
+__firebloom::sized_by::key_enc_len key_enc;	
+__firebloom::sized_by::ivlen iv;	
+__firebloom::sized_by::schedlen_auth sched_auth;	
+__firebloom::sized_by::schedlen_enc sched_enc;	
+uint32_t key_auth_len;	
+uint32_t key_enc_len;	
 size_t schedlen_auth;	
 size_t schedlen_enc;	
+u_int ivlen;	
 struct secreplay* replay[4];	
 u_int64_t created;	
 struct sadb_lifetime* lft_c;	

```
#### secreplay

```diff

 u_int32_t count;	
 u_int32_t seq;	
 u_int32_t lastseq;	
-caddr_t bitmap;	
+__firebloom::sized_by::wsize bitmap;	
 int overflow;	
 }

```
#### secashead

```diff

 }
  chain;	
 struct secasindex saidx;	
-ifnet_t ipsec_if;	
+struct ifnet* ipsec_if;	
 u_int outgoing_if;	
 u_int8_t dir;	
 u_int8_t state;	

```
#### __firebloom::wide_ptr.bidi_indexable.86

```diff

 struct __firebloom::wide_ptr.bidi_indexable.86 {
-char* ptr;	
-char* ub;	
-char* lb;	
+struct udphdr* ptr;	
+struct udphdr* ub;	
+struct udphdr* lb;	
 }

```
#### __firebloom::wide_ptr.indexable.88

```c
struct __firebloom::wide_ptr.indexable .88 {
  struct ip *ptr;
  struct ip *ub;
}

```
#### __firebloom::wide_ptr.bidi_indexable.122

```diff

 struct __firebloom::wide_ptr.bidi_indexable.122 {
-struct in_ifaddr* ptr;	
-struct in_ifaddr* ub;	
-struct in_ifaddr* lb;	
+ctrace_t* ptr;	
+ctrace_t* ub;	
+ctrace_t* lb;	
 }

```
#### tcp_heuristic

```diff

  list;	
 uint32_t th_last_access;	
 struct tcp_heuristic_key th_key;	
-char th_val_start[0];	
 uint8_t th_tfo_data_loss;	
 uint8_t th_tfo_req_loss;	
 uint8_t th_tfo_data_rst;	

 uint8_t th_tfo_in_backoff;	
 uint8_t th_mptcp_in_backoff;	
 uint8_t th_mptcp_heuristic_disabled;	
-char th_val_end[0];	
 }

```
#### tcpstat

```diff

 u_int32_t tcps_sack_rcv_blocks;	
 u_int32_t tcps_sack_send_blocks;	
 u_int32_t tcps_sack_sboverflow;	
+u_int32_t tcps_rack_recovery_episode;	
+u_int32_t tcps_rack_reordering_timeout_recovery_episode;	
+u_int32_t tcps_rack_rexmits;	
 u_int32_t tcps_bg_rcvtotal;	
 u_int32_t tcps_rxtfindrop;	
 u_int32_t tcps_fcholdpacket;	

```
#### tcpopt

```diff

 uint8_t to_nsacks;	
 u_char* to_sacks;	
 u_char* to_tfo;	
+uint8_t to_num_accecn;	
+uint8_t* to_accecn;	
+uint8_t to_accecn_order;	
 }

```
#### tcptimerlist

```diff

 struct timerlisthead lhead;	
 lck_mtx_t mtx;	
 lck_grp_t* mtx_grp;	
-thread_call_t call;	
+struct thread_call* call;	
 uint32_t runtime;	
 uint32_t schedtime;	
 uint32_t entries;	

```
#### __firebloom::wide_ptr.indexable.71

```c
struct __firebloom::wide_ptr.indexable .71 {
  void *ptr;
  void *ub;
}

```
#### flow_divert_pcb

```diff

 struct flow_divert_pcb {
 lck_mtx_t mtx;	
-socket_t so;	
+struct socket* so;	
 struct {
 struct flow_divert_pcb* rbe_left;	
 struct flow_divert_pcb* rbe_right;	

 }
  rb_link;	
 uint32_t hash;	
-mbuf_t connect_token;	
+struct mbuf* connect_token;	
 uint32_t flags;	
 uint32_t send_window;	
 struct flow_divert_group* group;	

 struct flow_divert_pcb* sle_next;	
 }
  tmp_list_entry;	
-mbuf_t connect_packet;	
-uint8_t* app_data;	
+struct mbuf* connect_packet;	
+__firebloom::counted_by::app_data_length app_data;	
 size_t app_data_length;	
 union sockaddr_in_4_6 local_endpoint;	
 struct sockaddr* original_remote_endpoint;	

```
#### flow_divert_group

```diff

 uint32_t ctl_unit;	
 uint8_t atomic_bits;	
 struct send_queue_head send_queue;	
-uint8_t* token_key;	
+__firebloom::counted_by::token_key_size token_key;	
 size_t token_key_size;	
 uint32_t flags;	
 struct flow_divert_trie signing_id_trie;	

```
#### flow_divert_trie

```diff

 struct flow_divert_trie {
-struct flow_divert_trie_node* nodes;	
-uint16_t* child_maps;	
-uint8_t* bytes;	
-void* memory;	
+__firebloom::counted_by::nodes_count nodes;	
+__firebloom::sized_by::child_maps_size child_maps;	
+__firebloom::counted_by::bytes_count bytes;	
+__firebloom::sized_by::memory_size memory;	
 uint16_t nodes_count;	
 uint16_t child_maps_count;	
 uint16_t bytes_count;	

 uint16_t child_maps_free_next;	
 uint16_t bytes_free_next;	
 uint16_t root;	
+size_t memory_size;	
+size_t child_maps_size;	
 }

```
#### tcp_cc_algo

```diff

  void (struct tcpcb*);* after_idle;	
  void (struct tcpcb*);* after_timeout;	
  int (struct tcpcb*, struct tcphdr*);* delay_ack;	
+ void (struct tcpcb*, struct tcphdr*, uint32_t, uint32_t, uint32_t);* process_ecn;	
+ void (struct tcpcb*, uint32_t);* set_bytes_acked;	
  void (struct tcpcb*);* switch_to;	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.136

```diff

 struct __firebloom::wide_ptr.bidi_indexable.136 {
-struct ip6_moptions* ptr;	
-struct ip6_moptions* ub;	
-struct ip6_moptions* lb;	
+struct cmsghdr* ptr;	
+struct cmsghdr* ub;	
+struct cmsghdr* lb;	
 }

```
#### ipfilt_tag_container

```diff

 struct ipfilt_tag_container {
 struct m_tag ipft_m_tag;	
-ipfilter_t ipft_filter_ref;	
+struct opaque_ipfilter* ipft_filter_ref;	
 }

```
#### __firebloom::wide_ptr.indexable.132

```c
struct __firebloom::wide_ptr.indexable .132 {
  struct flow_divert_group **ptr;
  struct flow_divert_group **ub;
}

```
#### uuid_search_info

```diff

 struct uuid_search_info {
 uuid_t target_uuid;	
-char* found_signing_id;	
+__firebloom::sized_by::found_signing_id_size found_signing_id;	
 boolean_t found_multiple_signing_ids;	
-proc_t found_proc;	
+struct proc* found_proc;	
+size_t found_signing_id_size;	
 }

```
#### __firebloom::wide_ptr.indexable.148

```c
struct __firebloom::wide_ptr.indexable .148 {
  uint8_t *ptr;
  uint8_t *ub;
}

```
#### __firebloom::wide_ptr.bidi_indexable.141

```c
struct __firebloom::wide_ptr.bidi_indexable .141 {
  struct socket *ptr;
  struct socket *ub;
  struct socket *lb;
}

```
#### __firebloom::wide_ptr.indexable.31

```c
struct __firebloom::wide_ptr.indexable .31 {
  uint8_t *ptr;
  uint8_t *ub;
}

```
#### ah_algorithm

```diff

 u_int16_t keymax;	
 const char* name;	
  int (struct ah_algorithm_state*, struct secasvar*);* init;	
- void (struct ah_algorithm_state*, caddr_t, size_t);* update;	
- void (struct ah_algorithm_state*, caddr_t, size_t);* result;	
+ void (struct ah_algorithm_state*, char*, size_t);* update;	
+ void (struct ah_algorithm_state*, char*, size_t);* result;	
  const struct ccdigest_info* ();* digest;	
  size_t (const struct ah_algorithm*);* schedlen;	
  int (const struct ah_algorithm*, struct secasvar*);* schedule;	

```
#### ah_algorithm_state

```diff

 struct ah_algorithm_state {
-union {
-struct secasvar* sav;	
 const struct ccdigest_info* digest;	
-}
- ;	
-union {
-MD5_CTX md5_ctx;	
-SHA1_CTX sha1_ctx;	
 struct cchmac_ctx hmac_ctx[34];	
 }
- ;	
-}

```
#### __firebloom::wide_ptr.indexable.98

```c
struct __firebloom::wide_ptr.indexable .98 {
  void *ptr;
  void *ub;
}

```
#### __firebloom::wide_ptr.indexable.15

```c
struct __firebloom::wide_ptr.indexable .15 {
  char *ptr;
  char *ub;
}

```
#### eventhandler_entry_in6_event

```diff

 struct eventhandler_entry_in6_event {
 struct eventhandler_entry ee;	
-in6_event_fn eh_func;	
+ void (struct eventhandler_entry_arg, in6_evhdlr_code_t, struct ifnet*, struct in6_addr*, uint32_t);* eh_func;	
 }

```
#### __firebloom::wide_ptr.indexable.9

```c
struct __firebloom::wide_ptr.indexable .9 {
  char *ptr;
  char *ub;
}

```
#### __firebloom::wide_ptr.indexable.43

```c
struct __firebloom::wide_ptr.indexable .43 {
  void *ptr;
  void *ub;
}

```
#### __firebloom::wide_ptr.indexable.59

```c
struct __firebloom::wide_ptr.indexable .59 {
  char *ptr;
  char *ub;
}

```
#### __firebloom::wide_ptr.indexable.146

```c
struct __firebloom::wide_ptr.indexable .146 {
  void *ptr;
  void *ub;
}

```
#### __firebloom::wide_ptr.indexable.60

```c
struct __firebloom::wide_ptr.indexable .60 {
  const bitmap_t *ptr;
  const bitmap_t *ub;
}

```
#### __firebloom::wide_ptr.indexable.63

```c
struct __firebloom::wide_ptr.indexable .63 {
  char *ptr;
  char *ub;
}

```
#### __firebloom::wide_ptr.indexable.62

```c
struct __firebloom::wide_ptr.indexable .62 {
  void *ptr;
  void *ub;
}

```
#### __firebloom::wide_ptr.indexable.23

```c
struct __firebloom::wide_ptr.indexable .23 {
  char *ptr;
  char *ub;
}

```
#### __firebloom::wide_ptr.indexable.49

```c
struct __firebloom::wide_ptr.indexable .49 {
  void *ptr;
  void *ub;
}

```
#### __firebloom::wide_ptr.indexable.21

```c
struct __firebloom::wide_ptr.indexable .21 {
  char *ptr;
  char *ub;
}

```
#### sadb_msghdr

```diff

 struct sadb_msghdr {
 struct sadb_msg* msg;	
-struct sadb_ext* ext[30];	
+struct sadb_ext_entry ext[30];	
 int extoff[30];	
 int extlen[30];	
 }

```
#### sadb_ext_entry

```c
struct sadb_ext_entry {
  int                            ext_len;
  uint16_t                       ext_type;
  __firebloom::sized_by::ext_len ext_buf;
}

```
#### sadb_sa_2

```c
struct sadb_sa_2 {
  struct sadb_sa sa;
  u_int16_t      sadb_sa_natt_port;
  union {
    u_int16_t sadb_reserved0;
    u_int16_t sadb_sa_natt_interval;
  };
  u_int16_t sadb_sa_natt_offload_interval;
  u_int16_t sadb_sa_natt_src_port;
}

```
#### __firebloom::wide_ptr.indexable.116

```c
struct __firebloom::wide_ptr.indexable .116 {
  char *ptr;
  char *ub;
}

```
#### __firebloom::wide_ptr.indexable.168

```c
struct __firebloom::wide_ptr.indexable .168 {
  void *ptr;
  void *ub;
}

```
#### __firebloom::wide_ptr.bidi_indexable.161

```c
struct __firebloom::wide_ptr.bidi_indexable .161 {
  struct keycb *ptr;
  struct keycb *ub;
  struct keycb *lb;
}

```
#### workq_threadreq_extended_param_s

```c
struct workq_threadreq_extended_param_s {
  struct work_interval *trp_work_interval;
  struct thread_group  *trp_permanent_preadopt_tg;
}

```
#### kctl

```diff

 struct kctl** tqe_prev;	
 }
  next;	
-kern_ctl_ref kctlref;	
+void* kctlref;	
 char name[96];	
 u_int32_t id;	
 u_int32_t reg_unit;	
 u_int32_t flags;	
 u_int32_t recvbufsize;	
 u_int32_t sendbufsize;	
-ctl_setup_func setup;	
-ctl_bind_func bind;	
-ctl_connect_func connect;	
-ctl_disconnect_func disconnect;	
-ctl_send_func send;	
-ctl_send_list_func send_list;	
-ctl_setopt_func setopt;	
-ctl_getopt_func getopt;	
-ctl_rcvd_func rcvd;	
+ errno_t (u_int32_t*, void**);* setup;	
+ errno_t (void*, struct sockaddr_ctl*, void**);* bind;	
+ errno_t (void*, struct sockaddr_ctl*, void**);* connect;	
+ errno_t (void*, u_int32_t, void*);* disconnect;	
+ errno_t (void*, u_int32_t, void*, struct mbuf*, int);* send;	
+ errno_t (void*, u_int32_t, void*, struct mbuf*, int);* send_list;	
+ errno_t (void*, u_int32_t, void*, int, void*, size_t);* setopt;	
+ errno_t (void*, u_int32_t, void*, int, void*, size_t*);* getopt;	
+ void (void*, u_int32_t, void*, int);* rcvd;	
 struct {
 struct ctl_cb* tqh_first;	
 struct ctl_cb** tqh_last;	

```
#### __firebloom::wide_ptr.indexable.75

```c
struct __firebloom::wide_ptr.indexable .75 {
  uint8_t *ptr;
  uint8_t *ub;
}

```
#### exec_port_actions

```diff

 uint32_t registered_count;	
 struct exception_port_action_t* excport_array;	
 ipc_port_t* portwatch_array;	
-ipc_port_t* registered_array;	
+ipc_port_t registered_array[3];	
 }

```
#### munmap_args

```diff

 struct munmap_args {
 char addr_l_[0];	
-user_addr_t addr;	
+user_addr_ut addr;	
 char addr_r_[0];	
 char len_l_[0];	
-user_size_t len;	
+user_size_ut len;	
 char len_r_[0];	
 }

```
#### mlock_args

```diff

 struct mlock_args {
 char addr_l_[0];	
-user_addr_t addr;	
+user_addr_ut addr;	
 char addr_r_[0];	
 char len_l_[0];	
-user_size_t len;	
+user_size_ut len;	
 char len_r_[0];	
 }

```
#### munlock_args

```diff

 struct munlock_args {
 char addr_l_[0];	
-user_addr_t addr;	
+user_addr_ut addr;	
 char addr_r_[0];	
 char len_l_[0];	
-user_size_t len;	
+user_size_ut len;	
 char len_r_[0];	
 }

```
#### jetsam_snapshot_entry

```diff

 uint64_t jse_frozen_to_swap_pages;	
 uint64_t csflags;	
 uint32_t cs_trust_level;	
+uint64_t jse_neural_nofootprint_total_pages;	
 }

```
#### memstat_bucket

```diff

 struct proc** tqh_last;	
 }
  list;	
-int count;	
-int relaunch_high_count;	
+uint32_t count;	
+uint32_t relaunch_high_count;	
 }

```
#### jetsam_state_s

```c
struct jetsam_state_s {
  _Bool               inited;
  _Bool               limit_to_low_bands;
  int                 index;
  thread_t            thread;
  int                 jld_idle_kills;
  uint32_t            errors;
  _Bool               sort_flag;
  _Bool               corpse_list_purged;
  _Bool               post_snapshot;
  uint64_t            memory_reclaimed;
  uint32_t            hwm_kills;
  sched_cond_atomic_t jt_wakeup_cond;
}

```
#### coalition_policy_set_args

```c
struct coalition_policy_set_args {
  char     cid_l_[0];
  uint64_t cid;
  char     cid_r_[0];
  char     flavor_l_[0];
  uint32_t flavor;
  char     flavor_r_[4];
  char     value_l_[0];
  uint32_t value;
  char     value_r_[4];
}

```
#### coalition_policy_get_args

```c
struct coalition_policy_get_args {
  char     cid_l_[0];
  uint64_t cid;
  char     cid_r_[0];
  char     flavor_l_[0];
  uint32_t flavor;
  char     flavor_r_[4];
}

```
#### _cs_profile_register_t

```c
struct _cs_profile_register_t {
  uuid_t      uuid;
  const void *sig_data;
  size_t      sig_size;
  const void *data;
  size_t      size;
}

```
#### eventhandler_entry_protoctl_event

```diff

 struct eventhandler_entry_protoctl_event {
 struct eventhandler_entry ee;	
-protoctl_event_fn eh_func;	
+ void (struct eventhandler_entry_arg, struct ifnet*, struct sockaddr*, struct sockaddr*, uint16_t, uint16_t, uint8_t, uint32_t, struct protoctl_ev_val*);* eh_func;	
 }

```
#### __firebloom::wide_ptr.indexable.57

```c
struct __firebloom::wide_ptr.indexable .57 {
  char *ptr;
  char *ub;
}

```
#### __firebloom::wide_ptr.indexable.79

```c
struct __firebloom::wide_ptr.indexable .79 {
  void *ptr;
  void *ub;
}

```
#### __firebloom::wide_ptr.indexable.58

```c
struct __firebloom::wide_ptr.indexable .58 {
  void *ptr;
  void *ub;
}

```
#### __firebloom::wide_ptr.indexable.120

```c
struct __firebloom::wide_ptr.indexable .120 {
  struct fileglob **ptr;
  struct fileglob **ub;
}

```
#### sflt_filter

```diff

 sflt_handle sf_handle;	
 int sf_flags;	
 char* sf_name;	
-sf_unregistered_func sf_unregistered;	
-sf_attach_func sf_attach;	
-sf_detach_func sf_detach;	
-sf_notify_func sf_notify;	
-sf_getpeername_func sf_getpeername;	
-sf_getsockname_func sf_getsockname;	
-sf_data_in_func sf_data_in;	
-sf_data_out_func sf_data_out;	
-sf_connect_in_func sf_connect_in;	
-sf_connect_out_func sf_connect_out;	
-sf_bind_func sf_bind;	
-sf_setoption_func sf_setoption;	
-sf_getoption_func sf_getoption;	
-sf_listen_func sf_listen;	
-sf_ioctl_func sf_ioctl;	
+ void (sflt_handle);* sf_unregistered;	
+ errno_t (void**, struct socket*);* sf_attach;	
+ void (void*, struct socket*);* sf_detach;	
+ void (void*, struct socket*, sflt_event_t, void*);* sf_notify;	
+ int (void*, struct socket*, struct sockaddr**);* sf_getpeername;	
+ int (void*, struct socket*, struct sockaddr**);* sf_getsockname;	
+ errno_t (void*, struct socket*, const struct sockaddr*, struct mbuf**, struct mbuf**, sflt_data_flag_t);* sf_data_in;	
+ errno_t (void*, struct socket*, const struct sockaddr*, struct mbuf**, struct mbuf**, sflt_data_flag_t);* sf_data_out;	
+ errno_t (void*, struct socket*, const struct sockaddr*);* sf_connect_in;	
+ errno_t (void*, struct socket*, const struct sockaddr*);* sf_connect_out;	
+ errno_t (void*, struct socket*, const struct sockaddr*);* sf_bind;	
+ errno_t (void*, struct socket*, struct sockopt*);* sf_setoption;	
+ errno_t (void*, struct socket*, struct sockopt*);* sf_getoption;	
+ errno_t (void*, struct socket*);* sf_listen;	
+ errno_t (void*, struct socket*, unsigned long, __firebloom::sized_by::(((request) >> 16) & 8191));* sf_ioctl;	
 struct sflt_filter_ext sf_ext;	
 }

```
#### sflt_filter_ext

```diff

 struct sflt_filter_ext {
 unsigned int sf_ext_len;	
-sf_accept_func sf_ext_accept;	
+ errno_t (void*, struct socket*, struct socket*, const struct sockaddr*, const struct sockaddr*);* sf_ext_accept;	
 void* sf_ext_rsvd[5];	
 }

```
#### proc_delegated_signal_info

```c
struct proc_delegated_signal_info {
  audit_token_t instigator;
  audit_token_t target;
}

```
#### tracker_db

```diff

 struct tracker_db {
-struct trackerhashhead* tracker_hashbase;	
+struct __firebloom::wide_ptr.indexable tracker_hashbase;	
 u_long tracker_hashmask;	
 uint32_t tracker_count;	
 uint32_t tracker_count_short;	

```
#### __firebloom::wide_ptr.indexable.17

```c
struct __firebloom::wide_ptr.indexable .17 {
  u_int8_t *ptr;
  u_int8_t *ub;
}

```
#### mac_policy_ops

```diff

 mpo_file_notify_close_t* mpo_file_notify_close;	
 mpo_proc_check_launch_constraints_t* mpo_proc_check_launch_constraints;	
 mpo_proc_notify_service_port_derive_t* mpo_proc_notify_service_port_derive;	
+mpo_proc_check_set_task_exception_port_t* mpo_proc_check_set_task_exception_port;	
+mpo_proc_check_set_thread_exception_port_t* mpo_proc_check_set_thread_exception_port;	
+mpo_proc_check_delegated_signal_t* mpo_proc_check_delegated_signal;	
 mpo_reserved_hook_t* mpo_reserved08;	
 mpo_reserved_hook_t* mpo_reserved09;	
 mpo_reserved_hook_t* mpo_reserved10;	

 mpo_reserved_hook_t* mpo_reserved19;	
 mpo_reserved_hook_t* mpo_reserved20;	
 mpo_reserved_hook_t* mpo_reserved21;	
-mpo_reserved_hook_t* mpo_reserved22;	
-mpo_reserved_hook_t* mpo_reserved23;	
-mpo_reserved_hook_t* mpo_reserved24;	
 mpo_necp_check_open_t* mpo_necp_check_open;	
 mpo_necp_check_client_action_t* mpo_necp_check_client_action;	
 mpo_file_check_library_validation_t* mpo_file_check_library_validation;	

 mpo_proc_check_set_task_special_port_t* mpo_proc_check_set_task_special_port;	
 mpo_vnode_notify_swap_t* mpo_vnode_notify_swap;	
 mpo_vnode_notify_unlink_t* mpo_vnode_notify_unlink;	
-mpo_reserved_hook_t* mpo_reserved32;	
+mpo_vnode_check_swap_t* mpo_vnode_check_swap;	
 mpo_reserved_hook_t* mpo_reserved33;	
 mpo_reserved_hook_t* mpo_reserved34;	
 mpo_reserved_hook_t* mpo_reserved35;	

```
#### ns_token

```diff

 struct ns_token {
-ifnet_t nt_ifp;	
+struct ifnet* nt_ifp;	
 struct {
-struct ns_token* sle_next;	
+struct ns_token* le_next;	
+struct ns_token** le_prev;	
 }
  nt_ifp_link;	
 struct {
-struct ns_token* sle_next;	
+struct ns_token* le_next;	
+struct ns_token** le_prev;	
 }
  nt_all_link;	
 uint32_t nt_state;	

```
#### skmem_arena_nexus

```diff

 struct skmem_cache* arn_ring_cache;	
 struct skmem_cache* arn_txaksd_cache;	
 struct skmem_cache* arn_rxfksd_cache;	
-void* arn_stats_obj;	
-struct __flowadv_entry* arn_flowadv_obj;	
+__firebloom::sized_by::arn_stats_obj_size arn_stats_obj;	
+size_t arn_stats_obj_size;	
+__firebloom::counted_by::arn_flowadv_entries arn_flowadv_obj;	
+size_t arn_flowadv_entries;	
 void* arn_nexusadv_obj;	
 }

```
#### cuckoo_hashtable

```diff

 uint32_t _resize_waiters;	
 lck_rw_t _resize_lock;	
 lck_mtx_t _lock;	
-struct _bucket* _buckets;	
+__firebloom::counted_by::_n_buckets _buckets;	
  int (struct cuckoo_node*, void*);* _obj_cmp;	
  void (struct cuckoo_node*);* _obj_retain;	
  void (struct cuckoo_node*);* _obj_release;	

```
#### cuckoo_hashtable_params

```diff

 struct cuckoo_hashtable_params {
 size_t cht_capacity;	
-cuckoo_obj_cmp_func cht_obj_cmp;	
-cuckoo_obj_retain_func cht_obj_retain;	
-cuckoo_obj_release_func cht_obj_release;	
+ int (struct cuckoo_node*, void*);* cht_obj_cmp;	
+ void (struct cuckoo_node*);* cht_obj_retain;	
+ void (struct cuckoo_node*);* cht_obj_release;	
 }

```
#### eventhandler_entry_net_filter_event

```diff

 struct eventhandler_entry_net_filter_event {
 struct eventhandler_entry ee;	
-net_filter_event_callback_t eh_func;	
+ void (struct eventhandler_entry_arg, enum net_filter_event_subsystems {NET_FILTER_EVENT_PF=1,
+NET_FILTER_EVENT_SOCKET=2,
+NET_FILTER_EVENT_INTERFACE=4,
+NET_FILTER_EVENT_IP=8,
+NET_FILTER_EVENT_ALF=16,
+NET_FILTER_EVENT_PARENTAL_CONTROLS=32,
+NET_FILTER_EVENT_PF_PRIVATE_PROXY=64});* eh_func;	
 }

```
#### __firebloom::wide_ptr.indexable.18

```c
struct __firebloom::wide_ptr.indexable .18 {
  void *ptr;
  void *ub;
}

```
#### __firebloom::wide_ptr.indexable.36

```c
struct __firebloom::wide_ptr.indexable .36 {
  void *ptr;
  void *ub;
}

```
#### __firebloom::wide_ptr.indexable.29

```c
struct __firebloom::wide_ptr.indexable .29 {
  char *ptr;
  char *ub;
}

```
#### __firebloom::wide_ptr.indexable.33

```c
struct __firebloom::wide_ptr.indexable .33 {
  struct skmem_bufctl *ptr;
  struct skmem_bufctl *ub;
}

```
#### __firebloom::wide_ptr.indexable.81

```c
struct __firebloom::wide_ptr.indexable .81 {
  uint64_t *ptr;
  uint64_t *ub;
}

```
#### nxctl_traffic_rule_type

```diff

 nxctl_traffic_rule_create_cb_t* ntrt_create;	
 nxctl_traffic_rule_destroy_cb_t* ntrt_destroy;	
 nxctl_traffic_rule_get_all_cb_t* ntrt_get_all;	
-void* ntrt_storage;	
+struct nxctl_traffic_rule_inet_storage* ntrt_storage;	
 }

```
#### __firebloom::wide_ptr.indexable.34

```c
struct __firebloom::wide_ptr.indexable .34 {
  volatile struct ip *ptr;
  volatile struct ip *ub;
}

```
#### flow_owner

```diff

 uuid_t fo_key;	
 const struct nexus_adapter* fo_nx_port_na;	
 const struct nx_flowswitch* fo_fsw;	
-bitmap_t* fo_flowadv_bmap;	
+__firebloom::counted_by::fo_num_flowadv_bmaps fo_flowadv_bmap;	
 uint32_t fo_flowadv_max;	
 uint32_t fo_num_flowadv;	
+uint32_t fo_num_flowadv_bmaps;	
 char fo_name[24];	
 }

```
#### __nx_stats_channel_errors

```diff

 struct __nx_stats_channel_errors {
-channel_ring_error_stats_t nxs_cres;	
+struct {
+uint32_t cres_pkt_alloc_failures;	
+uint32_t __cres_reserved[1];	
+}
+* nxs_cres;	
 }

```
#### fsw_ip_frag_mgr

```diff

 uint32_t ipfm_f_limit;	
 uint32_t ipfm_f_count;	
 lck_mtx_t ipfm_lock;	
-thread_call_t ipfm_timeout_tcall;	
+struct thread_call* ipfm_timeout_tcall;	
 struct ifnet* ipfm_ifp;	
 struct fsw_stats* ipfm_stats;	
 }

```
#### __firebloom::wide_ptr.indexable.68

```c
struct __firebloom::wide_ptr.indexable .68 {
  char *ptr;
  char *ub;
}

```
#### __firebloom::wide_ptr.indexable.67

```c
struct __firebloom::wide_ptr.indexable .67 {
  void *ptr;
  void *ub;
}

```
#### __firebloom::wide_ptr.indexable.19

```c
struct __firebloom::wide_ptr.indexable .19 {
  void *ptr;
  void *ub;
}

```
#### __firebloom::wide_ptr.indexable.82

```c
struct __firebloom::wide_ptr.indexable .82 {
  void *ptr;
  void *ub;
}

```
#### flow_agg

```diff

 struct __kern_packet* _fa_spkt;	
 }
  ;	
-uint8_t* _fa_sptr;	
+struct __firebloom::wide_ptr.indexable _fa_sptr;	
 _Bool _fa_sobj_is_pkt;	
 _Bool _fa_sobj_is_short;	
 uint32_t _fa_tcp_seq;	
 uint32_t _fa_ulen;	
 uint32_t _fa_total;	
-flow_agg_fix_pkt_sum_func _fa_fix_pkt_sum;	
+ uint16_t (uint16_t, uint16_t, uint16_t);* _fa_fix_pkt_sum;	
 }
  __flow_agg;	
 uint64_t __flow_agg_data[5];	

```
#### __firebloom::wide_ptr.bidi_indexable.153

```c
struct __firebloom::wide_ptr.bidi_indexable .153 {
  struct nx_llink_info_req *ptr;
  struct nx_llink_info_req *ub;
  struct nx_llink_info_req *lb;
}

```
#### __firebloom::wide_ptr.indexable.190

```c
struct __firebloom::wide_ptr.indexable .190 {
  struct __kern_channel_ring *ptr;
  struct __kern_channel_ring *ub;
}

```
#### __firebloom::wide_ptr.bidi_indexable.171

```c
struct __firebloom::wide_ptr.bidi_indexable .171 {
  struct ucred *ptr;
  struct ucred *ub;
  struct ucred *lb;
}

```
#### __firebloom::wide_ptr.indexable.111

```c
struct __firebloom::wide_ptr.indexable .111 {
  void *ptr;
  void *ub;
}

```
#### netif_gso_ip_tcp_state

```diff

 struct netif_gso_ip_tcp_state {
- void (struct netif_gso_ip_tcp_state*, struct __kern_packet*, uint8_t*);* update;	
+ void (struct netif_gso_ip_tcp_state*, struct __kern_packet*, struct __firebloom::wide_ptr.bidi_indexable.33);* update;	
  void (struct netif_gso_ip_tcp_state*, uint32_t, uint16_t, uint32_t*);* internal;	
 union {
 struct ip* ip;	

```
#### PerfControllerInterface

```diff

 WorkUpdateFunction workUpdate;	
 RegisterDriverDeviceFunction registerDriverDevice;	
 RegisterDriverDeviceFunction unregisterDriverDevice;	
+WorkEndWithResourcesFunction workEndWithResources;	
 }

```
#### DriverState

```diff

 uint32_t reserved;	
 uint64_t target_thread_group_id;	
 void* target_thread_group_data;	
-uint32_t device_type;	
+enum PerfDeviceID {kInvalid=0,
+kCPU=0,
+kANE=4,
+kGPU=5,
+kMSR=6,
+kStorage=7} device_type;	
 uint32_t instance_id;	
+bool resource_accounting;	
 }

```
#### ResourceAccounting

```c
struct ResourceAccounting {
  uint64_t mach_time_delta;
  uint64_t energy_nj_delta;
}

```
#### WorkTableEntry

```diff

 struct WorkTableEntry {
 struct thread_group* thread_group;	
+coalition_t coal;	
 bool started;	
 uint8_t perfcontrol_data[32];	
 }

```
#### embedded_panic_header

```diff

 uint64_t eph_roots_installed;	
 uint32_t eph_ext_paniclog_offset;	
 uint32_t eph_ext_paniclog_len;	
+uint32_t eph_panic_initiator_offset;	
+uint32_t eph_panic_initiator_len;	
 }

```
