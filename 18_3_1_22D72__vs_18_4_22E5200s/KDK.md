## KDKs

- `KDK_15.3.1_24D70.kdk/System/Library/Kernels/kernel.release.t6031`
- `KDK_15.4_24E5206s.kdk/System/Library/Kernels/kernel.release.t6031`

#### hib_exclave_iv

```c
struct hib_exclave_iv {
  uint8_t iv[12];
  uint8_t tag[16];
}

```
#### ipc_object

```diff

 struct ipc_object {
-ipc_object_bits_t io_bits;	
-ipc_object_refs_t io_references;	
+atomic ipc_object_bits_t io_bits;	
+atomic ipc_object_refs_t io_references;	
 }

```
#### turnstile

```diff

  ts_htable_link;	
 uintptr_t ts_proprietor;	
 os_ref_atomic_t ts_refcount;	
-uint32_t ts_type_gencount;	
+atomic uint32_t ts_type_gencount;	
 uint32_t ts_prim_count;	
 turnstile_update_flags_t ts_inheritor_flags;	
 uint8_t ts_priority;	

```
#### mpsc_queue_chain

```diff

 struct mpsc_queue_chain {
-struct mpsc_queue_chain* mpqc_next;	
+atomic struct mpsc_queue_chain* mpqc_next;	
 }

```
#### thread

```diff

 int16_t req_base_pri;	
 int16_t max_priority;	
 int16_t task_priority;	
-int16_t promotion_priority;	
 uint16_t priority_floor_count;	
 int16_t suspend_count;	
 int iotier_override;	

 union {
 struct thread_call_thread_state* thc_state;	
 struct {
+int os_reason;	
+exception_type_t exception_type;	
 mach_exception_code_t code;	
 mach_exception_subcode_t subcode;	
 }
- guard_exc_info;	
+ mach_exc_info;	
 }
  ;	
 int32_t user_stop_count;	

 uint32_t policy_reset;	
 uint32_t suspend_parked;	
 uint32_t corpse_dup;	
-volatile ast_t ast;	
+volatile atomic ast_t ast;	
 lck_mtx_t mutex;	
 struct ipc_port* ith_special_reply_port;	
 uint16_t t_dtrace_flags;	

 uint32_t kevent_overrides;	
 uint8_t user_promotion_basepri;	
 uint8_t kern_promotion_schedpri;	
-uint16_t kevent_ast_bits;	
+atomic uint16_t kevent_ast_bits;	
 io_stat_info_t thread_io_stats;	
 uint32_t thread_callout_interrupt_wakeups;	
 uint32_t thread_callout_platform_idle_wakeups;	

 uint16_t callout_woken_from_icontext;	
 uint16_t callout_woken_from_platform_idle;	
 uint16_t callout_woke_thread;	
-uint16_t guard_exc_fatal;	
+uint16_t mach_exc_fatal;	
+uint16_t mach_exc_ktriage;	
 uint16_t thread_bitfield_unused;	
 uint32_t th_bound_cluster_id;	
 struct thread_group* preadopt_thread_group;	

```
#### processor

```diff

 struct processor {
 processor_state_t state;	
-_Bool is_SMT;	
 _Bool is_recommended;	
-_Bool current_is_NO_SMT;	
 _Bool current_is_bound;	
 _Bool current_is_eagerpreempt;	
 _Bool pending_nonurgent_preemption;	

 struct timer_call running_timers[3];	
 struct run_queue runq;	
 struct recount_processor pr_recount;	
-processor_t processor_primary;	
-processor_t processor_secondary;	
 struct ipc_port* processor_self;	
 processor_t processor_list;	
 uint64_t timer_call_ttd;	

```
#### processor_set

```diff

 int cpu_set_hi;	
 int cpu_set_count;	
 int last_chosen;	
-uint64_t load_average;	
 uint64_t pset_load_average[6];	
 uint32_t pset_runnable_depth[6];	
 uint64_t pset_load_last_update;	
 cpumap_t cpu_bitmask;	
 cpumap_t recommended_bitmask;	
 cpumap_t cpu_state_map[7];	
-cpumap_t primary_map;	
 cpumap_t realtime_map;	
 cpumap_t cpu_available_map;	
 lck_ticket_t sched_lock;	

 cpumap_t perfcontrol_cpu_preferred_bitmask;	
 cpumap_t perfcontrol_cpu_migration_bitmask;	
 int cpu_preferred_last_chosen;	
-_Bool is_SMT;	
 }

```
#### rt_queue

```diff

 struct rt_queue {
-uint64_t earliest_deadline;	
-int count;	
-uint32_t constraint;	
-int ed_index;	
+atomic uint64_t earliest_deadline;	
+atomic int count;	
+atomic uint32_t constraint;	
+atomic int ed_index;	
 bitmap_t bitmap[1];	
 rt_queue_pri_t rt_queue_pri[31];	
 struct runq_stats runq_stats;	

```
#### sched_clutch_root

```diff

 bitmap_t scr_bound_warp_available[1];	
 struct priority_queue_deadline_min scr_unbound_root_buckets;	
 struct priority_queue_deadline_min scr_bound_root_buckets;	
-uint16_t scr_cumulative_run_count[6];	
+atomic uint16_t scr_cumulative_run_count[6];	
 struct sched_clutch_root_bucket scr_unbound_buckets[6];	
 struct sched_clutch_root_bucket scr_bound_buckets[6];	
 }

```
#### pset_node

```diff

 processor_set_t psets;	
 pset_node_t nodes;	
 pset_node_t node_list;	
-pset_node_t parent;	
 pset_cluster_type_t pset_cluster_type;	
 pset_map_t pset_map;	
-pset_map_t pset_idle_map;	
-pset_map_t pset_idle_primary_map;	
-pset_map_t pset_non_rt_map;	
-pset_map_t pset_non_rt_primary_map;	
-pset_map_t pset_recommended_map;	
+atomic pset_map_t pset_idle_map;	
+atomic pset_map_t pset_non_rt_map;	
+atomic pset_map_t pset_recommended_map;	
 }

```
#### recount_processor

```diff

 uint64_t rpr_last_interrupt_enter_time_mach;	
 uint64_t rpr_last_interrupt_leave_time_mach;	
 uint64_t rpr_idle_time_mach;	
-uint64_t rpr_state_last_abs_time;	
+atomic uint64_t rpr_state_last_abs_time;	
 uint8_t rpr_cpu_kind_index;	
 }

```
#### task

```diff

 uint64_t rop_pid;	
 uint64_t jop_pid;	
 uint8_t disable_user_jop;	
-uint8_t has_jitbox;	
+atomic uint8_t has_jitbox;	
+uint64_t jitbox_version;	
 uint64_t jitbox_start;	
 uint64_t jitbox_size;	
 boolean_t jitbox_enabled;	

 vmobject_list_output_t corpse_vmobject_list;	
 uint64_t corpse_vmobject_list_size;	
 vm_deferred_reclamation_metadata_t deferred_reclamation_metadata;	
+uint64_t task_cs_auxiliary_info;	
 }

```
#### kalloc_type_view

```diff

 const char* kt_signature;	
 kalloc_type_flags_t kt_flags;	
 uint32_t kt_size;	
-zone_t kt_zshared;	
+zone_t kt_zearly;	
 zone_t kt_zsig;	
 }

```
#### stackshot_context

```diff

 _Bool sc_panic_stackshot;	
 size_t sc_min_kcdata_size;	
 _Bool sc_is_singlethreaded;	
-stackshot_state_t sc_state;	
+atomic stackshot_state_t sc_state;	
 kern_return_t sc_retval;	
-uint32_t sc_cpus_working;	
+atomic uint32_t sc_cpus_working;	
 linked_kcdata_descriptor_t sc_pretask_kcdata;	
 linked_kcdata_descriptor_t sc_posttask_kcdata;	
 kcdata_descriptor_t sc_finalized_kcdata;	

```
#### stackshot_buffer

```diff

 struct stackshot_buffer {
 void* ssb_ptr;	
 size_t ssb_size;	
-size_t ssb_used;	
+atomic size_t ssb_used;	
 struct freelist_entry* ssb_freelist;	
-int ssb_freelist_lock;	
-size_t ssb_overhead;	
+atomic int ssb_freelist_lock;	
+atomic size_t ssb_overhead;	
 }

```
#### stackshot_workqueue

```diff

 struct stackshot_workqueue {
-uint32_t sswq_num_items;	
-uint32_t sswq_cur_item;	
+atomic uint32_t sswq_num_items;	
+atomic uint32_t sswq_cur_item;	
 size_t sswq_capacity;	
-_Bool sswq_populated;	
+atomic _Bool sswq_populated;	
 struct stackshot_workitem* sswq_items;	
 }

```
#### _vm_map

```diff

 unsigned int res0;	
 unsigned int pad;	
 unsigned int timestamp;	
+task_t owning_task;	
 }

```
#### pmap

```diff

 uint8_t main_trust_level;	
 vm_map_offset_t jit_region_start;	
 vm_map_offset_t jit_region_end;	
-int32_t ref_count;	
-int32_t nested_count;	
+atomic int32_t ref_count;	
+atomic int32_t nested_count;	
 uint32_t nested_no_bounds_refcnt;	
 uint16_t hw_asid;	
 uint8_t sw_asid;	

```
#### cpu_data

```diff

 struct cpu_data {
 unsigned short cpu_number;	
-cpu_flags_t cpu_flags;	
+atomic cpu_flags_t cpu_flags;	
 int cpu_type;	
 int cpu_subtype;	
 int cpu_threadtype;	

 _Bool cpu_hibernate;	
 _Bool cpu_running;	
 _Bool cluster_master;	
-_Bool sync_on_cswitch;	
 _Bool in_state_transition;	
 uint32_t cpu_decrementer;	
 get_decrementer_t cpu_get_decrementer_func;	

 vm_offset_t coresight_base[4];	
 uint64_t cpu_regmap_paddr;	
 uint32_t cpu_phys_id;	
-uint32_t cpu_l2_access_penalty;	
 platform_error_handler_t platform_error_handler;	
 int cpu_mcount_off;	
 volatile unsigned int cpu_sleep_token;	

 CPU_HALTED_WITH_STATE=2} halt_status;	
 uint64_t rop_key;	
 uint64_t jop_key;	
+uint64_t jitbox_version;	
 uint64_t jitbox_start;	
 uint64_t jitbox_size;	
 boolean_t jitbox_enabled;	

```
#### vm_page

```diff

 unsigned int vmp_wire_count;	
 unsigned int vmp_q_state;	
 unsigned int vmp_on_specialq;	
+unsigned int vmp_canonical;	
 unsigned int vmp_gobbled;	
 unsigned int vmp_laundry;	
 unsigned int vmp_no_cache;	
-unsigned int vmp_private;	
 unsigned int vmp_reference;	
 unsigned int vmp_lopage;	
 unsigned int vmp_realtime;	

 unsigned int vmp_wanted;	
 unsigned int vmp_tabled;	
 unsigned int vmp_hashed;	
-unsigned int vmp_fictitious;	
+unsigned int __vmp_unused;	
 unsigned int vmp_clustered;	
 unsigned int vmp_pmapped;	
 unsigned int vmp_xpmapped;	

```
#### port_label_hash

```diff

 struct port_label_hash {
-int plh_lock;	
+atomic int plh_lock;	
 uint16_t plh_size;	
 uint16_t plh_count;	
 struct ipc_service_port_label** plh_array;	

```
#### ipc_entry

```diff

 struct ipc_entry {
 union {
 struct ipc_object* __ptrauth(DA, true, 0xf444) ie_object;	
+struct ipc_port* __ptrauth(DA, true, 0xf444) ie_port;	
+struct ipc_pset* __ptrauth(DA, true, 0xf444) ie_pset;	
 volatile struct ipc_object* __ptrauth(DA, true, 0xf444) ie_volatile_object;	
 struct ipc_entry_table* __ptrauth(DA, true, 0x5f62) ie_self;	
 }

```
#### mach_assert_default

```c
struct mach_assert_default {
  struct mach_assert_hdr hdr;
  const char            *expr;
}

```
#### mach_assert_hdr

```c
struct mach_assert_hdr {
  mach_assert_type_t type;
  unsigned int       lineno;
  const char        *filename;
}

```
#### zone_stats

```diff

 uint64_t zs_mem_freed;	
 uint64_t zs_alloc_fail;	
 uint32_t zs_alloc_rr;	
-uint32_t zs_alloc_not_shared;	
+atomic uint32_t zs_alloc_not_early;	
 }

```
#### mpsc_daemon_queue

```diff

 struct mpsc_daemon_queue {
 mpsc_daemon_queue_kind_t mpd_kind;	
 mpsc_daemon_queue_options_t mpd_options;	
-mpsc_daemon_queue_state_t mpd_state;	
+atomic mpsc_daemon_queue_state_t mpd_state;	
 mpsc_daemon_invoke_fn_t mpd_invoke;	
 union {
 mpsc_daemon_queue_t mpd_target;	

```
#### mpsc_queue_head

```diff

 struct mpsc_queue_head {
 struct mpsc_queue_chain mpqh_head;	
-struct mpsc_queue_chain* mpqh_tail;	
+atomic struct mpsc_queue_chain* mpqh_tail;	
 }

```
#### ipc_policy_violations_rb_entry

```c
struct ipc_policy_violations_rb_entry {
  char                      proc_name[17];
  char                      service_name[86];
  char                      team_id[32];
  char                      signing_id[128];
  ipc_policy_violation_id_t violation_id;
  int                       sw_platform;
  int                       msgh_id;
  int                       sdk;
}

```
#### proc_ro

```diff

 struct {
 uint64_t p_uniqueid;	
 int p_idversion;	
+pid_t p_orig_ppid;	
+int p_orig_ppidversion;	
 uint32_t p_csflags;	
 struct {
 volatile struct ucred* __smr_ptr;	

```
#### proc_ro_data

```diff

 struct proc_ro_data {
 uint64_t p_uniqueid;	
 int p_idversion;	
+pid_t p_orig_ppid;	
+int p_orig_ppidversion;	
 uint32_t p_csflags;	
 struct {
 volatile struct ucred* __smr_ptr;	

```
#### smr_shash

```diff

 struct smr_shash {
-hw_lck_ptr_t* smrsh_array[2];	
-uint32_t smrsh_seed[2];	
-smrsh_state_t smrsh_state;	
-smrsh_rehash_t smrsh_rehashing;	
+atomic hw_lck_ptr_t* smrsh_array[2];	
+atomic uint32_t smrsh_seed[2];	
+atomic smrsh_state_t smrsh_state;	
+atomic smrsh_rehash_t smrsh_rehashing;	
 smrsh_policy_t smrsh_policy;	
 uint16_t smrsh_min_shift;	
 uint16_t __unused_bits;	

```
#### i_resource_coalition

```diff

 uint64_t cpu_cycles;	
 uint64_t ane_mach_time;	
 uint64_t ane_energy_nj;	
-uint64_t gpu_energy_nj;	
-uint64_t gpu_energy_nj_billed_to_me;	
-uint64_t gpu_energy_nj_billed_to_others;	
+atomic uint64_t gpu_energy_nj;	
+atomic uint64_t gpu_energy_nj_billed_to_me;	
+atomic uint64_t gpu_energy_nj_billed_to_others;	
 struct recount_coalition co_recount;	
 uint64_t task_count;	
 uint64_t dead_task_count;	

```
#### coal_sort_s

```c
struct coal_sort_s {
  int      pid;
  int      usr_order;
  uint64_t bytes;
}

```
#### kernel_panic_reason

```c
struct kernel_panic_reason {
  char buf[1024];
}

```
#### mach_assert_3x

```c
struct mach_assert_3x {
  struct mach_assert_hdr hdr;
  const char            *a;
  const char            *op;
  const char            *b;
}

```
#### zone_security_flags

```diff

 struct zone_security_flags {
-uint16_t z_submap_idx;	
-uint16_t z_kheap_id;	
-uint16_t z_kalloc_type;	
-uint16_t z_lifo;	
-uint16_t z_pgz_use_guards;	
-uint16_t z_submap_from_end;	
-uint16_t z_noencrypt;	
-uint16_t z_tag;	
+uint32_t z_submap_idx;	
+uint32_t z_kheap_id;	
+uint32_t z_kalloc_type;	
+uint32_t z_lifo;	
+uint32_t z_pgz_use_guards;	
+uint32_t z_submap_from_end;	
+uint32_t z_noencrypt;	
+uint32_t z_tag;	
+uint32_t z_unused;	
 zone_id_t z_sig_eq;	
 }

```
#### hw_spin_policy

```diff

 const char* hwsp_name;	
 union {
 const uint64_t* hwsp_timeout;	
-const uint64_t* hwsp_timeout_atomic;	
+const atomic uint64_t* hwsp_timeout_atomic;	
 }
  ;	
 uint16_t hwsp_timeout_shift;	

```
#### mpsc_ring

```c
struct mpsc_ring {
  char                     *mr_buffer;
  uint32_t                 *mr_writer_holds;
  union mpsc_ring_head_tail mr_head_tail;
  uint32_t                  mr_capacity;
  uint8_t                   mr_writer_count;
}

```
#### sched_clutch_bucket_group

```diff

 struct sched_clutch_bucket_group {
 uint8_t scbg_bucket;	
-uint32_t scbg_timeshare_tick;	
-uint32_t scbg_pri_shift;	
-uint32_t scbg_preferred_cluster;	
+atomic uint32_t scbg_timeshare_tick;	
+atomic uint32_t scbg_pri_shift;	
+atomic uint32_t scbg_preferred_cluster;	
 uint32_t scbg_amp_rebalance_last_chosen;	
 struct sched_clutch* scbg_clutch;	
 sched_clutch_counter_time_t scbg_blocked_data;	

```
#### sched_clutch

```diff

 struct sched_clutch {
-uint16_t sc_thr_count;	
+atomic uint16_t sc_thr_count;	
 union {
 struct thread_group* sc_tg;	
 }

```
#### startup_tunable_dt_source_spec

