## KDKs

- `KDK_15.4_24E5228e.kdk/System/Library/Kernels/kernel.release.t6031`
- `KDK_15.4_24E5238a.kdk/System/Library/Kernels/kernel.release.t6031`

#### __bounds_safety::wide_ptr.indexable.87

```diff

 struct __bounds_safety::wide_ptr.indexable.87 {
-uint8_t* ptr;	
-uint8_t* ub;	
+char* ptr;	
+char* ub;	
 }

```
#### __bounds_safety::wide_ptr.indexable.132

```c
struct __bounds_safety::wide_ptr.indexable.132 {
  struct flow_divert_group **ptr;
  struct flow_divert_group **ub;
}

```
#### flow_divert_pcb

```diff

 struct ifnet* original_last_outifp6;	
 struct ifnet* original_last_outifp;	
 uint8_t original_vflag;	
+_Bool plugin_locked;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.122

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.122 {
-const unsigned char* ptr;	
-const unsigned char* ub;	
-const unsigned char* lb;	
+ctrace_t* ptr;	
+ctrace_t* ub;	
+ctrace_t* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.127

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.127 {
-struct inpcb** ptr;	
-struct inpcb** ub;	
-struct inpcb** lb;	
+struct m_tag* ptr;	
+struct m_tag* ub;	
+struct m_tag* lb;	
 }

```
