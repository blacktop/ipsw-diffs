## libAmber.dylib

> `/usr/lib/libAmber.dylib`

```diff

-  __TEXT.__text: 0x29350
+  __TEXT.__text: 0x292f0
   __TEXT.__const: 0xbf0
   __TEXT.__gcc_except_tab: 0x2b9c
   __TEXT.__cstring: 0x5cfc
Sections:
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__cstring : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__weak_got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH.__data : content changed
Functions:
~ __ZN5amber12murMurHash64ENS_15ConstMemoryViewE : 260 -> 276
~ ____ZN5amber26DiskImageIORingsSubscriber7executeEv_block_invoke : 1528 -> 1512
~ __ZN5amber11BlockDevice19setPrefetchSequenceERKNS_11ArrayObjectINS_15ObjectStorePathEEEy : 404 -> 396
~ __ZN5amber11ArrayObjectINS_15ObjectStorePathEE9jsonParseERNS_15JSONInputStreamE : 652 -> 636
~ __ZNK5amber11ArrayObjectINS_15ObjectStorePathEE13jsonSerializeERNS_16JSONOutputStreamENSt3__117basic_string_viewIcNS5_11char_traitsIcEEEE : 284 -> 272
~ __ZNSt3__16vectorIN5amber15ObjectStorePathENS_9allocatorIS2_EEE16__destroy_vectorclB9fqe220106Ev : 176 -> 156
~ __ZNSt3__134__uninitialized_allocator_relocateB9fqe220106INS_9allocatorIN5amber15ObjectStorePathEEEPS3_EEvRT_T0_S8_S8_ : 180 -> 176
~ __ZN5amber10XPCSession17xpcSetStringArrayEPvPKcRKNSt3__16vectorINS4_12basic_stringIcNS4_11char_traitsIcEENS4_9allocatorIcEEEENS9_ISB_EEEE : 284 -> 264
~ __ZNSt3__134__uninitialized_allocator_relocateB9fqe220106INS_9allocatorIN5amber15ObjectStorePathEEEPS3_EEvRT_T0_S8_S8_.cold.1 : 96 -> 80

```
