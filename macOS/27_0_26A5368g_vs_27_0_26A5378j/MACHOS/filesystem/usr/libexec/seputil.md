## seputil

> `/usr/libexec/seputil`

```diff

-  __TEXT.__text: 0x13d84
+  __TEXT.__text: 0x13d88
   __TEXT.__auth_stubs: 0xa30
   __TEXT.__cstring: 0x5f15
   __TEXT.__const: 0x560
Sections:
~ __TEXT.__cstring : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA.__data : content changed
Functions:
~ sub_100001a34 : 9152 -> 9144
~ sub_10000406c -> sub_100004064 : 276 -> 268
~ sub_100008608 -> sub_1000085f8 : 388 -> 372
~ sub_100008864 -> sub_100008844 : 404 -> 400
~ sub_10000ba5c -> sub_10000ba38 : 216 -> 236
~ sub_10000e8a8 -> sub_10000e898 : 324 -> 336
~ sub_100012874 -> sub_100012870 : 1464 -> 1472
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.F2Y2Vn/Sources/AppleSEPUtil/libsep_testing/src/sep_testing.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.TXByz3/Sources/libembeddedtest/Framework/Source/filesystem.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.TXByz3/Sources/libembeddedtest/Framework/Source/info_pair.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.TXByz3/Sources/libembeddedtest/Framework/Source/issue.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.TXByz3/Sources/libembeddedtest/Framework/Source/issue_aggregate.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.TXByz3/Sources/libembeddedtest/Framework/Source/json.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.TXByz3/Sources/libembeddedtest/Framework/Source/results.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.TXByz3/Sources/libembeddedtest/Framework/Source/serialization.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.TXByz3/Sources/libembeddedtest/Framework/Source/test_case.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.TXByz3/Sources/libembeddedtest/Framework/Source/test_case_metric.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.TXByz3/Sources/libembeddedtest/Framework/Source/test_case_result.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.TXByz3/Sources/libembeddedtest/Framework/Source/test_case_statistic.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.TXByz3/Sources/libembeddedtest/Framework/Source/test_case_statistic_bucket.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.TXByz3/Sources/libembeddedtest/Framework/Source/test_case_statistic_metric.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.TXByz3/Sources/libembeddedtest/Framework/Source/test_suite.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EahZtq/Sources/AppleSEPUtil/libsep_testing/src/sep_testing.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xADniv/Sources/libembeddedtest/Framework/Source/filesystem.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xADniv/Sources/libembeddedtest/Framework/Source/info_pair.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xADniv/Sources/libembeddedtest/Framework/Source/issue.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xADniv/Sources/libembeddedtest/Framework/Source/issue_aggregate.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xADniv/Sources/libembeddedtest/Framework/Source/json.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xADniv/Sources/libembeddedtest/Framework/Source/results.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xADniv/Sources/libembeddedtest/Framework/Source/serialization.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xADniv/Sources/libembeddedtest/Framework/Source/test_case.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xADniv/Sources/libembeddedtest/Framework/Source/test_case_metric.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xADniv/Sources/libembeddedtest/Framework/Source/test_case_result.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xADniv/Sources/libembeddedtest/Framework/Source/test_case_statistic.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xADniv/Sources/libembeddedtest/Framework/Source/test_case_statistic_bucket.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xADniv/Sources/libembeddedtest/Framework/Source/test_case_statistic_metric.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xADniv/Sources/libembeddedtest/Framework/Source/test_suite.c"

```
