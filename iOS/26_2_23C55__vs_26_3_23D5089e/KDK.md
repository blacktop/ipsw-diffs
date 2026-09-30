## KDKs

- `KDK_26.2_25C56.kdk/System/Library/Kernels/kernel.release.t8142`
- `KDK_26.3_25D5087f.kdk/System/Library/Kernels/kernel.release.t8142`

#### pulled_thread_queue

```c
struct pulled_thread_queue {
  circle_queue_head_t ptq_threadq;
  cpumap_t            ptq_needs_smr_cpu_down;
  _Bool               ptq_queue_active;
}

```
#### trap_debounce_buffer

```c
struct trap_debounce_buffer {
  match_record_s records[2];
  size_t         tail;
}

```
#### sched_edge_steal_silo

```c
struct sched_edge_steal_silo {
  struct priority_queue_sched_max sess_steal_queues[6];
  _Atomic bitmap_t                sess_populated_steal_queues[1];
}

```
#### sched_clutch_root

```diff

 uint32_t scr_cluster_id;	
 processor_set_t scr_pset;	
 queue_head_t scr_clutch_buckets;	
-struct priority_queue_sched_max scr_foreign_buckets;	
+struct sched_edge_steal_silo scr_steal_silos[2];	
+_Atomic bitmap_t scr_populated_steal_silos[1];	
+_Atomic bitmap_t [1] scr_incoming_migration_allowed[6];	
 bitmap_t scr_unbound_runnable_bitmap[1];	
 bitmap_t scr_unbound_warp_available[1];	
 bitmap_t scr_bound_runnable_bitmap[1];	

```
#### sched_clutch_bucket

```diff

 struct sched_clutch_bucket {
-_Bool scb_foreign;	
+pset_id_t scb_preferred_pset_when_enqueued;	
 uint8_t scb_bucket;	
 uint8_t scb_priority;	
 uint16_t scb_thr_count;	

 queue_chain_t scb_listlink;	
 queue_chain_t scb_runqlink;	
 queue_head_t scb_thread_timeshare_queue;	
-struct priority_queue_entry_sched scb_foreignlink;	
+struct priority_queue_entry_sched scb_stealqlink;	
 }

```
#### skmem_sysctl

```diff

 int32_t rst_rlc_verbose;	
 int32_t use_rto_deadline;	
 int32_t rto_deadline_sojourn_factor;	
+int32_t allow_syn_prio;	
 }
  tcp;	
 struct {

```
#### processor

```diff

 processor_reason_t last_shutdown_reason;	
 processor_reason_t last_recommend_reason;	
 processor_reason_t last_derecommend_reason;	
+struct pulled_thread_queue processor_threadq;	
+struct pulled_thread_queue processor_threadq_interrupt;	
 _Bool processor_instartup;	
 _Bool processor_booted;	
 _Bool shutdown_temporary;	

```
