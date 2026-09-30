## HomeKitBackingStore

> `/System/Library/PrivateFrameworks/HomeKitBackingStore.framework/HomeKitBackingStore`

```diff

-1241.4.11.0.0
-  __TEXT.__text: 0x88e14
-  __TEXT.__auth_stubs: 0x8a0
-  __TEXT.__objc_methlist: 0x4fd8
-  __TEXT.__const: 0xc8
-  __TEXT.__gcc_except_tab: 0x5260
-  __TEXT.__cstring: 0x738e
-  __TEXT.__oslogstring: 0xd16f
-  __TEXT.__unwind_info: 0x1e58
-  __TEXT.__objc_classname: 0xede
-  __TEXT.__objc_methname: 0xcf5c
-  __TEXT.__objc_methtype: 0x1949
-  __TEXT.__objc_stubs: 0x9980
-  __DATA_CONST.__got: 0x588
-  __DATA_CONST.__const: 0x27f0
+1278.5.8.2.0
+  __TEXT.__text: 0x88d08
+  __TEXT.__auth_stubs: 0x8b0
+  __TEXT.__objc_methlist: 0x54f4
+  __TEXT.__const: 0xd0
+  __TEXT.__gcc_except_tab: 0x5280
+  __TEXT.__cstring: 0x7382
+  __TEXT.__oslogstring: 0xd22e
+  __TEXT.__unwind_info: 0x1e50
+  __TEXT.__objc_classname: 0xeed
+  __TEXT.__objc_methname: 0xd0a2
+  __TEXT.__objc_methtype: 0x197d
+  __TEXT.__objc_stubs: 0x9aa0
+  __DATA_CONST.__got: 0x590
+  __DATA_CONST.__const: 0x29b8
   __DATA_CONST.__objc_classlist: 0x390
   __DATA_CONST.__objc_catlist: 0xc8
-  __DATA_CONST.__objc_protolist: 0xb0
+  __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2c30
+  __DATA_CONST.__objc_selrefs: 0x2cf8
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x2d0
-  __DATA_CONST.__objc_arraydata: 0xb0
-  __AUTH_CONST.__auth_got: 0x460
+  __DATA_CONST.__objc_arraydata: 0xd0
+  __AUTH_CONST.__auth_got: 0x468
   __AUTH_CONST.__const: 0x880
-  __AUTH_CONST.__cfstring: 0x46e0
-  __AUTH_CONST.__objc_const: 0xb588
-  __AUTH_CONST.__objc_intobj: 0x180
-  __AUTH_CONST.__objc_arrayobj: 0x48
+  __AUTH_CONST.__cfstring: 0x46a0
+  __AUTH_CONST.__objc_const: 0xadd0
+  __AUTH_CONST.__objc_intobj: 0x1e0
+  __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH.__objc_data: 0x640
-  __DATA.__objc_ivar: 0x5c8
-  __DATA.__data: 0xa18
-  __DATA.__bss: 0x90
+  __DATA.__objc_ivar: 0x5cc
+  __DATA.__data: 0x8b0
+  __DATA.__bss: 0xa0
   __DATA_DIRTY.__objc_data: 0x1d60
-  __DATA_DIRTY.__bss: 0x1d0
+  __DATA_DIRTY.__bss: 0x1c0
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation

   - /System/Library/PrivateFrameworks/ApplePushService.framework/ApplePushService
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /System/Library/PrivateFrameworks/HMFoundation.framework/HMFoundation
+  - /System/Library/PrivateFrameworks/MobileStoreDemoKit.framework/MobileStoreDemoKit
   - /System/Library/PrivateFrameworks/NetAppsUtilities.framework/NetAppsUtilities
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 2142
-  Symbols:   2653
-  CStrings:  4145
+  Functions: 2145
+  Symbols:   2660
+  CStrings:  4159
 
Symbols:
+ _OBJC_CLASS_$_HMFMemoryMonitor
+ _objc_retainAutoreleasedReturnValue
CStrings:
+ "%{public}@Clearing cache after receiving memory pressure notification"
+ "%{public}@[%{public}@] Aborting block %lu because there are no records to push"
+ "%{public}@[%{public}@] Failed to abort block %lu: %@"
+ "%{public}@[%{public}@] Lost localZone in __fetchChanges"
+ "%{public}@[%{public}@] Received and decoded record: %{public}@/%{public}@/%@/%{timespec}.*P"
+ "@\"HMFMemoryMonitor\""
+ "HMFMemoryObserver"
+ "T@\"HMFMemoryMonitor\",R,N,V_memoryMonitor"
+ "_clearPreparedStatementsCache"
+ "_configureMemoryPressureHandler"
+ "_memoryMonitor"
+ "addObserver:debounceInterval:events:"
+ "initWithString:"
+ "initWithURL:preparedStatementsCache:memoryMonitor:"
+ "memoryMonitor"
+ "memoryMonitor:didReceiveMemoryEvent:"
+ "redactedDescription"
+ "removeObserver:"
+ "substringToIndex:"
+ "timeIntervalSince1970"
+ "v32@0:8@\"HMFMemoryMonitor\"16q24"
- "\x12\x11"
- "%{public}@Lost localZone in __fetchChanges"
- "%{public}@[%{public}@] No valid records to push; aborting"
- "%{public}@[%{public}@] Received and decoded record: %@/%@"
- "1.0.0"
- "4.0.0"
- "initWithVersionString:"

```
