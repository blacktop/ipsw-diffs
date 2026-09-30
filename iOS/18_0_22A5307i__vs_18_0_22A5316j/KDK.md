## KDKs

- `KDK_15.0_24A5289h.kdk/System/Library/Kernels/kernel.release.t6031`
- `KDK_15.0_24A5298h.kdk/System/Library/Kernels/kernel.release.t6031`

#### stackshot_context

```diff

 struct stackshot_buffer sc_buffers[6];	
 size_t sc_num_buffers;	
 struct stackshot_workqueue sc_workqueues[2];	
+struct port_label_hash sc_plh;	
 struct stackshot_duration_v2 sc_duration;	
 uint32_t sc_bytes_traced;	
 uint32_t sc_bytes_uncompressed;	

```
#### port_label_hash

```diff

 struct port_label_hash {
+int plh_lock;	
 uint16_t plh_size;	
 uint16_t plh_count;	
 struct ipc_service_port_label** plh_array;	
 int16_t* plh_chains;	
-uint8_t* plh_gen;	
 int16_t* plh_hash;	
-int16_t plh_curgen_min;	
-int16_t plh_curgen_max;	
-uint8_t plh_curgen;	
 }

```
#### stackshot_cpu_context

```diff

 linked_kcdata_descriptor_t scc_kcdata_tail;	
 uintptr_t* scc_stack_buffer;	
 struct stackshot_fault_stats scc_fault_stats;	
+struct _stackshot_validation_state scc_validation_state;	
+struct _stackshot_plh_gen_state scc_plh_gen;	
 }

```
#### _stackshot_plh_gen_state

```c
struct _stackshot_plh_gen_state {
  uint8_t *pgs_gen;
  int16_t  pgs_curgen_min;
  int16_t  pgs_curgen_max;
  uint8_t  pgs_curgen;
}

```
#### io_reprioritize_req

```diff

 uint32_t len;	
 int priority;	
 struct vnode* devvp;	
-queue_chain_t io_reprioritize_list;	
+struct mpsc_queue_chain iorr_elm;	
 }

```
#### vm_caps

```diff

 hv_caps_t hacr;	
 hv_caps_t mdcr;	
 hv_caps_t ich_hcr;	
-hv_caps_t actlr_el1;	
+hv_caps_t actlr_el1_guest;	
+hv_caps_t actlr_el1_vmm;	
 uint64_t restricted_state_mask;	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.17

```diff

 struct __firebloom::wide_ptr.bidi_indexable.17 {
-struct ether_header* ptr;	
-struct ether_header* ub;	
-struct ether_header* lb;	
+u_int8_t* ptr;	
+u_int8_t* ub;	
+u_int8_t* lb;	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.38

```diff

 struct __firebloom::wide_ptr.bidi_indexable.38 {
-struct sockaddr_dl* ptr;	
-struct sockaddr_dl* ub;	
-struct sockaddr_dl* lb;	
+char* ptr;	
+char* ub;	
+char* lb;	
 }

```
#### __firebloom::wide_ptr.indexable.36

```diff

 struct __firebloom::wide_ptr.indexable.36 {
-void* ptr;	
-void* ub;	
+char* ptr;	
+char* ub;	
 }

```
#### __firebloom::wide_ptr.indexable.46

```diff

 struct __firebloom::wide_ptr.indexable.46 {
-char* ptr;	
-char* ub;	
+uint8_t* ptr;	
+uint8_t* ub;	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.52

```diff

 struct __firebloom::wide_ptr.bidi_indexable.52 {
-struct sockaddr_dl* ptr;	
-struct sockaddr_dl* ub;	
-struct sockaddr_dl* lb;	
+struct ifdevmtu* ptr;	
+struct ifdevmtu* ub;	
+struct ifdevmtu* lb;	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.40

```diff

 struct __firebloom::wide_ptr.bidi_indexable.40 {
-char* ptr;	
-char* ub;	
-char* lb;	
+struct ifdevmtu* ptr;	
+struct ifdevmtu* ub;	
+struct ifdevmtu* lb;	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.45

```diff

 struct __firebloom::wide_ptr.bidi_indexable.45 {
-struct mbuf* ptr;	
-struct mbuf* ub;	
-struct mbuf* lb;	
+void* ptr;	
+void* ub;	
+void* lb;	
 }

```
#### __firebloom::wide_ptr.indexable.101

```c
struct __firebloom::wide_ptr.indexable .101 {
  char *ptr;
  char *ub;
}

```
#### __firebloom::wide_ptr.indexable.100

```diff

 struct __firebloom::wide_ptr.indexable.100 {
-char* ptr;	
-char* ub;	
+u_char* ptr;	
+u_char* ub;	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.131

```diff

 struct __firebloom::wide_ptr.bidi_indexable.131 {
-struct pf_mtag* ptr;	
-struct pf_mtag* ub;	
-struct pf_mtag* lb;	
+struct secpolicy* ptr;	
+struct secpolicy* ub;	
+struct secpolicy* lb;	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.113

```diff

 struct __firebloom::wide_ptr.bidi_indexable.113 {
-struct m_tag* ptr;	
-struct m_tag* ub;	
-struct m_tag* lb;	
+struct ifnet_keepalive_offload_frame* ptr;	
+struct ifnet_keepalive_offload_frame* ub;	
+struct ifnet_keepalive_offload_frame* lb;	
 }

```
#### __firebloom::wide_ptr.bidi_indexable.133

```diff

 struct __firebloom::wide_ptr.bidi_indexable.133 {
-struct in_ifaddr* ptr;	
-struct in_ifaddr* ub;	
-struct in_ifaddr* lb;	
+struct flowadv* ptr;	
+struct flowadv* ub;	
+struct flowadv* lb;	
 }

```
#### __firebloom::wide_ptr.indexable.99

```diff

 struct __firebloom::wide_ptr.indexable.99 {
-u_char* ptr;	
-u_char* ub;	
+struct user_msghdr_x* ptr;	
+struct user_msghdr_x* ub;	
 }

```
#### __firebloom::wide_ptr.indexable.82

```diff

 struct __firebloom::wide_ptr.indexable.82 {
-void* ptr;	
-void* ub;	
+uint64_t* ptr;	
+uint64_t* ub;	
 }

```
