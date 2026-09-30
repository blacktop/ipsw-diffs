## CoreCaptureDaemon

> `/System/Library/PrivateFrameworks/CoreCaptureDaemon.framework/CoreCaptureDaemon`

```diff

-1301.74.0.0.0
-  __TEXT.__text: 0x4073c
+1301.79.0.0.0
+  __TEXT.__text: 0x41930
   __TEXT.__auth_stubs: 0x1160
   __TEXT.__const: 0x500
   __TEXT.__gcc_except_tab: 0x268
-  __TEXT.__oslogstring: 0x73c2
-  __TEXT.__cstring: 0x87e8
-  __TEXT.__unwind_info: 0x600
+  __TEXT.__oslogstring: 0x7566
+  __TEXT.__cstring: 0x8a81
+  __TEXT.__unwind_info: 0x608
   __TEXT.__objc_classname: 0x1
   __TEXT.__objc_methname: 0x107
   __TEXT.__objc_stubs: 0x180

   __DATA_CONST.__objc_selrefs: 0x60
   __AUTH_CONST.__auth_got: 0x8c0
   __AUTH_CONST.__const: 0x1088
-  __AUTH_CONST.__cfstring: 0xa00
+  __AUTH_CONST.__cfstring: 0xa40
   __DATA.__data: 0x1
   __DATA.__common: 0x3c
   __DATA.__bss: 0x132

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 3D338067-68C0-3F73-8626-8184A752F096
-  Functions: 500
-  Symbols:   1077
-  CStrings:  1335
+  UUID: 1F0011E8-AEDA-337C-8AB4-960F0F33814B
+  Functions: 503
+  Symbols:   1080
+  CStrings:  1357
 
Symbols:
+ GCC_except_table147
+ GCC_except_table203
+ GCC_except_table218
+ GCC_except_table266
+ GCC_except_table357
+ GCC_except_table368
+ GCC_except_table372
+ GCC_except_table373
+ GCC_except_table434
+ GCC_except_table498
+ __ZN16CCProfileMonitor17mergeProfilePlistEPKvS1_
+ __ZN16CCProfileMonitor29sendProfileChangeNotificationEi
+ __ZN8CCDaemon29sendProfileChangeNotificationEi
+ ___block_descriptor_40_e33_v16?0"NSObject<OS_xpc_object>"8l
+ ___block_descriptor_40_e5_v8?0l
+ ___block_descriptor_40_e8_v12?0i8l
+ ___block_descriptor_tmp.161
+ ___block_descriptor_tmp.1721
+ ___block_descriptor_tmp.1785
+ ___block_descriptor_tmp.1878
+ ___block_descriptor_tmp.2139
+ ___block_descriptor_tmp.22
+ ___block_descriptor_tmp.2258
+ ___block_descriptor_tmp.26.2056
+ ___block_descriptor_tmp.392
+ ___block_descriptor_tmp.54
+ ___block_descriptor_tmp.607
+ ___block_descriptor_tmp.63
+ ___block_descriptor_tmp.821
+ ___block_literal_global.1257
+ ___block_literal_global.1783
+ ___block_literal_global.2095
+ ___block_literal_global.815
- GCC_except_table146
- GCC_except_table202
- GCC_except_table217
- GCC_except_table265
- GCC_except_table355
- GCC_except_table364
- GCC_except_table365
- GCC_except_table369
- GCC_except_table431
- GCC_except_table495
- ___block_descriptor_tmp.11
- ___block_descriptor_tmp.1541
- ___block_descriptor_tmp.160
- ___block_descriptor_tmp.1692
- ___block_descriptor_tmp.1756
- ___block_descriptor_tmp.1849
- ___block_descriptor_tmp.20
- ___block_descriptor_tmp.2105
- ___block_descriptor_tmp.2224
- ___block_descriptor_tmp.24
- ___block_descriptor_tmp.37
- ___block_descriptor_tmp.391
- ___block_descriptor_tmp.53
- ___block_descriptor_tmp.605
- ___block_descriptor_tmp.62
- ___block_descriptor_tmp.816
- ___block_literal_global.1250
- ___block_literal_global.1754
- ___block_literal_global.2063
- ___block_literal_global.810
CStrings:
+ "%s:%06u memory alloc failed\n"
+ "%s:%06u unable to allocate dictionary\n"
+ "/private/var/tmp/com.apple.corecaptured/com.apple.bluetooth.logging.plist"
+ "CCConfigure::applyConfiguration Configuration type is not dictionary\n"
+ "CCDaemon::sendProfileChangeNotification profile change notification received\n"
+ "CCProfileMonitor::profileCallback changed. previous state: %d, current state: %d\n"
+ "CCProfileMonitor::profileCallback during shutdown (1)\n"
+ "CCProfileMonitor::profileCallback during shutdown (2)\n"
+ "CCProfileMonitor::profileCallback empty dictionary. fProfileLoaded %d fProfileRemoveApplied %d\n"
+ "CCProfileMonitor::profileCallback failed to get fMutex, exiting\n"
+ "CCProfileMonitor::profileCallback no profile installed. previous state: %d, current state: %d\n"
+ "CCProfileMonitor::profileCallback read BT profile plist valid: %d mask: %d\n"
+ "CCProfileMonitor::profileCallback read WiFi profile plist valid: %d mask: %d\n"
+ "CCProfileMonitor::profileCallback starting states -> isShutdownPending %d fProfileLoaded %d fProfileRemoveApplied %d\n"
+ "CCProfileMonitor::profileCallback unchanged mask. previous state: %d, current state: %d\n"
+ "CCProfileMonitor::sendProfileChangeNotification profile change notification received\n"
+ "Created a bad offset, don't save it! newOffset %u, payload length %u, padding %u,sizeof metadata %lu, STATE %c, entry:%u"
+ "Invalid State readOffset : %d, writeOffset : %d state %c, entry %u "
+ "ProfileLoaded"
+ "ProfileRemoved"
+ "file:///private/var/Managed%20Preferences/mobile/com.apple.corecapture.configure.bt.plist"
+ "mergeProfilePlist"
+ "previous and current sequence numbers are same %u prev read offset %u,new read offset %u, previous write offset %u, new write offset %u, entry %u\n"
+ "v16@?0@\"NSObject<OS_xpc_object>\"8"
- "CCConfigure::applyConfiguration Configuration type is not directory\n"
- "CCProfileMonitor::profileCallback during shutdown (1) CCDaemon::getInstance().isShutdownPending() == true \n"
- "CCProfileMonitor::profileCallback during shutdown (2) CCDaemon::getInstance().isShutdownPending() == true \n"
- "CCProfileMonitor::profileCallback fKeyCount=0 fProfileLoaded:%d Removed\n"
- "CCProfileMonitor::profileCallback fProfileLoaded is true, exiting\n"
- "CCProfileMonitor::profileCallback failed to get fMutex, exiting \n"
- "CCProfileMonitor::profileCallback setting removeProfile, exiting\n"
- "CCProfileMonitor::profileCallback starting states CCDaemon::getInstance().isShutdownPending() %d fProfileLoaded %d fProfileRemoveApplied %d\n"
- "CCProfileMonitor::profileCallback:%d removePending token:%d fProfileLoaded:%d fProfileRemoveApplied:%d, setting removeProfile, exiting\n"
- "Created a bad offset, don't save it! entry:%u"
- "previous and current sequence numbers are same %u prev read offset %u,new read ofsset %u, previous write offset %u, new write offset %u, entry %u\n"

```
