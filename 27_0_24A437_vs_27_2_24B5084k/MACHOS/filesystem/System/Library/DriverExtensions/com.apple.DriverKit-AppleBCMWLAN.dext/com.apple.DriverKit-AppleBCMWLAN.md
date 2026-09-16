## com.apple.DriverKit-AppleBCMWLAN

> `/System/Library/DriverExtensions/com.apple.DriverKit-AppleBCMWLAN.dext/com.apple.DriverKit-AppleBCMWLAN`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__const`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__osclassinfo`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA.__data`

```diff

-1580.73.0.0.0
-  __TEXT.__text: 0x28ad80
+1582.4.0.0.0
+  __TEXT.__text: 0x28b79c
   __TEXT.__auth_stubs: 0x25c0
   __TEXT.__init_offsets: 0x1bc
-  __TEXT.__cstring: 0x831be
+  __TEXT.__cstring: 0x83602
   __TEXT.__const: 0x7f168
   __TEXT.__oslogstring: 0x1f27
-  __TEXT.__unwind_info: 0xa460
+  __TEXT.__unwind_info: 0xa480
   __TEXT.__eh_frame: 0x38
-  __DATA_CONST.__const: 0x21148
+  __DATA_CONST.__const: 0x211a8
   __DATA_CONST.__osclassinfo: 0x388
   __DATA_CONST.__auth_got: 0x12e0
   __DATA_CONST.__got: 0x108

   - /System/DriverKit/System/Library/PrivateFrameworks/IOFileValidation.framework/IOFileValidation
   - /System/DriverKit/System/Library/PrivateFrameworks/OLYHALDriverKit.framework/OLYHALDriverKit
   - /System/DriverKit/usr/lib/libc++.dylib
-  Functions: 14188
-  Symbols:   12064
-  CStrings:  13133
+  Functions: 14196
+  Symbols:   12068
+  CStrings:  13147
 
Symbols:
+ __ZN16AppleBCMWLANCore33checkForAdaptive11rFromASRSupportEv
+ __ZN23IO80211SkywalkInterface20postPeerPresenceDoneEP10ether_addrb
+ __ZN30AppleBCMWLANProximityInterface27applyInitialChannelSequenceEPKc
+ __ZThn80_N23IO80211SkywalkInterface20postPeerPresenceDoneEP10ether_addrb
CStrings:
+ " (NAN availability pending, will ride the next real sequence)"
+ " (WLC_E_IF_ADD retry)"
+ " + NAN availability"
+ "\"AppleBCMWLANV3_driverkit-1582.4\""
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.iPhoneOS27.2.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
+ "<redacted>"
+ "AppleBCMWLANV3_driverkit-1582.4"
+ "[dk] %s@%d:ERROR: NAN attribute header runs past the end of the attribute list\n"
+ "[dk] %s@%d:ERROR: NAN attribute length %u exceeds the remaining attribute list\n"
+ "[dk] %s@%d:ERROR: NAN shared key descriptor body %u too short, minimum %u\n"
+ "[dk] %s@%d:ERROR: NAN shared key descriptor key data length %u exceeds body %u\n"
+ "[dk] %s@%d:SlotBSS: deferred #%u (guard=fBcmInterfaceIdValid) id=%d valid=%d -- sequence saved, will replay on WLC_E_IF_ADD/interface creation\n"
+ "[dk] %s@%d:SlotBSS: deferred #%u (guard=fInterfaceCreated) -- sequence saved, will replay on interface creation\n"
+ "[dk] %s@%d:SlotBSS: no-op%s: no deferred channel sequence to replay (cached len=%u, pending=%d) -- not sending slot_bss%s\n"
+ "[dk] %s@%d:SlotBSS: replay #%u%s: FW AWDL interface created, re-applying deferred sequence len=%u enc=%u step=%u dup=%u flags=0x%x ch[0]=%u%s\n"
+ "[dk] %s@%d:SlotBSS: watchdog-skipped #%u -- SlotBSS failed but interface already invalid (chip reset in flight)\n"
+ "applyInitialChannelSequence"
- "\"AppleBCMWLANV3_driverkit-1580.73\""
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.iPhoneOS27.0.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
- "AppleBCMWLANV3_driverkit-1580.73"
```
