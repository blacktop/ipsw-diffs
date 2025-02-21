## libobjc.A.dylib

> `/usr/lib/libobjc.A.dylib`

```diff

-928.3.0.0.0
-  __TEXT.__text: 0x3ebc8
+940.2.0.0.0
+  __TEXT.__text: 0x40144
   __TEXT.__auth_stubs: 0x760
   __TEXT.__delay_helper: 0xec
-  __TEXT.__objc_init_offs: 0x0
-  __TEXT.__objc_methlist: 0x4e4
+  __TEXT.__objc_methlist: 0x5ec
+  __TEXT.__const: 0x4138
   __TEXT.__objc_opt_ro: 0x4000
-  __TEXT.__const: 0x4100
-  __TEXT.__cstring: 0x4807
-  __TEXT.__gcc_except_tab: 0xb2c
+  __TEXT.__cstring: 0x49ab
+  __TEXT.__gcc_except_tab: 0xb44
   __TEXT.__dof_objc_runt: 0x113f
-  __TEXT.__unwind_info: 0xd30
+  __TEXT.__objc_init_offs: 0x0
+  __TEXT.__unwind_info: 0xd60
   __TEXT.__objc_classname: 0x4d
   __TEXT.__objc_methname: 0x3c1
   __TEXT.__objc_methtype: 0x11e
-  __DATA_CONST.__got: 0x48
-  __DATA_CONST.__const: 0x8e8
+  __DATA_CONST.__got: 0x40
+  __DATA_CONST.__const: 0x908
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_nlclslist: 0x20
   __DATA_CONST.__objc_protolist: 0x8

   __DATA_CONST.__objc_selrefs: 0x1d0
   __DATA_CONST.__objc_scoffs: 0x28
   __AUTH_CONST.__auth_got: 0x3c0
-  __AUTH_CONST.__auth_ptr: 0x8
+  __AUTH_CONST.__auth_ptr: 0x10
   __AUTH_CONST.__const: 0x620
-  __AUTH_CONST.__objc_const: 0x658
+  __AUTH_CONST.__objc_const: 0x468
   __AUTH.__objc_data: 0x50
-  __AUTH.__data: 0x40
   __AUTH.__objc_opt_ptrs: 0x8
+  __AUTH.__data: 0x40
   __DATA.__objc_ivar: 0x8
   __DATA.__data: 0xb8
   __DATA.__bss: 0x458
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x140
   __DATA_DIRTY.__data: 0x948
-  __DATA_DIRTY.__bss: 0x1400
+  __DATA_DIRTY.__bss: 0x1380
   __DATA_DIRTY.__common: 0x20
+  - /usr/lib/libRosetta.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libc++abi.dylib
   - /usr/lib/libobjc-env.dylib
   - /usr/lib/swift/libswiftCore.dylib
-  Functions: 879
-  Symbols:   1086
-  CStrings:  555
+  Functions: 889
+  Symbols:   1102
+  CStrings:  562
 
Symbols:
+ __objc_supportsLazyRealization
+ _objc_thread_get_rip
+ _rosetta_is_current_process_translated
- __dyld_get_shared_cache_uuid
- __os_log_simple
CStrings:
+ "%s is faulting"
+ "%s is stochastically faulting"
+ "%s%s"
+ "CLASS: eagerly realizing class '%s' in objc_readClassPair, overlap found with superclass '%s' - subclass start %u < superclass size %u"
+ "Class %s is implemented in both %s (%p) and %s (%p). This may cause spurious casting failures and mysterious crashes. One of the duplicates must be removed or renamed."
+ "Class of category %s at %p in %s is set to %p, indicating it is missing from an installed root"
+ "POOL HIGHWATER:     "
+ "Superclass of %s at %p in %s is set to %p, indicating it is missing from an installed root"
+ "fault"
+ "stochastic-fault"
+ "stochasticFault"
- "1"
- "Class %s is implemented in both %s (%p) and %s (%p). One of the two will be used. Which one is undefined."
- "POOL HIGHWATER:     %s"
- "nonmeta class %s (%p) unexpectedly not realized"

```
