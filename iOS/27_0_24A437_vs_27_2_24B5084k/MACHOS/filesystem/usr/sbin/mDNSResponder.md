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
-  __TEXT.__text: 0x109a68
+3111.40.40.0.0
+  __TEXT.__text: 0x10a200
   __TEXT.__auth_stubs: 0x2fc0
   __TEXT.__objc_stubs: 0x20c0
   __TEXT.__objc_methlist: 0x694
-  __TEXT.__cstring: 0x17aed
-  __TEXT.__const: 0x14bc
-  __TEXT.__gcc_except_tab: 0x37c
-  __TEXT.__oslogstring: 0x210ca
+  __TEXT.__cstring: 0x17b50
+  __TEXT.__const: 0x14f4
+  __TEXT.__gcc_except_tab: 0x3a8
+  __TEXT.__oslogstring: 0x211f9
   __TEXT.__objc_classname: 0x646
   __TEXT.__objc_methname: 0x1e32
   __TEXT.__objc_methtype: 0x64d
-  __TEXT.__unwind_info: 0x1db0
+  __TEXT.__unwind_info: 0x1dc0
   __TEXT.__eh_frame: 0x7c
   __DATA_CONST.__const: 0x6238
   __DATA_CONST.__cfstring: 0x1200

   - /usr/lib/libnetworkextension.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
-  Functions: 1872
-  Symbols:   4153
-  CStrings:  4778
+  Functions: 1874
+  Symbols:   4156
+  CStrings:  4785
 
Symbols:
+ GCC_except_table1120
+ GCC_except_table1251
+ GCC_except_table1257
+ GCC_except_table1420
+ GCC_except_table1603
+ GCC_except_table1836
+ ___block_descriptor_56_e8_32s40bs48r_e8_v12?0B8ls32l8r48l8s40l8
+ __resolved_cache_update_tracking
+ _domain_name_labels_length_with_limit
+ _regRecordAddTSRRecord
- GCC_except_table1250
- GCC_except_table1256
- GCC_except_table1419
- GCC_except_table1602
- GCC_except_table1835
- ___block_descriptor_48_e8_32s40bs_e8_v12?0B8ls32l8s40l8
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