```c
struct startup_tunable_dt_source_spec {
  const char       *dt_base;
  const char       *dt_name;
  _Bool             dt_chosen_override;
  const char       *boot_arg_name;
  void             *var_addr;
  int               var_len;
  _Bool             var_is_bool;
  startup_source_t *source_addr;
}

```
#### static_if_key

```c
struct static_if_key {
  short             sik_enable_count;
  short             sik_init_value;
  unsigned int      sik_entries_count;
  static_if_entry_t sik_entries_head;
}

```
#### static_if_entry

```c
struct static_if_entry {
  static_if_offset_t sie_base;
  static_if_offset_t sie_target;
  unsigned long      sie_link;
}

```
#### work_interval_auto_join_info

```diff

 struct work_interval_auto_join_info {
 struct work_interval_deferred_finish_state deferred_finish_state;	
-work_interval_auto_join_status_t status;	
+atomic work_interval_auto_join_status_t status;	
 }

```
#### mach_vm_subsystem

```diff

 mach_msg_id_t end;	
 unsigned int maxsize;	
 vm_address_t reserved;	
-struct kern_routine_descriptor kroutine[26];	
+struct kern_routine_descriptor kroutine[27];	
 }

```
#### upl_page_info

```diff

 unsigned int cs_nx;	
 unsigned int needed;	
 unsigned int mark;	
+unsigned int reserved;	
 }

```
#### vm_object_fault_info

```diff

 unsigned int no_copy_on_read;	
 unsigned int fi_xnu_user_debug;	
 unsigned int fi_used_for_tpro;	
+unsigned int fi_change_wiring;	
+unsigned int fi_no_sleep;	
 unsigned int __vm_object_fault_info_unused_bits;	
 int pmap_options;	
 }

```
#### vm_deferred_reclamation_metadata_s

```diff

 struct vm_deferred_reclamation_metadata_s** tqe_prev;	
 }
  vdrm_list;	
-struct {
-struct vm_deferred_reclamation_metadata_s* tqe_next;	
-struct vm_deferred_reclamation_metadata_s** tqe_prev;	
-}
- vdrm_async_list;	
 lck_mtx_t vdrm_lock;	
 gate_t vdrm_gate;	
 task_t vdrm_task;	
 pid_t vdrm_pid;	
 vm_map_t vdrm_map;	
 os_refcnt_t vdrm_refcnt;	
-user_addr_t vdrm_reclaim_buffer;	
+user_addr_t vdrm_buffer_addr;	
 mach_vm_size_t vdrm_buffer_size;	
-user_addr_t vdrm_reclaim_indices;	
+mach_vm_reclaim_count_t vdrm_buffer_len;	
 uint64_t vdrm_reclaimed_at;	
-size_t vdrm_num_bytes_put_in_buffer;	
-size_t vdrm_num_bytes_reclaimed;	
 uint32_t vdrm_waiters;	
+uint64_t vdrm_last_sample_abs;	
+uint64_t vdrm_reclaimable_bytes_wma;	
+size_t vdrm_reclaimable_bytes_min;	
+size_t vdrm_cumulative_uncancelled_bytes;	
+size_t vdrm_cumulative_reclaimed_bytes;	
 }

```
#### mach_vm_reclaim_entry_s

```c
struct mach_vm_reclaim_entry_s {
  mach_vm_address_t        address;
  uint32_t                 size;
  mach_vm_reclaim_action_t behavior;
  uint8_t                  _unused[3];
}

```
#### vm_page_radix_node

```c
struct vm_page_radix_node {
  vm_page_radix_ptr_t vmpr_array[256];
}

```
#### _telemetry_scratch

```c
struct _telemetry_scratch {
  struct _telemetry_kernel_sample ts_sample;
  uint32_t                        ts_call_stack[128];
}

```
#### _telemetry_kernel_sample

```c
struct _telemetry_kernel_sample {
  clock_sec_t  tks_time_secs;
  uint64_t     tks_serial_number;
  uint64_t     tks_telemetry_skipped;
  uint64_t     tks_telemetry_period;
  uint64_t     tks_system_time_in_terminated_threads;
  uint64_t     tks_task_size;
  uint64_t     tks_pageins;
  uint64_t     tks_faults;
  uint64_t     tks_cow_faults;
  uint64_t     tks_thread_id;
  uint64_t     tks_system_time;
  clock_usec_t tks_time_usecs;
  uint32_t     tks_magic;
  uint32_t     tks_thread_state;
  uint32_t     tks_sched_pri;
  uint32_t     tks_base_pri;
  uint32_t     tks_sched_flags;
  uint32_t     tks_call_stack_size;
  uint32_t     tks_telemetry_source;
  uint32_t     tks_telemetry_generation;
  uint8_t      tks_cpu;
  uint8_t      tks_io_tier;
  char         tks_thread_name[64];
}

```
#### telemetry_target

```diff

 kUserMode=4,
 kIORecord=8,
 kPMIRecord=16,
-kMACFRecord=32} microsnapshot_flags;	
+kMACFRecord=32,
+kKernelThread=64} microsnapshot_flags;	
 _Bool include_metadata;	
 struct micro_snapshot_buffer* buffer;	
 lck_mtx_t* buffer_mtx;	

```
#### _telemetry_uuids

```c
struct _telemetry_uuids {
  errno_t  error;
  void    *uuid_info;
  uint32_t uuid_info_count;
  uint32_t uuid_info_size;
}

```
#### _telemetry_kernel_snapshots

```c
struct _telemetry_kernel_snapshots {
  struct micro_snapshot  tkse_micro_snap;
  struct task_snapshot   tkse_task_snap;
  struct thread_snapshot tkse_thread_snap;
}

```
#### trap_telemetry_tree

```c
struct trap_telemetry_tree {
  struct trap_telemetry_tree_entry *sph_root;
}

```
#### trap_telemetry_tree_entry

```c
struct trap_telemetry_tree_entry {
  struct {
    struct trap_telemetry_tree_entry *spe_left;
    struct trap_telemetry_tree_entry *spe_right;
  } link;
  match_record_s record;
}

```
#### match_record

```c
struct match_record {
  uintptr_t             fault_pc;
  trap_telemetry_type_t trap_type;
  uint64_t              trap_code;
}

```
#### rsb_entry

```c
struct rsb_entry {
  match_record_s           record;
  trap_telemetry_options_s options;
  size_t                   bt_frames_count;
  uintptr_t                bt_frames[15];
}

```
#### trap_debounce_buffer

```c
struct trap_debounce_buffer {
  match_record_s records[2];
  size_t         tail;
}

```
#### _ca_event_trap_telemetry_internal

```c
struct _ca_event_trap_telemetry_internal {
  ca_sstr            backtrace[256];
  unsigned long long trap_code;
  unsigned long long trap_offset;
  unsigned long long trap_type;
  ca_sstr            trap_uuid[37];
}

```
#### ccrng_schedule_atomic_flag_ctx

```diff

 struct ccrng_schedule_atomic_flag_ctx {
 ccrng_schedule_ctx_t schedule_ctx;	
-ccrng_schedule_action_t flag;	
+atomic ccrng_schedule_action_t flag;	
 }

```
#### entropy_cpu_data

```diff

 struct entropy_cpu_data {
 entropy_sample_t samples[2048];	
-uint32_t sample_count;	
+atomic uint32_t sample_count;	
 }

```
#### _TrustCacheRuntime

```diff

 _Bool allowSecondStaticTC;	
 _Bool allowEngineeringTC;	
 _Bool allowLegacyTC;	
-TrustCache_t* staticTCHead;	
-TrustCache_t* engineeringTCHead;	
+atomic TrustCache_t* staticTCHead;	
+atomic TrustCache_t* engineeringTCHead;	
 TrustCacheMutableRuntime_t* mutableRT;	
 }

```
#### _TrustCache

```diff

 struct _TrustCache {
-struct _TrustCache* next;	
+atomic struct _TrustCache* next;	
 TCType_t type;	
+_Bool tombstoned;	
 size_t moduleSize;	
 const TrustCacheModuleBase_t* module;	
 }

```
#### _TrustCacheMutableRuntime

```diff

 struct _TrustCacheMutableRuntime {
-TrustCache_t* loadableTCHead;	
+atomic TrustCache_t* loadableTCHead;	
 }

```
#### pmap_cpu_data

```diff

 struct pmap_cpu_data {
-const volatile struct pmap* active_pmap;	
-const volatile struct pmap* active_stage2_pmap;	
-const volatile struct pmap* inflight_pmap;	
-uint64_t inflight_pvh;	
+atomic const volatile struct pmap* active_pmap;	
+atomic const volatile struct pmap* active_stage2_pmap;	
+atomic const volatile struct pmap* inflight_pmap;	
+atomic uint64_t inflight_pvh;	
 uint64_t inflight_pvh_pc;	
 uint64_t inflight_pvh_lr;	
-uint64_t pvh_to_lock;	
+atomic uint64_t pvh_to_lock;	
 void* ppl_kern_saved_sp;	
 void* ppl_stack;	
 arm_context_t* save_area;	

```
#### kernel_brk_descriptor

```diff

 struct kernel_brk_descriptor {
-kernel_brk_type_t type;	
+trap_telemetry_type_t type;	
 uint16_t base;	
 uint16_t max;	
-kernel_brk_options_t options;	
- void (void*, uint16_t);* handle_breakpoint;	
+brk_telemetry_options_s options;	
+ const char* (void*, uint16_t);* handle_breakpoint;	
 }

```
#### proc

```diff

 struct proc* __ptrauth(DA, true, 0x5d4d) p_pptr;	
 proc_ro_t p_proc_ro;	
 pid_t p_ppid;	
-pid_t p_original_ppid;	
 pid_t p_pgrpid;	
 uid_t p_uid;	
 gid_t p_gid;	

 int p_pthsize;	
 uint32_t p_pth_tsd_offset;	
 user_addr_t p_stack_addr_hint;	
-struct workqueue* p_wqptr;	
+atomic struct workqueue* p_wqptr;	
 struct timeval p_start;	
 void* p_rcall;	
 void* p_pthhash;	

  p_memstat_list;	
 uint64_t p_memstat_userdata;	
 uint64_t p_memstat_idledeadline;	
-uint64_t p_memstat_idle_start;	
+uint64_t p_memstat_prio_start;	
 uint64_t p_memstat_idle_delta;	
 int32_t p_memstat_memlimit;	
 int32_t p_memstat_memlimit_active;	
 int32_t p_memstat_memlimit_inactive;	
 int32_t p_memstat_relaunch_flags;	
-uint32_t p_user_faults;	
+atomic uint32_t p_user_faults;	
 uint32_t p_memlimit_increase;	
 uint64_t p_crash_behavior_deadline;	
 uint32_t p_crash_count;	

```
#### fileproc

```diff

 struct fileproc {
 os_refcnt_t fp_iocount;	
-fileproc_vflags_t fp_vflags;	
+atomic fileproc_vflags_t fp_vflags;	
 fileproc_flags_t fp_flags;	
 uint16_t fp_guard_attrs;	
 struct fileglob* __ptrauth(DA, true, 0xc75) fp_glob;	

```
#### kqworkloop

```diff

 struct kqtailq kqwl_queue[6];	
 struct kqtailq kqwl_suppressed;	
 workq_threadreq_s kqwl_request;	
-thread_group_qos_t kqwl_preadopt_tg;	
+atomic thread_group_qos_t kqwl_preadopt_tg;	
 lck_spin_t kqwl_statelock;	
 thread_t kqwl_owner;	
 os_ref_atomic_t kqwl_retains;	
 thread_qos_t kqwl_wakeup_qos;	
-uint8_t kqwl_iotier_override;	
-uint16_t kqwl_preadopt_tg_needs_redrive;	
+atomic uint8_t kqwl_iotier_override;	
+atomic uint16_t kqwl_preadopt_tg_needs_redrive;	
 struct turnstile* kqwl_turnstile;	
 kqueue_id_t kqwl_dynamicid;	
 uint64_t kqwl_params;	

```
#### session

```diff

 struct tty* s_ttyp;	
 uint32_t s_ttyvid;	
 pid_t s_ttypgrpid;	
-dev_t s_ttydev;	
+atomic dev_t s_ttydev;	
 pid_t s_sid;	
 os_ref_atomic_t s_refcount;	
 char s_login[255];	

```
#### sigacts

```diff

 sigset_t ps_signodefer;	
 sigset_t ps_siginfo;	
 sigset_t ps_oldmask;	
-uint32_t ps_sigreturn_validation;	
+atomic uint32_t ps_sigreturn_validation;	
 int ps_flags;	
 int ps_sig;	
 int ps_code;	

```
#### workqueue

```diff

 lck_ticket_t wq_lock;	
 uint64_t wq_thread_call_last_run;	
 struct os_refcnt wq_refcnt;	
-workq_state_flags_t wq_flags;	
+atomic workq_state_flags_t wq_flags;	
 uint32_t wq_fulfilled;	
 uint32_t wq_creations;	
 uint32_t wq_timer_interval;	

 uint16_t wq_thidlecount;	
 uint16_t wq_thscheduled_count[7];	
 workq_threadreq_t wq_event_manager_threadreq;	
-wq_thactive_t wq_thactive;	
-uint64_t wq_lastblocked_ts[6];	
+atomic wq_thactive_t wq_thactive;	
+atomic uint64_t wq_lastblocked_ts[6];	
 struct proc* wq_proc;	
 struct uthread* wq_creator;	
 turnstile_inheritor_t wq_inheritor;	

```
#### ifnet

```diff

 ifnet_add_proto_func if_add_proto;	
 ifnet_del_proto_func if_del_proto;	
 ifnet_check_multi if_check_multi;	
+size_t if_proto_hash_count;	
 struct proto_hash_entry* if_proto_hash;	
 ifnet_detached_func if_detach;	
 u_int32_t if_flowhash;	

 lck_rw_t if_link_status_lock;	
 struct if_link_status* if_link_status;	
 struct if_interface_state if_interface_state;	
+uint64_t if_link_heuristics_start_time;	
+uint64_t if_congested_link_start_time;	
+uint64_t if_lqmstate_start_time;	
+thread_call_t if_link_heuristics_tcall;	
 struct if_tcp_ecn_stat* if_ipv4_stat;	
 struct if_tcp_ecn_stat* if_ipv6_stat;	
 struct {

```
#### if_data_internal

```diff

 u_int64_t ifi_dt_bytes;	
 u_int64_t ifi_fpackets;	
 u_int64_t ifi_fbytes;	
+u_int64_t ifi_link_heuristics_cnt;	
+u_int64_t ifi_link_heuristics_time;	
+u_int64_t ifi_congested_link_cnt;	
+u_int64_t ifi_congested_link_time;	
+u_int64_t ifi_lqm_good_cnt;	
+u_int64_t ifi_lqm_good_time;	
+u_int64_t ifi_lqm_poor_cnt;	
+u_int64_t ifi_lqm_poor_time;	
+u_int64_t ifi_lqm_min_viable_cnt;	
+u_int64_t ifi_lqm_min_viable_time;	
+u_int64_t ifi_lqm_bad_cnt;	
+u_int64_t ifi_lqm_bad_time;	
 struct timeval ifi_lastchange;	
 struct timeval ifi_lastupdown;	
 u_int32_t ifi_hwassist;	

```
#### ext_ref

```diff

 u_int16_t prefcnt;	
 u_int16_t flags;	
 u_int32_t priv;	
-uintptr_t ext_token;	
 }

```
#### pkthdr

```diff

 struct packet_tags tags;	
 union builtin_mtag builtin_mtag;	
 uint32_t comp_gencnt;	
-uint16_t pkt_ext_flags;	
-uint16_t pkt_crumbs;	
+uint32_t pkt_crumbs;	
+uint32_t pkt_compl_callbacks;	
+uint32_t pkt_ext_flags;	
+uint32_t pkt_unused;	
 struct {
 union {
 u_int8_t __mpriv8[16];	

  __mpriv_u;	
 }
  pkt_mpriv;	
-u_int32_t redzone;	
-u_int32_t pkt_compl_callbacks;	
 }

```
#### tcp_pktinfo

```diff

 struct tcp_pktinfo {
 union {
 struct {
-uint32_t segsz;	
+uint16_t seg_size;	
+uint16_t hdr_len;	
 uint32_t start_seq;	
 pid_t pid;	
 pid_t e_pid;	

```
#### pr_usrreqs

```diff

  int (struct socket*, struct sockaddr*, struct proc*);* pru_connect;	
  int (struct socket*, struct socket*);* pru_connect2;	
  int (struct socket*, struct sockaddr*, struct sockaddr*, struct proc*, uint32_t, sae_associd_t, sae_connid_t*, uint32_t, void*, uint32_t, struct uio*, user_ssize_t*);* pru_connectx;	
- int (struct socket*, u_long, __firebloom::sized_by::(((cmd) >> 16) & 8191), struct ifnet*, struct proc*);* pru_control;	
+ int (struct socket*, u_long, caddr_t, struct ifnet*, struct proc*);* pru_control;	
  int (struct socket*);* pru_detach;	
  int (struct socket*);* pru_disconnect;	
  int (struct socket*, sae_associd_t, sae_connid_t);* pru_disconnectx;	

```
#### pr_usrreqs_old

```diff

  int (struct socket*, struct sockaddr*, struct proc*);* pru_bind;	
  int (struct socket*, struct sockaddr*, struct proc*);* pru_connect;	
  int (struct socket*, struct socket*);* pru_connect2;	
- int (struct socket*, u_long, char*, struct ifnet*, struct proc*);* pru_control;	
+ int (struct socket*, u_long, caddr_t, struct ifnet*, struct proc*);* pru_control;	
  int (struct socket*);* pru_detach;	
  int (struct socket*);* pru_disconnect;	
  int (struct socket*, struct proc*);* pru_listen;	

```
#### ifreq

