## SafetyMonitor

> `/System/Library/PrivateFrameworks/SafetyMonitor.framework/SafetyMonitor`

```diff

-891.0.1.0.0
-  __TEXT.__text: 0x5836c
+893.0.5.0.2
+  __TEXT.__text: 0x58350
   __TEXT.__auth_stubs: 0x11e0
   __TEXT.__objc_methlist: 0x3550
   __TEXT.__const: 0xe70
-  __TEXT.__cstring: 0x6e64
+  __TEXT.__cstring: 0x6edc
   __TEXT.__swift5_typeref: 0x441
   __TEXT.__swift5_capture: 0xf4
   __TEXT.__constg_swiftt: 0x358

   __TEXT.__swift5_assocty: 0x48
   __TEXT.__swift5_proto: 0xb0
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__oslogstring: 0x31e0
-  __TEXT.__ustring: 0x818
+  __TEXT.__oslogstring: 0x3230
+  __TEXT.__ustring: 0x8c4
   __TEXT.__gcc_except_tab: 0x7d4
   __TEXT.__dlopen_cstrs: 0xa0
-  __TEXT.__unwind_info: 0x1ce8
+  __TEXT.__unwind_info: 0x1cec
   __TEXT.__eh_frame: 0x9c8
   __TEXT.__objc_classname: 0x7d7
-  __TEXT.__objc_methname: 0x9788
+  __TEXT.__objc_methname: 0x978c
   __TEXT.__objc_methtype: 0x170b
   __TEXT.__objc_stubs: 0x4900
   __DATA_CONST.__got: 0x148
-  __DATA_CONST.__const: 0x1090
+  __DATA_CONST.__const: 0x10a0
   __DATA_CONST.__objc_classlist: 0x200
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xf0

   __DATA_CONST.__objc_selrefs: 0x1a30
   __AUTH_CONST.__const: 0x7c8
   __AUTH_CONST.__objc_const: 0x1c58
-  __AUTH_CONST.__cfstring: 0x4140
+  __AUTH_CONST.__cfstring: 0x41c0
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__auth_got: 0x900
   __AUTH.__objc_data: 0x1008

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 3468741F-11C8-317C-8B9E-1F65CCDF788C
+  UUID: E91DB5BC-4EF2-38E1-998E-C82025ADD218
   Functions: 1748
   Symbols:   4600
-  CStrings:  3095
+  CStrings:  3103
 
Symbols:
+ -[SMSessionConfiguration isSameSession:]
+ ___101-[SMEligibilityChecker resolveEndpointsForDestinations:service:requiredCapabilities:completionBlock:]_block_invoke.59
+ ____RTSemaphoreWait_block_invoke
+ ___block_descriptor_72_e8_32s40s48s56bs_e34_v24?0"NSDictionary"8"NSError"16ls56l8s32l8s40l8s48l8
- -[SMSessionConfiguration isSimilar:]
- ___101-[SMEligibilityChecker resolveEndpointsForDestinations:service:requiredCapabilities:completionBlock:]_block_invoke_3
- ___RTSemaphoreWait_block_invoke
- ___block_descriptor_48_e8_32s40bs_e34_v24?0"NSDictionary"8"NSError"16ls40l8s32l8
CStrings:
+ " will be notified when\u00a0you\u00a0arrive."
+ " will be notified when\u00a0you\u00a0arrive.\nYour ETA is "
+ "%@, destinations, %@, service, %@, capabilities, %@, numResults, %ld, error, %@"
+ "GeneralRuleContactBlocked"
+ "GeneralRuleContactNotExists"
+ "L"
+ "SUGGESTION_NOTIFICATION_BODY_FALLBACK"
+ "isSameSession:"
- " will be notified when you arrive.\nYour ETA is "
- "Let them know when you arrive at %@"
- "isSimilar:"

```
