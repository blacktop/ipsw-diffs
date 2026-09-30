## com.apple.kernel

> `com.apple.kernel`

```diff

   __TEXT.__const: 0x36400
   __TEXT.__copyio_vectors: 0x2c0
-  __TEXT.__cstring: 0x886d1
-  __TEXT.__os_log: 0x3e026
+  __TEXT.__cstring: 0x886f9
+  __TEXT.__os_log: 0x3e117
   __TEXT.__eh_frame: 0x7e0
   __DATA_CONST.__hib_const: 0x120
   __DATA_CONST.__const: 0x119e90

   __DATA_CONST.__auth_ptr: 0x8
   __DATA_SPTM.__const: 0x3c000
   __TEXT_EXEC.__hib_text: 0xed8
-  __TEXT_EXEC.__text: 0x8b8434
+  __TEXT_EXEC.__text: 0x8b8984
   __TEXT_BOOT_EXEC.__bootcode: 0x5250
   __KLD.__text: 0x1460
   __LASTDATA_CONST.__mod_init_func: 0x8

   __PLK_LLVM_COV.__llvm_covmap: 0x0
   __PLK_LINKEDIT.__data: 0x0
   __LINKINFO.__symbolsets: 0x48096
-  Functions: 21340
+  Functions: 21345
   Symbols:   0
-  CStrings:  20761
+  CStrings:  20768
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__copyio_vectors : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__kalloc_type : content changed
~ __DATA_CONST.__assert : content changed
~ __DATA_CONST.__kalloc_var : content changed
~ __DATA_CONST.__exclaves_bt : content changed
~ __DATA_CONST.__kern_brk_desc : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __LASTDATA_CONST.__mod_init_func : content changed
~ __KLDDATA.__const : content changed
~ __KLDDATA.__mod_init_func : content changed
~ __KLDDATA.__mod_term_func : content changed
~ __DATA.__data : content changed
~ __BOOTDATA.__init_entry_set : content changed
~ __BOOTDATA.__init : content changed
~ __BOOTDATA.__static_ifinit : content changed
CStrings:
+ "%s: bpf%u already attached to %s error %d"
+ "%s: bpf%u and bpf%u have incompatible flags 0x%x != 0x%x error %d"
+ "%s: bpf%u and bpf%u have incompatible interfaces %s and %s error %d"
+ "%s: d_from is closing or detached error %d"
+ "%s: d_to is closing or detaching error %d"
+ "%s: interface %s not supported error %d"
+ "BIOCSETIF"
+ "BIOCSEXTHDR"
+ "BIOCSPKTHDRV2"
+ "BIOCSTRUNCATE"
- "%s: d_from is closing error %d"
- "%s: d_to is closing error %d"
- "bpf_setif"

```