```diff

 u_int32_t ifru_qosmarking_mode;	
 u_int32_t ifru_qosmarking_enabled;	
 u_int32_t ifru_disable_output;	
+int32_t ifru_point_to_point_mdns;	
 u_int32_t ifru_low_internet;	
 int ifru_low_power_mode;	
 u_int32_t ifru_tcp_kao_max;	

```
#### _attrlist_paths

```diff

 struct _attrlist_paths {
 char* fullpathptr;	
-ssize_t* fullpathlenp;	
+ssize_t fullpathlen;	
+size_t fullpathbuflen;	
 char* relpathptr;	
-ssize_t* relpathlenp;	
+ssize_t relpathlen;	
+size_t relpathbuflen;	
 char* REALpathptr;	
-ssize_t* REALpathlenp;	
+ssize_t REALpathlen;	
+size_t REALpathbuflen;	
 }

```
#### cs_blob

```diff

 }
  ;	
 unsigned int csb_validation_category;	
+uint64_t csb_auxiliary_info;	
 void* __ptrauth(DA, true, 0xe82b) csb_csm_obj;	
 _Bool csb_csm_managed;	
+uint32_t csb_csm_trust_level;	
 }

```
#### bpf_d

```diff

 uint32_t bd_write_size_max;	
 uint32_t bd_rtout;	
 struct bpf_if* bd_bif;	
-__firebloom::counted_by::bd_filter_len bd_filter;	
+__bounds_safety::counted_by::bd_filter_len bd_filter;	
 uint32_t bd_filter_len;	
 uint64_t bd_rcount;	
 uint64_t bd_dcount;	

```
#### __bounds_safety::wide_ptr.bidi_indexable.4

```c
struct __bounds_safety::wide_ptr.bidi_indexable.4 {
  char *ptr;
  char *ub;
  char *lb;
}

```
#### dlil_threading_info

```diff

 struct thread* dlth_driver_thread;	
 struct thread* dlth_poller_thread;	
 lck_grp_t* dlth_lock_grp;	
-char dlth_name[32];	
+char dlth_name_storage[32];	
+const char* dlth_name;	
 uint32_t dlth_trim_cnt;	
 uint32_t dlth_trim_pkts_dropped;	
 uint64_t dlth_pkts_cnt;	

```
#### kern_pbufpool

```diff

 struct skmem_region* pp_umd_region;	
 struct skmem_region* pp_ubft_region;	
 struct skmem_region* pp_kbft_region;	
-__firebloom::counted_by::pp_u_hash_table_size pp_u_hash_table;	
+__bounds_safety::counted_by::pp_u_hash_table_size pp_u_hash_table;	
 uint64_t pp_u_bufinuse;	
-__firebloom::counted_by::pp_u_bft_hash_table_size pp_u_bft_hash_table;	
+__bounds_safety::counted_by::pp_u_bft_hash_table_size pp_u_bft_hash_table;	
 uint64_t pp_u_bftinuse;	
 void* pp_ctx;	
  void (const void*);* pp_ctx_retain;	

```
#### skmem_cache

```diff

 size_t skm_hash_shift;	
 size_t skm_hash_mask;	
 size_t skm_hash_size;	
-__firebloom::counted_by::skm_hash_size skm_hash_table;	
+__bounds_safety::counted_by::skm_hash_size skm_hash_table;	
 struct {
 struct skmem_slab* tqh_first;	
 struct skmem_slab** tqh_last;	

 uint32_t skm_rs_busy;	
 uint32_t skm_rs_want;	
 size_t skm_cpu_cache_count;	
-struct skmem_cpu_cache skm_cpu_cache[0];	
+__bounds_safety::counted_by::skm_cpu_cache_count skm_cpu_cache;	
 }

```
#### skmem_obj_info

```diff

 struct skmem_obj_info {
-__firebloom::sized_by::oi_size oi_addr;	
+__bounds_safety::sized_by::oi_size oi_addr;	
 struct skmem_bufctl* oi_bc;	
 uint32_t oi_size;	
 obj_idx_t oi_idx_reg;	

```
#### skmem_bufctl

```diff

 struct skmem_bufctl* sle_next;	
 }
  bc_link;	
-__firebloom::sized_by::bc_lim bc_addr;	
+__bounds_safety::sized_by::bc_lim bc_addr;	
 void* bc_addrm;	
 struct skmem_slab* bc_slab;	
 uint32_t bc_lim;	

```
#### skmem_region

```diff

 uint32_t skr_seg_objs;	
 uint32_t skr_seg_bmap_len;	
 size_t skr_seg_bmap_size;	
-__firebloom::sized_by::skr_seg_bmap_size skr_seg_bmap;	
+__bounds_safety::sized_by::skr_seg_bmap_size skr_seg_bmap;	
 uint32_t skr_seg_free_cnt;	
 uint32_t skr_hash_initial;	
 uint32_t skr_hash_limit;	
 uint32_t skr_hash_shift;	
 uint32_t skr_hash_mask;	
 size_t skr_hash_size;	
-__firebloom::counted_by::skr_hash_size skr_hash_table;	
+__bounds_safety::counted_by::skr_hash_size skr_hash_table;	
 struct segfreehead skr_seg_free;	
 struct segtfreehead skr_seg_tfree;	
 uint32_t skr_seg_waiters;	

```
#### skmem_mag

```diff

  mg_link;	
 struct skmem_magtype* mg_magtype;	
 size_t mg_count;	
-void* mg_round[0];	
+__bounds_safety::counted_by::mg_count mg_round;	
 }

```
#### __packet_compl

```diff

  compl_data;	
 }
  ;	
-uint32_t compl_callbacks;	
+uint8_t compl_callbacks;	
 uint32_t compl_context;	
 }

```
#### tcpstat_local

```diff

 u_int64_t dospacket;	
 u_int64_t cleanup;	
 u_int64_t synwindow;	
+u_int64_t linkheur_stealthdrop;	
+u_int64_t linkheur_noackpri;	
+u_int64_t linkheur_comprxmt;	
+u_int64_t linkheur_synrxmt;	
+u_int64_t linkheur_rxmtfloor;	
 }

```
#### udpstat_local

```diff

 u_int64_t badmcast;	
 u_int64_t cleanup;	
 u_int64_t badipsec;	
+u_int64_t linkheur_stealthdrop;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.30

```c
struct __bounds_safety::wide_ptr.bidi_indexable.30 {
  struct bpf_hdr_ext *ptr;
  struct bpf_hdr_ext *ub;
  struct bpf_hdr_ext *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.25

```c
struct __bounds_safety::wide_ptr.bidi_indexable.25 {
  void *ptr;
  void *ub;
  void *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.34

```c
struct __bounds_safety::wide_ptr.bidi_indexable.34 {
  struct pktap_header *ptr;
  struct pktap_header *ub;
  struct pktap_header *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.35

```c
struct __bounds_safety::wide_ptr.bidi_indexable.35 {
  struct bpf_hdr *ptr;
  struct bpf_hdr *ub;
  struct bpf_hdr *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.36

```c
struct __bounds_safety::wide_ptr.bidi_indexable.36 {
  struct bpf_comp_hdr *ptr;
  struct bpf_comp_hdr *ub;
  struct bpf_comp_hdr *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.28

```c
struct __bounds_safety::wide_ptr.bidi_indexable.28 {
  u_char *ptr;
  u_char *ub;
  u_char *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.58

```c
struct __bounds_safety::wide_ptr.bidi_indexable.58 {
  u_int *ptr;
  u_int *ub;
  u_int *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.68

```c
struct __bounds_safety::wide_ptr.bidi_indexable.68 {
  struct bpf_if *ptr;
  struct bpf_if *ub;
  struct bpf_if *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.80

```c
struct __bounds_safety::wide_ptr.bidi_indexable.80 {
  struct ether_header *ptr;
  struct ether_header *ub;
  struct ether_header *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.85

```c
struct __bounds_safety::wide_ptr.bidi_indexable.85 {
  struct bpf_insn *ptr;
  struct bpf_insn *ub;
  struct bpf_insn *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.91

```c
struct __bounds_safety::wide_ptr.bidi_indexable.91 {
  struct bpf_packet *ptr;
  struct bpf_packet *ub;
  struct bpf_packet *lb;
}

```
#### bpf_packet

```diff

 struct bpf_packet {
 int bpfp_type;	
-__firebloom::sized_by::bpfp_header_length bpfp_header;	
+__bounds_safety::sized_by::bpfp_header_length bpfp_header;	
 size_t bpfp_header_length;	
 union {
 struct mbuf* bpfpu_mbuf;	

```
#### __bounds_safety::wide_ptr.bidi_indexable.99

```c
struct __bounds_safety::wide_ptr.bidi_indexable.99 {
  const uint32_t *ptr;
  const uint32_t *ub;
  const uint32_t *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.111

```c
struct __bounds_safety::wide_ptr.bidi_indexable.111 {
  struct xbpf_d *ptr;
  struct xbpf_d *ub;
  struct xbpf_d *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.83

```c
struct __bounds_safety::wide_ptr.bidi_indexable.83 {
  struct kalloc_heap *ptr;
  struct kalloc_heap *ub;
  struct kalloc_heap *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.79

```c
struct __bounds_safety::wide_ptr.bidi_indexable.79 {
  struct pktap_v2_hdr *ptr;
  struct pktap_v2_hdr *ub;
  struct pktap_v2_hdr *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.46

```c
struct __bounds_safety::wide_ptr.bidi_indexable.46 {
  struct mbuf *ptr;
  struct mbuf *ub;
  struct mbuf *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable

```c
struct __bounds_safety::wide_ptr.bidi_indexable {
  struct bpf_d *ptr;
  struct bpf_d *ub;
  struct bpf_d *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.56

```c
struct __bounds_safety::wide_ptr.bidi_indexable.56 {
  const void *ptr;
  const void *ub;
  const void *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.100

```c
struct __bounds_safety::wide_ptr.bidi_indexable.100 {
  struct __kern_buflet *ptr;
  struct __kern_buflet *ub;
  struct __kern_buflet *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.22

```c
struct __bounds_safety::wide_ptr.bidi_indexable.22 {
  struct bpf_d **ptr;
  struct bpf_d **ub;
  struct bpf_d **lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.37

```c
struct __bounds_safety::wide_ptr.bidi_indexable.37 {
  struct ifnet *ptr;
  struct ifnet *ub;
  struct ifnet *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.0

```c
struct __bounds_safety::wide_ptr.bidi_indexable.0 {
  struct bpf_packet *ptr;
  struct bpf_packet *ub;
  struct bpf_packet *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.19

```c
struct __bounds_safety::wide_ptr.bidi_indexable.19 {
  void *ptr;
  void *ub;
  void *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.20

```c
struct __bounds_safety::wide_ptr.bidi_indexable.20 {
  u_char *ptr;
  u_char *ub;
  u_char *lb;
}

```
#### __bounds_safety::wide_ptr.indexable

```c
struct __bounds_safety::wide_ptr.indexable {
  u_char *ptr;
  u_char *ub;
}

```
#### __bounds_safety::wide_ptr.indexable.30

```c
struct __bounds_safety::wide_ptr.indexable.30 {
  void *ptr;
  void *ub;
}

```
#### bridge_softc

```diff

 }
  sc_list;	
 lck_mtx_t sc_mtx;	
-__firebloom::counted_by::sc_rthash_size sc_rthash;	
+__bounds_safety::counted_by::sc_rthash_size sc_rthash;	
 struct _bridge_rtnode_list sc_rtlist;	
 uint32_t sc_rthash_key;	
 uint32_t sc_rthash_size;	

```
#### pf_ruleset

```diff

 struct pf_rulequeue queues[2];	
 struct {
 struct pf_rulequeue* ptr;	
-__firebloom::counted_by::rsize ptr_array;	
+__bounds_safety::counted_by::rsize ptr_array;	
 u_int32_t rcount;	
 u_int32_t rsize;	
 u_int32_t ticket;	

  active;	
 struct {
 struct pf_rulequeue* ptr;	
-__firebloom::counted_by::rsize ptr_array;	
+__bounds_safety::counted_by::rsize ptr_array;	
 u_int32_t rcount;	
 u_int32_t rsize;	
 u_int32_t ticket;	

```
#### nexus_netif_adapter

```diff

 struct nexus_netif_adapter {
 struct nexus_adapter nifna_up;	
 struct nx_netif* nifna_netif;	
-__firebloom::counted_by::nifna_tx_mit_count nifna_tx_mit;	
-__firebloom::counted_by::nifna_rx_mit_count nifna_rx_mit;	
+__bounds_safety::counted_by::nifna_tx_mit_count nifna_tx_mit;	
+__bounds_safety::counted_by::nifna_rx_mit_count nifna_rx_mit;	
 union {
 struct netif_filter* nifna_filter;	
 struct netif_flow* nifna_flow;	

```
#### nexus_adapter

```diff

 uint32_t na_scratch_cnt;	
 uint32_t na_all_rings_cnt;	
 uint64_t na_work_ts;	
-__firebloom::counted_by::na_tx_rings_cnt na_tx_rings;	
-__firebloom::counted_by::na_rx_rings_cnt na_rx_rings;	
-__firebloom::counted_by::na_all_rings_cnt na_all_rings;	
+__bounds_safety::counted_by::na_tx_rings_cnt na_tx_rings;	
+__bounds_safety::counted_by::na_rx_rings_cnt na_rx_rings;	
+__bounds_safety::counted_by::na_all_rings_cnt na_all_rings;	
 struct kern_nexus* na_nx;	
 volatile uint32_t na_refcount;	
 int na_si_users[6];	

 uint32_t na_total_slots;	
 const uint32_t na_flowadv_max;	
 const nexus_stats_type_t na_stats_type;	
-__firebloom::counted_by::na_alloc_free_rings_cnt na_alloc_rings;	
-__firebloom::counted_by::na_alloc_free_rings_cnt na_free_rings;	
-__firebloom::counted_by::na_event_rings_cnt na_event_rings;	
-__firebloom::counted_by::na_large_buf_alloc_rings_cnt na_large_buf_alloc_rings;	
+__bounds_safety::counted_by::na_alloc_free_rings_cnt na_alloc_rings;	
+__bounds_safety::counted_by::na_alloc_free_rings_cnt na_free_rings;	
+__bounds_safety::counted_by::na_event_rings_cnt na_event_rings;	
+__bounds_safety::counted_by::na_large_buf_alloc_rings_cnt na_large_buf_alloc_rings;	
 uint64_t na_ch_mit_ival;	
 struct kern_nexus_domain_provider* na_nxdom_prov;	
-__firebloom::counted_by::na_slot_ctxs_cnt na_slot_ctxs;	
-__firebloom::counted_by::na_scratch_cnt na_scratch;	
-__firebloom::counted_by::0 na_tail;	
+__bounds_safety::counted_by::na_slot_ctxs_cnt na_slot_ctxs;	
+__bounds_safety::counted_by::na_scratch_cnt na_scratch;	
+__bounds_safety::counted_by::0 na_tail;	
 void* na_private;	
 struct ifnet* na_ifp;	
 uint8_t na_kring_svc_lut[10];	
 uint32_t na_next_pipe;	
 uint32_t na_max_pipes;	
-__firebloom::counted_by::na_max_pipes na_pipes;	
+__bounds_safety::counted_by::na_max_pipes na_pipes;	
 char na_name[64];	
 uuid_t na_uuid;	
  int (struct nexus_adapter*, na_activate_mode_t);* na_activate;	

```
#### __kern_channel_ring

```diff

 volatile uint32_t ckr_alloc_ws;	
 struct nexus_adapter* ckr_na;	
 struct kern_pbufpool* ckr_pp;	
-__firebloom::counted_by::ckr_usds_cnt ckr_usds;	
+__bounds_safety::counted_by::ckr_usds_cnt ckr_usds;	
 slot_idx_t ckr_usds_cnt;	
-__firebloom::counted_by::ckr_ksds_cnt ckr_ksds;	
+__bounds_safety::counted_by::ckr_ksds_cnt ckr_ksds;	
 slot_idx_t ckr_ksds_cnt;	
 struct __slot_desc* ckr_ksds_last;	
 struct skmem_cache* ckr_ksds_cache;	
 uint32_t ckr_ring_id;	
 boolean_t ckr_rate_limited;	
-__firebloom::counted_by::ckr_scratch_cnt ckr_scratch;	
+__bounds_safety::counted_by::ckr_scratch_cnt ckr_scratch;	
 slot_idx_t ckr_scratch_cnt;	
  int (struct __kern_channel_ring*, struct proc*, uint32_t);* ckr_na_sync;	
 volatile  int (struct __kern_channel_ring*, struct proc*, uint32_t);* ckr_na_notify;	

  int (struct __kern_channel_ring*, struct proc*, uint32_t);* ckr_save_notify;	
 kern_packet_svc_class_t ckr_svc;	
 uint32_t ckr_slot_ctxs_set;	
-__firebloom::counted_by::ckr_slot_ctxs_cnt ckr_slot_ctxs;	
+__bounds_safety::counted_by::ckr_slot_ctxs_cnt ckr_slot_ctxs;	
 uint32_t ckr_slot_ctxs_cnt;	
 void* ckr_ctx;	
 struct ch_selinfo ckr_si;	

 struct nx_netif_mit* ckr_mit;	
 volatile uint32_t ckr_pending_intr;	
 volatile uint32_t ckr_pending_doorbell;	
-__firebloom::counted_by::ckr_tx_pool_count ckr_tx_pool;	
+__bounds_safety::counted_by::ckr_tx_pool_count ckr_tx_pool;	
 uint32_t ckr_tx_pool_count;	
 struct nx_mbq ckr_rx_queue;	
 struct __kern_channel_ring* ckr_pipe;	

```
#### kern_nexus

```diff

 struct kern_pbufpool* nx_rx_pp;	
 struct kern_pbufpool* nx_tx_pp;	
 struct kern_nexus_advisory nx_adv;	
-__firebloom::counted_by::nx_num_ports nx_ports;	
-__firebloom::sized_by::nx_ports_bmap_size nx_ports_bmap;	
+__bounds_safety::counted_by::nx_num_ports nx_ports;	
+__bounds_safety::sized_by::nx_ports_bmap_size nx_ports_bmap;	
 nexus_port_size_t nx_active_ports;	
 nexus_port_size_t nx_num_ports;	
 size_t nx_ports_bmap_size;	

```
#### nxbind

```diff

