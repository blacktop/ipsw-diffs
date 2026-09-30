## SpotlightServerKit

> `/System/Library/PrivateFrameworks/SpotlightServerKit.framework/Versions/A/SpotlightServerKit`

```diff

-2328.7.8.7.0
-  __TEXT.__text: 0xb33c
+2333.22.13.7.0
+  __TEXT.__text: 0xb50c
   __TEXT.__auth_stubs: 0xde0
   __TEXT.__objc_methlist: 0x600
   __TEXT.__const: 0xd0
   __TEXT.__cstring: 0x1631
   __TEXT.__oslogstring: 0x54b
-  __TEXT.__gcc_except_tab: 0x120
-  __TEXT.__unwind_info: 0x520
+  __TEXT.__gcc_except_tab: 0x130
+  __TEXT.__unwind_info: 0x568
   __TEXT.__objc_classname: 0xd8
   __TEXT.__objc_methname: 0xcab
   __TEXT.__objc_methtype: 0x35a

   - /System/Library/PrivateFrameworks/MetadataUtilities.framework/Versions/A/MetadataUtilities
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FAA08613-3902-3598-8032-6831FB621DF1
-  Functions: 428
-  Symbols:   1055
+  UUID: CB3F4961-B613-306C-AFD2-87068D6B93BA
+  Functions: 466
+  Symbols:   1097
   CStrings:  542
 
Symbols:
+ +[MDSToken initialize].cold.4
+ +[MDSToken initialize].cold.5
+ -[MDSMachSubsystem machPortNotify:object:].cold.1
+ -[MDSMachSubsystem registerForNoSendersNotification:withSelector:andObject:].cold.2
+ -[MDSMachSubsystem unregisterPort:].cold.1
+ -[MDSObject dealloc].cold.1
+ -[MDSObject initWithDeferredShutdown:].cold.1
+ -[MDSObject internalRegisterForDarwinNotification:forBlock:].cold.1
+ -[MDSObject registerForWakeUp:powerNap:delay:gracePeriod:callbackBlock:].cold.2
+ -[MDSObject registerForWakeUp:powerNap:delay:gracePeriod:callbackBlock:].cold.3
+ -[MDSObject registerForWakeUp:powerNap:delay:gracePeriod:callbackBlock:].cold.4
+ -[MDSObject setActivityRegistrationObjectId:].cold.1
+ -[MDSTwoFaceMachPortObject initWithDeferredShutdown:].cold.1
+ GetSystemBuildVersionStringLocal.cold.1
+ MDMachAbsoluteTimeDiff.cold.1
+ MDSLogParseLogArrayDictionary.cold.1
+ MDSTokenRegistryAddTokenForUUID.cold.4
+ MDSTokenRegistryAddTokenForUUID.cold.5
+ MDSecondsToMachAbsoluteTime.cold.1
+ _MDIsAppleInternal.cold.1
+ __21-[MDSObject shutdown]_block_invoke.cold.1
+ __53-[MDSMachSubsystem registerPort:withCallback:rights:]_block_invoke.cold.6
+ __53-[MDSMachSubsystem registerPort:withCallback:rights:]_block_invoke.cold.7
+ __53-[MDSMachSubsystem registerPort:withCallback:rights:]_block_invoke.cold.8
+ __53-[MDSMachSubsystem registerPort:withCallback:rights:]_block_invoke.cold.9
+ __60-[MDSObject internalRegisterForDarwinNotification:forBlock:]_block_invoke.cold.1
+ __72-[MDSObject registerForWakeUp:powerNap:delay:gracePeriod:callbackBlock:]_block_invoke.47.cold.3
+ __72-[MDSObject registerForWakeUp:powerNap:delay:gracePeriod:callbackBlock:]_block_invoke.47.cold.4
+ __72-[MDSObject registerForWakeUp:powerNap:delay:gracePeriod:callbackBlock:]_block_invoke.47.cold.5
+ __72-[MDSObject registerForWakeUp:powerNap:delay:gracePeriod:callbackBlock:]_block_invoke.54.cold.1
+ __72-[MDSObject registerForWakeUp:powerNap:delay:gracePeriod:callbackBlock:]_block_invoke.54.cold.2
+ __72-[MDSObject registerForWakeUp:powerNap:delay:gracePeriod:callbackBlock:]_block_invoke.54.cold.3
+ __72-[MDSObject registerForWakeUp:powerNap:delay:gracePeriod:callbackBlock:]_block_invoke.54.cold.4
+ __72-[MDSObject registerForWakeUp:powerNap:delay:gracePeriod:callbackBlock:]_block_invoke.61.cold.1
+ allow_COW_exempt.cold.1
+ drop_COW_extents.cold.1
+ mdsObjectMsgCallback.cold.2
+ path_bundle_index.cold.1
+ postNotification.cold.2
+ postNotification.cold.3
+ returnFreeActivitySlotIndex.cold.1
+ set_COW_exempt.cold.1
CStrings:
+ "/AppleInternal/Library/BuildRoots/0e5e56ba-061f-11f0-a913-122ba06eff56/Library/Caches/com.apple.xbs/Sources/Spotlight_frameworks/spotlight/server/Foundation/MDSMachPortObject.m"
+ "/AppleInternal/Library/BuildRoots/0e5e56ba-061f-11f0-a913-122ba06eff56/Library/Caches/com.apple.xbs/Sources/Spotlight_frameworks/spotlight/server/Foundation/MDSObject.m"
+ "/AppleInternal/Library/BuildRoots/0e5e56ba-061f-11f0-a913-122ba06eff56/Library/Caches/com.apple.xbs/Sources/Spotlight_frameworks/spotlight/server/Foundation/MDSReadCopyUpdate.m"
+ "/AppleInternal/Library/BuildRoots/0e5e56ba-061f-11f0-a913-122ba06eff56/Library/Caches/com.apple.xbs/Sources/Spotlight_frameworks/spotlight/server/Foundation/MDSToken.m"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/Spotlight_frameworks/spotlight/server/Foundation/MDSMachPortObject.m"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/Spotlight_frameworks/spotlight/server/Foundation/MDSObject.m"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/Spotlight_frameworks/spotlight/server/Foundation/MDSReadCopyUpdate.m"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/Spotlight_frameworks/spotlight/server/Foundation/MDSToken.m"

```
