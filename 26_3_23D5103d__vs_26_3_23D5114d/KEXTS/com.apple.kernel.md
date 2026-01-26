## com.apple.kernel

> `com.apple.kernel`

```diff

-12377.80.267.0.0
+12377.80.273.502.1
   __TEXT.__const: 0x354b0
   __TEXT.__copyio_vectors: 0x2c0
-  __TEXT.__cstring: 0x8048b
-  __TEXT.__os_log: 0x3c728
+  __TEXT.__cstring: 0x80485
+  __TEXT.__os_log: 0x3c780
   __TEXT.__eh_frame: 0x7e0
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x2d8

   __DATA_CONST.__exclaves_bt: 0x78
   __DATA_CONST.__kern_brk_desc: 0x78
   __DATA_SPTM.__const: 0x3c000
-  __TEXT_EXEC.__text: 0x8ac0dc
+  __TEXT_EXEC.__text: 0x8ac3a0
   __TEXT_EXEC.__hib_text: 0xf38
   __TEXT_BOOT_EXEC.__bootcode: 0x51d0
   __KLD.__text: 0x1638

   __PLK_LLVM_COV.__llvm_covmap: 0x0
   __PLK_LINKEDIT.__data: 0x0
   __LINKINFO.__symbolsets: 0x471ae
-  UUID: 1098B005-B050-36FD-B7D1-2E99300951DD
+  UUID: 765963DD-032B-30A2-81A7-E75134132BAB
   Functions: 20794
   Symbols:   0
-  CStrings:  20300
+  CStrings:  20301
 
Functions:
~ necp_client_add_flow : 3660 -> 3792
~ necp_update_client_result -> sub_fffffe0008633320 : 7660 -> 7720
~ sub_fffffe00087ee684 -> sub_fffffe00087ee744 : 516 -> 512
~ filt_aiotouch -> sub_fffffe00087eeaf4 : 60 -> 32
~ sub_fffffe00087eead0 -> sub_fffffe00087eeb70 : 208 -> 320
~ sub_fffffe00087eeba0 -> sub_fffffe00087eecb0 : 272 -> 320
~ sub_fffffe00087ef7d0 -> sub_fffffe00087ef910 : 228 -> 312
~ sub_fffffe00087efbf4 -> sub_fffffe00087efd88 : 600 -> 352
~ sub_fffffe00087efe4c -> sub_fffffe00087efee8 : 316 -> 600
~ aio_return : 452 -> 464
~ lio_listio : 1132 -> 1204
~ tracker_lookup : 568 -> 684
~ sub_fffffe0008b6738c -> sub_fffffe0008b6760c : 196 -> 264
~ sub_fffffe0008b78010 -> sub_fffffe0008b782d4 : 208 -> 204
~ sub_fffffe0008b78f70 -> sub_fffffe0008b79230 : 40005776 -> 40021456
~ sub_fffffe000b1a51c4 -> sub_fffffe000b1a91c4 : 18446744073669537340 -> 18446744073669520956
CStrings:
+ "%s: <pid %d> Disallow flow add with flow divert result\n"
+ "%s: <pid %d> Requested nexus not found\n"
+ "1111112222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221121122222222222211222122112222121"
+ "Ledger credit failed for exclaves carveout, error code %d @%s:%d"
+ "Retry lookup with v4"
- "%s: kn %p kev %p (NOT EXPECTED TO BE CALLED!!) @%s:%d"
- "11111122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221121122222222222211222122112222121"
- "Requested nexus not found"
- "filt_aiotouch"

```