 uint64_t nxb_uniqueid;	
 uuid_t nxb_exec_uuid;	
 uint32_t nxb_key_len;	
-__firebloom::sized_by::nxb_key_len nxb_key;	
+__bounds_safety::sized_by::nxb_key_len nxb_key;	
 }

```
#### nxdom_prov_cb

```diff

 struct nxdom_prov_cb {
  int (struct kern_nexus_domain_provider*);* dp_cb_init;	
  void (struct kern_nexus_domain_provider*);* dp_cb_fini;	
- int (struct kern_nexus_domain_provider*, const uint32_t, const struct nxprov_params*, struct nxprov_params*, __firebloom::counted_by::28, uint32_t);* dp_cb_params;	
+ int (struct kern_nexus_domain_provider*, const uint32_t, const struct nxprov_params*, struct nxprov_params*, __bounds_safety::counted_by::28, uint32_t);* dp_cb_params;	
  int (struct kern_nexus_domain_provider*, struct kern_nexus*, struct nexus_adapter*);* dp_cb_mem_new;	
  int (struct kern_nexus_domain_provider*, struct kern_nexus*, struct nx_cfg_req*, int, struct proc*, struct ucred*);* dp_cb_config;	
  int (struct kern_nexus*);* dp_cb_nx_ctor;	

```
#### netif_qset

```diff

 uint8_t nqs_num_rx_queues;	
 uint8_t nqs_num_tx_queues;	
 uint8_t nqs_num_queues;	
-struct netif_queue nqs_driver_queues[0];	
+__bounds_safety::counted_by::nqs_num_queues nqs_driver_queues;	
 }

```
#### kern_nexus_netif_llink_init

```diff

 uint8_t nli_num_qsets;	
 void* nli_ctx;	
 kern_nexus_netif_llink_id_t nli_link_id;	
-__firebloom::counted_by::nli_num_qsets nli_qsets;	
+__bounds_safety::counted_by::nli_num_qsets nli_qsets;	
 }

```
#### kern_nexus_advisory

```diff

 struct kern_nexus_advisory {
 struct skmem_region* nxv_reg;	
-__firebloom::sized_by::nxv_adv_size nxv_adv;	
+__bounds_safety::sized_by::nxv_adv_size nxv_adv;	
 nexus_advisory_type_t nxv_adv_type;	
 union {
 struct sk_nexusadv* flowswitch_nxv_adv;	

```
#### __user_channel_schema

```diff

 const volatile uint32_t csm_flags;	
 char csm_kern_name[256];	
 uuid_t csm_kern_uuid;	
-const uint32_t csm_tx_rings;	
-const uint32_t csm_rx_rings;	
-const uint32_t csm_allocator_ring_pairs;	
-const uint32_t csm_num_event_rings;	
-const uint32_t csm_large_buf_alloc_rings;	
+uint32_t csm_tx_rings;	
+uint32_t csm_rx_rings;	
+uint32_t csm_allocator_ring_pairs;	
+uint32_t csm_num_event_rings;	
+uint32_t csm_large_buf_alloc_rings;	
 const uint32_t csm_flowadv_max;	
 const mach_vm_offset_t csm_flowadv_ofs;	
 const uint64_t csm_md_redzone_cookie;	

 const mach_vm_offset_t csm_stats_ofs;	
 const nexus_stats_type_t csm_stats_type;	
 const mach_vm_offset_t csm_nexusadv_ofs;	
-struct {
-const mach_vm_offset_t ring_off;	
-const mach_vm_offset_t sd_off;	
-}
- csm_ring_ofs[0];	
+__bounds_safety::counted_by::csm_tx_rings + csm_rx_rings + csm_allocator_ring_pairs + csm_num_event_rings + csm_large_buf_alloc_rings csm_ring_ofs;	
 }

```
#### __kern_channel_event

```diff

 uint32_t ev_flags;	
 uint16_t _reserved;	
 uint16_t ev_dlen;	
-uint8_t ev_data[0];	
+__bounds_safety::counted_by::ev_dlen ev_data;	
 }

```
#### if_clone

```diff

 u_int32_t ifc_minifs;	
 u_int32_t ifc_maxunit;	
 u_int32_t ifc_bmlen;	
-__firebloom::counted_by::ifc_bmlen ifc_units;	
+__bounds_safety::counted_by::ifc_bmlen ifc_units;	
  int (struct if_clone*, u_int32_t, void*);* ifc_create;	
  int (struct ifnet*);* ifc_destroy;	
 uint8_t ifc_namelen;	

```
#### bridge_control

```diff

 struct bridge_control {
- int (struct bridge_softc*, __firebloom::sized_by::arg_len, size_t);* bc_func;	
+ int (struct bridge_softc*, __bounds_safety::sized_by::arg_len, size_t);* bc_func;	
 unsigned int bc_argsize;	
 unsigned int bc_flags;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.44

```c
struct __bounds_safety::wide_ptr.bidi_indexable.44 {
  char *ptr;
  char *ub;
  char *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.64

```c
struct __bounds_safety::wide_ptr.bidi_indexable.64 {
  struct _bridge_rtnode_list *ptr;
  struct _bridge_rtnode_list *ub;
  struct _bridge_rtnode_list *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.26

```c
struct __bounds_safety::wide_ptr.bidi_indexable.26 {
  void *ptr;
  void *ub;
  void *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.43

```c
struct __bounds_safety::wide_ptr.bidi_indexable.43 {
  struct ether_header *ptr;
  struct ether_header *ub;
  struct ether_header *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.88

```c
struct __bounds_safety::wide_ptr.bidi_indexable.88 {
  struct ether_arp *ptr;
  struct ether_arp *ub;
  struct ether_arp *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.93

```c
struct __bounds_safety::wide_ptr.bidi_indexable.93 {
  struct ip *ptr;
  struct ip *ub;
  struct ip *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.57

```c
struct __bounds_safety::wide_ptr.bidi_indexable.57 {
  uint8_t *ptr;
  uint8_t *ub;
  uint8_t *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.97

```c
struct __bounds_safety::wide_ptr.bidi_indexable.97 {
  struct ip6_hdr *ptr;
  struct ip6_hdr *ub;
  struct ip6_hdr *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.102

```c
struct __bounds_safety::wide_ptr.bidi_indexable.102 {
  struct icmp6_hdr *ptr;
  struct icmp6_hdr *ub;
  struct icmp6_hdr *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.104

```c
struct __bounds_safety::wide_ptr.bidi_indexable.104 {
  struct nd_neighbor_solicit *ptr;
  struct nd_neighbor_solicit *ub;
  struct nd_neighbor_solicit *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.107

```c
struct __bounds_safety::wide_ptr.bidi_indexable.107 {
  struct nd_opt_hdr *ptr;
  struct nd_opt_hdr *ub;
  struct nd_opt_hdr *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.108

```c
struct __bounds_safety::wide_ptr.bidi_indexable.108 {
  struct nd_neighbor_advert *ptr;
  struct nd_neighbor_advert *ub;
  struct nd_neighbor_advert *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.117

```c
struct __bounds_safety::wide_ptr.bidi_indexable.117 {
  struct llc *ptr;
  struct llc *ub;
  struct llc *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.124

```c
struct __bounds_safety::wide_ptr.bidi_indexable.124 {
  struct tcphdr *ptr;
  struct tcphdr *ub;
  struct tcphdr *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.139

```c
struct __bounds_safety::wide_ptr.bidi_indexable.139 {
  struct ifreq *ptr;
  struct ifreq *ub;
  struct ifreq *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.140

```c
struct __bounds_safety::wide_ptr.bidi_indexable.140 {
  struct ifmediareq32 *ptr;
  struct ifmediareq32 *ub;
  struct ifmediareq32 *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.146

```c
struct __bounds_safety::wide_ptr.bidi_indexable.146 {
  struct ifdrv32 *ptr;
  struct ifdrv32 *ub;
  struct ifdrv32 *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.152

```c
struct __bounds_safety::wide_ptr.bidi_indexable.152 {
  struct ifdrv64 *ptr;
  struct ifdrv64 *ub;
  struct ifdrv64 *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.170

```c
struct __bounds_safety::wide_ptr.bidi_indexable.170 {
  struct sockaddr *ptr;
  struct sockaddr *ub;
  struct sockaddr *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.95

```c
struct __bounds_safety::wide_ptr.bidi_indexable.95 {
  struct udphdr *ptr;
  struct udphdr *ub;
  struct udphdr *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.73

```c
struct __bounds_safety::wide_ptr.bidi_indexable.73 {
  struct bridge_rtnode *ptr;
  struct bridge_rtnode *ub;
  struct bridge_rtnode *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.181

```c
struct __bounds_safety::wide_ptr.bidi_indexable.181 {
  struct kern_event_msg *ptr;
  struct kern_event_msg *ub;
  struct kern_event_msg *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.182

```c
struct __bounds_safety::wide_ptr.bidi_indexable.182 {
  struct event *ptr;
  struct event *ub;
  struct event *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.48

```c
struct __bounds_safety::wide_ptr.bidi_indexable.48 {
  struct bridge_softc *ptr;
  struct bridge_softc *ub;
  struct bridge_softc *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.209

```c
struct __bounds_safety::wide_ptr.bidi_indexable.209 {
  struct sockaddr_dl *ptr;
  struct sockaddr_dl *ub;
  struct sockaddr_dl *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.67

```c
struct __bounds_safety::wide_ptr.bidi_indexable.67 {
  struct bridge_iflist *ptr;
  struct bridge_iflist *ub;
  struct bridge_iflist *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.49

```c
struct __bounds_safety::wide_ptr.bidi_indexable.49 {
  struct kalloc_type_view *ptr;
  struct kalloc_type_view *ub;
  struct kalloc_type_view *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.69

```c
struct __bounds_safety::wide_ptr.bidi_indexable.69 {
  const u_char *ptr;
  const u_char *ub;
  const u_char *lb;
}

```
#### __bounds_safety::wide_ptr.indexable.94

```c
struct __bounds_safety::wide_ptr.indexable.94 {
  uint8_t *ptr;
  uint8_t *ub;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.82

```c
struct __bounds_safety::wide_ptr.bidi_indexable.82 {
  struct mac_nat_entry *ptr;
  struct mac_nat_entry *ub;
  struct mac_nat_entry *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.29

```c
struct __bounds_safety::wide_ptr.bidi_indexable.29 {
  struct mbuf *ptr;
  struct mbuf *ub;
  struct mbuf *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.126

```c
struct __bounds_safety::wide_ptr.bidi_indexable.126 {
  struct in_ifaddr *ptr;
  struct in_ifaddr *ub;
  struct in_ifaddr *lb;
}

```
#### gso_ip_tcp_state

```diff

  void (struct gso_ip_tcp_state*, struct mbuf*);* update;	
  void (struct gso_ip_tcp_state*, struct mbuf*);* internal;	
 u_int ip_m0_len;	
-__firebloom::counted_by::ip_m0_len hdr;	
+__bounds_safety::counted_by::ip_m0_len hdr;	
 struct tcphdr* tcp;	
 int mac_hlen;	
 int ip_hlen;	

```
#### __bounds_safety::wide_ptr.bidi_indexable.176

```c
struct __bounds_safety::wide_ptr.bidi_indexable.176 {
  struct bridge_delayed_call *ptr;
  struct bridge_delayed_call *ub;
  struct bridge_delayed_call *lb;
}

```
#### ifnet_init_eparams

```diff

 u_int32_t ver;	
 u_int32_t len;	
 u_int32_t flags;	
-__firebloom::sized_by::uniqueid_len uniqueid;	
+__bounds_safety::sized_by::uniqueid_len uniqueid;	
 u_int32_t uniqueid_len;	
 const char* name;	
 u_int32_t unit;	

 u_int64_t input_lt_max;	
 u_int64_t ___reserved[2];	
  errno_t (struct ifnet*, struct mbuf*, char*, protocol_family_t*);* demux;	
- errno_t (struct ifnet*, protocol_family_t, __firebloom::counted_by::demux_count, u_int32_t);* add_proto;	
+ errno_t (struct ifnet*, protocol_family_t, __bounds_safety::counted_by::demux_count, u_int32_t);* add_proto;	
  errno_t (struct ifnet*, protocol_family_t);* del_proto;	
  errno_t (struct ifnet*, const struct sockaddr*);* check_multi;	
- errno_t (struct ifnet*, struct mbuf**, const struct sockaddr*, const char*, const char*);* framer;	
+ errno_t (struct ifnet*, struct mbuf**, const struct sockaddr*, __bounds_safety::sized_by_or_null::16, __bounds_safety::sized_by_or_null::16);* framer;	
 void* softc;	
  errno_t (struct ifnet*, unsigned long, void*);* ioctl;	
  errno_t (struct ifnet*, bpf_tap_mode,  errno_t (struct ifnet*, struct mbuf*);*);* set_bpf_tap;	
  void (struct ifnet*);* detach;	
  void (struct ifnet*, const struct kev_msg*);* event;	
-__firebloom::sized_by::broadcast_len broadcast_addr;	
+__bounds_safety::sized_by::broadcast_len broadcast_addr;	
 u_int32_t broadcast_len;	
- errno_t (struct ifnet*, struct mbuf**, const struct sockaddr*, const char*, const char*, u_int32_t*, u_int32_t*);* framer_extended;	
+ errno_t (struct ifnet*, struct mbuf**, const struct sockaddr*, __bounds_safety::sized_by_or_null::16, __bounds_safety::sized_by_or_null::16, u_int32_t*, u_int32_t*);* framer_extended;	
 ifnet_subfamily_t subfamily;	
 u_int16_t tx_headroom;	
 u_int16_t tx_trailer;	

```
#### __bounds_safety::wide_ptr.bidi_indexable.147

```c
struct __bounds_safety::wide_ptr.bidi_indexable.147 {
  const struct bridge_control *ptr;
  const struct bridge_control *ub;
  const struct bridge_control *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.186

```c
struct __bounds_safety::wide_ptr.bidi_indexable.186 {
  struct kalloc_heap *ptr;
  struct kalloc_heap *ub;
  struct kalloc_heap *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.183

```c
struct __bounds_safety::wide_ptr.bidi_indexable.183 {
  struct bstp_port *ptr;
  struct bstp_port *ub;
  struct bstp_port *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.190

```c
struct __bounds_safety::wide_ptr.bidi_indexable.190 {
  struct bstp_state *ptr;
  struct bstp_state *ub;
  struct bstp_state *lb;
}

```
#### ifnet_attach_proto_param

```diff

