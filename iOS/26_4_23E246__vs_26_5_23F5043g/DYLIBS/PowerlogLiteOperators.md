## PowerlogLiteOperators

> `/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`

```diff

-3031.102.1.0.0
-  __TEXT.__text: 0x5776d0
-  __TEXT.__auth_stubs: 0x3010
+3031.120.21.0.0
+  __TEXT.__text: 0x577a3c
+  __TEXT.__auth_stubs: 0x3020
   __TEXT.__objc_methlist: 0x30fd4
   __TEXT.__const: 0x2908
   __TEXT.__swift5_typeref: 0x6e4
   __TEXT.__constg_swiftt: 0x534
   __TEXT.__swift5_reflstr: 0x4de
   __TEXT.__swift5_fieldmd: 0x758
-  __TEXT.__cstring: 0x88ded
+  __TEXT.__cstring: 0x88eb5
   __TEXT.__swift5_proto: 0x15c
   __TEXT.__swift5_types: 0x54
   __TEXT.__swift5_assocty: 0x30

   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift_as_entry: 0x78
   __TEXT.__swift_as_ret: 0x80
-  __TEXT.__oslogstring: 0x1383d
+  __TEXT.__oslogstring: 0x13924
   __TEXT.__swift5_mpenum: 0x10
   __TEXT.__gcc_except_tab: 0x2ce8
   __TEXT.__ustring: 0x22
   __TEXT.__unwind_info: 0x9380
   __TEXT.__eh_frame: 0x1700
   __TEXT.__objc_classname: 0x298f
-  __TEXT.__objc_methname: 0x693a0
+  __TEXT.__objc_methname: 0x693c0
   __TEXT.__objc_methtype: 0x85dc
-  __TEXT.__objc_stubs: 0x36aa0
+  __TEXT.__objc_stubs: 0x36ac0
   __DATA_CONST.__got: 0x1b78
   __DATA_CONST.__const: 0xa8f8
   __DATA_CONST.__objc_classlist: 0xa98

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x155b0
+  __DATA_CONST.__objc_selrefs: 0x155b8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xb78
   __DATA_CONST.__objc_arraydata: 0x160f0
-  __AUTH_CONST.__auth_got: 0x1820
+  __AUTH_CONST.__auth_got: 0x1828
   __AUTH_CONST.__const: 0x2778
-  __AUTH_CONST.__cfstring: 0x76300
+  __AUTH_CONST.__cfstring: 0x763e0
   __AUTH_CONST.__objc_const: 0x3bc58
   __AUTH_CONST.__objc_intobj: 0x76b0
   __AUTH_CONST.__objc_arrayobj: 0x2d78

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 9F3B404B-B696-3CD3-A388-47679B2E5B12
+  UUID: 88FE6E6A-49EC-31F8-AF3A-19D3194322A4
   Functions: 20946
-  Symbols:   55924
-  CStrings:  53760
+  Symbols:   55926
+  CStrings:  53778
 
Symbols:
+ ___36-[PLPerformanceAgent countMachPort:]_block_invoke.559
+ ___42-[PLPerformanceAgent logEventPointRollout]_block_invoke.609
+ ___48-[PLPerformanceAgent logEventPointJetsamPrority]_block_invoke.538
+ ___48-[PLPerformanceAgent logEventPointJetsamPrority]_block_invoke.544
+ ___48-[PLPerformanceAgent logEventPointJetsamPrority]_block_invoke.550
+ ___52-[PLPerformanceAgent logEventPointAPFSFragmentation]_block_invoke.570
+ ___52-[PLPerformanceAgent logEventPointAPFSFragmentation]_block_invoke.574
+ ___52-[PLPerformanceAgent logEventPointAPFSFragmentation]_block_invoke.583
+ ___66-[PLPerformanceAgent logEventPointAPFSFragmentationWithContainer:]_block_invoke.592
+ ___66-[PLPerformanceAgent logEventPointAPFSFragmentationWithContainer:]_block_invoke.598
+ ___66-[PLPerformanceAgent logEventPointAPFSFragmentationWithContainer:]_block_invoke.604
+ _fmod
+ _objc_msgSend$bucketForValue:forBucketSize:
- ___36-[PLPerformanceAgent countMachPort:]_block_invoke.541
- ___42-[PLPerformanceAgent logEventPointRollout]_block_invoke.591
- ___48-[PLPerformanceAgent logEventPointJetsamPrority]_block_invoke.520
- ___48-[PLPerformanceAgent logEventPointJetsamPrority]_block_invoke.526
- ___48-[PLPerformanceAgent logEventPointJetsamPrority]_block_invoke.532
- ___52-[PLPerformanceAgent logEventPointAPFSFragmentation]_block_invoke.552
- ___52-[PLPerformanceAgent logEventPointAPFSFragmentation]_block_invoke.556
- ___52-[PLPerformanceAgent logEventPointAPFSFragmentation]_block_invoke.565
- ___66-[PLPerformanceAgent logEventPointAPFSFragmentationWithContainer:]_block_invoke.574
- ___66-[PLPerformanceAgent logEventPointAPFSFragmentationWithContainer:]_block_invoke.580
- ___66-[PLPerformanceAgent logEventPointAPFSFragmentationWithContainer:]_block_invoke.586
Functions:
~ -[OverallMemoryUsage init] : 584 -> 600
~ -[PLPerformanceAgent logEventPointSystemMemory:] : 3368 -> 3372
~ -[PLPerformanceAgent logEventPointVMStats] : 1004 -> 1328
~ -[PLACDiagnosticsService markCandidateForTestingWithTimestamp:] : 428 -> 404
~ -[PLACDiagnosticsService handleDiagnosticsTrigger:] : 492 -> 560
~ -[PLACDiagnosticsService startPeriodicChecking] : 456 -> 580
~ -[PLACDiagnosticsService resumePeriodicCheckingIfNeeded] : 436 -> 488
~ -[PLACDiagnosticsService performAdmissionCheckWithCompletion:] : 1200 -> 1512
CStrings:
+ "Candidate missing timestamp, clearing status and not resuming periodic check"
+ "Missing candidate info. Clearing candidate status and returning."
+ "Missing marked candidate date"
+ "Missing marked candidate date. Clearing candidate status and returning."
+ "Performing admission check for candidate: %@ regsitered at %@"
+ "bucketForValue:forBucketSize:"
+ "swapins_freezer"
+ "swapouts_freezer"
+ "swapouts_scavenger"
+ "vm.compressor.swapper.swapins_freezer"
+ "vm.compressor.swapper.swapouts_freezer"
+ "vm.compressor.swapper.swapouts_scavenger"
- "Performing admission check for candidate: %@"

```
