## com.apple.kernel

> `com.apple.kernel`

```diff

-12377.100.630.502.1
-  __TEXT.__const: 0x36160
+12377.102.10.0.0
+  __TEXT.__const: 0x36150
   __TEXT.__copyio_vectors: 0x2c0
-  __TEXT.__cstring: 0x888f2
-  __TEXT.__os_log: 0x3dd72
+  __TEXT.__cstring: 0x8843d
+  __TEXT.__os_log: 0x3dd23
   __TEXT.__eh_frame: 0x7e0
   __DATA_CONST.__hib_const: 0x120
-  __DATA_CONST.__const: 0x119ed0
+  __DATA_CONST.__const: 0x119d48
   __DATA_CONST.__kalloc_type: 0x14540
-  __DATA_CONST.__assert: 0xd70
+  __DATA_CONST.__assert: 0xc58
   __DATA_CONST.__kalloc_var: 0x78f0
   __DATA_CONST.__exclaves_bt: 0x78
   __DATA_CONST.__kern_brk_desc: 0x78

   __DATA_CONST.__auth_ptr: 0x8
   __DATA_SPTM.__const: 0x3c000
   __TEXT_EXEC.__hib_text: 0xed8
-  __TEXT_EXEC.__text: 0x8b4874
-  __TEXT_BOOT_EXEC.__bootcode: 0x5290
+  __TEXT_EXEC.__text: 0x8b3e40
+  __TEXT_BOOT_EXEC.__bootcode: 0x5250
   __KLD.__text: 0x1460
   __LASTDATA_CONST.__mod_init_func: 0x8
   __LAST.__pinst: 0x8
   __LAST.__last: 0x0
   __KLDDATA.__cstring: 0x6e1
-  __KLDDATA.__const: 0x37e0
+  __KLDDATA.__const: 0x3740
   __KLDDATA.__mod_init_func: 0x8
   __KLDDATA.__mod_term_func: 0x8
   __KLDDATA.__bss: 0x1
   __DATA.__data: 0x17ff9
   __DATA.__lock_grp: 0x5b18
   __DATA.__percpu: 0x7870
-  __DATA.__common: 0x79878
-  __DATA.__bss: 0xa34e8
+  __DATA.__common: 0x77778
+  __DATA.__bss: 0xa3588
   __BOOTDATA.__data: 0x18000
-  __BOOTDATA.__init_entry_set: 0x13710
-  __BOOTDATA.__init: 0x5b588
+  __BOOTDATA.__init_entry_set: 0x135a8
+  __BOOTDATA.__init: 0x5b568
   __BOOTDATA.__static_ifinit: 0x8
   __BOOTDATA.__static_if: 0x0
   __PRELINK_TEXT.__text: 0x0

   __PLK_LLVM_COV.__llvm_covmap: 0x0
   __PLK_LINKEDIT.__data: 0x0
   __LINKINFO.__symbolsets: 0x48024
-  UUID: A22AD7D4-162B-3534-BBFD-5F734EEE604D
-  Functions: 21310
+  UUID: 8A400573-143C-3FC7-A6D3-B881A2B3C271
+  Functions: 21315
   Symbols:   0
-  CStrings:  20752
+  CStrings:  20734
 
CStrings:
+ "ast.c"
+ "rwlock_count is %d for thread %p, possibly it still holds a rwlock @%s:%d"
- "!os_sub_overflow(*__counter, free_page_count, __counter)"
- "%s: binary '%s' does not satisfy requirements for 4k page size (fatal_mode=%d)"
- "Returning to userspace with floor boost set (may indicate kernel lock held), thread ptr %p tid %llu sched_flags 0x%x priority_floor_count %d @%s:%d"
- "Returning to userspace with rw lock held, thread ptr %p tid %llu sched_flags 0x%x rwlock_count %d @%s:%d"
- "Returning to userspace with waitqueue promotion, thread ptr %p tid %llu sched_flags 0x%x waitq %p @%s:%d"
- "active tag storages with free covered pages intended for kernel-tagged allocations"
- "active_kernel"
- "com.apple.private.4k-pages"
- "cpu_kernel_tagged"
- "free kernel-tagged pages in the MTE free queue"
- "free tagged pages for zalloc in CPU lists"
- "kernel_tagged"
- "load_machfile"
- "number of active tag storage pages supporting kernel allocators"
- "tag_storage_active_kernel"
- "tagged pages in use by zalloc"
- "tagged_kernel"
- "thread (ptr %p, tid %llu) has nonzero kern_promotion_schedpri %d when trying to return to userspace--this may indicate it still holds a kernel lock @%s:%d"
- "thread (ptr %p, tid %llu) is trying to go to userspace but is the inheritor of kernel turnstile %p (type %hhd, proprietor %p, waited on by thread (ptr %p, tid %llu)) @%s:%d"
- "thread (ptr %p, tid %llu) is trying to go to userspace but is the inheritor of kernel turnstile %p (type %hhd, proprietor %p, waiter unknown) @%s:%d"

```