 struct ifnet_attach_proto_param {
-__firebloom::counted_by::demux_count demux_array;	
+__bounds_safety::counted_by::demux_count demux_array;	
 u_int32_t demux_count;	
  errno_t (struct ifnet*, protocol_family_t, struct mbuf*, char*);* input;	
- errno_t (struct ifnet*, protocol_family_t, struct mbuf**, const struct sockaddr*, void*, char*, char*);* pre_output;	
+ errno_t (struct ifnet*, protocol_family_t, struct mbuf**, const struct sockaddr*, void*, __bounds_safety::sized_by::16, __bounds_safety::sized_by::16);* pre_output;	
  void (struct ifnet*, protocol_family_t, const struct kev_msg*);* event;	
  errno_t (struct ifnet*, protocol_family_t, unsigned long, void*);* ioctl;	
  errno_t (struct ifnet*, protocol_family_t);* detached;	

```
#### __bounds_safety::wide_ptr.bidi_indexable.131

```c
struct __bounds_safety::wide_ptr.bidi_indexable.131 {
  struct in6_ifaddr *ptr;
  struct in6_ifaddr *ub;
  struct in6_ifaddr *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.96

```c
struct __bounds_safety::wide_ptr.bidi_indexable.96 {
  uint16_t *ptr;
  uint16_t *ub;
  uint16_t *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.120

```c
struct __bounds_safety::wide_ptr.bidi_indexable.120 {
  struct brcsumstats *ptr;
  struct brcsumstats *ub;
  struct brcsumstats *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.38

```c
struct __bounds_safety::wide_ptr.bidi_indexable.38 {
  unsigned char *ptr;
  unsigned char *ub;
  unsigned char *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.106

```c
struct __bounds_safety::wide_ptr.bidi_indexable.106 {
  struct ifmediareq32 *ptr;
  struct ifmediareq32 *ub;
  struct ifmediareq32 *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.109

```c
struct __bounds_safety::wide_ptr.bidi_indexable.109 {
  struct if_linkparamsreq *ptr;
  struct if_linkparamsreq *ub;
  struct if_linkparamsreq *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.110

```c
struct __bounds_safety::wide_ptr.bidi_indexable.110 {
  struct if_qstatsreq *ptr;
  struct if_qstatsreq *ub;
  struct if_qstatsreq *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.114

```c
struct __bounds_safety::wide_ptr.bidi_indexable.114 {
  struct if_agentidreq *ptr;
  struct if_agentidreq *ub;
  struct if_agentidreq *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.115

```c
struct __bounds_safety::wide_ptr.bidi_indexable.115 {
  struct if_nsreq *ptr;
  struct if_nsreq *ub;
  struct if_nsreq *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.116

```c
struct __bounds_safety::wide_ptr.bidi_indexable.116 {
  struct if_netidreq *ptr;
  struct if_netidreq *ub;
  struct if_netidreq *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.127

```c
struct __bounds_safety::wide_ptr.bidi_indexable.127 {
  struct if_nat64req *ptr;
  struct if_nat64req *ub;
  struct if_nat64req *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.86

```c
struct __bounds_safety::wide_ptr.bidi_indexable.86 {
  struct ifstat *ptr;
  struct ifstat *ub;
  struct ifstat *lb;
}

```
#### __bounds_safety::wide_ptr.indexable.72

```c
struct __bounds_safety::wide_ptr.indexable.72 {
  char *ptr;
  char *ub;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.162

```c
struct __bounds_safety::wide_ptr.bidi_indexable.162 {
  struct if_order *ptr;
  struct if_order *ub;
  struct if_order *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.76

```c
struct __bounds_safety::wide_ptr.bidi_indexable.76 {
  u_int32_t *ptr;
  u_int32_t *ub;
  u_int32_t *lb;
}

```
#### __bounds_safety::wide_ptr.indexable.71

```c
struct __bounds_safety::wide_ptr.indexable.71 {
  void *ptr;
  void *ub;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.63

```c
struct __bounds_safety::wide_ptr.bidi_indexable.63 {
  const uint8_t *ptr;
  const uint8_t *ub;
  const uint8_t *lb;
}

```
#### __bounds_safety::wide_ptr.indexable.64

```c
struct __bounds_safety::wide_ptr.indexable.64 {
  uint8_t *ptr;
  uint8_t *ub;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.51

```c
struct __bounds_safety::wide_ptr.bidi_indexable.51 {
  struct ifnet *ptr;
  struct ifnet *ub;
  struct ifnet *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.84

```c
struct __bounds_safety::wide_ptr.bidi_indexable.84 {
  uuid_t *ptr;
  uuid_t *ub;
  uuid_t *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.39

```c
struct __bounds_safety::wide_ptr.bidi_indexable.39 {
  struct kalloc_heap *ptr;
  struct kalloc_heap *ub;
  struct kalloc_heap *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.52

```c
struct __bounds_safety::wide_ptr.bidi_indexable.52 {
  struct in_ifaddr *ptr;
  struct in_ifaddr *ub;
  struct in_ifaddr *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.66

```c
struct __bounds_safety::wide_ptr.bidi_indexable.66 {
  struct sockaddr *ptr;
  struct sockaddr *ub;
  struct sockaddr *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.75

```c
struct __bounds_safety::wide_ptr.bidi_indexable.75 {
  struct ifclassq *ptr;
  struct ifclassq *ub;
  struct ifclassq *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.189

```c
struct __bounds_safety::wide_ptr.bidi_indexable.189 {
  struct ifmultiaddr_dbg *ptr;
  struct ifmultiaddr_dbg *ub;
  struct ifmultiaddr_dbg *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.135

```c
struct __bounds_safety::wide_ptr.bidi_indexable.135 {
  struct radix_node_head *ptr;
  struct radix_node_head *ub;
  struct radix_node_head *lb;
}

```
#### if_linkheuristics

```c
struct if_linkheuristics {
  u_int64_t iflh_link_heuristics_cnt;
  u_int64_t iflh_link_heuristics_time;
  u_int64_t iflh_congested_link_cnt;
  u_int64_t iflh_congested_link_time;
  u_int64_t iflh_lqm_good_cnt;
  u_int64_t iflh_lqm_good_time;
  u_int64_t iflh_lqm_poor_cnt;
  u_int64_t iflh_lqm_poor_time;
  u_int64_t iflh_lqm_min_viable_cnt;
  u_int64_t iflh_lqm_min_viable_time;
  u_int64_t iflh_lqm_bad_cnt;
  u_int64_t iflh_lqm_bad_time;
  u_int64_t iflh_tcp_linkheur_stealthdrop;
  u_int64_t iflh_tcp_linkheur_noackpri;
  u_int64_t iflh_tcp_linkheur_comprxmt;
  u_int64_t iflh_tcp_linkheur_synrxmt;
  u_int64_t iflh_tcp_linkheur_rxmtfloor;
  u_int64_t iflh_udp_linkheur_stealthdrop;
}

```
#### nx_flowswitch

```diff

 uint32_t fsw_linger_cnt;	
 fsw_tso_mode_t fsw_tso_mode;	
 uint32_t fsw_tso_sw_mtu;	
+uint32_t fsw_tso_hw_v4_mtu;	
+uint32_t fsw_tso_hw_v6_mtu;	
 }

```
#### ifnet_fc_entry

```diff

 }
  ifce_entry;	
 u_int32_t ifce_flowhash;	
-struct ifnet* ifce_ifp;	
+ifnet_ref_t ifce_ifp;	
 }

```
#### ifnet_ioctl_event

```diff

 struct ifnet_ioctl_event {
-struct ifnet* ifp;	
+ifnet_ref_t ifp;	
 u_long ioctl_code;	
 }

```
#### ifnet_stats_per_flow

```diff

 u_int16_t ecn_fallback_droprxmt;	
 u_int16_t ecn_fallback_ce;	
 u_int16_t ecn_fallback_reorder;	
+u_int16_t _reserved_6;	
+u_int16_t _reserved_16;	
+u_int32_t _reserved_32;	
+u_int64_t linkheur_noackpri;	
+u_int64_t linkheur_comprxmt;	
+u_int64_t linkheur_synrxmt;	
+u_int64_t linkheur_rxmtfloor;	
 }

```
#### ether_desc_blk_str

```diff

 u_int32_t n_max_used;	
 u_int32_t n_count;	
 u_int32_t n_used;	
-struct en_desc block_ptr[0];	
+__bounds_safety::counted_by::n_count block_ptr;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.33

```c
struct __bounds_safety::wide_ptr.bidi_indexable.33 {
  u_int8_t *ptr;
  u_int8_t *ub;
  u_int8_t *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.41

```c
struct __bounds_safety::wide_ptr.bidi_indexable.41 {
  struct ether_header *ptr;
  struct ether_header *ub;
  struct ether_header *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.42

```c
struct __bounds_safety::wide_ptr.bidi_indexable.42 {
  const u_char *ptr;
  const u_char *ub;
  const u_char *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.50

```c
struct __bounds_safety::wide_ptr.bidi_indexable.50 {
  struct sockaddr_dl *ptr;
  struct sockaddr_dl *ub;
  struct sockaddr_dl *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.21

```c
struct __bounds_safety::wide_ptr.bidi_indexable.21 {
  struct en_desc *ptr;
  struct en_desc *ub;
  struct en_desc *lb;
}

```
#### __bounds_safety::wide_ptr.indexable.36

```c
struct __bounds_safety::wide_ptr.indexable.36 {
  char *ptr;
  char *ub;
}

```
#### __bounds_safety::wide_ptr.indexable.46

```c
struct __bounds_safety::wide_ptr.indexable.46 {
  uint8_t *ptr;
  uint8_t *ub;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.16

```c
struct __bounds_safety::wide_ptr.bidi_indexable.16 {
  char *ptr;
  char *ub;
  char *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.32

```c
struct __bounds_safety::wide_ptr.bidi_indexable.32 {
  uint8_t *ptr;
  uint8_t *ub;
  uint8_t *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.60

```c
struct __bounds_safety::wide_ptr.bidi_indexable.60 {
  struct ether_header *ptr;
  struct ether_header *ub;
  struct ether_header *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.61

```c
struct __bounds_safety::wide_ptr.bidi_indexable.61 {
  const struct sockaddr_inarp *ptr;
  const struct sockaddr_inarp *ub;
  const struct sockaddr_inarp *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.62

```c
struct __bounds_safety::wide_ptr.bidi_indexable.62 {
  struct ifaddr *ptr;
  struct ifaddr *ub;
  struct ifaddr *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.27

```c
struct __bounds_safety::wide_ptr.bidi_indexable.27 {
  struct mbuf *ptr;
  struct mbuf *ub;
  struct mbuf *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.24

```c
struct __bounds_safety::wide_ptr.bidi_indexable.24 {
  char *ptr;
  char *ub;
  char *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.53

```c
struct __bounds_safety::wide_ptr.bidi_indexable.53 {
  struct loopback_header *ptr;
  struct loopback_header *ub;
  struct loopback_header *lb;
}

```
#### __bounds_safety::wide_ptr.indexable.55

```c
struct __bounds_safety::wide_ptr.indexable.55 {
  const uint8_t *ptr;
  const uint8_t *ub;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.45

```c
struct __bounds_safety::wide_ptr.bidi_indexable.45 {
  struct if_linkheuristics *ptr;
  struct if_linkheuristics *ub;
  struct if_linkheuristics *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.5

```c
struct __bounds_safety::wide_ptr.bidi_indexable.5 {
  struct ifnet *ptr;
  struct ifnet *ub;
  struct ifnet *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.81

```c
struct __bounds_safety::wide_ptr.bidi_indexable.81 {
  struct sockaddr_dl *ptr;
  struct sockaddr_dl *ub;
  struct sockaddr_dl *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.40

```c
struct __bounds_safety::wide_ptr.bidi_indexable.40 {
  struct ifnet *ptr;
  struct ifnet *ub;
  struct ifnet *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.78

```c
struct __bounds_safety::wide_ptr.bidi_indexable.78 {
  struct ether_header *ptr;
  struct ether_header *ub;
  struct ether_header *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.55

```c
struct __bounds_safety::wide_ptr.bidi_indexable.55 {
  struct ifmediareq32 *ptr;
  struct ifmediareq32 *ub;
  struct ifmediareq32 *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.54

```c
struct __bounds_safety::wide_ptr.bidi_indexable.54 {
  struct ifaddr *ptr;
  struct ifaddr *ub;
  struct ifaddr *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.123

```c
struct __bounds_safety::wide_ptr.bidi_indexable.123 {
  struct kern_event_msg *ptr;
  struct kern_event_msg *ub;
  struct kern_event_msg *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.103

```c
struct __bounds_safety::wide_ptr.bidi_indexable.103 {
  struct nexus_controller *ptr;
  struct nexus_controller *ub;
  struct nexus_controller *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.31

```c
struct __bounds_safety::wide_ptr.bidi_indexable.31 {
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
#### ifbond_s

```diff

 short ifb_max_active;	
 struct LAG_s* ifb_active_lag;	
 struct ifmultiaddr* ifb_ifma_slow_proto;	
-__firebloom::counted_by::ifb_distributing_max ifb_distributing_array;	
+__bounds_safety::counted_by::ifb_distributing_max ifb_distributing_array;	
 int ifb_distributing_count;	
 int ifb_distributing_max;	
 int ifb_last_link_event;	

```
#### __bounds_safety::wide_ptr.indexable.86

```c
struct __bounds_safety::wide_ptr.indexable.86 {
  uint8_t *ptr;
  uint8_t *ub;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.113

```c
struct __bounds_safety::wide_ptr.bidi_indexable.113 {
  struct lacp_collector_tlv_s *ptr;
  struct lacp_collector_tlv_s *ub;
  struct lacp_collector_tlv_s *lb;
}

```
#### __bounds_safety::wide_ptr.indexable.85

```c
struct __bounds_safety::wide_ptr.indexable.85 {
  const uint8_t *ptr;
  const uint8_t *ub;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.71

```c
struct __bounds_safety::wide_ptr.bidi_indexable.71 {
  struct ifmediareq32 *ptr;
  struct ifmediareq32 *ub;
  struct ifmediareq32 *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.70

```c
struct __bounds_safety::wide_ptr.bidi_indexable.70 {
  struct ifreq *ptr;
  struct ifreq *ub;
  struct ifreq *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.119

```c
struct __bounds_safety::wide_ptr.bidi_indexable.119 {
  struct if_bond_partner_state *ptr;
  struct if_bond_partner_state *ub;
  struct if_bond_partner_state *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.118

```c
struct __bounds_safety::wide_ptr.bidi_indexable.118 {
  struct if_bond_status_req *ptr;
  struct if_bond_status_req *ub;
  struct if_bond_status_req *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.3

```c
struct __bounds_safety::wide_ptr.bidi_indexable.3 {
  struct devtimer_s *ptr;
  struct devtimer_s *ub;
  struct devtimer_s *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.47

```c
struct __bounds_safety::wide_ptr.bidi_indexable.47 {
  char *ptr;
  char *ub;
  char *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.59

```c
struct __bounds_safety::wide_ptr.bidi_indexable.59 {
  struct sockaddr *ptr;
  struct sockaddr *ub;
  struct sockaddr *lb;
}

```
#### __bounds_safety::wide_ptr.indexable.70

```c
struct __bounds_safety::wide_ptr.indexable.70 {
  uint8_t *ptr;
  uint8_t *ub;
}

```
#### ndrv_protocol_desc_kernel

```diff

 u_int32_t version;	
 u_int32_t protocol_family;	
 u_int32_t demux_count;	
-__firebloom::counted_by::demux_count demux_array;	
+__bounds_safety::counted_by::demux_count demux_array;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.12

```c
struct __bounds_safety::wide_ptr.bidi_indexable.12 {
  struct socket *ptr;
  struct socket *ub;
  struct socket *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.23

```c
struct __bounds_safety::wide_ptr.bidi_indexable.23 {
  lck_mtx_t *ptr;
  lck_mtx_t *ub;
  lck_mtx_t *lb;
}

```
#### __bounds_safety::wide_ptr.indexable.61

```c
struct __bounds_safety::wide_ptr.indexable.61 {
  char *ptr;
  char *ub;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.74

```c
struct __bounds_safety::wide_ptr.bidi_indexable.74 {
  struct route_event_nwk_wq_entry *ptr;
  struct route_event_nwk_wq_entry *ub;
  struct route_event_nwk_wq_entry *lb;
}

```
#### __bounds_safety::wide_ptr.indexable.42

```c
struct __bounds_safety::wide_ptr.indexable.42 {
  uint8_t *ptr;
  uint8_t *ub;
}

```
#### __bounds_safety::wide_ptr.indexable.48

```c
struct __bounds_safety::wide_ptr.indexable.48 {
  const void *ptr;
  const void *ub;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.65

```c
struct __bounds_safety::wide_ptr.bidi_indexable.65 {
  struct kalloc_heap *ptr;
  struct kalloc_heap *ub;
  struct kalloc_heap *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.72

```c
struct __bounds_safety::wide_ptr.bidi_indexable.72 {
  struct route_event *ptr;
  struct route_event *ub;
  struct route_event *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.101

```c
struct __bounds_safety::wide_ptr.bidi_indexable.101 {
  struct eventhandler_entry *ptr;
  struct eventhandler_entry *ub;
  struct eventhandler_entry *lb;
}

```
#### __bounds_safety::wide_ptr.indexable.47

```c
struct __bounds_safety::wide_ptr.indexable.47 {
  char *ptr;
  char *ub;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.77

```c
struct __bounds_safety::wide_ptr.bidi_indexable.77 {
  struct in6_ifaddr *ptr;
  struct in6_ifaddr *ub;
  struct in6_ifaddr *lb;
}

```
#### __bounds_safety::wide_ptr.indexable.57

```c
struct __bounds_safety::wide_ptr.indexable.57 {
  uint8_t *ptr;
  uint8_t *ub;
}

```
#### walkarg

```diff

 int w_tmemsize;	
 int w_op;	
 int w_arg;	
-__firebloom::sized_by::w_tmemsize w_tmem;	
+__bounds_safety::sized_by::w_tmemsize w_tmem;	
 struct sysctl_req* w_req;	
 }

```
#### nstat_provider

```diff

 struct nstat_provider* next;	
 nstat_provider_id_t nstat_provider_id;	
 size_t nstat_descriptor_length;	
- errno_t (__firebloom::sized_by::length, u_int32_t, void**);* nstat_lookup;	
+ errno_t (__bounds_safety::sized_by::length, u_int32_t, void**);* nstat_lookup;	
  int (void*);* nstat_gone;	
  errno_t (void*, struct nstat_counts*, int*);* nstat_counts;	
  errno_t (nstat_client*, nstat_msg_add_all_srcs*);* nstat_watcher_add;	
  void (nstat_client*);* nstat_watcher_remove;	
- errno_t (void*, __firebloom::sized_by::len, size_t);* nstat_copy_descriptor;	
+ errno_t (void*, __bounds_safety::sized_by::len, size_t);* nstat_copy_descriptor;	
  void (void*, boolean_t);* nstat_release;	
  _Bool (void*, nstat_provider_filter*, u_int64_t);* nstat_reporting_allowed;	
  _Bool (void*, void*);* nstat_cookie_equal;	

```
#### inpcb

```diff

 struct thread* inp_bind_in_progress_thread;	
  void (void*, int, uint32_t, uint32_t, _Bool*);* necp_cb;	
 size_t inp_resolver_signature_length;	
-__firebloom::sized_by::inp_resolver_signature_length inp_resolver_signature;	
+__bounds_safety::sized_by::inp_resolver_signature_length inp_resolver_signature;	
 struct ns_token* inp_netns_token;	
 struct ns_token* inp_wildcard_netns_token;	
-__firebloom::sized_by::inp_keepalive_datalen inp_keepalive_data;	
+__bounds_safety::sized_by::inp_keepalive_datalen inp_keepalive_data;	
 uint8_t inp_keepalive_datalen;	
 uint8_t inp_keepalive_type;	
 uint16_t inp_keepalive_interval;	

```
#### inpcbinfo

```diff

 uint16_t ipi_lastlow;	
 uint16_t ipi_lasthi;	
 struct kalloc_type_view* ipi_zone;	
-__firebloom::counted_by::ipi_hashbase_count ipi_hashbase;	
+__bounds_safety::counted_by::ipi_hashbase_count ipi_hashbase;	
 size_t ipi_hashbase_count;	
 u_long ipi_hashmask;	
-__firebloom::counted_by::ipi_porthashbase_count ipi_porthashbase;	
+__bounds_safety::counted_by::ipi_porthashbase_count ipi_porthashbase;	
 size_t ipi_porthashbase_count;	
 u_long ipi_porthashmask;	
 lck_attr_t ipi_lock_attr;	

```
#### ip_moptions

```diff

 u_short imo_num_memberships;	
 u_short imo_max_memberships;	
 u_short imo_max_filters;	
-__firebloom::counted_by::imo_max_memberships imo_membership;	
-__firebloom::counted_by::imo_max_filters imo_mfilters;	
+__bounds_safety::counted_by::imo_max_memberships imo_membership;	
+__bounds_safety::counted_by::imo_max_filters imo_mfilters;	
 u_int32_t imo_multicast_vif;	
 struct in_addr imo_multicast_addr;	
  void (struct ip_moptions*, int);* imo_trace;	

```
#### ip6_moptions

```diff

 u_short im6o_num_memberships;	
 u_short im6o_max_memberships;	
 u_short im6o_max_filters;	
-__firebloom::counted_by::im6o_max_memberships im6o_membership;	
-__firebloom::counted_by::im6o_max_filters im6o_mfilters;	
+__bounds_safety::counted_by::im6o_max_memberships im6o_membership;	
+__bounds_safety::counted_by::im6o_max_filters im6o_mfilters;	
  void (struct ip6_moptions*, int);* im6o_trace;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.89

```c
struct __bounds_safety::wide_ptr.bidi_indexable.89 {
  nstat_flow_data *ptr;
  nstat_flow_data *ub;
  nstat_flow_data *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.92

```c
struct __bounds_safety::wide_ptr.bidi_indexable.92 {
  struct xsocket_n *ptr;
  struct xsocket_n *ub;
  struct xsocket_n *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.94

```c
struct __bounds_safety::wide_ptr.bidi_indexable.94 {
  struct xsockstat_n *ptr;
  struct xsockstat_n *ub;
  struct xsockstat_n *lb;
}

```
#### tcpcb

```diff

