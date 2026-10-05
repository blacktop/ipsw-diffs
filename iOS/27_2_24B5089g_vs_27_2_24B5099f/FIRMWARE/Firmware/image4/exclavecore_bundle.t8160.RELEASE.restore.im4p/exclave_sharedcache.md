## exclave_sharedcache

> `Firmware/image4/exclavecore_bundle.t8160.RELEASE.restore.im4p/exclave_sharedcache`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_reflstr`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_types2`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_entry`
- `__TEXT.__chain_fixups`
- `__DATA.__TIGHTBEAM_VT`
- `__DATA.__TIGHTBEAM`
- `__DATA.__mod_init_func`
- `__DATA.__shared_cache`
- `__DATA.__got`
- `__PDATA.__auth_ptr`
- `__PDATA.__const`
- `__PDATA.__mod_init_func`
- `__PDATA.__data`
- `__PDATA.__shared_cache`

```diff

-1777.40.28.0.2
-  __TEXT.__text: 0x5faa84
+1777.40.34.0.0
+  __TEXT.__text: 0x5fc7fc
   __TEXT.__lcxx_override: 0xd0
-  __TEXT.__cstring: 0x50df1
-  __TEXT.__const: 0x123fa4
-  __TEXT.__swift5_typeref: 0x144ee
+  __TEXT.__cstring: 0x50e61
+  __TEXT.__const: 0x124124
+  __TEXT.__swift5_typeref: 0x1452c
   __TEXT.__swift5_reflstr: 0x13508
   __TEXT.__swift5_assocty: 0x7d10
-  __TEXT.__swift5_fieldmd: 0x1cdb0
-  __TEXT.__constg_swiftt: 0x28a48
+  __TEXT.__swift5_fieldmd: 0x1cdf4
+  __TEXT.__constg_swiftt: 0x28aa8
   __TEXT.__swift5_protos: 0x998
-  __TEXT.__swift5_proto: 0x3e94
-  __TEXT.__swift5_types: 0x251c
+  __TEXT.__swift5_proto: 0x3e98
+  __TEXT.__swift5_types: 0x2524
   __TEXT.__swift5_types2: 0x60
   __TEXT.__swift5_builtin: 0x15b8
-  __TEXT.__swift5_capture: 0x1048
-  __TEXT.__objc_methtype: 0xe1
+  __TEXT.__swift5_capture: 0x1068
+  __TEXT.__objc_methtype: 0x111
   __TEXT.__swift5_mpenum: 0x3b8
   __TEXT.__swift_as_entry: 0x9b4
   __TEXT.__swift_as_ret: 0xb2c

   __TEXT.__term_offsets: 0x0
   __TEXT.__thread_starts: 0x0
   __TEXT.__chain_fixups: 0xb8
-  __TEXT.__eh_frame: 0x35da8
+  __TEXT.__eh_frame: 0x36060
   __DATA.__TIGHTBEAM_VT: 0x8a0
   __DATA.__TIGHTBEAM: 0x238
-  __DATA.__const: 0x3e5e0
-  __DATA.__data: 0x19110
+  __DATA.__const: 0x3e798
+  __DATA.__data: 0x19150
   __DATA.__mod_init_func: 0x40
-  __DATA.__ENDPOINTS: 0x1a744
-  __DATA.__auth_ptr: 0x2490
+  __DATA.__ENDPOINTS: 0x1a84b
+  __DATA.__auth_ptr: 0x2498
   __DATA.__DEVICETREE: 0x18
   __DATA.__shared_cache: 0x380
   __DATA.__MMIOREGS: 0x795

   __DATA_CONST.__mod_term_func: 0x0
   Functions: 657
   Symbols:   1
-  CStrings:  7432
+  CStrings:  7436
 
CStrings:
+ " DisplayManager is not configured!"
+ " but a session is already active!"
+ " but startTimestampUS is nil!"
+ "Builtin.Borrow is not supported in runtime type lookup"
+ "Initialized count must be in 0 ... unsafeUninitializedCapacity."
+ "sharedmem_framemap_getPhysicalAddress"
+ "sharedmem_framemap_setMapped_delta"
+ "v24@?0{sharedmem_pagerange=QQ}8"
- "Initialized count set to greater than specified capacity."
- "localmap_map(%zx): localmap() remap with changed PA (%llx != %llx)\n"
- "sharedmem_framemap_getPhysicalAddresses"
- "sharedmem_framemap_setMapped"
```
