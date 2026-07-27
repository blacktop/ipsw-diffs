## libUSBCfwflasher.dylib

> `/usr/lib/libUSBCfwflasher.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__got`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH_CONST.__auth_got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__DATA.__data`

```diff

 35.0.0.0.0
-  __TEXT.__text: 0x23f2c
+  __TEXT.__text: 0x241d0
   __TEXT.__auth_stubs: 0xcb0
   __TEXT.__init_offsets: 0x18
   __TEXT.__objc_methlist: 0x4fc
-  __TEXT.__cstring: 0x904b
+  __TEXT.__cstring: 0x927f
+  __TEXT.__const: 0x670
   __TEXT.__gcc_except_tab: 0xdc8
-  __TEXT.__const: 0x660
   __TEXT.__oslogstring: 0x21a2
   __TEXT.__unwind_info: 0x720
   __TEXT.__objc_classname: 0x50

   __DATA_CONST.__objc_superrefs: 0x20
   __AUTH_CONST.__auth_got: 0x668
   __AUTH_CONST.__const: 0x238
-  __AUTH_CONST.__cfstring: 0x3020
+  __AUTH_CONST.__cfstring: 0x3160
   __AUTH_CONST.__objc_const: 0x720
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH.__objc_data: 0x190

   - /usr/lib/libobjc.A.dylib
   Functions: 436
   Symbols:   1032
-  CStrings:  1564
+  CStrings:  1574
 
Functions:
~ -[iecsUpdater flash:andErrorResponse:] : 11048 -> 11724
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iBVjh3/Sources/AstrisArmProbeServer/api/booster_api/astris_boostermanager.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iBVjh3/Sources/AstrisArmProbeServer/api/booster_api/astris_boostermanager_soc.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iBVjh3/Sources/AstrisArmProbeServer/api/concurrency/astris_attitude.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iBVjh3/Sources/AstrisArmProbeServer/api/misc/astris_user_default.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iBVjh3/Sources/AstrisArmProbeServer/api/probe_comms/astris_connect.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iBVjh3/Sources/AstrisArmProbeServer/api/probe_comms/astris_transact.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iBVjh3/Sources/AstrisArmProbeServer/api/socs/astris_explore_override.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iBVjh3/Sources/AstrisArmProbeServer/api/socs/astris_soc.cpp"
+ "3151.120.8b455"
+ "AstrisArmProbeServer-3151.120.8~455 (CheerG tools)"
+ "Attempting to un-bork firmware... status = 0x%X"
+ "Command set required to update this HW is not available.  Update process is forced to abort."
+ "Failed to write \"MAGIC\" data or send memory modify command. status=0x%02x"
+ "Firmware appears to be within the range known to have a broken update path.  Attempting to fix"
+ "MEMm response: %02X %02X %02X %02X"
+ "Memory modify failed and out of retries.  Aborting as retries were exhausted"
+ "Modifying memory..."
+ "Retrying memory modify command as it looks like it didn't execute..."
+ "Should think SFWu now usable"
+ "useBorkedSFWWorkarounds: %s"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2gw8Fw/Sources/AstrisArmProbeServer/api/booster_api/astris_boostermanager.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2gw8Fw/Sources/AstrisArmProbeServer/api/booster_api/astris_boostermanager_soc.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2gw8Fw/Sources/AstrisArmProbeServer/api/concurrency/astris_attitude.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2gw8Fw/Sources/AstrisArmProbeServer/api/misc/astris_user_default.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2gw8Fw/Sources/AstrisArmProbeServer/api/probe_comms/astris_connect.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2gw8Fw/Sources/AstrisArmProbeServer/api/probe_comms/astris_transact.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2gw8Fw/Sources/AstrisArmProbeServer/api/socs/astris_explore_override.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2gw8Fw/Sources/AstrisArmProbeServer/api/socs/astris_soc.cpp"
- "3151.120.8b409"
- "AstrisArmProbeServer-3151.120.8~409 (CheerGSeed tools)"
```
