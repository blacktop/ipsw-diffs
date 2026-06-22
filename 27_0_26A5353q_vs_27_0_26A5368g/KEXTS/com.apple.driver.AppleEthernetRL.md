## com.apple.driver.AppleEthernetRL

> `com.apple.driver.AppleEthernetRL`

```diff

-161.0.0.0.0
-  __TEXT.__cstring: 0x2822 sha256:1e2860986a8f24b11249b9c0d6e4930332f2e1c30e30bbcbdc803b5a79191b5e
+168.0.0.0.0
+  __TEXT.__cstring: 0x2a8f sha256:7bab1cc9dc1e6b5bfa95bb2042f0df449e6887ff6e8324b1c205c39e66d4283f
   __TEXT.__const: 0x22888 sha256:e6819cbd462422a66e7d879b369579314bbfc67cb36e04886c562fc1bd6de5db
   __TEXT.__os_log: 0x75 sha256:ac4fa6e42ffb66fbae4cf8acbb9978617b6efa0a7935e4d94fc3fe4b7310c3a7
-  __TEXT_EXEC.__text: 0x27d04 sha256:3100d30d440ae0658fc92b0bb19879463bbebc7a1550090d9e001d3cad880470
-  __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x1e8 sha256:c63bf0a7d24e9e7d202951b8796e830e5aae934e61a0886f52c4cb8f7f885885
+  __TEXT_EXEC.__text: 0x28430 sha256:241a5a352f1b923298b2884a517dc04d5b802979f43169c81460aeba61602f87
+  __TEXT_EXEC.__auth_stubs: 0x720 sha256:75b92d2a7e695100139027a75f18c7139419c90f4a993763ad2e8ac37f6197fb
+  __DATA.__data: 0x1e8 sha256:f315341d1e9e0fb56a41c382f4aea43ac329d4d10815ad4c7daa90e1815e639b
   __DATA.__common: 0x128 sha256:250f52cb2d6f1966a29f6ac771fa1cd185b8f8531396c8a4026c0fe635617e0c
   __DATA.__bss: 0x28 sha256:2c34ce1df23b838c5abf2a7f6437cca3d3067ed509ff25f11df6b11b582b51eb
-  __DATA_CONST.__mod_init_func: 0x40 sha256:74408263fc391ae4dbe46de6985f68169a6c63ef2ecdf3e526fac3ac055fd58b
-  __DATA_CONST.__mod_term_func: 0x40 sha256:57abe0bd930fd127b459b87819f22eb9ef55c44b384356c1130e2d3dacd9b8b4
-  __DATA_CONST.__const: 0x4a078 sha256:2ed89ca7ee262d676096a1840ff48411e0a500861dcee5b85a7faa750580eeb6
-  __DATA_CONST.__kalloc_type: 0x2c0 sha256:b5d82e84bc3a730d9d812e068de1919f864bc58dbc4348caef29b0529bdad8e8
-  __DATA_CONST.__kalloc_var: 0x320 sha256:050f28081d0b83ee3afe270f0049bb5d8c3e5d0bb827aa9b81c933ab133c144c
-  __DATA_CONST.__auth_got: 0x3a0 sha256:e4ac3e6b4bbb86dc66e9c9dbf19c3df11e327c2bf8e01d27c5485887f1053b5e
-  __DATA_CONST.__got: 0xc0 sha256:52cbedf0568d2eb0995b3c90868cfd00dad36d55ce85d863b2aba0a301c17a78
-  __DATA_CONST.__auth_ptr: 0x8 sha256:b7f3110abd0784d73da2bdefcc3262c6d1f2e54e9d50b8cdd42375dae4b62a4d
-  UUID: F7A4BAB2-1C10-3A11-A9E2-EA52FD13C1E2
-  Functions: 571
-  Symbols:   1362
-  CStrings:  332
+  __DATA_CONST.__mod_init_func: 0x40 sha256:5a87335afd41eacb238733f97e0c01ead6b7e49974af302591b115d10f50789d
+  __DATA_CONST.__mod_term_func: 0x40 sha256:d4d16c1c9cfce0489885d0e28c719c8f43d3da7b5dd5931f162cdcce1ce9a4db
+  __DATA_CONST.__const: 0x4a078 sha256:49b17cf7f5454f613505f30f939d3a0f27e164388ec9fc1cd3ce8df0380cca1c
+  __DATA_CONST.__kalloc_type: 0x2c0 sha256:0c82b760978f6d46e35fca4a7703afab7123f9bc6ad25e7eebedd924322c434b
+  __DATA_CONST.__kalloc_var: 0x320 sha256:b421ac72ceb5d3a7b296856c1cd05797e6e1cb3a4af4cda31bcbcd287bdb92ef
+  __DATA_CONST.__auth_got: 0x390 sha256:f4b029b15cb7489144d0e9cc32fff6d1051e12ae107cd585255feb2c8fb1c826
+  __DATA_CONST.__got: 0xc0 sha256:a16d0088bc5f8616da5b75699647b863383db7603d98b728a93f770271a0e53d
+  UUID: 04BDF321-0A2E-30E3-9830-A5A76890D116
+  Functions: 580
+  Symbols:   1370
+  CStrings:  343
 
Symbols:
+ _IORecursiveLockAlloc
+ _IORecursiveLockFree
+ _ZN15AppleEthernetRL22transmitTimeSyncPacketEPN20IOEthernetController19IOEthernetAVBPacketEy.cold.1
+ __ZL23re_set_phy_mcu_ram_codeP8re_softcPKtt
+ __ZN15AppleEthernetRL13finalizeRingsEv
+ __ZN15AppleEthernetRL18acquireAllAvbLocksEv
+ __ZN15AppleEthernetRL18releaseAllAvbLocksEv
+ __ZN15AppleEthernetRL19handleCarrierUpdateEP18IOTimerEventSource
+ __ZN15AppleEthernetRL20writeMultiBufferIPC2EhPKvjPh
+ __ZN15AppleEthernetRL23acquireAllWorkLoopLocksEv
+ __ZN15AppleEthernetRL23releaseAllWorkLoopLocksEv
+ __ZN15AppleEthernetRL23validateNicProxyHandoffEv
+ __ZZN15AppleEthernetRL13allocateRingsEvE19kalloc_type_view_73
+ __ZZN15AppleEthernetRL13allocateRingsEvE19kalloc_type_view_93
+ __ZZN15AppleEthernetRL13allocateRingsEvE20kalloc_type_view_103
+ __ZZN15AppleEthernetRL14startInterfaceEvE20kalloc_type_view_274
+ __ZZN15AppleEthernetRL14startInterfaceEvE20kalloc_type_view_458
+ __ZZN15AppleEthernetRL4stopEP9IOServiceE20kalloc_type_view_283
+ __ZZN15AppleEthernetRL9freeRingsEvE20kalloc_type_view_116
+ __ZZN15AppleEthernetRL9freeRingsEvE20kalloc_type_view_120
+ __ZZN15AppleEthernetRL9freeRingsEvE20kalloc_type_view_125
+ __ZZN15AppleEthernetRL9freeRingsEvE20kalloc_type_view_131
- _IOLockAlloc
- _IOLockFree
- _IOLockLock
- _IOLockUnlock
- __ZZN15AppleEthernetRL13allocateRingsEvE19kalloc_type_view_63
- __ZZN15AppleEthernetRL13allocateRingsEvE19kalloc_type_view_76
- __ZZN15AppleEthernetRL13allocateRingsEvE19kalloc_type_view_95
- __ZZN15AppleEthernetRL14startInterfaceEvE20kalloc_type_view_224
- __ZZN15AppleEthernetRL14startInterfaceEvE20kalloc_type_view_408
- __ZZN15AppleEthernetRL4stopEP9IOServiceE20kalloc_type_view_271
- __ZZN15AppleEthernetRL9freeRingsEvE20kalloc_type_view_108
- __ZZN15AppleEthernetRL9freeRingsEvE20kalloc_type_view_112
- __ZZN15AppleEthernetRL9freeRingsEvE20kalloc_type_view_117
- __ZZN15AppleEthernetRL9freeRingsEvE20kalloc_type_view_127
- ___chkstk_darwin
- ___chkstk_darwin_probe
CStrings:
+ " (recovered missed link-up edge)"
+ "121111121222121211111112111212221111122221122212122222222222111111222211111121222211221111221111221122221212112222121211222212121122221212112222121211222212121122222221111222121211211222222222211112221222112121121121122222222222222222222222222221111111222111"
+ "[0x%llx] rl::%s(%d): dropping %u local IPv4 beyond FW cap %u\n"
+ "[0x%llx] rl::%s(%d): dropping %u local IPv6 beyond FW cap %u\n"
+ "[0x%llx] rl::%s(%d): dropping %u other IPv4 beyond FW cap %u\n"
+ "[0x%llx] rl::%s(%d): dropping %u other IPv6 beyond FW cap %u\n"
+ "[0x%llx] rl::%s(%d): invalid IPv4 counts: local %u total %u (cap total %u)\n"
+ "[0x%llx] rl::%s(%d): invalid IPv6 counts: local %u total %u (cap total %u)\n"
+ "[0x%llx] rl::%s(%d): invalid wake port counts: UDP %u TCP %u (caps UDP %u TCP %u)\n"
+ "[0x%llx] rl::%s(%d): link_state=%s, media active %d->%d%s\n"
+ "handleCarrierUpdate"
+ "validateNicProxyHandoff"
- "12111112122212121111111211121222111112222112221212222222222211111122221111112122221122111122111122112222121211222212121122221212112222121211222212121122221212112222222111122212121121122222222221111222122211212112112112222222222222222222222222222111111122211"

```
