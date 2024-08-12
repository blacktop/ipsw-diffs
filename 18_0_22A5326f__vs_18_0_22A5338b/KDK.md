## KDKs

- `KDK_15.0_24A5309e.kdk/System/Library/Kernels/kernel.release.t6031`
- `KDK_15.0_24A5320a.kdk/System/Library/Kernels/kernel.release.t6031`

#### task

```diff

 boolean_t jitbox_enabled;	
 arm64_uexc_region_t uexc;	
 _Bool preserve_x18;	
+_Bool apt_traceable;	
 _Bool uses_1ghz_timebase;	
 counter_t faults;	
 counter_t pageins;	

```
#### ledger_entry_info

```diff

 uint64_t lei_limit;	
 uint64_t lei_refill_period;	
 uint64_t lei_last_refill;	
-int64_t lei_lifetime_max;	
 }

```
#### task_apt_token

```c
struct task_apt_token {
  ipc_port_t rport;
}

```
#### __firebloom::wide_ptr.bidi_indexable.72

```diff

 struct __firebloom::wide_ptr.bidi_indexable.72 {
-struct in6_aliasreq_64* ptr;	
-struct in6_aliasreq_64* ub;	
-struct in6_aliasreq_64* lb;	
+struct if_cellular_status_v1* ptr;	
+struct if_cellular_status_v1* ub;	
+struct if_cellular_status_v1* lb;	
 }

```
#### necp_session_policy

```diff

 necp_policy_id local_id;	
 necp_policy_order order;	
 u_int32_t result_size;	
-__firebloom::sized_by::result_size result;	
+u_int8_t* result;	
 u_int32_t conditions_size;	
-__firebloom::sized_by::conditions_size conditions;	
+u_int8_t* conditions;	
 u_int32_t route_rules_size;	
-__firebloom::sized_by::route_rules_size route_rules;	
+u_int8_t* route_rules;	
 uuid_t applied_app_uuid;	
 uuid_t applied_real_app_uuid;	
 u_int32_t applied_account_size;	
-__firebloom::sized_by::applied_account_size applied_account;	
+char* applied_account;	
 uuid_t applied_result_uuid;	
 u_int32_t applied_route_rules_id;	
 necp_kernel_policy_id kernel_socket_policies[1];	

```
#### necp_kernel_socket_policy

```diff

 pid_t cond_pid;	
 uid_t cond_uid;	
 uid_t cond_real_uid;	
-struct ifnet* cond_bound_interface;	
+ifnet_t cond_bound_interface;	
 struct necp_policy_condition_tc_range cond_traffic_class;	
 u_int16_t cond_protocol;	
 union necp_sockaddr_union cond_local_start;	

```
#### necp_kernel_ip_output_policy

```diff

 u_int64_t condition_mask;	
 u_int64_t condition_negated_mask;	
 necp_kernel_policy_id cond_policy_id;	
-struct ifnet* cond_bound_interface;	
+ifnet_t cond_bound_interface;	
 u_int16_t cond_protocol;	
 union necp_sockaddr_union cond_local_start;	
 union necp_sockaddr_union cond_local_end;	

```
#### substring

```diff

 struct substring {
 size_t length;	
-__firebloom::sized_by::length string;	
+char* string;	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.162

```diff

 struct __firebloom::wide_ptr.bidi_indexable.162 {
-struct kalloc_heap* ptr;	
-struct kalloc_heap* ub;	
-struct kalloc_heap* lb;	
+struct hook_desc* ptr;	
+struct hook_desc* ub;	
+struct hook_desc* lb;	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.152

```diff

 struct __firebloom::wide_ptr.bidi_indexable.152 {
-struct ip6_hdr* ptr;	
-struct ip6_hdr* ub;	
-struct ip6_hdr* lb;	
+struct pf_rule_addr* ptr;	
+struct pf_rule_addr* ub;	
+struct pf_rule_addr* lb;	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.156

```diff

 struct __firebloom::wide_ptr.bidi_indexable.156 {
-struct sockaddr_in6* ptr;	
-struct sockaddr_in6* ub;	
-struct sockaddr_in6* lb;	
+struct cfe_buf_stat* ptr;	
+struct cfe_buf_stat* ub;	
+struct cfe_buf_stat* lb;	
 }

```
#### __firebloom::wide_ptr.indexable.72

```diff

 struct __firebloom::wide_ptr.indexable.72 {
-void* ptr;	
-void* ub;	
+char* ptr;	
+char* ub;	
 }

```
#### uuid_search_info

```diff

 struct uuid_search_info {
 uuid_t target_uuid;	
-__firebloom::sized_by::found_signing_id_size found_signing_id;	
+char* found_signing_id;	
 boolean_t found_multiple_signing_ids;	
-struct proc* found_proc;	
+proc_t found_proc;	
 size_t found_signing_id_size;	
 }

```
#### __firebloom::wide_ptr.indexable.87

```c
struct __firebloom::wide_ptr.indexable .87 {
  uint8_t *ptr;
  uint8_t *ub;
}

```
#### __firebloom::wide_ptr.indexable.42

```diff

 struct __firebloom::wide_ptr.indexable.42 {
-u_int8_t* ptr;	
-u_int8_t* ub;	
+uint8_t* ptr;	
+uint8_t* ub;	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.158

```diff

 struct __firebloom::wide_ptr.bidi_indexable.158 {
-struct necp_session_policy* ptr;	
-struct necp_session_policy* ub;	
-struct necp_session_policy* lb;	
+struct sadb_alg* ptr;	
+struct sadb_alg* ub;	
+struct sadb_alg* lb;	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.141

```diff

 struct __firebloom::wide_ptr.bidi_indexable.141 {
-struct socket* ptr;	
-struct socket* ub;	
-struct socket* lb;	
+const struct sadb_sa* ptr;	
+const struct sadb_sa* ub;	
+const struct sadb_sa* lb;	
 }

```
#### __firebloom::wide_ptr.indexable.125

```c
struct __firebloom::wide_ptr.indexable .125 {
  uint8_t *ptr;
  uint8_t *ub;
}

```
#### __firebloom::wide_ptr.indexable.51

```c
struct __firebloom::wide_ptr.indexable .51 {
  uint8_t *ptr;
  uint8_t *ub;
}

```
#### __firebloom::wide_ptr.bidi_indexable.154

```diff

 struct __firebloom::wide_ptr.bidi_indexable.154 {
-struct necp_aggregate_route_rule* ptr;	
-struct necp_aggregate_route_rule* ub;	
-struct necp_aggregate_route_rule* lb;	
+struct kalloc_heap* ptr;	
+struct kalloc_heap* ub;	
+struct kalloc_heap* lb;	
 }

```
