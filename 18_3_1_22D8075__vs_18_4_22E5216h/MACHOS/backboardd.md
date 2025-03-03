## backboardd

> `/usr/libexec/backboardd`

```diff

-668.4.1.0.0
-  __TEXT.__text: 0xa4bec
-  __TEXT.__auth_stubs: 0x1c70
-  __TEXT.__objc_stubs: 0xece0
-  __TEXT.__objc_methlist: 0x6970
-  __TEXT.__const: 0x518
-  __TEXT.__gcc_except_tab: 0x5050
-  __TEXT.__objc_methname: 0x14fce
-  __TEXT.__cstring: 0x7456
-  __TEXT.__objc_classname: 0x1c8c
-  __TEXT.__objc_methtype: 0x4050
-  __TEXT.__oslogstring: 0xa427
+668.5.27.1.0
+  __TEXT.__text: 0xa37ac
+  __TEXT.__auth_stubs: 0x1cb0
+  __TEXT.__objc_stubs: 0xeb20
+  __TEXT.__objc_methlist: 0x73cc
+  __TEXT.__const: 0x4e0
   __TEXT.__dlopen_cstrs: 0x62
+  __TEXT.__gcc_except_tab: 0x5178
+  __TEXT.__objc_methname: 0x14e32
+  __TEXT.__cstring: 0x7573
+  __TEXT.__objc_classname: 0x1c0c
+  __TEXT.__objc_methtype: 0x4009
+  __TEXT.__oslogstring: 0xa39a
   __TEXT.__ustring: 0xc
-  __TEXT.__unwind_info: 0x2a88
-  __DATA_CONST.__auth_got: 0xe50
-  __DATA_CONST.__got: 0xa30
-  __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x4ca0
-  __DATA_CONST.__cfstring: 0x8220
-  __DATA_CONST.__objc_classlist: 0x5b8
+  __TEXT.__unwind_info: 0x2a00
+  __DATA_CONST.__auth_got: 0xe70
+  __DATA_CONST.__got: 0xa18
+  __DATA_CONST.__auth_ptr: 0x10
+  __DATA_CONST.__const: 0x4ce0
+  __DATA_CONST.__cfstring: 0x8440
+  __DATA_CONST.__objc_classlist: 0x5a8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x238
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x88
-  __DATA_CONST.__objc_superrefs: 0x430
+  __DATA_CONST.__objc_superrefs: 0x420
   __DATA_CONST.__linkguard: 0x18
   __DATA_CONST.__objc_intobj: 0x360
   __DATA_CONST.__objc_doubleobj: 0x40
   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x14450
-  __DATA.__objc_selrefs: 0x45c0
-  __DATA.__objc_ivar: 0xf78
-  __DATA.__objc_data: 0x3930
-  __DATA.__data: 0x1b50
+  __DATA.__objc_const: 0x130a0
+  __DATA.__objc_selrefs: 0x45f0
+  __DATA.__objc_ivar: 0xf88
+  __DATA.__objc_data: 0x3890
+  __DATA.__data: 0x1b58
   __DATA.__bss: 0x418
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsp.dylib
-  Functions: 3209
-  Symbols:   787
-  CStrings:  6359
+  Functions: 3192
+  Symbols:   789
+  CStrings:  6362
 
Symbols:
+ _BSEqualBools
+ _BSLogAddStateCaptureBlock
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x10
+ _tan
- _BKEventResolutionEntitlement
- _BKSNSStringFromIOHIDProximityDetectionMask
- _OBJC_CLASS_$_BKSHIDEventDescriptor
CStrings:
+ "\x02\x14\x11"
+ "\x0f\x0f"
+ "\x12\x1fA\x11#!\x1f\x04\""
+ "\x1e"
+ "!%%"
+ "@36@0:8@16I24d28"
+ "B24@?0@\"NSString\"8@\"CADisplay\"16"
+ "BK capslock: %{BOOL}u != GS capslock: %{BOOL}u"
+ "BKCADisplayDiffObserver"
+ "BKKeyboardInfo.m"
+ "BKMousePointerRegion.m"
+ "BSStandardCollection"
+ "C\x11\x11\x11\x13"
+ "Freeze brightness:%{BOOL}u to current value -- %{public}@"
+ "PlatformInputModeConfiguration"
+ "_availableDisplaysByUUID"
+ "_brightnessCurrentlyFrozen"
+ "_computeFrameForRegion:layoutDescriptor:accumulatedFrames:"
+ "_contactsByPathIndex"
+ "_content == ((void*)0)"
+ "_coreRemoveContactAtIndex:"
+ "_displayLock_diffObserverAssertion"
+ "_displaysBecomingUninterestingByUUID"
+ "_highIndex"
+ "_interestingDisplaysByUUID"
+ "_lastBrightnessFreezeReason"
+ "_lastBrightnessFreezeTime"
+ "_lastBrightnessUnfreezeReason"
+ "_lastBrightnessUnfreezeTime"
+ "_lock_setCapsLockState:forKeyboard:updateGS:"
+ "_lowIndex"
+ "_mutationtastic"
+ "_platformInputModeConfiguration"
+ "_pointerHIDServiceByServiceID"
+ "_pointerHIDServiceMatcher"
+ "_postImmutableDisplayToObservers:context:"
+ "_queue_invalidateTouchStreamClient:reason:"
+ "_serviceTerminationQueue"
+ "_updateGSCapsLockState"
+ "activeDisplaysDidChange:"
+ "addDiffObserver:"
+ "backboardd.BKMousePointerController.serviceTermination"
+ "backboardd.CADisplayDiffObserver"
+ "backboardd.CADisplayObserver"
+ "backlight locked now:%{BOOL}u for render overlays"
+ "brightnessFreeze"
+ "client request"
+ "correcting GS capslock state to: %{BOOL}u"
+ "currentlyFrozen"
+ "device removed: %{public}@"
+ "display %{public}@ became interesting because %{public}@"
+ "display %{public}@ became uninteresting because %{public}@"
+ "displayUUID != ((void*)0)"
+ "dropping uninteresting displays %{public}@"
+ "geometryForDisplay:"
+ "initWithRelativeRegion:edge:edgePosition:"
+ "invalid region size: %g,%g"
+ "invalidate touch stream (%{public}@) %{public}@"
+ "keyboardLayout != ((void*)0)"
+ "lastFreezeReason"
+ "lastFreezeTime"
+ "lastUnfreezeReason"
+ "lastUnfreezeTime"
+ "monitor:activeDisplaysDidChange:"
+ "not removing destination (contacts exist): %{public}@"
+ "not removing destination (external): %{public}@"
+ "platformInputModeConfiguration"
+ "point != ((void*)0)"
+ "process-exit"
+ "reason != ((void*)0)"
+ "regionToLayoutDescriptor"
+ "service removed"
+ "setPlatformInputModeConfiguration:"
+ "startObservingSynchronously:"
+ "tag changed to %{public}@ for display %{public}@ %{public}@"
+ "v16@?0@\"<BKCADisplayDiffObserver>\"8"
+ "v16@?0@\"BKTouchContact\"8"
+ "v32@0:8@\"BKCADisplayMonitor\"16@\"NSDictionary\"24"
+ "v32@0:8@16^v24"
+ "v32@0:8B16@20B28"
+ "v32@?0@\"NSNumber\"8@\"BKIOHIDService\"16^B24"
+ "valueWithBytes:objCType:"
+ "{CGRect={CGPoint=dd}{CGSize=dd}}"
- "\x02\x13\x11"
- "\x12\x1cA\x11#!\x1f\x04\""
- "\x1f"
- "!$%"
- "(%g,%g,%g,%g)"
- "@\"<BKMousePointerDeviceAvailabilityMonitorObserver>\""
- "@\"BKMousePointerDeviceAvailabilityMonitor\""
- "@44@0:8@16@24I32d36"
- "B16@?0@\"CADisplay\"8"
- "BKMousePointerDeviceAvailabilityMonitor"
- "BKMousePointerDeviceAvailabilityMonitorObserver"
- "C\x11\x13"
- "Locking backlight to current value: %@ for reason: %{public}@"
- "NSFastEnumerationReallyNeedsCount"
- "T@\"<BKMousePointerDeviceAvailabilityMonitorObserver>\",R,W,N,V_observer"
- "T@\"BKMousePointerDeviceAvailabilityMonitor\",&,N,V_deviceAvailabilityMonitor"
- "T@\"BKMousePointerRegion\",R,N,V_region"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_queue"
- "_BKHIDXXGetEventResolutionDescription: cannot encode %{public}@"
- "_BKHIDXXGetEventResolutionDescription: failed to decode event descriptor"
- "_BKHIDXXGetEventResolutionDescription: no event descriptor"
- "_BKMousePointerDeviceAvailabilityMonitorObserverContext"
- "_activeServices"
- "_computeFrameForRegionLayoutDescriptor:accumulatedFrames:"
- "_content == ((void *)0)"
- "_deviceAvailabilityMonitor"
- "_hidServiceMatcher"
- "_interestingDisplays"
- "_lock_setCapsLockState:forKeyboard:"
- "_locked_notifyObserversDidAddDevices:"
- "_locked_notifyObserversDidChangeAvailability"
- "_locked_notifyObserversDidRemoveDevices:"
- "_observer"
- "_observerContexts"
- "_pointerDeviceAvailabilityMonitor"
- "_pointerDeviceAvailabilityMonitorQueue"
- "_region"
- "_unsafeIndexedContacts"
- "activeDisplays"
- "addContact: pathIndex out of bounds -- %{public}@"
- "addObserver:queue:"
- "backboardd.CADisplayMonitor"
- "com.apple.backboard.BKMousePointerController.availabilityMonitorQueue"
- "com.apple.backboard.BKMousePointerDeviceAvailabilityMonitor.queue"
- "descriptionOfResolutionPathForEventDescriptor:senderDescriptor:"
- "descriptionOfResolutionPathForKeyCommand:senderDescriptor:"
- "deviceAvailabilityMonitor"
- "deviceServices"
- "devices removed: %{public}@"
- "display %{public}@ interesting because %{public}@"
- "display %{public}@ uninteresting because %{public}@"
- "display became active -- %@"
- "display became inactive -- %@"
- "displayUUID != ((void *)0)"
- "displays did change -- %@"
- "expected a valid place to put the description data"
- "geometryForDisplayUUID:"
- "hasActiveDisplays"
- "hasDeviceAvailable"
- "immutableDisplayForUUID:"
- "inactive mode -- synthesizing prox cancel for clients:%{public}@"
- "initWithObserver:queue:"
- "initWithRegion:relativeRegion:edge:edgePosition:"
- "invalidate touch stream (invalidated by client) %{public}@"
- "invalidate touch stream (process-exit) %{public}@"
- "keyEnumerator"
- "keyboardLayout != ((void *)0)"
- "mousePointerDeviceAvailabilityMonitorDidChangeAvailability:"
- "mousePointerIOHIDServicesAdded:"
- "mousePointerIOHIDServicesRemoved:"
- "now available: %{BOOL}u"
- "observer"
- "point != ((void *)0)"
- "pointSize:%g,%g cornerRadius:%g scale:%g display:%@"
- "q24@?0@\"BKTouchContact\"8@\"BKTouchContact\"16"
- "reason != ((void *)0)"
- "region"
- "remove clients with (%@)"
- "removeContact:"
- "removeContacts:"
- "removeDisappearanceObserver:"
- "services removed"
- "setDeviceAvailabilityMonitor:"
- "sortUsingComparator:"
- "v16@?0@\"<BKCADisplayObserver>\"8"
- "v24@0:8@\"BKMousePointerDeviceAvailabilityMonitor\"16"

```
