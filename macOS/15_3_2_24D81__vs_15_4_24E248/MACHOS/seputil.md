## seputil

> `/usr/libexec/seputil`

```diff

-842.60.8.0.0
-  __TEXT.__text: 0x14fb8
+850.100.14.0.0
+  __TEXT.__text: 0x12f34
   __TEXT.__auth_stubs: 0x9e0
-  __TEXT.__const: 0x448
-  __TEXT.__cstring: 0x5ac7
-  __TEXT.__oslogstring: 0x93
+  __TEXT.__cstring: 0x595c
+  __TEXT.__const: 0x440
+  __TEXT.__oslogstring: 0x5e
   __TEXT.__gcc_except_tab: 0x264
-  __TEXT.__unwind_info: 0x438
+  __TEXT.__unwind_info: 0x430
   __DATA_CONST.__auth_got: 0x4f8
   __DATA_CONST.__got: 0xc0
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x98
+  __DATA_CONST.__const: 0x80
   __DATA_CONST.__cfstring: 0x60
-  __DATA.__data: 0x920
-  __DATA.__bss: 0x8b8
+  __DATA.__data: 0x940
+  __DATA.__bss: 0x8f0
   __DATA.__common: 0x4
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libz.1.dylib
-  UUID: D7EC270F-12FE-3465-BF58-A8A4A4E6F6F6
-  Functions: 405
+  UUID: A4DBB8EE-C65E-36CB-AAE3-83BAA000C404
+  Functions: 428
   Symbols:   188
   CStrings:  656
 
CStrings:
+ "%s called with slot %u\n"
+ "%s: Bad hash hex string (%d)\n"
+ "%s: Missing hash\n"
+ "%s: bad arguments: %u %lu\n"
+ "%s: commit hash failed: 0x%x\n"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/libembeddedtest/Framework/Source/filesystem.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/libembeddedtest/Framework/Source/info_pair.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/libembeddedtest/Framework/Source/issue.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/libembeddedtest/Framework/Source/issue_aggregate.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/libembeddedtest/Framework/Source/json.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/libembeddedtest/Framework/Source/results.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/libembeddedtest/Framework/Source/serialization.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/libembeddedtest/Framework/Source/test_case.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/libembeddedtest/Framework/Source/test_case_metric.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/libembeddedtest/Framework/Source/test_case_result.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/libembeddedtest/Framework/Source/test_case_statistic.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/libembeddedtest/Framework/Source/test_case_statistic_bucket.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/libembeddedtest/Framework/Source/test_case_statistic_metric.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/libembeddedtest/Framework/Source/test_suite.c"
+ "/AppleInternal/Library/BuildRoots/656826c2-0194-11f0-9fc9-122ba06eff56/Library/Caches/com.apple.xbs/Sources/AppleSEPUtil/libsep_testing/src/sep_testing.c"
+ "commitApHash"
+ "commitSepHash"
+ "hash"
- "%s called with slot %u, for_ap %u\n"
- "-"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleSEPUtil/libsep_testing/src/sep_testing.c"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleSEPUtil/seputil/seputil.c"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleSEPUtil/seputil/shared_support.c"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleSEPUtil/seputil/tbm.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/libembeddedtest/Framework/Source/filesystem.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/libembeddedtest/Framework/Source/info_pair.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/libembeddedtest/Framework/Source/issue.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/libembeddedtest/Framework/Source/issue_aggregate.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/libembeddedtest/Framework/Source/json.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/libembeddedtest/Framework/Source/results.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/libembeddedtest/Framework/Source/serialization.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/libembeddedtest/Framework/Source/test_case.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/libembeddedtest/Framework/Source/test_case_metric.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/libembeddedtest/Framework/Source/test_case_result.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/libembeddedtest/Framework/Source/test_case_statistic.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/libembeddedtest/Framework/Source/test_case_statistic_bucket.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/libembeddedtest/Framework/Source/test_case_statistic_metric.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/libembeddedtest/Framework/Source/test_suite.c"
- "AssertMacros:(value = 0x%lx), %s file: %s, line: %d\n"
- "sepCommitHash"

```
