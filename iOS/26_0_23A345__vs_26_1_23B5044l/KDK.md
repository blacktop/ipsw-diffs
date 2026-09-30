## KDKs

- `KDK_26.0_25A353.kdk/System/Library/Kernels/kernel.release.t6031`
- `KDK_26.1_25B5042k.kdk/System/Library/Kernels/kernel.release.t6031`

#### trap_debounce_buffer

```c
struct trap_debounce_buffer {
  match_record_s records[2];
  size_t         tail;
}

```
#### ipc_service_port_label

```diff

 struct ipc_conn_port_label* __ptrauth(DA, true, 0xa6b2) ispl_sblabel;	
 mach_port_context_t ispl_launchd_context;	
 mach_port_name_t ispl_launchd_name;	
-uint8_t ispl_bootstrap_port;	
 uint8_t ispl_throttled;	
 uint8_t __ispl_unused;	
 uint8_t ispl_domain;	

```
#### coal_sort_s

```c
struct coal_sort_s {
  int      pid;
  int      usr_order;
  uint64_t bytes;
}

```
#### vnode

```diff

 int32_t v_usecount;	
 int32_t v_iocount;	
 void* __ptrauth(DA, true, 0x15d) v_owner;	
-uint8_t v_ext_flag;	
+_Atomic uint8_t v_ext_flag;	
 uint8_t v_type;	
 uint16_t v_tag;	
 uint32_t v_id;	

```
#### ipc_port

```diff

 waitq_flags_t ip_kernel_qos_override;	
 waitq_flags_t ip_srp_lost_link;	
 waitq_flags_t ip_srp_msg_sent;	
-waitq_flags_t ip_bootstrap;	
 waitq_flags_t __ip_unused;	
 }
  ;	

```
#### _TrustCacheInterface

```diff

 queryGetHashType_t queryGetHashType;	
 queryGetFlags_t queryGetFlags;	
 queryGetConstraintCategory_t queryGetConstraintCategory;	
+queryGetUUID_t queryGetUUID;	
 constructInvalid_t constructInvalid;	
 checkRuntimeForUUID_t checkRuntimeForUUID;	
 extractModule_t extractModule;	

```
#### _TrustCacheMutableRuntime

```diff

 struct _TrustCacheMutableRuntime {
 _Atomic TrustCache_t* loadableTCHead;	
+_Atomic TrustCache_t* mobileAssetTCHead;	
 }

```
