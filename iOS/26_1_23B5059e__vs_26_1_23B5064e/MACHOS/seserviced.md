## seserviced

> `/usr/libexec/seserviced`

```diff

-61.5.0.0.0
-  __TEXT.__text: 0x3e8758
+61.7.0.0.0
+  __TEXT.__text: 0x3e8c30
   __TEXT.__auth_stubs: 0x4a20
   __TEXT.__delay_stubs: 0x2c
   __TEXT.__delay_helper: 0x2c4
-  __TEXT.__objc_stubs: 0x9cc0
+  __TEXT.__objc_stubs: 0x9ce0
   __TEXT.__objc_methlist: 0x651c
   __TEXT.__const: 0xed18
-  __TEXT.__gcc_except_tab: 0x3624
-  __TEXT.__objc_methname: 0x12fa4
-  __TEXT.__oslogstring: 0x2a78c
-  __TEXT.__cstring: 0x235c4
+  __TEXT.__gcc_except_tab: 0x3694
+  __TEXT.__objc_methname: 0x12fc3
+  __TEXT.__oslogstring: 0x2a92d
+  __TEXT.__cstring: 0x23642
   __TEXT.__objc_classname: 0x11d8
-  __TEXT.__objc_methtype: 0x6673
+  __TEXT.__objc_methtype: 0x66bf
   __TEXT.__swift5_typeref: 0x4c10
   __TEXT.__constg_swiftt: 0x4d84
-  __TEXT.__swift5_reflstr: 0x54ba
-  __TEXT.__swift5_fieldmd: 0x5314
+  __TEXT.__swift5_reflstr: 0x54da
+  __TEXT.__swift5_fieldmd: 0x5320
   __TEXT.__swift5_builtin: 0x2bc
   __TEXT.__swift5_assocty: 0x6c0
   __TEXT.__swift5_capture: 0x22fc

   __DATA_CONST.__objc_arrayobj: 0x1e0
   __DATA_CONST.__objc_dictobj: 0xa0
   __DATA_CONST.__objc_intobj: 0x810
-  __DATA.__objc_const: 0x15c28
-  __DATA.__objc_selrefs: 0x4418
-  __DATA.__objc_ivar: 0xb40
+  __DATA.__objc_const: 0x15c20
+  __DATA.__objc_selrefs: 0x4428
+  __DATA.__objc_ivar: 0xb3c
   __DATA.__objc_data: 0x6330
-  __DATA.__data: 0xbd04
+  __DATA.__data: 0xbd14
   __DATA.__bss: 0xe580
   __DATA.__common: 0x700
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: BF45CC68-4442-3A7A-B6F3-BE089C6B9831
+  UUID: 1CF30FED-6E00-3444-8D06-260F8C19FEBC
   Functions: 11513
   Symbols:   2104
-  CStrings:  11873
+  CStrings:  11884
 
CStrings:
+ "%s : %i : (%@) Begin reporting endpoint statistics"
+ "%s : %i : (%@) DAS Expiration requested"
+ "%s : %i : (%@) Failed to expire task with error: %@"
+ "%s : %i : (%@) Finished reporting endpoint stats for task: %@"
+ "%s : %i : (%@) Finished reporting stats to CA"
+ "%s : %i : (%@) Handling statistics reporting for task: %@"
+ "%s : %i : (%@) Honor Defer request from system for task: %@"
+ "%s : %i : (%@) No stats to report"
+ "%s : %i : (%@) Processing ep of type: %ld"
+ "%s : %i : (%@) Received device config for ep of type: %@"
+ "%s : %i : (%@) Reporting endpoint stats for %ld endpoints"
+ "%s : %i : (%@) Reporting general statistics"
+ "%s : %i : (%@) Statistics reporting can only happen after first unlock"
+ "%s : %i : (%@) We have stats to report"
+ "+[KmlAnalyticsLogger postKmlGeneralStatisticsWithOwnerCarKeyCount:friendCarKeyCount:unifiedAccessHomeKeyCount:unifiedAccessHydraKeyCount:isProductionEnvironment:identifier:]"
+ "+[KmlEndpointManager reportEndpointStatistics:identifier:]"
+ "+[KmlEndpointManager reportEndpointStatistics:identifier:]_block_invoke"
+ "Could not retrieve SEABAAS certificate from server (%ld) : %@ %@"
+ "allHeaderFields"
+ "iOS (26.1) - SecureElementService-61.7"
+ "minDiscoveryScanRSSI"
+ "service:account:inviteDroppedForSessionID:fromID:error:"
+ "v56@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSString\"32@\"NSString\"40@\"NSError\"48"
- "%s : %i : Failed to expire task with error: %@"
- "%s : %i : Handling statistics reporting"
- "%s : %i : Honor Defer request from system"
- "%s : %i : No stats to report"
- "%s : %i : Reporting general statistics"
- "%s : %i : Statistics reporting can only happen after first unlock"
- "%s : %i : We have stats to report"
- "+[KmlAnalyticsLogger postKmlGeneralStatisticsWithOwnerCarKeyCount:friendCarKeyCount:unifiedAccessHomeKeyCount:unifiedAccessHydraKeyCount:isProductionEnvironment:]"
- "+[KmlEndpointManager reportEndpointStatistics:]"
- "Could not retrieve SEABAAS certificate from server (%ld) : %@"
- "T@\"NSManagedObjectContext\",R,N,V_context"
- "iOS (26.1) - SecureElementService-61.5"

```
