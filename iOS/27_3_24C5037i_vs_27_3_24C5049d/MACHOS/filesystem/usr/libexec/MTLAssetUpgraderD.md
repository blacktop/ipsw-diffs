## MTLAssetUpgraderD

> `/usr/libexec/MTLAssetUpgraderD`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-384.5.0.0.0
-  __TEXT.__text: 0x18498
+384.7.0.0.0
+  __TEXT.__text: 0x184c8
   __TEXT.__auth_stubs: 0x8c0
   __TEXT.__objc_stubs: 0x840
   __TEXT.__gcc_except_tab: 0xfe8
Functions:
~ __ZN17MTLArchiveUsageDB5storeERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEjjm : 444 -> 448
~ __ZN17MTLArchiveUsageDB5pruneEl : 280 -> 292
~ __ZN17MTLArchiveUsageDB18getPrioritizedListEv : 888 -> 896
~ __ZN13FileSignatureC2Ev : 16 -> 12
~ __ZN13FileSignatureC2ERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE : 172 -> 200
~ __ZN14ArchivePayloadC2E7MDB_val : 116 -> 108
~ __ZN15MTLArchiveMapDB6removeEP7MDB_txnRKNSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEjj : 920 -> 916
~ __ZN15MTLArchiveMapDB4readERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEjj : 1084 -> 1088
~ __ZN14MTLVersionedDB9dumpTableEv : 396 -> 404
```