 u_int32_t t_connect_time;	
 uint64_t t_rcvwnd_limited_total_time;	
 uint64_t t_rcvwnd_limited_start_time;	
-uint32_t t_comp_gencnt;	
-uint32_t t_comp_lastinc;	
+uint32_t t_comp_rxmt_gencnt;	
+uint32_t t_comp_ack_gencnt;	
+uint32_t t_comp_ack_lastinc;	
 uint32_t t_ts_offset;	
 uint32_t curr_rtt_hist[4];	
 uint32_t curr_rtt_min;	

```
#### __bounds_safety::wide_ptr.bidi_indexable.132

```c
struct __bounds_safety::wide_ptr.bidi_indexable.132 {
  nstat_route_descriptor *ptr;
  nstat_route_descriptor *ub;
  nstat_route_descriptor *lb;
}

```
#### __bounds_safety::wide_ptr.indexable.136

```c
struct __bounds_safety::wide_ptr.indexable.136 {
  char *ptr;
  char *ub;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.143

```c
struct __bounds_safety::wide_ptr.bidi_indexable.143 {
  nstat_tcp_descriptor *ptr;
  nstat_tcp_descriptor *ub;
  nstat_tcp_descriptor *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.148

```c
struct __bounds_safety::wide_ptr.bidi_indexable.148 {
  nstat_udp_descriptor *ptr;
  nstat_udp_descriptor *ub;
  nstat_udp_descriptor *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.153

```c
struct __bounds_safety::wide_ptr.bidi_indexable.153 {
  nstat_connection_descriptor *ptr;
  nstat_connection_descriptor *ub;
  nstat_connection_descriptor *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.157

```c
struct __bounds_safety::wide_ptr.bidi_indexable.157 {
  nstat_msg_src_description *ptr;
  nstat_msg_src_description *ub;
  nstat_msg_src_description *lb;
}

```
#### __bounds_safety::wide_ptr.indexable.140

```c
struct __bounds_safety::wide_ptr.indexable.140 {
  uint8_t *ptr;
  uint8_t *ub;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.160

```c
struct __bounds_safety::wide_ptr.bidi_indexable.160 {
  nstat_ifnet_descriptor *ptr;
  nstat_ifnet_descriptor *ub;
  nstat_ifnet_descriptor *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.171

```c
struct __bounds_safety::wide_ptr.bidi_indexable.171 {
  nstat_msg_sysinfo_counts *ptr;
  nstat_msg_sysinfo_counts *ub;
  nstat_msg_sysinfo_counts *lb;
}

```
#### __bounds_safety::wide_ptr.indexable.173

```c
struct __bounds_safety::wide_ptr.indexable.173 {
  struct nstat_sysinfo_keyval *ptr;
  struct nstat_sysinfo_keyval *ub;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.177

```c
struct __bounds_safety::wide_ptr.bidi_indexable.177 {
  nstat_msg_src_update *ptr;
  nstat_msg_src_update *ub;
  nstat_msg_src_update *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.179

```c
struct __bounds_safety::wide_ptr.bidi_indexable.179 {
  nstat_msg_src_extended_item_hdr *ptr;
  nstat_msg_src_extended_item_hdr *ub;
  nstat_msg_src_extended_item_hdr *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.191

```c
struct __bounds_safety::wide_ptr.bidi_indexable.191 {
  struct nstat_msg_hdr *ptr;
  struct nstat_msg_hdr *ub;
  struct nstat_msg_hdr *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.193

```c
struct __bounds_safety::wide_ptr.bidi_indexable.193 {
  nstat_msg_add_src_req *ptr;
  nstat_msg_add_src_req *ub;
  nstat_msg_add_src_req *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.196

```c
struct __bounds_safety::wide_ptr.bidi_indexable.196 {
  nstat_msg_add_all_srcs *ptr;
  nstat_msg_add_all_srcs *ub;
  nstat_msg_add_all_srcs *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.202

```c
struct __bounds_safety::wide_ptr.bidi_indexable.202 {
  nstat_msg_src_added *ptr;
  nstat_msg_src_added *ub;
  nstat_msg_src_added *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.90

```c
struct __bounds_safety::wide_ptr.bidi_indexable.90 {
  struct kalloc_heap *ptr;
  struct kalloc_heap *ub;
  struct kalloc_heap *lb;
}

```
#### __bounds_safety::wide_ptr.indexable.195

```c
struct __bounds_safety::wide_ptr.indexable.195 {
  struct nstat_msg_add_src *ptr;
  struct nstat_msg_add_src *ub;
}

```
#### __bounds_safety::wide_ptr.indexable.158

```c
struct __bounds_safety::wide_ptr.indexable.158 {
  struct nstat_msg_src_description *ptr;
  struct nstat_msg_src_description *ub;
}

```
#### __bounds_safety::wide_ptr.indexable.178

```c
struct __bounds_safety::wide_ptr.indexable.178 {
  struct nstat_msg_src_update *ptr;
  struct nstat_msg_src_update *ub;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.172

```c
struct __bounds_safety::wide_ptr.bidi_indexable.172 {
  nstat_sysinfo_keyval *ptr;
  nstat_sysinfo_keyval *ub;
  nstat_sysinfo_keyval *lb;
}

```
#### __bounds_safety::wide_ptr.indexable.174

```c
struct __bounds_safety::wide_ptr.indexable.174 {
  struct nstat_msg_sysinfo_counts *ptr;
  struct nstat_msg_sysinfo_counts *ub;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.166

```c
struct __bounds_safety::wide_ptr.bidi_indexable.166 {
  nstat_ifnet_desc_link_status *ptr;
  nstat_ifnet_desc_link_status *ub;
  nstat_ifnet_desc_link_status *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.169

```c
struct __bounds_safety::wide_ptr.bidi_indexable.169 {
  nstat_ifnet_desc_wifi_status *ptr;
  nstat_ifnet_desc_wifi_status *ub;
  nstat_ifnet_desc_wifi_status *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.167

```c
struct __bounds_safety::wide_ptr.bidi_indexable.167 {
  nstat_ifnet_desc_cellular_status *ptr;
  nstat_ifnet_desc_cellular_status *ub;
  nstat_ifnet_desc_cellular_status *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.168

```c
struct __bounds_safety::wide_ptr.bidi_indexable.168 {
  struct if_cellular_status_v1 *ptr;
  struct if_cellular_status_v1 *ub;
  struct if_cellular_status_v1 *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.145

```c
struct __bounds_safety::wide_ptr.bidi_indexable.145 {
  struct socket *ptr;
  struct socket *ub;
  struct socket *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.154

```c
struct __bounds_safety::wide_ptr.bidi_indexable.154 {
  const nstat_ifnet_add_param *ptr;
  const nstat_ifnet_add_param *ub;
  const nstat_ifnet_add_param *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.130

```c
struct __bounds_safety::wide_ptr.bidi_indexable.130 {
  struct rtentry *ptr;
  struct rtentry *ub;
  struct rtentry *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.128

```c
struct __bounds_safety::wide_ptr.bidi_indexable.128 {
  struct radix_node_head *ptr;
  struct radix_node_head *ub;
  struct radix_node_head *lb;
}

```
#### __bounds_safety::wide_ptr.indexable.74

```c
struct __bounds_safety::wide_ptr.indexable.74 {
  uint8_t *ptr;
  uint8_t *ub;
}

```
#### __bounds_safety::wide_ptr.indexable.78

```c
struct __bounds_safety::wide_ptr.indexable.78 {
  void *ptr;
  void *ub;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.129

```c
struct __bounds_safety::wide_ptr.bidi_indexable.129 {
  struct kalloc_heap *ptr;
  struct kalloc_heap *ub;
  struct kalloc_heap *lb;
}

```
#### ifnet_init_params

```diff

 struct ifnet_init_params {
-__firebloom::sized_by::uniqueid_len uniqueid;	
+__bounds_safety::sized_by::uniqueid_len uniqueid;	
 u_int32_t uniqueid_len;	
 const char* name;	
 u_int32_t unit;	

 u_int32_t type;	
  errno_t (struct ifnet*, struct mbuf*);* output;	
  errno_t (struct ifnet*, struct mbuf*, char*, protocol_family_t*);* demux;	
- errno_t (struct ifnet*, protocol_family_t, __firebloom::counted_by::demux_count, u_int32_t);* add_proto;	
+ errno_t (struct ifnet*, protocol_family_t, __bounds_safety::counted_by::demux_count, u_int32_t);* add_proto;	
  errno_t (struct ifnet*, protocol_family_t);* del_proto;	
  errno_t (struct ifnet*, const struct sockaddr*);* check_multi;	
- errno_t (struct ifnet*, struct mbuf**, const struct sockaddr*, const char*, const char*);* framer;	
+ errno_t (struct ifnet*, struct mbuf**, const struct sockaddr*, __bounds_safety::sized_by_or_null::16, __bounds_safety::sized_by_or_null::16);* framer;	
 void* softc;	
  errno_t (struct ifnet*, unsigned long, void*);* ioctl;	
  errno_t (struct ifnet*, bpf_tap_mode,  errno_t (struct ifnet*, struct mbuf*);*);* set_bpf_tap;	
  void (struct ifnet*);* detach;	
  void (struct ifnet*, const struct kev_msg*);* event;	
-__firebloom::sized_by::broadcast_len broadcast_addr;	
+__bounds_safety::sized_by::broadcast_len broadcast_addr;	
 u_int32_t broadcast_len;	
 }

```
#### __bounds_safety::wide_ptr.indexable.100

```c
struct __bounds_safety::wide_ptr.indexable.100 {
  const void *ptr;
  const void *ub;
}

```
#### net_str_id_entry

```diff

 uint32_t nsi_flags;	
 uint32_t nsi_id;	
 uint32_t nsi_length;	
-char nsi_string[-1];	
+__bounds_safety::counted_by::nsi_length nsi_string;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.112

```c
struct __bounds_safety::wide_ptr.bidi_indexable.112 {
  const struct mbuf **ptr;
  const struct mbuf **ub;
  const struct mbuf **lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.98

```c
struct __bounds_safety::wide_ptr.bidi_indexable.98 {
  struct ifnet *ptr;
  struct ifnet *ub;
  struct ifnet *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.137

```c
struct __bounds_safety::wide_ptr.bidi_indexable.137 {
  struct ipsec_stats_param *ptr;
  struct ipsec_stats_param *ub;
  struct ipsec_stats_param *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.125

```c
struct __bounds_safety::wide_ptr.bidi_indexable.125 {
  struct kern_nexus *ptr;
  struct kern_nexus *ub;
  struct kern_nexus *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.122

```c
struct __bounds_safety::wide_ptr.bidi_indexable.122 {
  struct mbuf *ptr;
  struct mbuf *ub;
  struct mbuf *lb;
}

```
#### necp_client

```diff

 struct _necp_client_flow_tree flow_registrations;	
 struct _necp_client_assertion_list assertion_list;	
 size_t assigned_group_members_length;	
-__firebloom::counted_by::assigned_group_members_length assigned_group_members;	
+__bounds_safety::counted_by::assigned_group_members_length assigned_group_members;	
 struct rtentry* current_route;	
 struct necp_client_interface_option interface_options[4];	
-struct __firebloom::wide_ptr.indexable extra_interface_options;	
+struct __bounds_safety::wide_ptr.indexable extra_interface_options;	
 u_int8_t interface_option_count;	
 struct necp_client_result_netagent failed_trigger_agent;	
 void* agent_handle;	

 uuid_t parent_client_id;	
 struct necp_client* original_parameters_source;	
 size_t parameters_length;	
-__firebloom::sized_by::parameters_length parameters;	
+__bounds_safety::sized_by::parameters_length parameters;	
 }

```
#### necp_client_flow

```diff

 union necp_sockaddr_union local_addr;	
 union necp_sockaddr_union remote_addr;	
 size_t assigned_results_length;	
-__firebloom::counted_by::assigned_results_length assigned_results;	
+__bounds_safety::counted_by::assigned_results_length assigned_results;	
 }

```
#### necp_client_update

```diff

  chain;	
 uuid_t client_id;	
 size_t update_length;	
-__firebloom::sized_by::update_length update;	
+__bounds_safety::sized_by::update_length update;	
 }

```
#### __bounds_safety::wide_ptr.indexable.133

```c
struct __bounds_safety::wide_ptr.indexable.133 {
  void *ptr;
  void *ub;
}

```
#### __bounds_safety::wide_ptr.indexable.126

```c
struct __bounds_safety::wide_ptr.indexable.126 {
  char *ptr;
  char *ub;
}

```
#### necp_client_group_members

```diff

 struct necp_client_group_members {
 size_t group_members_length;	
-__firebloom::sized_by::group_members_length group_members;	
+__bounds_safety::sized_by::group_members_length group_members;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.185

```c
struct __bounds_safety::wide_ptr.bidi_indexable.185 {
  struct necp_quic_stats *ptr;
  struct necp_quic_stats *ub;
  struct necp_quic_stats *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.188

```c
struct __bounds_safety::wide_ptr.bidi_indexable.188 {
  struct necp_tcp_stats *ptr;
  struct necp_tcp_stats *ub;
  struct necp_tcp_stats *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.136

```c
struct __bounds_safety::wide_ptr.bidi_indexable.136 {
  uint32_t *ptr;
  uint32_t *ub;
  uint32_t *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.151

```c
struct __bounds_safety::wide_ptr.bidi_indexable.151 {
  struct necp_client_interface_option *ptr;
  struct necp_client_interface_option *ub;
  struct necp_client_interface_option *lb;
}

```
#### __bounds_safety::wide_ptr.indexable.230

```c
struct __bounds_safety::wide_ptr.indexable.230 {
  struct necp_client_add_flow *ptr;
  struct necp_client_add_flow *ub;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.258

```c
struct __bounds_safety::wide_ptr.bidi_indexable.258 {
  nstat_interface_counts *ptr;
  nstat_interface_counts *ub;
  nstat_interface_counts *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.259

```c
struct __bounds_safety::wide_ptr.bidi_indexable.259 {
  struct necp_udp_stats *ptr;
  struct necp_udp_stats *ub;
  struct necp_udp_stats *lb;
}

```
#### __bounds_safety::wide_ptr.indexable.277

```c
struct __bounds_safety::wide_ptr.indexable.277 {
  struct necp_client_signable *ptr;
  struct necp_client_signable *ub;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.142

```c
struct __bounds_safety::wide_ptr.bidi_indexable.142 {
  struct selinfo *ptr;
  struct selinfo *ub;
  struct selinfo *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.174

```c
struct __bounds_safety::wide_ptr.bidi_indexable.174 {
  struct sockaddr_in *ptr;
  struct sockaddr_in *ub;
  struct sockaddr_in *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.204

```c
struct __bounds_safety::wide_ptr.bidi_indexable.204 {
  struct ifaddr *ptr;
  struct ifaddr *ub;
  struct ifaddr *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.207

```c
struct __bounds_safety::wide_ptr.bidi_indexable.207 {
  struct necp_client_update *ptr;
  struct necp_client_update *ub;
  struct necp_client_update *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.161

```c
struct __bounds_safety::wide_ptr.bidi_indexable.161 {
  struct necp_policy_condition_addr *ptr;
  struct necp_policy_condition_addr *ub;
  struct necp_policy_condition_addr *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.223

```c
struct __bounds_safety::wide_ptr.bidi_indexable.223 {
  struct nstat_counts *ptr;
  struct nstat_counts *ub;
  struct nstat_counts *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.247

```c
struct __bounds_safety::wide_ptr.bidi_indexable.247 {
  const struct sk_stats_flow *ptr;
  const struct sk_stats_flow *ub;
  const struct sk_stats_flow *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.250

```c
struct __bounds_safety::wide_ptr.bidi_indexable.250 {
  nstat_quic_descriptor *ptr;
  nstat_quic_descriptor *ub;
  nstat_quic_descriptor *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.260

```c
struct __bounds_safety::wide_ptr.bidi_indexable.260 {
  nstat_udp_descriptor *ptr;
  nstat_udp_descriptor *ub;
  nstat_udp_descriptor *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.222

```c
struct __bounds_safety::wide_ptr.bidi_indexable.222 {
  nstat_connection_descriptor *ptr;
  nstat_connection_descriptor *ub;
  nstat_connection_descriptor *lb;
}

```
#### _netagent_list

```diff

