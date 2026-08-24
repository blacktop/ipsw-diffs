## AccessibilityUIService

> `/System/Library/PrivateFrameworks/AccessibilityUIService.framework/Versions/A/AccessibilityUIService`

```diff

-3237.0.0.0.0
-  __TEXT.__text: 0xbe80
+3240.0.1.2.0
+  __TEXT.__text: 0xc09c
   __TEXT.__objc_methlist: 0x89c
   __TEXT.__swift5_typeref: 0x52
-  __TEXT.__const: 0x1e0
+  __TEXT.__const: 0x1f0
   __TEXT.__cstring: 0xa92
   __TEXT.__constg_swiftt: 0x68
   __TEXT.__swift5_reflstr: 0x5f

   __TEXT.__swift_as_entry: 0x8
   __TEXT.__swift_as_cont: 0x8
   __TEXT.__gcc_except_tab: 0x2a4
-  __TEXT.__oslogstring: 0xa0f
-  __TEXT.__unwind_info: 0x378
+  __TEXT.__oslogstring: 0xc8c
+  __TEXT.__unwind_info: 0x370
   __TEXT.__eh_frame: 0x100
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 261
-  Symbols:   766
-  CStrings:  101
+  Symbols:   767
+  CStrings:  104
 
Symbols:
+ _objc_msgSend$_services
Functions:
~ -[AXUIServiceManager _extractAndHandleRegistration:clientIdentifier:messageIdentifier:context:error:] : 388 -> 516
~ -[AXUIServiceEntitlementChecker serviceCanProcessMessageWithIdentifier:fromClientWithConnection:possibleRequiredEntitlements:needsToRequireEntitlements:] : 1216 -> 1248
~ -[AXUIAssertionManager invalidateAssertionIfNeeded] : 144 -> 264
~ ___51-[AXUIAssertionManager invalidateAssertionIfNeeded]_block_invoke : 268 -> 372
~ -[AXUIAssertionManager invalidateAssertionUIIfNeeded] : 144 -> 264
~ ___53-[AXUIAssertionManager invalidateAssertionUIIfNeeded]_block_invoke : 300 -> 336
CStrings:
+ "Can't invalidate Background Assertion, %lu services are still registered: %@. This timer is not automatically rescheduled — invalidation will not be retried until the next call to acquireAssertionIfNeeded/invalidateAssertionIfNeeded."
+ "Can't invalidate UI Assertion, still clients with UI assertion %@. This timer is not automatically rescheduled — invalidation will not be retried until the next call to acquireAssertionUIIfNeeded/invalidateAssertionUIIfNeeded."
+ "First registration for client %@ serviceBundleName=%@, triggered by message identifier %lu from pid %d"
+ "invalidateAssertionIfNeeded scheduling timer, current assertionBackground: %@"
+ "invalidateAssertionIfNeeded timer fired, assertionBackground: %@"
+ "invalidateAssertionUIIfNeeded scheduling timer, current assertionUI: %@"
+ "invalidateAssertionUIIfNeeded timer fired, assertionUI: %@"
- "Can't invalidate Background Assertion, still services are registered"
- "Can't invalidate UI Assertion, still clients with UI assertion %@"
- "invalidateAssertionIfNeeded timer"
- "invalidateAssertionUIIfNeeded timer"
```
