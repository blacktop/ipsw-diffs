## KnowledgeMonitor

> `/System/Library/PrivateFrameworks/KnowledgeMonitor.framework/KnowledgeMonitor`

```diff

-442.0.0.0.0
-  __TEXT.__text: 0x2cedc
-  __TEXT.__auth_stubs: 0xbd0
-  __TEXT.__objc_methlist: 0x2afc
+442.3.1.0.0
+  __TEXT.__text: 0x2dc78
+  __TEXT.__auth_stubs: 0xbe0
+  __TEXT.__objc_methlist: 0x2b54
   __TEXT.__const: 0x1a0
-  __TEXT.__gcc_except_tab: 0x620
-  __TEXT.__cstring: 0x3566
-  __TEXT.__oslogstring: 0x238d
+  __TEXT.__gcc_except_tab: 0x66c
+  __TEXT.__cstring: 0x3641
+  __TEXT.__oslogstring: 0x243e
   __TEXT.__dlopen_cstrs: 0x49
-  __TEXT.__unwind_info: 0xbbc
-  __TEXT.__objc_classname: 0x604
-  __TEXT.__objc_methname: 0x89e2
-  __TEXT.__objc_methtype: 0xd24
-  __TEXT.__objc_stubs: 0x6d00
+  __TEXT.__unwind_info: 0xbd8
+  __TEXT.__objc_classname: 0x607
+  __TEXT.__objc_methname: 0x8abc
+  __TEXT.__objc_methtype: 0xd4a
+  __TEXT.__objc_stubs: 0x6e20
   __DATA_CONST.__got: 0x188
-  __DATA_CONST.__const: 0x8f8
+  __DATA_CONST.__const: 0x920
   __DATA_CONST.__objc_classlist: 0x170
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x3bd0
-  __DATA_CONST.__objc_selrefs: 0x2150
+  __DATA_CONST.__objc_const: 0x3c50
+  __DATA_CONST.__objc_selrefs: 0x2198
   __DATA_CONST.__objc_arraydata: 0xe0
   __AUTH_CONST.__cfstring: 0x1ee0
-  __AUTH_CONST.__const: 0x380
+  __AUTH_CONST.__const: 0x3c0
   __AUTH_CONST.__objc_arrayobj: 0x198
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_const: 0x1a18
   __AUTH_CONST.__objc_intobj: 0x168
-  __AUTH_CONST.__auth_got: 0x5f8
+  __AUTH_CONST.__auth_got: 0x600
   __AUTH.__objc_data: 0x50
   __DATA.__objc_classrefs: 0x480
   __DATA.__objc_superrefs: 0x158
-  __DATA.__objc_ivar: 0x338
+  __DATA.__objc_ivar: 0x348
   __DATA.__data: 0x548
   __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0xe10
-  __DATA_DIRTY.__bss: 0xb0
+  __DATA_DIRTY.__bss: 0xc0
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1206
-  Symbols:   4480
-  CStrings:  2222
+  Functions: 1227
+  Symbols:   4542
+  CStrings:  2244
 
Symbols:
+ +[_DKNotificationKeybagLockMonitor getCurrentLockState].cold.1
+ +[_DKNotificationKeybagLockMonitor log]
+ -[_DKMonitor _instantMonitorNeedsActivation]
+ -[_DKMonitor _instantMonitorNeedsDeactivation]
+ -[_DKNotificationKeybagLockMonitor _activate]
+ -[_DKNotificationKeybagLockMonitor _deactivate]
+ -[_DKNotificationKeybagLockMonitor _enqueueKeybagLockedUpdate:timestamp:]
+ -[_DKNotificationKeybagLockMonitor _receiveNotificationEvent:]
+ -[_DKNotificationKeybagLockMonitor _receiveNotificationEvent:].cold.1
+ -[_DKNotificationKeybagLockMonitor _resume]
+ -[_DKNotificationKeybagLockMonitor _updateWithKeybagLocked:timestamp:]
+ GCC_except_table36
+ _MKBDeviceUnlockedSinceBoot
+ _OBJC_IVAR_$__DKNotificationKeybagLockMonitor._activated
+ _OBJC_IVAR_$__DKNotificationKeybagLockMonitor._donationQueue
+ _OBJC_IVAR_$__DKNotificationKeybagLockMonitor._donationQueueResumed
+ _OBJC_IVAR_$__DKNotificationKeybagLockMonitor._lastEvent
+ _OBJC_IVAR_$__DKNotificationKeybagLockMonitor._lastUpdate
+ ___39+[_DKNotificationKeybagLockMonitor log]_block_invoke
+ ___40-[_DKNotificationKeybagLockMonitor stop]_block_invoke
+ ___41-[_DKNotificationKeybagLockMonitor start]_block_invoke
+ ___45-[_DKNotificationKeybagLockMonitor _activate]_block_invoke
+ ___45-[_DKNotificationKeybagLockMonitor _activate]_block_invoke.20
+ ___45-[_DKNotificationKeybagLockMonitor _activate]_block_invoke_2
+ ___47-[_DKNotificationKeybagLockMonitor _deactivate]_block_invoke
+ ___61-[_DKNotificationKeybagLockMonitor receiveNotificationEvent:]_block_invoke
+ ___61-[_DKNotificationKeybagLockMonitor receiveNotificationEvent:]_block_invoke_2
+ ___73-[_DKNotificationKeybagLockMonitor _enqueueKeybagLockedUpdate:timestamp:]_block_invoke
+ ___block_descriptor_56_e8_32s40r48r_e22_v16?0"BMStoreEvent"8lr40l8r48l8s32l8
+ ___block_literal_global.155
+ ___block_literal_global.157
+ ___block_literal_global.23
+ _objc_msgSend$_activate
+ _objc_msgSend$_deactivate
+ _objc_msgSend$_enqueueKeybagLockedUpdate:timestamp:
+ _objc_msgSend$_instantMonitorNeedsActivation
+ _objc_msgSend$_instantMonitorNeedsDeactivation
+ _objc_msgSend$_receiveNotificationEvent:
+ _objc_msgSend$_resume
+ _objc_msgSend$_updateWithKeybagLocked:timestamp:
+ _objc_msgSend$initWithBundleID:isInstall:
+ _objc_msgSend$starting
- -[_DKNotificationKeybagLockMonitor deactivate]
- -[_DKNotificationKeybagLockMonitor dealloc]
- -[_DKNotificationKeybagLockMonitor receiveNotificationEvent:].cold.1
- GCC_except_table34
- _OBJC_IVAR_$__DKNotificationKeybagLockMonitor._enabled
- ___block_literal_global.170
- ___block_literal_global.172
- _objc_msgSend$initWithBundleID:title:category:subCategories:isInstall:
CStrings:
+ "\x11\x12"
+ "/Library/Caches/com.apple.xbs/Sources/DuetKnowledgeCollector/KnowledgeMonitor/KnowledgeMonitor/Monitors/_DKAppInstallMonitor.m:225"
+ "/Library/Caches/com.apple.xbs/Sources/DuetKnowledgeCollector/KnowledgeMonitor/KnowledgeMonitor/Monitors/_DKNotificationKeybagLockMonitor.m:276"
+ "/Library/Caches/com.apple.xbs/Sources/DuetKnowledgeCollector/KnowledgeMonitor/KnowledgeMonitor/Monitors/_DKNotificationMonitor.m:425"
+ "/Library/Caches/com.apple.xbs/Sources/DuetKnowledgeCollector/KnowledgeMonitor/KnowledgeMonitor/_DKMonitor.m:309"
+ "@\"BMDeviceKeybagLocked\""
+ "Checking current state of Device.KeybagLocked stream"
+ "Loaded last Device.KeybagLocked event %{public}@ at %f"
+ "Unexpected lock state %d"
+ "Writing keybagLocked event %{public}@ at %f"
+ "_DKNotificationKeybagLockMonitor.donations"
+ "_activate"
+ "_activated"
+ "_deactivate"
+ "_donationQueueResumed"
+ "_enqueueKeybagLockedUpdate:timestamp:"
+ "_instantMonitorNeedsActivation"
+ "_instantMonitorNeedsDeactivation"
+ "_lastEvent"
+ "_receiveNotificationEvent:"
+ "_resume"
+ "_updateWithKeybagLocked:timestamp:"
+ "initWithBundleID:isInstall:"
+ "starting"
+ "v28@0:8i16d20"
- "/Library/Caches/com.apple.xbs/Sources/DuetKnowledgeCollector/KnowledgeMonitor/KnowledgeMonitor/Monitors/_DKAppInstallMonitor.m:228"
- "/Library/Caches/com.apple.xbs/Sources/DuetKnowledgeCollector/KnowledgeMonitor/KnowledgeMonitor/Monitors/_DKNotificationMonitor.m:570"
- "/Library/Caches/com.apple.xbs/Sources/DuetKnowledgeCollector/KnowledgeMonitor/KnowledgeMonitor/_DKMonitor.m:293"
- "initWithBundleID:title:category:subCategories:isInstall:"

```