 struct _netagent_list {
-struct netagent_wrapper* lh_first;	
+struct netagent_registration* lh_first;	
 }

```
#### netagent_registration

```c
struct netagent_registration {
  struct {
    struct netagent_registration  *le_next;
    struct netagent_registration **le_prev;
  } global_chain;
  struct {
    struct netagent_registration  *tqe_next;
    struct netagent_registration **tqe_prev;
  } session_chain;
  lck_rw_t  agent_lock;
  u_int32_t control_unit;
  errno_t(u_int8_t, __bounds_safety::counted_by::16UL, pid_t, void *, void *,
          struct necp_client_agent_parameters *,
          __bounds_safety::sized_by::*assigned_results_length *, size_t *);
  *event_handler;
  void                                          *event_context;
  u_int32_t                                      generation;
  u_int64_t                                      use_count;
  u_int64_t                                      need_tokens_event_deadline;
  u_int32_t                                      token_count;
  u_int32_t                                      token_low_water;
  int32_t                                        last_client_error;
  u_int32_t                                      client_error_count;
  u_int8_t                                       allow_multiple_registrations;
  u_int8_t                                       __pad_bytes[2];
  struct netagent_token_list_s                   token_list;
  struct netagent_client_list_s                  pending_triggers_list;
  size_t                                         netagent_alloc_size;
  __bounds_safety::sized_by::netagent_alloc_size netagent;
}

```
#### netagent_token

```diff

 }
  token_chain;	
 u_int32_t token_length;	
-struct __firebloom::wide_ptr.indexable token_bytes;	
+struct __bounds_safety::wide_ptr.indexable token_bytes;	
 }

```
#### _netagent_registration_list

```c
struct _netagent_registration_list {
  struct netagent_registration  *tqh_first;
  struct netagent_registration **tqh_last;
}

```
#### netagent_session

```diff

 struct netagent_session {
 u_int32_t control_unit;	
 lck_mtx_t session_lock;	
-struct netagent_wrapper* wrapper;	
- errno_t (u_int8_t, __firebloom::counted_by::16UL, pid_t, void*, void*, struct necp_client_agent_parameters*, __firebloom::sized_by::*assigned_results_length*, size_t*);* event_handler;	
+struct _netagent_registration_list registrations;	
+ errno_t (u_int8_t, __bounds_safety::counted_by::16UL, pid_t, void*, void*, struct necp_client_agent_parameters*, __bounds_safety::sized_by::*assigned_results_length*, size_t*);* event_handler;	
 void* event_context;	
+_Bool allow_multiple_registrations;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.6

```c
struct __bounds_safety::wide_ptr.bidi_indexable.6 {
  void *ptr;
  void *ub;
  void *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.15

```c
struct __bounds_safety::wide_ptr.bidi_indexable.15 {
  u_int8_t *ptr;
  u_int8_t *ub;
  u_int8_t *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.7

```c
struct __bounds_safety::wide_ptr.bidi_indexable.7 {
  struct netagent_registration *ptr;
  struct netagent_registration *ub;
  struct netagent_registration *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.13

```c
struct __bounds_safety::wide_ptr.bidi_indexable.13 {
  struct netagent *ptr;
  struct netagent *ub;
  struct netagent *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.2

```c
struct __bounds_safety::wide_ptr.bidi_indexable.2 {
  uint8_t *ptr;
  uint8_t *ub;
  uint8_t *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.1

```c
struct __bounds_safety::wide_ptr.bidi_indexable.1 {
  struct kalloc_heap *ptr;
  struct kalloc_heap *ub;
  struct kalloc_heap *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.9

```c
struct __bounds_safety::wide_ptr.bidi_indexable.9 {
  const uint8_t *ptr;
  const uint8_t *ub;
  const uint8_t *lb;
}

```
#### pf_pdesc

```diff

 }
  lookup;	
 u_int64_t tot_len;	
-__firebloom::sized_by::hdrmaxlen hdr;	
+__bounds_safety::sized_by::hdrmaxlen hdr;	
 size_t hdrlen;	
 size_t hdrmaxlen;	
 struct pf_addr baddr;	

```
#### __bounds_safety::wide_ptr.bidi_indexable.17

```c
struct __bounds_safety::wide_ptr.bidi_indexable.17 {
  struct ifnet *ptr;
  struct ifnet *ub;
  struct ifnet *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.18

```c
struct __bounds_safety::wide_ptr.bidi_indexable.18 {
  struct mbuf *ptr;
  struct mbuf *ub;
  struct mbuf *lb;
}

```
#### eventhandler_entry_in6_clat46_event

```diff

 struct eventhandler_entry_in6_clat46_event {
 struct eventhandler_entry ee;	
- void (struct eventhandler_entry_arg, in6_clat46_evhdlr_code_t, pid_t, __firebloom::counted_by::16UL);* eh_func;	
+ void (struct eventhandler_entry_arg, in6_clat46_evhdlr_code_t, pid_t, __bounds_safety::counted_by::16UL);* eh_func;	
 }

```
#### __bounds_safety::wide_ptr.indexable.142

```c
struct __bounds_safety::wide_ptr.indexable.142 {
  uint8_t *ptr;
  uint8_t *ub;
}

```
#### __bounds_safety::wide_ptr.indexable.99

```c
struct __bounds_safety::wide_ptr.indexable.99 {
  void *ptr;
  void *ub;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.134

```c
struct __bounds_safety::wide_ptr.bidi_indexable.134 {
  struct pf_state_peer *ptr;
  struct pf_state_peer *ub;
  struct pf_state_peer *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.133

```c
struct __bounds_safety::wide_ptr.bidi_indexable.133 {
  struct icmp6_hdr *ptr;
  struct icmp6_hdr *ub;
  struct icmp6_hdr *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.138

```c
struct __bounds_safety::wide_ptr.bidi_indexable.138 {
  u_int8_t *ptr;
  u_int8_t *ub;
  u_int8_t *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.192

```c
struct __bounds_safety::wide_ptr.bidi_indexable.192 {
  struct ip *ptr;
  struct ip *ub;
  struct ip *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.8

```c
struct __bounds_safety::wide_ptr.bidi_indexable.8 {
  struct pf_ruleset *ptr;
  struct pf_ruleset *ub;
  struct pf_ruleset *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.141

```c
struct __bounds_safety::wide_ptr.bidi_indexable.141 {
  struct pfioc_kernel_token *ptr;
  struct pfioc_kernel_token *ub;
  struct pfioc_kernel_token *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.87

```c
struct __bounds_safety::wide_ptr.bidi_indexable.87 {
  struct m_tag *ptr;
  struct m_tag *ub;
  struct m_tag *lb;
}

```
#### __bounds_safety::wide_ptr.indexable.50

```c
struct __bounds_safety::wide_ptr.indexable.50 {
  char *ptr;
  char *ub;
}

```
#### cfil_sign_parameters

```diff

 struct cfil_sign_parameters {
 struct cfil_crypto_state* csp_state;	
 struct cfil_crypto_data* csp_data;	
-struct __firebloom::wide_ptr.indexable.50 csp_signature;	
+struct __bounds_safety::wide_ptr.indexable.66 csp_signature;	
 uint32_t* csp_signature_size;	
 }

```
#### __bounds_safety::wide_ptr.indexable.66

```c
struct __bounds_safety::wide_ptr.indexable.66 {
  uint8_t *ptr;
  uint8_t *ub;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.149

```c
struct __bounds_safety::wide_ptr.bidi_indexable.149 {
  struct ip *ptr;
  struct ip *ub;
  struct ip *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.163

```c
struct __bounds_safety::wide_ptr.bidi_indexable.163 {
  struct cfil_msg_sock_stats *ptr;
  struct cfil_msg_sock_stats *ub;
  struct cfil_msg_sock_stats *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.105

```c
struct __bounds_safety::wide_ptr.bidi_indexable.105 {
  struct mbuf *ptr;
  struct mbuf *ub;
  struct mbuf *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.155

```c
struct __bounds_safety::wide_ptr.bidi_indexable.155 {
  struct cfe_buf_stat *ptr;
  struct cfe_buf_stat *ub;
  struct cfe_buf_stat *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.144

```c
struct __bounds_safety::wide_ptr.bidi_indexable.144 {
  struct cfil_msg_set_crypto_key *ptr;
  struct cfil_msg_set_crypto_key *ub;
  struct cfil_msg_set_crypto_key *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.158

```c
struct __bounds_safety::wide_ptr.bidi_indexable.158 {
  struct cfil_udp_data_pending_context *ptr;
  struct cfil_udp_data_pending_context *ub;
  struct cfil_udp_data_pending_context *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.159

```c
struct __bounds_safety::wide_ptr.bidi_indexable.159 {
  struct cfil_udp_notify_shutdown_context *ptr;
  struct cfil_udp_notify_shutdown_context *ub;
  struct cfil_udp_notify_shutdown_context *lb;
}

```
#### __bounds_safety::wide_ptr.indexable.8

```c
struct __bounds_safety::wide_ptr.indexable.8 {
  const bitmap_t *ptr;
  const bitmap_t *ub;
}

```
#### fq_codel_sched_data

```diff

 struct fq_codel_sched_data {
 struct ifclassq* fqs_ifq;	
-__firebloom::counted_by::fqs_flows_count fqs_flows;	
+__bounds_safety::counted_by::fqs_flows_count fqs_flows;	
 uint32_t fqs_flows_count;	
 uint32_t fqs_pkt_droplimit;	
 uint8_t fqs_throttle;	

```
#### heap

```diff

 struct heap {
 size_t limit;	
 size_t size;	
-struct heap_elem p[0];	
+__bounds_safety::counted_by::limit p;	
 }

```
#### _mbuf

```diff

 struct _mbuf {
 struct _mbuf* _m_next;	
 void* _m_pad;	
-__firebloom::sized_by::_m_len _m_data;	
+__bounds_safety::sized_by::_m_len _m_data;	
 int32_t _m_len;	
 }

```
#### __bounds_safety::wide_ptr.indexable.56

```c
struct __bounds_safety::wide_ptr.indexable.56 {
  uint8_t *ptr;
  uint8_t *ub;
}

```
#### kev_in_collision

```diff

 struct net_event_data link_data;	
 struct in_addr ia_ipaddr;	
 u_char hw_len;	
-u_char hw_addr[-1];	
+__bounds_safety::counted_by::hw_len hw_addr;	
 }

```
#### __bounds_safety::wide_ptr.indexable.67

```c
struct __bounds_safety::wide_ptr.indexable.67 {
  char *ptr;
  char *ub;
}

```
#### __bounds_safety::wide_ptr.indexable.77

```c
struct __bounds_safety::wide_ptr.indexable.77 {
  void *ptr;
  void *ub;
}

```
#### __bounds_safety::wide_ptr.indexable.114

```c
struct __bounds_safety::wide_ptr.indexable.114 {
  char *ptr;
  char *ub;
}

```
#### __bounds_safety::wide_ptr.indexable.111

```c
struct __bounds_safety::wide_ptr.indexable.111 {
  void *ptr;
  void *ub;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.164

```c
struct __bounds_safety::wide_ptr.bidi_indexable.164 {
  struct fileglob *ptr;
  struct fileglob *ub;
  struct fileglob *lb;
}

```
#### dn_heap_entry

```diff

 struct dn_heap_entry {
 dn_key key;	
+size_t obj_size;	
 void* object;	
 }

```
#### secasvar

```diff

 u_int32_t spi;	
 u_int32_t flags;	
 u_int16_t flags2;	
-__firebloom::sized_by::key_auth_len key_auth;	
-__firebloom::sized_by::key_enc_len key_enc;	
-__firebloom::sized_by::ivlen iv;	
-__firebloom::sized_by::schedlen_auth sched_auth;	
-__firebloom::sized_by::schedlen_enc sched_enc;	
+__bounds_safety::sized_by::key_auth_len key_auth;	
+__bounds_safety::sized_by::key_enc_len key_enc;	
+__bounds_safety::sized_by::ivlen iv;	
+__bounds_safety::sized_by::schedlen_auth sched_auth;	
+__bounds_safety::sized_by::schedlen_enc sched_enc;	
 uint32_t key_auth_len;	
 uint32_t key_enc_len;	
 size_t schedlen_auth;	

```
#### secreplay

```diff

 u_int32_t count;	
 u_int32_t seq;	
 u_int32_t lastseq;	
-__firebloom::sized_by::wsize bitmap;	
+__bounds_safety::sized_by::wsize bitmap;	
 int overflow;	
 }

```
#### __bounds_safety::wide_ptr.indexable.44

```c
struct __bounds_safety::wide_ptr.indexable.44 {
  uint8_t *ptr;
  uint8_t *ub;
}

```
#### __bounds_safety::wide_ptr.indexable.88

```c
struct __bounds_safety::wide_ptr.indexable.88 {
  struct ip *ptr;
  struct ip *ub;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.121

```c
struct __bounds_safety::wide_ptr.bidi_indexable.121 {
  struct ip_moptions_dbg *ptr;
  struct ip_moptions_dbg *ub;
  struct ip_moptions_dbg *lb;
}

```
#### mptses

```diff

 uint8_t mpte_addrid_last;	
 uint32_t mpte_itfinfo_size;	
 struct mpt_itf_info _mpte_itfinfo[4];	
-struct mpt_itf_info* mpte_itfinfo;	
+__bounds_safety::counted_by::mpte_itfinfo_size mpte_itfinfo;	
 struct mbuf* mpte_reinjectq;	
 uint32_t mpte_subflow_switches;	
 uint32_t mpte_used_cell;	

```
#### __bounds_safety::wide_ptr.indexable.112

```c
struct __bounds_safety::wide_ptr.indexable.112 {
  char *ptr;
  char *ub;
}

```
#### tcpopt

```diff

 uint16_t to_mss;	
 uint8_t to_requested_s_scale;	
 uint8_t to_nsacks;	
-u_char* to_sacks;	
-u_char* to_tfo;	
+__bounds_safety::sized_by::to_sacks_size to_sacks;	
+uint32_t to_sacks_size;	
+__bounds_safety::sized_by::to_tfo_size to_tfo;	
+uint32_t to_tfo_size;	
 uint8_t to_num_accecn;	
-uint8_t* to_accecn;	
+__bounds_safety::sized_by::to_accecn_size to_accecn;	
+uint32_t to_accecn_size;	
 uint8_t to_accecn_order;	
 }

```
#### tcp_respond_args

```diff

