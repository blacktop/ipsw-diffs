## KDKs

- `KDK_26.4_25E246.kdk/System/Library/Kernels/kernel.release.t8142`
- `KDK_26.5_25F5042g.kdk/System/Library/Kernels/kernel.release.t8142`

#### vm_pageout_stat

```diff

 unsigned int vm_fault_copy_busy_trylock_count;	
 unsigned int vm_fault_copy_busy_retry_count;	
 unsigned int tagged_pages_grabbed;	
+unsigned int kernel_tagged_pages_grabbed;	
 unsigned int tagged_pages_grabbed_for_untagged;	
 unsigned int inline_ts_activated;	
+unsigned int inline_kts_activated;	
 unsigned int refill_ts_considered;	
 unsigned int refill_ts_activated;	
+unsigned int refill_kts_activated;	
 unsigned int refill_ts_deactivated;	
+unsigned int refill_kts_deactivated;	
 }

```
#### vm_statistics64

```diff

 natural_t internal_page_count;	
 uint64_t total_uncompressed_pages_in_compressor;	
 uint64_t swapped_count;	
+uint64_t total_tag_storage_pages;	
+uint64_t nontag_pageable_tag_storage_pages;	
+uint64_t nontag_wired_tag_storage_pages;	
+uint64_t free_tag_storage_pages;	
+uint64_t tag_storing_tag_storage_pages;	
+uint64_t total_tagged_pages;	
+uint64_t resident_tagged_pages;	
+uint64_t compressed_tagged_pages;	
+uint64_t tagged_compressions;	
+uint64_t tagged_decompressions;	
+uint64_t compressed_tag_storage_bytes;	
 }

```
#### open_vnode

```diff

 }
  chain;	
 vnode_t vp;	
+uint8_t vp_type;	
 dev_t dev;	
 uint64_t file_id;	
 uint32_t fstag;	

```
#### task_token_data

```c
struct task_token_data {
  _Atomic uint64_t tc_uids;
  _Atomic uint64_t tc_gids;
  _Atomic uint32_t tc_auid;
  _Atomic uint32_t tc_asid;
  _Atomic uint32_t tc_pid;
  _Atomic uint32_t tc_pidversion;
}

```
#### task

```diff

 struct ipc_port* __ptrauth(DA, true, 0xa454) itk_registered[3];	
 ipc_port_t* __ptrauth(DA, true, 0xec7b) itk_dyld_notify;	
 struct ipc_space* __ptrauth(DA, true, 0x8280) itk_space;	
+struct task_token_data* __ptrauth(DA, true, 0xb91f) task_tokens;	
 ledger_t ledger;	
 queue_head_t semaphore_list;	
 int semaphores_owned;	

```
#### proc_ro

```diff

  ;	
 union {
 struct {
-struct task_token_ro_data task_tokens;	
 struct task_filter_ro_data task_filters;	
 uint32_t t_flags_ro;	
 task_control_port_options_t task_control_port_options;	

```
#### task_ro_data

```diff

 struct task_ro_data {
-struct task_token_ro_data task_tokens;	
 struct task_filter_ro_data task_filters;	
 uint32_t t_flags_ro;	
 task_control_port_options_t task_control_port_options;	

```
#### proc

```diff

 void* p_pthhash;	
 volatile uint64_t was_throttled;	
 volatile uint64_t did_throttle;	
+char* p_execpath;	
 uint64_t p_dispatchqueue_offset;	
 uint64_t p_dispatchqueue_serialno_offset;	
 uint64_t p_dispatchqueue_label_offset;	

```
#### trap_debounce_buffer

```c
struct trap_debounce_buffer {
  match_record_s records[2];
  size_t         tail;
}

```
#### vm_page_pcpu

```diff

 uint32_t deactivate_suspend;	
 vm_page_t free_tagged_zero_page;	
 vm_page_t free_tagged_pages;	
+vm_page_t free_kernel_tagged_pages;	
 vm_page_t free_zero_page;	
 vm_page_t free_pages;	
 unsigned int start_color;	

```
