## seputil

> `/usr/libexec/seputil`

```diff

-880.80.7.0.0
-  __TEXT.__text: 0x15ea0
-  __TEXT.__auth_stubs: 0xa40
-  __TEXT.__cstring: 0x5f0a
-  __TEXT.__const: 0xc0c
+880.100.23.0.0
+  __TEXT.__text: 0x15a38
+  __TEXT.__auth_stubs: 0xa80
+  __TEXT.__cstring: 0x6364
+  __TEXT.__const: 0xc34
   __TEXT.__oslogstring: 0x6f
-  __TEXT.__gcc_except_tab: 0x274
-  __TEXT.__unwind_info: 0x4a8
-  __DATA_CONST.__auth_got: 0x528
+  __TEXT.__gcc_except_tab: 0x2a8
+  __TEXT.__unwind_info: 0x4d8
+  __DATA_CONST.__auth_got: 0x548
   __DATA_CONST.__got: 0xd0
   __DATA_CONST.__auth_ptr: 0x18
   __DATA_CONST.__const: 0x180
-  __DATA_CONST.__cfstring: 0x80
-  __DATA.__data: 0xc60
+  __DATA_CONST.__cfstring: 0x100
+  __DATA.__data: 0xc80
   __DATA.__common: 0xc
   __DATA.__bss: 0x8f5
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libz.1.dylib
-  UUID: D9FA614A-6552-3068-BBEF-291A14C2AC97
-  Functions: 472
-  Symbols:   196
-  CStrings:  734
+  UUID: 196CB791-2BA0-3104-A960-A6487D9363C3
+  Functions: 498
+  Symbols:   200
+  CStrings:  745
 
Symbols:
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE9__grow_byEmmmmmm
+ _mmap
+ _munmap
CStrings:
+ "\t\t--check-boot-size <file> Compares the TZ/AR sizes in the provided img4 file to the values given by iBoot"
+ "/"
+ "/Library/Caches/com.apple.xbs/2A6F5B5F-6464-498E-9316-93AC1A5EDB11/TemporaryDirectory.neQDDE/Sources/libembeddedtest/Framework/Source/filesystem.c"
+ "/Library/Caches/com.apple.xbs/2A6F5B5F-6464-498E-9316-93AC1A5EDB11/TemporaryDirectory.neQDDE/Sources/libembeddedtest/Framework/Source/info_pair.c"
+ "/Library/Caches/com.apple.xbs/2A6F5B5F-6464-498E-9316-93AC1A5EDB11/TemporaryDirectory.neQDDE/Sources/libembeddedtest/Framework/Source/issue.c"
+ "/Library/Caches/com.apple.xbs/2A6F5B5F-6464-498E-9316-93AC1A5EDB11/TemporaryDirectory.neQDDE/Sources/libembeddedtest/Framework/Source/issue_aggregate.c"
+ "/Library/Caches/com.apple.xbs/2A6F5B5F-6464-498E-9316-93AC1A5EDB11/TemporaryDirectory.neQDDE/Sources/libembeddedtest/Framework/Source/json.c"
+ "/Library/Caches/com.apple.xbs/2A6F5B5F-6464-498E-9316-93AC1A5EDB11/TemporaryDirectory.neQDDE/Sources/libembeddedtest/Framework/Source/results.c"
+ "/Library/Caches/com.apple.xbs/2A6F5B5F-6464-498E-9316-93AC1A5EDB11/TemporaryDirectory.neQDDE/Sources/libembeddedtest/Framework/Source/serialization.c"
+ "/Library/Caches/com.apple.xbs/2A6F5B5F-6464-498E-9316-93AC1A5EDB11/TemporaryDirectory.neQDDE/Sources/libembeddedtest/Framework/Source/test_case.c"
+ "/Library/Caches/com.apple.xbs/2A6F5B5F-6464-498E-9316-93AC1A5EDB11/TemporaryDirectory.neQDDE/Sources/libembeddedtest/Framework/Source/test_case_metric.c"
+ "/Library/Caches/com.apple.xbs/2A6F5B5F-6464-498E-9316-93AC1A5EDB11/TemporaryDirectory.neQDDE/Sources/libembeddedtest/Framework/Source/test_case_result.c"
+ "/Library/Caches/com.apple.xbs/2A6F5B5F-6464-498E-9316-93AC1A5EDB11/TemporaryDirectory.neQDDE/Sources/libembeddedtest/Framework/Source/test_case_statistic.c"
+ "/Library/Caches/com.apple.xbs/2A6F5B5F-6464-498E-9316-93AC1A5EDB11/TemporaryDirectory.neQDDE/Sources/libembeddedtest/Framework/Source/test_case_statistic_bucket.c"
+ "/Library/Caches/com.apple.xbs/2A6F5B5F-6464-498E-9316-93AC1A5EDB11/TemporaryDirectory.neQDDE/Sources/libembeddedtest/Framework/Source/test_case_statistic_metric.c"
+ "/Library/Caches/com.apple.xbs/2A6F5B5F-6464-498E-9316-93AC1A5EDB11/TemporaryDirectory.neQDDE/Sources/libembeddedtest/Framework/Source/test_suite.c"
+ "/Library/Caches/com.apple.xbs/60F04B94-09E1-48E3-AB29-2A822DC5AFDC/TemporaryDirectory.KTHady/Sources/AppleSEPUtil/libsep_testing/src/sep_testing.c"
+ "IODeviceTree:/arm-io/sep/iop-sep-nub"
+ "Sources/AppleSEPManager"
+ "ar0-size"
+ "ar1-size"
+ "check-boot-size"
+ "tz0-size"
+ "tz1-size"
- "%s: invalid argument passed to %s\n"
- "/Library/Caches/com.apple.xbs/Sources/AppleSEPUtil/libsep_testing/src/sep_testing.c"
- "/Library/Caches/com.apple.xbs/Sources/libembeddedtest/Framework/Source/filesystem.c"
- "/Library/Caches/com.apple.xbs/Sources/libembeddedtest/Framework/Source/info_pair.c"
- "/Library/Caches/com.apple.xbs/Sources/libembeddedtest/Framework/Source/issue.c"
- "/Library/Caches/com.apple.xbs/Sources/libembeddedtest/Framework/Source/issue_aggregate.c"
- "/Library/Caches/com.apple.xbs/Sources/libembeddedtest/Framework/Source/json.c"
- "/Library/Caches/com.apple.xbs/Sources/libembeddedtest/Framework/Source/results.c"
- "/Library/Caches/com.apple.xbs/Sources/libembeddedtest/Framework/Source/serialization.c"
- "/Library/Caches/com.apple.xbs/Sources/libembeddedtest/Framework/Source/test_case.c"
- "/Library/Caches/com.apple.xbs/Sources/libembeddedtest/Framework/Source/test_case_metric.c"
- "/Library/Caches/com.apple.xbs/Sources/libembeddedtest/Framework/Source/test_case_result.c"
- "/Library/Caches/com.apple.xbs/Sources/libembeddedtest/Framework/Source/test_case_statistic.c"
- "/Library/Caches/com.apple.xbs/Sources/libembeddedtest/Framework/Source/test_case_statistic_bucket.c"
- "/Library/Caches/com.apple.xbs/Sources/libembeddedtest/Framework/Source/test_case_statistic_metric.c"
- "/Library/Caches/com.apple.xbs/Sources/libembeddedtest/Framework/Source/test_suite.c"
- "get_firmware_path"

```