 unsigned int keep_alive;	
 unsigned int noconstrained;	
 unsigned int management_allowed;	
+unsigned int ultra_constrained_allowed;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.150

```c
struct __bounds_safety::wide_ptr.bidi_indexable.150 {
  struct m_tag *ptr;
  struct m_tag *ub;
  struct m_tag *lb;
}

```
#### __bounds_safety::wide_ptr.indexable.116

```c
struct __bounds_safety::wide_ptr.indexable.116 {
  void *ptr;
  void *ub;
}

```
#### __bounds_safety::wide_ptr.indexable.87

```c
struct __bounds_safety::wide_ptr.indexable.87 {
  char *ptr;
  char *ub;
}

```
#### flow_divert_pcb

```diff

 }
  tmp_list_entry;	
 struct mbuf* connect_packet;	
-__firebloom::counted_by::app_data_length app_data;	
+__bounds_safety::counted_by::app_data_length app_data;	
 size_t app_data_length;	
 union sockaddr_in_4_6 local_endpoint;	
 struct sockaddr* original_remote_endpoint;	

```
#### flow_divert_group

```diff

 uint32_t ctl_unit;	
 uint8_t atomic_bits;	
 struct send_queue_head send_queue;	
-__firebloom::counted_by::token_key_size token_key;	
+__bounds_safety::counted_by::token_key_size token_key;	
 size_t token_key_size;	
 uint32_t flags;	
 struct flow_divert_trie signing_id_trie;	

```
#### flow_divert_trie

```diff

 struct flow_divert_trie {
-__firebloom::counted_by::nodes_count nodes;	
-__firebloom::sized_by::child_maps_size child_maps;	
-__firebloom::counted_by::bytes_count bytes;	
-__firebloom::sized_by::memory_size memory;	
+__bounds_safety::counted_by::nodes_count nodes;	
+__bounds_safety::sized_by::child_maps_size child_maps;	
+__bounds_safety::counted_by::bytes_count bytes;	
+__bounds_safety::sized_by::memory_size memory;	
 uint16_t nodes_count;	
 uint16_t child_maps_count;	
 uint16_t bytes_count;	

```
#### tcp_cc_algo

```diff

 struct tcp_cc_algo {
 char name[16];	
-uint32_t num_sockets;	
+atomic uint32_t num_sockets;	
 uint32_t flags;	
  int (struct tcpcb*);* init;	
  int (struct tcpcb*);* cleanup;	

```
#### tcp_rcv_cc_algo

```diff

 struct tcp_rcv_cc_algo {
 char name[16];	
-uint32_t num_sockets;	
+atomic uint32_t num_sockets;	
 uint32_t flags;	
  void (struct tcpcb*);* init;	
  void (struct tcpcb*);* cleanup;	

```
#### __bounds_safety::wide_ptr.indexable.134

```c
struct __bounds_safety::wide_ptr.indexable.134 {
  struct flow_divert_group **ptr;
  struct flow_divert_group **ub;
}

```
#### __bounds_safety::wide_ptr.indexable.101

```c
struct __bounds_safety::wide_ptr.indexable.101 {
  char *ptr;
  char *ub;
}

```
#### uuid_search_info

```diff

 struct uuid_search_info {
 uuid_t target_uuid;	
-char* found_signing_id;	
+__bounds_safety::sized_by::found_signing_id_size found_signing_id;	
 boolean_t found_multiple_signing_ids;	
-proc_t found_proc;	
+struct proc* found_proc;	
 size_t found_signing_id_size;	
 }

```
#### __bounds_safety::wide_ptr.indexable.96

```c
struct __bounds_safety::wide_ptr.indexable.96 {
  void *ptr;
  void *ub;
}

```
#### __bounds_safety::wide_ptr.indexable.104

```c
struct __bounds_safety::wide_ptr.indexable.104 {
  void *ptr;
  void *ub;
}

```
#### __bounds_safety::wide_ptr.indexable.103

```c
struct __bounds_safety::wide_ptr.indexable.103 {
  struct icmp6_nodeinfo *ptr;
  struct icmp6_nodeinfo *ub;
}

```
#### __bounds_safety::wide_ptr.indexable.31

```c
struct __bounds_safety::wide_ptr.indexable.31 {
  char *ptr;
  char *ub;
}

```
#### __bounds_safety::wide_ptr.indexable.25

```c
struct __bounds_safety::wide_ptr.indexable.25 {
  char *ptr;
  char *ub;
}

```
#### __bounds_safety::wide_ptr.indexable.59

```c
struct __bounds_safety::wide_ptr.indexable.59 {
  void *ptr;
  void *ub;
}

```
#### __bounds_safety::wide_ptr.indexable.144

```c
struct __bounds_safety::wide_ptr.indexable.144 {
  void *ptr;
  void *ub;
}

```
#### __bounds_safety::wide_ptr.indexable.84

```c
struct __bounds_safety::wide_ptr.indexable.84 {
  void *ptr;
  void *ub;
}

```
#### __bounds_safety::wide_ptr.indexable.76

```c
struct __bounds_safety::wide_ptr.indexable.76 {
  const bitmap_t *ptr;
  const bitmap_t *ub;
}

```
#### __bounds_safety::wide_ptr.indexable.39

```c
struct __bounds_safety::wide_ptr.indexable.39 {
  char *ptr;
  char *ub;
}

```
#### __bounds_safety::wide_ptr.indexable.63

```c
struct __bounds_safety::wide_ptr.indexable.63 {
  void *ptr;
  void *ub;
}

```
#### __bounds_safety::wide_ptr.indexable.40

```c
struct __bounds_safety::wide_ptr.indexable.40 {
  char *ptr;
  char *ub;
}

```
#### __bounds_safety::wide_ptr.indexable.53

```c
struct __bounds_safety::wide_ptr.indexable.53 {
  uint8_t *ptr;
  uint8_t *ub;
}

```
#### __bounds_safety::wide_ptr.indexable.95

```c
struct __bounds_safety::wide_ptr.indexable.95 {
  void *ptr;
  void *ub;
}

```
#### __bounds_safety::wide_ptr.indexable.34

```c
struct __bounds_safety::wide_ptr.indexable.34 {
  char *ptr;
  char *ub;
}

```
#### sadb_ext_entry

```diff

 struct sadb_ext_entry {
 int ext_len;	
 uint16_t ext_type;	
-__firebloom::sized_by::ext_len ext_buf;	
+__bounds_safety::sized_by::ext_len ext_buf;	
 }

```
#### __bounds_safety::wide_ptr.indexable.163

```c
struct __bounds_safety::wide_ptr.indexable.163 {
  void *ptr;
  void *ub;
}

```
#### __bounds_safety::wide_ptr.indexable.75

```c
struct __bounds_safety::wide_ptr.indexable.75 {
  uint8_t *ptr;
  uint8_t *ub;
}

```
#### _posix_spawnattr

```diff

 int psa_dataless_iopolicy;	
 uint64_t psa_crash_behavior_deadline;	
 uint8_t psa_launch_type;	
+uint16_t psa_sec_flags;	
 uint32_t psa_crash_count;	
 uint32_t psa_throttle_timeout;	
 uint32_t psa_kqworkloop_soft_limit;	

```
#### proc_uniqidentifierinfo

```diff

 uint64_t p_uniqueid;	
 uint64_t p_puniqueid;	
 int32_t p_idversion;	
-uint32_t p_reserve2;	
+int32_t p_orig_ppidversion;	
+uint64_t p_reserve2;	
 uint64_t p_reserve3;	
-uint64_t p_reserve4;	
 }

```
#### experiment_spec

```diff

 uint64_t min_value;	
 uint64_t max_value;	
 uint64_t original_value;	
-_Bool modified;	
+atomic _Bool modified;	
 }

```
#### jetsam_snapshot_entry

```diff

 pid_t pid;	
 char name[33];	
 int32_t priority;	
-uint32_t state;	
+memorystatus_proc_state_t state;	
 uint32_t fds;	
 memorystatus_freeze_skip_reason_t jse_freeze_skip_reason;	
 uint8_t uuid[16];	

```
#### memstat_sort_info

```c
struct memstat_sort_info {
  coalition_t msi_coal;
  uint64_t    msi_page_count;
  pid_t       msi_pid;
  int         msi_ntasks;
}

```
#### memorystatus_priority_entry_v2

```c
struct memorystatus_priority_entry_v2 {
  pid_t                     pid;
  int32_t                   priority;
  uint64_t                  user_data;
  int32_t                   limit;
  memorystatus_proc_state_t state;
  uint64_t                  priority_start_mtime;
  uint8_t                   _reserved[96];
}

```
#### memorystatus_properties_entry_v1

```diff

 int use_probability;	
 uint64_t user_data;	
 int32_t limit;	
-uint32_t state;	
+memorystatus_proc_state_t state;	
 char proc_name[17];	
 char __pad1[3];	
 }

```
#### firehose_tracepoint_s

```diff

 }
  ;	
 uint64_t ft_stamp_and_length;	
-volatile uint64_t ft_atomic_stamp_and_length;	
+volatile atomic uint64_t ft_atomic_stamp_and_length;	
 }
  ;	
 uint8_t ft_data[0];	

```
#### oslog_coproc_args

```c
struct oslog_coproc_args {
  char        buff_l_[0];
  user_addr_t buff;
  char        buff_r_[0];
  char        buff_len_l_[0];
  uint64_t    buff_len;
  char        buff_len_r_[0];
  char        type_l_[0];
  uint32_t    type;
  char        type_r_[4];
  char        uuid_l_[0];
  user_addr_t uuid;
  char        uuid_r_[0];
  char        timestamp_l_[0];
  uint64_t    timestamp;
  char        timestamp_r_[0];
  char        offset_l_[0];
  uint32_t    offset;
  char        offset_r_[4];
  char        stream_log_l_[0];
  uint32_t    stream_log;
  char        stream_log_r_[4];
}

```
#### oslog_coproc_reg_args

```c
struct oslog_coproc_reg_args {
  char        uuid_l_[0];
  user_addr_t uuid;
  char        uuid_r_[0];
  char        file_path_l_[0];
  user_addr_t file_path;
  char        file_path_r_[0];
  char        file_path_len_l_[0];
  user_size_t file_path_len;
  char        file_path_len_r_[0];
}

```
#### mb_stat

```diff

 struct mb_stat {
 u_int32_t mbs_cnt;	
 u_int32_t mbs_pad;	
-mb_class_stat_t mbs_class[1];	
+mb_class_stat_t mbs_class[8];	
 }

```
#### omb_stat

```diff

 struct omb_stat {
 u_int32_t mbs_cnt;	
 u_int32_t mbs_pad;	
-struct omb_class_stat mbs_class[1];	
+struct omb_class_stat mbs_class[8];	
 }

```
#### __bounds_safety::wide_ptr.indexable.129

```c
struct __bounds_safety::wide_ptr.indexable.129 {
  void *ptr;
  void *ub;
}

```
#### __bounds_safety::wide_ptr.indexable.125

```c
struct __bounds_safety::wide_ptr.indexable.125 {
  uint8_t *ptr;
  uint8_t *ub;
}

```
#### __bounds_safety::wide_ptr.indexable.79

```c
struct __bounds_safety::wide_ptr.indexable.79 {
  void *ptr;
  void *ub;
}

```
#### __bounds_safety::wide_ptr.indexable.119

```c
struct __bounds_safety::wide_ptr.indexable.119 {
  struct fileglob **ptr;
  struct fileglob **ub;
}

```
#### sflt_filter

```diff

  errno_t (void*, struct socket*, struct sockopt*);* sf_setoption;	
  errno_t (void*, struct socket*, struct sockopt*);* sf_getoption;	
  errno_t (void*, struct socket*);* sf_listen;	
- errno_t (void*, struct socket*, unsigned long, __firebloom::sized_by::(((request) >> 16) & 8191));* sf_ioctl;	
+ errno_t (void*, struct socket*, unsigned long, __bounds_safety::sized_by::(((request) >> 16) & 8191));* sf_ioctl;	
 struct sflt_filter_ext sf_ext;	
 }

```
#### __bounds_safety::wide_ptr.indexable.52

```c
struct __bounds_safety::wide_ptr.indexable.52 {
  uint8_t *ptr;
  uint8_t *ub;
}

```
#### __bounds_safety::wide_ptr.indexable.58

```c
struct __bounds_safety::wide_ptr.indexable.58 {
  uint8_t *ptr;
  uint8_t *ub;
}

```
#### tracker_db

```diff

 struct tracker_db {
-struct __firebloom::wide_ptr.indexable tracker_hashbase;	
+struct __bounds_safety::wide_ptr.indexable tracker_hashbase;	
 u_long tracker_hashmask;	
 uint32_t tracker_count;	
 uint32_t tracker_count_short;	

```
#### __bounds_safety::wide_ptr.indexable.17

```c
struct __bounds_safety::wide_ptr.indexable.17 {
  u_int8_t *ptr;
  u_int8_t *ub;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.11

```c
struct __bounds_safety::wide_ptr.bidi_indexable.11 {
  struct tracker_db *ptr;
  struct tracker_db *ub;
  struct tracker_db *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.10

```c
struct __bounds_safety::wide_ptr.bidi_indexable.10 {
  struct tracker_hash_entry *ptr;
  struct tracker_hash_entry *ub;
  struct tracker_hash_entry *lb;
}

```
#### mac_policy_ops

```diff

 mpo_proc_notify_service_port_derive_t* mpo_proc_notify_service_port_derive;	
 mpo_proc_check_set_task_exception_port_t* mpo_proc_check_set_task_exception_port;	
 mpo_proc_check_set_thread_exception_port_t* mpo_proc_check_set_thread_exception_port;	
-mpo_proc_check_delegated_signal_t* mpo_proc_check_delegated_signal;	
 mpo_reserved_hook_t* mpo_reserved08;	
 mpo_reserved_hook_t* mpo_reserved09;	
 mpo_reserved_hook_t* mpo_reserved10;	

 mpo_reserved_hook_t* mpo_reserved19;	
 mpo_reserved_hook_t* mpo_reserved20;	
 mpo_reserved_hook_t* mpo_reserved21;	
+mpo_reserved_hook_t* mpo_reserved22;	
 mpo_necp_check_open_t* mpo_necp_check_open;	
 mpo_necp_check_client_action_t* mpo_necp_check_client_action;	
 mpo_file_check_library_validation_t* mpo_file_check_library_validation;	

 mpo_vnode_check_swap_t* mpo_vnode_check_swap;	
 mpo_reserved_hook_t* mpo_reserved33;	
 mpo_reserved_hook_t* mpo_reserved34;	
-mpo_reserved_hook_t* mpo_reserved35;	
+mpo_mount_notify_mount_t* mpo_mount_notify_mount;	
 mpo_vnode_check_copyfile_t* mpo_vnode_check_copyfile;	
 mpo_mount_check_quotactl_t* mpo_mount_check_quotactl;	
 mpo_mount_check_fsctl_t* mpo_mount_check_fsctl;	

```
#### __bounds_safety::wide_ptr.indexable.73

```c
struct __bounds_safety::wide_ptr.indexable.73 {
  void *ptr;
  void *ub;
}

```
#### skmem_arena_nexus

```diff

 struct skmem_cache* arn_ring_cache;	
 struct skmem_cache* arn_txaksd_cache;	
 struct skmem_cache* arn_rxfksd_cache;	
-__firebloom::sized_by::arn_stats_obj_size arn_stats_obj;	
+__bounds_safety::sized_by::arn_stats_obj_size arn_stats_obj;	
 size_t arn_stats_obj_size;	
-__firebloom::counted_by::arn_flowadv_entries arn_flowadv_obj;	
+__bounds_safety::counted_by::arn_flowadv_entries arn_flowadv_obj;	
 size_t arn_flowadv_entries;	
 void* arn_nexusadv_obj;	
 }

```
#### cuckoo_hashtable

```diff

 uint32_t _resize_waiters;	
 lck_rw_t _resize_lock;	
 lck_mtx_t _lock;	
-__firebloom::counted_by::_n_buckets _buckets;	
+__bounds_safety::counted_by::_n_buckets _buckets;	
  int (struct cuckoo_node*, void*);* _obj_cmp;	
  void (struct cuckoo_node*);* _obj_retain;	
  void (struct cuckoo_node*);* _obj_release;	

```
#### __bounds_safety::wide_ptr.indexable.35

```c
struct __bounds_safety::wide_ptr.indexable.35 {
  void *ptr;
  void *ub;
}

```
#### skmem_bufctl_audit

```diff

 struct skmem_bufctl* sle_next;	
 }
  bc_link;	
-__firebloom::sized_by::bc_lim bc_addr;	
+__bounds_safety::sized_by::bc_lim bc_addr;	
 void* bc_addrm;	
 struct skmem_slab* bc_slab;	
 uint32_t bc_lim;	

```
#### __bounds_safety::wide_ptr.indexable.97

```c
struct __bounds_safety::wide_ptr.indexable.97 {
  uint64_t *ptr;
  uint64_t *ub;
}

```
#### __bounds_safety::wide_ptr.indexable.51

```c
struct __bounds_safety::wide_ptr.indexable.51 {
  volatile struct ip6_hdr *ptr;
  volatile struct ip6_hdr *ub;
}

```
#### flow_owner

```diff

 uuid_t fo_key;	
 const struct nexus_adapter* fo_nx_port_na;	
 const struct nx_flowswitch* fo_fsw;	
-__firebloom::counted_by::fo_num_flowadv_bmaps fo_flowadv_bmap;	
+__bounds_safety::counted_by::fo_num_flowadv_bmaps fo_flowadv_bmap;	
 uint32_t fo_flowadv_max;	
 uint32_t fo_num_flowadv;	
 uint32_t fo_num_flowadv_bmaps;	

```
#### sk_stats_flow_adv

```diff

 char sfa_if_name[16];	
 pid_t sfa_owner_pid;	
 uint32_t sfa_entries_count;	
-struct sk_stats_flow_adv_ent sfa_entries[0];	
+__bounds_safety::counted_by::sfa_entries_count sfa_entries;	
 }

```
#### __bounds_safety::wide_ptr.indexable.89

```c
struct __bounds_safety::wide_ptr.indexable.89 {
  void *ptr;
  void *ub;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.156

```c
struct __bounds_safety::wide_ptr.bidi_indexable.156 {
  struct __kern_slot_desc *ptr;
  struct __kern_slot_desc *ub;
  struct __kern_slot_desc *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.165

```c
struct __bounds_safety::wide_ptr.bidi_indexable.165 {
  struct flow_mgr *ptr;
  struct flow_mgr *ub;
  struct flow_mgr *lb;
}

```
#### __bounds_safety::wide_ptr.indexable.69

```c
struct __bounds_safety::wide_ptr.indexable.69 {
  char *ptr;
  char *ub;
}

```
#### __bounds_safety::wide_ptr.indexable.68

```c
struct __bounds_safety::wide_ptr.indexable.68 {
  void *ptr;
  void *ub;
}

```
#### __bounds_safety::wide_ptr.indexable.19

```c
struct __bounds_safety::wide_ptr.indexable.19 {
  volatile struct ip6_hdr *ptr;
  volatile struct ip6_hdr *ub;
}

```
#### __bounds_safety::wide_ptr.indexable.105

```c
struct __bounds_safety::wide_ptr.indexable.105 {
  void *ptr;
  void *ub;
}

```
#### flow_agg

```diff

 struct __kern_packet* _fa_spkt;	
 }
  ;	
-struct __firebloom::wide_ptr.indexable _fa_sptr;	
+struct __bounds_safety::wide_ptr.indexable _fa_sptr;	
 _Bool _fa_sobj_is_pkt;	
 _Bool _fa_sobj_is_short;	
 uint32_t _fa_tcp_seq;	

```
#### __bounds_safety::wide_ptr.indexable.81

```c
struct __bounds_safety::wide_ptr.indexable.81 {
  void *ptr;
  void *ub;
}

```
#### nx_llink_info_req

```diff

 struct nx_llink_info_req {
 uint16_t nlir_version;	
 uint16_t nlir_llink_cnt;	
-struct nx_llink_info nlir_llink[0];	
+__bounds_safety::counted_by::nlir_llink_cnt nlir_llink;	
 }

```
#### __bounds_safety::wide_ptr.indexable.193

```c
struct __bounds_safety::wide_ptr.indexable.193 {
  struct __kern_channel_ring *ptr;
  struct __kern_channel_ring *ub;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.184

```c
struct __bounds_safety::wide_ptr.bidi_indexable.184 {
  struct __kern_netif_intf_advisory *ptr;
  struct __kern_netif_intf_advisory *ub;
  struct __kern_netif_intf_advisory *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.173

```c
struct __bounds_safety::wide_ptr.bidi_indexable.173 {
  struct kern_nexus_provider *ptr;
  struct kern_nexus_provider *ub;
  struct kern_nexus_provider *lb;
}

```
#### __bounds_safety::wide_ptr.indexable.113

```c
struct __bounds_safety::wide_ptr.indexable.113 {
  void *ptr;
  void *ub;
}

```
#### netif_gso_ip_tcp_state

```diff

 struct netif_gso_ip_tcp_state {
- void (struct netif_gso_ip_tcp_state*, struct __kern_packet*, struct __firebloom::wide_ptr.bidi_indexable.33);* update;	
+ void (struct netif_gso_ip_tcp_state*, struct __kern_packet*, struct __bounds_safety::wide_ptr.bidi_indexable.32);* update;	
  void (struct netif_gso_ip_tcp_state*, uint32_t, uint16_t, uint32_t*);* internal;	
 union {
 struct ip* ip;	

```
#### __bounds_safety::wide_ptr.indexable.65

```c
struct __bounds_safety::wide_ptr.indexable.65 {
  void *ptr;
  void *ub;
}

```
#### log_queue_entry

```diff

  lqe_link;	
 uint16_t lqe_size;	
 uint16_t lqe_lm_id;	
-log_queue_entry_state_t lqe_state;	
+atomic log_queue_entry_state_t lqe_state;	
 log_payload_s lqe_payload;	
 }

```
