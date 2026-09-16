## HomeKitDiagnosticExtension

> `/System/Library/Frameworks/HomeKit.framework/PlugIns/HomeKitDiagnosticExtension.appex/HomeKitDiagnosticExtension`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1493.1.5.1.1
-  __TEXT.__text: 0x23c30
-  __TEXT.__auth_stubs: 0x990
-  __TEXT.__objc_stubs: 0x3aa0
+1514.0.0.0.1
+  __TEXT.__text: 0x25378
+  __TEXT.__auth_stubs: 0x9b0
+  __TEXT.__objc_stubs: 0x3d60
   __TEXT.__objc_methlist: 0x1f9c
   __TEXT.__const: 0xe0
   __TEXT.__gcc_except_tab: 0x8fc
-  __TEXT.__cstring: 0x1bec
-  __TEXT.__oslogstring: 0x4cd3
-  __TEXT.__objc_methname: 0x3ed3
+  __TEXT.__cstring: 0x1ef6
+  __TEXT.__oslogstring: 0x503b
+  __TEXT.__objc_methname: 0x3fe8
   __TEXT.__objc_classname: 0x891
   __TEXT.__objc_methtype: 0x63e
-  __TEXT.__unwind_info: 0x960
-  __DATA_CONST.__const: 0x838
-  __DATA_CONST.__cfstring: 0x23a0
+  __TEXT.__ustring: 0x54
+  __TEXT.__unwind_info: 0x978
+  __DATA_CONST.__const: 0x878
+  __DATA_CONST.__cfstring: 0x29a0
   __DATA_CONST.__objc_classlist: 0x200
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x68

   __DATA_CONST.__objc_intobj: 0xf0
   __DATA_CONST.__objc_arraydata: 0x18
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA_CONST.__auth_got: 0x4d8
+  __DATA_CONST.__auth_got: 0x4e8
   __DATA_CONST.__got: 0x448
   __DATA.__objc_const: 0x4598
-  __DATA.__objc_selrefs: 0x12f8
+  __DATA.__objc_selrefs: 0x13a8
   __DATA.__objc_ivar: 0x118
   __DATA.__objc_data: 0x1400
   __DATA.__data: 0x4e0

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 628
-  Symbols:   301
-  CStrings:  1598
+  Functions: 634
+  Symbols:   303
+  CStrings:  1683
 
Symbols:
+ _HMAccessoryTransportTypesToString
+ _HMResidentDeviceStatusDescription
CStrings:
+ "\nNo homes found.\n"
+ "      - \"%@\" [%@] %@%@\n"
+ "    - \"%@\" %@%@ status=%@ enabled=%@\n"
+ "    Blocked: %@\n"
+ "    Bridged: %@\n"
+ "    Category: %@ (%@)\n"
+ "    Device ID: %@\n"
+ "    Firmware: %@\n"
+ "    Identifier: %@\n"
+ "    Manufacturer: %@\n"
+ "    Matter Node ID: %@\n"
+ "    Model: %@\n"
+ "    Reachable Transports: %@ (0x%lX)\n"
+ "    Reachable: %@\n"
+ "    Room: %@\n"
+ "    Serial: %@\n"
+ "    Services (%lu):\n"
+ "    Transport Types: %@ (0x%lX)\n"
+ "  Accessories: %lu\n"
+ "  Accessory: \"%@\"\n"
+ "  Hub State: %@\n"
+ "  Identifier: %@\n"
+ "  Primary: %@\n"
+ "  Residents (%lu):\n"
+ "  Rooms: %lu\n"
+ "  ✓ Home app Spotlight donations collected"
+ "  ✓ homed Spotlight donations collected"
+ "  ✓ homeutil mini dump collected"
+ "  ✗ Failed to collect Home app Spotlight donations"
+ "  ✗ Failed to collect homed Spotlight donations"
+ " (primary)"
+ "%@ / 0x%llX"
+ "%@-spotlight-donations.txt"
+ "(unknown)"
+ "<private>"
+ "AirPlay"
+ "BLE"
+ "Connected"
+ "Disconnected"
+ "Failed to write homeutil mini dump: %@"
+ "Generated: %@\n"
+ "Home App Spotlight Donation"
+ "Home: \"%@\"\n"
+ "IP"
+ "Not Available"
+ "Refusing homeutil mini dump on non-customer/SEED build"
+ "Refusing homeutil mini dump without user consent"
+ "Resident"
+ "STEP %lu/%lu: Collecting Home app Spotlight Donations"
+ "STEP %lu/%lu: Collecting homed Spotlight Donations"
+ "Unknown (%lu)"
+ "[%{public}@]   ✓ Home app Spotlight donations collected"
+ "[%{public}@]   ✓ homed Spotlight donations collected"
+ "[%{public}@]   ✓ homeutil mini dump collected"
+ "[%{public}@]   ✗ Failed to collect Home app Spotlight donations"
+ "[%{public}@]   ✗ Failed to collect homed Spotlight donations"
+ "[%{public}@] Failed to write homeutil mini dump: %@"
+ "[%{public}@] Refusing homeutil mini dump on non-customer/SEED build"
+ "[%{public}@] Refusing homeutil mini dump without user consent"
+ "[%{public}@] STEP %lu/%lu: Collecting Home app Spotlight Donations"
+ "[%{public}@] STEP %lu/%lu: Collecting homed Spotlight Donations"
+ "[%{public}@] customerOS / SEED build: consent=%@"
+ "[CURRENT] "
+ "[PRIMARY] "
+ "accessories"
+ "category"
+ "categoryType"
+ "customerOS / SEED build: consent=%@"
+ "firmwareVersion"
+ "homeHubState"
+ "homed Spotlight Donation"
+ "homeutil Mini Dump"
+ "homeutil Mini Dump\n"
+ "homeutil-mini-dump.txt"
+ "isBlocked"
+ "isBridged"
+ "isEnabled"
+ "isPrimary"
+ "isPrimaryService"
+ "isReachable"
+ "localizedDescription"
+ "manufacturer"
+ "matterNodeID"
+ "model"
+ "reachableTransports"
+ "rooms"
+ "search -b com.apple.%@ -A"
+ "serialNumber"
+ "serviceType"
+ "services"
+ "transportTypes"
+ "uniqueIdentifier"
+ "|"
+ "════════════════════════════════════════\n"
- "  ✓ Spotlight donations collected"
- "  ✗ Failed to collect Spotlight donations"
- "STEP %lu/%lu: Collecting Spotlight Donations"
- "Spotlight Donation"
- "[%{public}@]   ✓ Spotlight donations collected"
- "[%{public}@]   ✗ Failed to collect Spotlight donations"
- "[%{public}@] STEP %lu/%lu: Collecting Spotlight Donations"
- "homed-spotlight-donations.txt"
- "search -b com.apple.homed -A"
```
