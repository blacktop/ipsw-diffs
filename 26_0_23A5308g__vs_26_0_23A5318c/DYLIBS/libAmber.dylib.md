## libAmber.dylib

> `/usr/lib/libAmber.dylib`

```diff

-30.0.0.0.0
-  __TEXT.__text: 0xb4d10
+30.1.0.0.0
+  __TEXT.__text: 0xb5224
   __TEXT.__auth_stubs: 0x10c0
   __TEXT.__objc_methlist: 0x2d4
-  __TEXT.__gcc_except_tab: 0x9c54
-  __TEXT.__cstring: 0x10ff4
-  __TEXT.__const: 0x1d96
+  __TEXT.__gcc_except_tab: 0x9d14
+  __TEXT.__cstring: 0x11034
+  __TEXT.__const: 0x1d86
   __TEXT.__oslogstring: 0x3
-  __TEXT.__unwind_info: 0x39e0
+  __TEXT.__unwind_info: 0x3a08
   __TEXT.__objc_classname: 0xa0
   __TEXT.__objc_methname: 0x818
   __TEXT.__objc_methtype: 0x253

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2C958F12-B376-3777-A5C1-AFDE41583E00
-  Functions: 2330
-  Symbols:   6614
-  CStrings:  2861
+  UUID: A0CE3F87-63AA-3889-8012-57A929EAD819
+  Functions: 2331
+  Symbols:   6619
+  CStrings:  2863
 
Symbols:
+ __ZN5amber10BlockCache4readEyRKNS_17MutableMemoryViewE
+ __ZN5amber10BlockCache5writeEyRKNS_15ConstMemoryViewE
+ __ZN5amber14FileBlockCache8dataReadERKNS_17MutableMemoryViewEy
+ __ZN5amber14FileBlockCache9dataWriteERKNS_15ConstMemoryViewEy
+ __ZN5amber16MemoryBlockCache8dataReadERKNS_17MutableMemoryViewEy
+ __ZN5amber16MemoryBlockCache9dataWriteERKNS_15ConstMemoryViewEy
+ __ZN5amber16SharedBlockCache4readEjRKNS_5RangeERKNS_17MutableMemoryViewES3_RNS_10NBitVectorILj1EEE
+ __ZN5amber16SharedBlockCache5Shard4readEjRKNS_5RangeERKNS_17MutableMemoryViewES4_RNS_10NBitVectorILj1EEERNSt3__15mutexERNS_3SemERNSB_6atomicIiEE
+ __ZN5amber16SharedBlockCache5Shard5writeEjRKNS_5RangeERKNS_15ConstMemoryViewERNS_3SemERNSt3__16atomicIiEE
+ __ZN5amber16SharedBlockCache5Shard8readSyncEjRKNS_5RangeERKNS_17MutableMemoryViewES4_RNS_10NBitVectorILj1EEERNSt3__15mutexE
+ __ZN5amber16SharedBlockCache5Shard9writeSyncEjRKNS_5RangeERKNS_15ConstMemoryViewE
+ __ZN5amber22SharedCacheBlockDevice12setAttributeEjjRKNS_15ConstMemoryViewE
+ __ZN5amber22SharedCacheBlockDevice9ReadState14enqueueRequestEyj
- GCC_except_table92
- __ZN5amber10BlockCache4readEyPh
- __ZN5amber10BlockCache5writeEyPKh
- __ZN5amber14FileBlockCache8dataReadEPhy
- __ZN5amber14FileBlockCache9dataWriteEPKhy
- __ZN5amber16MemoryBlockCache8dataReadEPhy
- __ZN5amber16MemoryBlockCache9dataWriteEPKhy
- __ZN5amber16SharedBlockCache4readEjRKNS_5RangeEPvS3_RNS_10NBitVectorILj1EEE
- __ZN5amber16SharedBlockCache5Shard4readEjRKNS_5RangeEPhS4_RNS_10NBitVectorILj1EEERNSt3__15mutexERNS_3SemERNS9_6atomicIiEE
- __ZN5amber16SharedBlockCache5Shard5writeEjRKNS_5RangeEPKhRNS_3SemERNSt3__16atomicIiEE
- __ZN5amber16SharedBlockCache5Shard8readSyncEjRKNS_5RangeEPhS4_RNS_10NBitVectorILj1EEERNSt3__15mutexE
- __ZN5amber16SharedBlockCache5Shard9writeSyncEjRKNS_5RangeEPKh
- __ZN5amber22SharedCacheBlockDevice9ReadState14enqueueRequestEy
CStrings:
+ "30.1"
+ "data requests max aggregated I/O size"
+ "invalid max_io_size: %u"
- "30"

```
