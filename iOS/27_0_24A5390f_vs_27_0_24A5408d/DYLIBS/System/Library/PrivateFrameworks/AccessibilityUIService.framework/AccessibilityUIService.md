## AccessibilityUIService

> `/System/Library/PrivateFrameworks/AccessibilityUIService.framework/AccessibilityUIService`

```diff

-3237.1.0.0.0
-  __TEXT.__text: 0x1f380
+3240.3.0.0.0
+  __TEXT.__text: 0x1f61c
   __TEXT.__objc_methlist: 0x1c14
-  __TEXT.__const: 0x850
+  __TEXT.__const: 0x858
   __TEXT.__constg_swiftt: 0x184
   __TEXT.__swift5_typeref: 0x1d7
   __TEXT.__swift5_fieldmd: 0x120
   __TEXT.__cstring: 0x152e
   __TEXT.__swift5_types: 0x24
   __TEXT.__swift5_capture: 0x44
-  __TEXT.__oslogstring: 0x13c4
+  __TEXT.__oslogstring: 0x16eb
   __TEXT.__swift5_reflstr: 0xb5
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_proto: 0x48

   __TEXT.__swift_as_ret: 0x10
   __TEXT.__swift_as_cont: 0x20
   __TEXT.__gcc_except_tab: 0x488
-  __TEXT.__unwind_info: 0x8b0
+  __TEXT.__unwind_info: 0x8a0
   __TEXT.__eh_frame: 0x408
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/BoardServices.framework/BoardServices
   - /System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard
+  - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /System/Library/PrivateFrameworks/TouchAccommodations.framework/TouchAccommodations

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 740
-  Symbols:   2134
-  CStrings:  216
+  Symbols:   2135
+  CStrings:  220
 
Symbols:
+ ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
+ _objc_msgSend$connectedScenes
- ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
Functions:
~ -[AXUIServiceManager _extractAndHandleRegistration:clientIdentifier:messageIdentifier:context:error:] : 352 -> 476
~ -[AXUIServiceEntitlementChecker serviceCanProcessMessageWithIdentifier:fromClientWithConnection:possibleRequiredEntitlements:needsToRequireEntitlements:] : 1156 -> 1184
~ -[AXUIDisplayManager _sceneIsAttachable:] : 52 -> 140
~ -[AXUIDisplayManager _removeContentViewController:forService:completion:] : 468 -> 488
~ ___73-[AXUIDisplayManager _removeContentViewController:forService:completion:]_block_invoke : 836 -> 896
~ -[AXUIAssertionManager invalidateAssertionIfNeeded] : 140 -> 252
~ ___51-[AXUIAssertionManager invalidateAssertionIfNeeded]_block_invoke : 256 -> 348
~ -[AXUIAssertionManager invalidateAssertionUIIfNeeded] : 140 -> 252
~ ___53-[AXUIAssertionManager invalidateAssertionUIIfNeeded]_block_invoke : 392 -> 424
CStrings:
+ "Can't invalidate Background Assertion, %lu services are still registered: %@. This timer is not automatically rescheduled — invalidation will not be retried until the next call to acquireAssertionIfNeeded/invalidateAssertionIfNeeded."
+ "Can't invalidate UI Assertion, still clients with UI assertion %@. This timer is not automatically rescheduled — invalidation will not be retried until the next call to acquireAssertionUIIfNeeded/invalidateAssertionUIIfNeeded."
+ "First registration for client %@ serviceBundleName=%@, triggered by message identifier %lu from pid %d"
+ "_removeContentViewController for service %@: isLastVCInWindow=%d requestedSceneDestruction=%d (if NO, the scene for this service's content view controller remains alive)"
+ "invalidateAssertionIfNeeded scheduling timer, current assertionBackground: %@"
+ "invalidateAssertionIfNeeded timer fired, assertionBackground: %@"
+ "invalidateAssertionUIIfNeeded scheduling timer, current assertionUI: %@"
+ "invalidateAssertionUIIfNeeded timer fired, assertionUI: %@"
- "Can't invalidate Background Assertion, still services are registered"
- "Can't invalidate UI Assertion, still clients with UI assertion %@"
- "invalidateAssertionIfNeeded timer"
- "invalidateAssertionUIIfNeeded timer"
```
