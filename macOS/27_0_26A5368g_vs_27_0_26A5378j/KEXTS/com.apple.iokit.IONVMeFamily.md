## com.apple.iokit.IONVMeFamily

> `com.apple.iokit.IONVMeFamily`

```diff

-  __TEXT.__cstring: 0x1082c
+  __TEXT.__cstring: 0x109cd
   __TEXT.__const: 0x740
-  __TEXT_EXEC.__text: 0x5df14
+  __TEXT_EXEC.__text: 0x5e660
   __TEXT_EXEC.__auth_stubs: 0xe00
   __DATA.__data: 0x46c
   __DATA.__common: 0x578
   __DATA.__bss: 0x10
   __DATA_CONST.__mod_init_func: 0x110
   __DATA_CONST.__mod_term_func: 0x110
-  __DATA_CONST.__const: 0x15670
+  __DATA_CONST.__const: 0x156e0
   __DATA_CONST.__kalloc_type: 0x840
   __DATA_CONST.__kalloc_var: 0x690
   __DATA_CONST.__auth_got: 0x700
   __DATA_CONST.__got: 0x188
-  Functions: 3587
-  Symbols:   4724
-  CStrings:  1752
+  Functions: 3597
+  Symbols:   4733
+  CStrings:  1763
 
Sections:
~ __DATA.__data : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__mod_term_func : content changed
~ __DATA_CONST.__kalloc_type : content changed
~ __DATA_CONST.__kalloc_var : content changed
~ __DATA_CONST.__auth_got : content changed
~ __DATA_CONST.__got : content changed
Symbols:
+ _ZN23AppleANS2NVMeController19GetSanitizeCountersEv
+ _ZN23AppleANS2NVMeController21ParseSanitizeCountersEPh
+ __ZN23AppleANS2NVMeController19GetSanitizeCountersEv
+ __ZN23AppleANS2NVMeController21ParseSanitizeCountersEPh
+ __ZN27AppleEmbeddedNVMeController19GetSanitizeCountersEv
+ __ZN27AppleEmbeddedNVMeController21ParseSanitizeCountersEPh
+ __ZZN16IONVMeController16ReleaseResourcesEvE21kalloc_type_view_1789
+ __ZZN16IONVMeController17AllocateResourcesEvE21kalloc_type_view_1691
+ __ZZN16IONVMeController17AllocateResourcesEvE21kalloc_type_view_1756
+ __ZZN16IONVMeController22CreateCompletionQueuesEvE21kalloc_type_view_3708
+ __ZZN16IONVMeController22CreateCompletionQueuesEvE21kalloc_type_view_3734
+ __ZZN16IONVMeController22CreateSubmissionQueuesEvE21kalloc_type_view_3418
+ __ZZN16IONVMeController22CreateSubmissionQueuesEvE21kalloc_type_view_3443
+ __ZZN16IONVMeController22DeleteCompletionQueuesEvE21kalloc_type_view_3763
+ __ZZN16IONVMeController22DeleteSubmissionQueuesEvE21kalloc_type_view_3472
+ __ZZN24IONVMeBlockStorageDevice11QueueCreateEjE21kalloc_type_view_2048
+ __ZZN24IONVMeBlockStorageDevice11QueueDeleteEvE21kalloc_type_view_2081
+ __ZZN27AppleEmbeddedNVMeController19SetNamespacesStructEvE20kalloc_type_view_171
+ __ZZN27AppleEmbeddedNVMeController4freeEvE21kalloc_type_view_3422
- __ZZN16IONVMeController16ReleaseResourcesEvE21kalloc_type_view_1770
- __ZZN16IONVMeController17AllocateResourcesEvE21kalloc_type_view_1672
- __ZZN16IONVMeController17AllocateResourcesEvE21kalloc_type_view_1737
- __ZZN16IONVMeController22CreateCompletionQueuesEvE21kalloc_type_view_3689
- __ZZN16IONVMeController22CreateCompletionQueuesEvE21kalloc_type_view_3715
- __ZZN16IONVMeController22CreateSubmissionQueuesEvE21kalloc_type_view_3399
- __ZZN16IONVMeController22CreateSubmissionQueuesEvE21kalloc_type_view_3424
- __ZZN16IONVMeController22DeleteCompletionQueuesEvE21kalloc_type_view_3744
- __ZZN16IONVMeController22DeleteSubmissionQueuesEvE21kalloc_type_view_3453
- __ZZN24IONVMeBlockStorageDevice11QueueCreateEjE21kalloc_type_view_2046
- __ZZN24IONVMeBlockStorageDevice11QueueDeleteEvE21kalloc_type_view_2079
- __ZZN27AppleEmbeddedNVMeController19SetNamespacesStructEvE20kalloc_type_view_170
- __ZZN27AppleEmbeddedNVMeController4freeEvE21kalloc_type_view_3410
CStrings:
+ "%s::%d:fCompletionLoops: %d\n"
+ "%s::%d:nvme: CORE_DEBUG_EXPORT_STATS failed with status 0x%x\n"
+ "%s::%d:nvme: ParseSanitizeCounters: maxElements < elements\n"
+ "%s::%d:nvme: Sanitize counter keyNum: %u value: 0x%016llx\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QcoIek/Sources/IONVMeFamily/Common/AppleNVMeBuffer.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QcoIek/Sources/IONVMeFamily/Common/AppleNVMeController.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QcoIek/Sources/IONVMeFamily/Common/AppleNVMeRequest.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QcoIek/Sources/IONVMeFamily/Common/AppleNVMeRequestPool.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QcoIek/Sources/IONVMeFamily/Common/AppleNVMeRequestPoolTagReserve.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QcoIek/Sources/IONVMeFamily/Common/AppleNVMeRequestTimer.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QcoIek/Sources/IONVMeFamily/Common/AppleNVMeSMARTUserClient.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QcoIek/Sources/IONVMeFamily/Common/AppleNVMeUserClient.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QcoIek/Sources/IONVMeFamily/Common/AppleNVMeWorkLoop.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QcoIek/Sources/IONVMeFamily/Common/IONVMeBlockStorageDevice.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QcoIek/Sources/IONVMeFamily/Common/IONVMeController.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QcoIek/Sources/IONVMeFamily/Common/IONVMeControllerPolledAdapter.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QcoIek/Sources/IONVMeFamily/Embedded/AppleANS2CGNVMeController.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QcoIek/Sources/IONVMeFamily/Embedded/AppleANS2CGv2Controller.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QcoIek/Sources/IONVMeFamily/Embedded/AppleANS2DARTNVMeController.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QcoIek/Sources/IONVMeFamily/Embedded/AppleANS2NVMeController.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QcoIek/Sources/IONVMeFamily/Embedded/AppleANS3CGv2Controller.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QcoIek/Sources/IONVMeFamily/Embedded/AppleANS3NVMeController.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QcoIek/Sources/IONVMeFamily/Embedded/AppleEmbeddedNVMeController.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QcoIek/Sources/IONVMeFamily/Embedded/AppleEmbeddedNVMeDiagnostics.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QcoIek/Sources/IONVMeFamily/Embedded/AppleEmbeddedNVMeNVRAM.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QcoIek/Sources/IONVMeFamily/Embedded/AppleEmbeddedNVMeTemperatureSensor.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QcoIek/Sources/IONVMeFamily/Embedded/AppleNVMeEAN.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QcoIek/Sources/IONVMeFamily/Embedded/AppleNVMeEANUC.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QcoIek/Sources/IONVMeFamily/Embedded/AppleNVMeFWNamespaceDevice.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QcoIek/Sources/IONVMeFamily/Embedded/AppleNVMeFWNamespaceUC.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QcoIek/Sources/IONVMeFamily/Embedded/AppleNVMeNamespaceDevice.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QcoIek/Sources/IONVMeFamily/Embedded/AppleNVMeNamespaceUC.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QcoIek/Sources/IONVMeFamily/Embedded/AppleNVMeUpdateUC.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QcoIek/Sources/IONVMeFamily/Embedded/IOEmbeddedNVMeBlockDevice.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QcoIek/Sources/IONVMeFamily/Embedded/IONVMeEffaceableDevice.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QcoIek/Sources/IONVMeFamily/Embedded/IONVMeLifeboatBlockDevice.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QcoIek/Sources/IONVMeFamily/Embedded/NVMeSEPNotifier.cpp"
+ "SanitizeDone"
+ "SanitizeFailed"
+ "SanitizeStart"
+ "nvme-completion-loops"
+ "sanitize-counters"
+ "virtual IOReturn AppleANS2NVMeController::GetSanitizeCounters()"
+ "virtual bool IONVMeController::InitializeController()"
+ "virtual void AppleANS2NVMeController::ParseSanitizeCounters(uint8_t *)"
- "( inNumDwords <= NVMeFieldMax ( kNVMeGetLogPageNumDwordsLen ) )"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ATdboR/Sources/IONVMeFamily/Common/AppleNVMeBuffer.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ATdboR/Sources/IONVMeFamily/Common/AppleNVMeController.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ATdboR/Sources/IONVMeFamily/Common/AppleNVMeRequest.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ATdboR/Sources/IONVMeFamily/Common/AppleNVMeRequestPool.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ATdboR/Sources/IONVMeFamily/Common/AppleNVMeRequestPoolTagReserve.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ATdboR/Sources/IONVMeFamily/Common/AppleNVMeRequestTimer.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ATdboR/Sources/IONVMeFamily/Common/AppleNVMeSMARTUserClient.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ATdboR/Sources/IONVMeFamily/Common/AppleNVMeUserClient.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ATdboR/Sources/IONVMeFamily/Common/AppleNVMeWorkLoop.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ATdboR/Sources/IONVMeFamily/Common/IONVMeBlockStorageDevice.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ATdboR/Sources/IONVMeFamily/Common/IONVMeController.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ATdboR/Sources/IONVMeFamily/Common/IONVMeControllerPolledAdapter.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ATdboR/Sources/IONVMeFamily/Embedded/AppleANS2CGNVMeController.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ATdboR/Sources/IONVMeFamily/Embedded/AppleANS2CGv2Controller.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ATdboR/Sources/IONVMeFamily/Embedded/AppleANS2DARTNVMeController.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ATdboR/Sources/IONVMeFamily/Embedded/AppleANS2NVMeController.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ATdboR/Sources/IONVMeFamily/Embedded/AppleANS3CGv2Controller.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ATdboR/Sources/IONVMeFamily/Embedded/AppleANS3NVMeController.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ATdboR/Sources/IONVMeFamily/Embedded/AppleEmbeddedNVMeController.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ATdboR/Sources/IONVMeFamily/Embedded/AppleEmbeddedNVMeDiagnostics.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ATdboR/Sources/IONVMeFamily/Embedded/AppleEmbeddedNVMeNVRAM.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ATdboR/Sources/IONVMeFamily/Embedded/AppleEmbeddedNVMeTemperatureSensor.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ATdboR/Sources/IONVMeFamily/Embedded/AppleNVMeEAN.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ATdboR/Sources/IONVMeFamily/Embedded/AppleNVMeEANUC.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ATdboR/Sources/IONVMeFamily/Embedded/AppleNVMeFWNamespaceDevice.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ATdboR/Sources/IONVMeFamily/Embedded/AppleNVMeFWNamespaceUC.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ATdboR/Sources/IONVMeFamily/Embedded/AppleNVMeNamespaceDevice.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ATdboR/Sources/IONVMeFamily/Embedded/AppleNVMeNamespaceUC.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ATdboR/Sources/IONVMeFamily/Embedded/AppleNVMeUpdateUC.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ATdboR/Sources/IONVMeFamily/Embedded/IOEmbeddedNVMeBlockDevice.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ATdboR/Sources/IONVMeFamily/Embedded/IONVMeEffaceableDevice.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ATdboR/Sources/IONVMeFamily/Embedded/IONVMeLifeboatBlockDevice.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ATdboR/Sources/IONVMeFamily/Embedded/NVMeSEPNotifier.cpp"

```
