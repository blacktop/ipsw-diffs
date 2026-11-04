## mDNSResponder

> `/usr/sbin/mDNSResponder`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__cstring`
- `__TEXT.__const`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-3111.40.45.0.0
-  __TEXT.__text: 0x10a5f0
+3111.60.12.0.0
+  __TEXT.__text: 0x10a8d0
   __TEXT.__auth_stubs: 0x2fc0
   __TEXT.__objc_stubs: 0x20c0
   __TEXT.__objc_methlist: 0x694
   __TEXT.__cstring: 0x17b50
   __TEXT.__const: 0x14f4
   __TEXT.__gcc_except_tab: 0x3a8
-  __TEXT.__oslogstring: 0x212b6
+  __TEXT.__oslogstring: 0x2129e
   __TEXT.__objc_classname: 0x646
   __TEXT.__objc_methname: 0x1e32
   __TEXT.__objc_methtype: 0x64d
-  __TEXT.__unwind_info: 0x1dc8
+  __TEXT.__unwind_info: 0x1dd8
   __TEXT.__eh_frame: 0x7c
   __DATA_CONST.__const: 0x6238
   __DATA_CONST.__cfstring: 0x1200

   - /usr/lib/libnetworkextension.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
-  Functions: 1876
-  Symbols:   4130
+  Functions: 1879
+  Symbols:   4133
   CStrings:  4787
 
Symbols:
+ GCC_except_table1125
+ GCC_except_table1256
+ GCC_except_table1262
+ GCC_except_table1425
+ GCC_except_table1608
+ GCC_except_table1841
+ GCC_except_table492
+ _AddOrUpdateTSRForCacheGroup
+ _NegativeResponseHistoryFind
+ _mDNSGetLiveTSRForCacheGroup
- GCC_except_table1122
- GCC_except_table1253
- GCC_except_table1259
- GCC_except_table1422
- GCC_except_table1605
- GCC_except_table1838
- GCC_except_table489
CStrings:
+ "Purging orphaned cached TSR -- %{sensitive}s %{mdns:s_hash}u"
+ "mDNSResponder-3111.60.12"
- "Purging cached TSR record that matches orphaned TSR -- %{sensitive}s %{mdns:s_hash}u"
- "mDNSResponder-3111.40.45"
```
