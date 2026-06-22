## com.apple.plugin.IOgPTPPlugin

> `com.apple.plugin.IOgPTPPlugin`

```diff

-1500.96.0.0.0
-  __TEXT.__cstring: 0x6bd6 sha256:3afb6554d9a8c4982f5acc3b34577f46d9429fde6d2d74dbf2d0cc69b43c1723
-  __TEXT.__os_log: 0x1bd96 sha256:c2e6670fc1bd0082e05e3d3a0e2453728cb3fd827fd11232351633985e0f234f
+1501.1.0.0.0
+  __TEXT.__cstring: 0x6cc3 sha256:e61b415ec0a20f02c883922f99e6b63336940baa73375802b1f175b0db137ac9
+  __TEXT.__os_log: 0x1c46f sha256:92c7e9d811afaff06dfb36664698d3160ba0cef57c03c930f206379cc15e8522
   __TEXT.__const: 0x2d2 sha256:88e1b7b6082434d3f4b5cb85443c8b916080e932481bed8ca396701badec81fa
-  __TEXT_EXEC.__text: 0x6e43c sha256:5de02a50e15cb83b7e21def12b49fb05b1921192ede6941a27659d164cbdb0af
-  __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0xc8 sha256:4004698b182e137221007144f1c15ee3711275d75d03a32d368e392913d90c33
+  __TEXT_EXEC.__text: 0x6fcec sha256:820affa404eadce06ee2e6e74e7e87ba8a2a040681a8bd559710aa664c717f28
+  __TEXT_EXEC.__auth_stubs: 0xe40 sha256:226810a1f5463bd89baacaf853b94a572d13051a98f437a96a4d24a36ed3dd02
+  __DATA.__data: 0xc8 sha256:17afa0a2006edc554788b0890b278c693c86ff08ee61a0b71e94f90b53f036d8
   __DATA.__common: 0x5d8 sha256:2010b55891b05a55428204b4cc0e2d03cd13f0727289c1bda6dc6d8935538218
   __DATA.__bss: 0xc8 sha256:6d9c54dee5660c46886f32d80e57e9dd0ffa57ee0cd2a762b036d9c8e0c3a33a
-  __DATA_CONST.__mod_init_func: 0x110 sha256:febc2016313a67b190628b44d90be62d7b395a783858b7cdbaa3effc43cc9ec7
-  __DATA_CONST.__mod_term_func: 0x110 sha256:69551ec58995dd7b43c79e3344bd1c3afab4af9560e07b57584b62e775b339e2
-  __DATA_CONST.__const: 0xea70 sha256:5dd507b390555732a13ee5ef90ff9d415faa58611b729589e80369ac5cdae7fc
-  __DATA_CONST.__kalloc_type: 0x980 sha256:3cf49a2fec065e527dc89951d1a1b9040d667ffcfdf1af4e87d3f8fe01ff369a
-  __DATA_CONST.__auth_got: 0x718 sha256:7e54b738ddf74b04eb8d52f3913aa391394ab68f826713d6e623483733b32e9a
-  __DATA_CONST.__got: 0x1b0 sha256:49493d716773acd4e53223325f6d8092e108a8eba0dfb39a32d43c91388d870f
-  UUID: FCC6B92B-4641-357C-AAF3-CE27119569A6
-  Functions: 1633
+  __DATA_CONST.__mod_init_func: 0x110 sha256:a30e26d8f278f57070d38d02ac9f031ea4d6d72b5ad65b567a2693258e3ce7c5
+  __DATA_CONST.__mod_term_func: 0x110 sha256:150357ec5e537b3f1dba0a7c8d0c34a58c8f5ef139d32027c397c9792f584982
+  __DATA_CONST.__const: 0xea70 sha256:74900d12cc97391c9a892905d93cd0ec018a2517530533e0f03e88e0c8a03cf8
+  __DATA_CONST.__kalloc_type: 0x980 sha256:a76b97d1775113d6087d9112d89063b3c168ea7d2bfb428c3b54f37dca540319
+  __DATA_CONST.__auth_got: 0x720 sha256:9032d6a86c71930501dcbdd05dacdbe81a83b024ea773ff3b54c0600353d08d1
+  __DATA_CONST.__got: 0x1b0 sha256:9456c6be0cbfee51261ef0a6d47f39f979c6ef733e791e3e430f0f90069b89a3
+  UUID: 9B6E6C2C-271D-3062-B566-A24A4265D6DC
+  Functions: 1637
   Symbols:   0
-  CStrings:  1534
+  CStrings:  1569
 
CStrings:
+ "  %s(%s): Announce has null grandmasterIdentity from source 0x%016llx:%u\n"
+ "  %s(%s): port-manager refcount for %s (Unicast%s) already balanced (kIOReturnNotFound)\n"
+ "  %s(%s): purging stale Unicast%s entry for %s (hadPort=%d)\n"
+ "  %s(%s): unexpected 0x%08x rebalancing port-manager refcount for %s (Unicast%s)\n"
+ "%s %s %p terminated for %s, running cleanup\n"
+ "%s %s %p terminated with no %s property, dropping cleanup\n"
+ "%s %s %p terminated with no BSD Name property, dropping cleanup\n"
+ "%s called with NULL ifName, dropping cleanup\n"
+ "%s domain interface %s terminated\n"
+ "%s failed to allocate domains iterator for %s, leaving state intact\n"
+ "%s failed to allocate domainsArray for %s, leaving state intact\n"
+ "%s::%s UnicastUDPv4EtE port attach() failed for interface %s, provider %p (isInactive=%d)\n"
+ "%s::%s UnicastUDPv4EtE port init() failed for interface %s\n"
+ "%s::%s UnicastUDPv4EtE port start() failed for interface %s, provider %p (isInactive=%d)\n"
+ "%s::%s UnicastUDPv4PtP port attach() failed for interface %s, provider %p (isInactive=%d)\n"
+ "%s::%s UnicastUDPv4PtP port init() failed for interface %s\n"
+ "%s::%s UnicastUDPv4PtP port start() failed for interface %s, provider %p (isInactive=%d)\n"
+ "%s::%s UnicastUDPv6EtE port attach() failed for interface %s, provider %p (isInactive=%d)\n"
+ "%s::%s UnicastUDPv6EtE port init() failed for interface %s\n"
+ "%s::%s UnicastUDPv6EtE port start() failed for interface %s, provider %p (isInactive=%d)\n"
+ "%s::%s UnicastUDPv6PtP port attach() failed for interface %s, provider %p (isInactive=%d)\n"
+ "%s::%s UnicastUDPv6PtP port init() failed for interface %s\n"
+ "%s::%s UnicastUDPv6PtP port start() failed for interface %s, provider %p (isInactive=%d)\n"
+ "12111112122212121111111111111111121121121111111112222222222222112112111112122222111112112112222"
+ "Failed to add tsninterface terminated notifier.\n"
+ "IOTimeSyncgPTPManager %s dumped controller adapter for %s\n"
+ "IOTimeSyncgPTPManager %s dumped interface adapter for %s\n"
+ "IOTimeSyncgPTPManager %s dumped port manager for %s\n"
+ "LinkLayerEtE"
+ "LinkLayerPtP"
+ "NULL == fTSNInterfaceTerminatedNotifier"
+ "UDPv4EtE"
+ "UDPv4PtP"
+ "UDPv6EtE"
+ "UDPv6PtP"
+ "addUnicastUDPv4Port"
+ "addUnicastUDPv6Port"
+ "cleanupForInterfaceByName"
+ "notifier == fTSNInterfaceTerminatedNotifier"
+ "tsnInterfaceTerminated"
- "%s domain interface %s terminated"
- "121111121222121211111111111111111211211211111112222222222222112112111112122222111112112112222"
- "IOTimeSyncgPTPManager interfaceTerminated dumped controller adapter for %s\n"
- "IOTimeSyncgPTPManager interfaceTerminated dumped interface adapter for %s\n"
- "IOTimeSyncgPTPManager interfaceTerminated dumped port manager for %s\n"

```
