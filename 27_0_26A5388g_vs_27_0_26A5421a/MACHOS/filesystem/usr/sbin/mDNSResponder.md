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
-  __TEXT.__text: 0x107284
+3111.0.5.0.1
+  __TEXT.__text: 0x10742c
   __TEXT.__auth_stubs: 0x3000
   __TEXT.__objc_stubs: 0xf00
   __TEXT.__objc_methlist: 0x2a4
-  __TEXT.__const: 0x15dc
-  __TEXT.__cstring: 0x18a7f
+  __TEXT.__const: 0x15e4
+  __TEXT.__cstring: 0x18ab4
   __TEXT.__gcc_except_tab: 0x3d0
-  __TEXT.__oslogstring: 0x1fef8
+  __TEXT.__oslogstring: 0x1feec
   __TEXT.__objc_classname: 0x5fe
   __TEXT.__objc_methname: 0xe47
   __TEXT.__objc_methtype: 0x4ea
-  __TEXT.__unwind_info: 0x1618
+  __TEXT.__unwind_info: 0x1620
   __TEXT.__eh_frame: 0x7c
   __DATA_CONST.__const: 0x62d0
   __DATA_CONST.__cfstring: 0x1260

   - /usr/lib/libnetworkextension.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
-  Functions: 1800
-  Symbols:   3849
-  CStrings:  4568
+  Functions: 1802
+  Symbols:   3851
+  CStrings:  4569
 
Symbols:
+ GCC_except_table1230
+ GCC_except_table1239
+ GCC_except_table1367
+ GCC_except_table1763
+ GCC_except_table500
+ _downgrade_question_awdl_inclusion
+ _mDNS_DowngradeAuthRecordAWDLInclusion_internal
+ _mDNS_StopQueryWithRemoves
+ _mdns_clock_monotonic_ns
- GCC_except_table1229
- GCC_except_table1238
- GCC_except_table1366
- GCC_except_table1761
- GCC_except_table499
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
