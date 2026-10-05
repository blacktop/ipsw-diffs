## com.apple.DriverKit-AppleBCMWLAN

> `/System/Library/DriverExtensions/com.apple.DriverKit-AppleBCMWLAN.dext/com.apple.DriverKit-AppleBCMWLAN`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__const`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__osclassinfo`
- `__DATA.__data`

```diff

-1582.5.0.0.0
-  __TEXT.__text: 0x28b7e8
+1582.8.0.0.0
+  __TEXT.__text: 0x28b574
   __TEXT.__auth_stubs: 0x25c0
   __TEXT.__init_offsets: 0x1bc
-  __TEXT.__cstring: 0x83602
+  __TEXT.__cstring: 0x834c7
   __TEXT.__const: 0x7f168
   __TEXT.__oslogstring: 0x1f27
-  __TEXT.__unwind_info: 0xa488
+  __TEXT.__unwind_info: 0xa480
   __TEXT.__eh_frame: 0x38
-  __DATA_CONST.__const: 0x211a8
+  __DATA_CONST.__const: 0x211c0
   __DATA_CONST.__osclassinfo: 0x388
   __DATA_CONST.__auth_got: 0x12e0
   __DATA_CONST.__got: 0x108

   - /System/DriverKit/System/Library/PrivateFrameworks/OLYHALDriverKit.framework/OLYHALDriverKit
   - /System/DriverKit/usr/lib/libc++.dylib
   Functions: 14198
-  Symbols:   12070
-  CStrings:  13147
+  Symbols:   12073
+  CStrings:  13143
 
Symbols:
+ __ZN30AppleBCMWLANProximityInterface18setAGGRESSIVE_EDCAEP26apple80211_aggressive_edca
+ __ZThn112_N30AppleBCMWLANProximityInterface18setAGGRESSIVE_EDCAEP26apple80211_aggressive_edca
+ __ZThn128_N30AppleBCMWLANProximityInterface18setAGGRESSIVE_EDCAEP26apple80211_aggressive_edca
CStrings:
+ "\"AppleBCMWLANV3_driverkit-1582.8\""
+ "AppleBCMWLANV3_driverkit-1582.8"
- "\"AppleBCMWLANV3_driverkit-1582.5\""
- "AppleBCMWLANV3_driverkit-1582.5"
- "[dk] %s@%d:ERROR: NAN attribute header runs past the end of the attribute list\n"
- "[dk] %s@%d:ERROR: NAN attribute length %u exceeds the remaining attribute list\n"
- "[dk] %s@%d:ERROR: NAN shared key descriptor body %u too short, minimum %u\n"
- "[dk] %s@%d:ERROR: NAN shared key descriptor key data length %u exceeds body %u\n"
```
