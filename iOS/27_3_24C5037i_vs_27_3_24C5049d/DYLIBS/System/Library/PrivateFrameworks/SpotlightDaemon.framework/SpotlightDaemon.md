## SpotlightDaemon

> `/System/Library/PrivateFrameworks/SpotlightDaemon.framework/SpotlightDaemon`

```diff

-2465.2.7.101.0
-  __TEXT.__text: 0xca134
-  __TEXT.__objc_methlist: 0x4ef4
-  __TEXT.__const: 0x430
-  __TEXT.__cstring: 0xa040
-  __TEXT.__gcc_except_tab: 0x4aac
-  __TEXT.__oslogstring: 0xd7ed
+2465.2.13.0.0
+  __TEXT.__text: 0xca830
+  __TEXT.__objc_methlist: 0x4f1c
+  __TEXT.__const: 0x420
+  __TEXT.__cstring: 0xa0a5
+  __TEXT.__gcc_except_tab: 0x4b04
+  __TEXT.__oslogstring: 0xd917
   __TEXT.__dlopen_cstrs: 0xf4
-  __TEXT.__unwind_info: 0x36b0
+  __TEXT.__unwind_info: 0x36e8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3fc8
+  __DATA_CONST.__objc_selrefs: 0x3ff0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x158
   __DATA_CONST.__objc_arraydata: 0x320
   __DATA_CONST.__got: 0xc40
   __AUTH_CONST.__const: 0x1448
-  __AUTH_CONST.__cfstring: 0x8440
-  __AUTH_CONST.__objc_const: 0x6678
+  __AUTH_CONST.__cfstring: 0x8420
+  __AUTH_CONST.__objc_const: 0x66d8
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x3c0
   __AUTH_CONST.__objc_intobj: 0x228
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x1158
+  __AUTH_CONST.__auth_got: 0x1180
   __AUTH.__objc_data: 0x2d0
-  __DATA.__objc_ivar: 0x580
+  __DATA.__objc_ivar: 0x58c
   __DATA.__data: 0x410
   __DATA.__common: 0x4
   __DATA_DIRTY.__objc_data: 0xfa0

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  Functions: 3513
-  Symbols:   5273
-  CStrings:  2783
+  Functions: 3524
+  Symbols:   5294
+  CStrings:  2790
 
Symbols:
+ +[SPCoreSpotlightIndexer enableRecycleOnProcessFdLimit]
+ -[CSSearchAgent _queryContextFromXPCDictionary:searchConnection:]
+ -[SPConcreteCoreSpotlightIndexer _checkIndexDirectoryProbe:]
+ -[SPConcreteCoreSpotlightIndexer _deferOpenAfterFdShortage:openErrno:what:]
+ -[SPConcreteCoreSpotlightIndexer _inFdShortageBackoff]
+ -[SPLocalizedStringUsageReporter claimTerminalCall]
+ GCC_except_table1038
+ GCC_except_table1067
+ GCC_except_table1068
+ GCC_except_table1077
+ GCC_except_table1093
+ GCC_except_table1134
+ GCC_except_table1139
+ GCC_except_table1190
+ GCC_except_table1224
+ GCC_except_table1237
+ GCC_except_table1238
+ GCC_except_table1239
+ GCC_except_table1240
+ GCC_except_table1249
+ GCC_except_table1251
+ GCC_except_table1266
+ GCC_except_table1272
+ GCC_except_table1276
+ GCC_except_table1290
+ GCC_except_table1306
+ GCC_except_table1313
+ GCC_except_table1320
+ GCC_except_table1327
+ GCC_except_table1334
+ GCC_except_table1351
+ GCC_except_table1429
+ GCC_except_table1430
+ GCC_except_table1432
+ GCC_except_table1439
+ GCC_except_table1502
+ GCC_except_table1509
+ GCC_except_table1636
+ GCC_except_table1637
+ GCC_except_table335
+ GCC_except_table337
+ GCC_except_table348
+ GCC_except_table357
+ GCC_except_table381
+ GCC_except_table391
+ GCC_except_table405
+ GCC_except_table439
+ GCC_except_table440
+ GCC_except_table444
+ GCC_except_table467
+ GCC_except_table48
+ GCC_except_table504
+ GCC_except_table505
+ GCC_except_table52
+ GCC_except_table520
+ GCC_except_table521
+ GCC_except_table551
+ GCC_except_table56
+ GCC_except_table575
+ GCC_except_table589
+ GCC_except_table59
+ GCC_except_table592
+ GCC_except_table603
+ GCC_except_table604
+ GCC_except_table605
+ GCC_except_table63
+ GCC_except_table643
+ GCC_except_table657
+ GCC_except_table66
+ GCC_except_table669
+ GCC_except_table692
+ GCC_except_table698
+ GCC_except_table717
+ GCC_except_table718
+ GCC_except_table728
+ GCC_except_table764
+ GCC_except_table78
+ GCC_except_table789
+ GCC_except_table790
+ GCC_except_table791
+ GCC_except_table81
+ GCC_except_table818
+ GCC_except_table885
+ GCC_except_table90
+ GCC_except_table909
+ GCC_except_table935
+ GCC_except_table939
+ GCC_except_table947
+ GCC_except_table96
+ GCC_except_table970
+ GCC_except_table999
+ _OBJC_IVAR_$_SPConcreteCoreSpotlightIndexer._fdProcessLimitSinceUptimeNs
+ _OBJC_IVAR_$_SPConcreteCoreSpotlightIndexer._fdShortageUptimeNs
+ _OBJC_IVAR_$_SPLocalizedStringUsageReporter._terminalCallClaimed
+ _SPFdShortageForOpen
+ _SPFdShortageMarksNow
+ _SPLogUnattributedFdShortageOnce
+ __exit
+ _clock_gettime_nsec_np
+ _fd_resource_error_count
+ _fd_thread_resource_error_count
+ _sFdRecycleClaimed
+ _sFdRecycleEnabledUptimeNs
+ _sFdRecycleWouldHaveFiredLogged
+ _sFdUnattributedShortageLogged
+ _set_dir_stats
+ _touch_crash_state
- -[SPCoreSpotlightTask _makeFilterQueryStringForQueryContext:]
- GCC_except_table1030
- GCC_except_table1059
- GCC_except_table1060
- GCC_except_table1069
- GCC_except_table1085
- GCC_except_table1126
- GCC_except_table1131
- GCC_except_table1182
- GCC_except_table1216
- GCC_except_table1222
- GCC_except_table1223
- GCC_except_table1229
- GCC_except_table1232
- GCC_except_table1241
- GCC_except_table1243
- GCC_except_table1258
- GCC_except_table1264
- GCC_except_table1268
- GCC_except_table1282
- GCC_except_table1298
- GCC_except_table1305
- GCC_except_table1312
- GCC_except_table1319
- GCC_except_table1326
- GCC_except_table1343
- GCC_except_table1421
- GCC_except_table1422
- GCC_except_table1424
- GCC_except_table1431
- GCC_except_table1494
- GCC_except_table1501
- GCC_except_table1628
- GCC_except_table1629
- GCC_except_table332
- GCC_except_table334
- GCC_except_table344
- GCC_except_table350
- GCC_except_table374
- GCC_except_table384
- GCC_except_table398
- GCC_except_table432
- GCC_except_table433
- GCC_except_table437
- GCC_except_table460
- GCC_except_table47
- GCC_except_table497
- GCC_except_table498
- GCC_except_table51
- GCC_except_table513
- GCC_except_table514
- GCC_except_table53
- GCC_except_table544
- GCC_except_table568
- GCC_except_table57
- GCC_except_table582
- GCC_except_table585
- GCC_except_table596
- GCC_except_table597
- GCC_except_table598
- GCC_except_table60
- GCC_except_table636
- GCC_except_table64
- GCC_except_table650
- GCC_except_table662
- GCC_except_table685
- GCC_except_table691
- GCC_except_table710
- GCC_except_table711
- GCC_except_table721
- GCC_except_table757
- GCC_except_table782
- GCC_except_table783
- GCC_except_table784
- GCC_except_table80
- GCC_except_table811
- GCC_except_table82
- GCC_except_table877
- GCC_except_table88
- GCC_except_table901
- GCC_except_table923
- GCC_except_table927
- GCC_except_table95
- GCC_except_table962
- GCC_except_table98
- GCC_except_table991
CStrings:
+ "SIOpenIndexAtPathWithCallbacks"
+ "create-open of the new index"
+ "fd recycle would have fired (%{public}@, EMFILE for %llus)"
+ "index directory probe"
+ "not written"
+ "openIndex %@: %s failed for lack of file descriptors (%d); retry in %llus"
+ "openIndex %{public}@: open failed (%d) while fd shortages were counted"
+ "openIndex %{public}@: out of file descriptors (EMFILE) for %llus; exiting to recycle (crash record %{public}s)"
+ "written"
+ "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf01"
- "("
- "With filters: %@"
- "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf1"
```
