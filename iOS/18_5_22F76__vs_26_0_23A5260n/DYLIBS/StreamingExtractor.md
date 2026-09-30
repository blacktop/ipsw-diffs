## StreamingExtractor

> `/System/Library/PrivateFrameworks/StreamingExtractor.framework/StreamingExtractor`

```diff

-35.0.0.0.0
-  __TEXT.__text: 0xa828
-  __TEXT.__auth_stubs: 0x510
-  __TEXT.__objc_methlist: 0x6bc
+43.0.0.0.1
+  __TEXT.__text: 0xae04
+  __TEXT.__auth_stubs: 0x540
+  __TEXT.__objc_methlist: 0x74c
   __TEXT.__const: 0xd0
-  __TEXT.__cstring: 0x1428
-  __TEXT.__oslogstring: 0xc5e
+  __TEXT.__cstring: 0x1652
+  __TEXT.__oslogstring: 0xc9e
   __TEXT.__gcc_except_tab: 0x3b0
-  __TEXT.__unwind_info: 0x310
-  __TEXT.__objc_classname: 0xca
-  __TEXT.__objc_methname: 0x138d
-  __TEXT.__objc_methtype: 0x46b
-  __TEXT.__objc_stubs: 0xd80
-  __DATA_CONST.__got: 0xa0
-  __DATA_CONST.__const: 0x3c8
-  __DATA_CONST.__objc_classlist: 0x18
+  __TEXT.__unwind_info: 0x328
+  __TEXT.__objc_classname: 0xe2
+  __TEXT.__objc_methname: 0x1484
+  __TEXT.__objc_methtype: 0x498
+  __TEXT.__objc_stubs: 0xe40
+  __DATA_CONST.__got: 0xa8
+  __DATA_CONST.__const: 0x410
+  __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x518
+  __DATA_CONST.__objc_selrefs: 0x560
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x298
+  __DATA_CONST.__objc_superrefs: 0x18
+  __AUTH_CONST.__auth_got: 0x2b0
   __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__cfstring: 0x660
-  __AUTH_CONST.__objc_const: 0x938
-  __DATA.__objc_ivar: 0x58
+  __AUTH_CONST.__cfstring: 0x7a0
+  __AUTH_CONST.__objc_const: 0xa38
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0x60
   __DATA.__data: 0x2a8
   __DATA_DIRTY.__objc_data: 0xf0
   __DATA_DIRTY.__data: 0x88

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 36FBED20-12A0-3D76-AE50-CCDF2A8C94F1
-  Functions: 254
-  Symbols:   884
-  CStrings:  517
+  UUID: D50B54CE-7743-332B-8CB8-7EDB34A7C73F
+  Functions: 265
+  Symbols:   928
+  CStrings:  557
 
Symbols:
+ +[STReservableSpacePolicy __setErrorForPtr:code:]
+ +[STReservableSpacePolicy processPolicyWithErrorPtr:]
+ +[STReservableSpacePolicy threadPolicyWithErrorPtr:]
+ -[STRemoteExtractor setUsesReserveAccessPolicy:]
+ -[STRemoteExtractor usesReserveAccessPolicy]
+ -[STReservableSpacePolicy dealloc]
+ -[STReservableSpacePolicy initWithPolicyType:errorPtr:]
+ -[STReservableSpacePolicy invalidate]
+ -[STReservableSpacePolicy invalidate].cold.1
+ -[STReservableSpacePolicy policyType]
+ -[STReservableSpacePolicy setPolicyType:]
+ GCC_except_table101
+ GCC_except_table125
+ GCC_except_table130
+ GCC_except_table133
+ GCC_except_table134
+ GCC_except_table138
+ GCC_except_table139
+ GCC_except_table172
+ GCC_except_table173
+ GCC_except_table29
+ GCC_except_table39
+ _OBJC_CLASS_$_STReservableSpacePolicy
+ _OBJC_IVAR_$_STReservableSpacePolicy._invalidated
+ _OBJC_IVAR_$_STReservableSpacePolicy._policyType
+ _OBJC_METACLASS_$_STReservableSpacePolicy
+ _STRemoteExtractorEntitlement
+ _STRemoteExtractorOptionsUsesReservePolicy
+ _STReservableSpacePolicyErrorDomain
+ __OBJC_$_CLASS_METHODS_STReservableSpacePolicy
+ __OBJC_$_INSTANCE_METHODS_STReservableSpacePolicy
+ __OBJC_$_INSTANCE_VARIABLES_STReservableSpacePolicy
+ __OBJC_$_PROP_LIST_STReservableSpacePolicy
+ __OBJC_CLASS_RO_$_STReservableSpacePolicy
+ __OBJC_METACLASS_RO_$_STReservableSpacePolicy
+ _getiopolicy_np
+ _objc_autorelease
+ _objc_msgSend$__setErrorForPtr:code:
+ _objc_msgSend$debugDescription
+ _objc_msgSend$initWithPolicyType:errorPtr:
+ _objc_msgSend$numberWithBool:
+ _objc_msgSend$policyType
+ _objc_msgSend$setUsesReserveAccessPolicy:
+ _setiopolicy_np
- GCC_except_table123
- GCC_except_table124
- GCC_except_table127
- GCC_except_table132
- GCC_except_table136
- GCC_except_table137
- GCC_except_table170
- GCC_except_table171
- GCC_except_table27
- GCC_except_table37
- GCC_except_table99
CStrings:
+ "%{public}s: Invalidating the reservable space policy failed: %@"
+ "-[STReservableSpacePolicy invalidate]"
+ "<nil>"
+ "@24@0:8^@16"
+ "@32@0:8Q16^@24"
+ "A per-process policy for reservable space access is already enabled."
+ "A per-thread policy for reservable space access is already enabled."
+ "AB"
+ "Failed to set the reserve access policy for the current process."
+ "Failed to set the reserve access policy for the current thread."
+ "Getting the reserve access policy for the current process failed."
+ "Getting the reserve access policy for the current thread failed."
+ "STRemoteExtractorOptionsUsesReservePolicy"
+ "STReservableSpacePolicy"
+ "STReservableSpacePolicyErrorDomain"
+ "TB,N"
+ "TQ,N,V_policyType"
+ "__setErrorForPtr:code:"
+ "_invalidated"
+ "_policyType"
+ "com.apple.private.STRemoteExtractor"
+ "initWithPolicyType:errorPtr:"
+ "numberWithBool:"
+ "policyType"
+ "processPolicyWithErrorPtr:"
+ "setPolicyType:"
+ "setUsesReserveAccessPolicy:"
+ "threadPolicyWithErrorPtr:"
+ "usesReserveAccessPolicy"
+ "v32@0:8^@16Q24"

```
