## KDKs

- `KDK_26.1_25B5057f.kdk/System/Library/Kernels/kernel.release.t6031`
- `KDK_26.1_25B5062e.kdk/System/Library/Kernels/kernel.release.t6031`

#### __bounds_safety::wide_ptr.bidi_indexable.127

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.127 {
-struct inpcb** ptr;	
-struct inpcb** ub;	
-struct inpcb** lb;	
+struct ipovly* ptr;	
+struct ipovly* ub;	
+struct ipovly* lb;	
 }

```
#### skmem_sysctl

```diff

 int32_t l4s;	
 int32_t link_heuristics_flags;	
 int32_t link_heuristics_rto_min;	
+int32_t rst_rlc_enable;	
+uint32_t rst_rlc_bucket_ms;	
+int32_t rst_rlc_use_ts;	
+int32_t rst_rlc_verbose;	
 }
  tcp;	
 struct {

```
#### _CSConfigOSPolicy

```diff

 CMSPolicyFlags_t profileValidatedCTFlags;	
 CMSPolicyFlags_t appStoreQACTFlags;	
 CMSPolicyFlags_t profileValidatedQACTFlags;	
+CMSPolicyFlags_t platformQACTFlags;	
 CMSPolicyFlags_t profileCTFlags;	
 const char** developerLimit;	
 CSConfigFeatureSet_t featureSet;	

```
#### tcp_stats

```diff

 struct tcp_stats {
-uint64_t _arr[213];	
+uint64_t _arr[215];	
 }

```
#### kmem_page_meta

```diff

  ;	
 uint8_t km_page_marker;	
 uint8_t km_sizeclass;	
+uint8_t km_quarantined;	
+uint8_t km_avail_count;	
 union {
 uint16_t km_chunk_len;	
 uint16_t km_page_idx;	

```
#### necp_flow_defunct

```diff

 uuid_t flow_id;	
 uuid_t nexus_agent;	
 void* agent_handle;	
-void* socket_handle;	
 int proc_pid;	
 u_int32_t flags;	
 struct necp_client_agent_parameters close_parameters;	

```
#### __bounds_safety::wide_ptr.bidi_indexable.213

```c
struct __bounds_safety::wide_ptr.bidi_indexable.213 {
  struct llc *ptr;
  struct llc *ub;
  struct llc *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.166

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.166 {
-struct {
-struct tcp_notify_ack_marker* slh_first;	
-}
-* ptr;	
-struct {
-struct tcp_notify_ack_marker* slh_first;	
-}
-* ub;	
-struct {
-struct tcp_notify_ack_marker* slh_first;	
-}
-* lb;	
+struct tcp_notify_ack_marker* ptr;	
+struct tcp_notify_ack_marker* ub;	
+struct tcp_notify_ack_marker* lb;	
 }

```
#### tcpstat

```diff

 u_int32_t tcps_ka_offload_drops;	
 u_int32_t tcps_mptcp_triggered_cell;	
 u_int32_t tcps_fin_timeout_drops;	
+u_int64_t tcps_rst_dup_suppressed;	
+u_int64_t tcps_rst_not_suppressed;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.184

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.184 {
-struct tsegqe_head* ptr;	
-struct tsegqe_head* ub;	
-struct tsegqe_head* lb;	
+struct pf_anchor* ptr;	
+struct pf_anchor* ub;	
+struct pf_anchor* lb;	
 }

```
#### udpstat

```diff

 u_int32_t udps_snd_swcsum_bytes;	
 u_int32_t udps_snd6_swcsum;	
 u_int32_t udps_snd6_swcsum_bytes;	
+u_int64_t udps_port_unreach_dup_suppressed;	
+u_int64_t udps_port_unreach_not_suppressed;	
 }

```
#### in_endpoints

```c
struct in_endpoints {
  in_port_t           ie_fport;
  in_port_t           ie_lport;
  union in_dependaddr ie_dependfaddr;
  union in_dependaddr ie_dependladdr;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.129

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.129 {
-struct tseg_qent* ptr;	
-struct tseg_qent* ub;	
-struct tseg_qent* lb;	
+struct icmp* ptr;	
+struct icmp* ub;	
+struct icmp* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.185

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.185 {
-struct necp_quic_stats* ptr;	
-struct necp_quic_stats* ub;	
-struct necp_quic_stats* lb;	
+struct tsegqe_head* ptr;	
+struct tsegqe_head* ub;	
+struct tsegqe_head* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.135

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.135 {
-const struct sockaddr_in6* ptr;	
-const struct sockaddr_in6* ub;	
-const struct sockaddr_in6* lb;	
+struct in_ifaddr* ptr;	
+struct in_ifaddr* ub;	
+struct in_ifaddr* lb;	
 }

```
#### __bounds_safety::wide_ptr.indexable.123

```c
struct __bounds_safety::wide_ptr.indexable.123 {
  void *ptr;
  void *ub;
}

```
