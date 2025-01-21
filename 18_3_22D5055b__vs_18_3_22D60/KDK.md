## KDKs

- `KDK_15.3_24D5040f.kdk/System/Library/Kernels/kernel.release.t6041`
- `KDK_15.3_24D60.kdk/System/Library/Kernels/kernel.release.t6041`

#### m_hdr_common

```diff

 struct m_hdr_common {
 struct m_hdr M_hdr;	
 struct m_ext M_ext;	
+uint64_t m_hdr_crumbs;	
 struct pkthdr M_pkthdr;	
 }

```
#### soflow_hash_entry

```diff

 uint64_t soflow_txbytes;	
 uint64_t soflow_feat_ctxt_id;	
 void* soflow_feat_ctxt;	
+uint32_t soflow_filter_control_unit;	
+int32_t soflow_policies_gencount;	
+struct timeval soflow_timestamp;	
 }

```
#### necp_socket_info

```diff

 u_int32_t client_flags;	
 char* domain;	
 char* url;	
+struct soflow_hash_entry* soflow_entry;	
 unsigned int is_entitled;	
 unsigned int has_client;	
 unsigned int has_system_signed_result;	

```
#### cfil_info

```diff

 int cfi_dir;	
 uint64_t cfi_byte_inbound_count;	
 uint64_t cfi_byte_outbound_count;	
+struct timeval cfi_timestamp;	
 boolean_t cfi_isSignatureLatest;	
 u_int32_t cfi_filter_control_unit;	
 u_int32_t cfi_filter_policy_gencount;	

```
