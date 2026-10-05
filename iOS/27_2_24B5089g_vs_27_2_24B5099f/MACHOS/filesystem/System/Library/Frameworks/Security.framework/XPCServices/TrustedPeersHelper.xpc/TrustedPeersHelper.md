## TrustedPeersHelper

> `/System/Library/Frameworks/Security.framework/XPCServices/TrustedPeersHelper.xpc/TrustedPeersHelper`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_protos`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__objc_stublist`

```diff

-62460.40.56.502.1
-  __TEXT.__text: 0x2a5a98
-  __TEXT.__auth_stubs: 0x24b0
-  __TEXT.__objc_stubs: 0x61a0
-  __TEXT.__objc_methlist: 0x2954
-  __TEXT.__const: 0xd750
-  __TEXT.__cstring: 0x17e20
-  __TEXT.__swift5_typeref: 0x40aa
-  __TEXT.__oslogstring: 0xe35b
+62460.40.74.0.0
+  __TEXT.__text: 0x2aa000
+  __TEXT.__auth_stubs: 0x24e0
+  __TEXT.__objc_stubs: 0x61e0
+  __TEXT.__objc_methlist: 0x2968
+  __TEXT.__const: 0xd760
+  __TEXT.__cstring: 0x17f90
+  __TEXT.__swift5_typeref: 0x40ca
+  __TEXT.__oslogstring: 0xe68b
   __TEXT.__swift5_entry: 0x8
   __TEXT.__objc_classname: 0x14e3
-  __TEXT.__objc_methname: 0x92d1
+  __TEXT.__objc_methname: 0x9351
   __TEXT.__objc_methtype: 0x2a60
-  __TEXT.__constg_swiftt: 0x3cf4
+  __TEXT.__constg_swiftt: 0x3cfc
   __TEXT.__swift5_fieldmd: 0x2c08
   __TEXT.__swift5_builtin: 0xdc
   __TEXT.__swift5_reflstr: 0x26da

   __TEXT.__swift5_proto: 0x9ac
   __TEXT.__swift5_types: 0x2d4
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__swift5_capture: 0x53fc
+  __TEXT.__swift5_capture: 0x54b4
   __TEXT.__swift5_protos: 0x1c
   __TEXT.__gcc_except_tab: 0x128
-  __TEXT.__unwind_info: 0x68d8
-  __TEXT.__eh_frame: 0x8030
-  __DATA_CONST.__const: 0x15368
+  __TEXT.__unwind_info: 0x6980
+  __TEXT.__eh_frame: 0x8138
+  __DATA_CONST.__const: 0x15520
   __DATA_CONST.__cfstring: 0x1840
   __DATA_CONST.__objc_classlist: 0x278
   __DATA_CONST.__objc_catlist: 0x20

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__objc_superrefs: 0xf0
-  __DATA_CONST.__auth_got: 0x1268
-  __DATA_CONST.__got: 0xad8
+  __DATA_CONST.__auth_got: 0x1280
+  __DATA_CONST.__got: 0xaf8
   __DATA_CONST.__auth_ptr: 0x770
-  __DATA.__objc_const: 0x7080
-  __DATA.__objc_selrefs: 0x1f10
+  __DATA.__objc_const: 0x7098
+  __DATA.__objc_selrefs: 0x1f28
   __DATA.__objc_ivar: 0x1fc
   __DATA.__objc_data: 0x2d48
-  __DATA.__data: 0x85c8
+  __DATA.__data: 0x85d0
   __DATA.__objc_stublist: 0xa8
   __DATA.__common: 0xa28
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 9011
-  Symbols:   594
-  CStrings:  3269
+  Functions: 9059
+  Symbols:   596
+  CStrings:  3285
 
Symbols:
+ _kSecurityRTCEventNameTDLTDIDReapperance
+ _kSecurityRTCFieldMIDRolled
CStrings:
+ "Failed to save observed ego stable ID history: %{public}s"
+ "This device's new TDID matches one it has used before"
+ "Trusted peer's machine ID rolled, and the TDID changed to a different value"
+ "Trusted peer's machine ID rolled, and the TDID did not survive the roll"
+ "Trusted peer's machine ID rolled; the TDID was never present, either before or after"
+ "captureTDIDStabilityTelemetry: thisDeviceMachineID=%{public}s cachedMachineID=%{public}s resolvedMachineID=%{public}s existingStableID=%{public}s incomingStableID=%{public}s egoPairFound=%{bool,public}d midRolled=%{bool,public}d"
+ "checkEgoStableIDUniqueness: machineID=%{public}s candidate=%{public}s historyCount=%{public}ld tdidMatches=%{public}ld reused=%{bool,public}d midRolled=%{bool,public}d"
+ "notifyPeerTrustEstablished"
+ "notifyPeerTrustEstablished complete: %{public}s"
+ "notifyPeerTrustEstablished failed for %{public}s: %{public}s"
+ "notifyPeerTrustEstablished for %{public}s"
+ "notifyPeerTrustEstablished(reply:)"
+ "notifyPeerTrustEstablished: Octagon confirmed trust, submitting ego stable trusted device ID: %{public}s machineID: %{public}s"
+ "notifyPeerTrustEstablishedWithSpecificUser:reply:"
+ "observedEgoTrustedDeviceIDs"
+ "recordEgoStableIDIntoHistory: already present, not updating cache"
+ "recordEgoStableIDIntoHistory: cache updated, now containing %{public}ld entries"
+ "setObservedEgoTrustedDeviceIDs:"
- "Trusted peer's TDID is stable"
- "captureTDIDStabilityTelemetry: machineID=%{public}s existingStableID=%{public}s incomingStableID=%{public}s"
```
