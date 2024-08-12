## CoreMedia

> `/System/Library/Frameworks/CoreMedia.framework/CoreMedia`

```diff

-3145.72.4.0.0
-  __TEXT.__text: 0x163ec4
+3145.74.1.6.0
+  __TEXT.__text: 0x1652cc
   __TEXT.__auth_stubs: 0x3320
   __TEXT.__objc_methlist: 0x25c
   __TEXT.__const: 0x1928
-  __TEXT.__cstring: 0x1b9d7
-  __TEXT.__oslogstring: 0x557c
+  __TEXT.__cstring: 0x1babc
+  __TEXT.__oslogstring: 0x59e7
   __TEXT.__gcc_except_tab: 0x138
   __TEXT.__dlopen_cstrs: 0x190
-  __TEXT.__unwind_info: 0x3fd0
+  __TEXT.__unwind_info: 0x3fd8
   __TEXT.__objc_classname: 0xe8
   __TEXT.__objc_methname: 0x163d
   __TEXT.__objc_methtype: 0xb5b

   __AUTH.__objc_data: 0x1e0
   __AUTH.__data: 0x1f8
   __DATA.__objc_ivar: 0x90
-  __DATA.__data: 0xa49
+  __DATA.__data: 0xa51
   __DATA.__crash_info: 0x40
   __DATA.__bss: 0x1970
   __DATA.__common: 0x260

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 5628
-  Symbols:   8700
-  CStrings:  5114
+  Functions: 5631
+  Symbols:   8703
+  CStrings:  5129
 
Symbols:
+ _FigTimelineCoordinatorBeginSuspensionProposingTime
+ _FigTimelineCoordinatorEndSuspensionReApplyingGroupStateOnlyIfNeeded
- _figTimelineCoordinator_suspensionReasonsContainInternalSuspensionReasons
CStrings:
+ "<<< EndpointCentricHALPlugin >>> %!s(MISSING): Device list changed; updating list with %!d(MISSING) changed devices\n"
+ "<<< EndpointCentricHALPlugin >>> %!s(MISSING): Updating device list ... [done]\n"
+ "<<< FigHALAudioPluginSupport >>> %!s(MISSING): PropertiesChanged completed with status %!d(MISSING) (inObjectID: %!u(MISSING), numAddresses: %!d(MISSING))"
+ "<<< FigHALAudioPluginSupport >>> %!s(MISSING): Property change completed with status %!d(MISSING) (selector: '%!C(MISSING)', scope: '%!C(MISSING)', element: '%!C(MISSING)')"
+ "<<< FigHALAudioPluginSupport >>> %!s(MISSING): Sending (inObjectID: %!u(MISSING), numAddresses: %!d(MISSING))"
+ "<<< FigHALAudioPluginSupport >>> %!s(MISSING): Sending Property change (selector: '%!c(MISSING)%!c(MISSING)%!c(MISSING)%!c(MISSING)', scope: '%!c(MISSING)%!c(MISSING)%!c(MISSING)%!c(MISSING)', element: '%!c(MISSING)%!c(MISSING)%!c(MISSING)%!c(MISSING)')"
+ "<<<< FigTimelineCoordinator >>>> %!s(MISSING): %!@(MISSING) Other playback coordinator may be using timeline states. Keeping all."
+ "<<<< FigTimelineCoordinator >>>> %!s(MISSING): %!@(MISSING) Participant became suspended"
+ "<<<< FigTimelineCoordinator >>>> %!s(MISSING): %!@(MISSING) Setting expected timeline to propose when all participants are suspended %!@(MISSING)"
+ "<<<< FigTimelineCoordinator >>>> %!s(MISSING): %!@(MISSING) group timeline %!@(MISSING) does not reflect that all participants are suspended, proposing timeline %!@(MISSING)"
+ "FigHALAudioPropertySendChanges"
+ "FigHALAudioPropertySendOneChange"
+ "Trying to write to ring buffer while owning ringConfigurationLock for writing. Dropping log."
+ "endpointCentricPlugin_PeruseActivatedEndpoints_block_invoke"
+ "monitor->associatedObjects == NULL! Monitor = %!p(MISSING); RC = %!z(MISSING)u; serverObjectID = %!l(MISSING)lu; targetObjectID = %!l(MISSING)lu"

```
