## KDKs

- `KDK_26.3_25D5087f.kdk/System/Library/Kernels/kernel.release.t8142`
- `KDK_26.3.1_25D2128.kdk/System/Library/Kernels/kernel.release.t8142`

#### necp_client

```diff

 u_int8_t result[1024];	
 necp_policy_id policy_id;	
 necp_policy_id skip_policy_id;	
+necp_kernel_policy_result policy_result;	
+necp_kernel_policy_routing_result_parameter policy_result_parameter;	
+u_int32_t flow_divert_control_unit;	
+u_int32_t filter_control_unit;	
 u_int8_t ip_protocol;	
 int proc_pid;	
 u_int64_t delegated_upid;	

```
#### __bounds_safety::wide_ptr.bidi_indexable.17

```c
struct __bounds_safety::wide_ptr.bidi_indexable.17 {
  const void *ptr;
  const void *ub;
  const void *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.97

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.97 {
-const struct __kern_buflet* ptr;	
-const struct __kern_buflet* ub;	
-const struct __kern_buflet* lb;	
+struct __flow* ptr;	
+struct __flow* ub;	
+struct __flow* lb;	
 }

```
#### ml_topology_info

```diff

 ml_topology_cluster_t* boot_cluster;	
 unsigned int chip_revision;	
 unsigned int cluster_types;	
-unsigned int cluster_type_num_cpus[3];	
-unsigned int cluster_type_num_clusters[3];	
+unsigned int cluster_type_num_cpus[4];	
+unsigned int cluster_type_num_clusters[4];	
 unsigned int cluster_power_down;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.98

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.98 {
-struct __flow* ptr;	
-struct __flow* ub;	
-struct __flow* lb;	
+struct __kern_buflet* ptr;	
+struct __kern_buflet* ub;	
+struct __kern_buflet* lb;	
 }

```
#### __bounds_safety::wide_ptr.indexable.19

```c
struct __bounds_safety::wide_ptr.indexable.19 {
  uint8_t *ptr;
  uint8_t *ub;
}

```
