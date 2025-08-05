## CoreTelephony

> `/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`

```diff

-13085.1.0.0.0
-  __TEXT.__text: 0x18ed8c
+13090.3.0.0.0
+  __TEXT.__text: 0x18f068
   __TEXT.__auth_stubs: 0x1990
-  __TEXT.__objc_methlist: 0x1b42c
+  __TEXT.__objc_methlist: 0x1b464
   __TEXT.__const: 0x1002
-  __TEXT.__gcc_except_tab: 0x1df1c
-  __TEXT.__cstring: 0x1f84a
+  __TEXT.__gcc_except_tab: 0x1df98
+  __TEXT.__cstring: 0x1f851
   __TEXT.__oslogstring: 0x43e5
   __TEXT.__swift5_typeref: 0x17
-  __TEXT.__unwind_info: 0xd1d0
-  __TEXT.__objc_classname: 0x5928
-  __TEXT.__objc_methname: 0x22c57
+  __TEXT.__unwind_info: 0xd1f8
+  __TEXT.__objc_classname: 0x592f
+  __TEXT.__objc_methname: 0x22ca1
   __TEXT.__objc_methtype: 0x72e4
-  __TEXT.__objc_stubs: 0x16d00
+  __TEXT.__objc_stubs: 0x16d40
   __DATA_CONST.__got: 0xb00
   __DATA_CONST.__const: 0x7398
   __DATA_CONST.__objc_classlist: 0x1530
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x250
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x77e8
+  __DATA_CONST.__objc_selrefs: 0x77f8
   __DATA_CONST.__objc_protorefs: 0x48
-  __DATA_CONST.__objc_superrefs: 0x17a0
+  __DATA_CONST.__objc_superrefs: 0x17b0
   __DATA_CONST.__objc_arraydata: 0x20
   __AUTH_CONST.__auth_got: 0xce0
   __AUTH_CONST.__const: 0x2080

   __AUTH_CONST.__objc_const: 0x2f928
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0xa960
+  __AUTH.__objc_data: 0xaa50
   __DATA.__objc_ivar: 0x1438
   __DATA.__data: 0x1f88
   __DATA.__bss: 0x198
   __DATA.__common: 0x10
-  __DATA_DIRTY.__objc_data: 0x2a80
+  __DATA_DIRTY.__objc_data: 0x2990
   __DATA_DIRTY.__data: 0x90
   __DATA_DIRTY.__bss: 0x1329
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  UUID: 1931F820-D819-3C7C-8DE3-812BD558DAAC
-  Functions: 11282
-  Symbols:   38269
-  CStrings:  17131
+  UUID: 71DEA278-D71D-3B01-81FD-FA2F7072973F
+  Functions: 11284
+  Symbols:   38281
+  CStrings:  17133
 
Symbols:
+ +[CTXPCIsAnyPlanTransferableFromThisDeviceForFlowRequest allowedClassesForArguments]
+ -[CTXPCIsAnyPlanTransferableFromThisDeviceForFlowRequest ct_shortName]
+ -[CTXPCIsAnyPlanTransferableFromThisDeviceForFlowRequest flowType]
+ -[CTXPCIsAnyPlanTransferableFromThisDeviceForFlowRequest initWithFlowType:]
+ -[CTXPCIsAnyPlanTransferableFromThisDeviceForFlowRequest performRequestWithHandler:completionHandler:]
+ -[CTXPCIsAnyPlanTransferableFromThisDeviceForFlowRequest requiredEntitlement]
+ -[CoreTelephonyClient(PlanTransfer) isAnyPlanTransferableFromThisDeviceForFlow:OrError:]
+ GCC_except_table446
+ GCC_except_table458
+ GCC_except_table465
+ GCC_except_table473
+ GCC_except_table477
+ GCC_except_table488
+ GCC_except_table508
+ GCC_except_table523
+ GCC_except_table527
+ GCC_except_table531
+ GCC_except_table538
+ GCC_except_table545
+ GCC_except_table560
+ GCC_except_table572
+ GCC_except_table576
+ GCC_except_table578
+ GCC_except_table584
+ GCC_except_table588
+ GCC_except_table599
+ GCC_except_table606
+ GCC_except_table618
+ GCC_except_table622
+ GCC_except_table629
+ GCC_except_table640
+ GCC_except_table651
+ GCC_except_table665
+ GCC_except_table673
+ GCC_except_table674
+ GCC_except_table675
+ _OBJC_CLASS_$_CTXPCIsAnyPlanTransferableFromThisDeviceForFlowRequest
+ _OBJC_METACLASS_$_CTXPCIsAnyPlanTransferableFromThisDeviceForFlowRequest
+ __OBJC_$_CLASS_METHODS_CTXPCIsAnyPlanTransferableFromThisDeviceForFlowRequest
+ __OBJC_$_INSTANCE_METHODS_CTXPCIsAnyPlanTransferableFromThisDeviceForFlowRequest
+ __OBJC_CLASS_RO_$_CTXPCIsAnyPlanTransferableFromThisDeviceForFlowRequest
+ __OBJC_METACLASS_RO_$_CTXPCIsAnyPlanTransferableFromThisDeviceForFlowRequest
+ ___102-[CTXPCIsAnyPlanTransferableFromThisDeviceForFlowRequest performRequestWithHandler:completionHandler:]_block_invoke
+ ___88-[CoreTelephonyClient(PlanTransfer) isAnyPlanTransferableFromThisDeviceForFlow:OrError:]_block_invoke
+ ___88-[CoreTelephonyClient(PlanTransfer) isAnyPlanTransferableFromThisDeviceForFlow:OrError:]_block_invoke_2
+ _objc_msgSend$initWithFlowType:
+ _objc_msgSend$isAnyPlanTransferableFromThisDeviceForFlow:OrError:
+ _objc_msgSend$isAnyPlanTransferableFromThisDeviceForFlow:completion:
- -[CTXPCIsAnyPlanTransferableFromThisDeviceRequest ct_shortName]
- -[CTXPCIsAnyPlanTransferableFromThisDeviceRequest performRequestWithHandler:completionHandler:]
- -[CTXPCIsAnyPlanTransferableFromThisDeviceRequest requiredEntitlement]
- GCC_except_table475
- GCC_except_table476
- GCC_except_table487
- GCC_except_table500
- GCC_except_table525
- GCC_except_table526
- GCC_except_table530
- GCC_except_table537
- GCC_except_table547
- GCC_except_table562
- GCC_except_table570
- GCC_except_table574
- GCC_except_table575
- GCC_except_table587
- GCC_except_table598
- GCC_except_table602
- GCC_except_table617
- GCC_except_table621
- GCC_except_table638
- GCC_except_table639
- GCC_except_table664
- _OBJC_CLASS_$_CTXPCIsAnyPlanTransferableFromThisDeviceRequest
- _OBJC_METACLASS_$_CTXPCIsAnyPlanTransferableFromThisDeviceRequest
- __OBJC_$_INSTANCE_METHODS_CTXPCIsAnyPlanTransferableFromThisDeviceRequest
- __OBJC_CLASS_RO_$_CTXPCIsAnyPlanTransferableFromThisDeviceRequest
- __OBJC_METACLASS_RO_$_CTXPCIsAnyPlanTransferableFromThisDeviceRequest
- __ZN14CSIPhoneNumber14setMMIValidityE11MMIValidity
- __ZNK14CSIPhoneNumber14getMMIValidityEv
- ___80-[CoreTelephonyClient(PlanTransfer) isAnyPlanTransferableFromThisDeviceOrError:]_block_invoke
- ___80-[CoreTelephonyClient(PlanTransfer) isAnyPlanTransferableFromThisDeviceOrError:]_block_invoke_2
- ___95-[CTXPCIsAnyPlanTransferableFromThisDeviceRequest performRequestWithHandler:completionHandler:]_block_invoke
- _objc_msgSend$isAnyPlanTransferableFromThisDeviceWithCompletion:
CStrings:
+ "13090.3"
+ "13090.3~67"
+ "CTXPCIsAnyPlanTransferableFromThisDeviceForFlowRequest"
+ "IsAnyPlanTransferableFromThisDeviceForFlowRequest"
+ "initWithFlowType:"
+ "isAnyPlanTransferableFromThisDeviceForFlow:OrError:"
+ "isAnyPlanTransferableFromThisDeviceForFlow:completion:"
- "13085.1"
- "13085.1~24"
- "CTXPCIsAnyPlanTransferableFromThisDeviceRequest"
- "IsAnyPlanTransferableFromThisDeviceRequest"
- "isAnyPlanTransferableFromThisDeviceWithCompletion:"

```
