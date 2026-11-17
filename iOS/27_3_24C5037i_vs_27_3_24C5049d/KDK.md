## KDKs

- `KDK_27.3_26C5035r.kdk/System/Library/Kernels/kernel.release.t8152`
- `KDK_27.3_26C5047e.kdk/System/Library/Kernels/kernel.release.t8152`

#### vm_pageout_state

```diff

 unsigned int vm_pageout_deadlock_relief;	
 unsigned int vm_pageout_burst_inactive_throttle;	
 unsigned int vm_pageout_inactive;	
-unsigned int vm_pageout_clean_no_shadowing;	
-unsigned int vm_pageout_clean_but_shadowing;	
 uint64_t vm_page_filecache_min;	
 uint32_t vm_page_filecache_min_divisor;	
 uint32_t vm_page_xpmapped_min;	

```
#### _ca_event_vmo_file_snapshot_violation

```c
struct _ca_event_vmo_file_snapshot_violation {
  ca_sstr            proc_name[17];
  unsigned long long snapshot_size;
  unsigned long long fault_offset;
  _Bool              is_write;
  _Bool              is_trusted;
  _Bool              is_resilient_media;
  ca_sstr            backtrace[256];
}

```
#### vm_object

```diff

 struct vm_object {
 vm_page_queue_head_t memq;	
+vm_object_size_t vo_snapshot_file_size;	
 lck_rw_new_t Lock;	
 union {
 vm_object_size_t vou_size;	

```
#### necp_socket_info

```diff

 unsigned int real_is_platform_binary;	
 unsigned int is_delegated;	
 unsigned int is_local;	
+unsigned int signing_id_unavailable;	
 unsigned int __pad_bits;	
 }

```
#### _ca_event_vmo_file_snapshot_violation_stats

```c
struct _ca_event_vmo_file_snapshot_violation_stats {
  unsigned long long violations;
  unsigned long long violations_write;
  unsigned long long violations_untrusted;
  unsigned long long violations_resilient_media;
  unsigned long long events_dropped;
}

```
#### exclaves_ctx

```diff

 struct exclaves_ctx {
-exclaves_scid_t scid;	
-Exclaves_L4_IpcBuffer_t* ipcb;	
+scid_t scid;	
 conclave_id_t home;	
 conclave_id_t active;	
-exclaves_ctx_t next;	
+thread_t home_th;	
+thread_t active_th;	
+Exclaves_L4_IpcBuffer_t* ipcb;	
 uint64_t usecnt;	
 }

```
#### task

```diff

 uint32_t exclave_crash_info_length;	
 uint64_t task_cs_auxiliary_info;	
 task_sanitizer_config_t sanitizer_config;	
+_Atomic _Bool vmo_snapshot_violation_reported;	
 task_security_config_s security_config;	
 }

```
#### vm_object_fault_info

```diff

 unsigned int fi_change_wiring;	
 unsigned int fi_no_sleep;	
 unsigned int fi_pagein_telemetry;	
+unsigned int fi_snapshot_no_enforce;	
 unsigned int __vm_object_fault_info_unused_bits;	
 int pmap_options;	
 }

```
