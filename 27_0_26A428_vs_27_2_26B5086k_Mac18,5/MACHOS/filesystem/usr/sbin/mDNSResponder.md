## mDNSResponder

> `/usr/sbin/mDNSResponder`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-3111.0.5.0.1
-  __TEXT.__text: 0x106288
+3111.40.40.0.0
+  __TEXT.__text: 0x10689c
   __TEXT.__auth_stubs: 0x3000
   __TEXT.__objc_stubs: 0xf00
   __TEXT.__objc_methlist: 0x2a4
-  __TEXT.__const: 0x15e4
-  __TEXT.__cstring: 0x18ab4
-  __TEXT.__gcc_except_tab: 0x3d0
-  __TEXT.__oslogstring: 0x1feec
+  __TEXT.__const: 0x15dc
+  __TEXT.__cstring: 0x18b17
+  __TEXT.__gcc_except_tab: 0x3fc
+  __TEXT.__oslogstring: 0x2001b
   __TEXT.__objc_classname: 0x5fe
   __TEXT.__objc_methname: 0xe47
   __TEXT.__objc_methtype: 0x4ea
-  __TEXT.__unwind_info: 0x1d10
+  __TEXT.__unwind_info: 0x1d20
   __TEXT.__eh_frame: 0x7c
   __DATA_CONST.__const: 0x62d0
   __DATA_CONST.__cfstring: 0x1260

   - /usr/lib/libnetworkextension.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
-  Functions: 1802
-  Symbols:   3851
-  CStrings:  4569
+  Functions: 1804
+  Symbols:   3854
+  CStrings:  4576
 
Symbols:
+ GCC_except_table1152
+ GCC_except_table1231
+ GCC_except_table1240
+ GCC_except_table1368
+ GCC_except_table1764
+ ___block_descriptor_56_e8_32s40bs48r_e8_v12?0B8l
+ __resolved_cache_update_tracking
+ _domain_name_labels_length_with_limit
+ _regRecordAddTSRRecord
- GCC_except_table1230
- GCC_except_table1239
- GCC_except_table1367
- GCC_except_table1763
- ___block_descriptor_48_e8_32s40bs_e8_v12?0B8l
- _add_record_to_service
CStrings:
+ "!limit || ((limit - label) >= label_byte_count)"
+ "!limit || (label < limit)"
+ "!limit || (labels < limit)"
+ "Immediate cache flush for TXT record %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u"
+ "NEConfigurationManager showLocalNetworkAlertForApp scheduled handler more than once"
+ "[R%u->Q%u] Unexpected rrtype %{mdns:rrtype}d for tracker IP address reporting"
+ "[R%u] Get Tracker TLV value: %{mdns:yesno}d"
+ "mDNSResponder-3111.40.40"
- "mDNSResponder-3111.0.5.0.1"
```
