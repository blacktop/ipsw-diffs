## nearbyd

> `/usr/libexec/nearbyd`

```diff

-415.0.7.0.1
-  __TEXT.__text: 0x452e90
+417.0.4.0.0
+  __TEXT.__text: 0x454878
   __TEXT.__auth_stubs: 0x2480
-  __TEXT.__objc_stubs: 0xf440
+  __TEXT.__objc_stubs: 0xf540
   __TEXT.__init_offsets: 0x5c0
-  __TEXT.__objc_methlist: 0x8350
-  __TEXT.__gcc_except_tab: 0x3d6d0
+  __TEXT.__objc_methlist: 0x83b8
+  __TEXT.__gcc_except_tab: 0x3d8a0
   __TEXT.__const: 0x238f00
-  __TEXT.__cstring: 0x2bc0c
-  __TEXT.__objc_methname: 0x166a5
-  __TEXT.__oslogstring: 0x46ce6
-  __TEXT.__objc_classname: 0x1531
-  __TEXT.__objc_methtype: 0x1a417
-  __TEXT.__unwind_info: 0x185b4
+  __TEXT.__cstring: 0x2bef5
+  __TEXT.__objc_methname: 0x1691d
+  __TEXT.__oslogstring: 0x46dd7
+  __TEXT.__objc_classname: 0x1547
+  __TEXT.__objc_methtype: 0x1a42f
+  __TEXT.__unwind_info: 0x18604
   __TEXT.__eh_frame: 0x38
   __DATA_CONST.__auth_got: 0x1258
   __DATA_CONST.__got: 0x558
   __DATA_CONST.__auth_ptr: 0x50
-  __DATA_CONST.__const: 0x1f860
-  __DATA_CONST.__cfstring: 0xda60
-  __DATA_CONST.__objc_classlist: 0x3e0
+  __DATA_CONST.__const: 0x1f880
+  __DATA_CONST.__cfstring: 0xdce0
+  __DATA_CONST.__objc_classlist: 0x3e8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x238
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_arraydata: 0x2c8
+  __DATA_CONST.__objc_arraydata: 0x2d8
   __DATA_CONST.__objc_arrayobj: 0x138
   __DATA_CONST.__objc_intobj: 0x468
-  __DATA_CONST.__objc_dictobj: 0xa0
-  __DATA.__objc_const: 0x140c8
-  __DATA.__objc_selrefs: 0x4608
+  __DATA_CONST.__objc_dictobj: 0xc8
+  __DATA.__objc_const: 0x143a0
+  __DATA.__objc_selrefs: 0x4648
   __DATA.__objc_protorefs: 0x70
-  __DATA.__objc_classrefs: 0x6e8
-  __DATA.__objc_superrefs: 0x3a0
-  __DATA.__objc_ivar: 0x1014
-  __DATA.__objc_data: 0x26c0
+  __DATA.__objc_classrefs: 0x6f0
+  __DATA.__objc_superrefs: 0x3a8
+  __DATA.__objc_ivar: 0x105c
+  __DATA.__objc_data: 0x2710
   __DATA.__data: 0x2ea4
-  __DATA.__bss: 0xcdd0
+  __DATA.__bss: 0xcde8
   __DATA.__common: 0xec8
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libprotobuf-lite.dylib
   - /usr/lib/libprotobuf.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 20885
+  Functions: 20909
   Symbols:   880
-  CStrings:  15028
+  CStrings:  15085
 
CStrings:
+ "\x06)%\x11a\x11"
+ "#findalgs-peoplefinder,reinitializing particle filter. FindeeSlowlyMoving: %d, findeeStatic: %d"
+ "#findalgs-peoplefinder,shouldFeedPF: %d, peerStatic: %d, peerMovingSlowly: %d, hasLastPDR: %d"
+ "#ni-ca,CoreAnalytics: resetting analytics"
+ "#ni-ca,send find button availability analytics event:\n%@\n"
+ "#sa_algo_particlefilter,"
+ "#sa_algo_particlefilter,%s:%d: assertion failure in %s"
+ "#sa_algo_particlefilter,example deltaT: %f, frameRotNoise: %f, deltaZ: %f, deltaX: %f, px: %f, pz: %f, framerot: %f, stepscale: %f, vel: %f, vx: %f, vz: %f"
+ "#sa_algo_particlefilter,ingesting peer vio,  x: %f, y: %f, z: %f, range time: %f, current time: %f"
+ "#ses-ecosystem,AP asleep operation enabled for session ID %@."
+ "#ses-ecosystem,Could not determine ISO country for session ID %@."
+ "#ses-ecosystem,Prepare service request. avoidDedicatedAntennas = [%@], Session ID: %@. "
+ "#ses-ecosystem,[objectFromIdentifier] called for (0x%llx) but no accessory discovery token. Session ID: %@"
+ "%@---%@"
+ "/AppleInternal/Library/BuildRoots/529cd1b6-810a-11ee-9ed3-8e1462286c80/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.2.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
+ "/AppleInternal/Library/BuildRoots/529cd1b6-810a-11ee-9ed3-8e1462286c80/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.2.Internal.sdk/usr/local/include/google/protobuf/wire_format_lite_inl.h"
+ "/Library/Caches/com.apple.xbs/Sources/Proximity/Libraries/NearbyAlgorithms/Finding/ParticleFilter.cpp"
+ "@\"DetailsViewAnalytics\""
+ "DSLP heartbeat enabled: %s"
+ "DeltaTimeFromContainerCreationToDiscovery"
+ "DeltaTimeFromContainerCreationToFindButtonAvailable"
+ "DeltaTimeFromContainerCreationToFindButtonPressed"
+ "DeltaTimeFromDiscoveryToFindButtonAvailable"
+ "DeltaTimeFromFindButtonAvailableToFindButtonPressed"
+ "DetailsViewAnalytics"
+ "DistanceAtDiscovery"
+ "DistanceAtFindButtonAvailable"
+ "DistanceAtPressFind"
+ "DistanceBetweenStartAndEndFinding"
+ "EnteredFromActiveFindingUI"
+ "FindingTime"
+ "FirstRawRangeValueDuringSession"
+ "LastRange"
+ "MaxRawRangeValueDuringSession"
+ "MinimumRange"
+ "NumberOfSuccesses"
+ "PRRose: deep sleep exit request too quick after previous entry. waiting..."
+ "RangeAtFirstArrow"
+ "RangeAtFirstPose"
+ "SessionEndedWithNoRange"
+ "_currentRawRangeValue"
+ "_detailsViewAnalytics"
+ "_distanceAtDiscovery"
+ "_distanceAtEndFinding"
+ "_distanceAtFindButtonAvailable"
+ "_distanceAtFindButtonPressed"
+ "_enteredFromActiveFindingUI"
+ "_firstRawRangeValue"
+ "_maxRawRangeValue"
+ "_minRawRangeValue"
+ "_mostRecentDistance"
+ "_rangeAtFirstArrow"
+ "_rangeAtFirstPose"
+ "_sessionUniqueIdentifier"
+ "_timeAtContainerCreation"
+ "_timeAtDiscovery"
+ "_timeAtFindButtonAvailable"
+ "_timeAtFindButtonPressed"
+ "_timeAtFindingSessionEnd"
+ "com.apple.nearbyd.uwb.deepsleep.wakesuccess"
+ "com.apple.nearbyinteraction.peopleFindingSession.DetailsViewBehavior"
+ "initWithCurrentTime:"
+ "regulatory,geo,sm,noinit"
+ "resetAnalytics"
+ "resetFrameRotationForParticles"
+ "setEnteredFromActiveFindingUI:"
+ "submitAnalytics"
+ "updateDistanceAnalytics:"
+ "updateTimeAnalytics:currentTime:"
+ "updateWithMostRecentDistance:"
+ "updateWithMostRecentRawDistance:"
- "\x06)%\x11a"
- "#findalgs-devicefinder,Revoke due to range 2s timeout"
- "#findalgs-peoplefinder,reinitializing particle filter. FindeeSlowlyMoving: %d, findeeStatic: %d, pdrIsRecent: %d"
- "#findalgs-peoplefinder,shouldFeedPF: %d, pdrIsRecent: %d, peerStatic: %d, peerMovingSlowly: %d, hasLastPDR: %d"
- "#sa_algo_particlefilter,example deltaT: %f, frameRotNoise: %f, deltaH1: %f, deltaH2: %f, px: %f, pz: %f, framerot: %f, stepscale: %f, vel: %f, vx: %f, vz: %f"
- "#sa_algo_particlefilter,using peer PDR motion model"
- "#ses-ecosystem,AP asleep operation enabled for session container %@."
- "#ses-ecosystem,Could not determine ISO country for session container %@."
- "#ses-ecosystem,Prepare service request. avoidDedicatedAntennas = [%@], Container ID: %@. "
- "#ses-ecosystem,[objectFromIdentifier] called for (0x%llx) but no accessory discovery token. Session container: %@"
- "/AppleInternal/Library/BuildRoots/5ae9d77c-6742-11ee-a800-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
- "/AppleInternal/Library/BuildRoots/5ae9d77c-6742-11ee-a800-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/local/include/google/protobuf/wire_format_lite_inl.h"
- "UseCMADistance"
- "com.apple.CoreMotionAlgorithms.nearbyd"

```
