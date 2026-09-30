## DoNotDisturbServer

> `/System/Library/PrivateFrameworks/DoNotDisturbServer.framework/DoNotDisturbServer`

```diff

-433.4.2.0.0
-  __TEXT.__text: 0xc2ea4
-  __TEXT.__auth_stubs: 0x13b0
-  __TEXT.__objc_methlist: 0x8a94
+433.5.16.0.0
+  __TEXT.__text: 0xc2890
+  __TEXT.__auth_stubs: 0x1350
+  __TEXT.__objc_methlist: 0xa908
   __TEXT.__const: 0x458
-  __TEXT.__cstring: 0x89a4
-  __TEXT.__oslogstring: 0x11240
+  __TEXT.__cstring: 0x8894
+  __TEXT.__oslogstring: 0x11280
   __TEXT.__gcc_except_tab: 0xf74
   __TEXT.__dlopen_cstrs: 0x59
   __TEXT.__swift5_typeref: 0x150

   __TEXT.__swift5_types: 0x10
   __TEXT.__swift5_capture: 0x120
   __TEXT.__swift5_proto: 0xc
-  __TEXT.__unwind_info: 0x2820
-  __TEXT.__eh_frame: 0x538
-  __TEXT.__objc_classname: 0x289f
-  __TEXT.__objc_methname: 0x1973f
-  __TEXT.__objc_methtype: 0x7557
-  __TEXT.__objc_stubs: 0x109c0
-  __DATA_CONST.__got: 0xe60
-  __DATA_CONST.__const: 0x25b0
+  __TEXT.__swift_as_entry: 0x2c
+  __TEXT.__swift_as_ret: 0x2c
+  __TEXT.__unwind_info: 0x2808
+  __TEXT.__eh_frame: 0x530
+  __TEXT.__objc_classname: 0x28c2
+  __TEXT.__objc_methname: 0x19818
+  __TEXT.__objc_methtype: 0x7570
+  __TEXT.__objc_stubs: 0x10ae0
+  __DATA_CONST.__got: 0xe58
+  __DATA_CONST.__const: 0x25d8
   __DATA_CONST.__objc_classlist: 0x5f8
   __DATA_CONST.__objc_catlist: 0x148
-  __DATA_CONST.__objc_protolist: 0x3c8
+  __DATA_CONST.__objc_protolist: 0x3d0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4860
+  __DATA_CONST.__objc_selrefs: 0x4c58
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x3e0
   __DATA_CONST.__objc_arraydata: 0x330
-  __AUTH_CONST.__auth_got: 0x9e8
+  __AUTH_CONST.__auth_got: 0x9b8
   __AUTH_CONST.__auth_ptr: 0xb8
   __AUTH_CONST.__const: 0x1030
-  __AUTH_CONST.__cfstring: 0x7740
-  __AUTH_CONST.__objc_const: 0x29440
+  __AUTH_CONST.__cfstring: 0x7940
+  __AUTH_CONST.__objc_const: 0x25f38
   __AUTH_CONST.__objc_intobj: 0x2d0
   __AUTH_CONST.__objc_dictobj: 0x488
   __AUTH_CONST.__objc_arrayobj: 0x108
-  __AUTH.__objc_data: 0x998
+  __AUTH.__objc_data: 0x808
   __DATA.__objc_ivar: 0xa38
-  __DATA.__data: 0x32d0
+  __DATA.__data: 0x3330
   __DATA.__bss: 0x1c0
-  __DATA_DIRTY.__objc_data: 0x33d8
+  __DATA_DIRTY.__objc_data: 0x3568
   __DATA_DIRTY.__data: 0xb0
   __DATA_DIRTY.__bss: 0x218
   __DATA_DIRTY.__common: 0x1b0

   - /System/Library/PrivateFrameworks/WorkflowUIServices.framework/WorkflowUIServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 3768
-  Symbols:   4890
-  CStrings:  6651
+  Functions: 3787
+  Symbols:   4919
+  CStrings:  6666
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCompression
+ _kLostModeChangedRestrictedNotification
- _kLostModeChangedNotification
- _objc_release_x10
- _swift_arrayDestroy
CStrings:
+ "<invalid(%ld)>"
+ "<read error>"
+ "<redacted>"
+ "@\"NSDictionary\"20@0:8B16"
+ "@16@?0@\"CLRegion\"8"
+ "Breakthrough %{public}@ allowed with reason: %@ for configuration %@ with event details: %@."
+ "Checked if event source is a contact: source=%{private}@, contact=%{BOOL}d"
+ "Checked if event source is a favorite: source=%{private}@, favorite=%{BOOL}d"
+ "Checked if event source is a group contact: source=%{private}@, contact=%{BOOL}d"
+ "Checked if event source is a repeat: source=%{private}@, repeat=%{BOOL}d"
+ "Checked if event source is an emergency contact: source=%{private}@, emergencyContact=%{BOOL}d"
+ "Current DND state was calculated: state=%{private}@"
+ "DNDSLocationSysdiagnoseContributor"
+ "Requesting cached state for region %{private}@."
+ "State was updated: currentState=%{private}@"
+ "State was updated: previousState=%{private}@"
+ "_updateWithCachedStateForRegions:"
+ "accuracyAuthorization"
+ "circularRegionMonitoringAvailable"
+ "enteredRegionIdentifiers"
+ "explicitRegion"
+ "isMonitoringAvailableForClass:"
+ "locationServicesEnabled"
+ "maximumRegionMonitoringDistance"
+ "regionMonitoringAvailable"
+ "requestStateForRegion:"
+ "stored"
+ "sysdiagnoseDataRedacted:"
+ "untilExit"
- "Breakthrough %{public}@ allowed for configuration %@ with event details: %@."
- "Checked if event source is a contact: source=%{public}@, contact=%{BOOL}d"
- "Checked if event source is a favorite: source=%{public}@, favorite=%{BOOL}d"
- "Checked if event source is a group contact: source=%{public}@, contact=%{BOOL}d"
- "Checked if event source is a repeat: source=%{public}@, repeat=%{BOOL}d"
- "Checked if event source is an emergency contact: source=%{public}@, emergencyContact=%{BOOL}d"
- "Current DND state was calculated: state=%{public}@"
- "Fatal error"
- "Insufficient space allocated to copy string contents"
- "State was updated: currentState=%{public}@"
- "State was updated: previousState=%{public}@"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "invalid Collection: less than 'count' elements in collection"

```
