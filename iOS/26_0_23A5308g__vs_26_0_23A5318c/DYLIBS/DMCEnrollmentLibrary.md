## DMCEnrollmentLibrary

> `/System/Library/PrivateFrameworks/DMCEnrollmentLibrary.framework/DMCEnrollmentLibrary`

```diff

-50.0.0.0.0
-  __TEXT.__text: 0x294e0
+52.0.0.0.0
+  __TEXT.__text: 0x2968c
   __TEXT.__auth_stubs: 0x580
   __TEXT.__objc_methlist: 0x1aac
   __TEXT.__const: 0xf0
-  __TEXT.__oslogstring: 0x3cdd
-  __TEXT.__cstring: 0x234a
-  __TEXT.__gcc_except_tab: 0x938
+  __TEXT.__oslogstring: 0x3d62
+  __TEXT.__cstring: 0x235d
+  __TEXT.__gcc_except_tab: 0x94c
   __TEXT.__dlopen_cstrs: 0xae
   __TEXT.__unwind_info: 0x8d0
   __TEXT.__objc_classname: 0x21c
-  __TEXT.__objc_methname: 0x8557
-  __TEXT.__objc_methtype: 0x95d
+  __TEXT.__objc_methname: 0x8569
+  __TEXT.__objc_methtype: 0x971
   __TEXT.__objc_stubs: 0x6280
   __DATA_CONST.__got: 0x488
   __DATA_CONST.__const: 0x1258

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 059C07E0-2728-3A73-9251-34A54EF4FD08
+  UUID: 2675A634-BFF9-316E-8ABA-AA402511EB80
   Functions: 774
   Symbols:   3002
-  CStrings:  1911
+  CStrings:  1914
 
Symbols:
+ -[DMCEnrollmentFlowController _fetchEnrollmentProfileFromWebURL:machineInfo:anchorCertificateRefs:isReturnToService:]
+ ___117-[DMCEnrollmentFlowController _fetchEnrollmentProfileFromWebURL:machineInfo:anchorCertificateRefs:isReturnToService:]_block_invoke
+ ___117-[DMCEnrollmentFlowController _fetchEnrollmentProfileFromWebURL:machineInfo:anchorCertificateRefs:isReturnToService:]_block_invoke_2
+ _objc_msgSend$_fetchEnrollmentProfileFromWebURL:machineInfo:anchorCertificateRefs:isReturnToService:
- -[DMCEnrollmentFlowController _fetchEnrollmentProfileFromWebURL:machineInfo:anchorCertificateRefs:]
- ___99-[DMCEnrollmentFlowController _fetchEnrollmentProfileFromWebURL:machineInfo:anchorCertificateRefs:]_block_invoke
- ___99-[DMCEnrollmentFlowController _fetchEnrollmentProfileFromWebURL:machineInfo:anchorCertificateRefs:]_block_invoke_2
- _objc_msgSend$_fetchEnrollmentProfileFromWebURL:machineInfo:anchorCertificateRefs:
Functions:
~ -[DMCEnrollmentFlowController _workerQueue_performFlowStep:] : 4768 -> 4780
~ -[DMCEnrollmentFlowController _analyzeCloudConfig:enrollmentType:isDoingReturnToService:obliterationShelter:] : 1876 -> 1912
~ -[DMCEnrollmentFlowController _fetchEnrollmentProfileFromWebURL:machineInfo:anchorCertificateRefs:] -> -[DMCEnrollmentFlowController _fetchEnrollmentProfileFromWebURL:machineInfo:anchorCertificateRefs:isReturnToService:] : 288 -> 480
~ -[DMCServiceDiscoveryHelper discoverServerForUserIdentifier:anchorCertificateRefs:completionHandler:] : 964 -> 888
~ -[DMCServiceDiscoveryHelper _discoverServerURLForDomain:port:userIdentifier:anchorCertificateRefs:completionHandler:] : 528 -> 608
~ -[DMCServiceDiscoveryHelper _discoverServerURLForUserIdentifier:anchorCertificateRefs:completionHandler:] : 608 -> 680
~ -[DMCServiceDiscoveryHelper _discoverAppleServerWithUserIdentifier:anchorCertificateRefs:completionHandler:] : 260 -> 372
CStrings:
+ "-[DMCEnrollmentFlowController _fetchEnrollmentProfileFromWebURL:machineInfo:anchorCertificateRefs:isReturnToService:]_block_invoke_2"
+ "DMC_ENROLLMENT_UPDATE_FROM_FACTORY_VERSION_REQUIRED"
+ "Discovering Apple server with user identifier: %{public}@"
+ "Discovering servers with domain: %{public}@"
+ "Discovering servers with user identifier: %{public}@"
+ "_fetchEnrollmentProfileFromWebURL:machineInfo:anchorCertificateRefs:isReturnToService:"
+ "v44@0:8@16@24@32B40"
- "-[DMCEnrollmentFlowController _fetchEnrollmentProfileFromWebURL:machineInfo:anchorCertificateRefs:]_block_invoke_2"
- "DMC_ENROLLMENT_UPDATE_FROM_FACTORY_VERION_REQUIRED"
- "Domain is: %{public}@"
- "_fetchEnrollmentProfileFromWebURL:machineInfo:anchorCertificateRefs:"

```
