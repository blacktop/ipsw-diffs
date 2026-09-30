## TMHelperAgent

> `/System/Library/CoreServices/TimeMachine/TMHelperAgent.app/Contents/MacOS/TMHelperAgent`

```diff

-  __TEXT.__text: 0x32f8
-  __TEXT.__auth_stubs: 0x260
-  __TEXT.__objc_stubs: 0x1160
-  __TEXT.__objc_methlist: 0x5cc
-  __TEXT.__cstring: 0xd1b
-  __TEXT.__ustring: 0x136
+  __TEXT.__text: 0x48ac
+  __TEXT.__auth_stubs: 0x2c0
+  __TEXT.__objc_stubs: 0x1300
+  __TEXT.__objc_methlist: 0x60c
+  __TEXT.__cstring: 0xe72
+  __TEXT.__ustring: 0x1ba
   __TEXT.__objc_classname: 0x70
-  __TEXT.__objc_methname: 0x1528
-  __TEXT.__objc_methtype: 0x539
+  __TEXT.__objc_methname: 0x1666
+  __TEXT.__objc_methtype: 0x54a
   __TEXT.__const: 0x20
-  __TEXT.__unwind_info: 0x110
-  __DATA_CONST.__const: 0xe0
-  __DATA_CONST.__cfstring: 0x900
+  __TEXT.__gcc_except_tab: 0x28
+  __TEXT.__unwind_info: 0x138
+  __DATA_CONST.__const: 0x148
+  __DATA_CONST.__cfstring: 0xa40
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_intobj: 0x30
-  __DATA_CONST.__auth_got: 0x138
-  __DATA_CONST.__got: 0x130
+  __DATA_CONST.__auth_got: 0x170
+  __DATA_CONST.__got: 0x138
   __DATA.__objc_const: 0x508
-  __DATA.__objc_selrefs: 0x690
+  __DATA.__objc_selrefs: 0x700
   __DATA.__objc_ivar: 0xc
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x120

   - /System/Library/PrivateFrameworks/TimeMachinePrivate.framework/Versions/A/TimeMachinePrivate
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 61
-  Symbols:   84
-  CStrings:  433
+  Functions: 70
+  Symbols:   92
+  CStrings:  466
 
Sections:
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
+ _OBJC_CLASS_$_NSWorkspace
+ __Unwind_Resume
+ ___objc_personality_v0
+ _objc_autoreleaseReturnValue
+ _objc_copyWeak
+ _objc_destroyWeak
+ _objc_initWeak
+ _objc_loadWeakRetained
+ _objc_retainAutoreleaseReturnValue
+ _objc_storeStrong
+ _objc_unsafeClaimAutoreleasedReturnValue
- __Block_object_assign
- __Block_object_dispose
- _objc_autorelease
CStrings:
+ "%@"
+ "%s no volume UUID in message; ignoring"
+ "+[NSUserNotification(TMAdditions) backupErrorNotificationWithCode:messageParameters:destinationID:supportURL:]"
+ "-[TMHelperAgent _handleCoreStorageDeprecationNotificationRequest:]"
+ ".cxx_destruct"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KIx4rG/Sources/backupd/HelperAgent/NSUserNotification+HelperAgent.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KIx4rG/Sources/backupd/HelperAgent/TMHelperAgent.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KIx4rG/Sources/backupd/TimeMachinePrivate-Framework/IPC/SettingsPaneMessenger.m"
+ "@40@0:8q16Q24@32"
+ "@48@0:8q16@24@32@40"
+ "Encrypted Mac OS Extended disks will not be compatible with macOS 28."
+ "SupportURL"
+ "Time Machine Settings…"
+ "URLWithString:"
+ "Visit Apple Support"
+ "Will deliver notification: %@ { identifier: '%@' }"
+ "_handleCoreStorageDeprecationNotificationRequest:"
+ "backupCompleteNotificationWithDestinationID:"
+ "backupErrorNotificationWithCode:messageParameters:destinationID:supportURL:"
+ "com.apple.TimeMachine.CoreStorageDeprecation"
+ "com.apple.TimeMachine.VisitAppleSupport"
+ "coreStorageDeprecationNotificationWithVolumeUUID:supportURL:"
+ "destinationForID:"
+ "diskForVolumeUUID:"
+ "displayName"
+ "drySpellNotificationWithCode:days:destinationID:"
+ "isCoreStorageDeprecation"
+ "localizedCaseInsensitiveContainsString:"
+ "localizedStringWithFormat:"
+ "openURL:"
+ "previous notification date: %@"
+ "sharedWorkspace"
+ "supportURL"
+ "userVisibleVolumeName"
+ "“%@” will not be compatible with macOS 28."
- "%@ { identifier: '%@' }"
- "+[NSUserNotification(TMAdditions) backupErrorNotificationWithCode:messageParameters:destinationID:]"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7CgWxt/Sources/backupd/HelperAgent/NSUserNotification+HelperAgent.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7CgWxt/Sources/backupd/HelperAgent/TMHelperAgent.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7CgWxt/Sources/backupd/TimeMachinePrivate-Framework/IPC/SettingsPaneMessenger.m"
- "@48@0:8q16Q24@32@40"
- "DestinationDisplayName"
- "backupCompleteNotificationWithDestinationName:destinationID:"
- "backupErrorNotificationWithCode:messageParameters:destinationID:"
- "drySpellNotificationWithCode:days:destinationName:destinationID:"

```
