## DeviceManagement

> `/System/Library/PrivateFrameworks/DeviceManagement.framework/DeviceManagement`

```diff

-171.0.0.0.0
-  __TEXT.__text: 0x380a8
+183.0.0.0.0
+  __TEXT.__text: 0x38180
   __TEXT.__auth_stubs: 0x610
-  __TEXT.__objc_methlist: 0x6be4
+  __TEXT.__objc_methlist: 0x6bfc
   __TEXT.__const: 0x68
-  __TEXT.__cstring: 0x4fcf
+  __TEXT.__cstring: 0x500a
   __TEXT.__gcc_except_tab: 0x24c
   __TEXT.__oslogstring: 0x1043
   __TEXT.__ustring: 0xb64
   __TEXT.__unwind_info: 0xe4c
   __TEXT.__objc_classname: 0x16fb
-  __TEXT.__objc_methname: 0x9ce7
+  __TEXT.__objc_methname: 0x9d69
   __TEXT.__objc_methtype: 0xaf1
-  __TEXT.__objc_stubs: 0x4f00
+  __TEXT.__objc_stubs: 0x4f40
   __DATA_CONST.__got: 0x70
-  __DATA_CONST.__const: 0xf48
+  __DATA_CONST.__const: 0xf58
   __DATA_CONST.__objc_classlist: 0x5f0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xa688
-  __DATA_CONST.__objc_selrefs: 0x1d40
+  __DATA_CONST.__objc_const: 0xa6b8
+  __DATA_CONST.__objc_selrefs: 0x1d50
+  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__objc_classrefs: 0x318
+  __DATA_CONST.__objc_superrefs: 0x4a8
   __DATA_CONST.__objc_arraydata: 0x670
-  __AUTH_CONST.__objc_intobj: 0x14b8
+  __AUTH_CONST.__objc_intobj: 0x14e8
   __AUTH_CONST.__objc_arrayobj: 0x828
-  __AUTH_CONST.__cfstring: 0x72e0
+  __AUTH_CONST.__cfstring: 0x7320
   __AUTH_CONST.__objc_const: 0x5960
   __AUTH_CONST.__const: 0x440
   __AUTH_CONST.__auth_got: 0x318
   __AUTH.__objc_data: 0x3480
-  __DATA.__objc_protorefs: 0x18
-  __DATA.__objc_classrefs: 0x318
-  __DATA.__objc_superrefs: 0x4a8
-  __DATA.__objc_ivar: 0x884
+  __DATA.__objc_ivar: 0x888
   __DATA.__data: 0x430
   __DATA.__bss: 0x118
   __DATA_DIRTY.__objc_data: 0x6e0

   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 486D44E3-7EC5-3791-89BE-8956C9A1B0BE
-  Functions: 2224
-  Symbols:   7830
-  CStrings:  3992
+  UUID: 302E3D2E-5792-38E6-9CB0-E6856F1E0D87
+  Functions: 2226
+  Symbols:   7839
+  CStrings:  4001
 
Symbols:
+ -[DMFApp distributorIdentifier]
+ -[DMFApp setDistributorIdentifier:]
+ _DMFAppRatingAllApps
+ _DMFAppRatingUnrated
+ _OBJC_IVAR_$_DMFApp._distributorIdentifier
+ ___54-[DMFPolicyMonitor requestPoliciesForTypes:withError:]_block_invoke.117
+ ___54-[DMFPolicyMonitor requestPoliciesForTypes:withError:]_block_invoke.117.cold.1
+ ___56-[DMFEmergencyModeMonitor emergencyModeStatusWithError:]_block_invoke.65
+ ___56-[DMFEmergencyModeMonitor emergencyModeStatusWithError:]_block_invoke.65.cold.1
+ ___56-[DMFEmergencyModeMonitor enableEmergencyModeWithError:]_block_invoke.62
+ ___56-[DMFEmergencyModeMonitor enableEmergencyModeWithError:]_block_invoke.62.cold.1
+ ___57-[DMFEmergencyModeMonitor disableEmergencyModeWithError:]_block_invoke.64
+ ___57-[DMFEmergencyModeMonitor disableEmergencyModeWithError:]_block_invoke.64.cold.1
+ ___62-[DMFPolicyMonitor requestPoliciesForTypes:completionHandler:]_block_invoke.112
+ ___62-[DMFPolicyMonitor requestPoliciesForTypes:completionHandler:]_block_invoke.112.cold.1
+ ___62-[DMFPolicyMonitor requestPoliciesForTypes:completionHandler:]_block_invoke.116
+ ___68-[DMFEmergencyModeMonitor emergencyModeStatusWithCompletionHandler:]_block_invoke.67
+ ___68-[DMFEmergencyModeMonitor emergencyModeStatusWithCompletionHandler:]_block_invoke.67.cold.1
+ ___68-[DMFEmergencyModeMonitor enableEmergencyModeForDuration:withError:]_block_invoke.63
+ ___68-[DMFEmergencyModeMonitor enableEmergencyModeForDuration:withError:]_block_invoke.63.cold.1
+ ___81-[DMFPolicyMonitor addRegistration:forPolicyMonitorIdentifier:completionHandler:]_block_invoke.107.cold.1
+ ___81-[DMFPolicyMonitor addRegistration:forPolicyMonitorIdentifier:completionHandler:]_block_invoke.107.cold.2
+ ___81-[DMFPolicyMonitor addRegistration:forPolicyMonitorIdentifier:completionHandler:]_block_invoke.108
+ ___81-[DMFPolicyMonitor addRegistration:forPolicyMonitorIdentifier:completionHandler:]_block_invoke.111
+ _objc_msgSend$distributorIdentifier
+ _objc_msgSend$setDistributorIdentifier:
- ___54-[DMFPolicyMonitor requestPoliciesForTypes:withError:]_block_invoke.116
- ___54-[DMFPolicyMonitor requestPoliciesForTypes:withError:]_block_invoke.116.cold.1
- ___56-[DMFEmergencyModeMonitor emergencyModeStatusWithError:]_block_invoke.64
- ___56-[DMFEmergencyModeMonitor emergencyModeStatusWithError:]_block_invoke.64.cold.1
- ___56-[DMFEmergencyModeMonitor enableEmergencyModeWithError:]_block_invoke.61
- ___56-[DMFEmergencyModeMonitor enableEmergencyModeWithError:]_block_invoke.61.cold.1
- ___57-[DMFEmergencyModeMonitor disableEmergencyModeWithError:]_block_invoke.63
- ___57-[DMFEmergencyModeMonitor disableEmergencyModeWithError:]_block_invoke.63.cold.1
- ___62-[DMFPolicyMonitor requestPoliciesForTypes:completionHandler:]_block_invoke.111
- ___62-[DMFPolicyMonitor requestPoliciesForTypes:completionHandler:]_block_invoke.111.cold.1
- ___62-[DMFPolicyMonitor requestPoliciesForTypes:completionHandler:]_block_invoke.115
- ___68-[DMFEmergencyModeMonitor emergencyModeStatusWithCompletionHandler:]_block_invoke.66
- ___68-[DMFEmergencyModeMonitor emergencyModeStatusWithCompletionHandler:]_block_invoke.66.cold.1
- ___68-[DMFEmergencyModeMonitor enableEmergencyModeForDuration:withError:]_block_invoke.62
- ___68-[DMFEmergencyModeMonitor enableEmergencyModeForDuration:withError:]_block_invoke.62.cold.1
- ___81-[DMFPolicyMonitor addRegistration:forPolicyMonitorIdentifier:completionHandler:]_block_invoke.106
- ___81-[DMFPolicyMonitor addRegistration:forPolicyMonitorIdentifier:completionHandler:]_block_invoke.106.cold.1
- ___81-[DMFPolicyMonitor addRegistration:forPolicyMonitorIdentifier:completionHandler:]_block_invoke.106.cold.2
- ___81-[DMFPolicyMonitor addRegistration:forPolicyMonitorIdentifier:completionHandler:]_block_invoke.110
CStrings:
+ ";\x1d"
+ "Distributor Identifier         : %@\n"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",C,N,V_distributorIdentifier"
+ "_distributorIdentifier"
+ "distributorIdentifier"
+ "setDistributorIdentifier:"
- ":\x1d"

```
