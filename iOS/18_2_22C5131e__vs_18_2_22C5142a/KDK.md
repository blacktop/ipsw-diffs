## KDKs

- `KDK_15.2_24C5073e.kdk/System/Library/Kernels/kernel.release.t6030`
- `KDK_15.2_24C5089c.kdk/System/Library/Kernels/kernel.release.t6030`

#### __firebloom::wide_ptr.bidi_indexable.141

```diff

 struct __firebloom::wide_ptr.bidi_indexable.141 {
-const struct sadb_sa* ptr;	
-const struct sadb_sa* ub;	
-const struct sadb_sa* lb;	
+struct in6_pktinfo* ptr;	
+struct in6_pktinfo* ub;	
+struct in6_pktinfo* lb;	
 }

```
#### __firebloom::wide_ptr.indexable.143

```c
struct __firebloom::wide_ptr.indexable.143 {
  void *ptr;
  void *ub;
}

```
#### __firebloom::wide_ptr.bidi_indexable.149

```c
struct __firebloom::wide_ptr.bidi_indexable.149 {
  ctrace_t *ptr;
  ctrace_t *ub;
  ctrace_t *lb;
}

```
