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

-3109.0.0.0.0
-  __TEXT.__text: 0x10aa28
+3111.0.5.0.1
+  __TEXT.__text: 0x10abd0
   __TEXT.__auth_stubs: 0x2fc0
   __TEXT.__objc_stubs: 0x20c0
   __TEXT.__objc_methlist: 0x694
-  __TEXT.__cstring: 0x17ab8
-  __TEXT.__const: 0x14f4
+  __TEXT.__cstring: 0x17aed
+  __TEXT.__const: 0x14bc
   __TEXT.__gcc_except_tab: 0x37c
-  __TEXT.__oslogstring: 0x210d6
+  __TEXT.__oslogstring: 0x210ca
   __TEXT.__objc_classname: 0x646
   __TEXT.__objc_methname: 0x1e32
   __TEXT.__objc_methtype: 0x64d
-  __TEXT.__unwind_info: 0x16d8
+  __TEXT.__unwind_info: 0x16e0
   __TEXT.__eh_frame: 0x7c
   __DATA_CONST.__const: 0x6238
   __DATA_CONST.__cfstring: 0x1200

   - /usr/lib/libnetworkextension.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
-  Functions: 1870
-  Symbols:   4151
-  CStrings:  4777
+  Functions: 1872
+  Symbols:   4153
+  CStrings:  4778
 
Symbols:
+ GCC_except_table1250
+ GCC_except_table1256
+ GCC_except_table1419
+ GCC_except_table1602
+ GCC_except_table1835
+ GCC_except_table487
+ _downgrade_question_awdl_inclusion
+ _mDNS_DowngradeAuthRecordAWDLInclusion_internal
+ _mDNS_StopQueryWithRemoves
+ _mdns_clock_monotonic_ns
- GCC_except_table1249
- GCC_except_table1255
- GCC_except_table1418
- GCC_except_table1601
- GCC_except_table1833
- GCC_except_table486
- _DowngradeAuthRecordAWDLInclusion
- __mdns_powerlog_get_monotonic_time_ns
CStrings:
+ "RmvAutoBrowseDomain: ignoring remove event for system-wide local domain"
+ "clock_gettime_nsec_np(CLOCK_MONOTONIC_RAW) error: %{mdns:err}d"
+ "mDNSResponder-3111.0.5.0.1"
+ "mDNS_DowngradeAuthRecordAWDLInclusion"
+ "mDNS_DowngradeServiceSetAWDLInclusion"
- "AWDLTimeoutNotificationHandler: Downgrading kDNSServiceFlagsIncludeAWDL questions and AuthRecords"
- "clock_gettime_nsec_np() returned 0: %{mdns:err}d"
- "mDNSCoreDowngradeAWDLInclusion"
- "mDNSResponder-3109"
```
