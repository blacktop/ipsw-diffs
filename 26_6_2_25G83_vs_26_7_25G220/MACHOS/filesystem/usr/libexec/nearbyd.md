## nearbyd

> `usr/libexec/nearbyd`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__got`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

 524.0.7.0.0
-  __TEXT.__text: 0x4a2dc0
+  __TEXT.__text: 0x4aa9dc
   __TEXT.__auth_stubs: 0x2220
-  __TEXT.__objc_stubs: 0x12d80
-  __TEXT.__init_offsets: 0x2cc
-  __TEXT.__objc_methlist: 0xd518
-  __TEXT.__gcc_except_tab: 0x4df78
-  __TEXT.__const: 0x3530b8
-  __TEXT.__cstring: 0x34ace
-  __TEXT.__objc_methname: 0x1d76b
-  __TEXT.__oslogstring: 0x51ed0
+  __TEXT.__objc_stubs: 0x12e60
+  __TEXT.__init_offsets: 0x2d0
+  __TEXT.__objc_methlist: 0xd610
+  __TEXT.__gcc_except_tab: 0x4e650
+  __TEXT.__const: 0x353648
+  __TEXT.__cstring: 0x3507a
+  __TEXT.__objc_methname: 0x1d886
+  __TEXT.__oslogstring: 0x52721
   __TEXT.__objc_classname: 0x1bf3
-  __TEXT.__objc_methtype: 0x1ed8c
-  __TEXT.__unwind_info: 0x18c68
+  __TEXT.__objc_methtype: 0x1edac
+  __TEXT.__unwind_info: 0x19008
   __DATA_CONST.__auth_got: 0x1128
   __DATA_CONST.__got: 0x8e8
   __DATA_CONST.__auth_ptr: 0x70
-  __DATA_CONST.__const: 0x23120
-  __DATA_CONST.__cfstring: 0x14d80
+  __DATA_CONST.__const: 0x235e0
+  __DATA_CONST.__cfstring: 0x14e40
   __DATA_CONST.__objc_classlist: 0x540
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x290

   __DATA_CONST.__objc_intobj: 0x8e8
   __DATA_CONST.__objc_doubleobj: 0x30
   __DATA_CONST.__objc_dictobj: 0xc8
-  __DATA.__objc_const: 0x16c18
-  __DATA.__objc_selrefs: 0x5cc8
+  __DATA.__objc_const: 0x16c30
+  __DATA.__objc_selrefs: 0x5d08
   __DATA.__objc_ivar: 0x1654
   __DATA.__objc_data: 0x3480
   __DATA.__data: 0x3224
-  __DATA.__bss: 0xc5e8
+  __DATA.__bss: 0xc950
   __DATA.__common: 0xdb0
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 20316
+  Functions: 20495
   Symbols:   841
-  CStrings:  17532
+  CStrings:  17589
 
CStrings:
+ "#ble,Activate. Supports UWB: [%d], Supports WiFi ToF: [%d], Supports Perception: [%d], TokenFlags: [0x%08x]. ControlFlags: [0x%08x]"
+ "#intentaggr,Deliver handoff intention: %d, from source: %s, beforeExecute: %d"
+ "#intentaggr,clear up: fSilenceTimer == nil: %s"
+ "#intentaggr,delivered handoff intention %d to client for device: %llu"
+ "#intentaggr,silence timer armed for: %.1fs"
+ "#jointEsti, NRBYRegionJointEstimator reset"
+ "#jointEsti, Not configure exit execute region, return even when motion pullback Detected"
+ "#jointEsti, Not support current technology: %d"
+ "#jointEsti, Not support joint estimator for tech: %d"
+ "#jointEsti, Pullback detected, sending NON-Execute region back to client to dismiss handoff, %.4fs since execute detected"
+ "#jointEsti, We are already in Execute withdrawn state, NOP"
+ "#jointEsti, We are not in Execute Region yet but detected motion pullback?"
+ "#jointEsti, [Motion] spatial gesture based user handoff intention detected."
+ "#jointEsti, _combine joint Region cached [tech: %d] Region win: %f , current received [tech: %d] region: %f  "
+ "#jointEsti, _combineRegionCallback NOT update region to clients since its same"
+ "#jointEsti, should send out new BT region trigger by CV."
+ "#jointEsti, should send out new BT region trigger by Motion."
+ "#jointEsti, should send out new BT region trigger by PureBT."
+ "#jointEsti, should send out new region: %s, from tech [BT: %@], [wifi: %@]"
+ "#jointEsti, ~NRBYRegionJointEstimator"
+ "#regionmon Force set KRSSIThresholdOffset before execute with default write: %.2f"
+ "#regionmon _combineBTRegionForJointEstimatorCallback no _deviceRegionJointEstimators for deviceIdentifier: %llu"
+ "#regionmon _jointPrewarmStateUpdate: currentDeviceAssociationState for %llu, motion state: %d, orientation state: %d, Prewarm(Desk) Region state: %d"
+ "#regionmon offsetCurrentHighestBT for deviceId: %llu did not find any devices that match"
+ "#spatialGesturesPredictor #probabilities Other = %f, Handoff = %f"
+ "#spatialGesturesPredictor GesturePredictorSecondary successfully created!"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX26.7.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX26.7.Internal.sdk/usr/local/include/google/protobuf/wire_format_lite_inl.h"
+ "AudioAccessory11,1"
+ "AudioAccessory11,1,"
+ "DelegateProxy: updated cv distance: %.3f. Object: %{private}@"
+ "DelegateProxy: updated cv region %{private}@ (previous: %{private}@). Object: %{private}@"
+ "Device1,8235"
+ "HomeAccessory"
+ "HomeAccessory17,1"
+ "HomeAccessory17,2"
+ "Motion"
+ "NIPerceptionBubbleRSSIOffsetThreshold"
+ "NIPerceptionSignpost_HandoffGestureModelCreate"
+ "NIPerceptionSignpost_HandoffGestureModelDestroy"
+ "NRBYRegionJointEstimator.mm"
+ "Perception"
+ "PerceptionHandoffSessionEnableMonitorLog"
+ "Technology duplicated"
+ "_computeRecencyWeight"
+ "com.apple.nearbyd.reg_monitor.intention"
+ "deviceModelHomeAccessory:"
+ "didUpdateDeviceAssociationStatus:"
+ "object:didUpdateCVDistance:"
+ "object:didUpdateCVRegion:previousRegion:"
+ "session:didUpdateDeviceAssociationStatus:"
+ "session:object:didUpdateCVDistance:"
+ "session:object:didUpdateCVRegion:previousRegion:"
+ "supportsDeviceCVPerception"
+ "timeGap >= 0"
+ "v16@?0B8i12"
+ "v20@?0Q8f16"
+ "v28@?0d8Q16B24"
+ "v32@0:8@\"NINearbyObject\"16d24"
+ "v392@?0d8Q16i24{optional<nearby::algorithms::region_monitoring::Region>=(?=c{Region={basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}fiiiBB})B}28{optional<nearby::algorithms::region_monitoring::Region>=(?=c{Region={basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}fiiiBB})B}84{optional<nearby::algorithms::common::RangeResult>=(?=c{RangeResult=Qdfi{optional<nearby::algorithms::common::AngleMeasurement>=(?=c{AngleMeasurement=ffi})B}d{optional<int>=(?=ci)B}{optional<int>=(?=ci)B}{optional<double>=(?=cd)B}{optional<unsigned char>=(?=cC)B}{optional<double>=(?=cd)B}{optional<double>=(?=cd)B}ii{optional<nearby::algorithms::common::MagneticFieldStrengthCheckParameter>=(?=c{MagneticFieldStrengthCheckParameter=idd})B}{optional<double>=(?=cd)B}{optional<unsigned short>=(?=cS)B}{optional<unsigned char>=(?=cC)B}{optional<unsigned char>=(?=cC)B}{optional<double>=(?=cd)B}{optional<double>=(?=cd)B}{optional<double>=(?=cd)B}})B}140{optional<float>=(?=cf)B}380B388"
+ "v55@0:8@\"<PRBLEDiscoveryConsuming>\"16@\"NSObject<OS_dispatch_queue>\"24@\"NSData\"32@\"NSData\"40{NIBluetoothDiscoveryControlFlags=BBB}48I51"
+ "v55@0:8@16@24@32@40{NIBluetoothDiscoveryControlFlags=BBB}48I51"
- "#ble,Activate. Supports UWB: [%d], Supports WiFi ToF: [%d], TokenFlags: [0x%08x]. ControlFlags: [0x%08x]"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX26.6.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX26.6.Internal.sdk/usr/local/include/google/protobuf/wire_format_lite_inl.h"
- "v54@0:8@\"<PRBLEDiscoveryConsuming>\"16@\"NSObject<OS_dispatch_queue>\"24@\"NSData\"32@\"NSData\"40{NIBluetoothDiscoveryControlFlags=BB}48I50"
- "v54@0:8@16@24@32@40{NIBluetoothDiscoveryControlFlags=BB}48I50"
```
