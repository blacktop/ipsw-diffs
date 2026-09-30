## KDKs

- `KDK_15.0_24A5298h.kdk/System/Library/Kernels/kernel.release.t6031`
- `KDK_15.0_24A5309e.kdk/System/Library/Kernels/kernel.release.t6031`

#### lck_ticket_s

```c
struct lck_ticket_s {
  uint32_t        __lck_ticket_unused;
  uint32_t        lck_ticket_type;
  uint32_t        lck_ticket_padding;
  hw_lck_ticket_t tu;
  uint32_t        lck_ticket_owner;
}

```
#### lck_spin_s

```c
struct lck_spin_s {
  struct hslock hwlock;
  unsigned long type;
}

```
#### lck_mtx_s

```c
struct lck_mtx_s {
  uint32_t        lck_mtx_tsid;
  uint8_t         lck_mtx_type;
  uint32_t        lck_mtx_grp;
  lck_mtx_state_t lck_mtx;
}

```
#### lck_rw_s

```c
struct lck_rw_s {
  uint32_t      lck_rw_unused;
  uint32_t      lck_rw_type;
  uint32_t      lck_rw_padding;
  lck_rw_word_t lck_rw;
  uint32_t      lck_rw_owner;
}

```
#### vm_object

```diff

 unsigned int reusable_page_count;	
 struct vm_object* vo_copy;	
 uint32_t vo_copy_version;	
+uint32_t vo_inherit_copy_none;	
 uint32_t __vo_unused_padding;	
 struct vm_object* shadow;	
 memory_object_t pager;	

 vm_object_offset_t paging_offset;	
 memory_object_control_t pager_control;	
 memory_object_copy_strategy_t copy_strategy;	
-unsigned short paging_in_progress;	
-unsigned short vo_size_delta;	
-unsigned int activity_in_progress;	
+uint16_t paging_in_progress;	
+uint16_t vo_size_delta;	
+uint32_t activity_in_progress;	
 unsigned int all_wanted;	
 unsigned int pager_created;	
 unsigned int pager_initialized;	

```
#### ledger_entry_info

```diff

 uint64_t lei_limit;	
 uint64_t lei_refill_period;	
 uint64_t lei_last_refill;	
+int64_t lei_lifetime_max;	
 }

```
#### lck_mtx_mcs

```diff

 struct lck_mtx_mcs {
-struct _lck_mtx_* lmm_ilk_current;	
+struct lck_mtx_s* lmm_ilk_current;	
 struct lck_mtx_mcs* lmm_ilk_next;	
 unsigned long lmm_ilk_ready;	
 struct lck_mtx_mcs* lmm_as_next;	

```
#### _cs_profile

```diff

 uuid_t profile_uuid;	
 void* profile_obj;	
 _Bool skip_collector;	
+_Bool trusted;	
 struct {
 struct _cs_profile* sle_next;	
 }

```
