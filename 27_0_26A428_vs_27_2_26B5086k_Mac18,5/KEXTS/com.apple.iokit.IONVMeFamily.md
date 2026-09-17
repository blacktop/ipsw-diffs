## com.apple.iokit.IONVMeFamily

> `com.apple.iokit.IONVMeFamily`

```diff

-877.0.7.0.0
-  __TEXT.__cstring: 0x109cd
+877.40.5.0.0
+  __TEXT.__cstring: 0x10a34
   __TEXT.__const: 0x740
-  __TEXT_EXEC.__text: 0x5d684
+  __TEXT_EXEC.__text: 0x5c478
   __TEXT_EXEC.__auth_stubs: 0xe10
   __DATA.__data: 0x46c
   __DATA.__common: 0x578

   __DATA_CONST.__kalloc_var: 0x690
   __DATA_CONST.__auth_got: 0x708
   __DATA_CONST.__got: 0x188
-  Functions: 3597
-  Symbols:   3279
-  CStrings:  1763
+  Functions: 3564
+  Symbols:   3276
+  CStrings:  1767
 
Symbols:
+ _ZN16IONVMeController19CheckSanitizeStatusEb
+ __ZN16IONVMeController19CheckSanitizeStatusEb
+ __ZN16IONVMeController24SanitizeStatusTimerFiredEP18IOTimerEventSource
+ __ZZN16IONVMeController16ReleaseResourcesEvE21kalloc_type_view_1815
+ __ZZN16IONVMeController17AllocateResourcesEvE21kalloc_type_view_1717
+ __ZZN16IONVMeController17AllocateResourcesEvE21kalloc_type_view_1782
+ __ZZN16IONVMeController22CreateCompletionQueuesEvE21kalloc_type_view_3762
+ __ZZN16IONVMeController22CreateCompletionQueuesEvE21kalloc_type_view_3788
+ __ZZN16IONVMeController22CreateSubmissionQueuesEvE21kalloc_type_view_3472
+ __ZZN16IONVMeController22CreateSubmissionQueuesEvE21kalloc_type_view_3497
+ __ZZN16IONVMeController22DeleteCompletionQueuesEvE21kalloc_type_view_3817
+ __ZZN16IONVMeController22DeleteSubmissionQueuesEvE21kalloc_type_view_3526
+ __ZZN27AppleEmbeddedNVMeController4freeEvE21kalloc_type_view_3424
- _ZN16IONVMeController19CheckSanitizeStatusEv
- _ZN24IONVMeBlockStorageDevice16GetFieldCountersEP18IOMemoryDescriptorj
- _ZN24IONVMeBlockStorageDevice17GetSystemCountersEP18IOMemoryDescriptorPjj
- _ZN24IONVMeBlockStorageDevice20GetAlgorithmCountersEP18IOMemoryDescriptorPjj
- __ZN16IONVMeController19CheckSanitizeStatusEv
- __ZN16IONVMeController19CheckSanitizeStatusEv_vfpthunk_
- __ZZN16IONVMeController16ReleaseResourcesEvE21kalloc_type_view_1810
- __ZZN16IONVMeController17AllocateResourcesEvE21kalloc_type_view_1712
- __ZZN16IONVMeController17AllocateResourcesEvE21kalloc_type_view_1777
- __ZZN16IONVMeController22CreateCompletionQueuesEvE21kalloc_type_view_3729
- __ZZN16IONVMeController22CreateCompletionQueuesEvE21kalloc_type_view_3755
- __ZZN16IONVMeController22CreateSubmissionQueuesEvE21kalloc_type_view_3439
- __ZZN16IONVMeController22CreateSubmissionQueuesEvE21kalloc_type_view_3464
- __ZZN16IONVMeController22DeleteCompletionQueuesEvE21kalloc_type_view_3784
- __ZZN16IONVMeController22DeleteSubmissionQueuesEvE21kalloc_type_view_3493
- __ZZN27AppleEmbeddedNVMeController4freeEvE21kalloc_type_view_3422
CStrings:
+ "Sanitize Status Bytes Read"
+ "Sanitize Status Bytes Written"
+ "Sanitize Status End Time"
+ "Sanitize Status SSTAT"
+ "Sanitize Status Start Time"
- "fSanitizeInProgress == true"
```
