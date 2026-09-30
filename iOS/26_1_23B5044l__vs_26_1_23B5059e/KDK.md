## KDKs

- `KDK_26.1_25B5042k.kdk/System/Library/Kernels/kernel.release.t6031`
- `KDK_26.1_25B5057f.kdk/System/Library/Kernels/kernel.release.t6031`

#### jetsam_state_s

```diff

 _Bool errors_cleared;	
 _Bool sort_flag;	
 _Bool corpse_list_purged;	
+_Bool bg_approached;	
+_Bool fg_approached;	
 _Bool post_snapshot;	
 uint64_t memory_reclaimed;	
 uint32_t hwm_kills;	

```
#### vm_major_compact_stats_s

```c
struct vm_major_compact_stats_s {
  uint64_t asked_permission;
  uint64_t compactions;
  uint64_t moved_slots;
  uint64_t moved_bytes;
  uint64_t wasted_space_in_swapouts;
  uint64_t count_of_swapouts;
  uint64_t count_of_freed_segs;
  uint64_t bailed_compactions;
  uint64_t bytes_freed;
  uint64_t runtime_us;
}

```
#### vm_pageout_vminfo

```diff

 unsigned long vm_pageout_forcereclaimed_sharedcache;	
 unsigned long vm_pageout_protected_realtime;	
 unsigned long vm_pageout_forcereclaimed_realtime;	
+uint64_t vm_compactor_major_compactions_completed;	
+uint64_t vm_compactor_major_compactions_considered;	
+uint64_t vm_compactor_major_compactions_bailed;	
+uint64_t vm_compactor_major_compaction_bytes_freed;	
+uint64_t vm_compactor_major_compaction_bytes_moved;	
+uint64_t vm_compactor_major_compaction_slots_moved;	
+uint64_t vm_compactor_major_compaction_segments_freed;	
+uint64_t vm_compactor_swapouts_queued;	
+uint64_t vm_compactor_swapout_bytes_wasted;	
 }

```
#### memory_object

```diff

 os_ref_atomic_t mo_ref;	
 const struct memory_object_pager_ops* mo_pager_ops;	
 memory_object_control_t mo_control;	
+uint32_t mo_last_unmap_ctid;	
 }

```
#### sptm_client_state

```diff

 const void* sptm_pmap_io_ranges;	
 unsigned int sptm_pmap_io_ranges_count;	
 sptm_domain_t* sptm_panicking_domain_id;	
-uint8_t reserved[96];	
+const void* percpu_event_counters;	
+uint8_t reserved[88];	
 }

```
#### vm_pageout_stat

```diff

 unsigned int forcereclaimed_realtime;	
 unsigned int protected_sharedcache;	
 unsigned int protected_realtime;	
+unsigned long cswap_unripe_under_30s;	
+unsigned long cswap_unripe_under_60s;	
+unsigned long cswap_unripe_under_300s;	
+unsigned long cswap_reclaim_swapins;	
+unsigned long cswap_defrag_swapins;	
+unsigned long cswap_swap_threshold_exceeded;	
+unsigned long cswap_external_q_throttled;	
+unsigned long cswap_free_below_reserve;	
+unsigned long cswap_thrashing_detected;	
+unsigned long cswap_fragmentation_detected;	
+unsigned long major_compactions_considered;	
+unsigned long major_compactions_completed;	
+unsigned long major_compactions_bailed;	
+unsigned long major_compaction_bytes_freed;	
+unsigned long major_compaction_bytes_moved;	
+unsigned long major_compaction_slots_moved;	
+unsigned long major_compaction_segments_freed;	
+unsigned long swapouts_queued;	
+unsigned long swapout_bytes_wasted;	
 }

```
