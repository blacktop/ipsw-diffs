## TrustedPeersHelper

> `/System/Library/Frameworks/Security.framework/XPCServices/TrustedPeersHelper.xpc/TrustedPeersHelper`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_entry`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_capture`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__objc_stublist`

```diff

-62460.60.42.502.1
-  __TEXT.__text: 0x2aadb0
+62460.60.60.0.1
+  __TEXT.__text: 0x2ac110
   __TEXT.__auth_stubs: 0x24e0
-  __TEXT.__objc_stubs: 0x61e0
+  __TEXT.__objc_stubs: 0x6220
   __TEXT.__objc_methlist: 0x2994
-  __TEXT.__const: 0xd790
-  __TEXT.__cstring: 0x17f92
-  __TEXT.__swift5_typeref: 0x40fe
-  __TEXT.__oslogstring: 0xe76b
+  __TEXT.__const: 0xd780
+  __TEXT.__cstring: 0x181f2
+  __TEXT.__swift5_typeref: 0x412e
+  __TEXT.__oslogstring: 0xe90b
   __TEXT.__swift5_entry: 0x8
   __TEXT.__objc_classname: 0x14e3
-  __TEXT.__objc_methname: 0x93c1
+  __TEXT.__objc_methname: 0x93e1
   __TEXT.__objc_methtype: 0x2acf
   __TEXT.__constg_swiftt: 0x3d04
   __TEXT.__swift5_fieldmd: 0x2c14

   __TEXT.__gcc_except_tab: 0x128
   __TEXT.__unwind_info: 0x69a0
   __TEXT.__eh_frame: 0x8138
-  __DATA_CONST.__const: 0x155c0
+  __DATA_CONST.__const: 0x155f8
   __DATA_CONST.__cfstring: 0x1840
   __DATA_CONST.__objc_classlist: 0x278
   __DATA_CONST.__objc_catlist: 0x20

   __DATA_CONST.__objc_superrefs: 0xf0
   __DATA_CONST.__objc_intobj: 0x18
   __DATA_CONST.__auth_got: 0x1280
-  __DATA_CONST.__got: 0xaf8
+  __DATA_CONST.__got: 0xac0
   __DATA_CONST.__auth_ptr: 0x770
   __DATA.__objc_const: 0x70a0
-  __DATA.__objc_selrefs: 0x1f38
+  __DATA.__objc_selrefs: 0x1f48
   __DATA.__objc_ivar: 0x1fc
   __DATA.__objc_data: 0x2d48
-  __DATA.__data: 0x85e8
+  __DATA.__data: 0x85f8
   __DATA.__objc_stublist: 0xa8
   __DATA.__common: 0xa28
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 9073
-  Symbols:   597
-  CStrings:  3292
+  Functions: 9075
+  Symbols:   590
+  CStrings:  3308
 
Symbols:
+ _OBJC_CLASS_$_NSUserDefaults
+ _kSecurityRTCEventNameTDLTDIDReappearance
- _kSecurityRTCEventNameTDLTDIDReapperance
- _kSecurityRTCFieldAllowedRecordCount
- _kSecurityRTCFieldDisallowedRecordCount
- _kSecurityRTCFieldLookupKeyType
- _kSecurityRTCFieldMIDRolled
- _kSecurityRTCFieldMachineRecordAllowed
- _kSecurityRTCFieldRecordCount
- _kSecurityRTCFieldStableIDDuplicateDeviceCount
- _kSecurityRTCFieldStableTrustedDeviceIDInclusionEnabled
CStrings:
+ "%{public}s is set, leaving the TDID caches as they are"
+ "; no machine record matches this device"
+ "; the matching machine record is allowed"
+ "; the matching machine record is not allowed"
+ "Identity reroll reused this device's cached TDID"
+ "SkipTDIDCacheUpdates"
+ "TDID cached, but the new peer won't carry it"
+ "This device's TDID was last used under a previous MID"
+ "This device's stableID is shared with another MID on the TDL"
+ "Trusted peer's machine ID rolled, and a TDID appeared for the first time"
+ "Trusted peer's machine ID rolled, and the TDID survived the roll"
+ "boolForKey:"
+ "captureDuplicateTDIDTelemetry: egoMachineID=%{public}s duplicateStableIDCount=%{public}ld egoCollidingGroupCount=%{public}ld"
+ "checkEgoStableIDUniqueness: machineID=%{public}s candidate=%{public}s historyCount=%{public}ld tdidMatches=%{public}ld reused=%{bool,public}d midRolled=%{bool,public}d isIdentityReroll=%{bool,public}d"
+ "com.apple.security"
+ "initWithSuiteName:"
+ "prepareTDIDPresence: machineID=%{public}s hasCachedTDID=%{bool,public}d inclusionEnabled=%{bool,public}d peerCarriesTDID=%{bool,public}d code=%{public}ld notCarried=%{bool,public}d"
- "checkEgoStableIDUniqueness: machineID=%{public}s candidate=%{public}s historyCount=%{public}ld tdidMatches=%{public}ld reused=%{bool,public}d midRolled=%{bool,public}d"
```
